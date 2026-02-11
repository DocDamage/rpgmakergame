# Route Micro-Map: R17f - Palace Entrance Micro

## Route Overview

| Property | Value |
|----------|-------|
| **Route Name** | Palace Entrance Micro (R17f) |
| **Theme** | Final threshold from Crown District into Palace Interior |
| **Encounter Level Band** | 108-120 (scripted only) |
| **Mounts** | OFF |
| **Map Size** | 120 x 64 (x 0-119, y 0-63) |
| **Purpose** | Last pre-palace staging route with explicit final-act gate checks |

---

## Exits

| Destination | Coordinates | Notes |
|-------------|-------------|-------|
| **From Crown District upper gate** | (4, 54) | Arrival from R17e |
| **Back to Crown District** | (0, 58) | Return before commit |
| **To Palace Antechamber** | (118, 18) | Final dungeon entry |
| **To Final Save Alcove** | (64, 2) | Optional prep room |

---

## Key Anchors

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Oath bridge midpoint | (48, 36) | First clear sightline to palace doors |
| Conduit permit monolith | (82, 24) | Final permit check |
| Palace gate lattice | (112, 18) | Entry visual target |

---

## Terrain / Hazards

### A) Crown Synchrony Pulses

| Property | Value |
|----------|-------|
| **Zone** | x 34-96, y 20-40 |
| **Telegraph** | 1.6s floor ring + high-tone swell |
| **Active** | 2.8s |
| **Effect** | Adds 1 Crown Synchrony stack (no HP damage) |
| **Cooldown** | 14.0s |

### B) Gate Lattice Bursts

| Property | Value |
|----------|-------|
| **Emitters** | (92, 22), (100, 20), (108, 18) |
| **Telegraph** | 1.1s lattice line brighten |
| **Active** | 2.0s |
| **Effect** | Minor arc hit + short stagger |
| **Cooldown** | 10.0s |

---

## Encounter Pockets

### Pocket A - Oath Bridge Check

| Property | Value |
|----------|-------|
| **Location** | (44, 38) |
| **Composition** | 1x Crown Warden + 2x Phase Skulker |
| **Type** | Scripted one-time |

### Pocket B - Permit Monolith Guard

| Property | Value |
|----------|-------|
| **Location** | (82, 24) |
| **Composition** | 1x Bastion Prefect Drone elite + 2x Chrono Wisp |
| **Type** | Scripted one-time |

### Pocket C - Palace Gate Sentinel

| Property | Value |
|----------|-------|
| **Location** | (110, 18) |
| **Composition** | 1x Gate Sentinel mini-boss |
| **Type** | Optional rematch after clear |

---

## Interactables

| Type | Coordinates | Contents / Function |
|------|-------------|---------------------|
| Final save terminal | (62, 8) | Save before palace run |
| Rest node | (68, 8) | Full recovery |
| Chest (large) | (70, 4) | Final prep consumables + mat pack |
| Lore monolith | (36, 18) | Final pre-palace lore |

---

## Gating

| Lock | Condition |
|------|-----------|
| **R17f open** | `D8_CLEARED = TRUE` and `RELIC_SHADOW_SEATED = TRUE` |
| **Palace gate open** | `FINAL_ACT_OPEN = TRUE` |
| **Gate sentinel rematch** | `PALACE_INTERIOR_CLEARED = TRUE` |

---

## Quick Reference Coordinates

```text
Crown entry: (4, 54)              Crown return: (0, 58)
Palace exit: (118, 18)            Save alcove: (64, 2)

Synchrony zone: x 34-96, y 20-40
Lattice emitters: (92,22), (100,20), (108,18)

Pocket A: (44, 38)                Pocket B: (82, 24)
Pocket C: (110, 18)

Save terminal: (62, 8)            Rest node: (68, 8)
Large chest: (70, 4)              Lore monolith: (36, 18)
```

---

## Implementation Notes

- Keep this map compact and deliberate; it should feel like a commitment corridor, not a new dungeon.
- Route handoff target for this file is `chroma_edge_dungeon_palace_interior_map_sheet.md`.
