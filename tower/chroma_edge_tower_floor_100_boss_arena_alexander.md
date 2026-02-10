# Chroma's Edge — Aurora Ascension Tower: Floor 100 Boss Arena Sheet (v1)
## Alexander — Summon Trial ("The Final Accord")

---

## 0) Technical Specs

| Parameter | Value |
|-----------|-------|
| **Boss** | Alexander |
| **Identity** | Summon Trial — "The Final Accord" |
| **Stratum** | 91–100 (Eclipse) |
| **Recommended Level** | 200–230 |
| **Arena Goal** | True final exam: pattern mastery + resource discipline + mechanic execution, but always telegraphed and counterable |
| **Arena Size** | 112 × 88 tiles (1792 × 1408 px) |
| **Type** | Boss arena + prep hall + reward/selection sanctum |
| **Encounters** | OFF (boss only) |
| **Mounts** | Disabled |
| **Save** | Floor 100 terminal appears POST-clear |
| **Retry Point** | Floor 80 terminal |

---

## 1) Layout Overview

### 1) Prep Hall (Final Warning + Ready Check)

| Property | Value |
|----------|-------|
| **Bounds** | x 0–112, y 76–88 |
| **Features** | Safe pad + "Final Trial" plaque + one optional 1-time prep crate (high-tier consumables only) |

### 2) Main Arena (Accord Basin)

| Property | Value |
|----------|-------|
| **Bounds** | x 10–102, y 12–76 |
| **Layout** | Circular arena with 4 Accord Obelisks, 2 Sanctuary Fonts, 8 Prism Mirrors, Central Sigil |

### 3) Reward Sanctum (Weapon Selection + Summon Unlock + Terminal)

| Property | Value |
|----------|-------|
| **Bounds** | x 28–84, y 0–12 |
| **Features** | 12 weapon pedestals (pick 1), summon contract node, Floor 100 save terminal, clear banner |

---

## 2) Anchors & Coordinates (Local 0–111, 0–87)

### Entry / Lock

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Entry spawn** | (56, 84) | — |
| **Arena threshold** | y = 76 | Crossing to y≤75 locks doors |
| **Door lock trigger** | (56, 75) | — |

### Boss Spawn

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Alexander spawn** | (56, 44) | Center |

### Central Indicator / Optional Override

| Feature | Coordinates | Function |
|---------|-------------|----------|
| **Central Accord Sigil** | (56, 52) | Shows active trial state(s) |

### Accord Obelisks (4) — "Solve It" Tools

*Each obelisk corresponds to a trial condition; using the right one prevents wipes.*

| Obelisk | Coordinates | Trial |
|---------|-------------|-------|
| **Obelisk N (VALOR)** | (56, 18) | Line of Fire |
| **Obelisk E (WISDOM)** | (92, 44) | True Pattern |
| **Obelisk S (RESOLVE)** | (56, 70) | Endurance Oath |
| **Obelisk W (BALANCE)** | (20, 44) | The Accord Demands Variety |

### Sanctuary Fonts (2)

| Font | Coordinates |
|------|-------------|
| **Font L** | (40, 34) |
| **Font R** | (72, 34) |

### Prism Mirrors (8) — Beam Blockers / Reflectors (2×2 collision)

| Mirror | Coordinates |
|--------|-------------|
| **NW1** | (30, 26) |
| **NW2** | (42, 22) |
| **NE1** | (70, 22) |
| **NE2** | (82, 26) |
| **SW1** | (30, 62) |
| **SW2** | (42, 66) |
| **SE1** | (70, 66) |
| **SE2** | (82, 62) |

### Post-fight Sanctum

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Weapon Pedestal Ring (12)** | Center (56, 6) | See Section K |
| **Summon Contract Node** | (36, 6) | Unlock Alexander summon |
| **Floor 100 Save Terminal** | (76, 6) | Post-clear save |
| **Lift / Clear Exit Tile** | (56, 1) | Returns to Lobby + "Cleared" state |

---

## 3) Arena Systems

