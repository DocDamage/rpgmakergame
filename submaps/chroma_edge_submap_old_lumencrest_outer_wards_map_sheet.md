# Chroma's Edge — Old Lumencrest: Outer Wards Map Sheet (v1)
## Ruined Capital Hub — "A Dead City Trying to Look Normal"

---

## 0) Technical Specs

| Parameter | Value |
|-----------|-------|
| **Sub-Map Name** | Outer Wards (Old Lumencrest Hub) |
| **Type** | Ruined-capital hub + limited services + route branching |
| **Map Size** | 144 × 104 tiles (2304 × 1664 px) |
| **Encounters** | 0% inside safe perimeter |
| **Encounter Pockets** | Beyond hard gates (routes load separate maps) |
| **Time States** | Day / Night |
| **Night Atmosphere** | Denser fog + "frame-skip" VFX near certain landmarks |
| **Town Terminal** | YES (Damaged Relay Node) — limited early, expands post-D7 |
| **Mounts** | Allowed; restricted in core camp plaza + tight rubble lanes; allowed on perimeter road + boulevard edges |

---

## 1) Visual Identity (Art Direction)

| Element | Description |
|---------|-------------|
| **Materials** | Cracked marble, broken tram rails, toppled statues, quarantine fencing, tarp camps |
| **Palette** | Pale stone + soot gray + muted gold trim + cold cyan chrono-glow |

### Signature Props

| Prop | Description |
|------|-------------|
| **Shattered Tram Loop** | Rails + half-buried cars |
| **Quarantine Wall** | Paper seals + iron plates |
| **Mirror Plaza tiles** | Reflect "wrong sky" at night |
| **Crown Spire silhouette** | Always visible in distance (north-east skyline) |

---

## 2) Layout (District Blocks)

### District 1 — Scavenger Relay Camp (Safe Hub)

| Property | Value |
|----------|-------|
| **Bounds** | x 56–92, y 52–86 |
| **Features** | Vendor, save, clinic, contracts board |

### District 2 — Mirror Plaza (Landmark Square)

| Property | Value |
|----------|-------|
| **Bounds** | x 44–104, y 34–56 |
| **Features** | Open, elegant ruin; subtle time shimmer |

### District 3 — Shattered Market Rows

| Property | Value |
|----------|-------|
| **Bounds** | x 96–144, y 56–96 |
| **Features** | Collapsed stalls + salvage piles + NPC scav routes |

### District 4 — Tram Wreckline

| Property | Value |
|----------|-------|
| **Bounds** | x 24–74, y 8–34 |
| **Features** | Rails + car shells; leads toward Archive access |

### District 5 — Quarantine Wall & Checkpoint

| Property | Value |
|----------|-------|
| **Bounds** | x 0–26, y 30–86 |
| **Features** | Sealed gates, "compliance" signage, Dominion residue |

### District 6 — Perimeter Ring Road (Mount-friendly)

| Property | Value |
|----------|-------|
| **Bounds** | x 10–134, y 92–104 |
| **Features** | Wide lane that loops to exits without snagging on props |

---

## 3) Entrances / Exits (Edge Triggers)

Local coords (0–143, 0–103)

### Arrival / Return

| Exit To | Coordinates | Notes |
|---------|-------------|-------|
| **From Crownfall Viaduct** (arrival) | (8, 96) | Southwest ring road |
| **To Crownfall Viaduct** (return) | (0, 96) | West edge |

### Route Exits (Load Separate Maps)

| Exit To | Coordinates | Gate Condition |
|---------|-------------|----------------|
| **Grand Boulevard Route** | (143, 70) | East edge — always available |
| **Archive District** | (60, 0) | North edge — requires Time access (D7 cleared or Phase Key) |
| **Underworks** (sewers/transit) | (118, 102) | South-east manhole — opens after Tide seated OR "Seal-Cutter" from camp |
| **Crown District Approach** | (143, 18) | North-east barricade — late-game (story + Mass rubble clearance) |

---

## 4) Core Anchors & Coordinates

### Safe Hub Anchors

| Feature | Coordinates | Function |
|---------|-------------|----------|
| **SAVE CRYSTAL** ("Camp Beacon") | (74, 74) | Save point |
| **Camp Vendor Tent** | door (66, 78) | Main shop — Scav-Merchant "Kett" |
| **Field Clinic Tent** | door (80, 78) | Status cures |
| **Camp Sleep Cot / Rest Spot** | door (74, 84) | Rest/character scenes |
| **Contract Board** | (74, 70) | Quests/contracts |

### Terminal / Routing

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Damaged Lattice Relay Node** | (70, 60) | Pre-D7: lore + warnings; Post-D7: phase markers, route advisories, hidden pings |

