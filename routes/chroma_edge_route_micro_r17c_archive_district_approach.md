# Route Micro-Map: R17c - Archive District Approach

## Route Overview

| Property | Value |
|----------|-------|
| **Route Name** | Archive District Approach (R17c) |
| **Theme** | Intake ramp to "edited records" gatehouse |
| **Encounter Level Band** | 90-104 |
| **Mounts** | OFF |
| **Map Size** | 96 x 52 (x 0-95, y 0-51) |
| **Purpose** | Transitional combat route that delivers players into Archive Gatehouse tutorial map |

---

## Exits

| Destination | Coordinates | Notes |
|-------------|-------------|-------|
| **From R17b archive gate** | (2, 42) | Primary entry |
| **To Archive Gatehouse entry** | (94, 8) | Leads to Submap 1 |
| **Back to Grand Boulevard branch** | (0, 46) | Return path |
| **Service stair to Underworks** | (76, 50) | One-way emergency exit |

---

## Key Anchors

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Intake bastion arch | (18, 38) | Sets map identity |
| Citation drum array | (50, 24) | Audio landmark |
| Gatehouse lock face | (86, 10) | Final visual target |

---

## Terrain / Hazards

### A) Ink Pressure Trenches

| Property | Value |
|----------|-------|
| **Zone** | x 32-72, y 20-34 |
| **Telegraph** | 1.5s black ripple with white edge |
| **Active** | 3.4s |
| **Effect** | Pressure buildup + minor movement drag |
| **Cooldown** | 11.0s |

### B) Citation Beam Latches

| Latch | Coordinates | Size |
|-------|-------------|------|
| **Latch A** | (58, 18) | 1x3 |
| **Latch B** | (66, 28) | 1x3 |

| Property | Value |
|----------|-------|
| **Telegraph** | 1.1s vertical line glow |
| **Active** | 2.0s |
| **Effect** | Small hit + short silence |
| **Cooldown** | 10.0s |

---

## Encounter Pockets

### Pocket A - Intake Ramp

| Property | Value |
|----------|-------|
| **Location** | (20, 40) |
| **Composition** | 2x Crownshard Sentinel + 1x Seal Leech |

### Pocket B - Drum Array

| Property | Value |
|----------|-------|
| **Location** | (50, 24) |
| **Composition** | 1x Record Sentry elite + 2x Chrono Wisp |

### Pocket C - Gatehouse Steps

| Property | Value |
|----------|-------|
| **Location** | (84, 12) |
| **Composition** | 1x Wardbreaker + 2x Phase Skulker |

---

## Interactables

| Type | Coordinates | Contents / Function |
|------|-------------|---------------------|
| Chest (small) | (14, 14) | Consumables |
| Chest (medium) | (64, 40) | Archive prep materials |
| Gather node | (74, 6) | Seal Wax scrap |
| Lore tablet | (40, 10) | "Records are safer than people." |

---

## Gating

| Lock | Condition |
|------|-----------|
| **R17c open** | `ARCHIVE_DISTRICT_ACCESS_GRANTED = TRUE` |
| **Gatehouse entry active** | `ARCHIVE_DISTRICT_ACCESS_GRANTED = TRUE` |
| **Service stair unlocked** | `CROWN_ARCHIVE_KEY_ACQUIRED = TRUE` |

---

## Quick Reference Coordinates

```text
R17b entry: (2, 42)               Boulevard return: (0, 46)
Archive Gatehouse exit: (94, 8)   Service stair: (76, 50)

Ink trench: x 32-72, y 20-34
Latch A: (58, 18)                 Latch B: (66, 28)

Pocket A: (20, 40)                Pocket B: (50, 24)
Pocket C: (84, 12)

Chest S: (14, 14)                 Chest M: (64, 40)
Seal Wax node: (74, 6)            Lore tablet: (40, 10)
```

---

## Implementation Notes

- This map should hand off directly into `chroma_edge_dungeon_archive_district_map_sheet.md` Submap 1.
- Keep enemy density front-loaded so the gatehouse tutorial puzzle space starts clean.
