# Placeholder Asset Guide

## Philosophy

**Ship it first, polish later.** Use colored rectangles and silhouettes to make the game playable immediately. Art passes can happen in parallel.

## Placeholder Standards

### Color Coding

| Asset Type | Color | Hex | Notes |
|------------|-------|-----|-------|
| **Player Characters** | Blue | #3498db | Distinct from enemies |
| **NPCs (Friendly)** | Green | #2ecc71 | Safe to approach |
| **NPCs (Hostile)** | Red | #e74c3c | Will attack |
| **NPCs (Neutral)** | Yellow | #f1c40f | Neutral stance |
| **Enemies (Common)** | Dark Red | #c0392b | Combat targets |
| **Enemies (Elite)** | Purple | #9b59b6 | Stronger threat |
| **Bosses** | Black/Red | #2c3e50 | Major threat |
| **Items/Collectibles** | Gold | #f39c12 | Loot |
| **Interactive Objects** | Cyan | #00bcd4 | Can interact |
| **Terrain (Walkable)** | Brown variants | #8d6e63 | Ground |
| **Terrain (Blocked)** | Gray | #7f8c8d | Walls/cliffs |
| **Water** | Blue | #2980b9 | Swimming |
| **Hazards** | Orange | #e67e22 | Damaging |

### Size Standards

Use exact final dimensions so placeholders drop in:

| Asset Type | Size | Placeholder Shape |
|------------|------|-------------------|
| Overworld Characters | 16x24 | Rectangle with triangle "head" |
| NPCs | 16x24 | Rectangle with circle "head" |
| Enemies (Overworld) | 16x16 to 24x24 | Square with spike indicators |
| Enemies (Battle) | 48x48 | Larger square with details |
| Bosses (Battle) | 128x128+ | Large shape with "boss" indicator |
| Portraits | 64x64 or 96x96 | Circle with expression color |
| Tileset Tiles | 16x16 | Solid color blocks |
| UI Icons | 16x16, 32x32 | Simple geometric shapes |

### Naming Placeholders

Add `_PH` suffix until replaced:
```
spr_kade_walk_N_PH.png
spr_enemy_dust_skirmisher_PH.png
tileset_dustbelt_PH.png
```

When final art is ready, remove `_PH` suffix.

## Quick Placeholder Generator (Python)

```python
#!/usr/bin/env python3
"""Generate placeholder sprites."""
from PIL import Image

PALETTE = {
    'player': (52, 152, 219),
    'npc_friendly': (46, 204, 113),
    'npc_hostile': (231, 76, 60),
    'enemy': (192, 57, 43),
    'boss': (44, 62, 80),
    'item': (243, 156, 18),
    'interactive': (0, 188, 212),
    'ground': (141, 110, 99),
    'wall': (127, 140, 141),
    'water': (41, 128, 185),
    'hazard': (230, 126, 34),
}

def create_placeholder(name, size, color, output_dir="assets/placeholders"):
    """Create a simple colored rectangle placeholder."""
    img = Image.new('RGBA', size, (*color, 255))
    
    # Add border
    from PIL import ImageDraw
    draw = ImageDraw.Draw(img)
    draw.rectangle([0, 0, size[0]-1, size[1]-1], outline=(0, 0, 0, 128))
    
    # Add text label
    # (Optional - requires font)
    
    filepath = f"{output_dir}/{name}_PH.png"
    img.save(filepath)
    print(f"Created: {filepath}")
    return filepath

# Generate character placeholders
create_placeholder("spr_kade_walk_N", (16, 24), PALETTE['player'])
create_placeholder("spr_enemy_dust_skirmisher", (16, 16), PALETTE['enemy'])
create_placeholder("spr_boss_bloom", (128, 128), PALETTE['boss'])
```

## Game-Ready Checklist

Before an asset moves from placeholder to final:

- [ ] Correct dimensions
- [ ] Proper pivot point (bottom-center for characters)
- [ ] Transparent background (PNG)
- [ ] Follows naming convention
- [ ] Placed in correct directory
- [ ] Removed `_PH` suffix
- [ ] Validator script passes

## Silhouette Guide

For quick recognition, add simple silhouette features:

**Characters:**
- Triangle on top = head direction
- Small rectangle = weapon/item
- Stripes = clothing detail

**Enemies:**
- Spikes = dangerous/hostile
- Rounded = passive/docile
- Wings = flying
- Large = boss/elite

**Objects:**
- Chest: Rectangle with "V" top
- Door: Rectangle with gap
- Sign: Small rectangle on stick

## Priority Order for Final Art

1. **Player character** (Kade) - Most visible
2. **First dungeon** (D1) - Tutorial/first impression
3. **First town** (Dusthaven) - Hub time
4. **First 3 enemies** - Combat variety
5. **UI essentials** - Always on screen
6. **Remaining characters** - Party variety
7. **Remaining dungeons** - Content progression

## When to Replace Placeholders

Replace when:
- Player will see it for >10 seconds
- It's the focus of attention
- It appears in a cutscene
- The team has bandwidth

Keep placeholders when:
- It's background detail
- It's temporary/one-time
- Final art is in progress
- Time is better spent elsewhere
