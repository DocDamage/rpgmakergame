# Dungeon Map Sheet: The Remnant Vault — Postgame Endgame Loop

## 1. Overview

| Attribute | Value |
|-----------|-------|
| **Dungeon Name** | The Remnant Vault |
| **Type** | Post-Final Palace repeatable endgame dungeon |
| **Theme** | Reality leftovers—half-stitched rooms, edited geometry, echo-enemies that don't belong anywhere else |
| **Target Audience** | Players who cleared Final Palace; seeking materials, Origin upgrades, rare accessories, protocol currency, lore fragments |
| **Run Length** | 15–25 minutes per full clear (depending on tier) |
| **Tile Scale** | 16×16 px |

---

## 2. Unlock + Access

### Unlock Conditions

| Flag | Condition |
|------|-----------|
| `FINAL_PALACE_CLEARED` | Complete Final Palace |
| `PROGENITOR_ENGINE_DEFEATED` | Defeat Progenitor Engine |
| `AETHERREACH_ROUTE_OPEN` | True-ending route active |

### Primary Entry Point (Recommended)

| Location | Feature |
|----------|---------|
| **Aetherreach Notice Board** | "REMNANT VAULT: ACTIVE BREACH" |
| Result | Warps to Remnant Gatehouse (dungeon hub) |

### Secondary Entry Point (Optional)

| Location | Feature |
|----------|---------|
| **Old Lumencrest (Outer Wards)** | New collapsed stair / sealed rift door |
| Requirement | Remnant Key item to open |

---

## 3. Core Run Structure

### Layout Model: Hub + 3 Wings + Core Vault

```
┌─────────────────────────────────────────┐
│         REMNANT GATEHOUSE (Hub)         │
│   [Tier Select] [Vendor] [Forge]        │
│         [Wing A] [Wing B] [Wing C]      │
└───────────────────┬─────────────────────┘
                    │
        ┌───────────┼───────────┐
        ▼           ▼           ▼
   ┌─────────┐ ┌─────────┐ ┌─────────┐
   │Wing A   │ │Wing B   │ │Wing C   │
   │Clear    │ │Clear    │ │Clear    │
   │Objective│ │Objective│ │Objective│
   └────┬────┘ └────┬────┘ └────┬────┘
        │           │           │
        └───────────┼───────────┘
                    ▼
          ┌─────────────────┐
          │   VAULT SIGIL   │
          └────────┬────────┘
                   ▼
        ┌──────────────────────┐
        │    CORE VAULT        │
        │  (Boss + Rewards)    │
        └──────────────────────┘
```

### Replay Tiers

| Tiers | Modifiers | Scaling |
|-------|-----------|---------|
| 1–4 | 2 modifiers | Standard |
| 5+ | 3 modifiers | +enemy level, +reward scaling |

### Progress Guarantee
Every run grants deterministic crafting currency—no RNG brick.

---

## 4. Dungeon Identity Systems

### A) Remnant Modifiers ("Echo Rules")

Each run rolls modifiers displayed on entry UI:

| Modifier | Effect |
|----------|--------|
| **ECHO OF STILLNESS** | Stop panels appear periodically (telegraphed) |
| **ECHO OF NULL** | Dispel pulse every X seconds (reduced in ward fields) |
| **ECHO OF WEIGHT** | Gravity wells spawn (telegraphed pull zones) |
| **ECHO OF VEIL** | Veil patches reduce accuracy / apply confound-lite |
| **ECHO OF HEAT** | Vent grates pulse (Overheat buildup) |
| **ECHO OF FRACTURE** | Flicker tiles cause turn delay if ended on |

#### Modifier Rules
- Never stack unreadable chaos
- Same "family" modifiers don't appear together (e.g., no Stillness + Time Debt + Flicker)

### B) Echo Pressure Meter

| Meter | Effect |
|-------|--------|
| 0–2 | Normal state |
| 3 | Enemies gain minor speed |
| 6 | **ECHO SURGE**: Telegraphed elite wave |

- Meter increases when players eat big telegraphs
- Can be reduced via Stabilizers

