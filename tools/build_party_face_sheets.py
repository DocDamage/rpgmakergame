#!/usr/bin/env python3
"""
Build RPG Maker MZ face sheets for the 13 Chroma's Edge party actors.

Input:
  assets/*_Portrait.(png|jpg)

Output:
  img/faces/ChromaPartyFacesA.png  (actors 1-8, indices 0-7)
  img/faces/ChromaPartyFacesB.png  (actors 9-13, indices 0-4)
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Dict, List

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
ASSETS_DIR = ROOT / "assets"
FACES_DIR = ROOT / "img" / "faces"
ACTORS_PATH = ROOT / "data" / "Actors.json"

FACE_W = 144
FACE_H = 144
SHEET_W = FACE_W * 4
SHEET_H = FACE_H * 2


PORTRAIT_MAP: Dict[int, str] = {
    1: "Kade_Portrait.png",
    2: "Nix-7_Portrait.jpg",
    3: "Renna_Kyte_Portrait.jpg",
    4: "Twist_Portrait.jpg",
    5: "Dr_Marin_Suresh_Portrait.jpg",
    6: "Dr_Ines_Sova_Portrait.jpg",
    7: "Grit_Portrait.jpg",
    8: "Ashka_Verne_Portrait.jpg",
    9: "Senna_Portrait.jpg",
    10: "Callum_Drake_Portrait.png",
    11: "Petra_Portrait.png",
    12: "Vex_Portrait.png",
    13: "Nadia_Korr_Portrait.png",
}


def focused_square_crop(im: Image.Image) -> Image.Image:
    w, h = im.size
    ratio = w / h if h else 1.0

    if ratio < 0.9:
        size = int(min(w, h) * 0.9)
        x = (w - size) // 2
        y = int(h * 0.12)
    elif ratio > 1.2:
        size = int(h * 0.85)
        x = (w - size) // 2
        y = int(h * 0.08)
    else:
        size = int(min(w, h) * 0.88)
        x = (w - size) // 2
        y = int((h - size) * 0.25)

    x = max(0, min(x, w - size))
    y = max(0, min(y, h - size))

    return im.crop((x, y, x + size, y + size))


def to_face_tile(path: Path) -> Image.Image:
    with Image.open(path) as src:
        rgb = src.convert("RGB")
    cropped = focused_square_crop(rgb)
    return cropped.resize((FACE_W, FACE_H), Image.Resampling.LANCZOS)


def build_sheet(actor_ids: List[int], output_name: str) -> None:
    sheet = Image.new("RGB", (SHEET_W, SHEET_H), (0, 0, 0))
    for idx, actor_id in enumerate(actor_ids):
        source_name = PORTRAIT_MAP[actor_id]
        source_path = ASSETS_DIR / source_name
        if not source_path.exists():
            raise FileNotFoundError(f"Missing portrait source: {source_path}")

        tile = to_face_tile(source_path)
        col = idx % 4
        row = idx // 4
        x = col * FACE_W
        y = row * FACE_H
        sheet.paste(tile, (x, y))

    FACES_DIR.mkdir(parents=True, exist_ok=True)
    out_path = FACES_DIR / output_name
    sheet.save(out_path, format="PNG")


def update_actor_face_mapping() -> None:
    actors = json.loads(ACTORS_PATH.read_text(encoding="utf-8"))
    for actor in actors:
        if not actor:
            continue
        actor_id = int(actor["id"])
        if 1 <= actor_id <= 8:
            actor["faceName"] = "ChromaPartyFacesA"
            actor["faceIndex"] = actor_id - 1
        elif 9 <= actor_id <= 13:
            actor["faceName"] = "ChromaPartyFacesB"
            actor["faceIndex"] = actor_id - 9

    ACTORS_PATH.write_text(
        json.dumps(actors, ensure_ascii=False, separators=(",", ":")),
        encoding="utf-8",
        newline="\n",
    )


def main() -> None:
    build_sheet(list(range(1, 9)), "ChromaPartyFacesA.png")
    build_sheet(list(range(9, 14)), "ChromaPartyFacesB.png")
    update_actor_face_mapping()
    print("Built img/faces/ChromaPartyFacesA.png")
    print("Built img/faces/ChromaPartyFacesB.png")
    print("Updated data/Actors.json face mapping for actor IDs 1-13")


if __name__ == "__main__":
    main()

