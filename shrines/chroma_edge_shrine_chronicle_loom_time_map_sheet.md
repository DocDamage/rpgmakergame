# Shrine Map Sheet: Chronicle Loom Atrium (Time Shrine)

## 1. Overview

| Attribute | Value |
|-----------|-------|
| **Shrine Name** | Chronicle Loom Atrium |
| **Element** | Time |
| **Role** | Optional shrine that grants a Time Blessing + a Time craft core |
| **Theme** | Records, edits, and "locking a moment"—timeline control without becoming a gimmick |
| **Recommended Level** | 160–220 (scales if entered late) |
| **Total Footprint** | 1 exterior micro-map + 1 interior map + 1 trial chamber submap |
| **Tile Scale** | 16×16 px |

---

## 2. World Placement + Access

### Overworld Location
- **Position**: Near Chronowake Pier
- **Description**: Off a cliffside path that overlooks the Phase-Lane Crossing
- **Node Label**: `Time Shrine — Chronicle Loom`
- **Map Icon**: Hourglass + ring

### Access Rule
- Door sealed by **Chrono Seal**
- Open by triggering **3 Record Plates** on the exterior approach in the correct order (shown in a faded mural—no guessing)

---

## 3. Exterior Micro-Map — "Ledger Cliffwalk"

| Property | Value |
|----------|-------|
| **Size** | 40 × 28 tiles |
| **Purpose** | Quick "record order" unlock with strong hinting |
| **Encounters** | OFF |

### Key Anchors (local 0–39, 0–27)

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Entry from overworld | (20, 26) | Player spawn point |
| Shrine door (Chrono Seal) | (20, 4) | Opens when plates stepped in correct order |
| Save lantern (optional) | (6, 20) | Pre-shrine save point |
| **Record Plate 1** | (12, 18) | Step-on trigger |
| **Record Plate 2** | (28, 18) | Step-on trigger |
| **Record Plate 3** | (20, 12) | Step-on trigger |
| **Hint Mural** | (20, 9) | Shows symbols: I → II → III |
| Flavor plaque | (20, 7) | *"What's written can be re-written. But not without cost."* |

### Door Rule
Step plates in correct order (I → II → III) within 10 seconds → Chrono Seal dissolves.

---

## 4. Interior Map — "Hall of Edited Hours"

| Property | Value |
|----------|-------|
| **Size** | 64 × 48 tiles |
| **Lighting** | Cool blue, faint ticking, drifting motes like falling dust |
| **Encounters** | OFF |

### Layout Overview

| Room | Name | Type |
|------|------|------|
| Room 1 | Vestibule | Safe zone |
| Room 2 | Record Loom Gallery | Main puzzle area |
| Room 3 | Timestamp Cloister | Save + warp |
| Room 4 | Time-Lock Door | Portal to Trial Chamber |

### Anchors & Coordinates (local 0–63, 0–47)

#### Entry / Flow

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Interior entry spawn | (32, 44) | From exterior door |
| Return door to overworld | (32, 46) | Exit to Ledger Cliffwalk |
| Trial Door (Time-Lock Seal) | (32, 6) | Locked until puzzle solved |

#### Safe Utilities

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Save Crystal | (12, 38) | Standard save point |
| Warp Sigil | (52, 38) | Unlocks after clear |
| Keeper lectern | (32, 38) | Optional NPC location |

#### Record Loom Puzzle Props

**Core Concept**: "Edit" a timeline strip so an event lands on the correct timestamp.

| Object | Coordinates | Notes |
|--------|-------------|-------|
| **Timeline Strip Display** | y 22, x 14–50 | Visual lane |
| **Event Token (start)** | (14, 22) | Glowing bead, moves right automatically |
| **Target Timestamp Node** | (50, 22) | Goal destination |
| **Checkpoint Marker 1** | (28, 22) | Lever A pause point |
| **Checkpoint Marker 2** | (40, 22) | Lever B skip point |

**Edit Levers (3)** — Each changes strip behavior:

| Lever | Coordinates | Effect |
|-------|-------------|--------|
| Lever A (Delay) | (20, 28) | Token pauses 2s at Marker 1 |
| Lever B (Advance) | (32, 28) | Token skips ahead +3 tiles at Marker 2 |
| Lever C (Lock) | (44, 28) | Token immune to one "glitch" |

