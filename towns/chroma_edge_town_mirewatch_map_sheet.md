# Chroma's Edge — Mirewatch Town Map Sheet (v1)
## Swamp Boardwalk Town — "Survival by Community"

---

## A) Technical Specs

| Parameter | Value |
|-----------|-------|
| **Town Map Size** | 104 × 96 tiles |
| **Tile Size** | 16×16 px |
| **Full Texture** | 1664×1536 px |
| **Encounter Rate** | 0% (safe zone) |
| **Time States** | Day / Night (night = fog thicker + patrol risk visuals) |
| **Town Terminal** | Yes (humid, corroded casing; still functional) |
| **Mounts** | Allowed after D3 but boardwalk lanes restrict speed (tight turns) |
| **Water Traversal** | Small canoe taxi (town-only) for flavor + shortcuts (no combat) |

---

## B) Visual Identity (Art Direction)

### Materials
- Wet wood planks
- Rope bridges
- Reed fences
- Tarp roofs
- Glass jars
- Salt lines

### Color Palette
- Algae green
- Swamp brown
- Amber lanterns
- Pale teal spore-glow

### Signature Props
- **Lantern posts** every 6–8 tiles (keeps navigation readable)
- **Salt-line barriers** (keeps fungus "out")
- **Fan totems** (hand-cranked, Motion foreshadow)
- **Spore drying racks** (town silhouette)

---

## C) Town Layout (District Blocks)

### District 1 — Lantern Pier (Main Hub)
- **Bounds:** x 40–74, y 46–74
- **Vibe:** Central plaza on wide boardwalk, most NPC chatter and services

### District 2 — Spore Market Walk
- **Bounds:** x 56–92, y 70–92
- **Vibe:** Stalls: medicine, antidotes, filters, crafting mats

### District 3 — Clinic Row ("Sporehouse")
- **Bounds:** x 74–102, y 44–68
- **Vibe:** Medical/clean area; salt lines and fans; ties directly to D2 themes

### District 4 — Fog Shanties (Residences)
- **Bounds:** x 10–40, y 50–90
- **Vibe:** Narrow planks, hanging laundry, kids, daily life

### District 5 — Pumpworks + Fan Totems
- **Bounds:** x 18–52, y 22–46
- **Vibe:** Water pumps, drainage gates, ventilation mechanisms (Motion hint)

### District 6 — Trailhead Causeway (Dungeon Access)
- **Bounds:** x 0–20, y 10–34
- **Vibe:** Mud causeway + warning totems → leads to Fungal Depths (D2)

---

## D) Key Anchors & Coordinates (Local 0–103, 0–95)

### Main Spawn Points

| Spawn | Location | Coordinates | Context |
|-------|----------|-------------|---------|
| **SPAWN A** | Arrival from overworld | (52, 90) | Spore Market entrance |
| **SPAWN B** | Arrival from Dusthaven route | (20, 94) | Fog Shanties edge |
| **SPAWN C** | Return from Fungal Depths | (12, 26) | Trailhead Causeway |

### Town Terminal

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Mirewatch Lattice Terminal** | (86, 56) | Humid, corroded but functional |
| **Locked until** | — | PHASE 0, activates after first main Mirewatch story scene |
| **Post-D2** | — | Becomes a "wind-reading" node after Motion relic seated |

### Exits (Edge Triggers)

| Direction | Edge Trigger | Destination |
|-----------|--------------|-------------|
| **To Overworld — Swamp Track** (Dusthaven) | (52, 95) | Dusthaven route |
| **To Overworld — Marsh Causeway** (Prismridge) | (103, 76) | Shortcut (locked until D2 seated or sidequest) |
| **To Fungal Depths (D2)** | (0, 22) | Dungeon entrance |

---

## E) Main Buildings (Exterior Door Tiles)

| Building | Door Coordinates | Function |
|----------|------------------|----------|
| **Inn ("The Lantern & Reed")** | (52, 66) | Rest/save |
| **Clinic ("Sporehouse Clinic")** | (88, 58) | Medical services |
| **General Goods ("Salt & Stitch")** | (70, 84) | Supplies |
| **Alchemy Stall ("Bittercap Bench")** | (82, 86) | Antidotes/potions |
| **Craft Shed ("Filterwright's Shed")** | (60, 82) | Crafting |
| **Boat Taxi Dock** | (44, 74) | Town-only fast travel |
| **Quest Board** | (54, 74) | Lantern Pier |
| **Watch Platform** | (34, 44) | Scout NPC + fog alerts |
| **Broadcast Relic** (broken Dominion) | (76, 50) | Foreshadow; worsens PHASE 1+ |

---

## F) Interior Maps (Required)

### 1) The Lantern & Reed (Inn)
- **Interior Size:** 30×20
- **Entry Pad:** (15, 18)
- **Features:** Innkeeper, rest/save
- **Night Vibe:** Rain on tarp roof

### 2) Sporehouse Clinic
- **Interior Size:** 34×24
- **Entry Pad:** (17, 22)
- **Services:** Poison cure, sleep cure, "Dizzy" cure (Motion theme)
- **Prop:** Salt fan wall (foreshadows Vent Valves in D2)

### 3) Salt & Stitch (General Goods)
- **Interior Size:** 28×18
- **Entry Pad:** (14, 16)
- **Inventory:** Filters, rope bridges (later), basic supplies

### 4) Filterwright's Shed (Craft)
- **Interior Size:** 32×18
- **Entry Pad:** (16, 16)
- **Early Craft:** Mire Filter, Anti-toxin wraps
- **After D2:** Unlocks Slipstep related craft upgrades

### 5) Optional Interior: "Fog Chapel" (Tiny Quiet Hut)
- **Interior Size:** 18×14
- **Purpose:** Character beat + lore
- **Theme:** "We don't worship the swamp—we respect it"

