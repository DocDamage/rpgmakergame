# Tileset Replacement Guide
## Mapping Your Source Spritesheets to RPG Maker Runtime

---

## Overview

You have **22 themed tileset source spritesheets** in `assets/sprites/tilesets/` that can replace the **17 placeholder tilesets** in `img/tilesets/`.

### Source Assets Available:

### Dimensions Analysis:
| Theme | Source File | Dimensions | Type |
|-------|-------------|------------|------|
| Ashveil Stone | tileset_ashveilstone_source_primary.png | 784x832 | Multi-sheet composite |
| Capital Ruins | tileset_capitalruins_source_primary.png | 784x832 | Multi-sheet composite |
| Chrono Pier | tileset_chronopier_source_primary.png | 1440x848 | Wide composite |
| Dustbelt | tileset_dustbelt_source_primary.png | 608x720 | Medium sheet |
| Obsidian Industrial | tileset_obsidianindustrial_source_primary.png | 1440x848 | Wide composite |
| Uplands | tileset_uplands_source_primary.png | 784x832 | Multi-sheet composite |
| Remnant Glitch | tileset_remnantglitch_source_primary.png | 784x704 | Large sheet |
| Interior - Generic | tileset_interior_generic_source_primary.png | 768x768 | **RPG Maker Ready!** |
| Tower | tileset_tower_source_primary.png | 800x464 | Medium sheet |
| Aetherreach | tileset_aetherreach_source_primary.png | 720x448 | Medium sheet |
| Prism Highland | tileset_prismhighland_source_primary.png | 720x448 | Medium sheet |
| Tide Coast | tileset_tidecoast_source_primary.png | 576x416 | Small sheet |
| Ember Basalt | tileset_emberbasalt_source_primary.png | 640x336 | Small sheet |
| Mire Stilts | tileset_mirestilts_source_primary.png | 352x336 | Small sheet |
| Void Nexus | tileset_voidnexus_source_primary.png | 464x336 | Small sheet |
| Orion Overworld | tileset_orionoverworld_source_primary.png | 256x256 | Small sheet |
| Palace | tileset_palace_source_primary.png | 512x1024 | Tall sheet |
| Frost Citadel | tileset_frostcitadel_source_primary.png | 240x336 | Small sheet |
| Interior - Dim | tileset_interior_dim_source_primary.png | 1728x1536 | Very large sheet |
| Interior - Forge | tileset_interior_forge_source_primary.png | 384x144 | Small sheet |
| Interior - Grand | tileset_interior_grand_source_primary.png | 336x576 | Small sheet |

**Key Finding:** `tileset_interior_generic_source_primary.png` (768x768) is already RPG Maker MV/MZ B-sheet format!
| Theme | Source File | README |
|-------|-------------|--------|
| Aetherreach | tileset_aetherreach_source_primary.png | ✅ |
| Ashveil Stone | tileset_ashveilstone_source_primary.png | ✅ |
| Capital Ruins | tileset_capitalruins_source_primary.png | ✅ |
| Chrono Pier | tileset_chronopier_source_primary.png | ✅ |
| Dustbelt | tileset_dustbelt_source_primary.png | ✅ |
| Ember Basalt | tileset_emberbasalt_source_primary.png | ✅ |
| Frost Citadel | tileset_frostcitadel_source_primary.png | ✅ |
| Mire Stilts | tileset_mirestilts_source_primary.png | ✅ |
| Obsidian Industrial | tileset_obsidianindustrial_source_primary.png | ✅ |
| Orion Overworld | tileset_orionoverworld_source_primary.png | ✅ |
| Palace | tileset_palace_source_primary.png | ✅ |
| Prism Highland | tileset_prismhighland_source_primary.png | ✅ |
| Remnant Glitch | tileset_remnantglitch_source_primary.png | ✅ |
| Tide Coast | tileset_tidecoast_source_primary.png | ✅ |
| Tower | tileset_tower_source_primary.png | ✅ |
| Uplands | tileset_uplands_source_primary.png | ✅ |
| Void Nexus | tileset_voidnexus_source_primary.png | ✅ |
| Interior - Dim | tileset_interior_dim_source_primary.png | ✅ |
| Interior - Forge | tileset_interior_forge_source_primary.png | ✅ |
| Interior - Generic | tileset_interior_generic_source_primary.png | ✅ |
| Interior - Grand | tileset_interior_grand_source_primary.png | ✅ |

