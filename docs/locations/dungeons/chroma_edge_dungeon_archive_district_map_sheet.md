# Chroma's Edge — Archive District (Old Lumencrest) Map Sheet (v1)
## Time + Edited Records — "History as a Weapon, Truth as Infrastructure"

---

## 0) Technical Specs

| Parameter | Value |
|-----------|-------|
| **Dungeon Type** | Ruined-capital "dungeon-city" |
| **Theme** | TIME + Edited Records |
| **Recommended Level** | Lv 74–90 |
| **Primary Outcome** | CROWN ARCHIVE KEY (Crown Sigil Core) → unlocks Crown District gates + Timecraft upgrades + lore payload |
| **Structure** | 4 submaps |
| **Encounters** | ON (except Save Hub + Boss Aftermath) |
| **Save Points** | 1 (Redaction Atrium) + autosave pre-boss |
| **Key Mechanics** | Record States + Time Locks + Redaction Veil |
| **Return Loop** | Stacklift Shortcut unlocks after boss → fast return to Outer Wards hub |

---

## CORE MECHANICS (Archive-wide)

### A) Record States (The "Edited Records" System)

At Revision Consoles, set the district's "active record layer":

| State | Description |
|-------|-------------|
| **ORIGINAL** (pre-edit truth) | More intact routes, fewer seals, more hazards |
| **OFFICIAL** (Dominion-approved) | Doors open "legally," but some paths vanish |
| **REDACTED** (blanked) | Heavy fog veils text; hidden routes appear, enemies nastier |

**Rule:** Certain Palimpsest Doors only open in one state.

### B) Time Locks (Chrono Locks)

Doors requiring local phase alignment:
- PAST / PRESENT / FUTURE set via Chrono Dials
- Often paired with Record States: e.g., "OFFICIAL + PRESENT" to access "permit corridor"

### C) Redaction Veil (Soft Hazard)

Fog zones that:
- Lower visibility slightly (no cheap gotchas)
- Apply "Confounded" buildup (accuracy/initiative down)

**Counterplay:**
- Seal-Breaker Wax (consumable) clears a patch temporarily
- Light synergy: Light reveal highlights "true text" through veil (optional payoff)

---

## 1) Macro Flow (How it Plays)

```
[MAP 1 Gatehouse]
     |
     v
[MAP 2 Stacks Maze] --(Record + Time locks)-> (opens)
     |
     v
[MAP 3 Redaction Atrium] (SAVE)
     |
     v
[MAP 4 Vault of Revisions]
  Boss + Crown Archive Key
     |
  Stacklift Shortcut
     v
Back to Outer Wards hub
```

---

## SUBMAP 1 — ARCHIVE GATEHOUSE (Entry / Tutorial)

**Purpose:** Tone + introduce Record States safely + show "paperwork as architecture."

### Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 112 × 72 tiles |
| **Entry** | From Grand Boulevard (north exit at 112, 0) or Outer Wards north gate |
| **Exit** | To Stacks Maze |
| **Encounter Band** | Lv 74–80 (light) |

### Anchors (Local 0–111, 0–71)

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **ENTRY** | (56, 6) | No encounters first ~10 tiles |
| **Revision Console** (first tutorial) | (56, 24) | Set Record State |
| **Chrono Dial** (first tutorial) | (44, 30) | Set phase |
| **Gate to Map 2** | (56, 70) | Opens with OFFICIAL + PRESENT |

### Tutorial Puzzle (2-Step)

| Step | Action |
|------|--------|
| 1 | Console sets Record State (defaults to OFFICIAL) |
| 2 | Dial sets Phase (defaults PRESENT) |
| 3 | Chrono Lock opens when: OFFICIAL + PRESENT |

### Setpiece Beat

**Marble arch inscription:**
- **Original:** "PUBLIC RECORD"
- **Visual:** The word "PUBLIC" is chiseled out (redaction)

---

## SUBMAP 2 — THE STACKS MAZE (Main Puzzle Hub)

**Purpose:** Big library ruins + shelves-as-walls + Record State routing + two key fragments.

### Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 144 × 112 tiles |
| **Entry** | From Gatehouse |
| **Exit** | To Redaction Atrium (locked until 2 Citation Seals) |
| **Encounter Band** | Lv 76–86 (medium) |

### Layout Concept

Three wings around central catalog rotunda:
- **WING A:** Catalog Rotunda (center navigation)
- **WING B:** Scriptorium Ruins (ink hazards + OFFICIAL routes)
- **WING C:** Palimpsest Walkways (REDACTED fog + hidden ladders)

### Anchors

| Feature | Coordinates |
|---------|-------------|
| **ENTRY** | (72, 6) |
| **Central Revision Console** | (72, 52) |
| **Central Chrono Dial** | (72, 60) |
| **Exit Gate** (locked) | (72, 106) |

