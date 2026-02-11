# Strict Gate Unification Pass (2026-02-11)

## Scope
- Add a unified strict mode to the main audit gate runner.
- Ensure strict behavior is consistently applied across cohesion/runtime validators.

## Changes
1. `tools/run_project_audit_gate.py`
   - Added `--strict` flag.
   - Strict mode now propagates to:
     - `validate_content_integrity.py --strict-mainline`
     - `audit_story_cohesion.py --strict-act-gating --strict-npc-anchors`
     - `audit_quest_route_pacing.py --strict`
     - `validate_runtime_map_bridge.py --strict`
     - `validate_runtime_transfer_contract.py --strict`
     - `validate_runtime_world_dressing.py --warn-surplus --strict`
     - `validate_world_integrity.py --strict-gates`
2. `tools/validate_runtime_world_dressing.py`
   - Added `--strict` option (promotes warnings to errors).
3. `tools/README.md`
   - Added unified gate usage examples for normal and strict modes.
   - Added strict usage examples for runtime world-dressing validator.

## Validation
- `python3 tools/run_project_audit_gate.py --scope all` => pass
- `python3 tools/run_project_audit_gate.py --scope all --strict` => pass
- `python3 tools/validate_runtime_world_dressing.py --help` confirms new `--strict` option.

## Outcome
- One command now runs a true strict cohesion/runtime gate end-to-end.
- Strict regressions are easier to catch early in regular development cadence.
