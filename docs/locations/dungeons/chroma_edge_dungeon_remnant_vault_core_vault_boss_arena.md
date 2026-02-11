# Remnant Vault — Core Vault Boss Arena: The Remnant Custodian

## 1. Overview

| Attribute | Value |
|-----------|-------|
| **Boss Name** | The Remnant Custodian — "Stitchkeeper of the Leftover" |
| **Location** | Remnant Vault → Core Vault (end-of-run boss) |
| **Recommended Level** | Tier-scaled (T1–T10) |
| **Fight Identity** | Systems boss that echoes run modifiers; win by reading telegraphs, managing Integrity meter, using limited Stabilizers for burst + cast denial |
| **Arena Size** | 64 × 64 tiles |
| **Encounters** | OFF (boss only) |
| **Mounts** | Disabled |
| **Retry** | Ends run on wipe (standard vault run loop) |

---

## 2. Layout Overview

### Core Vault Chamber
Open square with two cover pylons (line blockers) and two single-use Stabilizers.

### Anchors & Coordinates (local 0–63, 0–63)

#### Entry / Flow

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Entry spawn | (32, 56) | Player entry point |
| Boss spawn | (32, 26) | Custodian appears here |
| **Reward cache** | (32, 10) | Post-victory loot |
| **Exit portal** | (32, 6) | Spawns after victory |

#### Cover Pylons (3×3 collision)

| Pylon | Coordinates | Purpose |
|-------|-------------|---------|
| **Pylon L** | (20, 24) | Line-of-sight blocker |
| **Pylon R** | (44, 24) | Line-of-sight blocker |

#### Boss-Room Stabilizers (single-use each)

| Stabilizer | Coordinates | Uses |
|------------|-------------|------|
| **Stabilizer L** | (16, 44) | 1 use |
| **Stabilizer R** | (48, 44) | 1 use |

---

## 3. Core Systems

### 1) Vault Integrity Meter (0–6 cracks)

| Mechanic | Details |
|----------|---------|
| **Gain +1** | When hit by signature hazard (Fault Lanes, Tear Rings, Collapse Ring) |
| **At 6 cracks** | Custodian casts CORE UNRAVEL on next action (telegraphed near-wipe) |
| **After Unravel resolves** | Integrity sets to 3 (can happen again, not instantly) |

### 2) Boss-Room Stabilizers (Win Lever)

| Property | Value |
|----------|-------|
| Interact time | 1.0s |
| Uses | 1 use each (2 total per run) |
| Effect | **STABILIZATION FIELD** (10s, radius ~6 tiles) |

#### Stabilization Field Effects

| Effect | Details |
|--------|---------|
| Hazard intensity | -70% |
| Custodian gains SYNCED | +30% damage taken (8s) |
| Integrity reduction | -2 immediately (min 0) |
| **CORE UNRAVEL cancel** | If charging: cancels it, STUNNED 2s, EXPOSED 10s (+20% damage taken) |

#### Rule
Only one Stabilization Field can be active at once.

### 3) Run Modifier Injection ("Echo Rules")

Custodian's **Echo Pulse** changes based on run modifiers:

| Run Modifier | Echo Pulse Effect |
|--------------|-------------------|
| **ECHO OF NULL** | Strips 1 buff |
| **ECHO OF STILLNESS** | Applies Stop/Slow-lite |
| **ECHO OF WEIGHT** | Pull/Heavy stacks |
| **ECHO OF VEIL** | Confound/accuracy down |
| **ECHO OF HEAT** | Overheat stacks |
| **ECHO OF FRACTURE** | Turn Delay if end on flicker tiles |

> Boss always feels "of your run," but base kit remains learnable.

---

## 4. Hazard Library

### 1) FAULT LANES (Two Lane Strikes)

| Property | Phase 1–2 | Phase 3 |
|----------|-----------|---------|
| **Frequency** | Every 12s | Every 10s |
| **Telegraph** | 1.4s thick split-lines | 1.4s thick split-lines |
| **Impact** | Heavy damage + Integrity +1 | Heavy damage + Integrity +1 |
| **Line-of-sight** | Blocked by Cover Pylons | Blocked by Cover Pylons |

