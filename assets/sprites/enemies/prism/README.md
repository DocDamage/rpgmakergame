# Prism Biome - Enemy Sprite Kit

## Overview
Crystal highlands enemy set - prismatic formations, reflective surfaces, light manipulation.

## Enemy Checklist

### Crystal Ranged
- [ ] **Overworld** (16x24) - Floating crystal shards
- [ ] **Battle Idle** (48x48) - Hovering crystal entity
- [ ] **Attack** (4-5 frames) - Light beam animation
- [ ] **Hurt** (2 frames) - Crack/shatter reaction
- [ ] **KO** (1 frame) - Shattered crystal

**Style:** Crystalline humanoid, refracts light, geometric

### Refraction Image
- [ ] **Overworld** - Shimmering, translucent
- [ ] **Battle Idle** (48x48) - Mirror-like duplicate
- [ ] **Attack** - Mimic player attack
- [ ] **Hurt** - Distortion
- [ ] **KO** - Fade to glass shards

**Style:** Mirror/clone appearance, distorted, reflective

## Naming Convention
```
spr_enemy_crystal_ranged_battle_idle.png
spr_enemy_refraction_image_overworld.png
```

## Stats Reference
```json
{
  "crystal_ranged": {
    "hp": 140, "mp": 60, "atk": 12, "def": 18, "mag": 22, "spr": 20, "spd": 10,
    "weaknesses": {"dark": 1.5, "earth": 1.3},
    "resists": {"light": 0.0, "physical": 0.8}
  },
  "refraction_image": {
    "hp": 100, "mp": 40, "atk": 15, "def": 10, "mag": 15, "spr": 15, "spd": 14,
    "weaknesses": {"dark": 1.5},
    "special": ["mimic", "clone"]
  }
}
```

## Status: ☐ Not Started | ☐ In Progress | ☐ Complete
