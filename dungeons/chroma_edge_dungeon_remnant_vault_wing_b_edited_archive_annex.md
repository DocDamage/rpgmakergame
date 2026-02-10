# Remnant Vault — Wing B: Edited Archive Annex

## 1. Overview

| Attribute | Value |
|-----------|-------|
| **Wing Name** | Edited Archive Annex |
| **Theme** | Time/Light |
| **Role** | "Read the record"—flicker slabs + record locks + truth beacons. Rewards clean movement and attention |
| **Objective** | Collect 3 Record Fragments → Commit at Archive Terminal → obtain Vault Sigil → return portal opens |
| **Map Size** | 96 × 64 tiles (local coords x 0–95, y 0–63) |
| **Encounters** | ON (room pockets), OFF (connectors) |
| **Core Counterplay** | Stabilizer Stations (2) + Truth Beacon (1) |

---

## 2. Global Wing Rules

### Baseline Hazards

| Hazard | Effect |
|--------|--------|
| **Flicker Slabs** | Ending a turn on a blank tile = Turn Delay +1 |
| **Prism Verdict** | Safe wedge—periodic positioning check (light/clarity theme) |

### Record Lock Rule
- Each Fragment is guaranteed behind a short combat/puzzle gate
- After all 3 obtained, Terminal always opens final door (no RNG)

---

## 3. Key Anchors & Navigation

### Entry / Exit

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Wing entry spawn | (48, 60) | From Remnant Gatehouse hub |
| Return Portal (post-completion) | (48, 58) | Spawns after Commit |

### Main Route

```
Entry → Lobby → Split to Fragment A/B → Mid Terminal Hall → Fragment C → Commit Terminal → Return
```

---

## 4. Room List

### ROOM 0 — Annex Entry (Safe)

| Property | Value |
|----------|-------|
| **Bounds** | x 38–58, y 54–63 |
| **Encounter** | None |

#### Props

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Wing Signpost | (48, 56) | "Edited Archive Annex — 3 Record Fragments" |
| Return Portal | (48, 58) | Spawns post-Commit |
| Exit to Room 1 | (48, 53) | North door |

---

### ROOM 1 — Index Lobby (Small Fight + Split)

| Property | Value |
|----------|-------|
| **Bounds** | x 18–78, y 40–54 |
| **Encounter Pocket** | Center (single wave) |

#### Hazards — Flicker Slabs Zone

| Property | Value |
|----------|-------|
| Zone | x 40–56, y 46–50 |
| Cycle | Every 12s |
| Telegraph | 1.4s |
| Active | 5.0s |
| Effect | 8 tiles flicker per cycle |

#### Doors

| Door | Coordinates | Destination |
|------|-------------|-------------|
| West | (20, 47) | Room 2 (Fragment A) |
| East | (76, 47) | Room 3 (Fragment B) |
| North | (48, 39) | Room 4 (Mid Hall) |

#### Encounter (Tier Scaling)

| Enemy | Count | Notes |
|-------|-------|-------|
| Chrono Scriber | 2 | Delay-lite |
| Rift Skirmisher | 2 | Fast melee |
| Null Caster | 1 | Tier 5+ only |

---

### ROOM 2 — Fragment A: "Misfile Stack" (Combat + Micro Puzzle)

| Property | Value |
|----------|-------|
| **Bounds** | x 2–34, y 26–54 |
| **Fragment** | **FRAGMENT A** at (12, 32) |

#### Mechanics — Record Shelf Locks

| Lock | Coordinates | Rule |
|------|-------------|------|
| Lock Plate 1 | (10, 44) | Step both within 8s → shelf slides open |
| Lock Plate 2 | (22, 44) | Step both within 8s → shelf slides open |

#### Hazards — Stop Panel

| Property | Value |
|----------|-------|
| Location | Centered near (18, 38) |
| Cycle | Every 18s |
| Telegraph | 1.6s |
| Active | 4.0s |
| Effect | STOP short + Turn Delay pressure |

#### Encounter

| Enemy | Count | Tier Note |
|-------|-------|-----------|
| Index Warden (Elite) | 1 | Tier 4+ only |
| Chrono Scriber | 2 | — |
| Rift Skirmisher | 1 | — |

#### Loot

| Object | Coordinates | Contents |
|--------|-------------|----------|
| **Chest A** | (28, 30) | Mats + currency (guaranteed) |
| **Fragment A** | (12, 32) | Glowing page shard |

#### Door

| Door | Coordinates | Destination |
|------|-------------|-------------|
| To Lobby | (20, 47) | Room 1 |

