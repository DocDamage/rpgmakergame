#!/usr/bin/env python3
"""
Validate canonical world-dressing anchors against runtime map event tags.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MAPS_DIR = ROOT / "assets" / "data" / "maps"
BRIDGE_PATH = ROOT / "assets" / "data" / "system" / "runtime_map_bridge_generated.json"
RUNTIME_DATA_DIR = ROOT / "data"

TAG_WORLD_DRESS = re.compile(r"<\s*chromaWorldDress\s*:\s*([A-Za-z0-9_:-]+)\s*>", re.I)

TAG_KEYS: tuple[str, ...] = (
    "poi",
    "landmark",
    "hazard",
    "interior",
    "ambient_npc",
    "region",
    "puzzle",
    "story_events",
    "key_npcs",
    "notes",
)


@dataclass(frozen=True)
class Issue:
    severity: str
    category: str
    detail: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate canonical world-dressing anchor propagation into runtime maps."
    )
    parser.add_argument(
        "--maps-dir",
        default=str(MAPS_DIR),
        help="Directory containing canonical map_*.json files.",
    )
    parser.add_argument(
        "--bridge",
        default=str(BRIDGE_PATH),
        help="Runtime bridge JSON path.",
    )
    parser.add_argument(
        "--runtime-dir",
        default=str(RUNTIME_DATA_DIR),
        help="Runtime data directory containing Map###.json files.",
    )
    parser.add_argument(
        "--warn-surplus",
        action="store_true",
        help="Warn when runtime world-dressing tag counts exceed canonical expectations.",
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


def load_canonical_maps(maps_dir: Path) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for path in sorted(maps_dir.glob("map_*.json")):
        data = load_json(path)
        entries = data.get("maps") if isinstance(data.get("maps"), list) else [data]
        for rec in entries:
            if not isinstance(rec, dict):
                continue
            map_id = rec.get("id")
            if not isinstance(map_id, str) or not map_id:
                continue
            out[map_id] = rec
    return out


def canonical_expected_counts(rec: dict[str, Any]) -> dict[str, int]:
    def list_count(key: str) -> int:
        value = rec.get(key)
        return len(value) if isinstance(value, list) else 0

    counts = {
        "poi": list_count("points_of_interest"),
        "landmark": list_count("landmarks"),
        "hazard": list_count("hazards"),
        "interior": list_count("interiors"),
        "ambient_npc": list_count("ambient_npcs"),
        "region": list_count("regions"),
        "puzzle": list_count("puzzles"),
        "story_events": 1 if list_count("events") > 0 else 0,
        "key_npcs": 1 if list_count("key_npcs") > 0 else 0,
        "notes": 1
        if isinstance(rec.get("notes"), str) and rec.get("notes", "").strip()
        else 0,
    }
    return counts


def runtime_actual_counts(map_path: Path) -> dict[str, int]:
    counts: dict[str, int] = {}
    data = load_json(map_path)
    events = data.get("events")
    if not isinstance(events, list):
        return counts
    for ev in events:
        if not isinstance(ev, dict):
            continue
        note = ev.get("note")
        if not isinstance(note, str):
            continue
        for tag in TAG_WORLD_DRESS.findall(note):
            key = tag.strip().lower()
            counts[key] = counts.get(key, 0) + 1
    return counts


def run_validation(args: argparse.Namespace) -> tuple[list[Issue], dict[str, int]]:
    issues: list[Issue] = []
    stats = {
        "canonical_maps": 0,
        "bridged_maps": 0,
        "validated_runtime_maps": 0,
        "expected_world_dress_tags": 0,
        "actual_world_dress_tags": 0,
    }

    maps_dir = Path(args.maps_dir)
    bridge_path = Path(args.bridge)
    runtime_dir = Path(args.runtime_dir)

    if not maps_dir.exists():
        issues.append(Issue("error", "inputs", f"Missing maps dir: {maps_dir}"))
        return issues, stats
    if not bridge_path.exists():
        issues.append(Issue("error", "inputs", f"Missing bridge file: {bridge_path}"))
        return issues, stats
    if not runtime_dir.exists():
        issues.append(Issue("error", "inputs", f"Missing runtime data dir: {runtime_dir}"))
        return issues, stats

    canonical = load_canonical_maps(maps_dir)
    stats["canonical_maps"] = len(canonical)

    bridge = load_json(bridge_path)
    mappings = bridge.get("mappings") if isinstance(bridge, dict) else None
    if not isinstance(mappings, list):
        issues.append(Issue("error", "schema", f"{bridge_path} missing list `mappings`"))
        return issues, stats

    for rec in mappings:
        if not isinstance(rec, dict):
            issues.append(Issue("error", "schema", "bridge mapping entry must be an object"))
            continue
        can_id = rec.get("canonical_map_id")
        runtime_id = rec.get("runtime_map_id")
        if not isinstance(can_id, str) or not can_id:
            issues.append(Issue("error", "schema", "bridge mapping missing canonical_map_id"))
            continue
        if not isinstance(runtime_id, int) or runtime_id <= 0:
            issues.append(Issue("error", "schema", f"{can_id}: invalid runtime_map_id"))
            continue
        stats["bridged_maps"] += 1

        canon_map = canonical.get(can_id)
        if canon_map is None:
            issues.append(
                Issue(
                    "error",
                    "canonical_missing",
                    f"{can_id} exists in bridge but not canonical map packs",
                )
            )
            continue

        map_path = runtime_dir / f"Map{runtime_id:03d}.json"
        if not map_path.exists():
            issues.append(
                Issue(
                    "error",
                    "runtime_missing",
                    f"{can_id} -> {map_path.name} missing",
                )
            )
            continue
        stats["validated_runtime_maps"] += 1

        expected = canonical_expected_counts(canon_map)
        actual = runtime_actual_counts(map_path)
        stats["expected_world_dress_tags"] += sum(expected.values())
        stats["actual_world_dress_tags"] += sum(actual.get(k, 0) for k in TAG_KEYS)

        for key in TAG_KEYS:
            exp = expected.get(key, 0)
            got = actual.get(key, 0)
            if got < exp:
                issues.append(
                    Issue(
                        "error",
                        "world_dressing_missing",
                        f"{can_id} ({map_path.name}) tag '{key}' expected>={exp} actual={got}",
                    )
                )
            elif args.warn_surplus and got > exp:
                issues.append(
                    Issue(
                        "warning",
                        "world_dressing_surplus",
                        f"{can_id} ({map_path.name}) tag '{key}' expected={exp} actual={got}",
                    )
                )

    if args.strict:
        issues = [
            Issue("error", issue.category, issue.detail)
            if issue.severity == "warning"
            else issue
            for issue in issues
        ]
    return issues, stats


def main() -> int:
    args = parse_args()
    issues, stats = run_validation(args)
    errors = [x for x in issues if x.severity == "error"]
    warnings = [x for x in issues if x.severity == "warning"]

    print("=" * 64)
    print("RUNTIME WORLD DRESSING VALIDATION")
    print("=" * 64)
    print(f"Canonical maps: {stats['canonical_maps']}")
    print(f"Bridge mappings: {stats['bridged_maps']}")
    print(f"Runtime maps validated: {stats['validated_runtime_maps']}")
    print(f"Expected world-dressing tags: {stats['expected_world_dress_tags']}")
    print(f"Actual world-dressing tags: {stats['actual_world_dress_tags']}")
    print("-" * 64)
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")

    if issues:
        print("-" * 64)
        for issue in issues:
            print(f"[{issue.severity.upper():7}] {issue.category:24} {issue.detail}")
    else:
        print("\nRuntime world-dressing checks passed.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
