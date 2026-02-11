# Chroma's Edge — Dusthaven Outskirts Micro-Map Sheet (v1)
## Transition Zone: "First Taste of Orion Outside Safety"

---

## A) Technical Specs

| Parameter | Value |
|-----------|-------|
| Map Size | 128 × 64 tiles |
| Tile Size | 16×16 px |
| Full Texture | 2048×1024 px |
| Type | Field micro-map (encounters ON) |
| Encounter Level Band | Lv 1–6 (scales to Lv 10 on late-game revisit) |
| Mounts | Not available early (pre-D3); after D3, mount allowed and encounter suppression applies |
| Time States | Day / Night (Night adds patrol risk + better loot) |

---

## B) Core Intent

This map is your "first taste of Orion outside safety," with:
- Clear routes to the 4 overworld directions
- 1 tutorial fight trigger (only once)
- 1 salvage loop (spark parts + early craft mats)
- Dominion pressure foreshadow (scouts + posters + a busted broadcast drone)

---

## C) Visual Identity

### Terrain
- Cracked clay flats
- Shallow gullies
- Scrap fences
- Broken pylons

### Landmarks
- **Water tank silhouette** visible behind the town wall (helps orientation)
- **Scrap windmill** (spinning loud, creaky)
- **Crashed Dominion relay drone** (first "Dominion tech in the dirt" object)

### Ambient
- Dust gusts
- Distant generator hum
- Coy scavenger calls

---

## D) Layout (District Blocks)

### 1) Town Gate Apron (Safe-ish)
- **Bounds:** x 54–82, y 2–18
- **Purpose:** Easing out of town, signposts, first salvage prompt
- **Encounters:** OFF in the first 6 tiles from gate

### 2) Scrapyard Flats (Main Combat Lane)
- **Bounds:** x 34–96, y 18–46
- **Purpose:** First random encounters, tutorial "field fight," visible branching paths

### 3) Gully Switchbacks (SE Route to Swamp Track)
- **Bounds:** x 86–127, y 34–63
- **Purpose:** Adds elevation feel with 1-tile chokepoints and a "hidden stash" loop

### 4) Coast Spur Cut (West Exit Lane)
- **Bounds:** x 0–34, y 28–48
- **Purpose:** Short canyon-like cut with scrap barricades and a night-only pick-up

---

## E) Key Anchors & Coordinates

*Coordinates are local (0–127, 0–63).*

### Entrances / Exits (Edge Triggers)

| Direction | Edge Trigger | Destination |
|-----------|--------------|-------------|
| **To Dusthaven Town Gate** | (68, 0) | Town interior |
| **North (Ashveil Road)** | (72, 63) | Overworld |
| **East (Prismridge Road)** | (127, 30) | Overworld |
| **SE (Mirewatch / Swamp Track)** | (120, 63) | Overworld |
| **West (Coast Road Spur)** | (0, 38) | Overworld |

### Signposts (Navigation Clarity)

| Feature | Coordinates | Details |
|---------|-------------|---------|
| **Four-way signpost cluster** | (70, 14) | Navigation aid |
| "ASHVEIL" | — | Points North |
| "PRISMRIDGE" | — | Points East |
| "MIREWATCH" | — | Points Southeast |
| "COAST" | — | Points West |

---

## F) Encounters & Spawn Tables

### Base (Lv 1–6)

| Enemy | Traits |
|-------|--------|
| **Dustjackals** | Fast, low HP |
| **Scrap Mites** | Status: "Rust" = minor atk down |
| **Gully Skulkers** | Ambush from edges |
| **Dominion Scout Pair** | Rare at day, common at night post-Scene 001 |

### Night Variant (Adds)

| Enemy | Traits |
|-------|--------|
| **Relay Hounds** | Dominion-trained beasts |
| **Patrol Drone (damaged)** | Mini-elite |

### Encounter Zones

| Zone | Bounds | Intensity |
|------|--------|-----------|
| **Zone A** (light) | x 52–86, y 16–22 | Town Gate Apron to Flats edge |
| **Zone B** (main) | x 34–96, y 22–46 | Scrapyard Flats |
| **Zone C** (harder early) | x 92–127, y 42–63 | Gully Switchbacks |

---

## G) Scripted Events (One-Time / Story-State)

### 1) First Field Fight Tutorial (ONE-TIME)

