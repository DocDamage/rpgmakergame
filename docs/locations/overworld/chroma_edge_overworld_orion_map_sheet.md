# Overworld Map Sheet: Orion (Chroma's Edge)

## 0) Sheet Specs

| Property | Value |
|----------|-------|
| **Tile Scale** | 16Ã—16 px |
| **Overworld Canvas** | 320 Ã— 180 tiles (x 0â€“319, y 0â€“179) |
| **Camera Framing** | 15Ã—9 tiles (engine dependent) |
| **Encounter Policy** | ON in routes, OFF in towns/nodes |
| **Layering** | Base Terrain / Roads / Water / Cliffs / Deco / Nodes / Act-2 Rift Overlay / Postgame Overlay |

---

## 1) Region Bands (Biome Layout)

**Continent Shape:** Long diagonal with coast + northern ice + central ruins

| Region | Location | Key Features |
|--------|----------|--------------|
| **Dustbelt Flats** | SW | Dusthaven start zone |
| **Ashveil Uplands** | W | Sanctuary + D1 (Ruins of Ashveil) |
| **Mirewood Basin** | W-Central | Mirewatch + D2 (Fungal Depths) |
| **Prismrange Highlands** | Central | Prismridge + D3 (Crystal Caverns) |
| **Emberstep Rim** | SE-Central | Cinderstep + D4 approaches (Skyspire Temple) |
| **Tidebreak Coast** | SE | Brinegate + D5 (Abyssal Trench) + Sunken City |
| **Obsidian Rift** | S | D6 (Obsidian Quarry / Molten Core) |
| **Frostmarch Expanse** | N/NW | Gravemark/Rimehold + D7 (Frozen Citadel) + Dragon's Graveyard |
| **Chronolittoral Shelf** | NE | Chronowake + Phase-Lane |
| **Old Lumencrest Ruins** | Far East | Capital chain into endgame (Archive/Crown/Void Nexus/Palace) |

---

## 2) Node Legend (Map Icons)

| Icon | Type | Symbol |
|------|------|--------|
| â— | Town | Blue node |
| â–² | Dungeon | Red node |
| â—† | Shrine | Gold node |
| â¬¡ | Lattice Terminal | White node |
| â¬† | Tower | Purple node |
| âš“ | Port / Sea Gate | Anchor symbol |
| â—‡ | Hidden Area | Grey (appears when discovered) |
| â›” | Major Gate/Barrier | Story lock |

---

## 3) Master Node List

### Starting Arc

| Node | Type | Coordinates | Notes |
|------|------|-------------|-------|
| **Dusthaven** | Town | (48, 132) | Starting town |
| **Dusthaven Outskirts** | Micro | (56, 126) | Tutorial zone |
| **Ashveil Sanctuary** | Town | (72, 112) | First sanctuary |
| **Ruins of Ashveil (D1 - Growth)** | Dungeon | (66, 98) | First dungeon |

### Mire / Growth

| Node | Type | Coordinates | Notes |
|------|------|-------------|-------|
| **Mirewatch** | Town | (92, 92) | Marsh hub |
| **Fungal Depths (D2 - Motion)** | Dungeon | (104, 86) | Motion-themed dungeon |
| **Mirewatch â†’ Fungal Transition** | Micro | (98, 88) | Connector |

### Prism / Light

| Node | Type | Coordinates | Notes |
|------|------|-------------|-------|
| **Prismridge** | Town | (140, 86) | Prism crystal town |
| **Crystal Caverns (D3 â€” Light)** | Dungeon | (156, 92) | Light-themed dungeon |
| **Prismridge â†’ Crystal Micro** | Micro | (148, 90) | Connector |

### Ember / Heat (Catastrophe Trigger After D4)

| Node | Type | Coordinates | Notes |
|------|------|-------------|-------|
| **Cinderstep** | Town | (170, 110) | Volcanic town |
| **Skyspire Temple (D4 - Heat)** | Dungeon | (184, 98) | Heat-themed dungeon |
| **Ember Stair Approach** | Micro | (176, 104) | Connector |

### Tide / Coast

| Node | Type | Coordinates | Notes |
|------|------|-------------|-------|
| **Brinegate Port** | Town | (210, 132) | Coastal port city |
| **Abyss Entry Pier** | Micro | (220, 138) | Submersible dock |
| **Abyssal Trench (D5 â€” Tide)** | Dungeon | (236, 150) | Underwater dungeon |
| **Marinus's Sanctum** | Shrine Node | (224, 124) | Tide Shrine |
| **Sunken City** | Hidden Area | (252, 156) | Reveals later |

### South Rift / Quarry

| Node | Type | Coordinates | Notes |
|------|------|-------------|-------|
| **Obsidian Quarry / Molten Core (D6 - Mass)** | Dungeon | (196, 152) | Mass-themed dungeon |

### Frost / Time

