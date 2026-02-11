/*:
 * @target MZ
 * @plugindesc v0.2.0 Boss mercy/kill choice persistence with totals and route score.
 * @author Chroma's Edge
 * @help
 * Stores mercy choices per boss/encounter id.
 *
 * Choice codes:
 * - none: 0
 * - spare: 1
 * - kill: 2
 *
 * Script calls:
 *   ChromaEdge.Mercy.setChoice("BOSS_MERCER", "spare")
 *   ChromaEdge.Mercy.choice("BOSS_MERCER")
 *   ChromaEdge.Mercy.score()
 *
 * @param spareScore
 * @text Spare Score Delta
 * @type number
 * @default 1
 *
 * @param killScore
 * @text Kill Score Delta
 * @type number
 * @default -1
 *
 * @command SetMercyChoice
 * @text Set Mercy Choice
 * @arg bossId
 * @type string
 * @default BOSS_MERCER
 * @arg choice
 * @type select
 * @option Spare
 * @value spare
 * @option Kill
 * @value kill
 * @option Clear
 * @value none
 * @default spare
 * @arg switchId
 * @text Success Switch
 * @type switch
 * @default 0
 *
 * @command GetMercyChoice
 * @text Get Mercy Choice
 * @arg bossId
 * @type string
 * @default BOSS_MERCER
 * @arg variableId
 * @type variable
 * @default 1
 *
 * @command CheckMercyChoice
 * @text Check Mercy Choice
 * @arg bossId
 * @type string
 * @default BOSS_MERCER
 * @arg choice
 * @type select
 * @option Spare
 * @value spare
 * @option Kill
 * @value kill
 * @default spare
 * @arg switchId
 * @type switch
 * @default 1
 *
 * @command ResetMercyChoice
 * @text Reset Mercy Choice
 * @arg bossId
 * @type string
 * @default BOSS_MERCER
 *
 * @command ResetAllMercyChoices
 * @text Reset All Mercy Choices
 *
 * @command GetMercyTotals
 * @text Get Mercy Totals
 * @arg sparedVariableId
 * @type variable
 * @default 0
 * @arg killedVariableId
 * @type variable
 * @default 0
 * @arg scoreVariableId
 * @type variable
 * @default 0
 */

