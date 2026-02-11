/*:
 * @target MZ
 * @plugindesc v0.2.0 Branching dialogue runtime with conditions, flags, and scene UI.
 * @author Chroma's Edge
 * @help
 * Loads dialogue trees from canonical JSON packs and opens interactive dialogue scenes.
 *
 * Supported response condition keys:
 * - flag_set / flag_not_set
 * - switch_on / switch_off
 * - variable_gte / variable_lte / variable_eq
 * - quest_complete / quest_active / quest_available
 * - affinity_gte { actorIdA, actorIdB, value }
 * - all / any (array of nested condition objects)
 *
 * Script calls:
 *   ChromaEdge.DialogueTree.open("DT_AMARA_MAIN")
 *   ChromaEdge.DialogueTree.openNpc("NPC_SISTER_AMARA")
 *   ChromaEdge.DialogueTree.setFlag("SEEN_AMARA", true)
 *
 * @param loadOnBoot
 * @text Load On Boot
 * @type boolean
 * @default true
 *
 * @param autoHookAmbientEvents
 * @text Auto Hook Ambient Events
 * @type boolean
 * @default true
 * @desc If true, action-button events tagged with <chromaAmbientNpc:...> open dialogue trees.
 *
 * @param allowCancelClose
 * @text Allow Cancel To Close
 * @type boolean
 * @default true
 *
 * @command ReloadDialogueData
 * @text Reload Dialogue Data
 * @arg switchId
 * @text Success Switch
 * @type switch
 * @default 0
 * @arg variableId
 * @text Dialogue Count Variable
 * @type variable
 * @default 0
 *
 * @command OpenDialogueTree
 * @text Open Dialogue Tree
 * @arg dialogId
 * @type string
 * @default DT_AMARA_MAIN
 * @arg speaker
 * @type string
 * @default
 *
 * @command OpenNpcDialogue
 * @text Open NPC Dialogue
 * @arg npcId
 * @type string
 * @default NPC_SISTER_AMARA
 *
 * @command SetDialogueFlag
 * @text Set Dialogue Flag
 * @arg flagId
 * @type string
 * @default SAMPLE_FLAG
 * @arg value
 * @type boolean
 * @default true
 *
 * @command CheckDialogueFlag
 * @text Check Dialogue Flag
 * @arg flagId
 * @type string
 * @default SAMPLE_FLAG
 * @arg switchId
 * @type switch
 * @default 1
 */

