# Chroma's Edge — Prismridge Town Map Sheet (v1)
## Crystal-Mining Town — "Visibility Can Be a Weapon"

---

## A) Technical Specs

| Parameter | Value |
|-----------|-------|
| **Town Map Size** | 112 × 104 tiles |
| **Tile Size** | 16×16 px |
| **Full Texture** | 1792×1664 px |
| **Encounter Rate** | 0% (safe zone) |
| **Time States** | Day / Night |
| **Town Terminal** | Yes (polished, semi-functional, "public-facing") |
| **Mounts** | Allowed after D3; stable system lives here |
| **Readability Rule** | Keep main boulevard very clear (organized vs Dusthaven/Mirewatch) |

---

## B) Visual Identity (Art Direction)

### Materials
- Pale stone
- Crystal inlays
- Metal braces
- Mining scaffolds
- Glass awnings

### Palette
- White stone + pastel prismatic highlights
- Cool blue neon
- Warm lanterns at night

### Signature Props
- **Refraction streetlamps** (split light into colors on pavement)
- **Dust masks** on NPCs (mining reality)
- **Prism banners** (almost propaganda vibes)
- **Crystal sluice canal** (shallow channel that glows)

---

## C) Town Layout (District Blocks)

### District 1 — Prism Boulevard (Main Spine)
- **Bounds:** x 34–80, y 16–80
- **Vibe:** The "clean" main street: shops, NPC chatter, story beats
- **Feature:** Refraction lamps form a natural path line

### District 2 — Market Steps
- **Bounds:** x 54–96, y 64–102
- **Vibe:** Tiered stalls: supplies, lens parts, crystal trade, accessories

### District 3 — The Stable Yard (Mount Hub)
- **Bounds:** x 10–34, y 52–88
- **Vibe:** Locked pre-D3 (looks like closed corral)
- **After D3:** Becomes mount system base

### District 4 — Mineworks Gate (Industry / D3 Access)
- **Bounds:** x 78–112, y 8–44
- **Vibe:** Scaffolds + carts + crystal dust in sunbeams
- **Leads to:** Crystal Caverns (D3) approach route

### District 5 — Lenswright Row (Tech + Upgrades)
- **Bounds:** x 6–34, y 16–50
- **Vibe:** Small workshops with glass, prisms, calibration rigs

### District 6 — Ridge Residences
- **Bounds:** x 34–56, y 80–104
- **Vibe:** Quiet, "working town" homes; human cost of mining

---

## D) Key Anchors & Coordinates (Local 0–111, 0–103)

### Main Spawn Points

| Spawn | Location | Coordinates | Context |
|-------|----------|-------------|---------|
| **SPAWN A** | Arrival from overworld / Dusthaven road | (56, 98) | Market Steps base |
| **SPAWN B** | Arrival from Mineworks / D3 return | (96, 34) | Mineworks Gate interior |
| **SPAWN C** | Arrival from Cinderstep route later | (111, 60) | East edge boulevard |

### Town Terminal

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Prismridge Lattice Terminal** | (24, 28) | "Public terminal" vibe: clean housing, faint static at night |
| **After D3** | — | Adds Gleam Sense tutorial and "Light anomalies detected" flavor pings |

### Exits (Edge Triggers)

| Direction | Edge Trigger | Destination |
|-----------|--------------|-------------|
| **To Overworld — West** (Dusthaven road) | (0, 74) | Dusthaven route |
| **To Overworld — East** (Cinderstep / Mountains) | (111, 60) | Cinderstep route |
| **To Overworld — South** (Meridian Junction) | (54, 103) | Locked until midgame gate |
| **To Crystal Caverns (D3)** | (111, 20) | Mineworks Gate corridor |

---

## E) Main Buildings (Exterior Door Tiles)