#### Locked Door

| Object | Coordinates | Unlock Condition |
|--------|-------------|------------------|
| Time-Lock Seal Door | (32, 6) | Event Token reaches Target Timestamp with exactly 2 edits applied |

---

## 5. Interior Puzzle — "Two Edits"

### Goal
Let the Event Token reach the Target Timestamp, but you must apply **exactly two edits** (not one, not three).

### Rules

| Element | Details |
|---------|---------|
| **Token Movement** | Moves at 1 tile/second along the strip |
| **Lever Effects** | Pulling a lever applies its effect for the remainder of the run |
| **Delay (A)** | Token pauses 2 seconds at Marker 1 |
| **Advance (B)** | Token skips ahead +3 tiles at Marker 2 |
| **Lock (C)** | Token becomes immune to one "glitch" |

### Glitch Event (Pressure)

| Property | Value |
|----------|-------|
| Timing | Every run, at 6 seconds in |
| Duration | 2 seconds |
| Effect | If token is in flicker zone without Lock, knocked back 2 tiles (soft fail) |

### Success/Failure Conditions

| Condition | Result |
|-----------|--------|
| Exactly 2 edits + Token arrives | ✓ SUCCESS → Door unlocks |
| 0–1 edits | ✗ "Insufficient revision" → Reset |
| 3 edits | ✗ "Overwritten record" → Reset |
| Glitch hits unprotected token | Soft fail, restart run |

> No damage. Just fast resets.

### Hint Plaque

**Near Lever B:**
> *"Two edits hold truth. Three makes fiction."*

---

## 6. Trial Chamber Submap — "Time-Lock Crucible"

| Property | Value |
|----------|-------|
| **Size** | 48 × 48 tiles |
| **Purpose** | Flicker slabs + stop zones + mini-boss that tries to rewind—player counters with Time Anchors |
| **Encounters** | ON (scripted boss fight only) |

### Anchors & Coordinates (local 0–47, 0–47)

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Entry portal spawn | (24, 44) | From Time-Lock Seal Door |
| Boss spawn | (24, 18) | Archivist Warden: Vell Orison |
| Exit portal | (24, 6) | Spawns after clear |
| Reward pedestal | (24, 10) | Time Blessing + loot |
| **Time Anchor A** | (12, 26) | Creates Time-Lock Field (cancels Stop → Slow) |
| **Time Anchor B** | (36, 26) | Creates Time-Lock Field (cancels Stop → Slow) |
| **Cover Pillar 1** | (14, 18) | 2×2 collision cover |
| **Cover Pillar 2** | (34, 18) | 2×2 collision cover |
| **Cover Pillar 3** | (14, 34) | 2×2 collision cover |
| **Cover Pillar 4** | (34, 34) | 2×2 collision cover |

---

## 7. Trial Script — "Vow of the Fixed Moment"

### Phase 0: Start
- Portal locks when player crosses y ≤ 40

### Phase 1: Flicker + Stillness Drill (30 seconds)

**Hazard A: Flicker Slabs**

| Property | Value |
|----------|-------|
| Frequency | Every 12 seconds |
| Telegraph | 1.4s shimmer |
| Active | 5.0s |
| Effect | Ending a turn on blank tile: Turn Delay +1 |

**Hazard B: Stillness Plate**

| Property | Value |
|----------|-------|
| Frequency | Every 18 seconds |
| Telegraph | 1.6s ticking grid |
| Active | 4.0s |
| Effect | Standing inside: STOP (short) + minor damage |
| Time-Lock Field | STOP becomes SLOW |

**Time Anchors**

| Property | Value |
|----------|-------|
| Interact time | 1.0s |
| Cooldown | 20s |
| Effect | Creates Time-Lock Field (8s, radius ~5) |

### Phase 2: Mini-Boss — Archivist Warden: Vell Orison

#### Boss Identity
Tries to rewind itself; player uses anchors to deny it.

#### Move List

| Move | Type | Telegraph | Effect |
|------|------|-----------|--------|
| **Secondhand Cleave** | Line | 0.9s | Damage |
| **Delay Citation** | Target stamp | 0.9s | Applies Slow + Turn Delay |
| **Afterimage Cut** | Delayed strike | 1.0s | Hits 2s later |
| **RECORD REWIND** | Signature | 2.2s clock vignette | Heal + cleanse (counterable) |

