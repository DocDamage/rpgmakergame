# Chroma's Edge — Aurora Ascension Tower: Hundredfold Vestibule (Lobby) Map Sheet (v1)
## Tower Access Hub — "The Tower Was Never Built to Be Climbed. It Was Built to Be Tested."

---

## 0) Technical Specs

| Parameter | Value |
|-----------|-------|
| **Lobby Name** | Hundredfold Vestibule ("Aurora Lobby") |
| **Role** | Tower access hub (start/resume runs), rewards delivery, vendor + evolution station, tower rules/tutorial, optional Eclipse modifiers |
| **Unlock Condition** | `RELIC_SHADOW_SEATED = TRUE` (post-D8) |
| **Recommended Level** | 100+ |
| **Map Size** | 128 × 96 tiles (2048 × 1536 px) |
| **Encounters** | 0% (safe zone) |
| **Time States** | Day/Night (cosmetic only) |
| **Mounts** | Allowed but auto-dismount inside lobby ring (tight + ceremonial) |
| **Save** | YES (Lobby Save Terminal) |
| **Fast Travel** | Terminal supports "Return to last Tower Save Floor" if any |

---

## 1) Visual Identity (Art Direction)

| Element | Description |
|---------|-------------|
| **Materials** | Polished obsidian stone, aurora glass panels, gold-inlaid floor rings, floating sigils |
| **Lighting** | Soft cyan + violet "eclipse pulse" that cycles every ~8 seconds |

### Signature Setpieces

| Prop | Description |
|------|-------------|
| **The Lift Core** | Center: circular elevator ring descending into tower |
| **Hundred Marks Wall** | 100 engraved slots, only some lit at start |
| **Aurora Relay Console** | Tower UI terminal |
| **Trophy Alcoves** | Boss emblems appear after defeats |

---

## 2) Layout Blocks (Districts)

### District 1 — Entry Hall

| Property | Value |
|----------|-------|
| **Bounds** | x 48–80, y 76–96 |
| **Features** | Arrival from overworld; big signage + tutorial plaque |

### District 2 — Lift Core Ring (Main Hub)

| Property | Value |
|----------|-------|
| **Bounds** | x 36–92, y 32–76 |
| **Features** | Central circular platform with elevator and main interactables |

### District 3 — Service Arcade (Vendors + Stations)

| Property | Value |
|----------|-------|
| **Bounds** | x 0–36, y 32–72 |
| **Features** | Vendor booth, exchange, repair/tuning, storage |

### District 4 — Records Arcade (Lore + Milestones)

| Property | Value |
|----------|-------|
| **Bounds** | x 92–128, y 32–72 |
| **Features** | Hundred Marks Wall, boss trophies, leaderboard/clear log |

### District 5 — Modifier Nook (Optional Challenge Mode)

| Property | Value |
|----------|-------|
| **Bounds** | x 44–84, y 0–32 |
| **Features** | "Eclipse Protocol" panel: toggles for harder modifiers |

---

## 3) Entrances / Exits (Edge Triggers)

Local coords (0–127, 0–95)

| Exit To | Coordinates | Notes |
|---------|-------------|-------|
| **From Overworld / Eclipse Confluence** | (64, 95) | South edge |
| **Back to Overworld** | (64, 95) | Bidirectional |
| **Tower Entry (Floor 1)** | (64, 54) | "Descend" trigger at Lift Core |
| **Resume Entry (last save floor)** | (64, 50) | Only if `TOWER_LAST_SAVE_FLOOR > 0` |

---

## 4) Key Anchors & Coordinates

### Central Interactables (Lift Core Ring)

| Feature | Coordinates | Function |
|---------|-------------|----------|
| **Lift Core Console** (Start/Resume) | (64, 52) | DESCEND / RESUME / EXIT |
| **Hundred Marks Wall** (milestones) | (108, 52) | Progress visualization |
| **Boss Trophy Pedestals** | (104, 44) to (120, 44) | Defeated boss emblems |
| **Lobby Save Terminal** | (64, 70) | Standard save + briefing |

### Services (Service Arcade)

| Feature | Coordinates | Function |
|---------|-------------|----------|
| **Ascension Cache** (Vendor) | door (18, 54) | Consumables, prep items |
| **Hundredfold Exchange** (Token Shop) | door (18, 42) | Token → mat conversion |
| **Aurora Crucible** (Summon Evolution) | (26, 62) | Evolve summons |
| **Relic Tuner** (Gear Tune Bench) | (26, 34) | Adjust relic loadouts |
| **Stash Chest / Storage** | (10, 62) | Item storage |

