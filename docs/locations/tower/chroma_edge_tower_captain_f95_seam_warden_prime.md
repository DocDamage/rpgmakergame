# Chroma's Edge — Tower Captain Arena: Floor 95 (v1)
## Seam Warden Prime (Eclipse/Shadow-Time Composite) — "Reality Clamp"

---

## 0) Technical Specs

| Parameter | Value |
|-----------|-------|
| **Captain** | Seam Warden Prime |
| **Identity** | Eclipse/Shadow-Time Composite — "Reality Clamp" |
| **Tower Floor** | 95 (optional Captain Door room) |
| **Recommended Level** | 225–240 |
| **Fight Identity** | Precision check: dispel pressure + phase/veil hazards + pin window via consoles. Hard, but never cheap |
| **Core Threats** | Seam Rifts, buff strip cadence, telegraphed "collapse" cast |
| **Arena Size** | 56 × 56 tiles (Template E: Arena + Prep Hall) |
| **Type** | Optional Captain Challenge arena (single fight) |
| **Encounters** | OFF (boss only) |
| **Mounts** | Disabled |
| **Retry behavior** | Standard Tower (resume at last save floor) |

---

## A) Access / Door Logic (on Floor 95)

| Property | Description |
|----------|-------------|
| **Door mark** | Black-white seal + split-ring icon |
| **Prompt** | "ENTER CAPTAIN CHALLENGE — SEAM WARDEN PRIME" |
| **Gating** | Once entered, cannot leave until win/lose |

---

## B) Layout Overview

### 1) Prep Hall (Safe)

| Property | Value |
|----------|-------|
| **Bounds** | x 0–56, y 44–56 |
| **Features** | Ready tile + optional one-time supply crate (endgame consumable) |

### 2) Arena Bowl (Seam Court)

| Property | Value |
|----------|-------|
| **Bounds** | x 6–50, y 6–44 |
| **Features** | 4 cover pylons + 2 Stabilizer Consoles + 2 Null Fonts + 1 Core Clamp Plate (risk-reward) |

### 3) Reward Pad

| Property | Value |
|----------|-------|
| **Chest** | Spawns above prep hall after victory |

---

## C) Anchors & Coordinates (Local 0–55, 0–55)

### Entry / Lock

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Entry spawn** | (28, 52) | — |
| **Arena threshold lock line** | y = 44 | Crossing to y≤43 locks doors |
| **Lock trigger** | (28, 43) | — |

### Boss Spawn

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Seam Warden Prime spawn** | (28, 22) | — |

### Cover Pylons (3×3 Collision; Blocks Line Attacks)

| Pylon | Coordinates |
|-------|-------------|
| **NW** | (16, 16) |
| **NE** | (40, 16) |
| **SW** | (16, 32) |
| **SE** | (40, 32) |

### Stabilizer Consoles (Primary Counterplay, 2)

| Console | Coordinates |
|---------|-------------|
| **Console L** | (10, 26) |
| **Console R** | (46, 26) |

### Null Fonts (Limited Relief, 2)

| Font | Coordinates |
|------|-------------|
| **Font L** | (20, 38) |
| **Font R** | (36, 38) |

### Core Clamp Plate (Optional High-Skill)

| Feature | Coordinates |
|---------|-------------|
| **Clamp Plate** | (28, 28) |

### Reward Spawn

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Captain chest** | (28, 46) | After victory |
| **Return gate** | (28, 54) | After victory |

---

## D) Core Systems

### 1) Seam Integrity (Mini-Meter)

| Cracks | Effect |
|--------|--------|
| **0–2** | Normal |
| **3** | Boss gains minor speed |
| **6** | Triggers **SEAM COLLAPSE** on next turn |

**Properties:**
- Gain cracks when hit by Seam hazards (rifts, collapse lines)
- Persist through phases (pressure)
- Reduced via consoles

### 2) Stabilizer Consoles (Primary Counterplay)

| Property | Value |
|----------|-------|
| **Interact time** | 1.3s |
| **Cooldown** | 26s per console (independent) |
| **Effect** | **REALITY CLAMP** for 10s |
| **Clamp effects** | -70% seam hazard damage/pull, -50% buff stripping, removes 2 Seam Integrity cracks (min 0), **PINNED** to Prime for 8s (+20% damage taken) |
| **Limit** | Only one Reality Clamp active at once |
| **Intent** | "Make the window, then burst" |

### 3) Null Fonts (Limited Relief)

