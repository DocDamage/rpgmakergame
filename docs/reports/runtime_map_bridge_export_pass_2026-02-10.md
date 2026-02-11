# Runtime Map Bridge Export Pass (2026-02-10)

## Scope

Implemented canonical map export into RPG Maker runtime map files so the validated world graph/story metadata can be traversed in-engine.

## Changes Applied

1. Exporter
- Added `tools/export_canonical_maps_to_rmmz.py`.
- Behavior:
  - reads canonical maps from `assets/data/maps/map_*.json`
  - generates/updates runtime `data/MapXXX.json` stubs (default starting at `Map002`)
  - preserves stable runtime IDs across reruns using note tags
  - writes bridge mapping artifact:
    - `assets/data/system/runtime_map_bridge_generated.json`
  - updates `data/MapInfos.json`
- Runtime map stubs include:
  - map note tags: `chromaGeneratedFromCanonical`, `chromaMapId`, `chromaMapType`, `chromaTileset`
  - a map info event (`EV_MAP_INFO`)
  - connection transfer events (`EV_XFER_*`) from canonical `connections`

2. Bridge validator
- Added `tools/validate_runtime_map_bridge.py`.
- Checks:
  - canonical map coverage in bridge mappings
  - runtime map file + note-tag consistency
  - `MapInfos` coverage
  - transfer event target-map integrity
  - stale generated runtime map detection

3. Audit gate integration
- Updated `tools/run_project_audit_gate.py` to include `runtime_map_bridge` check.

4. Policy update
- Updated `docs/CANONICAL_DATA_POLICY.md` with Runtime Map Bridge workflow and validator commands.

## Export Results

- Canonical maps exported: `98`
- Runtime generated maps: `98` (`Map002` .. `Map099`)
- Existing dev harness map preserved:
  - `Map001` (`DEV_AFFINITY_TEST`)
- MapInfos non-null entries: `99`

## Validation Results

1. Bridge consistency
- `python3 tools/validate_runtime_map_bridge.py`
- Result: `Errors: 0`, `Warnings: 0`

2. Audit gates
- `PATH="$HOME/.local/bin:$PATH" python3 tools/run_project_audit_gate.py --scope core`
  - Passed: `31`, Failed: `0`
- `PATH="$HOME/.local/bin:$PATH" python3 tools/run_project_audit_gate.py --scope all`
  - Passed: `31`, Failed: `0`

3. Export idempotency
- `python3 tools/export_canonical_maps_to_rmmz.py --dry-run`
- Result confirms deterministic mapping and no stale-map drift.

## Notes

- Connection gate tokens (`condition`/`trigger`) are now runtime-checked in generated transfer events:
  - switch gate when token matches a named system switch
  - quest-flag gate fallback via `ChromaEdge.Quests.flag("<TOKEN>")`
- Gate tokens are also preserved in event note tags (`chromaPortalGate`) for debugging and future tooling.
- Follow-up pass:
  - `docs/reports/runtime_map_world_dressing_pass_2026-02-10.md`
  - extends bridge export with metadata-driven world dressing markers and POI transfer synthesis.
- Follow-up pass 2:
  - `docs/reports/runtime_map_tile_geometry_pass_2026-02-10.md`
  - extends bridge export with metadata-driven tile-layer geometry painting.
- Follow-up pass 3:
  - `docs/reports/runtime_map_motif_presets_pass_2026-02-10.md`
  - adds map-type motif presets and motif tag validation for generated runtime maps.
