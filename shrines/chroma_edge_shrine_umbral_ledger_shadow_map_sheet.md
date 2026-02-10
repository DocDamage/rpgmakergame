# Shrine Map Sheet: Umbral Ledger Sepulcher (Shadow Shrine)

## 1. Overview

| Attribute | Value |
|-----------|-------|
| **Shrine Name** | Umbral Ledger Sepulcher |
| **Element** | Shadow |
| **Role** | Optional shrine that grants a Shadow Blessing + a Shadow craft core |
| **Theme** | Veils, echoes, and "truth hidden in absence"—reading what's missing, not brute forcing darkness |
| **Recommended Level** | 170–230 (scales if entered late) |
| **Total Footprint** | 1 exterior micro-map + 1 interior map + 1 trial chamber submap |
| **Tile Scale** | 16×16 px |

---

## 2. World Placement + Access

### Overworld Location
- **Position**: Off the ruined corridor between Old Lumencrest (Outer Wards) and the Archive District approach
- **Description**: Down a collapsed stair into a quiet undercroft (side spur, clearly optional)
- **Node Label**: `Shadow Shrine — Umbral Ledger`
- **Map Icon**: Crescent + notch

### Access Rule
- Door sealed by **Veil Lock**
- Open by lighting **3 Shade Lanterns** in the exterior approach in the correct order (shown by lantern chains' lengths: short → medium → long)

---

## 3. Exterior Micro-Map — "Veilstep Undercroft"

| Property | Value |
|----------|-------|
| **Size** | 40 × 28 tiles |
| **Purpose** | Quick lantern-order unlock with clear visual hinting |
| **Encounters** | OFF |

### Key Anchors (local 0–39, 0–27)

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Entry from overworld | (20, 26) | Player spawn point |
| Shrine door (Veil Lock) | (20, 4) | Opens when lanterns lit in correct order |
| Save lantern (optional) | (6, 20) | Pre-shrine save point |
| **Shade Lantern A** (short chain) | (12, 18) | Interact to light |
| **Shade Lantern B** (medium chain) | (28, 18) | Interact to light |
| **Shade Lantern C** (long chain) | (20, 10) | Interact to light |
| Flavor plaque | (20, 8) | *"The shadow is not a lie. It's a boundary."* |

### Door Rule
Light short → medium → long within 12 seconds → Veil Lock unknots → door opens.

---

## 4. Interior Map — "Ledger of the Unseen"

| Property | Value |
|----------|-------|
| **Size** | 64 × 48 tiles |
| **Lighting** | Low, cool violet; readable silhouettes; faint whisper SFX |
| **Encounters** | OFF |

### Layout Overview

| Room | Name | Type |
|------|------|------|
| Room 1 | Vestibule | Safe zone |
| Room 2 | Echo Gallery | Main puzzle area |
| Room 3 | Quiet Cloister | Save + warp |
| Room 4 | Null Seal Door | Portal to Trial Chamber |

### Anchors & Coordinates (local 0–63, 0–47)

#### Entry / Flow

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Interior entry spawn | (32, 44) | From exterior door |
| Return door to overworld | (32, 46) | Exit to Veilstep Undercroft |
| Trial Door (Null Seal) | (32, 6) | Locked until puzzle solved |

#### Safe Utilities

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Save Crystal | (12, 38) | Standard save point |
| Warp Sigil | (52, 38) | Unlocks after clear |
| Keeper spot | (32, 38) | Optional NPC location |

#### Echo Gallery Puzzle Props

**Core Concept**: Guide a "True Path" by stepping on the tiles that are missing from a pattern (shadow logic).

| Object | Coordinates | Notes |
|--------|-------------|-------|
| **Pattern Projector** | (32, 30) | Casts floor pattern |
| **Veil Plate 1** | (22, 24) | Stepping panel |
| **Veil Plate 2** | (42, 24) | Stepping panel |
| **Veil Plate 3** | (22, 18) | Stepping panel |
| **Veil Plate 4** | (42, 18) | Stepping panel |
| **Null Ink Node A** | (18, 14) | Target node |
| **Null Ink Node B** | (32, 12) | Target node |
| **Null Ink Node C** | (46, 14) | Target node |

#### Locked Door

| Object | Coordinates | Unlock Condition |
|--------|-------------|------------------|
| Null Seal Door | (32, 6) | Activate all 3 Null Ink Nodes by stepping on the missing tiles in the correct sequence |

---

## 5. Interior Puzzle — "The Missing Pattern"

### Goal
Three times, the floor projects a pattern and removes 4 tiles (they become "missing/void tiles"). Step on those missing tiles in the right order to charge each Null Ink Node.

### Rules

| Element | Details |
|---------|---------|
| **Start** | Interact with the Pattern Projector to begin a round |
| **Grid Area** | 6×6 center (x 26–38, y 16–28) lights up with pattern |
| **Missing Tiles** | 4 tiles go dark (void tiles) |
| **Order** | Step on missing tiles in displayed order (faint numbers 1–4) |
| **Progress** | Completing the order charges one Node (A → B → C) |

### Fail Behavior (no punishment)
Step on a lit (non-missing) tile → pattern resets immediately (soft fail, no damage).

### Hinting

**Plaque near Plate 2:**
> *"Read what isn't there."*

---

## 6. Trial Chamber Submap — "Nullcourt Crucible"

| Property | Value |
|----------|-------|
| **Size** | 48 × 48 tiles |
| **Purpose** | Veil zones + echo adds + buff suppression with clean counterplay |
| **Encounters** | ON (scripted boss fight only) |

### Anchors & Coordinates (local 0–47, 0–47)

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Entry portal spawn | (24, 44) | From Null Seal Door |
| Boss spawn | (24, 18) | Sepulcher Warden: Nyx Scriptor |
| Exit portal | (24, 6) | Spawns after clear |
| Reward pedestal | (24, 10) | Shadow Blessing + loot |
| **Ward Mirror A** | (12, 26) | Creates anti-dispel ward field |
| **Ward Mirror B** | (36, 26) | Creates anti-dispel ward field |
| **Null Fountain A** | (10, 34) | Cleanse Null Mark / Veil sickness |
| **Null Fountain B** | (38, 34) | Cleanse Null Mark / Veil sickness |
| **Cover Plinth 1** | (14, 18) | 2×2 collision cover |
| **Cover Plinth 2** | (34, 18) | 2×2 collision cover |
| **Cover Plinth 3** | (14, 34) | 2×2 collision cover |
| **Cover Plinth 4** | (34, 34) | 2×2 collision cover |

---

## 7. Trial Script — "Vow of the Unseen"

### Phase 0: Start
- Portal locks when player crosses y ≤ 40

### Phase 1: Veil Drill (30 seconds)

**Hazard A: Veil Curtains**

| Property | Value |
|----------|-------|
| Frequency | Every 18 seconds |
| Spawn | 2 veil patches |
| Telegraph | 1.0s smoky bloom |
| Active | 8.0s |
| Effect | Accuracy down/confounded-lite; increases chance of buff suppression landing |

**Hazard B: Null Lanes**

| Property | Value |
|----------|-------|
| Frequency | Every 14 seconds |
| Pattern | Two lane strikes |
| Telegraph | 1.4s thin violet lines |
| Effect | Medium damage + strips 1 buff (if any) |

### Phase 2: Mini-Boss — Sepulcher Warden: Nyx Scriptor

#### Boss Identity
Summons echo copies and strips buffs unless warded.

#### Move List

| Move | Type | Telegraph | Effect |
|------|------|-----------|--------|
| **Umbral Scythe** | Line | 0.8s | Damage |
| **Crown Lances** | 2 lanes | 1.2s | Lane damage |
| **Null Mark** | Target stamp | 0.9s | Next buff has high chance to vanish |
| **Echo Summons** | Adds | 1.2s shadow ripple | Spawns 1 echo (cap 2) that does chip + applies veil debuff |

#### Ward Mirrors (Counterplay)

| Property | Value |
|----------|-------|
| Interact time | 1.2s |
| Cooldown | 24s |
| Effect | WARD FIELD for 10s (radius ~5): buff strips reduced by 50%, Null Mark application reduced, echoes take extra damage while inside |

#### Null Fountains (Relief)

| Property | Value |
|----------|-------|
| Effect | Step to cleanse 1 major debuff (Null Mark → Veil sickness) |
| Cooldown | 20s |
| Limit (optional) | 3 uses total per fountain for tighter tuning |

### Clear Condition
Defeat Nyx Scriptor → Exit portal spawns + Reward pedestal unlocks.

---

## 8. Rewards + Flags

### Reward Pedestal Contents

#### Blessing: Benediction of the Veil

| Property | Value |
|----------|-------|
| **Type** | Shadow Blessing |
| **Effect** | +Shadow resistance; Once per battle, when a buff would be dispelled, prevent it and gain a short Ward (small barrier); Echo/illusion enemies take +damage from you for 6 seconds after you hit them |

#### Unique Item Drops

| Item | Type |
|------|------|
| Shadow Core Shard | Craft component / resonance upgrade |
| Umbral Sigil | Optional: unlocks Shadow-aligned node / summon enhancement |

#### Optional Treasure Chest

| Property | Value |
|----------|-------|
| Location | (40, 12) in Trial Chamber |
| Contents | Materials + currency + 1 Shadow-leaning accessory roll |

### Game Flags

| Flag | Trigger |
|------|---------|
| `SHRINE_SHADOW_FOUND` | Entering Veilstep Undercroft |
| `SHRINE_SHADOW_CLEARED` | Defeating Nyx Scriptor |
| `BLESSING_SHADOW_UNLOCKED` | Collecting from reward pedestal |
| `WARP_SHADOW_SHRINE_UNLOCKED` | Clearing the shrine |

---

## 9. NPC/Voice Lines

### Ledger Keeper (Quiet Cloister, at 32, 38)

| Context | Line |
|---------|------|
| Greeting | *"Step where the world is missing."* |
| Puzzle Hint | *"The veil is not the enemy. Your panic is."* |
| After Clear | *"You kept your shape in the dark."* |

---

## 10. Quick Reference

### Coordinate Summary

#### Exterior (Veilstep Undercroft) — 40×28
```
Entry: (20, 26)      Door: (20, 4)
Lantern A (short): (12, 18)    Lantern B (medium): (28, 18)
Lantern C (long): (20, 10)
Save: (6, 20)                  Plaque: (20, 8)

--- Order Hint ---
Short chain → Medium chain → Long chain
```

#### Interior (Ledger of the Unseen) — 64×48
```
Entry: (32, 44)           Exit: (32, 46)
Save: (12, 38)            Warp: (52, 38)
Keeper: (32, 38)          Trial Door: (32, 6)

--- Puzzle ---
Pattern Projector: (32, 30)
Veil Plate 1: (22, 24)    Veil Plate 2: (42, 24)
Veil Plate 3: (22, 18)    Veil Plate 4: (42, 18)
Node A: (18, 14)          Node B: (32, 12)          Node C: (46, 14)

--- Grid Area ---
6×6 center: x 26–38, y 16–28
```

#### Trial Chamber (Nullcourt Crucible) — 48×48
```
Entry: (24, 44)           Boss: (24, 18)
Exit: (24, 6)             Reward: (24, 10)
Ward Mirror A: (12, 26)   Ward Mirror B: (36, 26)
Null Fountain A: (10, 34) Null Fountain B: (38, 34)
Plinths: (14,18) (34,18) (14,34) (34,34)
```

---

## 11. Implementation Notes

- **Lantern chain lengths**: Visual indicator of correct order (short → medium → long); 12-second window
- **Missing pattern puzzle**: Project pattern → fade 4 tiles → display numbers 1–4 on void tiles
- **Step detection**: Check if player steps on non-void tile → instant reset; correct sequence charges node
- **Veil Curtains**: Accuracy debuff zone; also acts as amplifier for Null Mark success chance
- **Null Lanes**: Target buffs specifically; if no buffs present, just damage
- **Ward Mirror field**: Multi-purpose buff—reduce strip chance, reduce mark application, echo damage amp
- **Echo adds**: Cap at 2; chip damage + veil debuff application; vulnerable inside ward field
