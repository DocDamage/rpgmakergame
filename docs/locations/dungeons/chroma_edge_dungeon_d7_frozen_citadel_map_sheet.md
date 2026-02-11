# Chroma's Edge — Frozen Citadel (D7) Dungeon Map Sheet (v1)
## Time Foundation Dungeon — "Stasis, Revision, Inevitability"

---

## 0) Dungeon Technical Specs

| Parameter | Value |
|-----------|-------|
| **Dungeon Type** | Main Story Dungeon 7 |
| **Foundation Theme** | TIME (stasis, revision, inevitability) |
| **Recommended Level** | Lv 58–78 |
| **Primary Outcome** | Time Relic acquired + seated → unlocks Time traversal tech (phase-shift barriers, rewind utilities, Chronowake routes), story ramps into "reality management" territory |
| **Structure** | 4 submaps (approach → phase hub → save hub → spire/boss/pedestal) |
| **Encounters** | ON (except Safe Dome + Pedestal Chamber) |
| **Save Points** | 1 (Clockheart Narthex) + autosave before boss + autosave at Pedestal |
| **Key Mechanics** | Time Phase Shift (Past/Present/Future) + Stasis Fields + Chrono Dials |
| **Return Loop** | Glacier Lift Shortcut unlocks after boss → returns near entrance |

---

## 1) Macro Flow (How it Plays)

**Flow:** Rime Causeway → Shard Halls (Phase Hub) → Clockheart Narthex (Save) → Aeon Spire (Boss + Pedestal) → Glacier Lift Shortcut → Exit

### Macro ASCII

```
[MAP 1 Rime Causeway]
        |
        v
[MAP 2 Shard Halls]  (Time Phase puzzles)
        |
        v
[MAP 3 Clockheart Narthex] (SAVE + stabilizers)
        |
        v
[MAP 4 Aeon Spire]
   Boss + Time Pedestal
        |
   Glacier Lift Shortcut
        v
Back to Map 1 (fast return)
```

---

## CORE MECHANICS (Dungeon-Wide)

### A) Time Phase Shift (3 States)

The citadel exists in overlapping layers. Player can switch phases at Chrono Altars.

| Phase | Description |
|-------|-------------|
| **PAST** | Cleaner halls, fewer collapses, some bridges intact |
| **PRESENT** | Broken-but-traversable "current" state |
| **FUTURE** | Deeper frost + heavier decay, new fractures + alternate paths |

**Rule:** Certain doors/bridges only exist in certain phases.

### B) Stasis Fields (Soft Hazard)

Shimmering ice zones that apply "Stasis" buildup:
- In-map: Slows movement
- In battle: Increases cooldown/turn delay or reduces speed/initiative

**Counterplay:**
- Heat Relic synergy reduces buildup (cross-dungeon payoff)
- Stabilizer Totems reduce field density (optional objective)

### C) Chrono Dials (Puzzle Switches)

Rotary dials that set local "time pressure" (Past/Present/Future) for a corridor without changing the whole map. Used to open Chrono Locks.

---

## SUBMAP 1 — RIME CAUSEWAY (Approach)

**Purpose:** Establish tone + introduce Phase Shift safely + teach Stasis fields gently.

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 128 × 72 tiles |
| **Entry** | From Rimehold / Chronowake approach (ferry route) |
| **Exit** | To Shard Halls |
| **Encounter Band** | Lv 58–66 (light-medium) |

### B) Visual / Tone

Frozen bridge ruins, ice-carved statues, time "snow" drifting upward sometimes (wrong physics).

### C) Anchors (Local Coords)

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **ENTRY** | (64, 6) | Encounters OFF for first ~8 tiles |
| **EXIT to Submap 2** | (64, 70) | — |
| **First Chrono Altar** (tutorial) | (44, 24) | Full phase shift; starts in PRESENT |
| **Stasis Field intro lane** | x 52–76, y 30–34 | Mild buildup |
| **Chest** (early) | (96, 18) | Stasis Balm ×2 + Ether Drop ×1 |

### D) One-Time Script Beat (Recommended)