---

### ROOM 3 — Fragment B: "Prism Index" (Safe Wedge Check + Fight)

| Property | Value |
|----------|-------|
| **Bounds** | x 62–94, y 26–54 |
| **Fragment** | **FRAGMENT B** at (84, 32) |

#### Hazards — Prism Verdict (Safe Wedge)

| Property | Value |
|----------|-------|
| Cycle | Every 12s |
| Telegraph | 1.5s |
| Active | 8.0s |
| Effect | Outside wedge: chip + Dazzled buildup (short) |

#### Encounter

| Enemy | Count | Tier Note |
|-------|-------|-----------|
| Prism Skirmisher | 2 | Light-themed, fast line shots |
| Chrono Scriber | 1 | — |
| Refraction Image | 1 | Tier 6+ only; dies fast; distractor |

#### Optional Chest B

| Property | Value |
|----------|-------|
| Location | (92, 30) |
| Access | Only reachable safely during safe wedge active window |
| Contents | Better mat roll + accessory chance |

#### Door

| Door | Coordinates | Destination |
|------|-------------|-------------|
| To Lobby | (76, 47) | Room 1 |

---

### ROOM 4 — Mid Hall: "Redacted Corridor" (Stabilizer + Truth Loop)

| Property | Value |
|----------|-------|
| **Bounds** | x 18–78, y 18–40 |
| **Stabilizer** | Station #1 at (24, 28) |
| **Truth Beacon** | (48, 28) — required |

#### The Loop Mechanic

| Condition | Result |
|-----------|--------|
| Go north without activating Truth Beacon | Redirected to Room 4 start ("page flip" visual) |
| UI Toast | "RECORD EDIT DETECTED." |

#### Truth Beacon

| Property | Value |
|----------|-------|
| Interact time | 1.0s |
| Cooldown | 20s |
| Effect | Reveals "true door" outline (12s); disables loop redirect |

#### Encounter (2-Wave, Medium)

**Wave 1:**

| Enemy | Count |
|-------|-------|
| Chrono Scriber | 2 |
| Rift Skirmisher | 2 |

**Wave 2:**

| Enemy | Count | Tier Note |
|-------|-------|-----------|
| Null Caster | 1 | — |
| Redaction Adept (Elite) | 1 | Tier 6+ only |

#### Door

| Door | Coordinates | Destination |
|------|-------------|-------------|
| North | (48, 17) | Room 5 (Fragment C) |

---

### ROOM 5 — Fragment C: "Timestamp Vault" (Harder Room + Commit Access)

| Property | Value |
|----------|-------|
| **Bounds** | x 26–70, y 2–18 |
| **Fragment** | **FRAGMENT C** at (48, 10) |
| **Archive Terminal** | (48, 6) — locked until all 3 fragments obtained |
| **Stabilizer** | Station #2 at (28, 12) |

#### Hazards (Capstone)

**Flicker Slabs:**

| Property | Value |
|----------|-------|
| Zone | 8 tiles around center |
| Cycle | Every 10s |
| Telegraph | 1.4s |
| Active | 5.0s |

**Lag Pulse Ring:**

| Property | Value |
|----------|-------|
| Frequency | Every 16s |
| Telegraph | 1.4s expanding ring |
| Effect | Turn Delay +1 on hit |

#### Encounter

| Enemy | Count | Tier Note |
|-------|-------|-----------|
| Timestamp Curator (Elite) | 1 | — |
| Chrono Scriber | 1 | — |
| Null Caster | 1 | Tier 5+ only |
| Rift Skirmisher | 2 | Tier 7+ adds one more |

#### Archive Terminal UI

```
┌─────────────────────────────────────┐
│  ARCHIVE TERMINAL — COMMIT RECORD   │
├─────────────────────────────────────┤
│ Insert Record Fragments to          │
│ stabilize the Annex.                │
│                                     │
│ Fragments inserted: {0/3…3/3}       │
│                                     │
│  [COMMIT] (enabled at 3/3)          │
│  [CANCEL]                           │
└─────────────────────────────────────┘
```

#### On Commit (3/3)

1. UI Toast: "RECORD COMMITTED."
2. Spawn **VAULT SIGIL** at (48, 12)
3. Unlock all doors + spawn Return Portal at Entry

---

## 5. Loot & Rewards

### Guaranteed

| Source | Contents |
|--------|----------|
| **Chest A** (Room 2) | Mats + currency |
| **Each Fragment room** | 1–2 Core Dust + small mat roll |
| **Vault Sigil** | After Terminal Commit |

