# Chroma's Edge — Rimehold Town Map Sheet (v1)
## Wind-Bitten Fortress-Town — "Negotiating with Winter Every Day"

---

## 0) Town Technical Specs

| Parameter | Value |
|-----------|-------|
| **Town Name** | Rimehold |
| **Role** | D7 staging hub + Time gear economy + ferry link to Chronowake + phase-barrier traversal unlock town (post-D7) |
| **Map Size** | 112 × 96 tiles (1792 × 1536 px) |
| **Encounter Rate** | 0% (safe zone) |
| **Time States** | Day / Night |
| **Night Atmosphere** | Aurora shimmer + stronger "time static" VFX at certain props |
| **Town Terminal** | Yes — frost-sealed, humming |
| **Mounts** | Allowed (D3+) — restricted in inner walls (tight alleys + ice steps); allowed on Outer Snow Road |
| **Town Hazards** | None (icy slip VFX + drifting snow are set dressing) |

---

## 1) Visual Identity (Art Direction)

| Element | Description |
|---------|-------------|
| **Materials** | Dark stone, icebrick, iron braces, insulated pipework, warm window slits |
| **Palette** | Slate/blue ice + pale white snow + warm amber lamps + faint violet chrono-glow |

### Signature Props

| Prop | Description |
|------|-------------|
| **Heat-pipe rails** | Steam breath |
| **Frost clocks** | Faces cracked, hands moving wrong at night |
| **Aurora banners** | Local identity, not "magic cult" |
| **Chrono wards** | Glyph plates embedded in walls |

---

## 2) Town Layout (District Blocks)

### District 1 — Gatecourt (Main Hub)

| Property | Value |
|----------|-------|
| **Bounds** | x 38–78, y 44–76 |
| **Features** | Central square: quest board, inn access, key NPCs, clear navigation |

### District 2 — Warmworks Row (Forge + Press + Timecraft)

| Property | Value |
|----------|-------|
| **Bounds** | x 8–38, y 50–84 |
| **Features** | Workshops for Timeguard gear, stasis balms, and phase tools |

### District 3 — Ferry Steps (Chronowake Link)

| Property | Value |
|----------|-------|
| **Bounds** | x 78–112, y 62–96 |
| **Features** | Sloped stone steps down to docks (ferry terminal + ticket hall) |

### District 4 — Citadel Approach Quarter (D7 Staging)

| Property | Value |
|----------|-------|
| **Bounds** | x 78–112, y 10–44 |
| **Features** | Watchtowers, route boards, "Rime Causeway" departure |

### District 5 — Boreal Residences

| Property | Value |
|----------|-------|
| **Bounds** | x 38–78, y 76–96 |
| **Features** | Tight homes, soup lines, local life |

### District 6 — Quiet Annex (Chapel + Archives)

| Property | Value |
|----------|-------|
| **Bounds** | x 8–44, y 10–50 |
| **Features** | Lore room, calm scenes, "time anomaly" foreshadowing |

---

## 3) Key Anchors & Coordinates (Local 0–111, 0–95)

### Main Spawn Points

| Spawn | Coordinates | Context |
|-------|-------------|---------|
| **SPAWN A** (overworld snow road) | (20, 94) | Warmworks edge |
| **SPAWN B** (ferry/Chronowake) | (96, 90) | Ferry Steps |
| **SPAWN C** (D7 return) | (98, 24) | Citadel Approach |

### Town Terminal

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Rimehold Lattice Terminal** | (30, 30) | Pre-D7: "unstable time readings"; Post-D7: phase-barrier routing + Chronowake "time lane" markers |

### Exits (Edge Triggers)

| Exit To | Coordinates | Notes |
|---------|-------------|-------|
| **Overworld — South Snow Road** | (22, 95) | — |
| **Frozen Citadel Approach** (Rime Causeway) | (111, 24) | D7 micro-map |
| **Ferry Route** (Chronowake Pier) | (104, 95) | East edge |
| **Phase Barrier Pass** [post-D7] | (0, 26) | West edge, hidden route |

