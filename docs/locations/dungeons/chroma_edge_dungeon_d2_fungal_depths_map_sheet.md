# Chroma's Edge — Fungal Depths (D2) Dungeon Map Sheet (v1)
## Motion Foundation Dungeon — "Speed, Drift, Inertia"

---

## 0) Dungeon Technical Specs

| Parameter | Value |
|-----------|-------|
| **Dungeon Type** | Main Story Dungeon 2 |
| **Foundation Theme** | MOTION (speed, drift, inertia) expressed through fungal "wind-lungs" |
| **Recommended Level** | Lv 6–14 |
| **Primary Outcome** | Motion Relic acquired + seated → unlocks "flow" mechanics, reduces swamp-route hazards, expands crafting in Mirewatch/Ashveil |
| **Structure** | 4 submaps (clean pacing + minimap clarity) |
| **Encounters** | ON (except in Clinic + Pedestal chamber) |
| **Save Points** | 1 (Hidden Clinic) + autosave at Pedestal |
| **Key Mechanic** | Slipstream Tiles + Vent Valves |
| **Return Loop** | Mycelium Slide shortcut unlocks after boss → pops you back near entrance |

---

## 1) Macro Flow (How it Plays)

**Flow:** Mireglass Approach → Sporeward Hollows → Hidden Clinic (Save) → Flux Node (Boss + Pedestal) → Mycelium Slide Shortcut → Exit

### Macro ASCII

```
[MAP 1 Mireglass Approach]
        |
        v
[MAP 2 Sporeward Hollows] --(valves/puzzle loops)--> [MAP 3 Hidden Clinic (Save)]
        |
        v
[MAP 4 Flux Node]
   Boss Arena + Motion Pedestal
        |
   Mycelium Slide Shortcut
        v
Back near Map 1 entrance (fast return)
```

---

## CORE MECHANICS (Dungeon-Wide)

### A) Slipstream Tiles

| Aspect | Description |
|--------|-------------|
| **Visual** | Pale spores "flowing" along the ground |
| **Behavior** | Stepping onto a Slipstream tile pushes the party 1 tile in the stream direction |
| **Hazard** | If pushed into hazard: take minor damage + "Dizzy" buildup |

### B) Vent Valves (Directional Control)

- **Interactable** "valves" rotate wind/spore pressure in nearby lanes
- **Used to:**
  - Redirect Slipstream flow
  - Open/close Spore Doors
  - Safely cross "gust corridors" without being shoved into bramble pits

### C) Spore Lung Doors

- Organic doors that "breathe"
- Open only when local pressure is correct (set by valves + powered by Bio-Sparks)

---

## SUBMAP 1 — MIREGLASS APPROACH

**Purpose:** Swamp entry, introduces Slipstream gently + sets tone

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 96 × 64 tiles |
| **Entry** | From Mirewatch (or overworld edge) |
| **Exit** | To Sporeward Hollows |
| **Encounter Band** | Lv 6–9 (light) |

### B) Visual / Tone
- Shallow swamp water, reed fences, fog pockets
- Glassy puddles that reflect wrong (Motion = "the world slides")

### C) Anchors (Local Coords)

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **ENTRY** | (48, 6) | From Mirewatch |
| **EXIT** to Submap 2 | (48, 62) | Leads to Sporeward Hollows |
| **Slipstream tutorial lane** | (38, 22 → 58, 22) | One straight push path |
| **First valve** (safe tutorial) | (46, 28) | Rotates a small stream |
| **First chest** (early) | (72, 16) | 2× Potion + "Mire Filter" (quest item) |

### D) One-time Script Beat (Recommended)

| Parameter | Value |
|-----------|-------|
| **Trigger** | (50, 18) |
| **Event** | Party hears a "breathing" sound underground; wind blows without trees moving |
| **Flavor Line** | "This place has lungs." |

---

## SUBMAP 2 — SPOREWARD HOLLOWS

**Purpose:** Main puzzle zone: valves + pressure routing + loopbacks

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 112 × 80 tiles |
| **Entry** | From Mireglass Approach |
| **Exit** | To Hidden Clinic (locked by pressure gate) |
| **Encounter Band** | Lv 7–12 (medium) |

### B) Layout Concept

