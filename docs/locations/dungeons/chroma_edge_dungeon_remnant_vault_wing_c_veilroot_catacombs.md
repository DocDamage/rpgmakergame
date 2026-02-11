# Remnant Vault — Wing C: Veilroot Catacombs

## 1. Overview

| Attribute | Value |
|-----------|-------|
| **Wing Name** | Veilroot Catacombs |
| **Theme** | Shadow/Growth |
| **Role** | Control chaos—veil zones + echo adds + bud nodes that must be pruned, plus 2 Null Shrines to cleanse |
| **Objective** | Cleanse 2 Null Shrines → defeat Wing Warden → obtain Vault Sigil → return portal opens |
| **Map Size** | 96 × 64 tiles (local coords x 0–95, y 0–63) |
| **Encounters** | ON (room pockets), OFF (connectors) |
| **Core Counterplay** | Stabilizer Stations (2) + Cleansing Fonts (2) |

---

## 2. Global Wing Rules

### A) Veil Curtains (Baseline Hazard)

| Property | Value |
|----------|-------|
| Spawn | Every 18 seconds, 2 veil patches |
| Telegraph | 1.0s smoky bloom |
| Active | 8.0s |
| Effect | Confound-lite / accuracy down; +50% Null Mark chance while inside |

### B) Bud Nodes (Growth Pressure)

| Property | Value |
|----------|-------|
| Spawn | In specific rooms |
| Bloom timer | 10 seconds after spawn |
| Bloom effect | Enemies gain +regen and +damage (small) for remainder of fight |
| Drop | **Pollen Spark** pickup on death → cleanses 1 Veil Sickness / Wound / Null Mark-lite |

### C) Null Shrines (Objective Gates)

| Property | Value |
|----------|-------|
| Count | 2 shrines to cleanse |
| Channel time | 2.5s (interruptible by damage) |
| Purge Wave | 12s survival event after channel |
| Success | Shrine becomes Pure; drops Null Sigil (key item) |

---

## 3. Key Anchors & Navigation

### Entry / Exit

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Wing entry spawn | (48, 60) | From Remnant Gatehouse hub |
| Return Portal (post-completion) | (48, 58) | Spawns after Warden defeat |

### Route Shape

```
Entry → Catacomb Spine → Shrine A (west) + Shrine B (east) → Warden Antechamber (north) → Warden → Return
```

---

## 4. Room List

### ROOM 0 — Catacomb Entry (Safe)

| Property | Value |
|----------|-------|
| **Bounds** | x 38–58, y 54–63 |
| **Encounter** | None |

#### Props

| Object | Coordinates | Notes |
|--------|-------------|-------|
| Wing Signpost | (48, 56) | "Veilroot Catacombs — Cleanse 2 Null Shrines" |
| Return Portal | (48, 58) | Spawns post-Warden |
| Exit to Room 1 | (48, 53) | North door |

---

### ROOM 1 — Veilroot Spine (Small Fight + Split)

| Property | Value |
|----------|-------|
| **Bounds** | x 18–78, y 40–54 |
| **Encounter Pocket** | Center (single wave) |
| **Hazards** | Veil Curtains can spawn (baseline) |

#### Doors

| Door | Coordinates | Destination | Lock Status |
|------|-------------|-------------|-------------|
| West | (20, 47) | Room 2 (Shrine A) | Unlocked |
| East | (76, 47) | Room 3 (Shrine B) | Unlocked |
| North | (48, 39) | Room 4 (Antechamber) | Locked until both shrines purified |

#### Encounter (Tier Scaling)

| Enemy | Count | Tier Note |
|-------|-------|-----------|
| Rift Skirmisher | 2 | — |
| Null Caster | 1 | — |
| Echo Bud | 1 | Tier 5+ only; support add that buffs if alive |

---

### ROOM 2 — Null Shrine A: "Undercroft Reliquary" (Objective Event)

| Property | Value |
|----------|-------|
| **Bounds** | x 2–34, y 26–54 |
| **Null Shrine A** | (12, 34) |
| **Cleansing Font** | (28, 46) | Step to cleanse 1 major debuff; cooldown 20s |

#### Shrine Cleanse Event

**Step 1: Channel**

| Property | Value |
|----------|-------|
| Prompt | "CLEANSE NULL SHRINE" |
| Channel time | 2.5s (interruptible) |