---

## 4) Main Buildings (Exterior Door Tiles)

| Building | Door Coordinates | Function |
|----------|------------------|----------|
| **The Hearth Below** (Inn) | (56, 74) | Rest, rumors, warm steam pipes |
| **Secondhand Works** (Timecraft) | (22, 62) | Stasis balms, phase tools, Timeguard gear |
| **Frostward Aid** (Clinic) | (44, 74) | Stasis cures, phase sickness treatment |
| **Wool & Wick** (General Goods) | (70, 78) | Consumables, cold-weather wraps |
| **Clocksteel Press** (Pressworks) | (14, 72) | Armor plating, chrono bands, initiative gear |
| **Ledger of Seasons** (Archive) | (22, 34) | Lore hub, quest turn-in, D7 hints |
| **Aurora Quiet** (Chapel) | (34, 40) | Calm scenes, time anomaly foreshadow |
| **Ferry Ticket Hall** | (92, 78) | Chronowake ferry routing |
| **Watch Captain Office** | (96, 34) | D7 access gating, permit pressure scenes |
| **Quest Board** | (58, 66) | Gatecourt center |
| **Mount Hitch** [post-D3] | (78, 86) | Top of Ferry Steps |

---

## 5) Interior Maps (Required)

### 1) The Hearth Below (Inn)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 34 × 22 |
| **Entry Pad** | (17, 20) |
| **Features** | Rest/save, rumor board, warm steam pipes |

### 2) Secondhand Works (Timecraft Shop)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 36 × 24 |
| **Entry Pad** | (18, 22) |
| **Services** | Stasis balms, phase tools (post-D7), timeguard accessory upgrades |

### 3) Frostward Aid (Clinic)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 30 × 20 |
| **Entry Pad** | (15, 18) |
| **Services** | Stasis, slow, "phase sickness" (post-D7), general cures |

### 4) Clocksteel Press (Pressworks)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 34 × 20 |
| **Entry Pad** | (17, 18) |
| **Services** | Armor plating, chrono bands, "initiative" gear |

### 5) Ledger of Seasons (Archive Hall)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 30 × 20 |
| **Entry Pad** | (15, 18) |
| **Services** | Lore hub, quest turn-in, D7 hints (phase mechanics explained in-world) |

### 6) Ferry Ticket Hall

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 28 × 18 |
| **Entry Pad** | (14, 16) |
| **Services** | Route UI to Chronowake, late-game optional routes |

### 7) Watch Captain Office (Gate Control)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 22 × 16 |
| **Entry Pad** | (11, 14) |
| **Services** | D7 access gating, permit pressure scenes if Dominion escalation active |

---

## 6) Shops + Services (Inventory by Progress)

### Base (Pre-D7)

#### Wool & Wick

| Item | Type |
|------|------|
| Potions, Ethers, Antidotes | Consumables |
| Smoke Bombs | Escape aid |
| Cold-weather wraps | Defense buff |

#### Secondhand Works

| Item | Description |
|------|-------------|
| Stasis Balm (limited) | Reduces stasis buildup |
| "Warm Coil" | Reduces stasis buildup for X battles |
| Minor accessories | — |

#### Pressworks

| Item | Description |
|------|-------------|
| Basic Time-adjacent plating | Speed/initiative |
| Stasis resist charm (small) | — |

#### Clinic

| Service | Price |
|---------|-------|
| Stasis cures | Mid price |
| General cures | — |

---

### After D7 (Time Relic Seated) — Major Upgrade

#### Secondhand Works Expansion

| Item | Description |
|------|-------------|
| Phase Key consumables | Temporarily reveal phase doors on overworld |
| Rewind Step enhancer items | Upgrade field tech |
| Chrono Band upgrade line | — |

#### Pressworks Expansion

| Item | Description |
|------|-------------|
| Aeon Lens crafting mats | High-tier crit resist / hazard reduction |
| "Turn-Order" accessories | Combat initiative support |

#### Terminal Update