Three looping corridors around a central sinkhole:
- **Outer Ring:** Safer, longer routes
- **Inner Ring:** Faster, Slipstream-heavy
- **Sinkhole Rim:** Hazard zone with gusts + poison puddles

### C) Puzzle: PRESSURE ROUTE (3 Valves + 2 Bio-Sparks)

**Goal:** Open the Spore Lung Door to the Clinic by stabilizing pressure at a central manifold.

**Rules:**
- Two Bio-Sparks must be carried to power Manifold Nodes (A & B)
- Three Vent Valves set flow direction so the spark carrier isn't shoved into hazards
- This creates a "do the loop in the right order" navigation puzzle (not a timer sprint)

### D) Anchors

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **ENTRY** | (56, 6) | From Approach |
| **Clinic Door** (locked) | (56, 74) | Opens after manifold powered |
| **Central Manifold** (status display) | (56, 40) | — |
| **Valve #1** | (20, 26) | — |
| **Valve #2** | (92, 28) | — |
| **Valve #3** | (56, 54) | Near sinkhole rim; guarded |
| **Bio-Spark Node A** | (14, 58) | — |
| **Bio-Spark Node B** | (98, 60) | — |
| **Manifold Power Slot A** | (46, 42) | — |
| **Manifold Power Slot B** | (66, 42) | — |

### E) Optional Side Loop: "Mold Cache"

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Breakable root wall** | (10, 32) | — |
| **Loot chest** | (8, 44) | "Sporecloak Charm" (resist poison + small evasion) |
| **Lore scrap** | — | Old field note hints "clinic below" |

### F) Enemies

| Enemy | Traits |
|-------|--------|
| **Caplings** | Small fungus sprinters; stack "Dizzy" |
| **Mire Leeches** | Poison |
| **Sporebats** | Silence chance |
| **Windspores** | AoE push |
| **Dominion Scout** (rare) | Appears if story pressure flag active |

---

## SUBMAP 3 — HIDDEN CLINIC (SAFE ZONE)

**Purpose:** Calm pocket + save point + story logs + prep for boss mechanics

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 96 × 64 tiles |
| **Encounters** | OFF |
| **Entry** | From Sporeward Hollows |
| **Exit** | To Flux Node corridor |

### B) Visual / Tone
- Abandoned clinic carved into stone
- Fungus kept at bay by salt lines and fans
- Flickering Progenitor-tech instrumentation (non-Dominion feel)

### C) Anchors

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **ENTRY** | (48, 6) | From Hollows |
| **SAVE CRYSTAL / Rest Node** | (48, 34) | Safe zone anchor |
| **Supply cabinet** (1-time) | (16, 30) | Antidote ×2, Ether Drop ×1 |
| **Clinic log console** | (70, 20) | Lore: "Motion channels mimic respiration" |
| **Exit** to Submap 4 corridor | (48, 62) | — |

### D) Optional NPC Beat

| NPC | Location | Details |
|-----|----------|---------|
| **"Field Medic Survivor"** | (30, 40) | Sitting by a fan unit |
| **Dialogue** | — | "Don't fight the push. Redirect it." |

---

## SUBMAP 4 — FLUX NODE (RELIQUARY)

**Purpose:** Tension corridor → miniboss gate → boss arena → Motion Pedestal + shortcut

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 96 × 96 tiles |
| **Encounter Band** | Lv 10–14 (elite chance) |
| **Pre-boss antechamber** | No encounters |

### B) Corridor Hazards

| Hazard | Description |
|--------|-------------|
| **Gust Corridors** | Tiles that shove you 2 tiles every few seconds (timed cross) |
| **Valve safe pockets** | Stand here to avoid shove pulses |

### C) Anchors

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **ENTRY** | (48, 6) | From Clinic |
| **Alcove chest A** | (18, 26) | Weapon mat + antidote |
| **Alcove chest B** | (78, 26) | "Slipstep Boots" (reduce push distance by 1 tile) |
| **Miniboss gate** | (48, 44) | Draftguard Stalker |
| **Boss door** | (48, 66) | — |
| **Boss arena center** | (48, 80) | Moldwind Matron |
| **Pedestal chamber door** (post-boss) | (48, 90) | Opens after victory |
| **Mycelium Slide Shortcut** (post-boss) | (86, 74) | Returns to Submap 1 near entrance |

