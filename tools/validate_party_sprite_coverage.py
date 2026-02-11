#!/usr/bin/env python3
"""
Validate protagonist runtime sprite coverage and actor bindings.

Checks:
1. Actor IDs 1-13 are bound to expected runtime character/battler sheets.
2. Runtime and source-overworld sheets exist and match expected RPG Maker MZ
   single-character dimensions (144x256).
3. Runtime and source-SV actor sheets exist and match expected MZ SV dimensions
   (864x576).
4. Overworld and SV frames are non-empty (no transparent-only frame cells).
"""

from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from PIL import Image

from build_heroes99_overworld_sheets import HERO_SPECS, HeroSpec


ROOT = Path(__file__).resolve().parents[1]
ACTORS_PATH = ROOT / "data" / "Actors.json"
IMG_CHAR_DIR = ROOT / "img" / "characters"
IMG_FACE_DIR = ROOT / "img" / "faces"
IMG_SV_DIR = ROOT / "img" / "sv_actors"
ASSET_CHAR_DIR = ROOT / "assets" / "sprites" / "characters"

OW_W = 144
OW_H = 256
OW_CELL_W = 48
OW_CELL_H = 64

SV_W = 864
SV_H = 576
SV_CELL_W = 96
SV_CELL_H = 96
SV_MOTIONS = 18


@dataclass(frozen=True)
class Issue:
    severity: str
    category: str
    detail: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate protagonist runtime sprite coverage and actor bindings."
    )
    parser.add_argument(
        "--actors-path",
        default=str(ACTORS_PATH),
        help="Path to Actors.json (default: data/Actors.json).",
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as errors.",
    )
    return parser.parse_args()


def load_json(path: Path) -> object:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def expected_asset_overworld_path(spec: HeroSpec) -> Path:
    folder_slug = spec.asset_slug or spec.slug
    return ASSET_CHAR_DIR / folder_slug / "overworld" / f"spr_{spec.slug}_overworld_sheet.png"


def expected_asset_sv_path(spec: HeroSpec) -> Path:
    folder_slug = spec.asset_slug or spec.slug
    return ASSET_CHAR_DIR / folder_slug / "battle" / f"spr_{spec.slug}_sv_actor_sheet.png"


def actor_by_id(actors: list[object], actor_id: int) -> dict | None:
    if actor_id <= 0 or actor_id >= len(actors):
        return None
    rec = actors[actor_id]
    if isinstance(rec, dict):
        return rec
    return None


def has_pixels(frame: Image.Image) -> bool:
    alpha = frame.getchannel("A")
    return alpha.getbbox() is not None


def iter_overworld_frames(sheet: Image.Image) -> Iterable[tuple[int, int, Image.Image]]:
    for row in range(4):
        for col in range(3):
            left = col * OW_CELL_W
            top = row * OW_CELL_H
            yield row, col, sheet.crop((left, top, left + OW_CELL_W, top + OW_CELL_H))


