# Chroma's Edge — Tower Captain Arena: Floor 55 (v1)
## Gravemaster Bront Kessel (Mass) — "Weight of Judgment"

---

## 0) Technical Specs

| Parameter | Value |
|-----------|-------|
| **Captain** | Gravemaster Bront Kessel |
| **Identity** | Mass Captain — "Weight of Judgment" |
| **Tower Floor** | 55 (optional Captain Door room) |
| **Recommended Level** | 155–180 |
| **Fight Identity** | Gravity control + forced reposition. Stabilize pull zones, dodge compression slams, use Mass Anchors for safe windows |
| **Arena Size** | 56 × 56 tiles (Template E: Arena + Prep Hall) |
| **Type** | Optional Captain Challenge arena (single fight) |
| **Encounters** | OFF (boss only) |
| **Mounts** | Disabled |
| **Retry behavior** | Standard Tower (resume at last save floor) |

---

## A) Access / Door Logic (on Floor 55)

| Property | Description |
|----------|-------------|
| **Door mark** | Black seal + gravity icon |
| **Prompt** | "ENTER CAPTAIN CHALLENGE — GRAVEMASTER" |

---

## B) Layout Overview

### 1) Prep Hall (Safe)

| Property | Value |
|----------|-------|
| **Bounds** | x 0–56, y 44–56 |
| **Features** | Ready tile + optional one-time supply crate |

### 2) Arena Bowl (Grav Court)

| Property | Value |
|----------|-------|
| **Bounds** | x 6–50, y 6–44 |
| **Features** | 4 cover monoliths (navigation + line-block), 4 Mass Anchors (counterplay), 1 Center Dais (danger) |

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
| **Bront Kessel spawn** | (28, 22) | — |

### Center Dais (Hazard Focal Point)

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Dais** | (28, 26) | "Center danger" |

### Cover Monoliths (3×3 Collision)

| Monolith | Coordinates |
|----------|-------------|
| **NW** | (16, 16) |
| **NE** | (40, 16) |
| **SW** | (16, 32) |
| **SE** | (40, 32) |

### Mass Anchors (Primary Counterplay, 4)

| Anchor | Coordinates |
|--------|-------------|
| **Anchor N** | (28, 10) |
| **Anchor W** | (10, 22) |
| **Anchor E** | (46, 22) |
| **Anchor S** | (28, 38) |

### Reward Spawn

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Captain chest** | (28, 46) | After victory |
| **Return gate** | (28, 54) | After victory |

---

## D) Arena Systems

### 1) HEAVY Stacks (Main Debuff)

| Stacks | Effect |
|--------|--------|
| **4 stacks** | Movement reduced / turn order penalty |
| **6 stacks** | **CRUSH-PRONE** — takes bonus damage from slams |

### 2) Mass Anchors (Primary Counterplay)

| Property | Value |
|----------|-------|
| **Interact time** | 1.1s |
| **Cooldown** | 24s per anchor (independent) |
| **Effect** | **STABILITY FIELD** for 10s (radius ~5 tiles) |
| **Field effects** | Reduces pull/knockback by 70%, HEAVY gained -1 (min 0), converts "Crush-Prone" to "Heavy 3" |
| **Limit** | Only one Stability Field active at once |

### 3) Inertia Punish (Anti-Turtle)

| Trigger | Effect |
|---------|--------|
| **Stay inside Stability Field full duration** | Bront gains **INERTIA CHARGE** (1 stack) |
| **At 2 Inertia Charges** | Casts "Anchor Breaker" sooner (still telegraphed) |
| **Intent** | Discourage camping without deleting counterplay |

---

## E) Hazard Timing (Exact)

### 1) Singularity Pits (Gravity Wells)

| Property | Value |
|----------|-------|
| **Frequency** | Every 16 seconds (P2: 14s) |
| **Pattern** | 2 wells (6-tile radius pull zones) |
| **Telegraph** | 1.5s dark ring + low hum |
| **Active** | 8.0s |
| **Effect** | Pull 1 tile/2s toward center + HEAVY +1 if pulled |

### 2) Weightfall (Compression Slam)

| Property | Value |
|----------|-------|
| **Frequency** | Every 22 seconds (P2: 20s) |
| **Telegraph** | 2.0s rumble + expanding circle from Center Dais |
| **Impact** | Heavy damage near center, lighter at edge + HEAVY +2 if hit |

### 3) Grav Ripple (Shockline Push)

| Property | Value |
|----------|-------|
| **Frequency** | Every 14 seconds (P2: 12s) |
| **Pattern** | Two parallel lines sweep (horizontal OR vertical) |
| **Telegraph** | 1.2s line highlight + "thump" |
| **Effect** | Medium damage + knockback 2 tiles (reduced inside Stability Field) |

---

## F) Captain Moveset

### 1) Grav Hook

