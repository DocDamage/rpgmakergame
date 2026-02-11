#!/usr/bin/env python3
"""
Build provisional RPG Maker MZ overworld sheets for the 13 party protagonists
from Heroes99 layered sources.

Outputs:
  - Runtime sheets: img/characters/$ce_<slug>.png
  - Source copies:  assets/sprites/characters/<slug>/overworld/spr_<slug>_overworld_sheet.png
  - Preview board:  docs/reports/heroes99_overworld_party_preview_2026-02-10.png

Also updates:
  - data/Actors.json characterName/characterIndex for actor IDs 1-13

Notes:
  - Heroes99 is not a native RPG Maker walk-sheet pack. Direction rows are
    synthesized from compatible poses and mirrored side frames.
  - This pass is intended as production-usable placeholder/provisional runtime
    coverage until bespoke per-character directional walk sets are authored.
"""

from __future__ import annotations

import json
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Tuple

from PIL import Image, ImageDraw, ImageOps


ROOT = Path(__file__).resolve().parents[1]
ACTORS_PATH = ROOT / "data" / "Actors.json"
IMG_CHAR_DIR = ROOT / "img" / "characters"
ASSET_CHAR_DIR = ROOT / "assets" / "sprites" / "characters"
PREVIEW_PATH = ROOT / "docs" / "reports" / "heroes99_overworld_party_preview_2026-02-10.png"

HEROES99_ROOT_CANDIDATES = [
    ROOT / "img" / "heroes99",
    ROOT / "img" / "characters" / "protagonists" / "heroes99",
]

CELL_W = 100
CELL_H = 40
OUT_W = 48
OUT_H = 64
MAX_POSE_W = 38
MAX_POSE_H = 56
TAG_CLEAR_W = 28
TAG_CLEAR_H = 10

# 1-based (row, col) on the Heroes99 8x17 atlas.
POSE_MAP: Dict[str, List[Tuple[int, int]]] = {
    "down": [(3, 1), (3, 2), (3, 1)],
    "right": [(1, 1), (1, 2), (1, 3)],
    "up": [(4, 1), (4, 2), (4, 1)],
}


@dataclass(frozen=True)
class HeroSpec:
    actor_id: int
    slug: str
    skin: int
    face: int
    hair_style: str
    hair_color: int
    cloth: int
    cloth_color: int
    asset_slug: str | None = None

    @property
    def runtime_name(self) -> str:
        return f"$ce_{self.slug}"

    @property
    def source_sheet_path(self) -> Path:
        folder_slug = self.asset_slug or self.slug
        return (
            ASSET_CHAR_DIR
            / folder_slug
            / "overworld"
            / f"spr_{self.slug}_overworld_sheet.png"
        )

    @property
    def runtime_sheet_path(self) -> Path:
        return IMG_CHAR_DIR / f"{self.runtime_name}.png"


HERO_SPECS: List[HeroSpec] = [
    HeroSpec(1, "kade", 3, 1, "m3", 2, 1, 2),
    HeroSpec(2, "nix7", 2, 5, "f1", 4, 11, 4, asset_slug="nix-7"),
    HeroSpec(3, "renna", 3, 2, "f2", 7, 10, 8),
    HeroSpec(4, "twist", 4, 2, "m2", 1, 2, 6),
    HeroSpec(5, "suresh", 2, 4, "f6", 2, 4, 1),
    HeroSpec(6, "sova", 2, 3, "f5", 8, 13, 5),
    HeroSpec(7, "grit", 4, 6, "m7", 1, 6, 2),
    HeroSpec(8, "ashka", 4, 2, "f8", 2, 12, 6),
    HeroSpec(9, "senna", 3, 7, "m1", 1, 9, 7),
    HeroSpec(10, "callum", 2, 1, "m6", 2, 15, 4),
    HeroSpec(11, "petra", 5, 6, "m9", 1, 11, 2),
    HeroSpec(12, "vex", 2, 1, "m4", 3, 5, 1),
    HeroSpec(13, "korr", 3, 5, "f7", 1, 14, 2),
]

NEAREST = Image.Resampling.NEAREST


def find_heroes99_root() -> Path:
    for candidate in HEROES99_ROOT_CANDIDATES:
        if (candidate / "skin" / "skin_c1.png").exists():
            return candidate
    joined = "\n".join(str(p) for p in HEROES99_ROOT_CANDIDATES)
    raise FileNotFoundError(
        "Could not find Heroes99 source root. Checked:\n" + joined
    )


