# Chroma's Edge — Skyspire Temple (D4) Dungeon Map Sheet (v1)
## Heat Foundation Dungeon — "Purpose, Pressure, Transformation"

---

## 0) Dungeon Technical Specs

| Parameter | Value |
|-----------|-------|
| **Dungeon Type** | Main Story Dungeon 4 |
| **Foundation Theme** | HEAT (purpose, pressure, transformation) |
| **Recommended Level** | Lv 20–34 |
| **Primary Outcome** | Heat Relic acquired + seated → unlocks heat-resistant traversal options, expands forge crafts, hard-escalates Dominion presence |
| **Structure** | 4 submaps (big vertical vibe without making the player hate stairs) |
| **Encounters** | ON (except in Antechamber + Pedestal Chamber) |
| **Save Points** | 1 (Spire Nave) + autosave at Pedestal |
| **Key Mechanics** | Heat Gauge + Vent Valves + Furnace Choir Switches |
| **Return Loop** | Spire Lift Shortcut unlocks after boss → returns near entrance |

---

## 1) Macro Flow (How it Plays)

**Flow:** Ember Stair → Spire Nave (Save) → Furnace Choir (Puzzle Hub) → Heat Prime Chamber (Boss + Pedestal) → Spire Lift Shortcut → Exit

### Macro ASCII

```
[MAP 1 Ember Stair]
      |
      v
[MAP 2 Spire Nave] (SAVE)
      |
      v
[MAP 3 Furnace Choir] --(heat routing puzzles)-> (locks clear)
      |
      v
[MAP 4 Heat Prime Chamber]
   Boss Arena + Heat Pedestal
      |
   Spire Lift Shortcut
      v
Back to Map 1 near entrance (fast return)
```

---

## CORE MECHANICS (Dungeon-Wide)

### A) HEAT GAUGE (Soft Pressure)

Heat slowly increases in "hot zones." At thresholds you get debuffs:

| Level | Effect |
|-------|--------|
| **Warm** | Minor MP regen down |
| **Hot** | Accuracy down / periodic chip damage |
| **Critical** | **"Overheat"** (strong DoT + reduced healing) |

Heat resets partially in **Cooling Alcoves** or via **Coolant Pods** (consumable drop).

### B) VENT VALVES (Heat Flow Control)

- Rotatable valves redirect steam/fire flow
- Used to:
  - Lower heat in corridors
  - Open Thermal Locks
  - Create safe windows to cross Lava Grates

### C) FURNACE CHOIR SWITCHES (Rhythm Locks)

- Temple "sings" in pulses; switches must be hit in order matching the pulse pattern
- Puzzle rule: the room hum gives the sequence (no UI rhythm minigame required)

---

## SUBMAP 1 — EMBER STAIR

**Purpose:** "Welcome to heat." Introduces Heat Gauge gently + environmental hazards.

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 112 × 72 tiles |
| **Entry** | From Cinderstep (or mountain approach micro-map) |
| **Exit** | To Spire Nave |
| **Encounter Band** | Lv 20–26 (light-medium) |

### B) Visual / Tone
- Basalt stairs, vent grates, soot banners
- Old Progenitor stone bolted with Dominion scaffolds
- Air shimmers; you hear a low furnace "breath"

### C) Anchors (Local Coords)

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **ENTRY** | (56, 6) | From Cinderstep |
| **EXIT** to Submap 2 | (56, 70) | Leads to Spire Nave |
| **Cooling Alcove #1** (tutorial) | (18, 22) | Resets Heat Gauge |
| **First Vent Valve** (tutorial) | (66, 28) | Reduces heat in short lane |
| **Chest** (early) | (92, 16) | Coolant Pod ×2 + Potion ×1 |

### D) One-time Script Beat (Recommended)

| Parameter | Value |
|-----------|-------|
| **Trigger** | (56, 18) |
| **Event** | A "heat hymn" pulse rolls through stone; torches flare in sync |
| **Takeaway** | The temple isn't just hot—it's active |

---

## SUBMAP 2 — SPIRE NAVE (SAVE)

**Purpose:** Big cathedral chamber + save + first real valve routing.

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 128 × 104 tiles |
| **Entry** | From Ember Stair |
| **Exit** | To Furnace Choir (locked by Thermal Locks) |
| **Encounter Band** | Lv 22–30 (medium) |

### B) Layout Concept

