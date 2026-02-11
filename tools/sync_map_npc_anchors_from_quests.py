#!/usr/bin/env python3
"""
Sync map NPC anchors from quest step targets.

Adds missing `target_npc` values from quest steps into each target map's
`key_npcs` list so quest metadata and map metadata stay cohesive.
"""

from __future__ import annotations

import argparse
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any


CORE_QUEST_PACKS = (
    "quest_main_story.json",
    "quest_side_stories.json",
    "quest_generated_placeholders.json",
)


@dataclass(frozen=True)
class Change:
    map_id: str
    npc_id: str
    quest_id: str
    step_id: int
    source_pack: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Sync canonical map key_npcs from quest target_npc references."
    )
    parser.add_argument(
        "--maps-dir",
        default="assets/data/maps",
        help="Directory containing map_*.json files (default: assets/data/maps)",
    )
    parser.add_argument(
        "--quests-dir",
        default="assets/data/quests",
        help="Directory containing quest_*.json packs (default: assets/data/quests)",
    )
    parser.add_argument(
        "--scope",
        choices=("core", "all"),
        default="all",
        help="Quest pack scope: core or all (default: all)",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Do not write files; print planned changes only.",
    )
    return parser.parse_args()


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def dump_json(path: Path, data: Any) -> None:
    path.write_text(json.dumps(data, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")


def iter_map_records(maps_dir: Path) -> list[tuple[Path, dict[str, Any], dict[str, Any]]]:
    """
    Returns tuples of (file_path, file_json_root, map_record_dict).
    """
    out: list[tuple[Path, dict[str, Any], dict[str, Any]]] = []
    for path in sorted(maps_dir.glob("map_*.json")):
        root = load_json(path)
        if isinstance(root.get("maps"), list):
            for rec in root["maps"]:
                if isinstance(rec, dict):
                    out.append((path, root, rec))
        elif isinstance(root, dict):
            out.append((path, root, root))
    return out


def collect_quest_files(quests_dir: Path, scope: str) -> list[Path]:
    if scope == "all":
        return sorted(quests_dir.glob("quest_*.json"))
    return [quests_dir / name for name in CORE_QUEST_PACKS if (quests_dir / name).exists()]


def normalize_key_npcs(rec: dict[str, Any]) -> list[str]:
    raw = rec.get("key_npcs")
    if not isinstance(raw, list):
        return []
    out: list[str] = []
    seen: set[str] = set()
    for token in raw:
        if not isinstance(token, str) or not token:
            continue
        if token in seen:
            continue
        out.append(token)
        seen.add(token)
    return out


def main() -> int:
    args = parse_args()
    maps_dir = Path(args.maps_dir)
    quests_dir = Path(args.quests_dir)
    if not maps_dir.exists():
        print(f"Missing maps dir: {maps_dir}")
        return 1
    if not quests_dir.exists():
        print(f"Missing quests dir: {quests_dir}")
        return 1

    # Build map index.
    map_index: dict[str, tuple[Path, dict[str, Any], dict[str, Any]]] = {}
    roots_by_path: dict[Path, dict[str, Any]] = {}
    for path, root, rec in iter_map_records(maps_dir):
        map_id = rec.get("id")
        if not isinstance(map_id, str) or not map_id:
            continue
        if map_id in map_index:
            # Keep first; duplicate handling belongs in validators.
            continue
        map_index[map_id] = (path, root, rec)
        roots_by_path[path] = root

    changes: list[Change] = []
    changed_paths: set[Path] = set()

    for quest_path in collect_quest_files(quests_dir, args.scope):
        if not quest_path.exists():
            continue
        data = load_json(quest_path)
        quests = data.get("quests")
        if not isinstance(quests, list):
            continue
        for quest in quests:
            if not isinstance(quest, dict):
                continue
            quest_id = quest.get("id")
            if not isinstance(quest_id, str) or not quest_id:
                continue
            steps = quest.get("steps")
            if not isinstance(steps, list):
                continue
            for idx, step in enumerate(steps):
                if not isinstance(step, dict):
                    continue
                target_location = step.get("target_location")
                target_npc = step.get("target_npc")
                if not (isinstance(target_location, str) and target_location):
                    continue
                if not (isinstance(target_npc, str) and target_npc):
                    continue
                if target_location not in map_index:
                    continue

                _, _, rec = map_index[target_location]
                key_npcs = normalize_key_npcs(rec)
                if target_npc in key_npcs:
                    continue

                key_npcs.append(target_npc)
                rec["key_npcs"] = key_npcs
                changed_paths.add(map_index[target_location][0])
                step_id_raw = step.get("id")
                step_id = step_id_raw if isinstance(step_id_raw, int) else idx + 1
                changes.append(
                    Change(
                        map_id=target_location,
                        npc_id=target_npc,
                        quest_id=quest_id,
                        step_id=step_id,
                        source_pack=str(quest_path),
                    )
                )

    print("=" * 64)
    print("MAP NPC ANCHOR SYNC")
    print("=" * 64)
    print(f"Scope: {args.scope}")
    print(f"Maps loaded: {len(map_index)}")
    print(f"Changes: {len(changes)}")
    print(f"Files touched: {len(changed_paths)}")

    if changes:
        print("-" * 64)
        for ch in changes[:200]:
            print(
                f"{ch.map_id}: +{ch.npc_id} "
                f"(from {ch.quest_id} step {ch.step_id}, {ch.source_pack})"
            )
        if len(changes) > 200:
            print(f"... ({len(changes) - 200} additional changes omitted)")

    if args.dry_run:
        print("\nDry run only; no files written.")
        return 0

    for path in sorted(changed_paths):
        root = roots_by_path[path]
        dump_json(path, root)

    print("\nWrite complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
