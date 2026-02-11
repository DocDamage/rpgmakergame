#!/usr/bin/env python3
"""
Asset naming convention validator for Chroma's Edge.

Default behavior intentionally skips source/preview libraries and validates only
production-facing assets.
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path


PATTERNS = {
    "maps": r"^(OW|T|I|MIC|D[1-8]|SHR|TWR|PAL|RV|HID)_[A-Z_]+_\d+x\d+(_base)?\.json$",
    "sprites": r"^(spr|icon|tileset|fx|ui)_[a-z0-9_]+\.(png|ase|aseprite)$",
    "audio": r"^(bgm|sfx|vo|amb)_[a-z0-9_]+\.(ogg|wav|mp3)$",
    "data": (
        r"^(map|npc|item|enemy|quest|dialog|encounter|drop|achievement|ability|audio|"
        r"cutscene|boss|shop|system|tutorial)s?_[a-z0-9_]+\.json$"
    ),
}

ID_PATTERNS = {
    "map": r"^(OW|T|I|MIC|D[1-8]|SHR|TWR|PAL|RV|HID)_[A-Z][A-Z0-9_]*_\d+x\d+(_base)?$",
    "npc": r"^NPC_[A-Z][A-Z_]+$",
    "item": r"^ITEM_[A-Z][A-Z_]+$",
    "enemy": r"^ENEMY_[A-Z][A-Z_]+$",
    "quest": r"^Q_[A-Z][A-Z_]+$",
    "dialog": r"^DT_[A-Z][A-Z_]+$",
    "encounter": r"^[A-Z][A-Z0-9_]*_ENCOUNTERS$",
    "drop": r"^DROPS_[A-Z][A-Z_]+$",
}

DATA_SUBDIR_TO_ID_TYPE = {
    "maps": "map",
    "npcs": "npc",
    "items": "item",
    "enemies": "enemy",
    "quests": "quest",
    "dialogs": "dialog",
    "encounters": "encounter",
    "drops": "drop",
}

DEFAULT_SKIP_DIR_NAMES = {
    ".git",
    "__pycache__",
    "archive",
    "preview",
    "assetsformygame",
}

NON_ASSET_SUFFIXES = (".md", ".txt", ".py", ".pyc", ".gitignore")


def parse_args(argv: list[str]) -> tuple[Path, bool, bool]:
    include_preview = False
    validate_ids = False
    directory: Path | None = None

    for arg in argv[1:]:
        if arg == "--include-preview":
            include_preview = True
            continue
        if arg == "--validate-ids":
            validate_ids = True
            continue
        if arg in {"-h", "--help"}:
            print(
                "Usage: python tools/validate_naming.py "
                "[directory] [--include-preview] [--validate-ids]"
            )
            sys.exit(0)
        if directory is None:
            directory = Path(arg)
            continue
        print(f"Unexpected argument: {arg}")
        print(
            "Usage: python tools/validate_naming.py "
            "[directory] [--include-preview] [--validate-ids]"
        )
        sys.exit(1)

    return (directory or Path("assets"), include_preview, validate_ids)


def infer_category(filepath: Path, scan_root: Path) -> str | None:
    root_name = scan_root.name.lower()
    if root_name in PATTERNS:
        return root_name

    parts = [p.lower() for p in filepath.parts]
    if "assets" in parts:
        idx = parts.index("assets")
        if idx + 1 < len(parts):
            top = parts[idx + 1]
            if top in PATTERNS:
                return top

    for part in parts:
        if part in PATTERNS:
            return part

    return None


def should_skip_path(path: Path, include_preview: bool) -> bool:
    lowered_parts = {p.lower() for p in path.parts}
    skip_dirs = set(DEFAULT_SKIP_DIR_NAMES)
    if include_preview:
        skip_dirs.discard("preview")
        skip_dirs.discard("assetsformygame")
    return any(name in lowered_parts for name in skip_dirs)


def validate_filename(filepath: Path, category: str) -> tuple[bool, str]:
    filename = filepath.name
    if filename.startswith(".") or filename.startswith("_"):
        return True, "Skipped (hidden)"

    if filepath.suffix.lower() in NON_ASSET_SUFFIXES:
        return True, "Skipped (non-asset file)"

    pattern = PATTERNS[category]
    if re.match(pattern, filename):
        return True, f"Valid {category} naming"
    return False, f"Invalid {category} naming (expected pattern: {pattern})"


def should_validate_id(filepath: Path, category: str) -> str | None:
    if filepath.suffix.lower() != ".json":
        return None

    if category == "maps":
        return "map"

    if category != "data":
        return None

    parent = filepath.parent.name.lower()
    id_type = DATA_SUBDIR_TO_ID_TYPE.get(parent)
    if id_type is None:
        return None

    expected_prefix = f"{id_type}_"
    if not filepath.name.lower().startswith(expected_prefix):
        # Aggregate/helper files are allowed here; skip ID checks.
        return None

    return id_type


def validate_id_in_file(filepath: Path, id_type: str) -> list[tuple[bool, str]]:
    try:
        with filepath.open("r", encoding="utf-8") as fh:
            data = json.load(fh)
    except (json.JSONDecodeError, UnicodeDecodeError):
        return [(False, "Invalid JSON encoding/content")]
    except Exception as exc:  # pragma: no cover
        return [(False, f"Error reading file: {exc}")]

    if not isinstance(data, dict):
        return [(True, "Skipped ID check (JSON is not an object)")]

    file_id = data.get("id")
    if not file_id:
        return [(False, "Missing 'id' field")]

    expected = ID_PATTERNS[id_type]
    if re.match(expected, str(file_id)):
        return [(True, f"Valid {id_type} ID: {file_id}")]
    return [(False, f"Invalid {id_type} ID: {file_id} (expected pattern: {expected})")]


def scan_directory(directory: Path, include_preview: bool, validate_ids: bool) -> dict:
    results = {"valid": [], "invalid": [], "skipped": []}

    for root, dirs, files in os.walk(directory):
        root_path = Path(root)

        dirs[:] = [
            d for d in dirs
            if not d.startswith(".")
            and not should_skip_path(root_path / d, include_preview)
        ]

        if should_skip_path(root_path, include_preview):
            continue

        for filename in files:
            filepath = root_path / filename
            category = infer_category(filepath, directory)

            if category is None:
                results["skipped"].append((str(filepath), "Skipped (unknown category)"))
                continue

            valid, message = validate_filename(filepath, category)
            if "Skipped" in message:
                results["skipped"].append((str(filepath), message))
            elif valid:
                results["valid"].append((str(filepath), message))
            else:
                results["invalid"].append((str(filepath), message))

            if validate_ids:
                id_type = should_validate_id(filepath, category)
                if id_type is None:
                    continue
                for id_valid, id_msg in validate_id_in_file(filepath, id_type):
                    if not id_valid:
                        results["invalid"].append((str(filepath), id_msg))

    return results


def print_results(results: dict) -> int:
    print("=" * 60)
    print("ASSET NAMING VALIDATION REPORT")
    print("=" * 60)
    print(f"\nValid: {len(results['valid'])} files")
    print(f"Invalid: {len(results['invalid'])} files")
    print(f"Skipped: {len(results['skipped'])} files")

    if results["invalid"]:
        print("\n" + "-" * 60)
        print("INVALID FILES:")
        print("-" * 60)
        for filepath, message in results["invalid"]:
            print(f"- {filepath}")
            print(f"  -> {message}")
        print(f"\nFound {len(results['invalid'])} validation errors.")
        return 1

    print("\nAll files follow naming conventions.")
    return 0


def main() -> None:
    directory, include_preview, validate_ids = parse_args(sys.argv)
    if not directory.exists():
        print(f"Error: directory '{directory}' not found.")
        sys.exit(1)

    print(f"Scanning: {directory.resolve()}")
    if include_preview:
        print("Mode: include preview/source libraries")
    else:
        print("Mode: production-only (preview/source skipped)")
    if validate_ids:
        print("ID checks: enabled")
    else:
        print("ID checks: disabled (use --validate-ids to enable)")
    print("This may take a moment...\n")

    results = scan_directory(
        directory,
        include_preview=include_preview,
        validate_ids=validate_ids,
    )
    sys.exit(print_results(results))


if __name__ == "__main__":
    main()
