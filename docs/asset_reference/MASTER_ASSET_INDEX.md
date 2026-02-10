# Master Asset Reference Index
## Complete Guide to SNES Assets for Chroma's Edge

This is the central hub document linking all asset reference materials.

---

## 📚 DOCUMENTATION SUITE

### Core Documents:

| Document | Purpose | Status |
|----------|---------|--------|
| **MASTER_ASSET_INDEX.md** | This file - central hub | ✅ Complete |
| **ZONE_ASSET_MAPPING.md** | Zone-to-asset assignments | ✅ Complete |
| **EXTRACTION_COORDINATES.md** | Pixel coordinates for extraction | ✅ Complete |
| **VISUAL_STYLE_GUIDE.md** | Color/style adaptation rules | ✅ Complete |
| **IMPLEMENTATION_ROADMAP.md** | 4-week implementation plan | ✅ Complete |

### Zone-Specific Design:

| Document | Zone | Status |
|----------|------|--------|
| **PALACE_DUNGEON_LAYOUT.md** | Palace (Final Dungeon) | ✅ Complete |
| **CAPITAL_RUINS_ENCOUNTERS.md** | Capital Ruins | ✅ Complete |

---

## 🗂️ ASSET INVENTORY

### By Source Game:

#### Terranigma (Primary Source)
**Total Files:** 30+ maps
**Quality Rating:** ⭐⭐⭐⭐⭐ EXCELLENT

| File Category | Count | Best For |
|--------------|-------|----------|
| Loire Castle | 12 files | Palace dungeon |
| Louran Ruins | 1 file (50+ rooms) | Capital Ruins |
| Harbor of Freedom | 2 files | Tide Coast |
| Storkolm Village | 2 files | Uplands |
| Sylvain Castle | 4 files | Palace alternative |
| Various locations | 10+ files | Reference/inspiration |

#### Breath of Fire 2
**Total Files:** 5 maps
**Quality Rating:** ⭐⭐⭐⭐⭐ EXCELLENT

| File | Best For |
|------|----------|
| Windia (Exterior) | Aetherreach floating city |
| Various interiors | Reference |

#### Albert Odyssey 2
**Total Files:** 4 maps
**Quality Rating:** ⭐⭐⭐⭐ GOOD

| File | Best For |
|------|----------|
| Gote (Day & Noon) | Aetherreach cloud city |
| Throne Room | Palace alternative |
| Clouds | Sky/weather reference |

---

## 🎯 QUICK REFERENCE BY ZONE

### 🏛️ PALACE (Final Dungeon)
**Primary Source:** Terranigma Loire Castle
**Assets Needed:** 11 backgrounds
**Status:** Fully documented

**Key Assets:**
- Throne Room (RED CARPET) - Extract 1
- Royal Chambers - Extract 6
- Guard Hall - Extract 4
- Library - Extract 8
- Prison - Extract 10
- Chapel - Extract 11
- Tower Top - Extract 12

**Docs:** PALACE_DUNGEON_LAYOUT.md

---

### 🏚️ CAPITAL RUINS (Corrupted City)
**Primary Source:** Terranigma Louran Ruins
**Assets Needed:** 12+ backgrounds
**Status:** Fully documented

**Key Assets:**
- Entry Plaza - Extract 13
- Ruined Shops - Extracts 14-15
- Destroyed Homes - Extracts 16-18
- Town Square - Extract 19
- Memorial Hall - Extract 21
- Sewer/Underground - Extracts 22-23
- Palace Gate - Extract 24

**Docs:** CAPITAL_RUINS_ENCOUNTERS.md

---

### 🌊 TIDE COAST (Port Town)
**Primary Source:** Terranigma Harbor + Ship
**Assets Needed:** 5 backgrounds
**Status:** Documented

**Key Assets:**
- Harbor Main - Extract 25
- Ship Deck - Extract 27
- Ship Cabin - Extract 29
- Dock Area - Extract 26

**Docs:** ZONE_ASSET_MAPPING.md (Tide section)

---

### ☁️ AETHERREACH (Sky Town)
**Primary Source:** BoF2 Windia + Albert Odyssey
**Assets Needed:** 4 backgrounds
**Status:** Documented

**Key Assets:**
- Floating Plaza - Extract 32
- Cloud Bridge - Extract 33
- Day Variant - Extract 34
- Noon Variant - Extract 35

**Docs:** ZONE_ASSET_MAPPING.md (Aetherreach section)

---

### ⛰️ UPLANDS (Stone Sanctuary)
**Primary Source:** Terranigma Storkolm
**Assets Needed:** 3 backgrounds
**Status:** Documented

**Key Assets:**
- Village Center - Extract 30
- Stone Houses - Extract 31

**Docs:** ZONE_ASSET_MAPPING.md (Uplands section)

---

### 🗼 TOWER (Ascending Spire)
**Primary Source:** Terranigma Loire Castle Tower
**Assets Needed:** 3 backgrounds
**Status:** Documented

**Key Assets:**
- Tower Base - Extract 36
- Tower Mid - Extract 37
- Tower Top - Extract 38

**Docs:** ZONE_ASSET_MAPPING.md (Tower section)

---

## 📊 PRIORITY MATRIX

### Critical (Week 1):
| # | Asset | Zone | Impact |
|---|-------|------|--------|
| 1 | Throne Room | Palace | ⭐⭐⭐⭐⭐ Final boss |
| 2 | Entry Plaza | Capital | ⭐⭐⭐⭐⭐ Zone entry |
| 3 | Town Square | Capital | ⭐⭐⭐⭐⭐ Major battle |
| 4 | Floating Plaza | Aetherreach | ⭐⭐⭐⭐⭐ Unique zone |
| 5 | Harbor Main | Tide | ⭐⭐⭐⭐⭐ Hub area |

