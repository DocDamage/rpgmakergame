# Chroma's Edge — Tower Captain Arena: Floor 85 (v1)
## Echelon Custodian "Null-Scribe" (Composite) — "Rotating Edicts"

---

## 0) Technical Specs

| Parameter | Value |
|-----------|-------|
| **Captain** | Echelon Custodian "Null-Scribe" |
| **Identity** | Composite Captain — "Rotating Edicts" |
| **Tower Floor** | 85 (optional Captain Door room) |
| **Recommended Level** | 205–225 |
| **Fight Identity** | Systems captain. Rotates three Edicts mid-fight (regen → dispel → bleed). Read active Edict, use Edict Consoles, burst during Redaction Windows |
| **Arena Size** | 56 × 56 tiles (Template E: Arena + Prep Hall) |
| **Type** | Optional Captain Challenge arena (single fight) |
| **Encounters** | OFF (boss only) |
| **Mounts** | Disabled |
| **Retry behavior** | Standard Tower (resume at last save floor) |

---

## A) Access / Door Logic (on Floor 85)

| Property | Description |
|----------|-------------|
| **Door mark** | Black-white seal + quill icon |
| **Prompt** | "ENTER CAPTAIN CHALLENGE — NULL-SCRIBE" |

---

## B) Layout Overview

### 1) Prep Hall (Safe)

| Property | Value |
|----------|-------|
| **Bounds** | x 0–56, y 44–56 |
| **Features** | Ready tile + optional one-time supply crate |

### 2) Arena Bowl (Redaction Court)

| Property | Value |
|----------|-------|
| **Bounds** | x 6–50, y 6–44 |
| **Features** | 4 line-blocking plinths + 3 Edict Consoles + 1 Redaction Seal (risk/reward) |

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
| **Null-Scribe spawn** | (28, 22) | — |

### Cover Plinths (3×3 Collision; Blocks Line Attacks)

| Plinth | Coordinates |
|--------|-------------|
| **NW** | (16, 16) |
| **NE** | (40, 16) |
| **SW** | (16, 32) |
| **SE** | (40, 32) |

### Edict Consoles (Primary Counterplay, 3)

| Console | Coordinates | Function |
|---------|-------------|----------|
| **Console A** | (28, 10) | Edict Key |
| **Console B** | (10, 26) | Edict Key |
| **Console C** | (46, 26) | Edict Key |

### Redaction Seal (Risk-Reward Burst Window)

| Feature | Coordinates |
|---------|-------------|
| **Seal tile** | (28, 28) |

### Reward Spawn

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Captain chest** | (28, 46) | After victory |
| **Return gate** | (28, 54) | After victory |

---

## D) Core Systems

### 1) Rotating Edicts (The Gimmick)

| Edict | Effect |
|-------|--------|
| **EDICT OF RENEWAL** | Regen |
| **EDICT OF NULL** | Buff-dispel |
| **EDICT OF WOUNDS** | Bleed/DoT |

#### Cycle Timing

| Phase | Swap Frequency |
|-------|----------------|
| **P1** | Every 18 seconds |
| **P2+** | Every 15 seconds |
| **Telegraph** | 1.2s "Page Turn" (big icon + paper rip SFX) |

### 2) Edict Consoles (Primary Counterplay)

| Property | Value |
|----------|-------|
| **Interact time** | 1.1s |
| **Cooldown** | 22 seconds per console (independent) |
| **Effect** | "Stamp Counter-Clause" for 10 seconds |
| **Match effect** | Reduces active Edict by 70%, applies EXPOSED (+damage) for 8s |
| **Match rule** | Any console counters any Edict (prints clause based on current icon) |
| **Limit** | Only one Counter-Clause active at once |
| **Player job** | See icon → hit any console → get safe window |

### 3) Redaction Seal (Burst Window With Cost)

| Property | Value |
|----------|-------|
| **Channel time** | 2.0s (interruptible) |
| **Cooldown** | 35 seconds |
| **Effect** | **REDACTION WINDOW** for 8 seconds |
| **Window effects** | No adds, loses one special attack, party +damage |
| **Cost** | "Ink Burn" to channeler (small DoT, 10s) |

---

## E) Edict Effects

### EDICT OF RENEWAL (Regen)

| Effect | Details |
|--------|---------|
| **Regen** | 8% HP at end of turn |
| **Renewal Glyphs** | Spawns 2 on floor |
| **Glyph timing** | Every 12s while Renewal active |
| **Telegraph** | 1.2s green circles |
| **Active** | 8.0s |
| **Standing on glyph** | Heals boss slightly |

### EDICT OF NULL (Buff-Dispel)

| Effect | Details |
|--------|---------|
| **Turn start** | Removes 1 buff from each party member (strongest) |
| **Null Lances** | More frequent |
| **Null Pulse** | Every 14s while Null active |
| **Telegraph** | 1.6s expanding ring + static hiss |
| **Effect** | Strip 1 buff + Null Mark-lite (50% chance next buff vanishes) |

### EDICT OF WOUNDS (Bleed/DoT)

| Effect | Details |
|--------|---------|
| **WOUND stacks** | 0–6 (attacks apply stacks) |
| **At 4 stacks** | Target bleeds at end of turn |
| **Blood Script tiles** | Every 16s while Wounds active |
| **Telegraph** | 1.3s red ink blot circles |
| **Active** | 7.0s |
| **Standing in blot** | +1 WOUND per second |

---

## F) Hazard Timing (Global, Regardless of Edict)

### 1) Ledger Lines (Sweeping Lanes)

| Property | Value |
|----------|-------|
| **Frequency** | Every 12 seconds |
| **Telegraph** | 1.3s thin line(s) + "scribe scratch" |
| **Pattern** | 2 lanes (horizontal or vertical) |
| **Hit** | Medium damage + current Edict minor stack |

