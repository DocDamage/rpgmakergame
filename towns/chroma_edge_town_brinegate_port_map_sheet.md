# Chroma's Edge — Brinegate Port Town Map Sheet (v1)
## Stormbreak Harbor Town — "Everything here is built like it expects to be punched by the ocean"

---

## 0) Town Technical Specs

| Parameter | Value |
|-----------|-------|
| **Town Name** | Brinegate Port |
| **Role** | D5 staging hub + ferry hub (to Rimechain later) + aquatic-travel systems unlock (post-D5) |
| **Map Size** | 120 × 96 tiles (1920 × 1536 px) |
| **Encounter Rate** | 0% (safe zone) |
| **Time States** | Day / Night |
| **Day Atmosphere** | Bustling docks, gear hawkers, divers prepping |
| **Night Atmosphere** | Storm lamps, fewer civilians, more "watchers" |
| **Town Terminal** | Yes — salt-sealed casing, sonar-like ping at night |
| **Mounts** | Allowed (D3+) — restricted to upper streets; **no mounts on tight pier planks** |
| **Key Systems** | Pressure prep gear + dive routing + ferry network |

---

## 1) Visual Identity (Art Direction)

| Element | Description |
|---------|-------------|
| **Materials** | Wet timber, barnacled stone, iron cleats, rope netting, storm shutters, copper pipes |
| **Palette** | Slate gray, sea green, rust red, amber storm lanterns, faint cyan sonar glow |

### Signature Props

| Prop | Description |
|------|-------------|
| **Breakwater wall** | Wave spray VFX |
| **Sonar bell buoy** | Pinging light effect |
| **Salt-curtain shutters** | Keep spores/rot out |
| **Dive cages** | Hanging over water |

---

## 2) Town Layout (District Blocks)

### District 1 — Stormbreak Docks (Main Hub)

| Property | Value |
|----------|-------|
| **Bounds** | x 36–86, y 52–92 |
| **Features** | Primary services, quest board, inn access, dive vendor |
| **Navigation** | Readable straight planks + wide turning pads |

### District 2 — Breakwater Market

| Property | Value |
|----------|-------|
| **Bounds** | x 62–118, y 30–62 |
| **Features** | Gear stalls, pressure patches, rope kits, lens/valve crossover items |

### District 3 — Diver's Row (Prep + Repairs)

| Property | Value |
|----------|-------|
| **Bounds** | x 10–46, y 46–78 |
| **Features** | Dive shop, pressure clinic, equipment benches |

### District 4 — Harbor Office + Ferry Gate

| Property | Value |
|----------|-------|
| **Bounds** | x 90–118, y 62–92 |
| **Features** | Tickets, routes, later access to Chronowake Pier ferry |

### District 5 — Salt Chapel ("Quiet Tide")

| Property | Value |
|----------|-------|
| **Bounds** | x 18–56, y 18–46 |
| **Features** | Not culty. Practical rites for sailors. Great for character beats |

### District 6 — Customs Corner (Dominion Pressure)

| Property | Value |
|----------|-------|
| **Bounds** | x 0–22, y 62–92 |
| **Features** | "Permits + inspections" vibe. Escalates over phases |

---

## 3) Key Anchors & Coordinates (Local 0–119, 0–95)

### Main Spawn Points

| Spawn | Coordinates | Context |
|-------|-------------|---------|
| **SPAWN A** (overworld coast road) | (106, 32) | Market edge |
| **SPAWN B** (Abyss Entry Pier return) | (58, 90) | Deep docks |
| **SPAWN C** (night return) | (70, 70) | Stormbreak Docks center |

### Town Terminal

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Brinegate Lattice Terminal** | (88, 44) | Salt-sealed kiosk; sonar-like ping at night; post-D5 becomes "sea-node" activator |

### Exits (Edge Triggers)

| Exit To | Coordinates | Notes |
|---------|-------------|-------|
| **Overworld — Coastal Road** | (119, 34) | — |
| **Abyss Entry Pier** (D5 access) | (46, 95) | South edge |
| **Ferry Route** (Chronowake Pier) [mid/late] | (112, 90) | Locked until story progression |
| **Sunken City sea node** [post-D5] | (74, 94) | Boat launch for aquatic travel |

