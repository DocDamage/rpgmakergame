# Chroma's Edge — Eclipse Confluence Overworld Hub Map Sheet (v1)
## The World's Seams Tie Themselves Into a Knot — "Not a Town. Not a Dungeon. A Junction That Feels Like It's Thinking."

---

## 0) Technical Specs

| Parameter | Value |
|-----------|-------|
| **Map Name** | Eclipse Confluence |
| **Type** | Post-D8 endgame overworld hub node |
| **Role** | Connects 3 Unseen Vaults + offers seam routing + hosts safe chamber + gates Final Route |
| **Map Size** | 128 × 96 tiles (2048 × 1536 px) |
| **Encounters** | 0% inside Core Ring; ON in outer rim lanes (light) |
| **Time States** | Day / Night |
| **Night Atmosphere** | Stronger "eclipse pulse," higher elite chance in rim |
| **Mounts** | Disabled (seams destabilize mounts) |
| **Terminal** | YES (Seam Router Node) — primary postgame routing UI |
| **Save** | YES (Stillpoint Anchor) |

---

## 1) Unlock / Discovery

| Parameter | Value |
|-----------|-------|
| **Unlock Condition** | `RELIC_SHADOW_SEATED = TRUE` |
| **Discovery Rule** | First time player Shadowwalks through any seam, Confluence "pings" and becomes selectable node |

---

## 2) Visual Identity (Art Direction)

| Element | Description |
|---------|-------------|
| **Terrain** | Black glass sand, fractured stone plates, "stitch lines" of glowing seam energy |
| **Palette** | Matte black + deep violet + cold cyan highlights + thin white "lumen" rings |

### Signature Props

| Prop | Description |
|------|-------------|
| **Seam Knot** | Center sculpture/phenomenon |
| **Eclipse Rings** | Concentric circles in ground, rotating slowly |
| **Unseen pylons** | 3 vault gate pylons + 1 final gate pylon |
| **Floating debris** | Slow orbit, subtle |

---

## 3) Layout Blocks (Districts)

### District 1 — Core Ring (Safe Hub)

| Property | Value |
|----------|-------|
| **Bounds** | x 40–88, y 34–82 |
| **Features** | Save, terminal, prep, NPCs (if any), clear navigation |

### District 2 — Seam Rim (Encounter Belt)

| Property | Value |
|----------|-------|
| **Bounds** | x 18–110, y 12–92 |
| **Features** | Loop path around core; contains 3 vault gates + 1 optional elite encounter pocket |

### District 3 — Gate Courts (4 Spokes)

| Property | Value |
|----------|-------|
| **Layout** | North/East/South/West spokes from core to rim gates |
| **Feature** | Distinctive props so player never gets lost |

---

## 4) Entrances / Exits (Edge Triggers)

Local coords (0–127, 0–95)

### Seam Gate Entrances (Arrivals)

| From | Coordinates | Notes |
|------|-------------|-------|
| **Chronowake Seam** | (64, 95) | South entry |
| **Gravemark Seam** | (0, 52) | West entry |
| **Rimehold Seam** | (64, 0) | North entry |
| **Brinegate Seam** | (127, 52) | East entry |

*Note: Gates activate as player discovers them.*

### Exits (Vaults + Final Gate)

| To | Coordinates | Location |
|----|-------------|----------|
| **Vault of Quiet Glass** (Time) | (64, 6) | North gate court |
| **Vault of Boneweight** (Mass) | (10, 52) | West gate court |
| **Vault of Deep Salt** (Tide) | (118, 52) | East gate court |
| **Final Eclipse Gate** (endgame) | (64, 90) | South gate court; optional gating |

---

## 5) Key Anchors & Coordinates

### Core Ring Anchors (Safe)

| Feature | Coordinates | Function |
|---------|-------------|----------|
| **SAVE / Stillpoint Anchor** | (64, 62) | Save point |
| **Seam Router Terminal** | (64, 50) | Primary routing UI |
| **Eclipse Well** (rest/refill) | (52, 66) | Cleanses Umbral effects, refills Umbral Charges |
| **Null Cache** (vendor) | (76, 66) | Limited items |
| **Seam Log** (intel board) | (64, 72) | Vault completion + elite hunt hints |

### Landmark

| Feature | Coordinates | Description |
|---------|-------------|-------------|
| **Seam Knot** (centerpiece) | (64, 58) | Non-interactive VFX object or lore interact |

### Rim Utilities

| Feature | Coordinates | Function |
|---------|-------------|----------|
| **Lumen Anchor Pads** | (64, 26), (38, 52), (90, 52), (64, 84) | "Breather tiles" for rim encounters |

