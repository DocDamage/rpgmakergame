# Shrine Map Sheet: Verdant Covenant Grove (Growth Shrine)

## 1. Overview

| Attribute | Value |
|-----------|-------|
| **Shrine Name** | Verdant Covenant Grove |
| **Element** | Growth |
| **Role** | Optional shrine that grants a Growth Blessing + a Growth craft core |
| **Theme** | Ancient living temple—roots as locks, life as currency, "growth with restraint" |
| **Recommended Level** | 130–185 (scales if entered late) |
| **Total Footprint** | 1 exterior micro-map + 1 interior map + 1 trial chamber submap |
| **Tile Scale** | 16×16 px |

---

## 2. World Placement + Access

### Overworld Location
- **Position**: Off the marshwood corridor between Mirewatch and Fungal Depths
- **Description**: A side spur behind thick bramble—visible but not mandatory
- **Node Label**: `Growth Shrine — Verdant Covenant Grove`
- **Map Icon**: Leaf + ring

### Access Rule
- Shrine door is blocked by **Bramble Seal**
- Open by interacting with **3 Seed Totems** on the exterior approach (no combat required)

---

## 3. Exterior Micro-Map — "Bramblepath Hollow"

| Property | Value |
|----------|-------|
| **Size** | 40 × 28 tiles |
| **Purpose** | Short transition + "seed totems" door condition |
| **Encounters** | OFF |

### Key Anchors (local 0–39, 0–27)

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Entry from overworld | (20, 26) | Player spawn point |
| Shrine door (Bramble Seal) | (20, 4) | Opens when all totems activated |
| Save lantern (optional) | (6, 20) | Pre-shrine save point |
| **Seed Totem A** | (10, 18) | Required for entry |
| **Seed Totem B** | (30, 18) | Required for entry |
| **Seed Totem C** | (20, 10) | Required for entry |
| Stone plaque | (20, 8) | *"Life opens to those who listen."* |

### Door Rule
Activate all 3 Seed Totems → Bramble Seal "unlaces" (vine animation) → door opens.

---

## 4. Interior Map — "Covenant Hall"

| Property | Value |
|----------|-------|
| **Size** | 64 × 48 tiles |
| **Lighting** | Dappled green, drifting spores, soft bioluminescence |
| **Encounters** | OFF |

### Layout Overview

| Room | Name | Type |
|------|------|------|
| Room 1 | Rooted Vestibule | Safe zone |
| Room 2 | Lattice Garden | Main puzzle area |
| Room 3 | Bloom Cloister | Save + warp |
| Room 4 | Living Seal Door | Portal to Trial Chamber |

### Anchors & Coordinates (local 0–63, 0–47)

#### Entry / Flow

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Interior entry spawn | (32, 44) | From exterior door |
| Return door to overworld | (32, 46) | Exit to Bramblepath Hollow |
| Trial Door (Living Seal) | (32, 6) | Locked until puzzle solved |

#### Safe Utilities

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Save Crystal | (12, 38) | Standard save point |
| Warp Sigil | (52, 38) | Unlocks after clear |
| Keeper / altar spot | (32, 38) | Optional NPC location |

#### Puzzle Objects (Lattice Garden)

**Root Gates (4)** — Toggle open/closed

| Gate | Coordinates |
|------|-------------|
| Gate N | (32, 18) |
| Gate S | (32, 30) |
| Gate W | (22, 24) |
| Gate E | (42, 24) |

**Spore Lamps (4)** — Toggle nearby Root Gates

| Lamp | Coordinates | Affects |
|------|-------------|---------|
| Lamp 1 | (20, 18) | Nearby gates |
| Lamp 2 | (44, 18) | Nearby gates |
| Lamp 3 | (20, 30) | Nearby gates |
| Lamp 4 | (44, 30) | Nearby gates |

**Heartseed Pedestal (target)**

| Object | Coordinates |
|--------|-------------|
| Heartseed Pedestal | (32, 24) |

#### Locked Door