| Feature | Effect |
|---------|--------|
| Phase-barrier paths | Show on overworld |
| Chronowake "time lane" nodes | Revealed |

---

### Mid/Late Game

| Addition | Notes |
|----------|-------|
| Rare Time mats | Paradox Glass, Clocksteel Shards for endgame gear and hidden zones |

---

## 7) NPC List (Placement + Function)

### Story-Critical

| NPC | Schedule | Location |
|-----|----------|----------|
| **Warden "Elowen Thorne"** (steady leader) | Day | Gatecourt (58, 58) |
| | Night | Archive Hall interior |
| **Timewright "Orla Venn"** (phase expert) | Day | Secondhand Works |
| | Night | Terminal (30, 30) listening to the hum |
| **Watch Captain "Garrik Sleet"** | Day | Watch Office |
| | Night | Citadel Approach (100, 22) |

### Utility

| NPC | Location | Function |
|-----|----------|----------|
| Innkeeper | The Hearth Below | Rest services |
| Medic | Frostward Aid | Healing |
| Press Vendor | Clocksteel Press | Crafting bench |
| General Vendor | Wool & Wick | Standard goods |
| Ferry Clerk | Ticket Hall | Routing |
| Archivist | Ledger of Seasons | Lore |

### Flavor

| NPC | Description |
|-----|-------------|
| Pipe-worker | Tapping steam lines (District 2) |
| Kid counting clock ticks | Noticing "wrong" times (District 5) |
| Sailor | Waiting for Chronowake ferry (District 3) |

### Dominion Pressure NPC (Phase-Based)

| NPC | Phase | Location | Behavior |
|-----|-------|----------|----------|
| **Chrono Auditor** | PHASE 1+ | Near Ticket Hall (90, 70) | Paperwork intimidation, no fights |

---

## 8) Quest Hooks (Rimehold-Specific)

### Main Story (D7 Setup)

| Quest | Description |
|-------|-------------|
| **"The Causeway Opens"** | Meet Warden → get clearance to approach Frozen Citadel |
| **"Stasis Remedy"** | Clinic/Timewright tutorial: stasis fields + phase altars |

### Sidequests (Pre-D7)

| Quest | Objective | Reward |
|-------|-----------|--------|
| **Pipe Leak** | Fix 3 steam pipe nodes around town | Stasis Balm bundle |
| **Lost Ledger Page** | Small search in Quiet Annex | Discount + lore |

### Sidequests (Post-D7)

| Quest | Objective | Reward |
|-------|-----------|--------|
| **Phase Barrier Survey** | Unlock west exit (0, 26) route | Hidden path access |
| **Chronowake Contract** | Establish reliable ferry | Cheaper ferry + late-game route node |
| **Clocksteel Tempering** | Craft upgrade tier | Timeguard gear improvements |

---

## 9) Story-State Phases (Town Evolution)

### PHASE 0 — First Arrival (Hard Winter, Stable People)

| Aspect | State |
|--------|-------|
| Clocks | Mostly "normal" |
| Terminal | Low static |
| Atmosphere | Functional, cold but stable |

### PHASE 1 — Dominion Pressure Rising

| Aspect | State |
|--------|-------|
| Presence | Auditors, harsher signage |
| Night | Watch patrols more visible |
| Terminal | More static interference |

### PHASE 2 — After D7 Clear

| Aspect | State |
|--------|-------|
| Aurora | Feels calmer |
| Clocks | Stop "skipping" |
| Shops | Upgrade available |
| Terminal | Genuinely useful for routing |

### PHASE 3 — Midgame Revisit

| Aspect | State |
|--------|-------|
| Travelers | More pass through |
| Ferry Steps | Busier |
| Archive | Deeper lore entries |

### PHASE 4 — Late Game

| Aspect | State |
|--------|-------|
| Night | Curfew vibe if Dominion still strong |
| Quiet Annex | Strong scene hub for big character conversations |

---

## 10) Navigation / Collision Notes

