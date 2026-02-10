# Chroma's Edge — Shrine Map Sheet (v1)
## Pyreheart Reliquary (Heat Shrine)

---

## 0) Overview

| Parameter | Value |
|-----------|-------|
| **Shrine Name** | Pyreheart Reliquary |
| **Foundation** | Heat |
| **Role** | Optional shrine granting Heat Blessing + Heat craft core |
| **Theme** | Sacred furnace-temple—controlled flame, vows, "heat without ruin" |
| **Recommended Level** | 120–170 (scales if entered late) |
| **Total Footprint** | 1 exterior micro + 1 interior map + 1 trial chamber submap |
| **Tile Scale** | 16×16 px |

---

## 1) World Placement + Access

### Overworld Location

| Property | Value |
|----------|-------|
| **Location** | Volcanic band between Cinderstep and Obsidian Quarry (side spur, off critical path) |
| **Access Rule** | Always accessible once player reaches region; shrine trial door requires Heat attunement OR "ignite 3 braziers" puzzle |
| **Node Label** | Heat Shrine — Pyreheart Reliquary |
| **Map Icon** | Small flame inside a ring |

---

## 2) Sheet Specs

| Map | Size | Encounters |
|-----|------|------------|
| **Exterior Micro** | 40 × 28 tiles | OFF |
| **Interior (Reliquary Hall)** | 64 × 48 tiles | OFF in halls, ON in trial chamber (scripted) |
| **Trial Chamber (Pyreheart Crucible)** | 48 × 48 tiles | Scripted trial |

---

## 3) Exterior Micro-Map — "Ashgate Ledge"

### Purpose
Transition from overworld → shrine, quick risk flavor, no long dungeon.

### Key Anchors (Local 0–39, 0–27)

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Entry from overworld** | (20, 26) | — |
| **Shrine door** | (20, 4) | Big stone gate, heat haze |
| **Save lantern** (optional) | (6, 20) | — |
| **Jumpable lava crack** | x 10–30 at y 14 | Visual hazard only |

### Interactables

| Feature | Coordinates | Text |
|---------|-------------|------|
| **Lore plaque** | (20, 8) | "The flame remembers the vow." |

---

## 4) Interior Map — "Reliquary Hall"

### Lighting
Warm orange, furnace glow, ash motes.

### Layout Overview

| Room | Purpose |
|------|---------|
| **Room 1** | Entry Vestibule (safe) |
| **Room 2** | Furnace Nave (main puzzle) |
| **Room 3** | Ember Cloister (save + warp) |
| **Room 4** | Seal Door → Trial Chamber portal |

### Anchors & Coordinates (Local 0–63, 0–47)

#### Entry / Flow

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Interior entry spawn** | (32, 44) | — |
| **Return door to overworld** | (32, 46) | — |
| **To Trial Chamber door** | (32, 6) | Locked until puzzle solved |

#### Core Props

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Save Crystal** | (12, 38) | — |
| **Warp Sigil** | (52, 38) | Unlocks after clear |
| **Vendor/Keeper spot** | (32, 38) | Optional NPC |

#### Puzzle Objects (Furnace Nave)

| Brazier | Coordinates |
|---------|-------------|
| **Brazier A** | (18, 24) |
| **Brazier B** | (46, 24) |
| **Brazier C** | (18, 16) |
| **Brazier D** | (46, 16) |

| Valve Wheel | Coordinates | Controls |
|-------------|-------------|----------|
| **Valve Wheel 1** | (28, 28) | Horizontal conduit segment |
| **Valve Wheel 2** | (36, 28) | Horizontal conduit segment |
| **Valve Wheel 3** | (28, 12) | Vertical conduit segment |
| **Valve Wheel 4** | (36, 12) | Vertical conduit segment |

#### Heat Conduit Channels (Floor Lanes)

| Lane | Bounds |
|------|--------|
| **Horizontal** | y 20–21 from x 14–50 |
| **Vertical** | x 32–33 from y 12–28 |

#### Locked Door

| Feature | Coordinates | Unlock Condition |
|---------|-------------|------------------|
| **Trial Seal Door** | (32, 6) | All 4 braziers lit simultaneously for 5 seconds |

---

## 5) Reliquary Hall Puzzle — "Conduit Balance"

### Goal
Route heat to light all four braziers at once without "overloading" a line.

### How It Works

| Mechanic | Description |
|----------|-------------|
| **Valve Wheels** | Toggle conduit segments ON/OFF |
| **Heat Flow** | When ON, heat flows through segment and lights connected braziers |

### Overload Rule

| Condition | Effect |
|-----------|--------|
| **Trigger** | >2 braziers fed through same vertical trunk (x 32–33) for 6 seconds |
| **Result** | "Vents" — all braziers go out |
| **Telegraph** | Conduit turns bright white → hiss → vent burst |

### Player Hinting

| Feature | Location | Text |
|---------|----------|------|
| **Wall plaque** | Near Valve Wheel 2 | "Two flames may share a throat. Four will choke it." |

### Fail State

| Effect | Description |
|--------|-------------|
| **Vent burst** | Knocks party back 1 tile + minor chip |
| **Punishment** | None besides reset |

---

## 6) Trial Chamber Submap — "Pyreheart Crucible"

### Purpose
One clean scripted trial: movement + heat management + mini-boss.

### Anchors & Coordinates (Local 0–47, 0–47)

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Entry portal spawn** | (24, 44) | — |
| **Boss spawn** | (24, 18) | Pyre Warden |
| **Exit portal** (post-clear) | (24, 6) | — |
| **Trial reward pedestal** | (24, 10) | — |

#### Hazards

