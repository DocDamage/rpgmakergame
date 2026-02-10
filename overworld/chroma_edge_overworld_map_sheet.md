# Chroma's Edge — Overworld Map Sheet (v1)
## Build-Ready Layout for Orion

---

## A) Technical Specs (Locked)

| Parameter | Value |
|-----------|-------|
| Map Size | 256 × 256 tiles |
| Tile Size | 16×16 px |
| Full Texture | 4096 × 4096 px |
| Streaming | 16×16 tile chunks |
| Load Distance | 3×3 chunks around player |
| Overworld Terminals | 5 spine nodes + 1 per town |
| Mount Rule | 0% encounter rate while mounted |
| Mount Restriction | No mounts in Chroma Tower / Final Palace |

---

## B) Global Coordinate System

- **(0,0)** = top-left corner
- Coordinates below are anchor points (tile coords)
- Safe adjust range: ±5–10 tiles during art pass

---

## C) Macro Regions (Biome Blocks)

### 1) Ashwold Shelf (Starting Continent | Lv 1–30)
- **Bounds:** x 0–140, y 90–210
- **Theme:** Frontier badlands, swamps, first Growth pockets
- **Primary Roads:** Badlands Road, Swamp Road, Northern Approach Road
- **Hazards:** Motion jitter (wind wrong), Growth creep near Ashveil
- **Purpose:** Onboarding, first 3 dungeons, mounts unlock

### 2) Lumencrest Expanse (Eastern Continent | Lv 30–60)
- **Bounds:** x 140–255, y 90–200
- **Theme:** Bright mountains, heat vents, Dominion choke points
- **Hazards:** Heat mirage lanes, Light glare zones
- **Purpose:** Skyspire access, midgame economy, port travel

### 3) Rimechain Isles (Northern Isles | Lv 60–100)
- **Bounds:** x 110–220, y 0–80
- **Theme:** Cold + Time "stutter weather"
- **Travel:** Ferry route from east ports (or late-game flight)
- **Purpose:** Frozen Citadel chain, Time pedestal lead-in

### 4) Sable Expanse (Southern Wastes | Lv 100–150)
- **Bounds:** x 70–220, y 200–255
- **Theme:** Gravity scars, quarry states, Dominion blacksites
- **Hazards:** Mass pressure zones (slow tiles), rockfall events
- **Purpose:** Obsidian Quarry / Molten Core, heavy crafting loop

### 5) Progenitor Ring ("The Crown") (Endgame Approach Zone)
- **Bounds:** Centered near x 150, y 85 (ring radius ~18 tiles)
- **Theme:** "Too clean" ancient structure, reality feels audited
- **Access:** After Frozen Citadel route; Tower Gate unlock after Void Nexus
- **Purpose:** Eternal Hourglass + Chroma Tower Gate

### 6) Aetherreach (Sky Town) (Hidden | Lv 150+)
- **Note:** Not on base ground layer (separate sky layer map)
- **Access:** Aerial mount unlock (suggested: after Tower Floor 50 checkpoint)

---

## D) Overworld Anchors: Towns (12)

Each town includes: Terminal, Inn, Shops, Quest Board, Base Point

### Ashwold Shelf (4)

**Dusthaven** — (64, 156)
- Starting hub (Cantina + Scrap Garage nearby)
- Exits: N to Ashveil / E to Prismridge / SE to Mirewatch / W to coast road

**Ashveil Sanctuary** — (58, 112)
- Growth refuge town (first "sanctuary feel")
- Near: Ruins of Ashveil entrance

**Mirewatch** — (86, 178)
- Swamp boardwalk town; medicine + fungus trade
- Near: Fungal Depths approach

**Prismridge** — (118, 150)
- Crystal mining town; glow-dust economy; taming culture starts here after D3

### Lumencrest Expanse (3)

**Cinderstep** — (176, 140)
- Heat-vent foothill town; resist gear + mount upgrades

**Brinegate Port** — (228, 172)
- Stormbreak docks; aquatic travel vendor, deep-diving sidequests

**Halcyon Freeport** — (200, 190)
- Neutral rebuild hub; becomes postgame mission board HQ

### Rimechain Isles (2)

**Chronowake Pier** — (190, 58)
- Shipyard built around time glitches; ferry hub

