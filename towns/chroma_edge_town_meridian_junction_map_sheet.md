# Chroma's Edge — Meridian Junction Town Map Sheet (v1)
## Crossroads Hub — "Whoever Controls Routes Controls People"

---

## 0) Town Technical Specs

| Parameter | Value |
|-----------|-------|
| **Town Name** | Meridian Junction |
| **Role** | Major mid/late hub + fast-travel router + trade economy + quest consolidation point |
| **Map Size** | 144 × 112 tiles (2304 × 1792 px) |
| **Encounter Rate** | 0% (safe zone) |
| **Time States** | Day / Night |
| **Night Atmosphere** | More patrols + relay lights + harsher "inspection" vibe if Dominion pressure is high |
| **Town Terminal** | YES (Major) — routing, contracts, route status, phase markers (post-D7) |
| **Mounts** | Allowed (D3+) — restricted inside Relay Platform + tight market lanes; allowed in Caravan Yard + Outer Ring Road |

---

## 1) Visual Identity (Art Direction)

| Element | Description |
|---------|-------------|
| **Materials** | Cracked highway stone, rebuilt scaffolds, iron plates, relay pylons, tarps, rope signage |
| **Palette** | Dusty tan + steel gray + amber lamps + cyan relay glow (tech grit) |

### Signature Props

| Prop | Description |
|------|-------------|
| **Meridian Relay Spire** | Tall antenna tower; town silhouette anchor |
| **Route boards** | Magnet tiles showing "road open/closed" |
| **Caravan cranes + cargo nets** | — |
| **Dominion inspection seals** | Slapped over local signs (phase-based) |

---

## 2) Town Layout (District Blocks)

### District 1 — The Hub Ring (Central Plaza)

| Property | Value |
|----------|-------|
| **Bounds** | x 54–92, y 44–78 |
| **Features** | Terminal, quest board, key NPCs — the "circle" where every route feels reachable |

### District 2 — Relay Platform (Terminal + Control)

| Property | Value |
|----------|-------|
| **Bounds** | x 58–88, y 18–44 |
| **Features** | Elevated steel deck around the Relay Spire; cleanest area in town |

### District 3 — Market Lanes

| Property | Value |
|----------|-------|
| **Bounds** | x 88–144, y 54–96 |
| **Features** | Dense stalls: general goods, accessories, mats, travelers |

### District 4 — Caravan Yard (Stable + Freight)

| Property | Value |
|----------|-------|
| **Bounds** | x 0–54, y 54–112 |
| **Features** | Wide lanes for mounts/wagons, hitch posts, repair pit |

### District 5 — Clinic + Rest Row

| Property | Value |
|----------|-------|
| **Bounds** | x 48–92, y 78–112 |
| **Features** | Inn, clinic, simple homes — the "human" part |

### District 6 — Checkpoint Corner (Dominion Pressure)

| Property | Value |
|----------|-------|
| **Bounds** | x 0–28, y 18–54 |
| **Features** | Permit booth, inspection lane, holding pen (never fun) |

---

## 3) Key Anchors & Coordinates (Local 0–143, 0–111)

### Main Spawn Points

| Spawn | Coordinates | Context |
|-------|-------------|---------|
| **SPAWN A** (Prismridge road) | (132, 84) | Market Lanes |
| **SPAWN B** (Brinegate/coast) | (140, 66) | Market edge |
| **SPAWN C** (Gravemark road) | (12, 96) | Caravan Yard |
| **SPAWN D** (Cinderstep road) | (112, 24) | North-east access lane |
| **SPAWN E** (Rimehold route, late) | (72, 0) | Relay approach gate |

### Town Terminal (Major)

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Meridian Lattice Relay Terminal** | (72, 32) | Pre-Time: routing + contracts + region status; Post-D7: phase barrier markers + "time-lane advisories" |

### Exits (Edge Triggers)

