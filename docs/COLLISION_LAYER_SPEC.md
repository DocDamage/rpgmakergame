# Collision & Layer Specification

## Overview
This document defines the collision system and layer architecture for Chroma's Edge. **This is design data** - implement in your engine of choice.

## Layer Stack (Bottom to Top)

```
Layer 0: Background (parallax, non-interactive)
Layer 1: Ground (walkable tiles)
Layer 2: Ground Detail (decoration, walkable)
Layer 3: Elevation 1 (cliffs, stairs - blocks movement)
Layer 4: Objects Lower (tables, crates - blocks movement)
Layer 5: Characters (player, NPCs, enemies)
Layer 6: Objects Upper (roofs, trees - player walks under)
Layer 7: Effects (weather, particles)
Layer 8: Lighting Overlay (darkness, glow)
Layer 9: UI (always top)
```

### Layer Details

| Layer | Name | Walkable | Collision | Notes |
|-------|------|----------|-----------|-------|
| 0 | Background | N/A | None | Parallax layers |
| 1 | Ground | Yes | None | Base walkable surface |
| 2 | Ground Detail | Yes | None | Grass, cracks, decorations |
| 3 | Elevation | Varies | Height | Stairs, cliffs, ramps |
| 4 | Objects Lower | No | Full | Crates, furniture, walls |
| 5 | Characters | Yes | Entity | Dynamic collision |
| 6 | Objects Upper | N/A | None | Roofs, tree tops |
| 7 | Effects | N/A | None | Visual only |
| 8 | Lighting | N/A | None | Render overlay |
| 9 | UI | N/A | None | Interface layer |

## Collision Types

### Type Definitions

| Type | Behavior | Implementation |
|------|----------|----------------|
| **NONE** | Walkable | No collision check |
| **FULL** | Blocks all | Solid rectangle collision |
| **HEIGHT** | Blocks if elevation differs | Height map check |
| **WATER** | Slows, swimming | Speed modifier + swimming state |
| **HAZARD** | Damages on contact | Damage trigger on enter |
| **INTERACT** | Triggers event | On_interact callback |
| **ENCOUNTER** | Random battle | % chance per step |
| **ZONE** | Triggers transition | Load new map |

### Collision Data Format (per tile)

```json
{
  "tile_id": "autotile_001",
  "collision": {
    "type": "FULL",
    "shape": "rectangle",
    "bounds": {"x": 0, "y": 0, "w": 16, "h": 16}
  },
  "height": 0,
  "flags": ["blocks_sight", "blocks_projectiles"]
}
```

## Collision Shapes

### Supported Shapes

1. **Rectangle** (default)
   ```
   x, y, width, height
   ```

2. **Circle** (for rounded objects)
   ```
   center_x, center_y, radius
   ```

3. **Polygon** (for complex shapes)
   ```
   [x1,y1, x2,y2, x3,y3, ...]
   ```

4. **Tile-based** (grid aligned)
   ```
   Whole tile (16x16) collision
   ```

## Z-Depth & Y-Sorting

### Sorting Formula
```javascript
// Characters sort by Y position within layer
sort_order = layer_priority * 1000 + y_position

// Example:
// Player at (100, 200) on layer 5
sort_order = 5 * 1000 + 200 = 5200

// NPC at (100, 180) on layer 5  
sort_order = 5 * 1000 + 180 = 5180
// Result: NPC renders first (behind player)
```

### Upper/Lower Object Rules
```javascript
// Objects with "upper" flag render above characters
// when player is "in front" of them
if (object.upper && player.y > object.y) {
    object.layer = LAYER_UPPER_OBJECTS;  // Layer 6
} else {
    object.layer = LAYER_LOWER_OBJECTS;  // Layer 4
}
```

## Interaction System

### Trigger Types

| Trigger | Activation | Use Case |
|---------|------------|----------|
| **on_enter** | Player steps on tile | Zone transitions, hazards |
| **on_interact** | Button press near | NPCs, doors, chests |
| **on_approach** | Within radius | Auto-talk, detection |
| **on_leave** | Player exits zone | Cleanup, despawn |
| **on_collision** | Contact with entity | Push blocks, bump |

### Interaction Distance

```json
{
  "interaction": {
    "reach": 24,
    "facing_only": true,
    "height_tolerance": 8
  }
}
```

## Map Collision Data

### Per-Map Collision File

```json
{
  "map_id": "T_DUSTHAVEN_112x72",
  "tile_size": 16,
  "dimensions": {"w": 112, "h": 72},
  "collision_map": "collision_layer_data",
  "height_map": "height_layer_data",
  "zones": [
    {
      "id": "door_blacksmith",
      "type": "ZONE",
      "bounds": {"x": 80, "y": 45, "w": 16, "h": 16},
      "target": "I_SMITH_32x24",
      "target_coords": [16, 20]
    },
    {
      "id": "innkeeper_talk",
      "type": "INTERACT",
      "bounds": {"x": 30, "y": 40, "w": 16, "h": 16},
      "npc": "NPC_INNKEEPER",
      "dialog": "DT_INNKEEPER_MAIN"
    }
  ],
  "hazards": [
    {
      "id": "lava_pit",
      "type": "HAZARD",
      "bounds": {"x": 100, "y": 50, "w": 32, "h": 32},
      "damage": 50,
      "damage_type": "fire",
      "interval": 1.0
    }
  ]
}
```

## Entity Collision

### Character Hitbox

```json
{
  "entity": "player",
  "collision": {
    "type": "FULL",
    "shape": "rectangle",
    "width": 12,
    "height": 8,
    "offset_x": 2,
    "offset_y": 20
  },
  "layer": 5,
  "pushable": false,
  "solid": true
}
```

### Collision Response

| Entity A | Entity B | Response |
|----------|----------|----------|
| Player | Wall | Stop movement |
| Player | NPC | Stop + face NPC |
| Player | Push Block | Push block |
| Enemy | Player | Start battle |
| Enemy | Enemy | Path around |
| Projectile | Wall | Destroy projectile |
| Projectile | Enemy | Damage enemy |

## Implementation Notes

### For 2D Engines (Godot, Unity 2D, etc.)

1. **Use tilemap collision** for static geometry
2. **Use collision objects** for dynamic entities
3. **Y-sort** based on bottom of sprite
4. **Height maps** can be separate tile layer

### Performance Tips

1. **Spatial hashing** for many entities
2. **Collision layers/masks** (most engines support)
3. **Culling** off-screen collision checks
4. **Static vs dynamic** body separation

### Collision Layer Bitmask

```
Bit 0: Ground (Layer 1-2)
Bit 1: Solid Objects (Layer 3-4)
Bit 2: Characters (Layer 5)
Bit 3: Projectiles
Bit 4: Zones/Triggers
Bit 5: Hazards
```

## Status: ☐ Not Started | ☐ In Progress | ☐ Complete

*Note: This is design specification. Implementation depends on your game engine.*