### A) Accord Cycle (Alexander's "Trial States")

| State | Icon | Effect |
|-------|------|--------|
| **VALOR** | Crossed swords | Movement + survive beams |
| **WISDOM** | Eye | Identify real pattern / dispel-proof windows |
| **RESOLVE** | Shield | Heal check + endurance |
| **BALANCE** | Scales | Don't spam; rotate actions |

*Shown clearly on Central Sigil. Rotation: every 2 turns (P1–2), faster (P3).*

### B) Accord Obelisks (Primary Counterplay)

| Property | Value |
|----------|-------|
| **Interact time** | 1.0s |
| **Effect** | 12-second Accord Field: -60–75% state hazard severity, applies HARMONIZED (+damage taken or buff loss on boss) |
| **Cooldown** | 28 seconds per obelisk |
| **Limit** | Only one Accord Field active at a time |

### C) Sanctuary Fonts (Anti-Brick, Limited)

| Property | Value |
|----------|-------|
| **Effect** | Cleanse 1 major debuff (priority: Marked > Turn Delay > Null Mark > Eclipse Burn) |
| **Secondary** | 8s Sanctuary: max 1 buff removed/turn, small beam damage reduction |
| **Cooldown** | 24 seconds per font |
| **Total uses** | 3 times per font maximum |

### D) Prism Mirrors (Beam Routing)

| Property | Description |
|----------|-------------|
| **Function** | Block and redirect certain beam attacks, creating safe lanes |
| **Durability** | Do not fully break; can "overheat" cosmetically |

---

## 4) Boss Kit — Alexander

### Passive: Imperial Dispersion

| Condition | Effect |
|-----------|--------|
| **Normal** | Start of Alexander's turn: removes 1 buff from each party member |
| **HARMONIZED** | 50% chance instead |

### Passive: Summon's Authority

| Trigger | Effect |
|---------|--------|
| **Spam same action category** | Authority Stack (damage up + faster cycle) |
| **Reduction** | BALANCE Obelisk field clears up to 2 stacks, pauses gain |

---

## 5) Trial State Mechanics

### VALOR — "Line of Fire"

| Property | Description |
|----------|-------------|
| **Hazard** | Accord Beams sweep 2–3 lanes (heavy telegraph lines) |
| **Mirror-safe** | Mirrors create dead zones if positioned right |
| **Fail pressure** | Standing in lane = Marked + big damage |
| **Counter** | VALOR Obelisk widens safe windows, reduces Marked severity |

### WISDOM — "True Pattern"

| Property | Description |
|----------|-------------|
| **Mechanic** | Spawns 3 illusions + 1 real Alexander |
| **Tell** | Real Alexander charges "sigil tone" (audio cue + hand glow) |
| **Pressure** | Erasure Pulse (buff strip wave) unless HARMONIZED |
| **Counter** | WISDOM Obelisk suppresses illusions faster, weakens Erasure Pulse |

### RESOLVE — "Endurance Oath"

| Property | Description |
|----------|-------------|
| **Effect** | Steady chip + periodic "Judgment Slam" AOEs |
| **Check** | If party HP ends below threshold, Alexander gains Authority |
| **Counter** | RESOLVE Obelisk reduces chip, removes HP threshold check for 12s |

### BALANCE — "The Accord Demands Variety"

| Property | Description |
|----------|-------------|
| **Tracking** | Last 6 party actions (categories) |
| **Trigger** | Same category 3× = Authority Stack |
| **Risk** | High Authority = Tempo Break (turn delay) |
| **Counter** | BALANCE Obelisk clears 2 Authority Stacks, pauses Authority gain |

---

## 6) Phase Script (HP-Based)

### Phase 1 (100% → 70%) — "Proclamation"

| Aspect | Description |
|--------|-------------|
| **States** | One trial state at a time |
| **Rotation** | Every 2 turns |
| **Illusions** | Minimal (WISDOM = 2 copies) |

#### Moves

| Move | Trial |
|------|-------|
| **Accord Beam** | Valor |
| **Erasure Pulse** | Wisdom |
| **Judgment Slam** | Resolve |
| **Tempo Break** | Balance |

