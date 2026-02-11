/*:
 * @target MZ
 * @plugindesc v0.2.0 Affinity relationship menu scene with pair list and detail panel.
 * @author Chroma's Edge
 * @help
 * Displays relationship affinity values between party members (or all known actors).
 *
 * Script call:
 *   ChromaEdge.AffinityMenu.open()
 *
 * @param showMenuCommand
 * @text Show Menu Command
 * @type boolean
 * @default true
 *
 * @param menuCommandName
 * @text Menu Command Name
 * @type string
 * @default Affinity
 *
 * @param includeAllKnownActors
 * @text Include All Database Actors
 * @type boolean
 * @default false
 *
 * @command OpenAffinityMenu
 * @text Open Affinity Menu
 */

(() => {
  "use strict";

  const pluginName = "ChromaEdge_AffinityMenu";
  const params = PluginManager.parameters(pluginName);
  const showMenuCommand =
    String(params.showMenuCommand || "true").toLowerCase() === "true";
  const menuCommandName = String(params.menuCommandName || "Affinity");
  const includeAllKnownActors =
    String(params.includeAllKnownActors || "false").toLowerCase() === "true";

  const MENU_SYMBOL = "chromaAffinityMenu";

  const uniqueSorted = (arr) => {
    const seen = new Set();
    const result = [];
    for (const v of arr) {
      const id = Number(v) || 0;
      if (id <= 0 || seen.has(id)) continue;
      seen.add(id);
      result.push(id);
    }
    result.sort((a, b) => a - b);
    return result;
  };

  const actorIdsForMenu = () => {
    if (includeAllKnownActors && Array.isArray($dataActors)) {
      const ids = [];
      for (let i = 1; i < $dataActors.length; i += 1) {
        if ($dataActors[i]) ids.push(i);
      }
      return uniqueSorted(ids);
    }

    if ($gameParty) {
      const ids = $gameParty.members().map((actor) => actor.actorId());
      return uniqueSorted(ids);
    }

    return [];
  };

  const affinityValue = (actorIdA, actorIdB) => {
    if ($gameSystem && $gameSystem.chromaGetAffinity) {
      return Number($gameSystem.chromaGetAffinity(actorIdA, actorIdB)) || 0;
    }
    return 0;
  };

  const canDual = (actorIdA, actorIdB) => {
    if ($gameSystem && $gameSystem.chromaCanDualLimit) {
      return !!$gameSystem.chromaCanDualLimit(actorIdA, actorIdB);
    }
    return false;
  };

  const buildPairEntries = () => {
    const ids = actorIdsForMenu();
    const entries = [];

    for (let i = 0; i < ids.length; i += 1) {
      for (let j = i + 1; j < ids.length; j += 1) {
        const aId = ids[i];
        const bId = ids[j];
        const actorA = $dataActors[aId];
        const actorB = $dataActors[bId];
        if (!actorA || !actorB) continue;

        const value = affinityValue(aId, bId);
        const dlbReady = canDual(aId, bId);

        entries.push({
          actorIdA: aId,
          actorIdB: bId,
          actorNameA: String(actorA.name || `Actor ${aId}`),
          actorNameB: String(actorB.name || `Actor ${bId}`),
          affinity: value,
          dualReady: dlbReady,
        });
      }
    }

    entries.sort((a, b) => {
      if (a.affinity !== b.affinity) return b.affinity - a.affinity;
      const an = `${a.actorNameA}+${a.actorNameB}`.toLowerCase();
      const bn = `${b.actorNameA}+${b.actorNameB}`.toLowerCase();
      if (an < bn) return -1;
      if (an > bn) return 1;
      return 0;
    });

    return entries;
  };

  function Window_AffinityPairList() {
    this.initialize(...arguments);
  }

  Window_AffinityPairList.prototype = Object.create(Window_Selectable.prototype);
  Window_AffinityPairList.prototype.constructor = Window_AffinityPairList;

  Window_AffinityPairList.prototype.initialize = function(rect) {
    Window_Selectable.prototype.initialize.call(this, rect);
    this._entries = [];
    this.refresh();
    this.select(0);
  };

  Window_AffinityPairList.prototype.maxItems = function() {
    return this._entries.length;
  };

  Window_AffinityPairList.prototype.item = function() {
    const index = this.index();
    return index >= 0 ? this._entries[index] : null;
  };

  Window_AffinityPairList.prototype.setEntries = function(entries) {
    this._entries = Array.isArray(entries) ? entries.slice() : [];
    this.refresh();
    this.select(this._entries.length > 0 ? 0 : -1);
  };

  Window_AffinityPairList.prototype.drawItem = function(index) {
    const entry = this._entries[index];
    if (!entry) return;
    const rect = this.itemRect(index);
    const leftWidth = Math.max(120, rect.width - 90);

    this.changeTextColor(ColorManager.normalColor());
    this.drawText(
      `${entry.actorNameA} + ${entry.actorNameB}`,
      rect.x,
      rect.y,
      leftWidth,
      "left"
    );

    this.changeTextColor(ColorManager.systemColor());
    this.drawText(`Lv ${entry.affinity}`, rect.x + leftWidth, rect.y, 50, "right");

    if (entry.dualReady) {
      this.changeTextColor(ColorManager.powerUpColor());
      this.drawText("DLB", rect.x + rect.width - 36, rect.y, 36, "right");
    }

    this.resetTextColor();
  };

  function Window_AffinityDetail() {
    this.initialize(...arguments);
  }

  Window_AffinityDetail.prototype = Object.create(Window_Base.prototype);
  Window_AffinityDetail.prototype.constructor = Window_AffinityDetail;

  Window_AffinityDetail.prototype.initialize = function(rect) {
    Window_Base.prototype.initialize.call(this, rect);
    this._entry = null;
    this.refresh();
  };

  Window_AffinityDetail.prototype.setEntry = function(entry) {
    this._entry = entry || null;
    this.refresh();
  };

  Window_AffinityDetail.prototype.refresh = function() {
    this.contents.clear();

    if (!this._entry) {
      this.drawText("Select a pair to view details.", 0, 0, this.innerWidth, "left");
      return;
    }

    const e = this._entry;
    let y = 0;

    this.changeTextColor(ColorManager.systemColor());
    this.drawText("Affinity Pair", 0, y, this.innerWidth, "left");
    y += this.lineHeight();

    this.resetTextColor();
    this.drawText(`${e.actorNameA} + ${e.actorNameB}`, 0, y, this.innerWidth, "left");
    y += this.lineHeight();

    this.changeTextColor(ColorManager.systemColor());
    this.drawText("Affinity Level", 0, y, this.innerWidth, "left");
    y += this.lineHeight();

    this.resetTextColor();
    this.drawText(String(e.affinity), 0, y, this.innerWidth, "left");
    y += this.lineHeight();

    this.changeTextColor(ColorManager.systemColor());
    this.drawText("Dual Limit", 0, y, this.innerWidth, "left");
    y += this.lineHeight();

    if (e.dualReady) {
      this.changeTextColor(ColorManager.powerUpColor());
      this.drawText("Ready", 0, y, this.innerWidth, "left");
    } else {
      this.changeTextColor(ColorManager.normalColor());
      this.drawText("Not ready", 0, y, this.innerWidth, "left");
    }
    y += this.lineHeight();

    this.resetTextColor();
    this.drawText(
      "Raise affinity to unlock stronger pair synergy.",
      0,
      y + this.lineHeight() / 2,
      this.innerWidth,
      "left"
    );
  };

  function Scene_AffinityMenu() {
    this.initialize(...arguments);
  }

  Scene_AffinityMenu.prototype = Object.create(Scene_MenuBase.prototype);
  Scene_AffinityMenu.prototype.constructor = Scene_AffinityMenu;

  Scene_AffinityMenu.prototype.create = function() {
    Scene_MenuBase.prototype.create.call(this);
    this.createWindows();
    this.refreshData();
  };

  Scene_AffinityMenu.prototype.createWindows = function() {
    const top = this.mainAreaTop();
    const height = this.mainAreaHeight();
    const listWidth = Math.floor(Graphics.boxWidth * 0.54);

    const listRect = new Rectangle(0, top, listWidth, height);
    this._listWindow = new Window_AffinityPairList(listRect);
    this._listWindow.setHandler("cancel", this.popScene.bind(this));
    this._listWindow.setHandler("ok", this.onListOk.bind(this));
    this._listWindow.setHandler("pagedown", this.onListOk.bind(this));
    this._listWindow.setHandler("pageup", this.onListOk.bind(this));
    this.addWindow(this._listWindow);

    const detailRect = new Rectangle(listWidth, top, Graphics.boxWidth - listWidth, height);
    this._detailWindow = new Window_AffinityDetail(detailRect);
    this.addWindow(this._detailWindow);
  };

  Scene_AffinityMenu.prototype.refreshData = function() {
    this._entries = buildPairEntries();
    this._listWindow.setEntries(this._entries);
    this.refreshDetail();
  };

  Scene_AffinityMenu.prototype.refreshDetail = function() {
    this._detailWindow.setEntry(this._listWindow.item());
  };

  Scene_AffinityMenu.prototype.onListOk = function() {
    this.refreshDetail();
    this._listWindow.activate();
  };

  const openAffinityMenu = () => {
    SceneManager.push(Scene_AffinityMenu);
  };

  PluginManager.registerCommand(pluginName, "OpenAffinityMenu", () => {
    openAffinityMenu();
  });

  const _Window_MenuCommand_addOriginalCommands = Window_MenuCommand.prototype.addOriginalCommands;
  Window_MenuCommand.prototype.addOriginalCommands = function() {
    _Window_MenuCommand_addOriginalCommands.call(this);
    if (!showMenuCommand) return;

    const enabled = !!($gameSystem && $gameSystem.chromaGetAffinity);
    this.addCommand(menuCommandName, MENU_SYMBOL, enabled);
  };

  const _Scene_Menu_createCommandWindow = Scene_Menu.prototype.createCommandWindow;
  Scene_Menu.prototype.createCommandWindow = function() {
    _Scene_Menu_createCommandWindow.call(this);
    this._commandWindow.setHandler(MENU_SYMBOL, openAffinityMenu.bind(this));
  };

  const g = typeof window !== "undefined" ? window : globalThis;
  g.Imported = g.Imported || {};
  g.Imported.ChromaEdge_AffinityMenu = true;
  g.ChromaEdge = g.ChromaEdge || {};

  g.ChromaEdge.AffinityMenu = {
    open() {
      openAffinityMenu();
    },
    entries() {
      return buildPairEntries();
    },
  };
})();
