# Route Micro-Map: R17a - Old Lumencrest to Grand Boulevard

## Route Overview

| Property | Value |
|----------|-------|
| **Route Name** | Old Lumencrest to Grand Boulevard (R17a) |
| **Theme** | Camp perimeter to formal capital artery |
| **Encounter Level Band** | 86-100 |
| **Mounts** | ON (forced OFF inside choke pockets) |
| **Map Size** | 104 x 48 (x 0-103, y 0-47) |
| **Purpose** | First capital spine connector after Outer Wards hub |

---

## Exits

| Destination | Coordinates | Notes |
|-------------|-------------|-------|
| **From Outer Wards east gate** | (2, 30) | Primary entry from hub |
| **To Grand Boulevard west apron** | (102, 24) | Feeds R17b branch lane |
| **Return slip to camp ring road** | (14, 44) | QoL loop after first clear |

---

## Key Anchors

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Quarantine arch frame | (24, 28) | Visual start marker |
| Tram splice cut | x 44-68, y 30-36 | Broken rail crossing |
| Crown skyline reveal | (86, 18) | First clean spire view |

---

## Terrain / Hazards

### A) Seal Sweep Lanes

| Property | Value |
|----------|-------|
| **Zone** | x 34-64, y 20-30 |
| **Telegraph** | 1.4s paper-rattle + floor sigil glow |
| **Active** | 3.0s |
| **Effect** | Small chip damage + minor Confounded buildup |
| **Cooldown** | 10.0s |

### B) Null Stitch Cracks

| Vent | Coordinates | Size |
|------|-------------|------|
| **Crack A** | (72, 22) | 3x2 |
| **Crack B** | (80, 30) | 2x2 |

| Property | Value |
|----------|-------|
| **Telegraph** | 1.2s violet pulse |
| **Active** | 2.2s |
| **Effect** | Removes one non-ultimate buff |
| **Cooldown** | 13.0s |

---

## Encounter Pockets

### Pocket A - Gate Debris

| Property | Value |
|----------|-------|
| **Location** | (22, 34) |
| **Composition** | 2x Phase Scuttler + 1x Seal Leech |

### Pocket B - Tram Splice

| Property | Value |
|----------|-------|
| **Location** | (56, 30) |
| **Composition** | 1x Record Sentry (elite) + 2x Rift Skirmisher |

### Pocket C - Skyline Bend

| Property | Value |
|----------|-------|
| **Location** | (88, 20) |
| **Composition** | 1x Null Caster + 2x Chrono Wisp |

---

## Interactables

| Type | Coordinates | Contents / Function |
|------|-------------|---------------------|
| Chest (small) | (18, 12) | Consumables |
| Chest (medium) | (74, 40) | Craft materials |
| Gather node | (64, 10) | Paradox Glass shard |
| Lore slab | (42, 14) | "The road still expects permits." |

---

## Gating

| Lock | Condition |
|------|-----------|
| **R17a open** | `R16_COMPLETE = TRUE` |
| **Archive route marker visible** | `CROWN_CHAIN_STARTED = TRUE` |
| **Return slip active** | First reach of Grand Boulevard |

---

## Quick Reference Coordinates

```text
Outer Wards entry: (2, 30)      Grand Boulevard exit: (102, 24)
Return slip: (14, 44)

Seal Sweep Zone: x 34-64, y 20-30
Null Crack A: (72, 22)          Null Crack B: (80, 30)

Pocket A: (22, 34)              Pocket B: (56, 30)
Pocket C: (88, 20)

Chest S: (18, 12)               Chest M: (74, 40)
Paradox node: (64, 10)          Lore slab: (42, 14)
```

---

## Implementation Notes

- This micro-map is the low-friction handoff from `chroma_edge_submap_old_lumencrest_outer_wards_map_sheet.md` into the capital chain.
- Keep the main lane readable even with hazards active; this is a traversal map, not a lockout gauntlet.