### Landmark Props

| Feature | Coordinates | Description |
|---------|-------------|-------------|
| **Mirror Plaza Center Marker** | (74, 46) | Reflective tiles showing "wrong sky" at night |
| **Tram Car Husk** (setpiece) | (46, 22) | Half-buried rail car |
| **Quarantine Wall Main Seal Gate** | (18, 60) | Non-passable; flavor + story beats |

---

## 5) Buildings (Exterior Door Tiles)

| Building | Door Coordinates | Interior |
|----------|------------------|----------|
| **Scavenger Relay Tent** ("The Relay Camp") | (66, 78) | 1) Relay Camp Tent |
| **Field Clinic** ("Patchhouse") | (80, 78) | 2) Patchhouse Clinic |
| **Safehouse Bunk** ("Candlecell Shelter") | (74, 84) | 3) Candlecell Shelter |
| **Relay Bunker** (Terminal Access Room) | (70, 62) | 4) Relay Bunker |
| **Salvage Workshop** ("Bolt & Bind") | (92, 80) | 5) Bolt & Bind Workshop |
| **Quarantine Office Ruin** (optional) | (16, 72) | 6) Quarantine Office — opens PHASE 1+ or via quest |

---

## 6) Interior List (Required)

### 1) Relay Camp Tent

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 34 × 22 |
| **Services** | Vendor + rumors + contracts turn-in |

### 2) Patchhouse Clinic

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 30 × 18 |
| **Services** | Cures + status prep (Pressure/Stasis/Overheat) |

### 3) Candlecell Shelter (Rest)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 28 × 18 |
| **Services** | Rest/save flavor, character scenes, optional stash chest |

### 4) Relay Bunker (Terminal Room)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 24 × 16 |
| **Services** | Terminal interaction + story cutscenes + "route ping" unlocks |

### 5) Bolt & Bind Workshop

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 30 × 18 |
| **Services** | Basic upgrades, mat conversion, "seal-cutter" type items |

### 6) Quarantine Office Ruin (Optional)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 22 × 16 |
| **Services** | Mostly lore + one quest objective + one locked locker |

---

## 7) Camp Vendor (Inventory by Progress)

**Vendor:** Scav-Merchant "Kett"

### Base (First Arrival)

| Item | Description |
|------|-------------|
| Potions / Ethers / Antidotes | Standard consumables |
| Smoke Bombs | Escape aid |
| Rope Kit | Crafting mat |
| Stasis Balm (limited) | Stasis resist |
| Pressure Patch (limited) | Pressure resist |
| "Rubble Wedge" | Minor utility consumable |

### After Tide Seated (Post-D5)

| Item | Description |
|------|-------------|
| Kelp Filters | Oxygen prep |
| Better Pressure Patches | — |
| Brine mats exchange | — |

### After Mass Seated (Post-D6)

| Item | Description |
|------|-------------|
| Knockback resist charm | — |
| Anchor plating mats | — |
| "Loadbelt Greaves" craft token | If missed in D6 |

### After Time Seated (Post-D7)

| Item | Description |
|------|-------------|
| Phase Key (single-use) | Bypass time locks |
| Chrono Band upgrade mats | — |
| "Clockseal" consumable | Reduces stasis/phase hazards for X battles |

---

## 8) NPCs (Placement + Function)

### Core

| NPC | Coordinates | Function |
|-----|-------------|----------|
| **Camp Lead "Rook-9"** (or human leader) | (76, 76) | Story + permissions |
| **Kett** (vendor) | Inside Relay Camp | Shop |
| **Medic** | Inside Patchhouse | Healing |
| **Galen Quill** cameo (optional) | (70, 60) at night | Timewright flavor |

### Flavor

| NPC | Location | Description |
|-----|----------|-------------|
| 2 scavengers | Market Rows | Moving salvage |
| "Time-listener" | Mirror Plaza at night | Hears echoes |
| Refugee family | Ring Road | Humanizes the ruin |

---

## 9) Quests (Hub-Appropriate)

### Main Utility

| Quest | Description |
|-------|-------------|
| **"Set the Camp Beacon"** | Activates save + makes hub feel earned |

### Route Unlock

| Quest | Description |
|-------|-------------|
| **"Find the Relay Fuse"** | Opens full terminal functions |

### District Teases

| Quest | Description | Unlock |
|-------|-------------|--------|
| **"Ledger Page in the Tram"** | Points to Archive District | — |
| **"The Smell of Salt Below"** | Unlocks sewer access after Tide | Underworks |

### Dominion Echo

| Quest | Description | Effect |
|-------|-------------|--------|
| **"Quarantine Seal"** | Optional moral quest | Changes signage + NPC tone |

