/*:
 * @target MZ
 * @plugindesc v0.2.0 Tower floor progression, unlock state, and palace gate sync.
 * @author Chroma's Edge
 * @help
 * Tracks tower progression using canonical tower metadata and provides
 * script/plugin-command access for floor gating.
 *
 * Script calls:
 *   ChromaEdge.Tower.unlockTower(true)
 *   ChromaEdge.Tower.clearFloor(50)
 *   ChromaEdge.Tower.isFloorUnlocked(75)
 *   ChromaEdge.Tower.progress()
 *
 * @param towerUnlockSwitchId
 * @text Tower Unlock Switch Id
 * @type switch
 * @default 40
 *
 * @param palaceUnlockSwitchId
 * @text Palace Unlock Switch Id
 * @type switch
 * @default 41
 *
 * @param initialUnlockedFloor
 * @text Initial Unlocked Floor
 * @type number
 * @default 10
 *
 * @param loadOnBoot
 * @text Load Tower Data On Boot
 * @type boolean
 * @default true
 *
 * @command ReloadTowerData
 * @text Reload Tower Data
 * @arg switchId
 * @text Success Switch
 * @type switch
 * @default 0
 * @arg variableId
 * @text Floor Count Variable
 * @type variable
 * @default 0
 *
 * @command SetTowerUnlocked
 * @text Set Tower Unlocked
 * @arg value
 * @type boolean
 * @default true
 *
 * @command UnlockFloor
 * @text Unlock Floor
 * @arg floor
 * @type number
 * @default 10
 *
 * @command ClearFloor
 * @text Clear Floor
 * @arg floor
 * @type number
 * @default 10
 *
 * @command CheckFloorUnlocked
 * @text Check Floor Unlocked
 * @arg floor
 * @type number
 * @default 10
 * @arg switchId
 * @type switch
 * @default 1
 *
 * @command CheckFloorCleared
 * @text Check Floor Cleared
 * @arg floor
 * @type number
 * @default 10
 * @arg switchId
 * @type switch
 * @default 1
 *
 * @command SetTowerEventFlag
 * @text Set Tower Event Flag
 * @arg flagId
 * @type string
 * @default TOWER_CLEARED
 * @arg value
 * @type boolean
 * @default true
 *
 * @command GetTowerProgress
 * @text Get Tower Progress
 * @arg unlockedFloorVar
 * @type variable
 * @default 0
 * @arg clearedFloorVar
 * @type variable
 * @default 0
 * @arg percentVar
 * @type variable
 * @default 0
 */

