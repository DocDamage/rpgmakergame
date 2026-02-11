#!/usr/bin/env python3
"""
Validate canonical map bridge into RPG Maker runtime map files.
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
ASSET_MAPS_DIR = ROOT / "assets" / "data" / "maps"
BRIDGE_PATH = ROOT / "assets" / "data" / "system" / "runtime_map_bridge_generated.json"

MAP_FILE_RE = re.compile(r"^Map(\d{3})\.json$")
TAG_CANON_ID = re.compile(r"<\s*chromaMapId\s*:\s*([A-Za-z0-9_:-]+)\s*>", re.I)
TAG_GENERATED = re.compile(r"<\s*chromaGeneratedFromCanonical\s*:\s*true\s*>", re.I)
TAG_MAP_TYPE = re.compile(r"<\s*chromaMapType\s*:\s*([A-Za-z0-9_:-]+)\s*>", re.I)
TAG_TRANSFER_EVENTS = re.compile(r"<\s*chromaTransferEvents\s*:\s*(\d+)\s*>", re.I)
TAG_DRESSING_EVENTS = re.compile(r"<\s*chromaDressingEvents\s*:\s*(\d+)\s*>", re.I)
TAG_PAINTED_TILES = re.compile(r"<\s*chromaPaintedTiles\s*:\s*(\d+)\s*>", re.I)
TAG_MOTIF_PROFILE = re.compile(r"<\s*chromaMotifProfile\s*:\s*([A-Za-z0-9_:-]+)\s*>", re.I)


@dataclass(frozen=True)
class Issue:
    severity: str
    category: str
    detail: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate canonical-to-runtime map bridge consistency."
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


def canonical_map_ids() -> set[str]:
    out: set[str] = set()
    for path in sorted(ASSET_MAPS_DIR.glob("map_*.json")):
        data = load_json(path)
        entries = data.get("maps") if isinstance(data.get("maps"), list) else [data]
        for rec in entries:
            if not isinstance(rec, dict):
                continue
            map_id = rec.get("id")
            if isinstance(map_id, str) and map_id:
                out.add(map_id)
    return out


def runtime_maps() -> dict[int, dict[str, Any]]:
    out: dict[int, dict[str, Any]] = {}
    for path in sorted(DATA_DIR.glob("Map*.json")):
        m = MAP_FILE_RE.match(path.name)
        if not m:
            continue
        rid = int(m.group(1))
        data = load_json(path)
        if isinstance(data, dict):
            out[rid] = data
    return out


def generated_runtime_index(maps: dict[int, dict[str, Any]]) -> dict[str, int]:
    out: dict[str, int] = {}
    for rid, rec in maps.items():
        note = rec.get("note")
        if not isinstance(note, str):
            continue
        if not TAG_GENERATED.search(note):
            continue
        m = TAG_CANON_ID.search(note)
        if not m:
            continue
        can_id = m.group(1).strip()
        if can_id and can_id not in out:
            out[can_id] = rid
    return out


def geometry_nonzero_tiles(rec: dict[str, Any]) -> int | None:
    width = rec.get("width")
    height = rec.get("height")
    data = rec.get("data")
    if not isinstance(width, int) or not isinstance(height, int):
        return None
    if width <= 0 or height <= 0:
        return None
    if not isinstance(data, list):
        return None
    cells = width * height
    if len(data) < cells * 4:
        return None
    count = 0
    for z in (1, 2, 3):
        base = z * cells
        for idx in range(base, base + cells):
            value = data[idx]
            if isinstance(value, int) and value != 0:
                count += 1
    return count


def transfer_targets(rec: dict[str, Any]) -> list[int]:
    out: list[int] = []
    events = rec.get("events")
    if not isinstance(events, list):
        return out
    for ev in events:
        if not isinstance(ev, dict):
            continue
        pages = ev.get("pages")
        if not isinstance(pages, list):
            continue
        found_target: int | None = None
        for page in pages:
            if not isinstance(page, dict):
                continue
            lst = page.get("list")
            if not isinstance(lst, list):
                continue
            for cmd in lst:
                if not isinstance(cmd, dict):
                    continue
                if cmd.get("code") != 201:
                    continue
                params = cmd.get("parameters")
                if not isinstance(params, list) or len(params) < 2:
                    continue
                target = params[1]
                if isinstance(target, int):
                    found_target = target
                    break
            if found_target is not None:
                break
        if found_target is not None:
            out.append(found_target)
    return out


def run_validation(args: argparse.Namespace) -> list[Issue]:
    issues: list[Issue] = []

    if not BRIDGE_PATH.exists():
        issues.append(Issue("error", "inputs", f"Missing bridge artifact: {BRIDGE_PATH}"))
        return issues

    bridge = load_json(BRIDGE_PATH)
    if not isinstance(bridge, dict):
        issues.append(Issue("error", "schema", f"{BRIDGE_PATH} must be an object"))
        return issues

    mappings = bridge.get("mappings")
    if not isinstance(mappings, list):
        issues.append(Issue("error", "schema", f"{BRIDGE_PATH} missing list `mappings`"))
        return issues

    canonical_ids = canonical_map_ids()
    maps = runtime_maps()
    generated_idx = generated_runtime_index(maps)
    map_infos = load_json(DATA_DIR / "MapInfos.json")
    if not isinstance(map_infos, list):
        issues.append(Issue("error", "schema", "data/MapInfos.json must be a list"))
        return issues

    bridge_can_to_runtime: dict[str, int] = {}
    for rec in mappings:
        if not isinstance(rec, dict):
            issues.append(Issue("error", "schema", "bridge mapping entry must be an object"))
            continue
        can_id = rec.get("canonical_map_id")
        rid = rec.get("runtime_map_id")
        if not isinstance(can_id, str) or not can_id:
            issues.append(Issue("error", "schema", "bridge mapping missing canonical_map_id"))
            continue
        if not isinstance(rid, int) or rid <= 0:
            issues.append(Issue("error", "schema", f"{can_id}: invalid runtime_map_id"))
            continue
        if can_id in bridge_can_to_runtime and bridge_can_to_runtime[can_id] != rid:
            issues.append(Issue("error", "bridge_dupe", f"{can_id} mapped to multiple runtime IDs"))
            continue
        bridge_can_to_runtime[can_id] = rid

    runtime_edges: dict[int, set[int]] = {}
    generated_runtime_ids = set(bridge_can_to_runtime.values())
    overworld_runtime_ids: set[int] = set()

    for can_id in sorted(canonical_ids):
        if can_id not in bridge_can_to_runtime:
            issues.append(Issue("error", "bridge_missing", f"{can_id} missing from bridge mappings"))
            continue
        rid = bridge_can_to_runtime[can_id]
        rec = maps.get(rid)
        if rec is None:
            issues.append(Issue("error", "runtime_map_missing", f"{can_id} -> Map{rid:03d} missing"))
            continue
        note = rec.get("note", "")
        if not isinstance(note, str) or not TAG_GENERATED.search(note):
            issues.append(
                Issue("error", "runtime_map_note", f"Map{rid:03d} missing generated bridge note tag")
            )
        map_type_match = TAG_MAP_TYPE.search(note or "")
        if map_type_match and map_type_match.group(1).strip().lower() == "overworld":
            overworld_runtime_ids.add(rid)
        m = TAG_CANON_ID.search(note or "")
        if not m or m.group(1).strip() != can_id:
            issues.append(
                Issue("error", "runtime_map_note", f"Map{rid:03d} chromaMapId tag mismatch for {can_id}")
            )
        if rid >= len(map_infos) or not isinstance(map_infos[rid], dict):
            issues.append(
                Issue("error", "map_infos", f"MapInfos missing entry for Map{rid:03d} ({can_id})")
            )

        transfer_match = TAG_TRANSFER_EVENTS.search(note or "")
        dressing_match = TAG_DRESSING_EVENTS.search(note or "")
        painted_match = TAG_PAINTED_TILES.search(note or "")
        motif_match = TAG_MOTIF_PROFILE.search(note or "")
        if transfer_match is None:
            sev = "error" if args.strict else "warning"
            issues.append(
                Issue(sev, "runtime_map_note", f"Map{rid:03d} missing chromaTransferEvents tag")
            )
        if dressing_match is None:
            sev = "error" if args.strict else "warning"
            issues.append(
                Issue(sev, "runtime_map_note", f"Map{rid:03d} missing chromaDressingEvents tag")
            )
        if painted_match is None:
            sev = "error" if args.strict else "warning"
            issues.append(
                Issue(sev, "runtime_map_note", f"Map{rid:03d} missing chromaPaintedTiles tag")
            )
        if motif_match is None:
            sev = "error" if args.strict else "warning"
            issues.append(
                Issue(sev, "runtime_map_note", f"Map{rid:03d} missing chromaMotifProfile tag")
            )

        transfer_count = int(transfer_match.group(1)) if transfer_match else 0
        dressing_count = int(dressing_match.group(1)) if dressing_match else 0
        painted_count = int(painted_match.group(1)) if painted_match else 0
        transfers = transfer_targets(rec)
        if transfer_match is not None and transfer_count != len(transfers):
            sev = "error" if args.strict else "warning"
            issues.append(
                Issue(
                    sev,
                    "transfer_count",
                    f"Map{rid:03d} chromaTransferEvents={transfer_count} but transfer events={len(transfers)}",
                )
            )
        runtime_edges[rid] = {t for t in transfers if t in generated_runtime_ids}
        if dressing_count > 0 and painted_count <= 0:
            sev = "error" if args.strict else "warning"
            issues.append(
                Issue(
                    sev,
                    "painted_tiles",
                    f"Map{rid:03d} has dressing events ({dressing_count}) but chromaPaintedTiles is {painted_count}",
                )
            )

        nonzero_geo = geometry_nonzero_tiles(rec)
        if nonzero_geo is None:
            sev = "error" if args.strict else "warning"
            issues.append(
                Issue(sev, "runtime_map_schema", f"Map{rid:03d} has invalid map data layout")
            )
        elif painted_count != nonzero_geo:
            sev = "error" if args.strict else "warning"
            issues.append(
                Issue(
                    sev,
                    "painted_tiles",
                    f"Map{rid:03d} chromaPaintedTiles={painted_count} but non-zero layer tiles={nonzero_geo}",
                )
            )

    for can_id, rid in sorted(generated_idx.items()):
        if can_id not in canonical_ids:
            sev = "error" if args.strict else "warning"
            issues.append(
                Issue(sev, "stale_runtime_map", f"Map{rid:03d} references stale canonical map id {can_id}")
            )
        elif bridge_can_to_runtime.get(can_id) != rid:
            issues.append(
                Issue(
                    "error",
                    "bridge_runtime_mismatch",
                    f"{can_id} bridge points to Map{bridge_can_to_runtime.get(can_id)}, runtime note points to Map{rid:03d}",
                )
            )

    # Transfer event target existence checks for all runtime maps.
    for rid, rec in sorted(maps.items()):
        events = rec.get("events")
        if not isinstance(events, list):
            continue
        for ev in events:
            if not isinstance(ev, dict):
                continue
            pages = ev.get("pages")
            if not isinstance(pages, list):
                continue
            for page in pages:
                if not isinstance(page, dict):
                    continue
                lst = page.get("list")
                if not isinstance(lst, list):
                    continue
                for cmd in lst:
                    if not isinstance(cmd, dict):
                        continue
                    if cmd.get("code") != 201:
                        continue
                    params = cmd.get("parameters")
                    if not isinstance(params, list) or len(params) < 4:
                        issues.append(
                            Issue("error", "transfer_schema", f"Map{rid:03d} event{ev.get('id')} has invalid transfer params")
                        )
                        continue
                    target = params[1]
                    if not isinstance(target, int) or target not in maps:
                        issues.append(
                            Issue(
                                "error",
                                "transfer_target",
                                f"Map{rid:03d} event{ev.get('id')} transfers to missing map id {target}",
                            )
                        )

    # Runtime traversal cohesion checks for generated maps.
    for rid in sorted(generated_runtime_ids):
        runtime_edges.setdefault(rid, set())

    inbound: dict[int, int] = {rid: 0 for rid in generated_runtime_ids}
    for src, targets in runtime_edges.items():
        if src not in generated_runtime_ids:
            continue
        for dst in targets:
            if dst in inbound:
                inbound[dst] += 1

    for rid in sorted(generated_runtime_ids):
        if len(runtime_edges.get(rid, set())) == 0:
            sev = "error" if args.strict else "warning"
            issues.append(
                Issue(
                    sev,
                    "runtime_transfer_graph",
                    f"Map{rid:03d} has no outbound transfers to generated runtime maps",
                )
            )
        if inbound.get(rid, 0) == 0:
            sev = "error" if args.strict else "warning"
            issues.append(
                Issue(
                    sev,
                    "runtime_transfer_graph",
                    f"Map{rid:03d} has no inbound transfers from generated runtime maps",
                )
            )

    # Undirected connectivity over generated maps.
    undirected: dict[int, set[int]] = {rid: set() for rid in generated_runtime_ids}
    for src, targets in runtime_edges.items():
        if src not in generated_runtime_ids:
            continue
        for dst in targets:
            if dst not in generated_runtime_ids:
                continue
            undirected[src].add(dst)
            undirected[dst].add(src)

    seen: set[int] = set()
    components: list[list[int]] = []
    for rid in sorted(generated_runtime_ids):
        if rid in seen:
            continue
        stack = [rid]
        seen.add(rid)
        comp: list[int] = []
        while stack:
            cur = stack.pop()
            comp.append(cur)
            for nxt in undirected.get(cur, set()):
                if nxt in seen:
                    continue
                seen.add(nxt)
                stack.append(nxt)
        components.append(sorted(comp))

    if len(components) > 1:
        sizes = ",".join(str(len(c)) for c in sorted(components, key=len, reverse=True))
        sev = "error" if args.strict else "warning"
        issues.append(
            Issue(
                sev,
                "runtime_transfer_graph",
                f"Generated runtime map graph is disconnected: {len(components)} components (sizes={sizes})",
            )
        )

    # Directed reachability from overworld roots.
    if overworld_runtime_ids:
        reachable: set[int] = set()
        stack = sorted(overworld_runtime_ids)
        reachable.update(stack)
        while stack:
            cur = stack.pop()
            for nxt in runtime_edges.get(cur, set()):
                if nxt in reachable:
                    continue
                reachable.add(nxt)
                stack.append(nxt)
        unreachable = sorted(generated_runtime_ids - reachable)
        if unreachable:
            sev = "error" if args.strict else "warning"
            sample = ", ".join(f"Map{x:03d}" for x in unreachable[:10])
            issues.append(
                Issue(
                    sev,
                    "runtime_transfer_graph",
                    f"{len(unreachable)} generated maps unreachable from overworld roots (sample: {sample})",
                )
            )
    else:
        sev = "error" if args.strict else "warning"
        issues.append(
            Issue(
                sev,
                "runtime_transfer_graph",
                "No generated overworld runtime map found via <chromaMapType:overworld>",
            )
        )

    if args.strict:
        issues = [
            Issue("error", i.category, i.detail) if i.severity == "warning" else i for i in issues
        ]
    return issues


def main() -> int:
    args = parse_args()
    issues = run_validation(args)
    errors = [x for x in issues if x.severity == "error"]
    warnings = [x for x in issues if x.severity == "warning"]

    print("=" * 64)
    print("RUNTIME MAP BRIDGE VALIDATION")
    print("=" * 64)
    print(f"Errors: {len(errors)}")
    print(f"Warnings: {len(warnings)}")
    if issues:
        print("-" * 64)
        for issue in issues:
            print(f"[{issue.severity.upper():7}] {issue.category:22} {issue.detail}")
    else:
        print("\nRuntime map bridge checks passed.")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
