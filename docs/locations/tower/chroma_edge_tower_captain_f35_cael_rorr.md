# Chroma's Edge — Tower Captain Arena: Floor 35 (v1)
## Prism Adjudicator Cael Rorr (Light) — "Refraction Verdict"

---

## 0) Technical Specs

| Parameter | Value |
|-----------|-------|
| **Captain** | Prism Adjudicator Cael Rorr |
| **Identity** | Light Captain — "Refraction Verdict" |
| **Tower Floor** | 35 (optional Captain Door room) |
| **Recommended Level** | 130–155 |
| **Fight Identity** | Visibility + target verification. Reveal true adjudicator, manage safe wedge, use Prism Beacons to collapse clones |
| **Arena Size** | 56 × 56 tiles (Template E: Arena + Prep Hall) |
| **Type** | Optional Captain Challenge arena (single fight) |
| **Encounters** | OFF (boss only) |
| **Mounts** | Disabled |
| **Retry behavior** | Standard Tower (resume at last save floor) |

---

## A) Access / Door Logic (on Floor 35)

### Captain Door Spawn Rule

| Property | Description |
|----------|-------------|
| **Appearance** | Side door on Floor 35, marked with white seal + prism icon |
| **Prompt** | "ENTER CAPTAIN CHALLENGE — PRISM ADJUDICATOR" |
| **Gating** | Once entered: cannot leave until win/lose |

---

## B) Layout Overview

### 1) Prep Hall (Safe)

| Property | Value |
|----------|-------|
| **Bounds** | x 0–56, y 44–56 |
| **Features** | "Ready" tile + optional one-time supply crate |

### 2) Arena Bowl (Prism Court)

| Property | Value |
|----------|-------|
| **Bounds** | x 6–50, y 6–44 |
| **Features** | 4 mirror plinths (line blockers/reflectors), 4 Prism Beacons (reveal tools), 1 central dial (phase cue) |

### 3) Reward Pad (Spawns After Win)

| Property | Value |
|----------|-------|
| **Location** | Just above prep hall |

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
| **Cael Rorr spawn** | (28, 22) | — |

### Mirror Plinths (3×3 Collision, Block/Redirect Beams)

| Plinth | Coordinates |
|--------|-------------|
| **NW** | (16, 16) |
| **NE** | (40, 16) |
| **SW** | (16, 32) |
| **SE** | (40, 32) |

### Prism Beacons (Counterplay, 4)

| Beacon | Coordinates |
|--------|-------------|
| **Beacon N** | (28, 10) |
| **Beacon W** | (10, 22) |
| **Beacon E** | (46, 22) |
| **Beacon S** | (28, 38) |

### Central "Verdict Dial" (Visual Cue Only)

| Feature | Coordinates |
|---------|-------------|
| **Dial tile** | (28, 28) |

### Reward Spawn

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Captain reward chest** | (28, 46) | After victory |
| **Return gate to Floor 35** | (28, 54) | After victory |

---

## D) Arena Systems

### 1) Refraction Clones (Core Mechanic)

| Property | Description |
|----------|-------------|
| **Creation** | Cael spawns Refraction Images (clones) |
| **Visuals** | Look real unless revealed |
| **Damage** | Clones take reduced damage (or "fake" damage numbers) |
| **Real Cael tell** | Faint "spectrum shimmer" (subtle), but intended solve is Beacons |

### 2) "Misjudgment" Penalty

| Trigger | Effect |
|---------|--------|
| **Hit only clones for 8 seconds** | Cael triggers **CONTEMPT FLASH** (once/cycle) |
| **Contempt Flash** | Small AOE damage + applies Dazzled (short accuracy down) |
| **Intent** | Nudges players toward beacon loop without hard-punishing |

### 3) Prism Beacons (Primary Counterplay)

| Property | Value |
|----------|-------|
| **Interact time** | 1.0s |
| **Cooldown** | 22 seconds per beacon (independent) |
| **Effect** | **TRUE SPECTRUM PULSE** for 8 seconds (radius ~5 tiles) |
| **Pulse effects** | Reveals real Cael (true outline + clear highlight), clones become BRITTLE (+damage / expire faster) |
| **Limit** | Only one beacon pulse active at once |

### 4) Prism Verdict Safe Wedge

| Property | Description |
|----------|-------------|
| **Function** | Rotating "safe wedge" pattern forces positioning |
| **Design** | Telegraphed cleanly, interacts with beacons |

---

## E) Hazard Timing (Exact)

### 1) Prism Verdict (Safe Wedge)

| Property | Value |
|----------|-------|
| **Cycle** | Every 12 seconds |
| **Telegraph** | 1.5s wedge outline + chime |
| **Active** | 8.0s |
| **Outside wedge** | Chip damage + Dazzled buildup (stacks to 3) |

### 2) Refraction Lines (Bounce Beams)

| Property | Value |
|----------|-------|
| **Frequency** | Every 14 seconds (P3: every 12s) |
| **Telegraph** | 1.3s thin line(s) appear |
| **Pattern** | 2 beams that reflect off Mirror Plinths (predictable angles) |
| **Hit effect** | Medium damage + Expose (minor) for 6s |

### 3) Glint Mines (Phase 2+)

| Property | Value |
|----------|-------|
| **Frequency** | Every 18 seconds |
| **Pattern** | 3 small circles |
| **Telegraph** | 1.2s bright dots |
| **Active** | 6.0s |
| **Step effect** | Short stagger + Dazzled +1 |