| Property | Value |
|----------|-------|
| **Type** | Single-target pull line |
| **Effect** | Drags target 3 tiles toward Bront |
| **Telegraph** | 1.0s tether line + chain rattle |
| **On hit** | HEAVY +1 |

### 2) Anvil Drop

| Property | Value |
|----------|-------|
| **Type** | Targeted circle AOE |
| **Effect** | Punishes stationary play |
| **Telegraph** | 1.6s circle + falling debris |
| **On hit** | Heavy damage + HEAVY +2 |

### 3) Tectonic Shoulder

| Property | Value |
|----------|-------|
| **Type** | Short dash to lane, then cone slam |
| **Telegraph** | 0.9s dash line + shoulder glow |
| **On hit** | Knockback + stagger |

### 4) Anchor Breaker (Signature)

| Property | Value |
|----------|-------|
| **Type** | Marked target delayed crush |
| **Telegraph** | 2.2s sigil stamp + rising bass |
| **Stability Field effect** | Damage reduced 60%, no Crush-Prone |

### 5) Judgment Beam (Rare, Line)

| Property | Value |
|----------|-------|
| **Telegraph** | 1.2s thick line |
| **Block** | Blocked by monoliths |

---

## G) Phases (HP-Based)

### Phase 1 (100% → 60%) — "Measure the Weight"

| Aspect | Timing |
|--------|--------|
| **Gravity Wells** | Every 16s |
| **Grav Ripple** | Every 14s |
| **Weightfall** | Every 22s |
| **Anchor Breaker** | Every ~28s |

### Phase 2 (60% → 25%) — "Collapse Protocol"

| Aspect | Change |
|--------|--------|
| **Gravity Wells** | Every 14s (was 16s) |
| **Grav Ripple** | Every 12s (was 14s) |
| **Weightfall** | Every 20s (was 22s) |
| **New combo** | Grav Hook → Anvil Drop (still telegraphed) |

### Phase 3 (25% → 0%) — "Final Density"

| Aspect | Description |
|--------|-------------|
| **One-time at 25%** | **CENTER OF MASS** |
| **Anchor Breaker** | Frequency increases slightly |
| **Counterplay** | Stability Fields remain fully effective |

#### CENTER OF MASS

| Property | Value |
|----------|-------|
| **Telegraph** | 2.4s arena darkens + center ring glows |
| **Effect** | Spawns 3 Gravity Wells at once (8s), then returns to normal cadence |

---

## H) Fight Scripting (Sequence)

| Step | Event |
|------|-------|
| 1 | Enter → doors lock |
| 2 | Bront: "Stand still. Let the weight decide." |
| 3 | Hazards begin within 6 seconds (first Gravity Wells) |
| 4 | Phase shifts at 60% and 25% with "gravity surge" VFX |
| 5 | On defeat: hazards shut off, chest spawns, return gate unlocks |

---

## I) Rewards (Captain Door — Floor 55)

| Reward | Amount |
|--------|--------|
| **Tower Tokens** | +12 |
| **Duckets** | +120k–170k |
| **Tier 5 mats** | 4 rolls from Mass/Grav pool |
| **Gear** | 1 extra Tier 5 roll (Captain bonus, Mass-leaning affixes) |

### Flag

| Flag | Condition |
|------|-----------|
| `TOWER_CAPTAIN_F55_DEFEATED` | TRUE |

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
    │         Anchor N                │
    │         (28,10)                 │
    │            │                    │
    │    Monolith NW    Monolith NE   │
    │    (16,16)        (40,16)       │
    │       │              │          │
    │ Anchor W    DAIS    Anchor E    │
    │ (10,22)   (28,26)   (46,22)     │
    │       │              │          │
    │    Monolith SW    Monolith SE   │
    │    (16,32)        (40,32)       │
    │            │                    │
    │         Anchor S                │
    │         (28,38)                 │
    │            │                    │
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

HEAVY STACKS:
├─ 0–3: Normal
├─ 4: Movement reduced / turn order penalty
└─ 6: CRUSH-PRONE (bonus slam damage)

MASS ANCHORS (4):
├─ N(28,10), W(10,22), E(46,22), S(28,38)
├─ Field: 10s, -70% pull/knockback, HEAVY -1
├─ Converts Crush-Prone → Heavy 3 (mercy)
└─ Cooldown: 24s each

INERTIA PUNISH (Anti-Turtle):
└─ Stay full duration in field → Bront gains Inertia Charge
    (2 charges = Anchor Breaker casts sooner)

HAZARDS:
├─ Singularity Pits: Every 16s (P2: 14s), 2 wells, 1.5s telegraph
├─ Weightfall: Every 22s (P2: 20s), 2.0s telegraph from center
└─ Grav Ripple: Every 14s (P2: 12s), 2 parallel lines

PHASE SUMMARY:
P1 (100–60%): Measure the Weight — Standard cadence
P2 (60–25%): Collapse Protocol — Faster hazards, Hook→Drop combo
P3 (25–0%): Final Density — Center of Mass at 25%, faster Breakers
```
