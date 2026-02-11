# Chroma's Edge — The Void Nexus (D8) Dungeon Map Sheet (v1)
## Shadow Foundation Dungeon — "Absence, Concealment, Reflection, Ownership of the Unknown"

---

## 0) Dungeon Technical Specs

| Parameter | Value |
|-----------|-------|
| **Dungeon Type** | Final Foundation Dungeon |
| **Foundation Theme** | SHADOW (absence, concealment, reflection, ownership of the unknown) |
| **Recommended Level** | Lv 80–99 |
| **Primary Outcome** | Shadow Relic acquired + seated → unlocks Shadowwalk field tech + opens final act gate (Eclipse Routes / reality seams stabilize) |
| **Structure** | 5 submaps (final-dungeon pacing + escalation) |
| **Encounters** | ON (except Stillpoint Hub + Boss Aftermath + Pedestal) |
| **Save Points** | 2 (Stillpoint Hub + antechamber) + autosave before boss + autosave at pedestal |
| **Key Mechanics** | Umbral Gauge + Seen/Unseen Phase + Echo Dupes + Void Rifts |
| **Return Loop** | Nexus Gate Shortcut unlocks after boss → returns to entry breach |

---

## Unlock / Access Hook (Earned Entry)

| Requirement | Description |
|-------------|-------------|
| **Entry Location** | Crown District (inner capital) — beneath Crown Spire foundation chamber |
| **RELIC_TIDE_SEATED** | TRUE |
| **RELIC_MASS_SEATED** | TRUE |
| **RELIC_TIME_SEATED** | TRUE |
| **CROWN_ARCHIVE_KEY_ACQUIRED** | TRUE (authorizes entry through sealed conduit) |
| **Entry Trigger** | "The Spire's shadow doesn't match the sun." |

---

## CORE MECHANICS (Void Nexus-wide)

### A) Umbral Gauge (Shadow Pressure)

Builds in shadow-heavy zones and during certain puzzles.

| Level | Effect |
|-------|--------|
| **Dimmed** | Healing received -10%, accuracy -5% |
| **Hollow** | Periodic chip damage + "buff duration shortened" |
| **Unmoored** | Party becomes partially mirrored (controls invert for 2 seconds on map OR random target drift in combat) |

#### Relief Sources

| Source | Effect |
|--------|--------|
| **Lumen Anchors** | Safe pads |
| **Foundation Pylons** | Stabilize gauge + unlock puzzle states |
| **Stillpoint Rooms** | Full cleanse |

### B) Seen / Unseen Phase (Map-Layer Swap)

At Umbral Altars, toggle:

| Phase | Description |
|-------|-------------|
| **SEEN** | Physical world, rubble, locked doors, normal routes |
| **UNSEEN** | "Shadow copy" world—some walls vanish, new bridges exist, but hazards intensify |

**Rule:** Certain Veil Doors only exist in one phase.

### C) Echo Dupes (Shadow Copies)

In specific "mirror corridors," your party spawns a trailing echo.
- If echo touches you: Umbral Gauge spikes
- Desync echoes by stepping on **Sync Plates** or using phase swaps

### D) Void Rifts (Telegraphed Map Hazard)

Black seams that:
- Pull 1 tile toward the seam every few seconds (gentle)
- Apply **Void Rot** buildup if you stand too long (status that worsens Umbral effects)

---

## 1) Macro Flow (How it Plays)

```
Breach Vestibule → Echo Galleries → Null Records → Stillpoint Hub (SAVE) → Umbra Engine → Nexus Heart (Boss + Pedestal) → Shortcut

[MAP 1 Breach Vestibule]
        |
        v
[MAP 2 Echo Galleries]  (Seen/Unseen + Echo control)
        |
        v
[MAP 3 Null Records]    (edited reality / key collection)
        |
        v
[MAP 4 Stillpoint Hub]  (SAVE + stabilize + final prep)
        |
        v
[MAP 5 Umbra Engine + Nexus Heart]
   Boss + Shadow Pedestal + Shortcut
```

---

## SUBMAP 1 — BREACH VESTIBULE (Entry / Tone Lock)

**Purpose:** Establish "reality seam" tone + teach Seen/Unseen safely.

### Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 128 × 72 tiles |
| **Entry** | Crown Spire breach |
| **Exit** | To Echo Galleries |
| **Encounters** | OFF for first ~12 tiles, then light |

