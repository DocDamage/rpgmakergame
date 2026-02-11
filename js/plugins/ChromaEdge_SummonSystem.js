/*:
 * @target MZ
 * @plugindesc v0.2.0 Summon registry, unlock state, owner rules, and battle skill gating.
 * @author Chroma's Edge
 * @help
 * Implements summon ownership/unlock logic with save persistence and plugin commands.
 *
 * Core rules:
 * - Each summon has one owner actor.
 * - Owner can use their summon when it is unlocked.
 * - Callum can use any unlocked summon.
 *
 * Script calls:
 *   ChromaEdge.Summons.ids()
 *   ChromaEdge.Summons.get("ASHBORN")
 *   ChromaEdge.Summons.unlock("ASHBORN", true)
 *   ChromaEdge.Summons.canActorUse(10, "ASHBORN")
 *   ChromaEdge.Summons.fromSkill($dataSkills[282])
 *
 * @param callumActorId
 * @text Callum Actor Id
 * @type actor
 * @default 10
 *
 * @param seedCanonicalSummons
 * @text Seed Canonical Summons
 * @type boolean
 * @default true
 *
 * @param unlockCanonicalOnBoot
 * @text Unlock Canonical On Boot
 * @type boolean
 * @default false
 *
 * @param autoRegisterSkillSummons
 * @text Auto-Register Summon Skills
 * @type boolean
 * @default true
 *
 * @command RegisterSummon
 * @text Register Summon
 * @arg summonId
 * @type string
 * @default ASHBORN
 * @arg displayName
 * @type string
 * @default Ashborn
 * @arg ownerActorId
 * @type actor
 * @default 10
 * @arg unlocked
 * @type boolean
 * @default false
 *
 * @command SetSummonUnlocked
 * @text Set Summon Unlocked
 * @arg summonId
 * @type string
 * @default ASHBORN
 * @arg unlocked
 * @type boolean
 * @default true
 *
 * @command SetSummonOwner
 * @text Set Summon Owner
 * @arg summonId
 * @type string
 * @default ASHBORN
 * @arg ownerActorId
 * @type actor
 * @default 10
 *
 * @command IsSummonUsable
 * @text Check Summon Usable
 * @arg summonId
 * @type string
 * @default ASHBORN
 * @arg actorId
 * @type actor
 * @default 10
 * @arg switchId
 * @type switch
 * @default 1
 *
 * @command IsSkillSummonUsable
 * @text Check Skill Summon Usable
 * @arg skillId
 * @type skill
 * @default 282
 * @arg actorId
 * @type actor
 * @default 10
 * @arg switchId
 * @type switch
 * @default 1
 *
 * @command GetSummonOwner
 * @text Get Summon Owner
 * @arg summonId
 * @type string
 * @default ASHBORN
 * @arg variableId
 * @type variable
 * @default 1
 *
 * @command GetUnlockedSummonCount
 * @text Get Unlocked Summon Count
 * @arg variableId
 * @type variable
 * @default 1
 */

