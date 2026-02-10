# Chroma's Edge — Palace Interior (Old Lumencrest) Dungeon Map Sheet (v1)
## Capital Palace Gauntlet — "The City Isn't Ruined… It's Administered"

---

## 0) Technical Specs

| Parameter | Value |
|-----------|-------|
| **Dungeon Type** | Capital Palace Gauntlet (Final Act staging dungeon) |
| **Theme** | AUTHORITY + REVISION |
| **Recommended Level** | Lv 82–99 |
| **Primary Outcome** | SPIRE ACTUATOR / CONDUIT PERMIT → permanently opens Crown Spire Conduit route to D8 Void Nexus + endgame gear bump |
| **Structure** | 5 submaps |
| **Encounters** | ON (except Save Hub + Boss Aftermath + final access chamber) |
| **Save Points** | 1 (Judgment Atrium) + autosave pre-boss |
| **Key Mechanics** | Protocol States + Chrono Locks + Quarantine Ribs + Decree Trials |
| **Return Loop** | Processional Lift Shortcut unlocks after boss → returns to Crown District Hub |

---

## CORE MECHANICS (Palace-wide)

### A) Protocol States (Palace "Mode")

At Protocol Plinths, set palace to one of 3 operating modes:

| State | Description |
|-------|-------------|
| **OBEY** (OFFICIAL) | Gates open "legally," some side paths vanish |
| **QUESTION** (ORIGINAL) | Hidden routes + true murals appear, but hazards increase |
| **NULL** (REDACTED) | Veil fog appears; secret doors show up; stronger enemies/debuffs |

**Rule:** Many doors require both Protocol State and a Time Phase.

### B) Chrono Locks (Local Phase Requirement)

At Chrono Dials, set local locks to PAST / PRESENT / FUTURE:
- Used for "seal corridors," elevator power, and vault access

### C) Quarantine Ribs (Moving Architecture)

Thin iron rib "bars" slide across hallways on a cycle:
- **OBEY:** Ribs move slower (easier)
- **NULL:** Ribs move faster + add "Confounded" buildup

### D) Decree Trials (Simple Combat Gates)

A few doors open only after beating quick "trial" fights:
- Fast 1–2 wave encounters
- Themed as "compliance checks" (not random filler)

---

## 1) Macro Flow (How it Plays)

```
Antechamber → Ledger Halls (Protocol puzzles) → Judgment Atrium (SAVE) → Throne Engine (Boss) → Spire Root Access (Conduit opens) → Shortcut back

[MAP 1 Hall of Banners]
        |
        v
[MAP 2 Ledger Halls] (Protocol + Time locks)
        |
        v
[MAP 3 Judgment Atrium] (SAVE)
        |
        v
[MAP 4 Throne Engine] (Boss)
        |
        v
[MAP 5 Spire Root Access] (Conduit unlock + exit)
        |
   Processional Lift Shortcut
        v
Back to Crown District Hub
```

---

## SUBMAP 1 — HALL OF BANNERS (Entry / Tone Lock)

**Purpose:** Entrance pomp turned into checkpoint; introduces Protocol Plinth.

### Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 128 × 72 tiles |
| **Entry** | From Crown District Hub (Palace Antechamber door) |
| **Exit** | To Ledger Halls |
| **Encounters** | Light (or OFF for first 10 tiles) |

### Anchors (Local 0–127, 0–71)

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **ENTRY** | (12, 56) | — |
| **Protocol Plinth** (tutorial) | (52, 44) | Defaults to OBEY |
| **Chrono Dial** (tutorial) | (74, 44) | Defaults PRESENT |
| **Gate to Map 2** | (118, 40) | Opens only if OBEY + PRESENT |

### Setpiece

**Banners read:** "CROWN / ORDER / PUBLIC GOOD" — with "PUBLIC" partially chiseled away.

---

## SUBMAP 2 — LEDGER HALLS (Main Puzzle Hub)

**Purpose:** The palace's "bureaucracy architecture." 3 wings, each yields a Regnal Seal.

### Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 160 × 112 tiles |
| **Encounter Band** | Lv 82–94 |
| **Exit** | Locked until 3 seals placed |

### Central Anchors

| Feature | Coordinates |
|---------|-------------|
| **ENTRY** | (80, 6) |
| **Protocol Plinth** (central) | (80, 56) |
| **Chrono Dial** (central) | (92, 56) |
| **Seal Plinths** (3 slots) | (72, 98), (80, 98), (88, 98) |
| **Exit Gate** (locked) | (80, 106) → Map 3 |

### The 3 Seals

| Seal | Door | Location | Requirements |
|------|------|----------|--------------|
| **Seal of ACCESS** | (24, 50) [OBEY] | (16, 84) | OBEY + PRESENT |
| **Seal of TRUTH** | (80, 18) [QUESTION] | (108, 18) | QUESTION + PAST |
| **Seal of SILENCE** | (136, 50) [NULL] | (146, 86) | NULL + FUTURE |

### Optional Side Room — "Royal Index"

