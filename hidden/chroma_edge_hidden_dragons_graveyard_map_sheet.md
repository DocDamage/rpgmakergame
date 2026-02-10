# Chroma's Edge — Dragon's Graveyard Hidden Area Map Sheet (v1)
## Optional Mass Expedition — "Even Legends Have Weight"

---

## 0) Technical Specs

| Parameter | Value |
|-----------|-------|
| **Area Type** | Hidden Area (Optional) |
| **Unlock Condition** | `RELIC_MASS_SEATED = TRUE` (post-D6) |
| **Recommended Level** | Lv 60–90 (late-game curve) |
| **Theme** | Mass + ancient bones + "even legends have weight" |
| **Primary Rewards** | Mass-tier mats, unique accessory line, optional mount unlock, deep lore key pointing toward endgame anomalies |
| **Structure** | 4 submaps (expedition feel, not single arena) |
| **Encounters** | ON (except Safe Cairn + post-boss chamber) |
| **Key Mechanics** | Boneweight Gauge + Anchor Plates + Gravity Wells + Ossuary Keys |
| **Save Points** | 1 (Cairn of Stillstone) + autosave before optional boss |
| **Return Loop** | Riblift Shortcut unlocks after vault access → fast return to entrance |

---

## 1) Macro Flow (How it Plays)

**Flow:** Gravemark Spur → Ribcage Ravine → Cairn of Stillstone (Save/Safe) → Wyrm Sepulcher (Puzzle + Optional Boss + Vault) → Riblift Shortcut → Exit

### Macro ASCII

```
[MAP 1 Gravemark Spur]
        |
        v
[MAP 2 Ribcage Ravine]
        |
        v
[MAP 3 Cairn of Stillstone] (SAFE + SAVE)
        |
        v
[MAP 4 Wyrm Sepulcher]
  Puzzle + Optional Boss + Vault
        |
   Riblift Shortcut
        v
Back to Map 1 entrance
```

---

## CORE MECHANICS (Graveyard-Wide)

### A) Boneweight Gauge (Mass Variant)

Builds in "grave pressure" zones (dense bone fields + gravity scars).

| Level | Effect |
|-------|--------|
| **Weighted** | Movement speed down; encounter ambush rate slightly up |
| **Crushing** | Periodic chip + reduced evasion |
| **Pinned** | Disables dash/field tech until relief reached |

#### Relief Sources

| Source | Effect |
|--------|--------|
| **Anchor Plates** | Safe pads |
| **Stillstone Cairns** | Reduce gauge & cleanse "Pinned" |
| **Countermass Totems** | Optional objective lowering Boneweight gain in Map 4 |

### B) Anchor Plates (Hard Utility)

- Standing on one halts Boneweight gain
- Prevents forced movement from Gravity Wells
- Some gates open only when two plates are activated (switch puzzle)

### C) Gravity Wells (Telegraphed Pull)

- Swirling dust + floating pebbles mark active wells
- Pull 1 tile every few seconds toward a "sink" tile
- Anchor Plates = safe islands; otherwise route around or time crossings

### D) Ossuary Keys (3-Piece Progression)

Three "Bone Sigils" open the Sepulcher Vault:
- Skull Sigil
- Rib Sigil
- Spine Sigil

---

## SUBMAP 1 — GRAVEMARK SPUR (Hidden Approach)

**Purpose:** Reveal the secret route, establish "bones in the earth" vibe, teach Boneweight gently.

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 112 × 64 tiles |
| **Entry** | From Gravemark Outpost hidden route (unlocks after Mass seated) |
| **Exit** | To Ribcage Ravine |
| **Encounter Band** | Lv 60–70 (light-medium) |

### B) Visual / Tone

A canyon spur where the ground is studded with fossil plates. Wind sounds muffled—like the air itself is heavy.

### C) Anchors (Local Coords 0–111, 0–63)

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **ENTRY** | (56, 6) | Safe apron, no encounters first ~8 tiles |
| **EXIT to Map 2** | (56, 62) | — |
| **Anchor Plate tutorial** | (38, 24) | — |
| **Stillstone Cairn #1** | (78, 22) | Reduces gauge |
| **Chest** (early) | (18, 16) | Mass Patch ×1 + "Bone Resin" mat ×1 |

