# Chroma's Edge — Abyssal Trench (D5) Dungeon Map Sheet (v1)
## Tide Foundation Dungeon — "Flow, Memory, Cleansing vs Erasure"

---

## 0) Dungeon Technical Specs

| Parameter | Value |
|-----------|-------|
| **Dungeon Type** | Main Story Dungeon 5 |
| **Foundation Theme** | TIDE (flow, memory, cleansing vs erasure) |
| **Recommended Level** | Lv 30–46 |
| **Primary Outcome** | Tide Relic acquired + seated → unlocks aquatic traversal (overworld sea nodes + Sunken City access), expands Brinegate/Halcyon services, deepens Suresh's Leviathan arc |
| **Structure** | 4 submaps (pressure pacing + minimap clarity) |
| **Encounters** | ON (except in Airlock + Pedestal Chamber) |
| **Save Points** | 1 (Pressure Midpoint) + autosave at Pedestal |
| **Key Mechanics** | Pressure Gauge + Current Lanes + Air Pockets |
| **Return Loop** | Pressure Lift Shortcut unlocks after boss → returns to Entry Pier |

---

## 1) Macro Flow (How it Plays)

**Flow:** Silt Tunnels → Pressure Midpoint (Save) → Coral Throne (Puzzle Hub) → Abyss Pearl Pedestal (Boss + Seat) → Pressure Lift Shortcut → Exit

### Macro ASCII

```
[MAP 1 Silt Tunnels]
        |
        v
[MAP 2 Pressure Midpoint] (SAVE + AIRLOCK)
        |
        v
[MAP 3 Coral Throne] --(current routing)-> (locks clear)
        |
        v
[MAP 4 Abyss Pearl Pedestal]
   Boss Arena + Tide Pedestal
        |
   Pressure Lift Shortcut
        v
Back to Entry Pier / Brinegate access
```

---

## CORE MECHANICS (Dungeon-Wide)

### A) Pressure Gauge (Soft Timer / Environmental Stress)

In deep zones, pressure slowly rises. Threshold effects:

| Level | Effect |
|-------|--------|
| **Pressurized** | MP regen down |
| **Crush** | Periodic chip damage + reduced healing received |
| **Critical** | **"Pressure Shock"** (big DoT, accuracy down) |

Pressure resets in **Airlock Rooms** and can be reduced with **Equalizer Stations**.

### B) Current Lanes (Forced Movement / Routing)

- Waterflow tiles push the party 1 tile per step in flow direction
- Some lanes are "fast current" (2 tiles) and can shove into hazards unless rerouted

### C) Air Pockets (Safe Nodes)

- Small bubble caverns that reset pressure partially
- Act as "micro-breath" spots
- Often placed near puzzle reset pedestals

### D) Salinity Locks (Water Gates)

- Doors open only when local salinity matches the lock
- Set by **Brine Valves**

---

## SUBMAP 1 — SILT TUNNELS

**Purpose:** Entry + teach currents safely + establish the "underwater lungs" tone.

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 112 × 72 tiles |
| **Entry** | From Abyss Entry Pier (Brinegate Port route) |
| **Exit** | To Pressure Midpoint |
| **Encounter Band** | Lv 30–36 (light-medium) |

### B) Visual / Tone
- Dim stone tunnels, drifting silt
- Bioluminescent algae lines
- Distant whale-like groans that feel mechanical

### C) Anchors (Local Coords)

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **ENTRY** (Airlock Door) | (56, 6) | No encounters for first 8 tiles |
| **EXIT** to Submap 2 | (56, 70) | Leads to Pressure Midpoint |
| **Current tutorial lane** | x 40–72, y 24 | Gentle 1-tile push |
| **Equalizer Station #1** (tutorial) | (44, 30) | Reduces Pressure Gauge |
| **Air Pocket #1** | (18, 44) | Safe node, flavor |
| **Chest** (early) | (92, 18) | Pressure Patch ×2 + Potion ×1 |

### D) Enemy Table

| Enemy | Traits |
|-------|--------|
| **Silt Skitters** | Fast, low HP |
| **Brine Leeches** | Minor poison |
| **Glowjellies** | Silence chance |
| **Dominion Sonar Drone (Damaged)** | Rare, PHASE pressure flags |

---

## SUBMAP 2 — PRESSURE MIDPOINT (SAVE / AIRLOCK HUB)

**Purpose:** Safe hub + save + introduces salinity locks + sets up side shrine access.

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 128 × 96 tiles |
| **Encounters** | OFF in central airlock ring; ON in side tunnels |
| **Entry** | From Silt Tunnels |
| **Exit** | To Coral Throne (locked by Salinity Locks) |
| **Save Point** | Yes (central) |

