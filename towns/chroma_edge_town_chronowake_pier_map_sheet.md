# Chroma's Edge — Chronowake Pier Town Map Sheet (v1)
## Fog-Soaked Pier-Town — "Boats Arrive Before They Left"

---

## 0) Town Technical Specs

| Parameter | Value |
|-----------|-------|
| **Town Name** | Chronowake Pier |
| **Role** | Time-route hub + ferry nexus + phase-barrier navigation town (post-D7), "Time is infrastructure" showcase |
| **Map Size** | 120 × 92 tiles (1920 × 1472 px) |
| **Encounter Rate** | 0% (safe zone) |
| **Time States** | Day / Night |
| **Night Atmosphere** | Heavier fog + brighter chrono buoys + occasional "skip frame" VFX |
| **Town Terminal** | YES (Major) — Time routing UI hub |
| **Mounts** | Allowed (D3+) — restricted on narrow piers (upper boardwalk only) |
| **Town Special** | Time Lane Ferries (some routes only appear after Time relic seated) |

---

## 1) Visual Identity (Art Direction)

| Element | Description |
|---------|-------------|
| **Materials** | Wet black timber, old stone pylons, brass fittings, glass buoy lanterns, rope netting |
| **Palette** | Slate + sea green + pale cyan chrono glow + warm amber dock lamps |

### Signature Props

| Prop | Description |
|------|-------------|
| **Chrono Buoys** | "Ping" in irregular rhythm |
| **Time-silt sandglasses** | Embedded in rails |
| **Arrival boards** | Wrong times (subtle humor + dread) |
| **Phase-gate pylons** | Three-pronged, Past/Present/Future icons |

---

## 2) Town Layout (District Blocks)

### District 1 — Main Pier Concourse (Hub)

| Property | Value |
|----------|-------|
| **Bounds** | x 40–86, y 44–84 |
| **Features** | Big open dock deck: terminal, ticket hall, quest board, vendors |

### District 2 — Buoyline Docks (Time-Lane Berths)

| Property | Value |
|----------|-------|
| **Bounds** | x 86–120, y 48–92 |
| **Features** | Where "time ferries" berth; more chrono glow + fog |

### District 3 — Old Wharf (Local Life)

| Property | Value |
|----------|-------|
| **Bounds** | x 10–44, y 52–92 |
| **Features** | Fishers, repair benches, small inn, quiet NPC beats |

### District 4 — Phaseyard (Calibration / Tech Row)

| Property | Value |
|----------|-------|
| **Bounds** | x 8–44, y 18–52 |
| **Features** | Timewright workshop, stabilizers, phase tools |

### District 5 — Harbor Office + Customs

| Property | Value |
|----------|-------|
| **Bounds** | x 44–86, y 18–44 |
| **Features** | Permits, ferry routing, "chronological compliance" tension |

### District 6 — Sea Wall Walk (Scenic + Secrets)

| Property | Value |
|----------|-------|
| **Bounds** | x 0–18, y 14–84 |
| **Features** | Windy walkway with hidden lore + night-only pings |

---

## 3) Key Anchors & Coordinates (Local 0–119, 0–91)

### Main Spawn Points

| Spawn | Coordinates | Context |
|-------|-------------|---------|
| **SPAWN A** (Rimehold ferry) | (94, 88) | Buoyline dock |
| **SPAWN B** (Brinegate ferry) | (72, 88) | Main Concourse south edge |
| **SPAWN C** (overworld coast) | (12, 90) | Old Wharf edge |

### Town Terminal (Major)

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Chronowake Lattice Terminal** | (64, 62) | Pre-D7: limited functions; Post-D7: full Phase Lane Routing + barrier markers + time-lane ferry schedule |

### Exits (Edge Triggers)

| Exit To | Coordinates | Notes |
|---------|-------------|-------|
| **Ferry: Rimehold Route** | (104, 91) | East edge |
| **Ferry: Brinegate Route** | (70, 91) | South edge |
| **Overworld Coast Road** | (0, 64) | West edge |
| **Phase-Lane Crossing** [post-D7] | (119, 36) | East edge, locked until Time seated |

---

## 4) Main Buildings (Exterior Door Tiles)

| Building | Door Coordinates | Function |
|----------|------------------|----------|
| **The Wake & Wicker** (Inn) | (26, 74) | Rest, stories of impossible boats |
| **Saltclock Supply** (General Goods) | (54, 74) | Standard supplies + Clockseal consumables |
| **Tide & Time Aid** (Clinic) | (40, 74) | Stasis + pressure cures, calm draughts |
| **Buoy & Bell Workshop** (Timewright) | (24, 36) | Stasis balms, phase keys, timecraft upgrades |
| **Harbor Office / Ticket Hall** | (68, 34) | Ferry schedule UI, phase-lane access |
| **Chrono Compliance Office** (Customs) | (84, 34) | Permits, compliance tension |
| **Keel & Knot** (Boat Repair) | (14, 60) | Crafting bench, nautical gear |
| **Quest Board** | (60, 72) | Main Concourse center |
| **Mount Hitch** [post-D3] | (40, 86) | Upper concourse |

