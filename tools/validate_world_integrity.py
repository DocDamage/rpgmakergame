#!/usr/bin/env python3
"""
World integrity validator for Chroma's Edge.

Checks:
1. Map connection targets resolve to existing map IDs.
2. Main-quest stage-to-stage map hops are connected.
3. Encounter table references resolve and include the map that references them.
4. Gate trigger/condition tokens are sane (event-backed or known capability flags).
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


KNOWN_GATE_TOKENS = {
    "flight",
    "submersible",
    "ACT3_UNLOCKED",
    "POST_GAME_UNLOCKED",
    "ALL_WINGS_CLEARED",
}

KNOWN_GATE_PATTERNS = [
    re.compile(r"^f\d+_(cleared|unlocked)$", re.IGNORECASE),
    re.compile(r"^puzzle_solved$", re.IGNORECASE),
]


@dataclass(frozen=True)
class Issue:
    severity: str
    category: str
    detail: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate map/quest/encounter world integrity."
    )
    parser.add_argument(
        "--maps-dir",
        default="assets/data/maps",
        help="Directory containing map_*.json files (default: assets/data/maps)",
    )
    parser.add_argument(
        "--encounters-dir",
        default="assets/data/encounters",
        help="Directory containing encounter_*.json files (default: assets/data/encounters)",
    )
    parser.add_argument(
        "--quests-dir",
        default="content/quests/main",
        help="Directory containing main quest json files (default: content/quests/main)",
    )
    parser.add_argument(
        "--strict-gates",
        action="store_true",
        help="Treat unknown gate trigger/condition tokens as errors.",
    )
    return parser.parse_args()


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def iter_map_records(maps_dir: Path) -> list[tuple[Path, dict[str, Any]]]:
    records: list[tuple[Path, dict[str, Any]]] = []
    for path in sorted(maps_dir.glob("map_*.json")):
        data = load_json(path)
        if isinstance(data.get("maps"), list):
            for entry in data["maps"]:
                if isinstance(entry, dict):
                    records.append((path, entry))
            continue
        if isinstance(data, dict):
            records.append((path, data))
    return records


def iter_encounters(encounters_dir: Path) -> list[tuple[Path, dict[str, Any]]]:
    out: list[tuple[Path, dict[str, Any]]] = []
    for path in sorted(encounters_dir.glob("encounter_*.json")):
        data = load_json(path)
        if isinstance(data, dict):
            out.append((path, data))
    return out


def is_known_gate(token: str, event_set: set[str], event_set_lower: set[str]) -> bool:
    if token in KNOWN_GATE_TOKENS:
        return True
    if token in event_set:
        return True
    if token.upper() in event_set:
        return True
    if token.lower() in event_set_lower:
        return True
    return any(pattern.match(token) for pattern in KNOWN_GATE_PATTERNS)


def run_validation(args: argparse.Namespace) -> list[Issue]:
    issues: list[Issue] = []

    maps_dir = Path(args.maps_dir)
    encounters_dir = Path(args.encounters_dir)
    quests_dir = Path(args.quests_dir)

    if not maps_dir.exists():
        issues.append(Issue("error", "inputs", f"Missing maps dir: {maps_dir}"))
        return issues
    if not encounters_dir.exists():
        issues.append(
            Issue("error", "inputs", f"Missing encounters dir: {encounters_dir}")
        )
        return issues
    if not quests_dir.exists():
        issues.append(Issue("error", "inputs", f"Missing quests dir: {quests_dir}"))
        return issues

    map_records = iter_map_records(maps_dir)
    map_index: dict[str, tuple[Path, dict[str, Any]]] = {}
    event_set: set[str] = set()
    event_set_lower: set[str] = set()

    for path, record in map_records:
        map_id = record.get("id")
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
        map_index[map_id] = (path, record)
        for event in record.get("events", []):
            if isinstance(event, str):
                event_set.add(event)
                event_set_lower.add(event.lower())

    # 1) Dangling map connection targets
    for map_id, (path, record) in map_index.items():
        for conn in record.get("connections", []):
            if not isinstance(conn, dict):
                continue
            target = conn.get("target")
            if isinstance(target, str) and target and target not in map_index:
                issues.append(
                    Issue(
                        "error",
                        "map_targets",
                        f"{map_id} ({path}) -> missing target '{target}'",
                    )
                )

    # 2) Encounter table refs + map coverage
    encounter_index: dict[str, tuple[Path, set[str]]] = {}
    for path, record in iter_encounters(encounters_dir):
        table_id = record.get("id")
        if not isinstance(table_id, str) or not table_id:
            continue
        maps = set()
        raw_maps = record.get("maps", [])
        if isinstance(raw_maps, list):
            for m in raw_maps:
                if isinstance(m, str):
                    maps.add(m)
        encounter_index[table_id] = (path, maps)

    for map_id, (path, record) in map_index.items():
        table_id = record.get("encounter_table")
        if not isinstance(table_id, str) or not table_id:
            continue
        if table_id not in encounter_index:
            issues.append(
                Issue(
                    "error",
                    "encounters",
                    f"{map_id} ({path}) references missing encounter table '{table_id}'",
                )
            )
            continue
        enc_path, table_maps = encounter_index[table_id]
        if map_id not in table_maps:
            issues.append(
                Issue(
                    "error",
                    "encounters",
                    f"{map_id} ({path}) uses {table_id} but is absent from {enc_path} maps[]",
                )
            )

    # 3) Quest stage hop connectivity
    graph: dict[str, set[str]] = {}
    for map_id, (_, record) in map_index.items():
        graph.setdefault(map_id, set())
        for conn in record.get("connections", []):
            if not isinstance(conn, dict):
                continue
            target = conn.get("target")
            if isinstance(target, str) and target:
                graph[map_id].add(target)

    for quest_path in sorted(quests_dir.glob("quest_*.json")):
        data = load_json(quest_path)
        quest_id = data.get("quest_id") or quest_path.stem
        stages = data.get("stages", [])
        if not isinstance(stages, list):
            continue
        locs: list[str] = []
        for stage in stages:
            if not isinstance(stage, dict):
                continue
            loc = stage.get("target_location_id")
            if isinstance(loc, str) and loc:
                locs.append(loc)
        for src, dst in zip(locs, locs[1:]):
            if src == dst:
                continue
            if dst not in graph.get(src, set()):
                issues.append(
                    Issue(
                        "error",
                        "quest_hops",
                        f"{quest_id}: missing hop {src} -> {dst}",
                    )
                )

    # 4) Gate token sanity
    for map_id, (path, record) in map_index.items():
        for conn in record.get("connections", []):
            if not isinstance(conn, dict):
                continue
            for key in ("trigger", "condition"):
                token = conn.get(key)
                if not isinstance(token, str) or not token:
                    continue
                if not is_known_gate(token, event_set, event_set_lower):
                    sev = "error" if args.strict_gates else "warning"
                    issues.append(
                        Issue(
                            sev,
                            "gate_flags",
                            f"{map_id} ({path}) has unknown {key}='{token}'",
                        )
                    )

    return issues


def main() -> None:
    args = parse_args()
    issues = run_validation(args)
    errors = [i for i in issues if i.severity == "error"]
    warnings = [i for i in issues if i.severity == "warning"]

    print("=" * 64)
    print("WORLD INTEGRITY VALIDATION")
    print("=" * 64)
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")

    if errors:
        print("\nERRORS")
        print("-" * 64)
        for issue in errors:
            print(f"[{issue.category}] {issue.detail}")

    if warnings:
        print("\nWARNINGS")
        print("-" * 64)
        for issue in warnings:
            print(f"[{issue.category}] {issue.detail}")

    if errors:
        sys.exit(1)
    print("\nWorld integrity checks passed.")


if __name__ == "__main__":
    main()
