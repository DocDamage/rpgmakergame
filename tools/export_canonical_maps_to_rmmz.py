#!/usr/bin/env python3
"""
Export canonical `assets/data/maps` records into RPG Maker runtime map stubs.

Generates:
- `data/MapXXX.json` for canonical maps (starting at Map002 by default)
- `data/MapInfos.json` entries for generated maps
- `assets/data/system/runtime_map_bridge_generated.json` mapping artifact

Design goals:
- deterministic map-id assignment
- idempotent re-runs
- preserve existing non-generated runtime maps (e.g. Map001 dev harness)
"""

from __future__ import annotations

import argparse
import json
import math
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
ASSET_MAPS_DIR = ROOT / "assets" / "data" / "maps"
BRIDGE_OUT = ROOT / "assets" / "data" / "system" / "runtime_map_bridge_generated.json"

MAP_FILE_RE = re.compile(r"^Map(\d{3})\.json$")
TAG_CANON_ID = re.compile(r"<\s*chromaMapId\s*:\s*([A-Za-z0-9_:-]+)\s*>", re.I)
TAG_GENERATED = re.compile(r"<\s*chromaGeneratedFromCanonical\s*:\s*true\s*>", re.I)


@dataclass(frozen=True)
class CanonMap:
    source_path: str
    map_id: str
    display_name: str
    map_type: str
    tileset: str
    width: int
    height: int
    music: str
    connections: list[dict[str, Any]]
    landmarks: list[dict[str, Any]]
    hazards: list[dict[str, Any]]
    interiors: list[dict[str, Any]]
    ambient_npcs: list[dict[str, Any]]
    regions: list[dict[str, Any]]
    points_of_interest: list[dict[str, Any]]
    puzzles: list[dict[str, Any]]
    story_events: list[str]
    key_npcs: list[str]
    notes: str
    unlock_condition: str


@dataclass(frozen=True)
class MarkerPalette:
    landmark_tile: int
    hazard_tile: int
    interior_tile: int
    ambient_tile: int
    region_tile: int
    puzzle_tile: int
    poi_tile: int


@dataclass(frozen=True)
class MotifProfile:
    profile_id: str
    line_thickness: int
    hub_radius: int
    landmark_radius: int
    hazard_radius: int
    interior_radius: int
    puzzle_radius: int
    region_stride: int
    add_cross_spokes: bool
    add_anchor_loop: bool
    add_region_borders: bool


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Export canonical map metadata to RPG Maker runtime map stubs."
    )
    parser.add_argument(
        "--start-map-id",
        type=int,
        default=2,
        help="First runtime map id allowed for generated maps (default: 2).",
    )
    parser.add_argument(
        "--prune-stale",
        action="store_true",
        help="Delete stale previously-generated runtime maps that no longer exist canonically.",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned changes without writing files.",
    )
    return parser.parse_args()


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def dump_json(path: Path, data: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=True, indent=2) + "\n", encoding="utf-8")


def clamp_int(value: int, lo: int, hi: int) -> int:
    return max(lo, min(hi, value))


def list_of_dicts(value: Any) -> list[dict[str, Any]]:
    if not isinstance(value, list):
        return []
    return [x for x in value if isinstance(x, dict)]


def list_of_strings(value: Any) -> list[str]:
    if not isinstance(value, list):
        return []
    out: list[str] = []
    for item in value:
        if isinstance(item, str):
            text = item.strip()
            if text:
                out.append(text)
    return out


def load_canonical_maps() -> dict[str, CanonMap]:
    out: dict[str, CanonMap] = {}
    for path in sorted(ASSET_MAPS_DIR.glob("map_*.json")):
        data = load_json(path)
        entries = data.get("maps") if isinstance(data.get("maps"), list) else [data]
        for rec in entries:
            if not isinstance(rec, dict):
                continue
            map_id = rec.get("id")
            if not isinstance(map_id, str) or not map_id:
                continue
            if map_id in out:
                # keep first; duplicate detection exists in validators.
                continue

            dims = rec.get("dimensions") if isinstance(rec.get("dimensions"), dict) else {}
            width = int(dims.get("width", 32)) if isinstance(dims.get("width", 32), int) else 32
            height = int(dims.get("height", 24)) if isinstance(dims.get("height", 24), int) else 24
            display = rec.get("display_name") if isinstance(rec.get("display_name"), str) else map_id
            map_type = rec.get("type") if isinstance(rec.get("type"), str) else "unknown"
            tileset = rec.get("tileset") if isinstance(rec.get("tileset"), str) else ""
            music = rec.get("music") if isinstance(rec.get("music"), str) else ""
            conns = rec.get("connections") if isinstance(rec.get("connections"), list) else []
            clean_conns = [c for c in conns if isinstance(c, dict)]
            landmarks = list_of_dicts(rec.get("landmarks"))
            hazards = list_of_dicts(rec.get("hazards"))
            interiors = list_of_dicts(rec.get("interiors"))
            ambient_npcs = list_of_dicts(rec.get("ambient_npcs"))
            regions = list_of_dicts(rec.get("regions"))
            pois = list_of_dicts(rec.get("points_of_interest"))
            puzzles = list_of_dicts(rec.get("puzzles"))
            story_events = list_of_strings(rec.get("events"))
            key_npcs = list_of_strings(rec.get("key_npcs"))
            notes = rec.get("notes") if isinstance(rec.get("notes"), str) else ""
            unlock_condition = (
                rec.get("unlock_condition") if isinstance(rec.get("unlock_condition"), str) else ""
            )

            out[map_id] = CanonMap(
                source_path=str(path.relative_to(ROOT)),
                map_id=map_id,
                display_name=display,
                map_type=map_type,
                tileset=tileset,
                width=max(8, width),
                height=max(8, height),
                music=music,
                connections=clean_conns,
                landmarks=landmarks,
                hazards=hazards,
                interiors=interiors,
                ambient_npcs=ambient_npcs,
                regions=regions,
                points_of_interest=pois,
                puzzles=puzzles,
                story_events=story_events,
                key_npcs=key_npcs,
                notes=notes,
                unlock_condition=unlock_condition,
            )
    return out


def tileset_id_for(cmap: CanonMap, tileset_count: int) -> int:
    name = cmap.tileset
    typ = cmap.map_type.lower()
    if name == "Tileset_OrionOverworld" or typ == "overworld":
        return 1 if tileset_count >= 1 else 0
    if "Interior" in name:
        return 3 if tileset_count >= 3 else 1
    if typ in {
        "dungeon",
        "dungeon_submap",
        "tower",
        "tower_arena",
        "palace",
        "post_game",
        "shrine",
    }:
        return 4 if tileset_count >= 4 else 2
    return 2 if tileset_count >= 2 else 1


def runtime_size_for(cmap: CanonMap) -> tuple[int, int]:
    # Scaled playable stub, preserving rough aspect ratio.
    w = clamp_int(int(round(cmap.width / 4.0)), 24, 80)
    h = clamp_int(int(round(cmap.height / 4.0)), 18, 60)
    return w, h


def sanitize_tag_value(value: str, fallback: str = "NA") -> str:
    clean = re.sub(r"[^A-Za-z0-9_:-]+", "_", value.strip())
    clean = re.sub(r"_+", "_", clean).strip("_")
    return clean or fallback


def to_finite_number(value: Any) -> float | None:
    if isinstance(value, (int, float)):
        num = float(value)
        if math.isfinite(num):
            return num
    return None