| Property | Value |
|----------|-------|
| **Trigger** | (62, 22) |
| **Event** | Shattered bridge piece "rewinds" back into place for 2 seconds, then breaks again |
| **Lesson** | This place isn't frozen — it's looping |

---

## SUBMAP 2 — SHARD HALLS (Phase Hub)

**Purpose:** Main puzzle hub—3 wings, each yields a Time Sigil. Complete all → open gate to Narthex.

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 144 × 112 tiles |
| **Entry** | From Rime Causeway |
| **Exit** | To Clockheart Narthex (locked by 3 sigils) |
| **Encounter Band** | Lv 62–72 (medium) |

### B) Layout Concept

Central hall with 3 wings:
- **WING A:** Echo Gallery (Past-focused)
- **WING B:** Fracture Walk (Present-focused)
- **WING C:** Frostwound Annex (Future-focused)

Each wing teaches one strong "Time Phase" rule.

### C) Puzzle — The Triple Sigil

**Goal:** Collect 3 sigils → place at Chrono Gate.

| Sigil | Wing | Location | Notes |
|-------|------|----------|-------|
| **Sigil of Yesterday** | A | (12, 78) | Bridge exists only in PAST |
| **Sigil of Now** | B | (132, 80) | Moving platforms cycle in PRESENT |
| **Sigil of Tomorrow** | C | (104, 16) | Crack path + dense stasis in FUTURE |

#### Central Anchors

| Feature | Coordinates |
|---------|-------------|
| **ENTRY** | (72, 6) |
| **Chrono Gate** (locked) | (72, 106) |
| **Sigil Plinths** (3 slots) | (62, 96), (72, 96), (82, 96) |
| **Chrono Altar** (full phase shift) | (72, 54) |
| **Reset Pedestal** (restores dials) | (72, 64) |

#### Wing A — Echo Gallery (Past)

| Feature | Coordinates |
|---------|-------------|
| Wing door (only in PAST) | (24, 44) |
| Chrono Dial A | (18, 60) |
| Sigil of Yesterday chest | (12, 78) |

#### Wing B — Fracture Walk (Present)

| Feature | Coordinates |
|---------|-------------|
| Wing door (only in PRESENT) | (120, 44) |
| Chrono Dial B | (126, 62) |
| Sigil of Now chest | (132, 80) |

#### Wing C — Frostwound Annex (Future)

| Feature | Coordinates |
|---------|-------------|
| Wing door (only in FUTURE) | (72, 20) |
| Chrono Dial C | (90, 26) |
| Sigil of Tomorrow chest | (104, 16) |

### D) Optional Side Room — "Paradox Vault"

| Property | Value |
|----------|-------|
| **Hidden entrance** | (6, 48) — visible only in FUTURE |
| **Mini-elite** | Paradox Wisp |
| **Loot** | "Chrono Band" (reduces Stasis buildup + small speed/initiative) |

---

## SUBMAP 3 — CLOCKHEART NARTHEX (Save Hub)

**Purpose:** Safe(ish) calm core, save point, optional stabilizers that make Map 4 fairer.

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 112 × 80 tiles |
| **Entry** | From Shard Halls |
| **Exit** | To Aeon Spire corridor |
| **Save Point** | Yes |
| **Encounter Band** | Lv 66–74 (light; central ring is safe) |

### B) Visual / Tone

A cathedral-like chamber with a suspended frozen "clock heart" — an ancient mechanism trapped mid-tick.

### C) Anchors

| Feature | Coordinates |
|---------|-------------|
| **ENTRY** | (56, 6) |
| **SAVE CRYSTAL** | (56, 40) |
| **Clockheart Console** (lore + hint) | (56, 24) |
| **Exit to Submap 4** | (56, 74) |

### D) Optional Global QoL — Stabilizer Totems (2)

Activating both reduces Stasis field density + slows "phase flicker" hazards in Map 4.

| Totem | Coordinates |
|-------|-------------|
| **Totem #1** | (20, 54) |
| **Totem #2** | (92, 54) |

### E) Loot

