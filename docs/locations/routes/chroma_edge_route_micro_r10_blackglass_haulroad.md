# Route Micro-Map: R10 — Blackglass Haulroad

## Route Overview

| Property | Value |
|----------|-------|
| **Route Name** | Blackglass Haulroad (R10) |
| **Theme** | Ember ridges → obsidian flats → quarry rigs → molten glow |
| **Encounter Level Band** | 48–60 |
| **Mounts** | ON |
| **Map Size** | 104 × 56 (x 0–103, y 0–55) |
| **Purpose** | Pre-D6 quarry run; mixes heat hazards with Mass foreshadowing |

---

## Exits

| Destination | Coordinates | Notes |
|-------------|-------------|-------|
| **From Cinderstep side** | (10, 46) | Route start |
| **To Obsidian Quarry (D6) gate** | (94, 16) | Dungeon entrance |
| **Optional spur to Heat Shrine node** | (62, 8) | Unlocks after first quarry approach or shrine discovered |

---

## Key Anchors

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Haulroad signpost | (16, 44) | "CINDERSTEP ← / QUARRY →" |
| Quarry silhouette overlook | (52, 18) | Scenic view |
| Rig lane corridor | x 70–92, y 12–30 | Mine carts + pylons create cover |

---

## Terrain / Hazards

### A) Heat Vents (Chip + Overheat)

| Patch | Coordinates | Size |
|-------|-------------|------|
| **Vent Patch 1** | (34, 34) | 3×3 |
| **Vent Patch 2** | (76, 22) | 3×3 |

#### Vent Mechanics

| Property | Value |
|----------|-------|
| **Cycle** | 12s |
| **Telegraph** | 1.4s orange glow + hiss |
| **Active** | 3.0s |
| **Effect** | Small chip + Overheat +2 |

### B) Slagfall (Telegraphed Drops)

| Trigger | Player enters quarry corridor (x≥68) |
|---------|--------------------------------------|
| **Frequency** | Every 18s |
| **Telegraph** | 1.2s falling sparks |
| **Drop Tiles** | (74, 18), (80, 18), (86, 18) |
| **Effect** | Medium chip + brief stagger |

### C) Blackglass Tiles (Cosmetic Friction)

| Zone | Effect |
|------|--------|
| x 54–66, y 26–36 | Slight move slowdown (no combat debuff) |

---

## Encounter Pockets (4, Quarry-Focused)

### Pocket A (Ember Badlands)

| Property | Value |
|----------|-------|
| **Location** | (24, 40) |
| **Composition** | 2× Ember Skirmisher + 1× Heat Runner |

### Pocket B (Vent Field)

| Property | Value |
|----------|-------|
| **Location** | (36, 30) |
| **Composition** | 2× Cinder Caster + 2× Ember Skirmisher |

### Pocket C (Obsidian Flats)

| Property | Value |
|----------|-------|
| **Location** | (58, 26) |
| **Composition** | 1× Elite "Blackglass Brute" + 2× adds |
| **Notes** | Tier scaling |

### Pocket D (Quarry Corridor)

| Property | Value |
|----------|-------|
| **Location** | (82, 20) |
| **Composition** | 2× Heat Runner + 1× "Slag Mote" |
| **Notes** | Slag Mote dies fast; teaches target swap |

---

## Interactables

| Type | Coordinates | Contents |
|------|-------------|----------|
| Chest (small) | (20, 14) | Consumables |
| Chest (medium) | (62, 44) | Side spur behind vent timing |
| Gather: Ash Resin | (30, 12) | Crafting |
| Gather: Obsidian Chip Node | (56, 14) | First D6 mat drip |
| Lore sign | (70, 10) | *"They dug for power. Power dug back."* |

---

## Gating

| Lock | Condition |
|------|-----------|
| **R10 opens** | `D5_PROGRESS_BEAT_DONE = TRUE` (or Brinegate main beat) |
| **Heat Shrine spur** | `R10_FIRST_ENTER = TRUE` |

---

## Quick Reference Coordinates

```
Cinderstep entry: (10, 46)    D6 gate: (94, 16)
Heat Shrine spur: (62, 8)
Signpost: (16, 44)            Overlook: (52, 18)
Rig corridor: x 70–92, y 12–30

--- Pockets ---
A: (24, 40)                   B: (36, 30)
C: (58, 26)                   D: (82, 20)

--- Hazards ---
Vent 1: (34, 34)              Vent 2: (76, 22)
Slagfall tiles: (74,18) (80,18) (86,18)
Blackglass: x 54–66, y 26–36

--- Gather ---
Ash Resin: (30, 12)           Obsidian Chip: (56, 14)
```

---

## Implementation Notes

- **Mass foreshadow:** heavy rig lane and elite pressure preview D6 pacing
- **Slagfall telegraph:** Clear visual warning before impact
- **Slag Mote:** Fast-spawning add teaches target priority
- **Blackglass Brute:** Heavy Heat-themed elite
- **Medium chest:** Rewards timing vent cycles correctly