### 2) TEAR RINGS (Pull Rifts)

| Property | Value |
|----------|-------|
| **Frequency** | Every 14s (Phase 2–3 only) |
| **Telegraph** | 1.6s dark rings + static hiss |
| **Active** | 8.0s |
| **Effect** | Pull 1 tile per 2s; if pulled at least once → Integrity +1 |

### 3) ECHO PULSE RING (Modifier-Powered)

| Property | Value |
|----------|-------|
| **Frequency** | Every 16s (all phases) |
| **Telegraph** | 1.6s expanding ring + "page-tear" SFX |
| **On hit** | Medium damage + Echo Effect (see Modifier table above) |

#### Echo Effects by Modifier

| Modifier | Effect |
|----------|--------|
| **NULL** | Strip 1 buff (max 1 per pulse) |
| **STILLNESS** | Stop-lite (short) or Slow if inside Stabilization Field |
| **WEIGHT** | Heavy +1 |
| **VEIL** | Confound-lite/accuracy down |
| **HEAT** | Overheat +2 |
| **FRACTURE** | Turn Delay +1 |

---

## 5. Custodian Moveset

### 1) STITCHHOOK (Single-Target Pull)

| Property | Value |
|----------|-------|
| **Telegraph** | 1.0s tether line + chain rattle |
| **Effect** | Pulls target 3 tiles toward center + minor damage |
| **Combo intent** | Sets up Fault Lanes |

### 2) LEDGER CLEAVE (Cone)

| Property | Value |
|----------|-------|
| **Telegraph** | 1.0s cone outline |
| **Effect** | Medium damage + small pushback 1 tile |

### 3) ERRATA SPAWN (Adds)

| Property | Value |
|----------|-------|
| **Telegraph** | 1.2s paper tear at arena edges |
| **Spawns** | 1 Errata Drone (cap 2) |

#### Drone Behaviors (Inherit Run Modifier)

| Modifier | Drone Behavior |
|----------|----------------|
| **Null** | Minor dispel poke |
| **Stillness** | Slow poke |
| **Weight** | Small pull poke |
| **Heat** | Overheat poke |
| **Veil** | Accuracy poke |
| **Fracture** | Turn delay poke |

### 4) REDACTION STAMP (Target Mark → Delayed Hit)

| Property | Value |
|----------|-------|
| **Telegraph** | 1.2s stamp icon under target |
| **Delay** | 2.0s |
| **Impact** | Burst damage; if hit → Integrity +1 |

### 5) CORE UNRAVEL (Signature Near-Wipe)

| Property | Value |
|----------|-------|
| **Trigger** | Integrity reaches 6 (next action); scripted at 20% HP (Phase 3) |
| **Telegraph** | 2.6s full-screen crack vignette + deep fracture sound |
| **If resolves** | Massive damage + applies primary Echo debuff (one stack) + Integrity set to 3 |
| **Counter** | Activate Stabilizer before cast completes → cancel + stun + exposed |

---

## 6. Phase Plan (HP-Based)

### Phase 1 — "Initial Stitch" (100% → 70%)

**Goal**: Teach readability and cover play

| Hazard/Move | Frequency |
|-------------|-----------|
| Fault Lanes | Every 12s |
| Echo Pulse | Every 16s |
| Tear Rings | ❌ None |
| Errata Spawn | ❌ None (unless 3+ modifiers) |

**Typical Rotation** (~24s loop):
```
Stitchhook → Ledger Cleave → Fault Lanes → Echo Pulse → Redaction Stamp
```

### Phase 2 — "Active Revision" (70% → 35%)

**Goal**: Introduce rifts + adds, keep it solvable

| Hazard/Move | Frequency |
|-------------|-----------|
| Tear Rings | Every 14s (NEW) |
| Errata Spawn | Every 20s (cap 2) |
| Fault Lanes | Every 12s |
| Echo Pulse | Every 16s |

**Pressure Rule**: If 2 drones alive, Custodian delays spawning more (no infinite add spam).

### Phase 3 — "Final Redaction" (35% → 0%)

**Goal**: Tight pacing, clean burst windows with Stabilizers

