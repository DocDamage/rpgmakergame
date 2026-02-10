# Chroma's Edge — Gravemark Outpost Town Map Sheet (v1)
## Quarry Settlement on the Edge of the Sable Expanse — "Every Word Costs Something"

---

## 0) Town Technical Specs

| Parameter | Value |
|-----------|-------|
| **Town Name** | Gravemark Outpost |
| **Role** | D6 staging hub + Mass gear economy + crafting expansion + gateway to Obsidian Quarry/Molten Core |
| **Map Size** | 104 × 88 tiles (1664 × 1408 px) |
| **Encounter Rate** | 0% (safe zone) |
| **Time States** | Day / Night |
| **Day Atmosphere** | Work crews, cranes moving |
| **Night Atmosphere** | Quieter, more "gravity hum," stronger Dominion presence if pressure high |
| **Town Terminal** | Yes — reinforced, low-glow, "industrial lattice" vibe |
| **Mounts** | Allowed (D3+) — restricted in inner yard (tight gantries + cargo rails) |
| **Town Hazard Flavor** | Dust fall, distant rock groan, chain clinks (no damage) |

---

## 1) Visual Identity (Art Direction)

| Element | Description |
|---------|-------------|
| **Materials** | Black timber, riveted iron plates, basalt foundations, thick rope, pulley towers |
| **Palette** | Soot black, quarry gray, rust red, dim amber lamps, faint violet "gravity scar" shimmer |

### Signature Props

| Prop | Description |
|------|-------------|
| **Counterweight towers** | Big silhouette |
| **Ore rail tracks** | Running through town |
| **Anchor plates** | Embedded in ground (Mass foreshadow) |
| **Falling-dust VFX** | In certain alleys (visual only) |

---

## 2) Town Layout (District Blocks)

### District 1 — Anchor Yard (Central Hub)

| Property | Value |
|----------|-------|
| **Bounds** | x 34–74, y 34–68 |
| **Features** | Wide yard with rails + loading pads; main NPC congregation + quest board |

### District 2 — Forge & Press Row (Mass Crafting)

| Property | Value |
|----------|-------|
| **Bounds** | x 6–34, y 40–74 |
| **Features** | Heavy forge, press machines, armor plating, anchor gear |

### District 3 — Railhead Gate (Quarry Access)

| Property | Value |
|----------|-------|
| **Bounds** | x 74–104, y 52–86 |
| **Features** | Cargo gate, ore lift signs, route markers → leads to D6 entrance micro-map |

### District 4 — Bunkhouse Strip (Inn + Rest)

| Property | Value |
|----------|-------|
| **Bounds** | x 34–70, y 68–88 |
| **Features** | Sleeping blocks, stew line, low chatter, "work town" vibe |

### District 5 — Stabilizer Pumpworks

| Property | Value |
|----------|-------|
| **Bounds** | x 8–40, y 10–40 |
| **Features** | Gravity stabilizer rigs + counterweight stations (explains Mass systems diegetically) |

### District 6 — Dominion Ledger Booth (Pressure Corner)

| Property | Value |
|----------|-------|
| **Bounds** | x 0–18, y 62–88 |
| **Features** | Paperwork, permits, "safety inspections," intimidation without guns drawn |

---

## 3) Key Anchors & Coordinates (Local 0–103, 0–87)

### Main Spawn Points

| Spawn | Coordinates | Context |
|-------|-------------|---------|
| **SPAWN A** (overworld/Meridian Junction) | (14, 78) | North/west approach |
| **SPAWN B** (quarry return) | (96, 74) | From D6 dungeon |
| **SPAWN C** (night return) | (52, 60) | Anchor Yard center |

### Town Terminal

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Gravemark Lattice Terminal** | (26, 22) | Reinforced housing, low glow; post-D6 shows "gravity lanes stabilized" + Dragon's Graveyard breadcrumb |

### Exits (Edge Triggers)

| Exit To | Coordinates | Notes |
|---------|-------------|-------|
| **Overworld — North** (Meridian Junction/wastes) | (52, 87) | — |
| **Overworld — West** (Sable flats/optional) | (0, 44) | — |
| **Obsidian Quarry (D6)** approach | (103, 74) | East edge |
| **Dragon's Graveyard** [post-D6] | (8, 6) | Locked until Mass seated |

---

## 4) Main Buildings (Exterior Door Tiles)

| Building | Door Coordinates | Function |
|----------|------------------|----------|
| **The Heavy Blanket** (Inn/Bunkhouse) | (52, 78) | Rest, rumors, character beats |
| **Anvil & Anchor** (Forge) | (18, 62) | Weapon/armor upgrades, Mass crafts |
| **Plate & Pinion** (Pressworks) | (28, 70) | Plating mods, belt/gear QoL |
| **Rations & Rivets** (General Goods) | (66, 72) | Consumables, basic gear |
| **Dustward Aid** (Clinic) | (62, 80) | Status cures, Mass debuff healing |
| **Counterweight Station** (Stabilizer Office) | (24, 30) | Tutorial, story gating |
| **Dominion Ledger Booth** | (10, 78) | Permits, tension, sidequest turn-ins |
| **Quest Board** | (54, 66) | Anchor Yard center |
| **Mount Hitch** [post-D3] | (70, 74) | Outside bunkhouse; mounts not allowed deeper |