### Citation Seals (2 of 3)

| Seal | Coordinates | Location |
|------|-------------|----------|
| **Seal of SOURCE** | (30, 78) | Scriptorium wing |
| **Seal of SIGNATURE** | (118, 30) | Palimpsest wing |

### Wing-Specific Mechanics

**Scriptorium (OFFICIAL bias):**
- Conveyor-like "paper flow" tiles slide you 1 tile (mild), symbolizing bureaucratic momentum

**Palimpsest (REDACTED bias):**
- Redaction Veil zones hide ladders/holes (clearly shimmered at edges)

### Optional Side Room — "Index of the Unwritten"

| Property | Value |
|----------|-------|
| **Visibility** | Only in ORIGINAL state |
| **Entrance** | (12, 44) |
| **Loot** | Palimpsest Ring (anti-dispel / stasis resist) |
| **Lore** | "They didn't burn books. They replaced them." |

---

## SUBMAP 3 — REDACTION ATRIUM (Save Hub)

**Purpose:** Calm-but-haunted midpoint; gives player control and reduces fatigue.

### Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 112 × 80 tiles |
| **Encounters** | OFF in central dome |
| **Entry** | From Stacks Maze |
| **Exit** | To Vault Corridor |
| **Save Point** | YES |

### Anchors

| Feature | Coordinates |
|---------|-------------|
| **ENTRY** | (56, 6) |
| **SAVE CRYSTAL** | (56, 40) |
| **Revision Console** (stable) | (40, 44) |
| **Chrono Dial** (stable) | (72, 44) |
| **Exit to Map 4** | (56, 74) |

### Optional QoL Objective

Activate 2 "Lamp of Citation" pylons to reduce Redaction Veil density in Map 4:

| Lamp | Coordinates |
|------|-------------|
| **Lamp #1** | (20, 54) |
| **Lamp #2** | (92, 54) |

---

## SUBMAP 4 — VAULT OF REVISIONS (Final)

**Purpose:** The "history engine" chamber. Tight routing, strong theme, boss, reward, shortcut.

### Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 128 × 96 tiles |
| **Encounter Band** | Lv 82–90 (elite chance) |
| **Pre-boss antechamber** | No encounters + veil cleared |

### Corridor Puzzle: "The Three Seals"

Required seals:
- Seal of SOURCE
- Seal of SIGNATURE
- Final **Seal of SEAL** (found here)

### Anchors

| Feature | Coordinates |
|---------|-------------|
| **ENTRY** | (64, 6) |
| **Antechamber Clear Zone** | (64, 22) | Cleanses Confounded |
| **Final Seal (SEAL) pedestal** | (64, 42) |
| **Vault Door** (3-seal lock) | (64, 56) |
| **Boss Arena Center** | (64, 76) |
| **Aftermath Door** | (64, 92) |
| **Stacklift Shortcut** (post-clear) | (122, 74) | Returns to Outer Wards ring road |

### "Edited Corridor" Gimmick

Hallway where floor text changes per Record State:

| State | Floor Pattern |
|-------|---------------|
| **OFFICIAL** | Safe tiles form straight line |
| **ORIGINAL** | Safe tiles shift left (faster but more enemies) |
| **REDACTED** | Safe tiles zig-zag through veil (more hazards, better loot) |

---

## ENEMIES (Archive Table)

### Common

| Enemy | Traits |
|-------|--------|
| **Ink Wraiths** | Apply Confounded / silence-like effects |
| **Shelf Sentinels** | Constructs, high DEF, slow |
| **Paper Leeches** | Drain buffs, "bureaucracy" as status |
| **Chrono Wisps** | Initiative/turn pressure |

### Rare / Elite

| Enemy | Traits |
|-------|--------|
| **Redaction Auditor Drone** | Dispels + marks targets |
| **Crownshard Librarian** | Elite construct; drops rare mats |

---

## OPTIONAL MINIBOSS — "The Index Warden"

| Property | Value |
|----------|-------|
| **Trigger** | Guarding Seal of SIGNATURE (118, 30) in Map 2 OR gatekeeper before vault |
| **Reward** | Dial Key (set Chrono Dial instantly once per map) |

---

## FINAL BOSS — "The Redactor Engine"

### Arena

Circular vault with 3 Revision Pillars + rotating veil ring on edges.

### Boss Gimmick: "Rewrites the Fight"

| Phase | HP Threshold | Mechanics |
|-------|--------------|-----------|
| **Phase 1** | 100–65% | "Strike-through" attacks (delayed telegraphs) |
| **Phase 2** | 65–30% | **Record Flip** — boss forces Record State swap every few turns. Player can override by activating a Revision Pillar (one per flip) |
| **Phase 3** | 30–0% | **Blank Page** — temporarily removes party buffs (not permanent), summons Ink Wraith adds |

