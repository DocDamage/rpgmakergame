# Chroma's Edge — Final Palace: Floor 5 Boss Arena Sheet (v1)
## The Progenitor Engine — 8-Phase Finale ("Origin Protocol")

---

## 0) Technical Specs

| Parameter | Value |
|-----------|-------|
| **Boss** | The Progenitor Engine |
| **Floor** | F5 (Final) |
| **Recommended Level** | 200–230 |
| **Fight Identity** | Eight distinct Foundation programs. Each phase short, readable, solvable via matching Foundation Conduit |
| **Core Threats** | Stacked hazards, debuff pressure, limited cleanses, Eclipse Override end segment |
| **Arena Size** | 128 × 88 tiles (2048 × 1408 px) |
| **Type** | Boss arena + short prep hall + post-clear reward sanctum/terminal |
| **Encounters** | OFF (boss only) |
| **Mounts** | Disabled |
| **Retry Point** | F5 Sanctuary Terminal |

---

## 1) Layout Overview

### 1) Prep Hall

| Property | Value |
|----------|-------|
| **Bounds** | x 0–128, y 76–88 |
| **Features** | Safe pad + "Origin Protocol" warning plaque + optional 1-time prep crate |

### 2) Main Arena (Engine Chamber)

| Property | Value |
|----------|-------|
| **Bounds** | x 8–120, y 10–76 |
| **Layout** | Central Engine Core + 8 Foundation Conduits on rim + 2 Sanctuary Fonts + 2 Cover Pylons |

### 3) Post-Clear Sanctum

| Property | Value |
|----------|-------|
| **Bounds** | x 40–88, y 0–10 |
| **Features** | Final rewards, terminal, exit/credits trigger |

---

## 2) Anchors & Coordinates (Local 0–127, 0–87)

### Entry / Lock

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Party spawn** | (64, 84) | — |
| **Arena threshold** | y = 76 | Crossing to y≤75 locks doors |
| **Door lock trigger** | (64, 75) | — |

### Boss Spawn

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Engine Core center** | (64, 44) | — |

### 8 Foundation Conduits (Counterplay)

| Conduit | Coordinates | Foundation | Phase |
|---------|-------------|------------|-------|
| **HEAT** | (64, 14) | Heat | 1 (100→87.5%) |
| **TIDE** | (92, 22) | Tide | 2 (87.5→75%) |
| **GROWTH** | (114, 44) | Growth | 3 (75→62.5%) |
| **LIGHT** | (92, 66) | Light | 4 (62.5→50%) |
| **MOTION** | (64, 74) | Motion | 5 (50→37.5%) |
| **MASS** | (36, 66) | Mass | 6 (37.5→25%) |
| **TIME** | (14, 44) | Time | 7 (25→12.5%) |
| **SHADOW** | (36, 22) | Shadow | 8 (12.5→0%) |

### Sanctuary Fonts (Limited)

| Font | Coordinates |
|------|-------------|
| **Font L** | (48, 44) |
| **Font R** | (80, 44) |

### Cover Pylons (Line Blockers; 3×3 Collision)

| Pylon | Coordinates |
|-------|-------------|
| **Pylon L** | (48, 28) |
| **Pylon R** | (80, 28) |

### Post-fight

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Reward terminal / chest cluster** | (64, 6) | — |
| **Exit/credits tile** | (64, 2) | — |

---

## 3) Core Systems

### A) 8-Phase HP Script (Exact Thresholds)

| Phase | Foundation | HP Range | Duration |
|-------|------------|----------|----------|
| **1** | HEAT | 100% → 87.5% | ~12.5% |
| **2** | TIDE | 87.5% → 75% | ~12.5% |
| **3** | GROWTH | 75% → 62.5% | ~12.5% |
| **4** | LIGHT | 62.5% → 50% | ~12.5% |
| **5** | MOTION | 50% → 37.5% | ~12.5% |
| **6** | MASS | 37.5% → 25% | ~12.5% |
| **7** | TIME | 25% → 12.5% | ~12.5% |
| **8** | SHADOW | 12.5% → 0% | ~12.5% |

**Phase Shift:** 2.5s invuln + clears old hazards (debuffs remain). Big icon stamp + audio sting.

### B) Foundation Conduits (Primary Counterplay)

| Property | Value |
|----------|-------|
| **Interact time** | 1.0s |
| **Cooldown** | 30 seconds per conduit (independent) |
| **Effect** | STABILIZATION FIELD for 10 seconds: -70% hazard intensity, SYNCED (+20% damage taken) |
| **Limit** | Only one Stabilization Field active at a time |
| **Wrong conduit** | "Miswire" (fizzle), locked 8s, no damage penalty |

