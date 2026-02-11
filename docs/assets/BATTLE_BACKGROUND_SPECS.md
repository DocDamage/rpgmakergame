# Battle Background Specifications

## Overview
Battle backgrounds set the tone for combat encounters. Each biome needs a distinct visual identity.

## Technical Specs

| Property | Value |
|----------|-------|
| **Resolution** | 640x360 (16:9) or 480x270 ( scalable) |
| **Format** | PNG with transparency support for layers |
| **Color Depth** | 32-bit (24-bit + alpha) |
| **Style** | 16-bit JRPG pixel art (SNES/PS1 era) |
| **Parallax Layers** | 2-3 layers recommended |

## Background Checklist

### Core Biome Backgrounds (9)

#### 1. Dustbelt Battle BG
- [ ] **Base Layer:** Sand dunes, cracked earth
- [ ] **Mid Layer:** Rock formations, wagon wreckage
- [ ] **Effects:** Dust particles (animated), heat shimmer
- [ ] **Palette:** Warm earth tones (#C4A35A, #8B7355, #D4C5A3)
- [ ] **Naming:** `bg_battle_dustbelt.png`

#### 2. Uplands Battle BG
- [ ] **Base Layer:** Rocky highland terrain
- [ ] **Mid Layer:** Ancient stone markers, dead trees
- [ ] **Effects:** Wind particles, distant birds
- [ ] **Palette:** Gray-brown rocks (#7a7a7a, #5a5a5a, #6B8E5A moss)
- [ ] **Naming:** `bg_battle_uplands.png`

#### 3. Mire Battle BG
- [ ] **Base Layer:** Murky water, mud banks
- [ ] **Mid Layer:** Mangrove roots, hanging moss
- [ ] **Effects:** Bioluminescent glow (animated), mist
- [ ] **Palette:** Deep greens (#2d4a3e, #3e5a4e, #7FFFD4 glow)
- [ ] **Naming:** `bg_battle_mire.png`

#### 4. Prism Battle BG
- [ ] **Base Layer:** Crystal bedrock, prismatic stones
- [ ] **Mid Layer:** Crystal formations, reflective pools
- [ ] **Effects:** Light refraction (animated), sparkle
- [ ] **Palette:** Crystal blues/pinks (#87CEEB, #DDA0DD, #FFD700)
- [ ] **Naming:** `bg_battle_prism.png`

#### 5. Ember Battle BG
- [ ] **Base Layer:** Basalt rock, cooling lava crust
- [ ] **Mid Layer:** Lava vents, volcanic peaks
- [ ] **Effects:** Lava glow (animated), heat distortion, ember particles
- [ ] **Palette:** Fire oranges (#FF4500, #FF6347, #2d2d2d)
- [ ] **Naming:** `bg_battle_ember.png`

#### 6. Tide Battle BG
- [ ] **Base Layer:** Rocky shore, tidal pools
- [ ] **Mid Layer:** Coastal cliffs, distant ocean
- [ ] **Effects:** Wave animation, sea spray, seabirds
- [ ] **Palette:** Ocean blues (#4682B4, #5F9EA0, #F5F5DC sand)
- [ ] **Naming:** `bg_battle_tide.png`

#### 7. Frost Battle BG
- [ ] **Base Layer:** Snow field, ice sheets
- [ ] **Mid Layer:** Frozen ruins, dead pines
- [ ] **Effects:** Falling snow (animated), frost breath
- [ ] **Palette:** Ice whites/blues (#FFFAFA, #B0E0E6, #4682B4)
- [ ] **Naming:** `bg_battle_frost.png`

#### 8. Chrono Battle BG
- [ ] **Base Layer:** Time-frozen landscape
- [ ] **Mid Layer:** Clockwork mechanisms, phase architecture
- [ ] **Effects:** Time distortion (glitch/ripple), gear rotation
- [ ] **Palette:** Time silver/purple (#C0C0C0, #9370DB, #00CED1)
- [ ] **Naming:** `bg_battle_chrono.png`

#### 9. Capital/Void Battle BG
- [ ] **Base Layer:** Ruined capital streets
- [ ] **Mid Layer:** Collapsed monuments, void seams
- [ ] **Effects:** Void corruption (animated), glitch effects
- [ ] **Palette:** Ruined grays/void purple (#696969, #4B0082, #1a1a1a)
- [ ] **Naming:** `bg_battle_capital.png`

### Special Battle Backgrounds (5+)

#### 10. Boss Arena - Generic
- [ ] **Style:** Elevated circular platform, cosmic void background
- [ ] **Effects:** Energy aura, particle field
- [ ] **Naming:** `bg_battle_boss_generic.png`

#### 11. Tower Arena
- [ ] **Style:** Progenitor architecture, ascending energy
- [ ] **Effects:** Vertical energy flow, data streams
- [ ] **Naming:** `bg_battle_tower.png`

#### 12. Palace Arena
- [ ] **Style:** Cosmic throne room, starfield background
- [ ] **Effects:** Star twinkle, ethereal glow
- [ ] **Naming:** `bg_battle_palace.png`

#### 13. Remnant Vault Arena
- [ ] **Style:** Glitch corruption, unstable reality
- [ ] **Effects:** Heavy glitch, color separation, static
- [ ] **Naming:** `bg_battle_remnant.png`

#### 14. Shrine Arena
- [ ] **Style:** Sacred geometric platform, elemental theme
- [ ] **Variants:** One per foundation (8 total variants)
- [ ] **Naming:** `bg_battle_shrine_heat.png`, `bg_battle_shrine_growth.png`, etc.

## Layer Structure (for parallax)

```
Layer 0 (Back):    Sky/void - static or very slow
Layer 1 (Mid-Back): Far terrain - 0.3x scroll
Layer 2 (Mid):      Ground/arena floor - 0.6x scroll
Layer 3 (Front):    Foreground elements - 1.0x scroll (behind characters)
```

## Animation Specifications

| Effect | Frames | FPS | Notes |
|--------|--------|-----|-------|
| Dust particles | 4 | 8 | Drifting sand |
| Lava glow | 8 | 12 | Pulsing heat |
| Water waves | 8 | 10 | Ocean tide |
| Snow fall | 8 | 15 | Gentle descent |
| Bioluminescence | 8 | 6 | Slow pulse |
| Glitch effect | 4 | 12 | Random distortion |
| Star twinkle | 8 | 8 | Random pattern |

## File Naming Convention

```
bg_battle_{biome}_{variant}.png
bg_battle_{biome}_{variant}_layer{0-3}.png

Examples:
- bg_battle_dustbelt.png (flat composite)
- bg_battle_dustbelt_layer0.png (sky)
- bg_battle_dustbelt_layer1.png (dunes)
- bg_battle_dustbelt_layer2.png (foreground)

Animated:
- bg_battle_ember_layer1_f{0-7}.png (8-frame animation)
```

## Folder Structure

```
assets/
  backgrounds/
    battle/
      dustbelt/
        bg_battle_dustbelt_layer0.png
        bg_battle_dustbelt_layer1.png
        bg_battle_dustbelt_layer2.png
        fx_dust_particles_f0-3.png
      uplands/
      mire/
      prism/
      ember/
      tide/
      frost/
      chrono/
      capital/
      special/
        bg_battle_boss_generic.png
        bg_battle_tower.png
        bg_battle_palace.png
```

## Status Tracking

| Background | Layers | Animation | Status |
|------------|--------|-----------|--------|
| Dustbelt | ☐ | ☐ | ☐ |
| Uplands | ☐ | ☐ | ☐ |
| Mire | ☐ | ☐ | ☐ |
| Prism | ☐ | ☐ | ☐ |
| Ember | ☐ | ☐ | ☐ |
| Tide | ☐ | ☐ | ☐ |
| Frost | ☐ | ☐ | ☐ |
| Chrono | ☐ | ☐ | ☐ |
| Capital | ☐ | ☐ | ☐ |
| Boss Arena | ☐ | ☐ | ☐ |
| Tower | ☐ | ☐ | ☐ |
| Palace | ☐ | ☐ | ☐ |
| Remnant | ☐ | ☐ | ☐ |

*Legend: ☐ Not Started | 🔄 In Progress | ✅ Complete*
