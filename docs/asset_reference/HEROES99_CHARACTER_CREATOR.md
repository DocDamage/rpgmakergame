# Heroes99 v1.2 - Character Creator Pack
## Custom Protagonist Asset Guide

**Location:** `img/characters/protagonists/heroes99/`  
**Total Files:** 915 assets  
**Type:** Layer-based character generator

---

## 📦 PACKAGE CONTENTS

### Overview
Heroes99 is a modular character creator system that allows you to build custom protagonists by combining:
- **Body base** (skin tones)
- **Face** (expressions/features)
- **Hair** (male/female styles, 8 colors each)
- **Clothing** (17 outfit types, 8 colors each)
- **Weapons** (5 weapon types, multiple variations)

### Folder Structure
```
img/characters/protagonists/heroes99/
├── cloth/              ← 17 clothing sets (136 tops + 136 bottoms)
│   ├── cloth1/         ← (cloth1_c1_top.png ... cloth1_c8_top.png)
│   │   ├── cloth1_bot/ ← (cloth1_c1_bot.png ... cloth1_c8_bot.png)
│   │   └── cloth1_top/
│   ├── cloth2/
│   └── ... cloth17/
├── hair/               ← 23 hairstyles (8 colors each)
│   ├── f1/ - f9/       ← Female hair styles
│   ├── m1/ - m9/       ← Male hair styles
│   └── ...
├── face/               ← 7 face options
│   ├── face_c1.png
│   ├── face_c2.png
│   └── ... face_c7.png
├── skin/               ← 6 skin tones
│   ├── skin_c1.png
│   └── ... skin_c6.png
└── weapon/             ← 5 weapon sets
    ├── weapon1/
    ├── weapon2/
    └── ... weapon5/
```

---

## 🎨 ASSET BREAKDOWN

### Clothing Options (17 Sets)
| Set | Type | Colors | Components |
|-----|------|--------|------------|
| cloth1-17 | Various outfits | 8 colors each | Top + Bottom |

**Color Variations:** c1, c2, c3, c4, c5, c6, c7, c8

### Hair Options (23 Styles)
| Style ID | Gender | Colors |
|----------|--------|--------|
| f1-f9 | Female | 8 colors each |
| m1-m9 | Male | 8 colors each |
| (additional) | Unisex | 8 colors each |

### Face Options (7 Types)
| File | Description |
|------|-------------|
| face_c1.png | Face type 1 |
| face_c2.png | Face type 2 |
| ... | ... |
| face_c7.png | Face type 7 |

### Skin Tones (6 Options)
| File | Tone |
|------|------|
| skin_c1.png | Lightest |
| skin_c2.png | Light |
| skin_c3.png | Medium-light |
| skin_c4.png | Medium |
| skin_c5.png | Medium-dark |
| skin_c6.png | Darkest |

### Weapons (5 Types)
| Folder | Contents |
|--------|----------|
| weapon1/ | Swords |
| weapon2/ | Axes/Hammers |
| weapon3/ | Spears |
| weapon4/ | Staves |
| weapon5/ | Bows/Guns |

---

## 🎮 CREATING PROTAGONISTS

### For RPG Maker MZ

#### Option 1: Assemble in Image Editor (Recommended)
Use Photoshop, GIMP, or Aseprite to combine layers:

1. **Start with:** `skin/skin_c?.png`
2. **Add face:** `face/face_c?.png`
3. **Add hair:** `hair/f?/` or `hair/m?/` folder
4. **Add clothing:** `cloth/cloth?/` folder (top + bottom)
5. **Optional weapon:** `weapon/weapon?/`

#### Option 2: Use Frame Guide
Reference: `frameguide_v2.png`

Shows proper positioning of all elements for animation frames.

### Character Assembly Order (Bottom to Top)
```
1. Skin (base layer)
2. Face (expression)
3. Clothing bottom (pants/skirt)
4. Clothing top (shirt/armor)
5. Hair (top layer)
6. Weapon (optional, held layer)
```

---

## 👥 RECOMMENDED PROTAGONIST COMBINATIONS

### Classic JRPG Party (4 Characters)

#### Hero/Knight
```
Skin: skin_c3.png (medium)
Face: face_c1.png (heroic)
Hair: m3/ or m6/ (spiky hero hair, c1-black or c2-brown)
Clothing: cloth1/ or cloth5/ (armor-like, c1-silver or c2-blue)
Weapon: weapon1/ (sword)
```

#### Mage/Scholar
```
Skin: skin_c2.png (light)
Face: face_c3.png (wise)
Hair: m4/ or f5/ (long hair, c3-blonde or c7-purple)
Clothing: cloth3/ or cloth7/ (robes, c5-purple or c4-blue)
Weapon: weapon4/ (staff)
```

#### Rogue/Thief
```
Skin: skin_c4.png (medium-tan)
Face: face_c2.png (mischievous)
Hair: m2/ or f2/ (short/messy, c1-black)
Clothing: cloth2/ or cloth9/ (light armor, c6-green or c8-red)
Weapon: weapon5/ (daggers/bows) or weapon1/ (dual swords)
```

