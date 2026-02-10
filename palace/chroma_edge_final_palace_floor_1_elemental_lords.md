# Chroma's Edge — Final Palace: Floor 1 Boss Arena Sheet (v1)
## The Elemental Lords — 4-Phase Trial

---

## 0) Technical Specs

| Parameter | Value |
|-----------|-------|
| **Boss** | The Elemental Lords (single encounter, 4 phases) |
| **Floor** | F1 (Final Palace) |
| **Recommended Level** | 200–230 |
| **Fight Identity** | "Read the element → hit the matching altar → survive the pattern → burst in the window" exam |
| **Win Condition** | Shared HP bar; each phase is a different Lord mode |
| **Arena Size** | 96 × 72 tiles (1536 × 1152 px) |
| **Type** | Boss arena + short prep hall + post-clear terminal |
| **Encounters** | OFF (boss only) |
| **Mounts** | Disabled |
| **Retry Point** | F1 Sanctuary Terminal |

---

## 1) Layout Overview

### 1) Prep Hall

| Property | Value |
|----------|-------|
| **Bounds** | x 0–96, y 60–72 |
| **Features** | Safe pad + "Element Trial" plaque + optional 1-time prep crate (high-tier consumables) |

### 2) Main Arena (Element Court)

| Property | Value |
|----------|-------|
| **Bounds** | x 8–88, y 10–60 |
| **Layout** | Open circular court with 4 Element Altars + 1 Cleanse Font |

### 3) Post-Clear Terminal Nook

| Property | Value |
|----------|-------|
| **Bounds** | x 36–60, y 0–10 |
| **Features** | Sanctuary Terminal + elevator to Floor 2 |

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
| **Boss center** | (48, 34) | — |

### Element Altars (Counterplay)

| Altar | Coordinates | Element | Phase |
|-------|-------------|---------|-------|
| **Flame Altar** | (48, 14) | Heat | Phase 1 |
| **Tide Altar** | (78, 26) | Tide | Phase 2 |
| **Stone/Growth Altar** | (18, 44) | Growth/Stone | Phase 3 |
| **Storm/Light Altar** | (78, 44) | Light/Storm | Phase 4 |

### Cleanse / Relief

| Feature | Coordinates | Cooldown |
|---------|-------------|----------|
| **Cleanse Font** | (48, 52) | 20 seconds |

### Post-fight

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Sanctuary Terminal** | (48, 6) | — |
| **Lift tile to F2** | (48, 2) | — |

---

## 3) Core Systems

### A) Shared HP + Phase Locks

| Aspect | Description |
|--------|-------------|
| **HP Structure** | One shared boss HP bar |
| **Transitions** | 75% / 50% / 25% HP |
| **Shift Window** | 2.5 seconds invulnerable "Element Shift" (telegraphed) |

### B) Element Altars (Primary Counterplay)

| Property | Value |
|----------|-------|
| **Interact time** | 1.0s |
| **Effect (matching element)** | ELEMENT WARD for 12 seconds: -70% hazard intensity, EXPOSED (+15% boss damage) |
| **Cooldown** | 25 seconds per altar (independent) |
| **Limit** | Only one ELEMENT WARD active at once |
| **Wrong altar** | Fizzles + 5s "misfire" cooldown (time loss only) |

### C) Cleanse Font (Anti-Brick)

| Property | Value |
|----------|-------|
| **Effect** | Cleanse 1 major debuff (priority: Overheat / Pressure / Vinebind / Blind) |
| **Secondary** | 8 seconds minor resist to active phase's debuff |
| **Cooldown** | 20 seconds |

---

## 4) Boss Kit (Global Rules)

### Passive: Elemental Authority

| Lord | Authority Effect |
|------|------------------|
| **Flame** | Overheat application + burn lanes |
| **Tide** | Drift/pressure + slam |
| **Stone/Growth** | Roots + regen pulse |
| **Storm/Light** | Prism safe wedge + flashblind |

### Global Move: "Crown Confluence" (Phase Shift Pulse)

| Property | Description |
|----------|-------------|
| **Trigger** | Each phase start (75/50/25 HP) |
| **Telegraph** | 1.0s floor-wide sigil stamp + deep chime |
| **Effect** | Light knockback to edges + clears existing hazards |

---

## 5) Phase 1 — Flame Lord (100% → 75%)

| Property | Value |
|----------|-------|
| **State Icon** | Flame |
| **Debuff Theme** | Overheat |
| **Hazard Theme** | Burn Lanes |

### Arena Hazard Timing

#### Cauterize Lanes (Main Hazard)

