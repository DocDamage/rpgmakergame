# Route Micro-Map: R15 — Phase-Lane Causeway

## Route Overview

| Property | Value |
|----------|-------|
| **Route Name** | Phase-Lane Causeway (R15 Micro) |
| **Theme** | Pier pylons → shimmering seam bridge → lane terminal |
| **Encounter Level Band** | 78–92 |
| **Mounts** | OFF |
| **Map Size** | 72 × 40 (x 0–71, y 0–39) |
| **Purpose** | "This is different tech." Teach phase timing + terminal interaction |

---

## Exits

| Destination | Coordinates | Notes |
|-------------|-------------|-------|
| **From Chronowake (pier gate)** | (10, 34) | Route start |
| **To Meridian Junction side** | (62, 10) | Terminal exit |
| **Optional side spur to Time Shrine cliffwalk** | (20, 8) | Alternate Time Shrine connection |

---

## Key Anchors

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Phase seam bridge spine | Diagonal (18, 30) to (54, 14) | Main path |
| Lane Terminal dais | (60, 10) | Travel hub |
| Cover pylons | (34, 22) and (44, 18) | Safe spots |

---

## Terrain / Hazards (Phase Timing, Readable)

### A) Phase Flicker Tiles (Don't End Turn Here)

| Zone | x 28–50, y 16–28 |
|------|------------------|
| **Cycle** | 10s |
| **Telegraph** | 1.4s shimmer grid |
| **Active** | 4.5s |
| **Effect** | Turn Delay +1 if you end turn on flicker tile while active |

### B) Seam Lash (Lane Strikes)

| Lane | Coordinates | Pattern |
|------|-------------|---------|
| **Lane A** | x 26–46 at y 22 | Horizontal |
| **Lane B** | x 34–54 at y 18 | Horizontal |

#### Seam Lash Mechanics

| Property | Value |
|----------|-------|
| **Cycle** | 14s (alternating) |
| **Telegraph** | 1.2s thin white line |
| **Impact** | Instant |
| **Effect** | Medium chip + brief stagger |

---

## Encounter Pockets (2–3)

### Pocket A (Pier Pylons)

| Property | Value |
|----------|-------|
| **Location** | (22, 28) |
| **Composition** | 2× Chrono Scriber + 1× Phase Scuttler |

### Pocket B (Mid Seam)

| Property | Value |
|----------|-------|
| **Location** | (40, 20) |
| **Composition** | 1× Elite "Lane Warden Drone" + 2× Phase Scuttler |
| **Notes** | Tier scaling |

### Pocket C (Terminal Guard, Optional)

| Property | Value |
|----------|-------|
| **Location** | (58, 12) |
| **Composition** | 1× Null Caster + 2× Scuttler |
| **Notes** | Makes terminal feel earned |

---

## Terminal Interaction (Exact UI)

| Element | Details |
|---------|---------|
| **Location** | (60, 10) |
| **Title** | `PHASE-LANE TERMINAL` |
| **Body** | `Select a stable vector.` |
| **Options (as unlocked)** | `MERIDIAN JUNCTION` / `(Later) AETHERREACH` (post-Final Palace) |
| **Buttons** | `[CONFIRM]` `[BACK]` |

---

## Interactables

| Type | Coordinates | Contents |
|------|-------------|----------|
| Chest (small) | (14, 10) | Consumables |
| Gather: Phase Filament | (52, 30) | Rare mat seed |
| Lore slab | (30, 12) | *"A road that isn't a road."* |

---

## Gating

| Lock | Condition |
|------|-----------|
| **R15 opens** | `CHRONOWAKE_ARRIVED = TRUE` |
| **Terminal active** | `PHASE_KEY_OBTAINED = TRUE` (if story needs it) |

---

## Post-Clear QoL

| Condition | Effect |
|-----------|--------|
| First successful terminal use | Return Toggle: "Return to Chronowake?" |

---

## Quick Reference Coordinates

```
Chronowake entry: (10, 34)    Meridian exit: (62, 10)
Bridge spine: (18,30)→(54,14) Terminal: (60, 10)
Time Shrine spur: (20, 8)

--- Cover ---
Pylon 1: (34, 22)             Pylon 2: (44, 18)

--- Pockets ---
A: (22, 28)                   B: (40, 20)
C (optional): (58, 12)

--- Hazards ---
Flicker field: x 28–50, y 16–28 (10s cycle)
Seam Lane A: x 26–46, y 22     Seam Lane B: x 34–54, y 18

--- Gather ---
Phase Filament: (52, 30)
```

---

## Implementation Notes

- **Phase seam:** Visual "different tech" from standard routes
- **Flicker tiles:** First appearance of Turn Delay hazard
- **Seam lash:** Alternating lanes create movement puzzle
- **Lane Warden Drone:** Chrono/phase hybrid elite
- **Terminal UI:** Clean selection interface for Phase-Lane travel
- **Aetherreach unlock:** Terminal option appears post-Final Palace