---

## 10) Navigation / Collision Notes

1. **Mirror Plaza → Camp:** Keep as straight, readable line
2. **Rubble placement:** In edges, not main travel lanes
3. **Ring Road:** Allow fast traversal between exits with minimal snag

---

## 11) Secrets & Collectibles

| Secret | Coordinates | Loot / Effect |
|--------|-------------|---------------|
| **Chest** (tram car interior) | (42, 18) | Crown Sigil Fragment (key item) |
| **Night-only "wrong sky" ping** | (74, 46) | Reveals hidden marker on terminal later |
| **Pet sniff spot** [post-tame] | (104, 92) | Rare "Crown Resin" mat |
| **Locked locker** (Quarantine Office) | (16, 72) interior | "Compliance Ledger" (quest/lore) |

---

## Quick Reference Map Overview

```
                        NORTH
                          ↑
    ┌───────────────────────────────────────────────────────────┐
    │                                                           │
    │    DISTRICT 4: Tram Wreckline                             │
    │    (x 24–74, y 8–34)                                      │
    │    - Tram Car Husk (46,22)                                │
    │    - CHEST (42,18): Crown Sigil Fragment                  │
    │    - Exit to Archive District (60,0) [Time locked]        │
    │                                                           │
    │    ═══════════════════════════════════════════            │
    │                                                           │
    │    DISTRICT 2: Mirror Plaza            DISTRICT 5:        │
    │    (x 44–104, y 34–56)               Quarantine Wall      │
    │    - Center Marker (74,46)           (x 0–26, y 30–86)    │
    │    - "Wrong sky" [night]             - Seal Gate (18,60)  │
    │    - Time-listener NPC                 (flavor only)      │
    │                                        - Quarantine       │
    │    ═════════════════════════════════   Office (16,72)     │
    │                      │                                    │
    │    ══════════════════╪══════════════════════              │
    │                      │                                    │
    │    DISTRICT 1: Scavenger Relay Camp                       │
    │    (x 56–92, y 52–86)                                     │
    │                                                           │
    │    Save Crystal (74,74)      Terminal (70,60)             │
    │         │                         │                       │
    │    Vendor (66,78)          Relay Bunker (70,62)           │
    │    Clinic (80,78)               │                         │
    │    Rest Spot (74,84)       Camp Lead (76,76)              │
    │         │                         │                       │
    │    Contract Board (74,70)                                 │
    │                                                           │
    │    Bolt & Bind Workshop (92,80)                           │
    │                                                           │
    │    ═══════════════════════════════════════════            │
    │                                                           │
    │    DISTRICT 3: Shattered Market Rows    DISTRICT 6:       │
    │    (x 96–144, y 56–96)                Perimeter Ring Road │
    │    - Salvage piles                    (x 10–134, y 92–104)│
    │    - 2 scavenger NPCs                 - Mount-friendly    │
    │                                       - PET SNIFF (104,92)│
    │                                                           │
    │    Exits:                                                   │
    │    - Crownfall Viaduct (0,96) ← Arrival/Return            │
    │    - Grand Boulevard (143,70) → East                      │
    │    - Archive District (60,0) → North [Time locked]        │
    │    - Underworks (118,102) → South [Tide/Seal-Cutter]      │
    │    - Crown District (143,18) → North-East [Late]          │
    │                                                           │
    │    Crown Spire visible in north-east skyline              │
    │                                                           │
    └───────────────────────────────────────────────────────────┘
```

**Key Anchors Summary:**

| Feature | Coordinates |
|---------|-------------|
| **Crownfall Viaduct Exit** | (0, 96) |
| **Arrival from Viaduct** | (8, 96) |
| **Save Crystal** | (74, 74) |
| **Camp Vendor** | (66, 78) |
| **Clinic** | (80, 78) |
| **Rest Spot** | (74, 84) |
| **Contract Board** | (74, 70) |
| **Terminal** | (70, 60) |
| **Relay Bunker** | (70, 62) |
| **Camp Lead** | (76, 76) |
| **Mirror Plaza Center** | (74, 46) |
| **Tram Car Husk** | (46, 22) |
| **Tram Chest** | (42, 18) |
| **Quarantine Gate** | (18, 60) |
| **Quarantine Office** | (16, 72) |
| **Bolt & Bind Workshop** | (92, 80) |
| **Grand Boulevard Exit** | (143, 70) |
| **Archive Exit** [Time] | (60, 0) |
| **Underworks Exit** [Tide] | (118, 102) |
| **Crown District Exit** [Late] | (143, 18) |
| **Pet Sniff** | (104, 92) |
