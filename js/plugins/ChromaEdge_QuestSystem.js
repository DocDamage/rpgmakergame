/*:
 * @target MZ
 * @plugindesc v0.2.0 Runtime quest registry/state for canonical quest packs.
 * @author Chroma's Edge
 * @help
 * Loads quest content from `assets/data/quests` and provides:
 * - save-persistent quest state
 * - explicit quest/world-flag gating
 * - plugin commands for event integration
 * - script API for future quest journal UI
 *
 * Script calls:
 *   ChromaEdge.Quests.ready()
 *   ChromaEdge.Quests.ids()
 *   ChromaEdge.Quests.get("Q_PROLOGUE")
 *   ChromaEdge.Quests.start("Q_PROLOGUE")
 *   ChromaEdge.Quests.advance("Q_PROLOGUE")
 *   ChromaEdge.Quests.complete("Q_PROLOGUE")
 *   ChromaEdge.Quests.status("Q_PROLOGUE")
 *   ChromaEdge.Quests.step("Q_PROLOGUE")
 *   ChromaEdge.Quests.setFlag("POST_GAME", true)
 *   ChromaEdge.Quests.flag("POST_GAME")
 *
 * @param includeContentPacks
 * @text Include Content Packs
 * @type boolean
 * @default false
 * @desc Load quest_content_main_normalized and quest_content_mini_normalized.
 *
 * @param loadOnBoot
 * @text Load On Boot
 * @type boolean
 * @default true
 * @desc If true, quest packs are loaded during plugin initialization.
 *
 * @command ReloadQuestData
 * @text Reload Quest Data
 * @desc Reload quest packs from assets/data/quests.
 * @arg switchId
 * @text Success Switch
 * @type switch
 * @default 0
 * @arg variableId
 * @text Quest Count Variable
 * @type variable
 * @default 0
 *
 * @command StartQuest
 * @text Start Quest
 * @arg questId
 * @type string
 * @default Q_PROLOGUE
 * @arg force
 * @text Force Start
 * @type boolean
 * @default false
 * @arg switchId
 * @text Success Switch
 * @type switch
 * @default 0
 *
 * @command AdvanceQuest
 * @text Advance Quest
 * @arg questId
 * @type string
 * @default Q_PROLOGUE
 * @arg switchId
 * @text Success Switch
 * @type switch
 * @default 0
 *
 * @command CompleteQuest
 * @text Complete Quest
 * @arg questId
 * @type string
 * @default Q_PROLOGUE
 * @arg switchId
 * @text Success Switch
 * @type switch
 * @default 0
 *
 * @command FailQuest
 * @text Fail Quest
 * @arg questId
 * @type string
 * @default Q_PROLOGUE
 * @arg switchId
 * @text Success Switch
 * @type switch
 * @default 0
 *
 * @command SetQuestStep
 * @text Set Quest Step
 * @arg questId
 * @type string
 * @default Q_PROLOGUE
 * @arg stepId
 * @type number
 * @default 1
 * @arg switchId
 * @text Success Switch
 * @type switch
 * @default 0
 *
 * @command GetQuestStatus
 * @text Get Quest Status
 * @desc Stores status code: 0=locked, 1=active, 2=completed, 3=failed
 * @arg questId
 * @type string
 * @default Q_PROLOGUE
 * @arg variableId
 * @type variable
 * @default 1
 *
 * @command GetQuestStep
 * @text Get Quest Step
 * @arg questId
 * @type string
 * @default Q_PROLOGUE
 * @arg variableId
 * @type variable
 * @default 1
 *
 * @command CheckQuestAvailable
 * @text Check Quest Available
 * @arg questId
 * @type string
 * @default Q_PROLOGUE
 * @arg switchId
 * @type switch
 * @default 1
 *
 * @command CheckQuestComplete
 * @text Check Quest Complete
 * @arg questId
 * @type string
 * @default Q_PROLOGUE
 * @arg switchId
 * @type switch
 * @default 1
 *
 * @command SetQuestFlag
 * @text Set Quest Flag
 * @arg flagId
 * @type string
 * @default POST_GAME
 * @arg value
 * @type boolean
 * @default true
 */

