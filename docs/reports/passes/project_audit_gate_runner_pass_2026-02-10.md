# Project Audit Gate Runner Pass (2026-02-10)

## Scope

Added a single-command audit runner so cohesion, integrity, environment coverage, and JavaScript syntax checks can be executed consistently.

## Changes Applied

1. New gate runner script
- Added `tools/run_project_audit_gate.py`
- Runs:
  - `tools/validate_content_integrity.py --scope <scope> --strict-map-npc-anchors`
  - `tools/audit_story_cohesion.py --scope <scope>`
  - `tools/validate_world_integrity.py`
  - `tools/audit_environment_sprite_coverage.py --strict-candidates --strict-world-dressing`
  - `node --check` on all `js/**/*.js` (unless `--skip-js-syntax`)
- Supports:
  - `--scope core|all`
  - `--skip-js-syntax`

2. Policy update
- Updated `docs/CANONICAL_DATA_POLICY.md` with one-command runner usage:
  - `PATH="$HOME/.local/bin:$PATH" python3 tools/run_project_audit_gate.py --scope core`

## Validation Results

- Executed:
  - `PATH="$HOME/.local/bin:$PATH" python3 tools/run_project_audit_gate.py --scope core`
- Result:
  - Passed: `30`
  - Failed: `0`
- Included successful parser checks for all JS runtime/plugin files and minified libs.

## Cohesion Impact

- Audit execution is now deterministic and fast to re-run.
- Prevents drift between separate validators by centralizing required gates.
- Reduces regression risk for story/side-story coherence and environment-sprite world usage checks.
