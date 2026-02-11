# Parallax Layer Guide

## Overview
Parallax scrolling creates depth by moving background layers at different speeds relative to the camera. Essential for visual polish.

## Technical Implementation

### Layer Stack (Bottom to Top)

```
Layer 0: Background (sky, void, distant cosmos)
Layer 1: Far terrain (mountains, city skyline)
Layer 2: Mid terrain (hills, buildings, trees)
Layer 3: Ground layer (walkable tiles)
Layer 4: Player/NPCs
Layer 5: Foreground objects (roofs, overhangs)
Layer 6: Weather/effects overlay
```

### Scroll Speed Formula

```javascript
// layer_position = camera_position * scroll_factor

Layer 0 (Sky):         scroll_factor = 0.0  (static)
Layer 1 (Far):         scroll_factor = 0.2  (20% of camera speed)
Layer 2 (Mid):         scroll_factor = 0.5  (50% of camera speed)
Layer 3 (Ground):      scroll_factor = 1.0  (100% - locked to camera)
Layer 5 (Foreground):  scroll_factor = 1.2  (120% - moves faster)
```

## Per-Map-Type Specifications

### 1. Overworld Parallax (OW_ORION)

| Layer | Content | Scroll Factor | Size | Notes |
|-------|---------|---------------|------|-------|
| 0 | Sky gradient | 0.0 | 320x180 | Static, color shifts by time |
| 1 | Far biome silhouettes | 0.1 | 640x180 | Shows distant regions |
| 2 | Cloud layer | 0.15 | 640x180 | Slow drift animation |
| 3 | Ground/terrain | 1.0 | 320x180 | Main walkable layer |
| 4 | Weather overlay | 1.0 | 320x180 | Rain, snow, dust |

**Special Effects:**
- **Time of day:** Layer 0 shifts colors (dawn→day→dusk→night)
- **Weather:** Layer 4 has animated particles
- **Biome transition:** Layer 1/2 blend between regions

### 2. Town Parallax

#### Standard Town (Dusthaven example)

| Layer | Content | Scroll Factor | Notes |
|-------|---------|---------------|-------|
| 0 | Sky | 0.0 | Day/night cycle |
| 1 | Distant dunes | 0.2 | Establishes setting |
| 2 | Town walls/buildings | 0.4 | Creates depth |
| 3 | Street/ground | 1.0 | Walkable layer |
| 4 | Building roofs | 1.2 | Player walks behind |
| 5 | Dust particles | 1.0 | Weather overlay |

#### Vertical Town (Cinderstep - stacked)

| Layer | Content | Scroll Factor | Notes |
|-------|---------|---------------|-------|
| 0 | Smoke/red sky | 0.0 | Atmospheric |
| 1 | Lower town | 0.3 | Visible from upper |
| 2 | Mid terraces | 0.6 | 
| 3 | Current level | 1.0 | Walkable |
| 4 | Upper structures | 1.3 | Overhangs |

### 3. Dungeon Parallax

#### Cave/Interior (Crystal Caverns example)

| Layer | Content | Scroll Factor | Notes |
|-------|---------|---------------|-------|
| 0 | Deep cave darkness | 0.0 | Gradient to black |
| 1 | Crystal clusters | 0.3 | Glow effect |
| 2 | Rock walls | 0.6 | 
| 3 | Floor | 1.0 | Walkable |
| 4 | Stalactites | 1.1 | Ceiling details |
| 5 | Light rays | 0.8 | God rays from crystals |

### 4. Route/Micro-Map Parallax

| Layer | Content | Scroll Factor | Notes |
|-------|---------|---------------|-------|
| 0 | Sky/atmosphere | 0.0 | 
| 1 | Far landscape | 0.15 | Mountains, horizon |
| 2 | Near terrain | 0.4 | Trees, rocks |
| 3 | Path/ground | 1.0 | Walkable |
| 4 | Foreground foliage | 1.3 | Bushes, grass tufts |

## Tileset-Specific Guidelines

### Dustbelt (Desert)
- **Layer 1:** Distant dunes (rolling shapes)
- **Layer 2:** Mid rock formations
- **Effect:** Heat shimmer on Layer 1/2

### Uplands (Rocky)
- **Layer 1:** Mountain range silhouette
- **Layer 2:** Closer rock outcroppings
- **Effect:** Eagle birds on Layer 1

### Mire (Swamp)
- **Layer 1:** Mist/fog bank
- **Layer 2:** Distant cypress trees
- **Effect:** Fireflies on Layer 2

### Prism (Crystal)
- **Layer 1:** Giant crystal spires
- **Layer 2:** Reflective surfaces
- **Effect:** Light beams, sparkles

### Ember (Volcanic)
- **Layer 1:** Volcanic peaks, smoke plumes
- **Layer 2:** Lava flows (glowing)
- **Effect:** Ash particles, heat distortion

