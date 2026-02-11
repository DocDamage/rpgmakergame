# Chroma's Edge — Aurora Ascension Tower: Floor 50 Boss Arena Sheet (v1)
## High Cultist Mercer — Pre-Triumvirate ("The Foundation Choir")

---

## 0) Technical Specs

| Parameter | Value |
|-----------|-------|
| **Boss** | High Cultist Mercer |
| **Identity** | Pre-Triumvirate — "The Foundation Choir" |
| **Stratum** | 41–60 (Motion/Mass/Time lead-in; Mercer uses ALL Foundations chaotically) |
| **Recommended Level** | 145–170 |
| **Arena Goal** | Test mastery of mechanic recognition + counterplay (without becoming RNG sludge) |
| **Arena Size** | 88 × 72 tiles (1408 × 1152 px) |
| **Type** | Boss arena + prep hall + reward alcove |
| **Encounters** | OFF (boss only) |
| **Mounts** | Disabled |
| **Retry Point** | Floor 40 terminal |

---

## 1) Layout Overview

### 1) Prep Hall (Entry Buffer)

| Property | Value |
|----------|-------|
| **Bounds** | x 0–88, y 60–72 |
| **Features** | Safe pad + "Floor 50 milestone" warning plaque + optional 1-time prep crate |

### 2) Main Arena (Ritual Bowl)

| Property | Value |
|----------|-------|
| **Bounds** | x 8–80, y 12–60 |
| **Layout** | Circular ritual floor with 8 Foundation Obelisks, 2 Cleanse Fonts, Ritual Dial center |

### 3) Reward Alcove (Post-Fight)

| Property | Value |
|----------|-------|
| **Bounds** | x 28–60, y 0–12 |
| **Features** | Ultimate weapon chest + lift tile to Floor 51 |

---

## 2) Anchors & Coordinates (Local 0–87, 0–71)

### Entry / Lock

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Entry spawn** | (44, 68) | — |
| **Arena threshold** | y = 60 | Crossing to y≤59 locks doors |
| **Door lock trigger** | (44, 59) | — |

### Boss Spawn

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Mercer spawn** | (44, 34) | Center |

### Centerpiece

| Feature | Coordinates | Function |
|---------|-------------|----------|
| **Ritual Dial** (phase indicator / interrupt) | (44, 44) | Shows active Foundation(s) |

### Foundation Obelisks (8 Total — Counterplay)

| Obelisk | Coordinates | Counters |
|---------|-------------|----------|
| **HEAT** | (44, 14) | Heat hazards |
| **TIDE** | (70, 22) | Tide currents |
| **GROWTH** | (74, 44) | Growth vines |
| **LIGHT** | (60, 56) | Light prisms |
| **MOTION** | (28, 56) | Motion conveyors |
| **MASS** | (14, 44) | Mass gravity wells |
| **TIME** | (18, 22) | Time flicker |
| **SHADOW** | (44, 58) | Shadow veil |

### Cleanse Fonts (Status Relief)

| Font | Coordinates | Effect |
|------|-------------|--------|
| **Font A** | (26, 34) | Remove 1 debuff + 8s resist to status waves |
| **Font B** | (62, 34) | Remove 1 debuff + 8s resist to status waves |

*Note: Shadow Foundation temporarily disables fonts.*

### Post-Fight Rewards

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Milestone chest (Ultimate)** | (44, 6) | Ultimate weapon for random character |
| **Lift tile to Floor 51** | (44, 2) | — |

---

## 3) Arena Systems

### A) Foundation Roulette (Mercer's Core Gimmick)

| Aspect | Description |
|--------|-------------|
| **Activation** | 1 Foundation (P1), 2 Foundations (P2), 3 Foundations (P3) |
| **Display** | Ritual Dial shows current Foundation(s) — icon + color + audio sting |
| **Rotation** | Every 2 turns |
| **Hazard** | Each active Foundation spawns matching hazard pattern |

### B) Obelisk Counterfields (Player Agency)

| Property | Value |
|----------|-------|
| **Interact time** | 1.0s |
| **Effect** | Counterfield for 12 seconds |
| **Counterfield effects** | -70% Foundation hazard damage, applies Dissonance to Mercer (+damage taken / buff loss / regen reduced) |
| **Cooldown** | 25 seconds per obelisk (independent) |

### C) Cleanse Fonts (Anti-RNG Brick)

