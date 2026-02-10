# Route Micro-Map: R09 — Saltflare Coastway

## Route Overview

| Property | Value |
|----------|-------|
| **Route Name** | Saltflare Coastway (R09) |
| **Theme** | Ember rock → cliff coast → salt flats → port lights |
| **Encounter Level Band** | 40–52 |
| **Mounts** | ON |
| **Map Size** | 120 × 56 (x 0–119, y 0–55) |
| **Purpose** | Transition volcanic rim → Tide arc; introduces "surf lanes" + wet footing |

---

## Exits

| Destination | Coordinates | Notes |
|-------------|-------------|-------|
| **From Cinderstep side** | (10, 46) | Route start |
| **To Brinegate gate** | (110, 18) | Port town entrance |
| **Optional spur to Marinus's Sanctum node** | (86, 44) | Unlocks when Brinegate main beat starts or Tide key obtained |

---

## Key Anchors

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Cliff switchdown | x 26–44, y 18–44 | Descent path |
| Tidepool shelf | x 54–76, y 24–40 | Coastal shelf terrain |
| Port lantern line | x 96–114, y 16–24 | Approaching Brinegate |

---

## Terrain / Hazards

### A) Surf Wash Lanes (Positional + Tiny Chip)

| Lane | Coordinates | Pattern |
|------|-------------|---------|
| **Lane A** | x 58–64, y 28–38 | Vertical strip |
| **Lane B** | x 70–74, y 22–32 | Vertical strip |

#### Surf Mechanics

| Property | Value |
|----------|-------|
| **Cycle** | 12s |
| **Telegraph** | 1.2s foam line |
| **Active** | 3.5s |
| **Effect** | Shove 1 tile toward inland + small chip |
| **Status** | None |

### B) Slick Rock Tiles (Teach "Don't End Turn Here")

| Zone | Effect |
|------|--------|
| x 60–76, y 40–46 | End turn on slick rock during active surf → brief stagger |

---

## Encounter Pockets (4, Coastal Escalation)

### Pocket A (Embers Fade)

| Property | Value |
|----------|-------|
| **Location** | (24, 40) |
| **Composition** | 2× Ember Skirmisher + 1× Heat Runner |

### Pocket B (Cliff Shelf)

| Property | Value |
|----------|-------|
| **Location** | (38, 26) |
| **Composition** | 2× Cliff Skirmisher + 1× Wind Wisp (shove-lite) |

### Pocket C (Tidepools)

| Property | Value |
|----------|-------|
| **Location** | (66, 32) |
| **Composition** | 3× Tide Scuttler + 1× Brine Caster (wet poke) |

### Pocket D (Near Port)

| Property | Value |
|----------|-------|
| **Location** | (102, 20) |
| **Composition** | 1× Elite "Dockbreaker" + 2× Tide Scuttler |
| **Notes** | Tier scaling |

---

## Interactables

| Type | Coordinates | Contents |
|------|-------------|----------|
| Chest (small) | (18, 14) | Consumables |
| Chest (medium) | (74, 26) | Timing reward (between surf cycles) |
| Gather: Salt Kelp | (62, 20) | Crafting |
| Gather: Brine Resin | (84, 30) | Tide crafting |
| Lore sign | (52, 18) | *"The sea eats fire. Slowly."* |

---

## Gating

| Lock | Condition |
|------|-----------|
| **R09 opens** | `D4_CLEARED = TRUE` (or arrival beat to Cinderstep coast quest) |

---

## Quick Reference Coordinates

```
Cinderstep entry: (10, 46)    Brinegate gate: (110, 18)
Marinus spur: (86, 44)
Cliff switchdown: x 26–44, y 18–44
Tidepool shelf: x 54–76, y 24–40
Port lanterns: x 96–114, y 16–24

--- Pockets ---
A: (24, 40)                   B: (38, 26)
C: (66, 32)                   D: (102, 20)

--- Hazards ---
Surf Lane A: x 58–64, y 28–38
Surf Lane B: x 70–74, y 22–32
Slick rock: x 60–76, y 40–46

--- Gather ---
Salt Kelp: (62, 20)           Brine Resin: (84, 30)
```

---

## Implementation Notes

- **Tone shift:** Visual transition from volcanic reds to ocean blues/greens
- **Surf lanes:** First water-themed forced movement
- **Slick rock:** Teaches positional awareness (don't end turn in bad spots)
- **Medium chest:** Rewards timing surf cycles correctly
- **Marinus spur:** Optional shrine path unlocks with story progress
