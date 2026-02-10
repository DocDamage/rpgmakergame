# Kade - Character Asset Bundle

## Overview
Protagonist of Chroma's Edge. Complete "ship it" bundle for production pipeline testing.

Current imported source sheet:
- `assets/sprites/characters/kade/overworld/spr_kade_overworld_sheet.png`

## Asset Checklist

### Overworld Sprite (16x24 or 16x32)
- [ ] **Idle** (1-2 frames) - Subtle breathing
- [ ] **Walk North** (3 frames) - Step cycle
- [ ] **Walk South** (3 frames) - Step cycle  
- [ ] **Walk East** (3 frames) - Step cycle
- [ ] **Walk West** (3 frames) - Step cycle
- [ ] **Run** (3-4 frames, optional) - Faster movement

**Naming:** `spr_kade_walk_N.png`, `spr_kade_walk_S.png`, etc.

### Portrait Bust (64x64 or 96x96)
- [ ] **Neutral** - Default expression
- [ ] **Happy** - Positive reaction
- [ ] **Sad** - Concerned/sorrowful
- [ ] **Angry** - Frustrated/combat-ready
- [ ] **Surprised** - Shock/discovery

**Naming:** `spr_kade_portrait_neutral.png`, `spr_kade_portrait_happy.png`, etc.

### Battle Sprite (32x48 or 48x64)
- [ ] **Idle Pose** - Ready stance
- [ ] **Attack** (3-4 frames) - Strike + recovery
- [ ] **Skill** (4-6 frames) - Special ability
- [ ] **Hurt** (2 frames) - Hit + recoil
- [ ] **KO** (1 frame) - Down pose
- [ ] **Victory** (3-4 frames) - Celebration

**Naming:** `spr_kade_battle_idle.png`, `spr_kade_battle_attack.png`, etc.

### Optional (Nice to Have)
- [ ] **Cutscene Bust** - Higher detail for major scenes
- [ ] **Weapon Variants** - Visual equipment changes
- [ ] **Limit Break Pose** - Special stance

## Animation Specs

| Animation | Frames | Timing | Notes |
|-----------|--------|--------|-------|
| Idle | 1-2 | 500ms/frame | Slow, subtle breathing |
| Walk | 3 | 150ms/frame | 4 FPS step cycle |
| Run | 3-4 | 100ms/frame | 6 FPS faster cycle |
| Attack | 3-4 | 50ms on hit | Impact emphasis |
| Skill | 4-6 | Varies | Complexity-based |
| Hurt | 2 | Quick | Hit + recoil |
| Victory | 3-4 | 200ms/frame | Celebration |

## Pivot Points
- **Overworld**: Bottom center (ground alignment)
- **Battle**: Bottom center (ground alignment)
- **Portraits**: Center

## Style Guide
- **Palette**: Earth tones, dust-worn clothing
- **Silhouette**: Distinctive even at small size
- **Readability**: Clear at 16x24 resolution
- **Consistency**: Match other character proportions

## File Locations
```
assets/sprites/characters/kade/
  â”œâ”€ overworld/
  â”‚   â”œâ”€ spr_kade_walk_N.png
  â”‚   â”œâ”€ spr_kade_walk_S.png
  â”‚   â”œâ”€ spr_kade_walk_E.png
  â”‚   â””â”€ spr_kade_walk_W.png
  â”œâ”€ portraits/
  â”‚   â”œâ”€ spr_kade_portrait_neutral.png
  â”‚   â”œâ”€ spr_kade_portrait_happy.png
  â”‚   â”œâ”€ spr_kade_portrait_sad.png
  â”‚   â”œâ”€ spr_kade_portrait_angry.png
  â”‚   â””â”€ spr_kade_portrait_surprised.png
  â””â”€ battle/
      â”œâ”€ spr_kade_battle_idle.png
      â”œâ”€ spr_kade_battle_attack.png
      â”œâ”€ spr_kade_battle_skill.png
      â”œâ”€ spr_kade_battle_hurt.png
      â”œâ”€ spr_kade_battle_ko.png
      â””â”€ spr_kade_battle_victory.png
```

## Status: â˜ Not Started | â˜ In Progress | â˜ Complete