**Rimehold** — (152, 36)
- Ice-fort fishing town; "time-sick" NPC quests

### Sable Expanse (2)

**Meridian Junction** — (148, 214)
- Rail-crossroads megahub; factions collide; last big resupply before Ring

**Gravemark Outpost** — (108, 236)
- Quarry settlement; mass gear; heavy crafting

### Hidden Sky Town (1)

**Aetherreach** — (Sky Layer: center anchor equivalent to ~170, 60)
- Floating terraces; sky-market; late-game gear, superboss hints

---

## E) Main Story Dungeons (8) + Entrances

| Dungeon | Foundation | Coordinates | Access Notes |
|---------|------------|-------------|--------------|
| **Ruins of Ashveil** | Growth | (54, 108) | Early; connects to Ashveil Sanctuary |
| **Fungal Depths** | Motion | (92, 186) | Via Swamp Road from Dusthaven/Mirewatch |
| **Crystal Caverns** | Light | (134, 146) | Via Canyon Pass; mount/taming unlock after boss |
| **Skyspire Temple** | Heat | (196, 118) | Requires reaching Cinderstep; heat prep recommended |
| **Abyssal Trench** | Tide | Entry pier (28, 176) | Via Western Coastline; deep sections need aquatic mount |
| **Obsidian Quarry/Molten Core** | Mass | (102, 246) | Via Gravemark Outpost; fire-resist for deep floors |
| **Frozen Citadel** | Time | (176, 18) | Via Rimechain Isles ferry + cold gear |
| **Void Nexus** | Shadow | (122, 126) | Shadow Border region; late game; unlocks Tower Gate |

**Shrine/Pedestal Site:**
- **Marinus's Sanctum** — (18, 186) — Tide pedestal location

---

## F) Hidden Areas (5) — Placement + Gating

| Area | Coordinates | Unlock Requirements |
|------|-------------|---------------------|
| **Ancient Library** | (162, 132) | Puzzle key from Prismridge + Light pedestal effects |
| **Dragon's Graveyard** | (86, 252) | Mass gear + optional boss chain |
| **Sunken City** | (10, 210) offshore | Aquatic mount (Brinegate vendor or Tide progression) |
| **Celestial Observatory** | Sky Layer near Aetherreach | Aerial mount + "stargazing" minigame |
| **Primordial Grove** | (40, 96) | Growth stabilization + postgame tame questline |

---

## G) Overworld Lattice Terminals (5) (Fast Travel)

Towns have their own terminals. These 5 are the big "spine" nodes.

| Terminal | Coordinates | Region |
|----------|-------------|--------|
| **Half-Buried Terminal** | (104, 132) | Canyon Pass (central spine) |
| **Coastline Terminal** | (34, 170) | Western Coastline |
| **Mountain Relay Terminal** | (170, 120) | Lumencrest ridge |
| **Wastes Terminal** | (122, 232) | Sable Expanse |
| **Ring Gate Terminal** | (148, 96) | Progenitor Ring approach |

**Rule:** Fast travel only between activated terminals.

---

## H) World Boss Roam Zones

### ODIN — The Dark Rider (Lv 80)
- **Roam Zone:** Rectangle x 60–110, y 120–165 (plains)
- **Behavior:** Large sprite chase; faster than early mounts

### ULTIMA WEAPON — Ancient Destroyer (Lv 140)
- **Roam Zone:** Rectangle x 145–210, y 90–140 (mountains)

---

## I) Major Route Network

### Roads (Ground)

| Route | Path |
|-------|------|
| **Badlands Road** | Dusthaven ↔ Prismridge ↔ Meridian Junction |
| **Swamp Road** | Dusthaven ↔ Mirewatch ↔ Fungal Depths |
| **Northern Approach Road** | Dusthaven ↔ Ashveil Sanctuary ↔ Ruins of Ashveil |
| **Eastern Mountains Road** | Prismridge ↔ Canyon Pass ↔ Crystal Caverns ↔ Cinderstep |
| **Coast Road** | Dusthaven west spur ↔ Western Coastline ↔ Abyssal Trench pier |
| **Wastes Haul Route** | Meridian Junction ↔ Gravemark Outpost ↔ Obsidian Quarry |

### Sea Travel

