# Chroma's Edge — Final Palace: Floor 2 Boss Arena Sheet (v1)
## Time Devourer / The Chronowarden — Stop/Slow Trial

---

## 0) Technical Specs

| Parameter | Value |
|-----------|-------|
| **Boss** | Time Devourer / The Chronowarden |
| **Floor** | F2 (Final Palace) |
| **Recommended Level** | 200–230 |
| **Fight Identity** | Tempo denial + "time debt" management. You win by anchoring time, not brute forcing through Stop loops |
| **Core Threats** | STOP fields, SLOW stacks, DEVOUR MOMENT punish |
| **Arena Size** | 96 × 72 tiles (1536 × 1152 px) |
| **Type** | Boss arena + short prep hall + post-clear terminal |
| **Encounters** | OFF (boss only) |
| **Mounts** | Disabled |
| **Retry Point** | F2 Sanctuary Terminal |

---

## 1) Layout Overview

### 1) Prep Hall

| Property | Value |
|----------|-------|
| **Bounds** | x 0–96, y 60–72 |
| **Features** | Safe pad + "Chrono Trial" plaque + optional 1-time prep crate |

### 2) Main Arena (Chrono Circuit)

| Property | Value |
|----------|-------|
| **Bounds** | x 8–88, y 10–60 |
| **Layout** | Open arena with 4 Chrono Anchors, 1 Chrono Dial, 2 Sanctuary Fonts |

### 3) Post-Clear Terminal Nook

| Property | Value |
|----------|-------|
| **Bounds** | x 36–60, y 0–10 |
| **Features** | Sanctuary Terminal + elevator to Floor 3 |

---

## 2) Anchors & Coordinates (Local 0–95, 0–71)

### Entry / Lock

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Party spawn** | (48, 66) | — |
| **Arena threshold** | y = 60 | Crossing to y≤59 locks doors |
| **Door lock trigger** | (48, 59) | — |

### Boss Spawn

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Chronowarden center** | (48, 34) | — |

### Chrono Anchors (Counterplay, 4)

| Anchor | Coordinates |
|--------|-------------|
| **Anchor N** | (48, 14) |
| **Anchor W** | (18, 34) |
| **Anchor E** | (78, 34) |
| **Anchor S** | (48, 54) |

### Chrono Dial (Optional High-Skill Override)

| Feature | Coordinates |
|---------|-------------|
| **Chrono Dial** | (48, 44) |

### Sanctuary Fonts (Anti-Brick)

| Font | Coordinates |
|------|-------------|
| **Font L** | (30, 52) |
| **Font R** | (66, 52) |

### Post-fight

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Sanctuary Terminal** | (48, 6) | — |
| **Lift tile to F3** | (48, 2) | — |

---

## 3) Core Systems

### A) TIME DEBT (Main Meter)

| Stacks | Effect |
|--------|--------|
| **0–2** | Normal |
| **3** | Minor turn delay (noticeable) |
| **6** | Chronowarden gains Haste (acts more often) |
| **9** | Triggers **DEVOUR MOMENT** (telegraphed near-wipe) |

**Gain sources:** Standing in Stop/Slow hazards, getting hit by time attacks.

**Reset:** Anchors remove stacks; Fonts remove debuffs but NOT Debt.

### B) Chrono Anchors (Primary Counterplay)

| Property | Value |
|----------|-------|
| **Interact time** | 1.0s |
| **Effect** | Removes 2 TIME DEBT stacks + grants ANCHORFIELD (8s, radius ~4 tiles) |
| **ANCHORFIELD effects** | STOP becomes SLOW, reduces SLOW gain by 70% |
| **Cooldown** | 22 seconds per anchor (independent) |
| **Limit** | Only one ANCHORFIELD active at once |

### C) Sanctuary Fonts (Anti-Brick)

| Property | Value |
|----------|-------|
| **Effect** | Cleanse 1 major debuff (priority: Stop → Slow → Time Fray) |
| **Secondary** | 8 seconds "Stability": reduces incoming Debt gain by 30% |
| **Cooldown** | 20 seconds |
| **Limit** | No hard limit (Debt system prevents cheese) |

### D) Chrono Dial (Optional Risk-Reward)

