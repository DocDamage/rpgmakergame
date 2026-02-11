# Chroma's Edge — Aurora Ascension Tower: Floor 90 Boss Arena Sheet (v1)
## The Void Architect — Apex Shadow Construct ("Blueprint of Nothing")

---

## 0) Technical Specs

| Parameter | Value |
|-----------|-------|
| **Boss** | The Void Architect |
| **Identity** | Apex Shadow Construct — "Blueprint of Nothing" |
| **Stratum** | 81–100 (Eclipse) |
| **Recommended Level** | 200–230 |
| **Arena Goal** | Pre-final exam. Punishes sloppy buff-stacking; forces pin windows + hazard routing |
| **Arena Size** | 96 × 80 tiles (1536 × 1280 px) |
| **Type** | Boss arena + prep hall + reward alcove |
| **Encounters** | OFF (boss only) |
| **Mounts** | Disabled |
| **Retry Point** | Floor 80 terminal (next save at Floor 100) |

---

## 1) Layout Overview

### 1) Prep Hall (Entry Buffer)

| Property | Value |
|----------|-------|
| **Bounds** | x 0–96, y 68–80 |
| **Features** | Safe pad + warning plaque ("Buffs will be erased.") + optional 1-time prep crate |

### 2) Main Arena (Seam Foundry)

| Property | Value |
|----------|-------|
| **Bounds** | x 10–86, y 12–68 |
| **Layout** | Big open rectangle with 4 Seam Stabilizers, 2 Null Fountains, 4 Cover Spires, Blueprint Dais center |

### 3) Reward Alcove (Post-Fight)

| Property | Value |
|----------|-------|
| **Bounds** | x 34–62, y 0–12 |
| **Features** | Chest + lift tile to Floor 91 |

---

## 2) Anchors & Coordinates (Local 0–95, 0–79)

### Entry / Lock

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Entry spawn** | (48, 76) | — |
| **Arena threshold** | y = 68 | Crossing to y≤67 locks doors |
| **Door lock trigger** | (48, 67) | — |

### Boss Spawn

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Void Architect spawn** | (48, 38) | Center |

### Central Mechanic

| Feature | Coordinates | Function |
|---------|-------------|----------|
| **Blueprint Dais** (indicator + optional override) | (48, 48) | Shows active Blueprint icon(s) |

### Seam Stabilizers (Core Counterplay; 4 Total)

*Interactables that "pin" the boss into reality + stabilize hazards.*

| Stabilizer | Coordinates |
|------------|-------------|
| **Stabilizer N** | (48, 16) |
| **Stabilizer S** | (48, 64) |
| **Stabilizer W** | (16, 40) |
| **Stabilizer E** | (80, 40) |

### Null Fountains (Debuff Relief)

| Fountain | Coordinates |
|----------|-------------|
| **Fountain L** | (30, 30) |
| **Fountain R** | (66, 30) |

### Cover Spires (Line Blockers; 3×3 collision)

| Spire | Coordinates |
|-------|-------------|
| **Spire NW** | (28, 22) |
| **Spire NE** | (68, 22) |
| **Spire SW** | (28, 58) |
| **Spire SE** | (68, 58) |

### Post-fight

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Reward chest** | (48, 6) | — |
| **Lift tile to Floor 91** | (48, 2) | — |

---

## 3) Arena Systems

### A) Blueprint Cycle (Architect's "Mode")

| Blueprint | Effect |
|-----------|--------|
| **RIFT** | Pull + void seams |
| **ERASURE** | Buff strip + silence-like pressure |
| **PHASE** | Intangibility + blink lanes |

*Blueprint Dais displays active Blueprint icon(s) clearly.*

### B) Seam Stabilizers (Primary Counterplay)

| Property | Value |
|----------|-------|
| **Interact time** | 1.2s |
| **Effect** | Applies PINNED to boss for 10s (fully hittable; ends intangibility), reduces Blueprint hazard intensity 50% for 12s |
| **Cooldown** | 28 seconds per stabilizer (independent) |
| **Diminishing** | Re-using during PINNED refreshes only half duration |

### C) Null Fountains (Anti-Brick)

