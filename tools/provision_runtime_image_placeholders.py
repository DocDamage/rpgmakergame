#!/usr/bin/env python3
"""
Provision missing RPG Maker MZ runtime image files with deterministic placeholders.

This is a safety utility for development/runtime continuity. It only creates files
that do not already exist.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
IMG_DIR = ROOT / "img"

MAP_RE = re.compile(r"^Map\d{3}\.json$")

SYSTEM_IMAGES = {
    "Balloon": (768, 384),
    "ButtonSet": (768, 48),
    "GameOver": (816, 624),
    "IconSet": (512, 512),
    "Shadow1": (128, 64),
    "Shadow2": (64, 64),
    "Splash": (816, 624),
    "States": (768, 384),
    "Weapons1": (768, 256),
    "Weapons2": (768, 256),
    "Weapons3": (768, 256),
    "Window": (192, 192),
}

TITLE_SIZE = (816, 624)
BATTLEBACK_SIZE = (1000, 740)
PARALLAX_SIZE = (816, 624)


@dataclass(frozen=True)
class Target:
    category: str
    name: str
    width: int
    height: int

    @property
    def path(self) -> Path:
        return IMG_DIR / self.category / f"{self.name}.png"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Create missing runtime image placeholders (system/title/battleback/tileset/etc)."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned creations without writing files.",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing files (default: create only missing files).",
    )
    return parser.parse_args()


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def tileset_size(name: str) -> tuple[int, int]:
    if name.endswith("_A1") or name.endswith("_A2"):
        return (768, 576)
    return (768, 768)


def character_size(name: str) -> tuple[int, int]:
    if name.startswith("$"):
        return (144, 256)
    return (576, 384)


def label_color(category: str) -> tuple[int, int, int]:
    palette = {
        "system": (94, 142, 188),
        "tilesets": (140, 104, 170),
        "battlebacks1": (120, 160, 90),
        "battlebacks2": (180, 130, 88),
        "titles1": (86, 156, 154),
        "titles2": (86, 156, 154),
        "parallaxes": (92, 92, 132),
        "characters": (170, 118, 92),
    }
    return palette.get(category, (120, 120, 120))


def collect_targets() -> list[Target]:
    targets: dict[tuple[str, str], Target] = {}

    # Always include core hardcoded system sheets required by the engine.
    for name, (w, h) in SYSTEM_IMAGES.items():
        key = ("system", name)
        targets[key] = Target("system", name, w, h)

    system_path = DATA_DIR / "System.json"
    if system_path.exists():
        system = load_json(system_path)
        if isinstance(system, dict):
            for key in ("title1Name", "title2Name"):
                value = system.get(key)
                if isinstance(value, str) and value:
                    cat = "titles1" if key == "title1Name" else "titles2"
                    targets[(cat, value)] = Target(cat, value, *TITLE_SIZE)
            for key in ("battleback1Name", "battleback2Name"):
                value = system.get(key)
                if isinstance(value, str) and value:
                    cat = "battlebacks1" if key == "battleback1Name" else "battlebacks2"
                    targets[(cat, value)] = Target(cat, value, *BATTLEBACK_SIZE)
            for vehicle_key in ("boat", "ship", "airship"):
                rec = system.get(vehicle_key)
                if not isinstance(rec, dict):
                    continue
                character = rec.get("characterName")
                if isinstance(character, str) and character:
                    w, h = character_size(character)
                    targets[("characters", character)] = Target("characters", character, w, h)

    tilesets_path = DATA_DIR / "Tilesets.json"
    used_tileset_ids: set[int] = set()
    for map_path in sorted(DATA_DIR.glob("Map*.json")):
        if not MAP_RE.match(map_path.name):
            continue
        payload = load_json(map_path)
        if not isinstance(payload, dict):
            continue
        tid = payload.get("tilesetId")
        if isinstance(tid, int) and tid > 0:
            used_tileset_ids.add(tid)

        bb1 = payload.get("battleback1Name")
        bb2 = payload.get("battleback2Name")
        parallax = payload.get("parallaxName")
        if isinstance(bb1, str) and bb1:
            targets[("battlebacks1", bb1)] = Target("battlebacks1", bb1, *BATTLEBACK_SIZE)
        if isinstance(bb2, str) and bb2:
            targets[("battlebacks2", bb2)] = Target("battlebacks2", bb2, *BATTLEBACK_SIZE)
        if isinstance(parallax, str) and parallax:
            targets[("parallaxes", parallax)] = Target("parallaxes", parallax, *PARALLAX_SIZE)

    if tilesets_path.exists():
        tilesets = load_json(tilesets_path)
        if isinstance(tilesets, list):
            for tid in sorted(used_tileset_ids):
                if tid <= 0 or tid >= len(tilesets):
                    continue
                rec = tilesets[tid]
                if not isinstance(rec, dict):
                    continue
                names = rec.get("tilesetNames")
                if not isinstance(names, list):
                    continue
                for value in names:
                    if not isinstance(value, str) or not value:
                        continue
                    w, h = tileset_size(value)
                    targets[("tilesets", value)] = Target("tilesets", value, w, h)

    return sorted(targets.values(), key=lambda t: (t.category, t.name))


def draw_placeholder(target: Target) -> Image.Image:
    bg = (18, 20, 24, 255)
    fg = label_color(target.category)
    img = Image.new("RGBA", (target.width, target.height), bg)
    draw = ImageDraw.Draw(img)

    # Soft checker grid for visual debugging.
    step = max(8, min(target.width, target.height) // 12)
    for y in range(0, target.height, step):
        for x in range(0, target.width, step):
            if ((x // step) + (y // step)) % 2 == 0:
                draw.rectangle(
                    (x, y, min(x + step - 1, target.width - 1), min(y + step - 1, target.height - 1)),
                    fill=(fg[0], fg[1], fg[2], 46),
                )

    draw.rectangle((0, 0, target.width - 1, target.height - 1), outline=(fg[0], fg[1], fg[2], 190), width=2)

    text_lines = [
        "CHROMA'S EDGE",
        "RUNTIME PLACEHOLDER",
        f"{target.category}/{target.name}.png",
        f"{target.width}x{target.height}",
    ]
    y = max(8, target.height // 2 - 28)
    for line in text_lines:
        tw = int(draw.textlength(line))
        x = max(6, (target.width - tw) // 2)
        draw.text((x, y), line, fill=(230, 230, 230, 255))
        y += 14

    return img


def main() -> int:
    args = parse_args()
    targets = collect_targets()

    created = 0
    skipped = 0
    overwritten = 0

    print("=" * 72)
    print("PROVISION RUNTIME IMAGE PLACEHOLDERS")
    print("=" * 72)
    print(f"Targets discovered: {len(targets)}")
    print(f"Mode: {'dry-run' if args.dry_run else ('overwrite' if args.overwrite else 'create-missing')}")
    print("-" * 72)

    for target in targets:
        out_path = target.path
        exists = out_path.exists()
        if exists and not args.overwrite:
            skipped += 1
            continue
        if not args.dry_run:
            out_path.parent.mkdir(parents=True, exist_ok=True)
            image = draw_placeholder(target)
            image.save(out_path, format="PNG")
        if exists:
            overwritten += 1
        else:
            created += 1

    print(f"Created: {created}")
    print(f"Overwritten: {overwritten}")
    print(f"Skipped existing: {skipped}")
    print("\nDone.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
