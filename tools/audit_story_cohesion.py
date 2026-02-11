#!/usr/bin/env python3
"""
Story cohesion audit for canonical quest/map content.

Checks:
1. Quest step target locations resolve to canonical maps.
2. Quest step target NPCs are anchored on target maps (key/ambient/interior NPC lists).
3. Quests targeting act 2+ locations have explicit gating
   (`prerequisites` or `prerequisite_flags`).
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
        description="Audit story cohesion across quests and canonical maps."
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
        "--scope",
        choices=("core", "all"),
        default="core",
        help="Quest pack scope: core (curated runtime) or all (includes generated content packs).",
    )
    parser.add_argument(
        "--strict-act-gating",
        action="store_true",
        help="Treat missing act gating for act 2+ quest targets as errors.",
    )
    parser.add_argument(
        "--strict-npc-anchors",
        action="store_true",
        help="Treat missing map NPC anchors as errors for all scopes.",
    )
    return parser.parse_args()


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def iter_map_records(maps_dir: Path) -> list[tuple[Path, dict[str, Any]]]:
    out: list[tuple[Path, dict[str, Any]]] = []
    for path in sorted(maps_dir.glob("map_*.json")):
        data = load_json(path)
        entries = data.get("maps") if isinstance(data.get("maps"), list) else [data]
        for rec in entries:
            if isinstance(rec, dict):
                out.append((path, rec))
    return out


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


def collect_quest_files(quests_dir: Path, scope: str) -> tuple[list[Path], list[Issue]]:
    issues: list[Issue] = []
    if scope == "all":
        files = sorted(quests_dir.glob("quest_*.json"))
        return files, issues

    files: list[Path] = []
    for name in CORE_QUEST_PACKS:
        path = quests_dir / name
        if not path.exists():
            issues.append(
                Issue("error", "inputs", f"Missing core quest pack required for scope=core: {path}")
            )
            continue
        files.append(path)
    return files, issues


def as_string_list(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    out: list[str] = []
    for item in value:
        if isinstance(item, str) and item:
            out.append(item)
    return out


def run_audit(args: argparse.Namespace) -> tuple[list[Issue], dict[str, int]]:
    issues: list[Issue] = []
    stats = {
        "maps": 0,
        "quests": 0,
        "steps": 0,
    }

    quests_dir = Path(args.quests_dir)
    maps_dir = Path(args.maps_dir)
    if not quests_dir.exists():
        issues.append(Issue("error", "inputs", f"Missing quests dir: {quests_dir}"))
        return issues, stats
    if not maps_dir.exists():
        issues.append(Issue("error", "inputs", f"Missing maps dir: {maps_dir}"))
        return issues, stats

    map_index: dict[str, tuple[Path, dict[str, Any]]] = {}
    map_npcs: dict[str, set[str]] = {}
    map_act: dict[str, int] = {}
    for path, rec in iter_map_records(maps_dir):
        map_id = rec.get("id")
        if not isinstance(map_id, str) or not map_id:
            continue
        if map_id in map_index:
            issues.append(
                Issue(
                    "error",
                    "maps",
                    f"Duplicate map id '{map_id}' in {path} and {map_index[map_id][0]}",
                )
            )
            continue
        map_index[map_id] = (path, rec)
        map_npcs[map_id] = map_npc_anchor_set(rec)
        raw_act = rec.get("act")
        if isinstance(raw_act, int):
            map_act[map_id] = raw_act
    stats["maps"] = len(map_index)

    quest_files, file_issues = collect_quest_files(quests_dir, args.scope)
    issues.extend(file_issues)
    if any(i.severity == "error" and i.category == "inputs" for i in issues):
        return issues, stats

    for pack in quest_files:
        data = load_json(pack)
        quests = data.get("quests")
        if not isinstance(quests, list):
            issues.append(
                Issue("error", "schema", f"{pack}: top-level `quests` must be a list")
            )
            continue

        for quest in quests:
            if not isinstance(quest, dict):
                issues.append(
                    Issue("error", "schema", f"{pack}: quest entry must be an object")
                )
                continue
            quest_id = quest.get("id")
            if not isinstance(quest_id, str) or not quest_id:
                issues.append(Issue("error", "schema", f"{pack}: quest missing string id"))
                continue

            stats["quests"] += 1

            prereqs = as_string_list(quest.get("prerequisites"))
            prereq_flags = as_string_list(quest.get("prerequisite_flags"))
            has_gating = bool(prereqs or prereq_flags)

            steps = quest.get("steps")
            if not isinstance(steps, list):
                issues.append(
                    Issue("error", "schema", f"{quest_id} ({pack}) has non-list `steps`")
                )
                continue

            targeted_acts: list[int] = []
            for idx, step in enumerate(steps):
                stats["steps"] += 1
                if not isinstance(step, dict):
                    issues.append(
                        Issue(
                            "error",
                            "schema",
                            f"{quest_id} ({pack}) has non-object step at index {idx}",
                        )
                    )
                    continue

                step_id = step.get("id")
                sid = step_id if isinstance(step_id, int) else idx + 1
                target_location = step.get("target_location")
                target_npc = step.get("target_npc")

                if isinstance(target_location, str) and target_location:
                    if target_location not in map_index:
                        issues.append(
                            Issue(
                                "error",
                                "map_refs",
                                f"{quest_id} ({pack}) step {sid} target_location '{target_location}' does not resolve",
                            )
                        )
                    else:
                        act = map_act.get(target_location)
                        if isinstance(act, int):
                            targeted_acts.append(act)

                if (
                    isinstance(target_location, str)
                    and target_location
                    and isinstance(target_npc, str)
                    and target_npc
                    and target_location in map_index
                    and target_npc not in map_npcs.get(target_location, set())
                ):
                    sev = (
                        "error"
                        if args.scope == "core" or args.strict_npc_anchors
                        else "warning"
                    )
                    issues.append(
                        Issue(
                            sev,
                            "npc_anchors",
                            f"{quest_id} ({pack}) step {sid} targets NPC '{target_npc}' on {target_location}, but that map has no NPC anchor for it",
                        )
                    )

            if targeted_acts:
                min_act = min(targeted_acts)
                if min_act >= 2 and not has_gating:
                    sev = "error" if args.strict_act_gating else "warning"
                    issues.append(
                        Issue(
                            sev,
                            "act_gating",
                            f"{quest_id} ({pack}) targets act {min_act}+ locations with no prerequisites/prerequisite_flags",
                        )
                    )

    return issues, stats


def main() -> int:
    args = parse_args()
    issues, stats = run_audit(args)
    errors = [x for x in issues if x.severity == "error"]
    warnings = [x for x in issues if x.severity == "warning"]

    print("=" * 64)
    print("STORY COHESION AUDIT")
    print("=" * 64)
    print(f"Scope: {args.scope}")
    print(f"Maps scanned: {stats['maps']}")
    print(f"Quests scanned: {stats['quests']}")
    print(f"Steps scanned: {stats['steps']}")
    print("-" * 64)
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")

    if issues:
        print("-" * 64)
        for issue in issues:
            print(f"[{issue.severity.upper():7}] {issue.category:14} {issue.detail}")
    else:
        print("\nStory cohesion checks passed.")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
