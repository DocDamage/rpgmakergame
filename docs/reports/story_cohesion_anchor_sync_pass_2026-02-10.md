# Story Cohesion Anchor Sync Pass (2026-02-10)

## Scope

Follow-up major pass to remove remaining cross-pack cohesion warnings by aligning quest step NPC targets with canonical map anchor metadata.

## Changes Applied

1. Tooling
- Added `tools/sync_map_npc_anchors_from_quests.py`.
- Function:
  - scans quest step `target_location` + `target_npc` pairs
  - adds missing NPC IDs to map `key_npcs`
  - supports `--scope core|all` and `--dry-run`

2. Canonical map metadata sync
- Ran:
  - `python3 tools/sync_map_npc_anchors_from_quests.py --scope all`
- Result:
  - changes: `94`
  - files touched: `9`
- Updated map packs:
  - `assets/data/maps/map_capital_chain.json`
  - `assets/data/maps/map_dungeons_main.json`
  - `assets/data/maps/map_generated_placeholders.json`
  - `assets/data/maps/map_overworld.json`
  - `assets/data/maps/map_routes_act1.json`
  - `assets/data/maps/map_story_setpieces.json`
  - `assets/data/maps/map_tower_palace_remnant.json`
  - `assets/data/maps/map_towns_act1.json`
  - `assets/data/maps/map_towns_act2_3.json`

3. Runtime/toolchain support
- Installed local user-space Node runtime for JS syntax checks:
  - `~/.local/lib/node-lts`
  - `~/.local/bin/node`
- `npm` in this local package is not reliable in this environment; `node --check` works and is used for syntax validation.

## Validation Results

1. Story cohesion
- `python3 tools/audit_story_cohesion.py --scope core`
  - `Errors: 0`, `Warnings: 0`
- `python3 tools/audit_story_cohesion.py --scope all`
  - `Errors: 0`, `Warnings: 0`

2. JS syntax checks
- `node --check js/plugins/ChromaEdge_QuestSystem.js` passed
- `node --check js/plugins/ChromaEdge_QuestJournal.js` passed
- `node --check js/plugins/ChromaEdge_QuestTrackerHUD.js` passed

3. Integrity gates
- `python3 tools/validate_content_integrity.py` -> `Errors: 0`, `Warnings: 0`
- `python3 tools/validate_world_integrity.py` -> `Errors: 0`, `Warnings: 0`
- `python3 tools/audit_environment_sprite_coverage.py --strict-candidates --strict-world-dressing` -> `Errors: 0`, `Warnings: 0`

## Cohesion Impact

- Main story, side stories, and generated content packs now agree with canonical map NPC anchor metadata.
- Quest tracker/journal data can rely on map-level NPC anchors without unresolved target warnings.
- Story cohesion audits are clean at both curated runtime scope and full-content scope.
