# Remnant Vault — Wing A: Cinder-Scar Gallery

## 1. Overview

| Attribute | Value |
|-----------|-------|
| **Wing Name** | Cinder-Scar Gallery |
| **Theme** | Heat/Motion |
| **Role** | Fast, aggressive wing—vent lanes + conveyor strips pressure positioning without platforming |
| **Objective** | Destroy 3 Heat Nodes → obtain Vault Sigil → return portal opens |
| **Map Size** | 96 × 64 tiles (local coords x 0–95, y 0–63) |
| **Encounters** | ON (room pockets), OFF (connectors) |
| **Core Counterplay** | Stabilizer Stations (2) + readable telegraphs |

---

## 2. Global Wing Rules

### Active Hazards (Baseline)

| Hazard | Effect |
|--------|--------|
| **Flash Vents** | Periodic grates that apply Overheat stacks |
| **Conveyor Strips** | Slow forced-move zones (1 tile per 2s) |

### Success Condition

Heat Node A + B + C destroyed → spawn:
- `VAULT SIGIL` pickup at last node location
- `RETURN PORTAL` at entry room
- All connector doors unlock (clean backtracking)

---

## 3. Key Anchors & Navigation

### Entry / Exit

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Wing entry spawn | (48, 60) | From Remnant Gatehouse hub |
| Wing entry door (visual) | (48, 62) | Decorative seal |
| Return Portal (post-completion) | (48, 58) | Spawns after all nodes destroyed |

### Main Route

```
Entry → Gallery Spine → Split to Node A/B → Back to Spine → Node C → Return
```

---

## 4. Room List

### ROOM 0 — Entry Foyer (Safe)

| Property | Value |
|----------|-------|
| **Bounds** | x 38–58, y 54–63 |
| **Encounter** | None |

#### Props

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Wing Signpost | (48, 56) | "Cinder-Scar Gallery — 3 Heat Nodes" |
| Return Portal | (48, 58) | Spawns post-completion |
| Exit to Room 1 | (48, 53) | North door |

---

### ROOM 1 — Gallery Spine (Main Connector + Small Fight)

| Property | Value |
|----------|-------|
| **Bounds** | x 18–78, y 40–54 |
| **Encounter Pocket** | Center of room (single wave) |
| **Loot** | None |

#### Hazards

| Hazard | Coordinates | Notes |
|--------|-------------|-------|
| Conveyor Strip (eastbound) | x 24–72 at y 46–47 | Always ON |

#### Doors

| Door | Coordinates | Destination |
|------|-------------|-------------|
| West | (20, 47) | Room 2 (Node A Wing) |
| East | (76, 47) | Room 3 (Node B Wing) |
| North | (48, 39) | Room 5 (Stabilizer Hall) |

#### Encounter (Tier Scaling)

| Enemy | Count | Notes |
|-------|-------|-------|
| Rift Skirmisher | 2 | Fast melee |
| Null Caster | 1 | Tier 5+ only |
| Heat Runner | 1 | Fast melee, applies Overheat |

---

### ROOM 2 — Node A Wing (Heat Node A + Mini-Warden)

| Property | Value |
|----------|-------|
| **Bounds** | x 2–34, y 26–54 |
| **Objective** | **HEAT NODE A** at (12, 34) |

#### Props

| Object | Coordinates | Notes |
|--------|-------------|-------|
| **Heat Node A** | (12, 34) | Destructible objective |
| Mini-Warden Spawn | (18, 34) | "Cinder Docent" |
| Chest A | (28, 30) | Guaranteed small chest |
| Door to Spine | (20, 47) | Return to Room 1 |

#### Hazards — Flash Vents (2 grates)

| Grate | Coordinates | Size | Cycle |
|-------|-------------|------|-------|
| Grate A | (10, 44) | 3×3 | 12s |
| Grate B | (22, 44) | 3×3 | 12s |

**Vent Pattern:**
- Telegraph: 1.4s glow + hiss
- Active: 3.0s
- Effect: Overheat +2 + chip damage

#### Mini-Warden: Cinder Docent

| Move | Type | Telegraph | Effect |
|------|------|-----------|--------|
| **Cinder Arc** | Cone | 1.0s | Fire damage |
| **Brand Sigil** | Target mark | 0.8s | +Ignition debuff |
| **Compliance Sweep** | Lane | 1.3s | Blockable by 2×2 rubble pillars |

**On Death:** Heat Node becomes interactable/damageable

#### Chest A Contents
- Materials + currency

---

### ROOM 3 — Node B Wing (Heat Node B + Conveyor Trap)

| Property | Value |
|----------|-------|
| **Bounds** | x 62–94, y 26–54 |
| **Objective** | **HEAT NODE B** at (84, 34) |

#### Props