### B) Layout Concept

A circular pressure station with 3 spokes:
- **North spoke:** Shrine access (optional)
- **West spoke:** Valve room A
- **East spoke:** Valve room B
- **South:** Main route forward

### C) Mechanics Introduced — Salinity Locks (2)

Two locks must be tuned by Brine Valves (A & B) before the south gate opens.

### D) Anchors

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **ENTRY** | (64, 6) | From Silt Tunnels |
| **SAVE CRYSTAL / Rest Node** | (64, 44) | Central safe zone |
| **South Gate** to Submap 3 (locked) | (64, 90) | Opens after valves tuned |
| **Brine Valve A** (west spoke) | (26, 54) | — |
| **Brine Valve B** (east spoke) | (102, 54) | — |
| **Salinity Lock A** (left of south gate) | (54, 82) | — |
| **Salinity Lock B** (right of south gate) | (74, 82) | — |
| **Air Pocket #2** (hub bubble) | (64, 60) | — |

### E) Optional Side Location — MARINUS'S SANCTUM (Shrine)

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Shrine Door** | (64, 18) | North spoke |
| **Access** | Now OR after Tide relic for extra dialogue | Recommended now |

---

## SUBMAP 3 — CORAL THRONE (PUZZLE HUB)

**Purpose:** The "brain" of D5—current routing puzzle + pressure management + miniboss gate.

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 128 × 128 tiles |
| **Entry** | From Pressure Midpoint |
| **Exit** | To Abyss Pearl Reliquary corridor (locked until routing complete) |
| **Encounter Band** | Lv 34–44 (heavier) |

### B) Layout Concept

A coral-palace ruin wrapped around a huge whirlpool pit:
- **Outer Walkways:** Safer, longer
- **Inner Current Rings:** Faster, forced-movement lanes
- **Whirlpool Rim:** Hazard tiles that spike pressure faster

### C) Puzzle — CURRENT ROUTING TRIAD (3 Sluice Gates)

**Goal:** Redirect three current rings so the Throne Gate receives "stable flow."

**Rules:**
- Each gate rotates flow direction in a ring segment
- When correct, a Flow Sigil lights up at the throne
- Mistakes don't hard-fail—just get shoved into longer loops (JRPG-friendly)

#### Key Interactables

| Gate | Location |
|------|----------|
| **Sluice Gate #1** | (34, 50) |
| **Sluice Gate #2** | (94, 52) |
| **Sluice Gate #3** | (64, 88) | Hot zone: pressure rises faster here |

#### Flow Sigils (Visual Progress)

| Sigil | Location |
|-------|----------|
| **Sigil A** | (54, 66) |
| **Sigil B** | (64, 66) |
| **Sigil C** | (74, 66) |

#### Throne Gate

| Feature | Location | Notes |
|---------|----------|-------|
| **Throne Gate** (locked until 3 sigils) | (64, 110) | Opens after routing complete |

### D) Pressure Relief Side Objective (Optional)

Activate 2 **Vent-Bubble Vents** to reduce pressure gain in Submap 4.

| Vent | Location |
|------|----------|
| **Vent-Bubble #1** | (18, 96) |
| **Vent-Bubble #2** | (110, 96) |

### E) Miniboss Gate

After routing completes, the guardian manifests at the throne gate.

**MINIBOSS — "BRINEWARD SENTINEL"**

| Parameter | Value |
|-----------|-------|
| **Trigger** | (64, 112) |
| **Mechanic** | "Undertow" pulls party toward whirlpool rim; punishes poor positioning |
| **Reward** | **"Pearl Key"** (opens Reliquary door) |

---

## SUBMAP 4 — ABYSS PEARL RELIQUARY (FINAL)

**Purpose:** Tension corridor → boss arena → Tide Pedestal + aquatic unlock + shortcut.

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 96 × 96 tiles |
| **Encounter Band** | Lv 40–48 (elite chance) |
| **Pre-boss antechamber** | No encounters + pressure reset bubble |

### B) Corridor Hazards

| Hazard | Description |
|--------|-------------|
| **Crush Zones** | Tiles where Pressure Gauge climbs faster |
| **Surge Bursts** | Timed current pulses that shove 2 tiles (telegraphed) |
| **Equalizer Pockets** | Stand zones that briefly halt pressure climb |

### C) Anchors

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **ENTRY** | (48, 6) | From Coral Throne |
| **Antechamber Air Pocket** (pressure reset) | (48, 42) | Final reset before boss |
| **Chest A** | (18, 28) | Pressure Patch ×2 + Weapon mat |
| **Chest B** | (78, 28) | "Brineguard Charm" (reduces pressure gain + poison resist) |
| **Reliquary Door** (Pearl Key) | (48, 60) | — |
| **Boss Arena Center** | (48, 78) | Leviathan Remnant |
| **Pedestal Chamber Door** (post-boss) | (48, 90) | Opens after victory |
| **Pressure Lift Shortcut** (post-seat) | (86, 74) | Returns to Submap 1 entry pier |

