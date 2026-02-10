# Chroma's Edge — Crown District (Inner Capital) Hub Map Sheet (v1)
## The Boss-Town — "The City is Watching Itself"

---

## 0) Technical Specs

| Parameter | Value |
|-----------|-------|
| **Sub-Map Name** | Crown District (Inner Capital Hub) |
| **Type** | Final capital hub — "boss-town" |
| **Role** | Connects Crown District Approach → Spire Conduit → D8 Void Nexus entry; plus key interiors |
| **Map Size** | 128 × 96 tiles (2048 × 1536 px) |
| **Encounters** | 0% in hub (safe, but hostile atmosphere) |
| **Time States** | Day / Night |
| **Night Atmosphere** | Stronger "wrong-sky" reflections + more phase shimmer + louder distant mechanisms |
| **Terminal** | YES (Crown Conduit Node) — late-game routing + "seam readings" |
| **Mounts** | Disabled (tight architecture + phase interference + narrative weight) |

---

## 1) Visual Identity (Art Direction)

| Element | Description |
|---------|-------------|
| **Materials** | Blackened marble, gilded trim now dull, glass-inlaid floors, iron quarantine ribs, sealed banners |
| **Palette** | Pale stone + soot black + muted gold + cold cyan chrono-glow + faint violet umbral shimmer near spire |

### Signature Props

| Prop | Description |
|------|-------------|
| **Crown Spire** | Towering above (always visible) |
| **Quarantine Rib Gates** | Like cage bars made of policy |
| **Mirror Tiles** | Reflect a sky that isn't there (night especially) |
| **Silent Fountains** | Water frozen mid-motion in "time-ice" pockets |

---

## 2) Layout (District Blocks)

### District 1 — Crown Gate Plaza (Entry Square)

| Property | Value |
|----------|-------|
| **Bounds** | x 0–48, y 40–86 |
| **Features** | Wide, readable; one big statue base, no statue |

### District 2 — Processional Walk (Main Spine)

| Property | Value |
|----------|-------|
| **Bounds** | x 48–96, y 36–66 |
| **Features** | Straight ceremonial avenue to spire complex |

### District 3 — Sealed Court (Safe Chamber Cluster)

| Property | Value |
|----------|-------|
| **Bounds** | x 54–90, y 66–96 |
| **Features** | Only "safe room" vibe: camp shelter + save + prep |

### District 4 — Spire Forecourt (Terminal + Gate Logic)

| Property | Value |
|----------|-------|
| **Bounds** | x 84–128, y 20–60 |
| **Features** | Conduit Node location; reality seams visible |

### District 5 — Palace Perimeter Steps (Optional Upper Loop)

| Property | Value |
|----------|-------|
| **Bounds** | x 36–100, y 0–36 |
| **Features** | Loop with time locks, lore plaques, elite-less "pressure" setpiece |

---

## 3) Entrances / Exits (Edge Triggers)

Local coords (0–127, 0–95)

### Arrival / Return

| Exit To | Coordinates | Notes |
|---------|-------------|-------|
| **From Crown District Approach** | (0, 52) | Main entry |
| **Back to Crown District Approach** | (0, 60) | Return |

### Forward Progression Exits

| Exit To | Coordinates | Gate Condition |
|---------|-------------|----------------|
| **Crown Spire Conduit** (D8 pre-entry) | (127, 44) | CROWN_ARCHIVE_KEY_ACQUIRED = TRUE |
| **Palace Interior** (optional/final act) | (88, 0) | Story flag OR Shadow seated / final act open |

---

## 4) Core Anchors & Coordinates

### Safe / Services Cluster (Sealed Court)

| Feature | Coordinates | Function |
|---------|-------------|----------|
| **SAVE CRYSTAL** ("Crown Beacon") | (72, 82) | Save point |
| **Rest Chamber Door** ("Candle Vault") | (72, 92) | Rest/stash |
| **Field Clinic Pod** ("Quiet Mend") | (86, 86) | Status cures |
| **Cache Vendor Pod** ("Last Supplies") | (58, 86) | Limited shop |
| **Contract / Intel Board** | (72, 76) | Quests/info |

### Terminal / Routing (Spire Forecourt)

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Crown Conduit Node** (Major Terminal) | (104, 44) | Pre-D8: "seam instability" + locked "Shadow channel"; Post-D8: Eclipse Routes / Unseen caches / seam shortcuts |

### Gate Logic Props

| Feature | Coordinates | Function |
|---------|-------------|----------|
| **Record Gate Console** | (112, 54) | Pairs with Archive Key |
| **Phase Pylon** (flavor) | (96, 34) | Optional puzzle |