### C) Stabilizer Stations

| Property | Value |
|----------|-------|
| Interact time | 1.0s |
| Cooldown | 30s (per station) |
| Effect | Reduces Echo Pressure by -2 |
| | Creates Stabilization Field (10s): hazard intensity -70% |
| | Applies SYNCED to enemies (+damage taken, 8s) |
| Limit | Only one Stabilization Field active per room |

---

## 5. Map Sheets

### 5.1 Remnant Gatehouse (Hub)

| Property | Value |
|----------|-------|
| **Size** | 96 × 72 tiles |
| **Encounters** | OFF |
| **Purpose** | Selection hub + vendor + crafting + tier start |

#### Anchors & Coordinates (local 0–95, 0–71)

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Arrival spawn | (48, 66) | From Aetherreach |
| **Tier Console** | (48, 60) | "Select Vault Tier (1–10)" |
| **Modifier Display Obelisk** | (48, 56) | Shows active Echo Rules |
| **Remnant Broker** (Vendor) | (36, 60) | Currency exchange + keys |
| **Forge Terminal** | (60, 60) | Crafting station |
| **Save Crystal** | (68, 66) | Hub save point |
| **Warp Sigil** (to Aetherreach) | (28, 66) | Return to town |
| **Wing A Door** | (20, 30) | Cinder-Scar Gallery |
| **Wing B Door** | (48, 18) | Edited Archive Annex |
| **Wing C Door** | (76, 30) | Veilroot Catacombs |
| **Core Vault Seal Door** | (48, 30) | Locked until Vault Sigil acquired |

---

### 5.2 Wing A — Cinder-Scar Gallery (Heat/Motion)

| Property | Value |
|----------|-------|
| **Size** | 96 × 64 tiles |
| **Theme** | Heat/Motion flavor |
| **Core Mechanic** | Vent lanes + moving conveyors |
| **Objective** | Destroy 3 Heat Nodes |

#### Key Props

| Prop | Count | Notes |
|------|-------|-------|
| Heat Nodes | 3 | Miniboss-guarded |
| Stabilizer Stations | 2 | Echo Pressure relief |
| Optional chest | 1 | Behind timing gate |

---

### 5.3 Wing B — Edited Archive Annex (Time/Light)

| Property | Value |
|----------|-------|
| **Size** | 96 × 64 tiles |
| **Theme** | Time/Light flavor |
| **Core Mechanic** | Flicker slabs + record locks |
| **Objective** | Collect 3 Record Fragments + "commit" at terminal |

#### Key Props

| Prop | Count | Notes |
|------|-------|-------|
| Record Lock Terminal | 1 | Door gate / fragment commit |
| Stabilizers | 2 | Echo Pressure relief |
| Truth Beacon | 1 | Reveals false corridor exit |
| Optional chest | 1 | Behind puzzle gate |

---

### 5.4 Wing C — Veilroot Catacombs (Shadow/Growth)

| Property | Value |
|----------|-------|
| **Size** | 96 × 64 tiles |
| **Theme** | Shadow/Growth flavor |
| **Core Mechanic** | Veil patches + echo adds + bud nodes |
| **Objective** | Cleanse 2 Null Shrines + defeat wing Warden |

#### Key Props

| Prop | Count | Notes |
|------|-------|-------|
| Null Shrines | 2 | Interactive cleanse event |
| Stabilizers | 2 | Echo Pressure relief |
| Bud Nodes | Variable | Empower elites if ignored |

---

### 5.5 Core Vault (Boss Arena)

| Property | Value |
|----------|-------|
| **Size** | 64 × 64 tiles |
| **Encounters** | Boss only |
| **Purpose** | End-of-run boss + reward sanctum exit |

#### Anchors (local 0–63, 0–63)

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Entry spawn | (32, 56) | From hub |
| **Boss spawn** | (32, 26) | The Remnant Custodian |
| Cover Pylon 1 | (20, 24) | 2×2 collision |
| Cover Pylon 2 | (44, 24) | 2×2 collision |
| Stabilizer A | (16, 44) | Single-use in boss room |
| Stabilizer B | (48, 44) | Single-use in boss room |
| **Reward cache** | (32, 10) | Post-boss loot |
| Exit portal | (32, 6) | Return to Aetherreach |