---

## 2) FINAL BOSS — "LEVIATHAN REMNANT" (Deep Memory)

### Arena
Circular abyss pool with 4 coral pylons + current ring around the edge.

**Identity:** A deep-sea guardian shaped by Tide + trauma—this is where Suresh's "Leviathan" theme lands hard.

### Phase Mechanics

| Phase | HP Threshold | Mechanics |
|-------|--------------|-----------|
| **Phase 1** | 100–60% | **"Undertow Sweep"** currents rotate; pylons can be activated to create safe zones |
| **Phase 2** | 60–25% | **"Pressure Spike"** — boss raises pressure; players must interact with Arena Equalizers (2) to stabilize |
| **Phase 3** | 25–0% | **"Drown the Noise"** — silence/terror wave + add spawns (Glowjellies), while currents speed up |

### Arena Interactables

| Equalizer | Location |
|-----------|----------|
| **Equalizer A** | (26, 72) |
| **Equalizer B** | (70, 72) |

### Boss Reward

**RELIC ACQUIRED: TIDE FRAGMENT** (alt name: "Abyss Pearl Core")

---

## 3) PEDESTAL CHAMBER — Tide Seat

- **No encounters**
- The water here is impossibly still—like the ocean holding its breath

### Anchors

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Pedestal** | (48, 92) | Tide seat location |
| **Interact prompt** | — | "Seat relic?" |

### Suggested System Outputs

| Output | Effect |
|--------|--------|
| **RELIC SEATED — TIDE** | Canon flag |
| **WORLD EFFECT** | Coastal/sea routes stabilize (new overworld nodes appear) |
| **UNLOCK: AQUATIC TRAVEL** | Sunken City + deep shoreline points |
| **NEW FIELD TECH** | "Tide Veil" (reduces silence/fear + improves escape in water zones) |

---

## 4) Shortcut / Return Loop (QoL)

**After seating:**
- **Pressure Lift activates** at (86, 74)
- **Drop point:** Submap 1 near entry airlock (72, 12) → quick return to Brinegate route

---

## 5) Completion Flags

| Flag | Value |
|------|-------|
| **D5_CLEARED** | TRUE |
| **RELIC_TIDE_ACQUIRED** | TRUE |
| **RELIC_TIDE_SEATED** | TRUE |
| **AQUATIC_TRAVEL_UNLOCKED** | TRUE |

---

## Optional Shrine Hook — Marinus's Sanctum

If you want this to be more than flavor:

### Small Shrine Map (32×24)
- Accessed from Submap 2 north door (64, 18)
- **Gives:**
  - Lore about Tide vs Cleanse
  - Optional accessory: **Mariner's Seal** (pressure + silence resist)
  - One-time "calm water" cutscene: buffs boss prep (reduces pressure gain for next 10 battles)

---

## Quick Reference: Dungeon Overview

```
BRINEGATE PORT (Town)
       |
       v
[SUBMAP 1: SILT TUNNELS]
   Size: 112×72 | Lv 30–36 | Tutorial: Current Lanes
   Entry: (56, 6) | Exit: (56, 70)
   Equalizer: (44, 30) | Air Pocket: (18, 44)
       |
       v
[SUBMAP 2: PRESSURE MIDPOINT]
   Size: 128×96 | Lv — | Save: (64, 44)
   Valves: A (26, 54), B (102, 54)
   Locks: A (54, 82), B (74, 82)
   Shrine Access: (64, 18) [Marinus's Sanctum]
       |
       v
[SUBMAP 3: CORAL THRONE]
   Size: 128×128 | Lv 34–44
   Sluice Gates: #1 (34, 50), #2 (94, 52), #3 (64, 88)
   Flow Sigils: A (54, 66), B (64, 66), C (74, 66)
   Miniboss: BRINEWARD SENTINEL at (64, 112)
   Throne Gate: (64, 110)
       |
       v
[SUBMAP 4: ABYSS PEARL RELIQUARY]
   Size: 96×96 | Lv 40–48
   Reliquary Door: (48, 60) | Boss: LEVIATHAN REMNANT at (48, 78)
   Pedestal: (48, 92) | Pressure Lift: (86, 74)
   
   AQUATIC TRAVEL UNLOCKED
       |
       v
   (Shortcut back to Submap 1 entry pier)
       |
       v
BRINEGATE PORT (Town Return)
```
