/*:
 * @target MZ
 * @plugindesc v0.2.0 Dual Limit Break pair runtime, validation, and skill gating.
 * @author Chroma's Edge
 * @help
 * Implements dual limit pair state and checks against affinity + battle conditions.
 *
 * Skill note tags supported:
 *   <chromaDualLimitActors:1,2>
 *   <chromaDualPair:1,2>
 *
 * Script calls:
 *   ChromaEdge.DualLimitBreak.canPair(1, 2)
 *   ChromaEdge.DualLimitBreak.canUseSkill(1, 400)
 *   ChromaEdge.DualLimitBreak.setPairUnlocked(1, 2, true)
 *
 * @param requiredAffinity
 * @text Required Affinity
 * @type number
 * @default 10
 *
 * @param requiredTp
 * @text Required TP (Both Actors)
 * @type number
 * @default 100
 *
 * @param requireBothBattleMembers
 * @text Require Both In Battle Party
 * @type boolean
 * @default true
 *
 * @param requireBothTpFull
 * @text Require Both TP
 * @type boolean
 * @default true
 *
 * @param defaultPairsUnlocked
 * @text Default Pairs Unlocked
 * @type boolean
 * @default true
 *
 * @command SetPairUnlocked
 * @text Set Pair Unlocked
 * @arg actorIdA
 * @type actor
 * @default 1
 * @arg actorIdB
 * @type actor
 * @default 2
 * @arg unlocked
 * @type boolean
 * @default true
 *
 * @command CanPairUseDLB
 * @text Check Pair Can Use DLB
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
 * @command RegisterPairSkill
 * @text Register Pair Skill
 * @arg actorIdA
 * @type actor
 * @default 1
 * @arg actorIdB
 * @type actor
 * @default 2
 * @arg skillId
 * @type skill
 * @default 0
 * @arg displayName
 * @type string
 * @default
 *
 * @command CheckSkillUsable
 * @text Check DLB Skill Usable
 * @arg actorId
 * @type actor
 * @default 1
 * @arg skillId
 * @type skill
 * @default 1
 * @arg switchId
 * @type switch
 * @default 1
 *
 * @command ConsumePairTp
 * @text Consume Pair TP
 * @arg actorIdA
 * @type actor
 * @default 1
 * @arg actorIdB
 * @type actor
 * @default 2
 */

