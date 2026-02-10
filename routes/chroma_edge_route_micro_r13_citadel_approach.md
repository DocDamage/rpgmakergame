# Route Micro-Map: R13 — Citadel Approach

## Route Overview

| Property | Value |
|----------|-------|
| **Route Name** | Citadel Approach (R13 Micro) |
| **Theme** | Blizzard wall → glacial steps → citadel silhouette → time-frost shimmer |
| **Encounter Level Band** | 68–82 |
| **Mounts** | OFF |
| **Map Size** | 64 × 36 (x 0–63, y 0–35) |
| **Purpose** | Short, intense lead-in; introduces Time/Frost "slow zones" + seal gate |

---

## Exits

| Destination | Coordinates | Notes |
|-------------|-------------|-------|
| **From Rimehold (north gate)** | (8, 30) | Route start |
| **To Frozen Citadel (D7) entrance** | (56, 6) | Dungeon door |
| **Post-D7 shortcut ropeway** | (28, 18) | Unlocks after D7 |

---

## Key Anchors

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Blizzard threshold marker | (18, 26) | Weather warning |
| Chrono-Frost Seal Door | (46, 12) | Puzzle gate |
| Citadel pre-platform | (54, 10) | Final approach |

---

## Terrain / Hazards

### A) Time-Frost Patches (Slow Field)

| Patch | Coordinates | Size |
|-------|-------------|------|
| **Patch 1** | (26, 22) | 3×3 |
| **Patch 2** | (40, 16) | 3×3 |

#### Time-Frost Mechanics

| Property | Value |
|----------|-------|
| **Cycle** | 14s |
| **Telegraph** | 1.6s crystalline shimmer |
| **Active** | 5.0s |
| **Effect** | SLOW for 6s (no damage) |

### B) Blizzard Gust Wall (Positional)

| Zone | x 20–44, y 10–28 |
|------|------------------|
| **Cycle** | 12s |
| **Telegraph** | 1.2s wind shear lines |
| **Active** | 3.5s |
| **Effect** | Shove 2 tiles "downhill" |

### Micro Gate: Chrono-Frost Seal

#### Components

| Object | Coordinates | Role |
|--------|-------------|------|
| **Pylon 1** | (36, 20) | Activate |
| **Pylon 2** | (44, 20) | Activate |
| **Pylon 3** | (40, 14) | Activate |
| **Seal Door** | (46, 12) | Opens on success |

#### Rule

| Condition | Result |
|-----------|--------|
| Activate all 3 within 10 seconds | Door opens |
| Fail (timer expires) | Pylons reset (no damage) |

---

## Encounter Pockets (2–3, Controlled)

### Pocket A (Pre-Seal)

| Property | Value |
|----------|-------|
| **Location** | (22, 24) |
| **Composition** | 2× Frost Skirmisher + 1× Chrono Scriber |

### Pocket B (Seal Pylon Pressure)

| Property | Value |
|----------|-------|
| **Location** | (40, 18) |
| **Composition** | 1× Chill Caster + 2× Frost Skirmisher |

### Pocket C (Pre-Citadel Platform, Optional)

| Property | Value |
|----------|-------|
| **Location** | (54, 10) |
| **Composition** | 1× Elite "Citadel Watcher" + 2× adds |
| **Notes** | "Last check" before D7; tier scaling |

---

## Interactables

| Type | Coordinates | Contents |
|------|-------------|----------|
| Chest (small) | (14, 10) | Consumables |
| Chest (small) | (50, 30) | Materials |
| Gather: Frost Lichen | (30, 30) | Crafting |
| Gather: Chrono Shard | (48, 24) | Rare mat seed for time crafts |

---

## Post-D7 Shortcut (QoL)

| Condition | Effect |
|-----------|--------|
| `D7_CLEARED = TRUE` | Unlock Ropeway Gate at (28, 18) |
| **Benefit** | Fast-tracks back to (12, 28) — no approach repeat |

---

## Quick Reference Coordinates

```
Rimehold entry: (8, 30)       D7 entrance: (56, 6)
Blizzard marker: (18, 26)     Seal Door: (46, 12)
Pre-platform: (54, 10)        Shortcut: (28, 18) [locked]

--- Puzzle ---
Pylon 1: (36, 20)             Pylon 2: (44, 20)
Pylon 3: (40, 14)             Door: (46, 12)

--- Pockets ---
A: (22, 24)                   B: (40, 18)
C (optional): (54, 10)

--- Hazards ---
Time-Frost 1: (26, 22)        Time-Frost 2: (40, 16)
Blizzard wall: x 20–44, y 10–28

--- Gather ---
Frost Lichen: (30, 30)        Chrono Shard: (48, 24)
```

---

## Implementation Notes

- **Time-Frost:** First time/slow mechanic combination
- **Blizzard gust:** 2-tile shove creates positional pressure
- **Pylon puzzle:** Timed activation under combat pressure
- **Citadel Watcher:** Optional final gatekeeper before D7
- **Chrono Shard:** Rare material foreshadows Time crafts
- **Ropeway shortcut:** One-way fast return post-clear
