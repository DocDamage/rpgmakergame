# Chroma's Edge — Prism Mine Approach Micro-Map Sheet (v1)
## Prismridge → Crystal Caverns Transition Zone — "Industrial Spine"

---

## A) Technical Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 144 × 72 tiles |
| **Tile Size** | 16×16 px |
| **Full Texture** | 2304×1152 px |
| **Type** | Field micro-map (encounters ON) |
| **Encounter Band** | Lv 12–18 (scales to Lv 26 on revisit) |
| **Time States** | Day / Night (night = fewer miners, more "watchers") |
| **Mounts** | Pre-D3: No mounts (stable locked); Post-D3: Mounts allowed, mounted = 0% encounters |

---

## B) Core Intent

- Clean, readable route from town to dungeon
- Preview Light mechanics: hidden walkway reveal + glare hazard
- Give Prismridge "mining town" texture: scaffolds, carts, permits, inspectors
- Provide 1 optional loop with loot + lore (Dominion "survey" angle)

---

## C) Visual Identity

### Terrain
- Carved stone path + scaffold catwalks + crystal dust drifts

### Landmarks
- **Mine Gate Arch** with permit board
- **Crystal Sluice Channel** running alongside path (glows)
- **Collapsed Catwalk** (forces tiny detour)
- **Beam Emitter Pylon** (first "Light reveals reality" moment)

---

## D) Layout Blocks (Districts)

### 1) Mineworks Gate (Safe Apron)
- **Bounds:** x 60–96, y 0–16
- **Encounters:** OFF for first ~8 tiles
- **Features:** Permit board + guard booth + clear signposting

### 2) Scaffold Spine (Main Route)
- **Bounds:** x 40–120, y 16–44
- **Features:** Straightforward lane with catwalk branches

### 3) Sluice Bend (Glare Preview)
- **Bounds:** x 78–144, y 34–72
- **Features:** Bright reflective crystals = first Glare tiles (soft hazard)

### 4) Collapsed Catwalk Loop (Optional Loot)
- **Bounds:** x 0–44, y 26–58
- **Features:** Short loop: risk/reward + first hidden bridge reveal

---

## E) Entrances / Exits (Edge Triggers)

*Local coords (0–143, 0–71).*

| Direction | Edge Trigger | Destination |
|-----------|--------------|-------------|
| **To Prismridge Town** (Mineworks Gate) | (78, 0) | Prismridge town interior |
| **To Crystal Caverns (D3)** | (143, 56) | Dungeon entrance |
| **To Overworld** (optional bypass) | (0, 12) | Late unlock (locked until midgame) |

---

## F) Key Anchors & Navigation Props

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Signpost Cluster** | (80, 10) | Navigation hub |
| "PRISMRIDGE" (back) | — | Points west |
| "MINEWORKS" (forward) | — | Points east |
| "CRYSTAL CAVERNS" (east) | — | Points east |
| **Permit Board Prop** | (86, 6) | Flavor; changes with Dominion pressure |
| **Beam Emitter Pylon** (tutorial) | (58, 38) | Light tutorial |
| **Hidden Bridge Reveal Strip** | x 64–70, y 40 | Invisible until beam hits |
| **Dominion Survey Marker Stakes** | x 104–130, y 18–30 | Phase-based |

---

## G) Mechanics (Micro-Map Version)

### 1) Hidden Walkway Reveal (Light Tutorial)

- **Player interacts with:** Beam Emitter Pylon (58, 38)
- **Effect:** Beam sweeps wall and reveals hidden crystal plank bridge for 20 seconds (or until crossed)
- **Purpose:** Teach D3's core language before the dungeon

### 2) Glare Tiles (Soft Hazard Preview)

- **Location:** Sluice Bend
- **Effect:** Reflective ground builds Blinded slowly
- **Counterplay:** Walk on **Shade Boards** (darker planks) placed as safe lanes

---

## H) Scripted Events (One-Time + Phase-Based)

### 1) One-Time "Light Selects" Moment

| Parameter | Value |
|-----------|-------|
| **Trigger** | (62, 34) (approach pylon) |
| **Event** | Beam flickers; glyphs appear briefly; hidden bridge becomes visible |
| **Popup tip** | "Light can reveal hidden paths." |

### 2) Collapsed Catwalk Detour (Traversal Lesson)

| Parameter | Value |
|-----------|-------|
| **Trigger** | (34, 44) (broken walkway) |
| **Event** | Player must go down one ramp and back up (terrain matters) |

