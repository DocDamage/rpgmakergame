/*:
 * @target MZ
 * @plugindesc v0.1.0 Map HUD tracker for current quest objective.
 * @author Chroma's Edge
 * @help
 * Displays an on-map quest tracker window using ChromaEdge_QuestSystem data.
 *
 * Script calls:
 *   ChromaEdge.QuestTracker.show()
 *   ChromaEdge.QuestTracker.hide()
 *   ChromaEdge.QuestTracker.toggle()
 *   ChromaEdge.QuestTracker.refresh()
 *
 * @param enabledByDefault
 * @text Enabled By Default
 * @type boolean
 * @default true
 *
 * @param x
 * @text X
 * @type number
 * @default 0
 *
 * @param y
 * @text Y
 * @type number
 * @default 42
 *
 * @param width
 * @text Width
 * @type number
 * @default 430
 *
 * @param lineCount
 * @text Line Count
 * @type number
 * @min 2
 * @max 4
 * @default 2
 *
 * @param opacity
 * @text Window Opacity
 * @type number
 * @min 0
 * @max 255
 * @default 192
 *
 * @param showAvailableWhenNoActive
 * @text Show Available If No Active
 * @type boolean
 * @default true
 *
 * @param hideDuringMessage
 * @text Hide During Message
 * @type boolean
 * @default true
 *
 * @param showTargetMarker
 * @text Show Target Marker
 * @type boolean
 * @default true
 *
 * @param markerEnabledByDefault
 * @text Marker Enabled By Default
 * @type boolean
 * @default true
 *
 * @param markerYOffset
 * @text Marker Y Offset
 * @type number
 * @default 52
 *
 * @command SetQuestHudVisible
 * @text Set HUD Visible
 * @arg value
 * @type boolean
 * @default true
 *
 * @command ToggleQuestHud
 * @text Toggle HUD
 *
 * @command RefreshQuestHud
 * @text Refresh HUD
 *
 * @command SetQuestMarkerVisible
 * @text Set Marker Visible
 * @arg value
 * @type boolean
 * @default true
 *
 * @command ToggleQuestMarker
 * @text Toggle Marker
 */

