# Uplands Biome - Enemy Sprite Kit

## Overview
Second biome enemy set - rocky highlands, ancient stone, worn environments.

## Enemy Checklist

### Rock Brute
- [ ] **Overworld** (24x24) - Large, slow-moving sprite
- [ ] **Battle Idle** (64x64) - Heavy combat stance
- [ ] **Attack** (4-5 frames) - Slam/strike animation
- [ ] **Hurt** (2 frames) - Crumble reaction
- [ ] **KO** (1 frame) - Shattered

**Style:** Large stone humanoid, cracked surface, moss patches

### Wind Caster
- [ ] **Overworld** (16x24) - Floating, robes fluttering
- [ ] **Battle Idle** (48x48) - Hovering animation
- [ ] **Attack** (4-6 frames) - Wind spell cast
- [ ] **Hurt** (2 frames) - Knockback
- [ ] **KO** (1 frame) - Fallen

**Style:** Mage, flowing robes, wind effects, floating slightly

### Stray Wisp
- [ ] **Overworld** (16x16) - Small, bobbing glow
- [ ] **Battle Idle** (32x32) - Pulsing light
- [ ] **Attack** - Light burst
- [ ] **Hurt** - Dim flicker
- [ ] **KO** - Fade out

**Style:** Small glowing orb, ethereal, particle effects

## Naming Convention
```
spr_enemy_rock_brute_battle_idle.png
spr_enemy_wind_caster_overworld.png
spr_enemy_stray_wisp_attack.png
```

## Stats Reference
```json
{
  "rock_brute": {
    "hp": 250, "mp": 0, "atk": 25, "def": 20, "mag": 0, "spr": 10, "spd": 5,
    "weaknesses": {"water": 1.5, "earth": 0.5},
    "resists": {"physical": 0.75}
  },
  "wind_caster": {
    "hp": 150, "mp": 80, "atk": 8, "def": 6, "mag": 25, "spr": 15, "spd": 14,
    "weaknesses": {"earth": 1.5, "ice": 1.2},
    "absorbs": {"wind": 0}
  },
  "stray_wisp": {
    "hp": 60, "mp": 40, "atk": 5, "def": 3, "mag": 20, "spr": 20, "spd": 18,
    "weaknesses": {"dark": 1.5, "physical": 1.2},
    "resists": {"magic": 0.5}
  }
}
```

## Status: ☐ Not Started | ☐ In Progress | ☐ Complete