def scaled_axis(value: float, src_size: int, dst_size: int) -> int:
    if src_size <= 1:
        return clamp_int(int(round((dst_size - 1) / 2.0)), 1, dst_size - 2)
    scaled = value * float(dst_size - 1) / float(src_size - 1)
    return clamp_int(int(round(scaled)), 1, dst_size - 2)


def point_from_coords(coords: Any) -> tuple[float, float] | None:
    if not isinstance(coords, list) or len(coords) < 2:
        return None
    x = to_finite_number(coords[0])
    y = to_finite_number(coords[1])
    if x is None or y is None:
        return None
    return x, y


def area_center_from_coords(coords: Any) -> tuple[float, float] | None:
    if not isinstance(coords, list):
        return None
    if len(coords) >= 4:
        x1 = to_finite_number(coords[0])
        y1 = to_finite_number(coords[1])
        x2 = to_finite_number(coords[2])
        y2 = to_finite_number(coords[3])
        if None not in {x1, y1, x2, y2}:
            return ((x1 + x2) / 2.0, (y1 + y2) / 2.0)
    return point_from_coords(coords)


def canonical_point_to_runtime(
    cmap: CanonMap,
    point: tuple[float, float] | None,
    runtime_width: int,
    runtime_height: int,
) -> tuple[int, int] | None:
    if point is None:
        return None
    x = scaled_axis(point[0], cmap.width, runtime_width)
    y = scaled_axis(point[1], cmap.height, runtime_height)
    return x, y


def canonical_rect_to_runtime(
    cmap: CanonMap,
    coords: Any,
    runtime_width: int,
    runtime_height: int,
) -> tuple[int, int, int, int] | None:
    if not isinstance(coords, list) or len(coords) < 4:
        return None
    x1 = to_finite_number(coords[0])
    y1 = to_finite_number(coords[1])
    x2 = to_finite_number(coords[2])
    y2 = to_finite_number(coords[3])
    if None in {x1, y1, x2, y2}:
        return None
    rx1 = scaled_axis(min(x1, x2), cmap.width, runtime_width)
    ry1 = scaled_axis(min(y1, y2), cmap.height, runtime_height)
    rx2 = scaled_axis(max(x1, x2), cmap.width, runtime_width)
    ry2 = scaled_axis(max(y1, y2), cmap.height, runtime_height)
    return rx1, ry1, rx2, ry2


def reserve_event_slot(
    preferred_x: int,
    preferred_y: int,
    occupied: set[tuple[int, int]],
    width: int,
    height: int,
) -> tuple[int, int]:
    preferred = (
        clamp_int(preferred_x, 1, width - 2),
        clamp_int(preferred_y, 1, height - 2),
    )
    if preferred not in occupied:
        occupied.add(preferred)
        return preferred

    max_r = max(width, height)
    for radius in range(1, max_r + 1):
        # Deterministic square ring scan.
        for dx in range(-radius, radius + 1):
            x = clamp_int(preferred[0] + dx, 1, width - 2)
            y_top = clamp_int(preferred[1] - radius, 1, height - 2)
            y_bottom = clamp_int(preferred[1] + radius, 1, height - 2)
            for y in (y_top, y_bottom):
                candidate = (x, y)
                if candidate not in occupied:
                    occupied.add(candidate)
                    return candidate
        for dy in range(-radius + 1, radius):
            y = clamp_int(preferred[1] + dy, 1, height - 2)
            x_left = clamp_int(preferred[0] - radius, 1, width - 2)
            x_right = clamp_int(preferred[0] + radius, 1, width - 2)
            for x in (x_left, x_right):
                candidate = (x, y)
                if candidate not in occupied:
                    occupied.add(candidate)
                    return candidate

    occupied.add(preferred)
    return preferred


def pick_tile_candidates(
    flags: list[Any],
    lo: int,
    hi: int,
    predicate: Any,
    limit: int = 8,
) -> list[int]:
    out: list[int] = []
    for tid in range(max(1, lo), min(hi, len(flags))):
        flag = flags[tid]
        if not isinstance(flag, int):
            continue
        if predicate(flag):
            out.append(tid)
            if len(out) >= limit:
                break
    return out


def select_marker_palette(tilesets: list[Any], tileset_id: int) -> MarkerPalette:
    if tileset_id <= 0 or tileset_id >= len(tilesets):
        return MarkerPalette(0, 0, 0, 0, 0, 0, 0)
    ts = tilesets[tileset_id]
    if not isinstance(ts, dict):
        return MarkerPalette(0, 0, 0, 0, 0, 0, 0)
    flags = ts.get("flags")
    if not isinstance(flags, list):
        return MarkerPalette(0, 0, 0, 0, 0, 0, 0)

    # Prefer B-E page IDs for simple event marker graphics.
    star = pick_tile_candidates(flags, 0, 1536, lambda f: (f & 0x10) != 0, limit=12)
    solid = pick_tile_candidates(
        flags, 0, 1536, lambda f: (f & 0x10) == 0 and (f & 0x0F) != 0, limit=12
    )
    passable = pick_tile_candidates(
        flags, 0, 1536, lambda f: (f & 0x10) == 0 and (f & 0x0F) == 0, limit=12
    )

    landmark = star[0] if star else (solid[0] if solid else (passable[0] if passable else 0))
    hazard = solid[0] if solid else landmark
    interior = star[1] if len(star) > 1 else landmark
    ambient = passable[0] if passable else landmark
    region = passable[1] if len(passable) > 1 else ambient
    puzzle = solid[1] if len(solid) > 1 else hazard
    poi = star[2] if len(star) > 2 else landmark

    return MarkerPalette(
        landmark_tile=landmark,
        hazard_tile=hazard,
        interior_tile=interior,
        ambient_tile=ambient,
        region_tile=region,
        puzzle_tile=puzzle,
        poi_tile=poi,
    )


def find_passable_ground_tile(tilesets: list[Any], tileset_id: int) -> int:
    if tileset_id <= 0 or tileset_id >= len(tilesets):
        return 0
    ts = tilesets[tileset_id]
    if not isinstance(ts, dict):
        return 0
    flags = ts.get("flags")
    if not isinstance(flags, list):
        return 0
    # Search typical ground tile ranges first.
    ranges = [
        (2048, min(4096, len(flags))),
        (1536, min(2048, len(flags))),
        (0, min(1536, len(flags))),
    ]
    for lo, hi in ranges:
        for tid in range(lo, hi):
            flag = flags[tid]
            if not isinstance(flag, int):
                continue
            if (flag & 0x10) != 0:  # star tile
                continue
            if (flag & 0x0F) == 0:
                return tid
    return 0


def make_empty_map_data(width: int, height: int, ground_tile: int) -> list[int]:
    cells = width * height
    # Layer order: z0..z5
    return [ground_tile] * cells + [0] * (cells * 5)


def map_data_index(width: int, height: int, x: int, y: int, z: int) -> int:
    return (z * height + y) * width + x


def set_map_tile(
    map_data: list[int],
    width: int,
    height: int,
    x: int,
    y: int,
    z: int,
    tile_id: int,
) -> bool:
    if tile_id <= 0:
        return False
    if z < 0 or z > 3:
        return False
    if x < 0 or y < 0 or x >= width or y >= height:
        return False
    idx = map_data_index(width, height, x, y, z)
    if idx < 0 or idx >= len(map_data):
        return False
    if not isinstance(map_data[idx], int):
        return False
    if map_data[idx] != 0:
        return False
    map_data[idx] = tile_id
    return True


