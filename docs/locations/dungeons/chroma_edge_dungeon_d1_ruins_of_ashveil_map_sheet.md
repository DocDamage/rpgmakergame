# Chroma's Edge — Ruins of Ashveil (D1) Dungeon Map Sheet (v1)
## Growth Foundation Dungeon — "Life That Heals and Devours"

---

## 0) Dungeon Technical Specs

| Parameter | Value |
|-----------|-------|
| **Dungeon Type** | Main Story Dungeon 1 |
| **Foundation Theme** | GROWTH (life that heals and devours) |
| **Recommended Level** | Lv 2–8 |
| **Primary Outcome** | Growth Relic acquired + seated → unlocks early stabilization beats + new crafting at Ashveil |
| **Structure** | 4 submaps (for pacing + save/load + clean minimap readability) |
| **Tile Size** | 16×16 px |
| **Encounter Rate** | ON (except in Pedestal Chamber) |
| **Save Points** | 1 (Bloom Atrium) + autosave at Pedestal |
| **Return Loop** | Root Lift shortcut unlocked after boss → exits back to Ashveil Trailhead |

---

## 1) Macro Flow (How it Plays)

**Flow:** Vineway Approach → Outer Gate → Bloom Atrium (Save) → Reliquary Seat (Boss + Pedestal) → Root Lift Shortcut → Exit

### Macro ASCII

```
[MAP 1 Vineway Approach]
        |
        v
[MAP 2 Outer Gate] --(optional side room)-> [Cache Room]
        |
        v
[MAP 3 Bloom Atrium] --(loop/key)--> [Atrium Upper Walk]
        |
        v
[MAP 4 Reliquary Seat]
   Boss Arena + Growth Pedestal
        |
   Root Lift Shortcut
        v
Back to Map 1 exit near Trailhead (fast return)
```

---

## SUBMAP 1 — VINEWAY APPROACH

**Purpose:** Onboarding to dungeon hazards + first mini-puzzle + first "growth overrun" tiles

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 96 × 64 tiles |
| **Entry** | From Ashveil Sanctuary → Ruinpath Trailhead |
| **Exit** | Into Outer Ruins Gate |
| **Encounter Band** | Lv 2–5 (light) |

### B) Visual + Mechanics

- Overrun vines creep over stone
- Some tiles are **"soft slow"** terrain

**Mechanic (Tutorial): OVERRUN TILES**
- Walking on them applies **"Bramble Scratch"** (minor DOT) unless player clears vines via interactable or skill
- Foreshadow: Progenitor glyph-stones half covered in moss

### C) Anchors (Local Coordinates)

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **ENTRY** (from town) | (48, 6) | From Ruinpath Trailhead |
| **EXIT** to Submap 2 | (48, 62) | Leads to Outer Gate |
| **Tutorial node** (burn/clear vines) | (34, 26) | First Overrun Tile clearing |
| **First chest** (safe) | (70, 18) | 2× Potion / "Herb Wrap" |

### D) One-time Script Beat (Optional)

| Parameter | Value |
|-----------|-------|
| **Trigger** | (42, 22) |
| **Event** | Party hears "stone breathing" + sees vines pulse toward the ruins |
| **Reward** | Sets tone that Growth is not "nice nature" |

---

## SUBMAP 2 — OUTER RUINS GATE

**Purpose:** First real puzzle gate + introduces **"Seedlamp Circuit"** mechanic

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 112 × 80 tiles |
| **Entry** | From Vineway Approach |
| **Exit** | To Bloom Atrium |
| **Encounter Band** | Lv 3–6 (medium) |

### B) Core Puzzle: SEEDLAMP CIRCUIT (3 Lamps)

**Objective:** Activate 3 Seedlamps to open the Vine Gate to Bloom Atrium.

**Rule:**
- Each lamp is lit by finding a **Bio-Spark node** (interact)
- Carry Bio-Spark to lamp and "charge" it
- **Bio-Spark decays** after ~20 seconds (or X steps), so routes matter
- If it expires, player must fetch another spark