| Property | Value |
|----------|-------|
| **Visibility** | Only in QUESTION |
| **Entrance** | (10, 30) |
| **Loot** | Palimpsest Crownband (confounded resist + dispel resist) |

---

## SUBMAP 3 — JUDGMENT ATRIUM (Save Hub)

**Purpose:** Calm-but-oppressive midpoint, full reset station, optional stabilizers for boss map.

### Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 112 × 80 tiles |
| **Encounters** | OFF in center |
| **Save Point** | YES |

### Anchors

| Feature | Coordinates |
|---------|-------------|
| **ENTRY** | (56, 6) |
| **SAVE CRYSTAL** | (56, 40) |
| **Protocol Plinth** (stable) | (40, 44) |
| **Chrono Dial** (stable) | (72, 44) |
| **Exit to Map 4** | (56, 74) |

### Optional Boss QoL — "Crown Lamps" (2)

Activating reduces Quarantine Rib speed + veil density in Map 4:

| Lamp | Coordinates |
|------|-------------|
| **Lamp #1** | (20, 54) |
| **Lamp #2** | (92, 54) |

---

## SUBMAP 4 — THRONE ENGINE (Final Gauntlet + Boss)

**Purpose:** The palace's living control system—moving ribs, decree trials, boss arena.

### Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 176 × 112 tiles |
| **Encounter Band** | Lv 90–99 (elite chance) |
| **Pre-boss antechamber** | No encounters + cleanse pad |

### Anchors

| Feature | Coordinates |
|---------|-------------|
| **ENTRY** | (88, 6) |
| **Cleanse Pad** | (88, 46) | Clears Confounded + resets Protocol fatigue |
| **Boss Door** | (88, 70) |
| **Boss Arena Center** | (88, 92) |
| **Aftermath Door** | (88, 108) → Map 5 |

### Corridor Gimmicks

| Feature | Description |
|---------|-------------|
| **Quarantine Rib Lanes** | x 60–116, y 20–66 (moving bars) |
| **Decree Trial Gate A** | (64, 32) — opens after 1-wave fight |
| **Decree Trial Gate B** | (112, 54) — opens after 2-wave fight |

---

## FINAL BOSS — "The Crown Protocol"

*(Alt names: Regent-Null Engine / The Corrector)*

**Identity:** A machine-guardian that enforces Official reality through Protocol flips.

### Boss Mechanics

| Phase | HP Threshold | Mechanics |
|-------|--------------|-----------|
| **Phase 1** | 100–70% | Heavy strikes + "Permit Mark" (targets get debuffed if they ignore mechanics) |
| **Phase 2** | 70–35% | **Protocol Flip** every few turns (OBEY → QUESTION → NULL). Player can override the next flip by interacting with a Protocol Pillar |
| **Phase 3** | 35–0% | **Redaction Sweep** (veil ring closes in) + summons "Audit Copies" |

### Arena Interactables

| Feature | Coordinates |
|---------|-------------|
| **Protocol Pillar A** | (58, 90) |
| **Protocol Pillar B** | (118, 90) |
| **Chrono Dial Node** | (88, 84) | Lets player set arena to PAST/PRESENT/FUTURE briefly |

### Boss Reward

| Item | Description |
|------|-------------|
| **Key Item: SPIRE ACTUATOR** (or "Conduit Permit: Crown") | — |
| **Craft Mats** | Crown Alloy + Seal Wax + Paradox Glass (high tier) |
| **Accessory: CROWN SEAL OF CONTINUITY** (optional) | Confounded resist + buff-removal resist + small HP regen in "veil" zones |

---

## SUBMAP 5 — SPIRE ROOT ACCESS (Conduit Unlock)

**Purpose:** Quiet aftermath chamber + unlock route to Conduit micro-map.

### Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 112 × 72 tiles |
| **Encounters** | OFF |

### Anchors

| Feature | Coordinates |
|---------|-------------|
| **ENTRY** | (56, 6) |
| **Spire Root Console** | (56, 34) | Use SPIRE ACTUATOR |
| **Door to Crown Spire Conduit** | (110, 40) | Leads into Crown Spire Conduit: Recordfall Descent |
| **Processional Lift Shortcut** | (8, 60) | Back to Crown District Hub |

### Unlock Logic

Using the console sets:
- `SPIRE_ACTUATOR_INSTALLED = TRUE`
- `SPIRE_CONDUIT_ROUTE_OPEN = TRUE`

Enables the exit to the Conduit micro-map **permanently**.

---

## ENEMIES (Palace Interior)

### Common

| Enemy | Traits |
|-------|--------|
| **Crownshard Sentinels** | Tank constructs |
| **Seal-Leeches** | Buff drain / confounded |
| **Chrono Wisps** | Initiative pressure |
| **Audit Drones** | Mark targets; punish "rushing" |

### Rare / Elite

| Enemy | Traits |
|-------|--------|
| **Bastion Prefect Unit** | Hits hard, drops Crown Alloy |
| **Redaction Auditor** | Dispels + veil pulses |

---

## FLAGS / TRACKING