### D) One-Time Script Beat (Recommended)

| Property | Value |
|----------|-------|
| **Trigger** | (54, 18) |
| **Event** | A huge rib shadow passes under the dust—then you realize it's not moving… you are |

---

## SUBMAP 2 — RIBCAGE RAVINE (Traversal + Sigil Hunt)

**Purpose:** The main "bone canyon" map; introduces gravity wells properly; contains 2 sigils.

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 144 × 96 tiles |
| **Entry** | From Map 1 |
| **Exit** | To Cairn of Stillstone |
| **Encounter Band** | Lv 65–78 (medium) |

### B) Layout Concept

A ravine formed by a colossal ribcage:
- **Outer ridge path:** Safer, longer
- **Inner rib lanes:** Gravity wells + better loot
- **Collapsed sternum bridge:** Timed crossing

### C) Gravity Well Placement (Telegraphed)

| Well | Center | Pull Toward |
|------|--------|-------------|
| **Well A** | (72, 44) | (72, 50) |
| **Well B** | (112, 58) | (118, 64) |

### D) Sigils (2 of 3)

| Sigil | Coordinates | Location |
|-------|-------------|----------|
| **Rib Sigil** | (34, 72) | Behind bone arch; mild Boneweight zone |
| **Skull Sigil** | (128, 22) | Requires crossing sternum bridge timing |

### E) Anchors

| Feature | Coordinates |
|---------|-------------|
| **ENTRY** | (72, 6) |
| **EXIT to Map 3** | (72, 94) |
| **Anchor Plate** (near Well A) | (60, 42) |
| **Anchor Plate** (near Well B) | (106, 56) |
| **Chest** (ridge) | (20, 52) | "Anchor Charm" mat |
| **Chest** (inner lane) | (118, 80) | High-tier plating mat |

---

## SUBMAP 3 — CAIRN OF STILLSTONE (SAFE + SAVE HUB)

**Purpose:** Calm center that feels like a negotiated peace with gravity. Save, prep, optional totems.

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 112 × 80 tiles |
| **Encounters** | OFF in central ring |
| **Entry** | From Ribcage Ravine |
| **Exit** | To Wyrm Sepulcher |
| **Save Point** | Yes |

### B) Visual / Tone

A circular basin with a standing stone "cairn" that hums at a low frequency. Dust falls upward in tiny threads.

### C) Anchors

| Feature | Coordinates |
|---------|-------------|
| **ENTRY** | (56, 6) |
| **SAVE CRYSTAL** | (56, 40) |
| **Stillstone Cairn** (full cleanse) | (56, 28) |
| **Exit to Map 4 corridor** | (56, 74) |

### D) Optional Global QoL — Countermass Totems (2)

Activating both reduces Boneweight gain + weakens gravity wells in Map 4.

| Totem | Coordinates |
|-------|-------------|
| **Totem #1** | (22, 54) |
| **Totem #2** | (90, 54) |

### E) Optional Lore Node

| Feature | Coordinates | Text |
|---------|-------------|------|
| **Carved Ledger Stone** | (78, 34) | "The dragon didn't fall. The world got heavier." |

---

## SUBMAP 4 — WYRM SEPULCHER (Vault + Optional Boss)

**Purpose:** Climax map: bone cathedral, anchor plate gate puzzle, vault door, optional boss.

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 128 × 112 tiles |
| **Encounter Band** | Lv 75–90 (elite chance) |
| **Pre-boss antechamber** | No encounters + relief pad |
| **Core progression** | Acquire Spine Sigil → open Sepulcher Vault → optional boss triggers at vault |

### B) Core Puzzle — "Anchor Gate + Spine Sigil"

**Goal:** Open Load Gate using two Anchor Plates, then retrieve Spine Sigil.

#### Load Gate