| Property | Value |
|----------|-------|
| **Channel time** | 2.0s (interruptible) |
| **Option A: Freeze Cast** | Cancels next Devour Moment + delays boss rotation by 1 turn |
| **Option B: Slow Arena** | Slows all hazard timings by 30% for 10s |
| **Cooldown** | 35 seconds |

---

## 4) Arena Hazards (Exact Timings)

### Hazard 1: Stillness Panels (STOP Zones) — Primary

| Property | Value |
|----------|-------|
| **Frequency** | Every 11 seconds (P3: every 9s) |
| **Pattern** | 2 rectangular panels (6×3 tiles each) |
| **Telegraph** | 1.6s shimmering grid + ticking sound |
| **Active** | 4.0s |
| **Effect** | STOP (1.5s) + +2 TIME DEBT stacks |
| **Counter** | Inside ANCHORFIELD, STOP downgrades to SLOW |

### Hazard 2: Lag Pulse (SLOW Waves) — Secondary

| Property | Value |
|----------|-------|
| **Frequency** | Every 16 seconds (P3: every 13s) |
| **Pattern** | Expanding ring wave from boss center |
| **Telegraph** | 1.4s expanding circle + bass "thum" |
| **Effect** | SLOW (2 stacks) + +1 TIME DEBT if hit |
| **Note** | Can be line-of-sight softened behind props (optional) |

### Hazard 3: Time Fray (Fracture Tiles) — Phase 2+

| Property | Value |
|----------|-------|
| **Frequency** | Every 18 seconds |
| **Pattern** | 4 tiles turn to flicker "fray" for 6s |
| **Telegraph** | 1.2s shimmer → flicker |
| **Effect** | Turn Delay + +1 TIME DEBT if end turn on fray |

---

## 5) Boss Kit — Chronowarden Moveset

### Passive: Chronophagic Hunger

| Trigger | Effect |
|---------|--------|
| **Player under STOP when boss attacks** | Boss gains Hunger Stack |
| **At 3 Hunger Stacks** | Next major attack deals bonus damage + +1 Debt |
| **Reset** | Hunger clears when Anchor is used successfully |

### Core Attacks

| Attack | Description | Telegraph | Debuff |
|--------|-------------|-----------|--------|
| **Secondhand Cleave** | Line slash | Thin line + clockhand sweep (0.9s) | SLOW (1) + +1 Debt |
| **Hourglass Crush** | 2-circle slam | 1.8s twin circles + sand-fall VFX | Heavy hit + SLOW (2) + +2 Debt |
| **Chrono Snare** | Targeted trap | 1.3s rune circle under target | STOP (short) unless ANCHORFIELD |
| **Rewind Step** | Boss reposition | Boss blurs backward (0.6s) | Leaves 3-tile "afterimage line" (fray, 4s) |

---

## 6) Phase Script (HP-Based)

### Phase 1 (100% → 70%) — "Assessment of Time"

| Aspect | Description |
|--------|-------------|
| **Hazards** | Stillness Panels + Lag Pulse |
| **Boss attacks** | Secondhand Cleave, Chrono Snare, Hourglass Crush (rare) |
| **Devour Moment** | Not active (teased only) |
| **Intent** | Teach Anchors: "Anchorfield downgrades Stop" |

### Phase 2 (70% → 35%) — "Consumption Pattern"

| Aspect | Description |
|--------|-------------|
| **New hazard** | Time Fray |
| **Stillness Panels** | Spawn closer to center (higher pressure) |
| **Boss gains** | Rewind Step more often |
| **Devour Moment** | Active at Debt thresholds |

#### DEVOUR MOMENT Trigger Rule

| Condition | Effect |
|-----------|--------|
| **Any party member reaches 9 TIME DEBT** | Boss begins Devour Moment charge on next turn |

### Phase 3 (35% → 0%) — "Chronowarden Unbound"

| Aspect | Description |
|--------|-------------|
| **Stillness Panels** | Every 9s (was 11s) |
| **Lag Pulse** | Every 13s (was 16s) |
| **Time Fray** | Unchanged, but overlaps more |
| **Boss kit** | Stop/Slow application +1 stack (harsher) |
| **Mercy hook** | Anchor cooldown reduced by 2s ("you can still win if you play clean") |

