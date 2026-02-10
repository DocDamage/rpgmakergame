# Chroma's Edge — Final Palace: Floor 4 Boss Arena Sheet (v1)
## Ancient Drake — Flight/Ground + Gold Farm ("Gilded Wyrm")

---

## 0) Technical Specs

| Parameter | Value |
|-----------|-------|
| **Boss** | Ancient Drake ("Gilded Wyrm") |
| **Floor** | F4 (Final Palace) |
| **Recommended Level** | 200–230 |
| **Fight Identity** | Break air phase with ballistas/harpoons, earn gold by taking risks, punish on ground with clean telegraphs |
| **Design Goal** | Replayable farm that's profitable but not abusable, still feels like a legit boss |
| **Arena Size** | 112 × 72 tiles (1792 × 1152 px) |
| **Type** | Boss arena + short prep hall + post-clear terminal |
| **Encounters** | OFF (boss only) |
| **Mounts** | Disabled |
| **Retry Point** | F4 Sanctuary Terminal |
| **Replay toggle** | Optional "Rematch" on terminal after clear (gold farm loop) |

---

## 1) Layout Overview

### 1) Prep Hall

| Property | Value |
|----------|-------|
| **Bounds** | x 0–112, y 60–72 |
| **Features** | Safe pad + "Gilded Drake" plaque + optional 1-time prep crate |

### 2) Main Arena (Gilded Basin)

| Property | Value |
|----------|-------|
| **Bounds** | x 8–104, y 10–60 |
| **Layout** | Wide arena with 2 Harpoon Ballistas, 2 Anchor Chain Posts, 2 Treasure Vents, 4 Cover Ruins |

### 3) Post-Clear Terminal Nook

| Property | Value |
|----------|-------|
| **Bounds** | x 44–68, y 0–10 |
| **Features** | Sanctuary Terminal + elevator to Floor 5 |

---

## 2) Anchors & Coordinates (Local 0–111, 0–71)

### Entry / Lock

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Party spawn** | (56, 66) | — |
| **Arena threshold** | y = 60 | Crossing to y≤59 locks doors |
| **Door lock trigger** | (56, 59) | — |

### Boss Positions

| Phase | Position | Notes |
|-------|----------|-------|
| **Air phase center pass** | (56, 26) | Visual path midpoint |
| **Ground phase landing** | (56, 34) | — |

### Harpoon Ballistas (Primary Counterplay, 2)

| Ballista | Coordinates |
|----------|-------------|
| **Ballista L** | (20, 52) |
| **Ballista R** | (92, 52) |

### Anchor Chain Posts (Optional Extra Counterplay, 2)

| Post | Coordinates |
|------|-------------|
| **Chain Post L** | (20, 20) |
| **Chain Post R** | (92, 20) |

### Treasure Vents (Risk/Reward Zones, 2)

| Vent | Coordinates |
|------|-------------|
| **Vent N (hot zone)** | (56, 18) |
| **Vent S (hot zone)** | (56, 54) |

### Cover Ruins (3×3 Collision, 4)

| Ruin | Coordinates |
|------|-------------|
| **Ruin NW** | (32, 24) |
| **Ruin NE** | (80, 24) |
| **Ruin SW** | (32, 56) |
| **Ruin SE** | (80, 56) |

### Post-fight

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Sanctuary Terminal** | (56, 6) | — |
| **Lift tile to F5** | (56, 2) | — |

---

## 3) Core Systems

### A) Flight / Ground Cycle

| State | Description |
|-------|-------------|
| **Start** | Drake AIRBORNE |
| **Goal** | Build TETHER stacks using Ballistas |
| **Crash** | At 3 TETHER → forced CRASH LAND (Ground Window) |
| **Airborne limit** | Escape Lift after 60s airborne (soft enrage) |

### B) Ballistas (Primary Counterplay)

| Property | Value |
|----------|-------|
| **Interact time** | 1.4s |
| **Cooldown** | 18 seconds per ballista (independent) |
| **Effect (airborne only)** | TETHER +1, staggers flight pattern (reduces next lane speed) |
| **Misfire (grounded)** | Harmless, 8s cooldown |
| **Visual** | Ballista glows when Drake targetable in air |

### C) Anchor Chain Posts (Optional Skill)

| Property | Value |
|----------|-------|
| **Interact time** | 1.0s |
| **Cooldown** | 24 seconds |
| **Effect** | Chain Snare Zone (radius ~4 tiles, 10s) |
| **Trigger** | Drake crosses during dive → +1 TETHER (once per snare) |
| **Intent** | Skilled players shorten air phase (not required) |

### D) Gold Farm Hook — Gilded Scales