def paint_diamond(
    map_data: list[int],
    width: int,
    height: int,
    cx: int,
    cy: int,
    z: int,
    tile_id: int,
    radius: int,
    blocked: set[tuple[int, int]] | None = None,
) -> int:
    placed = 0
    rr = max(0, radius)
    for dx in range(-rr, rr + 1):
        max_dy = rr - abs(dx)
        for dy in range(-max_dy, max_dy + 1):
            x = cx + dx
            y = cy + dy
            if blocked is not None and (x, y) in blocked:
                continue
            if set_map_tile(map_data, width, height, x, y, z, tile_id):
                placed += 1
    return placed


def paint_line(
    map_data: list[int],
    width: int,
    height: int,
    start: tuple[int, int],
    end: tuple[int, int],
    z: int,
    tile_id: int,
    thickness: int = 0,
    blocked: set[tuple[int, int]] | None = None,
) -> int:
    x1, y1 = start
    x2, y2 = end
    steps = max(abs(x2 - x1), abs(y2 - y1))
    if steps <= 0:
        return paint_diamond(
            map_data,
            width,
            height,
            cx=x1,
            cy=y1,
            z=z,
            tile_id=tile_id,
            radius=max(0, thickness),
            blocked=blocked,
        )
    placed = 0
    for i in range(steps + 1):
        t = i / float(steps)
        x = int(round(x1 + (x2 - x1) * t))
        y = int(round(y1 + (y2 - y1) * t))
        placed += paint_diamond(
            map_data,
            width,
            height,
            cx=x,
            cy=y,
            z=z,
            tile_id=tile_id,
            radius=max(0, thickness),
            blocked=blocked,
        )
    return placed


def paint_region_pattern(
    map_data: list[int],
    width: int,
    height: int,
    rect: tuple[int, int, int, int],
    z: int,
    tile_id: int,
    stride: int = 4,
    blocked: set[tuple[int, int]] | None = None,
) -> int:
    x1, y1, x2, y2 = rect
    placed = 0
    for y in range(max(0, y1), min(height - 1, y2) + 1):
        for x in range(max(0, x1), min(width - 1, x2) + 1):
            if blocked is not None and (x, y) in blocked:
                continue
            if ((x + y) % max(2, stride)) != 0:
                continue
            if set_map_tile(map_data, width, height, x, y, z, tile_id):
                placed += 1
    return placed


def paint_rect_border(
    map_data: list[int],
    width: int,
    height: int,
    rect: tuple[int, int, int, int],
    z: int,
    tile_id: int,
    blocked: set[tuple[int, int]] | None = None,
) -> int:
    x1, y1, x2, y2 = rect
    placed = 0
    for x in range(max(0, x1), min(width - 1, x2) + 1):
        for y in (max(0, y1), min(height - 1, y2)):
            if blocked is not None and (x, y) in blocked:
                continue
            if set_map_tile(map_data, width, height, x, y, z, tile_id):
                placed += 1
    for y in range(max(0, y1), min(height - 1, y2) + 1):
        for x in (max(0, x1), min(width - 1, x2)):
            if blocked is not None and (x, y) in blocked:
                continue
            if set_map_tile(map_data, width, height, x, y, z, tile_id):
                placed += 1
    return placed


def unique_points(points: list[tuple[int, int]]) -> list[tuple[int, int]]:
    out: list[tuple[int, int]] = []
    seen: set[tuple[int, int]] = set()
    for point in points:
        if point in seen:
            continue
        seen.add(point)
        out.append(point)
    return out


def ordered_points_for_loop(
    points: list[tuple[int, int]],
    center: tuple[int, int],
) -> list[tuple[int, int]]:
    unique = unique_points(points)
    if len(unique) < 2:
        return unique

    cx, cy = center

    def key_func(p: tuple[int, int]) -> tuple[float, float]:
        dx = float(p[0] - cx)
        dy = float(p[1] - cy)
        return (math.atan2(dy, dx), dx * dx + dy * dy)

    return sorted(unique, key=key_func)


def motif_profile_for(cmap: CanonMap, width: int, height: int) -> MotifProfile:
    map_type = cmap.map_type.lower()
    large_map = max(width, height) >= 56

    if map_type == "overworld":
        return MotifProfile(
            profile_id="overworld_regional",
            line_thickness=1 if large_map else 0,
            hub_radius=3 if large_map else 2,
            landmark_radius=1,
            hazard_radius=2,
            interior_radius=1,
            puzzle_radius=1,
            region_stride=3,
            add_cross_spokes=True,
            add_anchor_loop=True,
            add_region_borders=True,
        )

    if map_type == "town":
        return MotifProfile(
            profile_id="town_plaza",
            line_thickness=1,
            hub_radius=2,
            landmark_radius=1,
            hazard_radius=1,
            interior_radius=1,
            puzzle_radius=1,
            region_stride=4,
            add_cross_spokes=True,
            add_anchor_loop=True,
            add_region_borders=False,
        )

    if map_type in {"tower", "tower_arena", "palace", "post_game"}:
        return MotifProfile(
            profile_id="spire_corridor",
            line_thickness=1,
            hub_radius=2,
            landmark_radius=1,
            hazard_radius=2,
            interior_radius=1,
            puzzle_radius=2,
            region_stride=4,
            add_cross_spokes=True,
            add_anchor_loop=False,
            add_region_borders=False,
        )

    if map_type in {"shrine", "hidden"}:
        return MotifProfile(
            profile_id="shrine_ring",
            line_thickness=0,
            hub_radius=2,
            landmark_radius=1,
            hazard_radius=2,
            interior_radius=1,
            puzzle_radius=2,
            region_stride=5,
            add_cross_spokes=False,
            add_anchor_loop=True,
            add_region_borders=False,
        )

    if map_type in {"dungeon", "dungeon_submap", "story_setpiece"}:
        return MotifProfile(
            profile_id="dungeon_corridor",
            line_thickness=1 if large_map else 0,
            hub_radius=1,
            landmark_radius=1,
            hazard_radius=2,
            interior_radius=1,
            puzzle_radius=2,
            region_stride=5,
            add_cross_spokes=False,
            add_anchor_loop=False,
            add_region_borders=False,
        )

    if map_type in {"route", "story_route", "special"}:
        return MotifProfile(
            profile_id="route_lane",
            line_thickness=1 if large_map else 0,
            hub_radius=2,
            landmark_radius=1,
            hazard_radius=2,
            interior_radius=1,
            puzzle_radius=1,
            region_stride=4,
            add_cross_spokes=False,
            add_anchor_loop=True,
            add_region_borders=False,
        )

    return MotifProfile(
        profile_id="default",
        line_thickness=0,
        hub_radius=2,
        landmark_radius=1,
        hazard_radius=2,
        interior_radius=1,
        puzzle_radius=1,
        region_stride=4,
        add_cross_spokes=False,
        add_anchor_loop=False,
        add_region_borders=False,
    )


def base_conditions() -> dict[str, Any]:
    return {
        "actorId": 1,
        "actorValid": False,
        "itemId": 1,
        "itemValid": False,
        "selfSwitchCh": "A",
        "selfSwitchValid": False,
        "switch1Id": 1,
        "switch1Valid": False,
        "switch2Id": 1,
        "switch2Valid": False,
        "variableId": 1,
        "variableValid": False,
        "variableValue": 0,
    }


