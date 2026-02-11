#!/usr/bin/env python3
"""
Content integrity validator for canonical assets/data content packs.

Checks:
1. Quest IDs are unique across all quest packs.
2. Quest references resolve (`prerequisites`, `unlocks`, reward quest unlocks).
3. Non-quest gate fields are explicit (`prerequisite_flags`, `unlock_flags`).
4. Quest steps reference valid maps/NPCs/items.
5. Main-story cohesion: `type=main` quests should not depend on non-main quests.
6. Prerequisite graph is acyclic.
7. Optional map-NPC anchor coherence (`target_npc` should be anchored on target map).
"""

from __future__ import annotations

import argparse
import json
import sys
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
        description="Validate canonical content integrity in assets/data."
    )
    parser.add_argument(
        "--quests-dir",
        default="assets/data/quests",
        help="Directory containing quest_*.json packs (default: assets/data/quests)",
    )
    parser.add_argument(
        "--maps-dir",
        default="assets/data/maps",
        help="Directory containing map_*.json files (default: assets/data/maps)",
    )
    parser.add_argument(
        "--npcs-dir",
        default="assets/data/npcs",
        help="Directory containing npc_*.json files (default: assets/data/npcs)",
    )
    parser.add_argument(
        "--items-dir",
        default="assets/data/items",
        help="Directory containing item_*.json files (default: assets/data/items)",
    )
    parser.add_argument(
        "--strict-mainline",
        action="store_true",
        help="Treat main-quest dependency on non-main quest types as errors.",
    )
    parser.add_argument(
        "--scope",
        choices=("all", "core"),
        default="all",
        help="Quest pack scope: all (default) or core runtime packs only.",
    )
    parser.add_argument(
        "--strict-map-npc-anchors",
        action="store_true",
        help="Treat missing map NPC anchors for quest target_npc as errors.",
    )
    return parser.parse_args()


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def load_map_ids(maps_dir: Path) -> set[str]:
    map_ids: set[str] = set()
    for path in sorted(maps_dir.glob("map_*.json")):
        data = load_json(path)
        if isinstance(data.get("maps"), list):
            for rec in data["maps"]:
                if isinstance(rec, dict):
                    map_id = rec.get("id")
                    if isinstance(map_id, str) and map_id:
                        map_ids.add(map_id)
        else:
            map_id = data.get("id")
            if isinstance(map_id, str) and map_id:
                map_ids.add(map_id)
    return map_ids


def map_npc_anchor_set(record: dict[str, Any]) -> set[str]:
    npcs: set[str] = set()

    key_npcs = record.get("key_npcs")
    if isinstance(key_npcs, list):
        for npc in key_npcs:
            if isinstance(npc, str) and npc:
                npcs.add(npc)

    ambient = record.get("ambient_npcs")
    if isinstance(ambient, list):
        for rec in ambient:
            if not isinstance(rec, dict):
                continue
            npc = rec.get("npc")
            if isinstance(npc, str) and npc:
                npcs.add(npc)

    interiors = record.get("interiors")
    if isinstance(interiors, list):
        for interior in interiors:
            if not isinstance(interior, dict):
                continue
            host_npc = interior.get("npc")
            if isinstance(host_npc, str) and host_npc:
                npcs.add(host_npc)
            i_ambient = interior.get("ambient_npcs")
            if isinstance(i_ambient, list):
                for rec in i_ambient:
                    if not isinstance(rec, dict):
                        continue
                    npc = rec.get("npc")
                    if isinstance(npc, str) and npc:
                        npcs.add(npc)

    return npcs


def load_map_npc_anchors(maps_dir: Path) -> dict[str, set[str]]:
    out: dict[str, set[str]] = {}
    for path in sorted(maps_dir.glob("map_*.json")):
        data = load_json(path)
        entries = data.get("maps") if isinstance(data.get("maps"), list) else [data]
        for rec in entries:
            if not isinstance(rec, dict):
                continue
            map_id = rec.get("id")
            if not isinstance(map_id, str) or not map_id:
                continue
            if map_id in out:
                continue
            out[map_id] = map_npc_anchor_set(rec)
    return out