### C) Sanctuary Fonts (Limited, Anti-Brick)

| Property | Value |
|----------|-------|
| **Effect** | Cleanse 1 major debuff + 8s Dispel Dampening (max 1 buff/turn) |
| **Cooldown** | 24 seconds |
| **Limit** | 3 uses total per font (entire fight) |

### D) Global Pressure: INSTABILITY

| Aspect | Description |
|--------|-------------|
| **Builds** | +1 when hit by phase signature hazard |
| **At 5 stacks** | Engine casts "Eclipse Pulse" + Instability resets to 0 |
| **Purpose** | Prevents "just heal through" sloppy play |

---

## 4) Global Boss Moves (All Phases)

### 1) Eclipse Pulse (Instability Punish)

| Property | Description |
|----------|-------------|
| **Telegraph** | 1.8s black-white strobe + bass hit |
| **Effect** | Medium party damage + phase-appropriate debuff (1 stack) |
| **Counter** | Inside active Stabilization Field = -60% damage |

### 2) Core Beam (Line Attack)

| Property | Description |
|----------|-------------|
| **Telegraph** | 1.2s thick line + rising whine |
| **Effect** | Heavy damage |
| **Block** | Cover Pylons block |

### 3) System Rewrite (Buff Pressure)

| Property | Description |
|----------|-------------|
| **Frequency** | Every 20 seconds |
| **Effect** | Removes 1 buff from each character (strongest) |
| **SYNCED** | Becomes 50% chance per character |

---

## 5) Phase-by-Phase Library

### PHASE 1 — HEAT (100% → 87.5%)

| Aspect | Description |
|--------|-------------|
| **Theme** | Burn lanes + Overheat |
| **Primary Debuff** | Overheat |

#### Hazards

| Hazard | Timing | Telegraph | Effect |
|--------|--------|-----------|--------|
| **Cauterize Rails** | Every 12s | 1.6s, active 3.0s | 2 lane beams |
| **Emberfield Patches** | Every 18s | 1.2s, active 6.0s | 3 circles |

#### Boss Attacks

| Attack | Timing | Telegraph | Effect |
|--------|--------|-----------|--------|
| **Forge Hammer** | Every 14s | 1.1s ring expansion | AOE + Overheat |
| **Core Beam** | Anti-cheese | — | Replaces Hammer if hug center |

#### Conduit Solve

HEAT conduit: reduces Overheat gain, shortens Emberfields by 2s.

---

### PHASE 2 — TIDE (87.5% → 75%)

| Aspect | Description |
|--------|-------------|
| **Theme** | Drift + pressure slams |
| **Primary Debuff** | Pressure |

#### Hazards

| Hazard | Timing | Telegraph | Effect |
|--------|--------|-----------|--------|
| **Current Shift** | Every 10s | 1.0s arrows, 8.0s | Drift 1 tile/2s |
| **Pressure Crush** | Every 16s | 1.8s, impact + 3s slow | 2 circles |

#### Boss Attacks

| Attack | Timing | Telegraph | Effect |
|--------|--------|-----------|--------|
| **Undertow Pull** | Every 18s | 1.2s swirl | Small pull + Pressure |

#### Conduit Solve

TIDE conduit: cancels drift entirely, halves Pressure stacks.

---

### PHASE 3 — GROWTH (75% → 62.5%)

| Aspect | Description |
|--------|-------------|
| **Theme** | Roots + regen nodes |
| **Primary Debuff** | Vinebind |

#### Hazards

| Hazard | Timing | Telegraph | Effect |
|--------|--------|-----------|--------|
| **Root Snare Bloom** | Every 9s | 1.3s | 2 targets, bind 2.5s |
| **Regrowth Node** | Every 18s | 1.0s pillar | +4% regen/turn per node (max 2) |

#### Boss Attacks

| Attack | Timing | Telegraph | Effect |
|--------|--------|-----------|--------|
| **Verdant Lance Fan** | Every 15s | 1.2s cracks | 3 spike lines |

#### Conduit Solve

GROWTH conduit: destroys active Regrowth Nodes, reduces bind duration.

---

### PHASE 4 — LIGHT (62.5% → 50%)

| Aspect | Description |
|--------|-------------|
| **Theme** | Prism safe wedge + flash |
| **Primary Debuff** | Blind-lite |

#### Hazards

| Hazard | Timing | Telegraph | Effect |
|--------|--------|-----------|--------|
| **Prism Verdict** | Every 12s | 1.5s, 8.0s | Safe wedge |
| **Flash Seal** | Every 18s | 1.0s flare | Blind-lite if outside wedge |

#### Boss Attacks

