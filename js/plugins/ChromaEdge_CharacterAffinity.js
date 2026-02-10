/*:
 * @target MZ
 * @plugindesc v0.1.0 Chroma's Edge affinity tracking foundation.
 * @author Chroma's Edge
 * @help
 * Week 1 foundation plugin.
 *
 * Tracks relationship affinity for actor pairs and exposes:
 * - plugin commands for eventing
 * - save persistence
 * - script-call API for future systems (DLB, menus, quests)
 *
 * Script calls:
 *   $gameSystem.chromaGetAffinity(actorIdA, actorIdB)
 *   $gameSystem.chromaSetAffinity(actorIdA, actorIdB, value)
 *   $gameSystem.chromaAddAffinity(actorIdA, actorIdB, delta)
 *   $gameSystem.chromaCanDualLimit(actorIdA, actorIdB)
 *
 * Optional global helper:
 *   ChromaEdge.Affinity.get(a, b)
 *   ChromaEdge.Affinity.set(a, b, value)
 *   ChromaEdge.Affinity.add(a, b, delta)
 *   ChromaEdge.Affinity.canDualLimit(a, b)
 *
 * @param minAffinity
 * @text Min Affinity
 * @type number
 * @min 0
 * @default 1
 *
 * @param maxAffinity
 * @text Max Affinity
 * @type number
 * @min 1
 * @default 10
 *
 * @param defaultAffinity
 * @text Default Affinity
 * @type number
 * @default 1
 *
 * @param dlbRequiredAffinity
 * @text DLB Requirement
 * @type number
 * @default 10
 *
 * @command SetAffinity
 * @text Set Affinity
 * @arg actorIdA
 * @type actor
 * @default 1
 * @arg actorIdB
 * @type actor
 * @default 2
 * @arg value
 * @type number
 * @default 1
 * @arg variableId
 * @text Store In Variable
 * @type variable
 * @default 0
 *
 * @command AddAffinity
 * @text Add Affinity
 * @arg actorIdA
 * @type actor
 * @default 1
 * @arg actorIdB
 * @type actor
 * @default 2
 * @arg delta
 * @type number
 * @default 1
 * @arg variableId
 * @text Store In Variable
 * @type variable
 * @default 0
 *
 * @command GetAffinity
 * @text Get Affinity
 * @arg actorIdA
 * @type actor
 * @default 1
 * @arg actorIdB
 * @type actor
 * @default 2
 * @arg variableId
 * @type variable
 * @default 1
 *
 * @command CanDualLimit
 * @text Can Use Dual Limit
 * @arg actorIdA
 * @type actor
 * @default 1
 * @arg actorIdB
 * @type actor
 * @default 2
 * @arg switchId
 * @type switch
 * @default 1
 *
 * @command ResetAllAffinity
 * @text Reset All Affinity
 * @arg value
 * @type number
 * @default 1
 *
 * @command SeedActiveParty
 * @text Seed Active Party Pairs
 * @arg value
 * @type number
 * @default 1
 */

