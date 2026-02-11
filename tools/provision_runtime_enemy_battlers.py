#!/usr/bin/env python3
"""
Provision runtime enemy battler images for RPG Maker MZ.

This project currently uses starter enemy battler names in `data/Enemies.json`
(`Goblin`, `Gnome`, `Crow`, `Treant`, `Hi_monster`) while production enemy art
lives under `assets/sprites/enemies/`.

This tool maps each runtime battler name to a curated production source sprite,
upscales with nearest-neighbor, and writes both:
  - img/sv_enemies/<BattlerName>.png  (used when side-view is enabled)
  - img/enemies/<BattlerName>.png     (used when side-view is disabled)
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Dict

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
ENEMIES_PATH = ROOT / "data" / "Enemies.json"
SV_ENEMIES_DIR = ROOT / "img" / "sv_enemies"
ENEMIES_DIR = ROOT / "img" / "enemies"

SOURCE_MAP: Dict[str, Path] = {
    "Goblin": ROOT / "assets" / "sprites" / "enemies" / "dustbelt" / "spr_enemy_dust_skirmisher.png",
    "Gnome": ROOT / "assets" / "sprites" / "enemies" / "dungeon" / "spr_enemy_growth_lurker.png",
    "Crow": ROOT / "assets" / "sprites" / "enemies" / "dustbelt" / "spr_enemy_dust_wasp.png",
    "Treant": ROOT / "assets" / "sprites" / "enemies" / "dungeon" / "spr_enemy_bloom_sprout.png",
    "Hi_monster": ROOT / "assets" / "sprites" / "enemies" / "obsidian" / "spr_enemy_quarry_brute.png",
}

NEAREST = Image.Resampling.NEAREST


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Provision runtime enemy battlers in img/sv_enemies and img/enemies."
    )
    parser.add_argument(
        "--scale",
        type=int,
        default=3,
        help="Nearest-neighbor upscale factor (default: 3).",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite existing runtime battler files.",
    )
    return parser.parse_args()


def load_enemy_battler_names() -> list[str]:
    data = json.loads(ENEMIES_PATH.read_text(encoding="utf-8"))
    names: list[str] = []
    for rec in data:
        if not isinstance(rec, dict):
            continue
        name = rec.get("battlerName")
        if isinstance(name, str) and name and name not in names:
            names.append(name)
    return names


def upscale(src: Image.Image, factor: int) -> Image.Image:
    if factor <= 1:
        return src.copy()
    return src.resize((src.width * factor, src.height * factor), NEAREST)


def ensure_runtime_battler(name: str, source: Path, scale: int, overwrite: bool) -> None:
    if not source.exists():
        raise FileNotFoundError(f"Missing source sprite for {name}: {source}")

    SV_ENEMIES_DIR.mkdir(parents=True, exist_ok=True)
    ENEMIES_DIR.mkdir(parents=True, exist_ok=True)

    sv_out = SV_ENEMIES_DIR / f"{name}.png"
    fv_out = ENEMIES_DIR / f"{name}.png"

    if not overwrite and sv_out.exists() and fv_out.exists():
        print(f"Skip existing: {name}")
        return

    with Image.open(source) as src:
        rgba = src.convert("RGBA")
        up = upscale(rgba, scale)
        up.save(sv_out, format="PNG")
        up.save(fv_out, format="PNG")
    print(f"Provisioned {name}: {source.relative_to(ROOT)} -> {sv_out.relative_to(ROOT)}, {fv_out.relative_to(ROOT)}")


def main() -> None:
    args = parse_args()
    battlers = load_enemy_battler_names()
    missing: list[str] = []
    for name in battlers:
        source = SOURCE_MAP.get(name)
        if source is None:
            missing.append(name)
            continue
        ensure_runtime_battler(name, source, args.scale, args.overwrite)

    if missing:
        msg = ", ".join(missing)
        raise SystemExit(f"No source mapping configured for enemy battler(s): {msg}")


if __name__ == "__main__":
    main()