(() => {
  "use strict";

  const pluginName = "ChromaEdge_QuestTrackerHUD";
  const params = PluginManager.parameters(pluginName);
  const enabledByDefault =
    String(params.enabledByDefault || "true").toLowerCase() === "true";
  const hudX = Number(params.x || 0);
  const hudY = Number(params.y || 42);
  const hudWidth = Number(params.width || 430);
  const hudLineCount = Math.max(2, Math.min(4, Number(params.lineCount || 2)));
  const hudOpacity = Math.max(0, Math.min(255, Number(params.opacity || 192)));
  const showAvailableWhenNoActive =
    String(params.showAvailableWhenNoActive || "true").toLowerCase() === "true";
  const hideDuringMessage =
    String(params.hideDuringMessage || "true").toLowerCase() === "true";
  const showTargetMarker =
    String(params.showTargetMarker || "true").toLowerCase() === "true";
  const markerEnabledByDefault =
    String(params.markerEnabledByDefault || "true").toLowerCase() === "true";
  const markerYOffset = Number(params.markerYOffset || 52);

  const toBool = (value) =>
    String(value === undefined ? "" : value).toLowerCase() === "true";

  const questApi = () => {
    const g = typeof window !== "undefined" ? window : globalThis;
    return g && g.ChromaEdge ? g.ChromaEdge.Quests : null;
  };

  const hasQuestRuntime = () => {
    const api = questApi();
    return !!(api && typeof api.ready === "function" && api.ready());
  };

  const currentCanonicalMapId = () => {
    if (!$dataMap || typeof $dataMap.note !== "string") return "";
    const note = $dataMap.note;
    const m = note.match(/<\s*(?:chromaMapId|questMapId)\s*:\s*([A-Za-z0-9_:-]+)\s*>/i);
    return m ? String(m[1]).trim() : "";
  };

  const normalizeStatusLabel = (status, available) => {
    if (status === "active") return "ACTIVE";
    if (status === "completed") return "COMPLETED";
    if (status === "failed") return "FAILED";
    if (status === "locked" && available) return "AVAILABLE";
    return "LOCKED";
  };

  const statusColor = (status, available) => {
    if (status === "active") return ColorManager.systemColor();
    if (status === "completed") return ColorManager.powerUpColor();
    if (status === "failed") return ColorManager.deathColor();
    if (status === "locked" && available) return ColorManager.textColor(14);
    return ColorManager.normalColor();
  };

  const questSteps = (quest) =>
    quest && Array.isArray(quest.steps)
      ? quest.steps.filter((s) => s && typeof s === "object")
      : [];

  const stepAt = (steps, index) => {
    const step = steps[index];
    if (!step) return null;
    const stepId = Number.isFinite(Number(step.id)) ? Number(step.id) : index + 1;
    return { step, stepId, index, total: steps.length };
  };

  const findStepInfo = (summary, quest) => {
    const steps = questSteps(quest);
    if (!steps.length) return null;

    const targetStep = Number(summary ? summary.stepId : 0);
    if (Number.isFinite(targetStep) && targetStep > 0) {
      const idx = steps.findIndex((s, i) => {
        const sid = Number.isFinite(Number(s.id)) ? Number(s.id) : i + 1;
        return sid === targetStep;
      });
      if (idx >= 0) return stepAt(steps, idx);
    }

    if (summary && summary.status === "completed") {
      return stepAt(steps, steps.length - 1);
    }
    return stepAt(steps, 0);
  };

  const getTrackedStepContext = () => {
    const entry = getTrackedEntry();
    if (!entry) return null;
    const api = questApi();
    const quest = api && typeof api.get === "function" ? api.get(entry.id) : null;
    const stepInfo = findStepInfo(entry.summary, quest);
    return {
      entry,
      quest,
      stepInfo,
      step: stepInfo ? stepInfo.step : null,
    };
  };

  const getTrackedEntry = () => {
    const api = questApi();
    if (!api || typeof api.ids !== "function" || typeof api.getSummary !== "function") {
      return null;
    }
    const ids = api.ids();
    if (!Array.isArray(ids) || ids.length === 0) return null;

    let activeEntry = null;
    let availableEntry = null;
    for (const questId of ids) {
      const summary = api.getSummary(questId);
      if (!summary) continue;
      const status = summary.status || "locked";
      const available =
        status === "locked" && typeof api.isAvailable === "function"
          ? !!api.isAvailable(questId)
          : false;
      const entry = { id: questId, summary, status, available };
      if (!activeEntry && status === "active") {
        activeEntry = entry;
      }
      if (!availableEntry && status === "locked" && available) {
        availableEntry = entry;
      }
      if (activeEntry && availableEntry) break;
    }

    if (activeEntry) return activeEntry;
    if (showAvailableWhenNoActive && availableEntry) return availableEntry;
    return null;
  };

  Game_System.prototype.chromaEnsureQuestHudData = function() {
    if (this._chromaQuestHudVisible === undefined) {
      this._chromaQuestHudVisible = enabledByDefault;
    }
    if (this._chromaQuestMarkerVisible === undefined) {
      this._chromaQuestMarkerVisible = markerEnabledByDefault;
    }
  };

  Game_System.prototype.chromaQuestHudVisible = function() {
    this.chromaEnsureQuestHudData();
    return !!this._chromaQuestHudVisible;
  };

  Game_System.prototype.chromaSetQuestHudVisible = function(value) {
    this.chromaEnsureQuestHudData();
    this._chromaQuestHudVisible = !!value;
    return this._chromaQuestHudVisible;
  };

  Game_System.prototype.chromaQuestMarkerVisible = function() {
    this.chromaEnsureQuestHudData();
    return !!this._chromaQuestMarkerVisible;
  };

  Game_System.prototype.chromaSetQuestMarkerVisible = function(value) {
    this.chromaEnsureQuestHudData();
    this._chromaQuestMarkerVisible = !!value;
    return this._chromaQuestMarkerVisible;
  };

  const _Game_System_initialize = Game_System.prototype.initialize;
  Game_System.prototype.initialize = function() {
    _Game_System_initialize.call(this);
    this.chromaEnsureQuestHudData();
  };

  const _DataManager_extractSaveContents = DataManager.extractSaveContents;
  DataManager.extractSaveContents = function(contents) {
    _DataManager_extractSaveContents.call(this, contents);
    if ($gameSystem && $gameSystem.chromaEnsureQuestHudData) {
      $gameSystem.chromaEnsureQuestHudData();
    }
  };

  function Window_QuestTrackerHud() {
    this.initialize(...arguments);
  }

  Window_QuestTrackerHud.prototype = Object.create(Window_Base.prototype);
  Window_QuestTrackerHud.prototype.constructor = Window_QuestTrackerHud;

  Window_QuestTrackerHud.prototype.initialize = function(rect) {
    Window_Base.prototype.initialize.call(this, rect);
    this.opacity = hudOpacity;
    this._snapshotKey = "";
    this._refreshCooldown = 0;
    this.refresh();
  };

  Window_QuestTrackerHud.prototype.update = function() {
    Window_Base.prototype.update.call(this);
    this.updateVisibility();
    if (!this.visible) return;

    if (this._refreshCooldown > 0) {
      this._refreshCooldown -= 1;
    } else {
      this._refreshCooldown = 15;
      this.refreshIfChanged();
    }
  };

  Window_QuestTrackerHud.prototype.forceRefresh = function() {
    this._snapshotKey = "";
    this.refresh();
  };

  Window_QuestTrackerHud.prototype.updateVisibility = function() {
    let visible = true;
    if (!$gameSystem || !$gameSystem.chromaQuestHudVisible()) {
      visible = false;
    }
    if (hideDuringMessage && $gameMessage && $gameMessage.isBusy()) {
      visible = false;
    }
    if (!hasQuestRuntime()) {
      visible = false;
    }
    this.visible = visible;
  };

  Window_QuestTrackerHud.prototype.snapshot = function() {
    const ctx = getTrackedStepContext();
    if (!ctx || !ctx.entry) {
      return {
        key: "none",
        status: "none",
        title: "No tracked quest",
        detail: "Open Quests menu to review available objectives.",
      };
    }

    const entry = ctx.entry;
    const stepInfo = ctx.stepInfo;
    const label = normalizeStatusLabel(entry.status, entry.available);
    const title = `${label}: ${entry.summary.name || entry.id}`;
    const canonicalMapId = currentCanonicalMapId();

    let detail = entry.summary.description || "";
    if (stepInfo && stepInfo.step) {
      const stepLabel =
        stepInfo.step.name ||
        stepInfo.step.description ||
        `Step ${stepInfo.stepId}/${stepInfo.total}`;
      const targetBits = [];
      if (stepInfo.step.target_location) {
        if (canonicalMapId && stepInfo.step.target_location === canonicalMapId) {
          targetBits.push("ON MAP");
        } else {
          targetBits.push(`GO: ${stepInfo.step.target_location}`);
        }
      }
      if (stepInfo.step.target_npc) {
        targetBits.push(stepInfo.step.target_npc);
      }
      const target = targetBits.length ? ` | ${targetBits.join(" | ")}` : "";
      detail = `Step ${stepInfo.stepId}/${stepInfo.total}: ${stepLabel}${target}`;
    }

    return {
      key: [
        entry.id,
        entry.status,
        entry.available ? 1 : 0,
        entry.summary ? entry.summary.stepId : 0,
        title,
        detail,
      ].join("|"),
      status: entry.status,
      available: entry.available,
      title,
      detail,
    };
  };

  Window_QuestTrackerHud.prototype.refreshIfChanged = function() {
    const shot = this.snapshot();
    if (shot.key !== this._snapshotKey) {
      this.refresh();
    }
  };

  Window_QuestTrackerHud.prototype.refresh = function() {
    this.contents.clear();
    const shot = this.snapshot();
    this._snapshotKey = shot.key;

    const lh = this.lineHeight();
    const width = this.innerWidth;

    this.changeTextColor(statusColor(shot.status, !!shot.available));
    this.drawText(shot.title, 0, 0, width, "left");
    this.changeTextColor(ColorManager.normalColor());

    const detailY = lh;
    this.drawTrimmedText(shot.detail, 0, detailY, width);
  };

  Window_QuestTrackerHud.prototype.drawTrimmedText = function(text, x, y, width) {
    const source = String(text || "");
    if (!source) return;
    let line = "";
    for (const ch of source) {
      const test = line + ch;
      if (this.textWidth(test) <= width) {
        line = test;
      } else {
        line += "...";
        break;
      }
    }
    this.drawText(line || source, x, y, width, "left");
  };

  const npcTagRegex = /<\s*questTargetNpc\s*:\s*([A-Za-z0-9_:-]+)\s*>/i;
  const questTagRegex = /<\s*questTargetQuest\s*:\s*([A-Za-z0-9_:-]+)\s*>/i;
  let markerIndexMapId = -1;
  let markerNpcIndex = {};
  let markerQuestIndex = {};

  const rebuildMarkerIndexIfNeeded = () => {
    if (!$gameMap || !$dataMap) return;
    const mapId = $gameMap.mapId();
    if (mapId === markerIndexMapId) return;

    markerIndexMapId = mapId;
    markerNpcIndex = {};
    markerQuestIndex = {};
    const events = Array.isArray($dataMap.events) ? $dataMap.events : [];
    for (const ev of events) {
      if (!ev || typeof ev !== "object" || !ev.id) continue;
      const text = `${ev.note || ""}\n${ev.name || ""}`;
      const npcMatch = text.match(npcTagRegex);
      if (npcMatch && npcMatch[1]) {
        const key = String(npcMatch[1]).trim().toUpperCase();
        if (key && !markerNpcIndex[key]) {
          markerNpcIndex[key] = ev.id;
        }
      }
      const questMatch = text.match(questTagRegex);
      if (questMatch && questMatch[1]) {
        const key = String(questMatch[1]).trim().toUpperCase();
        if (key && !markerQuestIndex[key]) {
          markerQuestIndex[key] = ev.id;
        }
      }
    }
  };

  const resolveTargetEventId = () => {
    const ctx = getTrackedStepContext();
    if (!ctx || !ctx.entry || !ctx.step) return 0;

    const step = ctx.step;
    const currentMap = currentCanonicalMapId();
    const targetLocation =
      typeof step.target_location === "string" ? step.target_location : "";
    if (targetLocation) {
      if (!currentMap) return 0;
      if (targetLocation !== currentMap) return 0;
    }

    rebuildMarkerIndexIfNeeded();

    const npcId = typeof step.target_npc === "string" ? step.target_npc : "";
    if (npcId) {
      const eventId = markerNpcIndex[npcId.toUpperCase()];
      if (eventId) return eventId;
    }

    const questId = ctx.entry.id ? String(ctx.entry.id).toUpperCase() : "";
    if (questId && markerQuestIndex[questId]) {
      return markerQuestIndex[questId];
    }
    return 0;
  };

  function Sprite_QuestTargetMarker() {
    this.initialize(...arguments);
  }

  Sprite_QuestTargetMarker.prototype = Object.create(Sprite.prototype);
  Sprite_QuestTargetMarker.prototype.constructor = Sprite_QuestTargetMarker;

  Sprite_QuestTargetMarker.prototype.initialize = function() {
    Sprite.prototype.initialize.call(this);
    this.bitmap = new Bitmap(30, 30);
    this.anchor.x = 0.5;
    this.anchor.y = 1.0;
    this._eventId = 0;
    this._pulse = 0;
    this.createMarkerBitmap();
    this.visible = false;
  };

  Sprite_QuestTargetMarker.prototype.createMarkerBitmap = function() {
    const bmp = this.bitmap;
    bmp.clear();
    bmp.drawCircle(15, 12, 10, "#ff5a4a");
    bmp.fontSize = 18;
    bmp.textColor = "#ffffff";
    bmp.outlineColor = "rgba(0,0,0,0.75)";
    bmp.outlineWidth = 4;
    bmp.drawText("!", 0, 2, 30, 20, "center");
  };

  Sprite_QuestTargetMarker.prototype.setEventId = function(eventId) {
    const nextId = Number(eventId || 0);
    if (this._eventId !== nextId) {
      this._eventId = nextId;
    }
  };

  Sprite_QuestTargetMarker.prototype.update = function() {
    Sprite.prototype.update.call(this);
    if (this._eventId <= 0) {
      this.visible = false;
      return;
    }
    const ev = $gameMap ? $gameMap.event(this._eventId) : null;
    if (!ev) {
      this.visible = false;
      return;
    }
    this._pulse += 0.14;
    this.x = ev.screenX();
    this.y = ev.screenY() - markerYOffset + Math.sin(this._pulse) * 4;
    this.visible = true;
  };

  const _Scene_Map_createAllWindows = Scene_Map.prototype.createAllWindows;
  Scene_Map.prototype.createAllWindows = function() {
    _Scene_Map_createAllWindows.call(this);
    this.createChromaQuestTrackerHud();
  };

  Scene_Map.prototype.createChromaQuestTrackerHud = function() {
    const wh = this.calcWindowHeight(hudLineCount, false);
    const rect = new Rectangle(hudX, hudY, hudWidth, wh);
    this._chromaQuestTrackerHud = new Window_QuestTrackerHud(rect);
    this.addWindow(this._chromaQuestTrackerHud);
  };

  const _Scene_Map_createDisplayObjects = Scene_Map.prototype.createDisplayObjects;
  Scene_Map.prototype.createDisplayObjects = function() {
    _Scene_Map_createDisplayObjects.call(this);
    this.createChromaQuestTargetMarker();
  };

  Scene_Map.prototype.createChromaQuestTargetMarker = function() {
    if (!showTargetMarker || !this._spriteset) return;
    this._chromaQuestTargetMarker = new Sprite_QuestTargetMarker();
    this._chromaQuestMarkerCooldown = 0;
    this._spriteset.addChild(this._chromaQuestTargetMarker);
  };

  Scene_Map.prototype.updateChromaQuestTargetMarker = function() {
    const marker = this._chromaQuestTargetMarker;
    if (!marker) return;

    if (!showTargetMarker || !$gameSystem || !$gameSystem.chromaQuestMarkerVisible()) {
      marker.setEventId(0);
      marker.visible = false;
      return;
    }
    if (hideDuringMessage && $gameMessage && $gameMessage.isBusy()) {
      marker.setEventId(0);
      marker.visible = false;
      return;
    }
    if (!hasQuestRuntime()) {
      marker.setEventId(0);
      marker.visible = false;
      return;
    }

    if ((this._chromaQuestMarkerCooldown || 0) <= 0) {
      const eventId = resolveTargetEventId();
      marker.setEventId(eventId);
      this._chromaQuestMarkerCooldown = 15;
    } else {
      this._chromaQuestMarkerCooldown -= 1;
    }
  };

  const _Scene_Map_update = Scene_Map.prototype.update;
  Scene_Map.prototype.update = function() {
    _Scene_Map_update.call(this);
    this.updateChromaQuestTargetMarker();
  };

  const refreshSceneHud = () => {
    const scene = SceneManager._scene;
    if (scene && scene._chromaQuestTrackerHud && scene._chromaQuestTrackerHud.forceRefresh) {
      scene._chromaQuestTrackerHud.forceRefresh();
    }
    if (scene && scene._chromaQuestTargetMarker) {
      scene._chromaQuestMarkerCooldown = 0;
      if (scene.updateChromaQuestTargetMarker) {
        scene.updateChromaQuestTargetMarker();
      }
    }
  };

  PluginManager.registerCommand(pluginName, "SetQuestHudVisible", (args) => {
    if ($gameSystem && $gameSystem.chromaSetQuestHudVisible) {
      $gameSystem.chromaSetQuestHudVisible(toBool(args.value));
      refreshSceneHud();
    }
  });

  PluginManager.registerCommand(pluginName, "ToggleQuestHud", () => {
    if ($gameSystem && $gameSystem.chromaSetQuestHudVisible) {
      $gameSystem.chromaSetQuestHudVisible(!$gameSystem.chromaQuestHudVisible());
      refreshSceneHud();
    }
  });

  PluginManager.registerCommand(pluginName, "RefreshQuestHud", () => {
    refreshSceneHud();
  });

  PluginManager.registerCommand(pluginName, "SetQuestMarkerVisible", (args) => {
    if ($gameSystem && $gameSystem.chromaSetQuestMarkerVisible) {
      $gameSystem.chromaSetQuestMarkerVisible(toBool(args.value));
      refreshSceneHud();
    }
  });

  PluginManager.registerCommand(pluginName, "ToggleQuestMarker", () => {
    if ($gameSystem && $gameSystem.chromaSetQuestMarkerVisible) {
      $gameSystem.chromaSetQuestMarkerVisible(!$gameSystem.chromaQuestMarkerVisible());
      refreshSceneHud();
    }
  });

  const g = typeof window !== "undefined" ? window : globalThis;
  g.Imported = g.Imported || {};
  g.Imported.ChromaEdge_QuestTrackerHUD = true;
  g.ChromaEdge = g.ChromaEdge || {};
  g.ChromaEdge.QuestTracker = {
    show() {
      if ($gameSystem && $gameSystem.chromaSetQuestHudVisible) {
        $gameSystem.chromaSetQuestHudVisible(true);
        refreshSceneHud();
      }
    },
    hide() {
      if ($gameSystem && $gameSystem.chromaSetQuestHudVisible) {
        $gameSystem.chromaSetQuestHudVisible(false);
        refreshSceneHud();
      }
    },
    toggle() {
      if ($gameSystem && $gameSystem.chromaSetQuestHudVisible) {
        $gameSystem.chromaSetQuestHudVisible(!$gameSystem.chromaQuestHudVisible());
        refreshSceneHud();
      }
    },
    refresh() {
      refreshSceneHud();
    },
    visible() {
      return $gameSystem && $gameSystem.chromaQuestHudVisible
        ? $gameSystem.chromaQuestHudVisible()
        : false;
    },
    markerShow() {
      if ($gameSystem && $gameSystem.chromaSetQuestMarkerVisible) {
        $gameSystem.chromaSetQuestMarkerVisible(true);
        refreshSceneHud();
      }
    },
    markerHide() {
      if ($gameSystem && $gameSystem.chromaSetQuestMarkerVisible) {
        $gameSystem.chromaSetQuestMarkerVisible(false);
        refreshSceneHud();
      }
    },
    markerToggle() {
      if ($gameSystem && $gameSystem.chromaSetQuestMarkerVisible) {
        $gameSystem.chromaSetQuestMarkerVisible(!$gameSystem.chromaQuestMarkerVisible());
        refreshSceneHud();
      }
    },
    markerVisible() {
      return $gameSystem && $gameSystem.chromaQuestMarkerVisible
        ? $gameSystem.chromaQuestMarkerVisible()
        : false;
    },
  };
})();