| Building | Door Coordinates | Function |
|----------|------------------|----------|
| **Inn ("The Glass Lullaby")** | (60, 86) | Rest/save |
| **General Goods ("Stone & Shine")** | (72, 82) | Supplies |
| **Lenswright Shop ("Refraction Works")** | (22, 40) | Tech/accessories |
| **Weapons/Mining Tools ("Pick & Edge")** | (84, 76) | Tools/upgrades |
| **Clinic ("Clearwater Station")** | (46, 86) | Medical |
| **Stable HQ ("Prism Corral")** [Mount Hub] | (18, 70) | Mount system base |
| **Beast Handler Office** (post-D3) | (12, 78) | Taming contracts |
| **Quest Board** | (64, 72) | Market Steps |
| **Foreman Office** (Mineworks) | (96, 20) | Story beats + mining permits |

---

## F) Interior Maps (Required)

### 1) Inn — The Glass Lullaby
- **Interior Size:** 32×22
- **Entry Pad:** (16, 20)
- **Vibe:** Soft light prisms on walls, quiet music, "rest in brightness" tone

### 2) Refraction Works (Lenswright / Tech Shop)
- **Interior Size:** 34×22
- **Entry Pad:** (17, 20)
- **Services:** Accessories, Light resist crafts, beam-trap utility items later
- **Signature Prop:** Calibration bench (holographic light lines)

### 3) Prism Corral (Stable HQ)
- **Interior Size:** 36×26
- **Entry Pad:** (18, 24)
- **Pre-D3:** Closed / minimal
- **Post-D3:** Full stable UI + mount roster + cosmetics + "Bond" upgrades

### 4) Foreman Office (Mineworks)
- **Interior Size:** 28×18
- **Entry Pad:** (14, 16)
- **Function:** Story quests, D3 warnings, Dominion "survey permit" tension

### 5) Clearwater Station (Clinic)
- **Interior Size:** 30×20
- **Entry Pad:** (15, 18)
- **Services:** Cures Blinded, Bleed (shard floors), general supplies

---

## G) Shops + Services (Inventory by Progress)

### Base (First Visit / Pre-D3 Clear)

| Shop | Inventory |
|------|-----------|
| **General Goods** | Potions, antidotes, smoke bomb, basic accessories |
| **Pick & Edge** | Early weapon upgrades + mining-tool cosmetics |
| **Clinic** | Cures poison + minor status (limited) |
| **Lenswright** | "Glare Salve" (reduces blinded buildup for X battles) |

### After D3 Clear + Light Relic Seated (Major Upgrade)

| Change | Details |
|--------|---------|
| **Stable unlock** | Mounts + taming kits + saddle cosmetics |
| **Lenswright expands** | Beam-trap diffusers, Prism Charm upgrades, secret-reveal items |
| **Clinic expands** | Blinded cure becomes cheap; adds "Lensguard Wraps" |
| **Quest board** | Mount hunts + "shard sentinel" rumor |

### After D4 (Heat) / Midgame

| Change | Details |
|--------|---------|
| **Heat-resistant tack** | Mount gear upgrades |
| **Dominion pressure** | More inspectors visible |

---

## H) Mount / Taming System Integration (Prismridge as HQ)

This town is where the system feels real.

### Stable Features (Post-D3)

| Feature | Function |
|---------|----------|
| **Mount Roster Management** | Rename, select active mount |
| **Bond Level** | Minor passive boosts |
| **Cosmetics** | Tack color, lantern tags, horn caps |
| **Mount Gear** | "Saddle modules" (QoL, traversal bonuses) |
| **Taming Contracts Board** | Hunts + capture quests |

### Stable Yard World Placement

| Feature | Location | Notes |
|---------|----------|-------|
| **Hitch posts** | (26, 84) and (8, 74) | Visual clarity |
| **Training ring** | Stable yard center | Tutorial cutscene location |

---

## I) NPC List (Placement + Function)

### Story-Critical

| NPC | Day Location | Night Location | Notes |
|-----|--------------|----------------|-------|
| **Foreman Talia Venn** | Mineworks Gate (96, 26) | Inn common area (62, 90) | Mining authority |
| **Lenswright Master Orlo Kest** | Refraction Works (22, 40) | Outside terminal (24, 28) | Staring at static |
| **Beast Handler Mira Tamsin** (post-D3) | Stable yard (16, 78) | — | Mount expert |