### Optional Challenge (Modifier Nook)

| Feature | Coordinates | Function |
|---------|-------------|----------|
| **Eclipse Protocol Panel** | (64, 18) | Toggle difficulty modifiers |
| **Modifier Preview Plaque** | (58, 22) | Explain modifiers |

---

## 5) Core Interactions

### A) Lift Core Console (Start / Resume / Exit)

**Location:** (64, 52)

| Option | Availability | Effect |
|--------|--------------|--------|
| **DESCEND (Floor 1)** | Always (once unlocked) | Begin new run at Floor 1 |
| **RESUME** | If `TOWER_LAST_SAVE_FLOOR > 0` | Jump to Floor 20/40/60/80/100 |
| **EXIT TOWER** | Always | Return to overworld |

**Rule Enforcement:**
- Saving only at Floors 20/40/60/80/100
- Lobby shows last save floor and allows resume

### B) Lobby Save Terminal

**Location:** (64, 70)

| Function | Description |
|----------|-------------|
| Standard save | — |
| Tower briefing | Rules text |
| Clear logs viewer | Optional statistics |

### C) Hundred Marks Wall (Progress Visualization)

**Location:** (108, 52)

| Display | Unlock Condition |
|---------|------------------|
| Boss sigils | Defeat F10/25/50/75/90/100 bosses |
| Terminal sigils | Reach F20/40/60/80/100 saves |
| Best floor reached | Track highest floor |
| Fastest segment times | Optional speedrun tracking |

### D) Eclipse Protocol Panel (Optional Difficulty Modifiers)

**Location:** (64, 18)

**Toggle one modifier at a time:**

| Modifier | Effect | Reward Bonus |
|----------|--------|--------------|
| **+Elite Density** | More elite spawns | +Tokens, +gear tier chance |
| **Hazard Intensified** | Foundation hazards stronger | +Tokens, +gear tier chance |
| **No Items** | Challenge run (no consumables) | Major token multiplier |
| **Timer Mode** | Rank/score tracking | Leaderboard entry |

---

## 6) Interiors (Recommended)

### 1) Ascension Cache (Vendor Interior)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 26 × 16 |
| **Function** | High-tier consumables, anti-status prep, (post-F50) Tier-5 mats |

### 2) Hundredfold Exchange (Token Shop)

| Parameter | Value |
|-----------|-------|
| **Interior Size** | 24 × 14 |
| **Function** | Token → mat conversion; Summon Evolution items (expensive, limited) |

**Note:** Summon Evolution Station can be on-map altar rather than interior.

---

## 7) Economy / Shop Setup (Non-Brickable)

### Vendor: Ascension Cache

#### Base (Immediately Post-D8)

| Item | Type |
|------|------|
| High Potion / High Ether bundles | Consumables |
| Smoke Bomb / Escape items | — |
| Seal-Breaker Wax, Clockseal, Umbral Ward | Tower prep staples |
| 1 rotating "rare mat pack" per visit | Mats |

#### After Floor 50 Unlocked

| Addition | Notes |
|----------|-------|
| Tier-5 mats | Paradox Glass / Crown Alloy Plates / Seal Wax equivalents (small quantities) |
| "Captain Lure" items | Optional: force captain door spawn on next stratum |

### Exchange: Tower Tokens

| Exchange | Rate |
|----------|------|
| Token → Mat | Fixed rates (anti-RNG) |
| Token → Summon Evolution items | Only after clearing relevant milestone floors |

---

## 8) NPCs (Minimal, Functional)

| NPC | Location | Function |
|-----|----------|----------|
| **Tower Steward ("The Attendant")** | (68, 74) | Explains rules, milestones, modifiers |
| **Quartermaster** | Vendor interior | Shopkeeper |
| **Archivist Echo** | (110, 58) | Lore + boss trophy commentary (post-kill unlock lines) |

**Atmosphere:** No crowd. Controlled facility.

---

## 9) Tutorial / Messaging

### On First Entry

> "A 100-floor ascent has been authorized."
> 
> "Save terminals exist every 20 floors."
> 
> "Defeat restores you to the last save terminal."

### On First Time Opening Lift

> "Choose: Descend or Resume."
> 
> "Milestone rewards: 10/20/50/100."

---

## 10) Gating Logic + Flags

### Unlock / Entry

| Requirement | Effect |
|-------------|--------|
| `RELIC_SHADOW_SEATED = TRUE` | Enables lobby access node on overworld |
| Optional | Require other seated foundations for strict alignment |

