/*:
 * @target MZ
 * @plugindesc v0.2.0 Data-driven NPC schedule loader and runtime map event positioning.
 * @author Chroma's Edge
 * @help
 * Loads NPC schedules from assets/data/npcs and applies day/night/rain coordinates
 * to map events tagged with:
 *   <chromaAmbientNpc:NPC_ID>
 *   <chromaNpcId:NPC_ID>
 *
 * Script calls:
 *   ChromaEdge.NpcScheduling.reload()
 *   ChromaEdge.NpcScheduling.applyCurrentMap()
 *   ChromaEdge.NpcScheduling.getNpc("NPC_SISTER_AMARA")
 *
 * @param loadOnBoot
 * @text Load On Boot
 * @type boolean
 * @default true
 *
 * @param enabledByDefault
 * @text Enabled By Default
 * @type boolean
 * @default true
 *
 * @param autoApplyOnMapLoad
 * @text Auto Apply On Map Load
 * @type boolean
 * @default true
 *
 * @param autoApplyOnTimeTick
 * @text Auto Apply On Time Tick
 * @type boolean
 * @default true
 *
 * @param autoUseRainSlot
 * @text Auto Use Rain Slot
 * @type boolean
 * @default true
 *
 * @param requireLocationMatch
 * @text Require NPC Location Match
 * @type boolean
 * @default true
 *
 * @command ReloadNpcSchedules
 * @text Reload NPC Schedules
 * @arg switchId
 * @text Success Switch
 * @type switch
 * @default 0
 * @arg variableId
 * @text NPC Count Variable
 * @type variable
 * @default 0
 *
 * @command ApplyCurrentMapSchedules
 * @text Apply Current Map Schedules
 *
 * @command SetSchedulingEnabled
 * @text Set Scheduling Enabled
 * @arg value
 * @type boolean
 * @default true
 *
 * @command MoveEventToNpc
 * @text Move Event To NPC Slot
 * @arg eventId
 * @type number
 * @default 1
 * @arg npcId
 * @type string
 * @default NPC_SISTER_AMARA
 * @arg slot
 * @type select
 * @option Auto
 * @value auto
 * @option Day
 * @value day
 * @option Night
 * @value night
 * @option Rain
 * @value rain
 * @default auto
 *
 * @command GetNpcCoordinates
 * @text Get NPC Coordinates
 * @arg npcId
 * @type string
 * @default NPC_SISTER_AMARA
 * @arg slot
 * @type select
 * @option Auto
 * @value auto
 * @option Day
 * @value day
 * @option Night
 * @value night
 * @option Rain
 * @value rain
 * @default auto
 * @arg variableIdX
 * @type variable
 * @default 0
 * @arg variableIdY
 * @type variable
 * @default 0
 */

