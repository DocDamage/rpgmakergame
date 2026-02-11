# Story Cohesion Runtime Scope Pass (2026-02-10)

## Scope

Major cohesion hardening pass focused on:
- runtime quest scope safety (curated-by-default progression)
- story/side-story structural auditability
- world object/dressing anchor coverage for map content

## Changes Applied

1. Runtime quest scope default set to curated packs:
- Updated `js/plugins/ChromaEdge_QuestSystem.js`
  - `includeContentPacks` plugin default changed to `false`
  - runtime fallback parameter default changed to `false`
- Updated `js/plugins.js`
  - `ChromaEdge_QuestSystem.parameters.includeContentPacks` set to `"false"`

2. New story cohesion audit tool:
- Added `tools/audit_story_cohesion.py`
- Checks:
  - quest step `target_location` resolves to canonical maps
  - `target_npc` has an anchor in target map NPC metadata (key/interior/ambient)
  - quests targeting act 2+ locations require explicit gating (`prerequisites` or `prerequisite_flags`)
- Supports runtime scopes:
  - `--scope core` (curated runtime packs)
  - `--scope all` (includes generated normalized packs)

3. Environment dressing audit strengthened:
- Updated `tools/audit_environment_sprite_coverage.py`
- Added `--strict-world-dressing`
  - warns on non-overworld maps missing all world-dressing anchors
  - anchor sources include: `landmarks`, `hazards`, `puzzles`, `points_of_interest`, `events`, `ambient_npcs`, `key_npcs`, `interiors`, `notes`
- Added summary metric: `Maps with world-dressing anchors`

4. Canonical map metadata anchor enrichment:
- Updated `assets/data/maps/map_tower_palace_remnant.json`
  - `TWR_LOBBY_96x64`: added `key_npcs` + `landmarks`
  - `TWR_REWARD_48x32`: added `landmarks`
  - `RV_GATEHOUSE_96x72`: added `key_npcs` + `landmarks`
- Updated `assets/data/maps/map_capital_chain.json`
  - `D_PALACE_128x96`: added `key_npcs` + `landmarks`

5. Policy update:
- Updated `docs/CANONICAL_DATA_POLICY.md`
  - added runtime quest scope guidance (`core` by default, content packs opt-in)
  - added `tools/audit_story_cohesion.py --scope core` to validation gate list

6. Generated-content gate normalization:
- Updated `tools/normalize_content_quests.py`
  - added zone-based default prerequisites for generated mini quests when missing:
    - act-2 zones -> `Q_FOURTH_RELIC`
    - act-3 zones -> `Q_WORLD_BREACHED`
    - post-game zones -> `Q_EPILOGUE`
- Regenerated:
  - `assets/data/quests/quest_content_main_normalized.json`
  - `assets/data/quests/quest_content_mini_normalized.json`

## Validation Results

1. Curated runtime cohesion:
- `python3 tools/audit_story_cohesion.py --scope core`
- Result: `Errors: 0`, `Warnings: 0`
- Coverage: `Maps=98`, `Quests=36`, `Steps=131`

2. Full-content diagnostic (non-curated packs included):
- `python3 tools/audit_story_cohesion.py --scope all`
- Result: `Errors: 0`, `Warnings: 317`
  - `npc_anchors`: `317`
  - `act_gating`: `0`
- Coverage: `Maps=98`, `Quests=251`, `Steps=816`

3. Environment/object dressing coverage:
- `python3 tools/audit_environment_sprite_coverage.py --strict-candidates --strict-world-dressing`
- Result: `Errors: 0`, `Warnings: 0`
- Key metric: `Maps with world-dressing anchors = 98/98`

4. Core integrity gates:
- `python3 tools/validate_content_integrity.py` -> `Errors: 0`, `Warnings: 0`
- `python3 tools/validate_world_integrity.py` -> `Errors: 0`, `Warnings: 0`

5. Syntax/parse checks:
- `python3 -m py_compile tools/audit_story_cohesion.py tools/audit_environment_sprite_coverage.py` passed
- Edited JSON files parse successfully

## Cohesion Impact

- Playable runtime progression now defaults to curated story/side-story quest packs only.
- Generated normalized content packs remain available for staged activation and cleanup.
- Story coherence is now auditable by scope, making risk in optional content explicit.
- Environment object usage is now checked as world-dressing metadata coverage rather than only asset-file presence.

## Follow-Up

- Anchor-sync follow-up completed in `docs/reports/story_cohesion_anchor_sync_pass_2026-02-10.md`.
- Post follow-up status: `tools/audit_story_cohesion.py --scope all` now reports `Errors: 0`, `Warnings: 0`.
