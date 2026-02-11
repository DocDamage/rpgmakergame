# Shrine Map Sheet: Gravestone Monad Sanctum (Mass Shrine)

## 1. Overview

| Attribute | Value |
|-----------|-------|
| **Shrine Name** | Gravestone Monad Sanctum |
| **Element** | Mass |
| **Role** | Optional shrine that grants a Mass Blessing + a Mass craft core |
| **Theme** | Gravity as doctrine—weight, stillness, and controlled collapse |
| **Recommended Level** | 150–210 (scales if entered late) |
| **Total Footprint** | 1 exterior micro-map + 1 interior map + 1 trial chamber submap |
| **Tile Scale** | 16×16 px |

---

## 2. World Placement + Access

### Overworld Location
- **Position**: Off the bleak ridge between Gravemark Outpost and Frozen Citadel approach routes
- **Description**: A side spur with broken stone rings
- **Node Label**: `Mass Shrine — Gravestone Monad`
- **Map Icon**: Black ring + dot

### Access Rule
- Door is sealed by **Inertia Lock**
- Open by placing **3 Weight Stones** onto pressure plates in the exterior micro-map (simple push puzzle)

---

## 3. Exterior Micro-Map — "Weightstep Causeway"

| Property | Value |
|----------|-------|
| **Size** | 40 × 28 tiles |
| **Purpose** | Quick push/plate unlock, minimal friction |
| **Encounters** | OFF |

### Key Anchors (local 0–39, 0–27)

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Entry from overworld | (20, 26) | Player spawn point |
| Shrine door (Inertia Lock) | (20, 4) | Opens when all plates pressed |
| Save lantern (optional) | (6, 20) | Pre-shrine save point |
| **Weight Stone A** | (12, 18) | Push to plate |
| **Weight Stone B** | (28, 18) | Push to plate |
| **Weight Stone C** | (20, 12) | Push to plate |
| **Plate A** | (10, 10) | Target for Weight Stone A |
| **Plate B** | (30, 10) | Target for Weight Stone B |
| **Plate C** | (20, 8) | Target for Weight Stone C |
| Flavor plaque | (20, 7) | *"Only weight that is chosen becomes strength."* |

### Door Rule
All 3 plates pressed → Inertia Lock clicks open (stone ring rotates).

---

## 4. Interior Map — "Hall of Still Weight"

| Property | Value |
|----------|-------|
| **Size** | 64 × 48 tiles |
| **Lighting** | Cold stone, heavy shadows, slow drifting dust |
| **Encounters** | OFF |

### Layout Overview

| Room | Name | Type |
|------|------|------|
| Room 1 | Vestibule | Safe zone |
| Room 2 | Gravity Lattice | Main puzzle area |
| Room 3 | Anchor Cloister | Save + warp |
| Room 4 | Compression Seal Door | Portal to Trial Chamber |

### Anchors & Coordinates (local 0–63, 0–47)

#### Entry / Flow

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Interior entry spawn | (32, 44) | From exterior door |
| Return door to overworld | (32, 46) | Exit to Weightstep Causeway |
| Trial Door (Compression Seal) | (32, 6) | Locked until puzzle solved |

#### Safe Utilities

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Save Crystal | (12, 38) | Standard save point |
| Warp Sigil | (52, 38) | Unlocks after clear |
| Keeper spot | (32, 38) | Optional NPC location |

#### Gravity Lattice Puzzle Props

**Core Concept**: Stabilize a gravity field by activating anchors in the right order.

| Object | Coordinates | Notes |
|--------|-------------|-------|
| **Mass Anchor N** | (32, 18) | North anchor point |
| **Mass Anchor S** | (32, 30) | South anchor point |
| **Mass Anchor W** | (22, 24) | West anchor point |
| **Mass Anchor E** | (42, 24) | East anchor point |
| **Gravity Orb Spawn L** | (18, 28) | Drifting hazard (left) |
| **Gravity Orb Spawn R** | (46, 28) | Drifting hazard (right) |
| **Stability Meter Pedestal** | (32, 24) | Visual feedback only |

#### Locked Door

| Object | Coordinates | Unlock Condition |
|--------|-------------|------------------|
| Compression Seal Door | (32, 6) | Stability Meter reaches 100% (three successful anchor cycles) |

---

## 5. Interior Puzzle — "Stability Cycles"

### Goal
Complete 3 Stability Cycles by "pinning" drifting gravity orbs with the correct anchors.

### Rules

| Element | Details |
|---------|---------|
| **Gravity Orbs** | Two orbs drift slowly toward the center |
| **Compression Pulse** | When an orb crosses the center ring, it causes a pulse and resets progress |
| **Anchor Activation** | Creates a Stability Field for 6 seconds that pushes or pulls orbs slightly |

### Correct Solve Pattern

| Hint Source | Pattern |
|-------------|---------|
| Floor engravings | N → E → S → W (clockwise stabilization) |
| Progress | Each correct activation within a 10-second window advances Stability Meter by 25% |
| Wrong order | No punishment—just doesn't advance |

### Telegraphs

| State | Visual | Audio |
|-------|--------|-------|
| Correct anchor | Meter ticks up | Deep "thunk" |
| Orb near center | Warning indicator | Rumble grows louder |

---

## 6. Trial Chamber Submap — "Compression Crucible"

| Property | Value |
|----------|-------|
| **Size** | 48 × 48 tiles |
| **Purpose** | Gravity wells + slam timing + mini-boss that punishes being pulled to center |
| **Encounters** | ON (scripted boss fight only) |

