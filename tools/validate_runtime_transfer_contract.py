#!/usr/bin/env python3
"""
Validate runtime transfer event contracts against canonical map metadata.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
MAPS_DIR = ROOT / "assets" / "data" / "maps"
BRIDGE_PATH = ROOT / "assets" / "data" / "system" / "runtime_map_bridge_generated.json"
RUNTIME_DIR = ROOT / "data"

TAG_GENERATED = re.compile(r"<\s*chromaGeneratedFromCanonical\s*:\s*true\s*>", re.I)
TAG_PORTAL_TARGET = re.compile(r"<\s*chromaPortalTarget\s*:\s*([A-Za-z0-9_:-]+)\s*>", re.I)
TAG_PORTAL_GATE = re.compile(r"<\s*chromaPortalGate\s*:\s*([^>\n]+)\s*>", re.I)
MAP_FILE_RE = re.compile(r"^Map(\d{3})\.json$")


@dataclass(frozen=True)
class Issue:
    severity: str
    category: str
    detail: str


@dataclass(frozen=True)
class TransferEvent:
    event_id: int
    name: str
    target_runtime_id: int | None
    target_canonical_id: str | None
    note_target_canonical_id: str | None
    gate_token: str
    has_conditional: bool


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate runtime transfer event contracts against canonical map expectations."
    )
    parser.add_argument(
        "--maps-dir",
        default=str(MAPS_DIR),
        help="Canonical maps directory (default: assets/data/maps).",
    )
    parser.add_argument(
        "--bridge",
        default=str(BRIDGE_PATH),
        help="Runtime bridge JSON path (default: assets/data/system/runtime_map_bridge_generated.json).",
    )
    parser.add_argument(
        "--runtime-dir",
        default=str(RUNTIME_DIR),
        help="Runtime data directory containing Map###.json files (default: data).",
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


def canonical_maps(maps_dir: Path) -> dict[str, dict[str, Any]]:
    out: dict[str, dict[str, Any]] = {}
    for path in sorted(maps_dir.glob("map_*.json")):
        data = load_json(path)
        entries = data.get("maps") if isinstance(data.get("maps"), list) else [data]
        for rec in entries:
            if not isinstance(rec, dict):
                continue
            map_id = rec.get("id")
            if isinstance(map_id, str) and map_id:
                out[map_id] = rec
    return out


def normalize_gate(value: Any) -> str:
    if isinstance(value, str):
        return value.strip().upper()
    return ""


def expected_transfers(rec: dict[str, Any], canonical_ids: set[str]) -> Counter[tuple[str, str]]:
    out: Counter[tuple[str, str]] = Counter()

    connections = rec.get("connections")
    if isinstance(connections, list):
        for conn in connections:
            if not isinstance(conn, dict):
                continue
            target = conn.get("target")
            if not isinstance(target, str) or target not in canonical_ids:
                continue
            gate = normalize_gate(conn.get("condition") or conn.get("trigger"))
            out[(target, gate)] += 1

    pois = rec.get("points_of_interest")
    if isinstance(pois, list):
        for poi in pois:
            if not isinstance(poi, dict):
                continue
            target = poi.get("target")
            if not isinstance(target, str) or target not in canonical_ids:
                continue
            gate = normalize_gate(poi.get("condition"))
            out[(target, gate)] += 1

    return out


def extract_transfer_events(
    runtime_map: dict[str, Any],
    runtime_to_canonical: dict[int, str],
) -> list[TransferEvent]:
    out: list[TransferEvent] = []
    events = runtime_map.get("events")
    if not isinstance(events, list):
        return out

    for ev in events:
        if not isinstance(ev, dict):
            continue
        event_id = ev.get("id") if isinstance(ev.get("id"), int) else 0
        name = ev.get("name") if isinstance(ev.get("name"), str) else ""
        note = ev.get("note") if isinstance(ev.get("note"), str) else ""
        pages = ev.get("pages")
        if not isinstance(pages, list):
            continue

        has_transfer = False
        has_conditional = False
        target_runtime: int | None = None
        for page in pages:
            if not isinstance(page, dict):
                continue
            commands = page.get("list")
            if not isinstance(commands, list):
                continue
            for cmd in commands:
                if not isinstance(cmd, dict):
                    continue
                code = cmd.get("code")
                if code == 111:
                    has_conditional = True
                if code != 201:
                    continue
                params = cmd.get("parameters")
                if not isinstance(params, list) or len(params) < 2:
                    continue
                runtime_target = params[1]
                if isinstance(runtime_target, int):
                    has_transfer = True
                    target_runtime = runtime_target
                    break
            if has_transfer:
                break

        if not has_transfer:
            continue

        note_target_match = TAG_PORTAL_TARGET.search(note)
        note_gate_match = TAG_PORTAL_GATE.search(note)
        note_target = note_target_match.group(1).strip() if note_target_match else None
        gate_token = normalize_gate(note_gate_match.group(1)) if note_gate_match else ""
        target_canonical = runtime_to_canonical.get(target_runtime) if target_runtime is not None else None

        out.append(
            TransferEvent(
                event_id=event_id,
                name=name,
                target_runtime_id=target_runtime,
                target_canonical_id=target_canonical,
                note_target_canonical_id=note_target,
                gate_token=gate_token,
                has_conditional=has_conditional,
            )
        )
    return out


def run_validation(args: argparse.Namespace) -> tuple[list[Issue], dict[str, int]]:
    issues: list[Issue] = []
    stats = {
        "canonical_maps": 0,
        "bridged_maps": 0,
        "runtime_maps_validated": 0,
        "expected_transfers": 0,
        "actual_transfers": 0,
    }

    maps_dir = Path(args.maps_dir)
    bridge_path = Path(args.bridge)
    runtime_dir = Path(args.runtime_dir)
    if not maps_dir.exists():
        issues.append(Issue("error", "inputs", f"Missing maps dir: {maps_dir}"))
        return issues, stats
    if not bridge_path.exists():
        issues.append(Issue("error", "inputs", f"Missing bridge file: {bridge_path}"))
        return issues, stats
    if not runtime_dir.exists():
        issues.append(Issue("error", "inputs", f"Missing runtime dir: {runtime_dir}"))
        return issues, stats

    canonical = canonical_maps(maps_dir)
    canonical_ids = set(canonical.keys())
    stats["canonical_maps"] = len(canonical_ids)

    bridge = load_json(bridge_path)
    mappings = bridge.get("mappings") if isinstance(bridge, dict) else None
    if not isinstance(mappings, list):
        issues.append(Issue("error", "schema", f"{bridge_path} missing list `mappings`"))
        return issues, stats

    canonical_to_runtime: dict[str, int] = {}
    runtime_to_canonical: dict[int, str] = {}
    for rec in mappings:
        if not isinstance(rec, dict):
            issues.append(Issue("error", "schema", "bridge mapping entry must be an object"))
            continue
        can_id = rec.get("canonical_map_id")
        runtime_id = rec.get("runtime_map_id")
        if not isinstance(can_id, str) or not can_id:
            issues.append(Issue("error", "schema", "bridge mapping missing canonical_map_id"))
            continue
        if not isinstance(runtime_id, int) or runtime_id <= 0:
            issues.append(Issue("error", "schema", f"{can_id}: invalid runtime_map_id"))
            continue
        if can_id in canonical_to_runtime and canonical_to_runtime[can_id] != runtime_id:
            issues.append(Issue("error", "schema", f"{can_id}: duplicate runtime mapping"))
            continue
        canonical_to_runtime[can_id] = runtime_id
        runtime_to_canonical[runtime_id] = can_id

    for can_id in sorted(canonical_ids):
        runtime_id = canonical_to_runtime.get(can_id)
        if runtime_id is None:
            issues.append(Issue("error", "bridge_missing", f"{can_id} missing from runtime bridge"))
            continue
        stats["bridged_maps"] += 1

        map_path = runtime_dir / f"Map{runtime_id:03d}.json"
        if not map_path.exists():
            issues.append(Issue("error", "runtime_missing", f"{can_id} -> {map_path.name} missing"))
            continue

        runtime_map = load_json(map_path)
        note = runtime_map.get("note")
        if not isinstance(note, str) or not TAG_GENERATED.search(note):
            issues.append(
                Issue(
                    "error",
                    "runtime_map_note",
                    f"{can_id} ({map_path.name}) missing generated-runtime note tag",
                )
            )

        expected = expected_transfers(canonical[can_id], canonical_ids)
        events = extract_transfer_events(runtime_map, runtime_to_canonical)
        actual: Counter[tuple[str, str]] = Counter()

        stats["runtime_maps_validated"] += 1
        stats["expected_transfers"] += sum(expected.values())
        stats["actual_transfers"] += len(events)

        for ev in events:
            prefix = f"{can_id} ({map_path.name}) event{ev.event_id}"
            if not ev.name.startswith("EV_XFER_"):
                issues.append(
                    Issue(
                        "warning",
                        "runtime_transfer_event",
                        f"{prefix} has non-standard transfer event name '{ev.name}'",
                    )
                )

            if ev.note_target_canonical_id is None:
                issues.append(
                    Issue(
                        "error",
                        "runtime_transfer_note",
                        f"{prefix} missing <chromaPortalTarget:...> note tag",
                    )
                )
            elif ev.note_target_canonical_id not in canonical_ids:
                issues.append(
                    Issue(
                        "error",
                        "runtime_transfer_note",
                        f"{prefix} points to unknown canonical target '{ev.note_target_canonical_id}'",
                    )
                )

            if ev.target_runtime_id is None:
                issues.append(
                    Issue(
                        "error",
                        "runtime_transfer_event",
                        f"{prefix} has no valid transfer target map id in command list",
                    )
                )
            elif ev.target_canonical_id is None:
                issues.append(
                    Issue(
                        "error",
                        "runtime_transfer_event",
                        f"{prefix} transfers to unmapped runtime map id {ev.target_runtime_id}",
                    )
                )

            if (
                ev.note_target_canonical_id is not None
                and ev.target_canonical_id is not None
                and ev.note_target_canonical_id != ev.target_canonical_id
            ):
                issues.append(
                    Issue(
                        "error",
                        "runtime_transfer_mismatch",
                        f"{prefix} note target '{ev.note_target_canonical_id}' != transfer target '{ev.target_canonical_id}'",
                    )
                )

            if ev.gate_token and not ev.has_conditional:
                issues.append(
                    Issue(
                        "error",
                        "runtime_transfer_gate",
                        f"{prefix} has gate token '{ev.gate_token}' but no conditional branch (code 111)",
                    )
                )
            if not ev.gate_token and ev.has_conditional:
                issues.append(
                    Issue(
                        "warning",
                        "runtime_transfer_gate",
                        f"{prefix} has conditional branch but no <chromaPortalGate:...> tag",
                    )
                )

            key_target = ev.note_target_canonical_id or ev.target_canonical_id
            if key_target is not None:
                actual[(key_target, ev.gate_token)] += 1

        missing = expected - actual
        extra = actual - expected
        for (target, gate), count in sorted(missing.items()):
            issues.append(
                Issue(
                    "error",
                    "runtime_transfer_missing",
                    f"{can_id} missing {count} transfer(s) to {target} gate='{gate or 'NONE'}'",
                )
            )
        for (target, gate), count in sorted(extra.items()):
            issues.append(
                Issue(
                    "error",
                    "runtime_transfer_extra",
                    f"{can_id} has unexpected {count} transfer(s) to {target} gate='{gate or 'NONE'}'",
                )
            )

    if args.strict:
        issues = [
            Issue("error", issue.category, issue.detail)
            if issue.severity == "warning"
            else issue
            for issue in issues
        ]
    return issues, stats


def main() -> int:
    args = parse_args()
    issues, stats = run_validation(args)
    errors = [x for x in issues if x.severity == "error"]
    warnings = [x for x in issues if x.severity == "warning"]

    print("=" * 68)
    print("RUNTIME TRANSFER CONTRACT VALIDATION")
    print("=" * 68)
    print(f"Canonical maps: {stats['canonical_maps']}")
    print(f"Bridge mappings: {stats['bridged_maps']}")
    print(f"Runtime maps validated: {stats['runtime_maps_validated']}")
    print(f"Expected transfers: {stats['expected_transfers']}")
    print(f"Actual transfer events: {stats['actual_transfers']}")
    print("-" * 68)
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")
    if issues:
        print("-" * 68)
        for issue in issues:
            print(f"[{issue.severity.upper():7}] {issue.category:26} {issue.detail}")
    else:
        print("\nRuntime transfer contract checks passed.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