def collect_quest_paths(quests_dir: Path, scope: str) -> tuple[list[Path], list[Issue]]:
    issues: list[Issue] = []
    if scope == "all":
        return sorted(quests_dir.glob("quest_*.json")), issues

    paths: list[Path] = []
    for name in CORE_QUEST_PACKS:
        path = quests_dir / name
        if not path.exists():
            issues.append(
                Issue(
                    "error",
                    "inputs",
                    f"Missing core quest pack required for scope=core: {path}",
                )
            )
            continue
        paths.append(path)
    return paths, issues


def load_npc_ids(npcs_dir: Path) -> set[str]:
    npc_ids: set[str] = set()
    for path in sorted(npcs_dir.glob("*.json")):
        data = load_json(path)
        npc_id = data.get("id")
        if isinstance(npc_id, str) and npc_id:
            npc_ids.add(npc_id)
    return npc_ids


def load_item_ids(items_dir: Path) -> set[str]:
    item_ids: set[str] = set()
    for path in sorted(items_dir.glob("*.json")):
        data = load_json(path)
        for rec in data.get("items", []):
            if isinstance(rec, dict):
                item_id = rec.get("id")
                if isinstance(item_id, str) and item_id:
                    item_ids.add(item_id)
    return item_ids


def iter_quests(
    quest_paths: list[Path],
) -> tuple[
    dict[str, tuple[Path, dict[str, Any]]],
    list[tuple[str, Path, dict[str, Any]]],
    list[Issue],
]:
    issues: list[Issue] = []
    quest_index: dict[str, tuple[Path, dict[str, Any]]] = {}
    ordered: list[tuple[str, Path, dict[str, Any]]] = []

    for path in quest_paths:
        data = load_json(path)
        quests = data.get("quests", [])
        if not isinstance(quests, list):
            issues.append(
                Issue("error", "schema", f"{path}: top-level `quests` must be a list")
            )
            continue
        for q in quests:
            if not isinstance(q, dict):
                issues.append(
                    Issue(
                        "error", "schema", f"{path}: quest entry must be an object"
                    )
                )
                continue
            quest_id = q.get("id")
            if not isinstance(quest_id, str) or not quest_id:
                issues.append(
                    Issue("error", "schema", f"{path}: quest missing string id")
                )
                continue
            if quest_id in quest_index:
                prev_path = quest_index[quest_id][0]
                issues.append(
                    Issue(
                        "error",
                        "duplicate_quest_id",
                        f"Quest id '{quest_id}' appears in both {prev_path} and {path}",
                    )
                )
                continue
            quest_index[quest_id] = (path, q)
            ordered.append((quest_id, path, q))
    return quest_index, ordered, issues


def ensure_string_list(
    value: Any, field: str, quest_id: str, path: Path, issues: list[Issue]
) -> list[str]:
    if value is None:
        return []
    if not isinstance(value, list):
        issues.append(
            Issue(
                "error",
                "schema",
                f"{quest_id} ({path}) has non-list `{field}`",
            )
        )
        return []
    out: list[str] = []
    for idx, token in enumerate(value):
        if not isinstance(token, str) or not token:
            issues.append(
                Issue(
                    "error",
                    "schema",
                    f"{quest_id} ({path}) has invalid `{field}[{idx}]` (must be non-empty string)",
                )
            )
            continue
        out.append(token)
    return out


def detect_cycles(graph: dict[str, set[str]]) -> list[list[str]]:
    WHITE = 0
    GRAY = 1
    BLACK = 2

    state: dict[str, int] = {node: WHITE for node in graph}
    parent: dict[str, str | None] = {node: None for node in graph}
    cycles: list[list[str]] = []

    def build_cycle(start: str, end: str) -> list[str]:
        chain = [start]
        cur = end
        while cur is not None and cur != start:
            chain.append(cur)
            cur = parent[cur]
        chain.append(start)
        chain.reverse()
        return chain

    def dfs(node: str) -> None:
        state[node] = GRAY
        for nxt in graph.get(node, set()):
            if state.get(nxt, WHITE) == WHITE:
                parent[nxt] = node
                dfs(nxt)
            elif state.get(nxt) == GRAY:
                cycles.append(build_cycle(nxt, node))
        state[node] = BLACK

    for node in sorted(graph):
        if state[node] == WHITE:
            dfs(node)
    return cycles


