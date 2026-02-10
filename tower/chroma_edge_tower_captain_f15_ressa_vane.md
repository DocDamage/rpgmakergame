# Chroma's Edge — Tower Captain Arena: Floor 15 (v1)
## Warden Pyre-Lieut. Ressa Vane (Heat) — "Overheat Audit"

---

## 0) Technical Specs

| Parameter | Value |
|-----------|-------|
| **Captain** | Warden Pyre-Lieut. Ressa Vane |
| **Identity** | Heat Warden — "Overheat Audit" |
| **Tower Floor** | 15 (optional Captain Door room) |
| **Recommended Level** | 110–130 |
| **Fight Identity** | Heat pressure + anti-heal punishment. Vent Ignition, time heals, use coolant tools |
| **Arena Size** | 56 × 56 tiles (Template E: Arena + Prep Hall) |
| **Type** | Optional Captain Challenge arena (single fight) |
| **Encounters** | OFF (boss only) |
| **Mounts** | Disabled |
| **Retry behavior** | Standard Tower (resume at last save floor) |

---

## A) Access / Door Logic (on Floor 15)

### Captain Door Spawn Rule

| Property | Description |
|----------|-------------|
| **Appearance** | Side door on Floor 15 (Template A/B/C), marked with red seal + flame icon |
| **Prompt** | "ENTER CAPTAIN CHALLENGE — HEAT WARDEN" |
| **Gating** | Once entered: cannot leave until win/lose (clean challenge) |

---

## B) Layout Overview

### 1) Prep Hall (Safe)

| Property | Value |
|----------|-------|
| **Bounds** | x 0–56, y 44–56 |
| **Features** | 1 "Ready" tile + optional one-time supply crate |

### 2) Arena Bowl

| Property | Value |
|----------|-------|
| **Bounds** | x 6–50, y 6–44 |
| **Features** | 4 cover pillars + 2 coolant valves + 4 vent grates (hazard) |

### 3) Reward Pad (Spawns After Win)

| Property | Value |
|----------|-------|
| **Bounds** | Center lane just above prep hall |

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
| **Ressa Vane spawn** | (28, 22) | — |

### Cover Pillars (3×3 Collision)

| Pillar | Coordinates |
|--------|-------------|
| **NW** | (16, 16) |
| **NE** | (40, 16) |
| **SW** | (16, 32) |
| **SE** | (40, 32) |

### Coolant Valves (Counterplay)

| Valve | Coordinates |
|-------|-------------|
| **Valve L** | (8, 24) |
| **Valve R** | (48, 24) |

### Vent Grates (Floor Hazard Clusters, 3×3 Each)

| Vent | Coordinates |
|------|-------------|
| **Vent A** | (20, 12) |
| **Vent B** | (36, 12) |
| **Vent C** | (20, 36) |
| **Vent D** | (36, 36) |

### Reward Spawn

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Captain reward chest** | (28, 46) | After victory |
| **Return gate to Floor 15** | (28, 54) | Unlocks after victory |

---

## D) Arena Systems

### 1) Ignition Stacks (Main Mechanic)

| Property | Description |
|----------|-------------|
| **Range** | 0–10 stacks |
| **At 6 stacks** | Target becomes **OVERHEATED** |
| **OVERHEATED effect** | Chip damage at end of turn, healing becomes risky |

### 2) "Overheat Audit" (Anti-Heal Punishment)

| Trigger | Effect |
|---------|--------|
| **Heal while OVERHEATED** | Ressa triggers **AUDIT BLAST** (once/turn max) |
| **Audit Blast** | Small burst damage + +2 Ignition |
| **Lesson** | Vent stacks first, then heal |

### 3) Coolant Valves (Primary Counterplay)

| Property | Value |
|----------|-------|
| **Interact time** | 1.1s |
| **Cooldown** | 22s per valve (independent) |
| **Effect** | **COOLANT FIELD** (radius ~4 tiles, 10s) |
| **Field effects** | -1 Ignition/2 seconds, prevents stacks >6 while inside |
| **Visual** | Frost-mist + blue ring |

---

## E) Hazard Timing (Exact)

### Vent Grates: "Flash Vent"

| Property | Value |
|----------|-------|
| **Frequency** | Every 12 seconds (P2+: every 10s) |
| **Pattern** | Two vents activate |
| **Telegraph** | 1.4s orange glow + hiss |
| **Active** | 3.0s |
| **Effect** | +2 Ignition + chip damage |

---

## F) Captain Moveset

### 1) Warden's Brand (Single Target)

| Property | Value |
|----------|-------|
| **Telegraph** | 0.8s flame sigil over target |
| **Effect** | +2 Ignition + minor damage |