### Resume Logic

| Value | Effect |
|-------|--------|
| `TOWER_LAST_SAVE_FLOOR ∈ {0,20,40,60,80,100}` | Track progress |
| If 0 | "Resume" hidden/disabled |

### Tracking Flags

| Flag | Purpose |
|------|---------|
| `TOWER_LOBBY_DISCOVERED` | First entry |
| `TOWER_UNLOCKED` | Access granted |
| `TOWER_LAST_SAVE_FLOOR` | Resume point |
| `TOWER_MODIFIER_ACTIVE` | NONE or modifier ID |
| `TOWER_BOSS_10_DEFEATED` etc. | Boss kill tracking |

---

## 11) Secrets / Flavor

| Secret | Coordinates | Conditions | Reward |
|--------|-------------|------------|--------|
| **Hidden plaque** | (12, 30) | Night only | "The tower was never built to be climbed. It was built to be tested." |
| **One-time cache** | (8, 72) | Once | Prep bundle: Clockseal + High Ether |
| **Pet sniff spot** | (96, 70) | Post-tame | "Aurora Resin" (rare craft mat) |

---

## Quick Reference Map Overview

```
                        NORTH
                          ↑
    ┌───────────────────────────────────────────────────────────┐
    │                                                           │
    │    DISTRICT 5: Modifier Nook                              │
    │    (x 44–84, y 0–32)                                      │
    │    - Eclipse Protocol Panel (64,18)                       │
    │    - Modifier Preview Plaque (58,22)                      │
    │                                                           │
    │    ═══════════════════════════════════════════            │
    │                      │                                    │
    │    ══════════════════╪══════════════════════              │
    │                      │                                    │
    │    DISTRICT 3: Service Arcade      DISTRICT 2:            │
    │    (x 0–36, y 32–72)             Lift Core Ring           │
    │    - Vendor door (18,54)         (x 36–92, y 32–76)       │
    │    - Exchange door (18,42)       ┌─────────────┐          │
    │    - Evolution (26,62)           │  LIFT CORE  │          │
    │    - Tuner (26,34)               │             │          │
    │    - Storage (10,62)             │ Console     │          │
    │                                    │ (64,52)     │          │
    │    ═══════════════════════════     │ DESCEND     │          │
    │                      │             │ RESUME      │          │
    │    ══════════════════╪════════════ │ EXIT        │          │
    │                      │             └─────────────┘          │
    │    DISTRICT 4: Records Arcade    Save Terminal (64,70)    │
    │    (x 92–128, y 32–72)           ├─ Lobby Beacon           │
    │    - Hundred Marks Wall (108,52) ├─ Briefing               │
    │    - Trophy Pedestals (104–120,44)└─ Clear Logs            │
    │    - Archivist Echo (110,58)                              │
    │                                                           │
    │    ═══════════════════════════════════════════            │
    │                      │                                    │
    │    DISTRICT 1: Entry Hall                                 │
    │    (x 48–80, y 76–96)                                     │
    │    - Arrival (64,95) from Overworld                       │
    │    - Tutorial signage                                     │
    │    - Steward NPC (68,74)                                  │
    │                                                           │
    │    Hidden Plaque [night]: (12,30)                         │
    │    One-time Cache: (8,72)                                 │
    │    Pet Sniff: (96,70)                                     │
    │                                                           │
    └───────────────────────────────────────────────────────────┘
```

**Key Anchors Summary:**

| Feature | Coordinates |
|---------|-------------|
| **Overworld Entry** | (64, 95) |
| **Lift Core Console** | (64, 52) |
| **Descend Trigger** | (64, 54) |
| **Resume Trigger** | (64, 50) |
| **Lobby Save Terminal** | (64, 70) |
| **Hundred Marks Wall** | (108, 52) |
| **Trophy Pedestals** | (104, 44) to (120, 44) |
| **Vendor Door** | (18, 54) |
| **Exchange Door** | (18, 42) |
| **Evolution Station** | (26, 62) |
| **Relic Tuner** | (26, 34) |
| **Storage Chest** | (10, 62) |
| **Eclipse Protocol Panel** | (64, 18) |
| **Modifier Preview** | (58, 22) |
| **Steward NPC** | (68, 74) |
| **Archivist Echo** | (110, 58) |
| **Hidden Plaque** [night] | (12, 30) |
| **One-time Cache** | (8, 72) |
| **Pet Sniff Spot** | (96, 70) |
