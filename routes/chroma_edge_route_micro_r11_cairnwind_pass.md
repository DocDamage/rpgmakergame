# Route Micro-Map: R11 — Cairnwind Pass

## Route Overview

| Property | Value |
|----------|-------|
| **Route Name** | Cairnwind Pass (R11) |
| **Theme** | Upland stone → wind-cut pass → first snow line → bleak outpost road |
| **Encounter Level Band** | 52–66 |
| **Mounts** | ON |
| **Map Size** | 120 × 56 (x 0–119, y 0–55) |
| **Purpose** | Major "world opens" route; introduces cold gust lanes + rockslide telegraph |

---

## Exits

| Destination | Coordinates | Notes |
|-------------|-------------|-------|
| **From Ashveil side** | (10, 46) | Route start |
| **To Gravemark Outpost gate** | (110, 18) | Town entrance |
| **Optional hidden spur** | (16, 10) | Dragon's Graveyard teaser (blocked until late flag) |

---

## Key Anchors

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Northbound Gate Obelisk | (28, 36) | Story gate |
| Pass choke / bridge | (58, 26) | Narrow crossing |
| Snowline shift | x 70–92, y 10–30 | Terrain palette swap |

---

## Terrain / Hazards

### A) Cold Gust Lanes (Positional)

| Lane | Coordinates | Pattern |
|------|-------------|---------|
| **Lane A** | x 40–44, y 22–34 | Vertical strip |
| **Lane B** | x 78–82, y 14–26 | Vertical strip |

#### Gust Mechanics

| Property | Value |
|----------|-------|
| **Cycle** | 12s |
| **Telegraph** | 1.0s white wind lines |
| **Active** | 4.0s |
| **Effect** | Shove 1 tile sideways + brief stagger (no damage) |

### B) Rockslide (Telegraphed Impact Zones)

| Zone | x 52–64 (pass choke only) |
|------|---------------------------|
| **Frequency** | Every 20s |
| **Telegraph** | 1.6s rumble + pebbles |
| **Impact Tiles** | (56, 24), (58, 24), (60, 24) |
| **Effect** | Medium damage + normal hit (no Integrity system here) |

---

## Encounter Pockets (4, "Midgame North" Vibe)

### Pocket A (Upland Exit)

| Property | Value |
|----------|-------|
| **Location** | (24, 40) |
| **Composition** | 2× Upland Skirmisher + 1× Chrono Scriber |
| **Notes** | Introduce time-lite early |

### Pocket B (Gate Obelisk)

| Property | Value |
|----------|-------|
| **Location** | (32, 34) |
| **Composition** | 2× Shield Brute + 1× Wind Wisp |

### Pocket C (Bridge Choke)

| Property | Value |
|----------|-------|
| **Location** | (58, 26) |
| **Composition** | 1× Elite "Cairn Sentinel" + 2× adds |
| **Notes** | Tier scaling |

### Pocket D (Snowline Approach)

| Property | Value |
|----------|-------|
| **Location** | (96, 18) |
| **Composition** | 2× Frost Skirmisher + 1× "Chill Caster" |
| **Notes** | Slow-lite debuff |

---

## Interactables

| Type | Coordinates | Contents |
|------|-------------|----------|
| Chest (small) | (18, 16) | Consumables |
| Chest (small) | (88, 40) | Materials |
| Gather: Stoneflower | (44, 12) | Crafting |
| Gather: Frost Lichen | (82, 34) | Crafting |
| Lore cairn | (60, 16) | *"The dead don't rest. They wait."* |

---

## Gating

| Lock | Condition |
|------|-----------|
| **R11 opens** | `ACT2_RIFT_OVERLAY = TRUE` (post-D4 catastrophe) |
| **Early approach message** | "PASS SEALED BY STORM." |

---

## Quick Reference Coordinates

```
Ashveil entry: (10, 46)       Gravemark gate: (110, 18)
Graveyard spur: (16, 10) [blocked late]
Gate Obelisk: (28, 36)        Bridge choke: (58, 26)
Snowline: x 70–92, y 10–30

--- Pockets ---
A: (24, 40)                   B: (32, 34)
C: (58, 26)                   D: (96, 18)

--- Hazards ---
Gust Lane A: x 40–44, y 22–34
Gust Lane B: x 78–82, y 14–26
Rockslide: x 52–64 (tiles 56,24 / 58,24 / 60,24)

--- Gather ---
Stoneflower: (44, 12)         Frost Lichen: (82, 34)
```

---

## Implementation Notes

- **World opens moment:** Pass unlocks after Act 2 catastrophe
- **Chrono Scriber:** First Time element enemy outside of Time zones
- **Cairn Sentinel:** Heavily armored elite for chokepoint fight
- **Dragon's Graveyard teaser:** Blocked path creates late-game mystery
- **Rockslide:** Uses standard damage (not Integrity system)