#### RECORD REWIND (Signature Mechanic)

| Trigger | One-time at 40% HP OR when taking burst damage quickly |
|---------|--------------------------------------------------------|
| Telegraph | 2.2s clock vignette + loud tick |
| Effect if resolves | Heals boss by up to 15% max HP + clears 1 debuff |
| Counter | Activate Time Anchor Time-Lock Field before completion → cast fails + boss becomes EXPOSED for 8s |

### Clear Condition
Defeat Vell Orison → Exit portal spawns + Reward pedestal unlocks.

---

## 8. Rewards + Flags

### Reward Pedestal Contents

#### Blessing: Benediction of the Fixed Second

| Property | Value |
|----------|-------|
| **Type** | Time Blessing |
| **Effect** | +Time resistance; Once per battle, negate one Turn Delay/Stop effect on the party member who would be hit first; When you cancel a rewind/stop effect, gain a short Haste window |

#### Unique Item Drops

| Item | Type |
|------|------|
| Time Core Shard | Craft component / resonance upgrade |
| Chrono Sigil | Optional: unlocks Time-aligned node / summon enhancement |

#### Optional Treasure Chest

| Property | Value |
|----------|-------|
| Location | (40, 12) in Trial Chamber |
| Contents | Materials + currency + 1 Time-leaning accessory roll |

### Game Flags

| Flag | Trigger |
|------|---------|
| `SHRINE_TIME_FOUND` | Entering Ledger Cliffwalk |
| `SHRINE_TIME_CLEARED` | Defeating Vell Orison |
| `BLESSING_TIME_UNLOCKED` | Collecting from reward pedestal |
| `WARP_TIME_SHRINE_UNLOCKED` | Clearing the shrine |

---

## 9. NPC/Voice Lines

### Chronicle Keeper (Timestamp Cloister, at 32, 38)

| Context | Line |
|---------|------|
| Greeting | *"Two edits. No more."* |
| Puzzle Hint | *"Lock the moment when it matters."* |
| After Clear | *"Your record held."* |

---

## 10. Quick Reference

### Coordinate Summary

#### Exterior (Ledger Cliffwalk) — 40×28
```
Entry: (20, 26)      Door: (20, 4)
Plate 1: (12, 18)    Plate 2: (28, 18)    Plate 3: (20, 12)
Save: (6, 20)        Hint Mural: (20, 9)  Plaque: (20, 7)

--- Order Hint ---
I → II → III (shown on mural)
```

#### Interior (Hall of Edited Hours) — 64×48
```
Entry: (32, 44)           Exit: (32, 46)
Save: (12, 38)            Warp: (52, 38)
Keeper: (32, 38)          Trial Door: (32, 6)

--- Puzzle ---
Timeline Strip: y 22, x 14–50
Event Token Start: (14, 22)    Target Node: (50, 22)
Marker 1: (28, 22)             Marker 2: (40, 22)
Lever A-Delay: (20, 28)        Lever B-Advance: (32, 28)
Lever C-Lock: (44, 28)

--- Glitch ---
At 6s: 2s flicker window
Unprotected: -2 tiles knockback
```

#### Trial Chamber (Time-Lock Crucible) — 48×48
```
Entry: (24, 44)           Boss: (24, 18)
Exit: (24, 6)             Reward: (24, 10)
Time Anchor A: (12, 26)   Time Anchor B: (36, 26)
Pillars: (14,18) (34,18) (14,34) (34,34)
```

---

## 11. Implementation Notes

- **Record Plate order**: Mural clearly shows I → II → III sequence; 10-second window to complete
- **Event Token**: Automatic movement at 1 tile/second; track position in real-time
- **Edit tracking**: Count lever pulls per run; must equal exactly 2 for success
- **Glitch timing**: Fixed at 6 seconds; check if token is in flicker zone (x ~30–38) and lacks Lock buff
- **Flicker Slabs**: Apply Turn Delay debuff on turn end if standing on affected tiles
- **Stillness Plate**: STOP → check for Time-Lock Field, convert to SLOW if present
- **RECORD REWIND**: Cast time allows for anchor activation; expose mechanic rewards proper counterplay