---

## Replacement Strategy

### Option 1: Biome-Specific Mapping (Recommended)

Based on your actual source dimensions, here's the optimal mapping:

#### Dungeon Tilesets (6 files)
| Runtime File | Best Source | Rationale |
|--------------|-------------|-----------|
| Dungeon_A1.png | tileset_ashveilstone_source_primary.png [crop 0,0-768,576] | Water/lava animations |
| Dungeon_A2.png | tileset_ashveilstone_source_primary.png [crop 0,576-768,1152] | Dungeon floors |
| Dungeon_A4.png | tileset_capitalruins_source_primary.png [crop 0,576-768,1152] | Stone walls |
| Dungeon_A5.png | tileset_capitalruins_source_primary.png [crop 0,0-768,576] | Capital details |
| Dungeon_B.png | tileset_interior_generic_source_primary.png | **EXACT FIT** - Objects |
| Dungeon_C.png | tileset_voidnexus_source_primary.png | Void decorations |

#### Outside Tilesets (7 files)
| Runtime File | Best Source | Rationale |
|--------------|-------------|-----------|
| Outside_A1.png | tileset_dustbelt_source_primary.png [resize 768x576] | Desert water |
| Outside_A2.png | tileset_dustbelt_source_primary.png [resize 768x576] | Desert ground |
| Outside_A3.png | tileset_uplands_source_primary.png [crop 0,0-768,576] | Building tops |
| Outside_A4.png | tileset_emberbasalt_source_primary.png [tile 768x768] | Volcanic walls |
| Outside_A5.png | tileset_prismhighland_source_primary.png [resize 768x768] | Crystal details |
| Outside_B.png | tileset_mirestilts_source_primary.png [tile 768x768] | Swamp objects |
| Outside_C.png | tileset_tidecoast_source_primary.png [resize 768x768] | Coastal deco |

#### World Tilesets (4 files)
| Runtime File | Best Source | Rationale |
|--------------|-------------|-----------|
| World_A1.png | tileset_orionoverworld_source_primary.png [tile 768x576] | Ocean tiles |
| World_A2.png | tileset_orionoverworld_source_primary.png [tile 768x576] | Terrain |
| World_B.png | tileset_tower_source_primary.png [crop 0,0-768,768] | Landmarks |
| World_C.png | tileset_palace_source_primary.png [crop 0,0-768,768] | Special features |

Replace each placeholder with the most appropriate themed tileset:

#### Dungeon Tilesets (6 files)
| Runtime File | Recommended Source | Biome |
|--------------|-------------------|-------|
| Dungeon_A1.png | tileset_ashveilstone_source_primary.png | Ruins (water/animated) |
| Dungeon_A2.png | tileset_ashveilstone_source_primary.png | Ruins (ground) |
| Dungeon_A4.png | tileset_obsidianindustrial_source_primary.png | Quarry (walls) |
| Dungeon_A5.png | tileset_capitalruins_source_primary.png | Capital (details) |
| Dungeon_B.png | tileset_voidnexus_source_primary.png | Void (objects) |
| Dungeon_C.png | tileset_frostcitadel_source_primary.png | Ice (decorations) |

#### Outside Tilesets (6 files)
| Runtime File | Recommended Source | Biome |
|--------------|-------------------|-------|
| Outside_A1.png | tileset_dustbelt_source_primary.png | Desert (water/animated) |
| Outside_A2.png | tileset_dustbelt_source_primary.png | Desert (ground) |
| Outside_A3.png | tileset_uplands_source_primary.png | Uplands (buildings) |
| Outside_A4.png | tileset_emberbasalt_source_primary.png | Volcanic (walls) |
| Outside_A5.png | tileset_prismhighland_source_primary.png | Crystal (details) |
| Outside_B.png | tileset_mirestilts_source_primary.png | Swamp (objects) |
| Outside_C.png | tileset_tidecoast_source_primary.png | Coastal (decorations) |