| Chest | Coordinates | Loot |
|-------|-------------|------|
| **Side chest** | (14, 18) | "Timeguard Wrap" (stasis resist + small HP regen) |

---

## SUBMAP 4 — AEON SPIRE (Final)

**Purpose:** Climb corridor + phase hazards + boss + Time pedestal + shortcut.

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 128 × 112 tiles |
| **Encounter Band** | Lv 72–80 (elite chance) |
| **Pre-boss antechamber** | No encounters + phase stabilized |

### B) Corridor Hazards

| Hazard | Description |
|--------|-------------|
| **Phase Flicker Tiles** | Periodically swap between walkable/blocked depending on phase |
| **Stasis Curtains** | Narrow bands that spike Stasis buildup |
| **Chrono Locks** | Doors that open only when local dial = correct phase |

### C) Anchors

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **ENTRY** | (64, 6) | — |
| **Chrono Dial** (local corridor control) | (64, 34) | — |
| **Antechamber Safe Ring** | (64, 62) | Stasis reset + no encounters |
| **Chest A** | (22, 28) | Stasis Balm ×2 + Weapon mat |
| **Chest B** | (106, 28) | "Aeon Lens" (crit resist + phase hazard reduce) |
| **Boss Door** | (64, 76) | — |
| **Boss Arena Center** | (64, 92) | — |
| **Pedestal Chamber Door** (post-boss) | (64, 106) | — |
| **Glacier Lift Shortcut** (post-seat) | (116, 88) | Returns to Submap 1 near entry |

---

## 2) Enemy Tables (Time-Flavored)

Enemies that mess with turn order, cooldowns, or status pacing.

### Common

| Enemy | Traits |
|-------|--------|
| **Frost Sentinels** | High DEF, slow |
| **Chrono Wisps** | Speed/initiative manipulation |
| **Rime Stalkers** | Ambush + Stasis buildup |
| **Hourglass Mites** | Tiny, annoying debuffers |

### Rare / Elite

| Enemy | Traits |
|-------|--------|
| **Dominion Chrono Surveyor** | Only if Dominion escalation flag active |
| **Paradox Warden** | Elite, drops rare Time mat |

---

## 3) Miniboss (Optional Gatekeeper) — "Secondhand Guard"

| Property | Value |
|----------|-------|
| **Placement** | Aeon Spire corridor before antechamber (64, 52) |
| **Concept** | Guardian that "steals turns" or applies Stasis quickly |
| **Reward** | "Dial Key" — lets player set Chrono Dials instantly once per map (QoL for puzzles) |

---

## 4) Final Boss — "The Eon Regent"

### Arena

Circular platform with 3 phase pylons (Past/Present/Future) and a frozen clockheart overhead.

### Phase Mechanics

| Phase | HP Threshold | Mechanics |
|-------|--------------|-----------|
| **Phase 1** | 100–65% | "Time cuts" — delayed-hit telegraphs |
| **Phase 2** | 65–30% | **Phase Shift Cycle** — arena shifts every few turns: PAST (fewer hazards, boss faster), PRESENT (balanced, summons adds), FUTURE (heavy stasis curtains, boss hits harder but slower) |
| **Phase 3** | 30–0% | **Rewrite Pulse** — boss attempts to "reset" player buffs; player must activate correct pylon to resist |

### Arena Interactables (Phase Pylons)

| Pylon | Coordinates |
|-------|-------------|
| **Past Pylon** | (34, 92) |
| **Present Pylon** | (64, 84) |
| **Future Pylon** | (94, 92) |

### Boss Reward

**RELIC ACQUIRED: TIME FRAGMENT**  
*(alt name: Aeon Core)*

---

## 5) Pedestal Chamber — Time Seat

- **No encounters**
- Silence so complete it feels like sound is afraid to move

### Anchors

| Feature | Coordinates |
|---------|-------------|
| **Pedestal** | (64, 110) |
| **Interact prompt** | "Seat relic?" |

### Suggested System Outputs