### Important (Week 2):
| # | Asset | Zone | Impact |
|---|-------|------|--------|
| 6 | Royal Chambers | Palace | ⭐⭐⭐⭐ Story moment |
| 7 | Ruined Shops | Capital | ⭐⭐⭐⭐ Variety |
| 8 | Destroyed Homes | Capital | ⭐⭐⭐⭐ Atmosphere |
| 9 | Ship Deck | Tide | ⭐⭐⭐⭐ Travel |
| 10 | Cloud Bridge | Aetherreach | ⭐⭐⭐⭐ Navigation |

### Polish (Week 3-4):
- All remaining backgrounds
- Effect overlays
- Animation elements
- Secret area art

---

## 🔗 EXTERNAL REFERENCES

### Parent Documents:
- `../PRODUCTION_CHECKLIST_MASTER.md` - Overall project status
- `../WORLD_NPC_DISTRIBUTION.md` - NPC placements (may need visual reference)
- `../SNES_ASSETS_ANALYSIS.md` - Initial asset analysis
- `../../content/dialog/MASTER_INDEX.md` - Content references

### Related Asset Analysis:
- `../FF_RECORD_KEEPER_ASSETS.md` - FF RK assets (if exists)
- `../TIME_FANTASY_INVENTORY.md` - TF tileset reference (if exists)

---

## 📝 FILE PATHS

### Documentation:
```
docs/
└── asset_reference/
    ├── MASTER_ASSET_INDEX.md (this file)
    ├── ZONE_ASSET_MAPPING.md
    ├── EXTRACTION_COORDINATES.md
    ├── VISUAL_STYLE_GUIDE.md
    ├── IMPLEMENTATION_ROADMAP.md
    ├── PALACE_DUNGEON_LAYOUT.md
    └── CAPITAL_RUINS_ENCOUNTERS.md
```

### Source Assets:
```
assets/
└── AssetsForMyGame/
    ├── SNES - Terranigma - Maps - [various].png
    ├── SNES - Breath of Fire 2 - Maps - [various].png
    └── SNES - Albert Odyssey 2 - Maps - [various].png
```

### Output Assets (To Create):
```
assets/
├── battle_backgrounds/
│   ├── palace/
│   ├── capital_ruins/
│   ├── tide/
│   ├── uplands/
│   └── aetherreach/
└── reference/snes/
    └── extracted/
```

---

## 🎓 USAGE WORKFLOW

### For Implementers:

1. **Start Here** (MASTER_ASSET_INDEX.md)
   - Find your zone
   - Note priority level
   - Check linked documents

2. **Read Design Doc**
   - PALACE_DUNGEON_LAYOUT.md (for Palace)
   - CAPITAL_RUINS_ENCOUNTERS.md (for Capital)
   - ZONE_ASSET_MAPPING.md (for others)

3. **Extract Assets**
   - EXTRACTION_COORDINATES.md for pixel coords
   - Follow extraction checklist

4. **Style Assets**
   - VISUAL_STYLE_GUIDE.md for color adjustments
   - Match to Time Fantasy palette

5. **Implement**
   - IMPLEMENTATION_ROADMAP.md for timeline
   - Test in engine
   - Iterate

---

## 📈 PROGRESS TRACKING

### Extraction Status:

| Zone | Total | Extracted | Adjusted | In-Game |
|------|-------|-----------|----------|---------|
| Palace | 11 | ⬜ | ⬜ | ⬜ |
| Capital | 12 | ⬜ | ⬜ | ⬜ |
| Tide | 5 | ⬜ | ⬜ | ⬜ |
| Aetherreach | 4 | ⬜ | ⬜ | ⬜ |
| Uplands | 3 | ⬜ | ⬜ | ⬜ |
| Tower | 3 | ⬜ | ⬜ | ⬜ |
| **TOTAL** | **38** | **⬜** | **⬜** | **⬜** |

**Last Updated:** 2026-02-07

---

## 💡 TIPS & NOTES

### Extraction Tips:
- Use "Nearest Neighbor" resizing to keep pixel art crisp
- Save originals before any adjustments
- Batch process similar adjustments
- Test one asset thoroughly before doing all

### Style Tips:
- When in doubt, desaturate slightly
- The RED CARPET in Palace is iconic - preserve it
- Capital Ruins should feel melancholic, not horror
- Aetherreach needs to feel magical and otherworldly

### Implementation Tips:
- Test backgrounds with character sprites overlaid
- Ensure text readability in all areas
- Effects shouldn't obscure gameplay
- Performance test with all effects active

---

## 🆘 TROUBLESHOOTING

### Common Issues:

**Q: Colors don't match Time Fantasy**
A: See VISUAL_STYLE_GUIDE.md color adjustment section

**Q: Which coordinate system to use?**
A: See EXTRACTION_COORDINATES.md - top-left origin

**Q: What resolution for battle backgrounds?**
A: 640x360 (SD) or 800x450 (HD)

**Q: Can I use these assets commercially?**
A: These are REFERENCE ONLY - recreate in your style

**Q: How long does extraction take?**
A: ~20-30 min per asset including adjustments

---

## 📞 SUPPORT

If you need help:
1. Check the specific zone document
2. Review VISUAL_STYLE_GUIDE.md
3. Check IMPLEMENTATION_ROADMAP.md for timeline
4. Refer to source SNES_ASSETS_ANALYSIS.md

---

*"Good documentation is like a compass - it keeps you pointed in the right direction."*

---

**Document Version:** 1.0  
**Created:** 2026-02-07  
**Last Updated:** 2026-02-07  
**Maintained By:** Development Team