| Flag | Condition |
|------|-----------|
| `PALACE_INTERIOR_DISCOVERED` | TRUE on first entry |
| `REGNAL_SEAL_ACCESS` | TRUE when collected |
| `REGNAL_SEAL_TRUTH` | TRUE when collected |
| `REGNAL_SEAL_SILENCE` | TRUE when collected |
| `PALACE_JUDGMENT_SAVE_UNLOCKED` | TRUE |
| `CROWN_PROTOCOL_DEFEATED` | TRUE after boss |
| `SPIRE_ACTUATOR_ACQUIRED` | TRUE |
| `SPIRE_ACTUATOR_INSTALLED` | TRUE after console use |
| `SPIRE_CONDUIT_ROUTE_OPEN` | TRUE |
| `PROCESSIONAL_LIFT_UNLOCKED` | TRUE |

---

## Optional Post-D8 Shadow Synergy

If `RELIC_SHADOW_SEATED = TRUE`, add one **UNSEEN pocket** in Map 2:

| Feature | Value |
|---------|-------|
| **Unseen Door** | (96, 30) — only in UNSEEN |
| **Reward** | Umbral Ward upgrade mat + lore ("the palace was edited last.") |

---

## Quick Reference: Dungeon Overview

```
CROWN DISTRICT HUB
       |
       v
[SUBMAP 1: HALL OF BANNERS]
   Size: 128×72 | Lv — (light)
   Entry: (12, 56) | Exit: (118, 40)
   Protocol Plinth: (52, 44) [OBEY]
   Chrono Dial: (74, 44) [PRESENT]
       |
       v
[SUBMAP 2: LEDGER HALLS]
   Size: 160×112 | Lv 82–94
   Entry: (80, 6) | Exit: (80, 106) [locked]
   Central Plinth: (80, 56) | Central Dial: (92, 56)
   Seals:
   ├─ ACCESS (16, 84): OBEY + PRESENT
   ├─ TRUTH (108, 18): QUESTION + PAST
   └─ SILENCE (146, 86): NULL + FUTURE
   Side room [QUESTION]: (10, 30) → Palimpsest Crownband
       |
       v
[SUBMAP 3: JUDGMENT ATRIUM]
   Size: 112×80 | Safe Hub
   Entry: (56, 6) | Save: (56, 40)
   Crown Lamps: (20, 54), (92, 54) — reduce Map 4 hazards
   Exit: (56, 74)
       |
       v
[SUBMAP 4: THRONE ENGINE]
   Size: 176×112 | Lv 90–99
   Entry: (88, 6) | Cleanse: (88, 46)
   Boss Door: (88, 70) | Arena: (88, 92)
   Boss: CROWN PROTOCOL
   ├─ Phase 1: Permit Mark
   ├─ Phase 2: Protocol Flip (Pillars override)
   └─ Phase 3: Redaction Sweep + Audit Copies
   Reward: SPIRE ACTUATOR
       |
       v
[SUBMAP 5: SPIRE ROOT ACCESS]
   Size: 112×72 | Safe
   Entry: (56, 6)
   Console: (56, 34) — install Actuator
   Conduit Exit: (110, 40) → Crown Spire Conduit
   Shortcut: (8, 60) → Crown District Hub
   
   SPIRE CONDUIT ROUTE PERMANENTLY OPENED
       |
       v
CROWN SPIRE CONDUIT → D8 VOID NEXUS
```

**Key Anchors Summary:**

| Feature | Coordinates |
|---------|-------------|
| **Submap 1 Entry** | (12, 56) |
| **Protocol Plinth** | (52, 44) |
| **Chrono Dial** | (74, 44) |
| **Submap 1 Exit** | (118, 40) |
| **Submap 2 Entry** | (80, 6) |
| **Central Plinth** | (80, 56) |
| **Central Dial** | (92, 56) |
| **ACCESS Seal** | (16, 84) |
| **TRUTH Seal** | (108, 18) |
| **SILENCE Seal** | (146, 86) |
| **Royal Index** [QUESTION] | (10, 30) |
| **Seal Plinths** | (72, 98), (80, 98), (88, 98) |
| **Submap 2 Exit** | (80, 106) |
| **Submap 3 Entry** | (56, 6) |
| **Save Crystal** | (56, 40) |
| **Crown Lamp #1** | (20, 54) |
| **Crown Lamp #2** | (92, 54) |
| **Submap 3 Exit** | (56, 74) |
| **Submap 4 Entry** | (88, 6) |
| **Cleanse Pad** | (88, 46) |
| **Trial Gate A** | (64, 32) |
| **Trial Gate B** | (112, 54) |
| **Boss Arena** | (88, 92) |
| **Protocol Pillar A** | (58, 90) |
| **Protocol Pillar B** | (118, 90) |
| **Chrono Node** | (88, 84) |
| **Submap 5 Entry** | (56, 6) |
| **Spire Root Console** | (56, 34) |
| **Conduit Exit** | (110, 40) |
| **Processional Lift** | (8, 60) |
