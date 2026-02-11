#!/usr/bin/env python3
"""
Validate runtime image/effect/movie references against filesystem assets.

Scans references from:
- data/System.json
- data/Actors.json
- data/Enemies.json
- data/Tilesets.json (map-used tilesets by default)
- data/Animations.json (Effekseer effect names)
- data/CommonEvents.json
- data/Troops.json
- data/Map###.json
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = ROOT / "data"
IMG_DIR = ROOT / "img"
EFFECTS_DIR = ROOT / "effects"
MOVIES_DIR = ROOT / "movies"

MAP_RE = re.compile(r"^Map\d{3}\.json$")
MOVIE_EXTS = (".webm", ".mp4", ".ogv", ".m4v")


@dataclass(frozen=True)
class Ref:
    kind: str
    token: str
    source: str


@dataclass(frozen=True)
class Issue:
    severity: str
    category: str
    detail: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate runtime image/effect/movie references."
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as errors.",
    )
    parser.add_argument(
        "--strict-effects",
        action="store_true",
        help="Treat missing animation effects as errors (default: warning).",
    )
    parser.add_argument(
        "--all-tilesets",
        action="store_true",
        help="Validate all Tilesets.json tilesetNames instead of map-used IDs only.",
    )
    return parser.parse_args()


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def add_ref(refs: list[Ref], kind: str, token: Any, source: str) -> None:
    if not isinstance(token, str):
        return
    text = token.strip()
    if not text:
        return
    refs.append(Ref(kind=kind, token=text, source=source))


def scan_move_command(refs: list[Ref], command: Any, source: str) -> None:
    if not isinstance(command, dict):
        return
    code = command.get("code")
    params = command.get("parameters")
    if code != 41 or not isinstance(params, list) or not params:
        return
    add_ref(refs, "characters", params[0], source)


def scan_move_route(refs: list[Ref], route: Any, source: str) -> None:
    if not isinstance(route, dict):
        return
    steps = route.get("list")
    if not isinstance(steps, list):
        return
    for move_idx, move_cmd in enumerate(steps):
        scan_move_command(refs, move_cmd, f"{source}.move[{move_idx}]")


def scan_command_list(refs: list[Ref], commands: Any, source_prefix: str) -> None:
    if not isinstance(commands, list):
        return
    for cmd_idx, cmd in enumerate(commands):
        if not isinstance(cmd, dict):
            continue
        code = cmd.get("code")
        params = cmd.get("parameters")
        if not isinstance(params, list):
            continue

        source = f"{source_prefix}.list[{cmd_idx}]"
        if code == 101:
            add_ref(refs, "faces", params[0] if params else None, source)
        elif code == 231:
            add_ref(refs, "pictures", params[1] if len(params) > 1 else None, source)
        elif code == 261:
            add_ref(refs, "movies", params[0] if params else None, source)
        elif code == 283:
            add_ref(refs, "battlebacks1", params[0] if params else None, source)
            add_ref(refs, "battlebacks2", params[1] if len(params) > 1 else None, source)
        elif code == 284:
            add_ref(refs, "parallaxes", params[0] if params else None, source)
        elif code == 322:
            add_ref(refs, "characters", params[1] if len(params) > 1 else None, source)
            add_ref(refs, "faces", params[3] if len(params) > 3 else None, source)
            add_ref(refs, "sv_actors", params[5] if len(params) > 5 else None, source)
        elif code == 323:
            add_ref(refs, "characters", params[1] if len(params) > 1 else None, source)
        elif code == 205:
            scan_move_route(refs, params[1] if len(params) > 1 else None, source)
        elif code == 505:
            scan_move_command(refs, params[0] if params else None, source)


def map_file_paths() -> list[Path]:
    out: list[Path] = []
    for path in sorted(DATA_DIR.glob("Map*.json")):
        if MAP_RE.match(path.name):
            out.append(path)
    return out


def map_used_tileset_ids(map_paths: list[Path]) -> set[int]:
    out: set[int] = set()
    for path in map_paths:
        payload = load_json(path)
        if not isinstance(payload, dict):
            continue
        tid = payload.get("tilesetId")
        if isinstance(tid, int) and tid > 0:
            out.add(tid)
    return out


def collect_refs(args: argparse.Namespace) -> list[Ref]:
    refs: list[Ref] = []
    map_paths = map_file_paths()

    system_path = DATA_DIR / "System.json"
    if system_path.exists():
        system = load_json(system_path)
        if isinstance(system, dict):
            add_ref(refs, "titles1", system.get("title1Name"), "System.title1Name")
            add_ref(refs, "titles2", system.get("title2Name"), "System.title2Name")
            add_ref(refs, "battlebacks1", system.get("battleback1Name"), "System.battleback1Name")
            add_ref(refs, "battlebacks2", system.get("battleback2Name"), "System.battleback2Name")
            add_ref(refs, "enemy_battler", system.get("battlerName"), "System.battlerName")
            for vehicle_key in ("boat", "ship", "airship"):
                vehicle = system.get(vehicle_key)
                if not isinstance(vehicle, dict):
                    continue
                add_ref(
                    refs,
                    "characters",
                    vehicle.get("characterName"),
                    f"System.{vehicle_key}.characterName",
                )

    actors_path = DATA_DIR / "Actors.json"
    if actors_path.exists():
        actors = load_json(actors_path)
        if isinstance(actors, list):
            for idx, actor in enumerate(actors):
                if not isinstance(actor, dict):
                    continue
                source = f"Actors[{idx}]"
                add_ref(refs, "characters", actor.get("characterName"), f"{source}.characterName")
                add_ref(refs, "faces", actor.get("faceName"), f"{source}.faceName")
                add_ref(refs, "sv_actors", actor.get("battlerName"), f"{source}.battlerName")

    enemies_path = DATA_DIR / "Enemies.json"
    if enemies_path.exists():
        enemies = load_json(enemies_path)
        if isinstance(enemies, list):
            for idx, enemy in enumerate(enemies):
                if not isinstance(enemy, dict):
                    continue
                add_ref(
                    refs,
                    "enemy_battler",
                    enemy.get("battlerName"),
                    f"Enemies[{idx}].battlerName",
                )

    tilesets_path = DATA_DIR / "Tilesets.json"
    if tilesets_path.exists():
        tilesets = load_json(tilesets_path)
        if isinstance(tilesets, list):
            valid_ids: set[int]
            if args.all_tilesets:
                valid_ids = {
                    idx
                    for idx, rec in enumerate(tilesets)
                    if idx > 0 and isinstance(rec, dict)
                }
            else:
                valid_ids = map_used_tileset_ids(map_paths)
            for tid in sorted(valid_ids):
                if tid <= 0 or tid >= len(tilesets):
                    continue
                rec = tilesets[tid]
                if not isinstance(rec, dict):
                    continue
                names = rec.get("tilesetNames")
                if not isinstance(names, list):
                    continue
                for name_idx, name in enumerate(names):
                    add_ref(refs, "tilesets", name, f"Tilesets[{tid}].tilesetNames[{name_idx}]")

    anim_path = DATA_DIR / "Animations.json"
    if anim_path.exists():
        anims = load_json(anim_path)
        if isinstance(anims, list):
            for idx, anim in enumerate(anims):
                if not isinstance(anim, dict):
                    continue
                add_ref(refs, "effects", anim.get("effectName"), f"Animations[{idx}].effectName")

    for seq_name in ("CommonEvents.json", "Troops.json"):
        path = DATA_DIR / seq_name
        if not path.exists():
            continue
        payload = load_json(path)
        if not isinstance(payload, list):
            continue
        for rec_idx, rec in enumerate(payload):
            if not isinstance(rec, dict):
                continue
            scan_command_list(refs, rec.get("list"), f"{seq_name}[{rec_idx}]")

    for path in map_paths:
        payload = load_json(path)
        if not isinstance(payload, dict):
            continue
        add_ref(refs, "battlebacks1", payload.get("battleback1Name"), f"{path.name}.battleback1Name")
        add_ref(refs, "battlebacks2", payload.get("battleback2Name"), f"{path.name}.battleback2Name")
        add_ref(refs, "parallaxes", payload.get("parallaxName"), f"{path.name}.parallaxName")

        events = payload.get("events")
        if not isinstance(events, list):
            continue
        for ev_idx, ev in enumerate(events):
            if not isinstance(ev, dict):
                continue
            pages = ev.get("pages")
            if not isinstance(pages, list):
                continue
            for page_idx, page in enumerate(pages):
                if not isinstance(page, dict):
                    continue
                image = page.get("image")
                if isinstance(image, dict):
                    add_ref(
                        refs,
                        "characters",
                        image.get("characterName"),
                        f"{path.name}.events[{ev_idx}].pages[{page_idx}].image.characterName",
                    )
                scan_command_list(
                    refs,
                    page.get("list"),
                    f"{path.name}.events[{ev_idx}].pages[{page_idx}]",
                )

    return refs


def exists_for_ref(ref: Ref) -> bool:
    token_path = Path(ref.token)
    if ref.kind == "battlebacks1":
        return (IMG_DIR / "battlebacks1" / f"{ref.token}.png").exists()
    if ref.kind == "battlebacks2":
        return (IMG_DIR / "battlebacks2" / f"{ref.token}.png").exists()
    if ref.kind == "titles1":
        return (IMG_DIR / "titles1" / f"{ref.token}.png").exists()
    if ref.kind == "titles2":
        return (IMG_DIR / "titles2" / f"{ref.token}.png").exists()
    if ref.kind == "parallaxes":
        return (IMG_DIR / "parallaxes" / f"{ref.token}.png").exists()
    if ref.kind == "characters":
        return (IMG_DIR / "characters" / f"{ref.token}.png").exists()
    if ref.kind == "faces":
        return (IMG_DIR / "faces" / f"{ref.token}.png").exists()
    if ref.kind == "sv_actors":
        return (IMG_DIR / "sv_actors" / f"{ref.token}.png").exists()
    if ref.kind == "pictures":
        return (IMG_DIR / "pictures" / f"{ref.token}.png").exists()
    if ref.kind == "tilesets":
        return (IMG_DIR / "tilesets" / f"{ref.token}.png").exists()
    if ref.kind == "effects":
        return (EFFECTS_DIR / f"{ref.token}.efkefc").exists()
    if ref.kind == "enemy_battler":
        return (
            (IMG_DIR / "enemies" / f"{ref.token}.png").exists()
            or (IMG_DIR / "sv_enemies" / f"{ref.token}.png").exists()
        )
    if ref.kind == "movies":
        if token_path.suffix:
            return (MOVIES_DIR / token_path).exists()
        return any((MOVIES_DIR / f"{ref.token}{ext}").exists() for ext in MOVIE_EXTS)
    return True


def severity_for(kind: str, strict_effects: bool) -> str:
    if kind == "effects":
        return "error" if strict_effects else "warning"
    if kind == "movies":
        return "warning"
    return "error"


def run_validation(args: argparse.Namespace) -> tuple[list[Issue], dict[str, int]]:
    refs = collect_refs(args)
    stats = {
        "refs": len(refs),
        "unique_refs": 0,
        "missing": 0,
    }
    by_kind: dict[str, int] = {}
    issues: list[Issue] = []

    unique: dict[tuple[str, str], list[Ref]] = {}
    for ref in refs:
        unique.setdefault((ref.kind, ref.token), []).append(ref)
        by_kind[ref.kind] = by_kind.get(ref.kind, 0) + 1
    stats["unique_refs"] = len(unique)

    for (kind, token), sources in sorted(unique.items(), key=lambda x: (x[0][0], x[0][1])):
        ref = Ref(kind=kind, token=token, source=sources[0].source)
        if exists_for_ref(ref):
            continue
        stats["missing"] += 1
        severity = severity_for(kind, args.strict_effects)
        source_sample = ", ".join(x.source for x in sources[:3])
        if len(sources) > 3:
            source_sample += ", ..."
        issues.append(
            Issue(
                severity=severity,
                category="missing_image_ref",
                detail=f"{kind}/{token} missing (referenced by {source_sample})",
            )
        )

    stats["by_kind"] = by_kind  # type: ignore[assignment]
    return issues, stats


def main() -> int:
    args = parse_args()
    issues, stats = run_validation(args)
    warnings = [x for x in issues if x.severity == "warning"]
    errors = [x for x in issues if x.severity == "error"]
    if args.strict and warnings:
        errors.extend(warnings)

    by_kind = stats.get("by_kind", {})
    if isinstance(by_kind, dict):
        kind_parts = [f"{k}={by_kind[k]}" for k in sorted(by_kind)]
        kind_summary = " ".join(kind_parts)
    else:
        kind_summary = ""

    print("=" * 72)
    print("RUNTIME IMAGE REFERENCE VALIDATION")
    print("=" * 72)
    print(f"References scanned: {stats['refs']}")
    print(f"Unique references: {stats['unique_refs']}")
    if kind_summary:
        print(f"By kind: {kind_summary}")
    print("-" * 72)
    print(f"Errors: {len([x for x in issues if x.severity == 'error'])}")
    print(f"Warnings: {len(warnings)}")
    if args.strict:
        print(f"Strict promoted warnings: {len(warnings)}")

    if issues:
        print("-" * 72)
        for issue in issues:
            print(f"[{issue.severity.upper():7}] {issue.category:20} {issue.detail}")
    else:
        print("\nRuntime image reference checks passed.")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
