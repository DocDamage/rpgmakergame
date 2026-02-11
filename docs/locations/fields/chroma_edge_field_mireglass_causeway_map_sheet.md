# Chroma's Edge — Mireglass Causeway Micro-Map Sheet (v1)
## Mirewatch → Fungal Depths Transition Zone — "The Swamp is Breathing"

---

## A) Technical Specs

| Parameter | Value |
|-----------|-------|
| **Map Size** | 128 × 72 tiles |
| **Tile Size** | 16×16 px |
| **Full Texture** | 2048×1152 px |
| **Type** | Field micro-map (encounters ON) |
| **Encounter Level Band** | Lv 6–12 (scales to Lv 18 on late revisit) |
| **Time States** | Day / Night (night = thicker fog + Dominion scout risk) |
| **Mounts** | Allowed only after D3; mounted = 0% encounters, but boardwalk choke points keep speed sane |

---

## B) Core Intent

- Provide a clear, readable path from Mirewatch to D2
- Teach the player a "preview" version of Motion/Slipstream behavior
- Add salvage value (filters, salt, spore mats) so it's worth revisiting
- Foreshadow Dominion presence without forcing a combat "raid" in town

---

## C) Visual Identity

### Terrain Mix
- Narrow boardwalk → mud flats → reed channels → sinkhole rim

### Landmarks
- **Fan Totem** (hand-cranked) = Motion foreshadow
- **Salt posts** (keeps fungus back) = town influence thinning out
- **Breathing fissure mist** near dungeon = "lungs below"

### Ambient
- Frog calls
- Wet wood creaks
- Distant exhale sound every ~20 seconds

---

## D) Layout Blocks (Readable Districts)

### 1) Lanternline Gate (Safe Apron)
- **Bounds:** x 52–86, y 0–14
- **Encounters:** OFF for first ~8 tiles from gate
- **Features:** Signposts + tutorial hint objects

### 2) Reed Channel Fork (Main Path Split)
- **Bounds:** x 34–94, y 14–40
- **Two parallel lanes:**
  - **Boardwalk lane:** Safe-ish, longer
  - **Mud lane:** Faster, more hazards + loot

### 3) Fan Totem Rise (Motion Preview Zone)
- **Bounds:** x 10–44, y 22–54
- **Features:** First "push" tiles (gentle Slipstream preview)

### 4) Sinkmouth Edge (Dungeon Threshold)
- **Bounds:** x 0–36, y 48–71
- **Vibe:** Spore fog heavier, salt lines broken, ground looks "soft"
- **Features:** Dungeon entrance clearly framed by roots/stone

---

## E) Entrances / Exits (Edge Triggers)

*Coordinates are local (0–127, 0–71).*

| Direction | Edge Trigger | Destination |
|-----------|--------------|-------------|
| **To Mirewatch Town** | (68, 0) | Mirewatch town interior |
| **To Fungal Depths (D2)** | (0, 60) | Dungeon entrance |
| **To Overworld Swamp Track** (optional bypass) | (127, 32) | Broader overworld connection |

---

## F) Key Anchors & Navigation Props

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Main Signpost Cluster** | (70, 10) | Navigation hub |
| "MIREWATCH" (back) | — | Points east |
| "FUNGAL DEPTHS" (west) | — | Points west |
| "SWAMP TRACK" (east) | — | Points southeast |
| **Fan Totem Landmark** | (28, 34) | Big silhouette; always visible |
| **Salt Post Line** (broken) | starts (44, 50), ends (18, 58) | Visual ramp-up |

---

## G) Mechanics (Micro-Map Version)

### 1) "Slipstream Preview" — Spore Drift Tiles

- **Appear in:** Fan Totem Rise + near Sinkmouth
- **Effect:** Pushes party 1 tile in arrow direction
- **Counterplay:** Stand on **"Anchor Planks"** (marked boards) to resist push

### 2) Hazard Tiles

| Hazard | Effect |
|--------|--------|
| **Leech Pools** | Apply poison buildup (slow, not brutal) |
| **Sinking Mud** | 20% move slow (pure traversal hazard, not damage) |

---

## H) Scripted Events (One-Time + Phase-Based)

### 1) One-Time Tutorial Push (Gentle)

| Parameter | Value |
|-----------|-------|
| **Trigger tile** | (34, 30) |
| **Event** | Wind/exhale pushes party 2 tiles once (non-damaging) |
| **Popup tip** | "Spore Drift pushes movement — use Anchor Planks or reroute." |

### 2) "Breathing Below" Foreshadow (Audio + VFX)