### 2) Footnote Mines (Phase 2+)

| Property | Value |
|----------|-------|
| **Frequency** | Every 18 seconds (P2+ only) |
| **Telegraph** | 1.2s small dots |
| **Active** | 6.0s |
| **Step** | Small stagger + adds 1 stack of current Edict debuff |

---

## G) Captain Moveset

### 1) Clause Cutter (Single-Target)

| Property | Value |
|----------|-------|
| **Telegraph** | 0.8s quill glow over target |
| **Effect** | Damage + current Edict stack (+2 in P3) |

### 2) Censure Sweep (Cone)

| Property | Value |
|----------|-------|
| **Telegraph** | 1.0s cone outline |
| **Effect** | Medium damage + pushes 1 tile |

### 3) Margin Seal (Trap)

| Property | Value |
|----------|-------|
| **Telegraph** | 1.3s square stamp on tile |
| **Effect** | After 2s, tile "locks" (brief slow/turn delay if standing on it) |

### 4) Add Spawn: Errata Drones (Phase 2+)

| Property | Value |
|----------|-------|
| **Telegraph** | 1.2s paper tear VFX near edges |
| **Spawn** | 1–2 drones (cap 2) |
| **Inheritance** | Drones inherit current Edict (regen/dispels/bleed pressure) |

### 5) "Edited Record" Swap (Signature Swap)

| Trigger | Each Edict change |
|---------|-------------------|
| **Telegraph** | 1.2s page turn |
| **Effect** | Immediate small burst tied to new Edict: Renewal (heal + glyph), Null (dispel wave), Wounds (ink blot scatter) |

---

## H) Phases (HP-Based)

### Phase 1 (100% → 60%) — "First Draft"

| Aspect | Description |
|--------|-------------|
| **Edict swap** | Every 18s |
| **Drones** | None |
| **Hazards** | Ledger Lines + Edict hazards |

### Phase 2 (60% → 25%) — "Second Draft"

| Aspect | Change |
|--------|--------|
| **Edict swap** | Every 15s (was 18s) |
| **New** | Errata Drones (cap 2) |
| **New** | Footnote Mines every 18s |
| **Edict strength** | Slightly stronger (regen +1%, wounds stack faster) |

### Phase 3 (25% → 0%) — "Final Redaction"

| Aspect | Description |
|--------|-------------|
| **One-time at 25%** | **REDACTION ORDER** |
| **Edict swap** | Remains 15s |
| **Hot period** | First 4 seconds after swap = higher hazard density |
| **Consoles** | Remain fully effective |

#### REDACTION ORDER

| Property | Value |
|----------|-------|
| **Telegraph** | 2.4s giant stamp over center Seal (28,28) |
| **Effect** | Immediate Edict swap + simultaneous Ledger Lines (still telegraphed) |

---

## I) Fight Scripting (Sequence)

| Step | Event |
|------|-------|
| 1 | Enter → doors lock |
| 2 | Null-Scribe: "Your ascent is… under revision." |
| 3 | Phase 1 begins with Renewal (always same for learnability) |
| 4 | Edict swaps on timer + on phase thresholds |
| 5 | On defeat: hazards shut off, chest spawns, return gate unlocks |

---

## J) Rewards (Captain Door — Floor 85)

| Reward | Amount |
|--------|--------|
| **Tower Tokens** | +18 |
| **Duckets** | +180k–220k |
| **Tier 5 mats** | 5 rolls from Composite/Eclipse pool (higher Shadow/Time weighting) |
| **Gear** | 1 extra Tier 5 roll (Captain bonus, anti-dispel/DoT-resist affix bias) |

### Flag

| Flag | Condition |
|------|-----------|
| `TOWER_CAPTAIN_F85_DEFEATED` | TRUE |

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
    │         Console A               │
    │         (28,10)                 │
    │            │                    │
    │    Plinth NW    Plinth NE       │
    │    (16,16)      (40,16)         │
    │       │            │            │
    │ Console B   SEAL    Console C   │
    │ (10,26)   (28,28)   (46,26)     │
    │       │            │            │
    │    Plinth SW    Plinth SE       │
    │    (16,32)      (40,32)         │
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

ROTATING EDICTS (Cycle):
├─ EDICT OF RENEWAL → EDICT OF NULL → EDICT OF WOUNDS → (loop)
├─ P1: Swap every 18s
├─ P2+: Swap every 15s
└─ Telegraph: 1.2s page turn

EDICT EFFECTS:
├─ RENEWAL: 8% regen/turn, Renewal Glyphs every 12s
├─ NULL: Strip 1 buff/turn, Null Pulse every 14s
└─ WOUNDS: WOUND stacks (bleed at 4), Blood Script every 16s

EDICT CONSOLES (3):
├─ A(28,10), B(10,26), C(46,26)
├─ Counter-Clause: 10s, -70% current Edict, EXPOSED (+damage, 8s)
└─ Cooldown: 22s each

REDACTION SEAL (28,28):
├─ Channel: 2.0s, Cooldown: 35s
├─ Window: 8s, no adds, +party damage
└─ Cost: Ink Burn (DoT, 10s)

GLOBAL HAZARDS:
├─ Ledger Lines: Every 12s, 2 lanes
└─ Footnote Mines: Every 18s (P2+), 6s active

PHASE SUMMARY:
P1 (100–60%): First Draft — 18s swaps, no drones
P2 (60–25%): Second Draft — 15s swaps, Errata Drones, Footnote Mines
P3 (25–0%): Final Redaction — Redaction Order at 25%, hot periods post-swap
```
