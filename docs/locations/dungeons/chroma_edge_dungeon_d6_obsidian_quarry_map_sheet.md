# Chroma's Edge — Obsidian Quarry / Molten Core (D6) Dungeon Map Sheet (v1)
## Mass Foundation Dungeon — "Weight, Gravity, Inevitability"

---

## 0) Dungeon Technical Specs

| Parameter | Value |
|-----------|-------|
| **Dungeon Type** | Main Story Dungeon 6 |
| **Foundation Theme** | MASS (weight, gravity, inevitability) |
| **Recommended Level** | Lv 44–62 |
| **Primary Outcome** | Mass Relic acquired + seated → unlocks heavy traversal lanes (gravity scars), opens Dragon's Graveyard access, expands Gravemark/Meridian crafting |
| **Structure** | 4 submaps (surface quarry → industrial descent → core → colossus arena) |
| **Encounters** | ON (except pre-boss antechamber + Pedestal Chamber) |
| **Save Points** | 1 (Quarry Core) + autosave at Pedestal |
| **Key Mechanics** | Mass Gauge + Anchor Plates + Conveyor Routing |
| **Return Loop** | Ore Lift Shortcut unlocks after boss → returns near entrance |

---

## 1) Macro Flow (How it Plays)

**Flow:** Gravemark Pit → Conveyor Maze → Quarry Core (Save) → Molten Core / Colossus Arena (Boss + Pedestal) → Ore Lift Shortcut → Exit

### Macro ASCII

```
[MAP 1 Gravemark Pit]
        |
        v
[MAP 2 Conveyor Maze]
        |
        v
[MAP 3 Quarry Core] (SAVE)
        |
        v
[MAP 4 Molten Core / Colossus Arena]
   Boss + Mass Pedestal
        |
   Ore Lift Shortcut
        v
Back near Map 1 entrance (fast return)
```

---

## CORE MECHANICS (Dungeon-Wide)

### A) Mass Gauge (Environmental Pressure)

Mass builds in "gravity scar" zones and deep tunnels.

| Level | Effect |
|-------|--------|
| **Heavy** | Speed -10%, jump/step animations heavier |
| **Crushing** | Periodic stamina/HP chip + reduced evasion |
| **Pinned** | Strong debuff: no dash, worse accuracy until relief zone reached |

#### Relief Sources

| Source | Effect |
|--------|--------|
| **Anchor Plates** | Safe pads, prevent knockback, halt Mass gain |
| **Counterweight Stations** | Reduce gauge for a corridor |
| **Stabilizer Totems** | Optional side objective that reduces Mass gain globally |

### B) Anchor Plates (Puzzle Pads)

- Stone/metal plates that "lock" gravity locally
- Standing on one prevents knockback and halts Mass gain
- Some doors ("Load Doors") open only when two plates are held simultaneously (party splits / switch toggles)

### C) Conveyor Routing (Industrial Puzzle)

- Conveyor belts and ore carts move items and the player
- Belts push you 1 tile per step
- Switch levers reverse or divert belts
- Used to deliver Counterweight Cores to gates (or to reach new platforms)

### D) Falling Debris (Telegraphed Hazard)

| Property | Description |
|----------|-------------|
| **Trigger** | Unstable zones |
| **Telegraph** | Dust shake + shadow circle |
| **Effect** | Damage + brief stun + Mass gauge spike |

---

## SUBMAP 1 — GRAVEMARK PIT

**Purpose:** Establish "weight" mood + teach Mass Gauge gently + introduce Anchor Plates.

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 128 × 80 tiles |
| **Entry** | From Gravemark Outpost / Sable route |
| **Exit** | Into Conveyor Maze |
| **Encounter Band** | Lv 44–52 (light-medium) |

### B) Visual / Tone

Open quarry bowl: cranes, cables, carved steps, gravity scars that distort debris arcs.

### C) Anchors (Local Coords)

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **ENTRY** (quarry gate) | (64, 6) | Encounters OFF for first ~8 tiles |
| **EXIT to Submap 2** | (118, 70) | Upper-right ramp to industrial tunnel |
| **Anchor Plate tutorial** | (40, 26) | — |
| **Counterweight Station #1** | (78, 30) | Reduces Mass in next lane (tutorial) |
| **Chest** (early) | (20, 18) | Pressure Patch ×1, Coolant Pod ×1, Weapon mat |

### D) One-Time Script Beat (Recommended)

| Property | Value |
|----------|-------|
| **Trigger** | (56, 20) |
| **Event** | A rock lifts an inch… then slams down like "gravity remembered it" |
| **Line** | "This place isn't broken. It's deciding." |

### E) Enemies

| Enemy | Traits |
|-------|--------|
| **Quarry Scarabs** | Armor up |
| **Slate Hounds** | Knockback bites |
| **Dust Wraiths** | Mass debuff |
| **Dominion Excavator Drone** | Rare elite, PHASE pressure flags |

