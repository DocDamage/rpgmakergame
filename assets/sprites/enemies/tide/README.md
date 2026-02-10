# Tide Biome - Enemy Sprite Kit

## Overview
Coastal/underwater biome enemy set - maritime, aquatic life, submerged ruins.

## Enemy Checklist

### Scuttler
- [ ] **Overworld** (16x16) - Sideways scuttle
- [ ] **Battle Idle** (40x40) - Crab stance
- [ ] **Attack** (3-4 frames) - Claw snap
- [ ] **Hurt** (2 frames) - Recoil
- [ ] **KO** (1 frame) - Flipped

**Style:** Crab-like, hard shell, sideways movement

### Brine Caster
- [ ] **Overworld** (16x24) - Floating, water effects
- [ ] **Battle Idle** (48x48) - Water mage stance
- [ ] **Attack** (4-6 frames) - Water spell
- [ ] **Hurt** - Splash
- [ ] **KO** - Dissolve

**Style:** Aquatic mage, flowing like water, bioluminescent

### Lampjaw Eel
- [ ] **Overworld** (16x16) - Slithering
- [ ] **Battle Idle** (48x32) - Coiled, lamp glowing
- [ ] **Attack** (4 frames) - Lunge bite
- [ ] **Hurt** (2 frames) - Thrash
- [ ] **KO** (1 frame) - Straight float

**Style:** Deep sea eel, bioluminescent lure, long body

## Naming Convention
```
spr_enemy_scuttler_battle_idle.png
spr_enemy_brine_caster_overworld.png
spr_enemy_lampjaw_eel_attack.png
```

## Stats Reference
```json
{
  "scuttler": {
    "hp": 160, "mp": 0, "atk": 22, "def": 25, "mag": 0, "spr": 8, "spd": 8,
    "weaknesses": {"thunder": 1.5, "ice": 1.0},
    "resists": {"water": 0.0, "physical": 0.8}
  },
  "brine_caster": {
    "hp": 140, "mp": 100, "atk": 8, "def": 8, "mag": 26, "spr": 18, "spd": 10,
    "weaknesses": {"thunder": 1.5, "ice": 1.2},
    "absorbs": ["water"]
  },
  "lampjaw_eel": {
    "hp": 110, "mp": 0, "atk": 30, "def": 6, "mag": 0, "spr": 5, "spd": 16,
    "weaknesses": {"thunder": 1.3},
    "resists": {"water": 0.25}
  }
}
```

## Status: ☐ Not Started | ☐ In Progress | ☐ Complete