| Property | Value |
|----------|-------|
| **Frequency** | Every 12s |
| **Pattern** | 2 lanes (horizontal or vertical) |
| **Telegraph** | 1.6s glowing lane lines |
| **Active** | 3.0s (standing = heavy chip + Overheat + Marked) |
| **Window** | ~7.4s before next lane event |

#### Emberfall Patches (Secondary)

| Property | Value |
|----------|-------|
| **Frequency** | Every 18s |
| **Pattern** | 3 patch circles |
| **Telegraph** | 1.2s orange rings |
| **Active** | 6.0s lingering fire tiles |

### Boss Attacks

| Attack | Description | Telegraph |
|--------|-------------|-----------|
| **Searing Brand** | Single target, applies Overheat (2 stacks) | Hand glow + aiming line (0.7s) |
| **Ashen Spiral** | Medium AOE around boss (punishes melee) | Expanding ring (1.0s) |

### Counterplay Notes

| Altar Effect | Description |
|--------------|-------------|
| Flame Altar | -70% lane damage/Overheat, Emberfall patches expire 2s faster during ward |

---

## 6) Phase 2 — Tide Lord (75% → 50%)

| Property | Value |
|----------|-------|
| **State Icon** | Tide |
| **Debuff Theme** | Pressure |
| **Hazard Theme** | Current Drift + Crush Zones |

### Arena Hazard Timing

#### Current Shift (Drift Cycle)

| Property | Value |
|----------|-------|
| **Frequency** | Every 10s |
| **Pattern** | Sets drift direction (N/E/S/W) |
| **Telegraph** | 1.0s floor arrows appear |
| **Active** | 8.0s (drift 1 tile every 2s) |

#### Pressure Crush (Slam Zones)

| Property | Value |
|----------|-------|
| **Frequency** | Every 16s |
| **Pattern** | 2 large circles |
| **Telegraph** | 1.8s deep-blue rings + "pressure hum" |
| **Impact** | Instant heavy damage + Pressure (3 stacks) if inside |
| **Aftereffect** | 3.0s slow field lingering |

### Boss Attacks

| Attack | Description | Telegraph |
|--------|-------------|-----------|
| **Brine Spear** | Line projectile | Thin line + splash sparkle (1.0s) |
| **Undertow Pull** | Small pull toward boss | Water swirl under boss (1.2s) |

### Counterplay Notes

| Altar Effect | Description |
|--------------|-------------|
| Tide Altar ward | Cancels drift entirely, reduces Pressure stacks by 70% |

---

## 7) Phase 3 — Stone/Growth Lord (50% → 25%)

| Property | Value |
|----------|-------|
| **State Icon** | Stone/Vine |
| **Debuff Theme** | Vinebind |
| **Hazard Theme** | Roots + Regen Nodes |

### Arena Hazard Timing

#### Root Snare Bloom

| Property | Value |
|----------|-------|
| **Frequency** | Every 9s |
| **Pattern** | Targets 2 players (or 2 random tiles) |
| **Telegraph** | 1.3s green circles |
| **Effect** | Brief bind (2.5s) + Vinebind buildup |

#### Regrowth Totems (Mini-Objects)

| Property | Value |
|----------|-------|
| **Frequency** | Every 18s |
| **Pattern** | Spawns 1 totem near edge (max 2 alive) |
| **Effect** | Boss +4% HP regen/turn while alive |
| **Telegraph** | Vine pillar rises (1.0s) |

### Boss Attacks

| Attack | Description | Telegraph |
|--------|-------------|-----------|
| **Petrifying Shardline** | 3 shard spikes in fan | Ground cracks (1.2s) |
| **Verdant Slam** | AOE stomp; leaves 4 thorn tiles for 6s | Both arms raised (0.9s) |

### Counterplay Notes

| Altar Effect | Description |
|--------------|-------------|
| Stone/Growth Altar ward | Instantly destroys active Regrowth Totems, reduces bind duration by 70% |

---

## 8) Phase 4 — Storm/Light Lord (25% → 0%)

| Property | Value |
|----------|-------|
| **State Icon** | Prism/Storm |
| **Debuff Theme** | Blind / Confounded-lite |
| **Hazard Theme** | Safe Wedge + Thunder Lines |

### Arena Hazard Timing

#### Prism Verdict (Safe Wedge) — Primary

| Property | Value |
|----------|-------|
| **Frequency** | Every 12s |
| **Telegraph** | 1.5s wedge outline appears |
| **Active** | 8.0s |
| **Outside effect** | Chip damage + Blind buildup (stacking) |