### Anchors (Local 0–127, 0–71)

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **ENTRY** | (64, 6) | — |
| **First Umbral Altar** (tutorial) | (64, 24) | Toggle Seen/Unseen |
| **Lumen Anchor** (safe pad) | (44, 30) | — |
| **Veil Door** (UNSEEN only) | (64, 52) | Forces tutorial |
| **Exit to Map 2** | (64, 70) | — |

### Setpiece Beat

**Hallway inscription flickers between:**
- "AUTHORIZED ENTRY"
- "NO ONE ENTERED"

...like the world can't agree what happened.

---

## SUBMAP 2 — ECHO GALLERIES (Phase + Echo Puzzle Hub)

**Purpose:** The "movement brain" of D8—echo management + phase routes + first key.

### Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 160 × 112 tiles |
| **Encounter Band** | Lv 80–92 (medium) |
| **Entry** | From Vestibule |
| **Exit** | To Null Records (locked by 2 Nexus Seals) |

### Layout Concept

Ring of galleries around central void pit:
- **Outer Walk:** Safe, longer
- **Inner Mirror Lanes:** Echo-heavy, faster
- **Void Bridges:** Only exist in UNSEEN

### Anchors

| Feature | Coordinates |
|---------|-------------|
| **ENTRY** | (80, 6) |
| **Central Umbral Altar** | (80, 56) |
| **Sync Plate A** | (46, 42) |
| **Sync Plate B** | (114, 42) |
| **Lumen Anchor** (mid) | (80, 72) |
| **Exit Gate** (locked) | (80, 106) |

### Nexus Seal #1 (Key Item)

| Property | Value |
|----------|-------|
| **Name** | "ECLIPSE MARK" (Nexus Seal A) |
| **Location** | (24, 88) |
| **Requirement** | UNSEEN bridge route |

### Optional Mini-Elite

| Property | Value |
|----------|-------|
| **Trigger** | (80, 30) — first time only |
| **Name** | "ECHO OF THE PARTY" |
| **Reward** | Umbral Band (reduces Umbral Gauge gain, +void rot resist) |

---

## SUBMAP 3 — NULL RECORDS (Edited Reality)

**Purpose:** "Edited records" theme—now reality itself is being redacted.

### Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 160 × 104 tiles |
| **Encounter Band** | Lv 84–96 (heavier) |
| **Entry** | From Echo Galleries |
| **Exit** | To Stillpoint Hub (locked by final seal) |

### Core Puzzle — RECORD STATES (3)

At Revision Consoles, choose:

| State | Description |
|-------|-------------|
| **TRUTH** (Original) | — |
| **DECREE** (Official) | — |
| **BLANK** (Redacted) | — |

Each state changes which corridors exist and which locks open.

### Anchors

| Feature | Coordinates |
|---------|-------------|
| **ENTRY** | (80, 6) |
| **Revision Console** (central) | (80, 44) |
| **Chrono Dial** (local phase lock) | (96, 44) |
| **Lumen Anchor** | (60, 58) |
| **Exit to Map 4** (locked) | (80, 98) |

### Nexus Seal #2 (Key Item)

| Property | Value |
|----------|-------|
| **Name** | "NULL SIGNET" (Nexus Seal B) |
| **Location** | (132, 28) |
| **Condition** | DECREE + PRESENT ("authorized access") |

### Final Seal (Key Item)

| Property | Value |
|----------|-------|
| **Name** | "SHADOW WITNESS" (Nexus Seal C) |
| **Location** | (24, 72) |
| **Condition** | BLANK + UNSEEN (truth hidden by erasure) |

---

## SUBMAP 4 — STILLPOINT HUB (Save / Prep / Stabilize)

**Purpose:** Calm eye of the storm. Full cleanse. Final prep. Optional stabilizers for Map 5.

### Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 112 × 80 tiles |
| **Encounters** | OFF (entire map) |
| **Save Point** | YES |

### Anchors

| Feature | Coordinates |
|---------|-------------|
| **ENTRY** | (56, 6) |
| **SAVE CRYSTAL** | (56, 40) |
| **Stillpoint Well** (full cleanse) | (56, 26) |
| **Exit to Map 5** | (56, 74) |

### Optional Foundation Pylons (3)

| Pylon | Coordinates | Effect |
|-------|-------------|--------|
| **Tide** | (28, 52) | Weakens rift pull in Map 5 |
| **Mass** | (56, 58) | Adds more safe anchors in Map 5 |
| **Time** | (84, 52) | Slows flicker tiles / lock timers in Map 5 |