---

## 5) Interior Maps (Required)

### 1) The Heavy Blanket (Inn/Bunkhouse)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 32 × 20 |
| **Entry Pad** | (16, 18) |
| **Vibe** | Thick walls, hammocks, stew pot |

### 2) Anvil & Anchor (Forge)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 42 × 26 |
| **Entry Pad** | (21, 24) |
| **Services** | Weapon/armor upgrades (heavy tier), Mass resist crafts |
| **Post-D6** | Gravity-lane tack modules, Anchor Step accessories |

### 3) Plate & Pinion (Pressworks)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 34 × 20 |
| **Entry Pad** | (17, 18) |
| **Services** | Plating mods (DEF, knockback resist), belt/gear QoL items |

### 4) Dustward Aid (Clinic)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 30 × 18 |
| **Entry Pad** | (15, 16) |
| **Services** | Mass debuffs (Pinned-type), bleed/burn cures (mid-price) |

### 5) Counterweight Station (Stabilizer Office)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 28 × 18 |
| **Entry Pad** | (14, 16) |
| **Function** | Story gating + tutorial explaining Mass gauge/anchor plates in plain language |

### 6) Dominion Ledger Booth (Pressure Room)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 20 × 14 |
| **Entry Pad** | (10, 12) |
| **Function** | Mostly tension + sidequest turn-ins (permits, bribes, falsification) |

---

## 6) Shops + Services (Inventory by Progress)

### Base (Pre-D6)

#### Rations & Rivets

| Item | Type |
|------|------|
| Potions, Antidotes | Consumables |
| Smoke Bombs | Escape aid |
| Rope Kits | Crafting mat |

#### Pressworks

| Item | Description |
|------|-------------|
| Basic knockback resist accessory | — |
| Belt greaves (if not found) | QoL |
| Crafting mats | — |

#### Forge

| Item | Description |
|------|-------------|
| Mid-heavy upgrades | — |
| Burn resist for core approach | — |
| "Mass Patch" (limited) | Consumable |

#### Clinic

| Service | Price |
|---------|-------|
| Status cures | Mid-price |
| Mass debuff cures | — |

---

### After D6 (Mass Relic Seated) — Major Upgrade

#### Forge Expansion

| Item | Description |
|------|-------------|
| Graveseal Mantle upgrade path | Mass resist armor |
| Anchor Step accessories | Field tech |
| Heavy-tier weapon tempering | — |

#### Pressworks Expansion

| Item | Description |
|------|-------------|
| Anchor Charm upgrades | — |
| "Countermass Pin" crafting | First knockback null |

#### Terminal Update

| Feature | Effect |
|---------|--------|
| Dragon's Graveyard route | Revealed on map |
| New gravity lanes | Show on overworld |

---

### Mid/Late Game

| Addition | Notes |
|----------|-------|
| Rare "gravity mats" | Needed for Time/Shadows prep (optional) |

---

## 7) NPC List (Placement + Function)

### Story-Critical

| NPC | Schedule | Location |
|-----|----------|----------|
| **Outpost Chief "Mara Kline"** (hard-nosed, pro-worker) | Day | Anchor Yard (52, 58) |
| | Night | Stabilizer Pumpworks (22, 28) |
| **Master Smith "Dorrin Vale"** (not friendly, but fair) | Day | Forge interior |
| | Night | Bunkhouse stew line |
| **Stabilizer Tech "Ione Sable"** | Day | Counterweight Station |
| | Night | Terminal area (26, 22) (listening to the hum) |

### Dominion Pressure NPC

| NPC | Schedule | Location | Notes |
|-----|----------|----------|-------|
| **Ledger Officer "Caspian Rook"** | Day | Ledger Booth interior | — |
| | Night | Near Railhead gate (88, 76) | Watching shipments |

### Utility

| NPC | Location | Function |
|-----|----------|----------|
| Innkeeper | The Heavy Blanket | Rest services |
| General Vendor | Rations & Rivets | Standard goods |
| Medic | Dustward Aid | Healing |
| Press Vendor | Plate & Pinion | Crafting bench |

### Flavor

| NPC | Description |
|-----|-------------|
| Exhausted miners | Dockside rest areas |
| Rail runners | Moving ore carts |
| Kid counting falling dust | District 1 |
| Old worker | "Gravity stories" (lore) |

---

## 8) Quest Hooks (Gravemark-Specific)

### Main Story

| Quest | Description |
|-------|-------------|
| **"Into the Quarry"** | Directs player to D6 entrance |
| **"Stabilizer Calibration"** | Optional prep quest reducing Mass gain in Submap 1/2 |

### Sidequests (Early)

| Quest | Objective | Reward |
|-------|-----------|--------|
| **Ore Shipment** | Deliver crate to Meridian Junction | Discount at general store |
| **Broken Rail Switch** | Repair minigame | Shortcut inside town opens |

### Sidequests (Post-D6)