| Property | Value |
|----------|-------|
| **Effect** | Remove one heavy debuff (priority: Null Mark > Void Rot > Confounded) |
| **Secondary** | 8 seconds Dispel Dampening (buffs can't be removed more than once/turn) |
| **Cooldown** | 20 seconds per fountain |
| **PHASE restriction** | Disabled during PHASE Blueprint unless boss is PINNED |

---

## 4) Hazards (Telegraphed, Punishing, Never Cheap)

### Void Rifts (RIFT Blueprint)

| Property | Value |
|----------|-------|
| **Count** | 1–2 rifts as dark rings |
| **Effect** | Pull 1 tile every 2 seconds, Void Rot buildup + chip damage inside |
| **Telegraph** | Ring appears → center darkens → pull starts |

### Erasure Pulse (ERASURE Blueprint)

| Property | Value |
|----------|-------|
| **Pattern** | Periodic wave from boss that strips buffs |
| **Telegraph** | Boss "writes" bright line in air → pulse expands |
| **Counter** | Hide behind Cover Spires or stand in Stabilizer's "stabilized lane" |

### Phase Lanes (PHASE Blueprint)

| Property | Value |
|----------|-------|
| **Count** | 2–3 lane strips blink off |
| **Effect** | End turn on "blank" tile = Turn Delay |
| **Telegraph** | Shimmer → flicker → blank |

---

## 5) Boss Kit — The Void Architect

### Passive: Auto-Dispersion

| Condition | Effect |
|-----------|--------|
| **Normal** | Start of Architect's turn: removes 1 buff from each party member (strongest first) |
| **PINNED** | 50% chance instead |

### Passive: Intangible Draft

| Condition | Effect |
|-----------|--------|
| **PHASE Blueprint** | Architect becomes INTANGIBLE (0/near-0 damage taken) |
| **Stabilizer use** | INTANGIBLE ends immediately |

### Debuff: Null Mark

| Property | Description |
|----------|-------------|
| **Source** | Several attacks |
| **Effect** | Next buff target receives is immediately erased |
| **Cleansing** | Null Fountain priority target |

---

## 6) Phases (HP-Based)

### Phase 1 (100% → 70%) — "Drafting"

| Aspect | Description |
|--------|-------------|
| **Blueprint** | 1 active at a time; rotates every 2 turns |

#### Moves

| Move | Description |
|------|-------------|
| **Line Etch** | Straight beam; blocked by Cover Spires |
| **Null Stamp** | Single-target: Null Mark |
| **Rift Seed** | Spawns 1 rift during RIFT Blueprint |

**Lesson:** Use stabilizers for burst windows; use fountains when marked.

### Phase 2 (70% → 35%) — "Reconfiguration"

| Aspect | Description |
|--------|-------------|
| **Blueprint** | 2 active at once (rotates every 2 turns) |
| **Arena** | Rifts + erasure overlap |

#### New Moves

| Move | Description |
|------|-------------|
| **Architect's Rewrite** | Moves one Cover Spire 2–3 tiles, changing safe angles |
| **Erasure Pulse** | Core threat begins |
| **Phase Skew** | Teleports to corner, fires diagonal line |

**Pressure:** Stabilizers matter more.

### Phase 3 (35% → 0%) — "Final Schema"

| Aspect | Description |
|--------|-------------|
| **Blueprint** | 2 active constantly; every 3 turns, briefly activates 3rd ("Triple Draft") |
| **Enrage** | ≤15%: faster blueprint rotation, but PINNED lasts +2s |

#### New Moves

| Move | Description |
|------|-------------|
| **Blueprint Collapse** | Big telegraph; spawns 2 rifts + erasure wave |
| **Void Partition** | Temporary seam wall splits arena, forces route choice |
| **Verdict** (≤15%) | Short enrage with extended PINNED window |

**Win condition:** stabilize → pin → burst → rotate cleanses.

---

## 7) Optional Interaction: Blueprint Dais "Override"

| Property | Value |
|----------|-------|
| **Location** | (48, 48) |
| **Channel time** | 2.0s |
| **Effect** | Freeze current Blueprint rotation for 1 extra turn |
| **Requirement** | Only usable while boss is PINNED |
| **Cooldown** | 35s |

*Note: Optional high-skill play. Stabilizers + fountains already carry the fight.*

---

## 8) Fight Scripting (Sequence)

| Step | Event |
|------|-------|
| 1 | Cross threshold → doors lock |
| 2 | Boss spawns with "writing in air" animation |
| 3 | First Blueprint shown on dais (big icon + audio sting) |
| 4 | Phase transitions at 70% and 35% (geometry-shift VFX) |
| 5 | On defeat: hazards stop, rifts close, fountains reactivate, reward alcove unlocks |

---

## 9) Rewards (Floor 90 Milestone)

| Reward | Details |
|--------|---------|
| **Tier 5 Rare Equipment** | 1 piece, premium roll |
| **Unique Component** | Architect Prism-Core (anti-dispel / phase-resist craft mat) |
| **Tower Tokens** | +35 |
| **Duckets** | +170,000–200,000 |
| **Rare Mats** | 5 rolls from Eclipse pool (higher Shadow/Time weight) |

### Bonus Challenge

| Condition | Bonus |
|-----------|-------|
| Defeat with 0 party deaths and ≤3 total cleanses | +15 tokens OR 1 extra Tier-5 gear roll |

---

## 10) Flags

| Flag | Condition |
|------|-----------|
| `TOWER_F90_CLEARED` | TRUE |
| `TOWER_BOSS_90_DEFEATED` | TRUE |
| `TOWER_LAST_REACHED_FLOOR` | 90 |

---

## 11) Failure / Retry Behavior

| Condition | Result |
|-----------|--------|
| **Wipe** | Resume at Floor 80 terminal (or Tower Lobby → Resume Floor 80) |
| **Intro/tutorial** | Skippable after first attempt |

---

## 12) Implementation Notes (Hard But Fair)

| Note | Priority |
|------|----------|
| INTANGIBLE unmistakable (boss outline shifts; damage shows "0"/"IMMUNE") | Critical |
| Stabilizers have loud feedback: "PINNED" feels correct | Critical |
| Null Fountains mandatory due to auto-dispel (cooldown honest but not cruel) | High |
| Never spawn rifts directly under player; always offset 2–3 tiles with telegraph | High |

---

## Quick Reference: Arena at a Glance

```
    NORTH (y=0, Reward Alcove)
       ↑
    ┌─────────────────────────────────────────────────────┐
    │  Reward Alcove (y 0–12)                             │
    │  - Chest (48,6)                                     │
    │  - Lift to F91 (48,2)                               │
    └─────────────────────────────────────────────────────┘
                      │
    ══════════════════╪════════════════════════════════════
                      │
    ┌─────────────────────────────────────────────────────┐
    │  Main Arena (y 12–68) — Seam Foundry                │
    │                                                     │
    │         Stabilizer N                                │
    │         (48,16)                                     │
    │              │                                      │
    │  Cover NW    │    Cover NE                         │
    │  (28,22)     │    (68,22)                          │
    │              │                                      │
    │              │    Blueprint Dais                   │
    │  Stabilizer W│     (48,48)      Stabilizer E       │
    │  (16,40) ────┼──────────────── (80,40)             │
    │              │                                      │
    │  ────ARCHITECT (48,38)────                        │
    │              │                                      │
    │  Fountain L (30,30)      Fountain R (66,30)         │
    │              │                                      │
    │  Cover SW    │    Cover SE                         │
    │  (28,58)     │    (68,58)                          │
    │              │                                      │
    │         Stabilizer S                                │
    │         (48,64)                                     │
    │                                                     │
    └─────────────────────────────────────────────────────┘
                      │
    ══════════════════╪════════════════════════════════════ (y=68)
                      │
    ┌─────────────────────────────────────────────────────┐
    │  Prep Hall (y 68–80)                                │
    │  - Entry spawn (48,76)                              │
    │  - Lock trigger (48,67)                             │
    │  - Warning: "Buffs will be erased"                  │
    └─────────────────────────────────────────────────────┘
                      │
                   SOUTH (y=79, Entry)

BLUEPRINT SUMMARY:
┌─────────────┬──────────────────────────────────────────────┐
│ RIFT        │ Pull + void seams (dark rings)              │
│ ERASURE     │ Buff strip + Erasure Pulse wave             │
│ PHASE       │ INTANGIBLE + Phase Lanes (blink tiles)      │
└─────────────┴──────────────────────────────────────────────┘

PHASE PROGRESSION:
P1 (100–70%): Drafting — 1 Blueprint at a time, learn stabilizers
P2 (70–35%): Reconfiguration — 2 Blueprints active, Rewrite spires
P3 (35–0%): Final Schema — 2 constant + Triple Draft every 3 turns

KEY MECHANICS:
- Seam Stabilizer: 10s PINNED (ends intangibility, -50% hazard dmg)
- Auto-Dispersion: 1 buff stripped/turn (50% chance while PINNED)
- Null Fountain: Cleanse debuff + Dispel Dampening (8s)
- Cover Spires: Block Erasure Pulse during ERASURE Blueprint
- Never re-use stabilizer during PINNED (diminishing returns)
```
