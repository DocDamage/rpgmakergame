# Capital/Void Biome - Enemy Sprite Kit

## Overview
Endgame biome enemy set - Dominion forces, void corruption, dark magic.

## Enemy Checklist

### Record Sentry
- [ ] **Overworld** (16x24) - Dominion archive guard
- [ ] **Battle Idle** (48x48) - Alert stance
- [ ] **Attack** (4-5 frames) - Tech/magic strike
- [ ] **Hurt** - System feedback
- [ ] **KO** - Deactivated

**Style:** Dominion uniform, mask/helmet, archive-themed gear

### Null Caster
- [ ] **Overworld** (16x24) - Void energy emanating
- [ ] **Battle Idle** (48x48) - Void mage stance
- [ ] **Attack** (4-6 frames) - Void spell
- [ ] **Hurt** - Glitch/dissolve
- [ ] **KO** - Fade to void

**Style:** Void-touched mage, darkness, corruption effects

### Void Elite
- [ ] **Overworld** (24x24) - Imposing, elite armor
- [ ] **Battle Idle** (64x64) - Combat ready
- [ ] **Attack** (5-6 frames) - Heavy strike
- [ ] **Hurt** - Void shield crack
- [ ] **KO** - Void implosion

**Style:** Elite soldier, void-empowered, dark aura, late-game threat

## Naming Convention
```
spr_enemy_record_sentry_battle_idle.png
spr_enemy_null_caster_overworld.png
spr_enemy_void_elite_attack.png
```

## Stats Reference
```json
{
  "record_sentry": {
    "hp": 200, "mp": 60, "atk": 22, "def": 18, "mag": 15, "spr": 15, "spd": 12,
    "weaknesses": {"void": 1.3, "thunder": 1.2},
    "resists": {"physical": 0.75}
  },
  "null_caster": {
    "hp": 160, "mp": 140, "atk": 8, "def": 8, "mag": 35, "spr": 25, "spd": 11,
    "weaknesses": {"light": 1.5},
    "resists": {"void": 0.0, "dark": 0.0}
  },
  "void_elite": {
    "hp": 350, "mp": 80, "atk": 38, "def": 28, "mag": 20, "spr": 18, "spd": 10,
    "weaknesses": {"light": 1.3},
    "resists": {"void": 0.25, "dark": 0.25, "physical": 0.7}
  }
}
```

## Status: ☐ Not Started | ☐ In Progress | ☐ Complete