#### World Tilesets (4 files)
| Runtime File | Recommended Source | Purpose |
|--------------|-------------------|---------|
| World_A1.png | tileset_orionoverworld_source_primary.png | Ocean (animated) |
| World_A2.png | tileset_orionoverworld_source_primary.png | Terrain (biomes) |
| World_B.png | tileset_orionoverworld_source_primary.png | Landmarks |
| World_C.png | tileset_orionoverworld_source_primary.png | Details |

### Option 2: Universal Single-Source

If your spritesheets are comprehensive enough, you could use one source for multiple slots:
- **Orion Overworld** → All World_A1-C.png
- **Ashveil Stone** → All Dungeon_A1-C.png  
- **Dustbelt** → All Outside_A1-C.png

---

## RPG Maker MV/MZ Tileset Specifications

### Required Dimensions:
| Sheet Type | Dimensions | Purpose |
|------------|------------|---------|
| A1 (Animated) | 768x576 | Water, lava, waterfalls |
| A2 (Ground) | 768x576 | Ground tiles, grass, dirt |
| A3 (Building) | 768x768 | Rooftops, walls |
| A4 (Wall) | 768x768 | Cliff faces, walls |
| A5 (Normal) | 768x768 | Details, objects |
| B (Normal) | 768x768 | Upper layer objects |
| C (Normal) | 768x768 | Upper layer decorations |

### Your Placeholder Files:
| File | Type | Current Size | Target Size |
|------|------|--------------|-------------|
| Dungeon_A1.png | A1 | 10 KB | Full spritesheet |
| Dungeon_A2.png | A2 | 10 KB | Full spritesheet |
| Dungeon_A4.png | A4 | 11 KB | Full spritesheet |
| Dungeon_A5.png | A5 | 11 KB | Full spritesheet |
| Dungeon_B.png | B | 11 KB | Full spritesheet |
| Dungeon_C.png | C | 11 KB | Full spritesheet |
| Outside_A1.png | A1 | 10 KB | Full spritesheet |
| Outside_A2.png | A2 | 10 KB | Full spritesheet |
| Outside_A3.png | A3 | 11 KB | Full spritesheet |
| Outside_A4.png | A4 | 11 KB | Full spritesheet |
| Outside_A5.png | A5 | 11 KB | Full spritesheet |
| Outside_B.png | B | 11 KB | Full spritesheet |
| Outside_C.png | C | 11 KB | Full spritesheet |
| World_A1.png | A1 | 10 KB | Full spritesheet |
| World_A2.png | A2 | 10 KB | Full spritesheet |
| World_B.png | B | 11 KB | Full spritesheet |
| World_C.png | C | 11 KB | Full spritesheet |

---

## Extraction Workflow

### Understanding Your Source Formats

Based on dimension analysis:

**Ready to Use (Minimal Processing):**
- `tileset_interior_generic_source_primary.png` (768x768) → Use directly as B/C sheet

**Composite Sheets (Need Cropping):**
- Ashveil Stone, Capital Ruins, Uplands (784x832) → Likely A1+A2+B combined
- Chrono Pier, Obsidian Industrial (1440x848) → Wide composites with multiple sections
- Remnant Glitch (784x704) → Multi-section sheet

**Single-Theme Sheets (May need tiling):**
- Tower, Aetherreach, Prism Highland, Dustbelt → May need duplication/tile arrangement
- Small sheets (Frost, Mire, Void, Ember) → Best for detail/B sheets

### Specific Extraction Recommendations

#### Large Composites (784x832) - Ashveil, Capital, Uplands
These appear to contain multiple RPG Maker sheet sections stacked:

| Section | Coordinates | Target File |
|---------|-------------|-------------|
| Top 576px | 0,0 to 767,575 | A1 or A2 (768x576) |
| Middle 576px | 0,576 to 767,1151 | A2 or A4 (768x576) |
| Bottom 768px | 0,1152 to 767,1919 | B or C (768x768) |

#### Wide Composites (1440x848) - Chrono, Obsidian
These have horizontal arrangement:

| Section | Coordinates | Target File |
|---------|-------------|-------------|
| Left 768px | 0,0 to 767,575 | A1/A2 (left half) |
| Right 768px | 768,0 to 1535,575 | A2 continuation |
| Lower section | 0,576 to 767,1151 | B/C sheet |

#### Ready-Made Sheet (768x768) - Interior Generic
```bash
# Direct copy - already RPG Maker format!
copy assets\sprites\tilesets\tileset_interior_generic_source_primary.png img\tilesets\Dungeon_B.png
```

### Extraction Tools

**Option A: Python/PIL Script (Automated)**

Save this as `tools/extract_tilesets.py`:

```python
"""
Tileset Extraction Tool for Chroma's Edge
Extracts sections from composite spritesheets into RPG Maker format
"""

from PIL import Image
import os

# Configuration: Map target files to source crops
EXTRACTION_MAP = [
    # (target_file, source_file, crop_box)
    ("Dungeon_A1.png", "tileset_ashveilstone_source_primary.png", (0, 0, 768, 576)),
    ("Dungeon_A2.png", "tileset_ashveilstone_source_primary.png", (0, 576, 768, 1152)),
    ("Dungeon_A4.png", "tileset_capitalruins_source_primary.png", (0, 576, 768, 1152)),
    ("Dungeon_A5.png", "tileset_capitalruins_source_primary.png", (0, 0, 768, 576)),
    ("Dungeon_C.png", "tileset_voidnexus_source_primary.png", (0, 0, 464, 336)),
    
    ("Outside_A3.png", "tileset_uplands_source_primary.png", (0, 0, 768, 576)),
    ("Outside_A4.png", "tileset_emberbasalt_source_primary.png", (0, 0, 640, 336)),
    ("Outside_A5.png", "tileset_prismhighland_source_primary.png", (0, 0, 720, 448)),
    ("Outside_B.png", "tileset_mirestilts_source_primary.png", (0, 0, 352, 336)),
    ("Outside_C.png", "tileset_tidecoast_source_primary.png", (0, 0, 576, 416)),
    
    ("World_B.png", "tileset_tower_source_primary.png", (0, 0, 768, 464)),
    ("World_C.png", "tileset_palace_source_primary.png", (0, 0, 512, 768)),
]

# Direct copies (already correct size)
DIRECT_COPIES = [
    ("Dungeon_B.png", "tileset_interior_generic_source_primary.png"),
]

SOURCE_DIR = "assets/sprites/tilesets"
TARGET_DIR = "img/tilesets"

def extract_tilesets():
    os.makedirs(TARGET_DIR, exist_ok=True)
    
    # Process extractions
    for target, source, crop_box in EXTRACTION_MAP:
        source_path = os.path.join(SOURCE_DIR, source)
        target_path = os.path.join(TARGET_DIR, target)
        
        if not os.path.exists(source_path):
            print(f"❌ Source not found: {source}")
            continue
            
        try:
            with Image.open(source_path) as img:
                # Extract crop region
                cropped = img.crop(crop_box)
                
                # Resize to target dimensions if needed
                target_size = get_target_size(target)
                if cropped.size != target_size:
                    cropped = cropped.resize(target_size, Image.Resampling.LANCZOS)
                
                cropped.save(target_path, "PNG")
                print(f"✅ Created: {target} ({cropped.size[0]}x{cropped.size[1]})")
        except Exception as e:
            print(f"❌ Error processing {target}: {e}")
    
    # Process direct copies
    for target, source in DIRECT_COPIES:
        source_path = os.path.join(SOURCE_DIR, source)
        target_path = os.path.join(TARGET_DIR, target)
        
        if os.path.exists(source_path):
            with Image.open(source_path) as img:
                img.save(target_path, "PNG")
            print(f"✅ Copied: {target}")
        else:
            print(f"❌ Source not found: {source}")

def get_target_size(filename):
    """Return target dimensions based on RPG Maker sheet type"""
    if "_A1" in filename or "_A2" in filename:
        return (768, 576)
    elif "_A3" in filename or "_A4" in filename or "_A5" in filename:
        return (768, 768)
    elif "_B" in filename or "_C" in filename:
        return (768, 768)
    return (768, 768)

if __name__ == "__main__":
    print("Extracting tilesets...")
    extract_tilesets()
    print("\nDone! Run 'python tools/run_project_audit_gate.py' to validate.")
```