(() => {
  "use strict";

  const pluginName = "ChromaEdge_MercyChoiceSystem";
  const params = PluginManager.parameters(pluginName);
  const spareScore = Number(params.spareScore || 1);
  const killScore = Number(params.killScore || -1);

  const CHOICE_CODE = {
    none: 0,
    spare: 1,
    kill: 2,
  };

  const normalizeBossId = (value) => String(value || "").trim().toUpperCase();

  const normalizeChoice = (choice) => {
    const c = String(choice || "").trim().toLowerCase();
    if (c === "spare") return "spare";
    if (c === "kill") return "kill";
    return "none";
  };

  const toInt = (value, fallback = 0) => {
    const parsed = Number(value);
    return Number.isFinite(parsed) ? Math.floor(parsed) : fallback;
  };

  const setSwitch = (switchId, value) => {
    const id = toInt(switchId, 0);
    if (id > 0 && $gameSwitches) $gameSwitches.setValue(id, !!value);
  };

  const setVariable = (variableId, value) => {
    const id = toInt(variableId, 0);
    if (id > 0 && $gameVariables) $gameVariables.setValue(id, value);
  };

  const questApi = () => {
    const g = typeof window !== "undefined" ? window : globalThis;
    return g && g.ChromaEdge ? g.ChromaEdge.Quests : null;
  };

  Game_System.prototype.chromaInitMercyData = function() {
    if (!this._chromaMercyChoices || typeof this._chromaMercyChoices !== "object") {
      this._chromaMercyChoices = {};
    }
  };

  Game_System.prototype.chromaMercyMap = function() {
    this.chromaInitMercyData();
    return this._chromaMercyChoices;
  };

  Game_System.prototype.chromaSetMercyChoice = function(bossId, choice) {
    const id = normalizeBossId(bossId);
    if (!id) return false;

    const c = normalizeChoice(choice);
    const map = this.chromaMercyMap();

    if (c === "none") {
      delete map[id];
    } else {
      map[id] = {
        bossId: id,
        choice: c,
        updatedAt: Date.now(),
      };
    }

    const q = questApi();
    if (q && typeof q.setFlag === "function") {
      q.setFlag(`MERCY_${id}_SPARED`, c === "spare");
      q.setFlag(`MERCY_${id}_KILLED`, c === "kill");
    }

    return true;
  };

  Game_System.prototype.chromaMercyChoice = function(bossId) {
    const id = normalizeBossId(bossId);
    if (!id) return "none";
    const rec = this.chromaMercyMap()[id];
    if (!rec || typeof rec !== "object") return "none";
    return normalizeChoice(rec.choice);
  };

  Game_System.prototype.chromaMercyChoiceCode = function(bossId) {
    const choice = this.chromaMercyChoice(bossId);
    return CHOICE_CODE[choice] == null ? CHOICE_CODE.none : CHOICE_CODE[choice];
  };

  Game_System.prototype.chromaHasMercyChoice = function(bossId, choice) {
    return this.chromaMercyChoice(bossId) === normalizeChoice(choice);
  };

  Game_System.prototype.chromaResetMercyChoice = function(bossId) {
    return this.chromaSetMercyChoice(bossId, "none");
  };

  Game_System.prototype.chromaResetAllMercyChoices = function() {
    this._chromaMercyChoices = {};
  };

  Game_System.prototype.chromaMercyCounts = function() {
    const map = this.chromaMercyMap();
    let spared = 0;
    let killed = 0;
    for (const key of Object.keys(map)) {
      const choice = normalizeChoice(map[key] && map[key].choice);
      if (choice === "spare") spared += 1;
      if (choice === "kill") killed += 1;
    }
    return { spared, killed };
  };

  Game_System.prototype.chromaMercyScore = function() {
    const counts = this.chromaMercyCounts();
    return counts.spared * spareScore + counts.killed * killScore;
  };

  Game_System.prototype.chromaMercyIds = function() {
    return Object.keys(this.chromaMercyMap()).sort();
  };

  const _Game_System_initialize = Game_System.prototype.initialize;
  Game_System.prototype.initialize = function() {
    _Game_System_initialize.call(this);
    this.chromaInitMercyData();
  };

  const _DataManager_extractSaveContents = DataManager.extractSaveContents;
  DataManager.extractSaveContents = function(contents) {
    _DataManager_extractSaveContents.call(this, contents);
    if ($gameSystem && $gameSystem.chromaInitMercyData) {
      $gameSystem.chromaInitMercyData();
    }
  };

  PluginManager.registerCommand(pluginName, "SetMercyChoice", (args) => {
    const ok = $gameSystem.chromaSetMercyChoice(args.bossId, args.choice);
    setSwitch(args.switchId, ok);
  });

  PluginManager.registerCommand(pluginName, "GetMercyChoice", (args) => {
    setVariable(args.variableId, $gameSystem.chromaMercyChoiceCode(args.bossId));
  });

  PluginManager.registerCommand(pluginName, "CheckMercyChoice", (args) => {
    const ok = $gameSystem.chromaHasMercyChoice(args.bossId, args.choice);
    setSwitch(args.switchId, ok);
  });

  PluginManager.registerCommand(pluginName, "ResetMercyChoice", (args) => {
    $gameSystem.chromaResetMercyChoice(args.bossId);
  });

  PluginManager.registerCommand(pluginName, "ResetAllMercyChoices", () => {
    $gameSystem.chromaResetAllMercyChoices();
  });

  PluginManager.registerCommand(pluginName, "GetMercyTotals", (args) => {
    const counts = $gameSystem.chromaMercyCounts();
    setVariable(args.sparedVariableId, counts.spared);
    setVariable(args.killedVariableId, counts.killed);
    setVariable(args.scoreVariableId, $gameSystem.chromaMercyScore());
  });

  const g = typeof window !== "undefined" ? window : globalThis;
  g.Imported = g.Imported || {};
  g.Imported.ChromaEdge_MercyChoiceSystem = true;
  g.ChromaEdge = g.ChromaEdge || {};

  g.ChromaEdge.Mercy = {
    setChoice(bossId, choice) {
      return $gameSystem ? $gameSystem.chromaSetMercyChoice(bossId, choice) : false;
    },
    choice(bossId) {
      return $gameSystem ? $gameSystem.chromaMercyChoice(bossId) : "none";
    },
    choiceCode(bossId) {
      return $gameSystem ? $gameSystem.chromaMercyChoiceCode(bossId) : CHOICE_CODE.none;
    },
    wasSpared(bossId) {
      return $gameSystem ? $gameSystem.chromaHasMercyChoice(bossId, "spare") : false;
    },
    wasKilled(bossId) {
      return $gameSystem ? $gameSystem.chromaHasMercyChoice(bossId, "kill") : false;
    },
    reset(bossId) {
      return $gameSystem ? $gameSystem.chromaResetMercyChoice(bossId) : false;
    },
    resetAll() {
      if (!$gameSystem) return;
      $gameSystem.chromaResetAllMercyChoices();
    },
    ids() {
      return $gameSystem ? $gameSystem.chromaMercyIds() : [];
    },
    counts() {
      return $gameSystem ? $gameSystem.chromaMercyCounts() : { spared: 0, killed: 0 };
    },
    score() {
      return $gameSystem ? $gameSystem.chromaMercyScore() : 0;
    },
  };
})();