**Step 2: Purge Wave (12s)**

| Wave | Timing | Enemies |
|------|--------|---------|
| Wave 1 | 0s | 2× Rift Skirmisher + 1× Echo Scribe |
| Wave 2 | 6s | 2× Rift Skirmisher + 1× Echo Scribe + 1× Null Caster (Tier 6+) |

**During Purge:**
- Veil Curtains spawn every 12s (tighter cadence)

**Step 3: Success**

| Result | Details |
|--------|---------|
| Shrine turns white | Visual change |
| Drop | **NULL SIGIL A** at (12, 34) |
| Toast | "NULL SIGIL ACQUIRED (1/2)." |

#### Bud Nodes
- Spawn 1 Bud Node at (18, 38) when purge begins

#### Loot

| Object | Coordinates | Contents |
|--------|-------------|----------|
| **Chest A** | (28, 30) | Mats + currency (guaranteed) |

#### Door

| Door | Coordinates | Destination |
|------|-------------|-------------|
| To Spine | (20, 47) | Room 1 |

---

### ROOM 3 — Null Shrine B: "Veilroot Chapel" (Objective Event + Optional Gate)

| Property | Value |
|----------|-------|
| **Bounds** | x 62–94, y 26–54 |
| **Null Shrine B** | (84, 34) |
| **Cleansing Font** | (68, 46) | Step to cleanse 1 major debuff; cooldown 20s |

#### Shrine Cleanse Event

**Purge Wave Spawns:**

| Wave | Timing | Enemies |
|------|--------|---------|
| Wave 1 | 0s | 2× Rift Skirmisher + 1× Null Caster |
| Wave 2 | 6s | 1× Elite "Veil Stalker" (Tier 6+) + 1× Echo Bud |

**Step 3: Success**

| Result | Details |
|--------|---------|
| Drop | **NULL SIGIL B** at (84, 34) |
| Toast | "NULL SIGIL ACQUIRED (2/2)." |

#### Bud Nodes
- Spawn 2 Bud Nodes at (78, 38) and (90, 38) at purge start

#### Optional Chest Gate

| Property | Value |
|----------|-------|
| Door tile | (92, 34) |
| Leads to | Room 3.1 "Root-Knot Cache" |

#### Door

| Door | Coordinates | Destination |
|------|-------------|-------------|
| To Spine | (76, 47) | Room 1 |

---

### ROOM 3.1 — Micro-Submap: "Root-Knot Cache" (Optional Chest Gate)

| Property | Value |
|----------|-------|
| **Size** | 28 × 20 tiles |
| **Access** | Loads from Room 3 at (92, 34) |
| **Purpose** | Small puzzle: "step on missing tiles" (shadow logic) while bud nodes spawn |

#### Mechanics

| Element | Details |
|---------|---------|
| Platform | 4×4 grid |
| Pattern | 4 tiles highlighted; 2 tiles go missing (dark) |
| Task | Step on missing tiles in order 1–2 (numbers faintly visible) |
| Success | Do twice → chest unlocks |

#### Pressure

| Trigger | Effect |
|---------|--------|
| Each attempt | Spawn 1 Bud Node (10s bloom timer) |
| Ignore buds | Swarmed by small adds |

#### Reward

| Object | Coordinates (local) | Contents |
|--------|---------------------|----------|
| **Chest B** | (24, 4) | Better mat roll + accessory chance |

#### Exit
- Returns player to Room 3 near (90, 36)

---

### ROOM 4 — Warden Antechamber: "Sealed Rootway" (Mid Fight + Stabilizer)

| Property | Value |
|----------|-------|
| **Bounds** | x 18–78, y 18–40 |
| **Door Lock** | North door locked until both Null Sigils acquired |
| **Stabilizer** | Station #1 at (24, 28) |
| **Hazards** | Veil Curtains (baseline) |

#### Bud Nodes
- Spawn 1 Bud Node at (48, 28) at start of Wave 2

#### Encounter (2-Wave Medium)

**Wave 1:**

| Enemy | Count |
|-------|-------|
| Rift Skirmisher | 2 |
| Null Caster | 1 |

**Wave 2:**

| Enemy | Count | Tier Note |
|-------|-------|-----------|
| Echo Scribe | 1 | — |
| Rootbound Enforcer (Elite) | 1 | Tier 6+ only |
| Veil Stalker | 1 | Tier 8+ only |