### C) Anchors

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **ENTRY** | (56, 6) | From Vineway Approach |
| **EXIT** to Submap 3 | (56, 74) | Locked by Vine Gate |
| **Vine Gate** | (56, 70) | Opens after 3 lamps |
| **Bio-Spark Node A** | (20, 22) | — |
| **Bio-Spark Node B** | (88, 28) | — |
| **Bio-Spark Node C** | (54, 42) | Guarded |
| **Seedlamp #1** | (28, 54) | — |
| **Seedlamp #2** | (84, 52) | — |
| **Seedlamp #3** | (56, 58) | Closest to gate; intended "last" |

### D) Optional Side Room: CACHE ROOM

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Access** | Cracked wall at (12, 40) | Breakable / interact |
| **Loot chest** | (8, 58) | "Growth Salve" (regen accessory) |
| **Flavor note** | — | "Dominion scouting report" (foreshadows pressure) |

### E) Enemy Table

| Enemy | Traits |
|-------|--------|
| **Bramble Rats** | Fast |
| **Sap Leeches** | Drain MP/TP lightly |
| **Vinebound Skulkers** | Ambush |
| **Dominion Scout** (rare, post-escalation) | 1 unit only |

---

## SUBMAP 3 — BLOOM ATRIUM

**Purpose:** Midpoint hub + save point + loop path + miniboss gate

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 128 × 128 tiles |
| **Entry** | From Outer Ruins Gate |
| **Exit** | To Reliquary Seat corridor |
| **Encounter Band** | Lv 4–8 (heavier) |

### B) Layout Concept

A circular garden ruin with **2 elevation lanes**:
- **Lower Ring** (combat lane)
- **Upper Walk** (puzzle lane / shortcuts)

### C) Mechanics Introduced

#### 1) POLLEN DRIFT ZONES
- Misty tiles that apply **"Drowsy"** buildup (slow / accuracy down)
- Encourages either quick traversal or clearing **Vent Roots**

#### 2) VENT ROOTS (2)
- Interactable growth vents
- When "sealed," reduce pollen zones in the Atrium

### D) Anchors

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **ENTRY** | (64, 10) | From Outer Gate |
| **SAVE CRYSTAL / Rest Node** | (64, 64) | Midpoint safe zone |
| **Vent Root #1** | (38, 46) | — |
| **Vent Root #2** | (90, 82) | — |
| **Upper Walk access** (vine ladder) | (28, 70) | — |
| **Upper Walk exit** (drop-down) | (102, 58) | — |
| **EXIT** to Submap 4 | (64, 118) | Locked by miniboss |

### E) Miniboss Gate

**Living gate** blocks the Reliquary corridor until defeated.

**MINIBOSS: "BLOOM GUARDIAN (Sprout Sentinel)"**

| Parameter | Value |
|-----------|-------|
| **Arena trigger** | (64, 110) |
| **After win** | Corridor vines retract |
| **Loot** | **"Rootkey Sigil"** (quest key item; dungeon clear proof) |

### F) Treasure

| Chest | Location | Contents |
|-------|----------|----------|
| **Upper Walk chest** | (96, 40) | 2× Antidote + 1× Ether Drop |
| **Hidden herb node** | (16, 92) | Craft mat (Growth fiber) |

---

## SUBMAP 4 — RELIQUARY SEAT

**Purpose:** Final corridor → boss arena → Growth Pedestal chamber + shortcut unlock

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 96 × 96 tiles |
| **Entry** | From Bloom Atrium |
| **Exit** | Back shortcut node (unlocks after boss) |
| **Encounter Band** | Lv 6–10 (elite chance) |

### B) Corridor Structure

- **Reliquary Hall:** Straight "tension hallway" with 2 side alcoves
- **Pre-boss antechamber:** No encounters, short breath moment

