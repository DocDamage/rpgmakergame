# Route Micro-Map: R03 — Marshroad Way

## Route Overview

| Property | Value |
|----------|-------|
| **Route Name** | Marshroad Way (R03) |
| **Theme** | Scrub forest → wetland edge → Mirewatch palisade |
| **Encounter Level Band** | 12–22 |
| **Mounts** | ON (optional) or OFF |
| **Map Size** | 104 × 56 (x 0–103, y 0–55) |

---

## Exits

| Destination | Coordinates | Notes |
|-------------|-------------|-------|
| **From Ashveil side** | (10, 46) | Route start |
| **To Mirewatch gate** | (94, 18) | Town entrance |
| **Side spur to Growth Shrine marker** | (30, 10) | Blocked by thick vines until shrine discovered |

---

## Key Anchors

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Wetland warning sign | (28, 34) | "WATCH YOUR STEP" |
| Boardwalk stretch | x 44–70, y 26–30 | Visual variety |
| Mirewatch lantern line | x 80–96, y 18–22 | Approaching town |

---

## Terrain / Hazards (First Real Status-Lite)

### Bog Tiles (Slow)

| Zone | Effect |
|------|--------|
| x 20–38, y 18–32 | Movement slowdown |

### Spore Puff Patches (Minor Debuff Intro)

| Patch | Coordinates | Size |
|-------|-------------|------|
| Patch 1 | (54, 22) | 3×3 |
| Patch 2 | (62, 34) | 3×3 |

#### Spore Puff Mechanics

| Property | Value |
|----------|-------|
| **Pulse cycle** | 10s |
| **Telegraph** | 1.2s (visible puff + soft hiss) |
| **Active** | 3.0s |
| **Effect** | "Spore Haze" (accuracy down-lite) for 6s |

---

## Encounter Pockets (4, with Breathing Room)

### Pocket A

| Property | Value |
|----------|-------|
| **Location** | (24, 40) |
| **Composition** | 2× Marsh Skirmisher + 1× Leechling |

### Pocket B (Bog)

| Property | Value |
|----------|-------|
| **Location** | (34, 26) |
| **Composition** | 2× Leechling + 1× Sporeling |
| **Notes** | Sporeling applies haze debuff |

### Pocket C (Boardwalk)

| Property | Value |
|----------|-------|
| **Location** | (58, 28) |
| **Composition** | 3× Marsh Skirmisher |
| **Notes** | Positioning check (narrow path) |

### Pocket D (Near Town)

| Property | Value |
|----------|-------|
| **Location** | (86, 20) |
| **Composition** | 1× Elite "Mire Bully" + 2× adds |
| **Notes** | Tier scaling; can be non-elite early |

---

## Interactables

| Type | Coordinates | Contents |
|------|-------------|----------|
| Chest (small) | (16, 12) | Consumables |
| Chest (small) | (74, 44) | Materials |
| Gather: Marsh Herb | (40, 10) | Crafting |
| Gather: Fungal Cap | (66, 40) | Crafting |
| Lore post | (50, 14) | *"Mirewatch keeps the lights on. Barely."* |

---

## Gating

| Lock | Condition |
|------|-----------|
| **R03 opens** | `ASHVEIL_MAIN_BEAT_DONE = TRUE` (leave sanctuary story beat) |

---

## Quick Reference Coordinates

```
Ashveil entry: (10, 46)       Mirewatch gate: (94, 18)
Warning sign: (28, 34)        Boardwalk: x 44–70, y 26–30
Lantern line: x 80–96, y 18–22
Shrine spur: (30, 10) [blocked]

--- Pockets ---
A: (24, 40)                   B: (34, 26)
C: (58, 28)                   D: (86, 20)

--- Hazards ---
Bog: x 20–38, y 18–32
Spore 1: (54, 22)             Spore 2: (62, 34)

--- Gather ---
Marsh Herb: (40, 10)          Fungal Cap: (66, 40)
```

---

## Implementation Notes

- **First real hazards:** Spore puffs introduce debuff mechanics gently
- **Boardwalk variety:** Breaks up terrain monotony
- **Elite introduction:** Mire Bully is first named enemy on route
- **Shrine teaser:** Blocked path to Growth Shrine creates mystery
- **Mount decision:** Enable if introduced by this point; otherwise keep OFF