| Property | Value |
|----------|-------|
| **Spawn** | Every 12 seconds during AIR phase |
| **Max active** | 4 nodes at once |
| **Pickup time** | 0.7s |
| **Risk** | Spawn near edges and Treasure Vents (danger zones) |
| **Conversion** | Each node = +X Duckets + Gilded Craft Mat chance |
| **Expiration** | Nodes vanish when Drake crashes |

---

## 4) Arena Hazards (Exact Timings)

### AIR PHASE Hazards

#### Skyline Strafe

| Property | Value |
|----------|-------|
| **Frequency** | Every 10 seconds (P2: 9s, P3: chains) |
| **Pattern** | 1 of 3 lanes (north/mid/south) |
| **Telegraph** | 1.6s lane highlight + wind-up roar |
| **Effect** | Heavy damage + Burn |

#### Gilded Breath Cone

| Property | Value |
|----------|-------|
| **Frequency** | Every 18 seconds (P2: 16s) |
| **Targeting** | Largest cluster of party members |
| **Telegraph** | 1.8s cone outline + gold ember buildup |
| **Effect** | Damage + Greed Brand |

#### Talonsnap Dive

| Property | Value |
|----------|-------|
| **Frequency** | Every 22 seconds |
| **Targeting** | One target with circle |
| **Telegraph** | 2.0s target ring + shadow overhead |
| **Impact** | Big hit + leaves Scorch Scar tiles (6s) |

#### Greed Brand (Debuff)

| Property | Description |
|----------|-------------|
| **Source** | Gilded Breath |
| **Effect** | +Duckets payout if survive, +10% damage taken by Drake (stacking to 3) |
| **Cleanse** | Sanctuary Terminal post-fight; in-fight optional |

### GROUND PHASE Hazards

#### Crownfire Stomp

| Property | Value |
|----------|-------|
| **Frequency** | Every 12 seconds |
| **Telegraph** | 1.4s expanding circle from Drake |
| **Effect** | AOE damage + knockback |

#### Tail Carve

| Property | Value |
|----------|-------|
| **Frequency** | Every 10 seconds |
| **Pattern** | 180° sweep behind Drake |
| **Telegraph** | 1.0s tail glow + arc indicator |
| **Effect** | Heavy damage + brief stagger |

#### Goldburst Eruption (Treasure Vent Synergy)

| Property | Value |
|----------|-------|
| **Frequency** | Every 16 seconds |
| **Pattern** | One vent erupts (alternates N/S) |
| **Telegraph** | 1.6s vent glow + rumble |
| **Effect** | Eruption line + falling coins, standing near = bonus Scale Nodes next AIR phase but chip damage now |

---

## 5) Boss Moveset

### AIR PHASE Attacks

| Attack | Description | Telegraph |
|--------|-------------|-----------|
| **Royal Strafe** | Skyline Strafe | 1.6s lane + roar |
| **Giltflame Exhale** | Gilded Breath Cone | 1.8s cone + embers |
| **Talonsnap Descent** | Dive | 2.0s ring + shadow |

### GROUND PHASE Attacks

| Attack | Description | Telegraph |
|--------|-------------|-----------|
| **Crownfire Stomp** | AOE stomp | 1.4s expanding circle |
| **Regal Tail Carve** | Tail sweep | 1.0s glow + arc |
| **Molten Hoard** | Targets vent, triggers Goldburst | 1.6s vent glow |

### Passive: Hoard Instinct

| Trigger | Effect |
|---------|--------|
| **3+ Scale Nodes in single AIR phase** | Hoard Rage for next ground window: +10% damage, +speed |

---

## 6) Phase Script (HP-Based + Mechanic-Based)

### Phase 1 (100% → 70%) — "First Flight"

| Aspect | Description |
|--------|-------------|
| **Start** | Drake airborne |
| **Hazards** | Strafe + Breath + Dive |
| **Scales** | Every 12s (max 4) |
| **Crash** | 3 TETHER → forced landing |

### Phase 2 (70% → 40%) — "Gilded Fury"

| Aspect | Description |
|--------|-------------|
| **Strafe** | Every 9s (was 10s) |
| **Breath** | Every 16s (was 18s) |
| **Ground** | Two stomps per cycle |
| **Special** | First crash drops Hoard Cache (boosts Duckets, adds Hoard Rage) |

### Phase 3 (40% → 0%) — "Ancient Wrath"

| Aspect | Description |
|--------|-------------|
| **Cycle** | Faster air/ground alternation |
| **Takeoff** | After 25s grounded unless damage pushed |
| **New move** | **Wingbreak Quake**: 2.2s wing flare, two shockwave rings + scorch scars |
| **Soft enrage** | >6 minutes: chains Breath → Dive more frequently |

---

## 7) Crash Landing Window (DPS Moment)

