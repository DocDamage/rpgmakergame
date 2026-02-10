# Visual Style Guide
## SNES Assets to Time Fantasy Integration

This guide ensures consistent visual style when using SNES reference assets with Time Fantasy tilesets.

---

## 🎨 COLOR PALETTE ANALYSIS

### Terranigma Palette:
```
Primary Colors:
- Stone Gray: #8B8680, #6B6660
- Royal Gold: #D4AF37, #B8941F
- Deep Red: #8B0000, #A52A2A (carpets)
- Dark Blue: #191970, #000080 (banners)
- Corruption Purple: #4B0082, #800080

Accent Colors:
- White Marble: #F5F5F5, #E8E8E8
- Wood Brown: #8B4513, #654321
- Water Blue: #4682B4, #5F9EA0
```

### Time Fantasy Palette:
```
Primary Colors:
- Grass Green: #7CB342, #558B2F
- Earth Brown: #795548, #5D4037
- Sky Blue: #29B6F6, #039BE5
- Stone Gray: #9E9E9E, #757575

Accent Colors:
- Highlight Yellow: #FFEB3B
- Magic Glow: #E040FB, #00E5FF
```

---

## 🔧 ADAPTATION GUIDELINES

### Palace Zone (Terranigma → Time Fantasy):

| Element | SNES Reference | TF Adaptation |
|---------|---------------|---------------|
| Throne Room | Red carpet, gold throne | Use GOLD PALACE tileset, add red carpet overlay |
| Stone Walls | Terranigma gray stone | Match to TF stone_gray variants |
| Gold Trim | Bright gold accents | Use TF gold_decorative tiles |
| Corruption | Purple/black vines | Add TF void/decay overlays |
| Banners | Dark blue hanging | Use TF flag banners, recolor blue |

**Key Adaptation:**
- Terranigma has MORE detail than Time Fantasy
- Simplify Terranigma backgrounds by reducing detail 20-30%
- Maintain the RED CARPET as focal point (iconic)

---

### Capital Ruins (Terranigma → Time Fantasy):

| Element | SNES Reference | TF Adaptation |
|---------|---------------|---------------|
| Ruined Walls | Broken stone sections | Use TF stone_damaged tiles |
| Rubble/Debris | Piles of rocks | Add TF debris overlay tiles |
| Dark Vines | Purple corruption | Use TF void_vines |
| Lighting | Dim, moody | Darken TF palette by 15% |
| Floor | Cracked stone | Use TF stone_cracked variants |

**Key Adaptation:**
- Desaturate Terranigma colors 10-15%
- Add more gray/brown for decayed feel
- Corruption effects from TF void tileset

---

### Tide Coast (Terranigma → Time Fantasy):

| Element | SNES Reference | TF Adaptation |
|---------|---------------|---------------|
| Water | Deep blue | Use TF water tiles, match hue |
| Docks | Wood planks | Use TF wood_dock tiles |
| Ships | Detailed vessels | Simplify to TF style, keep shape |
| Stone Piers | Gray blocks | Use TF stone_water_edge |

**Key Adaptation:**
- Water animation: Use TF water_animated
- Ship scale: Reduce detail to match TF character size

---

### Aetherreach (BoF2 + Albert Odyssey → Time Fantasy):

| Element | SNES Reference | TF Adaptation |
|---------|---------------|---------------|
| Cloud Ground | White fluffy | Use TF cloud tiles if available, or create |
| Floating Islands | Rock on clouds | Combine TF stone + white overlay |
| Sky Background | Light blue | TF sky_blue or gradient |
| Buildings | Cloud architecture | Use TF white stone, add cloud base |

**Key Adaptation:**
- This requires MOST adaptation - no direct TF equivalent
- Create cloud tileset based on references
- Use white/gray stone for buildings

---

## 📐 SCALE REFERENCE

### Character to Environment Ratio:

**SNES Standard (Terranigma):**
- Character: ~32x32 pixels
- Door: ~32x48 pixels
- Room: ~320x240 pixels

**Time Fantasy Standard:**
- Character: ~32x32 pixels ✅ MATCH
- Door: ~32x48 pixels ✅ MATCH
- Tile size: 32x32 pixels ✅ MATCH

**Verdict:** SNES and Time Fantasy use SAME scale! ✅

---

## 🎭 BATTLE BACKGROUND STYLE

### For Palace Throne Room:

```
Base Layer (TF):
- Floor: tf_palace_floor.png
- Walls: tf_palace_wall.png

Overlay (SNES Reference):
- Throne: Extract from Terranigma, place center-right
- Carpet: Red path leading to throne
- Columns: Use TF column sprites

Effects:
- Add corruption overlay (purple smoke)
- Throne glows with dark light
- Flickering torches (animated)
```

