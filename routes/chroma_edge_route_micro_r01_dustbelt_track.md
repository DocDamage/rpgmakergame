# Route Micro-Map: R01 — Dustbelt Track

## Route Overview

| Property | Value |
|----------|-------|
| **Route Name** | Dustbelt Track (R01) |
| **Theme** | Dry flats → scrub canyon → upland foothills |
| **Encounter Level Band** | 1–8 (early tutorial pacing) |
| **Mounts** | OFF (early game) |
| **Segments** | R01a (Outskirts) + R01b (Dustbelt Track) |

---

## R01a — Dusthaven Outskirts (Micro)

| Property | Value |
|----------|-------|
| **Map Size** | 48 × 32 (x 0–47, y 0–31) |
| **Purpose** | Transition zone + first tutorial encounter pocket + first gather nodes |

### Exits

| Destination | Coordinates | Notes |
|-------------|-------------|-------|
| **To Dusthaven Town** | (24, 30) | Return gate |
| **To R01b Dustbelt Track** | (44, 14) | Main route forward |
| **Optional side spur (Scrap Drift alcove)** | (6, 10) | Dead-end loot |

### Key Anchors

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Town gate signpost | (24, 26) | "ASHVEIL ROAD →" |
| Tutorial encounter trigger strip | y = 18 (x 18–30) | First combat tutorial |

### Terrain / Hazards

| Feature | Details |
|---------|---------|
| **Blockers** | Soft blockers only (fences, broken carts) — funnel camera learning |
| **Sand slow tiles (optional)** | x 10–18, y 12–16 — minor slowdown |
| **Lethal hazards** | None |

### Encounter Pocket (Fixed, First-Time Only)

| Trigger | y ≤ 18 |
| Flag | `R01_TUTORIAL_FIGHT_DONE` (one-time) |

#### Composition

| Enemy | Count |
|-------|-------|
| Dust Skirmisher | 2 |
| Sling Scavenger | 1 | Ranged tutorial |

### Interactables

| Type | Coordinates | Contents |
|------|-------------|----------|
| Gather: Scrap Pile | (10, 22) | Materials |
| Gather: Dry Herb | (14, 12) | Crafting |
| Chest (small) | (8, 8) | Early consumables + currency |
| Lore sign | (20, 10) | *"The dust never forgets footprints."* |

### Scripting Notes

- **First-time only:** Show Route UI tutorial (minimap, encounter warning, gather sparkle)
- **Block return to Dusthaven** only during tutorial fight; otherwise free

---

## R01b — Dustbelt Track (Main Route Micro)

| Property | Value |
|----------|-------|
| **Map Size** | 96 × 40 (x 0–95, y 0–39) |
| **Purpose** | First "real" route; introduces fork + camp vendor |

### Exits

| Destination | Coordinates | Notes |
|-------------|-------------|-------|
| **From Outskirts entry** | (4, 20) | Entry point |
| **To Ashveil Sanctuary approach** | (92, 12) | Route end |
| **Optional fork to Growth Shrine spur** | (60, 30) | Locked (bramble wall) |

### Key Anchors

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Route start signpost | (10, 20) | "DUSTHAVEN ← / ASHVEIL →" |
| Camp vendor spot (optional) | (48, 22) | Road merchant |
| Fork marker | (60, 26) | Shrine path indicator |

### Terrain / Hazards

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Canyon chokepoint** | x 34–46, y 16–26 | Good for early combat readability |
| **Status hazards** | None | Save for R03/R04 |

### Encounter Pockets (3 Total, Light Pacing)

#### Pocket A

| Property | Value |
|----------|-------|
| **Location** | (22, 22) |
| **Composition** | 2× Dust Skirmisher + 1× Sling Scavenger |

#### Pocket B (Canyon)

| Property | Value |
|----------|-------|
| **Location** | (40, 22) |
| **Composition** | 3× Dust Skirmisher (melee focus) |

#### Pocket C (Near Exit)

| Property | Value |
|----------|-------|
| **Location** | (78, 14) |
| **Composition** | 2× Skirmisher + 1× "Rustbeak" (fast flier) |

### Interactables

| Type | Coordinates | Contents |
|------|-------------|----------|
| Chest (small) | (28, 10) | First "route chest" |
| Gather: Ore Node | (70, 8) | Basic materials |
| Gather: Dry Herb | (74, 28) | Crafting |

### Camp Vendor (Optional NPC)

| Property | Value |
|----------|-------|
| **Location** | (48, 22) |
| **One-liner** | *"Road tax is pain. I sell painkillers."* |

### Gating

| Condition | Effect |
|-----------|--------|
| `D1_CLEARED = TRUE` OR Ashveil story beat | Bramble fork opens to Growth Shrine path |

---

## Quick Reference Coordinates

### R01a — Outskirts (48×32)
```
Dusthaven exit: (24, 30)      Track entry: (44, 14)
Side spur: (6, 10)            Signpost: (24, 26)
Trigger: y = 18               Chest: (8, 8)
```

### R01b — Main Track (96×40)
```
Outskirts entry: (4, 20)      Ashveil exit: (92, 12)
Signpost: (10, 20)            Vendor: (48, 22)
Fork: (60, 30) [locked]       Canyon: x 34–46, y 16–26
```

---

## Implementation Notes

- **Tutorial pacing:** First pocket is fixed; rest are standard random encounter zones
- **Fork teaser:** Growth Shrine path visible but blocked — creates curiosity
- **Vendor:** Optional QoL; can be disabled if economy pacing requires
- **Mount introduction:** R03 is planned mount unlock; keep R01–R02 OFF
