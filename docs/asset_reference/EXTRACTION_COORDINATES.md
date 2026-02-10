# Asset Extraction Coordinates
## Pixel-Perfect Reference for Battle Backgrounds

This document provides exact pixel coordinates for extracting battle backgrounds from SNES asset sheets.

---

## 🛠️ TOOLS NEEDED

- Image editor: GIMP (free), Photoshop, or Aseprite
- Format: PNG with transparency
- Recommended size: 640x360 or 800x450 (16:9) for backgrounds

---

## 🏛️ PALACE ASSETS

### File: `SNES - Terranigma - Maps - Loire Castle 2F (Throne Room & Lounges).png`
**Dimensions:** 1872 x 1472 pixels

#### Extract 1: Main Throne Room (RED CARPET)
```
Name: palace_throne_room_main.png
Coordinates:
  Top-Left: (20, 20)
  Bottom-Right: (460, 360)
Size: 440 x 340 pixels
Notes: The iconic throne with red carpet
```

#### Extract 2: Throne Room Variant
```
Name: palace_throne_room_alt.png
Coordinates:
  Top-Left: (480, 20)
  Bottom-Right: (920, 360)
Size: 440 x 340 pixels
Notes: Alternative throne arrangement
```

#### Extract 3: Guard Stations
```
Name: palace_guard_stations.png
Coordinates:
  Top-Left: (940, 20)
  Bottom-Right: (1380, 360)
Size: 440 x 340 pixels
Notes: For Hall of Guards encounter
```

#### Extract 4: Royal Lounge
```
Name: palace_royal_lounge.png
Coordinates:
  Top-Left: (20, 380)
  Bottom-Right: (460, 720)
Size: 440 x 340 pixels
Notes: Rest area background
```

#### Extract 5: Side Throne Room
```
Name: palace_throne_side.png
Coordinates:
  Top-Left: (480, 380)
  Bottom-Right: (920, 720)
Size: 440 x 340 pixels
Notes: Smaller throne for antechamber
```

---

### File: `SNES - Terranigma - Maps - Loire Castle 3F (Royal Bedchambers).png`
**Dimensions:** [To be measured]

#### Extract 6: Royal Bedchamber
```
Name: palace_bedchamber.png
Coordinates:
  Top-Left: (20, 20)
  Bottom-Right: (400, 300)
Size: 380 x 280 pixels
Notes: King's private quarters
```

#### Extract 7: Private Study
```
Name: palace_study.png
Coordinates:
  Top-Left: (420, 20)
  Bottom-Right: (800, 300)
Size: 380 x 280 pixels
Notes: Secret documents room
```

---

### File: `SNES - Terranigma - Maps - Loire Castle 1F (Various).png`
**Note:** Multiple 1F files exist

#### Extract 8: Library
```
Name: palace_library.png
Source: Library & Guest Room file
Coordinates:
  Top-Left: (20, 20)
  Bottom-Right: (400, 300)
Size: 380 x 280 pixels
Notes: Bookshelves and reading area
```

#### Extract 9: Kitchen
```
Name: palace_kitchen.png
Source: Kitchen & Pantry file
Coordinates:
  Top-Left: (20, 20)
  Bottom-Right: (400, 300)
Size: 380 x 280 pixels
Notes: Cooking area (environmental)
```

#### Extract 10: Prison/Dungeon
```
Name: palace_prison.png
Source: Prison file
Coordinates:
  Top-Left: (20, 20)
  Bottom-Right: (400, 300)
Size: 380 x 280 pixels
Notes: Dark cells
```

---

### File: `SNES - Terranigma - Maps - Sylvain Castle (Chapel & Throne Room).png`

#### Extract 11: Chapel
```
Name: palace_chapel.png
Coordinates:
  Top-Left: (480, 20)
  Bottom-Right: (920, 360)
Size: 440 x 340 pixels
Notes: Sacred altar area
```

#### Extract 12: Tower Pinnacle
```
Name: palace_tower_top.png
Coordinates:
  Top-Left: (20, 740)
  Bottom-Right: (460, 1080)
Size: 440 x 340 pixels
Notes: Highest point, true ending
```

---

## 🏚️ CAPITAL RUINS ASSETS

### File: `SNES - Terranigma - Maps - Louran (Ruins - Interior).png`
**Dimensions:** 1712 x 2464 pixels
**Layout:** Grid of ruined building interiors

