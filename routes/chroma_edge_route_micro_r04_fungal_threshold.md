# Route Micro-Map: R04 — Fungal Threshold

## Route Overview

| Property | Value |
|----------|-------|
| **Route Name** | Fungal Threshold (R04 Micro) |
| **Theme** | Palisade edge → fungus ravine mouth → dungeon door |
| **Encounter Level Band** | 18–26 |
| **Mounts** | OFF |
| **Map Size** | 56 × 36 (x 0–55, y 0–35) |

---

## Exits

| Destination | Coordinates | Notes |
|-------------|-------------|-------|
| **From Mirewatch (town gate)** | (8, 30) | Route start |
| **To Fungal Depths (D2) entrance** | (48, 6) | Dungeon door |
| **Loopback shortcut gate (post-D2)** | (28, 18) | Root door — unlocks after D2 |

---

## Key Anchors

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Guard post sign | (12, 28) | "DEPTHS AHEAD" |
| Spore Gate (mini puzzle) | (30, 14) | D2 entry gate |

---

## Terrain / Hazards

### Spore Fog Lanes (Pulsing)

| Lane | Coordinates | Pattern |
|------|-------------|---------|
| **Lane A** | x 18–22 at y 16–28 | Vertical strip |
| **Lane B** | x 34–38 at y 16–28 | Vertical strip |

#### Pulse Mechanics

| Property | Value |
|----------|-------|
| **Cycle** | 10s |
| **Telegraph** | 1.2s |
| **Active** | 3.0s |
| **Effect** | Spore Haze (accuracy down-lite) + tiny chip (optional) |

---

## Micro Puzzle: Spore Gate

### Objective
Open the root gate by toggling three Spore Lamps within time limit.

### Lamp Locations

| Lamp | Coordinates |
|------|-------------|
| **Lamp 1** | (22, 12) |
| **Lamp 2** | (30, 10) |
| **Lamp 3** | (38, 12) |

### Rule

| Condition | Result |
|-----------|--------|
| Toggle all 3 within 8 seconds | Gate opens |
| Timer expires | Reset, try again |

### Teaching Purpose

> Teaches "timed interact under light pressure" — precursor to shrine puzzles.

---

## Encounter Pockets (2, Controlled)

### Pocket A (Before Gate)

| Property | Value |
|----------|-------|
| **Location** | (20, 22) |
| **Composition** | 2× Sporeling + 1× Leechling |

### Pocket B (After Gate)

| Property | Value |
|----------|-------|
| **Location** | (40, 10) |
| **Composition** | 1× "Bud Node" + 2× Sporeling |
| **Notes** | Bud Node blooms in 10s and buffs adds — teaches pruning |

---

## Interactables

| Type | Coordinates | Contents |
|------|-------------|----------|
| Chest (small) | (44, 30) | Consumables |
| Gather: Fungal Cap | (12, 16) | Crafting |
| Gather: Marsh Herb | (40, 24) | Crafting |

---

## Post-D2 Shortcut (QoL)

| Condition | Effect |
|-----------|--------|
| `D2_CLEARED = TRUE` | Unlock Root Door at (28, 18) |
| **Benefit** | Short loop back to Mirewatch — no backtracking |

---

## Quick Reference Coordinates

```
Mirewatch entry: (8, 30)      D2 entrance: (48, 6)
Guard sign: (12, 28)          Spore Gate: (30, 14)
Shortcut gate: (28, 18) [locked until D2]

--- Pockets ---
A: (20, 22)                   B: (40, 10)

--- Puzzle ---
Lamp 1: (22, 12)              Lamp 2: (30, 10)
Lamp 3: (38, 12)              Gate: (30, 14)

--- Hazards ---
Lane A: x 18–22, y 16–28      Lane B: x 34–38, y 16–28

--- Gather ---
Fungal Cap: (12, 16)          Marsh Herb: (40, 24)
```

---

## Implementation Notes

- **Puzzle difficulty:** Simple 3-switch with generous 8s timer — introductory
- **Bud Node:** First time players see "kill adds before they empower" mechanic
- **Fog lanes:** Pulsing creates rhythm to movement — stop-and-go pacing
- **Shortcut:** QoL feature prevents tedious backtracking post-clear
- **Gate as barrier:** Physical gate blocks D2 until puzzle solved (no level gate)
