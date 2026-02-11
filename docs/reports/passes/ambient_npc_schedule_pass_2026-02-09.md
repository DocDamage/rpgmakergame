# Ambient NPC Schedule Pass (2026-02-09)

## Summary

- Converted ambient NPC schedules from static to moving day/night/rain variants.
- Applied updates to all generated ambient NPC records (`52` files).
- Kept `coords` as canonical day position for compatibility.

## Schedule Model

- `day`: original placement coordinate (matches `coords`)
- `night`: role-based shifted coordinate (patrol/market/route behavior)
- `rain`: role-based shelter/alternate-path coordinate

Role behavior was driven by ambient dialogue archetype (`DT_AMBIENT_*`) so movement style stays coherent with NPC role.

## Files Updated

- `assets/data/npcs/npc_ambient_*.json` (`52` files)

## Validation

- Naming + ID validation:
  - `python tools/validate_naming.py assets --validate-ids`
  - Result: `Invalid: 0`
- Schedule integrity checks:
  - `AMBIENT_SCHEDULE_ERRORS 0`
  - `AMBIENT_TOTAL 52`
  - `MOVED_AT_NIGHT 52`
  - `MOVED_IN_RAIN 52`
