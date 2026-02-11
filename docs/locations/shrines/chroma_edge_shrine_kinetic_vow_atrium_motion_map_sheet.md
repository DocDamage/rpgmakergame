# Shrine Map Sheet: Kinetic Vow Atrium (Motion Shrine)

## 1. Overview

| Attribute | Value |
|-----------|-------|
| **Shrine Name** | Kinetic Vow Atrium |
| **Element** | Motion |
| **Role** | Optional shrine that grants a Motion Blessing + a Motion craft core |
| **Theme** | Momentum, rhythm, and "movement as truth"—tempo control without feeling like a platformer |
| **Recommended Level** | 145–205 (scales if entered late) |
| **Total Footprint** | 1 exterior micro-map + 1 interior map + 1 trial chamber submap |
| **Tile Scale** | 16×16 px |

---

## 2. World Placement + Access

### Overworld Location
- **Position**: On a wind-swept canyon shelf between Prismridge and Skyspire Temple routes
- **Description**: A side spur with visible moving bridges
- **Node Label**: `Motion Shrine — Kinetic Vow Atrium`
- **Map Icon**: Arrow swirl

### Access Rule
- Door is sealed by **Kinetic Latch**
- Open by activating **3 Wind Cranks** in the exterior micro-map (they sync into a single "tempo" and unlock the latch)

---

## 3. Exterior Micro-Map — "Windstep Span"

| Property | Value |
|----------|-------|
| **Size** | 40 × 28 tiles |
| **Purpose** | Quick moving-bridge rhythm + 3 crank unlock |
| **Encounters** | OFF |

### Key Anchors (local 0–39, 0–27)

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Entry from overworld | (20, 26) | Player spawn point |
| Shrine door (Kinetic Latch) | (20, 4) | Opens when all cranks activated |
| Save lantern (optional) | (6, 20) | Pre-shrine save point |
| **Wind Crank A** | (10, 18) | Required for entry |
| **Wind Crank B** | (30, 18) | Required for entry |
| **Wind Crank C** | (20, 10) | Required for entry |

### Moving Bridge Strips (visual + timing)

Two 1-tile wide bridge lines that "extend/retract" on a cycle:

| Bridge | Coordinates | Cycle |
|--------|-------------|-------|
| Bridge L strip | x 12, y 12–22 | 6s total (3s extended, 3s retracted) |
| Bridge R strip | x 28, y 12–22 | 6s total (3s extended, 3s retracted) |

**Telegraph**: Bridge posts glow when about to extend.

### Door Rule
Activate all 3 Wind Cranks → latch clicks → door opens.

---

## 4. Interior Map — "Atrium of Pace"

| Property | Value |
|----------|-------|
| **Size** | 64 × 48 tiles |
| **Lighting** | Cool windlight + faint motion trails on the floor |
| **Encounters** | OFF |

### Layout Overview

| Room | Name | Type |
|------|------|------|
| Room 1 | Vestibule | Safe zone |
| Room 2 | Conveyor Choir | Main puzzle area |
| Room 3 | Tempo Cloister | Save + warp |
| Room 4 | Velocity Seal Door | Portal to Trial Chamber |

### Anchors & Coordinates (local 0–63, 0–47)

#### Entry / Flow

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Interior entry spawn | (32, 44) | From exterior door |
| Return door to overworld | (32, 46) | Exit to Windstep Span |
| Trial Door (Velocity Seal) | (32, 6) | Locked until puzzle solved |

#### Safe Utilities

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Save Crystal | (12, 38) | Standard save point |
| Warp Sigil | (52, 38) | Unlocks after clear |
| Keeper spot | (32, 38) | Optional NPC location |

#### Puzzle Objects (Conveyor Choir)

**Core Concept**: Route a "tempo charge" to a seal by toggling conveyor direction and gates.

| Object | Coordinates | Notes |
|--------|-------------|-------|
| **Tempo Core (start)** | (32, 32) | Glowing orb spawn point |
| **Velocity Seal Node (target)** | (32, 14) | Goal destination |

**Conveyor Strips** (force movement, 1 tile per 2s):