---

## 5) Interior Maps (Required)

### 1) The Wake & Wicker (Inn)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 34 × 22 |
| **Entry Pad** | (17, 20) |
| **Vibe** | Warm lamps, wet coats, "boats that don't make sense" stories |

### 2) Buoy & Bell Workshop (Timewright Shop)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 36 × 24 |
| **Entry Pad** | (18, 22) |
| **Inventory** | Stasis balms, phase keys, timecraft upgrades (post-D7) |

### 3) Harbor Office / Ticket Hall

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 30 × 20 |
| **Entry Pad** | (15, 18) |
| **Function** | Ferry schedule UI + phase-lane access gating |

### 4) Chrono Compliance Office (Dominion-ish Pressure Room)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 22 × 16 |
| **Entry Pad** | (11, 14) |
| **Function** | Tension + sidequest hub ("audit," permits) |

### 5) Tide & Time Aid (Clinic)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 30 × 20 |
| **Entry Pad** | (15, 18) |
| **Services** | Stasis + pressure cures, "calm draughts" |

### 6) Saltclock Supply (General Goods)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 28 × 18 |
| **Entry Pad** | (14, 16) |
| **Inventory** | Standard supplies + "Clockseal" consumables (reduce phase hazard next X battles) |

---

## 6) Shops + Services (Inventory by Progress)

### Base (Pre-D7 / Early Access)

#### General Goods

| Item | Type |
|------|------|
| Potions, Ethers | Consumables |
| Rope Kits | Crafting mat |
| Lanterns | Exploration aid |

#### Clinic

| Item | Description |
|------|-------------|
| Stasis Balm (limited) | Stasis resist |
| Silence cures | Status heal |

#### Timewright

| Item | Description |
|------|-------------|
| Small stasis resist accessories | — |
| "Warm Coil" items | Stasis buildup reduction |

#### Harbor Office

| Route | Status |
|-------|--------|
| Rimehold ↔ Chronowake | Basic ferry route |

---

### After D7 (Time Relic Seated) — Major Upgrade

#### Terminal (Routing Hub)

| Feature | Effect |
|---------|--------|
| Phase Barriers | Shown on map |
| Stabilized crossings | Revealed |
| Time lane ferries | Routes to special nodes |

#### Timewright Expansion

| Item | Description |
|------|-------------|
| Phase Key consumables | Reveal phase doors on overworld |
| Rewind Step enhancers | Upgrade field tech |
| Chrono Band upgrades | — |

#### Harbor Office Expansion

| Feature | Effect |
|---------|--------|
| Reliable Brinegate route | Opens |
| Phase-Lane Crossing micro-map | Unlocks |

---

### Mid/Late Game

| Addition | Notes |
|----------|-------|
| Rare mats | Paradox Glass, Buoycore Brass, Clocksteel filings |
| Optional "black ledger" vendor | Night only; shady choices |

---

## 7) NPC List (Placement + Function)

### Story-Critical

| NPC | Schedule | Location |
|-----|----------|----------|
| **Pierwarden "Sana Merrow"** (machine-runner) | Day | Main Concourse (66, 70) |
| | Night | Sea Wall Walk (10, 44) |
| **Timewright "Galen Quill"** (calibrator) | Day | Workshop interior |
| | Night | Terminal (64, 62) listening to pings |
| **Ferry Master "Old Tern"** (comic + wisdom) | Day | Ticket Hall |
| | Night | Inn interior |

### Dominion Pressure NPC

| NPC | Phase | Location | Behavior |
|-----|-------|----------|----------|
| **Chrono Auditor "Mave Rell"** | PHASE 1+ | Near Customs (86, 30) | Harsher post-D7 ("compliance checks") |

### Utility

| NPC | Location | Function |
|-----|----------|----------|
| Innkeeper | The Wake & Wicker | Rest |
| Medic | Tide & Time Aid | Healing |
| General Vendor | Saltclock Supply | Goods |
| Repair Bench Vendor | Keel & Knot | Crafting |
| Dockhand | Buoyline Docks | Flavor |

### Flavor

| NPC | Description |
|-----|-------------|
| Fisher who met himself yesterday | Old Wharf |
| Kid chasing "backwards foam" | Buoyline Docks |
| Sailor with "late arrival receipt" | Main Concourse |

---

## 8) Quest Hooks (Chronowake-Specific)

### Main Story (Post-D7 Integration)

| Quest | Description |
|-------|-------------|
| **"Lane Stabilization"** | Use terminal to mark phase crossing route (routing UI tutorial) |
| **"Audit Pressure"** | Deal with compliance office (noncombat or optional skirmish) |

### Sidequests

| Quest | Objective | Reward |
|-------|-----------|--------|
| **Missing Buoy** | Recover buoy core from nearby micro-map | Discount + terminal cosmetic change |
| **Backwards Cargo** | Deliver crate that must arrive "before dusk" | Time-themed fun reward |
| **Sea Wall Echo** | Night-only interaction | Reveals hidden phase door marker |