(() => {
  "use strict";

  const pluginName = "ChromaEdge_CharacterAffinity";
  const params = PluginManager.parameters(pluginName);
  const MIN_AFFINITY = Number(params.minAffinity || 1);
  const MAX_AFFINITY = Number(params.maxAffinity || 10);
  const DEFAULT_AFFINITY = Number(params.defaultAffinity || 1);
  const DLB_REQUIRED = Number(params.dlbRequiredAffinity || 10);

  const parseIntSafe = (value, fallback = 0) => {
    const parsed = Number(value);
    return Number.isFinite(parsed) ? Math.floor(parsed) : fallback;
  };

  const clampAffinity = (value) =>
    Math.max(MIN_AFFINITY, Math.min(MAX_AFFINITY, Math.round(value)));

  const pairKey = (actorIdA, actorIdB) => {
    const a = parseIntSafe(actorIdA);
    const b = parseIntSafe(actorIdB);
    if (a <= 0 || b <= 0 || a === b) return "";
    return a < b ? `${a}:${b}` : `${b}:${a}`;
  };

  Game_System.prototype.chromaInitAffinityData = function() {
    if (!this._chromaAffinity || typeof this._chromaAffinity !== "object") {
      this._chromaAffinity = {};
    }
  };

  Game_System.prototype.chromaAffinityMap = function() {
    this.chromaInitAffinityData();
    return this._chromaAffinity;
  };

  Game_System.prototype.chromaGetAffinity = function(actorIdA, actorIdB) {
    this.chromaInitAffinityData();
    const key = pairKey(actorIdA, actorIdB);
    if (!key) return DEFAULT_AFFINITY;
    if (this._chromaAffinity[key] == null) {
      this._chromaAffinity[key] = clampAffinity(DEFAULT_AFFINITY);
    }
    return clampAffinity(this._chromaAffinity[key]);
  };

  Game_System.prototype.chromaSetAffinity = function(actorIdA, actorIdB, value) {
    this.chromaInitAffinityData();
    const key = pairKey(actorIdA, actorIdB);
    if (!key) return DEFAULT_AFFINITY;
    const next = clampAffinity(parseIntSafe(value, DEFAULT_AFFINITY));
    this._chromaAffinity[key] = next;
    return next;
  };

  Game_System.prototype.chromaAddAffinity = function(actorIdA, actorIdB, delta) {
    const current = this.chromaGetAffinity(actorIdA, actorIdB);
    return this.chromaSetAffinity(actorIdA, actorIdB, current + parseIntSafe(delta, 0));
  };

  Game_System.prototype.chromaCanDualLimit = function(actorIdA, actorIdB) {
    return this.chromaGetAffinity(actorIdA, actorIdB) >= DLB_REQUIRED;
  };

  Game_System.prototype.chromaResetAllAffinity = function(value) {
    const target = clampAffinity(parseIntSafe(value, DEFAULT_AFFINITY));
    this.chromaInitAffinityData();
    Object.keys(this._chromaAffinity).forEach((key) => {
      this._chromaAffinity[key] = target;
    });
  };

  Game_System.prototype.chromaSeedActorPairs = function(actorIds, value) {
    const ids = (actorIds || []).map((id) => parseIntSafe(id)).filter((id) => id > 0);
    const base = clampAffinity(parseIntSafe(value, DEFAULT_AFFINITY));
    for (let i = 0; i < ids.length; i += 1) {
      for (let j = i + 1; j < ids.length; j += 1) {
        this.chromaSetAffinity(ids[i], ids[j], base);
      }
    }
  };

  Game_System.prototype.chromaSeedActivePartyPairs = function(value) {
    const members = $gameParty ? $gameParty.members() : [];
    const actorIds = members.map((actor) => actor.actorId());
    this.chromaSeedActorPairs(actorIds, value);
  };

  const _Game_System_initialize = Game_System.prototype.initialize;
  Game_System.prototype.initialize = function() {
    _Game_System_initialize.call(this);
    this.chromaInitAffinityData();
  };

  const _DataManager_extractSaveContents = DataManager.extractSaveContents;
  DataManager.extractSaveContents = function(contents) {
    _DataManager_extractSaveContents.call(this, contents);
    if ($gameSystem && $gameSystem.chromaInitAffinityData) {
      $gameSystem.chromaInitAffinityData();
    }
  };

  const setVariable = (variableId, value) => {
    const id = parseIntSafe(variableId);
    if (id > 0 && $gameVariables) {
      $gameVariables.setValue(id, value);
    }
  };

  const setSwitch = (switchId, value) => {
    const id = parseIntSafe(switchId);
    if (id > 0 && $gameSwitches) {
      $gameSwitches.setValue(id, !!value);
    }
  };

  PluginManager.registerCommand(pluginName, "SetAffinity", (args) => {
    const value = $gameSystem.chromaSetAffinity(args.actorIdA, args.actorIdB, args.value);
    setVariable(args.variableId, value);
  });

  PluginManager.registerCommand(pluginName, "AddAffinity", (args) => {
    const value = $gameSystem.chromaAddAffinity(args.actorIdA, args.actorIdB, args.delta);
    setVariable(args.variableId, value);
  });

  PluginManager.registerCommand(pluginName, "GetAffinity", (args) => {
    const value = $gameSystem.chromaGetAffinity(args.actorIdA, args.actorIdB);
    setVariable(args.variableId, value);
  });

  PluginManager.registerCommand(pluginName, "CanDualLimit", (args) => {
    const canUse = $gameSystem.chromaCanDualLimit(args.actorIdA, args.actorIdB);
    setSwitch(args.switchId, canUse);
  });

  PluginManager.registerCommand(pluginName, "ResetAllAffinity", (args) => {
    $gameSystem.chromaResetAllAffinity(args.value);
  });

  PluginManager.registerCommand(pluginName, "SeedActiveParty", (args) => {
    $gameSystem.chromaSeedActivePartyPairs(args.value);
  });

  const globalObject = typeof window !== "undefined" ? window : globalThis;
  globalObject.ChromaEdge = globalObject.ChromaEdge || {};
  globalObject.ChromaEdge.Affinity = {
    get(actorIdA, actorIdB) {
      return $gameSystem.chromaGetAffinity(actorIdA, actorIdB);
    },
    set(actorIdA, actorIdB, value) {
      return $gameSystem.chromaSetAffinity(actorIdA, actorIdB, value);
    },
    add(actorIdA, actorIdB, delta) {
      return $gameSystem.chromaAddAffinity(actorIdA, actorIdB, delta);
    },
    canDualLimit(actorIdA, actorIdB) {
      return $gameSystem.chromaCanDualLimit(actorIdA, actorIdB);
    },
    dump() {
      return Object.assign({}, $gameSystem.chromaAffinityMap());
    },
  };
})();
