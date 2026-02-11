/*:
 * @target MZ
 * @plugindesc v0.2.0 Persistent 24-hour time cycle with variable sync and optional map tint.
 * @author Chroma's Edge
 * @help
 * Provides a day/night clock used by NPC schedules and world-state checks.
 *
 * Script calls:
 *   ChromaEdge.DayNight.hour()
 *   ChromaEdge.DayNight.minute()
 *   ChromaEdge.DayNight.period()
 *   ChromaEdge.DayNight.setTime(18, 30)
 *
 * @param startHour
 * @text Start Hour
 * @type number
 * @min 0
 * @max 23
 * @default 8
 *
 * @param startMinute
 * @text Start Minute
 * @type number
 * @min 0
 * @max 59
 * @default 0
 *
 * @param realSecondsPerGameMinute
 * @text Real Seconds / Game Minute
 * @type number
 * @decimals 2
 * @min 0.1
 * @default 2
 *
 * @param syncVariableId
 * @text Hour Variable Id
 * @type variable
 * @default 21
 *
 * @param autoTintEnabled
 * @text Auto Tint Map
 * @type boolean
 * @default true
 *
 * @command SetTime
 * @text Set Time
 * @arg hour
 * @type number
 * @min 0
 * @max 23
 * @default 8
 * @arg minute
 * @type number
 * @min 0
 * @max 59
 * @default 0
 *
 * @command AddHours
 * @text Add Hours
 * @arg amount
 * @type number
 * @default 1
 *
 * @command AddMinutes
 * @text Add Minutes
 * @arg amount
 * @type number
 * @default 10
 *
 * @command SetPaused
 * @text Set Paused
 * @arg value
 * @type boolean
 * @default true
 *
 * @command TogglePaused
 * @text Toggle Paused
 *
 * @command SetAutoTint
 * @text Set Auto Tint
 * @arg value
 * @type boolean
 * @default true
 *
 * @command GetTime
 * @text Get Time
 * @arg hourVariableId
 * @type variable
 * @default 0
 * @arg minuteVariableId
 * @type variable
 * @default 0
 * @arg periodVariableId
 * @type variable
 * @default 0
 *
 * @command CheckIsNight
 * @text Check Is Night
 * @arg switchId
 * @type switch
 * @default 1
 */