(() => {
  "use strict";

  const pluginName = "ChromaEdge_TowerProgression";
  const params = PluginManager.parameters(pluginName);
  const towerUnlockSwitchId = Number(params.towerUnlockSwitchId || 40);
  const palaceUnlockSwitchId = Number(params.palaceUnlockSwitchId || 41);
  const initialUnlockedFloor = Number(params.initialUnlockedFloor || 10);
  const loadOnBoot = String(params.loadOnBoot || "true").toLowerCase() === "true";

  const TOWER_DATA_PATH = "assets/data/maps/map_tower_palace_remnant.json";

  const toInt = (value, fallback = 0) => {
    const parsed = Number(value);
    return Number.isFinite(parsed) ? Math.floor(parsed) : fallback;
  };

  const toBool = (value) =>
    String(value === undefined ? "" : value).toLowerCase() === "true";

  const setSwitch = (switchId, value) => {
    const id = toInt(switchId, 0);
    if (id > 0 && $gameSwitches) $gameSwitches.setValue(id, !!value);
  };

  const setVariable = (variableId, value) => {
    const id = toInt(variableId, 0);
    if (id > 0 && $gameVariables) $gameVariables.setValue(id, value);
  };

  const stripBom = (text) =>
    text && text.charCodeAt(0) === 0xfeff ? text.slice(1) : text;

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

  const parseUnlockFloorFromFlag = (flagId) => {
    const m = String(flagId || "").match(/F(\d+)_UNLOCKED/i);
    return m ? toInt(m[1], 0) : 0;
  };

  let towerRuntime = {
    ready: false,
    arenaByFloor: {},
    towerFloors: [],
    errors: [],
    warnings: [],
  };

  const buildTowerRuntime = () => {
    const errors = [];
    const warnings = [];
    const arenaByFloor = {};

    let data = null;
    try {
      data = loadJsonSync(TOWER_DATA_PATH);
    } catch (err) {
      errors.push(err.message || String(err));
      return {
        ready: false,
        arenaByFloor,
        towerFloors: [],
        errors,
        warnings,
      };
    }

    const maps = Array.isArray(data && data.maps) ? data.maps : [];
    for (const mapEntry of maps) {
      if (!mapEntry || typeof mapEntry !== "object") continue;
      if (String(mapEntry.type || "") !== "tower_arena") continue;
      const floor = toInt(mapEntry.floor, 0);
      if (floor <= 0) {
        warnings.push(`tower_arena entry missing floor: ${mapEntry.id || "(unknown id)"}`);
        continue;
      }
      if (!arenaByFloor[floor]) {
        arenaByFloor[floor] = {
          id: String(mapEntry.id || `FLOOR_${floor}`),
          floor,
          displayName: String(mapEntry.display_name || `Floor ${floor}`),
          events: Array.isArray(mapEntry.events)
            ? mapEntry.events.filter((e) => typeof e === "string" && e)
            : [],
          boss: String(mapEntry.boss || ""),
        };
      }
    }

    const towerFloors = Object.keys(arenaByFloor)
      .map((f) => toInt(f, 0))
      .filter((f) => f > 0)
      .sort((a, b) => a - b);

    return {
      ready: towerFloors.length > 0,
      arenaByFloor,
      towerFloors,
      errors,
      warnings,
    };
  };

  const reloadTowerRuntime = () => {
    towerRuntime = buildTowerRuntime();

    if (towerRuntime.warnings.length) {
      console.warn(`[${pluginName}] Tower warnings:`);
      for (const line of towerRuntime.warnings) {
        console.warn(`[${pluginName}] ${line}`);
      }
    }

    if (towerRuntime.errors.length) {
      console.error(`[${pluginName}] Tower errors:`);
      for (const line of towerRuntime.errors) {
        console.error(`[${pluginName}] ${line}`);
      }
    }

    return towerRuntime.ready;
  };

  const questApi = () => {
    const g = typeof window !== "undefined" ? window : globalThis;
    return g && g.ChromaEdge ? g.ChromaEdge.Quests : null;
  };

  Game_System.prototype.chromaInitTowerProgressionData = function() {
    if (!this._chromaTower || typeof this._chromaTower !== "object") {
      this._chromaTower = {
        towerUnlocked: false,
        palaceUnlocked: false,
        unlockedFloors: {},
        clearedFloors: {},
        eventFlags: {},
      };
    }

    const d = this._chromaTower;
    d.towerUnlocked = !!d.towerUnlocked;
    d.palaceUnlocked = !!d.palaceUnlocked;
    d.unlockedFloors = d.unlockedFloors && typeof d.unlockedFloors === "object" ? d.unlockedFloors : {};
    d.clearedFloors = d.clearedFloors && typeof d.clearedFloors === "object" ? d.clearedFloors : {};
    d.eventFlags = d.eventFlags && typeof d.eventFlags === "object" ? d.eventFlags : {};

    if (toInt(initialUnlockedFloor, 0) > 0) {
      d.unlockedFloors[String(toInt(initialUnlockedFloor, 0))] = true;
    }

    if ($gameSwitches) {
      if ($gameSwitches.value(towerUnlockSwitchId)) d.towerUnlocked = true;
      if ($gameSwitches.value(palaceUnlockSwitchId)) d.palaceUnlocked = true;
    }

    this.chromaTowerSyncSwitches();
  };

  Game_System.prototype.chromaTowerData = function() {
    this.chromaInitTowerProgressionData();
    return this._chromaTower;
  };

  Game_System.prototype.chromaTowerSyncSwitches = function() {
    const d = this._chromaTower && typeof this._chromaTower === "object" ? this._chromaTower : null;
    setSwitch(towerUnlockSwitchId, !!(d && d.towerUnlocked));
    setSwitch(palaceUnlockSwitchId, !!(d && d.palaceUnlocked));
  };

  Game_System.prototype.chromaTowerUnlocked = function() {
    return !!this.chromaTowerData().towerUnlocked;
  };

  Game_System.prototype.chromaSetTowerUnlocked = function(value) {
    const d = this.chromaTowerData();
    d.towerUnlocked = !!value;
    this.chromaTowerSyncSwitches();
    return d.towerUnlocked;
  };

  Game_System.prototype.chromaTowerPalaceUnlocked = function() {
    return !!this.chromaTowerData().palaceUnlocked;
  };

  Game_System.prototype.chromaSetTowerPalaceUnlocked = function(value) {
    const d = this.chromaTowerData();
    d.palaceUnlocked = !!value;
    this.chromaTowerSyncSwitches();
    return d.palaceUnlocked;
  };

  Game_System.prototype.chromaTowerUnlockFloor = function(floor) {
    const f = toInt(floor, 0);
    if (f <= 0) return false;
    const d = this.chromaTowerData();
    d.unlockedFloors[String(f)] = true;
    return true;
  };

  Game_System.prototype.chromaTowerIsFloorUnlocked = function(floor) {
    const f = toInt(floor, 0);
    if (f <= 0) return false;
    const d = this.chromaTowerData();
    return !!d.unlockedFloors[String(f)];
  };

  Game_System.prototype.chromaTowerIsFloorCleared = function(floor) {
    const f = toInt(floor, 0);
    if (f <= 0) return false;
    const d = this.chromaTowerData();
    return !!d.clearedFloors[String(f)];
  };

  Game_System.prototype.chromaTowerSetEventFlag = function(flagId, value) {
    const key = String(flagId || "").trim().toUpperCase();
    if (!key) return false;

    const d = this.chromaTowerData();
    if (value) d.eventFlags[key] = true;
    else delete d.eventFlags[key];

    const q = questApi();
    if (q && typeof q.setFlag === "function") {
      q.setFlag(key, !!value);
    }

    const unlockFloor = parseUnlockFloorFromFlag(key);
    if (unlockFloor > 0 && value) {
      this.chromaTowerUnlockFloor(unlockFloor);
    }

    if (key === "PALACE_ACCESS" && value) {
      this.chromaSetTowerPalaceUnlocked(true);
    }

    if (key === "TOWER_CLEARED" && value) {
      this.chromaSetTowerUnlocked(true);
    }

    return true;
  };

  Game_System.prototype.chromaTowerEventFlag = function(flagId) {
    const key = String(flagId || "").trim().toUpperCase();
    if (!key) return false;
    return !!this.chromaTowerData().eventFlags[key];
  };

  Game_System.prototype.chromaTowerClearFloor = function(floor) {
    const f = toInt(floor, 0);
    if (f <= 0) return false;

    const d = this.chromaTowerData();
    d.clearedFloors[String(f)] = true;
    d.unlockedFloors[String(f)] = true;
    if (!d.towerUnlocked) d.towerUnlocked = true;

    const arena = towerRuntime.arenaByFloor[f];
    if (arena && Array.isArray(arena.events)) {
      for (const flagId of arena.events) {
        this.chromaTowerSetEventFlag(flagId, true);
      }
    }

    if (f >= 100) {
      this.chromaTowerSetEventFlag("TOWER_CLEARED", true);
      this.chromaSetTowerPalaceUnlocked(true);
    }

    this.chromaTowerSyncSwitches();
    return true;
  };

  Game_System.prototype.chromaTowerHighestUnlockedFloor = function() {
    const d = this.chromaTowerData();
    const floors = Object.keys(d.unlockedFloors)
      .map((f) => toInt(f, 0))
      .filter((f) => f > 0)
      .sort((a, b) => b - a);
    return floors.length ? floors[0] : 0;
  };

  Game_System.prototype.chromaTowerHighestClearedFloor = function() {
    const d = this.chromaTowerData();
    const floors = Object.keys(d.clearedFloors)
      .map((f) => toInt(f, 0))
      .filter((f) => f > 0)
      .sort((a, b) => b - a);
    return floors.length ? floors[0] : 0;
  };

  Game_System.prototype.chromaTowerProgressPercent = function() {
    if (!towerRuntime.ready || towerRuntime.towerFloors.length <= 0) return 0;
    const total = towerRuntime.towerFloors.length;
    let cleared = 0;
    for (const floor of towerRuntime.towerFloors) {
      if (this.chromaTowerIsFloorCleared(floor)) cleared += 1;
    }
    return Math.round((cleared / total) * 100);
  };

  Game_System.prototype.chromaTowerSnapshot = function() {
    const d = this.chromaTowerData();
    return {
      towerUnlocked: !!d.towerUnlocked,
      palaceUnlocked: !!d.palaceUnlocked,
      highestUnlockedFloor: this.chromaTowerHighestUnlockedFloor(),
      highestClearedFloor: this.chromaTowerHighestClearedFloor(),
      progressPercent: this.chromaTowerProgressPercent(),
      unlockedFloors: Object.keys(d.unlockedFloors)
        .filter((k) => d.unlockedFloors[k])
        .map((k) => toInt(k, 0))
        .filter((k) => k > 0)
        .sort((a, b) => a - b),
      clearedFloors: Object.keys(d.clearedFloors)
        .filter((k) => d.clearedFloors[k])
        .map((k) => toInt(k, 0))
        .filter((k) => k > 0)
        .sort((a, b) => a - b),
      eventFlags: Object.keys(d.eventFlags)
        .filter((k) => d.eventFlags[k])
        .sort(),
    };
  };

  const _Game_System_initialize = Game_System.prototype.initialize;
  Game_System.prototype.initialize = function() {
    _Game_System_initialize.call(this);
    this.chromaInitTowerProgressionData();
  };

  const _DataManager_extractSaveContents = DataManager.extractSaveContents;
  DataManager.extractSaveContents = function(contents) {
    _DataManager_extractSaveContents.call(this, contents);
    if ($gameSystem && $gameSystem.chromaInitTowerProgressionData) {
      $gameSystem.chromaInitTowerProgressionData();
    }
  };

  PluginManager.registerCommand(pluginName, "ReloadTowerData", (args) => {
    const ok = reloadTowerRuntime();
    setSwitch(args.switchId, ok);
    setVariable(args.variableId, towerRuntime.towerFloors.length);
  });

  PluginManager.registerCommand(pluginName, "SetTowerUnlocked", (args) => {
    $gameSystem.chromaSetTowerUnlocked(toBool(args.value));
  });

  PluginManager.registerCommand(pluginName, "UnlockFloor", (args) => {
    $gameSystem.chromaTowerUnlockFloor(args.floor);
  });

  PluginManager.registerCommand(pluginName, "ClearFloor", (args) => {
    $gameSystem.chromaTowerClearFloor(args.floor);
  });

  PluginManager.registerCommand(pluginName, "CheckFloorUnlocked", (args) => {
    setSwitch(args.switchId, $gameSystem.chromaTowerIsFloorUnlocked(args.floor));
  });

  PluginManager.registerCommand(pluginName, "CheckFloorCleared", (args) => {
    setSwitch(args.switchId, $gameSystem.chromaTowerIsFloorCleared(args.floor));
  });

  PluginManager.registerCommand(pluginName, "SetTowerEventFlag", (args) => {
    $gameSystem.chromaTowerSetEventFlag(args.flagId, toBool(args.value));
  });

  PluginManager.registerCommand(pluginName, "GetTowerProgress", (args) => {
    setVariable(args.unlockedFloorVar, $gameSystem.chromaTowerHighestUnlockedFloor());
    setVariable(args.clearedFloorVar, $gameSystem.chromaTowerHighestClearedFloor());
    setVariable(args.percentVar, $gameSystem.chromaTowerProgressPercent());
  });

  const g = typeof window !== "undefined" ? window : globalThis;
  g.Imported = g.Imported || {};
  g.Imported.ChromaEdge_TowerProgression = true;
  g.ChromaEdge = g.ChromaEdge || {};

  g.ChromaEdge.Tower = {
    ready() {
      return towerRuntime.ready;
    },
    reload() {
      return reloadTowerRuntime();
    },
    floors() {
      return towerRuntime.towerFloors.slice();
    },
    unlockTower(value = true) {
      return $gameSystem ? $gameSystem.chromaSetTowerUnlocked(!!value) : false;
    },
    isTowerUnlocked() {
      return $gameSystem ? $gameSystem.chromaTowerUnlocked() : false;
    },
    unlockFloor(floor) {
      return $gameSystem ? $gameSystem.chromaTowerUnlockFloor(floor) : false;
    },
    clearFloor(floor) {
      return $gameSystem ? $gameSystem.chromaTowerClearFloor(floor) : false;
    },
    isFloorUnlocked(floor) {
      return $gameSystem ? $gameSystem.chromaTowerIsFloorUnlocked(floor) : false;
    },
    isFloorCleared(floor) {
      return $gameSystem ? $gameSystem.chromaTowerIsFloorCleared(floor) : false;
    },
    setEventFlag(flagId, value = true) {
      return $gameSystem ? $gameSystem.chromaTowerSetEventFlag(flagId, !!value) : false;
    },
    eventFlag(flagId) {
      return $gameSystem ? $gameSystem.chromaTowerEventFlag(flagId) : false;
    },
    progress() {
      return $gameSystem
        ? $gameSystem.chromaTowerSnapshot()
        : {
            towerUnlocked: false,
            palaceUnlocked: false,
            highestUnlockedFloor: 0,
            highestClearedFloor: 0,
            progressPercent: 0,
            unlockedFloors: [],
            clearedFloors: [],
            eventFlags: [],
          };
    },
  };

  if (loadOnBoot) {
    reloadTowerRuntime();
  }
})();
