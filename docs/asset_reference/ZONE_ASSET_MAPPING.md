# Zone-to-Asset Mapping Guide
## Complete Reference for All 15 Zones

This document maps every zone in Chroma's Edge to specific SNES asset references for battle backgrounds, map layouts, and visual inspiration.

---

## 🏛️ PALACE (Final Dungeon)

### Primary Assets: Terranigma Loire Castle

| Room Type | Asset File | Specific Section | Usage |
|-----------|------------|------------------|-------|
| **Throne Room** | Loire Castle 2F (Throne Room & Lounges) | Top-left quadrant (0.00-0.50, 0.00-0.33) | Final boss battle |
| **Royal Chambers** | Loire Castle 3F (Royal Bedchambers) | Top-left room | Pre-boss cutscene |
| **Guard Quarters** | Loire Castle 2F (Royal Quarters) | Top row sections | Enemy encounters |
| **Kitchen/Pantry** | Loire Castle 1F (Kitchen & Pantry) | Left side | Environmental storytelling |
| **Library** | Loire Castle 1F (Library & Guest Room) | Left section | Lore discovery area |
| **Prison/Dungeon** | Loire Castle 1F (Prison) | All sections | Prison break sequence |
| **Tower Ascent** | Loire Castle (Tower) | Vertical sections | Climbing sequence |
| **Chapel** | Sylvain Castle (Chapel & Throne Room) | Right side chapel | Sacred moments |

### Layout Flow:
```
Entrance → Guard Quarters → Kitchen → Library → Chapel → Royal Chambers → Throne Room (Boss)
                ↓
            Prison (Side quest)
                ↓
            Tower (Secret area)
```

---

## 🏙️ CAPITAL RUINS (Corrupted City)

### Primary Assets: Terranigma Louran Ruins

| Area Type | Asset Section | Coordinate | Usage |
|-----------|--------------|------------|-------|
| **Collapsed Building A** | Row 1, Col 1 | (0.00-0.25, 0.00-0.13) | Opening area |
| **Ruined Tavern** | Row 1, Col 2 | (0.25-0.50, 0.00-0.13) | NPC encounter |
| **Destroyed Home 1** | Row 2, Col 1 | (0.00-0.13, 0.13-0.23) | Loot/search |
| **Destroyed Home 2** | Row 2, Col 2 | (0.13-0.25, 0.13-0.23) | Enemy ambush |
| **Ruined Shop** | Row 3, Col 1-2 | (0.00-0.25, 0.23-0.33) | Merchant remnant |
| **Collapsed Tower** | Row 4, Col 1 | (0.00-0.13, 0.33-0.43) | Vertical exploration |
| **Underground Passage** | Row 5, Col 3 | (0.25-0.38, 0.43-0.53) | Secret path |
| **Final Ruins** | Row 7-8, various | (0.50-1.00, 0.60-0.90) | Pre-boss area |

### Total Rooms Available: 40+ unique ruined interiors

---

## 🌊 TIDE COAST (Port Town)

### Primary Assets: Terranigma Harbor of Freedom

| Location | Asset Section | Usage |
|----------|--------------|-------|
| **Main Dock** | Top-left quadrant | Central hub |
| **Ship Deck** | Ship (Exterior) | Travel/transition |
| **Ship Cabin** | Ship (Interior) | Rest/save point |
| **Warehouse District** | Harbor center-right | Quest location |
| **Fishing Pier** | Harbor bottom-left | Mini-game |
| **Tavern Exterior** | Harbor building cluster | Social hub |

### Water Texture Reference:
- Use Harbor water tiles for Tide zone
- Animated water sprites available

---

## ⛰️ UPLANDS (Stone Sanctuary)

### Primary Assets: Terranigma Storkolm

| Location | Asset Section | Usage |
|----------|--------------|-------|
| **Village Center** | Storkolm Exterior center | Main plaza |
| **Stone Houses** | Various building sections | NPC homes |
| **Elevated Paths** | Storkolm connecting walkways | Exploration routes |
| **Mountain Overlook** | Storkolm upper areas | Scenic viewpoint |

### Alternative: Albert Odyssey Clouds
- Use cloud layers for sky background
- Day/Noon variants for time-of-day system

---

## ☁️ AETHERREACH (Sky Town)