---

## F) Captain Moveset

### 1) Adjudication Ray (Primary Snipe)

| Property | Value |
|----------|-------|
| **Telegraph** | 0.9s straight aiming line + lens flare |
| **Effect** | Heavy single-target damage |
| **Block** | Blockable by Mirror Plinths |

### 2) Split Verdict (Clone Creation)

| Property | Value |
|----------|-------|
| **Telegraph** | 1.1s prism burst around Cael |
| **Effect** | Spawns 2 clones (P1), 3 clones (P2+) |
| **Duration** | Clones persist 12s base (shorter if BRITTLE) |

### 3) Prism Step (Reposition + Swap)

| Property | Value |
|----------|-------|
| **Telegraph** | 0.7s shimmer |
| **Effect** | Cael swaps places with a clone (or blinks to wedge edge) |

### 4) Censure Halo (AOE Ring)

| Property | Value |
|----------|-------|
| **Telegraph** | 1.0s expanding ring |
| **Effect** | Medium AOE; applies Dazzled +1 if hit |

### 5) Contempt Flash (Anti-Misjudgment Reaction)

| Property | Value |
|----------|-------|
| **Trigger** | 8s hitting only clones |
| **Telegraph** | 0.8s flash pop |
| **Effect** | Small AOE + Dazzled |

---

## G) Phases (HP-Based)

### Phase 1 (100% → 60%) — "Initial Hearing"

| Aspect | Description |
|--------|-------------|
| **Prism Verdict** | Normal cycle (12s) |
| **Refraction Lines** | Every 14s |
| **Clone pattern** | 2 clones per Split Verdict (every ~18s) |

### Phase 2 (60% → 25%) — "Appeal Denied"

| Aspect | Description |
|--------|-------------|
| **Prism Verdict** | 12s cycle, but wedge rotates faster during active window |
| **New hazard** | Glint Mines (every 18s) |
| **Clone pattern** | 3 clones |
| **Behavior** | Cael uses Prism Step more often to bait misjudgment |

### Phase 3 (25% → 0%) — "Final Sentence"

| Aspect | Description |
|--------|-------------|
| **One-time at 25%** | **SPECTRUM GAVEL** |
| **Refraction Lines** | Every 12s (was 14s) |
| **Beacons** | Remain fully effective |

#### SPECTRUM GAVEL

| Property | Value |
|----------|-------|
| **Telegraph** | 2.0s huge prism stamp on Dial tile (28,28) |
| **Effect** | Immediate Split Verdict + simultaneous Refraction Lines (still telegraphed) |

---

## H) Fight Scripting (Sequence)

| Step | Event |
|------|-------|
| 1 | Enter → doors lock |
| 2 | Cael: "Truth is a spectrum. You will be measured." |
| 3 | Prism Verdict begins within 6 seconds |
| 4 | Clones enter loop; Beacons teach the solve |
| 5 | Phase shifts at 60% and 25% with "prism chime" VFX |
| 6 | On defeat: hazards shut off, reward chest spawns, return gate unlocks |

---

## I) Rewards (Captain Door — Floor 35)

| Reward | Amount |
|--------|--------|
| **Tower Tokens** | +10 |
| **Duckets** | +90k–130k |
| **Tier 5 mats** | 3 rolls from Light/Prism pool |
| **Gear** | 1 extra Tier 5 roll (Captain bonus, Light-leaning affixes) |

### Flag

| Flag | Condition |
|------|-----------|
| `TOWER_CAPTAIN_F35_DEFEATED` | TRUE |

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
    │         Beacon N                │
    │         (28,10)                 │
    │            │                    │
    │    Plinth NW    Plinth NE       │
    │    (16,16)      (40,16)         │
    │       │            │            │
    │ Beacon W    DIAL    Beacon E    │
    │ (10,22)   (28,28)   (46,22)     │
    │       │            │            │
    │    Plinth SW    Plinth SE       │
    │    (16,32)      (40,32)         │
    │            │                    │
    │         Beacon S                │
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

REFRACTION CLONES:
├─ 2 clones (P1), 3 clones (P2+)
├─ Reduced damage taken
├─ Real Cael: faint spectrum shimmer
└─ Misjudgment (8s on clones): Contempt Flash (AOE + Dazzled)

PRISM BEACONS (4):
├─ N(28,10), W(10,22), E(46,22), S(28,38)
├─ Pulse: 8s, reveals real Cael, makes clones BRITTLE
└─ Cooldown: 22s each

PRISM VERDICT:
├─ Cycle: Every 12s
├─ Telegraph: 1.5s wedge outline
├─ Active: 8s
└─ Outside: Chip + Dazzled (stacks to 3)

REFRACTION LINES:
├─ Every 14s (P3: 12s)
├─ 2 beams, reflect off plinths
└─ Hit: Medium damage + Expose (6s)

GLINT MINES (P2+):
├─ Every 18s, 3 circles
├─ Telegraph: 1.2s dots
└─ Step: Stagger + Dazzled

PHASE SUMMARY:
P1 (100–60%): Initial Hearing — 2 clones, normal wedge
P2 (60–25%): Appeal Denied — 3 clones, faster wedge rotation, Glint Mines
P3 (25–0%): Final Sentence — Spectrum Gavel at 25%, faster Lines
```
