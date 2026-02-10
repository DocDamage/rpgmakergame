# Chroma's Edge — Cinderstep Town Map Sheet (v1)
## Heat-Vent Foothill Town — "Pressure From the Mountain and the Dominion"

---

## A) Technical Specs

| Parameter | Value |
|-----------|-------|
| **Town Map Size** | 112 × 96 tiles |
| **Tile Size** | 16×16 px |
| **Full Texture** | 1792×1536 px |
| **Encounter Rate** | 0% (safe zone) |
| **Time States** | Day / Night (night = more vent glow + curfew vibe later) |
| **Town Terminal** | Yes (ruggedized casing, heat-shielded) |
| **Mounts** | Allowed after D3; after D4 you can fit heat tack modules here |
| **Town Hazard Flavor** | No damage in town, but steam jets + heat shimmer are visual set dressing |

---

## B) Visual Identity (Art Direction)

### Materials
- Basalt stone
- Soot-stained metal
- Copper piping
- Ceramic tiles
- Heat shields
- Rope-lashed scaffolds

### Palette
- Charcoal/obsidian
- Ember orange
- Copper red
- Occasional teal coolant glow

### Signature Props
- **Vent chimneys** that "breathe" in slow pulses
- **Cooling troughs** (water/gel basins) around the forge district
- **Climber banners** marking safe ascent routes
- **Dominion permit placards** nailed over older local signs

---

## C) Town Layout (District Blocks)

### District 1 — Ventgate Plaza (Central Hub)
- **Bounds:** x 44–78, y 38–68
- **Vibe:** Wide, readable space. The "meeting + shopping + bulletin" node

### District 2 — Forge Row
- **Bounds:** x 10–44, y 42–78
- **Vibe:** Smiths, gear upgrades, coolant vendors, mount tack after D3/D4

### District 3 — Climber's Steps (Ascent Quarter)
- **Bounds:** x 72–112, y 16–54
- **Vibe:** Ropes, packs, ascent permits, route maps. Leads toward Skyspire approach

### District 4 — Steamwalk Residences
- **Bounds:** x 44–82, y 68–96
- **Vibe:** Working homes, soup pots, kids, quiet "town survives" vibe

### District 5 — Coolant Works + Pumps
- **Bounds:** x 6–34, y 10–42
- **Vibe:** Pumps and condenser rigs. Visual explanation for how anyone lives here

### District 6 — Dominion Checkpoint Corner
- **Bounds:** x 82–112, y 54–86
- **Vibe:** Not a fortress—more like a "polite threat" office with inspectors and posted rules

---

## D) Key Anchors & Coordinates (Local 0–111, 0–95)

### Main Spawn Points

| Spawn | Location | Coordinates | Context |
|-------|----------|-------------|---------|
| **SPAWN A** | Arrival from Prismridge road | (12, 58) | Forge Row edge |
| **SPAWN B** | Arrival from Skyspire return | (98, 28) | Climber's Steps |
| **SPAWN C** | Night return | (56, 60) | Ventgate Plaza |

### Town Terminal

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Cinderstep Lattice Terminal** | (28, 30) | Heat-shielded kiosk, slightly "authorized" vibe |
| **After D4** | — | Displays stable vent lanes + new heat route nodes |

### Exits (Edge Triggers)

| Direction | Edge Trigger | Destination |
|-----------|--------------|-------------|
| **To Overworld — West** (Prismridge/mountain road) | (0, 58) | Prismridge route |
| **To Skyspire Temple Approach** | (111, 30) | Ember Stair micro-map |
| **To Overworld — South** (Brinegate/Halcyon) | (64, 95) | Optional midgame unlock |

---

## E) Main Buildings (Exterior Door Tiles)

| Building | Door Coordinates | Function |
|----------|------------------|----------|
| **Inn ("The Ventgate Rest")** | (58, 78) | Rest/save |
| **Forge ("Tongs & Thunder")** | (22, 62) | Upgrades/heat crafting |
| **Heat Gear Shop ("Heatshield Outfitters")** | (36, 68) | Burn resist items |
| **Clinic ("Emberwell Aid")** | (68, 78) | Medical |
| **General Goods ("Ash & Salt Supply")** | (74, 66) | Basic supplies |
| **Ascent Office ("Spire Permit Hall")** | (92, 44) | D4 story gating |
| **Dominion Inspector Office** | (100, 72) | Tension/pressure |
| **Quest Board** | (56, 66) | Ventgate Plaza |
| **Mount Hitch Post** (post-D3) | (40, 74) | Forge Row edge |

---

## F) Interior Maps (Required)

### 1) The Ventgate Rest (Inn)
- **Interior Size:** 30×20
- **Entry Pad:** (15, 18)
- **Vibe:** Warm lighting, thick walls, "you can finally breathe" tone

### 2) Tongs & Thunder (Forge)
- **Interior Size:** 40×26
- **Entry Pad:** (20, 24)
- **Services:** Upgrade services, smith NPC, anvil stations, coolant trough prop
- **After D4:** Unlocks Heatguard crafting tier + mount tack modules

### 3) Heatshield Outfitters (Gear Shop)
- **Interior Size:** 32×20
- **Entry Pad:** (16, 18)
- **Inventory:** Burn resist, coolant pods, heat gauge reducers (field consumables)

### 4) Spire Permit Hall (Ascent Office)
- **Interior Size:** 28×18
- **Entry Pad:** (14, 16)
- **Function:** Story gating for D4 entry; later becomes "route board" for Skyspire revisits