### Landmark Props

| Feature | Coordinates | Description |
|---------|-------------|-------------|
| **Empty Regent Plinth** | (22, 62) | Statue base, no statue |
| **Mirror Tile Circle** | (64, 54) | Wrong-sky reflection |
| **Spire Shadow Seam** | (116, 38) | Visual tear in air |

---

## 5) Buildings / Structures (Exterior Door Tiles)

| Building | Door Coordinates | Interior |
|----------|------------------|----------|
| **Candle Vault** (Rest Chamber) | (72, 92) | 1) Candle Vault |
| **Quiet Mend** (Clinic Pod) | (86, 86) | 2) Quiet Mend |
| **Last Supplies** (Vendor Pod) | (58, 86) | 3) Last Supplies |
| **Crown Conduit Node Room** | (104, 46) | 4) Conduit Interior |
| **Record Gate Annex** | (112, 56) | 5) Gate Authorization |
| **Palace Antechamber** [optional] | (88, 2) | 6) Palace Staging |

---

## 6) Interiors (Required List)

### 1) Candle Vault (Rest Chamber)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 28 × 18 |
| **Function** | Rest/save flavor + stash chest + character beats |
| **Vibe** | Sealed stone, warm lamp, silence that feels curated |

### 2) Quiet Mend (Clinic Pod)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 24 × 16 |
| **Function** | Cures + prep |
| **Services** | Late-game status cures (Stasis/Pressure/Overheat/Umbral) |

### 3) Last Supplies (Vendor Pod)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 26 × 16 |
| **Function** | Limited shop (consumables + few high-tier mats) |

### 4) Crown Conduit Node Room (Terminal Interior)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 24 × 14 |
| **Function** | Routing UI + story cutscenes |
| **Optional** | "Ping" reveals Unseen caches post-D8 |

### 5) Record Gate Annex (Authorization Room)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 22 × 14 |
| **Function** | Key check + lore readout ("Authorized Records: Accepted") |
| **Puzzle** | OFFICIAL/ORIGINAL/REDACTED toggle for gate |

### 6) Palace Antechamber (Optional, Later)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 32 × 22 |
| **Function** | Staging room before palace dungeon / final act |
| **Combat** | No combat. Big mood. |

---

## 7) Services / Economy (Hub-Appropriate)

### Vendor Inventory (Last Supplies)

#### Base (On First Entry)

| Item | Type |
|------|------|
| High-tier potions/ethers | Consumables |
| Smoke bombs / escape items | — |
| Stasis Balm (limited) | Status resist |
| Pressure Patch (limited) | Status resist |
| Seal-Breaker Wax | Veil/Archive systems |
| Clockseal | Reduce phase/stasis hazards |

#### Post-D8 (Shadow Seated)

| Item | Type |
|------|------|
| Umbral Ward | Reduces Umbral Gauge gain |
| Phase Key (single-use) | Bypass locks |
| Rare mat bundle | Paradox Glass / Crown Alloy / Seal Wax |

### Clinic (Quiet Mend)

| Service | Description |
|---------|-------------|
| Full status cure list | — |
| "Panic/Confounded" cure | For Archive/Shadow mechanics |
| Optional "Prepare" buff | Small resist for next 10 battles |

---

## 8) NPCs (Minimal, Purposeful)

### Core

| NPC | Coordinates | Function |
|-----|-------------|----------|
| **Crown Warden** (Camp Lead) | (70, 84) / inside Candle Vault at night | Story anchor |
| **Tech/Timewright** cameo | (104, 44) at night | Terminal flavor |
| **Medic** | Inside Quiet Mend | Healing |
| **Vendor** | Inside Last Supplies | Shop |

### Non-Human / "Presence"

| NPC | Coordinates | Description |
|-----|-------------|-------------|
| **Silent Sentinel** | (24, 62) | Turns head slowly near empty plinth; no combat, just dread |

---

## 9) Quests / Beats (Hub Heavy Lifting)

| Quest | Description |
|-------|-------------|
| **"Authorize the Conduit"** | Insert Crown Archive Key at Record Gate Console |
| **"Seal the Court"** | Activate Crown Beacon (save unlock feels earned) |
| **"The Missing Regent"** | Interact with empty plinth + mirror circle (sets up D8 tone) |
| **"Purge the Seal"** | Remove quarantine stamp stacks (changes props + vendor discount) |

---

## 10) Gating & Flags

### Entering Crown District

| Requirement | Notes |
|-------------|-------|
| Usually gated | By Crown Archive Key + story (reached via Approach route) |