### For Capital Ruins:

```
Base Layer (TF):
- Floor: tf_stone_cracked.png
- Walls: tf_stone_damaged.png

Overlay (SNES Reference):
- Rubble piles
- Broken furniture
- Dark vines

Effects:
- Dust particles (animated)
- Dark fog overlay
- Occasional lightning flash
```

---

## 🖼️ BACKGROUND RESOLUTION GUIDE

### Recommended Sizes:

| Usage | Resolution | Aspect | Format |
|-------|-----------|--------|--------|
| Battle Background (SD) | 640x360 | 16:9 | PNG |
| Battle Background (HD) | 800x450 | 16:9 | PNG |
| Battle Background (FHD) | 960x540 | 16:9 | PNG |
| UI Backdrop | 320x180 | 16:9 | PNG |
| Map Preview | 400x300 | 4:3 | PNG |

### Extraction Workflow:

1. **Source:** Open SNES asset in editor
2. **Crop:** Select region using coordinates from extraction guide
3. **Resize:** Scale to target resolution (maintain aspect ratio)
4. **Filter:** Use "Nearest Neighbor" to keep pixel art crisp
5. **Adjust:** Match brightness/contrast to TF tilesets
6. **Export:** PNG with transparency where needed

---

## 🎨 COLOR MATCHING WORKFLOW

### Using GIMP/Photoshop:

```
Step 1: Open TF tileset for reference
Step 2: Open SNES background
Step 3: Create color adjustment layer
Step 4: Sample colors from TF reference
Step 5: Apply to SNES image:
  - Image → Adjustments → Match Color
  - Or manual Hue/Saturation adjustment
Step 6: Fine-tune until visually consistent
Step 7: Save as separate file
```

### Quick Adjustments:

| Zone | Hue Shift | Saturation | Brightness |
|------|-----------|------------|------------|
| Palace | 0 | -10% | -5% |
| Capital Ruins | 0 | -20% | -15% |
| Tide | +5 (blue) | +10% | 0 |
| Aetherreach | +10 (purple) | -5% | +10% |
| Uplands | -5 (brown) | -10% | -5% |

---

## 🔲 TRANSPARENCY GUIDE

### When to Use Transparency:

✅ **USE ALPHA:**
- Foreground elements (pillars, furniture)
- Character overlays
- Effect layers
- UI elements

❌ **NO ALPHA (Solid):**
- Floor textures
- Wall backgrounds
- Sky/background layers
- Base environment

### Implementation:
```
Layer Stack (bottom to top):
1. Sky/Background (solid)
2. Far wall (solid)
3. Floor (solid)
4. Mid-ground elements (solid)
5. Near elements (transparency optional)
6. Effects overlay (transparency)
7. Foreground framing (transparency)
```

---

## 🎯 QUALITY CHECKLIST

Before finalizing a battle background:

- [ ] Resolution matches target (640x360 or 800x450)
- [ ] Colors consistent with TF tilesets
- [ ] Pixel art is crisp (no blurring)
- [ ] Focal point clearly visible
- [ ] No visual clutter in character area
- [ ] Corruption/theme effects added
- [ ] Tested with character sprites overlaid
- [ ] File size optimized (< 500KB ideal)

---

## 📁 FILE NAMING CONVENTION

```
[zone]_[location]_[variant]_[size].png

Examples:
palace_throne_main_640.png
capital_ruins_shop_a_640.png
tide_harbor_day_800.png
aetherreach_plaza_640.png
```

---

## ✨ SPECIAL EFFECTS GUIDE

### Corruption Effect (Purple/Black):
```
Tool: Particle system or animated overlay
Color: #4B0082, #800080, #000000
Opacity: 20-40%
Animation: Slow drift upward
Placement: Corners, edges, behind throne
```

### Torch Light (Flickering):
```
Tool: Light overlay with animation
Color: #FF8C00, #FFA500
Opacity: Pulsing 30-60%
Animation: 0.1-0.3 second flicker
Placement: Wall sconces
```

### Water Reflection:
```
Tool: Shader or animated overlay
Color: #4682B4 with opacity
Animation: Gentle wave distortion
Placement: Floor in Tide zone
```

---

## 🎮 ENGINE IMPLEMENTATION NOTES

### RPG Maker MV/MZ:
- Battlebacks go in `img/battlebacks1/` and `battlebacks2/`
- Use 1000x740 for full-screen battlebacks
- Parallax layers for animated effects

### Godot:
- Use Sprite nodes for backgrounds
- ParallaxBackground for layered effects
- ShaderMaterial for water/corruption effects

### Unity:
- SpriteRenderer for backgrounds
- Canvas layers for UI separation
- ParticleSystem for corruption effects

---

*"Good art direction isn't about the assets you have - it's about how consistently you use them."*
