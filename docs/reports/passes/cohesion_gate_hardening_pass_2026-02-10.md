# Cohesion Gate Hardening Pass (2026-02-10)

## Scope

Hardening pass to prevent future quest/map cohesion regressions from entering canonical data.

## Changes Applied

1. `validate_content_integrity` enhancements
- Updated `tools/validate_content_integrity.py`:
  - added quest scope option:
    - `--scope all|core` (default `all`)
  - added map-NPC anchor verification:
    - checks each quest step `target_npc` is anchored in target map metadata (`key_npcs`, interior NPCs, ambient NPCs)
  - added strict anchor mode:
    - `--strict-map-npc-anchors` (promotes anchor drift to errors)

2. Policy update
- Updated `docs/CANONICAL_DATA_POLICY.md`:
  - default integrity gate now uses:
    - `python3 tools/validate_content_integrity.py --scope core --strict-map-npc-anchors`

3. JavaScript syntax validation capability
- Local user-space Node runtime is available and used for parser-level checks.
- Verified syntax checks with `node --check` for core runtime plugins and `js/plugins.js`.

## Validation Results

1. Content integrity
- `python3 tools/validate_content_integrity.py` -> `Errors: 0`, `Warnings: 0`
- `python3 tools/validate_content_integrity.py --scope core --strict-map-npc-anchors` -> `Errors: 0`, `Warnings: 0`
- `python3 tools/validate_content_integrity.py --scope all --strict-map-npc-anchors` -> `Errors: 0`, `Warnings: 0`

2. Story/map/environment gates
- `python3 tools/audit_story_cohesion.py --scope core` -> `Errors: 0`, `Warnings: 0`
- `python3 tools/audit_story_cohesion.py --scope all` -> `Errors: 0`, `Warnings: 0`
- `python3 tools/validate_world_integrity.py` -> `Errors: 0`, `Warnings: 0`
- `python3 tools/audit_environment_sprite_coverage.py --strict-candidates --strict-world-dressing` -> `Errors: 0`, `Warnings: 0`

3. JS syntax checks
- `node --check js/plugins/ChromaEdge_QuestSystem.js` passed
- `node --check js/plugins/ChromaEdge_QuestJournal.js` passed
- `node --check js/plugins/ChromaEdge_QuestTrackerHUD.js` passed
- `node --check js/plugins.js` passed

## Cohesion Impact

- Core runtime story and side-story data now have strict machine-enforced map/NPC anchor coherence.
- Cohesion checks are aligned with runtime quest scope (`core`) while remaining available for full-pack diagnostics (`all`).
- Parser-level JS checks are now part of practical validation, reducing integration risk in plugin/runtime edits.