def run_validation(args: argparse.Namespace) -> list[Issue]:
    issues: list[Issue] = []

    quests_dir = Path(args.quests_dir)
    maps_dir = Path(args.maps_dir)
    npcs_dir = Path(args.npcs_dir)
    items_dir = Path(args.items_dir)

    for p, label in (
        (quests_dir, "quests"),
        (maps_dir, "maps"),
        (npcs_dir, "npcs"),
        (items_dir, "items"),
    ):
        if not p.exists():
            issues.append(Issue("error", "inputs", f"Missing {label} dir: {p}"))
    if any(i.severity == "error" and i.category == "inputs" for i in issues):
        return issues

    map_ids = load_map_ids(maps_dir)
    map_npc_anchors = load_map_npc_anchors(maps_dir)
    npc_ids = load_npc_ids(npcs_dir)
    item_ids = load_item_ids(items_dir)

    quest_paths, quest_path_issues = collect_quest_paths(quests_dir, args.scope)
    issues.extend(quest_path_issues)
    if any(i.severity == "error" and i.category == "inputs" for i in issues):
        return issues

    quest_index, quests, quest_index_issues = iter_quests(quest_paths)
    issues.extend(quest_index_issues)

    # Build quick type lookup for mainline cohesion checks.
    quest_type: dict[str, str] = {}
    for qid, _, q in quests:
        qtype = q.get("type")
        if isinstance(qtype, str) and qtype:
            quest_type[qid] = qtype
        else:
            quest_type[qid] = "unknown"

    prereq_graph: dict[str, set[str]] = {qid: set() for qid, _, _ in quests}

    for quest_id, path, quest in quests:
        prereqs = ensure_string_list(
            quest.get("prerequisites"), "prerequisites", quest_id, path, issues
        )
        unlocks = ensure_string_list(
            quest.get("unlocks"), "unlocks", quest_id, path, issues
        )
        ensure_string_list(
            quest.get("prerequisite_flags"),
            "prerequisite_flags",
            quest_id,
            path,
            issues,
        )
        ensure_string_list(
            quest.get("unlock_flags"),
            "unlock_flags",
            quest_id,
            path,
            issues,
        )

        for dep in prereqs:
            if dep not in quest_index:
                issues.append(
                    Issue(
                        "error",
                        "quest_refs",
                        f"{quest_id} ({path}) prerequisite '{dep}' does not resolve",
                    )
                )
            else:
                prereq_graph[quest_id].add(dep)

        for uq in unlocks:
            if uq not in quest_index:
                issues.append(
                    Issue(
                        "error",
                        "quest_refs",
                        f"{quest_id} ({path}) unlock '{uq}' does not resolve",
                    )
                )

        steps = quest.get("steps")
        if not isinstance(steps, list):
            issues.append(
                Issue("error", "schema", f"{quest_id} ({path}) has non-list `steps`")
            )
            continue
        if not steps:
            issues.append(
                Issue("warning", "quest_steps", f"{quest_id} ({path}) has no steps")
            )

        step_ids: set[int] = set()
        for idx, step in enumerate(steps):
            if not isinstance(step, dict):
                issues.append(
                    Issue(
                        "error",
                        "schema",
                        f"{quest_id} ({path}) has non-object step at index {idx}",
                    )
                )
                continue

            sid = step.get("id")
            if isinstance(sid, int):
                if sid in step_ids:
                    issues.append(
                        Issue(
                            "warning",
                            "quest_steps",
                            f"{quest_id} ({path}) has duplicate step id {sid}",
                        )
                    )
                step_ids.add(sid)

            loc = step.get("target_location")
            if isinstance(loc, str) and loc and loc not in map_ids:
                issues.append(
                    Issue(
                        "error",
                        "map_refs",
                        f"{quest_id} ({path}) step {sid} target_location '{loc}' does not resolve",
                    )
                )

            npc = step.get("target_npc")
            if isinstance(npc, str) and npc and npc not in npc_ids:
                issues.append(
                    Issue(
                        "error",
                        "npc_refs",
                        f"{quest_id} ({path}) step {sid} target_npc '{npc}' does not resolve",
                    )
                )
            if (
                isinstance(loc, str)
                and loc
                and loc in map_ids
                and isinstance(npc, str)
                and npc
                and npc in npc_ids
                and npc not in map_npc_anchors.get(loc, set())
            ):
                sev = "error" if args.strict_map_npc_anchors else "warning"
                issues.append(
                    Issue(
                        sev,
                        "npc_anchor_refs",
                        f"{quest_id} ({path}) step {sid} target_npc '{npc}' is not anchored on map '{loc}' key/interior/ambient NPC metadata",
                    )
                )

            rewards = step.get("rewards")
            if isinstance(rewards, dict):
                reward_unlocks = ensure_string_list(
                    rewards.get("unlocks"),
                    "rewards.unlocks",
                    quest_id,
                    path,
                    issues,
                )
                ensure_string_list(
                    rewards.get("unlock_flags"),
                    "rewards.unlock_flags",
                    quest_id,
                    path,
                    issues,
                )
                for uq in reward_unlocks:
                    if uq not in quest_index:
                        issues.append(
                            Issue(
                                "error",
                                "quest_refs",
                                f"{quest_id} ({path}) step {sid} reward unlock '{uq}' does not resolve",
                            )
                        )
                items = rewards.get("items")
                if items is not None and not isinstance(items, list):
                    issues.append(
                        Issue(
                            "error",
                            "schema",
                            f"{quest_id} ({path}) step {sid} rewards.items must be a list",
                        )
                    )
                if isinstance(items, list):
                    for item_rec in items:
                        if not isinstance(item_rec, dict):
                            issues.append(
                                Issue(
                                    "error",
                                    "schema",
                                    f"{quest_id} ({path}) step {sid} has non-object reward item",
                                )
                            )
                            continue
                        item_id = item_rec.get("item")
                        if isinstance(item_id, str) and item_id and item_id not in item_ids:
                            issues.append(
                                Issue(
                                    "error",
                                    "item_refs",
                                    f"{quest_id} ({path}) step {sid} reward item '{item_id}' does not resolve",
                                )
                            )

        top_rewards = quest.get("rewards")
        if isinstance(top_rewards, dict):
            top_unlocks = ensure_string_list(
                top_rewards.get("unlocks"),
                "rewards.unlocks",
                quest_id,
                path,
                issues,
            )
            ensure_string_list(
                top_rewards.get("unlock_flags"),
                "rewards.unlock_flags",
                quest_id,
                path,
                issues,
            )
            for uq in top_unlocks:
                if uq not in quest_index:
                    issues.append(
                        Issue(
                            "error",
                            "quest_refs",
                            f"{quest_id} ({path}) reward unlock '{uq}' does not resolve",
                        )
                    )
            top_items = top_rewards.get("items")
            if top_items is not None and not isinstance(top_items, list):
                issues.append(
                    Issue(
                        "error",
                        "schema",
                        f"{quest_id} ({path}) rewards.items must be a list",
                    )
                )
            if isinstance(top_items, list):
                for item_rec in top_items:
                    if not isinstance(item_rec, dict):
                        issues.append(
                            Issue(
                                "error",
                                "schema",
                                f"{quest_id} ({path}) has non-object reward item",
                            )
                        )
                        continue
                    item_id = item_rec.get("item")
                    if isinstance(item_id, str) and item_id and item_id not in item_ids:
                        issues.append(
                            Issue(
                                "error",
                                "item_refs",
                                f"{quest_id} ({path}) reward item '{item_id}' does not resolve",
                            )
                        )

    # Mainline cohesion: main quests should not require non-main quests.
    for quest_id, path, quest in quests:
        if quest_type.get(quest_id) != "main":
            continue
        prereqs = quest.get("prerequisites", [])
        if not isinstance(prereqs, list):
            continue
        for dep in prereqs:
            if not isinstance(dep, str):
                continue
            dep_type = quest_type.get(dep, "unknown")
            if dep_type != "main":
                sev = "error" if args.strict_mainline else "warning"
                issues.append(
                    Issue(
                        sev,
                        "mainline_cohesion",
                        f"{quest_id} ({path}) depends on non-main quest {dep} (type={dep_type})",
                    )
                )

    # Cycle detection on prerequisite graph.
    for cyc in detect_cycles(prereq_graph):
        issues.append(
            Issue(
                "error",
                "quest_cycles",
                "Prerequisite cycle: " + " -> ".join(cyc),
            )
        )

    return issues


def main() -> int:
    args = parse_args()
    issues = run_validation(args)

    errors = [x for x in issues if x.severity == "error"]
    warnings = [x for x in issues if x.severity == "warning"]

    print("=" * 64)
    print("CONTENT INTEGRITY VALIDATION")
    print("=" * 64)
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")
    if issues:
        print("-" * 64)
        for issue in issues:
            print(f"[{issue.severity.upper():7}] {issue.category:18} {issue.detail}")
    else:
        print("\nContent integrity checks passed.")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
