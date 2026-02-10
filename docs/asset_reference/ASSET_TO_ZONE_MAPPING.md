# Asset to Zone Mapping
## Complete Visual Reference for All New Assets

---

## 🗺️ QUICK REFERENCE TABLE

| Zone | Primary Assets | Secondary Assets | Parallax |
|------|---------------|------------------|----------|
| **Palace** | Terranigma Loire/Sylvain Castles | Albert Odyssey 2 Throne | None (indoor) |
| **Capital Ruins** | Terranigma Louran, Alvanista Castle | Star Ocean Castle Town | Gloomwood (night) |
| **Frost** | Ice Cavern Tileset | Ice Fang Castle | Ice Castle Parallax |
| **Ember** | Lava Cavern Tileset, Burning Heroes | Fire Shrines | Smoke overlay |
| **Uplands** | Lufia 2 Shrines, Magna Braban Castle | 7 Small Shrines | Whitewood Vale |
| **Tide** | Terranigma Harbor, Ship Maps | Submarine Cave | Ocean horizon |
| **Aetherreach** | Star Ocean Clouds, Windia | Dragon Shrine | Star Ocean Cloud Parallax |
| **Void** | Dark Dimension Tileset, Phantom Castle | Undead Tileset | Dark void |
| **Chrono** | Steampunk Tileset, Tower of Bloodshed | Gear objects | Cloud/fog |
| **Tower** | Loire Castle Tower, Multiple Shrines | Various towers | Sky through windows |
| **Remnant** | Gloomwood Forest assets | Rocky Objects | Gloomwood Parallax |
| **Dustbelt** | Arabian Nights, Giant Worm Terrain | Ifrit's Castle | Sand dunes |
| **Mire** | Sewer Maps, Malice's Castle Sewers | Rocky Objects | Gloomwood (swamp tint) |
| **Prism** | Ice Cavern (recolored), Crystal objects | Reflective pools | Crystal shimmer |
| **Obsidian** | Steampunk, Craftpix Objects | Factory machinery | Industrial haze |

---

## 🏛️ PALACE ZONE - DETAILED MAPPING

### Final Dungeon Layout:
```
Floor 1 (Entry):
- Entrance Hall → Terranigma Loire Castle 1F (Quarters hallway)
- Guard Stations → Terranigma Loire Castle 1F (various rooms)
- Storage → Terranigma Loire Castle BF (Pantry)
- Prison → Terranigma Loire Castle BF (Prison cells)

Floor 2 (Royal):
- Library → Terranigma Loire Castle 1F (Library & Guest Room)
- Royal Lounge → Terranigma Loire Castle 2F (Lounges)
- Throne Antechamber → Terranigma Sylvain Castle (Anteroom)
- MAIN THRONE ROOM → Terranigma Loire Castle 2F (Throne Room)

Floor 3 (Private):
- Royal Bedchambers → Terranigma Loire Castle 3F (Bedchambers)
- Secret Study → Terranigma Sylvain Castle (Royal Chambers)

Tower (Ascent):
- Floors 1-5 → Terranigma Loire Castle (Tower base)
- Floors 6-10 → Terranigma Loire Castle (Tower mid)
- Floors 11-15 → Tengai Makyou Zero Royal Dragon Castle

Secret Areas:
- Chapel → Terranigma Sylvain Castle (Chapel)
- Hidden Vault → Albert Odyssey 2 (Throne Room)
```

### Battle Backgrounds to Extract:
| Room | Source File | Coordinates | Output Name |
|------|-------------|-------------|-------------|
| Throne Room (Final Boss) | Loire Castle 2F | (0,0)-(468,368) | palace_throne_final.png |
| Throne Antechamber | Sylvain Castle | (480,20)-(920,360) | palace_throne_ante.png |
| Royal Lounge | Loire Castle 2F | (20,380)-(460,720) | palace_lounge.png |
| Library | Loire Castle 1F | Left section | palace_library.png |
| Prison | Loire Castle BF | (0,0)-(400,300) | palace_prison.png |
| Chapel | Sylvain Castle | (480,740)-(920,1080) | palace_chapel.png |
| Tower Top | Tengai Makyou Zero | Castle 10 | palace_tower_top.png |