(() => {
  "use strict";

  const pluginName = "ChromaEdge_DayNightSystem";
  const params = PluginManager.parameters(pluginName);
  const startHour = Math.max(0, Math.min(23, Number(params.startHour || 8)));
  const startMinute = Math.max(0, Math.min(59, Number(params.startMinute || 0)));
  const realSecondsPerGameMinute = Math.max(0.1, Number(params.realSecondsPerGameMinute || 2));
  const syncVariableId = Number(params.syncVariableId || 21);
  const autoTintEnabled =
    String(params.autoTintEnabled || "true").toLowerCase() === "true";

  const PERIOD_CODE = {
    dawn: 1,
    day: 2,
    dusk: 3,
    night: 4,
  };

  const toInt = (value, fallback = 0) => {
    const parsed = Number(value);
    return Number.isFinite(parsed) ? Math.floor(parsed) : fallback;
  };

  const toBool = (value) =>
    String(value === undefined ? "" : value).toLowerCase() === "true";

  const setVariable = (variableId, value) => {
    const id = toInt(variableId, 0);
    if (id > 0 && $gameVariables) $gameVariables.setValue(id, value);
  };

  const setSwitch = (switchId, value) => {
    const id = toInt(switchId, 0);
    if (id > 0 && $gameSwitches) $gameSwitches.setValue(id, !!value);
  };

  const normalizeTime = (hour, minute) => {
    let h = toInt(hour, startHour);
    let m = toInt(minute, startMinute);

    while (m >= 60) {
      h += 1;
      m -= 60;
    }
    while (m < 0) {
      h -= 1;
      m += 60;
    }
    while (h >= 24) h -= 24;
    while (h < 0) h += 24;

    return { hour: h, minute: m };
  };

  const periodForHour = (hour) => {
    const h = Math.max(0, Math.min(23, toInt(hour, 0)));
    if (h >= 5 && h <= 7) return "dawn";
    if (h >= 8 && h <= 17) return "day";
    if (h >= 18 && h <= 19) return "dusk";
    return "night";
  };

  const lerp = (a, b, t) => a + (b - a) * t;

  const toneKeyframes = [
    { h: 0, tone: [-68, -68, 0, 128] },
    { h: 5, tone: [-40, -40, 0, 80] },
    { h: 7, tone: [0, 0, 0, 0] },
    { h: 17, tone: [0, 0, 0, 0] },
    { h: 19, tone: [-36, -36, 0, 72] },
    { h: 22, tone: [-58, -58, 0, 112] },
    { h: 24, tone: [-68, -68, 0, 128] },
  ];

  const toneForHourMinute = (hour, minute) => {
    const h = Math.max(0, Math.min(23, toInt(hour, 0))) + Math.max(0, Math.min(59, toInt(minute, 0))) / 60;

    let left = toneKeyframes[0];
    let right = toneKeyframes[toneKeyframes.length - 1];
    for (let i = 0; i < toneKeyframes.length - 1; i += 1) {
      const a = toneKeyframes[i];
      const b = toneKeyframes[i + 1];
      if (h >= a.h && h <= b.h) {
        left = a;
        right = b;
        break;
      }
    }

    const span = Math.max(0.0001, right.h - left.h);
    const t = Math.max(0, Math.min(1, (h - left.h) / span));
    return [
      Math.round(lerp(left.tone[0], right.tone[0], t)),
      Math.round(lerp(left.tone[1], right.tone[1], t)),
      Math.round(lerp(left.tone[2], right.tone[2], t)),
      Math.round(lerp(left.tone[3], right.tone[3], t)),
    ];
  };

  Game_System.prototype.chromaInitDayNightData = function() {
    if (!this._chromaDayNight || typeof this._chromaDayNight !== "object") {
      this._chromaDayNight = {
        hour: startHour,
        minute: startMinute,
        paused: false,
        autoTint: autoTintEnabled,
        frameAccumulator: 0,
        dayCount: 0,
        tick: 0,
        lastTintSnapshot: "",
      };
    }

    this._chromaDayNight.hour = normalizeTime(
      this._chromaDayNight.hour,
      this._chromaDayNight.minute
    ).hour;
    this._chromaDayNight.minute = normalizeTime(
      this._chromaDayNight.hour,
      this._chromaDayNight.minute
    ).minute;
    this._chromaDayNight.paused = !!this._chromaDayNight.paused;
    this._chromaDayNight.autoTint =
      this._chromaDayNight.autoTint == null
        ? autoTintEnabled
        : !!this._chromaDayNight.autoTint;
    this._chromaDayNight.frameAccumulator = Math.max(
      0,
      toInt(this._chromaDayNight.frameAccumulator, 0)
    );
    this._chromaDayNight.dayCount = Math.max(0, toInt(this._chromaDayNight.dayCount, 0));
    this._chromaDayNight.tick = Math.max(0, toInt(this._chromaDayNight.tick, 0));
    this._chromaDayNight.lastTintSnapshot = String(this._chromaDayNight.lastTintSnapshot || "");

    this.chromaDayNightSyncVariable();
  };

  Game_System.prototype.chromaDayNightData = function() {
    this.chromaInitDayNightData();
    return this._chromaDayNight;
  };

  Game_System.prototype.chromaDayNightHour = function() {
    return this.chromaDayNightData().hour;
  };

  Game_System.prototype.chromaDayNightMinute = function() {
    return this.chromaDayNightData().minute;
  };

  Game_System.prototype.chromaDayNightTick = function() {
    return this.chromaDayNightData().tick;
  };

  Game_System.prototype.chromaDayNightPeriod = function() {
    const d = this.chromaDayNightData();
    return periodForHour(d.hour);
  };

  Game_System.prototype.chromaDayNightIsNight = function() {
    return this.chromaDayNightPeriod() === "night";
  };

  Game_System.prototype.chromaSetDayNightPaused = function(value) {
    const d = this.chromaDayNightData();
    d.paused = !!value;
    return d.paused;
  };

  Game_System.prototype.chromaSetDayNightAutoTint = function(value) {
    const d = this.chromaDayNightData();
    d.autoTint = !!value;
    return d.autoTint;
  };

  Game_System.prototype.chromaSetTime = function(hour, minute) {
    const d = this.chromaDayNightData();
    const before = `${d.hour}:${d.minute}`;
    const next = normalizeTime(hour, minute);
    d.hour = next.hour;
    d.minute = next.minute;
    const after = `${d.hour}:${d.minute}`;
    if (after !== before) {
      d.tick += 1;
      this.chromaDayNightSyncVariable();
      this.chromaDayNightApplyTint(true);
    }
    return { hour: d.hour, minute: d.minute };
  };

  Game_System.prototype.chromaAddMinutes = function(amount) {
    const d = this.chromaDayNightData();
    return this.chromaSetTime(d.hour, d.minute + toInt(amount, 0));
  };

  Game_System.prototype.chromaAddHours = function(amount) {
    return this.chromaAddMinutes(toInt(amount, 0) * 60);
  };

  Game_System.prototype.chromaDayNightSyncVariable = function() {
    const data = this._chromaDayNight;
    const hour =
      data && Number.isFinite(Number(data.hour))
        ? Math.max(0, Math.min(23, toInt(data.hour, startHour)))
        : startHour;
    setVariable(syncVariableId, hour);
  };

  Game_System.prototype.chromaDayNightUpdate = function() {
    const d = this.chromaDayNightData();
    if (d.paused) {
      this.chromaDayNightApplyTint(false);
      return;
    }

    const framesPerMinute = Math.max(1, Math.round(realSecondsPerGameMinute * 60));
    d.frameAccumulator += 1;
    if (d.frameAccumulator >= framesPerMinute) {
      d.frameAccumulator = 0;
      const beforeHour = d.hour;
      this.chromaAddMinutes(1);
      if (d.hour < beforeHour) {
        d.dayCount += 1;
      }
    }

    this.chromaDayNightApplyTint(false);
  };

  Game_System.prototype.chromaDayNightApplyTint = function(force) {
    if (!$gameScreen) return;
    const d = this.chromaDayNightData();
    if (!d.autoTint) return;

    const tone = toneForHourMinute(d.hour, d.minute);
    const snapshot = `${tone[0]},${tone[1]},${tone[2]},${tone[3]}`;
    if (!force && snapshot === d.lastTintSnapshot) return;

    d.lastTintSnapshot = snapshot;
    const duration = force ? 12 : 45;
    $gameScreen.startTint(tone, duration);
  };

  const _Game_System_initialize = Game_System.prototype.initialize;
  Game_System.prototype.initialize = function() {
    _Game_System_initialize.call(this);
    this.chromaInitDayNightData();
  };

  const _DataManager_extractSaveContents = DataManager.extractSaveContents;
  DataManager.extractSaveContents = function(contents) {
    _DataManager_extractSaveContents.call(this, contents);
    if ($gameSystem && $gameSystem.chromaInitDayNightData) {
      $gameSystem.chromaInitDayNightData();
      $gameSystem.chromaDayNightApplyTint(true);
    }
  };

  const _Game_Map_update = Game_Map.prototype.update;
  Game_Map.prototype.update = function(sceneActive) {
    _Game_Map_update.call(this, sceneActive);
    if (sceneActive && $gameSystem && $gameSystem.chromaDayNightUpdate) {
      $gameSystem.chromaDayNightUpdate();
    }
  };

  PluginManager.registerCommand(pluginName, "SetTime", (args) => {
    $gameSystem.chromaSetTime(args.hour, args.minute);
  });

  PluginManager.registerCommand(pluginName, "AddHours", (args) => {
    $gameSystem.chromaAddHours(args.amount);
  });

  PluginManager.registerCommand(pluginName, "AddMinutes", (args) => {
    $gameSystem.chromaAddMinutes(args.amount);
  });

  PluginManager.registerCommand(pluginName, "SetPaused", (args) => {
    $gameSystem.chromaSetDayNightPaused(toBool(args.value));
  });

  PluginManager.registerCommand(pluginName, "TogglePaused", () => {
    const now = $gameSystem.chromaSetDayNightPaused(!$gameSystem.chromaDayNightData().paused);
    if (!now) {
      $gameSystem.chromaDayNightApplyTint(true);
    }
  });

  PluginManager.registerCommand(pluginName, "SetAutoTint", (args) => {
    $gameSystem.chromaSetDayNightAutoTint(toBool(args.value));
    $gameSystem.chromaDayNightApplyTint(true);
  });

  PluginManager.registerCommand(pluginName, "GetTime", (args) => {
    setVariable(args.hourVariableId, $gameSystem.chromaDayNightHour());
    setVariable(args.minuteVariableId, $gameSystem.chromaDayNightMinute());
    setVariable(args.periodVariableId, PERIOD_CODE[$gameSystem.chromaDayNightPeriod()] || 0);
  });

  PluginManager.registerCommand(pluginName, "CheckIsNight", (args) => {
    setSwitch(args.switchId, $gameSystem.chromaDayNightIsNight());
  });

  const g = typeof window !== "undefined" ? window : globalThis;
  g.Imported = g.Imported || {};
  g.Imported.ChromaEdge_DayNightSystem = true;
  g.ChromaEdge = g.ChromaEdge || {};

  g.ChromaEdge.DayNight = {
    hour() {
      return $gameSystem ? $gameSystem.chromaDayNightHour() : startHour;
    },
    minute() {
      return $gameSystem ? $gameSystem.chromaDayNightMinute() : startMinute;
    },
    period() {
      return $gameSystem ? $gameSystem.chromaDayNightPeriod() : periodForHour(startHour);
    },
    periodCode() {
      return PERIOD_CODE[this.period()] || 0;
    },
    isNight() {
      return $gameSystem ? $gameSystem.chromaDayNightIsNight() : false;
    },
    tick() {
      return $gameSystem ? $gameSystem.chromaDayNightTick() : 0;
    },
    setTime(hour, minute = 0) {
      return $gameSystem ? $gameSystem.chromaSetTime(hour, minute) : null;
    },
    addHours(amount) {
      return $gameSystem ? $gameSystem.chromaAddHours(amount) : null;
    },
    addMinutes(amount) {
      return $gameSystem ? $gameSystem.chromaAddMinutes(amount) : null;
    },
    pause() {
      return $gameSystem ? $gameSystem.chromaSetDayNightPaused(true) : true;
    },
    resume() {
      return $gameSystem ? $gameSystem.chromaSetDayNightPaused(false) : false;
    },
    paused() {
      return $gameSystem ? !!$gameSystem.chromaDayNightData().paused : false;
    },
    setAutoTint(value) {
      if (!$gameSystem) return false;
      $gameSystem.chromaSetDayNightAutoTint(!!value);
      $gameSystem.chromaDayNightApplyTint(true);
      return !!value;
    },
  };
})();
