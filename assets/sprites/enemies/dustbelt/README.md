# Dustbelt Biome - Enemy Sprite Kit

## Overview
First biome enemy set for early game/tutorial area.

## Enemy Checklist

### Dust Skirmisher
- [ ] **Overworld** (16x16 to 24x24) - Wandering sprite
- [ ] **Battle Idle** (48x48) - Combat stance
- [ ] **Attack** (3-4 frames) - Melee strike
- [ ] **Hurt** (2 frames) - Hit reaction
- [ ] **KO** (1 frame) - Defeated pose

**Style:** Humanoid, ragged clothing, dust-stained

### Dust Scavenger (Ranged)
- [ ] **Overworld** - Crossbow/sling visible
- [ ] **Battle Idle** - Ranged stance
- [ ] **Attack** (3-4 frames) - Crossbow/sling animation
- [ ] **Hurt** (2 frames)
- [ ] **KO** (1 frame)

**Style:** Lighter armor, ranged weapon, scavenger pack

### Dust Wasp (Flier)
- [ ] **Overworld** - Hovering animation
- [ ] **Battle Idle** - Wing flutter
- [ ] **Attack** - Stinger lunge
- [ ] **Hurt** - Spin recoil
- [ ] **KO** - Fallen

**Style:** Insectoid, stinger, wing blur effect

## Naming Convention
```
spr_enemy_dust_skirmisher_battle_idle.png
spr_enemy_dust_scavenger_overworld.png
spr_enemy_dust_wasp_attack.png
```

## Stats Reference
```json
{
  "dust_skirmisher": {
    "hp": 120, "mp": 0, "atk": 15, "def": 8, "mag": 0, "spr": 5, "spd": 10,
    "weaknesses": {"fire": 1.5, "ice": 1.0, "thunder": 1.0},
    "resists": {"earth": 0.5}
  },
  "dust_scavenger": {
    "hp": 100, "mp": 0, "atk": 18, "def": 6, "mag": 0, "spr": 4, "spd": 12,
    "weaknesses": {"fire": 1.5, "thunder": 1.2},
    "resists": {"earth": 0.5}
  },
  "dust_wasp": {
    "hp": 80, "mp": 0, "atk": 20, "def": 4, "mag": 0, "spr": 3, "spd": 15,
    "weaknesses": {"fire": 1.5, "ice": 1.2},
    "resists": {"earth": 0.0}
  }
}
```

## Status: ☐ Not Started | ☐ In Progress | ☐ Complete