### Primary Assets: Breath of Fire 2 Windia

| Location | Asset Section | Usage |
|----------|--------------|-------|
| **Floating Plaza** | Windia Exterior center | Main hub |
| **Cloud Bridges** | Windia connecting paths | Navigation |
| **Sky Buildings** | Windia various structures | Shops/inn |
| **Landing Platform** | Windia edge sections | Airship dock |

### Secondary: Albert Odyssey Gote
- Day/Noon variants for time system
- Cloud texture reference

---

## 🗼 TOWER (Ascending Spire)

### Primary Assets: Terranigma Loire Castle Tower

| Floor | Asset Section | Theme |
|-------|--------------|-------|
| **Floors 1-5** | Tower lower sections | Guard quarters |
| **Floors 6-10** | Tower middle sections | Laboratory/magical |
| **Floors 11-15** | Tower upper sections | Royal archives |
| **Pinnacle** | Sylvain Castle Throne | Final floor boss |

---

## 🌲 OTHER ZONE ASSETS

### EMBER (Ashlands)
- **Burning Heroes Fire City** (from previous analysis)
- Terranigma dark/ruined sections for burned areas

### FROST (Ice Caverns)
- Star Ocean ice dungeon references
- Terranigma cold-toned sections

### CHRONO (Clockwork City)
- Terranigma mechanical sections (if any)
- Previous steampunk assets

### VOID
- Dark sections from any Terranigma dungeon
- Sylvain Castle dark chapel

### DUSTBELT
- Louran Ruins sand-colored sections
- Desert-appropriate ruins

---

## 🎨 BATTLE BACKGROUND QUICK REFERENCE

### High-Priority Extractions:

| Zone | Background | Source File | Priority |
|------|-----------|-------------|----------|
| Palace | Throne Room | Loire Castle 2F | ⭐⭐⭐⭐⭐ |
| Palace | Royal Chamber | Loire Castle 3F | ⭐⭐⭐⭐⭐ |
| Capital | Ruined Building A | Louran Row 1-1 | ⭐⭐⭐⭐⭐ |
| Capital | Ruined Building B | Louran Row 1-2 | ⭐⭐⭐⭐⭐ |
| Capital | Collapsed Tower | Louran Row 4-1 | ⭐⭐⭐⭐ |
| Tide | Ship Deck | Ship Exterior | ⭐⭐⭐⭐ |
| Tide | Harbor Dock | Harbor of Freedom | ⭐⭐⭐⭐ |
| Aetherreach | Floating Plaza | Windia Exterior | ⭐⭐⭐⭐⭐ |
| Uplands | Stone Village | Storkolm Exterior | ⭐⭐⭐⭐ |

---

## 📋 EXTRACTION WORKSHEET

### To Extract (Pixel Coordinates):

#### Palace - Throne Room
```
File: SNES - Terranigma - Maps - Loire Castle 2F (Throne Room & Lounges).png
Resolution: 1872x1472
Extract: (0, 0) to (936, 490) - Top-left throne room
```

#### Capital - Ruin Set 1
```
File: SNES - Terranigma - Maps - Louran (Ruins - Interior).png
Resolution: 1712x2464
Extract: (0, 0) to (428, 320) - First ruined building
Extract: (428, 0) to (856, 320) - Second ruined building
Extract: (856, 0) to (1284, 320) - Third ruined building
```

#### Tide - Harbor
```
File: SNES - Terranigma - Maps - Harbor of Freedom (Exterior).png
Resolution: 1584x1552
Extract: (0, 0) to (792, 776) - Full harbor scene
```

#### Aetherreach - Floating City
```
File: SNES - Breath of Fire 2 - Maps - Windia (Exterior).png
Extract full image as reference
```

---

## 🎯 IMPLEMENTATION ORDER

### Week 1: Critical Path
1. Extract Palace Throne Room (final battle)
2. Extract 3-4 Capital Ruins backgrounds
3. Document Aetherreach reference

### Week 2: Important
4. Extract Tide Harbor elements
5. Extract Palace additional rooms
6. Document Uplands reference

### Week 3: Polish
7. Extract remaining backgrounds
8. Create zone-specific style guides
9. Final review and organization

---

*Last Updated: 2026-02-07*