### Entering D8 (Void Nexus)

| Requirement | Notes |
|-------------|-------|
| CROWN_ARCHIVE_KEY_ACQUIRED | TRUE |
| All Seated Foundations | Recommended: Tide, Mass, Time (plus earlier) |
| Location | Record Gate Console / Conduit Node |

### Completion Flags

| Flag | Condition |
|------|-----------|
| **CROWN_DISTRICT_DISCOVERED** | TRUE on first entry |
| **CROWN_BEACON_ACTIVATED** | TRUE when save crystal used |
| **CONDUIT_AUTHORIZED** | TRUE after key authorization |
| **VOID_NEXUS_GATE_OPEN** | TRUE when D8 access granted |

---

## 11) Secrets / Collectibles

| Secret | Coordinates | Loot / Effect |
|--------|-------------|---------------|
| **Night-only Mirror Ping** | (64, 54) | Terminal later reveals 1 Unseen cache marker |
| **Chest behind sealed banner** | (46, 18) | Crown Alloy Plate + Paradox Glass |
| **Lore plaque** (upper loop) | (78, 10) | "They didn't conquer the capital. They corrected it." |
| **Pet sniff spot** | (92, 70) | "Umbral Resin" (rare craft mat, post-D8 better drops) |

---

## Quick Reference Map Overview

```
                        NORTH
                          ↑
    ┌───────────────────────────────────────────────────────────┐
    │                                                           │
    │    DISTRICT 5: Palace Perimeter Steps                     │
    │    (x 36–100, y 0–36)                                     │
    │    - Time locks + lore plaques                            │
    │    - Lore plaque (78,10)                                  │
    │    - CHEST (46,18)                                        │
    │    - Palace Antechamber door (88,2) [locked]              │
    │                                                           │
    │    ═══════════════════════════════════════════            │
    │                                                           │
    │    DISTRICT 4: Spire Forecourt         DISTRICT 2:        │
    │    (x 84–128, y 20–60)               Processional Walk    │
    │    - Conduit Node (104,44)           (x 48–96, y 36–66)   │
    │    - Conduit door (104,46)           - Main avenue        │
    │    - Record Gate Console (112,54)    - Mirror Circle      │
    │    - Gate Annex door (112,56)          (64,54)            │
    │    - Phase Pylon (96,34)                                  │
    │    - Spire Shadow Seam (116,38)      DISTRICT 1:          │
    │                                        Crown Gate Plaza   │
    │    ═══════════════════════════       (x 0–48, y 40–86)    │
    │                      │               - Empty Plinth       │
    │    ══════════════════╪════════════════   (22,62)          │
    │                      │               - Silent Sentinel    │
    │    DISTRICT 3: Sealed Court            (24,62)            │
    │    (x 54–90, y 66–96)                - Entry (0,52)       │
    │                                        Return (0,60)      │
    │    SAVE CRYSTAL (72,82)                                   │
    │         │                                                 │
    │    Candle Vault (72,92)    Quiet Mend (86,86)             │
    │    Contract Board (72,76)  Last Supplies (58,86)          │
    │                                                           │
    │    Warden (70,84)        PET SNIFF (92,70)                │
    │                                                           │
    │    Exits:                                                   │
    │    - D8 Void Nexus → (127,44) [Key required]              │
    │    - Palace Interior ↑ (88,0) [Story locked]              │
    │                                                           │
    └───────────────────────────────────────────────────────────┘
```

**Key Anchors Summary:**

| Feature | Coordinates |
|---------|-------------|
| **Entry from Approach** | (0, 52) |
| **Return to Approach** | (0, 60) |
| **Empty Regent Plinth** | (22, 62) |
| **Silent Sentinel** | (24, 62) |
| **Processional Walk** | x 48–96, y 36–66 |
| **Mirror Tile Circle** | (64, 54) |
| **Crown Beacon (Save)** | (72, 82) |
| **Contract Board** | (72, 76) |
| **Candle Vault** | (72, 92) |
| **Last Supplies** | (58, 86) |
| **Quiet Mend** | (86, 86) |
| **Crown Conduit Node** | (104, 44) |
| **Conduit Room Door** | (104, 46) |
| **Record Gate Console** | (112, 54) |
| **Gate Annex Door** | (112, 56) |
| **Phase Pylon** | (96, 34) |
| **Spire Shadow Seam** | (116, 38) |
| **Lore Plaque** | (78, 10) |
| **Chest** | (46, 18) |
| **Pet Sniff** | (92, 70) |
| **D8 Void Nexus Exit** | (127, 44) |
| **Palace Interior Exit** | (88, 0) |
