#!/usr/bin/env python3
"""
Validate runtime audio token coverage against RPG Maker runtime folders.

Checks references from:
- data/System.json
- data/CommonEvents.json
- data/Troops.json
- data/Map###.json

And ensures each token resolves in:
- audio/bgm
- audio/bgs
- audio/me
- audio/se
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
AUDIO_DIR = ROOT / "audio"
MAP_RE = re.compile(r"^Map\d{3}\.json$")
AUDIO_EXTS = (".ogg", ".m4a", ".wav", ".mp3")


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
        description="Validate runtime audio references resolve to files in audio/*."
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Treat warnings as errors.",
    )
    return parser.parse_args()


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as fh:
        return json.load(fh)


def add_ref(refs: list[Ref], kind: str, obj: Any, source: str) -> None:
    if not isinstance(obj, dict):
        return
    token = obj.get("name")
    if not isinstance(token, str):
        return
    token = token.strip()
    if not token:
        return
    refs.append(Ref(kind=kind, token=token, source=source))


def collect_refs() -> list[Ref]:
    refs: list[Ref] = []

    system_path = DATA_DIR / "System.json"
    if system_path.exists():
        system = load_json(system_path)
        if isinstance(system, dict):
            add_ref(refs, "bgm", system.get("battleBgm"), "System.battleBgm")
            add_ref(refs, "bgm", system.get("titleBgm"), "System.titleBgm")
            add_ref(refs, "me", system.get("defeatMe"), "System.defeatMe")
            add_ref(refs, "me", system.get("victoryMe"), "System.victoryMe")
            add_ref(refs, "me", system.get("gameoverMe"), "System.gameoverMe")
            for vehicle_key in ("boat", "ship", "airship"):
                vehicle = system.get(vehicle_key)
                if isinstance(vehicle, dict):
                    add_ref(refs, "bgm", vehicle.get("bgm"), f"System.{vehicle_key}.bgm")
            sounds = system.get("sounds")
            if isinstance(sounds, list):
                for idx, entry in enumerate(sounds):
                    add_ref(refs, "se", entry, f"System.sounds[{idx}]")

    for data_name in ("CommonEvents.json", "Troops.json"):
        path = DATA_DIR / data_name
        if not path.exists():
            continue
        payload = load_json(path)
        if not isinstance(payload, list):
            continue
        for rec_idx, rec in enumerate(payload):
            if not isinstance(rec, dict):
                continue
            cmd_list = rec.get("list")
            if not isinstance(cmd_list, list):
                continue
            for cmd_idx, cmd in enumerate(cmd_list):
                if not isinstance(cmd, dict):
                    continue
                code = cmd.get("code")
                params = cmd.get("parameters")
                if not isinstance(params, list) or not params:
                    continue
                source_prefix = f"{data_name}[{rec_idx}].list[{cmd_idx}]"
                if code == 241:
                    add_ref(refs, "bgm", params[0], source_prefix)
                elif code == 245:
                    add_ref(refs, "bgs", params[0], source_prefix)
                elif code == 249:
                    add_ref(refs, "me", params[0], source_prefix)
                elif code == 250:
                    add_ref(refs, "se", params[0], source_prefix)

    for path in sorted(DATA_DIR.glob("Map*.json")):
        if not MAP_RE.match(path.name):
            continue
        payload = load_json(path)
        if not isinstance(payload, dict):
            continue
        add_ref(refs, "bgm", payload.get("bgm"), f"{path.name}.bgm")
        add_ref(refs, "bgs", payload.get("bgs"), f"{path.name}.bgs")

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
                cmd_list = page.get("list")
                if not isinstance(cmd_list, list):
                    continue
                for cmd_idx, cmd in enumerate(cmd_list):
                    if not isinstance(cmd, dict):
                        continue
                    code = cmd.get("code")
                    params = cmd.get("parameters")
                    if not isinstance(params, list) or not params:
                        continue
                    source_prefix = (
                        f"{path.name}.events[{ev_idx}].pages[{page_idx}].list[{cmd_idx}]"
                    )
                    if code == 241:
                        add_ref(refs, "bgm", params[0], source_prefix)
                    elif code == 245:
                        add_ref(refs, "bgs", params[0], source_prefix)
                    elif code == 249:
                        add_ref(refs, "me", params[0], source_prefix)
                    elif code == 250:
                        add_ref(refs, "se", params[0], source_prefix)

    return refs


def token_exists(kind: str, token: str) -> bool:
    folder = AUDIO_DIR / kind
    for ext in AUDIO_EXTS:
        if (folder / f"{token}{ext}").exists():
            return True
    return False


def run_validation(args: argparse.Namespace) -> tuple[list[Issue], dict[str, int]]:
    refs = collect_refs()
    issues: list[Issue] = []
    stats = {
        "refs": len(refs),
        "bgm_refs": 0,
        "bgs_refs": 0,
        "me_refs": 0,
        "se_refs": 0,
        "unique_tokens": 0,
    }

    unique: dict[tuple[str, str], list[Ref]] = {}
    for ref in refs:
        if ref.kind in ("bgm", "bgs", "me", "se"):
            stats[f"{ref.kind}_refs"] += 1
        unique.setdefault((ref.kind, ref.token), []).append(ref)
    stats["unique_tokens"] = len(unique)

    for kind in ("bgm", "bgs", "me", "se"):
        if stats[f"{kind}_refs"] <= 0:
            continue
        if not (AUDIO_DIR / kind).exists():
            issues.append(
                Issue(
                    "warning",
                    "audio_dirs",
                    f"Missing runtime audio folder: {AUDIO_DIR / kind}",
                )
            )

    for (kind, token), sources in sorted(unique.items(), key=lambda x: (x[0][0], x[0][1])):
        if token_exists(kind, token):
            continue
        source_sample = ", ".join(x.source for x in sources[:3])
        if len(sources) > 3:
            source_sample += ", ..."
        issues.append(
            Issue(
                "error",
                "missing_audio",
                f"{kind}/{token} missing (referenced by {source_sample})",
            )
        )

    return issues, stats


def main() -> int:
    args = parse_args()
    issues, stats = run_validation(args)
    warnings = [x for x in issues if x.severity == "warning"]
    errors = [x for x in issues if x.severity == "error"]
    if args.strict and warnings:
        errors.extend(warnings)

    print("=" * 72)
    print("RUNTIME AUDIO REFERENCE VALIDATION")
    print("=" * 72)
    print(f"References scanned: {stats['refs']}")
    print(
        f"By kind: bgm={stats['bgm_refs']} bgs={stats['bgs_refs']} me={stats['me_refs']} se={stats['se_refs']}"
    )
    print(f"Unique tokens: {stats['unique_tokens']}")
    print("-" * 72)
    print(f"Errors: {len([x for x in issues if x.severity == 'error'])}")
    print(f"Warnings: {len(warnings)}")
    if args.strict:
        print(f"Strict promoted warnings: {len(warnings)}")

    if issues:
        print("-" * 72)
        for issue in issues:
            print(f"[{issue.severity.upper():7}] {issue.category:16} {issue.detail}")
    else:
        print("\nRuntime audio reference checks passed.")

    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