(() => {
  "use strict";

  const pluginName = "ChromaEdge_DualLimitBreak";
  const params = PluginManager.parameters(pluginName);
  const requiredAffinity = Number(params.requiredAffinity || 10);
  const requiredTp = Number(params.requiredTp || 100);
  const requireBothBattleMembers =
    String(params.requireBothBattleMembers || "true").toLowerCase() === "true";
  const requireBothTpFull =
    String(params.requireBothTpFull || "true").toLowerCase() === "true";
  const defaultPairsUnlocked =
    String(params.defaultPairsUnlocked || "true").toLowerCase() === "true";

  const toInt = (value, fallback = 0) => {
    const parsed = Number(value);
    return Number.isFinite(parsed) ? Math.floor(parsed) : fallback;
  };

  const toBool = (value) =>
    String(value === undefined ? "" : value).toLowerCase() === "true";

  const deepClone = (value) => JSON.parse(JSON.stringify(value));

  const pairKey = (actorIdA, actorIdB) => {
    const a = toInt(actorIdA, 0);
    const b = toInt(actorIdB, 0);
    if (a <= 0 || b <= 0 || a === b) return "";
    return a < b ? `${a}:${b}` : `${b}:${a}`;
  };

  const parsePairFromSkillNote = (skill) => {
    if (!skill || typeof skill !== "object") return null;

    const parseIds = (raw) => {
      const bits = String(raw || "")
        .split(",")
        .map((v) => toInt(v.trim(), 0))
        .filter((v) => v > 0);
      if (bits.length < 2) return null;
      return { actorIdA: bits[0], actorIdB: bits[1] };
    };

    if (skill.meta && skill.meta.chromaDualLimitActors) {
      return parseIds(skill.meta.chromaDualLimitActors);
    }
    if (skill.meta && skill.meta.chromaDualPair) {
      return parseIds(skill.meta.chromaDualPair);
    }

    const note = String(skill.note || "");
    let m = note.match(/<\s*chromaDualLimitActors\s*:\s*([0-9]+\s*,\s*[0-9]+)\s*>/i);
    if (!m) {
      m = note.match(/<\s*chromaDualPair\s*:\s*([0-9]+\s*,\s*[0-9]+)\s*>/i);
    }
    return m ? parseIds(m[1]) : null;
  };

  const setSwitch = (switchId, value) => {
    const id = toInt(switchId, 0);
    if (id > 0 && $gameSwitches) $gameSwitches.setValue(id, !!value);
  };

  Game_System.prototype.chromaInitDualLimitData = function() {
    if (!this._chromaDualLimit || typeof this._chromaDualLimit !== "object") {
      this._chromaDualLimit = {};
    }
  };

  Game_System.prototype.chromaDualLimitMap = function() {
    this.chromaInitDualLimitData();
    return this._chromaDualLimit;
  };

  Game_System.prototype.chromaEnsureDualLimitPair = function(actorIdA, actorIdB) {
    const key = pairKey(actorIdA, actorIdB);
    if (!key) return null;
    const [aText, bText] = key.split(":");
    const a = toInt(aText, 0);
    const b = toInt(bText, 0);
    const map = this.chromaDualLimitMap();

    if (!map[key] || typeof map[key] !== "object") {
      map[key] = {
        key,
        actorIdA: a,
        actorIdB: b,
        unlocked: defaultPairsUnlocked,
        skillId: 0,
        displayName: "",
      };
    }

    const rec = map[key];
    rec.key = key;
    rec.actorIdA = a;
    rec.actorIdB = b;
    rec.unlocked = !!rec.unlocked;
    rec.skillId = Math.max(0, toInt(rec.skillId, 0));
    rec.displayName = String(rec.displayName || "");
    return rec;
  };

  Game_System.prototype.chromaSetDualLimitPairUnlocked = function(
    actorIdA,
    actorIdB,
    unlocked
  ) {
    const rec = this.chromaEnsureDualLimitPair(actorIdA, actorIdB);
    if (!rec) return false;
    rec.unlocked = !!unlocked;
    return true;
  };

  Game_System.prototype.chromaRegisterDualLimitPairSkill = function(
    actorIdA,
    actorIdB,
    skillId,
    displayName
  ) {
    const rec = this.chromaEnsureDualLimitPair(actorIdA, actorIdB);
    if (!rec) return false;
    rec.skillId = Math.max(0, toInt(skillId, 0));
    if (displayName != null && String(displayName).trim()) {
      rec.displayName = String(displayName).trim();
    }
    return true;
  };

  Game_System.prototype.chromaDualLimitPair = function(actorIdA, actorIdB) {
    const rec = this.chromaEnsureDualLimitPair(actorIdA, actorIdB);
    return rec ? deepClone(rec) : null;
  };

  Game_System.prototype.chromaDualLimitPairBySkill = function(skill) {
    const tagged = parsePairFromSkillNote(skill);
    if (tagged) {
      const rec = this.chromaEnsureDualLimitPair(tagged.actorIdA, tagged.actorIdB);
      if (rec) {
        if (toInt(skill.id, 0) > 0 && rec.skillId <= 0) rec.skillId = toInt(skill.id, 0);
        if (!rec.displayName && skill.name) rec.displayName = String(skill.name);
        return rec;
      }
    }

    const sid = toInt(skill && skill.id, 0);
    if (sid <= 0) return null;
    const map = this.chromaDualLimitMap();
    for (const key of Object.keys(map)) {
      const rec = map[key];
      if (rec && toInt(rec.skillId, 0) === sid) return rec;
    }
    return null;
  };

  Game_System.prototype.chromaDualLimitAffinityReady = function(actorIdA, actorIdB) {
    if (this.chromaCanDualLimit) {
      return !!this.chromaCanDualLimit(actorIdA, actorIdB);
    }
    if (this.chromaGetAffinity) {
      return toInt(this.chromaGetAffinity(actorIdA, actorIdB), 0) >= requiredAffinity;
    }
    return false;
  };

  Game_System.prototype.chromaDualLimitPairActorsReady = function(actorIdA, actorIdB) {
    const aId = toInt(actorIdA, 0);
    const bId = toInt(actorIdB, 0);
    if (aId <= 0 || bId <= 0) return false;

    const actorA = $gameActors ? $gameActors.actor(aId) : null;
    const actorB = $gameActors ? $gameActors.actor(bId) : null;
    if (!actorA || !actorB) return false;

    if ($gameParty && $gameParty.inBattle()) {
      if (requireBothBattleMembers) {
        const partyIds = $gameParty.battleMembers().map((m) => m.actorId());
        if (!partyIds.includes(aId) || !partyIds.includes(bId)) return false;
      }
      if (requireBothTpFull) {
        if (actorA.tp < requiredTp || actorB.tp < requiredTp) return false;
      }
    }

    return true;
  };

  Game_System.prototype.chromaDualLimitCanPair = function(actorIdA, actorIdB) {
    const rec = this.chromaEnsureDualLimitPair(actorIdA, actorIdB);
    if (!rec || !rec.unlocked) return false;
    if (!this.chromaDualLimitAffinityReady(rec.actorIdA, rec.actorIdB)) return false;
    if (!this.chromaDualLimitPairActorsReady(rec.actorIdA, rec.actorIdB)) return false;
    return true;
  };

  Game_System.prototype.chromaDualLimitCanActorUseSkill = function(actor, skill) {
    const rec = this.chromaDualLimitPairBySkill(skill);
    if (!rec) return true;
    if (!actor || !actor.actorId) return false;
    const aid = actor.actorId();
    if (aid !== rec.actorIdA && aid !== rec.actorIdB) return false;
    return this.chromaDualLimitCanPair(rec.actorIdA, rec.actorIdB);
  };

  Game_System.prototype.chromaDualLimitConsumePairTp = function(actorIdA, actorIdB) {
    const rec = this.chromaEnsureDualLimitPair(actorIdA, actorIdB);
    if (!rec) return false;
    const actorA = $gameActors ? $gameActors.actor(rec.actorIdA) : null;
    const actorB = $gameActors ? $gameActors.actor(rec.actorIdB) : null;
    if (!actorA || !actorB) return false;

    actorA.setTp(Math.max(0, actorA.tp - requiredTp));
    actorB.setTp(Math.max(0, actorB.tp - requiredTp));
    return true;
  };

  const _Game_System_initialize = Game_System.prototype.initialize;
  Game_System.prototype.initialize = function() {
    _Game_System_initialize.call(this);
    this.chromaInitDualLimitData();
  };

  const _DataManager_extractSaveContents = DataManager.extractSaveContents;
  DataManager.extractSaveContents = function(contents) {
    _DataManager_extractSaveContents.call(this, contents);
    if ($gameSystem && $gameSystem.chromaInitDualLimitData) {
      $gameSystem.chromaInitDualLimitData();
    }
  };

  const _Game_Actor_meetsSkillConditions = Game_Actor.prototype.meetsSkillConditions;
  Game_Actor.prototype.meetsSkillConditions = function(skill) {
    const base = _Game_Actor_meetsSkillConditions.call(this, skill);
    if (!base) return false;
    if (!$gameSystem || !$gameSystem.chromaDualLimitCanActorUseSkill) return base;
    return $gameSystem.chromaDualLimitCanActorUseSkill(this, skill);
  };

  const _Game_BattlerBase_paySkillCost = Game_BattlerBase.prototype.paySkillCost;
  Game_BattlerBase.prototype.paySkillCost = function(skill) {
    _Game_BattlerBase_paySkillCost.call(this, skill);
    if (!(this instanceof Game_Actor)) return;
    if (!$gameSystem || !$gameSystem.chromaDualLimitPairBySkill) return;

    const rec = $gameSystem.chromaDualLimitPairBySkill(skill);
    if (!rec) return;
    const aid = this.actorId();
    const partnerId = aid === rec.actorIdA ? rec.actorIdB : rec.actorIdA;
    if (partnerId <= 0) return;

    const partner = $gameActors ? $gameActors.actor(partnerId) : null;
    if (!partner) return;
    partner.setTp(Math.max(0, partner.tp - requiredTp));
  };

  PluginManager.registerCommand(pluginName, "SetPairUnlocked", (args) => {
    $gameSystem.chromaSetDualLimitPairUnlocked(
      args.actorIdA,
      args.actorIdB,
      toBool(args.unlocked)
    );
  });

  PluginManager.registerCommand(pluginName, "CanPairUseDLB", (args) => {
    const ok = $gameSystem.chromaDualLimitCanPair(args.actorIdA, args.actorIdB);
    setSwitch(args.switchId, ok);
  });

  PluginManager.registerCommand(pluginName, "RegisterPairSkill", (args) => {
    $gameSystem.chromaRegisterDualLimitPairSkill(
      args.actorIdA,
      args.actorIdB,
      args.skillId,
      args.displayName
    );
  });

  PluginManager.registerCommand(pluginName, "CheckSkillUsable", (args) => {
    const actor = $gameActors ? $gameActors.actor(toInt(args.actorId, 0)) : null;
    const skill = $dataSkills ? $dataSkills[toInt(args.skillId, 0)] : null;
    const ok = !!(
      actor &&
      skill &&
      $gameSystem.chromaDualLimitCanActorUseSkill(actor, skill)
    );
    setSwitch(args.switchId, ok);
  });

  PluginManager.registerCommand(pluginName, "ConsumePairTp", (args) => {
    $gameSystem.chromaDualLimitConsumePairTp(args.actorIdA, args.actorIdB);
  });

  const g = typeof window !== "undefined" ? window : globalThis;
  g.Imported = g.Imported || {};
  g.Imported.ChromaEdge_DualLimitBreak = true;
  g.ChromaEdge = g.ChromaEdge || {};

  g.ChromaEdge.DualLimitBreak = {
    pairKey(actorIdA, actorIdB) {
      return pairKey(actorIdA, actorIdB);
    },
    getPair(actorIdA, actorIdB) {
      return $gameSystem ? $gameSystem.chromaDualLimitPair(actorIdA, actorIdB) : null;
    },
    setPairUnlocked(actorIdA, actorIdB, unlocked = true) {
      return $gameSystem
        ? $gameSystem.chromaSetDualLimitPairUnlocked(actorIdA, actorIdB, !!unlocked)
        : false;
    },
    registerSkill(actorIdA, actorIdB, skillId, displayName = "") {
      return $gameSystem
        ? $gameSystem.chromaRegisterDualLimitPairSkill(
            actorIdA,
            actorIdB,
            skillId,
            displayName
          )
        : false;
    },
    canPair(actorIdA, actorIdB) {
      return $gameSystem ? $gameSystem.chromaDualLimitCanPair(actorIdA, actorIdB) : false;
    },
    canUseSkill(actorId, skillId) {
      if (!$gameSystem || !$gameActors || !$dataSkills) return false;
      const actor = $gameActors.actor(toInt(actorId, 0));
      const skill = $dataSkills[toInt(skillId, 0)];
      if (!actor || !skill) return false;
      return $gameSystem.chromaDualLimitCanActorUseSkill(actor, skill);
    },
    consumePairTp(actorIdA, actorIdB) {
      return $gameSystem
        ? $gameSystem.chromaDualLimitConsumePairTp(actorIdA, actorIdB)
        : false;
    },
    parseSkillPair(skill) {
      const rec = $gameSystem ? $gameSystem.chromaDualLimitPairBySkill(skill) : null;
      return rec ? deepClone(rec) : null;
    },
  };
})();
