# Route Micro-Map: R06 — Crystal Gate Pass

## Route Overview

| Property | Value |
|----------|-------|
| **Route Name** | Crystal Gate Pass (R06 Micro) |
| **Theme** | Cliff shelf → crystal mouth → cavern door |
| **Encounter Level Band** | 28–36 |
| **Mounts** | OFF |
| **Map Size** | 64 × 36 (x 0–63, y 0–35) |
| **Purpose** | Short connector + first "beam routing" taste (Light foreshadow) |

---

## Exits

| Destination | Coordinates | Notes |
|-------------|-------------|-------|
| **From Prismridge (east gate)** | (8, 30) | Route start |
| **To Crystal Caverns (D3) entrance** | (56, 6) | Dungeon door |
| **Optional post-clear shortcut door** | (30, 18) | Unlocks after D3 |

---

## Key Anchors

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Prism Gate pedestal | (32, 16) | Puzzle center |
| Crystal arch choke | x 44–58, y 10–18 | Narrow passage |

---

## Terrain / Hazards

### Prism Beam Gate (Micro Puzzle)

#### Components

| Object | Coordinates | Role |
|--------|-------------|------|
| **Emitter** | (24, 20) | Beam source |
| **Reflector A** | (32, 22) | Rotatable mirror |
| **Reflector B** | (40, 18) | Rotatable mirror |
| **Target Crest above door** | (56, 8) | Destination |

#### Rule

| Condition | Result |
|-----------|--------|
| Rotate both reflectors to land beam on crest | Door opens |
| Beam misses | Door remains locked |

### Low-Pressure Hazard: "Shardfall"

| Property | Value |
|----------|-------|
| **Telegraph** | 1.2s sparkle |
| **Effect** | Chip damage (tiny) on 2 tiles |
| **Frequency** | Every 16s while in choke zone |
| **Locations (random)** | (34, 14), (38, 14), (42, 14) |

---

## Encounter Pockets (2, Controlled)

### Pocket A (Before Gate)

| Property | Value |
|----------|-------|
| **Location** | (22, 24) |
| **Composition** | 2× Prism Skirmisher + 1× Ridge Skirmisher |

### Pocket B (Choke)

| Property | Value |
|----------|-------|
| **Location** | (46, 14) |
| **Composition** | 1× "Crystal Mite" swarm + 1× Stone Wisp |
| **Tier 7+** | Add one more Prism Skirmisher |

---

## Interactables

| Type | Coordinates | Contents |
|------|-------------|----------|
| Chest (small) | (14, 10) | Consumables |
| Gather: Prism Shard Node | (44, 28) | Crafting |
| Lore slab | (28, 10) | *"The caverns sing in bright fractures."* |

---

## Post-D3 Shortcut (QoL)

| Condition | Effect |
|-----------|--------|
| `D3_CLEARED = TRUE` | Unlock Crystal Latch Door at (30, 18) |
| **Benefit** | Short loop back to Prismridge gate |

---

## Quick Reference Coordinates

```
Prismridge entry: (8, 30)     D3 entrance: (56, 6)
Gate pedestal: (32, 16)       Choke: x 44–58, y 10–18
Shortcut: (30, 18) [locked]

--- Puzzle ---
Emitter: (24, 20)             Reflector A: (32, 22)
Reflector B: (40, 18)         Target: (56, 8)

--- Pockets ---
A: (22, 24)                   B: (46, 14)

--- Hazards ---
Shardfall tiles: (34,14) (38,14) (42,14)

--- Gather ---
Prism Shard: (44, 28)
```

---

## Implementation Notes

- **Beam puzzle:** Simple 2-mirror routing — precursor to shrine puzzles
- **Shardfall:** Low-pressure hazard creates urgency without threat
- **Crystal Mite swarm:** First "swarm" enemy type (multiple weak units)
- **Choke design:** Narrow passage forces tactical positioning
- **Puzzle gating:** Beam gate blocks D3 until solved (no level requirement)