### Phase 2 (70% → 35%) — "Edict"

| Aspect | Description |
|--------|-------------|
| **States** | One at a time, hazards intensify |
| **Illusions** | WISDOM increases to 3 copies |
| **New mechanic** | Eclipse Ring (slow closing ring once per phase, telegraphed) |
| **Reward** | Correct obelisk applies HARMONIZED longer |

### Phase 3 (35% → 0%) — "Final Accord"

| Aspect | Description |
|--------|-------------|
| **Rotation** | Faster (every 1–2 turns) |
| **Eclipse Verdict** | Every 4 turns: two trial hazards at once for one turn (telegraphed dual icons) |
| **Fonts** | Critical (but limited uses) |
| **Enrage** (≤12%) | Rotation locks to BALANCE + VALOR alternating |

---

## 7) Signature Attack (Telegraphed Wipe… With a Solve)

### ECLIPSE VERDICT (Phase 3 Setpiece)

| Property | Description |
|----------|-------------|
| **Telegraph** | Central Sigil pulses black-white 2 times, then locks |
| **Effect** | Massive arena-wide strike + Marked + Turn Delay |
| **Counter** | Party inside active Accord Field OR behind mirror-safe line |
| **Intent** | "You learned the tower" moment — not a coin flip |

---

## 8) Optional Interaction: Central Accord Sigil "Override"

| Property | Value |
|----------|-------|
| **Location** | (56, 52) |
| **Channel time** | 2.0s (while HARMONIZED) |
| **Effect** | Freeze current trial state for 1 extra turn |
| **Cooldown** | 40s |
| **Risk** | Central position is dangerous |

*Note: Optional high-skill play. Obelisks + fonts already support fairness.*

---

## 9) Fight Scripting (Sequence)

| Step | Event |
|------|-------|
| 1 | Cross threshold → doors lock |
| 2 | Alexander: "You have climbed. Now prove you deserve the summit." |
| 3 | Central Sigil displays first trial state (icon + audio sting) |
| 4 | Phase transitions at 70% and 35% (brief VFX) |
| 5 | On defeat: hazards stop, reward sanctum unlocks |
| 6 | Summon contract node activates, weapon pedestals light up |

---

## 10) Rewards (Floor 100 Milestone)

### 1) Best-in-Slot Legendary Weapon (Pick 1 of 12)

In Reward Sanctum: 12 weapon pedestals (one per "final" weapon choice).

| Layout | Description |
|--------|-------------|
| **Pedestals** | 6 on top arc, 6 on bottom arc around (56, 6) |
| **Selection** | Interact → preview stats → confirm |
| **Lockout** | After selection, others dim and lock |

### 2) Summon Unlock

| Feature | Details |
|---------|---------|
| **Location** | Summon Contract Node (36, 6) |
| **Message** | "Alexander has entered your pact." |
| **Unlock** | `SUMMON_ALEXANDER_UNLOCKED = TRUE` |
| **Bonus** | Optional: "Summon battle" rematch mode in Tower Lobby |

### 3) Clear Chest Add-ons

| Reward | Amount |
|--------|--------|
| **Tower Tokens** | +60 |
| **Duckets** | +200,000 |
| **Rare Mats** | 6 rolls from Eclipse pool (highest tier) |
| **Optional** | Legendary accessory OR summon evolution item |

---

## 11) Flags

| Flag | Condition |
|------|-----------|
| `TOWER_F100_CLEARED` | TRUE |
| `TOWER_BOSS_100_DEFEATED` | TRUE |
| `TOWER_TOWER_CLEARED` | TRUE |
| `TOWER_LAST_SAVE_FLOOR` | 100 (set after terminal use) |
| `BEST_IN_SLOT_WEAPON_SELECTED` | TRUE |
| `SUMMON_ALEXANDER_UNLOCKED` | TRUE |

---

## 12) Post-clear: Floor 100 Terminal + Victory Routing