---

## 2) MINIBOSS — "DRAFTGUARD STALKER"

| Parameter | Value |
|-----------|-------|
| **Trigger** | (48, 44) |
| **Concept** | Fungus-limbed predator that "rides" Slipstream lanes |
| **Mechanics** | Spawns Slipstream lines during fight; punishes standing still (Motion theme) |
| **Reward** | **"Vent Key"** (opens boss door / proves progression) |

---

## 3) FINAL BOSS — "MOLDWIND MATRON"

### Arena
Circular cavern with 4 "lung vents" around the rim

**Identity:** Fungal queen fused to a vent organ; she "breathes" Motion into spores

### Phase Mechanics

| Phase | HP Threshold | Mechanics |
|-------|--------------|-----------|
| **Phase 1** | 100–60% | **"Exhale"** pushes party positions + spawns Windspores |
| **Phase 2** | 60–25% | Vents begin cycling; players must rotate Arena Valves to prevent being shoved into poison rims |
| **Phase 3** | 25–0% | **"Hypervent"** — rapid push pulses + add waves (2 Capling swarms) |

### Boss Reward

**RELIC ACQUIRED: MOTION FRAGMENT** (alt name: Kinetic Spore Core)

---

## 4) PEDESTAL CHAMBER — Motion Seat

- **No encounters**
- The room feels like a calm breath after panic

### Anchors

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Pedestal** | (48, 92) | Motion seat location |
| **Interact prompt** | — | "Seat relic?" |
| **Cutscene vibe** | — | Air "settles," Slipstream sound becomes rhythmic, not chaotic |

### Suggested System Outputs

| Output | Effect |
|--------|--------|
| **RELIC SEATED — MOTION** | Canon flag |
| **WORLD EFFECT** | Swamp-route gust hazards reduced near Mirewatch |
| **NEW FIELD TECH** | "Slipstep" (short dash / reposition skill) |
| **NEW CRAFTING** | Slipstep Boots upgrade recipes unlocked |

---

## 5) Shortcut / Return Loop (QoL)

**After seating:**
- **Mycelium Slide activates** at (86, 74)
- Drops you back to **Submap 1 near entrance**
- **Recommended drop point:** (78, 50) — close to dungeon entrance

---

## 6) Completion Flags

| Flag | Value |
|------|-------|
| **D2_CLEARED** | TRUE |
| **RELIC_MOTION_ACQUIRED** | TRUE |
| **RELIC_MOTION_SEATED** | TRUE |

### Unlocks

| Location | Unlock |
|----------|--------|
| **Mirewatch** | Vendor upgrades (anti-poison + movement gear) |
| **Ashveil** | Crafting add-on (mobility accessories) |
| **Overworld** | Traversal feels smoother on swamp lanes |

---

## Quick Reference: Dungeon Overview

```
MIREWATCH (Town)
       |
       v
[SUBMAP 1: MIREGLASS APPROACH]
   Size: 96×64 | Lv 6–9 | Tutorial: Slipstream Tiles
   Entry: (48, 6) | Exit: (48, 62)
       |
       v
[SUBMAP 2: SPOREWARD HOLLOWS]
   Size: 112×80 | Lv 7–12 | Puzzle: Pressure Route (3 Valves + 2 Bio-Sparks)
   Entry: (56, 6) | Exit: (56, 74) | Manifold: (56, 40)
       |
       v
[SUBMAP 3: HIDDEN CLINIC (SAFE)]
   Size: 96×64 | Lv — | Save: (48, 34)
   Entry: (48, 6) | Exit: (48, 62)
   Vibe: Progenitor-tech clinic, calm
       |
       v
[SUBMAP 4: FLUX NODE]
   Size: 96×96 | Lv 10–14
   Entry: (48, 6) | Miniboss: (48, 44) | Boss Door: (48, 66)
   Boss: MOLDWIND MATRON at (48, 80)
   Pedestal: (48, 92) | Slide: (86, 74)
       |
       v
   (Shortcut back to Submap 1 near entrance)
       |
       v
MIREWATCH (Town Return)
```
