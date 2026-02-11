/*:
 * @target MZ
 * @plugindesc v0.2.0 Quest Journal UI (menu command, filters, list, detail pane).
 * @author Chroma's Edge
 * @help
 * Provides an in-game quest journal scene backed by ChromaEdge_QuestSystem.
 *
 * Features:
 * - Menu command entry (optional)
 * - Filter tabs: Active, Available, Completed, Failed, All
 * - Quest list + detail pane
 * - Plugin command to open journal from events
 *
 * Script call:
 *   ChromaEdge.QuestJournal.open()
 *
 * @param showMenuCommand
 * @text Show Menu Command
 * @type boolean
 * @default true
 *
 * @param menuCommandName
 * @text Menu Command Name
 * @type string
 * @default Quests
 *
 * @param defaultFilter
 * @text Default Filter
 * @type select
 * @option Active
 * @value active
 * @option Available
 * @value available
 * @option Completed
 * @value completed
 * @option Failed
 * @value failed
 * @option All
 * @value all
 * @default active
 *
 * @command OpenQuestJournal
 * @text Open Quest Journal
 * @desc Open the quest journal scene.
 */

(() => {
  "use strict";

  const pluginName = "ChromaEdge_QuestJournal";
  const params = PluginManager.parameters(pluginName);
  const showMenuCommand =
    String(params.showMenuCommand || "true").toLowerCase() === "true";
  const menuCommandName = String(params.menuCommandName || "Quests");
  const defaultFilter = String(params.defaultFilter || "active");
  const MENU_SYMBOL = "chromaQuestJournal";
  const FILTERS = ["active", "available", "completed", "failed", "all"];

  const statusText = (entry) => {
    if (!entry) return "Unknown";
    if (entry.status === "locked" && entry.available) return "Available";
    switch (entry.status) {
      case "active":
        return "Active";
      case "completed":
        return "Completed";
      case "failed":
        return "Failed";
      default:
        return "Locked";
    }
  };

  const statusColor = (entry) => {
    if (!entry) return ColorManager.normalColor();
    const isAvailableLocked = entry.status === "locked" && entry.available;
    if (entry.status === "active") return ColorManager.systemColor();
    if (isAvailableLocked) return ColorManager.textColor(14);
    if (entry.status === "completed") return ColorManager.powerUpColor();
    if (entry.status === "failed") return ColorManager.deathColor();
    return ColorManager.normalColor();
  };

  const statusCodeShort = (entry) => {
    if (!entry) return "--";
    if (entry.status === "locked" && entry.available) return "NEW";
    switch (entry.status) {
      case "active":
        return "ACT";
      case "completed":
        return "CLR";
      case "failed":
        return "FAL";
      default:
        return "LOC";
    }
  };

  const questApi = () => {
    const g = typeof window !== "undefined" ? window : globalThis;
    const api = g && g.ChromaEdge ? g.ChromaEdge.Quests : null;
    return api || null;
  };

  const hasQuestRuntime = () => {
    const api = questApi();
    return !!(api && typeof api.ready === "function" && api.ready());
  };

  const isFilterSymbol = (symbol) => FILTERS.includes(symbol);

  const questTypeRank = (type) => {
    switch (type) {
      case "main":
        return 0;
      case "character":
        return 1;
      case "side":
        return 2;
      case "bounty":
        return 3;
      default:
        return 4;
    }
  };

  const statusRank = (entry) => {
    if (!entry) return 99;
    if (entry.status === "active") return 0;
    if (entry.status === "locked" && entry.available) return 1;
    if (entry.status === "locked") return 2;
    if (entry.status === "completed") return 3;
    if (entry.status === "failed") return 4;
    return 5;
  };

  const matchesFilter = (entry, filterSymbol) => {
    switch (filterSymbol) {
      case "active":
        return entry.status === "active";
      case "available":
        return entry.status === "locked" && entry.available;
      case "completed":
        return entry.status === "completed";
      case "failed":
        return entry.status === "failed";
      case "all":
      default:
        return true;
    }
  };

  const buildEntries = (filterSymbol) => {
    const api = questApi();
    if (!api || typeof api.ids !== "function" || typeof api.getSummary !== "function") {
      return [];
    }

    const ids = api.ids();
    const entries = [];
    for (const questId of ids) {
      const summary = api.getSummary(questId);
      if (!summary) continue;
      const quest = typeof api.get === "function" ? api.get(questId) : null;
      const available =
        summary.status === "locked" && typeof api.isAvailable === "function"
          ? !!api.isAvailable(questId)
          : false;
      const entry = {
        id: questId,
        summary,
        quest,
        status: summary.status || "locked",
        available,
      };
      if (matchesFilter(entry, filterSymbol)) {
        entries.push(entry);
      }
    }

    entries.sort((a, b) => {
      const sr = statusRank(a) - statusRank(b);
      if (sr !== 0) return sr;
      const ta = questTypeRank((a.summary && a.summary.type) || "");
      const tb = questTypeRank((b.summary && b.summary.type) || "");
      if (ta !== tb) return ta - tb;
      const aa = (a.summary && a.summary.act) || 999;
      const bb = (b.summary && b.summary.act) || 999;
      if (aa !== bb) return aa < bb ? -1 : 1;
      const an = ((a.summary && a.summary.name) || a.id).toLowerCase();
      const bn = ((b.summary && b.summary.name) || b.id).toLowerCase();
      if (an < bn) return -1;
      if (an > bn) return 1;
      return 0;
    });

    return entries;
  };

  const findCurrentStep = (entry) => {
    if (!entry || !entry.quest || !Array.isArray(entry.quest.steps)) {
      return null;
    }
    const steps = entry.quest.steps.filter((s) => s && typeof s === "object");
    if (!steps.length) return null;

    const stepId = Number(entry.summary ? entry.summary.stepId : 0);
    let index = -1;
    if (Number.isFinite(stepId) && stepId > 0) {
      index = steps.findIndex((s, i) => {
        const sid = Number.isFinite(Number(s.id)) ? Number(s.id) : i + 1;
        return sid === stepId;
      });
    }
    if (index < 0) {
      index = entry.status === "completed" ? steps.length - 1 : 0;
    }

    const step = steps[index];
    const stepNumber = Number.isFinite(Number(step.id)) ? Number(step.id) : index + 1;
    return {
      step,
      index,
      stepNumber,
      total: steps.length,
    };
  };

  const normalizeActText = (actValue) => {
    if (actValue === undefined || actValue === null || actValue === "") return "-";
    if (actValue === "post_game") return "Post-Game";
    return String(actValue);
  };

  function Window_QuestJournalFilter() {
    this.initialize(...arguments);
  }

  Window_QuestJournalFilter.prototype = Object.create(Window_Command.prototype);
  Window_QuestJournalFilter.prototype.constructor = Window_QuestJournalFilter;

  Window_QuestJournalFilter.prototype.maxCols = function() {
    return 5;
  };

  Window_QuestJournalFilter.prototype.makeCommandList = function() {
    this.addCommand("Active", "active");
    this.addCommand("Available", "available");
    this.addCommand("Completed", "completed");
    this.addCommand("Failed", "failed");
    this.addCommand("All", "all");
  };

  Window_QuestJournalFilter.prototype.setCurrentFilter = function(symbol) {
    const target = isFilterSymbol(symbol) ? symbol : "active";
    const index = this.findSymbol(target);
    if (index >= 0) this.select(index);
  };

  function Window_QuestJournalList() {
    this.initialize(...arguments);
  }

  Window_QuestJournalList.prototype = Object.create(Window_Selectable.prototype);
  Window_QuestJournalList.prototype.constructor = Window_QuestJournalList;

  Window_QuestJournalList.prototype.initialize = function(rect) {
    Window_Selectable.prototype.initialize.call(this, rect);
    this._items = [];
    this._filterSymbol = isFilterSymbol(defaultFilter) ? defaultFilter : "active";
    this._detailWindow = null;
    this.refresh();
    this.select(0);
  };

  Window_QuestJournalList.prototype.maxItems = function() {
    return this._items.length;
  };

  Window_QuestJournalList.prototype.item = function() {
    return this._items[this.index()] || null;
  };

  Window_QuestJournalList.prototype.setFilterSymbol = function(symbol) {
    const nextSymbol = isFilterSymbol(symbol) ? symbol : "all";
    if (this._filterSymbol !== nextSymbol) {
      this._filterSymbol = nextSymbol;
      this.refresh();
      this.select(0);
    } else {
      this.updateDetail();
      this.updateHelp();
    }
  };

  Window_QuestJournalList.prototype.setDetailWindow = function(detailWindow) {
    this._detailWindow = detailWindow;
    this.updateDetail();
  };

  Window_QuestJournalList.prototype.refresh = function() {
    this._items = buildEntries(this._filterSymbol);
    Window_Selectable.prototype.refresh.call(this);
  };

  Window_QuestJournalList.prototype.drawItem = function(index) {
    const entry = this._items[index];
    if (!entry) return;
    const rect = this.itemLineRect(index);
    const statusWidth = 58;

    this.resetTextColor();
    this.changeTextColor(statusColor(entry));
    this.drawText(statusCodeShort(entry), rect.x, rect.y, statusWidth, "left");

    this.changeTextColor(ColorManager.normalColor());
    const name = (entry.summary && entry.summary.name) || entry.id;
    this.drawText(name, rect.x + statusWidth, rect.y, rect.width - statusWidth, "left");
  };

  Window_QuestJournalList.prototype.select = function(index) {
    Window_Selectable.prototype.select.call(this, index);
    this.updateDetail();
    this.updateHelp();
  };

  Window_QuestJournalList.prototype.updateDetail = function() {
    if (this._detailWindow) {
      this._detailWindow.setEntry(this.item());
    }
  };

  Window_QuestJournalList.prototype.updateHelp = function() {
    if (!this._helpWindow) return;
    if (!hasQuestRuntime()) {
      this._helpWindow.setText("Quest runtime unavailable. Enable ChromaEdge_QuestSystem.");
      return;
    }
    const entry = this.item();
    if (!entry) {
      this._helpWindow.setText("No quests in this filter.");
      return;
    }
    const desc = (entry.summary && entry.summary.description) || "";
    const stat = statusText(entry);
    this._helpWindow.setText(`${stat}: ${desc}`);
  };

  function Window_QuestJournalDetail() {
    this.initialize(...arguments);
  }

  Window_QuestJournalDetail.prototype = Object.create(Window_Base.prototype);
  Window_QuestJournalDetail.prototype.constructor = Window_QuestJournalDetail;

  Window_QuestJournalDetail.prototype.initialize = function(rect) {
    Window_Base.prototype.initialize.call(this, rect);
    this._entry = null;
    this.refresh();
  };

  Window_QuestJournalDetail.prototype.setEntry = function(entry) {
    this._entry = entry || null;
    this.refresh();
  };

  Window_QuestJournalDetail.prototype.refresh = function() {
    this.contents.clear();
    const entry = this._entry;
    if (!entry) {
      this.drawText("Select a quest to view details.", 0, 0, this.innerWidth, "left");
      return;
    }

    const lh = this.lineHeight();
    let y = 0;
    const width = this.innerWidth;
    const name = (entry.summary && entry.summary.name) || entry.id;
    const type = (entry.summary && entry.summary.type) || "unknown";
    const zone = (entry.summary && entry.summary.zone) || "-";
    const act = normalizeActText(entry.summary ? entry.summary.act : "");

    this.changeTextColor(ColorManager.systemColor());
    this.drawText(name, 0, y, width, "left");
    y += lh;

    this.changeTextColor(statusColor(entry));
    this.drawText(statusText(entry), 0, y, 180, "left");
    this.changeTextColor(ColorManager.normalColor());
    this.drawText(`Type: ${type}`, 180, y, width - 180, "left");
    y += lh;

    this.drawText(`Zone: ${zone}`, 0, y, Math.floor(width / 2), "left");
    this.drawText(`Act: ${act}`, Math.floor(width / 2), y, width - Math.floor(width / 2), "left");
    y += lh;

    this.changePaintOpacity(false);
    this.contents.fillRect(0, y + Math.floor(lh / 2), width, 1, ColorManager.normalColor());
    this.changePaintOpacity(true);
    y += lh;

    const description = (entry.summary && entry.summary.description) || "";
    y = this.drawWrappedText(description, 0, y, width);
    y += 4;

    const stepInfo = findCurrentStep(entry);
    if (stepInfo && stepInfo.step) {
      this.changeTextColor(ColorManager.systemColor());
      this.drawText(
        `Step ${stepInfo.stepNumber}/${stepInfo.total}`,
        0,
        y,
        width,
        "left"
      );
      y += lh;
      this.changeTextColor(ColorManager.normalColor());

      const stepName = stepInfo.step.name || stepInfo.step.description || "Objective";
      y = this.drawWrappedText(stepName, 0, y, width);

      const objective = stepInfo.step.description || "";
      if (objective && objective !== stepName) {
        y = this.drawWrappedText(objective, 0, y, width);
      }

      const targetParts = [];
      if (stepInfo.step.target_location) {
        targetParts.push(`Location: ${stepInfo.step.target_location}`);
      }
      if (stepInfo.step.target_npc) {
        targetParts.push(`NPC: ${stepInfo.step.target_npc}`);
      }
      if (targetParts.length > 0) {
        y += 4;
        for (const line of targetParts) {
          this.drawText(line, 0, y, width, "left");
          y += lh;
        }
      }
    } else {
      this.changeTextColor(ColorManager.normalColor());
      this.drawText("No step data available.", 0, y, width, "left");
    }
  };

  Window_QuestJournalDetail.prototype.drawWrappedText = function(text, x, y, width) {
    const lh = this.lineHeight();
    const source = String(text || "").replace(/\r/g, "");
    if (!source) return y + lh;

    const paragraphs = source.split("\n");
    for (let pIndex = 0; pIndex < paragraphs.length; pIndex += 1) {
      const paragraph = paragraphs[pIndex].trim();
      if (!paragraph) {
        y += lh;
        continue;
      }

      const words = paragraph.split(/\s+/);
      let line = "";
      for (const word of words) {
        const next = line ? `${line} ${word}` : word;
        if (this.textWidth(next) <= width || !line) {
          line = next;
        } else {
          this.drawText(line, x, y, width, "left");
          y += lh;
          line = word;
        }
      }
      if (line) {
        this.drawText(line, x, y, width, "left");
        y += lh;
      }
    }
    return y;
  };

  function Scene_QuestJournal() {
    this.initialize(...arguments);
  }

  Scene_QuestJournal.prototype = Object.create(Scene_MenuBase.prototype);
  Scene_QuestJournal.prototype.constructor = Scene_QuestJournal;

  Scene_QuestJournal.prototype.initialize = function() {
    Scene_MenuBase.prototype.initialize.call(this);
  };

  Scene_QuestJournal.prototype.helpAreaHeight = function() {
    return this.calcWindowHeight(2, false);
  };

  Scene_QuestJournal.prototype.create = function() {
    Scene_MenuBase.prototype.create.call(this);
    this.createHelpWindow();
    this.createFilterWindow();
    this.createListWindow();
    this.createDetailWindow();
    this._filterWindow.deactivate();
    this._listWindow.activate();
  };

  Scene_QuestJournal.prototype.createFilterWindow = function() {
    const rect = this.filterWindowRect();
    this._filterWindow = new Window_QuestJournalFilter(rect);
    this._filterWindow.setCurrentFilter(
      isFilterSymbol(defaultFilter) ? defaultFilter : "active"
    );
    this._filterWindow.setHandler("ok", this.onFilterOk.bind(this));
    this._filterWindow.setHandler("cancel", this.popScene.bind(this));
    this.addWindow(this._filterWindow);
  };

  Scene_QuestJournal.prototype.createListWindow = function() {
    const rect = this.listWindowRect();
    this._listWindow = new Window_QuestJournalList(rect);
    this._listWindow.setHelpWindow(this._helpWindow);
    this._listWindow.setFilterSymbol(this._filterWindow.currentSymbol());
    this._listWindow.setHandler("ok", this.onListOk.bind(this));
    this._listWindow.setHandler("cancel", this.onListCancel.bind(this));
    this.addWindow(this._listWindow);
  };

  Scene_QuestJournal.prototype.createDetailWindow = function() {
    const rect = this.detailWindowRect();
    this._detailWindow = new Window_QuestJournalDetail(rect);
    this.addWindow(this._detailWindow);
    this._listWindow.setDetailWindow(this._detailWindow);
  };

  Scene_QuestJournal.prototype.filterWindowRect = function() {
    const wx = 0;
    const wy = this.mainAreaTop();
    const ww = Graphics.boxWidth;
    const wh = this.calcWindowHeight(1, true);
    return new Rectangle(wx, wy, ww, wh);
  };

  Scene_QuestJournal.prototype.listWindowRect = function() {
    const wx = 0;
    const wy = this._filterWindow.y + this._filterWindow.height;
    const ww = Math.floor(Graphics.boxWidth * 0.42);
    const wh = this.mainAreaBottom() - wy;
    return new Rectangle(wx, wy, ww, wh);
  };

  Scene_QuestJournal.prototype.detailWindowRect = function() {
    const listRect = this.listWindowRect();
    const wx = listRect.width;
    const wy = listRect.y;
    const ww = Graphics.boxWidth - listRect.width;
    const wh = listRect.height;
    return new Rectangle(wx, wy, ww, wh);
  };

  Scene_QuestJournal.prototype.onFilterOk = function() {
    this._listWindow.setFilterSymbol(this._filterWindow.currentSymbol());
    this._filterWindow.deactivate();
    this._listWindow.activate();
    this._listWindow.select(0);
  };

  Scene_QuestJournal.prototype.onListOk = function() {
    const item = this._listWindow.item();
    if (!item) {
      SoundManager.playBuzzer();
    } else {
      this._detailWindow.setEntry(item);
      this._listWindow.activate();
    }
  };

  Scene_QuestJournal.prototype.onListCancel = function() {
    this._listWindow.deactivate();
    this._filterWindow.activate();
  };

  const _Window_MenuCommand_addOriginalCommands =
    Window_MenuCommand.prototype.addOriginalCommands;
  Window_MenuCommand.prototype.addOriginalCommands = function() {
    _Window_MenuCommand_addOriginalCommands.call(this);
    if (!showMenuCommand) return;
    const enabled = !!questApi();
    this.addCommand(menuCommandName, MENU_SYMBOL, enabled);
  };

  const _Scene_Menu_createCommandWindow = Scene_Menu.prototype.createCommandWindow;
  Scene_Menu.prototype.createCommandWindow = function() {
    _Scene_Menu_createCommandWindow.call(this);
    this._commandWindow.setHandler(
      MENU_SYMBOL,
      this.commandChromaQuestJournal.bind(this)
    );
  };

  Scene_Menu.prototype.commandChromaQuestJournal = function() {
    SceneManager.push(Scene_QuestJournal);
  };

  PluginManager.registerCommand(pluginName, "OpenQuestJournal", () => {
    SceneManager.push(Scene_QuestJournal);
  });

  const g = typeof window !== "undefined" ? window : globalThis;
  g.Imported = g.Imported || {};
  g.Imported.ChromaEdge_QuestJournal = true;
  g.ChromaEdge = g.ChromaEdge || {};
  g.ChromaEdge.QuestJournal = {
    open() {
      SceneManager.push(Scene_QuestJournal);
    },
    sceneClass() {
      return Scene_QuestJournal;
    },
  };
})();
