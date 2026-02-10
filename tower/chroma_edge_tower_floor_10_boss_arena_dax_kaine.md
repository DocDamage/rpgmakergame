# Chroma's Edge — Aurora Ascension Tower: Floor 10 Boss Arena Sheet (v1)
## Commander Dax Kaine — Dominion Vanguard (Dual Plasma Cannons)

---

## 0) Technical Specs

| Parameter | Value |
|-----------|-------|
| **Boss** | Commander Dax Kaine |
| **Identity** | Dominion Vanguard — Dual Plasma Cannons |
| **Stratum** | 1–10 (Heat) |
| **Recommended Level** | 100–120 |
| **Arena Goal** | Teach tower boss language: telegraphs + interactables + "don't facetank beams" |
| **Save** | None (next save is Floor 20) |
| **Arena Size** | 72 × 56 tiles (1152 × 896 px) |
| **Type** | Boss arena + small prep hall + reward alcove |
| **Encounters** | OFF (boss only) |
| **Mounts** | Disabled |
| **Camera** | Keep boss fully readable during cannon telegraphs |

---

## 1) Layout Overview

### 1) Prep Hall (Entry Buffer)

| Property | Value |
|----------|-------|
| **Bounds** | x 0–72, y 44–56 |
| **Features** | Safe pad + "ready" prompt + optional consumable crate |
| **Lock** | Door locks once player crosses threshold (y≤43) |

### 2) Main Arena (Combat Bowl)

| Property | Value |
|----------|-------|
| **Bounds** | x 6–66, y 6–44 |
| **Features** | Symmetrical, 4 cover pillars, 2 coolant valves, 2 heat vents, 1 central pressure plate |

### 3) Reward Alcove (Post-Fight)

| Property | Value |
|----------|-------|
| **Bounds** | x 28–44, y 0–6 |
| **Features** | Chest + floor lift tile to Floor 11 |

---

## 2) Anchors & Coordinates (Local 0–71, 0–55)

### Entry / Lock

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Entry spawn** | (36, 52) | — |
| **Arena threshold** | y = 44 | Crossing to y≤43 locks doors |
| **Door lock trigger** | (36, 43) | — |

### Boss Spawn

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Dax Kaine spawn** | (36, 22) | Center |

### Cover Pillars (Block Line Attacks)

| Pillar | Coordinates | Notes |
|--------|-------------|-------|
| **Pillar NW** | (18, 18) | 3×3 collision |
| **Pillar NE** | (54, 18) | 3×3 collision |
| **Pillar SW** | (18, 30) | 3×3 collision |
| **Pillar SE** | (54, 30) | 3×3 collision |

*Pillars should have optional "burn mark" decal.*

### Arena Interactables

| Feature | Coordinates | Function |
|---------|-------------|----------|
| **Coolant Valve A** | (10, 22) | Disable vents / reduce Overheat |
| **Coolant Valve B** | (62, 22) | Disable vents / reduce Overheat |
| **Heat Vent A** | (24, 36) | Floor hazard tile cluster |
| **Heat Vent B** | (48, 36) | Floor hazard tile cluster |
| **Pressure Plate** (optional) | (36, 34) | Suppression toggle |

### Post-Fight Rewards

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Reward chest** | (36, 3) | — |
| **Lift tile to Floor 11** | (36, 1) | — |

---

## 3) Arena Hazards

### A) Heat Vents (Telegraphed)

| Property | Value |
|----------|-------|
| **Pulse cycle** | Every ~10–14 seconds, lasting 3 seconds |
| **Effect** | Overheat buildup + small chip damage |
| **Telegraph** | Floor glow → hiss → flame |

### B) Coolant Valves (Player Counterplay)

| Property | Value |
|----------|-------|
| **Interact time** | 1.2s |
| **Effect A** | Disable both vents for 12 seconds |
| **Effect B** (alt) | Reduce Overheat buildup by 50% for 20 seconds |
| **Cooldown** | 25 seconds per valve (independent) |

### C) Cover Pillars

| Property | Value |
|----------|-------|
| **Function** | Block Dax's straight-line beam attacks |
| **Durability** | Cosmetically degrade but don't fully break on F10 |

---

## 4) Boss Kit — Core Mechanics

### Passive: Vanguard Plating

| Property | Value |
|----------|-------|
| **Effect** | Armor (flat damage reduction) |
| **Armor decrease triggers** | Suppression effect (pressure plate), armor-break skills, standing in coolant field |

### Status Theme

| Status | Application |
|--------|-------------|
| **Armor Break** | Frequent |
| **Overheat** | Frequent |
| **Dominion Mark** (optional) | Increases damage from next cannon attack |

---

## 5) Phase Script (HP-Based)

### Phase 1 (100% → 70%): "Line Discipline"

| Attack | Description | Counter |
|--------|-------------|---------|
| **Plasma Sweep** | Telegraphed lane beam | Hide behind pillars OR sidestep |
| **Shrapnel Burst** | Small AOE around boss | Anti-melee greed |
| **Armor Rend** | Single-target Armor Break | — |
| **Arena** | Heat vents pulse normally | — |

### Phase 2 (70% → 35%): "Dual Pattern"

| Attack | Description | Counter |
|--------|-------------|---------|
| **Crossfire Grid** | Two beams intersect (X or +) | Read floor telegraph |
| **Vanguard Rush** | Dash to nearest, leaves burn trail | Sidestep |
| **Command Uplink** | Self-buff: +speed/initiative | Can be suppressed by pressure plate |
| **Arena** | Vents pulse more frequently until coolant used | Teach valves |