#### Door

| Door | Coordinates | Destination |
|------|-------------|-------------|
| North | (48, 17) | Room 5 (Warden Arena) |

#### Unlock Toast
- When both Null Sigils acquired: "ROOTWAY UNSEALED."

---

### ROOM 5 — Wing Warden Arena: "Catacomb Heart"

| Property | Value |
|----------|-------|
| **Bounds** | x 26–70, y 2–18 |
| **Warden Spawn** | (48, 12) |
| **Vault Sigil Spawn** | (48, 10) (after defeat) |
| **Stabilizer** | Station #2 at (28, 12) |

#### Hazards (Capstone)

**Veil Curtains:**

| Property | Value |
|----------|-------|
| Frequency | Every 16s (tighter) |

**Null Lanes:**

| Property | Value |
|----------|-------|
| Frequency | Every 12s |
| Telegraph | 1.4s thin violet lines |
| Effect | Medium damage + strips 1 buff (if any) |

#### Bud Nodes (Cap 2 alive)

| Spawn Trigger | Location |
|---------------|----------|
| Fight start | (38, 10) |
| Warden at 60% HP | (58, 10) |

---

## 5. Wing Warden: Veilroot Curator

### Identity
Shadow-growth hybrid that spawns buds and marks targets; punishes ignoring objective mechanics.

### Move List

| Move | Type | Telegraph | Effect |
|------|------|-----------|--------|
| **Umbral Scythe** | Line | 0.8s thin line | Damage + Null Mark-lite |
| **Root Snare** | Target circle | 1.3s | Bind/slow-lite |
| **Ledger Bloom** | Bud summon | 1.2s vine surge | Spawns Bud Node (cap 2) |
| **Null Verdict** | Pulse | 1.6s expanding ring | Removes 1 buff if outside Stabilizer Field |

### "Bloom Punish" (Anti-Ignore Rule)

| Trigger | Effect |
|---------|--------|
| Bud Node blooms during fight | Curator gains Regrowth (+small regen) and immediately casts Null Lanes once (still telegraphed) |

### Defeat Rewards

| Result | Details |
|--------|---------|
| Drop | **VAULT SIGIL** at (48, 10) |
| Toasts | "VAULT SIGIL ACQUIRED." / "RETURN PORTAL OPENED." |
| Unlock | All doors unlock; Return Portal spawns at Entry |

---

## 6. Loot & Rewards

### Guaranteed

| Source | Contents |
|--------|----------|
| **Chest A** (Room 2) | Mats + currency |
| **Each purified Null Shrine** | Core Dust + mat roll (fixed minimum) |
| **Vault Sigil** | After Warden defeat |

### Optional

| Source | Contents |
|--------|----------|
| **Chest B** (Room 3.1) | Higher mat roll + accessory chance |

### Tier Scaling

| Tier | Adjustments |
|------|-------------|
| **1–3** | 1 Bud Node per shrine event; no elites in Room 4 |
| **4–6** | Elites appear in Room 3 purge wave and Room 4 wave 2 |
| **7–10** | Tighter veil cadence in Room 5; extra Null Caster in Room 1 |

---

## 7. UI Text (Exact Prompts)

### Null Shrine Interaction
```
┌─────────────────────────┐
│      NULL SHRINE        │
├─────────────────────────┤
│ Cleanse the corruption  │
│ and endure the purge    │
│ wave.                   │
│                         │
│  [CLEANSE]  [CANCEL]    │
└─────────────────────────┘
```

### Post-Cleanse Toasts
```
"NULL SIGIL ACQUIRED (1/2)."
"NULL SIGIL ACQUIRED (2/2)."
"ROOTWAY UNSEALED."
```

### Wing Completion
```
"VAULT SIGIL ACQUIRED."
"RETURN PORTAL OPENED."
```

---

## 8. Navigation Flowchart