def iter_sv_motion_frames(sheet: Image.Image) -> Iterable[tuple[int, int, Image.Image]]:
    for motion_index in range(SV_MOTIONS):
        block_col = (motion_index // 6) * 3
        row = motion_index % 6
        for pattern in range(3):
            col = block_col + pattern
            left = col * SV_CELL_W
            top = row * SV_CELL_H
            frame = sheet.crop((left, top, left + SV_CELL_W, top + SV_CELL_H))
            yield motion_index, pattern, frame


def validate_overworld_sheet(path: Path, label: str, issues: list[Issue]) -> None:
    if not path.exists():
        issues.append(Issue("error", "overworld", f"{label} missing file: {path}"))
        return
    with Image.open(path) as img:
        sheet = img.convert("RGBA")
    if sheet.size != (OW_W, OW_H):
        issues.append(
            Issue(
                "error",
                "overworld",
                f"{label} expected {OW_W}x{OW_H}, got {sheet.size[0]}x{sheet.size[1]} ({path})",
            )
        )
        return

    blank = [(r, c) for (r, c, frame) in iter_overworld_frames(sheet) if not has_pixels(frame)]
    if blank:
        issues.append(
            Issue(
                "error",
                "overworld",
                f"{label} has blank overworld frame(s): {blank} ({path})",
            )
        )


def validate_sv_sheet(path: Path, label: str, issues: list[Issue]) -> None:
    if not path.exists():
        issues.append(Issue("error", "sv_actor", f"{label} missing file: {path}"))
        return
    with Image.open(path) as img:
        sheet = img.convert("RGBA")
    if sheet.size != (SV_W, SV_H):
        issues.append(
            Issue(
                "error",
                "sv_actor",
                f"{label} expected {SV_W}x{SV_H}, got {sheet.size[0]}x{sheet.size[1]} ({path})",
            )
        )
        return

    blank = [
        (motion, pattern)
        for (motion, pattern, frame) in iter_sv_motion_frames(sheet)
        if not has_pixels(frame)
    ]
    if blank:
        issues.append(
            Issue(
                "error",
                "sv_actor",
                f"{label} has blank SV frame(s): {blank[:12]}{' ...' if len(blank) > 12 else ''} ({path})",
            )
        )


def run_validation(args: argparse.Namespace) -> tuple[list[Issue], dict[str, int]]:
    issues: list[Issue] = []
    stats = {
        "actors_checked": 0,
        "overworld_sheets_checked": 0,
        "sv_sheets_checked": 0,
    }

    actors_path = Path(args.actors_path)
    if not actors_path.exists():
        issues.append(Issue("error", "inputs", f"Missing actors file: {actors_path}"))
        return issues, stats

    raw = load_json(actors_path)
    if not isinstance(raw, list):
        issues.append(Issue("error", "inputs", f"Actors JSON is not an array: {actors_path}"))
        return issues, stats
    actors: list[object] = raw

    for spec in HERO_SPECS:
        stats["actors_checked"] += 1
        actor = actor_by_id(actors, spec.actor_id)
        actor_label = f"actor {spec.actor_id:02d} ({spec.slug})"
        if actor is None:
            issues.append(Issue("error", "actors", f"{actor_label} missing record in Actors.json"))
            continue

        expected_char = f"$ce_{spec.slug}"
        expected_sv = f"ce_sv_{spec.slug}"
        char_name = actor.get("characterName")
        char_index = actor.get("characterIndex")
        battler_name = actor.get("battlerName")
        face_name = actor.get("faceName")

        if char_name != expected_char:
            issues.append(
                Issue(
                    "error",
                    "actors",
                    f"{actor_label} characterName mismatch: expected {expected_char}, got {char_name}",
                )
            )
        if char_index != 0:
            issues.append(
                Issue(
                    "error",
                    "actors",
                    f"{actor_label} characterIndex mismatch: expected 0, got {char_index}",
                )
            )
        if battler_name != expected_sv:
            issues.append(
                Issue(
                    "error",
                    "actors",
                    f"{actor_label} battlerName mismatch: expected {expected_sv}, got {battler_name}",
                )
            )
        if not isinstance(face_name, str) or not face_name:
            issues.append(Issue("warning", "actors", f"{actor_label} has empty faceName"))
        elif not (IMG_FACE_DIR / f"{face_name}.png").exists():
            issues.append(
                Issue(
                    "error",
                    "actors",
                    f"{actor_label} face image missing: {IMG_FACE_DIR / f'{face_name}.png'}",
                )
            )

        runtime_ow = IMG_CHAR_DIR / f"{expected_char}.png"
        source_ow = expected_asset_overworld_path(spec)
        validate_overworld_sheet(runtime_ow, f"{actor_label} runtime overworld", issues)
        validate_overworld_sheet(source_ow, f"{actor_label} source overworld", issues)
        stats["overworld_sheets_checked"] += 2

        runtime_sv = IMG_SV_DIR / f"{expected_sv}.png"
        source_sv = expected_asset_sv_path(spec)
        validate_sv_sheet(runtime_sv, f"{actor_label} runtime sv", issues)
        validate_sv_sheet(source_sv, f"{actor_label} source sv", issues)
        stats["sv_sheets_checked"] += 2

    return issues, stats


def main() -> int:
    args = parse_args()
    issues, stats = run_validation(args)

    errors = [x for x in issues if x.severity == "error"]
    warnings = [x for x in issues if x.severity == "warning"]
    if args.strict and warnings:
        errors.extend(warnings)

    print("=" * 68)
    print("PARTY SPRITE COVERAGE VALIDATION")
    print("=" * 68)
    print(f"Actors checked: {stats['actors_checked']}")
    print(f"Overworld sheets checked: {stats['overworld_sheets_checked']}")
    print(f"SV sheets checked: {stats['sv_sheets_checked']}")
    print("-" * 68)
    print(f"Errors: {len([x for x in issues if x.severity == 'error'])}")
    print(f"Warnings: {len(warnings)}")
    if args.strict:
        print(f"Strict promoted warnings: {len(warnings)}")

    if issues:
        print("-" * 68)
        for issue in issues:
            print(f"[{issue.severity.upper():7}] {issue.category:14} {issue.detail}")
    else:
        print("\nParty sprite coverage checks passed.")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