| Object | Coordinates | Unlock Condition |
|--------|-------------|------------------|
| Living Seal Door | (32, 6) | Heartseed reaches pedestal with exactly 2 root gates open |

---

## 5. Covenant Hall Puzzle — "Root Lattice Logic"

### Goal
Guide a living Heartseed (a glowing seed sprite that travels along root lines) to the Heartseed Pedestal—but you must keep the lattice "balanced."

### Mechanics

| Element | Details |
|---------|---------|
| **Heartseed Start** | (32, 34) — spawns when entering garden region |
| **Movement** | 1 tile/second along available root lines toward "brightest path" |
| **Spore Lamps** | Toggle nearby Root Gates open/closed |

### Balance Rule

| Gates Open | Result |
|------------|--------|
| **Exactly 2** | ✓ SUCCESS — Living Seal opens |
| **1** | ✗ "Starved" — seed withers → reset |
| **3–4** | ✗ "Wild growth" — overrun → reset |

### Telegraphs

| State | Visual | Audio |
|-------|--------|-------|
| Wither | Seed dims | Soft "dry crackle" SFX |
| Overrun | Roots surge | "Vine rush" SFX |

> **Reset is instant and non-punishing** (no damage), just time.

### Player Hint

**Plaque near Lamp 2:**
> *"Two paths feed the grove. More is hunger. Less is drought."*

---

## 6. Trial Chamber Submap — "Bloomwrit Crucible"

| Property | Value |
|----------|-------|
| **Size** | 48 × 48 tiles |
| **Purpose** | Movement + cleanse check + mini-boss with summons that must be pruned |
| **Encounters** | ON (scripted boss fight only) |

### Anchors & Coordinates (local 0–47, 0–47)

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Entry portal spawn | (24, 44) | From Living Seal Door |
| Boss spawn | (24, 18) | Covenant Warden: Mycel Regent |
| Exit portal | (24, 6) | Spawns after clear |
| Reward pedestal | (24, 10) | Growth Blessing + loot |
| **Purity Pool A** | (10, 26) | Reduces Vinebind + clears Spore Sickness |
| **Purity Pool B** | (38, 26) | 20s cooldown per pool |
| **Bramble Column 1** | (14, 18) | 2×2 collision cover |
| **Bramble Column 2** | (34, 18) | 2×2 collision cover |
| **Bramble Column 3** | (14, 34) | 2×2 collision cover |
| **Bramble Column 4** | (34, 34) | 2×2 collision cover |
| Optional chest | (40, 12) | Mats + currency + Growth-leaning accessory |

---

## 7. Trial Script — "Vow of Measured Growth"

### Phase 0: Start
- Lock portal when player crosses y ≤ 40

### Phase 1: Pruning Pattern (30 seconds)
- **Bramble Rings** appear under 2 tiles at a time
- **Telegraph**: 1.2s green circles → active 3.0s
- **Effect**: Standing inside inflicts Vinebind +2

### Phase 2: Mini-Boss — Covenant Warden: Mycel Regent

#### Boss Identity
Spawns "bud" adds that empower it unless pruned.

#### Move List

| Move | Type | Telegraph | Effect |
|------|------|-----------|--------|
| **Spore Lance** | Line | 1.0s thin line | Damage |
| **Root Snare** | Target circle | 1.3s | Bind/Root |
| **Bloomburst** | AOE ring | 1.4s expanding ring | Area damage |
| **Regrowth Edict** | Summon | 1.2s vine surge | Spawns 2 Bud Nodes (max 4) |

#### Bud Nodes

| Property | Value |
|----------|-------|
| Behavior | Stationary, low HP |
| Bloom Timer | 10 seconds |
| **If NOT killed:** | Bud "blooms" → Boss gains +3% HP regen per turn (stacking) |
| **On Death:** | Drops Pollen Spark pickup → reduces Vinebind by 2 |

#### Purity Pools

| Property | Value |
|----------|-------|
| Effect | Clears one major debuff (priority: Vinebind → Spore Sickness) |
| Cooldown | 20s per pool |