---

## 6. Enemy Families + Encounter Pacing

### Enemy Types

| Enemy | Role | Behavior |
|-------|------|----------|
| **Rift Skirmishers** | Fast melee | Low HP, high mobility |
| **Null Casters** | Dispel/support | Marks targets, strips buffs |
| **Grav Sentinels** | Tank/control | Pulls, applies Heavy |
| **Chrono Scribers** | Time debuff | Delay, stop-lite effects |
| **Echo Buds** | Support nodes | Empower elites if alive |

### Pacing Rules

| Pattern | Target |
|---------|--------|
| Wing flow | Room → Room → Mini-Event → Warden → Return |
| Combat pockets | 6–8 total per wing (not 20) |
| Stabilizer placement | Always visible before high-pressure rooms |

---

## 7. Wing Completion & Return Flow

### On Wing Objective Complete:

1. **Drop**: `VAULT SIGIL` (Key Item)
2. **Spawn**: Return Portal at wing entrance
3. **UI Toast**: 
   - "VAULT SIGIL ACQUIRED."
   - "CORE VAULT SEAL WEAKENED."
4. **Return to hub**: Core Vault door unlocks

---

## 8. Core Vault Boss: The Remnant Custodian

### Identity
A stitched guardian made of leftover "programs." Rotates mini-phases based on run's active modifiers.

### Boss Behavior
- Always telegraphs (no cheap hits)
- Uses 2 signature moves:

| Move | Description |
|------|-------------|
| **Fault Lanes** | Lane strikes |
| **Echo Pulse** | Ring pulse / dispel-lite / slow-lite (scales with modifier) |

### Counterplay
- Boss room stabilizers are limited-use "burst windows"
- Low Echo Pressure = boss starts with reduced aggression (reward for clean play)

---

## 9. Rewards & Progression

### A) Guaranteed Per-Run Rewards (Deterministic)

| Reward | Description |
|--------|-------------|
| **Remnant Shards** | Main currency (scales by tier) |
| **Core Dust** | Craft material for Origin upgrades (fixed minimum per tier) |
| **1 "Vault Roll"** | Gear roll (quality scales by tier) |
| **1 "Echo Sigil Fragment"** | Combine 5 into Echo Sigil |

#### Anti-RNG Rule
> Even with awful luck, X runs = guaranteed upgrade.
> 
> Example: Tier 5+ grants enough Core Dust that 3–4 clears = one meaningful craft.

### B) Optional Treasure (Controlled RNG)

| Location | Count | Type |
|----------|-------|------|
| Each wing | 1 guaranteed | Small chest |
| Each wing | 1 optional | Behind puzzle/timing gate |
| Core Vault | 1 big cache | Always present |

### C) Unique Chase Items

| Item Type | Drop Source |
|-----------|-------------|
| **Seam-Reinforced Accessories** | Vault cache (anti-dispel, phase resist, stop resist) |
| **Protocol Tokens** | Tier 5+ (unlock higher-tier Eclipse Protocols) |
| **Cosmetics/Titles** | Tier 10+ clears |

---

## 10. Remnant Broker (Hub Vendor)

### Always Available

| Item | Type |
|------|------|
| Remnant Keys | Entry keys (for secondary access) |
| High-end consumables | Combat supplies |
| Shard conversion | Shards → Core Dust (capped per day) |

### Tier-Gated

| Tier | Unlock |
|------|--------|
| 3+ | Origin-tier upgrade recipes |
| 5+ | Protocol unlock components |
| 8+ | Cosmetic tokens |

### Vendor One-Liners

> *"You want profit? Keep your pressure meter low."*

> *"The Vault doesn't cheat. It just remembers."*

---

## 11. UI Text (Exact Prompts)