### Grid System:
- **Rows:** 8 rows of ruins
- **Columns:** Variable (4-6 per row)
- **Average Room Size:** ~214 x 308 pixels

#### Row 1 - Large Public Buildings

**Extract 13: Entry Plaza**
```
Name: ruins_entry_plaza.png
Coordinates:
  Top-Left: (20, 20)
  Bottom-Right: (400, 300)
Size: 380 x 280 pixels
Notes: Large ruined hall
```

**Extract 14: Ruined Shop A**
```
Name: ruins_shop_a.png
Coordinates:
  Top-Left: (428, 20)
  Bottom-Right: (856, 320)
Size: 428 x 300 pixels
Notes: Merchant district
```

**Extract 15: Ruined Shop B**
```
Name: ruins_shop_b.png
Coordinates:
  Top-Left: (856, 20)
  Bottom-Right: (1284, 320)
Size: 428 x 300 pixels
Notes: Another shop
```

#### Row 2-3 - Residential Buildings

**Extract 16: Destroyed Home A**
```
Name: ruins_home_a.png
Coordinates:
  Top-Left: (20, 320)
  Bottom-Right: (214, 568)
Size: 194 x 248 pixels
Notes: Small house interior
```

**Extract 17: Destroyed Home B**
```
Name: ruins_home_b.png
Coordinates:
  Top-Left: (214, 320)
  Bottom-Right: (428, 568)
Size: 214 x 248 pixels
Notes: Another house
```

**Extract 18: Apartment Building**
```
Name: ruins_apartment.png
Coordinates:
  Top-Left: (428, 320)
  Bottom-Right: (856, 568)
Size: 428 x 248 pixels
Notes: Multi-room structure
```

#### Row 4 - Town Square

**Extract 19: Town Square**
```
Name: ruins_town_square.png
Coordinates:
  Top-Left: (20, 568)
  Bottom-Right: (400, 820)
Size: 380 x 252 pixels
Notes: Large open area
```

**Extract 20: Market Stalls**
```
Name: ruins_market.png
Coordinates:
  Top-Left: (400, 568)
  Bottom-Right: (800, 820)
Size: 400 x 252 pixels
Notes: Destroyed marketplace
```

#### Row 5 - Memorial/Ceremonial

**Extract 21: Memorial Hall**
```
Name: ruins_memorial.png
Coordinates:
  Top-Left: (20, 820)
  Bottom-Right: (400, 1070)
Size: 380 x 250 pixels
Notes: Hero statues
```

#### Row 6-7 - Underground/Sewers

**Extract 22: Sewer Tunnel**
```
Name: ruins_sewer.png
Coordinates:
  Top-Left: (400, 1070)
  Bottom-Right: (800, 1320)
Size: 400 x 250 pixels
Notes: Underground passage
```

**Extract 23: Underground Chamber**
```
Name: ruins_underground.png
Coordinates:
  Top-Left: (800, 1070)
  Bottom-Right: (1200, 1320)
Size: 400 x 250 pixels
Notes: Large cavern room
```

#### Row 8 - Palace Approach

**Extract 24: Palace Gate**
```
Name: ruins_palace_gate.png
Coordinates:
  Top-Left: (20, 2100)
  Bottom-Right: (500, 2400)
Size: 480 x 300 pixels
Notes: Final approach
```

---

## 🌊 TIDE COAST ASSETS

### File: `SNES - Terranigma - Maps - Harbor of Freedom (Exterior).png`
**Dimensions:** 1584 x 1552 pixels

#### Extract 25: Harbor Main
```
Name: tide_harbor_main.png
Coordinates:
  Top-Left: (20, 20)
  Bottom-Right: (600, 400)
Size: 580 x 380 pixels
Notes: Full harbor scene
```

#### Extract 26: Ship Deck
```
Name: tide_ship_deck.png
Coordinates:
  Top-Left: (600, 20)
  Bottom-Right: (1100, 400)
Size: 500 x 380 pixels
Notes: Ship for battles/travel
```

#### Extract 27: Dock Area
```
Name: tide_dock.png
Coordinates:
  Top-Left: (20, 400)
  Bottom-Right: (400, 780)
Size: 380 x 380 pixels
Notes: Pier/dock section
```

---