### Tide (Coastal)
- **Layer 1:** Ocean horizon
- **Layer 2:** Waves, rocks
- **Effect:** Seabirds, spray

### Frost (Ice)
- **Layer 1:** Glacier walls
- **Layer 2:** Ice formations
- **Effect:** Falling snow, aurora

### Chrono (Time)
- **Layer 1:** Clockwork mechanisms
- **Layer 2:** Phase-shifted architecture
- **Effect:** Time ripples

### Capital (Ruins)
- **Layer 1:** Palace silhouette (ominous)
- **Layer 2:** Ruined buildings
- **Effect:** Void seams, ash fall

## Implementation Code Template

```javascript
// Parallax Layer System
class ParallaxLayer {
  constructor(image, scrollFactor, zIndex) {
    this.image = image;
    this.scrollFactor = scrollFactor;
    this.zIndex = zIndex;
    this.offsetX = 0;
    this.offsetY = 0;
  }
  
  update(cameraX, cameraY) {
    // Calculate parallax offset
    this.offsetX = cameraX * this.scrollFactor;
    this.offsetY = cameraY * this.scrollFactor;
    
    // Handle tiling for infinite scroll
    if (this.scrollFactor < 1.0) {
      this.offsetX = this.offsetX % this.image.width;
      this.offsetY = this.offsetY % this.image.height;
    }
  }
  
  render(ctx, screenWidth, screenHeight) {
    const x = -this.offsetX;
    const y = -this.offsetY;
    
    // Draw with tiling for layers that need it
    if (this.scrollFactor < 1.0) {
      // Tile horizontally
      for (let tx = x; tx < screenWidth; tx += this.image.width) {
        ctx.drawImage(this.image, tx, y);
      }
    } else {
      ctx.drawImage(this.image, x, y);
    }
  }
}

// Layer setup per map type
const overworldLayers = [
  new ParallaxLayer(skyImage, 0.0, 0),
  new ParallaxLayer(farMountains, 0.1, 1),
  new ParallaxLayer(cloudsImage, 0.15, 2),
  // Ground layer is rendered separately
];

const townLayers = [
  new ParallaxLayer(skyImage, 0.0, 0),
  new ParallaxLayer(distantBuildings, 0.2, 1),
  new ParallaxLayer(midBuildings, 0.4, 2),
  new ParallaxLayer(foregroundRoofs, 1.2, 5),
];
```

## File Naming & Organization

```
assets/
  backgrounds/
    parallax/
      overworld/
        parallax_ow_layer0_sky.png
        parallax_ow_layer1_mountains.png
        parallax_ow_layer2_clouds.png
      towns/
        dusthaven/
          parallax_town_layer0_sky.png
          parallax_town_layer1_dunes.png
          parallax_town_layer2_walls.png
          parallax_town_layer4_roofs.png
      dungeons/
        d1_ruins/
          parallax_d1_layer0_darkness.png
          parallax_d1_layer1_crystals.png
          parallax_d1_layer2_walls.png
```

## Quick Reference: Scroll Factors

| Visual Element | Scroll Factor | Use Case |
|----------------|---------------|----------|
| Sky | 0.0 | Always static |
| Far horizon | 0.1-0.2 | Mountains, city skyline |
| Mid-ground | 0.3-0.5 | Buildings, trees, hills |
| Near ground | 0.6-0.9 | Fences, rocks, details |
| Walkable | 1.0 | Player moves here |
| Foreground | 1.1-1.3 | Overhangs, roofs |

## Optimization Tips

1. **Tile repeating layers** - Don't make giant images, tile smaller ones
2. **Limit layer count** - 3-4 layers max for performance
3. **Use power-of-2 dimensions** - Easier GPU handling
4. **Compress static layers** - Use appropriate formats
5. **Animate sparingly** - Animated layers cost more

## Status Tracking

| Map Type | Layer 0 | Layer 1 | Layer 2 | Layer 3+ | Status |
|----------|---------|---------|---------|----------|--------|
| Overworld | ☐ | ☐ | ☐ | ☐ | ☐ |
| Town - Dusthaven | ☐ | ☐ | ☐ | ☐ | ☐ |
| Town - Ashveil | ☐ | ☐ | ☐ | ☐ | ☐ |
| Town - Mirewatch | ☐ | ☐ | ☐ | ☐ | ☐ |
| Town - Prismridge | ☐ | ☐ | ☐ | ☐ | ☐ |
| Dungeon - D1 | ☐ | ☐ | ☐ | ☐ | ☐ |
| Dungeon - D2 | ☐ | ☐ | ☐ | ☐ | ☐ |
| Routes | ☐ | ☐ | ☐ | ☐ | ☐ |

*Legend: ☐ Not Started | 🔄 In Progress | ✅ Complete*