(() => {
  "use strict";

  const pluginName = "ChromaEdge_NPCScheduling";
  const params = PluginManager.parameters(pluginName);
  const loadOnBoot = String(params.loadOnBoot || "true").toLowerCase() === "true";
  const enabledByDefault =
    String(params.enabledByDefault || "true").toLowerCase() === "true";
  const autoApplyOnMapLoad =
    String(params.autoApplyOnMapLoad || "true").toLowerCase() === "true";
  const autoApplyOnTimeTick =
    String(params.autoApplyOnTimeTick || "true").toLowerCase() === "true";
  const autoUseRainSlot =
    String(params.autoUseRainSlot || "true").toLowerCase() === "true";
  const requireLocationMatch =
    String(params.requireLocationMatch || "true").toLowerCase() === "true";

  const NPC_DIRECTORY = "assets/data/npcs";
  const MAP_DIRECTORY = "assets/data/maps";

  const toInt = (value, fallback = 0) => {
    const parsed = Number(value);
    return Number.isFinite(parsed) ? Math.floor(parsed) : fallback;
  };

  const toBool = (value) =>
    String(value === undefined ? "" : value).toLowerCase() === "true";

  const deepClone = (value) => JSON.parse(JSON.stringify(value));

  const stripBom = (text) =>
    text && text.charCodeAt(0) === 0xfeff ? text.slice(1) : text;

  const setSwitch = (switchId, value) => {
    const id = toInt(switchId, 0);
    if (id > 0 && $gameSwitches) $gameSwitches.setValue(id, !!value);
  };

  const setVariable = (variableId, value) => {
    const id = toInt(variableId, 0);
    if (id > 0 && $gameVariables) $gameVariables.setValue(id, value);
  };

  const parseTag = (note, tagName) => {
    const m = String(note || "").match(
      new RegExp(`<\\s*${tagName}\\s*:\\s*([^>]+)\\s*>`, "i")
    );
    return m && m[1] ? String(m[1]).trim() : "";
  };

  const normalizeCoords = (coords) => {
    if (!Array.isArray(coords) || coords.length < 2) return null;
    const x = Number(coords[0]);
    const y = Number(coords[1]);
    if (!Number.isFinite(x) || !Number.isFinite(y)) return null;
    return [x, y];
  };

  const loadJsonSync = (relativePath) => {
    if (typeof require === "function" && Utils && Utils.isNwjs()) {
      const fs = require("fs");
      const path = require("path");
      const root = path.dirname(process.mainModule.filename);
      const fullPath = path.join(root, relativePath);
      if (!fs.existsSync(fullPath)) {
        throw new Error(`Missing file: ${relativePath}`);
      }
      return JSON.parse(stripBom(fs.readFileSync(fullPath, "utf8")));
    }

    const xhr = new XMLHttpRequest();
    xhr.open("GET", relativePath, false);
    xhr.overrideMimeType("application/json");
    xhr.send();
    if (xhr.status >= 400) {
      throw new Error(`HTTP ${xhr.status}: ${relativePath}`);
    }
    return JSON.parse(stripBom(xhr.responseText));
  };

  const buildNpcRuntime = () => {
    const npcById = {};
    const canonicalDimensions = {};
    const warnings = [];
    const errors = [];

    if (typeof require === "function" && Utils && Utils.isNwjs()) {
      const fs = require("fs");
      const path = require("path");
      const root = path.dirname(process.mainModule.filename);

      const npcDir = path.join(root, NPC_DIRECTORY);
      if (fs.existsSync(npcDir)) {
        const npcFiles = fs
          .readdirSync(npcDir)
          .filter((f) => f.toLowerCase().endsWith(".json"))
          .sort();

        for (const file of npcFiles) {
          try {
            const raw = fs.readFileSync(path.join(npcDir, file), "utf8");
            const data = JSON.parse(stripBom(raw));
            const npcId = String(data.id || "").trim();
            if (!npcId) continue;
            npcById[npcId] = {
              id: npcId,
              name: String(data.name || npcId),
              location: String(data.location || "").trim(),
              schedule: {
                day: normalizeCoords(data.schedule && data.schedule.day),
                night: normalizeCoords(data.schedule && data.schedule.night),
                rain: normalizeCoords(data.schedule && data.schedule.rain),
              },
              coords: normalizeCoords(data.coords),
              flags: data.flags && typeof data.flags === "object" ? data.flags : {},
              dialogTree: String(data.dialog_tree || "").trim(),
            };
          } catch (err) {
            warnings.push(`${file}: ${err.message || String(err)}`);
          }
        }
      }

      const mapDir = path.join(root, MAP_DIRECTORY);
      if (fs.existsSync(mapDir)) {
        const mapFiles = fs
          .readdirSync(mapDir)
          .filter((f) => f.toLowerCase().endsWith(".json"))
          .sort();

        for (const file of mapFiles) {
          try {
            const raw = fs.readFileSync(path.join(mapDir, file), "utf8");
            const data = JSON.parse(stripBom(raw));

            if (data && typeof data === "object" && data.id && data.dimensions) {
              const w = toInt(data.dimensions.width, 0);
              const h = toInt(data.dimensions.height, 0);
              if (w > 0 && h > 0) {
                canonicalDimensions[String(data.id).trim()] = { width: w, height: h };
              }
            }

            const maps = Array.isArray(data && data.maps) ? data.maps : [];
            for (const mapEntry of maps) {
              if (!mapEntry || typeof mapEntry !== "object") continue;
              const cid = String(mapEntry.id || "").trim();
              const dim = mapEntry.dimensions;
              if (!cid || !dim || typeof dim !== "object") continue;
              const w = toInt(dim.width, 0);
              const h = toInt(dim.height, 0);
              if (w > 0 && h > 0) {
                canonicalDimensions[cid] = { width: w, height: h };
              }
            }
          } catch (err) {
            warnings.push(`${file}: ${err.message || String(err)}`);
          }
        }
      }
    } else {
      // Browser fallback: use ambient runtime index.
      try {
        const idx = loadJsonSync("assets/data/npcs/npc_ambient_runtime_index.json");
        const byTown = Array.isArray(idx.by_town) ? idx.by_town : [];
        for (const town of byTown) {
          const townId = String(town.town_id || "").trim();
          for (const npc of Array.isArray(town.npcs) ? town.npcs : []) {
            if (!npc || typeof npc !== "object") continue;
            const npcId = String(npc.npc || "").trim();
            if (!npcId) continue;
            npcById[npcId] = {
              id: npcId,
              name: String(npc.name || npcId),
              location: townId,
              schedule: {
                day: normalizeCoords(npc.day),
                night: normalizeCoords(npc.night),
                rain: normalizeCoords(npc.rain),
              },
              coords: normalizeCoords(npc.day) || normalizeCoords(npc.night),
              flags: {},
              dialogTree: String(npc.dialog_tree || "").trim(),
            };
          }
        }
      } catch (err) {
        errors.push(`Fallback ambient runtime index: ${err.message || String(err)}`);
      }
    }

    const npcIds = Object.keys(npcById).sort();
    return {
      ready: npcIds.length > 0,
      npcById,
      npcIds,
      canonicalDimensions,
      warnings,
      errors,
    };
  };

  let runtime = {
    ready: false,
    npcById: {},
    npcIds: [],
    canonicalDimensions: {},
    warnings: [],
    errors: [],
  };

  const reloadRuntime = () => {
    runtime = buildNpcRuntime();
    if (runtime.warnings.length) {
      console.warn(`[${pluginName}] NPC schedule warnings:`);
      for (const line of runtime.warnings) {
        console.warn(`[${pluginName}] ${line}`);
      }
    }
    if (runtime.errors.length) {
      console.error(`[${pluginName}] NPC schedule errors:`);
      for (const line of runtime.errors) {
        console.error(`[${pluginName}] ${line}`);
      }
    }
    return runtime.ready;
  };

  const dayNightApi = () => {
    const g = typeof window !== "undefined" ? window : globalThis;
    return g && g.ChromaEdge ? g.ChromaEdge.DayNight : null;
  };

  const questApi = () => {
    const g = typeof window !== "undefined" ? window : globalThis;
    return g && g.ChromaEdge ? g.ChromaEdge.Quests : null;
  };

  const currentCanonicalMapId = () => {
    if (!$dataMap || typeof $dataMap.note !== "string") return "";
    return parseTag($dataMap.note, "chromaMapId");
  };

  const currentScheduleSlot = (npc) => {
    if (autoUseRainSlot && $gameScreen && typeof $gameScreen.weatherType === "function") {
      const weather = String($gameScreen.weatherType() || "none");
      if (weather !== "none" && npc && npc.schedule && npc.schedule.rain) {
        return "rain";
      }
    }

    const dn = dayNightApi();
    if (dn && typeof dn.isNight === "function" && dn.isNight()) {
      return "night";
    }

    return "day";
  };

  const conditionFlagSet = (token) => {
    const key = String(token || "").trim();
    if (!key) return false;

    const q = questApi();
    if (q) {
      if (typeof q.isComplete === "function" && q.isComplete(key)) return true;
      if (typeof q.flag === "function" && q.flag(key)) return true;
    }

    if ($gameSystem && $gameSystem.chromaDialogueFlag && $gameSystem.chromaDialogueFlag(key)) {
      return true;
    }

    if ($dataSystem && Array.isArray($dataSystem.switches) && $gameSwitches) {
      for (let i = 1; i < $dataSystem.switches.length; i += 1) {
        if (String($dataSystem.switches[i] || "") === key) {
          return !!$gameSwitches.value(i);
        }
      }
    }

    return false;
  };

  const npcVisible = (npc) => {
    if (!npc || typeof npc !== "object") return false;
    const flags = npc.flags && typeof npc.flags === "object" ? npc.flags : {};

    const unlockBy = String(flags.unlocked_by || "").trim();
    if (unlockBy && !conditionFlagSet(unlockBy)) return false;

    const disappearsOn = String(flags.disappears_on || "").trim();
    if (disappearsOn && conditionFlagSet(disappearsOn)) return false;

    return true;
  };

  const projectCoordsToCurrentMap = (x, y, canonicalMapId) => {
    const mapW = $dataMap ? toInt($dataMap.width, 0) : 0;
    const mapH = $dataMap ? toInt($dataMap.height, 0) : 0;
    if (mapW <= 0 || mapH <= 0) return null;

    let projectedX = Number(x);
    let projectedY = Number(y);

    const dim = runtime.canonicalDimensions[canonicalMapId];
    if (dim && dim.width > 0 && dim.height > 0) {
      const scaleX = dim.width / mapW;
      const scaleY = dim.height / mapH;

      if (projectedX > mapW - 1 || projectedY > mapH - 1) {
        projectedX = projectedX / Math.max(1, scaleX);
        projectedY = projectedY / Math.max(1, scaleY);
      }
    }

    const clampedX = Math.max(0, Math.min(mapW - 1, Math.round(projectedX)));
    const clampedY = Math.max(0, Math.min(mapH - 1, Math.round(projectedY)));
    return { x: clampedX, y: clampedY };
  };

  const slotCoords = (npc, slot) => {
    if (!npc || !npc.schedule) return null;
    const chosen = slot === "auto" || !slot ? currentScheduleSlot(npc) : slot;
    const source =
      normalizeCoords(npc.schedule[chosen]) ||
      normalizeCoords(npc.schedule.day) ||
      normalizeCoords(npc.schedule.night) ||
      normalizeCoords(npc.schedule.rain) ||
      normalizeCoords(npc.coords);
    if (!source) return null;
    return { slot: chosen, x: source[0], y: source[1] };
  };

  const applyEventVisibility = (event, visible) => {
    if (!event) return;

    if (!visible) {
      if (!event._chromaSchedThroughRecorded) {
        event._chromaSchedThroughRecorded = true;
        event._chromaSchedOriginalThrough = event.isThrough();
      }
      event.setTransparent(true);
      event.setThrough(true);
      return;
    }

    event.setTransparent(false);
    if (event._chromaSchedThroughRecorded) {
      event.setThrough(!!event._chromaSchedOriginalThrough);
    }
  };

  const taggedNpcIdForEvent = (event) => {
    if (!event || !event.event) return "";
    const ev = event.event();
    if (!ev) return "";
    const note = ev.note || "";
    return parseTag(note, "chromaAmbientNpc") || parseTag(note, "chromaNpcId");
  };

  const applyNpcToEvent = (event, npcId, slot = "auto") => {
    const npc = runtime.npcById[String(npcId || "").trim()] || null;
    if (!event || !npc) return false;

    const canonicalMapId = currentCanonicalMapId();
    if (requireLocationMatch && npc.location && canonicalMapId && npc.location !== canonicalMapId) {
      applyEventVisibility(event, false);
      return true;
    }

    const visible = npcVisible(npc);
    if (!visible) {
      applyEventVisibility(event, false);
      return true;
    }

    const coords = slotCoords(npc, slot);
    if (!coords) {
      applyEventVisibility(event, false);
      return true;
    }

    const projected = projectCoordsToCurrentMap(coords.x, coords.y, canonicalMapId);
    if (!projected) return false;

    if (event.x !== projected.x || event.y !== projected.y) {
      event.locate(projected.x, projected.y);
    }
    applyEventVisibility(event, true);
    return true;
  };

  const applyCurrentMapSchedules = () => {
    if (!runtime.ready || !$gameMap || !$gameSystem || !$gameSystem.chromaNpcSchedulingEnabled()) {
      return 0;
    }

    const events = $gameMap.events();
    let touched = 0;
    for (const event of events) {
      const npcId = taggedNpcIdForEvent(event);
      if (!npcId) continue;
      if (applyNpcToEvent(event, npcId, "auto")) {
        touched += 1;
      }
    }
    return touched;
  };

  Game_System.prototype.chromaInitNpcSchedulingData = function() {
    if (this._chromaNpcSchedulingEnabled === undefined) {
      this._chromaNpcSchedulingEnabled = enabledByDefault;
    }
    if (this._chromaNpcSchedulingLastTick === undefined) {
      this._chromaNpcSchedulingLastTick = -1;
    }
  };

  Game_System.prototype.chromaNpcSchedulingEnabled = function() {
    this.chromaInitNpcSchedulingData();
    return !!this._chromaNpcSchedulingEnabled;
  };

  Game_System.prototype.chromaSetNpcSchedulingEnabled = function(value) {
    this.chromaInitNpcSchedulingData();
    this._chromaNpcSchedulingEnabled = !!value;
    return this._chromaNpcSchedulingEnabled;
  };

  Game_System.prototype.chromaNpcSchedulingLastTick = function() {
    this.chromaInitNpcSchedulingData();
    return this._chromaNpcSchedulingLastTick;
  };

  Game_System.prototype.chromaSetNpcSchedulingLastTick = function(value) {
    this.chromaInitNpcSchedulingData();
    this._chromaNpcSchedulingLastTick = toInt(value, -1);
  };

  const _Game_System_initialize = Game_System.prototype.initialize;
  Game_System.prototype.initialize = function() {
    _Game_System_initialize.call(this);
    this.chromaInitNpcSchedulingData();
  };

  const _DataManager_extractSaveContents = DataManager.extractSaveContents;
  DataManager.extractSaveContents = function(contents) {
    _DataManager_extractSaveContents.call(this, contents);
    if ($gameSystem && $gameSystem.chromaInitNpcSchedulingData) {
      $gameSystem.chromaInitNpcSchedulingData();
    }
  };

  const _Scene_Map_onMapLoaded = Scene_Map.prototype.onMapLoaded;
  Scene_Map.prototype.onMapLoaded = function() {
    _Scene_Map_onMapLoaded.call(this);
    if (autoApplyOnMapLoad) {
      applyCurrentMapSchedules();
    }
  };

  const _Scene_Map_update = Scene_Map.prototype.update;
  Scene_Map.prototype.update = function() {
    _Scene_Map_update.call(this);

    if (!autoApplyOnTimeTick) return;
    if (!$gameSystem || !$gameSystem.chromaNpcSchedulingEnabled()) return;

    const g = typeof window !== "undefined" ? window : globalThis;
    const dn = g && g.ChromaEdge ? g.ChromaEdge.DayNight : null;
    if (!dn || typeof dn.tick !== "function") return;

    const tick = toInt(dn.tick(), 0);
    if (tick <= $gameSystem.chromaNpcSchedulingLastTick()) return;

    $gameSystem.chromaSetNpcSchedulingLastTick(tick);
    applyCurrentMapSchedules();
  };

  PluginManager.registerCommand(pluginName, "ReloadNpcSchedules", (args) => {
    const ok = reloadRuntime();
    setSwitch(args.switchId, ok);
    setVariable(args.variableId, runtime.npcIds.length);
  });

  PluginManager.registerCommand(pluginName, "ApplyCurrentMapSchedules", () => {
    applyCurrentMapSchedules();
  });

  PluginManager.registerCommand(pluginName, "SetSchedulingEnabled", (args) => {
    $gameSystem.chromaSetNpcSchedulingEnabled(toBool(args.value));
    if ($gameSystem.chromaNpcSchedulingEnabled()) {
      applyCurrentMapSchedules();
    }
  });

  PluginManager.registerCommand(pluginName, "MoveEventToNpc", (args) => {
    const eventId = toInt(args.eventId, 0);
    const event = $gameMap ? $gameMap.event(eventId) : null;
    if (!event) return;
    applyNpcToEvent(event, args.npcId, String(args.slot || "auto"));
  });

  PluginManager.registerCommand(pluginName, "GetNpcCoordinates", (args) => {
    const npcId = String(args.npcId || "").trim();
    const npc = runtime.npcById[npcId] || null;
    if (!npc) {
      setVariable(args.variableIdX, 0);
      setVariable(args.variableIdY, 0);
      return;
    }

    const coords = slotCoords(npc, String(args.slot || "auto"));
    if (!coords) {
      setVariable(args.variableIdX, 0);
      setVariable(args.variableIdY, 0);
      return;
    }

    setVariable(args.variableIdX, Math.round(coords.x));
    setVariable(args.variableIdY, Math.round(coords.y));
  });

  const g = typeof window !== "undefined" ? window : globalThis;
  g.Imported = g.Imported || {};
  g.Imported.ChromaEdge_NPCScheduling = true;
  g.ChromaEdge = g.ChromaEdge || {};

  g.ChromaEdge.NpcScheduling = {
    ready() {
      return runtime.ready;
    },
    reload() {
      return reloadRuntime();
    },
    npcIds() {
      return runtime.npcIds.slice();
    },
    getNpc(npcId) {
      const id = String(npcId || "").trim();
      const npc = id ? runtime.npcById[id] : null;
      return npc ? deepClone(npc) : null;
    },
    enabled() {
      return $gameSystem ? $gameSystem.chromaNpcSchedulingEnabled() : false;
    },
    setEnabled(value) {
      return $gameSystem ? $gameSystem.chromaSetNpcSchedulingEnabled(!!value) : false;
    },
    currentMapId() {
      return currentCanonicalMapId();
    },
    currentSlot(npcId = "") {
      const npc = runtime.npcById[String(npcId || "").trim()] || null;
      return currentScheduleSlot(npc);
    },
    coordinates(npcId, slot = "auto") {
      const npc = runtime.npcById[String(npcId || "").trim()] || null;
      const coords = slotCoords(npc, slot);
      return coords ? { slot: coords.slot, x: coords.x, y: coords.y } : null;
    },
    applyCurrentMap() {
      return applyCurrentMapSchedules();
    },
    applyEvent(eventId, npcId, slot = "auto") {
      if (!$gameMap) return false;
      const event = $gameMap.event(toInt(eventId, 0));
      if (!event) return false;
      return applyNpcToEvent(event, npcId, slot);
    },
  };

  if (loadOnBoot) {
    reloadRuntime();
  }
})();