(() => {
  "use strict";

  const pluginName = "ChromaEdge_DialogueTree";
  const params = PluginManager.parameters(pluginName);
  const loadOnBoot = String(params.loadOnBoot || "true").toLowerCase() === "true";
  const autoHookAmbientEvents =
    String(params.autoHookAmbientEvents || "true").toLowerCase() === "true";
  const allowCancelClose =
    String(params.allowCancelClose || "true").toLowerCase() === "true";

  const DIALOG_PACKS = [
    "assets/data/dialogs/dialog_npc_baseline.json",
    "assets/data/dialogs/dialog_ambient_banter_pack.json",
    "assets/data/dialogs/dialog_generated_placeholders.json",
  ];

  const NPC_DIRECTORY = "assets/data/npcs";

  const toInt = (value, fallback = 0) => {
    const parsed = Number(value);
    return Number.isFinite(parsed) ? Math.floor(parsed) : fallback;
  };

  const toBool = (value) =>
    String(value === undefined ? "" : value).toLowerCase() === "true";

  const stripBom = (text) =>
    text && text.charCodeAt(0) === 0xfeff ? text.slice(1) : text;

  const deepClone = (value) => JSON.parse(JSON.stringify(value));

  const setSwitch = (switchId, value) => {
    const id = toInt(switchId, 0);
    if (id > 0 && $gameSwitches) $gameSwitches.setValue(id, !!value);
  };

  const setVariable = (variableId, value) => {
    const id = toInt(variableId, 0);
    if (id > 0 && $gameVariables) $gameVariables.setValue(id, value);
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

  const loadNpcFilesSync = () => {
    const results = [];

    if (typeof require === "function" && Utils && Utils.isNwjs()) {
      const fs = require("fs");
      const path = require("path");
      const root = path.dirname(process.mainModule.filename);
      const fullDir = path.join(root, NPC_DIRECTORY);
      if (!fs.existsSync(fullDir)) return results;

      const files = fs
        .readdirSync(fullDir)
        .filter((f) => f.toLowerCase().endsWith(".json"))
        .sort();

      for (const fileName of files) {
        try {
          const raw = fs.readFileSync(path.join(fullDir, fileName), "utf8");
          results.push(JSON.parse(stripBom(raw)));
        } catch (err) {
          console.warn(`[${pluginName}] Failed loading NPC file ${fileName}:`, err);
        }
      }
      return results;
    }

    try {
      const idx = loadJsonSync("assets/data/npcs/npc_ambient_runtime_index.json");
      const byTown = Array.isArray(idx && idx.by_town) ? idx.by_town : [];
      for (const town of byTown) {
        const npcs = Array.isArray(town && town.npcs) ? town.npcs : [];
        for (const n of npcs) {
          if (!n || typeof n !== "object") continue;
          results.push({
            id: n.npc,
            name: n.name || n.npc,
            location: town.town_id || "",
            dialog_tree: n.dialog_tree || "",
            schedule: {
              day: n.day || null,
              night: n.night || null,
              rain: n.rain || null,
            },
          });
        }
      }
    } catch (_err) {
      // no-op fallback
    }

    return results;
  };

  const listToNodeMap = (nodes) => {
    const map = {};
    const items = Array.isArray(nodes) ? nodes : [];
    for (const node of items) {
      if (!node || typeof node !== "object") continue;
      const nodeId = String(node.id || "").trim();
      if (!nodeId) continue;
      map[nodeId] = {
        id: nodeId,
        text: String(node.text || ""),
        responses: Array.isArray(node.responses)
          ? node.responses.filter((r) => r && typeof r === "object")
          : [],
        actions: Array.isArray(node.actions)
          ? node.actions.filter((a) => a && typeof a === "object")
          : [],
      };
    }
    return map;
  };

  let runtime = {
    ready: false,
    dialogById: {},
    dialogIds: [],
    npcById: {},
    errors: [],
    warnings: [],
  };

  let switchNameIndex = null;

  const invalidateSwitchIndex = () => {
    switchNameIndex = null;
  };

  const buildSwitchIndex = () => {
    if (switchNameIndex) return switchNameIndex;
    switchNameIndex = {};
    if (!$dataSystem || !Array.isArray($dataSystem.switches)) return switchNameIndex;

    for (let i = 1; i < $dataSystem.switches.length; i += 1) {
      const name = String($dataSystem.switches[i] || "").trim();
      if (!name) continue;
      switchNameIndex[name] = i;
      switchNameIndex[name.toUpperCase()] = i;
    }
    return switchNameIndex;
  };

  const resolveSwitchId = (nameOrId) => {
    const asInt = toInt(nameOrId, 0);
    if (asInt > 0) return asInt;
    const key = String(nameOrId || "").trim();
    if (!key) return 0;
    const index = buildSwitchIndex();
    return toInt(index[key] || index[key.toUpperCase()] || 0, 0);
  };

  const dialogById = (dialogId) => {
    const id = String(dialogId || "").trim();
    return id ? runtime.dialogById[id] || null : null;
  };

  const npcById = (npcId) => {
    const id = String(npcId || "").trim();
    return id ? runtime.npcById[id] || null : null;
  };

  const questApi = () => {
    const g = typeof window !== "undefined" ? window : globalThis;
    return g && g.ChromaEdge ? g.ChromaEdge.Quests : null;
  };

  const isFlagSet = (flagId) => {
    const id = String(flagId || "").trim();
    if (!id) return false;

    if ($gameSystem && $gameSystem.chromaDialogueFlag) {
      if ($gameSystem.chromaDialogueFlag(id)) return true;
    }

    const q = questApi();
    if (q && typeof q.flag === "function" && q.flag(id)) {
      return true;
    }

    const switchId = resolveSwitchId(id);
    if (switchId > 0 && $gameSwitches) {
      return !!$gameSwitches.value(switchId);
    }

    return false;
  };

  const valueAsConditionObject = (value) =>
    value && typeof value === "object" ? value : null;

  const checkVariableClause = (clause, fn) => {
    const obj = valueAsConditionObject(clause);
    if (!obj) return false;
    const variableId = toInt(obj.id, 0);
    if (variableId <= 0 || !$gameVariables) return false;
    const lhs = Number($gameVariables.value(variableId));
    const rhs = Number(obj.value);
    if (!Number.isFinite(lhs) || !Number.isFinite(rhs)) return false;
    return fn(lhs, rhs);
  };

  const evaluateCondition = (condition) => {
    if (!condition || typeof condition !== "object") return true;

    if (Array.isArray(condition.all)) {
      for (const child of condition.all) {
        if (!evaluateCondition(child)) return false;
      }
    }

    if (Array.isArray(condition.any)) {
      const anyOk = condition.any.some((child) => evaluateCondition(child));
      if (!anyOk) return false;
    }

    if (condition.flag_set != null) {
      if (!isFlagSet(condition.flag_set)) return false;
    }

    if (condition.flag_not_set != null) {
      if (isFlagSet(condition.flag_not_set)) return false;
    }

    if (condition.switch_on != null) {
      const sid = resolveSwitchId(condition.switch_on);
      if (sid <= 0 || !$gameSwitches || !$gameSwitches.value(sid)) return false;
    }

    if (condition.switch_off != null) {
      const sid = resolveSwitchId(condition.switch_off);
      if (sid <= 0 || !$gameSwitches || !!$gameSwitches.value(sid)) return false;
    }

    if (condition.variable_gte != null) {
      if (!checkVariableClause(condition.variable_gte, (a, b) => a >= b)) return false;
    }

    if (condition.variable_lte != null) {
      if (!checkVariableClause(condition.variable_lte, (a, b) => a <= b)) return false;
    }

    if (condition.variable_eq != null) {
      if (!checkVariableClause(condition.variable_eq, (a, b) => a === b)) return false;
    }

    const q = questApi();
    if (condition.quest_complete != null) {
      const qid = String(condition.quest_complete || "").trim();
      if (!qid || !q || typeof q.isComplete !== "function" || !q.isComplete(qid)) {
        return false;
      }
    }

    if (condition.quest_active != null) {
      const qid = String(condition.quest_active || "").trim();
      if (!qid || !q || typeof q.status !== "function" || q.status(qid) !== "active") {
        return false;
      }
    }

    if (condition.quest_available != null) {
      const qid = String(condition.quest_available || "").trim();
      if (!qid || !q || typeof q.isAvailable !== "function" || !q.isAvailable(qid)) {
        return false;
      }
    }

    if (condition.affinity_gte != null) {
      const clause = valueAsConditionObject(condition.affinity_gte);
      if (!clause || !$gameSystem || !$gameSystem.chromaGetAffinity) return false;
      const a = toInt(clause.actorIdA, 0);
      const b = toInt(clause.actorIdB, 0);
      const value = toInt(clause.value, 0);
      if (a <= 0 || b <= 0) return false;
      if (toInt($gameSystem.chromaGetAffinity(a, b), 0) < value) return false;
    }

    return true;
  };

  const applyNodeActions = (actions) => {
    const list = Array.isArray(actions) ? actions : [];
    const q = questApi();

    for (const action of list) {
      if (!action || typeof action !== "object") continue;

      if (action.set_flag != null && $gameSystem && $gameSystem.chromaSetDialogueFlag) {
        $gameSystem.chromaSetDialogueFlag(action.set_flag, true);
      }

      if (action.clear_flag != null && $gameSystem && $gameSystem.chromaSetDialogueFlag) {
        $gameSystem.chromaSetDialogueFlag(action.clear_flag, false);
      }

      if (action.set_switch != null && $gameSwitches) {
        const sid = resolveSwitchId(action.set_switch);
        if (sid > 0) {
          const value = action.value == null ? true : !!action.value;
          $gameSwitches.setValue(sid, value);
        }
      }

      if (action.set_variable && typeof action.set_variable === "object" && $gameVariables) {
        const variableId = toInt(action.set_variable.id, 0);
        if (variableId > 0) {
          $gameVariables.setValue(variableId, action.set_variable.value);
        }
      }

      if (action.add_variable && typeof action.add_variable === "object" && $gameVariables) {
        const variableId = toInt(action.add_variable.id, 0);
        if (variableId > 0) {
          const current = Number($gameVariables.value(variableId)) || 0;
          const delta = Number(action.add_variable.delta) || 0;
          $gameVariables.setValue(variableId, current + delta);
        }
      }

      if (action.set_quest_flag && typeof action.set_quest_flag === "object") {
        if (q && typeof q.setFlag === "function") {
          const flagId = String(action.set_quest_flag.flag || "").trim();
          if (flagId) q.setFlag(flagId, action.set_quest_flag.value !== false);
        }
      }

      if (action.start_quest != null && q && typeof q.start === "function") {
        q.start(String(action.start_quest), !!action.force);
      }

      if (action.advance_quest != null && q && typeof q.advance === "function") {
        q.advance(String(action.advance_quest));
      }

      if (action.complete_quest != null && q && typeof q.complete === "function") {
        q.complete(String(action.complete_quest));
      }

      if (action.call_common_event != null && $gameTemp) {
        const ceId = toInt(action.call_common_event, 0);
        if (ceId > 0) $gameTemp.reserveCommonEvent(ceId);
      }
    }
  };

  const buildRuntime = () => {
    const dialogBy = {};
    const npcBy = {};
    const warnings = [];
    const errors = [];

    for (const packPath of DIALOG_PACKS) {
      let data = null;
      try {
        data = loadJsonSync(packPath);
      } catch (err) {
        errors.push(`${packPath}: ${err.message || String(err)}`);
        continue;
      }

      const dialogs = Array.isArray(data && data.dialogs) ? data.dialogs : [];
      for (let i = 0; i < dialogs.length; i += 1) {
        const dialog = dialogs[i];
        if (!dialog || typeof dialog !== "object") {
          warnings.push(`${packPath} dialogs[${i}] is not an object; skipped`);
          continue;
        }
        const dialogId = String(dialog.id || "").trim();
        if (!dialogId) {
          warnings.push(`${packPath} dialogs[${i}] missing id; skipped`);
          continue;
        }
        if (dialogBy[dialogId]) {
          warnings.push(`${packPath} duplicate dialog id '${dialogId}' skipped`);
          continue;
        }

        const nodes = listToNodeMap(dialog.nodes);
        const nodeIds = Object.keys(nodes);
        if (nodeIds.length <= 0) {
          warnings.push(`${packPath} dialog '${dialogId}' has no valid nodes`);
        }
        const startId =
          nodeIds.includes(String(dialog.start || "").trim()) && dialog.start
            ? String(dialog.start).trim()
            : nodeIds[0] || "";

        dialogBy[dialogId] = {
          id: dialogId,
          start: startId,
          nodes,
          packPath,
        };
      }
    }

    const npcs = loadNpcFilesSync();
    for (const npc of npcs) {
      if (!npc || typeof npc !== "object") continue;
      const npcId = String(npc.id || "").trim();
      if (!npcId) continue;

      npcBy[npcId] = {
        id: npcId,
        name: String(npc.name || npcId),
        location: String(npc.location || ""),
        dialogTree: String(npc.dialog_tree || "").trim(),
      };
    }

    const dialogIds = Object.keys(dialogBy).sort();
    return {
      ready: dialogIds.length > 0,
      dialogById: dialogBy,
      dialogIds,
      npcById: npcBy,
      warnings,
      errors,
    };
  };

  const reloadRuntime = () => {
    runtime = buildRuntime();
    invalidateSwitchIndex();

    if (runtime.warnings.length) {
      console.warn(`[${pluginName}] Dialogue load warnings:`);
      for (const line of runtime.warnings) {
        console.warn(`[${pluginName}] ${line}`);
      }
    }

    if (runtime.errors.length) {
      console.error(`[${pluginName}] Dialogue load errors:`);
      for (const line of runtime.errors) {
        console.error(`[${pluginName}] ${line}`);
      }
    }

    return runtime.ready;
  };

  Game_System.prototype.chromaInitDialogueData = function() {
    if (!this._chromaDialogueFlags || typeof this._chromaDialogueFlags !== "object") {
      this._chromaDialogueFlags = {};
    }
    if (!this._chromaDialogueVisited || typeof this._chromaDialogueVisited !== "object") {
      this._chromaDialogueVisited = {};
    }
  };

  Game_System.prototype.chromaDialogueFlag = function(flagId) {
    this.chromaInitDialogueData();
    const id = String(flagId || "").trim();
    if (!id) return false;
    return !!this._chromaDialogueFlags[id];
  };

  Game_System.prototype.chromaSetDialogueFlag = function(flagId, value) {
    this.chromaInitDialogueData();
    const id = String(flagId || "").trim();
    if (!id) return false;
    if (value) this._chromaDialogueFlags[id] = true;
    else delete this._chromaDialogueFlags[id];
    return true;
  };

  Game_System.prototype.chromaDialogueFlagIds = function() {
    this.chromaInitDialogueData();
    return Object.keys(this._chromaDialogueFlags).sort();
  };

  Game_System.prototype.chromaMarkDialogueVisited = function(dialogId, nodeId) {
    this.chromaInitDialogueData();
    const dId = String(dialogId || "").trim();
    const nId = String(nodeId || "").trim();
    if (!dId || !nId) return false;
    if (!this._chromaDialogueVisited[dId]) this._chromaDialogueVisited[dId] = {};
    this._chromaDialogueVisited[dId][nId] = true;
    return true;
  };

  Game_System.prototype.chromaHasVisitedDialogueNode = function(dialogId, nodeId) {
    this.chromaInitDialogueData();
    const dId = String(dialogId || "").trim();
    const nId = String(nodeId || "").trim();
    if (!dId || !nId) return false;
    return !!(
      this._chromaDialogueVisited[dId] && this._chromaDialogueVisited[dId][nId]
    );
  };

  const _Game_System_initialize = Game_System.prototype.initialize;
  Game_System.prototype.initialize = function() {
    _Game_System_initialize.call(this);
    this.chromaInitDialogueData();
  };

  const _DataManager_extractSaveContents = DataManager.extractSaveContents;
  DataManager.extractSaveContents = function(contents) {
    _DataManager_extractSaveContents.call(this, contents);
    if ($gameSystem && $gameSystem.chromaInitDialogueData) {
      $gameSystem.chromaInitDialogueData();
    }
  };

  function visibleResponses(node) {
    const list = Array.isArray(node && node.responses) ? node.responses : [];
    return list.filter((response) => {
      if (!response || typeof response !== "object") return false;
      if (!response.text || !response.next) return false;
      return evaluateCondition(response.show_if);
    });
  }

  let pendingPayload = null;

  const pushDialogueScene = (payload) => {
    pendingPayload = payload;
    SceneManager.push(Scene_ChromaDialogueTree);
  };

  function Window_DialogueTreeBody() {
    this.initialize(...arguments);
  }

  Window_DialogueTreeBody.prototype = Object.create(Window_Base.prototype);
  Window_DialogueTreeBody.prototype.constructor = Window_DialogueTreeBody;

  Window_DialogueTreeBody.prototype.initialize = function(rect) {
    Window_Base.prototype.initialize.call(this, rect);
    this._speaker = "";
    this._text = "";
    this.refresh();
  };

  Window_DialogueTreeBody.prototype.setContent = function(speaker, text) {
    const nextSpeaker = String(speaker || "");
    const nextText = String(text || "");
    if (nextSpeaker === this._speaker && nextText === this._text) return;
    this._speaker = nextSpeaker;
    this._text = nextText;
    this.refresh();
  };

  Window_DialogueTreeBody.prototype.refresh = function() {
    this.contents.clear();
    const speakerLine = this._speaker ? this._speaker : "Dialogue";
    this.changeTextColor(ColorManager.systemColor());
    this.drawText(speakerLine, 0, 0, this.innerWidth, "left");
    this.resetTextColor();
    this.drawTextEx(this._text || "...", 0, this.lineHeight());
  };

  function Window_DialogueTreeChoices() {
    this.initialize(...arguments);
  }

  Window_DialogueTreeChoices.prototype = Object.create(Window_Command.prototype);
  Window_DialogueTreeChoices.prototype.constructor = Window_DialogueTreeChoices;

  Window_DialogueTreeChoices.prototype.initialize = function(rect) {
    this._responses = [];
    Window_Command.prototype.initialize.call(this, rect);
    this.refresh();
    this.select(0);
  };

  Window_DialogueTreeChoices.prototype.maxCols = function() {
    return 1;
  };

  Window_DialogueTreeChoices.prototype.setResponses = function(responses) {
    this._responses = Array.isArray(responses) ? responses.slice() : [];
    this.refresh();
    this.select(0);
  };

  Window_DialogueTreeChoices.prototype.currentResponse = function() {
    return this.currentExt();
  };

  Window_DialogueTreeChoices.prototype.makeCommandList = function() {
    if (!this._responses.length) {
      this.addCommand("Close", "close", true, null);
      return;
    }
    for (const response of this._responses) {
      this.addCommand(String(response.text || "..."), "response", true, response);
    }
  };

  function Scene_ChromaDialogueTree() {
    this.initialize(...arguments);
  }

  Scene_ChromaDialogueTree.prototype = Object.create(Scene_MenuBase.prototype);
  Scene_ChromaDialogueTree.prototype.constructor = Scene_ChromaDialogueTree;

  Scene_ChromaDialogueTree.prototype.initialize = function() {
    Scene_MenuBase.prototype.initialize.call(this);
    this._payload = pendingPayload;
    pendingPayload = null;
    this._dialog = null;
    this._currentNode = null;
  };

  Scene_ChromaDialogueTree.prototype.create = function() {
    Scene_MenuBase.prototype.create.call(this);

    const payload = this._payload || {};
    this._dialog = dialogById(payload.dialogId);
    if (!this._dialog) {
      this.popScene();
      return;
    }

    this._dialogId = this._dialog.id;
    this._speaker = String(payload.speaker || payload.npcName || "");

    if (!this._speaker && payload.npcId) {
      const npc = npcById(payload.npcId);
      if (npc) this._speaker = npc.name;
    }

    this.createBodyWindow();
    this.createChoiceWindow();
    this.gotoNode(String(payload.nodeId || this._dialog.start || ""));
  };

  Scene_ChromaDialogueTree.prototype.createBodyWindow = function() {
    const top = this.mainAreaTop();
    const bodyHeight = this.calcWindowHeight(7, false);
    const rect = new Rectangle(0, top, Graphics.boxWidth, bodyHeight);
    this._bodyWindow = new Window_DialogueTreeBody(rect);
    this.addWindow(this._bodyWindow);
  };

  Scene_ChromaDialogueTree.prototype.createChoiceWindow = function() {
    const top = this._bodyWindow.y + this._bodyWindow.height;
    const lines = 6;
    const rect = new Rectangle(0, top, Graphics.boxWidth, this.calcWindowHeight(lines, true));
    this._choiceWindow = new Window_DialogueTreeChoices(rect);
    this._choiceWindow.setHandler("response", this.onChooseResponse.bind(this));
    this._choiceWindow.setHandler("close", this.popScene.bind(this));
    this._choiceWindow.setHandler("cancel", this.onChoiceCancel.bind(this));
    this.addWindow(this._choiceWindow);
    this._choiceWindow.activate();
  };

  Scene_ChromaDialogueTree.prototype.onChoiceCancel = function() {
    if (allowCancelClose) {
      this.popScene();
      return;
    }
    this._choiceWindow.activate();
  };

  Scene_ChromaDialogueTree.prototype.onChooseResponse = function() {
    const response = this._choiceWindow.currentResponse();
    if (!response || !response.next) {
      this.popScene();
      return;
    }
    this.gotoNode(String(response.next));
  };

  Scene_ChromaDialogueTree.prototype.gotoNode = function(nodeId) {
    if (!this._dialog || !this._dialog.nodes) {
      this.popScene();
      return;
    }

    const node = this._dialog.nodes[nodeId] || null;
    if (!node) {
      this.popScene();
      return;
    }

    this._currentNode = node;
    if ($gameSystem && $gameSystem.chromaMarkDialogueVisited) {
      $gameSystem.chromaMarkDialogueVisited(this._dialog.id, node.id);
    }

    applyNodeActions(node.actions);

    const speaker = this._speaker || "Dialogue";
    this._bodyWindow.setContent(speaker, String(node.text || ""));

    const responses = visibleResponses(node);
    this._choiceWindow.setResponses(responses);
    this._choiceWindow.activate();
  };

  const openDialogueTree = (dialogId, options = {}) => {
    const id = String(dialogId || "").trim();
    if (!id) return false;
    if (!runtime.ready) reloadRuntime();

    const dialog = dialogById(id);
    if (!dialog) return false;

    pushDialogueScene({
      dialogId: id,
      nodeId: options.nodeId || dialog.start,
      speaker: options.speaker || "",
      npcId: options.npcId || "",
      npcName: options.npcName || "",
    });
    return true;
  };

  const openNpcDialogue = (npcId, options = {}) => {
    const npc = npcById(npcId);
    if (!npc || !npc.dialogTree) return false;
    return openDialogueTree(npc.dialogTree, {
      nodeId: options.nodeId,
      speaker: options.speaker,
      npcId: npc.id,
      npcName: npc.name,
    });
  };

  const parseEventTag = (note, tagName) => {
    const re = new RegExp(`<\\s*${tagName}\\s*:\\s*([^>]+)\\s*>`, "i");
    const m = String(note || "").match(re);
    return m && m[1] ? String(m[1]).trim() : "";
  };

  const _Game_Event_start = Game_Event.prototype.start;
  Game_Event.prototype.start = function() {
    if (
      autoHookAmbientEvents &&
      SceneManager._scene instanceof Scene_Map &&
      this.isTriggerIn([0])
    ) {
      const ev = this.event();
      const note = ev ? ev.note || "" : "";
      const treeId =
        parseEventTag(note, "chromaDialogueTree") || parseEventTag(note, "chromaDialogTree");
      const npcId =
        parseEventTag(note, "chromaAmbientNpc") || parseEventTag(note, "chromaNpcId");

      let opened = false;
      if (treeId) {
        opened = openDialogueTree(treeId, {});
      } else if (npcId) {
        opened = openNpcDialogue(npcId, {});
      }

      if (opened) {
        return;
      }
    }

    _Game_Event_start.call(this);
  };

  PluginManager.registerCommand(pluginName, "ReloadDialogueData", (args) => {
    const ok = reloadRuntime();
    setSwitch(args.switchId, ok);
    setVariable(args.variableId, runtime.dialogIds.length);
  });

  PluginManager.registerCommand(pluginName, "OpenDialogueTree", (args) => {
    openDialogueTree(args.dialogId, { speaker: args.speaker });
  });

  PluginManager.registerCommand(pluginName, "OpenNpcDialogue", (args) => {
    openNpcDialogue(args.npcId, {});
  });

  PluginManager.registerCommand(pluginName, "SetDialogueFlag", (args) => {
    if ($gameSystem && $gameSystem.chromaSetDialogueFlag) {
      $gameSystem.chromaSetDialogueFlag(args.flagId, toBool(args.value));
    }
  });

  PluginManager.registerCommand(pluginName, "CheckDialogueFlag", (args) => {
    const value = isFlagSet(args.flagId);
    setSwitch(args.switchId, value);
  });

  const g = typeof window !== "undefined" ? window : globalThis;
  g.Imported = g.Imported || {};
  g.Imported.ChromaEdge_DialogueTree = true;
  g.ChromaEdge = g.ChromaEdge || {};

  g.ChromaEdge.DialogueTree = {
    ready() {
      return runtime.ready;
    },
    reload() {
      return reloadRuntime();
    },
    ids() {
      return runtime.dialogIds.slice();
    },
    get(dialogId) {
      const dialog = dialogById(dialogId);
      return dialog ? deepClone(dialog) : null;
    },
    resolveNpc(npcId) {
      const npc = npcById(npcId);
      return npc ? deepClone(npc) : null;
    },
    open(dialogId, options = {}) {
      return openDialogueTree(dialogId, options || {});
    },
    openNpc(npcId, options = {}) {
      return openNpcDialogue(npcId, options || {});
    },
    setFlag(flagId, value = true) {
      return $gameSystem ? $gameSystem.chromaSetDialogueFlag(flagId, !!value) : false;
    },
    flag(flagId) {
      return isFlagSet(flagId);
    },
    flags() {
      return $gameSystem && $gameSystem.chromaDialogueFlagIds
        ? $gameSystem.chromaDialogueFlagIds()
        : [];
    },
    hasVisited(dialogId, nodeId) {
      return $gameSystem && $gameSystem.chromaHasVisitedDialogueNode
        ? $gameSystem.chromaHasVisitedDialogueNode(dialogId, nodeId)
        : false;
    },
    evaluateCondition(condition) {
      return evaluateCondition(condition);
    },
    loadErrors() {
      return runtime.errors.slice();
    },
    loadWarnings() {
      return runtime.warnings.slice();
    },
  };

  if (loadOnBoot) {
    reloadRuntime();
  }
})();