| Exit To | Coordinates | Notes |
|---------|-------------|-------|
| **Prismridge** | (143, 92) | East edge |
| **Brinegate** (coast road) | (143, 64) | East edge |
| **Cinderstep** (mountain road) | (143, 20) | East edge |
| **Gravemark Outpost** | (0, 96) | West edge |
| **Rimehold** / north snow road | (72, 0) | North edge, late unlock |
| **Overworld Wastes spur** (optional) | (0, 40) | West edge |

---

## 4) Main Buildings (Exterior Door Tiles)

| Building | Door Coordinates | Function |
|----------|------------------|----------|
| **Crosswind Lodge** (Inn) | (68, 96) | Rest, rumors, caravan chatter |
| **Wayfarer Aid** (Clinic) | (84, 96) | Multi-status cures |
| **Route & Ration** (General Goods) | (112, 76) | Standard supplies |
| **Junction Charms** (Accessories) | (124, 66) | Resist charms, gear |
| **Bolt & Bale** (Repair/Smith) | (34, 86) | Upgrades, mats conversion |
| **Hitch & Harness** (Stable Office) | (18, 86) | Mount storage, tack swap |
| **Meridian Ledger** (Contract Hall) | (52, 66) | Bounty board, shipment contracts |
| **Dominion Permit Booth** | (12, 34) | Permits, inspections, tension |
| **Quest Board** | (74, 72) | Hub Ring center |

---

## 5) Interior Maps (Required)

### 1) Crosswind Lodge (Inn)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 36 × 24 |
| **Entry Pad** | (18, 22) |
| **Features** | Rest/save, rumor wall, caravan chatter cutscenes |

### 2) Wayfarer Aid (Clinic)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 32 × 20 |
| **Entry Pad** | (16, 18) |
| **Services** | Cures broad status (Burn, Pressure Shock, Stasis, etc.) by progression |

### 3) Meridian Ledger (Contract Hall)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 34 × 22 |
| **Entry Pad** | (17, 20) |
| **Services** | Bounty board, shipment contracts, faction reputation |

### 4) Bolt & Bale (Repair/Smith)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 40 × 24 |
| **Entry Pad** | (20, 22) |
| **Services** | Upgrades, mats conversion, mount tack modules (post-D3+) |

### 5) Hitch & Harness (Stable Office)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 34 × 22 |
| **Entry Pad** | (17, 20) |
| **Services** | Mount storage, tack swap, bond items (secondary to Prismridge) |

### 6) Meridian Relay Control (Terminal Deck Room)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 26 × 18 |
| **Entry Pad** | (13, 16) |
| **Services** | Story scenes, terminal tutorial, "route stabilization" quests |

### 7) Dominion Permit Booth (Pressure Room)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 22 × 16 |
| **Entry Pad** | (11, 14) |
| **Services** | Narrative tension, permit gates, optional sidequest routes |

---

## 6) Shops + Services (Inventory by Progress)

### Base (When First Unlocked as Hub)

#### General Goods

| Item | Type |
|------|------|
| Potions, Ethers | Consumables |
| Antidotes, Smoke Bombs | Status/escape |
| Rope Kits | Crafting mat |

#### Accessories

| Item | Description |
|------|-------------|
| Resist charms | Glare/Burn/Pressure/Stasis minor versions |

#### Repair/Smith

| Item | Description |
|------|-------------|
| Mid-tier upgrades | — |
| "Kit" crafts | Coolant, pressure patch, stasis balm (by story) |

#### Stable

| Item | Description |
|------|-------------|
| Tack basics | — |
| Travel feed | QoL buffs |
| Mount cosmetics | Small |

---

### Post-D5 (Tide Seated)

| Addition | Notes |
|----------|-------|
| Pressure patches | — |
| Kelp filters | — |
| Brine mats exchange | — |

### Post-D6 (Mass Seated)

| Addition | Notes |
|----------|-------|
| Knockback resist | — |
| Anchor gear | — |
| Heavy plating tier | — |
| Gravity mat exchange | — |

### Post-D7 (Time Seated)

