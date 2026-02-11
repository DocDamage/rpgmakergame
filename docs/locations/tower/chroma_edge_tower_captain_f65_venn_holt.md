# Chroma's Edge — Tower Captain Arena: Floor 65 (v1)
## Chrono Surveyor Venn Holt (Time) — "Rewind Audit"

---

## 0) Technical Specs

| Parameter | Value |
|-----------|-------|
| **Captain** | Chrono Surveyor Venn Holt |
| **Identity** | Time Captain — "Rewind Audit" |
| **Tower Floor** | 65 (optional Captain Door room) |
| **Recommended Level** | 170–195 |
| **Fight Identity** | Turn order pressure + controlled rewinds. Lock timeline with anchors, burst during Time-Locked windows |
| **Arena Size** | 56 × 56 tiles (Template E: Arena + Prep Hall) |
| **Type** | Optional Captain Challenge arena (single fight) |
| **Encounters** | OFF (boss only) |
| **Mounts** | Disabled |
| **Retry behavior** | Standard Tower (resume at last save floor) |

---

## A) Access / Door Logic (on Floor 65)

| Property | Description |
|----------|-------------|
| **Door mark** | Cyan seal + clock icon |
| **Prompt** | "ENTER CAPTAIN CHALLENGE — CHRONO SURVEYOR" |

---

## B) Layout Overview

### 1) Prep Hall (Safe)

| Property | Value |
|----------|-------|
| **Bounds** | x 0–56, y 44–56 |
| **Features** | Ready tile + optional one-time supply crate |

### 2) Arena Bowl (Survey Grid)

| Property | Value |
|----------|-------|
| **Bounds** | x 6–50, y 6–44 |
| **Features** | Open court with 4 Time Anchors, 4 Survey Pillars (LoS blockers), central Chrono Dial (visual cue) |

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
| **Venn Holt spawn** | (28, 22) | — |

### Time Anchors (Primary Counterplay, 4)

| Anchor | Coordinates |
|--------|-------------|
| **Anchor N** | (28, 10) |
| **Anchor W** | (10, 22) |
| **Anchor E** | (46, 22) |
| **Anchor S** | (28, 38) |

### Survey Pillars (3×3 Collision; Blocks Line Attacks)

| Pillar | Coordinates |
|--------|-------------|
| **NW** | (16, 16) |
| **NE** | (40, 16) |
| **SW** | (16, 32) |
| **SE** | (40, 32) |

### Central Dial (Visual Cue Only)

| Feature | Coordinates |
|---------|-------------|
| **Dial tile** | (28, 28) |

### Reward Spawn

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Captain chest** | (28, 46) | After victory |
| **Return gate** | (28, 54) | After victory |

---

## D) Arena Systems

### 1) TIME DEBT (Mini-Meter)

| Stacks | Effect |
|--------|--------|
| **3** | Minor Turn Delay (small) |
| **6** | **DESYNCED** — more likely to be "skipped" by Venn's effects |
| **8** | Triggers **REWIND AUDIT** on Venn's next action |

### 2) Time Anchors (Primary Counterplay)

| Property | Value |
|----------|-------|
| **Interact time** | 1.0s |
| **Cooldown** | 24s per anchor (independent) |
| **Effect** | **TIME-LOCK FIELD** for 10s (radius ~5 tiles) |
| **Field effects** | -70% TIME DEBT gain, STOP→SLOW inside, blocks Rewind Audit |
| **Limit** | Only one Time-Lock Field active at once |
| **Big payoff** | Activate during Rewind Audit charge → cast fails → Venn gains **EXPOSED** (+damage) for 8s |

### 3) Survey Marks (Anti-Camp)

| Property | Value |
|----------|-------|
| **Frequency** | Every 12 seconds |
| **Pattern** | 2 tiles stamped |
| **Effect** | Standing on marked tile when it triggers = TIME DEBT +1 |
| **Intent** | Forces movement, prevents pillar hugging forever |

---

## E) Hazard Timing (Exact)

### 1) Temporal Gaps (Flicker Slabs)

| Property | Value |
|----------|-------|
| **Frequency** | Every 12 seconds (P3: 10s) |
| **Telegraph** | 1.4s shimmer → flicker |
| **Active** | 5.0s (tiles "blank out") |
| **Effect** | End turn on blank = Turn Delay + TIME DEBT +1 |

### 2) Stillness Plates (Stop Panels)

| Property | Value |
|----------|-------|
| **Frequency** | Every 18 seconds (P2: 16s) |
| **Pattern** | 1 rectangle (~7×3 tiles) |
| **Telegraph** | 1.6s ticking grid |
| **Active** | 4.0s |
| **Effect** | STOP (short) + TIME DEBT +2 |
| **Time-Lock Field** | STOP becomes SLOW (no full stop) |

### 3) Survey Marks

| Property | Value |
|----------|-------|
| **Frequency** | Every 12 seconds |
| **Telegraph** | 0.8s tiny crosshair stamp |
| **Trigger** | On stamp completion (instant) |
| **Effect** | TIME DEBT +1 |

---

## F) Captain Moveset

### 1) Chrono Scanline (Line Snipe)

| Property | Value |
|----------|-------|
| **Telegraph** | 1.1s thin line + rising chirp |
| **Effect** | Medium-heavy damage + TIME DEBT +1 |
| **Block** | Blocked by Survey Pillars |
| **Frequency** | P3: every ~12s (more frequent) |