def compose_hero_atlas(source_root: Path, spec: HeroSpec) -> Image.Image:
    layer_paths = [
        source_root / "skin" / f"skin_c{spec.skin}.png",
        source_root / "face" / f"face_c{spec.face}.png",
        source_root
        / "cloth"
        / f"cloth{spec.cloth}"
        / f"cloth{spec.cloth}_bot"
        / f"cloth{spec.cloth}_c{spec.cloth_color}_bot.png",
        source_root
        / "cloth"
        / f"cloth{spec.cloth}"
        / f"cloth{spec.cloth}_top"
        / f"cloth{spec.cloth}_c{spec.cloth_color}_top.png",
        source_root
        / "hair"
        / spec.hair_style
        / f"{spec.hair_style}_bot"
        / f"{spec.hair_style}_c{spec.hair_color}_bot.png",
        source_root
        / "hair"
        / spec.hair_style
        / f"{spec.hair_style}_top"
        / f"{spec.hair_style}_c{spec.hair_color}_top.png",
    ]

    for layer_path in layer_paths:
        if not layer_path.exists():
            raise FileNotFoundError(f"Missing layer: {layer_path}")

    atlas = Image.new("RGBA", (CELL_W * 8, CELL_H * 17), (0, 0, 0, 0))
    for layer_path in layer_paths:
        with Image.open(layer_path) as layer:
            atlas.alpha_composite(layer.convert("RGBA"))
    return atlas


def _clear_frame_tag(cell: Image.Image) -> Image.Image:
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
    cell = _clear_frame_tag(cell)
    bbox = cell.getbbox()
    if bbox is None:
        return Image.new("RGBA", (OUT_W, OUT_H), (0, 0, 0, 0))

    pose = cell.crop(bbox)
    scale = min(MAX_POSE_W / pose.width, MAX_POSE_H / pose.height)
    out_w = max(1, int(round(pose.width * scale)))
    out_h = max(1, int(round(pose.height * scale)))
    pose = pose.resize((out_w, out_h), NEAREST)

    frame = Image.new("RGBA", (OUT_W, OUT_H), (0, 0, 0, 0))
    x = (OUT_W - out_w) // 2
    y = OUT_H - out_h
    frame.alpha_composite(pose, (x, y))
    return frame


def build_rmmz_sheet(atlas: Image.Image) -> Image.Image:
    down = [extract_pose_frame(atlas, r, c) for (r, c) in POSE_MAP["down"]]
    right = [extract_pose_frame(atlas, r, c) for (r, c) in POSE_MAP["right"]]
    left = [ImageOps.mirror(frame) for frame in right]
    up = [extract_pose_frame(atlas, r, c) for (r, c) in POSE_MAP["up"]]

    # RPG Maker row order for character sheets: down, left, right, up.
    rows = [down, left, right, up]

    sheet = Image.new("RGBA", (OUT_W * 3, OUT_H * 4), (0, 0, 0, 0))
    for row_idx, row_frames in enumerate(rows):
        for col_idx, frame in enumerate(row_frames):
            sheet.alpha_composite(frame, (col_idx * OUT_W, row_idx * OUT_H))
    return sheet


def save_outputs(spec: HeroSpec, sheet: Image.Image) -> None:
    spec.runtime_sheet_path.parent.mkdir(parents=True, exist_ok=True)
    spec.source_sheet_path.parent.mkdir(parents=True, exist_ok=True)
    sheet.save(spec.runtime_sheet_path, format="PNG")
    sheet.save(spec.source_sheet_path, format="PNG")


def update_actor_character_mapping(specs: Iterable[HeroSpec]) -> None:
    by_actor = {spec.actor_id: spec for spec in specs}
    actors = json.loads(ACTORS_PATH.read_text(encoding="utf-8"))
    for actor in actors:
        if not actor:
            continue
        actor_id = int(actor.get("id", 0))
        spec = by_actor.get(actor_id)
        if spec is None:
            continue
        actor["characterName"] = spec.runtime_name
        actor["characterIndex"] = 0

    ACTORS_PATH.write_text(
        json.dumps(actors, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
        newline="\n",
    )


def build_preview(specs: List[HeroSpec]) -> None:
    cols = 4
    margin = 16
    label_h = 18
    tile_w = OUT_W * 3
    tile_h = OUT_H * 4
    rows = (len(specs) + cols - 1) // cols
    canvas_w = margin + cols * (tile_w + margin)
    canvas_h = margin + rows * (tile_h + label_h + margin)
    out = Image.new("RGBA", (canvas_w, canvas_h), (26, 26, 30, 255))
    draw = ImageDraw.Draw(out)

    for i, spec in enumerate(specs):
        col = i % cols
        row = i // cols
        x = margin + col * (tile_w + margin)
        y = margin + row * (tile_h + label_h + margin)
        with Image.open(spec.runtime_sheet_path) as sheet:
            out.alpha_composite(sheet.convert("RGBA"), (x, y))
        draw.text((x, y + tile_h + 2), f"{spec.actor_id:02d} {spec.slug}", fill=(220, 220, 220, 255))

    PREVIEW_PATH.parent.mkdir(parents=True, exist_ok=True)
    out.save(PREVIEW_PATH, format="PNG")


def main() -> None:
    source_root = find_heroes99_root()
    for spec in HERO_SPECS:
        atlas = compose_hero_atlas(source_root, spec)
        sheet = build_rmmz_sheet(atlas)
        save_outputs(spec, sheet)
        print(f"Built {spec.runtime_sheet_path.relative_to(ROOT)}")

    update_actor_character_mapping(HERO_SPECS)
    build_preview(HERO_SPECS)
    print("Updated data/Actors.json character mapping for actor IDs 1-13")
    print(f"Built {PREVIEW_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