Run with:
```bash
python tools/extract_tilesets.py
```

**Option B: Image Editor (Manual)**

**Option A: Python/PIL Script (Automated)**
```python
from PIL import Image

# Example: Extract A1 from Ashveil Stone
source = Image.open('assets/sprites/tilesets/tileset_ashveilstone_source_primary.png')
a1_section = source.crop((0, 0, 768, 576))
a1_section.save('img/tilesets/Dungeon_A1.png')
```

**Option B: Image Editor (Manual)**
1. Open source in GIMP/Photoshop
2. Set canvas size to target (768x576 for A1/A2, 768x768 for B/C)
3. Copy appropriate section
4. Save as PNG to img/tilesets/

**Option C: RPG Maker Resource Manager**
1. Import source into RPG Maker
2. Use built-in tileset editor to arrange
3. Export arranged tileset

### Method 1: Copy Direct (If Already Formatted)
If your source spritesheets are already RPG Maker MV/MZ formatted:

```bash
# Example: Replace Dungeon_A1 with Ashveil Stone
copy assets\sprites\tilesets\tileset_ashveilstone_source_primary.png img\tilesets\Dungeon_A1.png
```

### Method 2: Extract by Coordinates (If Composite Sheet)
If your source contains multiple tilesets in one sheet, extract by pixel coordinates:

| Target File | Source | Extraction Coords | Size |
|-------------|--------|-------------------|------|
| Dungeon_A1.png | tileset_ashveilstone_source_primary.png | 0,0 to 767,575 | 768x576 |
| Dungeon_A2.png | tileset_ashveilstone_source_primary.png | 0,576 to 767,1151 | 768x576 |
| Dungeon_B.png | tileset_ashveilstone_source_primary.png | 768,0 to 1535,767 | 768x768 |

