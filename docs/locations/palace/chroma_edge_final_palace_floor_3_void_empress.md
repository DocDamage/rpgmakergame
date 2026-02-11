# Chroma's Edge — Final Palace: Floor 3 Boss Arena Sheet (v1)
## Void Empress — Buff-Dispel Trial ("The Null Crown")

---

## 0) Technical Specs

| Parameter | Value |
|-----------|-------|
| **Boss** | Void Empress ("The Null Crown") |
| **Floor** | F3 (Final Palace) |
| **Recommended Level** | 200–230 |
| **Fight Identity** | She erases your setup. You win by creating protected buff windows, cleansing Null Mark, timing bursts inside safe periods |
| **Core Threats** | Buff strip cadence, Null Mark (buffs instantly erased), telegraphed "wipe" with solve |
| **Arena Size** | 96 × 72 tiles (1536 × 1152 px) |
| **Type** | Boss arena + short prep hall + post-clear terminal |
| **Encounters** | OFF (boss only) |
| **Mounts** | Disabled |
| **Retry Point** | F3 Sanctuary Terminal |

---

## 1) Layout Overview

### 1) Prep Hall

| Property | Value |
|----------|-------|
| **Bounds** | x 0–96, y 60–72 |
| **Features** | Safe pad + "Null Crown" plaque + optional 1-time prep crate |

### 2) Main Arena (Crown Court)

| Property | Value |
|----------|-------|
| **Bounds** | x 8–88, y 10–60 |
| **Layout** | Open arena with 4 Ward Mirrors, 2 Null Fountains, 4 Cover Spires |

### 3) Post-Clear Terminal Nook

| Property | Value |
|----------|-------|
| **Bounds** | x 36–60, y 0–10 |
| **Features** | Sanctuary Terminal + elevator to Floor 4 |

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
| **Void Empress center** | (48, 34) | — |

### Ward Mirrors (Counterplay, 4)

| Mirror | Coordinates |
|--------|-------------|
| **Ward Mirror N** | (48, 16) |
| **Ward Mirror W** | (20, 34) |
| **Ward Mirror E** | (76, 34) |
| **Ward Mirror S** | (48, 52) |

### Null Fountains (Anti-Brick, 2)

| Fountain | Coordinates |
|----------|-------------|
| **Fountain L** | (34, 48) |
| **Fountain R** | (62, 48) |

### Cover Spires (Line Blockers; 3×3 Collision, 4)

| Spire | Coordinates |
|-------|-------------|
| **Spire NW** | (28, 24) |
| **Spire NE** | (68, 24) |
| **Spire SW** | (28, 56) |
| **Spire SE** | (68, 56) |

### Post-fight

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Sanctuary Terminal** | (48, 6) | — |
| **Lift tile to F4** | (48, 2) | — |

---

## 3) Core Systems

### A) Imperial Dispersion (Boss Buff Strip Cadence)

| Condition | Effect |
|-----------|--------|
| **Normal** | Start of Empress's turn: removes 1 buff from each party member (strongest/most recent) |
| **Null Mark target** | Next buff gain erased immediately (doesn't count as turn's dispel) |
| **Inside WARD FIELD** | Imperial Dispersion becomes 50% chance per character |

### B) Ward Mirrors (Primary Counterplay)

| Property | Value |
|----------|-------|
| **Interact time** | 1.2s |
| **Effect** | WARD FIELD for 10s (radius ~5 tiles) |
| **WARD FIELD effects** | Dispel Dampening (max 1 buff/turn), Null Mark rate -70%, HARMONIZED (+15% boss damage) |
| **Cooldown** | 26 seconds per mirror (independent) |
| **Limit** | Only one WARD FIELD active at once |

### C) Null Fountains (Anti-Brick Cleanse)

| Property | Value |
|----------|-------|
| **Effect** | Cleanse 1 major debuff (priority: Null Mark → Void Rot → Confounded) |
| **Secondary** | 8s "Sanctuary Sheen": next buff can't be erased, Null Mark application -30% |
| **Cooldown** | 20 seconds |
| **Disable rule** | Disabled during Crown of Silence unless WARD FIELD active |

---

## 4) Arena Hazards (Exact Timings)

### Hazard 1: Royal Erasure Wave (Erasure Pulse)