#### Thunderline Cross (Secondary Burst)

| Property | Value |
|----------|-------|
| **Frequency** | Every 14s |
| **Telegraph** | 1.4s cross-lane lines + crackle audio |
| **Impact** | Instant heavy hit in lines + brief stagger |

#### Flash Seal

| Property | Value |
|----------|-------|
| **Frequency** | Every 18s |
| **Telegraph** | Boss eye-glow + screen-edge flare (1.0s) |
| **Effect** | Blind-lite unless inside wedge |

### Boss Attacks

| Attack | Description | Telegraph |
|--------|-------------|-----------|
| **Radiant Spear** | Fast line | Short line (0.6s) |
| **Stormstep** | Blink reposition; leaves 3-tile spark trail for 4s | Blink visual |

### Counterplay Notes

| Altar Effect | Description |
|--------------|-------------|
| Storm/Light Altar ward | Expands safe wedge ~35%, reduces Blind buildup by 70%, Thunderline hitbox slightly narrower |

---

## 9) Phase Transition Script

At HP 75/50/25:

| Step | Event |
|------|-------|
| 1 | Boss becomes invulnerable for 2.5s |
| 2 | **Crown Confluence** triggers: 1.0s telegraph → pulse knockback → clears hazards/totems |
| 3 | New element icon stamps on floor for 1.0s |
| 4 | Next phase begins |

---

## 10) Fight Scripting (Sequence)

| Step | Event |
|------|-------|
| 1 | Cross threshold → doors lock |
| 2 | Line (optional): "Only the worthy may ascend." |
| 3 | Phase 1 begins (Flame icon) |
| 4 | Phase shifts at 75/50/25 with Confluence pulse |
| 5 | On defeat: hazards stop, terminal nook unlocks, elevator to F2 enables |

---

## 11) Rewards (F1 Clear)

| Reward | Details |
|--------|---------|
| **Materials** | Legendary mat bundle (elemental-themed) |
| **Gear** | 1 premium Tier 5 roll |
| **Duckets** | Endgame amount |
| **Flag** | `FINAL_PALACE_F1_CLEARED = TRUE` |

---

## 12) Implementation Notes (Hard But Never Cheap)

| Rule | Implementation |
|------|----------------|
| **Telegraphs** | Every hazard ≥ 1.0s (no surprise wipes) |
| **Spawning** | Never spawn circles directly under player without telegraph |
| **Visuals** | Active element icon: huge (UI + floor stamp + audio sting) |
| **Lighting** | Optional: tint arena per phase (warm → blue → green → violet) |

---

## Quick Reference: Phase Summary

```
ELEMENTAL LORDS — 4 PHASES

PHASE 1: FLAME LORD (100% → 75%)
├─ Hazard: Cauterize Lanes (every 12s, 2 lanes)
├─ Hazard: Emberfall Patches (every 18s, 3 patches)
├─ Debuff: Overheat (2 stacks from Searing Brand)
├─ Altar: Flame Altar (48, 14)
└─ Counter: -70% lane damage, patches expire faster

PHASE 2: TIDE LORD (75% → 50%)
├─ Hazard: Current Shift (every 10s, 8s drift)
├─ Hazard: Pressure Crush (every 16s, 2 circles)
├─ Debuff: Pressure (3 stacks from crush)
├─ Altar: Tide Altar (78, 26)
└─ Counter: Cancels drift, -70% Pressure gain

PHASE 3: STONE/GROWTH LORD (50% → 25%)
├─ Hazard: Root Snare Bloom (every 9s, 2 targets)
├─ Hazard: Regrowth Totems (every 18s, +4% regen each)
├─ Debuff: Vinebind (from root snares)
├─ Altar: Stone/Growth Altar (18, 44)
└─ Counter: Destroys totems instantly, -70% bind duration

PHASE 4: STORM/LIGHT LORD (25% → 0%)
├─ Hazard: Prism Verdict (every 12s, safe wedge)
├─ Hazard: Thunderline Cross (every 14s, cross lanes)
├─ Hazard: Flash Seal (every 18s, Blind-lite)
├─ Debuff: Blind (outside wedge), Confounded-lite
├─ Altar: Storm/Light Altar (78, 44)
└─ Counter: +35% wedge size, -70% Blind buildup

GLOBAL:
├─ Cleanse Font: (48, 52), 20s cooldown
├─ Phase shifts at 75/50/25 with Crown Confluence
├─ Wrong altar = 5s misfire (no punishment)
└─ One ELEMENT WARD active at once (no stacking)
```
