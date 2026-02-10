# Frost Biome - Enemy Sprite Kit

## Overview
Frozen tundra biome enemy set - ice, snow, frozen ruins, cold atmosphere.

## Enemy Checklist

### Frost Skirmisher
- [ ] **Overworld** (16x24) - Winter gear, ice weapons
- [ ] **Battle Idle** (48x48) - Ready stance with ice blade
- [ ] **Attack** (3-4 frames) - Ice blade strike
- [ ] **Hurt** (2 frames) - Frost shatter
- [ ] **KO** (1 frame) - Frozen collapse

**Style:** Humanoid in furs, ice-encrusted weapons, cold aura

### Chill Caster
- [ ] **Overworld** (16x24) - Floating ice crystals
- [ ] **Battle Idle** (48x48) - Ice mage stance
- [ ] **Attack** (4-6 frames) - Ice spell cast
- [ ] **Hurt** - Ice crack
- [ ] **KO** - Shattered ice statue

**Style:** Frost mage, crystalline robes, snow particles

### Frozen Watcher
- [ ] **Overworld** (16x16) - Stationary, eye glow
- [ ] **Battle Idle** (48x48) - Statue-like, alert
- [ ] **Attack** - Eye beam / Ice shard
- [ ] **Hurt** - Cracking
- [ ] **KO** - Crumbled statue

**Style:** Animated ice statue, single glowing eye, defensive

## Naming Convention
```
spr_enemy_frost_skirmisher_battle_idle.png
spr_enemy_chill_caster_overworld.png
spr_enemy_frozen_watcher_attack.png
```

## Stats Reference
```json
{
  "frost_skirmisher": {
    "hp": 170, "mp": 0, "atk": 26, "def": 16, "mag": 0, "spr": 10, "spd": 11,
    "weaknesses": {"fire": 1.5, "thunder": 1.0},
    "resists": {"ice": 0.0}
  },
  "chill_caster": {
    "hp": 130, "mp": 110, "atk": 8, "def": 8, "mag": 28, "spr": 20, "spd": 10,
    "weaknesses": {"fire": 1.5, "thunder": 1.0},
    "absorbs": ["ice"]
  },
  "frozen_watcher": {
    "hp": 200, "mp": 40, "atk": 15, "def": 30, "mag": 15, "spr": 25, "spd": 3,
    "weaknesses": {"fire": 1.5},
    "resists": {"physical": 0.6, "ice": 0.0}
  }
}
```

## Status: ☐ Not Started | ☐ In Progress | ☐ Complete