| Attack | Timing | Telegraph | Effect |
|--------|--------|-----------|--------|
| **Radiant Spear** | Every 10s | 0.7s | Fast line, heavy hit |

#### Conduit Solve

LIGHT conduit: expands safe wedge ~35%, reduces Blind buildup.

---

### PHASE 5 — MOTION (50% → 37.5%)

| Aspect | Description |
|--------|-------------|
| **Theme** | Conveyor strips + tempo pressure |
| **Primary Debuff** | Turn order disruption |

#### Hazards

| Hazard | Timing | Telegraph | Effect |
|--------|--------|-----------|--------|
| **Conveyor Hymn** | Every 14s | 1.2s arrows, 8.0s | 2 strips, forced 1 tile/2s |
| **Dash Gates** | Every 18s | 1.4s | 2 lanes, chip + turn delay |

#### Boss Attacks

| Attack | Timing | Telegraph | Effect |
|--------|--------|-----------|--------|
| **Vector Chop** | Every 16s | 1.0s line | Targeted dash, leaves 4s afterline |

#### Conduit Solve

MOTION conduit: reduces forced movement speed, prevents turn-delay from Dash Gates.

---

### PHASE 6 — MASS (37.5% → 25%)

| Aspect | Description |
|--------|-------------|
| **Theme** | Gravity wells + pull lanes |
| **Primary Debuff** | Heavy (slow), vulnerability in center |

#### Hazards

| Hazard | Timing | Telegraph | Effect |
|--------|--------|-----------|--------|
| **Gravity Wells** | Every 16s | 1.5s rings, 8.0s | Spawn 2, pull 1 tile/2s |
| **Compression Slam** | Every 20s | 2.0s rumble | Heavy damage near center |

#### Boss Attacks

| Attack | Timing | Telegraph | Effect |
|--------|--------|-----------|--------|
| **Anchor Breaker** | Every 14s | 0.9s | Single target, Heavy stack |

#### Conduit Solve

MASS conduit: reduces pull strength, shrinks dangerous center radius.

---

### PHASE 7 — TIME (25% → 12.5%)

| Aspect | Description |
|--------|-------------|
| **Theme** | Flicker tiles + turn delay |
| **Primary Debuff** | Turn delay |

#### Hazards

| Hazard | Timing | Telegraph | Effect |
|--------|--------|-----------|--------|
| **Flicker Slabs** | Every 12s | 1.4s shimmer, 5.0s | 8 tiles blank, Turn Delay if end turn on |
| **Lag Pulse Ring** | Every 16s | 1.4s expanding | Turn Delay if hit |

#### Boss Attacks

| Attack | Timing | Telegraph | Effect |
|--------|--------|-----------|--------|
| **Secondhand Cleave** | Every 10s | 0.9s | Small delay |

#### Conduit Solve

TIME conduit: "solidifies" flicker slabs inside field (safe tiles stay safe), halves delay.

---

### PHASE 8 — SHADOW (12.5% → 0%)

| Aspect | Description |
|--------|-------------|
| **Theme** | Veil zones + echo copies + buff suppression |
| **Primary Debuff** | Null Mark-lite / accuracy reduction |

#### Hazards

| Hazard | Timing | Telegraph | Effect |
|--------|--------|-----------|--------|
| **Veil Curtains** | Every 18s | 1.0s, 8.0s | 2 patches, accuracy down |
| **Echo Spawn** | Every 14s | 1.2s ripple | 1 copy (max 2), chip + minor debuff |

#### Boss Attacks

| Attack | Timing | Telegraph | Effect |
|--------|--------|-----------|--------|
| **Null Lances** | Every 10s | 1.2s | 2 lanes, heavy + strip 1 buff |

#### Conduit Solve

SHADOW conduit: reveals safe lanes through Veil, slows echo spawn, reduces buff strip.

---

## 6) Eclipse Override (Activates at 10% HP)

### Overlay Rule

Engine runs **two hazard families at once**:
- Current phase hazard
- One "echoed" hazard from prior foundation (fixed order, learnable)

### Fixed Echo Order

| HP | Current | Echoed |
|----|---------|--------|
| 10% | Shadow | Time |
| 5% | Shadow | Time + Heat (final burst) |

### Eclipse Signature: ORIGIN VERDICT

| Property | Description |
|----------|-------------|
| **Telegraph** | 2.8s floor-wide "ORIGIN" stamp + rising choir + sigil black-white |
| **Unresolved** | Massive damage + strip 2 buffs + 2 debuffs |

### Solve Options (All Valid)