| Heat Grate | Coordinates |
|------------|-------------|
| **Grate 1** | (14, 18) |
| **Grate 2** | (34, 18) |
| **Grate 3** | (14, 30) |
| **Grate 4** | (34, 30) |

| Cooling Rune | Coordinates | Effect |
|--------------|-------------|--------|
| **Rune L** | (10, 24) | Stand to reduce Overheat |
| **Rune R** | (38, 24) | Stand to reduce Overheat |

---

## 7) Trial Script — "Vow of Controlled Flame"

### Phase 0: Start

| Trigger | Effect |
|---------|--------|
| **Step past y ≤ 40** | Doors/portal lock |

### Phase 1: Heat Pattern (30 seconds)

| Property | Description |
|----------|-------------|
| **Pattern** | Heat grates pulse clockwise |
| **Telegraph** | 1.2s glow → 3.0s active |
| **Effect** | Standing on active grate: Overheat +2 stacks |

### Phase 2: Mini-Boss — Pyre Warden

| Property | Value |
|----------|-------|
| **HP** | Mid (tuned to region) |
| **Theme** | Applies Overheat, punishes standing still |

#### Moves

| Move | Description | Telegraph |
|------|-------------|-----------|
| **Cinder Arc** | Cone attack | 1.0s |
| **Brand Sigil** | Target mark | 0.8s |
| **Furnace Ring** | AOE ring | 1.4s |
| **Temper Check** | Small burst if player hits 8 Overheat | Reactive (not wipe) |

#### Counterplay

| Mechanic | Effect |
|----------|--------|
| **Cooling Runes** | Reduce Overheat by 1/second, prevent exceeding 6 stacks |

### Clear Condition

| Trigger | Effect |
|---------|--------|
| **Defeat Pyre Warden** | Unlock exit portal + reward pedestal |

---

## 8) Rewards + Flags

### Reward Pedestal: Heat Blessing

| Property | Value |
|----------|-------|
| **Blessing Name** | Pyreheart Benediction |
| **Effect** | +Heat resistance; first time per battle you would gain Overheat past 6, cap it at 6 and gain small barrier |

### Unique Item Drop

| Item | Purpose |
|------|---------|
| **Heat Core Shard** | Craft component / resonance upgrade |
| **Ember Sigil** | Unlocks Heat-aligned skill node or summon enhancement |

### Treasure Chest

| Property | Value |
|----------|-------|
| **Location** | (40, 12) in Trial Chamber |
| **Contains** | Mid-tier mats + currency + 1 Heat-aligned accessory roll |

### Flags

| Flag | Condition |
|------|-----------|
| `SHRINE_HEAT_FOUND` | TRUE |
| `SHRINE_HEAT_CLEARED` | TRUE |
| `BLESSING_HEAT_UNLOCKED` | TRUE |
| `WARP_HEAT_SHRINE_UNLOCKED` | TRUE (enables warp sigil in hall) |

---

## 9) NPC/Voice (Optional One-Liners)

### Ashbound Keeper (Reliquary Hall, at 32,38)

| Context | Line |
|---------|------|
| **General** | "Flame is not fury. It's focus." |
| **Puzzle hint** | "Light all four. Don't choke the throat." |
| **After clear** | "Your heat holds shape. Good." |

---

## Quick Reference: Shrine Layout

```
EXTERIOR — ASHGATE LEDGE (40×28)
├─ Entry (20,26)
├─ Save lantern (6,20)
├─ Lava crack (x10–30, y14) [visual]
├─ Lore plaque (20,8)
└─ Shrine door (20,4) → INTERIOR

INTERIOR — RELIQUARY HALL (64×48)
Room 1: Entry Vestibule (safe)
  └─ Entry (32,44), Return (32,46)

Room 2: Furnace Nave (puzzle)
  ├─ Braziers: A(18,24), B(46,24), C(18,16), D(46,16)
  ├─ Valves: 1(28,28), 2(36,28), 3(28,12), 4(36,12)
  ├─ Conduits: Horizontal (y20–21, x14–50), Vertical (x32–33, y12–28)
  └─ Hint plaque (near Valve 2)

Room 3: Ember Cloister (save/warp)
  ├─ Save Crystal (12,38)
  ├─ Warp Sigil (52,38) [post-clear]
  └─ Keeper (32,38)

Room 4: Trial Seal Door (32,6)
  └─ Unlocks: All 4 braziers lit 5s simultaneously

TRIAL CHAMBER — PYREHEART CRUCIBLE (48×48)
├─ Entry portal (24,44)
├─ Heat Grates: (14,18), (34,18), (14,30), (34,30)
├─ Cooling Runes: (10,24), (38,24)
├─ Boss: Pyre Warden (24,18)
├─ Reward pedestal (24,10)
├─ Treasure chest (40,12)
└─ Exit portal (24,6) [post-clear]

PUZZLE SOLUTION HINT:
├─ Goal: Light all 4 braziers simultaneously
├─ Constraint: >2 braziers through vertical trunk (x32–33) = vent
├─ Hint: "Two flames may share a throat. Four will choke it."
└─ Strategy: Balance horizontal/vertical flow

PYRE WARDEN FIGHT:
├─ Heat grates pulse clockwise (1.2s glow, 3s active)
├─ Overheat management via Cooling Runes
├─ Moves: Cinder Arc, Brand Sigil, Furnace Ring
└─ Temper Check at 8 Overheat (burst, not wipe)

REWARDS:
├─ Blessing: Pyreheart Benediction (Overheat cap + barrier)
├─ Items: Heat Core Shard, Ember Sigil
├─ Chest: Mid mats + Heat accessory
└─ Warp unlock for shrine
```
