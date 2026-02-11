# Content Runtime Validation Pass (2026-02-10)

## Scope

Second major cohesion step after stabilization + content normalization:
- make quest dependency semantics explicit and machine-validated
- enforce canonical cross-reference integrity for quests/maps/NPCs/items
- enforce map-to-tileset environment sprite coverage checks

## Changes Applied

1. Normalization schema hardening:
- Updated `tools/normalize_content_quests.py` to split quest references from non-quest gate tokens:
  - `prerequisites` / `unlocks` => quest IDs only
  - `prerequisite_flags` / `unlock_flags` => non-quest state tokens
- Step reward unlocks now emit `unlock_flags` when source token is not a quest.
- Alias registry now includes `state_tokens` summary/list in:
  - `assets/data/system/content_id_aliases_generated.json`

2. Generated content packs refreshed:
- `assets/data/quests/quest_content_main_normalized.json`
- `assets/data/quests/quest_content_mini_normalized.json`
- `assets/data/items/item_content_story_generated.json`
- `assets/data/system/content_id_aliases_generated.json`

3. Legacy canonical quest cleanup (schema consistency):
- Updated non-quest unlock tokens to explicit flag fields:
  - `assets/data/quests/quest_main_story.json`
  - `assets/data/quests/quest_side_stories.json`
  - `assets/data/quests/quest_generated_placeholders.json`

4. New validation tools:
- `tools/validate_content_integrity.py`
  - validates canonical quest pack schema and cross-references
  - validates mainline dependency cohesion
  - validates prerequisite graph acyclicity
- `tools/audit_environment_sprite_coverage.py`
  - validates map-referenced tilesets have source PNG + README
  - validates curation candidate coverage
  - validates town world-dressing/service-to-interior consistency

5. Policy update:
- Updated `docs/CANONICAL_DATA_POLICY.md` with quest token semantics and expanded validation gate commands.

## Validation Results

All core integrity gates pass:
- `python3 tools/validate_content_integrity.py` => `Errors: 0`, `Warnings: 0`
- `python3 tools/audit_environment_sprite_coverage.py --strict-candidates` => `Errors: 0`, `Warnings: 0`
- `python3 tools/validate_world_integrity.py` => `Errors: 0`, `Warnings: 0`

## Cohesion Impact

- Story and side-story quest references are now structurally separable from world-state gating flags.
- Canonical quest data now validates cleanly under strict cross-reference checks.
- Environment sprite deployment is now auditable against map usage and town dressing data.
