# Chroma's Edge — Aurora Ascension Tower: Floor 75 Boss Arena Sheet (v1)
## The Sentinel — Apex Construct (Pattern-Learning Judge)

---

## 0) Technical Specs

| Parameter | Value |
|-----------|-------|
| **Boss** | The Sentinel |
| **Identity** | Apex Construct — Pattern-Learning Judge |
| **Stratum** | 71–80 (Shadow/Time-adjacent endgame bracket) |
| **Recommended Level** | 170–200 |
| **Arena Goal** | "Stop spamming." Rewards adaptation management, smart rotations, and using arena tools to create burst windows |
| **Arena Size** | 96 × 72 tiles (1536 × 1152 px) |
| **Type** | Boss arena + prep hall + reward alcove |
| **Encounters** | OFF (boss only) |
| **Mounts** | Disabled |
| **Retry Point** | Floor 60 terminal (next save at Floor 80) |

---

## 1) Layout Overview

### 1) Prep Hall

| Property | Value |
|----------|-------|
| **Bounds** | x 0–96, y 60–72 |
| **Features** | Safe pad + "adaptive threat" warning plaque + optional 1-time prep crate |

### 2) Main Arena (Judgment Circuit)

| Property | Value |
|----------|-------|
| **Bounds** | x 8–88, y 12–60 |
| **Layout** | Octagonal floor with central dais, 4 Pattern Nodes, 2 Disruption Consoles, 4 Cover Monoliths, Perimeter Scan Lanes |

### 3) Reward Alcove

| Property | Value |
|----------|-------|
| **Bounds** | x 34–62, y 0–12 |
| **Features** | Boss chest + lift tile to Floor 76 |

---

## 2) Anchors & Coordinates (Local 0–95, 0–71)

### Entry / Lock

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Entry spawn** | (48, 68) | — |
| **Arena threshold** | y = 60 | Crossing to y≤59 locks doors |
| **Door lock trigger** | (48, 59) | — |

### Boss Spawn

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Sentinel spawn** | (48, 34) | Center |

### Cover Monoliths (Line-Blockers; 3×3 collision)

| Monolith | Coordinates |
|----------|-------------|
| **Monolith NW** | (26, 26) |
| **Monolith NE** | (70, 26) |
| **Monolith SW** | (26, 46) |
| **Monolith SE** | (70, 46) |

### Pattern Nodes (Adaptation Control)

*Interactables that store/vent "pattern data" — used to prevent immunity stacking.*

| Node | Coordinates |
|------|-------------|
| **Node A** | (48, 16) |
| **Node B** | (16, 34) |
| **Node C** | (80, 34) |
| **Node D** | (48, 56) |

### Disruption Consoles (Vulnerability Windows)

| Console | Coordinates | Effect |
|---------|-------------|--------|
| **Console Left** | (32, 34) | Initiate Desync |
| **Console Right** | (64, 34) | Initiate Desync |

### Perimeter Scan Lanes (Hazard Bands)

| Lane | Bounds |
|------|--------|
| **North band** | y 14–18 |
| **South band** | y 54–58 |
| **West band** | x 14–18 |
| **East band** | x 78–82 |

### Post-fight

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Reward chest** | (48, 6) | — |
| **Lift tile to Floor 76** | (48, 2) | — |

---

## 3) Arena Systems

### A) Adaptation Meter (Sentinel Learns You)

| Aspect | Description |
|--------|-------------|
| **Tracking** | Last 6 actions (categories, not exact skills) |
| **Categories** | Strike / Burst / AOE / Heal / Buff / Debuff / Control |

#### Penalty Rule (Anti-Spam)

| Condition | Effect |
|-----------|--------|
| **Same category 3× in last 6 actions** | Counter Protocol vs that category for 12 seconds |
| **Examples** | Strike spam → +evasion + retaliatory parry; Heal spam → Mend Tax (reduced healing) |
| **Hard cap** | Max 2 Counter Protocols at once |

### B) Pattern Nodes (Safety Valve)

| Property | Value |
|----------|-------|
| **Interact time** | 1.0s |
| **Effect** | Removes one active Counter Protocol OR prevents next one |
| **Cooldown** | 20 seconds per node (independent) |