---

## 🏚️ CAPITAL RUINS ZONE - DETAILED MAPPING

### District Layout:
```
Entry Plaza:
- Base → Terranigma Louran Ruins Row 1, Col 1
- Shops → Terranigma Louran Ruins Row 1, Col 2-3

Residential Quarter:
- Homes → Louran Ruins Row 2-3
- Apartments → Louran Ruins Row 3, wide section

Town Square:
- Center → Louran Ruins Row 4
- Market → Louran Ruins Row 4, right section

Memorial District:
- Hall of Heroes → Louran Ruins Row 5
- Fallen Statues → Use Pictologica FF statues

Underground:
- Sewers → Tales of Phantasia Malice's Castle Sewers
- Secret Passages → Louran Ruins Row 6-7

Palace Approach:
- Gate → Louran Ruins Row 8
- Courtyard → Star Ocean Castle Town (ruined version)
- Palace Entrance → Magna Braban Anatea Castle (corrupted)
```

### Corruption Visuals:
- Use `tf_darkdimension` for void-touched areas
- Use `undead_tileset` for heavily corrupted zones
- Darken all colors 25%
- Add purple/black overlay

---

## ⛰️ UPLANDS ZONE - DETAILED MAPPING

### Sanctuary of the High:
```
Main Temple (High Shrine):
- Exterior → Lufia 2 - Shrine to Alunze Kingdom (Exterior)
- Interior → Lufia 2 - Shrine to Alunze Kingdom (Interior)
- Main Hall → Use as central hub

7 Small Shrines (The Circle):
1. Shrine of Dust (Earth) → Lufia 2 - Small Shrine to Gordovan
2. Shrine of Tides (Water) → Lufia 2 - Small Shrine to Agurio
3. Shrine of Flame (Fire) → Bakumatsu - Red Shrines
4. Shrine of Frost (Ice) → Lufia 2 - Small Shrine to Aleyn
5. Shrine of Storms (Wind) → Lufia 2 - Small Shrine to Treadool
6. Shrine of Life (Nature) → Lufia 2 - Small Shrine to Dragon Egg
7. Shrine of Memory (Time) → Lufia 2 - Small Shrine to Parcelyte

Town (Ashveil Sanctuary):
- Layout → Star Ocean - Astral Castle Town
- Gate → Magna Braban - Salanan Castle Entrance
- Houses → Mix of castle town buildings
```

### Parallax Setup:
- Layer 1 (Back): Whitewood Vale Parallax
- Layer 2 (Mid): Mountain range (from parallax)
- Layer 3 (Front): Cloud layer (subtle)

---

## ❄️ FROST ZONE - DETAILED MAPPING

### Ice Citadel Structure:
```
Surface Town (Rimehold):
- Buildings → Time Fantasy Winter tileset
- Ice effects → Ice Cavern A1 (autotiles)
- Parallax → Ice Castle Parallax BG

Ice Caverns (Dungeon):
- Level 1-3 → Dungeon A1 ICE CAVERN
- Level 4-6 → Dungeon A2 ICE CAVERN
- Level 7-9 → Dungeon A4 ICE CAVERN
- Boss Area → Tengai Makyou Zero - Ice Fang Castle

Frozen Lake:
- Surface → Ice Cavern B (water as ice)
- Underwater → Submarine Cave Shrine (recolored)

Shrine of Frost:
- Exterior → Lufia 2 - Small Shrine to Aleyn
- Interior → Ice-themed with crystal formations
```

### Visual Effects:
- Snow particles (weather effect)
- Ice Castle parallax scrolling slowly
- Blue/white color grading

---

## 🔥 EMBER ZONE - DETAILED MAPPING