---

## SUBMAP 2 — CONVEYOR MAZE

**Purpose:** The industrial "brain" — belts, ore carts, counterweights, load doors.

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 128 × 112 tiles |
| **Entry** | From Gravemark Pit |
| **Exit** | To Quarry Core (locked by counterweight delivery) |
| **Encounter Band** | Lv 48–58 (medium) |

### B) Layout Concept

A multi-tier factory grid:
- **Upper Catwalks:** Safer, fewer belts
- **Belt Lanes:** Forced movement
- **Ore Chutes:** Drop-down shortcuts
- **2 Load Doors** gating progress

### C) Puzzle — Counterweight Delivery (2 Cores)

**Goal:** Deliver 2 Counterweight Cores to the Core Gate to access Submap 3.

**Rules:**
- Each core is picked up from a bay, then must ride conveyors to the correct socket
- Player must flip belt switches to route cores correctly
- Standing on Anchor Plates stops belt movement locally (lets you time routes)

### D) Anchors

| Feature | Coordinates |
|---------|-------------|
| **ENTRY** | (14, 10) |
| **Core Gate** (locked) | (118, 98) |
| **Core A pickup bay** | (28, 34) |
| **Core B pickup bay** | (44, 76) |
| **Socket A** | (104, 94) |
| **Socket B** | (112, 94) |
| **Lever 1** (diverts belt north/south) | (50, 38) |
| **Lever 2** (reverses mid-belt) | (66, 60) |
| **Lever 3** (activates chute drop route) | (88, 74) |
| **Anchor Plate #1** | (38, 50) |
| **Anchor Plate #2** | (78, 44) |
| **Anchor Plate #3** | (96, 66) |

### E) Optional Side Room — "Magnet Crane Bay"

| Property | Value |
|----------|-------|
| **Door** | (8, 64) — requires small key from chest |
| **Mini-elite** | Magnet Warden |
| **Loot** | "Anchor Charm" (reduces knockback + slows Mass gain) |

---

## SUBMAP 3 — QUARRY CORE (SAVE)

**Purpose:** Calm-before-hell hub + save + global stabilizer objective.

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 112 × 80 tiles |
| **Encounters** | ON at edges; central platform is safe-ish |
| **Entry** | From Conveyor Maze |
| **Exit** | To Molten Core descent |
| **Save Point** | Yes |

### B) Visual / Tone

A massive circular chamber where the quarry's "logic" lives: counterweights, ancient stone rings, gravity scars like veins.

### C) Anchors

| Feature | Coordinates |
|---------|-------------|
| **ENTRY** | (56, 6) |
| **SAVE CRYSTAL** | (56, 40) |
| **Exit to Submap 4** (sealed by stabilizer or brute-force) | (56, 74) |

### D) Optional Global QoL Objective — Stabilizer Totems (2)

Activating both reduces Mass Gauge gain in Submap 4.

| Totem | Coordinates |
|-------|-------------|
| **Totem #1** | (20, 52) |
| **Totem #2** | (92, 52) |

### E) Loot

| Chest | Coordinates | Loot |
|-------|-------------|------|
| **Side chest** | (14, 20) | "Loadbelt Greaves" (belt push distance -1, Mass gain -10%) |

---

## SUBMAP 4 — MOLTEN CORE / COLOSSUS ARENA (FINAL)

**Purpose:** Molten descent + gravity hazards + colossus boss + Mass pedestal + shortcut.

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 96 × 112 tiles |
| **Encounter Band** | Lv 56–64 (elite chance) |
| **Pre-boss antechamber** | No encounters + big relief pad |

### B) Corridor Hazards

| Hazard | Description |
|--------|-------------|
| **Lava Flow Tiles** | Periodic surge; step during surge = damage + burn buildup |
| **Gravity Wells** | Pull 1 tile toward center every few seconds (telegraphed by swirling debris) |
| **Falling Debris** | Telegraphed circles in unstable lanes |
| **Anchor Plates** | Placed to create "safe islands" during pulls |

### C) Anchors

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **ENTRY** | (48, 6) | — |
| **Antechamber Relief Pad** | (48, 46) | Mass reset + no hazards |
| **Chest A** | (18, 24) | Weapon mat + Mass Patch ×1 |
| **Chest B** | (78, 24) | "Graveseal Mantle" (Mass gain -20%, burn resist) |
| **Boss Door** | (48, 64) | — |
| **Boss Arena Center** | (48, 90) | Colossus fight |
| **Pedestal Chamber Door** (post-boss) | (48, 106) | — |
| **Ore Lift Shortcut** (post-seat) | (86, 86) | Returns to Submap 1 near entry |

---

## 2) Miniboss (Optional) — "Orebound Enforcer"

| Property | Value |
|----------|-------|
| **Placement** | Submap 4 corridor before antechamber |
| **Concept** | Armored construct that uses knockback + gravity pulls |
| **Reward** | "Countermass Pin" (prevents first knockback each battle) |

