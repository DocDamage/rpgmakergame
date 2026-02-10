# Route Micro-Map: R17d - Crown District Approach

## Route Overview

| Property | Value |
|----------|-------|
| **Route Name** | Crown District Approach (R17d) |
| **Theme** | Quarantine ring gauntlet at the inner capital wall |
| **Encounter Level Band** | 92-108 |
| **Mounts** | ON on outer lane, OFF in inner perimeter cuts |
| **Map Size** | 192 x 96 (x 0-191, y 0-95) |
| **Purpose** | Required route from boulevard/wards into Crown District hub |
| **Related Full Sheet** | `chroma_edge_submap_crown_district_approach_map_sheet.md` |

---

## Exits

| Destination | Coordinates | Notes |
|-------------|-------------|-------|
| **From Grand Boulevard** | (0, 22) | Main progression entry |
| **From Outer Wards alternate** | (0, 74) | Secondary route |
| **To Crown District hub** | (191, 28) | Requires archive key |
| **To Underworks bypass** | (132, 95) | Tide route |

---

## Key Anchors

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Crownward notice board | (18, 26) | Restriction messaging |
| Phase barrier + pylon | (92, 24) and (84, 30) | Time bypass tutorial |
| Crown gate console | (182, 28) | Final key check |

---

## Terrain / Hazards

### A) Watchlight Sweeps

| Property | Value |
|----------|-------|
| **Towers** | (72, 18), (122, 58), (168, 22) |
| **Telegraph** | 1.0s bell + cone fade-in |
| **Active** | 3.0s sweep |
| **Effect** | Applies Marked (encounter rate up for 30s) |
| **Cooldown** | 8.0s between sweeps |

### B) Compliance Seal Pads

| Property | Value |
|----------|-------|
| **Zones** | x 70-160, y 10-34 and x 150-190, y 18-50 |
| **Telegraph** | 1.2s seal flutter |
| **Active** | 2.8s |
| **Effect** | Minor Confounded buildup |
| **Cooldown** | 9.0s |

---

## Encounter Pockets

### Pocket A - Service Road Mid

| Property | Value |
|----------|-------|
| **Location** | (64, 56) |
| **Composition** | 2x Crownshard Sentinel + 1x Chrono Wisp |

### Pocket B - Garden Cut

| Property | Value |
|----------|-------|
| **Location** | (108, 24) |
| **Composition** | 1x Phase Skulker elite + 2x Seal Leech |

### Pocket C - Wallwalk Catacomb

| Property | Value |
|----------|-------|
| **Location** | (142, 84) |
| **Composition** | 1x Wardbreaker + 2x Rift Skirmisher |

### Pocket D - Gate Bastion

| Property | Value |
|----------|-------|
| **Location** | (176, 30) |
| **Composition** | 1x Bastion Prefect Drone + 2x Chrono Wisp |

---

## Interactables

| Type | Coordinates | Contents / Function |
|------|-------------|---------------------|
| Chest (small) | (74, 14) | Paradox mat |
| Chest (medium) | (154, 90) | Craft bundle |
| Chest (medium) | (176, 44) | Bastion accessory mat |
| Gather node | (164, 82) | Crown Alloy plate |

---

## Gating

| Lock | Condition |
|------|-----------|
| **Crown gate open** | `CROWN_ARCHIVE_KEY_ACQUIRED = TRUE` |
| **Rubble shortcut** | `RELIC_MASS_SEATED = TRUE` |
| **Underworks skip** | `RELIC_TIDE_SEATED = TRUE` or `SEAL_CUTTER = TRUE` |

---

## Quick Reference Coordinates

```text
Grand Boulevard entry: (0, 22)    Outer Wards entry: (0, 74)
Crown District exit: (191, 28)    Underworks exit: (132, 95)

Notice board: (18, 26)
Phase barrier: (92, 24)           Phase pylon: (84, 30)
Crown gate console: (182, 28)

Tower A: (72, 18)                 Tower B: (122, 58)
Tower C: (168, 22)

Pocket A: (64, 56)                Pocket B: (108, 24)
Pocket C: (142, 84)               Pocket D: (176, 30)
```

---

## Implementation Notes

- This file is the route-level implementation contract; detailed district scripting remains in `chroma_edge_submap_crown_district_approach_map_sheet.md`.
- Preserve readable lanes so this route remains replayable during endgame farming loops.