| Property | Value |
|----------|-------|
| **Effect** | Cleanse 1 major debuff (priority: Null Mark → Turn Delay → Void Rot) |
| **Secondary** | 8s Dispel Dampening (max 1 buff/turn) |
| **Cooldown** | 24s |
| **Limit** | 2 uses per font total (UI shows charges) |

### 4) Core Clamp Plate (Risk-Reward, Optional)

| Property | Value |
|----------|-------|
| **Channel time** | 2.0s |
| **Cooldown** | 40s |
| **Use condition** | Only while Prime is **PINNED** |
| **Effect** | Extends PINNED by +4s, but spawns 2 rifts immediately (still telegraphed) |
| **Intent** | "Hero play" lever for skilled players |

---

## E) Hazard Timing (Exact)

### 1) Tear Rings (Seam Rifts)

| Property | Value |
|----------|-------|
| **Frequency** | Every 14 seconds (P2: 12s) |
| **Pattern** | 2 rifts (pull zones, radius ~4) |
| **Telegraph** | 1.6s dark ring + static hiss |
| **Active** | 8.0s |
| **Effect** | Pull 1 tile/2s; pulled at least once = Seam Integrity +1 |

### 2) Fault Lanes (Collapse Lines)

| Property | Value |
|----------|-------|
| **Frequency** | Every 12 seconds (P3: 10s) |
| **Pattern** | 2 lane strikes (horizontal/vertical) |
| **Telegraph** | 1.4s thick split-line |
| **Impact** | Heavy damage + Seam Integrity +1 if hit |
| **Block** | Blockable by cover pylons (LoS) |

### 3) Veil Curtains (Phase 2+)

| Property | Value |
|----------|-------|
| **Frequency** | Every 18 seconds |
| **Pattern** | 2 veil patches |
| **Telegraph** | 1.0s smoky bloom |
| **Active** | 8.0s |
| **Effect** | Accuracy down/confounded-lite; increases "buff nick" chance |

---

## F) Captain Moveset

### 1) Seam Scythe

| Property | Value |
|----------|-------|
| **Type** | Fast line strike |
| **Telegraph** | 0.8s thin line + blade hiss |
| **Hit** | Damage + Seam Integrity +1 (if cracked, applies Void Rot minor) |

### 2) Null Quota

| Property | Value |
|----------|-------|
| **Type** | Dispel by rule |
| **Telegraph** | 1.0s stamp icon over party UI |
| **Effect** | Removes 1 buff from each character |
| **Passive** | Also applied at start of Prime's next turn |

### 3) Phase Step

| Property | Value |
|----------|-------|
| **Type** | Reposition blink |
| **Telegraph** | 0.7s shimmer |
| **Effect** | Leaves 3-tile "phase scar" for 4s (minor rift contact) |

### 4) Judicator Pin

| Property | Value |
|----------|-------|
| **Type** | Single-target root setup |
| **Telegraph** | 1.2s chain glyph under target |
| **Effect** | Short root + sets up for Fault Lanes (combo pressure) |

### 5) SEAM COLLAPSE (Signature Near-Wipe)

| Property | Value |
|----------|-------|
| **Trigger** | Seam Integrity hits 6 → casts on next turn |
| **Telegraph** | 2.6s full-screen crack vignette + loud fracture |
| **Resolved** | Massive damage + 2 debuffs + cracks reset to 3 |
| **Counter** | Reality Clamp before completion → cancels collapse + stuns Prime 2s (free burst) |

---

## G) Phases (HP-Based)

### Phase 1 (100% → 60%) — "Stitchwork"

| Aspect | Timing |
|--------|--------|
| **Rifts** | Every 14s |
| **Fault Lanes** | Every 12s |
| **Null Quota** | Every ~20s |
| **Veils** | None |
| **Goal** | Teach console = clamp + crack reduction |

### Phase 2 (60% → 25%) — "Unravel"

| Aspect | Change |
|--------|--------|
| **Veil Curtains** | Every 18s (new) |
| **Rifts** | Every 12s (was 14s) |
| **Null Quota** | Every 16–18s (more frequent) |
| **Phase Step** | More often to bait positioning |

### Phase 3 (25% → 0%) — "Prime Cut"

| Aspect | Description |
|--------|-------------|
| **One-time at 25%** | **ECLIPSE INDICTMENT** |
| **Fault Lanes** | Every 10s (was 12s) |
| **Consoles** | Remain fully effective |
| **Clamp Plate** | "Finish window" option (hero play) |

#### ECLIPSE INDICTMENT