### Optional

| Source | Contents |
|--------|----------|
| **Chest B** (Room 3) | Better mat roll + accessory chance |

### Tier Scaling

| Tier | Adjustments |
|------|-------------|
| **1–3** | Fewer elites, lighter hazard density |
| **4–6** | Elite in Room 2 and Room 5; adds Null Caster reliably |
| **7–10** | Tighter Flicker cadence in Room 5; +1 skirmisher in Room 1 |

---

## 6. Navigation Flowchart

```
┌─────────────────────────────────────────────────────────────────┐
│                      ANNEX ENTRY (Room 0)                       │
│                          [Safe Zone]                            │
└─────────────────────────────┬───────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                      INDEX LOBBY (Room 1)                       │
│            [Flicker Slabs + Split Path + Fight]                 │
└─────────────┬───────────────────────────────┬───────────────────┘
              │                               │
              ▼                               ▼
┌─────────────────────────┐       ┌───────────────────────────────┐
│  FRAGMENT A (Room 2)    │       │    FRAGMENT B (Room 3)        │
│  ["Misfile Stack"]      │       │    ["Prism Index"]            │
│                         │       │                               │
│  • Lock Plates puzzle   │       │  • Prism Verdict safe wedge   │
│  • Stop Panel hazard    │       │  • Optional Chest B           │
│  • Chest A (guaranteed) │       │                               │
└───────────┬─────────────┘       └───────────────┬───────────────┘
            │                                     │
            └─────────────────┬───────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                MID HALL (Room 4) — "Redacted Corridor"          │
│           [Stabilizer #1 + Truth Beacon + 2-Wave Fight]         │
│                                                                 │
│  • Truth Beacon: disables loop redirect                         │
│  • Loop trap until beacon activated                             │
└─────────────────────────────┬───────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│               FRAGMENT C (Room 5) — "Timestamp Vault"           │
│       [Stabilizer #2 + Lag Pulse + Archive Terminal]            │
│                                                                 │
│  • Fragment C at (48, 10)                                       │
│  • Terminal at (48, 6) — Commit at 3/3 fragments                │
│  → VAULT SIGIL acquired → Return to Entry                       │
└─────────────────────────────────────────────────────────────────┘
```

---

## 7. Coordinate Quick Reference

### Entry & Hub
```
Entry Spawn: (48, 60)          Wing Sign: (48, 56)
Return Portal: (48, 58)        To Lobby: (48, 53)
```

### Room 1 — Index Lobby
```
Flicker Zone: x 40–56, y 46–50
West Door: (20, 47)            East Door: (76, 47)
North Door: (48, 39)
```

### Room 2 — Fragment A (Misfile Stack)
```
Fragment A: (12, 32)           Chest A: (28, 30)
Lock Plates: (10, 44) (22, 44)
Stop Panel: near (18, 38)
To Lobby: (20, 47)
```

### Room 3 — Fragment B (Prism Index)
```
Fragment B: (84, 32)           Chest B: (92, 30)
To Lobby: (76, 47)
```

### Room 4 — Mid Hall (Redacted Corridor)
```
Stabilizer #1: (24, 28)        Truth Beacon: (48, 28)
North Door: (48, 17)
```

### Room 5 — Fragment C (Timestamp Vault)
```
Fragment C: (48, 10)           Terminal: (48, 6)
Stabilizer #2: (28, 12)
Flicker Zone: 8 tiles around center
Vault Sigil spawn: (48, 12)
```

---

## 8. Implementation Notes

- **Fragment Order**: A and B can be collected in any order; C is always last
- **Loop mechanic**: Room 4 redirect happens only once until Truth Beacon activated; stays disabled for remainder of run
- **Stabilizer placement**:
  - Station #1: Before loop + mid-fight (Room 4)
  - Station #2: In capstone room (Room 5)
- **Chest B timing**: Only accessible during Prism Verdict safe wedge active window—skill check for better reward
- **Fragment tracking**: UI shows {0/3} → {3/3} progress; Terminal enables COMMIT button at max
- **Completion flow**: 
  - All doors unlock post-Commit
  - Return Portal spawns at Entry (48, 58)
  - Toast: "RECORD COMMITTED." + "RETURN PORTAL OPENED."
- **Truth Beacon persistence**: Once activated, "true door" outline stays visible and loop permanently disabled
- **Tier scaling**: Enemy additions and hazard frequency adjustments based on selected Vault Tier