### File: `SNES - Terranigma - Maps - Ship (Exterior & Interior).png`

#### Extract 28: Ship Exterior
```
Name: tide_ship_exterior.png
Top-Left: (20, 20)
Bottom-Right: (500, 350)
Size: 480 x 330 pixels
Notes: Ship deck battle background
```

#### Extract 29: Ship Cabin
```
Name: tide_ship_cabin.png
Top-Left: (20, 370)
Bottom-Right: (400, 650)
Size: 380 x 280 pixels
Notes: Interior cabin
```

---

## ⛰️ UPLANDS ASSETS

### File: `SNES - Terranigma - Maps - Storkolm (Exterior).png`

#### Extract 30: Village Center
```
Name: uplands_village.png
Top-Left: (center section, TBD)
Size: 480 x 360 pixels
Notes: Stone village plaza
```

#### Extract 31: Stone Houses
```
Name: uplands_houses.png
Top-Left: (building cluster, TBD)
Size: 400 x 300 pixels
Notes: Residential area
```

---

## ☁️ AETHERREACH ASSETS

### File: `SNES - Breath of Fire 2 - Maps - Windia (Exterior).png`

#### Extract 32: Floating Plaza
```
Name: aetherreach_plaza.png
Top-Left: (center, TBD)
Size: 640 x 360 pixels
Notes: Main floating city square
```

#### Extract 33: Cloud Bridge
```
Name: aetherreach_bridge.png
Top-Left: (path section, TBD)
Size: 480 x 300 pixels
Notes: Walkway between islands
```

---

### File: `SNES - Albert Odyssey 2 - Maps - Gote (Exterior Day & Noon).png`

#### Extract 34: Cloud City Day
```
Name: aetherreach_day.png
Top-Left: (day variant, TBD)
Size: 640 x 360 pixels
Notes: Daytime lighting
```

#### Extract 35: Cloud City Noon
```
Name: aetherreach_noon.png
Top-Left: (noon variant, TBD)
Size: 640 x 360 pixels
Notes: Alternative lighting
```

---

## 🗼 TOWER ASSETS

### File: `SNES - Terranigma - Maps - Loire Castle (Tower).png`

#### Extract 36: Tower Base
```
Name: tower_base.png
Top-Left: (bottom section, TBD)
Size: 400 x 400 pixels
Notes: Lower floors
```

#### Extract 37: Tower Mid
```
Name: tower_mid.png
Top-Left: (middle section, TBD)
Size: 400 x 400 pixels
Notes: Middle floors
```

#### Extract 38: Tower Top
```
Name: tower_top.png
Top-Left: (top section, TBD)
Size: 400 x 400 pixels
Notes: Upper floors
```

---

## 📋 EXTRACTION CHECKLIST

### Priority 1 (Essential):
- [ ] palace_throne_room_main.png
- [ ] palace_throne_room_alt.png
- [ ] ruins_entry_plaza.png
- [ ] ruins_shop_a.png
- [ ] ruins_town_square.png
- [ ] aetherreach_plaza.png
- [ ] tide_harbor_main.png

### Priority 2 (Important):
- [ ] palace_royal_lounge.png
- [ ] palace_bedchamber.png
- [ ] palace_guard_stations.png
- [ ] ruins_home_a.png
- [ ] ruins_memorial.png
- [ ] ruins_palace_gate.png
- [ ] tide_ship_deck.png

### Priority 3 (Polish):
- [ ] palace_library.png
- [ ] palace_chapel.png
- [ ] ruins_sewer.png
- [ ] ruins_underground.png
- [ ] uplands_village.png
- [ ] tower_top.png

---

## 🎨 POST-PROCESSING NOTES

### Color Adjustments:
- **Palace:** Slightly darken for ominous feel
- **Capital Ruins:** Desaturate 10-15% for decayed look
- **Tide:** Enhance blue tones for water
- **Aetherreach:** Add slight glow for magical feel

### Format Requirements:
- Resolution: 640x360 (standard) or 800x450 (HD)
- Format: PNG with alpha channel
- Color depth: 32-bit (RGBA)
- File naming: [zone]_[description].png

### Organization:
```
assets/battle_backgrounds/
├── palace/
├── capital_ruins/
├── tide/
├── uplands/
├── aetherreach/
└── tower/
```

---

*Extract these carefully - they're your visual foundation!*
