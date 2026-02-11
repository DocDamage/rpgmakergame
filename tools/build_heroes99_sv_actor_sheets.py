#!/usr/bin/env python3
"""
Build provisional RPG Maker MZ side-view actor sheets for the 13 party
protagonists from Heroes99 layered sources.

Outputs:
  - Runtime sheets: img/sv_actors/ce_sv_<slug>.png
  - Source mirrors: assets/sprites/characters/<slug>/battle/spr_<slug>_sv_actor_sheet.png
  - Preview board:  docs/reports/heroes99_sv_actor_party_preview_2026-02-10.png

Also updates:
  - data/Actors.json battlerName for actor IDs 1-13

Notes:
  - Heroes99 is not a native RPG Maker side-view actor format.
  - This pass synthesizes the 18 MZ actor motions from atlas poses.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List, Tuple

from PIL import Image, ImageDraw, ImageOps

from build_heroes99_overworld_sheets import HERO_SPECS, HeroSpec, compose_hero_atlas, find_heroes99_root


ROOT = Path(__file__).resolve().parents[1]
ACTORS_PATH = ROOT / "data" / "Actors.json"
IMG_SV_DIR = ROOT / "img" / "sv_actors"
ASSET_CHAR_DIR = ROOT / "assets" / "sprites" / "characters"
PREVIEW_PATH = ROOT / "docs" / "reports" / "heroes99_sv_actor_party_preview_2026-02-10.png"

CELL_W = 100
CELL_H = 40
SV_FRAME_W = 96
SV_FRAME_H = 96
MAX_POSE_W = 70
MAX_POSE_H = 88
TAG_CLEAR_W = 28
TAG_CLEAR_H = 10
MIRROR_X = True

MOTIONS: List[str] = [
    "walk",
    "wait",
    "chant",
    "guard",
    "damage",
    "evade",
    "thrust",
    "swing",
    "missile",
    "skill",
    "spell",
    "item",
    "escape",
    "victory",
    "dying",
    "abnormal",
    "sleep",
    "dead",
]

# 1-based (row, col) on Heroes99 atlas.
MOTION_POSES: Dict[str, List[Tuple[int, int]]] = {
    "walk": [(3, 1), (3, 2), (3, 3)],
    "wait": [(1, 1), (1, 2), (1, 3)],
    "chant": [(11, 1), (11, 2), (11, 3)],
    "guard": [(16, 1), (16, 2), (16, 3)],
    "damage": [(13, 1), (13, 2), (13, 3)],
    "evade": [(15, 2), (15, 3), (15, 4)],
    "thrust": [(6, 1), (6, 2), (6, 3)],
    "swing": [(7, 1), (7, 2), (7, 3)],
    "missile": [(8, 1), (8, 2), (8, 3)],
    "skill": [(9, 1), (9, 2), (9, 3)],
    "spell": [(12, 1), (12, 2), (12, 3)],
    "item": [(5, 1), (5, 2), (5, 3)],
    "escape": [(15, 3), (15, 4), (15, 5)],
    "victory": [(17, 1), (17, 2), (17, 1)],
    "dying": [(14, 1), (14, 2), (14, 3)],
    "abnormal": [(13, 2), (13, 3), (13, 2)],
    "sleep": [(14, 3), (14, 4), (14, 5)],
    "dead": [(14, 4), (14, 4), (14, 4)],
}

NEAREST = Image.Resampling.NEAREST


def clear_frame_tag(cell: Image.Image) -> Image.Image:
    out = cell.copy()
    px = out.load()
    for y in range(min(TAG_CLEAR_H, out.height)):
        for x in range(min(TAG_CLEAR_W, out.width)):
            px[x, y] = (0, 0, 0, 0)
    return out


def extract_pose_frame(atlas: Image.Image, row: int, col: int) -> Image.Image:
    left = (col - 1) * CELL_W
    top = (row - 1) * CELL_H
    cell = atlas.crop((left, top, left + CELL_W, top + CELL_H))
    cell = clear_frame_tag(cell)
    bbox = cell.getbbox()
    if bbox is None:
        return Image.new("RGBA", (SV_FRAME_W, SV_FRAME_H), (0, 0, 0, 0))

    pose = cell.crop(bbox)
    if MIRROR_X:
        pose = ImageOps.mirror(pose)

    scale = min(MAX_POSE_W / pose.width, MAX_POSE_H / pose.height)
    out_w = max(1, int(round(pose.width * scale)))
    out_h = max(1, int(round(pose.height * scale)))
    pose = pose.resize((out_w, out_h), NEAREST)

    frame = Image.new("RGBA", (SV_FRAME_W, SV_FRAME_H), (0, 0, 0, 0))
    x = (SV_FRAME_W - out_w) // 2
    y = SV_FRAME_H - out_h
    frame.alpha_composite(pose, (x, y))
    return frame


def build_sv_sheet(atlas: Image.Image) -> Image.Image:
    # MZ layout: 9 columns x 6 rows, cw=width/9 ch=height/6
    # cx = floor(motionIndex / 6) * 3 + pattern ; cy = motionIndex % 6
    out = Image.new("RGBA", (SV_FRAME_W * 9, SV_FRAME_H * 6), (0, 0, 0, 0))
    for motion_index, motion in enumerate(MOTIONS):
        frames = [extract_pose_frame(atlas, r, c) for (r, c) in MOTION_POSES[motion]]
        block_col = (motion_index // 6) * 3
        row = motion_index % 6
        for pattern, frame in enumerate(frames):
            x = (block_col + pattern) * SV_FRAME_W
            y = row * SV_FRAME_H
            out.alpha_composite(frame, (x, y))
    return out


def runtime_name(spec: HeroSpec) -> str:
    return f"ce_sv_{spec.slug}"


def source_sv_path(spec: HeroSpec) -> Path:
    folder_slug = spec.asset_slug or spec.slug
    return (
        ASSET_CHAR_DIR
        / folder_slug
        / "battle"
        / f"spr_{spec.slug}_sv_actor_sheet.png"
    )


def runtime_sv_path(spec: HeroSpec) -> Path:
    return IMG_SV_DIR / f"{runtime_name(spec)}.png"


def save_outputs(spec: HeroSpec, sheet: Image.Image) -> None:
    runtime_path = runtime_sv_path(spec)
    source_path = source_sv_path(spec)
    runtime_path.parent.mkdir(parents=True, exist_ok=True)
    source_path.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(runtime_path, format="PNG")
    sheet.save(source_path, format="PNG")


def update_actor_battlers() -> None:
    by_actor = {spec.actor_id: spec for spec in HERO_SPECS}
    actors = json.loads(ACTORS_PATH.read_text(encoding="utf-8"))
    for actor in actors:
        if not actor:
            continue
        actor_id = int(actor.get("id", 0))
        spec = by_actor.get(actor_id)
        if spec is None:
            continue
        actor["battlerName"] = runtime_name(spec)

    ACTORS_PATH.write_text(
        json.dumps(actors, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
        newline="\n",
    )


def build_preview() -> None:
    cols = 2
    margin = 14
    label_h = 18
    tile_w = 9 * SV_FRAME_W // 3
    tile_h = 6 * SV_FRAME_H // 3
    rows = (len(HERO_SPECS) + cols - 1) // cols
    out = Image.new(
        "RGBA",
        (margin + cols * (tile_w + margin), margin + rows * (tile_h + label_h + margin)),
        (24, 24, 28, 255),
    )
    draw = ImageDraw.Draw(out)
    for i, spec in enumerate(HERO_SPECS):
        col = i % cols
        row = i // cols
        x = margin + col * (tile_w + margin)
        y = margin + row * (tile_h + label_h + margin)
        with Image.open(runtime_sv_path(spec)) as src:
            thumb = src.resize((tile_w, tile_h), NEAREST)
        out.alpha_composite(thumb, (x, y))
        draw.text((x, y + tile_h + 2), f"{spec.actor_id:02d} {spec.slug}", fill=(220, 220, 220, 255))

    PREVIEW_PATH.parent.mkdir(parents=True, exist_ok=True)
    out.save(PREVIEW_PATH, format="PNG")


def main() -> None:
    source_root = find_heroes99_root()
    for spec in HERO_SPECS:
        atlas = compose_hero_atlas(source_root, spec)
        sheet = build_sv_sheet(atlas)
        save_outputs(spec, sheet)
        print(f"Built {runtime_sv_path(spec).relative_to(ROOT)}")
    update_actor_battlers()
    build_preview()
    print("Updated data/Actors.json battler mapping for actor IDs 1-13")
    print(f"Built {PREVIEW_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