| Parameter | Value |
|-----------|-------|
| **Trigger** | (20, 56) (near broken salt line) |
| **Event** | Fog pulses outward like an exhale; reeds bend late (uncanny) |
| **Optional party line** | "That wasn't wind." |

### 3) Dominion Scout Glimpse (No Forced Combat)

| Parameter | Value |
|-----------|-------|
| **Condition** | Night only, PHASE 1+ |
| **Location** | Silhouette on far boardwalk (92, 18) |
| **Behavior** | If player approaches, disappears into fog (sets tension) |
| **Later revisit** | Can turn into optional mini-elite |

---

## I) Encounters & Zones

### Base Spawn Table (Lv 6–12)

| Enemy | Traits |
|-------|--------|
| **Caplings** | Fast, light "Dizzy" buildup |
| **Mire Leeches** | Poison |
| **Reed Skulkers** | Ambush from edges |
| **Windspores** | Small push + AoE |

### Encounter Zones

| Zone | Bounds | Intensity | Vibe |
|------|--------|-----------|------|
| **Zone A** (light) | x 46–90, y 14–22 | Reed Fork boardwalk | Easy |
| **Zone B** (main) | x 18–60, y 24–54 | Fan Totem Rise | Medium |
| **Zone C** (heavier) | x 0–36, y 52–71 | Sinkmouth Edge | Harder |

---

## J) Salvage / Gathering Nodes (Worth Returning For)

### Always-On Nodes (Respawn per day or per load)

| Node | Location | Contents |
|------|----------|----------|
| **Reed Bundle** | (78, 26) | Crafting fiber |
| **Salt Sack** (small) | (58, 44) | "Salt Line Kit" mat |
| **Glowcap Cluster** | (24, 62) | Antidote ingredient |

### Night-Only Risk Node

| Node | Location | Conditions | Contents |
|------|----------|------------|----------|
| **Washed Crate** | (12, 40) | Night only, PHASE 1+ | Ammo pack + chance for early accessory |

---

## K) Secrets & Shortcuts (Map-Ready)

| Secret | Location | Effect |
|--------|----------|--------|
| **Under-Boardwalk Crawlspace** | (86, 36) → (62, 52) | Bypass leech pool lane |
| **Hidden Note Bottle** | (16, 28) | Lore: clinic mention / "fans keep it from taking us" |
| **Chest** (early) | (40, 60) behind reeds | Mire Filter parts (ties to Mirewatch craft) |

---

## L) Story-State Phases (Set Dressing + Difficulty)

### PHASE 0 — First Time (Pre-D2 Clear)
- Salt line mostly intact
- Drift tiles minimal, leech pools small

### PHASE 1 — Post-Scene 001 Pressure (Dominion Escalation)
- More broken posters on poles
- Night "scout glimpse" active
- Slightly higher encounter rate in Zone C

### PHASE 2 — Post-D2 Relic Seated
- Fans spin steadier, fog thins slightly
- Drift tiles become more predictable (less "random shove")

### PHASE 3 — Post-D3 Mounts Unlocked
- Adds **Hitch Post** near gate (82, 8) (cosmetic + stable behavior)
- Mounted travel suppresses encounters

---

## M) Implementation Notes (So It Plays Clean)

- Keep the dungeon entrance visible from ~10 tiles away (players shouldn't get lost in reeds)
- Drift tiles should never push directly into an unavoidable hazard (always a safe plank option)
- Put loot on the "faster but riskier" mud lane so players learn risk/reward

---

## Quick Reference: Layout Overview

```
                    MIREWATCH TOWN GATE
                    [Exit at (68, 0)]
                           |
         +-----------------+-----------------+
         |                                   |
    LANTERLINE GATE                     SIGNPOSTS (70, 10)
    (Safe Zone)                         "Mirewatch" | "Fungal Depths" | "Swamp Track"
         |                                   |
         v                                   v
    REED CHANNEL FORK (y 14–40)
    +------------------+------------------+
    |                                     |
Boardwalk Lane                        Mud Lane
(safe, longer)                        (fast, hazards + loot)
    |                                     |
    +------------------+------------------+
                       |
                       v
              FAN TOTEM RISE (y 22–54)
              [Fan Totem at (28, 34)]
              First Spore Drift tiles
              Anchor Planks for safety
                       |
                       v
              SINKMOUTH EDGE (y 48–71)
              [Dungeon entrance at (0, 60)]
              Broken salt lines
              Heavy spore fog
              "Breathing" fissure
```