| Property | Value |
|----------|-------|
| **Effect** | Remove 1 debuff + 8 seconds minor resist to random status waves |
| **Cooldown** | 18 seconds per font |
| **Shadow disable** | Fonts disabled while Shadow Foundation active |

---

## 4) Hazard Library (Foundation → Effect)

| Foundation | Hazard | Telegraph | Effect |
|------------|--------|-----------|--------|
| **HEAT** | Cauterize Lines | Glowing lane lines | 2–3 sweeping beams, Overheat buildup |
| **TIDE** | Pressure Current | Flowing glyph arrows | Gentle push current, forced 1-tile drift/2s |
| **GROWTH** | Vinebind Blooms | Green circles | Root tiles pop up, snare + Mercer heals extra |
| **LIGHT** | Prism Verdict | Rotating safe wedge | Outside wedge = chip + Blind buildup |
| **MOTION** | Conveyor Hymn | Motion arrows | Forced movement, enemies gain initiative |
| **MASS** | Gravity Wells | Dark rings | Pull toward center, slow, center hurts more |
| **TIME** | Flicker Slabs | Shimmer tiles | Tiles blink out, stepping on blank = stun/delay |
| **SHADOW** | Veil Ring | Shadow patches | Reduced accuracy/visibility, faster Echo Copies |

---

## 5) Mercer Kit (Boss Moveset)

### Passive: "The Choir" (Illusion Copies)

| Property | Description |
|----------|-------------|
| **Copies** | Take reduced damage; only real Mercer takes full damage |
| **Tell: Truth Glint** | Real Mercer has subtle glow flicker on hands/eyes (stronger with LIGHT Counterfield) |

---

## 6) Phases (HP-Based)

### Phase 1 (100% → 70%) — "Sermon of One"

| Aspect | Description |
|--------|-------------|
| **Roulette** | 1 Foundation active (rotates every 2 turns) |
| **Copies** | 1 illusion copy (max 1) |
| **Add cap** | 2 |

#### Moves

| Move | Description |
|------|-------------|
| **Foundation Hymn** | Activates current Foundation hazard |
| **Censure Bolt** | Single target, mild debuff |
| **Summon Acolyte** | Every other turn |

**Lesson:** Read dial → hit matching obelisk → stabilize.

### Phase 2 (70% → 40%) — "Sermon of Two"

| Aspect | Description |
|--------|-------------|
| **Roulette** | 2 Foundations active at once (rotates every 2 turns) |
| **Copies** | 2 illusion copies (max 2) |
| **Add cap** | 4 |

#### Moves

| Move | Description |
|------|-------------|
| **Doctrine Surge** | Random status wave (telegraphed) |
| **Choir Command** | Buffs adds/copies |
| **Seal of Denial** | Locks 1 random obelisk for 10s (telegraphed!) |

**Pressure:** Overlaps become real; cleanse fonts matter.

### Phase 3 (40% → 0%) — "Eclipse Litany"

| Aspect | Description |
|--------|-------------|
| **Roulette** | 3 Foundations active at once (rotates every 2 turns) |
| **Copies** | 3 illusion copies (max 3) |
| **Add cap** | 6 |

#### New Moves

| Move | Description |
|------|-------------|
| **Triune Invocation** | Big overlap burst (strongest telegraph) |
| **Absence Step** | Mercer swaps places with a copy |
| **Final Canticle** (≤15%) | Short enrage: faster rotation + heavier chip |

**Key rule:** Counter 2 of 3 Foundations with obelisks = manageable.

---

## 7) Optional Interaction: Ritual Dial Interrupt

| Property | Value |
|----------|-------|
| **Location** | (44, 44) |
| **Channel time** | 2.0s |
| **Effect** | Cancels next Roulette rotation (holds current foundations 1 extra turn), applies Dissonance to Mercer |
| **Cooldown** | 30s |
| **Risk** | Channel point exposed during hazards |

*Note: If keeping simpler, cut this—obelisk counterplay carries the design.*

---

## 8) Adds (Capped, Clean)

| Add | Description |
|-----|-------------|
| **Acolyte of Mercer** | Low HP, small debuffs |
| **Foundation Wisp** | Phase 2+, tied to active Foundation |
| **Total cap** | 6 bodies on field (including illusions) |
| **Replacement** | When cap reached, new spawns replace oldest add (not copies) |