A tall nave with:
- **Central aisle** (main route)
- **Left balcony** (loot + cooling)
- **Right machinery aisle** (valves + locks)

### C) Mechanics Introduced

#### Thermal Locks (2)
Stone doors with heat sigils. Open when local heat is set to correct state via valves.

### D) Anchors

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **ENTRY** | (64, 6) | From Ember Stair |
| **SAVE CRYSTAL** | (64, 48) | Midpoint safe zone |
| **Thermal Lock A** (left) | (30, 72) | Opens via valve routing |
| **Thermal Lock B** (right) | (98, 72) | Opens via valve routing |
| **Valve #1** (right aisle) | (88, 56) | — |
| **Valve #2** (left balcony) | (40, 54) | — |
| **Exit** to Submap 3 | (64, 98) | Opens after both locks |

### E) Optional Side Objective: "Quench Totems" (2)

Activating both reduces Heat Gauge gain for rest of dungeon (QoL reward).

| Totem | Location |
|-------|----------|
| **Quench Totem #1** | (20, 84) |
| **Quench Totem #2** | (108, 84) |

### F) Enemy Table

| Enemy | Traits |
|-------|--------|
| **Cinder Wisps** | Burn buildup |
| **Ash Stalkers** | Ambush |
| **Forge Scarabs** | Armor up, weak to water/tide |
| **Dominion Purifier** (rare) | Elite, appears on PHASE pressure flags |

---

## SUBMAP 3 — FURNACE CHOIR (PUZZLE HUB)

**Purpose:** The brain of D4—rhythm locks + heat routing + miniboss gate.

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 128 × 128 tiles |
| **Entry** | From Spire Nave |
| **Exit** | To Heat Prime Chamber corridor (locked until puzzles complete) |
| **Encounter Band** | Lv 26–34 (heavier) |

### B) Layout Concept

A choir platform ring around a central furnace pit:
- **Upper Choir Walk** (switch puzzles)
- **Lower Foundry Ring** (heat hazards + valves)
- **Central Furnace Pit** (no walking—visual dread)

### C) Puzzle: FURNACE HYMN SEQUENCE (3 Switch Clusters)

Must complete 3 clusters to open the Prime Door.

**Rules:**
- Each cluster has 3 switches
- Correct order hinted by room's hum pulses (low → mid → high)
- Completing a cluster stabilizes heat in one wing (reduces overheat pressure)

#### Switch Cluster Anchors

| Cluster | Switch Locations |
|---------|------------------|
| **Cluster 1** (Upper West) | (26, 36), (30, 40), (34, 44) |
| **Cluster 2** (Upper East) | (98, 36), (94, 40), (90, 44) |
| **Cluster 3** (Lower South) | (64, 96), (60, 100), (68, 100) |

#### Valves (Heat Routing)

| Valve | Location | Function |
|-------|----------|----------|
| **Valve A** | (50, 74) | Cool lower ring lane |
| **Valve B** | (78, 74) | Opens safe crossing window |
| **Valve C** | (64, 54) | Links to Prime Door heat state |

### D) Miniboss Gate

After all 3 clusters, a "perfect heat" guardian manifests.

**MINIBOSS: CHOIRWARDEN (Bell-Forged Sentinel)**

| Parameter | Value |
|-----------|-------|
| **Arena trigger** | (64, 112) |
| **Mechanic** | Swaps between "Glow" (high damage) and "Quench" (high defense) on hymn pulses |
| **Reward** | **"Furnace Sigil"** (key item; opens Prime Door) |

### E) Exit

| Feature | Location | Notes |
|---------|----------|-------|
| **Prime Door** (locked until Sigil) | (64, 124) | Leads to Submap 4 |

---

## SUBMAP 4 — HEAT PRIME CHAMBER (FINAL)

**Purpose:** Tension corridor → boss arena → Heat Pedestal + shortcut unlock.

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 96 × 96 tiles |
| **Encounter Band** | Lv 30–36 (elite chance) |
| **Pre-boss antechamber** | No encounters |

### B) Corridor Hazards

| Hazard | Description |
|--------|-------------|
| **Lava Grates** | Periodic flare pulses (telegraphed) |
| **Steam Jets** | Push + burn buildup (valve safe pockets exist) |