### C) Anchors

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **ENTRY** | (48, 6) | From Bloom Atrium |
| **Alcove chest A** | (20, 30) | Weapon upgrade mat |
| **Alcove chest B** | (76, 30) | "Moss Charm" (resist bramble/pollen) |
| **Boss door** | (48, 64) | — |
| **Boss arena center** | (48, 78) | — |
| **Pedestal chamber door** | (48, 90) | Opens post-boss |
| **Root Lift Shortcut** | (86, 84) | Connects back to Submap 1 near exit |

---

## 2) FINAL BOSS — "ROOTBOUND WARDEN"

### Arena
Circular stone bowl, vines forming a crown around the rim

**Boss Identity:** Ancient Progenitor guardian corrupted by unmanaged Growth

### Phase Mechanics

| Phase | HP Threshold | Mechanics |
|-------|--------------|-----------|
| **Phase 1** | 100–50% | Summons bramble lines (telegraphed) |
| **Phase 2** | 50–25% | **"Bloom Burst"** pollen AoE + adds (2 sproutlings) |
| **Phase 3** | 25–0% | Tries to **"Overrun"** parts of arena (more slow/DOT tiles) |

### Boss Reward

**RELIC ACQUIRED: GROWTH FRAGMENT** (or "Verdant Seed" for softer naming)

---

## 3) PEDESTAL CHAMBER — Growth Seat

- **No encounters**
- Quiet, clean stone
- Vines pulled back like the room is holding its breath

### Anchors

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Pedestal** | (48, 92) | Growth seat location |
| **Interact prompt** | — | "Seat relic?" |

### Cutscene Beats
- Prime network "accepts" seat
- Subtle world stabilization pulse

### System Outputs

| Output | Effect |
|--------|--------|
| **RELIC SEATED — GROWTH** | Canon flag |
| **WORLD EFFECT** | Minor Overrun reduced on overworld routes near Ashveil |
| **NEW CRAFTING** | Growth Fiber recipes unlocked in Ashveil |

---

## 4) Shortcut / Return Loop (Critical QoL)

**After pedestal cutscene:**
- **Root Lift activates** at (86, 84)
- Drops player into **Submap 1 near Trailhead exit**
- **Drop point:** Submap 1 at (74, 52) — close to dungeon entrance

---

## 5) Dungeon Completion Flags

| Flag | Purpose |
|------|---------|
| **D1_CLEARED** | = TRUE |
| **RELIC_GROWTH_ACQUIRED** | = TRUE |
| **RELIC_GROWTH_SEATED** | = TRUE |

### Unlocks in Ashveil

| Unlock | Details |
|--------|---------|
| **Clinic upgrade** | Tier 1 |
| **Crafting tier** | Tier 1 |
| **New NPC lines** | "The vines are calmer today" |

---

## Quick Reference: Dungeon Overview

```
ASHVEIL SANCTUARY (Town)
       |
       v
[SUBMAP 1: VINEWAY APPROACH]
   Size: 96×64 | Lv 2–5 | Tutorial: Overrun Tiles
   Entry: (48, 6) | Exit: (48, 62)
       |
       v
[SUBMAP 2: OUTER RUINS GATE]
   Size: 112×80 | Lv 3–6 | Puzzle: Seedlamp Circuit (3)
   Entry: (56, 6) | Exit: (56, 74) | Gate: (56, 70)
       |
       v
[SUBMAP 3: BLOOM ATRIUM]
   Size: 128×128 | Lv 4–8 | Save: (64, 64)
   Mechanics: Pollen Zones, Vent Roots (2), Miniboss Gate
   Miniboss: BLOOM GUARDIAN at (64, 110)
       |
       v
[SUBMAP 4: RELIQUARY SEAT]
   Size: 96×96 | Lv 6–10
   Boss: ROOTBOUND WARDEN at (48, 78)
   Pedestal: (48, 92) | Root Lift: (86, 84)
       |
       v
   (Shortcut back to Submap 1 exit)
       |
       v
ASHVEIL TRAILHEAD (Town Return)
```