(() => {
  "use strict";

  const pluginName = "ChromaEdge_QuestSystem";
  const params = PluginManager.parameters(pluginName);
  const includeContentPacks =
    String(params.includeContentPacks || "false").toLowerCase() === "true";
  const loadOnBoot = String(params.loadOnBoot || "true").toLowerCase() === "true";

  const STATUS = {
    locked: 0,
    active: 1,
    completed: 2,
    failed: 3,
  };
  const VALID_STATUS = Object.keys(STATUS).reduce((acc, key) => {
    acc[key] = true;
    return acc;
  }, {});

  const CORE_QUEST_PACKS = [
    "assets/data/quests/quest_main_story.json",
    "assets/data/quests/quest_side_stories.json",
    "assets/data/quests/quest_generated_placeholders.json",
  ];
  const CONTENT_QUEST_PACKS = [
    "assets/data/quests/quest_content_main_normalized.json",
    "assets/data/quests/quest_content_mini_normalized.json",
  ];

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
    if (id > 0 && $gameSwitches) {
      $gameSwitches.setValue(id, !!value);
    }
  };

  const setVariable = (variableId, value) => {
    const id = toInt(variableId, 0);
    if (id > 0 && $gameVariables) {
      $gameVariables.setValue(id, value);
    }
  };

  const loadTextSync = (relativePath) => {
    if (typeof require === "function" && Utils && Utils.isNwjs()) {
      const fs = require("fs");
      const path = require("path");
      const root = path.dirname(process.mainModule.filename);
      const fullPath = path.join(root, relativePath);
      if (!fs.existsSync(fullPath)) {
        throw new Error(`Missing file: ${relativePath}`);
      }
      return fs.readFileSync(fullPath, "utf8");
    }

    const xhr = new XMLHttpRequest();
    xhr.open("GET", relativePath, false);
    xhr.overrideMimeType("application/json");
    xhr.send();
    if (xhr.status >= 400) {
      throw new Error(`HTTP ${xhr.status}: ${relativePath}`);
    }
    return xhr.responseText;
  };

  const loadJsonSync = (relativePath) => {
    const text = stripBom(loadTextSync(relativePath));
    return JSON.parse(text);
  };

  let questRuntime = {
    ready: false,
    questById: {},
    questIds: [],
    packMeta: [],
    errors: [],
    warnings: [],
  };

  const activeQuestPackList = () =>
    includeContentPacks
      ? CORE_QUEST_PACKS.concat(CONTENT_QUEST_PACKS)
      : CORE_QUEST_PACKS.slice();

  const logWarnings = (warnings) => {
    if (!warnings.length) return;
    console.warn(`[${pluginName}] Quest load warnings:`);
    for (const line of warnings) {
      console.warn(`[${pluginName}] ${line}`);
    }
  };

  const logErrors = (errors) => {
    if (!errors.length) return;
    console.error(`[${pluginName}] Quest load errors:`);
    for (const line of errors) {
      console.error(`[${pluginName}] ${line}`);
    }
  };

  const buildQuestRuntime = () => {
    const warnings = [];
    const errors = [];
    const questById = {};
    const packMeta = [];
    const questPacks = activeQuestPackList();

    for (const packPath of questPacks) {
      let data = null;
      try {
        data = loadJsonSync(packPath);
      } catch (err) {
        errors.push(`${packPath}: ${err.message || String(err)}`);
        continue;
      }

      const packId =
        data && typeof data.id === "string" && data.id
          ? data.id
          : `PACK_${packPath}`;
      const quests = Array.isArray(data && data.quests) ? data.quests : [];
      packMeta.push({
        id: packId,
        path: packPath,
        count: quests.length,
      });

      for (let i = 0; i < quests.length; i += 1) {
        const quest = quests[i];
        if (!quest || typeof quest !== "object") {
          warnings.push(`${packPath} quests[${i}] is not an object; skipped`);
          continue;
        }
        const questId = quest.id;
        if (typeof questId !== "string" || !questId) {
          warnings.push(`${packPath} quests[${i}] missing string id; skipped`);
          continue;
        }
        if (questById[questId]) {
          warnings.push(
            `${packPath} duplicate quest id '${questId}' skipped (kept first)`
          );
          continue;
        }
        questById[questId] = deepClone(quest);
      }
    }

    const questIds = Object.keys(questById).sort();
    return {
      ready: questIds.length > 0,
      questById,
      questIds,
      packMeta,
      errors,
      warnings,
    };
  };

  const reloadQuestRuntime = () => {
    questRuntime = buildQuestRuntime();
    logWarnings(questRuntime.warnings);
    logErrors(questRuntime.errors);
    return questRuntime.ready;
  };

  const getQuest = (questId) =>
    typeof questId === "string" && questId ? questRuntime.questById[questId] : null;

  const listStringField = (obj, fieldName) => {
    if (!obj || typeof obj !== "object" || !Array.isArray(obj[fieldName])) {
      return [];
    }
    return obj[fieldName].filter((v) => typeof v === "string" && v);
  };

  const questSteps = (quest) => {
    if (!quest || !Array.isArray(quest.steps)) return [];
    return quest.steps.filter((s) => s && typeof s === "object");
  };

  const stepIdAt = (steps, index) => {
    const step = steps[index];
    if (!step) return 0;
    if (typeof step.id === "number") return Math.floor(step.id);
    return index + 1;
  };

  const stepIndexForId = (steps, stepId) => {
    for (let i = 0; i < steps.length; i += 1) {
      if (stepIdAt(steps, i) === stepId) return i;
    }
    return -1;
  };

  Game_System.prototype.chromaInitQuestData = function() {
    if (!this._chromaQuestState || typeof this._chromaQuestState !== "object") {
      this._chromaQuestState = {};
    }
    if (!this._chromaQuestFlags || typeof this._chromaQuestFlags !== "object") {
      this._chromaQuestFlags = {};
    } else if (Array.isArray(this._chromaQuestFlags)) {
      const migrated = {};
      for (const flagId of this._chromaQuestFlags) {
        if (typeof flagId === "string" && flagId) {
          migrated[flagId] = true;
        }
      }
      this._chromaQuestFlags = migrated;
    }
  };

  Game_System.prototype.chromaQuestStateMap = function() {
    this.chromaInitQuestData();
    return this._chromaQuestState;
  };

  Game_System.prototype.chromaQuestFlagsMap = function() {
    this.chromaInitQuestData();
    return this._chromaQuestFlags;
  };

  Game_System.prototype.chromaQuestFlag = function(flagId) {
    if (typeof flagId !== "string" || !flagId) return false;
    const flags = this.chromaQuestFlagsMap();
    return !!flags[flagId];
  };

  Game_System.prototype.chromaSetQuestFlag = function(flagId, value) {
    if (typeof flagId !== "string" || !flagId) return false;
    const flags = this.chromaQuestFlagsMap();
    if (value) {
      flags[flagId] = true;
      return true;
    }
    delete flags[flagId];
    return true;
  };

  Game_System.prototype.chromaQuestFlagIds = function() {
    const flags = this.chromaQuestFlagsMap();
    return Object.keys(flags).sort();
  };

  Game_System.prototype.chromaEnsureQuestRecord = function(questId) {
    if (typeof questId !== "string" || !questId) return null;
    this.chromaInitQuestData();
    const map = this._chromaQuestState;
    if (!map[questId] || typeof map[questId] !== "object") {
      map[questId] = {
        status: "locked",
        stepId: 0,
        updatedAt: Date.now(),
      };
    }
    const rec = map[questId];
    if (!VALID_STATUS[rec.status]) rec.status = "locked";
    rec.stepId = toInt(rec.stepId, 0);
    if (rec.stepId < 0) rec.stepId = 0;
    return rec;
  };

  Game_System.prototype.chromaQuestStatus = function(questId) {
    const rec = this.chromaEnsureQuestRecord(questId);
    return rec ? rec.status : "locked";
  };

  Game_System.prototype.chromaQuestStep = function(questId) {
    const rec = this.chromaEnsureQuestRecord(questId);
    return rec ? rec.stepId : 0;
  };

  Game_System.prototype.chromaSetQuestStatus = function(questId, status) {
    if (!VALID_STATUS[status]) return false;
    const rec = this.chromaEnsureQuestRecord(questId);
    if (!rec) return false;
    rec.status = status;
    rec.updatedAt = Date.now();
    return true;
  };

  Game_System.prototype.chromaSetQuestStep = function(questId, stepId) {
    const quest = getQuest(questId);
    if (!quest) return false;
    const nextStepId = toInt(stepId, 0);
    if (nextStepId <= 0) return false;
    const steps = questSteps(quest);
    if (!steps.length) return false;
    if (stepIndexForId(steps, nextStepId) < 0) return false;
    const rec = this.chromaEnsureQuestRecord(questId);
    if (!rec) return false;
    rec.stepId = nextStepId;
    rec.updatedAt = Date.now();
    if (rec.status === "locked") rec.status = "active";
    return true;
  };

  Game_System.prototype.chromaIsQuestComplete = function(questId) {
    return this.chromaQuestStatus(questId) === "completed";
  };

  Game_System.prototype.chromaIsQuestAvailable = function(questId) {
    const quest = getQuest(questId);
    if (!quest) return false;
    const prereqQuests = listStringField(quest, "prerequisites");
    for (const depId of prereqQuests) {
      if (!this.chromaIsQuestComplete(depId)) {
        return false;
      }
    }
    const prereqFlags = listStringField(quest, "prerequisite_flags");
    for (const flagId of prereqFlags) {
      if (!this.chromaQuestFlag(flagId)) {
        return false;
      }
    }
    return true;
  };

  Game_System.prototype.chromaApplyQuestCompletionFlags = function(questId) {
    const quest = getQuest(questId);
    if (!quest) return false;

    for (const flagId of listStringField(quest, "flags_set")) {
      this.chromaSetQuestFlag(flagId, true);
    }
    for (const flagId of listStringField(quest, "unlock_flags")) {
      this.chromaSetQuestFlag(flagId, true);
    }
    const rewards = quest.rewards;
    if (rewards && typeof rewards === "object") {
      for (const flagId of listStringField(rewards, "unlock_flags")) {
        this.chromaSetQuestFlag(flagId, true);
      }
    }
    return true;
  };

  Game_System.prototype.chromaStartQuest = function(questId, force) {
    const quest = getQuest(questId);
    if (!quest) return false;
    if (!force && !this.chromaIsQuestAvailable(questId)) {
      return false;
    }
    const steps = questSteps(quest);
    if (!steps.length) return false;
    const rec = this.chromaEnsureQuestRecord(questId);
    if (!rec) return false;
    if (rec.status === "completed") return false;
    rec.status = "active";
    if (rec.stepId <= 0 || stepIndexForId(steps, rec.stepId) < 0) {
      rec.stepId = stepIdAt(steps, 0);
    }
    rec.updatedAt = Date.now();
    return true;
  };

  Game_System.prototype.chromaAdvanceQuest = function(questId) {
    const quest = getQuest(questId);
    if (!quest) return false;
    const steps = questSteps(quest);
    if (!steps.length) return false;

    const rec = this.chromaEnsureQuestRecord(questId);
    if (!rec) return false;
    if (rec.status === "locked") {
      if (!this.chromaStartQuest(questId, false)) return false;
    }
    if (rec.status === "completed" || rec.status === "failed") return false;
    rec.status = "active";

    let index = stepIndexForId(steps, rec.stepId);
    if (index < 0) {
      rec.stepId = stepIdAt(steps, 0);
      rec.updatedAt = Date.now();
      return true;
    }

    if (index >= steps.length - 1) {
      return this.chromaCompleteQuest(questId);
    }

    index += 1;
    rec.stepId = stepIdAt(steps, index);
    rec.updatedAt = Date.now();
    return true;
  };

  Game_System.prototype.chromaCompleteQuest = function(questId) {
    const quest = getQuest(questId);
    if (!quest) return false;
    const rec = this.chromaEnsureQuestRecord(questId);
    if (!rec) return false;
    const steps = questSteps(quest);
    if (steps.length > 0) {
      rec.stepId = stepIdAt(steps, steps.length - 1);
    }
    rec.status = "completed";
    rec.updatedAt = Date.now();
    this.chromaApplyQuestCompletionFlags(questId);
    return true;
  };

  Game_System.prototype.chromaFailQuest = function(questId) {
    const rec = this.chromaEnsureQuestRecord(questId);
    if (!rec) return false;
    rec.status = "failed";
    rec.updatedAt = Date.now();
    return true;
  };

  Game_System.prototype.chromaResetQuest = function(questId) {
    const rec = this.chromaEnsureQuestRecord(questId);
    if (!rec) return false;
    rec.status = "locked";
    rec.stepId = 0;
    rec.updatedAt = Date.now();
    return true;
  };

  Game_System.prototype.chromaQuestSummary = function(questId) {
    const quest = getQuest(questId);
    if (!quest) return null;
    const rec = this.chromaEnsureQuestRecord(questId);
    return {
      id: questId,
      name: quest.name || questId,
      type: quest.type || "unknown",
      zone: quest.zone || "",
      act: quest.act,
      status: rec.status,
      stepId: rec.stepId,
      prerequisites: listStringField(quest, "prerequisites"),
      prerequisite_flags: listStringField(quest, "prerequisite_flags"),
      unlocks: listStringField(quest, "unlocks"),
      unlock_flags: listStringField(quest, "unlock_flags"),
      description: quest.description || "",
    };
  };

  const _Game_System_initialize = Game_System.prototype.initialize;
  Game_System.prototype.initialize = function() {
    _Game_System_initialize.call(this);
    this.chromaInitQuestData();
  };

  const _DataManager_extractSaveContents = DataManager.extractSaveContents;
  DataManager.extractSaveContents = function(contents) {
    _DataManager_extractSaveContents.call(this, contents);
    if ($gameSystem && $gameSystem.chromaInitQuestData) {
      $gameSystem.chromaInitQuestData();
    }
  };

  PluginManager.registerCommand(pluginName, "ReloadQuestData", (args) => {
    const ok = reloadQuestRuntime();
    setSwitch(args.switchId, ok);
    setVariable(args.variableId, questRuntime.questIds.length);
  });

  PluginManager.registerCommand(pluginName, "StartQuest", (args) => {
    const ok = $gameSystem.chromaStartQuest(args.questId, toBool(args.force));
    setSwitch(args.switchId, ok);
  });

  PluginManager.registerCommand(pluginName, "AdvanceQuest", (args) => {
    const ok = $gameSystem.chromaAdvanceQuest(args.questId);
    setSwitch(args.switchId, ok);
  });

  PluginManager.registerCommand(pluginName, "CompleteQuest", (args) => {
    const ok = $gameSystem.chromaCompleteQuest(args.questId);
    setSwitch(args.switchId, ok);
  });

  PluginManager.registerCommand(pluginName, "FailQuest", (args) => {
    const ok = $gameSystem.chromaFailQuest(args.questId);
    setSwitch(args.switchId, ok);
  });

  PluginManager.registerCommand(pluginName, "SetQuestStep", (args) => {
    const ok = $gameSystem.chromaSetQuestStep(args.questId, args.stepId);
    setSwitch(args.switchId, ok);
  });

  PluginManager.registerCommand(pluginName, "GetQuestStatus", (args) => {
    const status = $gameSystem.chromaQuestStatus(args.questId);
    setVariable(args.variableId, STATUS[status] == null ? STATUS.locked : STATUS[status]);
  });

  PluginManager.registerCommand(pluginName, "GetQuestStep", (args) => {
    setVariable(args.variableId, $gameSystem.chromaQuestStep(args.questId));
  });

  PluginManager.registerCommand(pluginName, "CheckQuestAvailable", (args) => {
    const value = $gameSystem.chromaIsQuestAvailable(args.questId);
    setSwitch(args.switchId, value);
  });

  PluginManager.registerCommand(pluginName, "CheckQuestComplete", (args) => {
    const value = $gameSystem.chromaIsQuestComplete(args.questId);
    setSwitch(args.switchId, value);
  });

  PluginManager.registerCommand(pluginName, "SetQuestFlag", (args) => {
    $gameSystem.chromaSetQuestFlag(args.flagId, toBool(args.value));
  });

  const g = typeof window !== "undefined" ? window : globalThis;
  g.Imported = g.Imported || {};
  g.Imported.ChromaEdge_QuestSystem = true;
  g.ChromaEdge = g.ChromaEdge || {};

  g.ChromaEdge.Quests = {
    ready() {
      return questRuntime.ready;
    },
    ids() {
      return questRuntime.questIds.slice();
    },
    count() {
      return questRuntime.questIds.length;
    },
    get(questId) {
      const quest = getQuest(questId);
      return quest ? deepClone(quest) : null;
    },
    getSummary(questId) {
      if (!$gameSystem || !$gameSystem.chromaQuestSummary) return null;
      return $gameSystem.chromaQuestSummary(questId);
    },
    packs() {
      return deepClone(questRuntime.packMeta);
    },
    loadErrors() {
      return questRuntime.errors.slice();
    },
    loadWarnings() {
      return questRuntime.warnings.slice();
    },
    reload() {
      return reloadQuestRuntime();
    },
    status(questId) {
      return $gameSystem ? $gameSystem.chromaQuestStatus(questId) : "locked";
    },
    statusCode(questId) {
      const key = this.status(questId);
      return STATUS[key] == null ? STATUS.locked : STATUS[key];
    },
    step(questId) {
      return $gameSystem ? $gameSystem.chromaQuestStep(questId) : 0;
    },
    isAvailable(questId) {
      return $gameSystem ? $gameSystem.chromaIsQuestAvailable(questId) : false;
    },
    isComplete(questId) {
      return $gameSystem ? $gameSystem.chromaIsQuestComplete(questId) : false;
    },
    start(questId, force = false) {
      return $gameSystem ? $gameSystem.chromaStartQuest(questId, !!force) : false;
    },
    advance(questId) {
      return $gameSystem ? $gameSystem.chromaAdvanceQuest(questId) : false;
    },
    complete(questId) {
      return $gameSystem ? $gameSystem.chromaCompleteQuest(questId) : false;
    },
    fail(questId) {
      return $gameSystem ? $gameSystem.chromaFailQuest(questId) : false;
    },
    setStep(questId, stepId) {
      return $gameSystem ? $gameSystem.chromaSetQuestStep(questId, stepId) : false;
    },
    reset(questId) {
      return $gameSystem ? $gameSystem.chromaResetQuest(questId) : false;
    },
    setFlag(flagId, value = true) {
      return $gameSystem ? $gameSystem.chromaSetQuestFlag(flagId, !!value) : false;
    },
    flag(flagId) {
      return $gameSystem ? $gameSystem.chromaQuestFlag(flagId) : false;
    },
    flags() {
      return $gameSystem ? $gameSystem.chromaQuestFlagIds() : [];
    },
  };

  if (loadOnBoot) {
    reloadQuestRuntime();
  }
})();