### C) Anchors

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **ENTRY** | (48, 6) | From Furnace Choir |
| **Cooling Alcove** (pre-boss) | (48, 42) | Final reset before boss |
| **Chest A** | (18, 28) | Coolant Pod ×2 + Weapon mat |
| **Chest B** | (78, 28) | "Heatguard Mantle" (burn resist + lower heat gain) |
| **Boss Door** | (48, 60) | — |
| **Boss Arena Center** | (48, 78) | Ember Priest |
| **Pedestal Chamber Door** (post-boss) | (48, 90) | Opens after victory |
| **Spire Lift Shortcut** (post-boss) | (86, 74) | Returns to Submap 1 near entrance |

---

## 2) FINAL BOSS — "EMBER PRIEST" (Temple Guardian)

### Arena
Circular platform, 4 vent pillars on rim, molten ring hazard at edges.

**Identity:** Not a "person priest," but a Progenitor guardian shaped by Dominion doctrine—Heat turned into obedience.

### Phase Mechanics

| Phase | HP Threshold | Mechanics |
|-------|--------------|-----------|
| **Phase 1** | 100–60% | "Brand" attacks (burn buildup) + vent pillar activations |
| **Phase 2** | 60–25% | **Hymn Pulse** begins — every X turns the room "sings," changing pillar states:<br>• **Exhale:** Pushes party 1 tile toward edges (danger)<br>• **Inhale:** Pulls toward center (safe for edge flare) |
| **Phase 3** | 25–0% | **"Purpose Made Pain"** — boss tries to force Overheat; players must hit valves mid-fight to reduce room temperature |

### Boss Reward

**RELIC ACQUIRED: HEAT FRAGMENT** (alt name: "Ember Core")

---

## 3) PEDESTAL CHAMBER — Heat Seat

- **No encounters**
- Quiet, basalt smooth, flame is steady not raging

### Anchors

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Pedestal** | (48, 92) | Heat seat location |
| **Interact prompt** | — | "Seat relic?" |

### Suggested System Outputs

| Output | Effect |
|--------|--------|
| **RELIC SEATED — HEAT** | Canon flag |
| **WORLD EFFECT** | Heat-vent crossings become stable (new traversal lanes open near Cinderstep/Lumencrest) |
| **NEW FIELD TECH** | "Heat Buffer" (reduces burn/overheat for X battles) |
| **NEW CRAFTING** | Heatguard gear recipes unlocked (Cinderstep forge + Prismridge tack upgrades) |

---

## 4) Shortcut / Return Loop (QoL)

**After seating:**
- **Spire Lift activates** at (86, 74)
- **Recommended drop point:** Submap 1 at (92, 50) near entrance scaffolds (fast return to Cinderstep)

---

## 5) Completion Flags

| Flag | Value |
|------|-------|
| **D4_CLEARED** | TRUE |
| **RELIC_HEAT_ACQUIRED** | TRUE |
| **RELIC_HEAT_SEATED** | TRUE |

### Unlocks

| Unlock | Details |
|--------|---------|
| **Cinderstep forge** | Upgrade tier |
| **Overworld "heat lanes"** | Vents, scorched passes |
| **Dominion escalation** | Inspectors, permit checks increase in Lumencrest towns |

---

## Quick Reference: Dungeon Overview

```
CINDERSTEP (Town)
       |
       v
[SUBMAP 1: EMBER STAIR]
   Size: 112×72 | Lv 20–26 | Tutorial: Heat Gauge
   Entry: (56, 6) | Exit: (56, 70)
   Cooling Alcove: (18, 22) | First Valve: (66, 28)
       |
       v
[SUBMAP 2: SPIRE NAVE]
   Size: 128×104 | Lv 22–30 | Save: (64, 48)
   Thermal Locks: (30, 72) & (98, 72)
   Valves: (88, 56) & (40, 54)
   Quench Totems: (20, 84) & (108, 84)
       |
       v
[SUBMAP 3: FURNACE CHOIR]
   Size: 128×128 | Lv 26–34
   Switch Clusters: West (26–34, 36–44), East (90–98, 36–44), South (60–68, 96–100)
   Valves: A (50, 74), B (78, 74), C (64, 54)
   Miniboss: CHOIRWARDEN at (64, 112)
   Prime Door: (64, 124)
       |
       v
[SUBMAP 4: HEAT PRIME CHAMBER]
   Size: 96×96 | Lv 30–36
   Boss Door: (48, 60) | Ember Priest at (48, 78)
   Pedestal: (48, 92) | Spire Lift: (86, 74)
       |
       v
   (Shortcut back to Submap 1 near entrance)
       |
       v
CINDERSTEP (Town Return)
```
