# Ambient NPC Population Pass (2026-02-09)

## Summary

- Generated and wired ambient town population NPCs across all town hubs.
- Added `52` new NPC data records (`4` per town across `13` towns).
- Linked each ambient NPC to a `DT_AMBIENT_*` banter tree.
- Added explicit per-map placement entries via `ambient_npcs` arrays.

## Files Updated

- `assets/data/maps/map_towns_act1.json`
- `assets/data/maps/map_towns_act2_3.json`
- `assets/data/npcs/npc_ambient_*.json` (`52` new files)

## Placement Model

- Map-level placement in each town map:
  - `ambient_npcs[]` entries include:
    - `npc` (NPC ID)
    - `coords` (map coordinates)
    - `dialog_tree` (assigned ambient dialog ID)
- NPC record-level placement also set:
  - `location` = town map ID
  - `coords` = matching map placement coordinates
  - day/night/rain schedules aligned to placement coordinate

## Validation

- Naming + ID validation:
  - `python tools/validate_naming.py assets --validate-ids`
  - Result: `Invalid: 0`
- Ambient wiring integrity:
  - map -> NPC references: valid
  - NPC -> dialog references: valid
  - coordinate bounds check: valid
  - result: `AMBIENT_WIRING_ERRORS 0`