#### Healer/Priest
```
Skin: skin_c2.png (light)
Face: face_c4.png (gentle)
Hair: f3/ or f6/ (long, c2-brown or c8-white)
Clothing: cloth4/ or cloth8/ (robes, c7-pink or c1-white)
Weapon: weapon4/ (staff) or none
```

### Extended Party (Up to 8 Characters)

#### Warrior
```
Hair: m7/ or m9/ (warrior style)
Clothing: cloth6/ or cloth11/ (heavy armor)
Weapon: weapon2/ (axe/hammer)
```

#### Archer/Ranger
```
Hair: f4/ or m5/ (practical)
Clothing: cloth10/ or cloth12/ (light)
Weapon: weapon5/ (bow)
```

#### Dark Mage
```
Hair: f7/ or m8/ (dark colors)
Clothing: cloth13/ or cloth14/ (dark robes)
Weapon: weapon4/ (dark staff)
```

#### Summoner
```
Hair: f8/ or f9/ (exotic)
Clothing: cloth15/ or cloth16/ (fancy robes)
Weapon: weapon4/ (ornate staff)
```

---

## 📊 TOTAL COMBINATIONS POSSIBLE

| Component | Options | Variations |
|-----------|---------|------------|
| Skin | 6 | - |
| Face | 7 | - |
| Hair | 23 | × 8 colors = 184 |
| Clothing | 17 | × 8 colors = 136 |
| Weapons | 5 | Multiple each |

**Total Unique Characters:** 6 × 7 × 184 × 136 = **1,053,312 combinations!**

---

## 🛠️ TOOLS FOR ASSEMBLY

### Recommended Software
1. **Aseprite** (paid) - Best for pixel art, has layers
2. **GIMP** (free) - Full featured, layer support
3. **Photoshop** (paid) - Industry standard
4. **GraphicsGale** (free) - Pixel art focused

### Batch Processing (Python/PIL)
```python
from PIL import Image

# Example: Assemble a character
def create_character(skin_num, face_num, hair_folder, cloth_num, color_num):
    base = Image.open(f'skin/skin_c{skin_num}.png')
    face = Image.open(f'face/face_c{face_num}.png')
    hair = Image.open(f'hair/{hair_folder}/hair_c{color_num}.png')
    top = Image.open(f'cloth/cloth{cloth_num}/cloth{cloth_num}_top/cloth{cloth_num}_c{color_num}_top.png')
    bot = Image.open(f'cloth/cloth{cloth_num}/cloth{cloth_num}_bot/cloth{cloth_num}_c{color_num}_bot.png')
    
    # Composite images
    base.paste(bot, (0,0), bot)
    base.paste(top, (0,0), top)
    base.paste(face, (0,0), face)
    base.paste(hair, (0,0), hair)
    
    return base
```

---

## 📝 USAGE NOTES

### For Side-View Battle (SV_Actors)
These assets appear to be designed for:
- **Overworld sprites** (8-directional movement)
- **Side-view battle** (if full animation frames included)
- **Portraits** (if face sets included)

Check `list_of_animation_full.gif` for animation frame reference.

### Color Palette
Reference: `clothcolor.aseprite`, `haircolor.aseprite`

Standard 8-color palette:
- c1: Black/Dark
- c2: Brown/Earth
- c3: Blonde/Gold
- c4: Blue/Water
- c5: Purple/Magic
- c6: Green/Nature
- c7: Pink/Red/Fire
- c8: White/Silver

### File Naming Convention
```
[component]_[color].[ext]
[component]_[number]_[color]_[part].[ext]

Examples:
  skin_c3.png
  face_c5.png
  cloth1_c4_top.png
  cloth12_c2_bot.png
```

---

## ✅ QUICK START CHECKLIST

1. [ ] Review `samples.gif` for example characters
2. [ ] Check `catalog_cloth.png` for clothing preview
3. [ ] Check `catalog_hair.png` for hair preview
4. [ ] Pick skin tone (c1-c6)
5. [ ] Pick face (c1-c7)
6. [ ] Pick hair style (f1-f9, m1-m9)
7. [ ] Pick clothing (cloth1-17)
8. [ ] Pick colors (c1-c8 for each)
9. [ ] Assemble in image editor
10. [ ] Export as RPG Maker MZ sprite sheet

---

## 📚 REFERENCE FILES

| File | Purpose |
|------|---------|
| samples.gif | Example character combinations |
| catalog_cloth.png | All clothing options preview |
| catalog_hair.png | All hair options preview |
| color_variations.gif | Color palette examples |
| frameguide_v2.png | Animation frame layout |
| list_of_animation_full.gif | Full animation reference |
| layer.gif | Layer order demonstration |
| weapon_types.gif | Weapon style preview |

---

## 🎨 ART STYLE NOTES

- **Resolution:** Appears to be pixel art (check frameguide)
- **Style:** JRPG/Anime inspired
- **Format:** PNG with transparency
- **Animation:** Multi-frame (check animation GIFs)

---

*"Create your heroes. Build your legend."*