def base_move_route() -> dict[str, Any]:
    return {
        "list": [{"code": 0, "parameters": []}],
        "repeat": True,
        "skippable": False,
        "wait": False,
    }


def empty_image() -> dict[str, Any]:
    return {
        "tileId": 0,
        "characterName": "",
        "direction": 2,
        "pattern": 0,
        "characterIndex": 0,
    }


def make_info_event(
    event_id: int,
    x: int,
    y: int,
    cmap: CanonMap,
    connection_count: int,
    anchor_count: int,
) -> dict[str, Any]:
    return {
        "id": event_id,
        "name": "EV_MAP_INFO",
        "note": "",
        "x": x,
        "y": y,
        "pages": [
            {
                "conditions": base_conditions(),
                "directionFix": False,
                "image": empty_image(),
                "list": [
                    {"code": 101, "indent": 0, "parameters": ["", 0, 0, 2, "Map Bridge"]},
                    {"code": 401, "indent": 0, "parameters": [f"{cmap.display_name} ({cmap.map_id})"]},
                    {
                        "code": 401,
                        "indent": 0,
                        "parameters": [
                            f"type={cmap.map_type}  links={connection_count}  anchors={anchor_count}"
                        ],
                    },
                    {"code": 0, "indent": 0, "parameters": []},
                ],
                "moveFrequency": 3,
                "moveRoute": base_move_route(),
                "moveSpeed": 3,
                "moveType": 0,
                "priorityType": 1,
                "stepAnime": False,
                "through": False,
                "trigger": 0,
                "walkAnime": True,
            }
        ],
    }


def normalize_direction(direction: str) -> str:
    d = direction.lower()
    if d in {"north", "up"}:
        return "north"
    if d in {"south", "down"}:
        return "south"
    if d in {"west", "left"}:
        return "west"
    if d in {"east", "right"}:
        return "east"
    return "special"


def slot_position(direction: str, index: int, count: int, width: int, height: int) -> tuple[int, int]:
    count = max(1, count)
    frac = (index + 1) / (count + 1)
    if direction == "north":
        x = clamp_int(int(round(frac * (width - 3))) + 1, 1, width - 2)
        return x, 1
    if direction == "south":
        x = clamp_int(int(round(frac * (width - 3))) + 1, 1, width - 2)
        return x, height - 2
    if direction == "west":
        y = clamp_int(int(round(frac * (height - 3))) + 1, 1, height - 2)
        return 1, y
    if direction == "east":
        y = clamp_int(int(round(frac * (height - 3))) + 1, 1, height - 2)
        return width - 2, y
    x = clamp_int(int(round(frac * (width - 3))) + 1, 1, width - 2)
    return x, max(2, height - 3)


def make_transfer_event(
    event_id: int,
    x: int,
    y: int,
    source_map_id: str,
    target_map_id: str,
    target_runtime_id: int,
    target_x: int,
    target_y: int,
    conn: dict[str, Any],
    gate_switch_id: int | None,
    portal_tile_id: int,
) -> dict[str, Any]:
    direction = conn.get("direction", "special")
    gate = conn.get("condition") or conn.get("trigger")
    gate_text = f" gate={gate}" if isinstance(gate, str) and gate else ""
    note_bits = [f"<chromaPortalTarget:{target_map_id}>"]
    if gate_text:
        note_bits.append(f"<chromaPortalGate:{gate}>")
    note = "\n".join(note_bits)
    name = f"EV_XFER_{direction.upper()}_{event_id:03d}"

    commands: list[dict[str, Any]] = [
        {
            "code": 108,
            "indent": 0,
            "parameters": [
                f"{source_map_id} -> {target_map_id}{gate_text}"
            ],
        }
    ]

    if isinstance(gate, str) and gate:
        if gate_switch_id is not None and gate_switch_id > 0:
            commands.extend(
                [
                    {"code": 111, "indent": 0, "parameters": [0, gate_switch_id, 0]},
                    {
                        "code": 201,
                        "indent": 1,
                        "parameters": [0, target_runtime_id, target_x, target_y, 0, 0],
                    },
                    {"code": 0, "indent": 1, "parameters": []},
                    {"code": 411, "indent": 0, "parameters": []},
                    {"code": 101, "indent": 1, "parameters": ["", 0, 0, 2, "Path Sealed"]},
                    {"code": 401, "indent": 1, "parameters": [f"Requires switch: {gate}."]},
                    {"code": 0, "indent": 1, "parameters": []},
                ]
            )
        else:
            # Fall back to quest-flag runtime check for non-switch gate tokens.
            gate_lit = json.dumps(gate)
            expr = (
                "(() => { "
                "const g = (typeof window !== 'undefined') ? window : globalThis; "
                "return !!(g && g.ChromaEdge && g.ChromaEdge.Quests && "
                f"typeof g.ChromaEdge.Quests.flag === 'function' && g.ChromaEdge.Quests.flag({gate_lit})); "
                "})()"
            )
            commands.extend(
                [
                    {"code": 111, "indent": 0, "parameters": [12, expr]},
                    {
                        "code": 201,
                        "indent": 1,
                        "parameters": [0, target_runtime_id, target_x, target_y, 0, 0],
                    },
                    {"code": 0, "indent": 1, "parameters": []},
                    {"code": 411, "indent": 0, "parameters": []},
                    {"code": 101, "indent": 1, "parameters": ["", 0, 0, 2, "Path Sealed"]},
                    {"code": 401, "indent": 1, "parameters": [f"Requires flag: {gate}."]},
                    {"code": 0, "indent": 1, "parameters": []},
                ]
            )
    else:
        commands.extend(
            [
                {
                    "code": 201,
                    "indent": 0,
                    "parameters": [0, target_runtime_id, target_x, target_y, 0, 0],
                },
                {"code": 0, "indent": 0, "parameters": []},
            ]
        )
    commands.append({"code": 0, "indent": 0, "parameters": []})

    return {
        "id": event_id,
        "name": name[:40],
        "note": note,
        "x": x,
        "y": y,
        "pages": [
            {
                "conditions": base_conditions(),
                "directionFix": False,
                "image": {
                    "tileId": portal_tile_id,
                    "characterName": "",
                    "direction": 2,
                    "pattern": 0,
                    "characterIndex": 0,
                },
                "list": commands,
                "moveFrequency": 3,
                "moveRoute": base_move_route(),
                "moveSpeed": 3,
                "moveType": 0,
                "priorityType": 1,
                "stepAnime": False,
                "through": False,
                "trigger": 0,  # action button
                "walkAnime": True,
            }
        ],
    }


def world_anchor_count(cmap: CanonMap) -> int:
    return (
        len(cmap.landmarks)
        + len(cmap.hazards)
        + len(cmap.interiors)
        + len(cmap.ambient_npcs)
        + len(cmap.regions)
        + len(cmap.points_of_interest)
        + len(cmap.puzzles)
        + len(cmap.story_events)
        + len(cmap.key_npcs)
    )