| Node | Type | Coordinates | Notes |
|------|------|-------------|-------|
| **Gravemark Outpost** | Town | (78, 52) | Northern outpost |
| **Rimehold** | Town | (104, 32) | Ice fortress town |
| **Frozen Citadel (D7 â€” Time)** | Dungeon | (112, 18) | Time-themed dungeon |
| **Rimehold â†’ Frozen Micro** | Micro | (110, 26) | Connector |
| **Dragon's Graveyard** | Hidden Area | (64, 18) | Reveals late |

### Chrono Shelf (Phase-Lane)

| Node | Type | Coordinates | Notes |
|------|------|-------------|-------|
| **Chronowake Pier** | Town | (220, 44) | Time port town |
| **Phase-Lane Crossing** | Micro | (236, 38) | Chrono travel hub |
| **Meridian Junction** | Town | (252, 52) | Junction hub |

### Ruined Capital Chain (Endgame Corridor)

| Node | Type | Coordinates | Notes |
|------|------|-------------|-------|
| **Old Lumencrest: Outer Wards** | Town-Style Hub | (282, 86) | Former capital |
| **Grand Boulevard** | Route Micro | (290, 80) | Connector |
| **Archive District** | Dungeon | (300, 74) | Palace dungeon 1 |
| **Crown District Approach** | Route | (306, 66) | Connector |
| **Crown District** | Hub | (310, 58) | Palace district hub |
| **Void Nexus (D8 â€” Shadow Foundation)** | Dungeon | (304, 52) | Shadow palace dungeon |
| **Crown District â†’ Palace Entrance** | Micro | (312, 52) | Connector |
| **Palace Interior** | Dungeon | (316, 46) | Final Palace |
| **Eclipse Confluence** | Map Sheet | (296, 40) | Endgame zone |

### Meta / Postgame

| Node | Type | Coordinates | Notes |
|------|------|-------------|-------|
| **Hundred-Floor Tower** | Node | (260, 62) | Optional challenge tower |
| **Aetherreach** | Sky Town | *(Not on overworld)* | Phase-Lane travel |
| **Remnant Vault** | Postgame Hub | *(Not on overworld)* | Aetherreach Notice Board |

---

## 4) Shrines (Optional, Repeatable Warp Targets)

| Shrine | Name | Element | Coordinates | Location |
|--------|------|---------|-------------|----------|
| â—† | **Pyreheart Reliquary** | Heat | (188, 132) | Near Cinderstep/Obsidian band |
| â—† | **Verdant Covenant Grove** | Growth | (110, 96) | Mire belt |
| â—† | **Prismwrit Chapel** | Light | (150, 72) | Prism ridge spur |
| â—† | **Kinetic Vow Atrium** | Motion | (172, 86) | Skyspire route shelf |
| â—† | **Gravestone Monad** | Mass | (72, 42) | Near Gravemark |
| â—† | **Chronicle Loom** | Time | (210, 34) | Near Chronowake cliffwalk |
| â—† | **Umbral Ledger** | Shadow | (276, 92) | Lumencrest undercroft spur |
| â—† | **Marinus's Sanctum** | Tide | (224, 124) | Coast (also listed above) |

---

## 5) Route IDs (Roads / Paths / Sea Lanes)

### Act 1 Ground Routes

| ID | Route | Notes |
|----|-------|-------|
| **R01** | Dusthaven â†” Dusthaven Outskirts â†” Ashveil Road | Starting route |
| **R02** | Ashveil â†” Ruins of Ashveil (D1) | First dungeon access |
| **R03** | Ashveil â†” Mirewatch Marshroad | Unlocks after intro |
| **R04** | Mirewatch â†” Fungal Depths (Micro connector) | D2 access |
| **R05** | Mirewatch â†” Prismridge Ridgepath | Unlocks after D1 |
| **R06** | Prismridge â†” Crystal Caverns (Micro connector) | D3 access |
| **R07** | Prismridge â†” Cinderstep Switchbacks | Unlocks after D2 |
| **R08** | Cinderstep â†” Ember Stair Approach â†” Skyspire Temple (D4) | D4 access |

### Coast / Tide Routes

| ID | Route | Notes |
|----|-------|-------|
| **R09** | Cinderstep â†” Brinegate Coastal Road | Coastal highway |
| **S01** | Brinegate â†” Abyss Entry Pier | Sea Lane |
| **S02** | Abyss Entry Pier â†” Abyssal Trench | Deep Lane (requires Submersible) |

### South Rift / Quarry

| ID | Route | Notes |
|----|-------|-------|
| **R10** | Cinderstep â†” Obsidian Quarry (D6) | D6 Mass dungeon access |

### North / Frost / Chrono

