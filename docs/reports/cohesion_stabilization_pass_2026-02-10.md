# Cohesion Stabilization Pass (2026-02-10)

## Scope

This pass applied high-impact data and asset integration fixes to improve world/story cohesion in the canonical `assets/data` layer and production sprite pipeline.

## Changes Applied

1. Mainline progression blockers removed:
- Updated `assets/data/quests/quest_generated_placeholders.json`:
  - `Q_ALL_RELICS` no longer requires `Q_KORR_LIBERATION`.
  - `Q_SEVENTH_RELIC` no longer requires `Q_KORR_LIBERATION`.

2. Tower progression routing aligned to main-story steps:
- Updated `assets/data/maps/map_tower_palace_remnant.json`:
  - Added lobby links to `TWR_ARENA_F50_64x64` (`f50_unlocked`) and `TWR_ARENA_F100_64x64` (`f100_unlocked`).
  - Added lobby access hooks for captain/optional floors (`F15/F25/F35/F55/F65/F85/F95`) with progression triggers.
  - Added `F50_UNLOCKED` to `TWR_ARENA_F10_48x48` events.
  - Added `F100_UNLOCKED` to `TWR_ARENA_F50_64x64` events.

3. Shrine trial chain connectivity added:
- Updated `assets/data/maps/map_hidden_shrines.json`:
  - Added sequential shrine-to-shrine links:
    - Heat -> Growth -> Light -> Motion -> Mass -> Time -> Shadow -> Tide
  - Each hop is gated by previous shrine clear flag.
- Updated `assets/data/maps/map_overworld.json`:
  - Added overworld entrance hook to shrine circuit start (`SHR_HEAT_64x48`, post-game gated).

4. Halcyon Freeport promoted from script/lore-only to canonical map data:
- Added `T_HALCYON_FREEPORT_112x72` to `assets/data/maps/map_towns_act2_3.json`.
- Added post-game world-node connection in `assets/data/maps/map_overworld.json`.
- Added Brinegate post-game ferry connection in `assets/data/maps/map_towns_act1.json`.
- Added Aetherreach/Halcyon crosslink and Remnant Gatehouse linkage.

5. Environment sprite pipeline promotion:
- Promoted 20 curated tileset candidates into active production path:
  - `assets/sprites/tilesets/_curation_candidates/*.png`
- Added `tileset_uplands_source_primary.png` alias source in active tileset folder.
- Updated alias note in `assets/sprites/tilesets/README_Tileset_Uplands.md`.

## Validation Results

1. Structural validator:
- `python3 tools/validate_world_integrity.py`
- Result: `Errors: 0`, `Warnings: 0`

2. JSON parse validation (edited files):
- Result: all edited JSON files parse successfully.

3. Cohesion metrics snapshot (post-pass):
- `ASSETS_MAP_COUNT`: `98` (was `97`)
- `ASSETS_QUEST_REF_MISSING`: `0`
- `MAIN_QUEST_NON_MAIN_PREREQ`: `0` (was `2`)
- Directed overworld reachability gaps: `0` (was `22`)
- Quest step transition gaps (graph reachability check): `0` (was `8`)
- Active curation candidate count: `20` (was `0`)
- Missing tileset source PNGs: `0` (was `1`)

## Remaining Intentional/Deferred Items

1. `Tileset_Uplands` remains a legacy alias spec and is intentionally not used as the primary map tileset ID.
2. `content/quests/*` remains a parallel narrative content layer and is not yet ID-normalized to canonical runtime IDs in `assets/data/*`.
3. Runtime `data/Map*.json` and plugin implementation remain separate from this content/data cohesion pass.
