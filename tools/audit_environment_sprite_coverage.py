#!/usr/bin/env python3
"""
Environment sprite and world-dressing audit.

Checks:
1. Every map-referenced tileset has a production source PNG and README.
2. Optional curation candidate coverage for each referenced tileset.
3. Town dressing density (ambient NPC and interior counts).
4. Service-to-interior consistency for town maps.
5. Optional world-dressing anchors for non-overworld maps.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


@dataclass(frozen=True)
class Issue:
    severity: str
    category: str
    detail: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Audit map tileset coverage and town world-dressing density."
    )
    parser.add_argument(
        "--maps-dir",
        default="assets/data/maps",
        help="Directory containing map_*.json files (default: assets/data/maps)",
    )
    parser.add_argument(
        "--tilesets-dir",
        default="assets/sprites/tilesets",
        help="Directory containing tileset source/readme files (default: assets/sprites/tilesets)",
    )
    parser.add_argument(
        "--town-min-ambient",
        type=int,
        default=4,
        help="Minimum ambient NPC count for town maps before warning (default: 4)",
    )
    parser.add_argument(
        "--town-min-interiors",
        type=int,
        default=3,
        help="Minimum interior count for town maps before warning (default: 3)",
    )
    parser.add_argument(
        "--strict-candidates",
        action="store_true",
        help="Treat missing curation candidate tileset copies as warnings.",
    )
    parser.add_argument(
        "--strict-world-dressing",
        action="store_true",
        help="Warn when non-overworld maps have no world-dressing anchors (landmarks/hazards/puzzles/notes/NPCs/events).",
    )
    return parser.parse_args()


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def tileset_slug(tileset_id: str) -> str:
    """
    Convert `Tileset_ChronoPier` -> `chronopier`.
    """
    base = tileset_id
    if base.startswith("Tileset_"):
        base = base[len("Tileset_") :]
    # Production source filenames are compact lowercase (no word separators).
    base = re.sub(r"[^A-Za-z0-9]+", "", base)
    return base.lower()


def expected_tileset_files(tilesets_dir: Path, tileset_id: str) -> tuple[Path, Path, Path]:
    slug = tileset_slug(tileset_id)
    readme = tilesets_dir / f"README_{tileset_id}.md"
    source = tilesets_dir / f"tileset_{slug}_source_primary.png"
    candidate = tilesets_dir / "_curation_candidates" / f"tileset_cand_{tileset_id.lower()}.png"
    return readme, source, candidate


def normalize_service(service: str) -> str:
    return service.strip().lower()


def interior_type_matches_service(interior_type: str, service: str) -> bool:
    t = interior_type.strip().lower()
    s = normalize_service(service)
    if s == "shop":
        return t in {
            "shop",
            "itemshop",
            "market",
            "vendor",
            "dock_market",
            "supply_depot",
        }
    if s == "inn":
        return t in {"inn", "tavern"}
    if s == "smith":
        return t in {"smith", "forge"}
    if s == "gambling":
        return t in {"secret", "gambling", "casino"}
    return True


def map_has_world_dressing_anchor(rec: dict[str, Any]) -> bool:
    """
    World-dressing anchors are metadata that indicate object/narrative set dressing.
    """
    list_fields = (
        "landmarks",
        "hazards",
        "puzzles",
        "points_of_interest",
        "events",
        "ambient_npcs",
        "key_npcs",
        "interiors",
    )
    for key in list_fields:
        value = rec.get(key)
        if isinstance(value, list) and value:
            return True
    notes = rec.get("notes")
    if isinstance(notes, str) and notes.strip():
        return True
    return False


def run_audit(args: argparse.Namespace) -> tuple[list[Issue], dict[str, int]]:
    issues: list[Issue] = []
    stats = {
        "maps": 0,
        "towns": 0,
        "maps_with_world_dressing_anchors": 0,
        "tilesets_referenced": 0,
        "tilesets_with_sources": 0,
        "tilesets_with_readmes": 0,
        "tilesets_with_candidates": 0,
    }

    maps_dir = Path(args.maps_dir)
    tilesets_dir = Path(args.tilesets_dir)
    if not maps_dir.exists():
        issues.append(Issue("error", "inputs", f"Missing maps dir: {maps_dir}"))
        return issues, stats
    if not tilesets_dir.exists():
        issues.append(Issue("error", "inputs", f"Missing tilesets dir: {tilesets_dir}"))
        return issues, stats

    tileset_usage: dict[str, list[str]] = {}

    for path in sorted(maps_dir.glob("map_*.json")):
        data = load_json(path)
        entries = data.get("maps") if isinstance(data.get("maps"), list) else [data]
        for rec in entries:
            if not isinstance(rec, dict):
                continue
            map_id = rec.get("id")
            if not isinstance(map_id, str) or not map_id:
                continue
            stats["maps"] += 1

            map_type = rec.get("type")
            has_anchor = map_has_world_dressing_anchor(rec)
            if has_anchor:
                stats["maps_with_world_dressing_anchors"] += 1
            elif args.strict_world_dressing and map_type != "overworld":
                issues.append(
                    Issue(
                        "warning",
                        "world_dressing",
                        f"{map_id} has no world-dressing anchor metadata (landmarks/hazards/puzzles/notes/NPCs/events)",
                    )
                )

            tileset = rec.get("tileset")
            if isinstance(tileset, str) and tileset:
                tileset_usage.setdefault(tileset, []).append(map_id)

            if rec.get("type") == "town":
                stats["towns"] += 1
                interiors = rec.get("interiors")
                ambient = rec.get("ambient_npcs")
                restrictions = rec.get("restrictions")
                limited_access = (
                    isinstance(restrictions, list)
                    and any(isinstance(x, str) and x == "limited_access" for x in restrictions)
                )
                interior_count = len(interiors) if isinstance(interiors, list) else 0
                ambient_count = len(ambient) if isinstance(ambient, list) else 0

                if interior_count < args.town_min_interiors and not limited_access:
                    issues.append(
                        Issue(
                            "warning",
                            "town_dressing",
                            f"{map_id} has only {interior_count} interiors (<{args.town_min_interiors})",
                        )
                    )
                if ambient_count < args.town_min_ambient:
                    issues.append(
                        Issue(
                            "warning",
                            "town_dressing",
                            f"{map_id} has only {ambient_count} ambient NPCs (<{args.town_min_ambient})",
                        )
                    )

                services = rec.get("services")
                if isinstance(services, list) and isinstance(interiors, list):
                    interior_types = [
                        x.get("type", "")
                        for x in interiors
                        if isinstance(x, dict) and isinstance(x.get("type"), str)
                    ]
                    for svc in services:
                        if not isinstance(svc, str):
                            continue
                        if not any(
                            interior_type_matches_service(i_type, svc)
                            for i_type in interior_types
                        ):
                            issues.append(
                                Issue(
                                    "warning",
                                    "town_services",
                                    f"{map_id} service '{svc}' has no matching interior type",
                                )
                            )

                if isinstance(interiors, list):
                    for entry in interiors:
                        if not isinstance(entry, dict):
                            continue
                        itype = entry.get("type", "unknown")
                        i_ambient = entry.get("ambient_npcs")
                        if isinstance(i_ambient, list) and not i_ambient:
                            issues.append(
                                Issue(
                                    "warning",
                                    "interior_dressing",
                                    f"{map_id} interior type '{itype}' has empty ambient_npcs",
                                )
                            )

    stats["tilesets_referenced"] = len(tileset_usage)

    for tileset_id in sorted(tileset_usage):
        readme, source, candidate = expected_tileset_files(tilesets_dir, tileset_id)
        if not readme.exists():
            issues.append(
                Issue(
                    "error",
                    "tilesets",
                    f"{tileset_id} referenced by maps but missing {readme}",
                )
            )
        else:
            stats["tilesets_with_readmes"] += 1

        if not source.exists():
            issues.append(
                Issue(
                    "error",
                    "tilesets",
                    f"{tileset_id} referenced by maps but missing {source}",
                )
            )
        else:
            stats["tilesets_with_sources"] += 1

        if candidate.exists():
            stats["tilesets_with_candidates"] += 1
        elif args.strict_candidates:
            issues.append(
                Issue(
                    "warning",
                    "tileset_candidates",
                    f"{tileset_id} has no staged curation candidate at {candidate}",
                )
            )

    return issues, stats


def main() -> int:
    args = parse_args()
    issues, stats = run_audit(args)
    errors = [x for x in issues if x.severity == "error"]
    warnings = [x for x in issues if x.severity == "warning"]

    print("=" * 64)
    print("ENVIRONMENT SPRITE COVERAGE AUDIT")
    print("=" * 64)
    print(f"Maps scanned: {stats['maps']}")
    print(f"Towns scanned: {stats['towns']}")
    print(f"Maps with world-dressing anchors: {stats['maps_with_world_dressing_anchors']}")
    print(f"Tilesets referenced by maps: {stats['tilesets_referenced']}")
    print(f"Tilesets with source PNGs: {stats['tilesets_with_sources']}")
    print(f"Tilesets with READMEs: {stats['tilesets_with_readmes']}")
    print(f"Tilesets with curation candidates: {stats['tilesets_with_candidates']}")
    print("-" * 64)
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")

    if issues:
        print("-" * 64)
        for issue in issues:
            print(f"[{issue.severity.upper():7}] {issue.category:18} {issue.detail}")
    else:
        print("\nEnvironment sprite coverage checks passed.")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
