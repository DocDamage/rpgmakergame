# Runtime World Dressing Sync Pass (2026-02-11)

## Scope
- Ensure canonical world/environment dressing metadata is actually represented in runtime maps.
- Close propagation drift between `assets/data/maps/*.json` and `data/Map###.json`.
- Add a hard validation gate so this does not regress.

## Key Finding
- Before re-export, canonical overworld (`OW_ORION_320x180`) contained rich anchors
  (`landmarks`, `hazards`, `puzzles`, `events`, `notes`) but runtime `Map049` only
  had POI/region/key-NPC world-dressing tags.
- This meant world object markers were defined canonically but not fully present in-game.

## Fixes Applied
1. Regenerated runtime maps from canonical source:
   - `python3 tools/export_canonical_maps_to_rmmz.py`
   - Updated:
     - `data/Map002.json` .. `data/Map099.json`
     - `data/MapInfos.json`
     - `assets/data/system/runtime_map_bridge_generated.json`
2. Added new validator:
   - `tools/validate_runtime_world_dressing.py`
   - Verifies per-map canonical anchor counts vs runtime `<chromaWorldDress:...>` tags.
3. Integrated validator into main gate:
   - `tools/run_project_audit_gate.py` now includes `runtime_world_dressing`.
4. Documented usage:
   - `tools/README.md`

## Validation
- `python3 tools/validate_runtime_world_dressing.py`
  - Canonical maps: `98`
  - Runtime maps validated: `98`
  - Expected world-dressing tags: `354`
  - Actual world-dressing tags: `354`
  - Errors: `0`, Warnings: `0`
- `python3 tools/run_project_audit_gate.py --scope all`
  - All checks passed, including new `runtime_world_dressing`.

## Outcome
- Overworld/environment object anchors are now coherently propagated into runtime maps.
- Future drift is blocked by an explicit validation gate.
