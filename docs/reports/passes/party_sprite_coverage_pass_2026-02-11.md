# Party Sprite Coverage Pass (2026-02-11)

## Scope
- Added a hard validator for protagonist runtime sprite completeness and actor binding consistency.
- Integrated the validator into the project audit gate.

## New Validator
- `tools/validate_party_sprite_coverage.py`

Checks:
- Actor IDs `1-13` map to expected runtime sheets:
  - `characterName`: `$ce_<slug>`
  - `characterIndex`: `0`
  - `battlerName`: `ce_sv_<slug>`
- Runtime + source overworld sheets exist and are `144x256` (3x4 frames).
- Runtime + source SV sheets exist and are `864x576` (9x6 blocks / 18 motions).
- No blank frame cells in overworld or SV motion frames.
- Actor face image references resolve.

## Gate Integration
- Updated `tools/run_project_audit_gate.py` with new step:
  - `party_sprite_coverage`

## Validation Results
```bash
python3 tools/validate_party_sprite_coverage.py
python3 tools/validate_party_sprite_coverage.py --strict
python3 tools/run_project_audit_gate.py --scope all
python3 tools/run_project_audit_gate.py --scope all --strict
```

All commands passed.

- Actors checked: `13`
- Overworld sheets checked: `26` (runtime + source)
- SV sheets checked: `26` (runtime + source)
- Errors: `0`
- Warnings: `0`

## Conclusion
Main-character sprite runtime coverage is complete for the current 13-protagonist party set,
with validated directional overworld sheets and side-view actor sheets wired into `data/Actors.json`.
