# Mire Biome - Enemy Sprite Kit

## Overview
Swamp biome enemy set - wetlands, bioluminescence, fungal infection.

## Enemy Checklist

### Leechling
- [ ] **Overworld** (16x16) - Small, wriggling
- [ ] **Battle Idle** (32x32) - Swarm sprite
- [ ] **Attack** - Lunge/bite
- [ ] **Hurt** - Recoil
- [ ] **KO** - Deflated

**Style:** Small leech-like creature, slimy, swarm behavior

### Sporeling
- [ ] **Overworld** (16x16) - Floating spores
- [ ] **Battle Idle** (40x40) - Pulsing fungal mass
- [ ] **Attack** (4 frames) - Spore burst
- [ ] **Hurt** - Spore release
- [ ] **KO** - Collapsed

**Style:** Fungal humanoid, spore clouds, bioluminescent spots

### Mire Bully
- [ ] **Overworld** (24x24) - Large amphibian
- [ ] **Battle Idle** (64x64) - Heavy stance
- [ ] **Attack** (4-5 frames) - Tongue strike / body slam
- [ ] **Hurt** (2 frames) - Recoil
- [ ] **KO** (1 frame) - Belly-up

**Style:** Large frog/toad, warty skin, swamp muck

## Naming Convention
```
spr_enemy_leechling_battle_idle.png
spr_enemy_sporeling_overworld.png
spr_enemy_mire_bully_attack.png
```

## Stats Reference
```json
{
  "leechling": {
    "hp": 70, "mp": 0, "atk": 12, "def": 4, "mag": 0, "spr": 3, "spd": 16,
    "weaknesses": {"fire": 1.5, "ice": 1.0},
    "abilities": ["leech", "swarm"]
  },
  "sporeling": {
    "hp": 110, "mp": 50, "atk": 8, "def": 6, "mag": 18, "spr": 12, "spd": 10,
    "weaknesses": {"fire": 1.5, "wind": 1.2},
    "inflicts": ["poison", "confuse"]
  },
  "mire_bully": {
    "hp": 300, "mp": 0, "atk": 30, "def": 15, "mag": 0, "spr": 8, "spd": 6,
    "weaknesses": {"ice": 1.3, "lightning": 1.2},
    "resists": {"water": 0.5, "earth": 0.75}
  }
}
```

## Status: ☐ Not Started | ☐ In Progress | ☐ Complete
