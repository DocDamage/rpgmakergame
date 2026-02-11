# Quest Route Pacing Pass (2026-02-11)

## Scope
- Validate quest travel flow against canonical map connectivity.
- Ensure step-to-step quest routes are reachable and not directionality-broken.

## Tooling Added
- New audit:
  - `tools/audit_quest_route_pacing.py`
- Audit gate integration:
  - `tools/run_project_audit_gate.py` includes `quest_route_pacing`.
- Docs update:
  - `tools/README.md`

## Validation Results
- `python3 tools/audit_quest_route_pacing.py --scope core`
  - Quests scanned: `36`
  - Quests with locations: `36`
  - Transitions checked: `59`
  - Errors: `0`
  - Warnings: `0`
- `python3 tools/audit_quest_route_pacing.py --scope all`
  - Quests scanned: `251`
  - Quests with locations: `251`
  - Transitions checked: `113`
  - Errors: `0`
  - Warnings: `0`
- `python3 tools/run_project_audit_gate.py --scope all`
  - Full pass, including `quest_route_pacing`.

## Outcome
- Main + side quest travel progression is route-cohesive under canonical graph rules.
- Route pacing regressions now fail/flag inside the standard audit pipeline.