---

## 3) Final Boss — "Obsidian Colossus"

### Arena

Circular platform above molten basin, 4 anchor pylons on rim, gravity wells cycle.

### Phase Mechanics

| Phase | HP Threshold | Mechanics |
|-------|--------------|-----------|
| **Phase 1** | 100–65% | Heavy slam cones + throws rocks (telegraphed) |
| **Phase 2** | 65–30% | **Gravity Inversion Pulse** — arena wells pull toward edges, then snap back to center. Players must stand on Anchor Pylons to resist pulls |
| **Phase 3** | 30–0% | **Molten Heart Exposure** — core opens; damage window appears, but lava surges more often |

### Arena Interactables

| Pylon | Coordinates |
|-------|-------------|
| **Anchor Pylon A** | (22, 86) |
| **Anchor Pylon B** | (74, 86) |
| **Anchor Pylon C** | (22, 96) |
| **Anchor Pylon D** | (74, 96) |

### Boss Reward

**RELIC ACQUIRED: MASS FRAGMENT**  
*(alt names: Gravity Core / Weight of Ages Shard)*

---

## 4) Pedestal Chamber — Mass Seat

- **No encounters**
- Quiet stone, heavy air, the sense that even sound falls faster

### Anchors

| Feature | Coordinates |
|---------|-------------|
| **Pedestal** | (48, 108) |
| **Interact prompt** | "Seat relic?" |

### Suggested System Outputs

| Output | Effect |
|--------|--------|
| **RELIC SEATED — MASS** | Canon flag |
| **WORLD EFFECT** | Gravity scars stabilize (new overworld lanes open in Sable Expanse) |
| **UNLOCK: ANCHOR STEP** (Field Tech) | Prevents forced movement once per encounter; improves "push block" interactions |
| **NEW ACCESS** | Dragon's Graveyard becomes reachable (hidden area gating) |

---

## 5) Shortcut / Return Loop (QoL)

**After seating:**
- **Ore Lift activates** at (86, 86)
- **Drop point:** Submap 1 at (92, 18) (near quarry gate) → fast return to Gravemark Outpost

---

## 6) Completion Flags

| Flag | Value |
|------|-------|
| **D6_CLEARED** | TRUE |
| **RELIC_MASS_ACQUIRED** | TRUE |
| **RELIC_MASS_SEATED** | TRUE |
| **GRAVITY_LANES_UNLOCKED** | TRUE |

---

## Quick Reference: Dungeon Overview

```
GRAVEMARK OUTPOST (Town)
       |
       v
[SUBMAP 1: GRAVEMARK PIT]
   Size: 128×80 | Lv 44–52 | Tutorial: Mass Gauge, Anchor Plates
   Entry: (64, 6) | Exit: (118, 70)
   Script beat: (56, 20) — "This place isn't broken. It's deciding."
   Chest: (20, 18) — Pressure Patch, Coolant Pod
       |
       v
[SUBMAP 2: CONVEYOR MAZE]
   Size: 128×112 | Lv 48–58
   Puzzle: 2 Counterweight Cores → Core Gate (118, 98)
   Cores: A (28, 34), B (44, 76) → Sockets A (104, 94), B (112, 94)
   Side room: (8, 64) — Magnet Crane Bay → Anchor Charm
       |
       v
[SUBMAP 3: QUARRY CORE]
   Size: 112×80 | Lv — | Save: (56, 40)
   Exit: (56, 74) | Stabilizer Totems: (20, 52), (92, 52)
   Loot: Loadbelt Greaves (14, 20)
       |
       v
[SUBMAP 4: MOLTEN CORE / COLOSSUS ARENA]
   Size: 96×112 | Lv 56–64
   Relief pad: (48, 46) | Boss arena: (48, 90)
   Boss: OBSIDIAN COLOSSUS (3 phases)
   Pedestal: (48, 108) | Shortcut: (86, 86)
   
   ANCHOR STEP UNLOCKED
   GRAVITY LANES UNLOCKED
       |
       v
   (Ore Lift returns to Submap 1 near entrance)
       |
       v
GRAVEMARK OUTPOST (Town Return)
```

**Key Anchors Summary:**

| Feature | Coordinates |
|---------|-------------|
| **Submap 1 Entry** | (64, 6) |
| **Submap 1 Exit** | (118, 70) |
| **Submap 1 Chest** | (20, 18) |
| **Submap 2 Entry** | (14, 10) |
| **Submap 2 Exit** | (118, 98) |
| **Submap 3 Entry** | (56, 6) |
| **Submap 3 Save** | (56, 40) |
| **Submap 3 Exit** | (56, 74) |
| **Submap 4 Entry** | (48, 6) |
| **Antechamber Relief** | (48, 46) |
| **Boss Arena** | (48, 90) |
| **Pedestal** | (48, 108) |
| **Ore Lift Shortcut** | (86, 86) |
