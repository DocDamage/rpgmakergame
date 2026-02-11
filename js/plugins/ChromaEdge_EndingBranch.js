/*:
 * @target MZ
 * @plugindesc v0.2.0 Ending route state (Free Prime/Anchor) with auto-evaluation and switch sync.
 * @author Chroma's Edge
 * @help
 * Persists final ending route decisions and exposes auto-evaluation logic.
 *
 * Route codes:
 * - none: 0
 * - free_prime: 1
 * - anchor: 2
 *
 * Script calls:
 *   ChromaEdge.Ending.evaluateAuto()
 *   ChromaEdge.Ending.choose("free_prime")
 *   ChromaEdge.Ending.route()
 *
 * @param freePrimeSwitchId
 * @text Free Prime Switch Id
 * @type switch
 * @default 50
 *
 * @param anchorSwitchId
 * @text Anchor Switch Id
 * @type switch
 * @default 51
 *
 * @param requireTowerCleared
 * @text Require Tower Cleared
 * @type boolean
 * @default true
 *
 * @param freePrimeMinMercyScore
 * @text Free Prime Min Mercy Score
 * @type number
 * @default 1
 *
 * @command EvaluateEndingRoute
 * @text Evaluate Ending Route
 * @arg variableId
 * @text Route Code Variable
 * @type variable
 * @default 0
 * @arg applyRoute
 * @text Apply Evaluated Route
 * @type boolean
 * @default false
 *
 * @command ChooseEndingRoute
 * @text Choose Ending Route
 * @arg route
 * @type select
 * @option Free Prime
 * @value free_prime
 * @option Anchor
 * @value anchor
 * @option Clear
 * @value none
 * @default free_prime
 * @arg switchId
 * @text Success Switch
 * @type switch
 * @default 0
 *
 * @command GetEndingRoute
 * @text Get Ending Route
 * @arg variableId
 * @type variable
 * @default 1
 *
 * @command CheckEndingRoute
 * @text Check Ending Route
 * @arg route
 * @type select
 * @option Free Prime
 * @value free_prime
 * @option Anchor
 * @value anchor
 * @default free_prime
 * @arg switchId
 * @type switch
 * @default 1
 */