---

## 7) Signature Mechanic: DEVOUR MOMENT

| Property | Description |
|----------|-------------|
| **Name** | "Devour Moment" |
| **Trigger** | Any member hits 9 TIME DEBT → boss charges on next turn |
| **Telegraph** | 2.2s full-screen clock VFX + arena dims + loud tick |
| **Effect (if resolves)** | Heavy party damage + SLOW (3) + Debt set to 6 (catastrophic) |

### How to Prevent (Multiple Options)

| Method | Effect |
|--------|--------|
| **Use Chrono Anchor** | Removes Debt + disrupts charge |
| **Channel Chrono Dial** | Freeze Cast option cancels Devour |
| **Cleanse STOP from 2+ party members** | Reduces Devour to survivable hit |

*Design intent: Multiple solves so builds aren't gated.*

---

## 8) Fight Scripting (Sequence)

| Step | Event |
|------|-------|
| 1 | Cross threshold → doors lock |
| 2 | Boss: "Your seconds are mine." |
| 3 | TIME DEBT UI appears (first time only) |
| 4 | Phase transitions at 70% and 35% with 2.0s "gear-shift" VFX |
| 5 | On defeat: hazards stop, terminal nook unlocks, F3 elevator activates |

---

## 9) Rewards (F2 Clear)

| Reward | Details |
|--------|---------|
| **Materials** | Time/Chrono legendary mat bundle |
| **Gear** | 1 premium Tier 5 roll |
| **Duckets** | Endgame amount |
| **Flag** | `FINAL_PALACE_F2_CLEARED = TRUE` |

---

## 10) Implementation Notes (Hard But Fair)

| Rule | Implementation |
|------|----------------|
| **STOP zones** | Unmistakable: grid + ticking + hard outline |
| **Spawning** | Never spawn Stillness Panels directly under player without 1.6s telegraph |
| **Anchor feedback** | Loud: "ANCHORFIELD ACTIVE" should feel like relief |
| **Devour Moment** | Always ≥ 2.0s decision time (room to react) |

---

## Quick Reference: Phase Summary

```
CHRONOWARDEN — 3 PHASES + DEVOUR MOMENT

PHASE 1 (100% → 70%): ASSESSMENT OF TIME
├─ Hazards: Stillness Panels (11s), Lag Pulse (16s)
├─ Attacks: Cleave, Snare, Crush (rare)
├─ No Devour Moment (tutorial phase)
└─ Goal: Learn Anchors downgrade Stop → Slow

PHASE 2 (70% → 35%): CONSUMPTION PATTERN
├─ Adds: Time Fray (18s)
├─ Panels: Spawn closer to center (higher pressure)
├─ Boss: Rewind Step more often
└─ Devour Moment: Active at 9 TIME DEBT

PHASE 3 (35% → 0%): CHRONOWARDEN UNBOUND
├─ Panels: Every 9s (faster)
├─ Pulse: Every 13s (faster)
├─ Kit: Stop/Slow +1 stack (harsher)
└─ Mercy: Anchor cooldown -2s

TIME DEBT METER:
├─ 0–2: Normal
├─ 3: Minor turn delay
├─ 6: Boss gains Haste
└─ 9: DEVOUR MOMENT triggers

DEVOUR MOMENT:
├─ Telegraph: 2.2s clock VFX + dim + loud tick
├─ Prevent: Anchor use OR Dial channel OR cleanse 2× STOP
└─ If hits: Heavy damage + SLOW(3) + Debt reset to 6

ANCHORS (4):
├─ N(48,14), W(18,34), E(78,34), S(48,54)
├─ Effect: -2 Debt + ANCHORFIELD (8s, Stop→Slow)
└─ Cooldown: 22s each (20s in P3)

FONTS (2):
├─ L(30,52), R(66,52)
├─ Effect: Cleanse debuff + Stability (8s, -30% Debt gain)
└─ Cooldown: 20s

CHRONO DIAL (48,44):
├─ Channel: 2.0s
├─ Effect: Freeze Devour OR Slow arena 30% for 10s
└─ Cooldown: 35s
```