### Arena Interactables (Revision Pillars)

| Pillar | Coordinates |
|--------|-------------|
| **Pillar A** | (38, 74) |
| **Pillar B** | (64, 66) |
| **Pillar C** | (90, 74) |

---

## REWARDS

### Primary (Always)

| Item | Description |
|------|-------------|
| **CROWN ARCHIVE KEY** (Crown Sigil Core) | Unlocks Crown District Approach gate + certain quarantine seals in the capital |

### Secondary (Pick 1–2)

| Item | Description |
|------|-------------|
| **Accessory: PALIMPSEST RING** | Reduces dispel impact, reduces Confounded buildup |
| **Craft Mats** | Paradox Glass / Clocksteel / Seal Wax (high tier) |

### Lore Payload

**"Edited ledger" entries:** Explicitly show two conflicting versions of the capital's fall.

---

## FLAGS / TRACKING

| Flag | Condition |
|------|-----------|
| `LUMENCREST_ARCHIVE_DISCOVERED` | TRUE on first entry |
| `ARCHIVE_SEAL_SOURCE` | TRUE when collected |
| `ARCHIVE_SEAL_SIGNATURE` | TRUE when collected |
| `ARCHIVE_SEAL_SEAL` | TRUE when collected |
| `ARCHIVE_VAULT_OPENED` | TRUE when 3 seals used |
| `REDACTOR_ENGINE_DEFEATED` | TRUE after boss |
| `CROWN_ARCHIVE_KEY_ACQUIRED` | TRUE after boss |
| `ARCHIVE_STACKLIFT_UNLOCKED` | TRUE after clear |

---

## Quick Reference: Dungeon Overview

```
GRAND BOULEVARD / OUTER WARDS
       |
       v
[SUBMAP 1: ARCHIVE GATEHOUSE]
   Size: 112×72 | Lv 74–80
   Entry: (56, 6) | Tutorial: Record States + Time Locks
   Console: (56, 24) | Dial: (44, 30)
   Gate: (56, 70) — needs OFFICIAL + PRESENT
       |
       v
[SUBMAP 2: THE STACKS MAZE]
   Size: 144×112 | Lv 76–86
   Entry: (72, 6) | Exit: (72, 106) [locked]
   Central Console: (72, 52) | Central Dial: (72, 60)
   Seals: SOURCE (30, 78) | SIGNATURE (118, 30)
   Side room [ORIGINAL only]: (12, 44) → Palimpsest Ring
   Optional Miniboss: INDEX WARDEN → Dial Key
       |
       v
[SUBMAP 3: REDACTION ATRIUM]
   Size: 112×80 | Safe Hub
   Entry: (56, 6) | Save: (56, 40)
   Lamps of Citation: (20, 54), (92, 54) — reduce veil in Map 4
   Exit: (56, 74)
       |
       v
[SUBMAP 4: VAULT OF REVISIONS]
   Size: 128×96 | Lv 82–90
   Entry: (64, 6) | Antechamber: (64, 22)
   Final Seal: (64, 42) | Vault Door: (64, 56)
   Boss: REDACTOR ENGINE at (64, 76)
   Reward: CROWN ARCHIVE KEY + Palimpsest Ring
   Shortcut: (122, 74)
   
   CROWN DISTRICT UNLOCKED
       |
       v
OUTER WARDS HUB RETURN
```

**Key Anchors Summary:**

| Feature | Coordinates |
|---------|-------------|
| **Submap 1 Entry** | (56, 6) |
| **Submap 1 Console** | (56, 24) |
| **Submap 1 Dial** | (44, 30) |
| **Submap 1 Exit** | (56, 70) |
| **Submap 2 Entry** | (72, 6) |
| **Central Console** | (72, 52) |
| **Central Dial** | (72, 60) |
| **Seal of SOURCE** | (30, 78) |
| **Seal of SIGNATURE** | (118, 30) |
| **Index Warden** | (118, 30) or vault gate |
| **Side Room** [ORIGINAL] | (12, 44) |
| **Submap 2 Exit** | (72, 106) |
| **Submap 3 Entry** | (56, 6) |
| **Save Crystal** | (56, 40) |
| **Lamp #1** | (20, 54) |
| **Lamp #2** | (92, 54) |
| **Submap 3 Exit** | (56, 74) |
| **Submap 4 Entry** | (64, 6) |
| **Antechamber** | (64, 22) |
| **Final Seal** | (64, 42) |
| **Vault Door** | (64, 56) |
| **Boss Arena** | (64, 76) |
| **Pillar A** | (38, 74) |
| **Pillar B** | (64, 66) |
| **Pillar C** | (90, 74) |
| **Stacklift Shortcut** | (122, 74) |
