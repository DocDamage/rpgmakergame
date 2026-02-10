# Chrono/Phase Biome - Enemy Sprite Kit

## Overview
Time-distorted biome enemy set - clockwork, phase-shifting, temporal anomalies.

## Enemy Checklist

### Chrono Scribe
- [ ] **Overworld** (16x24) - Robed figure with time motifs
- [ ] **Battle Idle** (48x48) - Floating, time distortion
- [ ] **Attack** (4-6 frames) - Time magic cast
- [ ] **Hurt** - Glitch/rewind effect
- [ ] **KO** - Fade to static

**Style:** Time mage, clockwork elements, distorted/blurry edges

### Phase Scuttler
- [ ] **Overworld** (16x16) - Flickering in/out
- [ ] **Battle Idle** (40x40) - Phasing between states
- [ ] **Attack** - Teleport strike
- [ ] **Hurt** - Desync effect
- [ ] **KO** - Phase out permanently

**Style:** Insectoid, translucent, teleport effects

### Drone
- [ ] **Overworld** (16x16) - Mechanical hovering
- [ ] **Battle Idle** (40x40) - Scanning animation
- [ ] **Attack** - Laser/scan beam
- [ ] **Hurt** - System glitch
- [ ] **KO** - Crash/deactivation

**Style**: Mechanical, clockwork/tech hybrid, glowing lens

## Naming Convention
```
spr_enemy_chrono_scribe_battle_idle.png
spr_enemy_phase_scuttler_overworld.png
spr_enemy_drone_attack.png
```

## Stats Reference
```json
{
  "chrono_scribe": {
    "hp": 160, "mp": 120, "atk": 10, "def": 10, "mag": 30, "spr": 22, "spd": 12,
    "weaknesses": {"dark": 1.3, "physical": 1.0},
    "resists": {"time": 0.0},
    "special": ["haste", "slow", "rewind"]
  },
  "phase_scuttler": {
    "hp": 120, "mp": 40, "atk": 24, "def": 8, "mag": 10, "spr": 8, "spd": 20,
    "weaknesses": {"light": 1.3},
    "special": ["teleport", "phase_shift"]
  },
  "drone": {
    "hp": 100, "mp": 60, "atk": 18, "def": 15, "mag": 12, "spr": 10, "spd": 14,
    "weaknesses": {"thunder": 1.5, "water": 1.2},
    "resists": {"physical": 0.8}
  }
}
```

## Status: ☐ Not Started | ☐ In Progress | ☐ Complete