def make_marker_event(
    event_id: int,
    name_prefix: str,
    x: int,
    y: int,
    tile_id: int,
    note_tags: list[str],
    header: str,
    lines: list[str],
) -> dict[str, Any]:
    name = f"{name_prefix}_{event_id:03d}"[:40]
    note = "\n".join(note_tags)
    commands: list[dict[str, Any]] = []
    if lines:
        commands.append({"code": 101, "indent": 0, "parameters": ["", 0, 0, 2, header]})
        for text in lines[:4]:
            commands.append({"code": 401, "indent": 0, "parameters": [text[:120]]})
        commands.append({"code": 0, "indent": 0, "parameters": []})
    commands.append({"code": 0, "indent": 0, "parameters": []})
    return {
        "id": event_id,
        "name": name,
        "note": note,
        "x": x,
        "y": y,
        "pages": [
            {
                "conditions": base_conditions(),
                "directionFix": True,
                "image": {
                    "tileId": tile_id,
                    "characterName": "",
                    "direction": 2,
                    "pattern": 0,
                    "characterIndex": 0,
                },
                "list": commands,
                "moveFrequency": 3,
                "moveRoute": base_move_route(),
                "moveSpeed": 3,
                "moveType": 0,
                "priorityType": 1,
                "stepAnime": False,
                "through": True,
                "trigger": 0,
                "walkAnime": False,
            }
        ],
    }


def paint_world_geometry(
    map_data: list[int],
    width: int,
    height: int,
    cmap: CanonMap,
    palette: MarkerPalette,
    motif: MotifProfile,
    center: tuple[int, int],
    transfer_points: list[tuple[int, int]],
    poi_points: list[tuple[int, int]],
    landmark_points: list[tuple[int, int]],
    hazard_points: list[tuple[int, int]],
    interior_points: list[tuple[int, int]],
    ambient_points: list[tuple[int, int]],
    region_rects: list[tuple[int, int, int, int]],
    puzzle_points: list[tuple[int, int]],
    blocked: set[tuple[int, int]],
) -> int:
    painted = 0

    route_tile = palette.ambient_tile or palette.region_tile or palette.poi_tile
    region_tile = palette.region_tile or route_tile
    landmark_tile = palette.landmark_tile or route_tile
    hazard_tile = palette.hazard_tile or landmark_tile
    interior_tile = palette.interior_tile or landmark_tile
    ambient_tile = palette.ambient_tile or route_tile
    puzzle_tile = palette.puzzle_tile or hazard_tile

    center_x, center_y = center
    line_thickness = max(0, motif.line_thickness)
    region_stride = max(2, motif.region_stride)

    for rect in region_rects:
        painted += paint_region_pattern(
            map_data=map_data,
            width=width,
            height=height,
            rect=rect,
            z=1,
            tile_id=region_tile,
            stride=region_stride,
            blocked=blocked,
        )
        if motif.add_region_borders:
            painted += paint_rect_border(
                map_data=map_data,
                width=width,
                height=height,
                rect=rect,
                z=2,
                tile_id=route_tile,
                blocked=blocked,
            )

    for point in unique_points(transfer_points + poi_points):
        painted += paint_line(
            map_data=map_data,
            width=width,
            height=height,
            start=center,
            end=point,
            z=2,
            tile_id=route_tile,
            thickness=line_thickness,
            blocked=blocked,
        )

    if motif.add_cross_spokes:
        spoke_points = [
            (center_x, 1),
            (center_x, height - 2),
            (1, center_y),
            (width - 2, center_y),
        ]
        for edge in spoke_points:
            painted += paint_line(
                map_data=map_data,
                width=width,
                height=height,
                start=center,
                end=edge,
                z=2,
                tile_id=route_tile,
                thickness=max(0, line_thickness - 1),
                blocked=blocked,
            )

    if motif.add_anchor_loop:
        loop_points = ordered_points_for_loop(
            landmark_points + interior_points + transfer_points + poi_points,
            center=center,
        )
        if len(loop_points) >= 3:
            for idx, point in enumerate(loop_points):
                nxt = loop_points[(idx + 1) % len(loop_points)]
                painted += paint_line(
                    map_data=map_data,
                    width=width,
                    height=height,
                    start=point,
                    end=nxt,
                    z=2,
                    tile_id=route_tile,
                    thickness=0,
                    blocked=blocked,
                )
        elif len(loop_points) == 2:
            painted += paint_line(
                map_data=map_data,
                width=width,
                height=height,
                start=loop_points[0],
                end=loop_points[1],
                z=2,
                tile_id=route_tile,
                thickness=0,
                blocked=blocked,
            )

    for x, y in landmark_points:
        painted += paint_diamond(
            map_data=map_data,
            width=width,
            height=height,
            cx=x,
            cy=y,
            z=3,
            tile_id=landmark_tile,
            radius=max(1, motif.landmark_radius),
            blocked=blocked,
        )

    for x, y in hazard_points:
        painted += paint_diamond(
            map_data=map_data,
            width=width,
            height=height,
            cx=x,
            cy=y,
            z=3,
            tile_id=hazard_tile,
            radius=max(1, motif.hazard_radius),
            blocked=blocked,
        )

    for x, y in interior_points:
        painted += paint_diamond(
            map_data=map_data,
            width=width,
            height=height,
            cx=x,
            cy=y,
            z=3,
            tile_id=interior_tile,
            radius=max(1, motif.interior_radius),
            blocked=blocked,
        )

    for x, y in ambient_points:
        if (x, y) in blocked:
            continue
        if set_map_tile(
            map_data=map_data,
            width=width,
            height=height,
            x=x,
            y=y,
            z=3,
            tile_id=ambient_tile,
        ):
            painted += 1

    for x, y in puzzle_points:
        painted += paint_diamond(
            map_data=map_data,
            width=width,
            height=height,
            cx=x,
            cy=y,
            z=3,
            tile_id=puzzle_tile,
            radius=max(1, motif.puzzle_radius),
            blocked=blocked,
        )
        painted += paint_line(
            map_data=map_data,
            width=width,
            height=height,
            start=center,
            end=(x, y),
            z=2,
            tile_id=route_tile,
            thickness=0,
            blocked=blocked,
        )

    if motif.profile_id == "town_plaza":
        for point in unique_points(interior_points):
            painted += paint_line(
                map_data=map_data,
                width=width,
                height=height,
                start=center,
                end=point,
                z=2,
                tile_id=route_tile,
                thickness=max(0, line_thickness - 1),
                blocked=blocked,
            )
        painted += paint_diamond(
            map_data=map_data,
            width=width,
            height=height,
            cx=center_x,
            cy=center_y,
            z=2,
            tile_id=interior_tile,
            radius=max(2, motif.hub_radius + 1),
            blocked=blocked,
        )

    if motif.profile_id in {"dungeon_corridor", "spire_corridor"}:
        chain_points = ordered_points_for_loop(hazard_points + puzzle_points, center=center)
        if len(chain_points) >= 2:
            for idx in range(len(chain_points) - 1):
                painted += paint_line(
                    map_data=map_data,
                    width=width,
                    height=height,
                    start=chain_points[idx],
                    end=chain_points[idx + 1],
                    z=2,
                    tile_id=route_tile,
                    thickness=max(0, line_thickness - 1),
                    blocked=blocked,
                )

    # Add a map-type motif hub around center to make hubs readable.
    if motif.hub_radius > 0:
        painted += paint_diamond(
            map_data=map_data,
            width=width,
            height=height,
            cx=center_x,
            cy=center_y,
            z=2,
            tile_id=landmark_tile,
            radius=max(1, motif.hub_radius),
            blocked=blocked,
        )

    return painted