| Strip | Coordinates |
|-------|-------------|
| Strip A | x 20–44 at y 28 |
| Strip B | x 20–44 at y 20 |
| Strip C | y 20–28 at x 20 |
| Strip D | y 20–28 at x 44 |

**Direction Levers** (toggle strip direction):

| Lever | Coordinates | Affects |
|-------|-------------|---------|
| Lever A | (18, 28) | Strip A |
| Lever B | (46, 28) | Strip B |
| Lever C | (18, 20) | Strip C |
| Lever D | (46, 20) | Strip D |

**Gate Pads** (open/close 2-tile gate):

| Pad | Coordinates |
|-----|-------------|
| Gate Pad 1 | (26, 24) |
| Gate Pad 2 | (38, 24) |

#### Locked Door

| Object | Coordinates | Unlock Condition |
|--------|-------------|------------------|
| Velocity Seal Door | (32, 6) | Tempo charge reaches the Velocity Seal Node within 20 seconds |

---

## 5. Atrium Puzzle — "Tempo Routing"

### Goal
Send the Tempo Charge (a small glowing orb) from (32,32) to (32,14) by toggling conveyor directions and opening the right gate at the right moment.

### Rules

| Element | Details |
|---------|---------|
| **Levers** | Pulling a lever flips a conveyor strip's direction instantly |
| **Gate Pads** | Standing on a Gate Pad toggles that gate open while you stand on it (step-off closes) |
| **Tempo Charge** | Moves automatically along conveyor strips and turns at corners |

### Timer Pressure
- **Time limit**: 20 seconds per attempt
- **On fail**: Charge fizzles and respawns after 2 seconds (no damage)

### Telegraphs

| Element | Visual | Audio |
|---------|--------|-------|
| Conveyor direction | Floor arrows | — |
| Tempo Charge | Glowing orb | "Ticks" faster as time runs out |

### Optional "Clean Solve" Hint

**Plaque near Lever A:**
> *"Don't fight the current. Re-write it."*

---

## 6. Trial Chamber Submap — "Velocity Crucible"

| Property | Value |
|----------|-------|
| **Size** | 48 × 48 tiles |
| **Purpose** | Movement execution + burst windows—hazards are conveyors + dash gates + a mini-boss that punishes standing still |
| **Encounters** | ON (scripted boss fight only) |

### Anchors & Coordinates (local 0–47, 0–47)

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Entry portal spawn | (24, 44) | From Velocity Seal Door |
| Boss spawn | (24, 18) | Pace Warden: Aerolith Marshal |
| Exit portal | (24, 6) | Spawns after clear |
| Reward pedestal | (24, 10) | Motion Blessing + loot |
| **Speed Glyph A** | (12, 26) | Haste + immunity to forced-move stagger (6s) |
| **Speed Glyph B** | (36, 26) | Haste + immunity to forced-move stagger (6s) |
| **Cover Pylon 1** | (14, 18) | 2×2 collision cover |
| **Cover Pylon 2** | (34, 18) | 2×2 collision cover |
| **Cover Pylon 3** | (14, 34) | 2×2 collision cover |
| **Cover Pylon 4** | (34, 34) | 2×2 collision cover |

---

## 7. Trial Script — "Vow of Momentum"

### Phase 0: Start
- Portal locks when player crosses y ≤ 40

### Phase 1: Conveyor + Gate Drill (30 seconds)

**Hazard: "Conveyor Hymn"**

| Property | Value |
|----------|-------|
| Pattern | Two conveyor strips activate alternatingly |
| Timing | Strip set 1 active for 8s → 2s pause → strip set 2 active for 8s |
| Telegraph | 1.2s arrows appear before activation |
| Forced move | 1 tile per 2s |
| Wall hit | Brief stagger (Speed Glyph prevents this) |

### Phase 2: Mini-Boss — Pace Warden: Aerolith Marshal

#### Boss Identity
Fast reposition, lane bursts, punishes "stand and cast."

#### Move List

| Move | Type | Telegraph | Effect |
|------|------|-----------|--------|
| **Vector Chop** | Dash line | 1.0s | Leaves afterline hazard (4s) |
| **Dash Gates** | 2 short lanes | 1.4s | Chip damage + turn delay if hit |
| **Kinetic Pulse** | Ring | 1.2s | Pushes 1 tile |
| **Tempo Tax** | Anti-camp | 0.8s | Punishes standing still |