1. **Gatecourt:** Keep open with 2–3 big lanes (fast access to inn/clinic/board)
2. **Citadel Approach:** Visually obvious exit (watchtowers + banners pointing east)
3. **Ferry Steps:** Slope cleanly—no snaggy props on main descent lane

---

## 11) Secrets & Collectibles

| Secret | Coordinates | Loot / Effect |
|--------|-------------|---------------|
| **Chest behind pipe stack** | (16, 44) | Paradox Glass (rare mat) |
| **Hidden clock face note** [night] | (62, 84) | Starts post-D7 sidequest |
| **Pet sniff spot** [post-tame] | (86, 18) | "Rime Resin" (rare craft mat) |
| **Terminal ping** [post-D7] | (30, 30) | Reveals hidden phase-door marker on overworld |

---

## Quick Reference Map Overview

```
                        NORTH
                          ↑
    ┌───────────────────────────────────────────────────────────┐
    │                                                           │
    │    DISTRICT 6: Quiet Annex                                │
    │    (x 8–44, y 10–50)                                      │
    │    - Ledger of Seasons door (22,34)                       │
    │    - Aurora Quiet chapel (34,40)                          │
    │    - Terminal (30,30)                                     │
    │    - CHEST (16,44): Paradox Glass                         │
    │    - Phase Barrier Exit [post-D7]: (0,26)                 │
    │                                                           │
    │         ═══════════════════════════════════               │
    │                                                           │
    │    DISTRICT 2: Warmworks Row                              │
    │    (x 8–38, y 50–84)                                      │
    │    - Secondhand Works door (22,62)                        │
    │    - Clocksteel Press door (14,72)                        │
    │                                                           │
    │              ═══════════════════════════════════          │
    │                                                           │
    │         DISTRICT 1: Gatecourt          DISTRICT 4:        │
    │         (x 38–78, y 44–76)           Citadel Approach     │
    │         - Quest Board (58,66)        (x 78–112, y 10–44)  │
    │         - Inn door (56,74)           - Watch Office       │
    │         - SPAWN A (20,94)              door (96,34)       │
    │                                      - SPAWN C (98,24)    │
    │                                      - D7 Exit (111,24)   │
    │                                                           │
    │    ════════════════════════════════════                   │
    │                                                           │
    │    DISTRICT 5: Boreal Residences      DISTRICT 3:         │
    │    (x 38–78, y 76–96)               Ferry Steps           │
    │    - Clinic door (44,74)            (x 78–112, y 62–96)   │
    │    - General Goods door (70,78)     - Ferry Hall door     │
    │    - CLOCK NOTE (62,84) [night]       (92,78)             │
    │                                     - SPAWN B (96,90)     │
    │                                     - Ferry Exit (104,95) │
    │                                     - Mount Hitch (78,86) │
    │                                                           │
    │    PET SNIFF (86,18)                                      │
    │                                                           │
    │    Overworld exit: (22,95) South                          │
    │                                                           │
    └───────────────────────────────────────────────────────────┘
```

**Key Anchors Summary:**

| Feature | Coordinates |
|---------|-------------|
| **Spawn A** (overworld) | (20, 94) |
| **Spawn B** (ferry) | (96, 90) |
| **Spawn C** (D7 return) | (98, 24) |
| **Terminal** | (30, 30) |
| **D7 Exit** (Rime Causeway) | (111, 24) |
| **Ferry Exit** | (104, 95) |
| **Phase Barrier** [post-D7] | (0, 26) |
| **Overworld South** | (22, 95) |
| **Inn** | (56, 74) |
| **Secondhand Works** | (22, 62) |
| **Clinic** | (44, 74) |
| **General Goods** | (70, 78) |
| **Pressworks** | (14, 72) |
| **Archive** | (22, 34) |
| **Chapel** | (34, 40) |
| **Ferry Hall** | (92, 78) |
| **Watch Office** | (96, 34) |
| **Quest Board** | (58, 66) |
| **Mount Hitch** | (78, 86) |
| **Chest** | (16, 44) |
| **Clock Note** [night] | (62, 84) |
| **Pet Sniff** | (86, 18) |
