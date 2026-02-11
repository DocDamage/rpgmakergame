# Route Micro-Map: R14 — Glacier Shelfway

## Route Overview

| Property | Value |
|----------|-------|
| **Route Name** | Glacier Shelfway (R14) |
| **Theme** | Ice shelf cliffs → aurora fog → chrono shoreline pylons |
| **Encounter Level Band** | 72–86 |
| **Mounts** | ON (recommend: -15% speed in shelf gust zones) |
| **Map Size** | 128 × 56 (x 0–127, y 0–55) |
| **Purpose** | Connects Frostmarch to Chrono coast; introduces "time eddy" tiles |

---

## Exits

| Destination | Coordinates | Notes |
|-------------|-------------|-------|
| **From Rimehold side** | (10, 46) | Route start |
| **To Chronowake gate** | (118, 18) | Town entrance |
| **Optional spur to Time Shrine approach** | (96, 10) | Opens when Time Shrine discovered or first Chronowake arrival |

---

## Key Anchors

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Shelf cliff choke | x 44–60, y 14–36 | Guardrails + windbreak stones |
| Aurora fog basin | x 64–90, y 20–44 | Soft glow, mood shift |
| Chrono pylon line | x 98–120, y 14–24 | Approaching town |

---

## Terrain / Hazards

### A) Shelf Gust Lanes (Positional)

| Lane | Coordinates | Pattern |
|------|-------------|---------|
| **Lane A** | x 50–54, y 18–30 | Vertical strip |
| **Lane B** | x 78–82, y 26–38 | Vertical strip |

#### Gust Mechanics

| Property | Value |
|----------|-------|
| **Cycle** | 12s |
| **Telegraph** | 1.2s white shear lines |
| **Active** | 3.5s |
| **Effect** | Shove 1 tile sideways + brief stagger (no damage) |

### B) Time Eddy Patches (Time-Lite)

| Patch | Coordinates | Size |
|-------|-------------|------|
| **Patch 1** | (70, 30) | 3×3 |
| **Patch 2** | (88, 34) | 3×3 |

#### Time Eddy Mechanics

| Property | Value |
|----------|-------|
| **Cycle** | 14s |
| **Telegraph** | 1.6s clock-shimmer |
| **Active** | 5.0s |
| **Effect** | SLOW 6s (no damage) |

---

## Encounter Pockets (4)

### Pocket A (Departing Rimehold)

| Property | Value |
|----------|-------|
| **Location** | (24, 40) |
| **Composition** | 2× Frost Skirmisher + 1× Chrono Scriber |

### Pocket B (Shelf Choke)

| Property | Value |
|----------|-------|
| **Location** | (52, 26) |
| **Composition** | 1× Elite "Shelf Sentinel" + 2× Frost Skirmisher |
| **Notes** | Tier scaling |

### Pocket C (Aurora Basin)

| Property | Value |
|----------|-------|
| **Location** | (76, 34) |
| **Composition** | 2× Chrono Scriber + 1× Chill Caster + 1× "Time Wisp" |
| **Notes** | Telegraph poke |

### Pocket D (Near Chronowake Pylons)

| Property | Value |
|----------|-------|
| **Location** | (110, 20) |
| **Composition** | 2× "Phase Scuttler" + 1× Null Caster |
| **Notes** | Act 2+ flavor |

---

## Interactables

| Type | Coordinates | Contents |
|------|-------------|----------|
| Chest (small) | (18, 12) | Consumables |
| Chest (medium) | (84, 18) | Guarded by Pocket C |
| Gather: Frost Lichen | (44, 10) | Crafting |
| Gather: Chrono Shard | (92, 26) | Rare mat |
| Lore post | (66, 16) | *"The coastline ticks."* |

---

## Gating

| Lock | Condition |
|------|-----------|
| **R14 opens** | `D7_CLEARED = TRUE` (or Rimehold main beat for earlier access) |

---

## Post-Route QoL

| Condition | Effect |
|-----------|--------|
| First Chronowake arrival | One-way sled chute at (62, 12) → drops to (28, 40) |

---

## Quick Reference Coordinates

```
Rimehold entry: (10, 46)      Chronowake gate: (118, 18)
Time Shrine spur: (96, 10)
Shelf choke: x 44–60, y 14–36  Aurora basin: x 64–90, y 20–44
Chrono pylons: x 98–120, y 14–24
Shortcut sled: (62, 12) → (28, 40)

--- Pockets ---
A: (24, 40)                   B: (52, 26)
C: (76, 34)                   D: (110, 20)

--- Hazards ---
Gust Lane A: x 50–54, y 18–30
Gust Lane B: x 78–82, y 26–38
Time Eddy 1: (70, 30)         Time Eddy 2: (88, 34)

--- Gather ---
Frost Lichen: (44, 10)        Chrono Shard: (92, 26)
```

---

## Implementation Notes

- **Aurora fog:** Visual mood shift from ice blues to chrono purples
- **Time eddies:** First Time element hazards outside of Time zone
- **Shelf Sentinel:** Elite tuned for tier 72–86
- **Phase Scuttler:** Chrono/phase hybrid enemy type
- **Sled chute:** One-way fast return post-discovery