### Cinderstep & Fire Lands:
```
Town (Cinderstep):
- Layout → Burning Heroes - Fire City & Fire Castle (Exterior)
- Buildings → Burning Heroes Fire City structures
- Forge → Custom using lava tileset

Fire Castle (Main Dungeon):
- Exterior → Burning Heroes Fire City & Fire Castle
- Interior → Burning Heroes - Fire Castle (Interior)
- Boss Room → Ifrit's Castle (Arabian Nights)

Lava Caverns:
- All levels → Dungeon A1/A2/A4/B LAVA CAVERN
- Magma flows → Animated autotiles
- Crystal formations → Recolor Prism assets

Fire Bear Shrine (Beast Tribe):
- Location → Tengai Makyou Zero - Fire Bear Shrine
- Used in Beast War questline

Firepoint Village:
- Secondary town → Tengai Makyou Zero - Firepoint Village
- Access to hidden areas
```

### Visual Effects:
- Lava glow (tint screen orange in areas)
- Heat shimmer (parallax overlay)
- Smoke/fog layers
- Ash particles

---

## 🌊 TIDE ZONE - DETAILED MAPPING

### Brinegate Port:
```
Harbor District:
- Main Port → Terranigma - Harbor of Freedom
- Docks → Harbor docks section
- Warehouses → Harbor warehouse section

Ships:
- Merchant Vessels → Terranigma - Ship (Exterior)
- Ship Interiors → Terranigma - Ship (Interior)
- Battle Decks → Extract from Ship Exterior for battles

Underwater Areas:
- Ruins → Submarine Cave Shrine (Waterless)
- Underwater → Submarine Cave Shrine (with water overlay)
- Seabed → Craftpix - Seabed Objects

Coastal Caves:
- Tidal caves → Ice Cavern (recolored blue/green)
- Pirate hideouts → Cutthroat Island maps
```

### Parallax:
- Ocean horizon (gradient)
- Ships in distance
- Seagulls (animated)

---

## ☁️ AETHERREACH ZONE - DETAILED MAPPING

### Sky Town Structure:
```
Floating Plaza:
- Layout → Breath of Fire 2 - Windia
- Buildings → Mix of castle and cloud structures
- Gardens → Cloud-floating island aesthetic

Airship Dock:
- Platform → Star Ocean - Cloud Parallax platforms
- Airships → Airship assets from Time Fantasy

Dragon Shrine:
- Exterior → Tengai Makyou Zero - Dragon Shrine (Exterior)
- Interior → Dragon Shrine (Interior)
- Highest point in zone

Sky Palaces:
- Noble quarters → Star Ocean - Astral Castle Town (modified)
- Peacock Shrine → Tengai Makyou Zero - Peacock Shrine

Between Islands:
- Cloud bridges → Cloud tileset
- Fog transitions → Star Ocean - Fog Parallax
```

### Parallax Setup (CRITICAL):
- **Layer 1 (Back)**: Star Ocean - Cloud Parallax 1
- **Layer 2 (Mid)**: Star Ocean - Fog Parallax (lower opacity)
- **Layer 3 (Front)**: Subtle cloud edges

---

## 🌑 VOID ZONE - DETAILED MAPPING

### The Darkness:
```
Void Approach:
- Corrupted lands → Dark Dimension tileset
- Twisted trees → Gloomwood Forest (corrupted tint)

The Remembered City:
- Buildings from erased timelines → Mix of all castle sets (darkened)
- Impossible architecture → Phantom Castle pieces

Void Palace:
- Exterior → Tengai Makyou Zero - Phantom Castle (Entrance)
- Interior → Phantom Castle rooms (Sara's Room, etc.)
- Throne → Dhaos' Castle (Tales of Phantasia)

Void Heart:
- Deepest area → Undead Tileset (cursed land)
- Reality tears → Animated void portals
```

### Visual Effects:
- Darken everything 50%
- Purple/black color scheme
- Void particles (floating motes)
- Reality distortion effects

---

## ⛩️ 12 SHRINES - EXACT LOCATIONS

