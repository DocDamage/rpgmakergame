# Runtime Image Placeholder Provision Pass (2026-02-11)

## Scope
- Added a non-destructive runtime image foundation tool to provision missing
  RPG Maker MZ image dependencies with deterministic placeholder PNGs.
- Executed the tool for current project references.

## New Tool
- `tools/provision_runtime_image_placeholders.py`

Behavior:
- Creates files only when missing (unless `--overwrite` is provided).
- Discovers required targets from:
  - hardcoded MZ system sheets (`Window`, `IconSet`, `Balloon`, etc.)
  - `data/System.json` title/battleback/vehicle references
  - map-used tileset names from `data/Map###.json` + `data/Tilesets.json`
  - map battleback/parallax references

## Run Log
```bash
python3 tools/provision_runtime_image_placeholders.py --dry-run
python3 tools/provision_runtime_image_placeholders.py
```

Results:
- Targets discovered: `33`
- Created: `33`
- Overwritten: `0`
- Skipped existing: `0`

## Created Runtime Foundations
- `img/system/*` core files (`Window`, `IconSet`, `Balloon`, `States`, `Weapons1-3`, etc.)
- `img/tilesets/*` for currently used runtime map tilesets
- `img/titles1/Ruins.png`
- `img/battlebacks1/GrassMaze.png`
- `img/battlebacks2/GrassMaze.png`
- `img/characters/Vehicle.png`

## Validation
```bash
NW_RUNTIME_SECONDS=20 tools/run_nw_playtest.sh
python3 tools/run_project_audit_gate.py --scope all --strict
```

Both commands passed after provisioning.

## Notes
- These placeholders are runtime safety scaffolding and should be replaced by
  final art/audio-ready assets as production content is finalized.