| Feature | Location | Function |
|---------|----------|----------|
| **Save Terminal** | (76, 6) | Saves clear state + logs reward choice |
| **Exit Tile** | (56, 1) | Returns to Tower Lobby with "Cleared" banner + NG+ modifiers |

---

## 13) Implementation Notes (Epic But Fair)

| Note | Priority |
|------|----------|
| Trial icons huge and distinct; audio cues matter | Critical |
| Dispel feels like payoff: HARMONIZED windows are the reward | Critical |
| Sanctuary Fonts limited-use prevents cheese, avoids RNG brick | High |
| Eclipse Verdict solvable via Accord Field OR mirror-safe line | Critical |

---

## Quick Reference: Arena at a Glance

```
    NORTH (y=0, Reward Sanctum)
       ↑
    ┌───────────────────────────────────────────────────────────────┐
    │  Reward Sanctum (y 0–12)                                      │
    │  - 12 Weapon Pedestals (ring around 56,6)                     │
    │  - Summon Contract Node (36,6)                                │
    │  - Save Terminal (76,6)                                       │
    │  - Exit Tile (56,1)                                           │
    └───────────────────────────────────────────────────────────────┘
                      │
    ══════════════════╪══════════════════════════════════════════════
                      │
    ┌───────────────────────────────────────────────────────────────┐
    │  Main Arena (y 12–76) — Accord Basin                          │
    │                                                               │
    │  NW1     NW2              NE2     NE1                         │
    │ (30,26)  (42,22)          (82,26) (70,22)                     │
    │    │        │              │        │                         │
    │  SW1     Mirror    N     Mirror    SE1                        │
    │ (30,62)  (22)   (56,18)   (22)    (70,66)                     │
    │              ╲    │    ╱                                      │
    │    W ──────── SIGIL (56,52) ──────── E                        │
    │  (20,44)      │    │    │      (92,44)                        │
    │    (Obelisk)  │    │    │      (Obelisk)                      │
    │              ALEXANDER                                        │
    │              (56,44)                                          │
    │                                                               │
    │  SW2     Mirror    S     Mirror    SE2                        │
    │ (42,66)  (22)   (56,70)   (22)    (82,62)                     │
    │              ╱    │    ╲                                      │
    │              Font L  Font R                                   │
    │            (40,34)  (72,34)                                   │
    │                                                               │
    └───────────────────────────────────────────────────────────────┘
                      │
    ══════════════════╪══════════════════════════════════════════════ (y=76)
                      │
    ┌───────────────────────────────────────────────────────────────┐
    │  Prep Hall (y 76–88)                                          │
    │  - Entry spawn (56,84)                                        │
    │  - Lock trigger (56,75)                                       │
    │  - "Final Trial" plaque                                       │
    └───────────────────────────────────────────────────────────────┘
                      │
                   SOUTH (y=87, Entry)

ACCORD TRIALS:
┌───────────┬─────────────────────────────────────────┐
│ VALOR     │ Beams, movement, mirror-safe lanes     │
│ WISDOM    │ 3 illusions, audio tell, Erasure Pulse │
│ RESOLVE   │ Chip + Judgment Slam, heal check       │
│ BALANCE   │ Spam tracking, Authority Stacks        │
└───────────┴─────────────────────────────────────────┘

PHASE PROGRESSION:
P1 (100–70%): Proclamation — 1 trial at a time, every 2 turns
P2 (70–35%): Edict — intensified hazards, Eclipse Ring, 3 copies
P3 (35–0%): Final Accord — fast rotation, Eclipse Verdict (dual trials)
              Enrage: BALANCE + VALOR alternating

ECLIPSE VERDICT:
- Telegraph: Sigil pulses black-white 2×, locks
- Effect: Arena-wide strike + Marked + Turn Delay
- Counter: Accord Field active OR mirror-safe line

LIMITED RESOURCES:
- Sanctuary Fonts: 3 uses each (24s cooldown)
- Accord Obelisks: 28s cooldown (independent)
- Only 1 Accord Field active at once
```