| Parameter | Value |
|-----------|-------|
| **Trigger Tile** | (62, 24) — player crosses "scrap fence gap" |
| **Enemies** | 2× Dustjackals + 1× Scrap Mite |
| **Teaching Beats** | Guard, items, basic formation |
| **After Drop** | "Spare Capacitor" or "Bandage Kit" (guaranteed) |

### 2) Dominion Broadcast Drone (Foreshadow)

| Parameter | Value |
|-----------|-------|
| **Object** | Crashed drone at (44, 34) |
| **Interaction** | Plays static + partial Dominion message |
| **State Change** | After Scene 001, message becomes clearer + harsher |
| **Loot** | Relay Scrap (craft mat) |

### 3) "Renna's Trail" Spark Marker (Pre-Recruit Hint)

| Parameter | Value |
|-----------|-------|
| **Marker** | Glowing tool-scratch on a pipe (58, 40) |
| **Flavor Text** | "Someone fixed this fast. Not Dominion." |

---

## H) Salvage / Gathering Nodes

### Always-On Nodes (Respawn per map reload or per day)

| Node | Location | Contents |
|------|----------|----------|
| **Scrap Pile A** | (40, 26) | Metal bits / low chance potion |
| **Scrap Pile B** | (88, 28) | Wires / cloth |
| **Water Barrel Cache** | (98, 18) | 1× water ration (quest item later) |

### Night-Only Node (Risk/Reward)

| Node | Location | Conditions | Contents |
|------|----------|------------|----------|
| **Patrol Drop Crate** | (18, 44) | Night only, post-Scene 001 | Ammo pack + chance for early accessory |

---

## I) Secrets & Mini Shortcuts

| Secret | Location | Effect |
|--------|----------|--------|
| **Gully Crawlspace** | (104, 54) → (92, 44) | 1-tile tunnel bypasses tougher choke |
| **Hidden Stash** | Behind tarp fence (30, 34) | "Old Coin" (vendor sell) + lore note fragment |

---

## J) Story-State Phases (Set Dressing + Difficulty)

### PHASE 0 — Pre-Scene 001
- Fewer signs of Dominion
- Encounters mostly wildlife + mites

### PHASE 1 — Post-Scene 001 (Dominion Broadcast Escalation)
- Adds posters on poles + patrol footprints
- Night spawns include Scout Pair and Damaged Drone

### PHASE 2 — Post-D3 (Mount Unlock)
- Adds **Mount Hitch Post** near Town Gate Apron (78, 10)
- Mounted traversal suppresses encounters (per system rules)

### PHASE 3 — Late Game Return
- Optional elite spawn: **"Hawk Enforcer"** night-only mini-boss (one-time)
- Loot: Cosmetic mount plate / high-tier scrap

---

## K) Audio / VFX Hooks

| Element | Location | Description |
|---------|----------|-------------|
| **Dust Gust VFX** | x 50–90, y 26–30 | Pure visual, no gameplay |
| **Night Hum** | Near crashed drone (44, 34) | Intensifies proximity |
| **Distant Cantina Music** | Gate Apron only | Comfort cue, audible in safe zone |

---

## L) Implementation Notes (So It Plays Clean)

- Keep branch points **visible from the gate apron** (player sees "the world opens")
- Don't clutter the main lane; place scrap piles at edges
- Make gully switchbacks narrow (1–2 tiles) to feel dangerous without being maze-y

---

## M) Quick Reference: Layout Overview

```
                    NORTH EXIT (72, 63)
                          |
                          v
    +---------------------+---------------------+
    |                                         |
WEST|     TOWN GATE APRON (Safe Zone)         |EAST
EXIT|     [Signposts at 70, 14]               |EXIT
(0, |                                         |(127
 38)|              |                          |,30)
    |              v                          |
    |     SCRAPYARD FLATS (Combat Zone)       |
    |     [Drone at 44, 34]                   |
    |     [Tutorial at 62, 24]                |
    |              |                          |
    |    +---------+----------+               |
    |    |                    |               |
    |    v                    v               |
    | COAST SPUR         GULLY SWITCHBACKS    |
    | (West Exit)        (SE Exit)            |
    | [Night Crate]      [Crawlspace]         |
    |                    [Hidden Stash]       |
    +-----------------------------------------+
                          |
                    SE EXIT (120, 63)
```