**Transition:** Short VFX pulse at 70%

### Phase 3 (35% → 0%): "Execution Window"

| Attack | Description | Counter |
|--------|-------------|---------|
| **Overcharge Protocol** | Plants feet, charges 2s, fires 90° sweep beam | Pillar rotation gameplay OR coolant to shorten |
| **Plasma Hammer** | Big single-target slam after Overcharge | Punishes panic heals |
| **Arena** | One vent pulses continuously unless coolant used | Still telegraphed |

**Transition:** Short VFX pulse at 35%

---

## 6) Optional Mechanic: Pressure Plate (Suppression)

| Property | Value |
|----------|-------|
| **Location** | (36, 34) |
| **Activation** | Stand 2 seconds |
| **Effect** | Suppression Field for 8 seconds |
| **Field effects** | Boss armor -25%, Overcharge charge speed reduced |
| **Cooldown** | 30 seconds |
| **Risk** | Plate in unsafe lane (exposed while holding) |

*Note: If not using this mechanic, pillars + valves are sufficient.*

---

## 7) Fight Scripting (Sequence)

| Step | Event |
|------|-------|
| 1 | Player enters arena threshold → doors lock |
| 2 | Dax drops from above / steps out of heat shimmer |
| 3 | Boss bark (optional): "Unauthorized ascent. Final warning." |
| 4 | Boss begins in Phase 1 |
| 5 | Phase transitions at 70% and 35% (short VFX pulse, no long cutscenes) |
| 6 | On defeat: arena hazards stop, doors unlock, chest spawns, lift activates |

---

## 8) Rewards (Floor 10 Milestone)

### Mandatory Clear Rewards

| Reward | Details |
|--------|---------|
| **Tier 4–5 Rare Equipment** | 1 piece |
| **Tower Tokens** | +10 |
| **Duckets** | +80,000–110,000 |
| **Rare Mats** | 2 rolls from "Heat/Metal" pool |

### Optional Bonus

| Condition | Bonus |
|-----------|-------|
| Used 0 items OR beat within X turns | Extra +5 tokens OR additional mat roll |

---

## 9) Flags

| Flag | Condition |
|------|-----------|
| `TOWER_F10_CLEARED` | TRUE |
| `TOWER_BOSS_10_DEFEATED` | TRUE |
| `TOWER_LAST_REACHED_FLOOR` | 10 |
| **Unlock** | Trophy icon on Lobby's Hundred Marks Wall |

---

## 10) Failure / Retry Behavior

| Condition | Behavior |
|-----------|----------|
| **On wipe** | Respawn at Tower Lobby (next save is Floor 20) |
| **Resume option** | "Resume at Floor 1" (or tower's chosen restart behavior pre-20) |
| **Boss intro** | Skippable on retries |

---

## 11) Implementation Notes

| Note | Priority |
|------|----------|
| Beam telegraphs thicker than normal on F10 (training boss) | High |
| Pillars block beams reliably — no "clipped corners" | High |
| Coolant valves readable: bright handle + hiss + visible feedback | High |
| Keep arena symmetrical for fair pillar positioning | Medium |
| VFX pulses at phase transitions (not long cutscenes) | Medium |

---

## Quick Reference: Arena at a Glance

```
    NORTH (y=0, Reward Alcove)
       ↑
    ┌───────────────────────────────────────────┐
    │  Reward Alcove (y 0–6)                    │
    │  - Chest (36,3)                           │
    │  - Lift to F11 (36,1)                     │
    └───────────────────────────────────────────┘
                      │
    ══════════════════╪══════════════════════════
                      │
    ┌───────────────────────────────────────────┐
    │  Main Arena (y 6–44)                      │
    │                                           │
    │      NW Pillar        NE Pillar         │
    │      (18,18)          (54,18)           │
    │           │                │              │
    │  Valve A  │    DAX KAINE   │  Valve B    │
    │  (10,22)  │    (36,22)     │  (62,22)    │
    │           │                │              │
    │      SW Pillar        SE Pillar         │
    │      (18,30)          (54,30)           │
    │                                           │
    │  Heat Vent A    Pressure    Heat Vent B   │
    │  (24,36)        Plate       (48,36)       │
    │                 (36,34)                   │
    │                                           │
    └───────────────────────────────────────────┘
                      │
    ══════════════════╪══════════════════════════ (y=44 threshold)
                      │
    ┌───────────────────────────────────────────┐
    │  Prep Hall (y 44–56)                      │
    │  - Entry spawn (36,52)                    │
    │  - Lock trigger (36,43)                   │
    │  - Safe pad + optional crate              │
    └───────────────────────────────────────────┘
                      │
                   SOUTH (y=55, Entry)

PHASE SUMMARY:
P1 (100–70%): Line Discipline — Plasma Sweep, Shrapnel, Armor Rend
P2 (70–35%): Dual Pattern — Crossfire Grid, Vanguard Rush, Command Uplink
P3 (35–0%): Execution Window — Overcharge Protocol, Plasma Hammer

KEY MECHANICS:
- Pillars block beams
- Valves disable vents / reduce Overheat
- Pressure plate (optional) suppresses boss armor/speed
- Vents pulse telegraphed heat damage
```
