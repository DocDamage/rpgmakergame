# Route Micro-Map: R12 — Frostmarch Iceway

## Route Overview

| Property | Value |
|----------|-------|
| **Route Name** | Frostmarch Iceway (R12) |
| **Theme** | Dead pines → frozen flats → ice ridges → Rimehold lanterns |
| **Encounter Level Band** | 60–74 |
| **Mounts** | ON (speed limit if system supports) |
| **Map Size** | 112 × 56 (x 0–111, y 0–55) |
| **Purpose** | Long north route; introduces slick ice + whiteout pulses |

---

## Exits

| Destination | Coordinates | Notes |
|-------------|-------------|-------|
| **From Gravemark side** | (10, 46) | Route start |
| **To Rimehold gate** | (102, 18) | Town entrance |
| **Optional spur to Mass Shrine node** | (30, 10) | Gravestone Monad (unlocks on arrival or discovery) |

---

## Key Anchors

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Ice ridge corridor | x 38–64, y 18–40 | Walls funnel combat |
| Frozen lake crossing | x 66–88, y 28–42 | Open space |
| Rimehold lantern line | x 92–108, y 16–24 | Approaching town |

---

## Terrain / Hazards

### A) Slick Ice Tiles (Movement Risk)

| Zone | Rule |
|------|------|
| x 42–62, y 24–36 | End turn on ice: 25% chance of Slip (1 tile reposition) |

### B) Whiteout Pulse (Visibility + Aim Pressure)

| Property | Value |
|----------|-------|
| **Cycle** | 18s |
| **Telegraph** | 1.8s soft howl |
| **Active** | 6.0s |
| **Zone** | x 66–88, y 22–44 |
| **Effect** | Accuracy down-lite + ranged telegraphs dimmer (still visible) |

---

## Encounter Pockets (4, Frosty Escalation)

### Pocket A (Dead Pines)

| Property | Value |
|----------|-------|
| **Location** | (24, 40) |
| **Composition** | 2× Frost Skirmisher + 1× Chill Caster |

### Pocket B (Ice Corridor)

| Property | Value |
|----------|-------|
| **Location** | (50, 30) |
| **Composition** | 3× Frost Skirmisher + 1× "Ice Shardling" |
| **Notes** | Ranged poke |

### Pocket C (Lake Crossing)

| Property | Value |
|----------|-------|
| **Location** | (78, 34) |
| **Composition** | 1× Elite "Frostbound Enforcer" + 2× adds |
| **Notes** | Tier scaling |

### Pocket D (Near Town)

| Property | Value |
|----------|-------|
| **Location** | (96, 20) |
| **Composition** | 2× Chill Caster + 1× Grav Sentinel |
| **Notes** | Optional: introduce weight pull here |

---

## Interactables

| Type | Coordinates | Contents |
|------|-------------|----------|
| Chest (small) | (18, 12) | Consumables |
| Chest (medium) | (72, 18) | Lake crossing reward (easier during non-whiteout) |
| Gather: Frost Lichen | (44, 14) | Crafting |
| Gather: Ice Crystal Node | (84, 26) | Materials |
| Lore post | (66, 20) | *"Rimehold doesn't welcome. It endures."* |

---

## Gating

| Lock | Condition |
|------|-----------|
| **R12 opens** | `R11_COMPLETED = TRUE` (first time reaching Gravemark) |
| **Rimehold guard check** | Optional one-time story gate |

---

## Quick Reference Coordinates

```
Gravemark entry: (10, 46)     Rimehold gate: (102, 18)
Mass Shrine spur: (30, 10)
Ice corridor: x 38–64, y 18–40
Lake crossing: x 66–88, y 28–42
Lanterns: x 92–108, y 16–24

--- Pockets ---
A: (24, 40)                   B: (50, 30)
C: (78, 34)                   D: (96, 20)

--- Hazards ---
Slick ice: x 42–62, y 24–36 (25% slip chance)
Whiteout: x 66–88, y 22–44 (18s cycle)

--- Gather ---
Frost Lichen: (44, 14)        Ice Crystal: (84, 26)
```

---

## Implementation Notes

- **Ice slip:** Keep at 25% to avoid frustration; adds flavor without chaos
- **Whiteout:** 6s duration creates windows of vulnerability
- **Medium chest:** Easier fight during clear weather = reward for timing
- **Grav Sentinel:** Optional Mass element introduction in Frost zone
- **Mass Shrine spur:** Gravestone Monad access