---

## 4) Main Buildings (Exterior Door Tiles)

| Building | Door Coordinates | Function |
|----------|------------------|----------|
| **The Breakwater Lantern** (Inn) | (74, 74) | Rest, rumors, character beats |
| **Deepwright Outfitters** (Dive Shop) | (28, 66) | Pressure patches, equalizers, dive gear |
| **Brine Medic Station** (Clinic) | (20, 58) | Poison/silence/pressure cures |
| **Rope & Ration** (General Goods) | (90, 58) | Consumables, rope kits |
| **Harbor Office / Ferry Tickets** | (104, 78) | Routes, tickets, weather delays |
| **Hull & Hook** (Shipwright Bench) | (44, 58) | Craft/upgrade: sealants, storm lamps, sea-node upgrades |
| **Quiet Tide Chapel** | (34, 34) | Rites, lore, Tide ≠ Cleanse philosophy |
| **Customs Office** (Dominion) | (10, 78) | Inspections, permits, phase-based tension |
| **Quest Board** | (72, 66) | Stormbreak Docks center |

---

## 5) Interior Maps (Required)

### 1) The Breakwater Lantern (Inn)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 32 × 22 |
| **Entry Pad** | (16, 20) |
| **Atmosphere** | Storm audio + warm lantern pools; sailors + divers swapping rumors |

### 2) Deepwright Outfitters (Dive Shop)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 36 × 24 |
| **Entry Pad** | (18, 22) |
| **Inventory** | Pressure patches, equalizers, diving kits |
| **Post-D5 Unlock** | Aquatic travel gear + Sunken City charts |

### 3) Brine Medic Station (Clinic)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 30 × 20 |
| **Entry Pad** | (15, 18) |
| **Services** | Poison/silence cures; post-D5 adds pressure-related cures (cheap) |

### 4) Harbor Office / Ferry Tickets

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 28 × 18 |
| **Entry Pad** | (14, 16) |
| **Function** | Ferry route UI + story gating + "weather delays" flavor |

### 5) Hull & Hook (Shipwright Bench)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 34 × 20 |
| **Entry Pad** | (17, 18) |
| **Crafting** | Rope kits, sealant wraps, storm lamps; later sea-node upgrades (post-D5) |

### 6) Quiet Tide Chapel

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 24 × 18 |
| **Entry Pad** | (12, 16) |
| **Purpose** | Character beats + lore (Tide ≠ Cleanse) |

### 7) Terminal Alcove (Optional — Tech Nook)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 18 × 14 |
| **Entry Pad** | (9, 12) |
| **Post-D5 Feature** | "Sea lattice nodes detected" prompt |

---

## 6) Shops + Services (Inventory by Progress)

### Base (Pre-D5 Clear)

#### Deepwright Outfitters

| Item | Description |
|------|-------------|
| Pressure Patch (limited) | Reduces pressure effects |
| Equalizer Capsule | Stabilizes pressure for X battles |
| Silence Salts | Reduces silence chance |

#### Rope & Ration

| Item | Description |
|------|-------------|
| Potions, Antidotes | Standard consumables |
| Smoke Bombs | Escape aid |
| Rope Kits | Crafting mat |

#### Clinic

| Service | Price |
|---------|-------|
| Poison cure | Mid-price |
| Silence cure | Mid-price |

#### Shipwright Bench

| Item | Description |
|------|-------------|
| Sealant wraps | Weather protection |
| Storm lamp | Reduces ambush chance at sea-adjacent maps |

---

### After D5 (Tide Relic Seated) — Major Upgrade

| Unlock | Effect |
|--------|--------|
| **AQUATIC TRAVEL UNLOCK UI** | Sea travel system accessible |

#### Deepwright Expansion

| Item | Description |
|------|-------------|
| Sea-Node Charts | Sunken City markers |
| Current Bridle / Aquatic Tack | Mount gear for aquatic traversal |
| Pressure Stabilizer | Superior version |

#### Clinic Expansion