| Addition | Notes |
|----------|-------|
| Phase keys | — |
| Chrono bands | — |
| Stasis balm supply | — |
| Phase-barrier route toggles | Terminal feature |
| "Time-lane deliveries" | Fun weird quests |

---

## 7) NPC List (Placement + Function)

### Story-Critical

| NPC | Schedule | Location |
|-----|----------|----------|
| **Relay Marshal "Hessa Ward"** | Day | Relay Platform (72, 38) |
| (runs routing like battlefield) | Night | Contract Hall |
| **Fixer "Jory Pike"** | Day | Bolt & Bale |
| (repairs, knows everyone) | Night | Inn |
| **Stablemaster "Kellan Rooke"** | Day | Hitch & Harness |
| (practical, no nonsense) | Night | Caravan Yard (26, 102) |

### Dominion Pressure NPC

| NPC | Phase | Location | Behavior |
|-----|-------|----------|----------|
| **Permit Officer "Verrin Hale"** | PHASE 1+ | Checkpoint Corner (14, 40) | Grows harsher at night |

### Utility + Flavor

| NPC | Description |
|-----|-------------|
| Route runner | Moving between districts |
| Map seller | Market Lanes |
| Caravan cook | Caravan Yard |
| Lost traveler | Hub Ring |
| "Signal listener" kid | Relay Platform stairs (hears relay pings) |

---

## 8) Quest Hooks (Meridian Junction-Specific)

### Main Story Utility (Hub Core)

| Quest | Description |
|-------|-------------|
| **"Route Status: Updated"** | Terminal tutorial; unlocks route visibility (blocked/open) |
| **"Relay Stabilization"** | Small tasks reducing random overworld hazards on 1 chosen route |

### Sidequests (Good Hub Content)

| Quest | Objective | Reward |
|-------|-----------|--------|
| **Shipment Contract** | Deliver mats to Gravemark/Prismridge/Brinegate | Reputation + discounts |
| **Broken Pylon** | Fix relay node outside town | Unlocks better terminal features |
| **Permit Problem** | Bypass, forge, or earn travel permit | Branch flavor, same progression |
| **Missing Caravan** | Short rescue outside town | Introduces late-game enemies early |

### Post-Time (Fun Weird)

| Quest | Objective | Reward |
|-------|-----------|--------|
| **Backdated Delivery** | Deliver something "before it was ordered" | Time-lane quest |
| **Phase Marker Survey** | Reveal 3 phase doors on overworld | Rewards |

---

## 9) Story-State Phases (Town Evolution)

### PHASE 0 — First Arrival (Busy, Neutral)

| Aspect | State |
|--------|-------|
| Atmosphere | Town feels like it's holding itself together through competence |
| Visual | Functional, busy |

### PHASE 1 — Dominion Pressure Rising

| Aspect | State |
|--------|-------|
| Inspection | More seals |
| Searches | Occasional "random searches" |
| Signage | Harsher at checkpoint |

### PHASE 2 — Post-D5 (Tide Calm)

| Aspect | State |
|--------|-------|
| Coastal | Fewer delay notices |
| Market | New sea goods show up |

### PHASE 3 — Post-D6 (Mass Stabilized)

| Aspect | State |
|--------|-------|
| Freight | Moves smoother |
| Caravan Yard | Expands (more stalls visible) |

### PHASE 4 — Post-D7 (Time Seated)

| Aspect | State |
|--------|-------|
| Terminal | Becomes the routing brain |
| Phase advisories | Appear |
| NPC dialogue | Gets unsettling: "I've said this already." |

---

## 10) Navigation / Collision Notes

1. **Hub Ring:** Must be wide and clean — player should hit terminal → board → inn/clinic in seconds
2. **Market Lanes:** Keep two parallel main aisles so density doesn't become a maze
3. **Caravan Yard:** Big open pads for mounts/wagons — don't clutter with tiny props

---

## 11) Secrets & Collectibles