(() => {
  "use strict";

  const pluginName = "ChromaEdge_EndingBranch";
  const params = PluginManager.parameters(pluginName);
  const freePrimeSwitchId = Number(params.freePrimeSwitchId || 50);
  const anchorSwitchId = Number(params.anchorSwitchId || 51);
  const requireTowerCleared =
    String(params.requireTowerCleared || "true").toLowerCase() === "true";
  const freePrimeMinMercyScore = Number(params.freePrimeMinMercyScore || 1);

  const ROUTE_CODE = {
    none: 0,
    free_prime: 1,
    anchor: 2,
  };

  const normalizeRoute = (route) => {
    const r = String(route || "").trim().toLowerCase();
    if (r === "free_prime" || r === "freeprime" || r === "prime") return "free_prime";
    if (r === "anchor") return "anchor";
    return "none";
  };

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

  const mercyApi = () => {
    const g = typeof window !== "undefined" ? window : globalThis;
    return g && g.ChromaEdge ? g.ChromaEdge.Mercy : null;
  };

  const towerApi = () => {
    const g = typeof window !== "undefined" ? window : globalThis;
    return g && g.ChromaEdge ? g.ChromaEdge.Tower : null;
  };

  const questApi = () => {
    const g = typeof window !== "undefined" ? window : globalThis;
    return g && g.ChromaEdge ? g.ChromaEdge.Quests : null;
  };

  const towerCleared = () => {
    const tower = towerApi();
    if (tower && typeof tower.eventFlag === "function") {
      if (tower.eventFlag("TOWER_CLEARED")) return true;
    }
    if (tower && typeof tower.progress === "function") {
      const progress = tower.progress();
      if (progress && Number(progress.highestClearedFloor) >= 100) return true;
    }
    if ($gameSwitches && $gameSwitches.value(40)) return true;
    return false;
  };

  const mercyScore = () => {
    const mercy = mercyApi();
    if (mercy && typeof mercy.score === "function") {
      return Number(mercy.score()) || 0;
    }
    return 0;
  };

  const canResolveEnding = () => {
    if (!requireTowerCleared) return true;
    return towerCleared();
  };

  Game_System.prototype.chromaInitEndingBranchData = function() {
    if (!this._chromaEndingBranch || typeof this._chromaEndingBranch !== "object") {
      this._chromaEndingBranch = {
        route: "none",
        seenRoutes: {},
        evaluatedRoute: "none",
        evaluatedAt: 0,
      };
    }

    const d = this._chromaEndingBranch;
    d.route = normalizeRoute(d.route);
    d.evaluatedRoute = normalizeRoute(d.evaluatedRoute);
    d.evaluatedAt = toInt(d.evaluatedAt, 0);
    d.seenRoutes = d.seenRoutes && typeof d.seenRoutes === "object" ? d.seenRoutes : {};

    this.chromaEndingBranchSyncSwitches();
  };

  Game_System.prototype.chromaEndingBranchData = function() {
    this.chromaInitEndingBranchData();
    return this._chromaEndingBranch;
  };

  Game_System.prototype.chromaEndingBranchSyncSwitches = function() {
    const d =
      this._chromaEndingBranch && typeof this._chromaEndingBranch === "object"
        ? this._chromaEndingBranch
        : null;
    const route = normalizeRoute(d ? d.route : "none");
    setSwitch(freePrimeSwitchId, route === "free_prime");
    setSwitch(anchorSwitchId, route === "anchor");
  };

  Game_System.prototype.chromaEvaluateEndingRoute = function() {
    const d = this.chromaEndingBranchData();

    let route = "none";
    if (canResolveEnding()) {
      route = mercyScore() >= freePrimeMinMercyScore ? "free_prime" : "anchor";
    }

    d.evaluatedRoute = route;
    d.evaluatedAt = Date.now();
    return route;
  };

  Game_System.prototype.chromaEndingRoute = function() {
    return this.chromaEndingBranchData().route;
  };

  Game_System.prototype.chromaChooseEndingRoute = function(route) {
    const normalized = normalizeRoute(route);
    const d = this.chromaEndingBranchData();

    if (normalized !== "none" && !canResolveEnding()) {
      return false;
    }

    d.route = normalized;
    if (normalized !== "none") {
      d.seenRoutes[normalized] = true;
    }

    this.chromaEndingBranchSyncSwitches();

    const q = questApi();
    if (q && typeof q.setFlag === "function") {
      q.setFlag("ENDING_FREE_PRIME", normalized === "free_prime");
      q.setFlag("ENDING_ANCHOR", normalized === "anchor");
    }

    return true;
  };

  Game_System.prototype.chromaEndingHasSeenRoute = function(route) {
    const key = normalizeRoute(route);
    if (key === "none") return false;
    return !!this.chromaEndingBranchData().seenRoutes[key];
  };

  Game_System.prototype.chromaEndingRouteCode = function() {
    const route = this.chromaEndingRoute();
    return ROUTE_CODE[route] == null ? ROUTE_CODE.none : ROUTE_CODE[route];
  };

  Game_System.prototype.chromaEndingEvaluatedRouteCode = function() {
    const route = this.chromaEvaluateEndingRoute();
    return ROUTE_CODE[route] == null ? ROUTE_CODE.none : ROUTE_CODE[route];
  };

  const _Game_System_initialize = Game_System.prototype.initialize;
  Game_System.prototype.initialize = function() {
    _Game_System_initialize.call(this);
    this.chromaInitEndingBranchData();
  };

  const _DataManager_extractSaveContents = DataManager.extractSaveContents;
  DataManager.extractSaveContents = function(contents) {
    _DataManager_extractSaveContents.call(this, contents);
    if ($gameSystem && $gameSystem.chromaInitEndingBranchData) {
      $gameSystem.chromaInitEndingBranchData();
    }
  };

  PluginManager.registerCommand(pluginName, "EvaluateEndingRoute", (args) => {
    const route = $gameSystem.chromaEvaluateEndingRoute();
    if (toBool(args.applyRoute)) {
      $gameSystem.chromaChooseEndingRoute(route);
    }
    setVariable(args.variableId, ROUTE_CODE[route] == null ? ROUTE_CODE.none : ROUTE_CODE[route]);
  });

  PluginManager.registerCommand(pluginName, "ChooseEndingRoute", (args) => {
    const ok = $gameSystem.chromaChooseEndingRoute(args.route);
    setSwitch(args.switchId, ok);
  });

  PluginManager.registerCommand(pluginName, "GetEndingRoute", (args) => {
    setVariable(args.variableId, $gameSystem.chromaEndingRouteCode());
  });

  PluginManager.registerCommand(pluginName, "CheckEndingRoute", (args) => {
    const ok = $gameSystem.chromaEndingRoute() === normalizeRoute(args.route);
    setSwitch(args.switchId, ok);
  });

  const g = typeof window !== "undefined" ? window : globalThis;
  g.Imported = g.Imported || {};
  g.Imported.ChromaEdge_EndingBranch = true;
  g.ChromaEdge = g.ChromaEdge || {};

  g.ChromaEdge.Ending = {
    route() {
      return $gameSystem ? $gameSystem.chromaEndingRoute() : "none";
    },
    routeCode() {
      return $gameSystem ? $gameSystem.chromaEndingRouteCode() : ROUTE_CODE.none;
    },
    evaluateAuto() {
      return $gameSystem ? $gameSystem.chromaEvaluateEndingRoute() : "none";
    },
    evaluateAutoCode() {
      return $gameSystem ? $gameSystem.chromaEndingEvaluatedRouteCode() : ROUTE_CODE.none;
    },
    choose(route) {
      return $gameSystem ? $gameSystem.chromaChooseEndingRoute(route) : false;
    },
    canResolve() {
      return canResolveEnding();
    },
    hasSeen(route) {
      return $gameSystem ? $gameSystem.chromaEndingHasSeenRoute(route) : false;
    },
    mercyScore() {
      return mercyScore();
    },
  };
})();