### C) Disruption Consoles (Damage Window)

| Property | Value |
|----------|-------|
| **Interact time** | 1.5s (risky) |
| **Effect** | Applies DESYNC to Sentinel for 10s: +25% damage taken, freezes Adaptation Meter |
| **Cooldown** | 30 seconds |
| **Requirement** | At least 2 Pattern Nodes charged OR Sentinel above 25% HP |

---

## 4) Hazards (Telegraphed, Not Cheap)

### Perimeter Scan Sweep

| Property | Value |
|----------|-------|
| **Frequency** | Every 12–16 seconds |
| **Pattern** | One perimeter band activates, sweeps inward 4 tiles |
| **Telegraph** | Band lights + audio "scan tone" |
| **Effect** | Chip damage + "Marked" (ambush chance / accuracy down) |
| **Counter** | Hide behind monoliths or stand in dead zone opposite active band |

### Null Squares (Late-Phase)

| Property | Value |
|----------|-------|
| **Phase** | Phase 2+ |
| **Count** | 2–4 tiles become "null" for 6 seconds |
| **Telegraph** | Tiles invert color (black glass) |
| **Effect** | End turn on them = small stun/turn delay |

---

## 5) Boss Kit — The Sentinel

### Passive: Adaptive Carapace

| Property | Description |
|----------|-------------|
| **Effect** | Gains Counter Protocols via Adaptation Meter rules |
| **DESYNC interaction** | Adaptive Carapace suppressed during Desync |

### Passive: Behavior Mirror

| Property | Description |
|----------|-------------|
| **Effect** | Apply same debuff twice in a row → Sentinel reflects weaker version back (telegraphed) |

---

## 6) Phases (HP-Based)

### Phase 1 (100% → 70%) — "Assessment"

| Aspect | Description |
|--------|-------------|
| **Meter** | Active, but Counter Protocols mild |
| **Arena** | Perimeter Scan Sweep starts (slow) |

#### Moves

| Move | Description |
|------|-------------|
| **Judgment Beam** | Straight line, blocked by monoliths |
| **Vector Step** | Short dash; leaves small "afterline" hazard |
| **Protocol Ping** | Marks one target; encourages swapping positions |

**Lesson:** Rotate action categories; use Pattern Nodes only if triggered.

### Phase 2 (70% → 35%) — "Correction"

| Aspect | Description |
|--------|-------------|
| **Counters** | Stronger; Sentinel "reads" healing/buff patterns |
| **Arena** | Scan Sweep faster; Null Squares introduced |

#### New Moves

| Move | Description |
|------|-------------|
| **Punitive Parry** | If Strike-counter active: retaliates |
| **Mend Tax** | If Heal-counter active: reduces healing received |
| **Field Partition** | Spawns 2 Null Squares |

**Lesson:** Use Pattern Nodes proactively + time Desync window to burn phase.

### Phase 3 (35% → 0%) — "Verdict"

| Aspect | Description |
|--------|-------------|
| **Counters** | Can hold 2 at once (reaches cap faster) |
| **Arena** | Scan Sweep + Null Squares can overlap (telegraphed) |

#### New Moves

| Move | Description |
|------|-------------|
| **Verdict Array** | Two intersecting beams; monolith dance |
| **Audit Lock** | Temporarily disables ONE random Pattern Node for 10s (telegraphed with red seal icon) |
| **Final Measure** (≤15%) | Short enrage: faster scans, but longer Desync vulnerability |

**Lesson:** Maintain rhythm: dump counter → trigger Desync → burst → reposition.

---

## 7) Fight Scripting (Sequence)

| Step | Event |
|------|-------|
| 1 | Cross threshold → doors lock |
| 2 | Sentinel "wakes" (no speech; clean boot-up tone) |
| 3 | UI/tutorial pop (first time only): "The Sentinel adapts to repeated actions." |
| 4 | Phase shifts at 70% and 35% (VFX pulse + meter beep) |
| 5 | On defeat: hazards stop, nodes go dark, reward alcove unlocks |

---

## 8) Rewards (Floor 75 Milestone)