---

## G) Shops + Services (Inventory by Progress)

### Base (First Visit / Pre-D2 Clear)

| Shop | Inventory |
|------|-----------|
| **General Goods** | Potions, antidotes (limited), smoke bomb, rope (flavor) |
| **Clinic** | Poison cures + basic status cures |
| **Craft** | Mire Filters, "Salt Line Kit" (field consumable to reduce poison ticks) |

### After D2 Clear + Motion Relic Seated

| Change | Details |
|--------|---------|
| **Clinic expands** | Stronger cures, "Anti-Dizzy" tonics |
| **Craft expands** | Slipstep Boots (upgrade path), vent-related charms |
| **NEW vendor** | "Ventwright" appears on Pumpworks platform (44, 34) |

### After D3 (Mount Unlock)

| Feature | Location | Details |
|---------|----------|---------|
| **Stable Hitch** | (58, 92) | Outside market |
| **Mount cosmetics** | — | Reed Mantle, Lantern Tag |
| **Speed restriction** | — | Boardwalk clamps so mounts don't feel glitchy |

---

## H) NPC List (Placement + Function)

### Story-Critical

| NPC | Day Location | Night Location | Notes |
|-----|--------------|----------------|-------|
| **Warden Jessa Morn** (town leader) | Lantern Pier (56, 62) | Watch Platform (34, 44) | Practical, not preachy |
| **Doc Brann** (clinic lead) | Clinic interior | Clinic interior | Medicine-first, suspicious of Dominion |
| **Scout Kip** | Trailhead Causeway (10, 30) | Pumpworks (30, 34) | Points to D2 causeway + warns about Slipstreams |

### Utility NPCs

| NPC | Function |
|-----|----------|
| **Innkeeper** | Rest/save |
| **Filterwright** | Craft vendor |
| **Alchemist Stall Vendor** | Potions/antidotes |
| **Boat Taxi Operator** | Fast travel inside town (small fee) |

### Flavor NPCs

- Kid catching glowbugs
- Fisherman
- "Fog Singer" (not cult)
- Grumpy reed farmer

### Dominion Pressure NPCs (Phase-Based)

| NPC | Phase | Details |
|-----|-------|---------|
| **Suspicious Stranger** (informant) | PHASE 1+ | Appears in Market at night |
| **Scout Pair** | PHASE 1+ | Visible on far planks (tension, no combat) |

---

## I) Quest Hooks (Mirewatch-Specific)

### Main Story

| Quest | Purpose |
|-------|---------|
| **"Breathing Below"** | Send party to Fungal Depths (D2) |
| **"Clinic Log"** | Optional lore console explaining Motion-as-respiration |

### Sidequests (Early)

| Quest | Type | Reward |
|-------|------|--------|
| **Salt Line Repair** | Placement | Place 3 salt kits on boardwalk edges (teaches interactables) |
| **Missing Canoe** | Fetch | Find at swamp edge (tiny micro-map) |
| **Filter Parts Run** | Delivery | Fetch from Dusthaven Outskirts (connects towns) |

### Sidequests (Later)

| Quest | Unlock | Reward |
|-------|--------|--------|
| **Marsh Causeway Unlock** | After D2 | Opens east shortcut toward Prismridge |
| **Dominion Speaker Sabotage** | PHASE 1+ | Disable broken broadcast relic without alerting watchers |

---

## J) Story-State Phases (Town Evolution)

### PHASE 0 — First Arrival (Suspicious Calm)
- Fog heavy
- Fewer civilians out
- Terminal locked
- "Don't touch the old tech" vibe

### PHASE 1 — Post-Scene 001 Pressure (Dominion Message Creep)
- Broken speaker starts emitting static advisories
- Night NPCs whisper about "scouts in the reeds"

### PHASE 2 — After D2 Clear
- Fans spin steadier
- Fog thins slightly (visual reward)
- New vendor and craft unlocks

### PHASE 3 — Midgame Revisit
- Refugees increase
- Clinic busier
- Boat taxi gets second route (shortcut across residences)

### PHASE 4 — Late Game
- Fewer kids outside
- More watchers
- Optional "curfew feel" at night (lanterns dimmed, doors shut)

---

## K) Navigation / Collision Notes

- Boardwalk loops should always "return to Lantern Pier" (don't trap players)
- Use lantern posts as natural breadcrumbs every few tiles
- Water gaps are hard blockers (except canoe taxi nodes)

---

## L) Secrets / Collectibles

| Secret | Location | Contents |
|--------|----------|----------|
| **Chest** (boardwalk underside ladder) | (28, 72) | "Sporecloak Charm" (if not gotten in D2) |
| **Hidden herb patch** | (18, 84) | Rare antidote ingredient |
| **Pet sniff spot** (after tame system) | (92, 78) | "Glowcap Resin" mat |
| **Lore bottle** (floating) | (12, 60) | Short note about "the swamp breathing" |

---

## Quick Reference: Layout Overview

```
                    TRAILHEAD CAUSEWAY
                    [Exit to D2 at (0, 22)]
                           |
    PUMPWORKS              |              CLINIC ROW
    [Fans/Totems]          |              [Sporehouse]
    (18–52, 22–46)         |              (74–102, 44–68)
                           |
    FOG SHANTIES  -------- LANTERN PIER --------  SPORE MARKET
    (10–40, 50–90)         (40–74, 46–74)        (56–92, 70–92)
    [Residences]           [Main Hub]            [Stalls]
                           |
                      [Boat Dock (44, 74)]
                           |
                    SWAMP TRACK EXIT
                    [To Dusthaven (52, 95)]
                    [Marsh Causeway (103, 76)]
```