### Hub Tier Console
```
┌─────────────────────────┐
│      REMNANT VAULT      │
├─────────────────────────┤
│ Select Vault Tier and   │
│ begin a run.            │
│                         │
│    [BEGIN]  [CANCEL]    │
└─────────────────────────┘
```

### Modifier Obelisk
```
┌─────────────────────────┐
│       ECHO RULES        │
├─────────────────────────┤
│ Active modifiers:       │
│ • {Modifier 1}          │
│ • {Modifier 2}          │
│ • {Modifier 3} (Tier 5+)│
│                         │
│      [CONFIRM]          │
└─────────────────────────┘
```

### Wing Door Prompt
```
ENTER WING: {Wing Name}

Objective: {Objective}

[ENTER]    [BACK]
```

### Core Vault Door
```
CORE VAULT SEALED

Requires: VAULT SIGIL

[UNLOCK] (if player has sigil)
```

### End Cache
```
┌─────────────────────────┐
│     REMNANT CACHE       │
├─────────────────────────┤
│ Claim:                  │
│ • Remnant Shards        │
│ • Core Dust             │
│ • Vault Roll            │
│                         │
│       [CLAIM]           │
└─────────────────────────┘
```

---

## 12. Flags

### Core Flags

| Flag | Trigger |
|------|---------|
| `REMNANT_VAULT_UNLOCKED` | First access to dungeon |
| `REMNANT_VAULT_TIER_SELECTED` | Player chooses tier |
| `REMNANT_WING_A_CLEARED` | Wing A objective complete |
| `REMNANT_WING_B_CLEARED` | Wing B objective complete |
| `REMNANT_WING_C_CLEARED` | Wing C objective complete |
| `REMNANT_VAULT_SIGIL_ACQUIRED` | Pick up Vault Sigil |
| `REMNANT_CORE_VAULT_OPEN` | Unlock Core Vault door |
| `REMNANT_CORE_BOSS_DEFEATED` | Defeat Remnant Custodian |
| `REMNANT_VAULT_RUN_COMPLETE` | Exit via reward cache |

### Optional QoL Flags

| Flag | Purpose |
|------|---------|
| `REMNANT_VAULT_DAILY_BONUS_CLAIMED` | Daily first-clear bonus tracking |

---

## 13. Quick Reference

### Gatehouse Hub Coordinates (96×72)
```
Arrival: (48, 66)          Save: (68, 66)
Warp: (28, 66)             Tier Console: (48, 60)
Vendor: (36, 60)           Forge: (60, 60)
Modifier Obelisk: (48, 56)

Wing Doors:
  A: (20, 30)    B: (48, 18)    C: (76, 30)
Core Vault: (48, 30)
```

### Core Vault Coordinates (64×64)
```
Entry: (32, 56)            Boss: (32, 26)
Cover: (20, 24) (44, 24)
Stabilizers: (16, 44) (48, 44) [single-use]
Reward: (32, 10)           Exit: (32, 6)
```

### Wing Summary

| Wing | Theme | Objective | Key Mechanic |
|------|-------|-----------|--------------|
| **A: Cinder-Scar Gallery** | Heat/Motion | Destroy 3 Heat Nodes | Vent lanes + conveyors |
| **B: Edited Archive Annex** | Time/Light | Collect 3 Record Fragments | Flicker slabs + record locks |
| **C: Veilroot Catacombs** | Shadow/Growth | Cleanse 2 Null Shrines | Veil patches + bud nodes |

### Echo Pressure Meter
```
0–2: Normal
3: Enemy speed boost
6: ECHO SURGE (elite wave)
```

---

## 14. Implementation Notes

- **Modifier selection**: Random roll, prevent conflicting families
- **Stabilizer balance**: 30s cooldown prevents spam; single field per room
- **Pressure gain**: Tied to hit-by-telegraph events, not time
- **Boss scaling**: Fault Lanes + Echo Pulse effects change based on active modifiers
- **Anti-friction**: Guaranteed currency prevents "wasted run" feeling
- **Tier progression**: Higher tiers = more modifiers + higher enemy levels + better gear rolls
- **Wing choice**: Can be random assignment OR player choice (configure per design preference)