---

## SUBMAP 5 — UMBRA ENGINE + NEXUS HEART (Final)

**Purpose:** Final climb corridor + high-pressure hazards + boss arena + Shadow pedestal + shortcut.

### Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 176 × 112 tiles |
| **Encounter Band** | Lv 90–99 (elite chance) |
| **Pre-boss antechamber** | No encounters + full cleanse + optional last merchant |

### Corridor Hazards

| Hazard | Description |
|--------|-------------|
| **Flicker Bridges** | Exist only in SEEN or UNSEEN on a cycle (telegraphed) |
| **Void Rifts** | Gentle pull + Void Rot buildup |
| **Echo Surge Hall** | Spawns fast echo mirroring your last 6 steps (timing puzzle) |

### Anchors

| Feature | Coordinates |
|---------|-------------|
| **ENTRY** | (88, 6) |
| **Antechamber Cleanse Pad** | (88, 48) |
| **Boss Door** | (88, 70) |
| **Boss Arena Center** | (88, 90) |
| **Pedestal Chamber Door** (post-boss) | (88, 108) |
| **Nexus Gate Shortcut** (post-seat) | (168, 86) | Returns to Map 1 near entry (96, 14) |

---

## 3) Final Boss — "The Void Nexus Regent"

### Arena

Circular void platform with 4 Foundation Pillars at rim and rotating "shadow ring" that flips Seen/Unseen mechanics mid-fight.

### Phase Mechanics

| Phase | HP Threshold | Mechanics |
|-------|--------------|-----------|
| **Phase 1** | 100–70% | "Veil Cleave" (delayed slash lines) + "Rift Pulse" (telegraphed pull) |
| **Phase 2** | 70–35% | **Eclipse Swap** — arena forces Seen/Unseen flip every few turns. Counterplay: activate Foundation Pillar to "pin" reality for one cycle |
| **Phase 3** | 35–0% | **Echo Dominion** — boss spawns Echo-Party adds (weaker copies). Counterplay: step on Sync Plates to weaken echoes |

### Arena Interactables

#### Foundation Pillars

| Pillar | Coordinates |
|--------|-------------|
| **Pillar A** | (54, 88) |
| **Pillar B** | (122, 88) |
| **Pillar C** | (54, 98) |
| **Pillar D** | (122, 98) |

#### Sync Plates

| Plate | Coordinates |
|-------|-------------|
| **Center-left** | (74, 92) |
| **Center-right** | (102, 92) |

### Boss Reward

**RELIC ACQUIRED: SHADOW FRAGMENT**  
*(alt names: Umbra Core / Eclipse Shard)*

---

## 4) Pedestal Chamber — Shadow Seat

- **No encounters**
- The room is lit by nothing, yet everything is visible

### Anchors

| Feature | Coordinates |
|---------|-------------|
| **Pedestal** | (88, 110) |
| **Interact prompt** | "Seat relic?" |

### Suggested System Outputs

| Output | Effect |
|--------|--------|
| **RELIC SEATED — SHADOW** | Canon flag |
| **WORLD EFFECT: ECLIPSE ROUTES** | Hidden seams appear on overworld + capital |
| **NEW FIELD TECH: SHADOWWALK** | Phase through thin barriers / slip past patrol gates / reveal "Unseen" caches on maps |
| **FINAL ACT GATE** | Nexus sealed—path to endgame opens |

---

## 5) Completion Flags

| Flag | Value |
|------|-------|
| **D8_CLEARED** | TRUE |
| **RELIC_SHADOW_ACQUIRED** | TRUE |
| **RELIC_SHADOW_SEATED** | TRUE |
| **SHADOWWALK_UNLOCKED** | TRUE |
| **ECLIPSE_ROUTES_UNLOCKED** | TRUE |

---

## 6) Enemy Tables (Void Nexus)

### Common

| Enemy | Traits |
|-------|--------|
| **Umbral Skulkers** | Ambush + void rot |
| **Rift Wisps** | Pull/slow |
| **Null Sentinels** | Construct tanks; punish greedy routes |
| **Ink-Phantoms** | Confounded + silence-like effects |

### Rare / Elite

| Enemy | Traits |
|-------|--------|
| **Regent's Auditor** | Dispels buffs, marks targets |
| **Seam Warden** | Elite; drops high-tier Shadow mats |

---

## 7) QoL + Replay Value