(() => {
  "use strict";

  const pluginName = "ChromaEdge_SummonSystem";
  const params = PluginManager.parameters(pluginName);
  const callumActorId = Number(params.callumActorId || 10);
  const seedCanonicalSummons =
    String(params.seedCanonicalSummons || "true").toLowerCase() === "true";
  const unlockCanonicalOnBoot =
    String(params.unlockCanonicalOnBoot || "false").toLowerCase() === "true";
  const autoRegisterSkillSummons =
    String(params.autoRegisterSkillSummons || "true").toLowerCase() === "true";

  const CANONICAL_SUMMONS = [
    { id: "DRAKONIS", displayName: "Drakonis", ownerActorId: 1 },
    { id: "GLACIEM", displayName: "Glaciem", ownerActorId: 2 },
    { id: "VOLTARIS", displayName: "Voltaris", ownerActorId: 3 },
    { id: "MARINUS", displayName: "Marinus", ownerActorId: 5 },
    { id: "MORTIS", displayName: "Mortis", ownerActorId: 4 },
    { id: "NIHILUS", displayName: "Nihilus", ownerActorId: 6 },
    { id: "TREMOR", displayName: "Tremor", ownerActorId: 7 },
    { id: "ZEPHYROS", displayName: "Zephyros", ownerActorId: 8 },
    { id: "PYRAXIS", displayName: "Pyraxis", ownerActorId: 9 },
    { id: "ASHBORN", displayName: "Ashborn", ownerActorId: 10 },
    { id: "AGONIS", displayName: "Agonis", ownerActorId: 11 },
    { id: "AEGIS", displayName: "Aegis", ownerActorId: 12 },
    { id: "LIBERATOR", displayName: "LIBERATOR", ownerActorId: 13 },
  ];

  const toInt = (value, fallback = 0) => {
    const parsed = Number(value);
    return Number.isFinite(parsed) ? Math.floor(parsed) : fallback;
  };

  const toBool = (value) =>
    String(value === undefined ? "" : value).toLowerCase() === "true";

  const normalizeSummonId = (raw) => {
    if (raw == null) return "";
    const cleaned = String(raw)
      .trim()
      .replace(/\s+/g, "_")
      .replace(/[^A-Za-z0-9_]/g, "_")
      .replace(/_+/g, "_")
      .replace(/^_+|_+$/g, "");
    return cleaned.toUpperCase();
  };

  const summonIdFromSkill = (skill) => {
    if (!skill || typeof skill !== "object") return "";
    if (skill.meta && skill.meta.chromaSummonId) {
      return normalizeSummonId(skill.meta.chromaSummonId);
    }
    const name = String(skill.name || "");
    const m = name.match(/^\s*Summon\s*:\s*(.+?)\s*$/i);
    if (m && m[1]) return normalizeSummonId(m[1]);
    return "";
  };

  const summonDisplayNameFromSkill = (skill) => {
    const name = String((skill && skill.name) || "");
    const m = name.match(/^\s*Summon\s*:\s*(.+?)\s*$/i);
    if (m && m[1]) return String(m[1]).trim();
    return "";
  };

  const isSummonSkill = (skill) => !!summonIdFromSkill(skill);

  const deepClone = (value) => JSON.parse(JSON.stringify(value));

  const setSwitch = (switchId, value) => {
    const id = toInt(switchId, 0);
    if (id > 0 && $gameSwitches) $gameSwitches.setValue(id, !!value);
  };

  const setVariable = (variableId, value) => {
    const id = toInt(variableId, 0);
    if (id > 0 && $gameVariables) $gameVariables.setValue(id, value);
  };

  Game_System.prototype.chromaInitSummonData = function() {
    if (!this._chromaSummons || typeof this._chromaSummons !== "object") {
      this._chromaSummons = {};
    }
    if (this._chromaSummonsSkillSeeded !== true) {
      this._chromaSummonsSkillSeeded = false;
    }
    if (this._chromaSummonsCanonicalSeeded !== true) {
      this._chromaSummonsCanonicalSeeded = false;
    }
    if (seedCanonicalSummons && !this._chromaSummonsCanonicalSeeded) {
      this._chromaSummonsCanonicalSeeded = true;
      this.chromaSeedCanonicalSummons(unlockCanonicalOnBoot);
    }
  };

  Game_System.prototype.chromaSummonMap = function() {
    this.chromaInitSummonData();
    return this._chromaSummons;
  };

  Game_System.prototype.chromaEnsureSummonEntry = function(summonId) {
    const id = normalizeSummonId(summonId);
    if (!id) return null;
    const map = this.chromaSummonMap();
    if (!map[id] || typeof map[id] !== "object") {
      map[id] = {
        id,
        displayName: id,
        ownerActorId: 0,
        unlocked: false,
        source: "runtime",
      };
    }
    const rec = map[id];
    rec.id = id;
    rec.displayName = String(rec.displayName || id);
    rec.ownerActorId = toInt(rec.ownerActorId, 0);
    rec.unlocked = !!rec.unlocked;
    rec.source = String(rec.source || "runtime");
    return rec;
  };

  Game_System.prototype.chromaRegisterSummon = function(
    summonId,
    displayName,
    ownerActorId,
    unlocked,
    source = "runtime"
  ) {
    const rec = this.chromaEnsureSummonEntry(summonId);
    if (!rec) return null;
    if (displayName != null && String(displayName).trim()) {
      rec.displayName = String(displayName).trim();
    }
    if (ownerActorId != null) {
      rec.ownerActorId = Math.max(0, toInt(ownerActorId, 0));
    }
    if (unlocked != null) {
      rec.unlocked = !!unlocked;
    }
    rec.source = String(source || rec.source || "runtime");
    return rec;
  };

  Game_System.prototype.chromaSeedCanonicalSummons = function(unlockAll) {
    const unlock = !!unlockAll;
    for (const entry of CANONICAL_SUMMONS) {
      const existing = this.chromaGetSummon(entry.id);
      const nextUnlocked = existing ? existing.unlocked : unlock;
      this.chromaRegisterSummon(
        entry.id,
        entry.displayName,
        entry.ownerActorId,
        nextUnlocked,
        "canonical"
      );
    }
  };

  Game_System.prototype.chromaRegisterSkillSummons = function() {
    if (this._chromaSummonsSkillSeeded) return;
    if (!Array.isArray($dataSkills) || $dataSkills.length <= 1) return;

    for (let i = 1; i < $dataSkills.length; i += 1) {
      const skill = $dataSkills[i];
      if (!skill) continue;
      const summonId = summonIdFromSkill(skill);
      if (!summonId) continue;
      const displayName = summonDisplayNameFromSkill(skill) || summonId;
      const existing = this.chromaGetSummon(summonId);
      const ownerActorId = existing ? existing.ownerActorId : callumActorId;
      const unlocked = existing ? existing.unlocked : false;
      this.chromaRegisterSummon(
        summonId,
        displayName,
        ownerActorId,
        unlocked,
        "skill"
      );
    }

    this._chromaSummonsSkillSeeded = true;
  };

  Game_System.prototype.chromaGetSummon = function(summonId) {
    const rec = this.chromaEnsureSummonEntry(summonId);
    return rec ? deepClone(rec) : null;
  };

  Game_System.prototype.chromaSummonIds = function() {
    this.chromaRegisterSkillSummons();
    return Object.keys(this.chromaSummonMap()).sort();
  };

  Game_System.prototype.chromaSetSummonUnlocked = function(summonId, unlocked) {
    const rec = this.chromaEnsureSummonEntry(summonId);
    if (!rec) return false;
    rec.unlocked = !!unlocked;
    return true;
  };

  Game_System.prototype.chromaSetSummonOwner = function(summonId, ownerActorId) {
    const rec = this.chromaEnsureSummonEntry(summonId);
    if (!rec) return false;
    rec.ownerActorId = Math.max(0, toInt(ownerActorId, 0));
    return true;
  };

  Game_System.prototype.chromaSummonOwner = function(summonId) {
    const rec = this.chromaEnsureSummonEntry(summonId);
    return rec ? rec.ownerActorId : 0;
  };

  Game_System.prototype.chromaIsSummonUnlocked = function(summonId) {
    const rec = this.chromaEnsureSummonEntry(summonId);
    return rec ? !!rec.unlocked : false;
  };

  Game_System.prototype.chromaCanActorUseSummon = function(actorId, summonId) {
    const aid = toInt(actorId, 0);
    if (aid <= 0) return false;
    const rec = this.chromaEnsureSummonEntry(summonId);
    if (!rec || !rec.unlocked) return false;
    if (rec.ownerActorId > 0 && aid === rec.ownerActorId) return true;
    if (aid === callumActorId) return true;
    return false;
  };

  Game_System.prototype.chromaCanActorUseSummonSkill = function(actor, skill) {
    if (!skill || !isSummonSkill(skill)) return true;
    const aid = actor && actor.actorId ? actor.actorId() : 0;
    if (aid <= 0) return false;
    this.chromaRegisterSkillSummons();
    const summonId = summonIdFromSkill(skill);
    return this.chromaCanActorUseSummon(aid, summonId);
  };

  Game_System.prototype.chromaUnlockedSummonCount = function() {
    this.chromaRegisterSkillSummons();
    let count = 0;
    for (const summonId of this.chromaSummonIds()) {
      if (this.chromaIsSummonUnlocked(summonId)) count += 1;
    }
    return count;
  };

  const _Game_System_initialize = Game_System.prototype.initialize;
  Game_System.prototype.initialize = function() {
    _Game_System_initialize.call(this);
    this.chromaInitSummonData();
  };

  const _DataManager_extractSaveContents = DataManager.extractSaveContents;
  DataManager.extractSaveContents = function(contents) {
    _DataManager_extractSaveContents.call(this, contents);
    if ($gameSystem && $gameSystem.chromaInitSummonData) {
      $gameSystem.chromaInitSummonData();
      $gameSystem.chromaRegisterSkillSummons();
    }
  };

  const _Game_Actor_meetsSkillConditions = Game_Actor.prototype.meetsSkillConditions;
  Game_Actor.prototype.meetsSkillConditions = function(skill) {
    const base = _Game_Actor_meetsSkillConditions.call(this, skill);
    if (!base) return false;
    if (!$gameSystem || !$gameSystem.chromaCanActorUseSummonSkill) return base;
    return $gameSystem.chromaCanActorUseSummonSkill(this, skill);
  };

  PluginManager.registerCommand(pluginName, "RegisterSummon", (args) => {
    $gameSystem.chromaRegisterSummon(
      args.summonId,
      args.displayName,
      args.ownerActorId,
      toBool(args.unlocked),
      "command"
    );
  });

  PluginManager.registerCommand(pluginName, "SetSummonUnlocked", (args) => {
    $gameSystem.chromaSetSummonUnlocked(args.summonId, toBool(args.unlocked));
  });

  PluginManager.registerCommand(pluginName, "SetSummonOwner", (args) => {
    $gameSystem.chromaSetSummonOwner(args.summonId, args.ownerActorId);
  });

  PluginManager.registerCommand(pluginName, "IsSummonUsable", (args) => {
    const ok = $gameSystem.chromaCanActorUseSummon(args.actorId, args.summonId);
    setSwitch(args.switchId, ok);
  });

  PluginManager.registerCommand(pluginName, "IsSkillSummonUsable", (args) => {
    const actor = $gameActors ? $gameActors.actor(toInt(args.actorId, 0)) : null;
    const skill = $dataSkills ? $dataSkills[toInt(args.skillId, 0)] : null;
    const ok = !!(
      actor &&
      skill &&
      $gameSystem.chromaCanActorUseSummonSkill(actor, skill)
    );
    setSwitch(args.switchId, ok);
  });

  PluginManager.registerCommand(pluginName, "GetSummonOwner", (args) => {
    setVariable(args.variableId, $gameSystem.chromaSummonOwner(args.summonId));
  });

  PluginManager.registerCommand(pluginName, "GetUnlockedSummonCount", (args) => {
    setVariable(args.variableId, $gameSystem.chromaUnlockedSummonCount());
  });

  const g = typeof window !== "undefined" ? window : globalThis;
  g.Imported = g.Imported || {};
  g.Imported.ChromaEdge_SummonSystem = true;
  g.ChromaEdge = g.ChromaEdge || {};

  g.ChromaEdge.Summons = {
    normalizeId(id) {
      return normalizeSummonId(id);
    },
    ids() {
      return $gameSystem ? $gameSystem.chromaSummonIds() : [];
    },
    get(summonId) {
      return $gameSystem ? $gameSystem.chromaGetSummon(summonId) : null;
    },
    register(summonId, displayName, ownerActorId = 0, unlocked = false) {
      if (!$gameSystem) return null;
      return $gameSystem.chromaRegisterSummon(
        summonId,
        displayName,
        ownerActorId,
        unlocked,
        "script"
      );
    },
    unlock(summonId, value = true) {
      return $gameSystem
        ? $gameSystem.chromaSetSummonUnlocked(summonId, !!value)
        : false;
    },
    isUnlocked(summonId) {
      return $gameSystem ? $gameSystem.chromaIsSummonUnlocked(summonId) : false;
    },
    setOwner(summonId, actorId) {
      return $gameSystem ? $gameSystem.chromaSetSummonOwner(summonId, actorId) : false;
    },
    ownerId(summonId) {
      return $gameSystem ? $gameSystem.chromaSummonOwner(summonId) : 0;
    },
    canActorUse(actorId, summonId) {
      return $gameSystem
        ? $gameSystem.chromaCanActorUseSummon(actorId, summonId)
        : false;
    },
    canActorUseSkill(actorId, skillId) {
      if (!$gameSystem || !$gameActors || !$dataSkills) return false;
      const actor = $gameActors.actor(toInt(actorId, 0));
      const skill = $dataSkills[toInt(skillId, 0)];
      if (!actor || !skill) return false;
      return $gameSystem.chromaCanActorUseSummonSkill(actor, skill);
    },
    fromSkill(skill) {
      return summonIdFromSkill(skill);
    },
    unlockedCount() {
      return $gameSystem ? $gameSystem.chromaUnlockedSummonCount() : 0;
    },
    callumActorId() {
      return callumActorId;
    },
  };
})();
