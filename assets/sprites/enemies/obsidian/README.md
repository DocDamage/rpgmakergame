# Obsidian Biome - Enemy Sprite Kit

## Overview
Industrial mining biome enemy set - machinery, corrupted miners, lava hazards.

## Enemy Checklist

### Quarry Brute
- [ ] **Overworld** (24x24) - Heavy, mechanical
- [ ] **Battle Idle** (64x64) - Corrupted miner stance
- [ ] **Attack** (4-5 frames) - Pickaxe/drill strike
- [ ] **Hurt** (2 frames) - Spark/spasm
- [ ] **KO** (1 frame) - Collapsed machinery

**Style:** Corrupted miner, heavy gear, mechanical parts

### Lava Hazard Unit
- [ ] **Overworld** (16x24) - Hovering drone
- [ ] **Battle Idle** (48x48) - Mechanical threat display
- [ ] **Attack** (4 frames) - Heat beam/flame vent
- [ ] **Hurt** - System failure sparks
- [ ] **KO** - Deactivated heap

**Style:** Industrial drone, hazard warnings, glowing hot parts

## Naming Convention
```
spr_enemy_quarry_brute_battle_idle.png
spr_enemy_lava_hazard_unit_overworld.png
```

## Stats Reference
```json
{
  "quarry_brute": {
    "hp": 280, "mp": 0, "atk": 32, "def": 22, "mag": 0, "spr": 10, "spd": 5,
    "weaknesses": {"water": 1.3, "thunder": 1.2},
    "resists": {"fire": 0.5, "physical": 0.75}
  },
  "lava_hazard_unit": {
    "hp": 150, "mp": 40, "atk": 15, "def": 18, "mag": 20, "spr": 12, "spd": 8,
    "weaknesses": {"water": 1.5, "thunder": 1.3},
    "resists": {"fire": 0.0}
  }
}
```

## Status: ☐ Not Started | ☐ In Progress | ☐ Complete
