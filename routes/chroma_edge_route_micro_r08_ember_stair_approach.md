# Route Micro-Map: R08 — Ember Stair Approach

## Route Overview

| Property | Value |
|----------|-------|
| **Route Name** | Ember Stair Approach (R08 Micro) |
| **Theme** | Volcanic stair-run + wind shear + temple silhouette |
| **Encounter Level Band** | 38–48 |
| **Mounts** | OFF |
| **Map Size** | 72 × 40 (x 0–71, y 0–39) |
| **Purpose** | Last micro before D4; teaches Heat pressure with timing + safe pockets |

---

## Exits

| Destination | Coordinates | Notes |
|-------------|-------------|-------|
| **From Cinderstep approach node** | (10, 34) | Route start |
| **To Skyspire Temple (D4) entrance** | (62, 6) | Dungeon door |
| **Optional post-clear shortcut chute** | (28, 22) | Unlocks after D4 |

---

## Key Anchors

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Stair spine | Diagonal (14, 32) to (58, 10) | Main path |
| Temple pre-gate platform | (58, 10) | Final approach |
| Windbreak pillars (cover) | (36, 22) and (44, 18) | Safe spots |

---

## Terrain / Hazards (Heat Intro, Fair)

### A) Shear Gust Walls

Two gust "curtains" sweep across the stairs:

| Curtain | Zone | Direction |
|---------|------|-----------|
| **Curtain 1** | x 24–40, y 20–30 | Cross-stair |
| **Curtain 2** | x 44–60, y 12–22 | Cross-stair |

#### Shear Mechanics

| Property | Value |
|----------|-------|
| **Cycle** | 10s |
| **Telegraph** | 1.2s horizontal wind lines |
| **Active** | 3.5s |
| **Shove** | 2 tiles down-stair direction |
| **Chip damage** | Burning cinders (small) |

### B) Safe Pockets

| Location | Effect |
|----------|--------|
| Behind windbreak pillars | Gust shove reduced to 0 tiles |

**Teaching:** "Use cover" — pillar positioning blocks gust

### Micro Gate: "Temple Latch"

| Object | Coordinates | Rule |
|--------|-------------|------|
| **Latch Sigil** | (58, 12) | Defeat guard pack → unlocks → door opens |

---

## Encounter Pockets (3, Tuned)

### Pocket A (Lower Steps)

| Property | Value |
|----------|-------|
| **Location** | (20, 28) |
| **Composition** | 2× Ember Skirmisher + 1× Heat Runner |

### Pocket B (Shear Zone)

| Property | Value |
|----------|-------|
| **Location** | (34, 22) |
| **Composition** | 1× Wind Wisp + 2× Ember Skirmisher |

### Pocket C (Pre-Gate Guard Pack)

| Property | Value |
|----------|-------|
| **Location** | (56, 10) |
| **Composition** | 1× Elite "Skyspire Aspirant" + 2× adds |
| **Notes** | On clear: unlock Temple Latch |

---

## Interactables

| Type | Coordinates | Contents |
|------|-------------|----------|
| Chest (small) | (16, 10) | Consumables |
| Chest (small) | (46, 34) | Materials |
| Gather: Cinder Bloom | (30, 34) | Crafting |
| Gather: Ash Resin | (50, 26) | Heat gear craft mat |

---

## Post-D4 Shortcut (QoL)

| Condition | Effect |
|-----------|--------|
| `D4_CLEARED = TRUE` | Open Chute Door at (28, 22) |
| **Benefit** | Short drop-path back to lower stair (fast return to Cinderstep) |

---

## Quick Reference Coordinates

```
Cinderstep entry: (10, 34)    D4 entrance: (62, 6)
Stair spine: (14,32)→(58,10)  Pre-gate: (58, 10)
Shortcut chute: (28, 22) [locked]

--- Cover Pillars ---
Pillar 1: (36, 22)            Pillar 2: (44, 18)

--- Pockets ---
A: (20, 28)                   B: (34, 22)
C: (56, 10) [unlocks latch]

--- Hazards ---
Curtain 1: x 24–40, y 20–30   Curtain 2: x 44–60, y 12–22
Latch: (58, 12)

--- Gather ---
Cinder Bloom: (30, 34)        Ash Resin: (50, 26)
```

---

## Implementation Notes

- **Heat escalation:** hazard cadence tightens before D4 entry
- **Cover mechanics:** Pillars create safe zones — teaches positioning
- **Latch gate:** Combat-gated (defeat pack) rather than puzzle-gated
- **Shear timing:** 10s cycle allows rhythm learning
- **Elite Aspirant:** Named enemy foreshadows Skyspire trials
- **Chute shortcut:** Vertical drop creates satisfying return path