| Method | Effect |
|--------|--------|
| **Inside Stabilization Field** | Survivable hit + fewer strips |
| **Behind Cover Pylon** | LoS block, reduced damage, no strip |
| **Sanctuary Font during telegraph** | Prevents extra strip, clears 1 debuff |

### Eclipse Reward Hook

| Condition | Effect |
|-----------|--------|
| **Correct conduit during Eclipse** | SYNCED (Extended) for 14s (was 10s) |

---

## 7) Fight Scripting (Sequence)

| Step | Event |
|------|-------|
| 1 | Enter → doors lock → Engine "boots" (2s) |
| 2 | Phase 1 starts (HEAT icon stamp) |
| 3 | Phase shifts at each HP gate (2.5s) |
| 4 | System Rewrite every 20s |
| 5 | At 10% HP → Eclipse Override begins |
| 6 | On defeat → hazards stop, doors unlock, post-clear sanctum activates |

---

## 8) Rewards (F5 Clear)

### Flags

| Flag | Condition |
|------|-----------|
| `FINAL_PALACE_CLEARED` | TRUE |
| `PROGENITOR_ENGINE_DEFEATED` | TRUE |

### Rewards

| Reward | Details |
|--------|---------|
| **Choice** | BIS weapon OR Engine Core craft line |
| **Materials** | Legendary mat bundle (Eclipse pool) |
| **Unlocks** | NG+, Eclipse modifiers, postgame hunts |
| **Terminal** | Save + credits/epilogue trigger |

---

## 9) Implementation Notes (Amazing 8-Phase Finale)

| Rule | Implementation |
|------|----------------|
| **Phase simplicity** | 2 hazards + 1 boss attack per phase (readable, fast) |
| **Conduit feedback** | Loud (icon + color + "field ring"), players must know they succeeded |
| **Wrong conduit** | Never kills—just wastes time |
| **Eclipse Override** | Scary, but Extended SYNC window is emotional payoff |

---

## Quick Reference: 8-Phase Summary

```
THE PROGENITOR ENGINE — 8 FOUNDATION PHASES

PHASE 1: HEAT (100→87.5%)
├─ Hazards: Cauterize Rails (12s), Emberfield Patches (18s)
├─ Attack: Forge Hammer (14s)
└─ Conduit: -Overheat, -2s Emberfields

PHASE 2: TIDE (87.5→75%)
├─ Hazards: Current Shift (10s), Pressure Crush (16s)
├─ Attack: Undertow Pull (18s)
└─ Conduit: Cancels drift, halves Pressure

PHASE 3: GROWTH (75→62.5%)
├─ Hazards: Root Snare (9s), Regrowth Node (18s, max 2)
├─ Attack: Verdant Lance Fan (15s)
└─ Conduit: Destroys nodes, reduces binds

PHASE 4: LIGHT (62.5→50%)
├─ Hazards: Prism Verdict (12s), Flash Seal (18s)
├─ Attack: Radiant Spear (10s)
└─ Conduit: +35% wedge size, -Blind buildup

PHASE 5: MOTION (50→37.5%)
├─ Hazards: Conveyor Hymn (14s), Dash Gates (18s)
├─ Attack: Vector Chop (16s)
└─ Conduit: -forced movement, no turn-delay

PHASE 6: MASS (37.5→25%)
├─ Hazards: Gravity Wells (16s), Compression Slam (20s)
├─ Attack: Anchor Breaker (14s)
└─ Conduit: -pull strength, shrinks center danger

PHASE 7: TIME (25→12.5%)
├─ Hazards: Flicker Slabs (12s), Lag Pulse Ring (16s)
├─ Attack: Secondhand Cleave (10s)
└─ Conduit: Solidifies slabs, halves delay

PHASE 8: SHADOW (12.5→0%)
├─ Hazards: Veil Curtains (18s), Echo Spawn (14s, max 2)
├─ Attack: Null Lances (10s)
└─ Conduit: Reveals veil lanes, slows echoes

ECLIPSE OVERRIDE (10% HP):
├─ 10%: Shadow + Time (dual hazards)
├─ 5%: Shadow + Time + Heat (triple burst)
├─ Origin Verdict: 2.8s telegraph, massive if unresolved
├─ Solve: Field OR pylon LoS OR font cleanse
└─ Extended SYNC: 14s (was 10s) during Eclipse

GLOBAL SYSTEMS:
├─ Conduits: 8 on rim, 30s cd each, 1 active at once
├─ Fonts: 2×(48,44)/(80,44), 3 uses each, 24s cd
├─ Pylons: 2×(48,28)/(80,28), block Core Beam
├─ System Rewrite: Every 20s, strip 1 buff (50% during SYNC)
└─ Instability: +1 on hazard hit, 5 = Eclipse Pulse
```