---

## 9) Fight Scripting (Sequence)

| Step | Event |
|------|-------|
| 1 | Player crosses threshold → doors lock |
| 2 | Mercer appears: "The Foundations will witness your ascent." |
| 3 | Ritual Dial lights Phase 1 Foundation |
| 4 | Rotate foundations every 2 turns |
| 5 | Phase transitions at 70% and 40% (quick VFX) |
| 6 | On defeat: hazards stop, copies vanish, alcove unlocks, chest spawns, lift activates |

---

## 10) Rewards (Floor 50 Milestone)

### Mandatory Clear Rewards

| Reward | Details |
|--------|---------|
| **Milestone Chest (Ultimate Weapon)** | Ultimate weapon for random character |
| **Tier 5 Rare Equipment** | 1 piece |
| **Tower Tokens** | +30 |
| **Duckets** | +140,000–180,000 |
| **Rare Mats** | 4 rolls from Composite Foundation pool |

### Bonus Challenge

| Condition | Bonus |
|-----------|-------|
| Activate 3 different Obelisks in single rotation window | +10 tokens OR +1 extra mat roll |

---

## 11) Flags

| Flag | Condition |
|------|-----------|
| `TOWER_F50_CLEARED` | TRUE |
| `TOWER_BOSS_50_DEFEATED` | TRUE |
| `TOWER_ULTIMATE_WEAPON_GRANTED` | TRUE |
| `TOWER_LAST_REACHED_FLOOR` | 50 |

---

## 12) Implementation Notes

| Note | Priority |
|------|----------|
| Roulette icons BIG and audible (fight dies if state unreadable) | Critical |
| Hazards telegraphed separately (never stack invisibly) | High |
| Illusion copies visually distinct (outline/opacity/wrong shadow) | High |
| Random status waves telegraphed and cleansable | High |

---

## Quick Reference: Arena at a Glance

```
    NORTH (y=0, Reward Alcove)
       ↑
    ┌─────────────────────────────────────────────────────┐
    │  Reward Alcove (y 0–12)                             │
    │  - Ultimate Chest (44,6)                            │
    │  - Lift to F51 (44,2)                               │
    └─────────────────────────────────────────────────────┘
                      │
    ══════════════════╪════════════════════════════════════
                      │
    ┌─────────────────────────────────────────────────────┐
    │  Main Arena (y 12–60) — Ritual Bowl                 │
    │                                                     │
    │              HEAT Obelisk                           │
    │              (44,14)                                │
    │                   │                                 │
    │  TIME    TIDE     │     TIDE     GROWTH             │
    │  (18,22) (70,22)  │     (70,22)  (74,44)            │
    │       │      │    │    │      │                     │
    │       └─── MERCER (44,34) ────┘                     │
    │              │                                      │
    │         Ritual Dial (44,44)                         │
    │              │                                      │
    │  MASS    MOTION   │   LIGHT    GROWTH               │
    │  (14,44) (28,56)  │   (60,56)  (74,44)              │
    │       │      │    │    │      │                     │
    │       └─── SHADOW (44,58) ────┘                     │
    │              │                                      │
    │  Font A (26,34)    Font B (62,34)                   │
    │                                                     │
    └─────────────────────────────────────────────────────┘
                      │
    ══════════════════╪════════════════════════════════════ (y=60)
                      │
    ┌─────────────────────────────────────────────────────┐
    │  Prep Hall (y 60–72)                                │
    │  - Entry spawn (44,68)                              │
    │  - Lock trigger (44,59)                             │
    │  - Safe pad + prep crate                            │
    └─────────────────────────────────────────────────────┘
                      │
                   SOUTH (y=71, Entry)

PHASE SUMMARY:
P1 (100–70%): Sermon of One — 1 Foundation, 1 copy, teach obelisks
P2 (70–40%): Sermon of Two — 2 Foundations, 2 copies, overlaps begin
P3 (40–0%): Eclipse Litany — 3 Foundations, 3 copies, Triune Invocation

KEY MECHANICS:
- Ritual Dial shows active Foundation(s) clearly
- Matching Obelisk creates Counterfield (-70% hazard, Dissonance on Mercer)
- Cleanse Fonts remove debuffs (disabled by Shadow)
- Cap: 6 total bodies (adds + illusions)
- Truth Glint reveals real Mercer
```