### Clear Condition
Defeat Mycel Regent → Exit portal spawns + Reward pedestal unlocks.

---

## 8. Rewards + Flags

### Reward Pedestal Contents

#### Blessing: Covenant of Renewal

| Property | Value |
|----------|-------|
| **Type** | Growth Blessing |
| **Effect** | +Growth resistance; Once per battle, when you would be bound/rooted, cleanse it instantly and gain a short Regen buff |

#### Unique Item Drops

| Item | Type |
|------|------|
| Growth Core Shard | Craft component / resonance upgrade |
| Verdant Sigil | Optional: unlocks Growth-aligned node / summon enhancement |

#### Optional Treasure Chest

| Property | Value |
|----------|-------|
| Location | (40, 12) in Trial Chamber |
| Contents | Materials + currency + 1 Growth-leaning accessory roll |

### Game Flags

| Flag | Trigger |
|------|---------|
| `SHRINE_GROWTH_FOUND` | Entering Bramblepath Hollow |
| `SHRINE_GROWTH_CLEARED` | Defeating Mycel Regent |
| `BLESSING_GROWTH_UNLOCKED` | Collecting from reward pedestal |
| `WARP_GROWTH_SHRINE_UNLOCKED` | Clearing the shrine |

---

## 9. NPC/Voice Lines

### Grove Keeper (Covenant Hall, at 32, 38)

| Context | Line |
|---------|------|
| Greeting | *"Growth is not speed. It's balance."* |
| Puzzle Hint | *"Two gates. No more. No less."* |
| After Clear | *"You pruned what needed pruning."* |

---

## 10. Quick Reference

### Coordinate Summary

#### Exterior (Bramblepath Hollow) — 40×28
```
Entry: (20, 26)      Door: (20, 4)
Totem A: (10, 18)    Totem B: (30, 18)    Totem C: (20, 10)
Save: (6, 20)        Plaque: (20, 8)
```

#### Interior (Covenant Hall) — 64×48
```
Entry: (32, 44)           Exit: (32, 46)
Save: (12, 38)            Warp: (52, 38)
Keeper: (32, 38)          Trial Door: (32, 6)

--- Puzzle ---
Heartseed Start: (32, 34)     Pedestal: (32, 24)
Gate N: (32, 18)              Gate S: (32, 30)
Gate W: (22, 24)              Gate E: (42, 24)
Lamp 1: (20, 18)              Lamp 2: (44, 18)
Lamp 3: (20, 30)              Lamp 4: (44, 30)
```

#### Trial Chamber (Bloomwrit Crucible) — 48×48
```
Entry: (24, 44)           Boss: (24, 18)
Exit: (24, 6)             Reward: (24, 10)
Pool A: (10, 26)          Pool B: (38, 26)
Chest: (40, 12)
Columns: (14,18) (34,18) (14,34) (34,34)
```

---

## 11. Implementation Notes

- **Heartseed movement**: 1 tile/second along root lines; pathfinding toward pedestal
- **Gate toggling**: Spore Lamps toggle associated Root Gates by proximity:
  - **Lamp 1** (20, 18) → toggles **Gate N** (32, 18) + **Gate W** (22, 24)
  - **Lamp 2** (44, 18) → toggles **Gate N** (32, 18) + **Gate E** (42, 24)
  - **Lamp 3** (20, 30) → toggles **Gate S** (32, 30) + **Gate W** (22, 24)
  - **Lamp 4** (44, 30) → toggles **Gate S** (32, 30) + **Gate E** (42, 24)
  - **Solution**: Activate Lamp 1 + Lamp 4 (or Lamp 2 + Lamp 3) to open exactly Gates N + S, creating direct path
- **Reset behavior**: Instant, no damage, Heartseed returns to (32, 34)
- **Bud Node bloom timer**: 10s countdown visible as growth animation
- **Purity Pool cooldown**: Track per-pool, 20s visual indicator when available
