# Route Micro-Map: R02 — Ashveil Fellpath

## Route Overview

| Property | Value |
|----------|-------|
| **Route Name** | Ashveil Fellpath (R02) |
| **Theme** | Stone uplands, ruined statues, first Growth/ruin foreshadowing |
| **Encounter Level Band** | 8–15 |
| **Mounts** | OFF |
| **Map Size** | 80 × 48 (x 0–79, y 0–47) |

---

## Exits

| Destination | Coordinates | Notes |
|-------------|-------------|-------|
| **From Ashveil Sanctuary** | (8, 40) | Route start |
| **To Ruins of Ashveil (D1) Gate** | (72, 10) | Dungeon entrance |
| **Optional overlook (lore + chest)** | (50, 42) | Scenic reward |

---

## Key Anchors

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Sanctuary signpost | (12, 38) | "SANCTUARY ← / RUINS →" |
| Ruins warning obelisk | (68, 14) | *"Roots test the unready."* |
| Bridge choke | (40, 24) | Collapsed stone span |

---

## Terrain / Hazards

### Overrun Bramble Tiles (Growth Foreshadowing)

| Property | Value |
|----------|-------|
| **Zone** | x 34–46, y 22–26 |
| **Effect** | Slight move slowdown (not a debuff) |
| **Theme** | Introduces early Growth pressure before D1 |

### Falling Pebble Telegraph

| Property | Value |
|----------|-------|
| **Location** | Bridge choke (40, 24) |
| **Effect** | Cosmetic only (visual flavor) |

---

## Encounter Pockets (3)

### Pocket A (Foothills)

| Property | Value |
|----------|-------|
| **Location** | (22, 34) |
| **Composition** | 2× Upland Skirmisher + 1× Pebble Caster |

### Pocket B (Bridge)

| Property | Value |
|----------|-------|
| **Location** | (40, 26) |
| **Composition** | 3× Skirmisher + 1× Shield Brute |
| **Notes** | Mini-tank tutorial |

### Pocket C (Ruins Approach)

| Property | Value |
|----------|-------|
| **Location** | (64, 18) |
| **Composition** | 2× Skirmisher + 1× "Stone Wisp" |
| **Notes** | Teaches targeting priority |

---

## Interactables

| Type | Coordinates | Contents |
|------|-------------|----------|
| Chest (medium) | (54, 44) | Overlook reward |
| Gather: Stoneflower | (18, 18) | Crafting |
| Gather: Ore Node | (30, 12) | Materials |
| Lore slab | (62, 28) | *"The ruin began as a promise."* |

---

## Scripting Notes

### First Time at Ruins Gate

| Trigger | First entry to ruins gate |
|---------|---------------------------|
| **Effect** | 1-2 lines party VO about roots moving under stone |
| **Purpose** | Foreshadow D1 mechanics and Growth element |

---

## Quick Reference Coordinates

```
Ashveil entry: (8, 40)        D1 gate: (72, 10)
Sanctuary sign: (12, 38)      Warning obelisk: (68, 14)
Bridge choke: (40, 24)        Overlook: (50, 42)
Overlook chest: (54, 44)      Lore slab: (62, 28)

--- Pockets ---
A: (22, 34)                   B: (40, 26)
C: (64, 18)

--- Hazards ---
Bramble tiles: x 34-46, y 22-26
```

---

## Implementation Notes

- **Growth theme:** Use subtle visual/audio cues (root creaks, seed pulses) but no hard mechanics
- **Bridge choke:** Narrow passage creates natural combat chokepoint
- **Overlook reward:** Medium chest encourages exploration
- **Shield brute:** First enemy with significant HP pool — teaches sustained damage