| Object | Coordinates | Notes |
|--------|-------------|-------|
| **Heat Node B** | (84, 34) | Destructible objective |
| Mini-Warden Spawn | (78, 34) | "Ash Marshal" |
| Door to Spine | (76, 47) | Return to Room 1 |
| Micro-gate doorway | (92, 34) | Leads to Room 4 (Belt Cutout) |

#### Hazards

**Conveyor Strips (northbound):**

| Strip | Coordinates | Direction |
|-------|-------------|-----------|
| Strip 1 | x 74–88 at y 44–45 | Push north |
| Strip 2 | x 74–88 at y 38–39 | Push north |

**Flash Vent (1 grate):**

| Grate | Coordinates | Size | Cycle |
|-------|-------------|------|-------|
| Grate C | (84, 48) | 3×3 | 12s |

#### Mini-Warden: Ash Marshal

| Move | Type | Telegraph | Effect |
|------|------|-----------|--------|
| **Vector Chop** | Dash line | 1.0s | Leaves afterline hazard (4s) |
| **Furnace Ring** | AOE | 1.4s | Fire burst |
| **Heat Ledger** | Pulse | 1.2s | Overheat +1 if not moving |

#### Chest B (Optional)
- Location: (92, 30) — behind timing gate
- Access: Via Room 4 micro-submap
- Contents: Better mat roll + accessory chance

---

### ROOM 4 — Micro-Submap: "Belt Cutout" (Optional Chest Gate)

| Property | Value |
|----------|-------|
| **Size** | 28 × 20 tiles |
| **Access** | Loads from Room 3 doorway at (92, 34) |
| **Purpose** | Optional reward; teaches "ride conveyor, don't panic" |

#### Layout
- One looping conveyor path with 2 vent bursts
- Goal: Reach chest platform before "vent wall" cycles twice

#### Hazards

| Hazard | Timing |
|--------|--------|
| Conveyor | Always ON |
| Vent bursts | Every 10s |
| Telegraph | 1.2s glow |
| Active | 2.5s |

#### Reward

| Object | Coordinates (local) | Contents |
|--------|---------------------|----------|
| **Chest B** | (24, 4) | Higher mat roll + accessory chance |

#### Exit
- Returns player to Room 3 near (90, 36)

---

### ROOM 5 — Stabilizer Hall (Midpoint Relief + Big Fight)

| Property | Value |
|----------|-------|
| **Bounds** | x 18–78, y 18–40 |
| **Stabilizer** | Station #1 at (24, 28) |
| **Encounter** | 2-wave pocket (main wing fight) |

#### Hazards — Flash Vents (2 grates)

| Grate | Coordinates | Size | Cycle |
|-------|-------------|------|-------|
| Grate D | (40, 22) | 3×3 | 12s |
| Grate E | (56, 22) | 3×3 | 12s |

#### Encounter (Tier Scaling)

**Wave 1:**

| Enemy | Count | Tier Note |
|-------|-------|-----------|
| Rift Skirmisher | 3 | — |
| Grav Sentinel | 1 | Tier 4+ only |

**Wave 2:**

| Enemy | Count | Tier Note |
|-------|-------|-----------|
| Null Caster | 1 | — |
| Heat Runner | 1 | — |
| **Cinderbound Enforcer** (Elite) | 1 | Tier 6+ only |

#### Doors

| Door | Coordinates | Destination |
|------|-------------|-------------|
| North | (48, 17) | Room 6 (Node C Arena) |

---

### ROOM 6 — Node C Arena (Heat Node C + Elite Warden)

| Property | Value |
|----------|-------|
| **Bounds** | x 26–70, y 2–18 |
| **Objective** | **HEAT NODE C** at (48, 8) |
| **Stabilizer** | Station #2 at (28, 12) |

#### Props

| Object | Coordinates | Notes |
|--------|-------------|-------|
| **Heat Node C** | (48, 8) | Final objective |
| Elite Warden Spawn | (48, 12) | "Gallery Warden — Pyreframe" |
| Stabilizer Station #2 | (28, 12) | Optimal use timing |

#### Hazards (Capstone Room)

**Flash Vents (4 grates):**

| Grate | Coordinates | Size | Cycle |
|-------|-------------|------|-------|
| Grate F | (34, 6) | 3×3 | 10s (tightened) |
| Grate G | (62, 6) | 3×3 | 10s |
| Grate H | (34, 14) | 3×3 | 10s |
| Grate I | (62, 14) | 3×3 | 10s |

**Conveyor Strip:**

| Strip | Coordinates | Direction |
|-------|-------------|-----------|
| Westbound | x 32–64 at y 10–11 | Always ON |

#### Elite Warden: Gallery Warden — Pyreframe

| Move | Type | Telegraph | Effect |
|------|------|-----------|--------|
| **Crownfire Stomp** | AOE ring | 1.4s | Heavy fire damage |
| **Compliance Sweep** | Lane | 1.3s | Sweeping attack |
| **Talonsnap Marker** | Target circle | 1.2s | Delayed hit |
| **Overheat Audit** (reaction) | Trigger | — | If player heals while Overheated → small burst (once/turn) |