| ID | Route | Notes |
|----|-------|-------|
| **R11** | Ashveil â†” Gravemark Pass | Locked until midgame |
| **R12** | Gravemark â†” Rimehold Iceway | Northern route |
| **R13** | Rimehold â†” Frozen Citadel (Micro connector) | D7 access |
| **R14** | Rimehold â†” Chronowake Shelf Road | Time route |
| **R15** | Chronowake â†” Phase-Lane Crossing (Micro) â†” Meridian Junction | Chrono highway |
| **R16** | Meridian â†” Old Lumencrest (ruins corridor) | Endgame approach |
| **R17** | Lumencrest â†” Archive District â†” Crown District chain | Route-micros |
| **R17a** | Old Lumencrest -> Grand Boulevard | `chroma_edge_route_micro_r17a_old_lumencrest_to_grand_boulevard.md` |
| **R17b** | Grand Boulevard -> Archive entry | `chroma_edge_route_micro_r17b_grand_boulevard_to_archive_entry.md` |
| **R17c** | Archive District approach | `chroma_edge_route_micro_r17c_archive_district_approach.md` |
| **R17d** | Crown District approach | `chroma_edge_route_micro_r17d_crown_district_approach.md` |
| **R17e** | Crown hub connector | `chroma_edge_route_micro_r17e_crown_hub_connector.md` |
| **R17f** | Palace entrance micro | `chroma_edge_route_micro_r17f_palace_entrance_micro.md` |

---

## 6) Progression Gates

### Act 1 Locks

| Lock | Condition |
|------|-----------|
| R03 opens | After Dusthaven intro ("leave town" flag) |
| R05 opens | After D1 completion |
| R07 opens | After D2 completion |
| R08 access | After D3 completion |
| Sea Lane S01 | After Brinegate main quest arrival |
| Deep Lane S02 | After Submersible / Tide clearance |

### The Big Shift (After D4 â€” Catastrophe)

**Apply Act 2 Rift Overlay:**

| Effect | Details |
|--------|---------|
| New rifts | Appear on several routes |
| Warped roads | Some roads crack/warp (short detours or micro-maps) |
| Monster surge | New encounter tables on affected routes |
| Unlock R11 | North pass opens |
| Unlock R16 | East ruins corridor opens |

### Endgame Corridor Locks

| Lock | Condition |
|------|-----------|
| Old Lumencrest â†’ Archive â†’ Crown | Opens during Act 2 |
| Void Nexus / Palace | After Archive/Crown story beats |

---

## 7) Fast Travel Network (Warp Sigils)

**Rule:** Every town + every shrine grants a Warp Sigil after first arrival (or shrine clear).

### Always Available Warp Hubs

- Dusthaven, Ashveil, Mirewatch, Prismridge, Cinderstep, Brinegate
- Gravemark, Rimehold, Chronowake, Meridian
- Old Lumencrest, Crown District

### Late Unlock

| Condition | Effect |
|-----------|--------|
| After Catastrophe | Allow warping from anywhere when not in "blocked route state" |

---

## 8) Endgame Overworld Changes (Overlay Plan)

### Act 2 Rift Overlay (Post D4)

| Change | Routes Affected |
|--------|-----------------|
| **Rift Tears** | R05, R07, R09, R12, R16 |
| **Warped Zone encounters** | New tables on rift segments |
| **New shortcut** | Collapsed wall becomes passable (world feels reconfigured) |

### Post-Progenitor / Final Palace Clear

| Change | Effect |
|--------|--------|
| **Suppress random rifts** | Reduce visual noise |
| **Leave "scar lines"** | World history markers |
| **Enable Aetherreach route** | Phase-Lane terminal access |
| **Enable Remnant Vault** | Aetherreach Notice Board access |
| **Optional reveals** | Sunken City / Dragon's Graveyard discoverable if not found |

---

## 9) Coordinate Quick Reference

### Act 1 Cluster (SW-Central)
```
Dusthaven: (48, 132)      Ashveil: (72, 112)        D1: (66, 98)
Mirewatch: (92, 92)       D2: (104, 86)            Prismridge: (140, 86)
D3: (156, 92)             Cinderstep: (170, 110)    D4: (184, 98)
```

### Coast / Tide (SE)
```
Brinegate: (210, 132)     Tide Shrine: (224, 124)   D5: (236, 150)
Sunken City: (252, 156)   D6: (196, 152)
```

### North / Frost (N-NW)
```
Gravemark: (78, 52)       Rimehold: (104, 32)       D7: (112, 18)
Dragon's Graveyard: (64, 18)
```

### Chrono / Endgame (NE-E)
```
Chronowake: (220, 44)     Phase-Lane: (236, 38)     Meridian: (252, 52)
Tower: (260, 62)          Lumencrest: (282, 86)     Crown: (310, 58)
Palace: (316, 46)         Eclipse: (296, 40)
```

### Shrine Ring
```
Heat: (188, 132)          Growth: (110, 96)         Light: (150, 72)
Motion: (172, 86)         Mass: (72, 42)            Time: (210, 34)
Shadow: (276, 92)         Tide: (224, 124)
```

---

## 10) Implementation Notes

- **Node distances:** Designed for ~15â€“30 seconds travel between adjacent nodes
- **Random encounters:** Only on route segments, not at node centers
- **Hidden areas:** Use grey â—‡ until `AREA_DISCOVERED` flag set
- **Rift overlay:** Visual layer toggle, doesn't change base terrain
- **Shrines:** Grant warp immediately on discovery, blessing after clear
- **Postgame overlays:** Applied via map shader/tint layers, not geometry changes