| Secret | Coordinates | Loot / Effect |
|--------|-------------|---------------|
| **Chest under caravan ramp** | (18, 108) | Rare mat bundle (rotation by progression) |
| **Hidden relay note** [night] | (84, 26) | On platform stairs → starts terminal sidequest |
| **Pet sniff spot** [post-tame] | (118, 88) | "Route Resin" (rare craft mat) |
| **Terminal ping** [post-D7] | (72, 32) | Reveals one hidden phase-door marker on overworld |

---

## Quick Reference Map Overview

```
                        NORTH
                          ↑
    ┌───────────────────────────────────────────────────────────┐
    │                                                           │
    │         DISTRICT 2: Relay Platform                        │
    │         (x 58–88, y 18–44)                                │
    │         - Terminal (72,32)                                │
    │         - RELAY NOTE [night] (84,26)                      │
    │         - SPAWN E (72,0) — Rimehold exit                  │
    │                                                           │
    │    ═══════════════════════════════════════════            │
    │                                                           │
    │    DISTRICT 6: Checkpoint Corner      DISTRICT 1:         │
    │    (x 0–28, y 18–54)                The Hub Ring          │
    │    - Permit Booth door (12,34)      (x 54–92, y 44–78)    │
    │    - Officer Verrin Hale (14,40)    - Quest Board (74,72) │
    │                                     - Terminal (72,32)    │
    │    ═══════════════════════════════════════════            │
    │                                                           │
    │    DISTRICT 4: Caravan Yard           DISTRICT 3:         │
    │    (x 0–54, y 54–112)               Market Lanes          │
    │    - Hitch & Harness door (18,86)   (x 88–144, y 54–96)   │
    │    - Bolt & Bale door (34,86)       - General Goods       │
    │    - CHEST (18,108)                   door (112,76)       │
    │    - SPAWN C (12,96)                - Junction Charms     │
    │    - Stablemaster night: (26,102)     door (124,66)       │
    │                                     - SPAWN A (132,84)    │
    │    ═══════════════════════════      - SPAWN B (140,66)    │
    │                              ═══════════════════════      │
    │    DISTRICT 5: Clinic + Rest Row                          │
    │    (x 48–92, y 78–112)                                    │
    │    - Inn door (68,96)                                     │
    │    - Clinic door (84,96)                                  │
    │    - Contract Hall door (52,66)                           │
    │                                                           │
    │    Exits: (143,92) Prismridge, (143,64) Brinegate         │
    │           (143,20) Cinderstep, (0,96) Gravemark           │
    │           (0,40) Wastes spur, (72,0) Rimehold             │
    │                                                           │
    │    PET SNIFF (118,88)                                     │
    │                                                           │
    └───────────────────────────────────────────────────────────┘
```

**Key Anchors Summary:**

| Feature | Coordinates |
|---------|-------------|
| **Terminal** | (72, 32) |
| **Quest Board** | (74, 72) |
| **Spawn A** (Prismridge) | (132, 84) |
| **Spawn B** (Brinegate) | (140, 66) |
| **Spawn C** (Gravemark) | (12, 96) |
| **Spawn D** (Cinderstep) | (112, 24) |
| **Spawn E** (Rimehold) | (72, 0) |
| **Inn** | (68, 96) |
| **Clinic** | (84, 96) |
| **General Goods** | (112, 76) |
| **Accessories** | (124, 66) |
| **Repair/Smith** | (34, 86) |
| **Stable** | (18, 86) |
| **Contract Hall** | (52, 66) |
| **Permit Booth** | (12, 34) |
| **Officer Verrin Hale** | (14, 40) |
| **Chest** | (18, 108) |
| **Relay Note** [night] | (84, 26) |
| **Pet Sniff** | (118, 88) |
| **Prismridge Exit** | (143, 92) |
| **Brinegate Exit** | (143, 64) |
| **Cinderstep Exit** | (143, 20) |
| **Gravemark Exit** | (0, 96) |
| **Wastes Exit** | (0, 40) |
| **Rimehold Exit** | (72, 0) |