| Reward | Details |
|--------|---------|
| **Tier 5 Rare Equipment** | 1 piece, high-quality roll |
| **Unique Component** | Sentinel Core (craft mat for "Anti-Adapt" gear line) |
| **Tower Tokens** | +28 |
| **Duckets** | +160,000–190,000 |
| **Rare Mats** | 4 rolls from Eclipse/Construct pool |

### Bonus Challenge

| Condition | Bonus |
|-----------|-------|
| Defeat without triggering more than 2 Counter Protocols total | +12 tokens OR 1 extra Tier-5 gear roll |

---

## 9) Flags

| Flag | Condition |
|------|-----------|
| `TOWER_F75_CLEARED` | TRUE |
| `TOWER_BOSS_75_DEFEATED` | TRUE |
| `TOWER_LAST_REACHED_FLOOR` | 75 |

---

## 10) Failure / Retry Behavior

| Condition | Result |
|-----------|--------|
| **Wipe** | Resume at Floor 60 terminal (or Tower Lobby → Resume Floor 60) |
| **Intro/tutorial** | Skippable after first attempt |

---

## 11) Implementation Notes (Hard But Fair)

| Note | Priority |
|------|----------|
| Counter Protocols visible (icons + label like "STRIKE COUNTER") | Critical |
| Adaptation Meter tracks categories, not specific skills | Critical |
| Pattern Nodes impossible to miss (big glow, audible hum) | High |
| Never disable both Disruption Consoles at once | High |

---

## Quick Reference: Arena at a Glance

```
    NORTH (y=0, Reward Alcove)
       ↑
    ┌─────────────────────────────────────────────────────┐
    │  Reward Alcove (y 0–12)                             │
    │  - Chest (48,6)                                     │
    │  - Lift to F76 (48,2)                               │
    └─────────────────────────────────────────────────────┘
                      │
    ══════════════════╪════════════════════════════════════
                      │
    ┌─────────────────────────────────────────────────────┐
    │  Main Arena (y 12–60) — Judgment Circuit            │
    │                                                     │
    │         Perimeter Scan: North (y 14–18)             │
    │              ↓                                      │
    │              Node A (48,16)                         │
    │                   │                                 │
    │  West       Monolith NE ─┐   ┌─ Monolith NW       │
    │  (x14–18)   (70,26)      │   │      (26,26)       │
    │  ↓                       │   │                      │
    │  Node B (16,34)          │   │        Node C (80,34)│
    │       │                  │   │             │        │
    │  Console L ───────────── SENTINEL ───────── Console R│
    │       (32,34)          (48,34)           (64,34)   │
    │       │                  │   │             │        │
    │       │              Monolith SW  Monolith SE      │
    │       │               (26,46)     (70,46)          │
    │       │                  │   │                      │
    │  West Scan ↑             │   │        ↑ East Scan  │
    │            │             │   │                      │
    │            │        Node D (48,56)                  │
    │            │             │                          │
    │  Perimeter Scan: South (y 54–58) ←───────────────┘
    │                                                     │
    └─────────────────────────────────────────────────────┘
                      │
    ══════════════════╪════════════════════════════════════ (y=60)
                      │
    ┌─────────────────────────────────────────────────────┐
    │  Prep Hall (y 60–72)                                │
    │  - Entry spawn (48,68)                              │
    │  - Lock trigger (48,59)                             │
    └─────────────────────────────────────────────────────┘
                      │
                   SOUTH (y=71, Entry)

PHASE SUMMARY:
P1 (100–70%): Assessment — mild counters, learn rotation
P2 (70–35%): Correction — strong counters, Null Squares, Desync timing
P3 (35–0%): Verdict — fast 2-counter cap, Verdict Array, Audit Lock

KEY MECHANICS:
- Adaptation Meter: 6-action memory, 3× same category = Counter Protocol
- Pattern Nodes: Remove active counter or prevent next (20s cd each)
- Disruption Console: 10s DESYNC (+25% damage, freeze meter)
- Perimeter Scan: Hide behind monoliths or stand in dead zone
- Counter Protocol hard cap: 2 at once
```