| Hazard/Move | Frequency |
|-------------|-----------|
| Fault Lanes | Every 10s (tightened) |
| Tear Rings | Every 12s (tightened) |
| Echo Pulse | Every 14s (tightened) |
| Errata Spawn | Every 18s (still cap 2) |

**Scripted Moment**: At 20% HP, Custodian forces CORE UNRAVEL once (even if Integrity < 6)
- Fully telegraphed
- Intended to be countered by remaining Stabilizer (if saved)

---

## 7. Encounter Scripting (Sequence)

| Step | Event |
|------|-------|
| 1 | Party enters → arena seals |
| 2 | Boss one-liner: *"Leftovers belong to the vault."* |
| 3 | Phase 1 begins (first Fault Lanes within 6s) |
| 4 | Phase shift at 70% (1.8s invuln, clears Tear Rings, keeps Integrity) |
| 5 | Phase shift at 35% (1.8s invuln, clears Tear Rings, keeps Integrity) |
| 6 | Scripted Unravel at 20% (if not already triggered) |
| 7 | Victory: hazards stop, reward cache unlocks, exit portal spawns |

---

## 8. Rewards (Boss Cache Delivery)

### Reward Cache UI
```
┌─────────────────────────┐
│      REMNANT CACHE      │
├─────────────────────────┤
│       [CLAIM]           │
└─────────────────────────┘
```

### Always (Deterministic)

| Reward | Details |
|--------|---------|
| **Remnant Shards** | Scaled by Tier |
| **Core Dust** | Fixed minimum by Tier; never bricks progress |
| **Vault Roll ×1** | Gear roll, quality scales |
| **Echo Sigil Fragment ×1** | Combine 5 → Echo Sigil |

### Bonus (Scaled by Tier)

| Tier | Bonus Rewards |
|------|---------------|
| **Tier 1–4** | 1 bonus mat roll |
| **Tier 5–7** | 2 bonus mat rolls + small chance at rare accessory |
| **Tier 8–10** | 3 bonus mat rolls + higher rare accessory chance + cosmetic/title token chance |

---

## 9. Quick Reference

### Arena Coordinates (64×64)
```
Entry Spawn: (32, 56)          Boss Spawn: (32, 26)
Reward Cache: (32, 10)         Exit Portal: (32, 6)

Cover Pylons:
  Pylon L: (20, 24)            Pylon R: (44, 24)

Stabilizers (single-use each):
  Stabilizer L: (16, 44)       Stabilizer R: (48, 44)
```

### Integrity System
```
Max: 6 cracks
Gain: Hit by Fault Lanes, Tear Rings, Redaction Stamp
At 6: CORE UNRAVEL casts
After Unravel: Reset to 3

Stabilizer Effect:
  - Integrity -2 (min 0)
  - Can cancel Unravel → Stun 2s + Exposed 10s
```

### Phase Thresholds
```
Phase 1: 100% → 70%
Phase 2: 70% → 35%
Phase 3: 35% → 0%
  Scripted Unravel at 20%
```

### Hazard Timing Summary

| Hazard | P1 | P2 | P3 |
|--------|----|----|----|
| Fault Lanes | 12s | 12s | 10s |
| Tear Rings | ❌ | 14s | 12s |
| Echo Pulse | 16s | 16s | 14s |
| Errata Spawn | ❌* | 20s | 18s |

*Unless 3+ modifiers active

---

## 10. Implementation Notes

- **Stabilizer balance**: Fight balanced around using at least one Stabilizer; saving second for 20% Unravel is "smart clear"
- **Cover pylons**: Give consistent way to handle lane pressure without pure DPS checks
- **Integrity loop**: Creates skill expression that feels earned, not RNG
- **Phase invulnerability**: 1.8s at 70% and 35%; clears Tear Rings but preserves Integrity
- **Drone cap**: Hard cap at 2 prevents add spam overwhelm
- **Modifier injection**: Only Echo Pulse changes; base moveset stays consistent for learnability
- **Unravel safety**: Always fully telegraphed (2.6s); sufficient time to react with Stabilizer
- **Tier scaling**: Higher tiers increase damage numbers and hazard frequency slightly, but core patterns remain
