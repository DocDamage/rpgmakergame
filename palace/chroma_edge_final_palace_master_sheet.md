# Chroma's Edge — Final Palace: The Progenitor Spire (v1)
## Apex Palace: Endgame Boss Gauntlet (5 Floors, 5 Bosses)

---

## 0) Technical Specs

| Parameter | Value |
|-----------|-------|
| **Dungeon Name** | Apex Palace: The Progenitor Spire |
| **Type** | Endgame boss-gauntlet |
| **Floors** | 5 (boss-only) |
| **Recommended Level** | 200–230 |
| **Role** | "True finale" dungeon after Tower / endgame routing |

### Entry Requirements

| Requirement | Flag |
|-------------|------|
| **Relic Shadow Seated** | `RELIC_SHADOW_SEATED = TRUE` |
| **Tower Floor 100 Defeated** | `TOWER_BOSS_100_DEFEATED = TRUE` |
| **Final Act Open** | `FINAL_ACT_OPEN = TRUE` |

---

## 1) Global Rules

| Feature | Implementation |
|---------|----------------|
| **Encounters** | OFF (boss-only floors) |
| **Healing** | Sanctuary Terminal after each boss |
| **Save Cadence** | Save at F1 start, then after each boss terminal (player choice) |
| **Retry Behavior** | Wipe → respawn at that floor's Sanctuary Terminal |
| **Map Size** | 96 × 72 tiles (F1-F3), 112 × 72 (F4), 128 × 88 (F5) |

---

## 2) Global Dungeon Mechanic: Crown Synchrony