---

## 6) Structures / "Buildings" (Exterior Door Tiles)

These are "constructs" functioning like doors:

| Structure | Door Coordinates | Interior |
|-----------|------------------|----------|
| **Seam Router Node Room** | (64, 48) | 1) Seam Router Interior |
| **Stillpoint Chamber** | (64, 64) | 2) Stillpoint Interior |
| **Null Cache Pod** | (76, 68) | 3) Null Cache Interior |
| **Gate: Quiet Glass** | (64, 10) | — |
| **Gate: Boneweight** | (14, 52) | — |
| **Gate: Deep Salt** | (114, 52) | — |
| **Final Eclipse Gate** | (64, 88) | — |

---

## 7) Interiors (Required List)

### 1) Stillpoint Chamber (Save + Cleanse)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 24 × 16 |
| **Function** | Save + full cleanse + optional rest |
| **Vibe** | Absolute quiet, soft white ring light |

### 2) Seam Router Node Room (Terminal UI)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 26 × 16 |
| **Function** | Seam routing UI + vault tracking + eclipse cycle state |
| **Post-Clear** | Allows "fast travel between discovered seams" |

### 3) Null Cache Pod (Vendor)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 22 × 14 |
| **Function** | Limited supplies + rare mat exchange |

---

## 8) Vendor ("Null Cache") Inventory

### Base (First Arrival)

| Item | Type |
|------|------|
| High-tier potions/ethers | Consumables |
| Clockseal | Phase/stasis hazard reduction |
| Seal-Breaker Wax | Veil clears |
| Umbral Ward (minor) | Reduces Umbral Gauge gain |
| 1 rotating mat bundle | Paradox Glass / Crown Alloy / Seal Wax |

### After Each Vault Cleared

| Vault Cleared | Unlocks |
|---------------|---------|
| **Quiet Glass** | Chrono Band upgrade mat / Time resist accessory |
| **Boneweight** | Knockback immunity craft token / Mass plating mat |
| **Deep Salt** | Kelp Filter+ bundle / Pressure resist accessory |

---

## 9) Rim Encounters (Optional)

### Core Ring

| Property | Value |
|----------|-------|
| **Encounters** | 0% always |

### Seam Rim

| Property | Value |
|----------|-------|
| **Encounter Rate** | Low |
| **Level** | Lv 90–99 variants |
| **Enemies** | Rift Wisps, Umbral Skulkers, Null Sentinels |

### Rim Elite Pocket (Night-Only)

| Property | Value |
|----------|-------|
| **Spawn Zone** | (96, 18) or (30, 18) |
| **Elite** | Seam Warden Prime (once per eclipse cycle) |
| **Reward** | Amplifier mats / rare crafting core |

---

## 10) Gating Logic

### Vault Gates

| Requirement | Description |
|-------------|-------------|
| **Base** | `RELIC_SHADOW_SEATED = TRUE` |
| **Optional Foundation Check** | Corresponding foundation seated to enter: |
| Quiet Glass | `RELIC_TIME_SEATED` |
| Boneweight | `RELIC_MASS_SEATED` |
| Deep Salt | `RELIC_TIDE_SEATED` |

### Final Eclipse Gate (Endgame Route)

| Option | Description |
|--------|-------------|
| **Option A (Completion Gate)** | Opens when all 3 vaults cleared: `VAULT_QUIET_GLASS_CLEARED`, `VAULT_BONEWEIGHT_CLEARED`, `VAULT_DEEP_SALT_CLEARED` |
| **Option B (Story Gate)** | Opens immediately post-D8, becomes easier/shorter if vaults cleared |

---

## 11) Eclipse Cycle Integration

| Feature | Description |
|---------|-------------|
| **Visual Indicator** | Ring light around Seam Knot changes intensity |
| **States** | Clear / Veil / Eclipse |
| **Terminal Display** | Shows current state and effects (elite chance, cache spawns) |

---

## 12) Secrets / Collectibles

| Secret | Coordinates | Conditions | Reward |
|--------|-------------|------------|--------|
| **Unseen Cache Node** | (22, 84) | Night only | Rare mat bundle |
| **Lore Interact** (Seam Knot) | (64, 58) | — | Unlocks "Seam Log" entries |
| **Pet Sniff Spot** | (106, 84) | — | "Eclipse Resin" (rare craft mat) |

---

## 13) Flags / Tracking

