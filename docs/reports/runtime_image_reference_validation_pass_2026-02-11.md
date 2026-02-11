# Runtime Image Reference Validation Pass (2026-02-11)

## Scope
- Added a dedicated validator for non-audio runtime visual references.
- Integrated image/effect/movie reference checks into the strict project audit gate.

## New Tool
- `tools/validate_runtime_image_references.py`

Coverage:
- `data/System.json`
- `data/Actors.json`
- `data/Enemies.json`
- `data/Tilesets.json` (map-used IDs by default)
- `data/Animations.json` (`effectName` -> `effects/*.efkefc`)
- `data/CommonEvents.json`
- `data/Troops.json`
- `data/Map###.json`

Event command parsing includes:
- `101` Show Text face sheet
- `231` Show Picture
- `261` Play Movie
- `283` Change Battle Back
- `284` Change Parallax
- `322` Change Actor Images
- `323` Change Vehicle Image
- `205` Set Movement Route (image changes)
- `505` Movement Route continuation (image changes)

## Gate Integration
- Updated `tools/run_project_audit_gate.py` with step:
  - `runtime_image_references`

Strict mode now runs:
```bash
python3 tools/validate_runtime_image_references.py --strict --strict-effects
```

## Validation Results
```bash
python3 tools/validate_runtime_image_references.py
python3 tools/validate_runtime_image_references.py --strict --strict-effects
python3 tools/run_project_audit_gate.py --scope all --strict
NW_RUNTIME_SECONDS=12 tools/run_nw_playtest.sh
```

All commands passed.

Image validator summary:
- References scanned: `188`
- Unique references: `174`
- Missing errors: `0`
- Warnings: `0`

By kind:
- `effects=120`
- `tilesets=17`
- `characters=16`
- `faces=13`
- `sv_actors=13`
- `enemy_battler=6`
- `battlebacks1=1`
- `battlebacks2=1`
- `titles1=1`

## Notes
- This pass intentionally excludes audio authoring and does not alter your in-progress
  audio composition workflow.