### 2) Delay Citation (Targeted Debuff)

| Property | Value |
|----------|-------|
| **Telegraph** | 0.9s "stamp" icon over target |
| **Effect** | SLOW (2 stacks) + TIME DEBT +2 |

### 3) Afterimage Cut (Delayed Strike)

| Property | Value |
|----------|-------|
| **Telegraph** | 1.0s ghost silhouette at target tile |
| **Delay** | Strike lands 2 seconds later |
| **Effect** | Damage + TIME DEBT +1 |
| **P2+** | Double Afterimage (two silhouettes) |

### 4) Rewind Step (Reposition + Hazard Drop)

| Property | Value |
|----------|-------|
| **Telegraph** | 0.7s blur |
| **Effect** | Venn blinks to new lane, drops 2 Flicker Slabs immediately |

### 5) REWIND AUDIT (Signature)

| Trigger | Effect |
|---------|--------|
| **Any target hits 8 TIME DEBT** OR **phase threshold** | Begins charging |
| **Telegraph** | 2.2s full-screen clock vignette + loud tick |
| **If resolves** | Restores Venn's HP to 6 seconds ago (cap: +20% max), clears 1 debuff, TIME DEBT +1 to whole party |
| **Counter** | Time-Lock Field active before completion → cast fizzles → Venn EXPOSED (+damage) for 8s |

---

## G) Phases (HP-Based)

### Phase 1 (100% → 60%) — "Initial Survey"

| Aspect | Timing |
|--------|--------|
| **Flicker Slabs** | Every 12s |
| **Stop Panels** | Every 18s |
| **Attacks** | Scanline, Delay Citation, Afterimage Cut |
| **Rewind Audit** | Only via 8 Time Debt (no free casts) |

### Phase 2 (60% → 25%) — "Edited Record"

| Aspect | Change |
|--------|--------|
| **Stop Panels** | Every 16s (was 18s) |
| **New** | **Double Afterimage**: two delayed silhouettes |
| **Rewind Audit** | Auto-cast once at 50% HP (one-time, +20% max cap) |

### Phase 3 (25% → 0%) — "Final Measurement"

| Aspect | Change |
|--------|--------|
| **Flicker Slabs** | Every 10s (was 12s) |
| **Scanline** | Every ~12s (more frequent) |
| **One-time at 25%** | **TIMELINE SNAPSHOT** |
| **Rewind Audit** | Time-Lock always cancels it |

#### TIMELINE SNAPSHOT

| Property | Value |
|----------|-------|
| **Telegraph** | 2.4s big stamp on central Dial (28,28) |
| **Effect** | Stamps 6 Survey Marks around arena (movement check), then returns to normal |

---

## H) Fight Scripting (Sequence)

| Step | Event |
|------|-------|
| 1 | Enter → doors lock |
| 2 | Venn: "Your progress is provisional." |
| 3 | Hazard loop begins within 6 seconds |
| 4 | Phase shifts at 60% and 25% with "gear-shift" VFX |
| 5 | On defeat: hazards stop, chest spawns, return gate unlocks |

---

## I) Rewards (Captain Door — Floor 65)

| Reward | Amount |
|--------|--------|
| **Tower Tokens** | +14 |
| **Duckets** | +140k–190k |
| **Tier 5 mats** | 4 rolls from Time/Chrono pool |
| **Gear** | 1 extra Tier 5 roll (Captain bonus, Time-leaning affixes) |

### Flag

| Flag | Condition |
|------|-----------|
| `TOWER_CAPTAIN_F65_DEFEATED` | TRUE |

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
    │    Pillar NW    Pillar NE       │
    │    (16,16)      (40,16)         │
    │       │            │            │
    │ Anchor W    DIAL    Anchor E    │
    │ (10,22)   (28,28)   (46,22)     │
    │       │            │            │
    │    Pillar SW    Pillar SE       │
    │    (16,32)      (40,32)         │
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

TIME DEBT METER:
├─ 0–2: Normal
├─ 3: Minor Turn Delay
├─ 6: DESYNCED (more likely to be "skipped")
└─ 8: Triggers REWIND AUDIT

TIME ANCHORS (4):
├─ N(28,10), W(10,22), E(46,22), S(28,38)
├─ Field: 10s, -70% DEBT gain, STOP→SLOW, blocks Rewind Audit
├─ Counter Rewind Audit → Venn EXPOSED (+damage, 8s)
└─ Cooldown: 24s each

SURVEY MARKS:
├─ Every 12s, 2 tiles stamped
└─ Standing on trigger = TIME DEBT +1

HAZARDS:
├─ Flicker Slabs: Every 12s (P3: 10s), 1.4s shimmer, 5s blank
├─ Stop Panels: Every 18s (P2: 16s), 1.6s ticking, STOP + DEBT +2
└─ Survey Marks: Every 12s, 0.8s crosshair

REWIND AUDIT:
├─ Trigger: 8 DEBT or phase threshold
├─ Telegraph: 2.2s clock vignette + tick
├─ Effect: HP to 6s ago (cap +20% max), clear 1 debuff, party DEBT +1
└─ Counter: Time-Lock Field → fizzles → EXPOSED

PHASE SUMMARY:
P1 (100–60%): Initial Survey — Standard cadence, Audit via DEBT only
P2 (60–25%): Edited Record — Faster panels, Double Afterimage, Audit at 50% HP
P3 (25–0%): Final Measurement — Faster slabs, Snapshot at 25%, frequent Scanlines
```