| Quest | Objective | Reward |
|-------|-----------|--------|
| **Dragon's Graveyard Survey** | Unlock hidden area access | Breadcrumb quest |
| **Ledger Disruption** | Expose/fake records | Rewards + reduced Dominion hassle (visual change) |

---

## 9) Story-State Phases (Town Evolution)

### PHASE 0 — First Arrival (Work Town, Tense but Functioning)

| Aspect | State |
|--------|-------|
| Atmosphere | Crews active, minimal Dominion visibility |
| Visual | Full activity, cranes moving |

### PHASE 1 — Dominion Pressure Rising

| Aspect | State |
|--------|-------|
| Atmosphere | More permit signs, ledger officer harsher |
| Night | Patrol silhouettes |

### PHASE 2 — After D6 Clear

| Aspect | State |
|--------|-------|
| Atmosphere | Town feels steadier; fewer dust falls |
| Vibe | "We can breathe" |
| Unlocks | New crafts, gravity lane unlocks |

### PHASE 3 — Midgame Revisit

| Aspect | State |
|--------|-------|
| Atmosphere | Refugees/workers pass through; bunkhouse busier |

### PHASE 4 — Late Game

| Aspect | State |
|--------|-------|
| Night | Curfew vibe; more watchers |
| Forge | Remains open (player needs it) |

---

## 10) Navigation / Collision Notes

1. **Anchor Yard:** Keep open with 2–3 big lanes (avoid snagging on rails)
2. **Rails:** Use as "guides," but don't let them become annoying blockers
3. **Railhead Gate:** Visually scream "THIS GOES TO THE QUARRY"

---

## 11) Secrets & Collectibles

| Secret | Coordinates | Loot / Effect |
|--------|-------------|---------------|
| **Chest behind counterweight tower** | (12, 26) | "Anchor Charm" mat |
| **Hidden ledger note** | (8, 84) | Night only → unlocks sidequest branch |
| **Pet sniff spot** [post-tame] | (90, 66) | Rare "Gravemoss Resin" |
| **Terminal ping** [post-D6] | (26, 22) | Reveals Dragon's Graveyard route marker |

---

## Quick Reference Map Overview

```
                        NORTH
                          ↑
    ┌─────────────────────────────────────────────────────────┐
    │                                                           │
    │    DISTRICT 5: Stabilizer Pumpworks                       │
    │    (x 8–40, y 10–40)                                      │
    │    - Counterweight Station door (24,30)                   │
    │    - CHEST (12,26): Anchor Charm mat                      │
    │    - Terminal (26,22)                                     │
    │                                                           │
    │         ═══════════════════════════════════               │
    │                                                           │
    │    DISTRICT 2: Forge & Press Row      DISTRICT 1:         │
    │    (x 6–34, y 40–74)                  Anchor Yard         │
    │    - Forge door (18,62)               (x 34–74, y 34–68)  │
    │    - Pressworks door (28,70)          - SPAWN C (52,60)   │
    │    - Quest Board (54,66)                                  │
    │                                                           │
    │              ════════════════════════════════             │
    │                                                           │
    │    DISTRICT 4: Bunkhouse Strip         DISTRICT 3:        │
    │    (x 34–70, y 68–88)                Railhead Gate        │
    │    - Inn door (52,78)                (x 74–104, y 52–86)  │
    │    - Mount Hitch (70,74)             - D6 Exit (103,74)   │
    │                                      - SPAWN B (96,74)    │
    │                                                           │
    │    ════════════════════════════════════                   │
    │                                                           │
    │    DISTRICT 6: Dominion Ledger Booth                      │
    │    (x 0–18, y 62–88)                                      │
    │    - Ledger door (10,78)                                  │
    │    - LEDGER NOTE (8,84) [night only]                      │
    │    - SPAWN A (14,78)                                      │
    │                                                           │
    │    PET SNIFF (90,66)                                      │
    │                                                           │
    │    Overworld exits: (52,87) North, (0,44) West           │
    │    Dragon's Graveyard [post-D6]: (8,6)                    │
    │                                                           │
    └───────────────────────────────────────────────────────────┘
```

**Key Anchors Summary:**

| Feature | Coordinates |
|---------|-------------|
| **Spawn A** (overworld) | (14, 78) |
| **Spawn B** (D6 return) | (96, 74) |
| **Spawn C** (night) | (52, 60) |
| **Terminal** | (26, 22) |
| **D6 Exit** | (103, 74) |
| **Dragon's Graveyard** [post-D6] | (8, 6) |
| **Overworld North** | (52, 87) |
| **Overworld West** | (0, 44) |
| **Inn** | (52, 78) |
| **Forge** | (18, 62) |
| **Pressworks** | (28, 70) |
| **General Goods** | (66, 72) |
| **Clinic** | (62, 80) |
| **Stabilizer Office** | (24, 30) |
| **Ledger Booth** | (10, 78) |
| **Quest Board** | (54, 66) |
| **Mount Hitch** | (70, 74) |
| **Chest** | (12, 26) |
| **Ledger Note** [night] | (8, 84) |
| **Pet Sniff** | (90, 66) |