| Property | Value |
|----------|-------|
| **Frequency** | Every 14 seconds (P3: every 12s) |
| **Telegraph** | 1.6s expanding ring + sharp "glass scrape" audio |
| **Effect on hit** | Strip 1 buff + Null Mark (1 stack) + medium damage |
| **Counter** | Inside WARD FIELD (strip 50% chance, Null Mark rate reduced) OR behind spires (optional LoS) |

### Hazard 2: Crown Lances (Null Lances)

| Property | Value |
|----------|-------|
| **Frequency** | Every 10 seconds (P3: every 8s) |
| **Pattern** | 2 lane lines (horizontal/vertical/diagonal) |
| **Telegraph** | 1.2s thin violet lines + crackle |
| **Active** | Instant strike + 0.5s linger |
| **Effect** | Heavy damage + strip 1 buff + Void Rot |

### Hazard 3: Veil Curtains (Veil Patches)

| Property | Value |
|----------|-------|
| **Frequency** | Every 18 seconds |
| **Pattern** | 2 patches near mid-edges |
| **Telegraph** | 1.0s smoky bloom |
| **Active** | 8.0s |
| **Effect** | Accuracy down/confounded-lite + increased Null Mark chance |

### Hazard 4: Orbit of Denial (Null Orbs) — Phase 2+

| Property | Value |
|----------|-------|
| **Frequency** | Every 22 seconds |
| **Pattern** | 3 orbits orbiting boss for 6s, then detonate outward |
| **Telegraph** | 1.4s orb formation + rising whine |
| **Detonation** | 8 radial shots |
| **Effect** | Damage + Null Mark (1) |

---

## 5) Boss Moveset

| Attack | Description | Telegraph | Effect |
|--------|-------------|-----------|--------|
| **Crown Seal** | Single target mark | 0.8s crown sigil stamp over target | Null Mark (2 stacks) |
| **Edict Slash** | Cone attack | 1.0s cone outline | Medium damage + strip 1 buff |
| **Imperial Reflection** | Mirror-step reposition | 0.6s shimmer | Boss relocates near mirror, leaves 3-tile "afterimage strip" (Veil, 4s) |
| **Decree Break** | Anti-burst punish | 1.2s hand raise + snap | If party has >6 total buffs, removes 1 extra from 2 most-buffed characters |

---

## 6) Phases (HP-Based)

### Phase 1 (100% → 70%) — "Court of Removal"

| Aspect | Description |
|--------|-------------|
| **Hazards** | Erasure Pulse, Null Lances, Veil Curtains |
| **Boss attacks** | Crown Seal, Edict Slash, Imperial Reflection |
| **Fountains** | Fully available |
| **Intent** | Teach loop: Mirror → Ward Field → burst → cleanse Null Mark → reposition |

### Phase 2 (70% → 35%) — "Crown of Silence"

| Aspect | Description |
|--------|-------------|
| **New hazard** | Null Orbs (every 22s) |
| **New mechanic** | **Crown of Silence cycle** (every 28s, 10s active) |

#### Crown of Silence

| Property | Value |
|----------|-------|
| **Telegraph** | 2.0s arena dims + crown outline above boss |
| **Active duration** | 10 seconds |
| **Effect** | Null Fountains disabled, Imperial Dispersion guaranteed (no 50% roll) unless WARD FIELD active |
| **Solve** | Activating WARD FIELD re-enables fountains + restores Dispersion to 50% |

### Phase 3 (35% → 0%) — "Null Crown Ascendant"

| Aspect | Description |
|--------|-------------|
| **Erasure Pulse** | Every 12s (was 14s) |
| **Null Lances** | Every 8s (was 10s) |
| **Veil Curtains** | Unchanged |
| **Null Orbs** | Unchanged |
| **Crown of Silence** | Every 24s (shorter cycle) |
| **New move** | **Regal Nullstep**: 0.9s shadow-shear, boss blinks opposite side + immediate Null Lances |
| **Mercy** | Mirror cooldowns stay generous |

---

## 7) Signature Attack: Royal Null Decree

| Property | Description |
|----------|-------------|
| **Name** | "Royal Null Decree" |
| **Triggers** | 60% and 25% HP only |
| **Telegraph** | 2.6s huge floor text stamp ("DECREE") + rising choir note |
| **Effect (unresolved)** | Strip ALL buffs, Null Mark (3) to everyone, massive damage (likely wipe) |

