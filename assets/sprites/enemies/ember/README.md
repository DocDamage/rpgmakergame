# Ember/Heat Biome - Enemy Sprite Kit

## Overview
Volcanic biome enemy set - lava, fire, heat distortion, industrial elements.

## Enemy Checklist

### Ember Runner
- [ ] **Overworld** (16x24) - Fast, fire trail
- [ ] **Battle Idle** (48x48) - Crouched, flames
- [ ] **Attack** (3-4 frames) - Dash strike
- [ ] **Hurt** - Flame burst
- [ ] **KO** - Ash pile

**Style:** Fast canine/beast, flames trailing, glowing hot

### Heat Caster
- [ ] **Overworld** (16x24) - Floating embers
- [ ] **Battle Idle** (48x48) - Fire mage stance
- [ ] **Attack** (4-6 frames) - Fireball cast
- [ ] **Hurt** - Ember scatter
- [ ] **KO** - Extinguished

**Style:** Fire mage, robes of flame, ember particles

### Slag Mote
- [ ] **Overworld** (16x16) - Floating molten chunk
- [ ] **Battle Idle** (32x32) - Pulsing heat
- [ ] **Attack** - Explosion
- [ ] **Hurt** - Splatter
- [ ] **KO** - Cooled rock

**Style:** Floating magma chunk, unstable, explosive

## Naming Convention
```
spr_enemy_ember_runner_battle_idle.png
spr_enemy_heat_caster_overworld.png
spr_enemy_slag_mote_attack.png
```

## Stats Reference
```json
{
  "ember_runner": {
    "hp": 130, "mp": 0, "atk": 28, "def": 8, "mag": 0, "spr": 5, "spd": 18,
    "weaknesses": {"water": 1.5, "ice": 1.3},
    "resists": {"fire": 0.0}
  },
  "heat_caster": {
    "hp": 120, "mp": 90, "atk": 10, "def": 7, "mag": 28, "spr": 12, "spd": 12,
    "weaknesses": {"water": 1.5, "ice": 1.5},
    "absorbs": ["fire"]
  },
  "slag_mote": {
    "hp": 50, "mp": 0, "atk": 35, "def": 5, "mag": 0, "spr": 3, "spd": 8,
    "weaknesses": {"water": 2.0},
    "special": ["self_destruct", "burn"]
  }
}
```

## Status: ☐ Not Started | ☐ In Progress | ☐ Complete