#### On Node C Destroyed

1. Spawn **VAULT SIGIL** at (48, 8)
2. UI Toast:
   - "VAULT SIGIL ACQUIRED."
   - "RETURN PORTAL OPENED."

---

## 5. Loot & Rewards

### Guaranteed

| Source | Contents |
|--------|----------|
| **Chest A** (Room 2) | Mats + currency |
| **Each Heat Node** | 1–2 Core Dust + small mat roll |
| **Vault Sigil** | Key item for Core Vault access |

### Optional

| Source | Contents |
|--------|----------|
| **Chest B** (Room 4) | Better mat roll + accessory chance |

### Tier Scaling

| Tier | Adjustments |
|------|-------------|
| **1–3** | Fewer elites, no Enforcer |
| **4–6** | Adds Grav Sentinel + Null Caster consistently |
| **7–10** | Elite versions appear in Room 5 and Room 6 |

---

## 6. Navigation Flowchart

```
┌─────────────────────────────────────────────────────────────────┐
│                        ENTRY FOYER (Room 0)                     │
│                         [Safe Zone]                             │
└─────────────────────────────┬───────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                     GALLERY SPINE (Room 1)                      │
│              [Conveyor + Small Fight + Split Path]              │
└─────────────┬───────────────────────────────┬───────────────────┘
              │                               │
              ▼                               ▼
┌─────────────────────────┐       ┌───────────────────────────────┐
│  NODE A WING (Room 2)   │       │    NODE B WING (Room 3)       │
│  [Heat Node A +         │       │    [Heat Node B + Conveyor    │
│   Cinder Docent]        │       │     + Ash Marshal]            │
│                         │       │                               │
│  Chest A (guaranteed)   │       │    ┌─────────────────────┐    │
│                         │       │    │ BELT CUTOUT (Rm 4)  │    │
└───────────┬─────────────┘       │    │ [Optional Chest B]  │    │
            │                     │    └─────────────────────┘    │
            │                     └───────────────┬───────────────┘
            │                                     │
            └─────────────────┬───────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                STABILIZER HALL (Room 5)                         │
│        [Stabilizer #1 + 2-Wave Major Fight]                     │
└─────────────────────────────┬───────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                 NODE C ARENA (Room 6)                           │
│      [Heat Node C + Stabilizer #2 + Pyreframe Elite]            │
│                                                                 │
│    → VAULT SIGIL acquired → Return to Entry Foyer               │
└─────────────────────────────────────────────────────────────────┘
```

---

## 7. Coordinate Quick Reference

### Entry & Hub
```
Entry Spawn: (48, 60)          Entry Door: (48, 62)
Return Portal: (48, 58)        Wing Sign: (48, 56)
```

### Room 1 — Gallery Spine
```
Conveyor: x 24–72, y 46–47
West Door: (20, 47)            East Door: (76, 47)
North Door: (48, 39)
```

### Room 2 — Node A Wing
```
Heat Node A: (12, 34)          Warden: (18, 34)
Grates: (10, 44) (22, 44)
Chest A: (28, 30)
```

### Room 3 — Node B Wing
```
Heat Node B: (84, 34)          Warden: (78, 34)
Grate: (84, 48)
Conveyors: x 74–88, y 44–45 and y 38–39
Micro-gate: (92, 34)
```

### Room 4 — Belt Cutout (28×20)
```
Chest B (local): (24, 4)
```

### Room 5 — Stabilizer Hall
```
Stabilizer #1: (24, 28)
Grates: (40, 22) (56, 22)
North Door: (48, 17)
```

### Room 6 — Node C Arena
```
Heat Node C: (48, 8)           Warden: (48, 12)
Stabilizer #2: (28, 12)
Conveyor: x 32–64, y 10–11
Grates: (34, 6) (62, 6) (34, 14) (62, 14)
```

---

## 8. Implementation Notes

- **Node Order Flexibility**: Node A/B can be done in any order. Node C door is always open but tuned harder—players choose risk/reward.
- **Stabilizer Placement**: 
  - Station #1: Before biggest mid-fight (Room 5)
  - Station #2: In capstone room (Room 6)
- **Completion Flow**: 
  - All doors unlock post-completion
  - Return Portal spawns at Entry Foyer (48, 58)
- **Vent Synchronization**: Consider offsetting vent cycles slightly so players aren't overwhelmed by simultaneous activations
- **Micro-Submap Loading**: Room 4 loads as separate 28×20 instance; door at (92, 34) triggers transition
- **Tier Scaling Implementation**: Enemy replacements/additions based on selected Vault Tier at hub
- **Overheat Audit**: Passive reaction trigger—check player heal action while Overheated debuff active