### How to Survive / Solve

| Method | Effect |
|--------|--------|
| **Inside WARD FIELD** | Strips 1–2 buffs max + heavy-but-survivable damage |
| **Behind Cover Spire** | LoS block: half damage + fewer debuffs |
| **Null Fountain during telegraph** | Sanctuary Sheen prevents buff erase chain from Null Mark |

*Multiple valid answers respect different party builds.*

---

## 8) Fight Scripting (Sequence)

| Step | Event |
|------|-------|
| 1 | Cross threshold → doors lock |
| 2 | Boss (optional): "Your power is borrowed. I will reclaim it." |
| 3 | Phase 1 begins; Imperial Dispersion activates immediately |
| 4 | Phase transitions at 70% and 35% with 2.0s "crown flare" VFX |
| 5 | Royal Null Decree triggers at 60% and 25% HP |
| 6 | On defeat: hazards stop, fountains enable, terminal nook unlocks, F4 elevator activates |

---

## 9) Rewards (F3 Clear)

| Reward | Details |
|--------|---------|
| **Materials** | Shadow/void legendary mat bundle |
| **Gear** | 1 premium Tier 5 roll |
| **Duckets** | Endgame payout |
| **Flag** | `FINAL_PALACE_F3_CLEARED = TRUE` |

---

## 10) Implementation Notes (Brutal But Fair)

| Rule | Implementation |
|------|----------------|
| **Null Mark** | Unmistakable: icon + subtle "static" sound when buff erased |
| **WARD FIELD** | Loud feedback: "WARD ACTIVE — DISPERSAL SUPPRESSED" |
| **Veil Patches** | Never spawn directly under players without 1.0s telegraph |
| **Royal Null Decree** | Always full 2.6s warning (reaction time required) |

---

## Quick Reference: Phase Summary

```
VOID EMPRESS — 3 PHASES + ROYAL NULL DECREE

PHASE 1 (100% → 70%): COURT OF REMOVAL
├─ Hazards: Erasure Pulse (14s), Null Lances (10s), Veil Curtains (18s)
├─ Attacks: Crown Seal, Edict Slash, Imperial Reflection
├─ Fountains: Fully available
└─ Goal: Learn Ward Field loop

PHASE 2 (70% → 35%): CROWN OF SILENCE
├─ Adds: Null Orbs (22s)
├─ New: Crown of Silence cycle (28s, 10s active)
│   ├─ Fountains disabled
│   ├─ Dispersion guaranteed (no 50% roll)
│   └─ Solve: Ward Field re-enables fountains
└─ Royal Null Decree at 60% HP

PHASE 3 (35% → 0%): NULL CROWN ASCENDANT
├─ Pulse: Every 12s (faster)
├─ Lances: Every 8s (faster)
├─ Silence cycle: Every 24s (shorter)
├─ New: Regal Nullstep (blink + immediate Lances)
└─ Royal Null Decree at 25% HP

IMPERIAL DISPERSION:
├─ Normal: 1 buff stripped/turn per character
├─ Null Mark: Next buff gain erased immediately
└─ Ward Field: 50% chance to strip (Dispel Dampening)

WARD MIRRORS (4):
├─ N(48,16), W(20,34), E(76,34), S(48,52)
├─ Effect: WARD FIELD (10s, Dispel Dampening, -70% Null Mark)
├─ HARMONIZED: +15% boss damage
└─ Cooldown: 26s each

NULL FOUNTAINS (2):
├─ L(34,48), R(62,48)
├─ Effect: Cleanse debuff + Sanctuary Sheen (8s, next buff protected)
├─ Disabled during Crown of Silence unless Ward Field active
└─ Cooldown: 20s

ROYAL NULL DECREE:
├─ Triggers: 60% and 25% HP
├─ Telegraph: 2.6s floor text + choir note
├─ Unresolved: Strip ALL buffs + Null Mark(3) + massive damage
└─ Solve: Ward Field OR spire LoS OR fountain Sheen

COVER SPIRES (4):
├─ NW(28,24), NE(68,24), SW(28,56), SE(68,56)
└─ 3×3 collision, blocks LoS for Null Decree
```