| Trigger | Effect |
|---------|--------|
| **TETHER reaches 3** | Telegraph: chain snap SFX + wobble (1.0s) |
| **Landing** | (56, 34) |
| **GROUNDED debuff** | +20% damage taken (18 seconds), no Strafe/Breath/Dive |
| **Lift Off attempt** | After 18s: 2.0s wing beat + dust spiral telegraph |
| **Interrupt** | Optional: extend grounded by 6s |

---

## 8) Fight Scripting (Sequence)

| Step | Event |
|------|-------|
| 1 | Cross threshold → doors lock |
| 2 | Drake roar; AIR Phase begins |
| 3 | Ballistas glow when targetable; scale nodes begin spawning |
| 4 | Tether to 3 → crash → Ground window |
| 5 | Repeat until HP thresholds push phase changes |
| 6 | On defeat: hazards stop, payout calculated, terminal nook unlocks, F5 elevator activates |

---

## 9) Rewards + Gold Farm Payout

### Base Clear Reward (Always)

| Reward | Details |
|--------|---------|
| **Duckets** | Endgame amount |
| **Materials** | Legendary mat bundle |
| **Gear** | 1 premium Tier 5 roll |
| **Flag** | `FINAL_PALACE_F4_CLEARED = TRUE` |

### Gold Farm Payout (Risk-Scaled)

| Component | Formula |
|-----------|---------|
| **Base Duckets** | Fixed endgame amount |
| **Scale Bonus** | (# Nodes) × (2% of Base), cap +40% (20 nodes max) |
| **Greed Brand Bonus** | +5% per stack at victory, cap 3 = +15% |
| **Hoard Rage Tradeoff** | +10% payout but Drake damage was higher |

### Optional Rare Drop (Replay Value)

| Drop | Details |
|------|---------|
| **Gilded Scale Fragment** | Craft mat |
| **Guaranteed** | 1 on clear |
| **Bonus** | +1 per 5 nodes collected (cap +3) |

---

## 10) Implementation Notes (Fun Farming)

| Rule | Implementation |
|------|----------------|
| **Scale pickups** | Fast (0.7s), clearly audible |
| **Ballista ready** | Obvious (glow + clang) |
| **Node spawning** | Never inside unavoidable lane strikes |
| **Farming design** | More scales = more danger (Hoard Rage + vent risk) |

---

## Quick Reference: Phase Summary

```
ANCIENT DRAKE — FLIGHT/GROUND + GOLD FARM

PHASE 1 (100% → 70%): FIRST FLIGHT
├─ Start: Airborne
├─ Hazards: Strafe (10s), Breath (18s), Dive (22s)
├─ Scales: Every 12s (max 4)
└─ Crash: 3 TETHER → Grounded (+20% damage, 18s)

PHASE 2 (70% → 40%): GILDED FURY
├─ Strafe: Every 9s (faster)
├─ Breath: Every 16s (faster)
├─ Ground: Two stomps per cycle
└─ Special: First crash drops Hoard Cache (+Duckets, +Rage)

PHASE 3 (40% → 0%): ANCIENT WRATH
├─ Cycle: Faster air/ground alternation
├─ Takeoff: After 25s grounded (unless damage pushed)
├─ New: Wingbreak Quake (2.2s wing flare, dual rings)
└─ Soft enrage: >6 minutes chains Breath→Dive

BALLISTAS (2):
├─ L(20,52), R(92,52)
├─ Interact: 1.4s, Cooldown: 18s each
├─ Effect: TETHER +1, staggers flight pattern
└─ Misfire (grounded): 8s cooldown

CHAIN POSTS (2) [Optional]:
├─ L(20,20), R(92,20)
├─ Interact: 1.0s, Cooldown: 24s
└─ Effect: Chain Snare Zone (10s), Drake crossing = +1 TETHER

TREASURE VENTS (2):
├─ N(56,18), S(56,54)
├─ Goldburst Eruption: Every 16s (alternates)
├─ Effect: Chip damage now, bonus Scale spawns next AIR phase
└─ Telegraph: 1.6s glow + rumble

GILDED SCALES:
├─ Spawn: Every 12s during AIR (max 4 active)
├─ Pickup: 0.7s
├─ Risk: Near edges and vents
├─ Payout: +2% Base Duckets per node (cap 20 nodes = +40%)
└─ Vanish: On Drake crash

GREED BRAND:
├─ Source: Gilded Breath
├─ Effect: +Duckets payout, +10% damage taken (stack to 3)
└─ Cleanse: Post-fight or optional Font

HOARD RAGE:
├─ Trigger: 3+ Scales in single AIR phase
├─ Effect: +10% Drake damage/speed next ground window
└─ Tradeoff: +10% Duckets payout

GROUNDBREAK QUAKES:
├─ Phase 3 only
├─ Telegraph: 2.2s wing flare
└─ Effect: Dual shockwave rings + scorch scars
```