### Utility

- Innkeeper
- Tool vendor
- General vendor
- Medic

### Flavor

- Miners swapping rumors
- Kids playing with prism shards
- "Bright-eyed zealot" NPC (Light-as-ideology)
- Dominion Surveyor (phase-based) near Mineworks gate

---

## J) Quest Hooks (Prismridge-Specific)

### Main Story

| Quest | Purpose |
|-------|---------|
| **"Mineworks Permit"** | Sets up entry to Crystal Caverns (D3) |
| **"Truth in the Light"** | Optional lore framing Light as power, not purity |

### Sidequests (Early)

| Quest | Type | Reward |
|-------|------|--------|
| **Lens Calibration** | Fetch | Fetch 3 lens parts → accessory |
| **Dust Mask Delivery** | Delivery | Help miners → tool shop discounts |
| **Lost Cart** | Retrieval | Micro-map retrieval → teaches "hidden path reveal" |

### Sidequests (Post-D3)

| Quest | Unlock | Reward |
|-------|--------|--------|
| **First Taming Contract** | Post-D3 | Catch low-tier mount |
| **Stable Expansion** | Post-D3 | Gather mats → second stall row + cosmetics |
| **"Gleam Sense Test"** | Post-D3 | Find 3 secrets using Light passive |

---

## K) Story-State Phases (Town Evolution)

### PHASE 0 — First Arrival (Industrial Optimism)
- Clean main street
- Mining pride
- Faint weirdness at terminal at night

### PHASE 1 — Dominion Pressure Rising (Post-Scene 001)
- Surveyor appears
- "Permits" become a theme
- Some NPCs whisper about disappearances

### PHASE 2 — After D3 Clear (Celebration + New Economy)
- Stable opens fully
- Banners go up
- "Prism Stag" legend becomes town identity
- Terminal pings "Light anomalies"

### PHASE 3 — Midgame
- More inspectors + barricades near Mineworks
- Some miners relocated (residence district emptier)

### PHASE 4 — Late Game
- Curfew vibes at night
- Fewer civilians outside
- Stable remains active (players still need it)

---

## L) Navigation / Collision Notes

- Prism Boulevard must be **straight and readable** (contrast with Mirewatch's loops)
- Use refraction lamps as breadcrumb line every ~8 tiles
- Market Steps: wide stair tiles (don't make it fiddly)

---

## M) Secrets / Collectibles

| Secret | Location | Contents |
|--------|----------|----------|
| **Chest** (scaffold catwalk) | (102, 12) | "Lensguard Cloak" mat |
| **Hidden stash** (behind prism banner) | (40, 90) | Sellable "Glitter Shard" |
| **Pet sniff spot** (post tame) | (88, 96) | "Prism Resin" |
| **Terminal lore ping** (post D3) | Interact at (24, 28) | Secret note about "Light selecting what you see" |

---

## Quick Reference: Layout Overview

```
    MINWORKS GATE (D3 Access)
    [Exit at (111, 20)]
           |
    FOREMAN OFFICE (96, 20)
           |
    +------------------+------------------+
    |                                     |
LENSMITH ROW (6–34, 16–50)          RIDGE RESIDENCES
[Tech shops]                          (34–56, 80–104)
    |                                     |
    +------------------+------------------+
                       |
              PRISM BOULEVARD (Main Spine)
              (34–80, 16–80)
              [Refraction lamp line]
                       |
    +------------------+------------------+
    |                                     |
THE STABLE YARD                     MARKET STEPS
(10–34, 52–88)                      (54–96, 64–102)
[Mount Hub -                        [Tiered stalls]
 locked pre-D3]
    |                                     |
    +------------------+------------------+
                       |
              Terminal (24, 28)
                       |
              West Exit (0, 74)
              East Exit (111, 60)
              South Exit [locked] (54, 103)
```
