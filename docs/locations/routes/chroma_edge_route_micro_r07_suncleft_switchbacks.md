# Route Micro-Map: R07 — Suncleft Switchbacks

## Route Overview

| Property | Value |
|----------|-------|
| **Route Name** | Suncleft Switchbacks (R07) |
| **Theme** | Highlands → sun-baked cliffs → ember rock |
| **Encounter Level Band** | 32–42 |
| **Mounts** | ON |
| **Map Size** | 104 × 56 (x 0–103, y 0–55) |
| **Purpose** | Transition Light → Heat/Motion + introduce wind gust lanes |

---

## Exits

| Destination | Coordinates | Notes |
|-------------|-------------|-------|
| **From Prismridge side** | (10, 46) | Route start |
| **To Cinderstep gate** | (94, 18) | Town entrance |
| **Optional spur to Motion Shrine shelf** | (60, 8) | Blocked until Motion Shrine discovered |

---

## Key Anchors

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Switchback stairs visual | x 30–48, y 20–44 | Climbing path |
| Cliff ledge mid-rest | (52, 28) | Safe point |
| Ember rocks begin | x 70–96, y 10–28 | Heat theme transition |

---

## Terrain / Hazards

### A) Wind Gust Lanes (Non-Lethal, Positional)

| Lane | Coordinates | Pattern |
|------|-------------|---------|
| **Lane A** | x 36–40, y 22–34 | Vertical strip |
| **Lane B** | x 58–62, y 14–26 | Vertical strip |

#### Gust Mechanics

| Property | Value |
|----------|-------|
| **Cycle** | 12s |
| **Telegraph** | 1.0s wind lines |
| **Active** | 4.0s |
| **Effect** | Shove 1 tile + brief stagger |
| **Damage** | None |

### B) Sunstone Heat Tiles (Cosmetic + Tiny Pressure)

| Zone | Effect |
|------|--------|
| x 78–88, y 18–24 | Overheat +1 if standing still 2 turns |

**Teaching:** "Keep moving" before Skyspire Motion challenges

---

## Encounter Pockets (4, Climbing Intensity)

### Pocket A (Ridge Departure)

| Property | Value |
|----------|-------|
| **Location** | (24, 40) |
| **Composition** | 2× Prism Skirmisher + 1× Ridge Skirmisher |

### Pocket B (Switchbacks)

| Property | Value |
|----------|-------|
| **Location** | (40, 28) |
| **Composition** | 3× Cliff Skirmisher (melee) + 1× Wind Wisp |
| **Notes** | Wind Wisp applies shove-lite |

### Pocket C (Ledge)

| Property | Value |
|----------|-------|
| **Location** | (56, 24) |
| **Composition** | 1× Elite "Cliffbreaker" + 2× adds |
| **Notes** | Tier scaling |

### Pocket D (Ember Edge)

| Property | Value |
|----------|-------|
| **Location** | (86, 20) |
| **Composition** | 2× Ember Skirmisher + 1× Heat Runner |

---

## Interactables

| Type | Coordinates | Contents |
|------|-------------|----------|
| Chest (small) | (18, 16) | Consumables |
| Chest (medium) | (52, 10) | Ledge reward (reachable during gust lull) |
| Gather: Prism Shard Node | (34, 12) | Materials |
| Gather: Cinder Bloom | (82, 34) | First Heat-adjacent herb |
| Lore sign | (68, 14) | *"Past this line, the air burns faster."* |

---

## Gating

| Lock | Condition |
|------|-----------|
| **R07 opens** | `D3_CLEARED = TRUE` |

---

## Quick Reference Coordinates

```
Prismridge entry: (10, 46)    Cinderstep gate: (94, 18)
Motion spur: (60, 8) [blocked]
Switchbacks: x 30–48, y 20–44  Ledge: (52, 28)
Ember start: x 70–96, y 10–28

--- Pockets ---
A: (24, 40)                   B: (40, 28)
C: (56, 24)                   D: (86, 20)

--- Hazards ---
Gust Lane A: x 36–40, y 22–34
Gust Lane B: x 58–62, y 14–26
Heat tiles: x 78–88, y 18–24

--- Gather ---
Prism Shard: (34, 12)         Cinder Bloom: (82, 34)
```

---

## Implementation Notes

- **Tone shift:** Visual progression from crystal blues to ember reds
- **Wind introduction:** First forced movement hazard (non-lethal)
- **Heat tiles:** Teach movement patterns before Skyspire
- **Medium chest:** Rewards timing gust lanes correctly
- **Shrine teaser:** Motion Shrine path blocked until discovered