### Shrine Name | Asset Used | Zone | Element
|--------------|------------|------|---------|
| **Shrine of the Chroma** | Lufia 2 - Shrine to Alunze Kingdom | Uplands | Balance |
| **Shrine of Dust** | Lufia 2 - Small Shrine to Gordovan | Dustbelt | Earth |
| **Shrine of Tides** | Lufia 2 - Small Shrine to Agurio | Tide | Water |
| **Shrine of Flame** | Bakumatsu - Red Shrines | Ember | Fire |
| **Shrine of Frost** | Lufia 2 - Small Shrine to Aleyn | Frost | Ice |
| **Shrine of Storms** | Lufia 2 - Small Shrine to Treadool | Aetherreach | Wind |
| **Shrine of Life** | Lufia 2 - Small Shrine to Dragon Egg | Remnant | Nature |
| **Shrine of Memory** | Lufia 2 - Small Shrine to Parcelyte | Capital | Time |
| **Shrine of Depths** | Submarine Cave Shrine | Tide | Ocean |
| **Shrine of Peaks** | Tengai Makyou Zero - Peacock Shrine | Uplands | Sky |
| **Shrine of Decay** | Rudra no Hihou - Nuad Shrine | Mire | Swamp |
| **Shrine of Purity** | Lennus 2 - Purification Shrine | Void | Purification |

### Shrine Map Template:
```
[Entrance] → [Antechamber] → [Main Hall]
                        ↓
                  [Pedestal Room] ← Boss
                        ↓
                   [Treasure]
```

---

## 🛠️ IMPLEMENTATION PRIORITY

### Week 1: Core Zones
1. **Palace** - Extract throne room, set up final dungeon
2. **Capital Ruins** - Use Louran ruins for main exploration
3. **Uplands** - Set up 12 shrines using Lufia assets

### Week 2: Biomes
4. **Frost** - Ice Cavern tileset + Ice Castle parallax
5. **Ember** - Lava Cavern + Burning Heroes Fire City
6. **Tide** - Harbor of Freedom layout

### Week 3: Advanced
7. **Aetherreach** - Cloud parallax setup
8. **Void** - Dark dimension + undead tilesets
9. **Chrono** - Steampunk tileset implementation

### Week 4: Polish
10. **Remnant** - Gloomwood/Whitewood parallax
11. **Dustbelt** - Arabian Nights integration
12. **Tower** - Multi-floor castle pieces

---

## 📝 EXTRACTION COORDINATES (New Assets)

### For Battle Backgrounds:

**Albert Odyssey 2 - Throne Room:**
```
File: SNES - Albert Odyssey 2 - Maps - Throne Room.png
Extract: (50, 50) to (550, 450)
Output: palace_throne_albert.png
```

**Lufia 2 - Alunze Shrine (Interior):**
```
File: SNES - Lufia 2 - Maps - Shrine to Alunze Kingdom.png
Extract: Center section for shrine interior
Output: uplands_shrine_main.png
```

**Tengai Makyou Zero - Ice Fang Castle:**
```
File: SNES - Tengai Makyou Zero - Maps - Ice Fang Castle.png
Extract: Boss room section
Output: frost_boss_room.png
```

**Burning Heroes - Fire Castle Interior:**
```
File: SNES - Burning Heroes - Maps - Fire Castle (Interior).png
Extract: Throne and main halls
Output: ember_fire_throne.png
```

---

## ✅ FINAL VERDICT

### All Assets Are 100% Usable:

| Asset Category | Quantity | Implementation Status |
|----------------|----------|----------------------|
| Castle Maps | 40+ | Ready for extraction/use |
| Shrine Maps | 15+ | 12 shrines mapped |
| Dungeon Tilesets | 10+ | All zones covered |
| Parallax BGs | 3+ | Zone assignments ready |
| Terrain Objects | 100+ | Decoration ready |

### You Can Build the Entire Game With What You Have.

No additional assets needed. Just extraction, setup, and implementation.

---

*"The assets don't make the game. What you DO with them does."*