#### Tempo Tax (Anti-Camp Mechanic)

| Trigger | Effect |
|---------|--------|
| Character ends turns on the same tile 2 turns in a row | Telegraph: 0.8s "target bracket" → small burst + forced 2-tile shove |

#### Counterplay

| Strategy | Effect |
|----------|--------|
| Use Speed Glyphs | Ignore conveyor stagger and maintain positioning |
| Burst timing | Attack when boss finishes Vector Chop (short recovery window) |

### Clear Condition
Defeat Aerolith Marshal → Exit portal spawns + Reward pedestal unlocks.

---

## 8. Rewards + Flags

### Reward Pedestal Contents

#### Blessing: Oath of Velocity

| Property | Value |
|----------|-------|
| **Type** | Motion Blessing |
| **Effect** | +Motion resistance; Every 3rd action grants Haste for 1 turn (or extends existing Haste by 1); First forced-move/knockback each battle is reduced to 0 tiles |

#### Unique Item Drops

| Item | Type |
|------|------|
| Motion Core Shard | Craft component / resonance upgrade |
| Kinetic Sigil | Optional: unlocks Motion-aligned node / summon enhancement |

#### Optional Treasure Chest

| Property | Value |
|----------|-------|
| Location | (40, 12) in Trial Chamber |
| Contents | Materials + currency + 1 Motion-leaning accessory roll |

### Game Flags

| Flag | Trigger |
|------|---------|
| `SHRINE_MOTION_FOUND` | Entering Windstep Span |
| `SHRINE_MOTION_CLEARED` | Defeating Aerolith Marshal |
| `BLESSING_MOTION_UNLOCKED` | Collecting from reward pedestal |
| `WARP_MOTION_SHRINE_UNLOCKED` | Clearing the shrine |

---

## 9. NPC/Voice Lines

### Atrium Keeper (Tempo Cloister, at 32, 38)

| Context | Line |
|---------|------|
| Greeting | *"Speed is honesty."* |
| Puzzle Hint | *"Route the charge. Don't chase it."* |
| After Clear | *"Your rhythm holds."* |

---

## 10. Quick Reference

### Coordinate Summary

#### Exterior (Windstep Span) — 40×28
```
Entry: (20, 26)      Door: (20, 4)
Crank A: (10, 18)    Crank B: (30, 18)    Crank C: (20, 10)
Save: (6, 20)

--- Moving Bridges ---
Bridge L: x 12, y 12–22
Bridge R: x 28, y 12–22
Cycle: 6s (3s extend, 3s retract)
```

#### Interior (Atrium of Pace) — 64×48
```
Entry: (32, 44)           Exit: (32, 46)
Save: (12, 38)            Warp: (52, 38)
Keeper: (32, 38)          Trial Door: (32, 6)

--- Puzzle ---
Tempo Core Start: (32, 32)    Velocity Seal Node: (32, 14)

Conveyor Strips:
  Strip A: x 20–44, y 28      Strip B: x 20–44, y 20
  Strip C: x 20, y 20–28      Strip D: x 44, y 20–28

Levers: A(18,28) B(46,28) C(18,20) D(46,20)
Gate Pads: 1(26,24) 2(38,24)
```

#### Trial Chamber (Velocity Crucible) — 48×48
```
Entry: (24, 44)           Boss: (24, 18)
Exit: (24, 6)             Reward: (24, 10)
Speed Glyph A: (12, 26)   Speed Glyph B: (36, 26)
Pylons: (14,18) (34,18) (14,34) (34,34)
```

---

## 11. Implementation Notes

- **Conveyor strips**: Force player movement at 1 tile per 2s while active
- **Gate pads**: Binary state—gate open only while player stands on pad
- **Tempo Charge**: Automatic movement along conveyor paths, corner-turning logic
- **Conveyor Hymn hazard**: Alternating strip sets with clear telegraph arrows
- **Tempo Tax**: Track player position across turns; trigger if same tile for 2 consecutive turn ends
- **Speed Glyph effect**: Grants Haste buff + "Steady Footing" (ignore forced-move stagger)
