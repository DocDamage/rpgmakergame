# Route Micro-Map: R05 — Glimmerfen Ridgepath

## Route Overview

| Property | Value |
|----------|-------|
| **Route Name** | Glimmerfen Ridgepath (R05) |
| **Theme** | Wetland edge → mossy rise → prismatic stone outcrops |
| **Encounter Level Band** | 22–32 |
| **Mounts** | ON (if unlocked; otherwise OFF) |
| **Map Size** | 112 × 56 (x 0–111, y 0–55) |
| **Purpose** | Bridge "mire" tone into "prism" tone + introduce light hazards softly |

---

## Exits

| Destination | Coordinates | Notes |
|-------------|-------------|-------|
| **From Mirewatch side** | (10, 46) | Route start |
| **To Prismridge gate** | (102, 16) | Town entrance |
| **Optional spur to Growth Shrine node** | (20, 10) | Blocked until Growth Shrine discovered |

---

## Key Anchors

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Boardwalk → stone path transition | x 34–46, y 34–38 | Visual shift point |
| Ridge overlook (camera moment) | (56, 18) | Scenic vista |
| Prism boulder field | x 70–92, y 14–30 | Light theme terrain |

---

## Terrain / Hazards

### A) Bog Tiles (Minor, Early Stretch Only)

| Zone | Effect |
|------|--------|
| x 16–30, y 30–44 | Slow movement |

### B) Prism Glare Patches (Intro to Light)

| Patch | Coordinates | Size |
|-------|-------------|------|
| Patch 1 | (62, 26) | 3×3 |
| Patch 2 | (80, 22) | 3×3 |

#### Glare Mechanics

| Property | Value |
|----------|-------|
| **Cycle** | 14s |
| **Telegraph** | 1.6s shimmer |
| **Active** | 5.0s |
| **Effect** | Dazzled-lite (accuracy down short) |
| **Damage** | None (teaches readability) |

---

## Encounter Pockets (4, Breathable)

### Pocket A (Mire Tail)

| Property | Value |
|----------|-------|
| **Location** | (24, 40) |
| **Composition** | 2× Marsh Skirmisher + 1× Sporeling |

### Pocket B (Transition Rise)

| Property | Value |
|----------|-------|
| **Location** | (42, 32) |
| **Composition** | 3× Ridge Skirmisher (melee) |

### Pocket C (Prism Field)

| Property | Value |
|----------|-------|
| **Location** | (78, 24) |
| **Composition** | 2× Prism Skirmisher (ranged line) + 1× Stone Wisp |

### Pocket D (Near Town)

| Property | Value |
|----------|-------|
| **Location** | (94, 18) |
| **Composition** | 1× Elite "Gleam Stalker" + 2× adds |
| **Notes** | Tier scaling; can be non-elite at low end |

---

## Interactables

| Type | Coordinates | Contents |
|------|-------------|----------|
| Chest (small) | (18, 14) | Consumables |
| Chest (small) | (86, 34) | Materials |
| Gather: Fungal Cap | (36, 12) | Crafting |
| Gather: Prism Shard Node | (74, 16) | First "crystal" material trickle |
| Lore post | (56, 20) | *"The ridge catches light like a blade."* |

---

## Gating

| Lock | Condition |
|------|-----------|
| **R05 opens** | `D2_CLEARED = TRUE` (or Mirewatch main beat) |

---

## Quick Reference Coordinates

```
Mirewatch entry: (10, 46)     Prismridge gate: (102, 16)
Shrine spur: (20, 10) [blocked]
Transition: x 34–46, y 34–38   Overlook: (56, 18)
Boulder field: x 70–92, y 14–30

--- Pockets ---
A: (24, 40)                   B: (42, 32)
C: (78, 24)                   D: (94, 18)

--- Hazards ---
Bog: x 16–30, y 30–44
Glare 1: (62, 26)             Glare 2: (80, 22)

--- Gather ---
Fungal Cap: (36, 12)          Prism Shard: (74, 16)
```

---

## Implementation Notes

- **Tone bridge:** Visual shift from moss/wet to stone/crystal
- **Light introduction:** Glare patches are harmless but teach timing
- **Prism Skirmishers:** First enemies with line attacks — teaches positioning
- **Elite scaling:** Gleam Stalker scales with party level
- **Shrine teaser:** Blocked path creates mystery for Growth Shrine