### 2) Compliance Sweep (Lane Beam)

| Property | Value |
|----------|-------|
| **Telegraph** | 1.3s thick lane line from Ressa |
| **Effect** | Heavy damage + +1 Ignition |
| **Block** | Blockable by pillars |

### 3) Heat Ledger (Debuff Pulse)

| Property | Value |
|----------|-------|
| **Telegraph** | 1.2s "paper seal" swirl + heat shimmer |
| **Effect** | Ignition +1 to all not inside Coolant Field |
| **Frequency** | P1: 18s, P2+: 14s |

### 4) Punitive Lunge (Gap Close)

| Property | Value |
|----------|-------|
| **Telegraph** | 0.9s dash line |
| **Effect** | Medium damage + knockback; punishes valve campers |

### 5) Audit Blast (Reaction)

| Property | Value |
|----------|-------|
| **Trigger** | Healing while Overheated |
| **Limit** | Once/turn max |
| **Effect** | Small burst + +2 Ignition |

---

## G) Phases (HP-Based)

### Phase 1 (100% → 60%) — "First Citation"

| Aspect | Description |
|--------|-------------|
| **Vent cycle** | Every 12s |
| **Rotation** | Brand + Sweep emphasis |
| **Heat Ledger** | Every 18s |

### Phase 2 (60% → 25%) — "Escalation Notice"

| Aspect | Description |
|--------|-------------|
| **Vent cycle** | Every 10s (faster) |
| **Heat Ledger** | Every 14s (faster) |
| **New** | **Double Sweep**: two crossing lanes (telegraphed separately) |

### Phase 3 (25% → 0%) — "Final Warning"

| Aspect | Description |
|--------|-------------|
| **Overcharge** | Sweep lanes linger 0.5s longer |
| **Coolant Fields** | Still work (counterplay preserved) |
| **One-time at 20%** | **"Warden's Ultimatum"** |

#### Warden's Ultimatum

| Property | Value |
|----------|-------|
| **Telegraph** | 2.0s big seal stamp |
| **Effect** | Pushes everyone to 5 Ignition (not 6+) |
| **Type** | Pressure spike, not wipe |

---

## H) Fight Scripting (Sequence)

| Step | Event |
|------|-------|
| 1 | Enter → doors lock |
| 2 | Ressa: "Unauthorized heat signature detected." |
| 3 | Fight begins |
| 4 | Phase transitions at 60% and 25% with flame-seal flare |
| 5 | On defeat: vents shut off, chest spawns, return gate unlocks |

---

## I) Rewards (Captain Door)

| Reward | Amount |
|--------|--------|
| **Tower Tokens** | +8 (bonus) |
| **Duckets** | +60k–90k |
| **Tier 5 mats** | 2 rolls from Heat/Metal pool |
| **Gear** | 1 extra Tier 4–5 roll (Captain bonus) |

### Flag

| Flag | Condition |
|------|-----------|
| `TOWER_CAPTAIN_F15_DEFEATED` | TRUE |

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
    │      Vent A      Vent B         │
    │     (20,12)     (36,12)         │
    │          ╲      ╱               │
    │    Pillar NW  Pillar NE         │
    │    (16,16)    (40,16)           │
    │              │                  │
    │  Valve L ─── BOSS ─── Valve R   │
    │  (8,24)    (28,22)    (48,24)   │
    │              │                  │
    │    Pillar SW  Pillar SE         │
    │    (16,32)    (40,32)           │
    │          ╱      ╲               │
    │      Vent C      Vent D         │
    │     (20,36)     (36,36)         │
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

IGNITION SYSTEM:
├─ 0–5 stacks: Normal
├─ 6+ stacks: OVERHEATED (chip damage, risky heals)
└─ Max: 10 stacks

OVERHEAT AUDIT:
└─ Heal while OVERHEATED → Audit Blast (burst +2 Ignition)

COOLANT VALVES (2):
├─ L(8,24), R(48,24)
├─ Field: 10s, -1 Ignition/2s, caps at 6
└─ Cooldown: 22s each

VENT GRATES (4):
├─ A(20,12), B(36,12), C(20,36), D(36,36)
├─ Activate: Every 12s (P2+: 10s), 2 at a time
├─ Telegraph: 1.4s glow + hiss
└─ Effect: +2 Ignition + chip damage

PHASE SUMMARY:
P1 (100–60%): First Citation — 12s vents, Brand + Sweep
P2 (60–25%): Escalation — 10s vents, Double Sweep, faster Ledger
P3 (25–0%): Final Warning — Longer sweeps, Ultimatum at 20%
```