### 5) Dominion Inspector Office (Pressure Room)
- **Interior Size:** 22×16
- **Entry Pad:** (11, 14)
- **Function:** Story tension + optional sidequest turn-in ("papers")

### 6) Emberwell Aid (Clinic)
- **Interior Size:** 30×20
- **Entry Pad:** (15, 18)
- **Services:** Cures Burn / Overheat effects (cheap after D4)

---

## G) Shops + Services (Inventory by Progress)

### Base (Pre-D4)

| Shop | Inventory |
|------|-----------|
| **General Goods** | Potions, antidotes, smoke bombs, rope kit |
| **Outfitters** | Basic burn resist items, Coolant Pod (limited) |
| **Forge** | Weapon/armor upgrades (mid-tier), simple heat resist crafts |

### After D4 (Heat Relic Seated) — Major Upgrade

| Change | Details |
|--------|---------|
| **Outfitters** | Better coolant, Heat Buffer kits, burn/overheat counters |
| **Forge** | Heatguard Mantle upgrades, "tempered" weapons, heat tack modules |
| **Clinic** | Overheat cures become cheap; adds "heat fatigue" tonic |

### Mid/Late Game

Adds mount gear that helps with hot overworld lanes and later "Molten Core" prep:
- **Vent-Seal Saddle Pad** (reduces heat gain while mounted)
- **Ceramic Hoofwraps** (ignore hot ground slow tiles)

---

## H) NPC List (Placement + Function)

### Story-Critical

| NPC | Day Location | Night Location | Notes |
|-----|--------------|----------------|-------|
| **Master Smith Braska Holt** | Forge interior | Plaza by quest board | — |
| **Ascent Marshal Keir Sable** | Permit Hall | Climber's Steps (checking ropes) | Local route leader |
| **Dominion Inspector Alden Pryce** | Checkpoint corner | Inspector Office | Antagonistic bureaucrat |

### Utility

- Innkeeper
- Medic
- Outfitter vendor
- General vendor
- Tack module vendor (post-D3)

### Flavor

- Climbers stretching
- Miners with soot masks
- Kids roasting food on vent grates (safe)
- "Vent listener" old-timer who predicts pulses

---

## I) Quest Hooks (Cinderstep-Specific)

### Main Story

| Quest | Purpose |
|-------|---------|
| **"Ascent Clearance"** | Get permission (or workaround) to reach Skyspire Temple approach |
| **"Cooling the Path"** | Teaches coolant + heat prep before D4 |

### Sidequests (Early)

| Quest | Type | Reward |
|-------|------|--------|
| **Coolant Run** | Fetch | Fetch condenser parts → Coolant Pods |
| **Broken Rope Bridge** | Repair | Opens tiny shortcut inside town |
| **Lost Miner** | Search | Small search outside town micro-map |

### Sidequests (Post-D4)

| Quest | Unlock | Reward |
|-------|--------|--------|
| **Forge Tempering** | Post-D4 | Gather rare slag → weapon upgrade tier |
| **Inspector Papers** | Post-D4 | Falsify, steal, or earn permits (branch flavor) |
| **Mount Heat Tack Trial** | Post-D4 | Timed run around town perimeter (tutorial) |

---

## J) Story-State Phases (Town Evolution)

### PHASE 0 — First Arrival (Hardworking, Wary)
- Minimal Dominion presence
- Locals handle their own problems

### PHASE 1 — Dominion Pressure Rising
- More permit signs
- Inspector patrol "visibility"
- Harsher NPC dialogue

### PHASE 2 — After D4 Clear
- Visual reward: vents pulse steadier, fewer "panic" props
- Forge fully upgrades
- Town feels empowered, not just threatened

### PHASE 3 — Midgame
- More refugees passing through
- Clinic busier
- Inspector office becomes more active

### PHASE 4 — Late Game
- Curfew vibe at night (fewer civilians outside)
- Climber's Steps gets barricades (but you can still pass)

---

## K) Navigation / Collision Notes

- Keep Ventgate Plaza open and centered (like Prismridge's boulevard philosophy)
- Forge Row should feel dense but not maze-y: 2–3 clear lanes max
- Climber's Steps must visually point toward the Skyspire Approach exit

---

## L) Secrets / Collectibles

| Secret | Location | Contents |
|--------|----------|----------|
| **Chest behind slag pile** | (14, 72) | "Tempering Shard" (forge mat) |
| **Hidden coolant stash** | (20, 18) inside Coolant Works alley | Coolant Pod ×1 |
| **Lore plaque** (Progenitor stone) | (86, 34) | "Heat was meant for transformation, not obedience." |
| **Pet sniff spot** (post tame) | (76, 90) | Rare "Ash Resin" craft mat |

---

## Quick Reference: Layout Overview

```
                    SKYSPIRE APPROACH (D4)
                    [Exit at (111, 30)]
                           |
              CLIMBER'S STEPS (72–112, 16–54)
              [Ascent Office at (92, 44)]
                           |
    FORGE ROW              |              DOMINION CHECKPOINT
    (10–44, 42–78)         |              (82–112, 54–86)
    [Tongs & Thunder]      |              [Inspector Office]
                           |
              +------------+------------+
                           |
              VENTGATE PLAZA (44–78, 38–68)
              [Main Hub]
              [Quest Board (56, 66)]
              [Terminal (28, 30)]
                           |
              +------------+------------+
                           |
    COOLANT WORKS          |              STEAMWALK RESIDENCES
    (6–34, 10–42)          |              (44–82, 68–96)
    [Pumps/Condensers]     |              [Homes]
                           |
                    WEST EXIT (0, 58)
                    [To Prismridge]
```
