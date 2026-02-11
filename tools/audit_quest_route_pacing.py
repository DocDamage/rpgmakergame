#!/usr/bin/env python3
"""
Audit quest route pacing/cohesion against canonical map connectivity.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import deque
from dataclasses import dataclass
from pathlib import Path
from typing import Any


CORE_QUEST_PACKS = (
    "quest_main_story.json",
    "quest_side_stories.json",
    "quest_generated_placeholders.json",
)


@dataclass(frozen=True)
class Issue:
    severity: str
    category: str
    detail: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Audit quest route pacing and reachability using canonical map graph."
    )
    parser.add_argument(
        "--maps-dir",
        default="assets/data/maps",
        help="Directory containing map_*.json files (default: assets/data/maps).",
    )
    parser.add_argument(
        "--quests-dir",
        default="assets/data/quests",
        help="Directory containing quest_*.json packs (default: assets/data/quests).",
    )
    parser.add_argument(
        "--scope",
        choices=("core", "all"),
        default="core",
        help="Quest pack scope: core or all (default: core).",
    )
    parser.add_argument(
        "--warn-hop-threshold",
        type=int,
        default=6,
        help="Warn when directed path hop count exceeds this value (default: 6).",
    )
    parser.add_argument(
        "--main-only",
        action="store_true",
        help="Only evaluate quests where type == 'main'.",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as errors.",
    )
    return parser.parse_args()


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def collect_quest_paths(quests_dir: Path, scope: str) -> tuple[list[Path], list[Issue]]:
    issues: list[Issue] = []
    if scope == "all":
        return sorted(quests_dir.glob("quest_*.json")), issues

    out: list[Path] = []
    for filename in CORE_QUEST_PACKS:
        path = quests_dir / filename
        if not path.exists():
            issues.append(
                Issue(
                    "error",
                    "inputs",
                    f"Missing core quest pack required for scope=core: {path}",
                )
            )
            continue
        out.append(path)
    return out, issues


def map_graph(maps_dir: Path) -> tuple[dict[str, set[str]], set[str], set[str], list[Issue]]:
    issues: list[Issue] = []
    ids: set[str] = set()
    graph: dict[str, set[str]] = {}
    overworld_roots: set[str] = set()

    records: list[dict[str, Any]] = []
    for path in sorted(maps_dir.glob("map_*.json")):
        data = load_json(path)
        entries = data.get("maps") if isinstance(data.get("maps"), list) else [data]
        for rec in entries:
            if not isinstance(rec, dict):
                continue
            map_id = rec.get("id")
            if not isinstance(map_id, str) or not map_id:
                continue
            if map_id in ids:
                issues.append(Issue("error", "maps", f"Duplicate map id detected: {map_id}"))
                continue
            ids.add(map_id)
            records.append(rec)
            if str(rec.get("type", "")).strip().lower() == "overworld":
                overworld_roots.add(map_id)

    for map_id in ids:
        graph[map_id] = set()

    for rec in records:
        src = rec.get("id")
        if not isinstance(src, str) or src not in ids:
            continue

        connections = rec.get("connections")
        if isinstance(connections, list):
            for conn in connections:
                if not isinstance(conn, dict):
                    continue
                target = conn.get("target")
                if isinstance(target, str) and target in ids:
                    graph[src].add(target)

        pois = rec.get("points_of_interest")
        if isinstance(pois, list):
            for poi in pois:
                if not isinstance(poi, dict):
                    continue
                target = poi.get("target")
                if isinstance(target, str) and target in ids:
                    graph[src].add(target)

    return graph, ids, overworld_roots, issues


def shortest_path_len(graph: dict[str, set[str]], src: str, dst: str) -> int | None:
    if src == dst:
        return 0
    if src not in graph or dst not in graph:
        return None
    seen = {src}
    q: deque[tuple[str, int]] = deque([(src, 0)])
    while q:
        node, dist = q.popleft()
        for nxt in graph.get(node, set()):
            if nxt == dst:
                return dist + 1
            if nxt in seen:
                continue
            seen.add(nxt)
            q.append((nxt, dist + 1))
    return None


def undirected_graph(graph: dict[str, set[str]]) -> dict[str, set[str]]:
    out: dict[str, set[str]] = {k: set() for k in graph}
    for src, targets in graph.items():
        for dst in targets:
            out.setdefault(src, set()).add(dst)
            out.setdefault(dst, set()).add(src)
    return out


def step_locations(quest: dict[str, Any]) -> list[str]:
    out: list[str] = []
    steps = quest.get("steps")
    if not isinstance(steps, list):
        return out
    for step in steps:
        if not isinstance(step, dict):
            continue
        loc = step.get("target_location")
        if isinstance(loc, str) and loc.strip():
            out.append(loc.strip())
    return out


def dedupe_consecutive(seq: list[str]) -> list[str]:
    out: list[str] = []
    for token in seq:
        if not out or out[-1] != token:
            out.append(token)
    return out


def run_audit(args: argparse.Namespace) -> tuple[list[Issue], dict[str, int]]:
    issues: list[Issue] = []
    stats = {
        "maps": 0,
        "quest_packs": 0,
        "quests_scanned": 0,
        "quests_with_locations": 0,
        "quest_transitions": 0,
        "checked_from_overworld": 0,
    }

    maps_dir = Path(args.maps_dir)
    quests_dir = Path(args.quests_dir)
    if not maps_dir.exists():
        issues.append(Issue("error", "inputs", f"Missing maps dir: {maps_dir}"))
        return issues, stats
    if not quests_dir.exists():
        issues.append(Issue("error", "inputs", f"Missing quests dir: {quests_dir}"))
        return issues, stats

    graph, map_ids, overworld_roots, graph_issues = map_graph(maps_dir)
    issues.extend(graph_issues)
    stats["maps"] = len(map_ids)
    undir = undirected_graph(graph)

    quest_paths, path_issues = collect_quest_paths(quests_dir, args.scope)
    issues.extend(path_issues)
    stats["quest_packs"] = len(quest_paths)

    for qpath in quest_paths:
        data = load_json(qpath)
        quests = data.get("quests")
        if not isinstance(quests, list):
            issues.append(Issue("error", "schema", f"{qpath} top-level `quests` must be a list"))
            continue
        for q in quests:
            if not isinstance(q, dict):
                continue
            qid = q.get("id")
            if not isinstance(qid, str) or not qid:
                continue
            qtype = q.get("type")
            if args.main_only and qtype != "main":
                continue
            stats["quests_scanned"] += 1

            locs = dedupe_consecutive(step_locations(q))
            if not locs:
                continue
            stats["quests_with_locations"] += 1

            for loc in locs:
                if loc not in map_ids:
                    issues.append(
                        Issue(
                            "error",
                            "quest_map_ref",
                            f"{qid} references missing target_location '{loc}'",
                        )
                    )

            if overworld_roots:
                # Check first stage reachability from any overworld root.
                first = locs[0]
                if first in map_ids:
                    stats["checked_from_overworld"] += 1
                    dists = [shortest_path_len(graph, root, first) for root in sorted(overworld_roots)]
                    dists = [d for d in dists if d is not None]
                    if not dists:
                        issues.append(
                            Issue(
                                "error",
                                "quest_start_unreachable",
                                f"{qid} first target '{first}' unreachable from overworld roots",
                            )
                        )

            for src, dst in zip(locs, locs[1:]):
                if src not in map_ids or dst not in map_ids:
                    continue
                stats["quest_transitions"] += 1
                directed = shortest_path_len(graph, src, dst)
                if directed is None:
                    und = shortest_path_len(undir, src, dst)
                    if und is None:
                        issues.append(
                            Issue(
                                "error",
                                "quest_route_unreachable",
                                f"{qid} has unreachable transition {src} -> {dst}",
                            )
                        )
                    else:
                        issues.append(
                            Issue(
                                "warning",
                                "quest_route_directional",
                                f"{qid} transition {src} -> {dst} only reachable if directionality is ignored (hops={und})",
                            )
                        )
                    continue
                if directed > args.warn_hop_threshold:
                    issues.append(
                        Issue(
                            "warning",
                            "quest_route_length",
                            f"{qid} transition {src} -> {dst} is long (hops={directed} > {args.warn_hop_threshold})",
                        )
                    )

    if args.strict:
        issues = [
            Issue("error", issue.category, issue.detail) if issue.severity == "warning" else issue
            for issue in issues
        ]
    return issues, stats


def main() -> int:
    args = parse_args()
    issues, stats = run_audit(args)
    errors = [i for i in issues if i.severity == "error"]
    warnings = [i for i in issues if i.severity == "warning"]

    print("=" * 68)
    print("QUEST ROUTE PACING AUDIT")
    print("=" * 68)
    print(f"Scope: {args.scope}")
    print(f"Main-only: {args.main_only}")
    print(f"Maps: {stats['maps']}")
    print(f"Quest packs: {stats['quest_packs']}")
    print(f"Quests scanned: {stats['quests_scanned']}")
    print(f"Quests with locations: {stats['quests_with_locations']}")
    print(f"Quest transitions checked: {stats['quest_transitions']}")
    print(f"First-target overworld checks: {stats['checked_from_overworld']}")
    print("-" * 68)
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")

    if issues:
        print("-" * 68)
        for issue in issues:
            print(f"[{issue.severity.upper():7}] {issue.category:26} {issue.detail}")
    else:
        print("\nQuest route pacing checks passed.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