def parse_generated_mapping_from_runtime() -> dict[str, int]:
    out: dict[str, int] = {}
    for path in sorted(DATA_DIR.glob("Map*.json")):
        m = MAP_FILE_RE.match(path.name)
        if not m:
            continue
        map_id = int(m.group(1))
        data = load_json(path)
        if not isinstance(data, dict):
            continue
        note = data.get("note")
        if not isinstance(note, str):
            continue
        if not TAG_GENERATED.search(note):
            continue
        m_can = TAG_CANON_ID.search(note)
        if not m_can:
            continue
        can_id = m_can.group(1).strip()
        if can_id and can_id not in out:
            out[can_id] = map_id
    return out


def map_file_path(runtime_id: int) -> Path:
    return DATA_DIR / f"Map{runtime_id:03d}.json"


def main() -> int:
    args = parse_args()
    canonical = load_canonical_maps()
    if not canonical:
        print("No canonical maps found under assets/data/maps.")
        return 1

    tilesets = load_json(DATA_DIR / "Tilesets.json")
    if not isinstance(tilesets, list):
        print("data/Tilesets.json is invalid.")
        return 1
    system = load_json(DATA_DIR / "System.json")
    switches = system.get("switches") if isinstance(system, dict) else None
    switch_name_to_id: dict[str, int] = {}
    if isinstance(switches, list):
        for sid, name in enumerate(switches):
            if sid <= 0:
                continue
            if isinstance(name, str) and name:
                key = name.strip().upper()
                if key and key not in switch_name_to_id:
                    switch_name_to_id[key] = sid

    existing_generated = parse_generated_mapping_from_runtime()
    assigned: dict[str, int] = {}

    # Preserve existing generated assignments first.
    for can_id in sorted(canonical):
        if can_id in existing_generated:
            assigned[can_id] = existing_generated[can_id]

    used_ids = set(assigned.values())
    used_ids.add(1)  # keep dev map reserved
    next_id = max(args.start_map_id, 2)

    # Allocate deterministic new IDs for remaining canonical maps.
    for can_id in sorted(canonical):
        if can_id in assigned:
            continue
        while next_id in used_ids:
            next_id += 1
        assigned[can_id] = next_id
        used_ids.add(next_id)

    # Precompute runtime dimensions/tileset for transfer targets.
    runtime_dims: dict[str, tuple[int, int]] = {}
    runtime_tilesets: dict[str, int] = {}
    for can_id, cmap in canonical.items():
        runtime_dims[can_id] = runtime_size_for(cmap)
        runtime_tilesets[can_id] = tileset_id_for(cmap, len(tilesets) - 1)

    map_payloads: dict[int, dict[str, Any]] = {}
    for can_id in sorted(canonical):
        cmap = canonical[can_id]
        runtime_id = assigned[can_id]
        width, height = runtime_dims[can_id]
        tileset_id = runtime_tilesets[can_id]
        ground_tile = find_passable_ground_tile(tilesets, tileset_id)

        note_lines = [
            "<chromaGeneratedFromCanonical:true>",
            f"<chromaMapId:{cmap.map_id}>",
            f"<chromaMapType:{cmap.map_type}>",
            f"<chromaTileset:{cmap.tileset}>",
        ]

        marker_palette = select_marker_palette(tilesets, tileset_id)
        transfer_count = 0
        dressing_count = 0

        conns_by_dir: dict[str, list[dict[str, Any]]] = {
            "north": [],
            "south": [],
            "east": [],
            "west": [],
            "special": [],
        }
        for conn in cmap.connections:
            d = conn.get("direction")
            if not isinstance(d, str):
                d = "special"
            conns_by_dir[normalize_direction(d)].append(conn)

        events: list[Any] = [None]
        occupied: set[tuple[int, int]] = set()
        next_event_id = 1
        transfer_points: list[tuple[int, int]] = []
        poi_points: list[tuple[int, int]] = []
        landmark_points: list[tuple[int, int]] = []
        hazard_points: list[tuple[int, int]] = []
        interior_points: list[tuple[int, int]] = []
        ambient_points: list[tuple[int, int]] = []
        region_rects: list[tuple[int, int, int, int]] = []
        puzzle_points: list[tuple[int, int]] = []

        # Info event near center.
        info_x, info_y = reserve_event_slot(max(2, width // 2), max(2, height // 2), occupied, width, height)
        events.append(
            make_info_event(
                event_id=next_event_id,
                x=info_x,
                y=info_y,
                cmap=cmap,
                connection_count=len(cmap.connections),
                anchor_count=world_anchor_count(cmap),
            )
        )
        next_event_id += 1

        for direction in ("north", "south", "east", "west", "special"):
            group = conns_by_dir[direction]
            for idx, conn in enumerate(group):
                target = conn.get("target")
                if not isinstance(target, str) or target not in assigned:
                    continue
                tx_map_id = assigned[target]
                tw, th = runtime_dims[target]
                target_x = max(2, tw // 2)
                target_y = max(2, th // 2)

                conn_point = canonical_point_to_runtime(
                    cmap,
                    point_from_coords(conn.get("coords")),
                    width,
                    height,
                )
                if conn_point is None:
                    conn_point = slot_position(direction, idx, len(group), width, height)
                x, y = reserve_event_slot(conn_point[0], conn_point[1], occupied, width, height)

                gate_token = str((conn.get("condition") or conn.get("trigger") or "")).strip().upper()
                ev = make_transfer_event(
                    event_id=next_event_id,
                    x=x,
                    y=y,
                    source_map_id=cmap.map_id,
                    target_map_id=target,
                    target_runtime_id=tx_map_id,
                    target_x=target_x,
                    target_y=target_y,
                    conn=conn,
                    gate_switch_id=switch_name_to_id.get(gate_token),
                    portal_tile_id=marker_palette.poi_tile,
                )
                events.append(ev)
                next_event_id += 1
                transfer_count += 1
                transfer_points.append((x, y))

        # Convert points-of-interest into transfer portals where possible.
        for poi in cmap.points_of_interest:
            poi_name = poi.get("name") if isinstance(poi.get("name"), str) else "Point of Interest"
            target = poi.get("target")
            gate_value = poi.get("condition")
            gate_token = gate_value.strip().upper() if isinstance(gate_value, str) else ""
            poi_point = canonical_point_to_runtime(
                cmap,
                point_from_coords(poi.get("coords")),
                width,
                height,
            )
            if poi_point is None:
                poi_point = (max(2, width // 2), max(2, height // 2))
            x, y = reserve_event_slot(poi_point[0], poi_point[1], occupied, width, height)

            if isinstance(target, str) and target in assigned:
                tx_map_id = assigned[target]
                tw, th = runtime_dims[target]
                conn_like: dict[str, Any] = {"direction": "special"}
                if gate_token:
                    conn_like["condition"] = gate_token
                ev = make_transfer_event(
                    event_id=next_event_id,
                    x=x,
                    y=y,
                    source_map_id=cmap.map_id,
                    target_map_id=target,
                    target_runtime_id=tx_map_id,
                    target_x=max(2, tw // 2),
                    target_y=max(2, th // 2),
                    conn=conn_like,
                    gate_switch_id=switch_name_to_id.get(gate_token),
                    portal_tile_id=marker_palette.poi_tile,
                )
                poi_tags = [
                    "<chromaWorldDress:poi>",
                    f"<chromaPoiName:{sanitize_tag_value(poi_name)}>",
                ]
                if gate_token:
                    poi_tags.append(f"<chromaPoiGate:{sanitize_tag_value(gate_token)}>")
                if isinstance(ev.get("note"), str) and ev["note"]:
                    ev["note"] = ev["note"] + "\n" + "\n".join(poi_tags)
                else:
                    ev["note"] = "\n".join(poi_tags)
                events.append(ev)
                next_event_id += 1
                transfer_count += 1
                transfer_points.append((x, y))
                poi_points.append((x, y))
                continue

            marker_lines = [poi_name]
            if isinstance(target, str) and target:
                marker_lines.append(f"Target: {target}")
            if gate_token:
                marker_lines.append(f"Gate: {gate_token}")
            events.append(
                make_marker_event(
                    event_id=next_event_id,
                    name_prefix="EV_POI",
                    x=x,
                    y=y,
                    tile_id=marker_palette.poi_tile,
                    note_tags=[
                        "<chromaWorldDress:poi>",
                        f"<chromaPoiName:{sanitize_tag_value(poi_name)}>",
                    ],
                    header="Point of Interest",
                    lines=marker_lines,
                )
            )
            next_event_id += 1
            dressing_count += 1
            poi_points.append((x, y))

        for landmark in cmap.landmarks:
            name = landmark.get("name") if isinstance(landmark.get("name"), str) else "Landmark"
            ltype = landmark.get("type") if isinstance(landmark.get("type"), str) else "landmark"
            point = canonical_point_to_runtime(
                cmap,
                point_from_coords(landmark.get("coords")),
                width,
                height,
            )
            if point is None:
                continue
            x, y = reserve_event_slot(point[0], point[1], occupied, width, height)
            lines = [name, f"Type: {ltype}"]
            events.append(
                make_marker_event(
                    event_id=next_event_id,
                    name_prefix="EV_LMK",
                    x=x,
                    y=y,
                    tile_id=marker_palette.landmark_tile,
                    note_tags=[
                        "<chromaWorldDress:landmark>",
                        f"<chromaLandmarkType:{sanitize_tag_value(ltype)}>",
                    ],
                    header="Landmark",
                    lines=lines,
                )
            )
            next_event_id += 1
            dressing_count += 1
            landmark_points.append((x, y))

        for hazard in cmap.hazards:
            htype = hazard.get("type") if isinstance(hazard.get("type"), str) else "hazard"
            effect = hazard.get("effect") if isinstance(hazard.get("effect"), str) else ""
            point = canonical_point_to_runtime(
                cmap,
                area_center_from_coords(hazard.get("coords")),
                width,
                height,
            )
            if point is None:
                continue
            x, y = reserve_event_slot(point[0], point[1], occupied, width, height)
            lines = [f"Hazard: {htype}"]
            if effect:
                lines.append(f"Effect: {effect}")
            events.append(
                make_marker_event(
                    event_id=next_event_id,
                    name_prefix="EV_HAZ",
                    x=x,
                    y=y,
                    tile_id=marker_palette.hazard_tile,
                    note_tags=[
                        "<chromaWorldDress:hazard>",
                        f"<chromaHazardType:{sanitize_tag_value(htype)}>",
                    ],
                    header="Hazard",
                    lines=lines,
                )
            )
            next_event_id += 1
            dressing_count += 1
            hazard_points.append((x, y))

        for interior in cmap.interiors:
            itype = interior.get("type") if isinstance(interior.get("type"), str) else "interior"
            target = interior.get("target") if isinstance(interior.get("target"), str) else ""
            hidden = bool(interior.get("hidden"))
            point = canonical_point_to_runtime(
                cmap,
                point_from_coords(interior.get("coords")),
                width,
                height,
            )
            if point is None:
                continue
            x, y = reserve_event_slot(point[0], point[1], occupied, width, height)
            lines = [f"Entrance: {itype}"]
            if target:
                lines.append(f"Leads to: {target}")
            if hidden:
                lines.append("Hidden access.")
            tags = [
                "<chromaWorldDress:interior>",
                f"<chromaInteriorType:{sanitize_tag_value(itype)}>",
            ]
            if target:
                tags.append(f"<chromaInteriorTarget:{target}>")
            if hidden:
                tags.append("<chromaInteriorHidden:true>")
            events.append(
                make_marker_event(
                    event_id=next_event_id,
                    name_prefix="EV_INT",
                    x=x,
                    y=y,
                    tile_id=marker_palette.interior_tile,
                    note_tags=tags,
                    header="Interior",
                    lines=lines,
                )
            )
            next_event_id += 1
            dressing_count += 1
            interior_points.append((x, y))

        for ambient in cmap.ambient_npcs:
            npc_id = ambient.get("npc") if isinstance(ambient.get("npc"), str) else "NPC_UNKNOWN"
            dialog_tree = (
                ambient.get("dialog_tree") if isinstance(ambient.get("dialog_tree"), str) else ""
            )
            point = canonical_point_to_runtime(
                cmap,
                point_from_coords(ambient.get("coords")),
                width,
                height,
            )
            if point is None:
                continue
            x, y = reserve_event_slot(point[0], point[1], occupied, width, height)
            lines = [npc_id]
            if dialog_tree:
                lines.append(f"Dialog: {dialog_tree}")
            events.append(
                make_marker_event(
                    event_id=next_event_id,
                    name_prefix="EV_AMB",
                    x=x,
                    y=y,
                    tile_id=marker_palette.ambient_tile,
                    note_tags=[
                        "<chromaWorldDress:ambient_npc>",
                        f"<chromaAmbientNpc:{sanitize_tag_value(npc_id)}>",
                    ],
                    header="Local",
                    lines=lines,
                )
            )
            next_event_id += 1
            dressing_count += 1
            ambient_points.append((x, y))

        for region in cmap.regions:
            region_name = region.get("name") if isinstance(region.get("name"), str) else "region"
            encounters = (
                region.get("encounters") if isinstance(region.get("encounters"), str) else ""
            )
            point = canonical_point_to_runtime(
                cmap,
                area_center_from_coords(region.get("coords")),
                width,
                height,
            )
            if point is None:
                continue
            x, y = reserve_event_slot(point[0], point[1], occupied, width, height)
            lines = [region_name]
            if encounters:
                lines.append(f"Encounters: {encounters}")
            events.append(
                make_marker_event(
                    event_id=next_event_id,
                    name_prefix="EV_REGION",
                    x=x,
                    y=y,
                    tile_id=marker_palette.region_tile,
                    note_tags=[
                        "<chromaWorldDress:region>",
                        f"<chromaRegion:{sanitize_tag_value(region_name)}>",
                    ],
                    header="Region",
                    lines=lines,
                )
            )
            next_event_id += 1
            dressing_count += 1
            rect = canonical_rect_to_runtime(cmap, region.get("coords"), width, height)
            if rect is not None:
                region_rects.append(rect)

        for puzzle in cmap.puzzles:
            ptype = puzzle.get("type") if isinstance(puzzle.get("type"), str) else "puzzle"
            point = canonical_point_to_runtime(
                cmap,
                point_from_coords(puzzle.get("location") or puzzle.get("coords")),
                width,
                height,
            )
            if point is None:
                continue
            x, y = reserve_event_slot(point[0], point[1], occupied, width, height)
            events.append(
                make_marker_event(
                    event_id=next_event_id,
                    name_prefix="EV_PUZ",
                    x=x,
                    y=y,
                    tile_id=marker_palette.puzzle_tile,
                    note_tags=[
                        "<chromaWorldDress:puzzle>",
                        f"<chromaPuzzleType:{sanitize_tag_value(ptype)}>",
                    ],
                    header="Puzzle",
                    lines=[f"Mechanic: {ptype}"],
                )
            )
            next_event_id += 1
            dressing_count += 1
            puzzle_points.append((x, y))

        if cmap.story_events:
            story_lines = [f"Story beats: {len(cmap.story_events)}"]
            story_lines.extend(cmap.story_events[:3])
            sx, sy = reserve_event_slot(max(2, width // 2), max(3, (height // 2) + 2), occupied, width, height)
            events.append(
                make_marker_event(
                    event_id=next_event_id,
                    name_prefix="EV_STORY",
                    x=sx,
                    y=sy,
                    tile_id=marker_palette.puzzle_tile,
                    note_tags=["<chromaWorldDress:story_events>"],
                    header="Story State",
                    lines=story_lines,
                )
            )
            next_event_id += 1
            dressing_count += 1

        if cmap.key_npcs:
            npc_lines = [f"Key contacts: {len(cmap.key_npcs)}"]
            npc_lines.extend(cmap.key_npcs[:3])
            nx, ny = reserve_event_slot(max(2, width // 2), max(2, (height // 2) - 2), occupied, width, height)
            events.append(
                make_marker_event(
                    event_id=next_event_id,
                    name_prefix="EV_KEYNPC",
                    x=nx,
                    y=ny,
                    tile_id=marker_palette.ambient_tile,
                    note_tags=["<chromaWorldDress:key_npcs>"],
                    header="Key NPCs",
                    lines=npc_lines,
                )
            )
            next_event_id += 1
            dressing_count += 1

        if cmap.notes.strip():
            note_lines_text = [cmap.notes.strip()[:110]]
            bx, by = reserve_event_slot(max(2, width // 2), max(2, (height // 2) + 4), occupied, width, height)
            events.append(
                make_marker_event(
                    event_id=next_event_id,
                    name_prefix="EV_BRIEF",
                    x=bx,
                    y=by,
                    tile_id=marker_palette.landmark_tile,
                    note_tags=["<chromaWorldDress:notes>"],
                    header="Map Brief",
                    lines=note_lines_text,
                )
            )
            next_event_id += 1
            dressing_count += 1

        motif = motif_profile_for(cmap, width, height)
        map_data = make_empty_map_data(width, height, ground_tile)
        painted_tiles = paint_world_geometry(
            map_data=map_data,
            width=width,
            height=height,
            cmap=cmap,
            palette=marker_palette,
            motif=motif,
            center=(info_x, info_y),
            transfer_points=transfer_points,
            poi_points=poi_points,
            landmark_points=landmark_points,
            hazard_points=hazard_points,
            interior_points=interior_points,
            ambient_points=ambient_points,
            region_rects=region_rects,
            puzzle_points=puzzle_points,
            blocked=occupied,
        )

        note_lines.append(f"<chromaTransferEvents:{transfer_count}>")
        note_lines.append(f"<chromaDressingEvents:{dressing_count}>")
        note_lines.append(f"<chromaPaintedTiles:{painted_tiles}>")
        note_lines.append(f"<chromaMotifProfile:{motif.profile_id}>")
        if cmap.unlock_condition:
            note_lines.append(
                f"<chromaUnlockCondition:{sanitize_tag_value(cmap.unlock_condition)}>"
            )
        if cmap.notes.strip():
            note_lines.append("<chromaMapNotes:true>")

        payload = {
            "autoplayBgm": False,
            "autoplayBgs": False,
            "battleback1Name": "",
            "battleback2Name": "",
            "bgm": {"name": "", "pan": 0, "pitch": 100, "volume": 90},
            "bgs": {"name": "", "pan": 0, "pitch": 100, "volume": 90},
            "disableDashing": False,
            "displayName": cmap.display_name,
            "encounterList": [],
            "encounterStep": 30,
            "height": height,
            "note": "\n".join(note_lines),
            "parallaxLoopX": False,
            "parallaxLoopY": False,
            "parallaxName": "",
            "parallaxShow": True,
            "parallaxSx": 0,
            "parallaxSy": 0,
            "scrollType": 0,
            "specifyBattleback": False,
            "tilesetId": tileset_id,
            "width": width,
            "data": map_data,
            "events": events,
        }
        map_payloads[runtime_id] = payload

    # Build/patch MapInfos while preserving existing non-generated entries.
    map_infos_path = DATA_DIR / "MapInfos.json"
    map_infos = load_json(map_infos_path)
    if not isinstance(map_infos, list):
        print("data/MapInfos.json is invalid.")
        return 1

    highest_runtime_id = max([1] + list(map_payloads.keys()))
    if len(map_infos) <= highest_runtime_id:
        map_infos.extend([None] * (highest_runtime_id + 1 - len(map_infos)))

    for can_id, runtime_id in assigned.items():
        cmap = canonical[can_id]
        map_infos[runtime_id] = {
            "id": runtime_id,
            "expanded": False,
            "name": f"CAN_{cmap.map_id}"[:48],
            "order": runtime_id,
            "parentId": 0,
            "scrollX": 0,
            "scrollY": 0,
        }

    stale_ids: list[int] = []
    if args.prune_stale:
        current_generated_ids = set(existing_generated.values())
        valid_ids = set(assigned.values())
        stale_ids = sorted(x for x in current_generated_ids if x not in valid_ids)
        for rid in stale_ids:
            if rid < len(map_infos):
                map_infos[rid] = None

    # Build bridge artifact.
    bridge = {
        "id": "RUNTIME_MAP_BRIDGE_GENERATED",
        "summary": {
            "canonical_maps": len(canonical),
            "runtime_generated_maps": len(assigned),
            "start_map_id": args.start_map_id,
            "pruned_stale_runtime_maps": len(stale_ids),
        },
        "mappings": [
            {
                "canonical_map_id": can_id,
                "runtime_map_id": assigned[can_id],
                "display_name": canonical[can_id].display_name,
                "type": canonical[can_id].map_type,
                "source_path": canonical[can_id].source_path,
            }
            for can_id in sorted(assigned)
        ],
    }

    print("=" * 72)
    print("CANONICAL MAP EXPORT -> RPGMZ RUNTIME")
    print("=" * 72)
    print(f"Canonical maps: {len(canonical)}")
    print(f"Generated runtime maps: {len(assigned)}")
    print(f"Stale maps to prune: {len(stale_ids)}")
    print(f"Dry run: {'yes' if args.dry_run else 'no'}")

    if args.dry_run:
        return 0

    for rid, payload in sorted(map_payloads.items()):
        dump_json(map_file_path(rid), payload)

    if args.prune_stale:
        for rid in stale_ids:
            p = map_file_path(rid)
            if p.exists():
                p.unlink()

    dump_json(map_infos_path, map_infos)
    dump_json(BRIDGE_OUT, bridge)

    print("Write complete.")
    print(f"Updated: {map_infos_path.relative_to(ROOT)}")
    print(f"Updated: {BRIDGE_OUT.relative_to(ROOT)}")
    print("Map files written:", len(map_payloads))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