| Property | Value |
|----------|-------|
| **Telegraph** | 2.4s black-white seal over center (28,28) |
| **Effect** | Spawns 3 rifts (8s) + immediate Fault Lanes (still telegraphed) |

---

## H) Fight Scripting (Sequence)

| Step | Event |
|------|-------|
| 1 | Enter → doors lock |
| 2 | Prime: "Reality requires enforcement." |
| 3 | Hazard loop begins within 6 seconds (first Fault Lanes) |
| 4 | Phase shifts at 60% and 25% with "fracture pulse" VFX |
| 5 | On defeat: hazards shut off, chest spawns, return gate unlocks |

---

## I) Rewards (Captain Door — Floor 95)

| Reward | Amount |
|--------|--------|
| **Tower Tokens** | +22 |
| **Duckets** | +220k–260k |
| **Tier 5 mats** | 6 rolls from Eclipse/Seam pool (high Shadow/Time weight) |
| **Unique Component** | **Seam Warden Seal** (craft key for anti-dispel / phase resist gear) |
| **Gear** | 1 extra Tier 5 roll (Captain bonus; premium affix bias) |

### Flag

| Flag | Condition |
|------|-----------|
| `TOWER_CAPTAIN_F95_DEFEATED` | TRUE |

---

## Quick Reference: Arena at a Glance

```
    NORTH (y=0)
       ↑
    ┌─────────────────────────────────┐
    │  Reward Pad (y 44–56)           │
    │  - Chest (28,46)                │
    │  - Return Gate (28,54)          │
    └─────────────────────────────────┘
                      │
    ══════════════════╪═════════════════ (y=44)
                      │
    ┌─────────────────────────────────┐
    │  Arena Bowl (y 6–44)            │
    │                                 │
    │    Pylon NW    Pylon NE         │
    │    (16,16)     (40,16)          │
    │       │           │             │
    │ Console L  CLAMP  Console R     │
    │ (10,26)   (28,28)  (46,26)      │
    │       │           │             │
    │    Font L         Font R        │
    │    (20,38)        (36,38)       │
    │       │           │             │
    │    Pylon SW    Pylon SE         │
    │    (16,32)     (40,32)          │
    │                                 │
    │         BOSS                    │
    │         (28,22)                 │
    │                                 │
    └─────────────────────────────────┘
                      │
    ══════════════════╪═════════════════ (y=44)
                      │
    ┌─────────────────────────────────┐
    │  Prep Hall (y 44–56)            │
    │  - Entry (28,52)                │
    │  - Lock (28,43)                 │
    └─────────────────────────────────┘
                      │
                   SOUTH (y=55)

SEAM INTEGRITY (0–6 CRACKS):
├─ 0–2: Normal
├─ 3: Boss gains minor speed
└─ 6: Triggers SEAM COLLAPSE (near-wipe)

STABILIZER CONSOLES (2):
├─ L(10,26), R(46,26)
├─ Reality Clamp: 10s
│   ├─ -70% hazard damage/pull
│   ├─ -50% buff stripping
│   ├─ Remove 2 cracks
│   └─ PINNED to Prime (+20% damage, 8s)
└─ Cooldown: 26s each

SEAM COLLAPSE:
├─ Trigger: 6 cracks
├─ Telegraph: 2.6s crack vignette + fracture
├─ Effect: Massive damage + 2 debuffs + cracks to 3
└─ Counter: Reality Clamp → cancels + stuns 2s

NULL FONTS (2):
├─ L(20,38), R(36,38)
├─ Cleanse debuff + Dispel Dampening (8s)
├─ Cooldown: 24s
└─ Limit: 2 uses each

CORE CLAMP PLATE (28,28):
├─ Channel: 2.0s, Cooldown: 40s
├─ Use: Only while PINNED
├─ Effect: Extends PINNED +4s, spawns 2 rifts
└─ Intent: Hero play

HAZARDS:
├─ Tear Rings: Every 14s (P2: 12s), 2 rifts, 1.6s telegraph
├─ Fault Lanes: Every 12s (P3: 10s), 2 lanes, 1.4s telegraph
└─ Veil Curtains: Every 18s (P2+), 2 patches, 1.0s telegraph

PHASE SUMMARY:
P1 (100–60%): Stitchwork — Standard cadence, teach console loop
P2 (60–25%): Unravel — Veils added, faster rifts, frequent Quota
P3 (25–0%): Prime Cut — Eclipse Indictment at 25%, faster lanes, hero plays
```