| Flag | Condition |
|------|-----------|
| `ECLIPSE_CONFLUENCE_DISCOVERED` | TRUE on first arrival |
| `ECLIPSE_CONFLUENCE_BEACON_ACTIVE` | TRUE when save activated |
| `SEAM_ROUTER_UNLOCKED` | TRUE when terminal used |
| `VAULT_QUIET_GLASS_CLEARED` | TRUE after vault |
| `VAULT_BONEWEIGHT_CLEARED` | TRUE after vault |
| `VAULT_DEEP_SALT_CLEARED` | TRUE after vault |
| `FINAL_ECLIPSE_GATE_OPEN` | TRUE when endgame route opens |

---

## Quick Reference Map Overview

```
                        NORTH
                          ↑
    ┌───────────────────────────────────────────────────────────┐
    │                                                           │
    │    NORTH SPOKE                                            │
    │    - Seam arrival (64,0) [Rimehold]                       │
    │    - Lumen Anchor (64,26)                                 │
    │    - Gate: Vault of Quiet Glass (64,10) → (64,6)          │
    │         [Time vault entrance]                             │
    │                                                           │
    │    ═══════════════════════════════════════════            │
    │                                                           │
    │    DISTRICT 1: CORE RING (Safe)                           │
    │    (x 40–88, y 34–82)                                     │
    │                                                           │
    │         NORTH                                             │
    │           │                                               │
    │    WEST ──┼── EAST                                        │
    │           │                                               │
    │         SOUTH                                             │
    │                                                           │
    │    Seam Knot (64,58) ═══════ Centerpiece                  │
    │         │                                                 │
    │    Terminal (64,50)    SAVE (64,62)                       │
    │    Router Room         Stillpoint Chamber                 │
    │         │                                                 │
    │    Eclipse Well (52,66)   Null Cache (76,66)              │
    │         │                       │                         │
    │    Seam Log (64,72)       Vendor Pod                      │
    │                                                           │
    │    ═══════════════════════════════════════════            │
    │                                                           │
    │    DISTRICT 2: SEAM RIM (Encounter Belt)                  │
    │    (x 18–110, y 12–92)                                    │
    │    - Loop path around core                                │
    │    - Lumen Anchors at cardinals                           │
    │    - Elite pocket: (96,18) or (30,18) [night]             │
    │    - Unseen Cache: (22,84) [night]                        │
    │    - Pet Sniff: (106,84)                                  │
    │                                                           │
    │    ═══════════════════════════════════════════            │
    │                                                           │
    │    WEST SPOKE              EAST SPOKE                     │
    │    - Arrival (0,52)        - Arrival (127,52)             │
    │    [Gravemark]             [Brinegate]                    │
    │    - Anchor (38,52)        - Anchor (90,52)               │
    │    - Gate: Boneweight      - Gate: Deep Salt              │
    │      (14,52) → (10,52)       (114,52) → (118,52)          │
    │      [Mass vault]            [Tide vault]                 │
    │                                                           │
    │    ═══════════════════════════════════════════            │
    │                                                           │
    │    SOUTH SPOKE                                            │
    │    - Arrival (64,95) [Chronowake]                         │
    │    - Lumen Anchor (64,84)                                 │
    │    - Gate: Final Eclipse Gate (64,88) → (64,90)           │
    │         [Endgame route / finale access]                   │
    │                                                           │
    │    Seam Knot Ring Light:                                  │
    │    - Dim (Clear) / Pulse (Veil) / Bright (Eclipse)        │
    │                                                           │
    └───────────────────────────────────────────────────────────┘
```

**Key Anchors Summary:**

| Feature | Coordinates |
|---------|-------------|
| **Seam Knot** | (64, 58) |
| **Terminal** | (64, 50) |
| **Save Anchor** | (64, 62) |
| **Eclipse Well** | (52, 66) |
| **Null Cache** | (76, 66) |
| **Seam Log** | (64, 72) |
| **Rimehold Arrival** | (64, 0) |
| **Quiet Glass Gate** | (64, 10) → (64, 6) |
| **Gravemark Arrival** | (0, 52) |
| **Boneweight Gate** | (14, 52) → (10, 52) |
| **Brinegate Arrival** | (127, 52) |
| **Deep Salt Gate** | (114, 52) → (118, 52) |
| **Chronowake Arrival** | (64, 95) |
| **Final Eclipse Gate** | (64, 88) → (64, 90) |
| **Lumen Anchors** | (64, 26), (38, 52), (90, 52), (64, 84) |
| **Elite Pocket** [night] | (96, 18) or (30, 18) |
| **Unseen Cache** [night] | (22, 84) |
| **Pet Sniff** | (106, 84) |