| Aspect | Description |
|--------|-------------|
| **Meter** | UI bar measuring "how stable reality is" |
| **Builds** | When players eat avoidable hazards / fail floor mechanics |
| **Penalty** | High stacks: bosses gain minor speed/dispels |
| **Reset** | At each floor terminal (pressures execution, doesn't ruin runs) |

---

## 3) Overall Structure

Each floor follows this pattern:

```
[PREP HALL] → [BOSS ARENA] → [SANCTUARY TERMINAL] → [ELEVATOR TO NEXT FLOOR]
```

| Floor | Boss | Theme | Key Mechanic |
|-------|------|-------|--------------|
| **F1** | Elemental Lords | Elemental trial | 4-phase rotation, matching Element Altars |
| **F2** | Chronowarden Devourer | Time-stop predator | TIME DEBT meter, Chrono Anchors |
| **F3** | Void Empress | Buff-dispel check | WARD WINDOWS, Null Mark cleansing |
| **F4** | Ancient Gilded Drake | Flight/ground cycle | Break wings, gold farm mechanic |
| **F5** | The Progenitor Engine | True finale | 8 Foundation phases, 8 Conduits |

---

## 4) Floor 1 — Elemental Lords

### Technical

| Property | Value |
|----------|-------|
| **Map size** | 96 × 72 tiles |
| **Prep Hall** | y 60–72 |
| **Arena** | y 10–60 |
| **Post Terminal** | y 0–10 |

### Arena Anchors (Local 0–95, 0–71)

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Party spawn** | (48, 66) | — |
| **Boss center** | (48, 34) | — |
| **Flame Altar** | (48, 14) | Counter: Heat |
| **Tide Altar** | (78, 26) | Counter: Tide |
| **Stone/Growth Altar** | (18, 44) | Counter: Growth/Stone |
| **Storm/Light Altar** | (78, 44) | Counter: Light/Storm |
| **Cleanse Font** | (48, 52) | 20s cooldown |
| **Reward terminal** | (48, 6) | Post-clear |

### 4-Phase Script

| Phase | Element | Hazard | Counter |
|-------|---------|--------|---------|
| **P1** | Flame Lord | 2–3 burn lanes + Overheat stacks | Flame Altar: -70% Overheat, +damage |
| **P2** | Tide Lord | Drift + Pressure + "drown line" AOE | Tide Altar: cancels drift, -Pressure |
| **P3** | Stone/Growth Lord | Root binds + boss regen | Stone Altar: suppress regen, break binds |
| **P4** | Storm/Light Lord | Rotating safe wedge + blind | Storm Altar: expands safe zone, reveals |

**Transition Rule:** Each phase begins with 2-second telegraph (element icon stamp on floor).

### F1 Clear Reward

| Reward | Details |
|--------|---------|
| **Materials** | Legendary mat bundle |
| **Gear** | 1 high-tier gear roll |
| **Flag** | `FINAL_PALACE_F1_CLEARED = TRUE` |

---

## 5) Floor 2 — Chronowarden Devourer

### Theme
Movement and tempo denial; you must "re-anchor time."

### Technical

| Property | Value |
|----------|-------|
| **Map size** | 96 × 72 |
| **Core mechanic** | TIME DEBT meter (builds on stop/slow hits) |

### Arena Anchors

| Feature | Coordinates | Function |
|---------|-------------|----------|
| **Boss center** | (48, 34) | — |
| **Chrono Anchor N** | (48, 14) | Clears 2 TIME DEBT stacks |
| **Chrono Anchor W** | (18, 34) | Clears 2 TIME DEBT stacks |
| **Chrono Anchor E** | (78, 34) | Clears 2 TIME DEBT stacks |
| **Chrono Anchor S** | (48, 54) | Clears 2 TIME DEBT stacks |
| **Chrono Dial** | (48, 44) | Risk-reward override |
| **Sanctuary Fonts** | (30, 52), (66, 52) | Debuff relief |

### Mechanics

#### TIME DEBT

| Stacks | Effect |
|--------|--------|
| **3 stacks** | Minor turn delay |
| **6 stacks** | Time Stop Burst (telegraphed big hit) |

#### Chrono Anchors

| Property | Value |
|----------|-------|
| **Interact** | 1.0s |
| **Effect** | Clears 2 TIME DEBT stacks + creates 8s Haste bubble |
| **Cooldown** | 22s each |

#### Chrono Dial (Optional High Skill)

| Property | Value |
|----------|-------|
| **Channel** | 2.0s |
| **Effect** | Freezes boss's next "Stop" cast OR slows hazards for 10s |
| **Cooldown** | 35s |

### Boss Phases

| Phase | HP | Mechanics |
|-------|-----|-----------|
| **P1** | 100–70% | Slow fields + line beams |
| **P2** | 70–35% | "Rewind slam" + more stop zones |
| **P3** | 35–0% | "Time devour" pull + Debt ramps faster (anchors recharge faster) |

### F2 Clear Reward

| Reward | Details |
|--------|---------|
| **Materials** | Time-focused legendary mat |
| **Gear** | Accessory core |
| **Flag** | `FINAL_PALACE_F2_CLEARED = TRUE` |

---

## 6) Floor 3 — Void Empress

### Theme
She erases your setup; you must create protected windows.

### Technical

| Property | Value |
|----------|-------|
| **Map size** | 96 × 72 |
| **Core mechanic** | WARD WINDOWS (buff-protection fields) |

### Arena Anchors

| Feature | Coordinates | Function |
|---------|-------------|----------|
| **Boss center** | (48, 34) | — |
| **Ward Mirror N** | (48, 16) | Spawns Ward Field |
| **Ward Mirror W** | (20, 34) | Spawns Ward Field |
| **Ward Mirror E** | (76, 34) | Spawns Ward Field |
| **Ward Mirror S** | (48, 52) | Spawns Ward Field |
| **Null Fountain L** | (34, 48) | Cleanse debuffs |
| **Null Fountain R** | (62, 48) | Cleanse debuffs |
| **Cover Spires** | (28, 24), (68, 24), (28, 56), (68, 56) | Optional cover |

### Mechanics

#### Empress Passive: "Imperial Dispel"

| Condition | Effect |
|-----------|--------|
| **Normal** | Removes 1 buff/character per turn |
| **Null Crown window** | Stronger dispel rate |

#### Ward Mirrors

| Property | Value |
|----------|-------|
| **Interact** | 1.2s |
| **Effect** | WARD FIELD for 10s: buffs max 1 removal/turn, reduces Null Mark rate |
| **Cooldown** | 26s each |
| **Limit** | Only 1 Ward Field active at a time |

#### Null Fountains

| Property | Value |
|----------|-------|
| **Effect** | Cleanse Null Mark / Void Rot / Confounded |
| **Cooldown** | 20s |

### Boss Phases

| Phase | HP | Mechanics |
|-------|-----|-----------|
| **P1** | 100–70% | Dispel pulses + targeted Null Mark |
| **P2** | 70–35% | Summons void adds (cap) that explode into dispel waves |
| **P3** | 35–0% | "Crown of Silence" — disables fountains unless Ward Field active |

### F3 Clear Reward

| Reward | Details |
|--------|---------|
| **Materials** | Shadow/void legendary mat |
| **Gear** | Premium gear roll |
| **Flag** | `FINAL_PALACE_F3_CLEARED = TRUE` |

---

## 7) Floor 4 — Ancient Gilded Drake

### Theme
Break wings → force landing → punish greed. This floor is your intended gold farm.

### Technical

| Property | Value |
|----------|-------|
| **Map size** | 112 × 72 (wider for flight lanes) |
| **Replay** | Allow re-fight via terminal if desired |

### Arena Anchors

| Feature | Coordinates | Function |
|---------|-------------|----------|
| **Drake center (ground)** | (56, 34) | — |
| **Sky lanes** | Top half y 12–32 | Flight telegraphs |
| **Harpoon Ballista L** | (20, 52) | Apply Tether stacks |
| **Harpoon Ballista R** | (92, 52) | Apply Tether stacks |
| **Anchor Chain L** | (20, 20) | — |
| **Anchor Chain R** | (92, 20) | — |
| **Treasure Vent 1** | (56, 18) | Danger/reward zone |
| **Treasure Vent 2** | (56, 54) | Danger/reward zone |

### Mechanics

#### Flight/Ground Cycle

| State | Mechanic |
|-------|----------|
| **Airborne (start)** | Flight lane hazards, harder to hit |
| **Ballista use** | 1.4s interact, 18s cooldown, applies Tether stack |
| **3 Tether stacks** | Drake crashes to ground for 20s (DPS window) |

#### Gold Farm Hook

| Mechanic | Description |
|----------|-------------|
| **Gilded Scales** | Drake sheds 2–4 nodes during flight phase |
| **Pickup** | Interact to collect, risks flight lane damage |
| **Payout** | Convert to large Duckets bonus post-fight |

### Boss Phases

| Phase | HP | Mechanics |
|-------|-----|-----------|
| **P1** | 100–70% | Flight lanes + tail sweep on landing |
| **P2** | 70–35% | Fire/gold breath cone + stomp shockwaves |
| **P3** | 35–0% | "Greed Roar" — gold vents activate (standing = bonus scales but damage) |

### F4 Clear Reward

| Reward | Details |
|--------|---------|
| **Duckets** | Large payout |
| **Materials** | Legendary mat |
| **Gear** | Chance at "Gilded" accessory |
| **Flag** | `FINAL_PALACE_F4_CLEARED = TRUE` |

---

## 8) Floor 5 — The Progenitor Engine

### Theme
The source machine running the whole "edited world." Every phase is short, distinct, and solvable via arena counter tools.

### Technical

| Property | Value |
|----------|-------|
| **Map size** | 128 × 88 tiles (finale needs space) |
| **Core mechanic** | FOUNDATION CONDUITS (8 counterplay nodes) |
| **Checkpoint** | Optional Phase 4 intermission save (mercy option) |

### Arena Anchors

| Feature | Coordinates | Function |
|---------|-------------|----------|
| **Engine core** | (64, 44) | Boss position |
| **Heat Conduit** | (64, 14) | Counter: Heat phase |
| **Tide Conduit** | (92, 22) | Counter: Tide phase |
| **Growth Conduit** | (114, 44) | Counter: Growth phase |
| **Light Conduit** | (92, 66) | Counter: Light phase |
| **Motion Conduit** | (64, 74) | Counter: Motion phase |
| **Mass Conduit** | (36, 66) | Counter: Mass phase |
| **Time Conduit** | (14, 44) | Counter: Time phase |
| **Shadow Conduit** | (36, 22) | Counter: Shadow phase |
| **Sanctuary Fonts** | (48, 44), (80, 44) | 3 uses each, whole fight |
| **Cover Pylons** | (48, 28), (80, 28) | Beam breaks |

### Conduit Rules (Counterplay)

| Property | Value |
|----------|-------|
| **Interact** | 1.0s |
| **Effect** | Stabilization Field for 10s: -70% phase hazard, applies SYNCED (vulnerability) |
| **Cooldown** | 30s per conduit |
| **Limit** | Only 1 Stabilization Field active at a time |

### 8 Phases (Short, Punchy)

Each phase is ~12–20% HP (or timed segments). Telegraphed by huge icon + floor stamp.

| Phase | Foundation | Hazard |
|-------|------------|--------|
| **P1** | HEAT | Burn lanes + overheat stacks |
| **P2** | TIDE | Drift + pressure pulses |
| **P3** | GROWTH | Binds + regen nodes |
| **P4** | LIGHT | Prism safe wedge + reveal checks |
| **P5** | MOTION | Conveyor strips + initiative pressure |
| **P6** | MASS | Gravity wells + pull lanes |
| **P7** | TIME | Flicker tiles + turn delay threats |
| **P8** | SHADOW | Veil zones + echo copies + buff suppression |

### Finale Overlay: Eclipse Override (Last 10%)

| Aspect | Description |
|--------|-------------|
| **Effect** | Two hazards overlap at once (telegraphed) |
| **Skill reward** | Correct conduit use during Eclipse = longer SYNC window |

### Sanctuary Fonts (Anti-Brick)

| Property | Value |
|----------|-------|
| **Uses** | 3 per font (whole fight) |
| **Effect** | Cleanse major debuff + 8s dispel dampening |

### F5 Clear Rewards (Finale)

| Reward | Details |
|--------|---------|
| **Story** | Credits trigger |
| **Gear Choice** | Pick 1 of 12 BIS legendaries (or Engine Core crafts) |
| **Unlocks** | NG+, Eclipse modifiers, postgame hunts |

### Flags

| Flag | Condition |
|------|-----------|
| `FINAL_PALACE_CLEARED` | TRUE |
| `PROGENITOR_ENGINE_DEFEATED` | TRUE |

---

## 9) Transitions + UI Prompts

### Floor Entry

```
═══════════════════════════════════════
         FLOOR {n}: {BOSS NAME}
═══════════════════════════════════════
```

### Post-Clear Terminal

```
╔══════════════════════════════════════════════╗
║  SANCTUARY TERMINAL — SAVE / PREP / DESCEND  ║
╚══════════════════════════════════════════════╝
```

### Final Floor Warning

```
═══════════════════════════════════════
   THE PROGENITOR ENGINE AWAKENS.
═══════════════════════════════════════
```

---

## 10) Flag Summary

| Flag | Floor | Trigger |
|------|-------|---------|
| `FINAL_PALACE_F1_CLEARED` | 1 | Elemental Lords defeated |
| `FINAL_PALACE_F2_CLEARED` | 2 | Chronowarden Devourer defeated |
| `FINAL_PALACE_F3_CLEARED` | 3 | Void Empress defeated |
| `FINAL_PALACE_F4_CLEARED` | 4 | Ancient Gilded Drake defeated |
| `FINAL_PALACE_F5_CLEARED` | 5 | Progenitor Engine defeated |
| `FINAL_PALACE_CLEARED` | — | All floors cleared |
| `PROGENITOR_ENGINE_DEFEATED` | — | True finale complete |
| `NG_PLUS_UNLOCKED` | — | Post-clear unlock |

---

## 11) Quick Reference: Floor Overview

```
THE PROGENITOR SPIRE — 5 FLOOR GAUNTLET

F1: ELEMENTAL LORDS (4-Phase Rotation)
    ├─ Flame → Tide → Stone → Storm
    ├─ 4 Element Altars for counterplay
    └─ Teaching floor: match element to altar

F2: CHRONOWARDEN DEVOURER (Time Debt)
    ├─ TIME DEBT meter (max 6)
    ├─ 4 Chrono Anchors clear stacks
    └─ Chrono Dial for high-skill override

F3: VOID EMPRESS (Buff-Dispel)
    ├─ Ward Mirrors create buff-protection fields
    ├─ Null Fountains cleanse marks
    └─ Crown of Silence in P3 (fountains disabled without Ward)

F4: ANCIENT GILDED DRAKE (Gold Farm)
    ├─ Break wings with Ballistas (3 tethers)
    ├─ Collect Gilded Scales during flight
    └─ P3 "Greed Roar" for bonus rewards

F5: THE PROGENITOR ENGINE (8-Phase Finale)
    ├─ 8 Foundation phases in sequence
    ├─ 8 Conduits around arena rim
    ├─ Eclipse Override (last 10%): 2 hazards overlap
    └─ True ending trigger

GLOBAL MECHANICS:
• Crown Synchrony meter (anti-sloppy penalty)
• Sanctuary Terminals between floors
• NG+ unlock on F5 clear
```