| Output | Effect |
|--------|--------|
| **RELIC SEATED — TIME** | Canon flag |
| **WORLD EFFECT** | Phase barriers stabilize (new routes appear at Chronowake / Rimechain nodes) |
| **NEW FIELD TECH: REWIND STEP** | Option A: Undo last overworld movement/choice once per screen; Option B: Once per battle, reverse last instance of forced movement/status |
| **NEW CRAFTING** | Timeguard gear recipes unlocked (Rimehold + Gravemark pressworks) |

---

## 6) Shortcut / Return Loop (QoL)

**After seating:**
- **Glacier Lift activates** at (116, 88)
- **Drop point:** Submap 1 at (92, 16) — near entry approach

---

## 7) Completion Flags

| Flag | Value |
|------|-------|
| **D7_CLEARED** | TRUE |
| **RELIC_TIME_ACQUIRED** | TRUE |
| **RELIC_TIME_SEATED** | TRUE |
| **PHASE_BARRIERS_UNLOCKED** | TRUE |

---

## Quick Reference: Dungeon Overview

```
RIMEHOLD/CHRONOWAKE (Town)
       |
       v
[SUBMAP 1: RIME CAUSEWAY]
   Size: 128×72 | Lv 58–66
   Entry: (64, 6) | Exit: (64, 70)
   Chrono Altar: (44, 24) — Phase Shift tutorial
   Script beat: (62, 22) — "This place isn't frozen. It's looping."
   Chest: (96, 18) — Stasis Balm ×2
       |
       v
[SUBMAP 2: SHARD HALLS]
   Size: 144×112 | Lv 62–72
   Entry: (72, 6) | Exit: (72, 106)
   Gate: (72, 106) — needs 3 sigils
   Sigils:
   ├─ Yesterday (Past wing): (12, 78)
   ├─ Now (Present wing): (132, 80)
   └─ Tomorrow (Future wing): (104, 16)
   Side room: Paradox Vault (6, 48) [FUTURE only] → Chrono Band
       |
       v
[SUBMAP 3: CLOCKHEART NARTHEX]
   Size: 112×80 | Lv 66–74
   Entry: (56, 6) | Save: (56, 40)
   Stabilizers: (20, 54), (92, 54)
   Clockheart Console: (56, 24)
   Loot: Timeguard Wrap (14, 18)
       |
       v
[SUBMAP 4: AEON SPIRE]
   Size: 128×112 | Lv 72–80
   Entry: (64, 6) | Boss arena: (64, 92)
   Miniboss: Secondhand Guard (64, 52) → Dial Key
   Boss: THE EON REGENT (3 phases)
   Pedestal: (64, 110) | Shortcut: (116, 88)
   
   REWIND STEP UNLOCKED
   PHASE BARRIERS UNLOCKED
       |
       v
   (Glacier Lift returns to Submap 1)
       |
       v
RIMEHOLD/CHRONOWAKE (Town Return)
```

**Key Anchors Summary:**

| Feature | Coordinates |
|---------|-------------|
| **Submap 1 Entry** | (64, 6) |
| **Submap 1 Exit** | (64, 70) |
| **Submap 1 Altar** | (44, 24) |
| **Submap 2 Entry** | (72, 6) |
| **Submap 2 Gate** | (72, 106) |
| **Sigil A (Yesterday)** | (12, 78) |
| **Sigil B (Now)** | (132, 80) |
| **Sigil C (Tomorrow)** | (104, 16) |
| **Paradox Vault** | (6, 48) |
| **Submap 3 Entry** | (56, 6) |
| **Submap 3 Save** | (56, 40) |
| **Stabilizer Totems** | (20, 54), (92, 54) |
| **Submap 3 Exit** | (56, 74) |
| **Submap 4 Entry** | (64, 6) |
| **Antechamber Safe Ring** | (64, 62) |
| **Miniboss** | (64, 52) |
| **Boss Arena** | (64, 92) |
| **Past Pylon** | (34, 92) |
| **Present Pylon** | (64, 84) |
| **Future Pylon** | (94, 92) |
| **Pedestal** | (64, 110) |
| **Glacier Lift** | (116, 88) |