### Post-Clear Fast Travel

D8 becomes a fast-travel seam between:
- **Crown District ↔ Chronowake** (world routing reward)

### Post-Clear "Unseen Doors"

| Door | Leads To |
|------|----------|
| **Lore Vault** | Optional deep lore |
| **Super-Elite Arena** | Rematch arena (NG+ bait) |

---

## Quick Reference: Dungeon Overview

```
CROWN DISTRICT / SPIRE FOUNDATION
       |
       v
[SUBMAP 1: BREACH VESTIBULE]
   Size: 128×72 | Lv — (light)
   Entry: (64, 6) | Tutorial: Seen/Unseen
   Altar: (64, 24) | Veil Door: (64, 52)
   Exit: (64, 70)
       |
       v
[SUBMAP 2: ECHO GALLERIES]
   Size: 160×112 | Lv 80–92
   Entry: (80, 6) | Exit: (80, 106) [locked]
   Central Altar: (80, 56)
   Sync Plates: A (46, 42), B (114, 42)
   Seal A — ECLIPSE MARK: (24, 88) [UNSEEN]
   Mini-elite: ECHO OF THE PARTY (80, 30) → Umbral Band
       |
       v
[SUBMAP 3: NULL RECORDS]
   Size: 160×104 | Lv 84–96
   Entry: (80, 6) | Exit: (80, 98) [locked]
   Revision Console: (80, 44) | Chrono Dial: (96, 44)
   Seal B — NULL SIGNET: (132, 28) [DECREE + PRESENT]
   Seal C — SHADOW WITNESS: (24, 72) [BLANK + UNSEEN]
       |
       v
[SUBMAP 4: STILLPOINT HUB]
   Size: 112×80 | Safe Zone
   Entry: (56, 6) | Save: (56, 40)
   Stillpoint Well: (56, 26)
   Foundation Pylons: Tide (28,52), Mass (56,58), Time (84,52)
   Exit: (56, 74)
       |
       v
[SUBMAP 5: UMBRA ENGINE + NEXUS HEART]
   Size: 176×112 | Lv 90–99
   Entry: (88, 6) | Antechamber: (88, 48)
   Boss: VOID NEXUS REGENT at (88, 90)
   Reward: SHADOW FRAGMENT → SHADOWWALK UNLOCKED
   Pedestal: (88, 110) | Shortcut: (168, 86)
   
   ECLIPSE ROUTES UNLOCKED
   FINAL ACT GATE OPENED
       |
       v
NEXUS GATE SHORTCUT → CROWN DISTRICT / CHRONOWAKE
```

**Key Anchors Summary:**

| Feature | Coordinates |
|---------|-------------|
| **Submap 1 Entry** | (64, 6) |
| **Submap 1 Altar** | (64, 24) |
| **Veil Door** | (64, 52) |
| **Submap 1 Exit** | (64, 70) |
| **Submap 2 Entry** | (80, 6) |
| **Central Altar** | (80, 56) |
| **Sync Plate A** | (46, 42) |
| **Sync Plate B** | (114, 42) |
| **Seal A (Eclipse Mark)** | (24, 88) |
| **Echo Mini-Elite** | (80, 30) |
| **Submap 2 Exit** | (80, 106) |
| **Submap 3 Entry** | (80, 6) |
| **Revision Console** | (80, 44) |
| **Chrono Dial** | (96, 44) |
| **Seal B (Null Signet)** | (132, 28) |
| **Seal C (Shadow Witness)** | (24, 72) |
| **Submap 3 Exit** | (80, 98) |
| **Submap 4 Entry** | (56, 6) |
| **Save Crystal** | (56, 40) |
| **Stillpoint Well** | (56, 26) |
| **Tide Pylon** | (28, 52) |
| **Mass Pylon** | (56, 58) |
| **Time Pylon** | (84, 52) |
| **Submap 4 Exit** | (56, 74) |
| **Submap 5 Entry** | (88, 6) |
| **Antechamber** | (88, 48) |
| **Boss Door** | (88, 70) |
| **Boss Arena** | (88, 90) |
| **Pillar A** | (54, 88) |
| **Pillar B** | (122, 88) |
| **Pillar C** | (54, 98) |
| **Pillar D** | (122, 98) |
| **Sync Plate (left)** | (74, 92) |
| **Sync Plate (right)** | (102, 92) |
| **Pedestal** | (88, 110) |
| **Nexus Gate Shortcut** | (168, 86) |