| Route | Path |
|-------|------|
| **Ferry Route** | Brinegate Port ↔ Chronowake Pier (Rimechain access) |
| **Halcyon Shuttle** | Halcyon ↔ Chronowake (cheaper, slower, more encounters if unmounted) |

### Sky Travel

| Route | Path |
|-------|------|
| **Aerial Routes** | Aetherreach, Celestial Observatory, shortcut lanes over mountains/wastes |
| **Unlock:** Tower Floor 50 checkpoint |

---

## J) Progression Gates (Story-Lock Summary)

| Checkpoint | Unlocks |
|------------|---------|
| **Start** | Dusthaven region only (Ashwold mid-band) |
| **After D1 (Growth)** | North routes stabilize; Ashveil sidequests open |
| **After D2 (Motion)** | Swamp Road shortcuts; fewer "wind wrong" hazards |
| **After D3 (Light)** | Taming + Luminous Strider (0% encounters mounted) |
| **After D4 (Heat)** | Heat-vent crossings; "Lava Strider" traversal opens |
| **After D5 (Tide)** | Underwater nodes; Sunken City access |
| **After D6 (Mass)** | Deep Sable Expanse; Dragon's Graveyard feasible |
| **After D7 (Time)** | Progenitor Ring access (Eternal Hourglass sequence) |
| **After D8 (Shadow)** | Progenitor Ring Gate → Chroma Tower entry |
| **After Tower F50** | Aerial mount unlock (Aetherreach + sky content) |

---

## K) Quick ASCII Macro Map

```
(0,0)
      RIMECHAIN ISLES (Time)
        [Rimehold]      [Chronowake Pier]----(FERRY)----[Brinegate Port]
             \               |                         /
              \        [Frozen Citadel]               /
               \___________ICE/SEA___________________/

  ASHWOLD SHELF (Start)                       LUMENCREST (Heat/Light)
 [Ashveil]--[Ruins]                               [Cinderstep]--[Skyspire]
     |                                            /
 [Dusthaven]---[Prismridge]---[Crystal Caverns]---/
     |    \                 (Half-Buried Terminal)
 [Mirewatch]--[Fungal Depths]
     |
 (west spur)--> Western Coastline --> Abyssal Trench pier --> Marinus's Sanctum

                 [Meridian Junction]  (rail crossroads)
                        |
                 [Gravemark Outpost]----[Obsidian Quarry/Molten Core]
                        |
                  SABLE EXPANSE (Mass)

          Shadow Border -> [Void Nexus] -> Progenitor Ring Gate -> Chroma Tower
                                      (Ring Gate Terminal)

Sky Layer (later): [Aetherreach] + [Celestial Observatory]
```

---

## L) Encounter Zone Tiers

| Region | Lv Range | Encounter Types |
|--------|----------|-----------------|
| Ashwold Shelf | 1–30 | Feral wildlife, Dominion scouts, bandits |
| Lumencrest Expanse | 30–60 | Heat beasts, Foundry zealots, light phantoms |
| Rimechain Isles | 60–100 | Time-echoes, frost wraiths, cult remnants |
| Sable Expanse | 100–150 | Gravity thralls, mass horrors, Dominion blacksites |
| Progenitor Ring | 100+ | Protocol constructs, reality aberrations |
| Aetherreach (Sky) | 150+ | Sky predators, lost constructs, superbosses |

---

## M) Visual Biome Summary (Art Direction Notes)

| Region | Palette | Key Visuals |
|--------|---------|-------------|
| Ashwold Shelf | Browns, muted greens, rust | Scrap piles, dead trees, frontier ruins |
| Lumencrest Expanse | Bright golds, harsh whites, deep reds | Sun-bleached stone, heat shimmer, crystal outcroppings |
| Rimechain Isles | Ice blues, pale grays, aurora greens | Frozen fjords, time-flicker effects, whale-oil lamps |
| Sable Expanse | Deep blacks, glowing orange seams, ash grays | Gravity scars, floating rocks, industrial wreckage |
| Progenitor Ring | Clean whites, geometric golds, lattice blues | Ancient stone, perfect symmetry, reality "hum" |
| Aetherreach | Sky blues, cloud whites, sunset golds | Floating terraces, wind-torn cloth, distant horizons |