```
┌─────────────────────────────────────────────────────────────────┐
│                    CATACOMB ENTRY (Room 0)                      │
│                         [Safe Zone]                             │
└─────────────────────────────┬───────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│                  VEILROOT SPINE (Room 1)                        │
│          [Veil Curtains + Split Path + Small Fight]             │
└─────────────┬───────────────────────────────┬───────────────────┘
              │                               │
              ▼                               ▼
┌─────────────────────────┐       ┌───────────────────────────────┐
│  NULL SHRINE A (Room 2) │       │    NULL SHRINE B (Room 3)     │
│  ["Undercroft Reliquary"]│      │    ["Veilroot Chapel"]        │
│                         │       │                               │
│  • Cleanse Font (28,46) │       │  • Cleanse Font (68,46)       │
│  • Bud Node: (18,38)    │       │  • Bud Nodes: (78,38) (90,38) │
│  • Chest A: (28,30)     │       │  • Chest B Gate: (92,34)      │
│                         │       │                               │
│  → NULL SIGIL A         │       │    ┌─────────────────────┐    │
│    "(1/2)"              │       │    │ ROOT-KNOT CACHE     │    │
└───────────┬─────────────┘       │    │ (Room 3.1)          │    │
            │                     │    │ [Optional Chest B]  │    │
            │                     │    └─────────────────────┘    │
            │                     └───────────────┬───────────────┘
            │                                     │
            └─────────────────┬───────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│           WARDEN ANTECHAMBER (Room 4) — "Sealed Rootway"        │
│         [Stabilizer #1 + Veil + Bud Node + 2-Wave Fight]        │
│                                                                 │
│  • Bud Node at (48,28) in Wave 2                                │
│  • Door unlocks after both Null Sigils                          │
│  • Toast: "ROOTWAY UNSEALED."                                   │
└─────────────────────────────┬───────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────────┐
│            WARDEN ARENA (Room 5) — "Catacomb Heart"             │
│    [Stabilizer #2 + Veilroot Curator + Capstone Hazards]        │
│                                                                 │
│  • Veilroot Curator at (48,12)                                  │
│  • Bud caps: 2 alive max                                        │
│  • Bud spawns: (38,10) start, (58,10) at 60% HP                │
│  → VAULT SIGIL at (48,10) → Return to Entry                     │
└─────────────────────────────────────────────────────────────────┘
```

---

## 9. Coordinate Quick Reference

### Entry & Hub
```
Entry Spawn: (48, 60)          Wing Sign: (48, 56)
Return Portal: (48, 58)        To Spine: (48, 53)
```

### Room 1 — Veilroot Spine
```
West Door: (20, 47)            East Door: (76, 47)
North Door: (48, 39) [locked until shrines purified]
```

### Room 2 — Null Shrine A (Undercroft Reliquary)
```
Shrine A: (12, 34)             Cleansing Font: (28, 46)
Bud Node: (18, 38)             Chest A: (28, 30)
To Spine: (20, 47)
```

### Room 3 — Null Shrine B (Veilroot Chapel)
```
Shrine B: (84, 34)             Cleansing Font: (68, 46)
Bud Nodes: (78, 38) (90, 38)
Chest Gate: (92, 34)           To Spine: (76, 47)
```

### Room 3.1 — Root-Knot Cache (28×20)
```
Chest B (local): (24, 4)
```

### Room 4 — Warden Antechamber
```
Stabilizer #1: (24, 28)        Bud Node: (48, 28) [Wave 2]
North Door: (48, 17)           To Warden Arena
```

### Room 5 — Catacomb Heart
```
Warden: (48, 12)               Vault Sigil: (48, 10)
Stabilizer #2: (28, 12)
Bud Spawns: (38, 10) [start], (58, 10) [60% HP]
```

---

## 10. Implementation Notes

- **Shrine order**: A and B can be done in any order; both required to unlock Room 4 north door
- **Door lock logic**: Check for `NULL_SIGIL_A` and `NULL_SIGIL_B` in inventory; unlock + toast when both present
- **Bud Node behavior**: Track 10s bloom timer; if not killed → apply regen/damage buff to all enemies in room
- **Pollen Spark pickup**: Cleanses priority: Veil Sickness → Wound → Null Mark-lite
- **Cleansing Font**: 20s cooldown per font; step-triggered cleanse
- **Bloom Punish**: Only triggers if Bud Node reaches bloom state during Warden fight; casts Null Lanes as immediate response
- **Purge Wave timing**: 0s and 6s spawns; 12s total duration
- **Tier scaling**: Enemy additions and hazard frequency adjustments based on selected Vault Tier at hub
- **Micro-submap loading**: Room 3.1 loads as separate 28×20 instance; door at (92, 34) triggers transition