### 3) Dominion Inspector Beat (Non-Combat Tension)

| Parameter | Value |
|-----------|-------|
| **Condition** | Night only, PHASE 1+ (after early Dominion escalation) |
| **Location** | Surveyor silhouette at (98, 12) near permit board |
| **Behavior** | Short dialogue: "Permits updated. Don't wander." Then leaves |

---

## I) Encounters & Spawn Tables

### Base Spawn Table (Lv 12–18)

| Enemy | Traits |
|-------|--------|
| **Shard Crawlers** | Defense up in bright zones |
| **Gleam Bats** | Blinded buildup |
| **Prism Wisps** | Element shift / resist trick |
| **Dominion Surveyor Drone (Damaged)** | Mini-elite (PHASE 1+) |

### Encounter Zones

| Zone | Bounds | Intensity | Vibe |
|------|--------|-----------|------|
| **Zone A** (light) | x 52–112, y 18–34 | Scaffold Spine mid-lane | Easy |
| **Zone B** (main) | x 88–144, y 40–70 | Sluice Bend | Higher glare + more bats |
| **Zone C** (optional harder) | x 0–40, y 30–56 | Collapsed Catwalk Loop | Harder |

---

## J) Salvage / Gathering Nodes (Replay Value)

### Always-On Nodes (Respawn per day or reload)

| Node | Location | Contents |
|------|----------|----------|
| **Crystal Dust Pile** | (112, 46) | Craft mat (lens polish) |
| **Wire Bundle** | (46, 22) | Basic tech mat |
| **Lens Fragment** | (26, 52) | Accessory craft component |

### Night-Only Risk Node

| Node | Location | Conditions | Contents |
|------|----------|------------|----------|
| **Inspector Drop Crate** | (120, 20) | Night only, PHASE 1+ | Ammo pack + chance "Glare Salve" |

---

## K) Secrets & Optional Loops

### 1) Hidden Bridge → Facet Nook

- **Reveal bridge at:** x 64–70, y 40
- **Leads to:** Small nook with chest at (18, 46)
- **Chest contents:** "Prism Charm" (or Lens Cloth + ether drop)
- **Lore Note:** "Light isn't truth. It's access."

### 2) Under-Scaffold Crawlspace (Fast Return Shortcut)

- **Entrance:** (74, 30)
- **Exit:** (54, 18)
- **Purpose:** Dodge glare zone if player prefers (accessibility)

---

## L) Story-State Phases (Set Dressing + Difficulty)

### PHASE 0 — First Approach (Pre-D3)
- Miners present, town feels industrious
- Beam pylon tutorial is clean and friendly
- Minimal Dominion signage

### PHASE 1 — Dominion Pressure Rising
- Permit board has harsher language
- Survey stakes appear
- Night inspector silhouette event active

### PHASE 2 — Post-D3 (Mount Unlock)
- Stable banners visible from gate
- Mounted travel suppresses encounters
- "Prism Stag" icon painted near Mine Gate (celebration)

### PHASE 3 — Mid/Late Revisit
- More drones at night
- Optional mini-elite: "Facet Guardian Scout" appears in Zone C once

---

## M) Implementation Notes (So It Plays Clean)

- Make D3 entrance visible from ~12–15 tiles away (player should always feel the pull forward)
- Glare tiles should be avoidable via shade boards (don't force Blinded)
- Keep tutorial beam reveal unmissable (place pylon directly on main spine)

---

## Quick Reference: Layout Overview

```
                    PRISMRIDGE TOWN GATE
                    [Exit at (78, 0)]
                           |
              PERMIT BOARD (86, 6)
              SIGNPOSTS (80, 10)
              "Prismridge" | "Mineworks" | "Crystal Caverns"
                           |
                           v
              MINEWORKS GATE (Safe Zone)
              (y 0–16, encounters OFF)
                           |
                           v
              SCAFFOLD SPINE (Main Route)
              (y 16–44, x 40–120)
              Beam Pylon (58, 38) → Hidden Bridge Reveal
                           |
              +------------+------------+
              |                         |
        Collapsed Loop            SLUICE BEND
        (x 0–44, y 26–58)         (x 78–144, y 34–72)
        [Optional loot]           [Glare tiles]
        [Facet Nook at (18,46)]   [Shade Boards for safety]
              |                         |
              +------------+------------+
                           |
                           v
              CRYSTAL CAVERNS (D3) ENTRANCE
              [Edge trigger at (143, 56)]
```