---

## 9) Story-State Phases (Town Evolution)

### PHASE 0 — First Arrival

| Aspect | State |
|--------|-------|
| Atmosphere | Mostly normal pier town |
| Arrival boards | Odd times (flavor) |
| Terminal | Limited use |

### PHASE 1 — Dominion Pressure Rising

| Aspect | State |
|--------|-------|
| Presence | Auditors, permit signage |
| Customs | More presence |

### PHASE 2 — Post-D7 Clear

| Aspect | State |
|--------|-------|
| Time-lane berths | Activate |
| Buoy glow | Steadies |
| Ferry routes | Expand |

### PHASE 3 — Midgame Revisit

| Aspect | State |
|--------|-------|
| Travelers | More "time tourists" |
| Trade | New goods |

### PHASE 4 — Late Game

| Aspect | State |
|--------|-------|
| Night | Curfew vibe |
| Workshop | Stays open (player needs it) |

---

## 10) Navigation / Collision Notes

1. **Main Concourse:** Keep open and rectangular (fast access to terminal/board/vendors)
2. **Buoyline Docks:** Narrow planks force walking (no mounts)
3. **Sea Wall Walk:** Clear side path with 2–3 small secret nooks, not a maze

---

## 11) Secrets & Collectibles

| Secret | Coordinates | Loot / Effect |
|--------|-------------|---------------|
| **Chest under sea wall stairs** | (6, 74) | Paradox Glass (rare mat) |
| **Night-only buoy ping spot** | (110, 70) | Reveals 1 hidden phase-door marker |
| **Pet sniff spot** [post-tame] | (18, 86) | "Drift Resin" (rare craft mat) |
| **Terminal ping** [post-D7] | (64, 62) | Reveals "time lane" to future hidden area node |

---

## Quick Reference Map Overview

```
                        NORTH
                          ↑
    ┌───────────────────────────────────────────────────────────┐
    │                                                           │
    │    DISTRICT 4: Phaseyard          DISTRICT 5:             │
    │    (x 8–44, y 18–52)              Harbor Office +         │
    │    - Timewright door (24,36)      Customs                 │
    │                                     (x 44–86, y 18–44)    │
    │                                   - Harbor Office door    │
    │    DISTRICT 6: Sea Wall Walk        (68,34)               │
    │    (x 0–18, y 14–84)              - Customs door (84,34)  │
    │    - Windy walkway                - Auditor (86,30)       │
    │    - CHEST (6,74)                                         │
    │    - Pierwarden night: (10,44)    ═══════════════════     │
    │                                                           │
    │         ══════════════════════════════════════════════    │
    │                                                           │
    │         DISTRICT 1: Main Pier Concourse                   │
    │         (x 40–86, y 44–84)                                │
    │         - Terminal (64,62)                                │
    │         - Quest Board (60,72)                             │
    │         - Inn door (26,74)                                │
    │         - Clinic door (40,74)                             │
    │         - General Goods door (54,74)                      │
    │         - Mount Hitch (40,86)                             │
    │                                                           │
    │    ═══════════════════════════════════════════            │
    │                                                           │
    │    DISTRICT 3: Old Wharf            DISTRICT 2:           │
    │    (x 10–44, y 52–92)             Buoyline Docks          │
    │    - Repair Bench door (14,60)    (x 86–120, y 48–92)     │
    │    - SPAWN C (12,90)              - Time-lane berths      │
    │    - PET SNIFF (18,86)            - Chrono glow + fog     │
    │                                   - SPAWN A (94,88)       │
    │                                   - BUOY PING (110,70)    │
    │                                                         │
    │    SPAWN B (72,88)                                      │
    │                                                           │
    │    Ferry exits: (104,91) Rimehold, (70,91) Brinegate    │
    │    Overworld: (0,64) West                               │
    │    Phase-Lane [post-D7]: (119,36) East                  │
    │                                                           │
    └───────────────────────────────────────────────────────────┘
```

**Key Anchors Summary:**

| Feature | Coordinates |
|---------|-------------|
| **Spawn A** (Rimehold ferry) | (94, 88) |
| **Spawn B** (Brinegate ferry) | (72, 88) |
| **Spawn C** (overworld) | (12, 90) |
| **Terminal** | (64, 62) |
| **Rimehold Ferry** | (104, 91) |
| **Brinegate Ferry** | (70, 91) |
| **Overworld West** | (0, 64) |
| **Phase-Lane** [post-D7] | (119, 36) |
| **Inn** | (26, 74) |
| **General Goods** | (54, 74) |
| **Clinic** | (40, 74) |
| **Timewright Workshop** | (24, 36) |
| **Harbor Office** | (68, 34) |
| **Customs Office** | (84, 34) |
| **Repair Bench** | (14, 60) |
| **Quest Board** | (60, 72) |
| **Mount Hitch** | (40, 86) |
| **Chest** | (6, 74) |
| **Buoy Ping** [night] | (110, 70) |
| **Pet Sniff** | (18, 86) |