| Service | Notes |
|---------|-------|
| Pressure shock cures | Now available |

#### Harbor Office

| Route | Change |
|-------|--------|
| Chronowake Pier ferry | Becomes reliable and cheaper |

---

### Mid/Late Game

| Addition | Notes |
|----------|-------|
| Rare salvage goods | Used for Mass/Time prep |
| Optional "black-market" tide tech | Night only; moral choice hooks |

---

## 7) NPC List (Placement + Function)

### Story-Critical

| NPC | Schedule | Location |
|-----|----------|----------|
| **Harbormaster Rell Ardent** (practical, doesn't fear storms) | Day | Harbor Office (104, 78) |
| | Night | Breakwater walk (82, 90) |
| **Divewright "Nima Calder"** (gear expert, allergic to nonsense) | Day | Deepwright Outfitters interior |
| | Night | Dock edge (60, 88) |
| **Brine Medic "Dr. Sola Quen"** (calm, sharp) | Always | Clinic interior |

### Utility

| NPC | Location | Function |
|-----|----------|----------|
| Innkeeper | The Breakwater Lantern | Rest services |
| General Vendor | Rope & Ration | Standard goods |
| Shipwright Vendor | Hull & Hook | Crafting bench |
| Chapel Keeper | Quiet Tide Chapel | Lore, blessings |

### Flavor

| NPC | Description |
|-----|-------------|
| Net mender | Working dockside |
| Fisher kid | Runs errands |
| "Storm singer" | Sings to calm waters |
| Old sailor | Gives wrong advice confidently |

### Dominion Pressure NPC (Phase-Based)

| NPC | Phase | Location | Behavior |
|-----|-------|----------|----------|
| **Customs Officer "Verrin Holt"** (paperwork bully) | PHASE 1+ | Customs Office (10, 78) | Inspections, permit hassles |
| | Escalation | Night patrols | More aggressive barks |

---

## 8) Quest Hooks (Brinegate-Specific)

### Main Story

| Quest | Description |
|-------|-------------|
| **"Deep Prep"** | Required supplies/tutorial before entering Abyssal Trench (D5) |
| **"The Entry Pier"** | Unlocks the micro-map access to D5 |

### Sidequests (Early)

| Quest | Objective | Reward |
|-------|-----------|--------|
| **Storm Lantern Repair** | Collect 3 parts from market | Anti-ambush item |
| **Lost Dive Cage** | Retrieve from shallow water edge (mini micro-map) | Pressure Patch bundle |
| **Chapel Offering** | Optional offering at Quiet Tide | Small buff token (silence resist ×10 battles) |

### Sidequests (Post-D5)

| Quest | Objective | Reward |
|-------|-----------|--------|
| **Sunken City Charting** | Unlock sea node locations | Postgame content groundwork |
| **Ferry Contract** | Open consistent route to Chronowake Pier | Rimechain access |
| **Customs Disruption** | Remove permit chokehold | Reputation + discount |

---

## 9) Story-State Phases (Town Evolution)

### PHASE 0 — First Arrival (Busy, Cautious)

| Aspect | State |
|--------|-------|
| Atmosphere | Divers prepping, gear talk, storms normal |
| Dominion Presence | Minimal |
| Visual | Open docks, relaxed patrols |

### PHASE 1 — Dominion Pressure Rising

| Aspect | State |
|--------|-------|
| Atmosphere | Permit signs on docks, more "inspection" NPC barks |
| Dominion Presence | Customs corner more visible |
| NPC Barks | Hostile, bureaucratic |

### PHASE 2 — After D5 Clear (Big Shift)

| Aspect | State |
|--------|-------|
| Atmosphere | Relief + awe — "the sea feels calmer" |
| Systems | Aquatic travel opens; terminal pings sea nodes |
| Visual | Less tension, more travelers |

### PHASE 3 — Midgame Revisit

| Aspect | State |
|--------|-------|
| Atmosphere | More travelers pass through (route hub) |
| Services | Ferry route active + more trade goods |

### PHASE 4 — Late Game

| Aspect | State |
|--------|-------|
| Night Atmosphere | Curfew vibes if Dominion still strong elsewhere |
| Secrets | Optional black-market tide tech appears |

---

## 10) Navigation / Collision Notes

1. **Dock readability:** Wide pads every 10–12 tiles so players don't snag on props
2. **Mount restriction:** Enforce "no mounts on tight piers" via subtle signage + collision funnels
3. **Fast lane:** Breakwater Market should be the efficient route from overworld spawn → docks → D5 exit

---

## 11) Secrets & Collectibles

| Secret | Coordinates | Loot / Effect |
|--------|-------------|---------------|
| **Chest behind stacked nets** | (64, 82) | "Brineguard Charm" mat |
| **Hidden bottle note** | (30, 22) | Near chapel walkway — Tide lore |
| **Pet sniff spot** [post-tame] | (92, 90) | Rare "Saltglass Resin" |
| **Terminal ping** [post-D5] | (88, 44) | Reveals hidden sea-node marker (Sunken City breadcrumb) |

---

## Quick Reference Map Overview

```
                        NORTH
                          ↑
    ┌───────────────────────────────────────────────────────────┐
    │                                                           │
    │    DISTRICT 5: Quiet Tide          DISTRICT 2:            │
    │    (x 18–56, y 18–46)            Breakwater Market        │
    │    - Salt Chapel                  (x 62–118, y 30–62)     │
    │    - Tide lore                     - Gear stalls          │
    │      door (34,34)                  - Terminal (88,44)     │
    │    BOTTLE NOTE (30,22)             - Overworld exit       │
    │                                      (119,34)             │
    │                                      SPAWN A (106,32)     │
    │                                    ═══════════════════    │
    │    ══════════════════════════════  DISTRICT 3: Diver's    │
    │    DISTRICT 6: Customs Corner      Row (x 10–46, y 46–78) │
    │    (x 0–22, y 62–92)               - Dive shop (28,66)    │
    │    - Dominion pressure             - Clinic (20,58)       │
    │    - door (10,78)                  - Hull & Hook (44,58)  │
    │                                                           │
    │         ═══════════════════════════════════════════════   │
    │              DISTRICT 1: Stormbreak Docks                 │
    │                (x 36–86, y 52–92)                         │
    │    - Main hub - Quest board (72,66)                       │
    │    - Inn door (74,74)                                     │
    │    - SPAWN C (70,70)                                      │
    │    - Chest (64,82)                                        │
    │                                                           │
    │              ═══════════════════════════  DISTRICT 4:     │
    │                                            Harbor Office  │
    │    CHEST (64,82)                           (x 90–118)     │
    │    STACKED NETS                              - Tickets    │
    │                              FERRY GATE      - door       │
    │                              (112,90)        (104,78)     │
    │    PET SNIFF (92,90)                                      │
    │                                                           │
    │    SPAWN B (58,90) ←────  D5 EXIT (46,95)                 │
    │                           SUNKEN CITY (74,94) [post-D5]   │
    │                                                           │
    └───────────────────────────────────────────────────────────┘
```

**Key Anchors Summary:**

| Feature | Coordinates |
|---------|-------------|
| **Overworld Exit** | (119, 34) |
| **Spawn A** (overworld arrival) | (106, 32) |
| **Spawn B** (D5 return) | (58, 90) |
| **Spawn C** (night) | (70, 70) |
| **Terminal** | (88, 44) |
| **D5 Exit** (Abyss Entry Pier) | (46, 95) |
| **Sunken City boat** [post-D5] | (74, 94) |
| **Ferry to Chronowake** | (112, 90) |
| **Inn** | (74, 74) |
| **Dive Shop** | (28, 66) |
| **Clinic** | (20, 58) |
| **General Goods** | (90, 58) |
| **Harbor Office** | (104, 78) |
| **Shipwright** | (44, 58) |
| **Chapel** | (34, 34) |
| **Customs Office** | (10, 78) |
| **Quest Board** | (72, 66) |
| **Chest** | (64, 82) |
| **Bottle Note** | (30, 22) |
| **Pet Sniff Spot** | (92, 90) |