### Anchors & Coordinates (local 0–47, 0–47)

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Entry portal spawn | (24, 44) | From Compression Seal Door |
| Boss spawn | (24, 18) | Monad Warden: Brimstone Colossus |
| Exit portal | (24, 6) | Spawns after clear |
| Reward pedestal | (24, 10) | Mass Blessing + loot |
| **Stability Totem A** | (10, 26) | Creates anti-pull Stability bubble |
| **Stability Totem B** | (38, 26) | Creates anti-pull Stability bubble |
| **Cover Monolith 1** | (14, 18) | 2×2 collision cover |
| **Cover Monolith 2** | (34, 18) | 2×2 collision cover |
| **Cover Monolith 3** | (14, 34) | 2×2 collision cover |
| **Cover Monolith 4** | (34, 34) | 2×2 collision cover |

---

## 7. Trial Script — "Vow of Gravity"

### Phase 0: Start
- Portal locks when player crosses y ≤ 40

### Phase 1: Gravity Well Drill (30 seconds)

**Hazard: "Singularity Pits"**

| Property | Value |
|----------|-------|
| Spawn | Every 16 seconds: spawn 2 wells |
| Telegraph | 1.5s dark ring + low hum |
| Active | 8.0s |
| Effect | Pull 1 tile per 2s; if pulled at least once → applies Heavy +1 |

**Stability Totems**

| Property | Value |
|----------|-------|
| Interact time | 1.0s |
| Cooldown | 20s |
| Effect | Creates Stability bubble (8s): reduces pull and clears 1 Heavy |

### Phase 2: Mini-Boss — Monad Warden: Brimstone Colossus

#### Boss Identity
Compression slams + pulls; players must "stabilize" at the right times.

#### Move List

| Move | Type | Telegraph | Effect |
|------|------|-----------|--------|
| **Grav Hook** | Single target pull | 1.0s tether line | Pulls target |
| **Weightfall** | Center slam | 2.0s rumble + expanding circle | Heavy area damage |
| **Grav Ripple** | Sweeping lanes | 1.2s lane highlight | Lane damage |
| **Anchor Breaker** | Signature | 2.2s sigil stamp on target | Massive damage (reduced by Stability bubble) |

#### Counterplay

| Mechanic | Effect |
|----------|--------|
| Stability bubble | Standing inside when Anchor Breaker resolves reduces damage massively |
| Positioning | Stay away from center to avoid slam follow-up |

### Clear Condition
Defeat Brimstone Colossus → Exit portal spawns + Reward pedestal unlocks.

---

## 8. Rewards + Flags

### Reward Pedestal Contents

#### Blessing: Monad's Gravity Oath

| Property | Value |
|----------|-------|
| **Type** | Mass Blessing |
| **Effect** | +Mass resistance; First time each battle you would be pulled/knocked back, negate it; When you gain Heavy, gain a small barrier (once per turn max) |

#### Unique Item Drops

| Item | Type |
|------|------|
| Mass Core Shard | Craft component / resonance upgrade |
| Grav Sigil | Optional: unlocks Mass-aligned node / summon enhancement |

#### Optional Treasure Chest

| Property | Value |
|----------|-------|
| Location | (40, 12) in Trial Chamber |
| Contents | Materials + currency + 1 Mass-leaning accessory roll |

### Game Flags

| Flag | Trigger |
|------|---------|
| `SHRINE_MASS_FOUND` | Entering Weightstep Causeway |
| `SHRINE_MASS_CLEARED` | Defeating Brimstone Colossus |
| `BLESSING_MASS_UNLOCKED` | Collecting from reward pedestal |
| `WARP_MASS_SHRINE_UNLOCKED` | Clearing the shrine |

---

## 9. NPC/Voice Lines

### Monad Keeper (Anchor Cloister, at 32, 38)

| Context | Line |
|---------|------|
| Greeting | *"Weight is honesty."* |
| Puzzle Hint | *"Clockwise. Stabilize the drift."* |
| After Clear | *"You didn't collapse. You held."* |

---

## 10. Quick Reference

### Coordinate Summary

#### Exterior (Weightstep Causeway) — 40×28
```
Entry: (20, 26)      Door: (20, 4)
Weight Stone A: (12, 18)    Weight Stone B: (28, 18)    Weight Stone C: (20, 12)
Plate A: (10, 10)           Plate B: (30, 10)           Plate C: (20, 8)
Save: (6, 20)               Plaque: (20, 7)
```

#### Interior (Hall of Still Weight) — 64×48
```
Entry: (32, 44)           Exit: (32, 46)
Save: (12, 38)            Warp: (52, 38)
Keeper: (32, 38)          Trial Door: (32, 6)

--- Puzzle ---
Stability Pedestal: (32, 24)
Anchor N: (32, 18)        Anchor S: (32, 30)
Anchor W: (22, 24)        Anchor E: (42, 24)
Orb Spawn L: (18, 28)     Orb Spawn R: (46, 28)

--- Pattern ---
Clockwise: N → E → S → W
```

#### Trial Chamber (Compression Crucible) — 48×48
```
Entry: (24, 44)           Boss: (24, 18)
Exit: (24, 6)             Reward: (24, 10)
Stability Totem A: (10, 26)   Stability Totem B: (38, 26)
Monoliths: (14,18) (34,18) (14,34) (34,34)
```

---

## 11. Implementation Notes

- **Weight Stones**: Standard pushable objects (similar to block puzzles)
- **Gravity Orbs**: Slow drift toward center (32, 24); speed increases slightly as they approach
- **Anchor activation**: Creates directional push/pull force field affecting orbs
- **Compression Pulse**: Reset Stability Meter to 0%; visual shockwave effect
- **Singularity Wells**: Pull vector toward well center; apply Heavy debuff on successful pull
- **Stability bubble**: Zone buff that nullifies pull effects and clears Heavy stacks
- **Anchor Breaker**: Check if target is inside Stability bubble at resolution time for damage reduction