| Feature | Coordinates |
|---------|-------------|
| **Gate** | (64, 46) — opens when both plates active |
| **Plate A** | (44, 40) |
| **Plate B** | (84, 40) |

Once gate opens → corridor to Sigil.

#### Spine Sigil

| Feature | Coordinates |
|---------|-------------|
| **Spine Sigil pedestal** | (64, 66) |

### C) Vault Door (3 Sigils)

| Feature | Coordinates | Requirement |
|---------|-------------|-------------|
| **Vault Door** | (64, 84) | Skull + Rib + Spine Sigils |

### D) Anchors

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **ENTRY** | (64, 6) | — |
| **Relief Pad** (antechamber) | (64, 34) | Resets Boneweight |
| **Chest A** | (18, 22) | "Graveseal Mantle" upgrade mat |
| **Chest B** | (110, 22) | "Countermass Pin" craft mat |
| **Riblift Shortcut** (post-vault) | (118, 92) | Returns to Map 1 near entry |

---

## 2) Optional Boss — "Gravewyrm Echo"

| Property | Value |
|----------|-------|
| **Trigger** | Opening the Sepulcher Vault OR looting the core chest |
| **Arena** | Vault chamber with 4 anchor pylons and rotating gravity wells |

### Boss Identity

Not a living dragon—an echo shaped by Mass + memory. It fights like something that can't let go of its own weight.

### Phase Mechanics

| Phase | HP Threshold | Mechanics |
|-------|--------------|-----------|
| **Phase 1** | 100–65% | Tail-sweep knockbacks + bone shard volleys (telegraphed arcs) |
| **Phase 2** | 65–30% | **Gravity Ring activates** — wells rotate every X turns. Anchor Pylons prevent forced movement if you stand on them |
| **Phase 3** | 30–0% | **Mass Collapse** — arena "heaviness" spikes. Players must trigger Stillstone Pulse to stabilize |

### Arena Interactables

| Pylon | Coordinates |
|-------|-------------|
| **Anchor Pylon A** | (34, 92) |
| **Anchor Pylon B** | (94, 92) |
| **Anchor Pylon C** | (34, 102) |
| **Anchor Pylon D** | (94, 102) |
| **Stillstone Pulse Lever** | (64, 96) | 1–2 uses; reduces Boneweight spike |

### Boss Rewards

| Reward | Description |
|--------|-------------|
| **Accessory: WYRMGRAV SIGIL** | Boneweight gain -20%, Knockback immunity 1st time per battle, increased "gravity mat" drop rate |
| **Key Item: DRAGON BONE CORE** | Used for top-tier forge/pressworks crafting |
| **Optional Mount: FOSSIL DRAKE** | Slow but ignores "gravity scar slow tiles" on overworld |

---

## 3) Vault Loot (Always Available)

Inside the vault after opening with 3 sigils:

| Feature | Coordinates | Loot |
|---------|-------------|------|
| **Core Chest** | (64, 104) | Dragon Bone Core (if not from boss), Rare plating mats, High credits |
| **Lore Tablet** | (76, 104) | "Gravity scars as stitches" — hints at late-game Mass/Time interference |

---

## 4) Enemies (Area Table)

| Enemy | Traits |
|-------|--------|
| **Bone Scarabs** | Armor up |
| **Grave Dust Wraiths** | Boneweight spike on hit |
| **Rib Hounds** | Knockback |
| **Ossuary Wisps** | Debuff + pull setups |
| **Dominion Excavator Unit** | Rare elite if Dominion escalation active |

---

## 5) Return Loop (QoL)

**After opening the vault (boss optional):**

| Feature | Coordinates | Effect |
|---------|-------------|--------|
| **Riblift activates** | (118, 92) | — |
| **Drop point** | (90, 14) | Map 1 near entry → fast exit back to Gravemark route |

---

## 6) (Optional) Time Relic Synergy Add-On

If `RELIC_TIME_SEATED = TRUE`, add a tiny "phase door" pocket inside Map 4:

| Feature | Value |
|---------|-------|
| **Phase Crack Door** | (12, 88) — visible only in FUTURE phase |
| **Micro-room size** | 20 × 14 |
| **Contents** | Chrono Band upgrade mat, Lore about "the dragon died twice" (Time weirdness payoff) |

---

## 7) Flags / Tracking

| Flag | Condition |
|------|-----------|
| `DRAGONS_GRAVEYARD_DISCOVERED` | TRUE on first entry |
| `DRAGONS_GRAVEYARD_SIGILS_COLLECTED` | [Skull, Rib, Spine] array |
| `DRAGONS_GRAVEYARD_VAULT_OPENED` | TRUE after Vault Door opened |
| `GRAVEWYRM_ECHO_DEFEATED` | TRUE after optional boss (optional) |
| `RIBLIFT_SHORTCUT_UNLOCKED` | TRUE after Vault opened |
| `FOSSIL_DRAKE_UNLOCKED` | TRUE after mount obtained (optional) |

---

## Quick Reference: Area Overview

```
GRAVEMARK OUTPOST (Town)
       |
       v
[SUBMAP 1: GRAVEMARK SPUR]
   Size: 112×64 | Lv 60–70
   Entry: (56, 6) | Exit: (56, 62)
   Anchor tutorial: (38, 24) | Cairn: (78, 22)
   Script beat: (54, 18) — "The rib shadow isn't moving… you are."
   Chest: (18, 16) — Bone Resin
       |
       v
[SUBMAP 2: RIBCAGE RAVINE]
   Size: 144×96 | Lv 65–78
   Entry: (72, 6) | Exit: (72, 94)
   Gravity Wells: A (72, 44), B (112, 58)
   Sigils: Rib (34, 72), Skull (128, 22)
   Chests: Ridge (20, 52), Inner (118, 80)
       |
       v
[SUBMAP 3: CAIRN OF STILLSTONE]
   Size: 112×80 | Safe Hub
   Entry: (56, 6) | Save: (56, 40)
   Stillstone Cairn: (56, 28)
   Totems: (22, 54), (90, 54)
   Lore Stone: (78, 34)
       |
       v
[SUBMAP 4: WYRM SEPULCHER]
   Size: 128×112 | Lv 75–90
   Load Gate: (64, 46) — needs Plate A (44,40) + B (84,40)
   Spine Sigil: (64, 66)
   Vault Door: (64, 84) — needs 3 sigils
   Optional Boss: GRAVEWYRM ECHO
     ├─ Rewards: Wyrmgrav Sigil, Dragon Bone Core, Fossil Drake mount
   Relief Pad: (64, 34)
   Core Chest: (64, 104)
   Riblift: (118, 92)
   
   FOSSIL DRAKE MOUNT UNLOCKED (optional)
       |
       v
GRAVEMARK OUTPOST RETURN
```

**Key Anchors Summary:**

| Feature | Coordinates |
|---------|-------------|
| **Submap 1 Entry** | (56, 6) |
| **Submap 1 Exit** | (56, 62) |
| **Submap 2 Entry** | (72, 6) |
| **Submap 2 Exit** | (72, 94) |
| **Gravity Well A** | (72, 44) |
| **Gravity Well B** | (112, 58) |
| **Rib Sigil** | (34, 72) |
| **Skull Sigil** | (128, 22) |
| **Submap 3 Entry** | (56, 6) |
| **Save Crystal** | (56, 40) |
| **Stillstone Cairn** | (56, 28) |
| **Totem #1** | (22, 54) |
| **Totem #2** | (90, 54) |
| **Submap 3 Exit** | (56, 74) |
| **Submap 4 Entry** | (64, 6) |
| **Relief Pad** | (64, 34) |
| **Load Gate** | (64, 46) |
| **Plate A** | (44, 40) |
| **Plate B** | (84, 40) |
| **Spine Sigil** | (64, 66) |
| **Vault Door** | (64, 84) |
| **Core Chest** | (64, 104) |
| **Lore Tablet** | (76, 104) |
| **Riblift** | (118, 92) |
| **Phase Crack** [Time seated] | (12, 88) |