### Method 3: Use RPG Maker Editor
1. Open RPG Maker MZ
2. Go to **Tools > Resource Manager**
3. Navigate to **img/tilesets/**
4. Import your source spritesheets
5. Apply to appropriate tileset slots

---

## Current Status

### ✅ Completed (13/17)
| File | Source Used | Size |
|------|-------------|------|
| Dungeon_A1.png | Ashveil Stone (crop) | 98 KB |
| Dungeon_A2.png | Ashveil Stone (crop) | 46 KB |
| Dungeon_A4.png | Capital Ruins (crop) | 164 KB |
| Dungeon_A5.png | Capital Ruins (crop) | 381 KB |
| Dungeon_B.png | Interior Generic (copy) | 35 KB |
| Dungeon_C.png | Void Nexus (crop) | 560 KB |
| Outside_A3.png | Uplands (crop) | 381 KB |
| Outside_A4.png | Ember Basalt (resize) | 544 KB |
| Outside_A5.png | Prism Highland (resize) | 441 KB |
| Outside_B.png | Mire Stilts (resize) | 688 KB |
| Outside_C.png | Tide Coast (resize) | 380 KB |
| World_B.png | Tower (crop) | 363 KB |
| World_C.png | Palace (crop) | 50 KB |

### ⚠️ Remaining Placeholders (4/17)
| File | Type | Current Size | Recommended Source |
|------|------|--------------|-------------------|
| Outside_A1.png | A1 Animated | 10 KB | Dustbelt (water/rivers) |
| Outside_A2.png | A2 Ground | 10 KB | Dustbelt (desert ground) |
| World_A1.png | A1 Animated | 10 KB | Orion Overworld (ocean) |
| World_A2.png | A2 Ground | 10 KB | Orion Overworld (terrain) |

### Quick Fix for Remaining 4

Add these to the extraction script:

```python
# For the remaining placeholders, tile/resize smaller sources
("Outside_A1.png", "tileset_dustbelt_source_primary.png", (0, 0, 608, 576)),  # Crop then tile
("Outside_A2.png", "tileset_dustbelt_source_primary.png", (0, 0, 608, 720)),  # Resize to 768x576
("World_A1.png", "tileset_orionoverworld_source_primary.png", (0, 0, 256, 256)),  # Tile pattern
("World_A2.png", "tileset_orionoverworld_source_primary.png", (0, 0, 256, 256)),  # Tile pattern
```

Or manually in an image editor:
1. Open the source (Dustbelt = 608x720, Orion = 256x256)
2. For A1/A2 (768x576): Resize source to fit
3. For animated tiles: Ensure autotile patterns align

## Recommended Priority Order

### Phase 1: World/Overworld (4 files)
1. World_A2.png - Most visible (terrain)
2. World_A1.png - Ocean animation
3. World_B.png - Landmarks
4. World_C.png - Details

### Phase 2: Outside/Field (7 files)
5. Outside_A2.png - Ground (most common)
6. Outside_A1.png - Water animation
7. Outside_B.png - Objects
8. Outside_A4.png - Cliffs/walls
9. Outside_A3.png - Buildings
10. Outside_A5.png - Details
11. Outside_C.png - Decorations

### Phase 3: Dungeon (6 files)
12. Dungeon_A2.png - Dungeon floors
13. Dungeon_A1.png - Water/lava
14. Dungeon_A4.png - Walls
15. Dungeon_B.png - Objects
16. Dungeon_A5.png - Details
17. Dungeon_C.png - Decorations

---

## Validation After Replacement

After replacing tilesets, run:

```bash
python tools/run_project_audit_gate.py --scope all
```

This validates:
- All tileset references resolve
- Image dimensions are correct
- No corruption in transfer

---

## Interior Tilesets (Bonus)

You also have 4 interior tilesets available for town interiors:

| Source File | Use For |
|-------------|---------|
| tileset_interior_generic_source_primary.png | Standard houses |
| tileset_interior_forge_source_primary.png | Smith/forge interiors |
| tileset_interior_grand_source_primary.png | Halls/sanctuaries |
| tileset_interior_dim_source_primary.png | Secrets/caves |

These can be imported as custom tilesets in RPG Maker for interior maps.

---

## Quick Reference: File Mapping

```
img/tilesets/                    assets/sprites/tilesets/
────────────────────────────────────────────────────────────
Dungeon_A1.png      ← tileset_ashveilstone_source_primary.png [crop A1]
Dungeon_A2.png      ← tileset_ashveilstone_source_primary.png [crop A2]
Dungeon_A4.png      ← tileset_obsidianindustrial_source_primary.png [crop A4]
Dungeon_A5.png      ← tileset_capitalruins_source_primary.png [crop A5]
Dungeon_B.png       ← tileset_voidnexus_source_primary.png [crop B]
Dungeon_C.png       ← tileset_frostcitadel_source_primary.png [crop C]

Outside_A1.png      ← tileset_dustbelt_source_primary.png [crop A1]
Outside_A2.png      ← tileset_dustbelt_source_primary.png [crop A2]
Outside_A3.png      ← tileset_uplands_source_primary.png [crop A3]
Outside_A4.png      ← tileset_emberbasalt_source_primary.png [crop A4]
Outside_A5.png      ← tileset_prismhighland_source_primary.png [crop A5]
Outside_B.png       ← tileset_mirestilts_source_primary.png [crop B]
Outside_C.png       ← tileset_tidecoast_source_primary.png [crop C]

World_A1.png        ← tileset_orionoverworld_source_primary.png [crop A1]
World_A2.png        ← tileset_orionoverworld_source_primary.png [crop A2]
World_B.png         ← tileset_orionoverworld_source_primary.png [crop B]
World_C.png         ← tileset_orionoverworld_source_primary.png [crop C]
```

---

## Next Steps

1. **Check Source Dimensions**: Verify your source spritesheet dimensions
2. **Choose Mapping Strategy**: Biome-specific or universal
3. **Extract/Copy**: Use appropriate method based on source format
4. **Validate**: Run audit gate to confirm
5. **Test In-Game**: Check maps render correctly

---

*Guide Generated: 2026-02-11*
*Source Assets: 22 themed tilesets*
*Target Replacements: 17 placeholder slots*
