# Chroma's Edge — Aurora Ascension Tower (The Hundredfold) Master Sheet (v1)
## 100-Floor Endgame Tower — "Test of Mastery"

---

## 0) Technical Specs

| Parameter | Value |
|-----------|-------|
| **Tower Name** | Aurora Ascension Tower ("The Hundredfold") |
| **Type** | 100-Floor Endgame Challenge Dungeon |
| **Entry Requirement** | Defeat Void Nexus (D8) — `D8_CLEARED = TRUE` |
| **Recommended Entry Level** | Lv 100+ |
| **Average Floor Time** | 5–10 minutes per floor |
| **Total Estimated Clear Time** | 8–16 hours (can be completed across sessions) |

---

## 1) Core Systems

### Save / Respawn

| Feature | Implementation |
|---------|----------------|
| **Save Terminals** | Floors 20, 40, 60, 80, 100 |
| **Exit + Re-enter** | Resume at last save floor |
| **Death** | Respawn at last save terminal (no progress loss) |
| **Abandon Run** | Can exit at any terminal; resume later |

### Reward Cadence

| Milestone | Reward |
|-----------|--------|
| **Every Floor Clear** | 50,000–200,000 Duckets + 1–3 rare materials |
| **Every 10 Floors** | 1 Rare equipment piece (Tier 4–5) |
| **Every 20 Floors** | 1 Legendary equipment + 1 Summon Evolution item |
| **Floor 50** | Ultimate weapon (random character) |
| **Floor 100** | Best-in-slot Legendary weapon (pick 1 of 12) |

### Tower Token System (Anti-Brick)

| Source | Amount |
|--------|--------|
| **Each clear chest** | 1–3 Tower Tokens |
| **Terminal exchange** | Tokens → Paradox Glass / Crown Alloy Plates / Seal Wax / Summon evolution items |

---

## 2) Enemy Scaling Brackets

| Floors | Level Range | Theme |
|--------|-------------|-------|
| **1–20** | Lv 100–120 | Heat (enforcement/firepower) |
| **21–40** | Lv 120–145 | Tide (pressure, currents) |
| **41–60** | Lv 145–170 | Growth (living architecture) |
| **61–80** | Lv 170–200 | Light/Motion/Mass (varied) |
| **81–90** | Lv 200–230 | Shadow/Composite (mixed mechanics) |
| **91–100** | Lv 230+ | Eclipse (clean arenas, brutal consistency) |

---

## 3) Tower Structure — 10 Strata

Instead of 100 unique floors, build **10 strata** (10 floors each) with **5 reusable floor templates** + authored **setpiece floors**.

### Strata Themes (8 Foundations + Endgame Warp)

| Stratum | Floors | Theme | Foundation |
|---------|--------|-------|------------|
| **1** | 1–10 | Heat | Firepower, enforcement vibe |
| **2** | 11–20 | Tide | Pressure, currents, drowning corridors |
| **3** | 21–30 | Growth | Living architecture, regen enemies |
| **4** | 31–40 | Light | Visibility tricks, refraction hazards |
| **5** | 41–50 | Motion | Initiative/turn order, conveyor tiles |
| **6** | 51–60 | Mass | Gravity wells, knockback lanes |
| **7** | 61–70 | Time | Phase locks, rewind tiles |
| **8** | 71–80 | Shadow | Seen/Unseen lanes, veil pockets |
| **9** | 81–90 | Composite Warp | Mixed mechanics, elite density up |
| **10** | 91–100 | Eclipse | Clean arenas, brutal consistency, final test |

---

## 4) Floor Types (Build Kit)

Each floor rolls as one of these, weighted by stratum:

| Type | Description | Weight |
|------|-------------|--------|
| **Clear Floor** | Standard pathing + fights | 40% |
| **Key Floor** | 3 switches/keys unlock exit | 20% |
| **Trial Floor** | 2 scripted waves, no randoms | 15% |
| **Hazard Floor** | Foundation hazard is the "puzzle" | 15% |
| **Arena Floor** | Single elite pack or miniboss room | 10% |

### Set Floors (Authored)

| Floor | Type | Notes |
|-------|------|-------|
| **10, 25, 50, 75, 90, 100** | Major Boss | Fixed encounters |
| **20, 40, 60, 80, 100** | Save Terminal | Sanctuary layout |

---

## 5) Map Template Kit (Reusable)

### Template A — "Ring + 2 Spokes"

| Property | Value |
|----------|-------|
| **Size** | 72 × 72 tiles |
| **Layout** | Loop path with 2 gates |
| **Best For** | Key Floors |

### Template B — "Spine Corridor"

| Property | Value |
|----------|-------|
| **Size** | 88 × 56 tiles |
| **Layout** | Straight-ish run |
| **Best For** | Speed climbing floors |

### Template C — "Four Rooms"

| Property | Value |
|----------|-------|
| **Size** | 64 × 64 tiles |
| **Layout** | Each room has lever/elite; center hub |
| **Best For** | Trial Floors |

### Template D — "Zig-Zag Switchbacks"

| Property | Value |
|----------|-------|
| **Size** | 96 × 64 tiles |
| **Layout** | Angled corridors |
| **Best For** | Hazard placement, ambush setups |

### Template E — "Arena + Prep Hall"

| Property | Value |
|----------|-------|
| **Size** | 56 × 56 tiles |
| **Layout** | Small arena with prep area |
| **Best For** | Captain Challenge rooms |

### Special Templates

| Template | Use |
|----------|-----|
| **Boss Arena** | Custom arenas for F10/25/50/75/90/100 |
| **Sanctuary** | Fixed terminal floors (F20/40/60/80/100) |

---

## 6) Boss Floors (Major Encounters)

### Floor 10 — Commander Dax Kaine

| Property | Value |
|----------|-------|
| **Identity** | Dominion Vanguard |
| **Visual** | Dual plasma cannons, heavy armor |
| **Mechanics** | Plasma Sweep beam telegraphs, Coolant Valve system, Armor Break pressure |
| **Phase Count** | 3 |
| **Arena Size** | 72×56 tiles |
| **Key System** | 4 cover pillars, 2 coolant valves (disable vents), optional pressure plate |
| **Document** | [Floor 10 Boss Arena Sheet](chroma_edge_tower_floor_10_boss_arena_dax_kaine.md) |

### Floor 25 — Dr. Yakov Thorne

| Property | Value |
|----------|-------|
| **Identity** | Growth Lieutenant |
| **Mechanics** | Absorb mechanic (pod imprisonment), Purge Pylon regen reduction, add control |
| **Passive** | Cultivator's Renewal (10% HP/turn regen, reduced by Purge Pylons) |
| **Arena Size** | 80×64 tiles |
| **Phase 3** | Absorb every 3 turns + Mitosis Command (doubles adds) |
| **Document** | [Floor 25 Boss Arena Sheet](chroma_edge_tower_floor_25_boss_arena_yakov_thorne.md) |

### Floor 50 — High Cultist Mercer

| Property | Value |
|----------|-------|
| **Identity** | Pre-Triumvirate Cult Leader |
| **Mechanics** | Foundation Roulette (1→2→3 active), 8 Obelisk Counterfields, illusion copies |
| **Arena Size** | 88×72 tiles |
| **Key System** | Ritual Dial shows active Foundations; Truth Glint reveals real Mercer |
| **Reward** | Ultimate weapon (random character) |
| **Story** | Triumvirate confrontation begins after |
| **Document** | [Floor 50 Boss Arena Sheet](chroma_edge_tower_floor_50_boss_arena_mercer.md) |

### Floor 75 — The Sentinel

| Property | Value |
|----------|-------|
| **Identity** | Apex Construct (Pattern-Learning Judge) |
| **Mechanics** | Adaptation Meter (tracks last 6 actions), Counter Protocols, Desync burst windows |
| **Arena Size** | 96×72 tiles |
| **Key System** | 4 Pattern Nodes (remove counters), 2 Disruption Consoles (freeze meter, +25% damage) |
| **Category Tracking** | Strike/Burst/AOE/Heal/Buff/Debuff/Control (3× = Counter Protocol) |
| **Document** | [Floor 75 Boss Arena Sheet](chroma_edge_tower_floor_75_boss_arena_sentinel.md) |

### Floor 90 — The Void Architect

| Property | Value |
|----------|-------|
| **Identity** | Apex Shadow Construct ("Blueprint of Nothing") |
| **Mechanics** | Auto-Dispersion (buff strip), INTANGIBLE phases (PHASE Blueprint), PINNED windows |
| **Arena Size** | 96×80 tiles |
| **Key System** | 4 Seam Stabilizers (end intangibility), 2 Null Fountains (cleanse + dispel dampening) |
| **Blueprints** | RIFT (pull/void seams) → ERASURE (buff strip wave) → PHASE (intangibility) |
| **Document** | [Floor 90 Boss Arena Sheet](chroma_edge_tower_floor_90_boss_arena_void_architect.md) |

### Floor 100 — Alexander

| Property | Value |
|----------|-------|
| **Identity** | Summon Trial ("The Final Accord") |
| **Mechanics** | 4 Accord Trials (VALOR/WISDOM/RESOLVE/BALANCE), Eclipse Verdict signature attack |
| **Arena Size** | 112×88 tiles |
| **Key System** | 4 Accord Obelisks (create Accord Fields), 8 Prism Mirrors (beam routing) |
| **Trial States** | Valor (beams) → Wisdom (illusions) → Resolve (endurance) → Balance (anti-spam) |
| **Reward** | Best-in-slot Legendary weapon (pick 1 of 12 characters) |
| **Unlock** | Alexander summon + optional rematch mode |
| **Document** | [Floor 100 Boss Arena Sheet](chroma_edge_tower_floor_100_boss_arena_alexander.md) |

---

## 7) Tower Captains (Optional Challenge Doors)

**Skip-able side rooms** using Template E. Spawn on specific floors.

### Captain Door Floors

| Floor | Captain | Theme |
|-------|---------|-------|
| **15** | Warden Pyre-Lieut. Ressa Vane | Heat |
| **35** | Prism Adjudicator Cael Rorr | Light |
| **55** | Gravemaster Bront Kessel | Mass |
| **65** | Chrono Surveyor Venn Holt | Time |
| **85** | Echelon Custodian "Null-Scribe" | Composite |
| **95** | Seam Warden Prime | Eclipse |

### Captain Details

| Captain | Floor | Key Mechanic | Drop | Document |
|---------|-------|--------------|------|----------|
| **Ressa Vane** | 15 | Ignition stacks (0-10), Overheat at 6+, heal punishes via Audit Blast, Coolant Valves | Tier 5 mats + bonus gear | [F15 Arena](chroma_edge_tower_captain_f15_ressa_vane.md) |
| **Cael Rorr** | 35 | Refraction clones (2→3), Misjudgment penalty, Prism Beacons reveal true target | Tier 5 mats + bonus gear | [F35 Arena](chroma_edge_tower_captain_f35_cael_rorr.md) |
| **Bront Kessel** | 55 | HEAVY stacks (CRUSH-PRONE at 6), Gravity Wells, Mass Anchors, Inertia Punish anti-turtle | Tier 5 mats + bonus gear | [F55 Arena](chroma_edge_tower_captain_f55_bront_kessel.md) |
| **Venn Holt** | 65 | TIME DEBT (REWIND AUDIT at 8), Time-Lock Fields, Survey Marks anti-camp | Tier 5 mats + bonus gear | [F65 Arena](chroma_edge_tower_captain_f65_venn_holt.md) |
| **Null-Scribe** | 85 | Rotating Edicts (Renewal→Null→Wounds), Edict Consoles, Redaction Seal hero play | Tier 5 mats + bonus gear | [F85 Arena](chroma_edge_tower_captain_f85_null_scribe.md) |
| **Seam Warden Prime** | 95 | Seam Integrity (COLLAPSE at 6 cracks), Reality Clamp, Core Clamp Plate hero play | Premium amplifier mats + Seam Warden Seal | [F95 Arena](chroma_edge_tower_captain_f95_seam_warden_prime.md) |

**Total Named Fights:** 6 Captains + 6 Major Bosses = **12 named encounters**

---

## 8) Terminal Floor Layout (F20/40/60/80/100)

### Fixed "Sanctuary" Map — No Combat

| Feature | Function |
|---------|----------|
| **Save Terminal** | Save progress |
| **Vendor** | Tier 5 mats appear after Floor 50 |
| **Relic Tuning Station** | Adjust relic loadouts |
| **Summon Evolution Station** | Evolve summons |
| **Continue/Exit Selector** | Choose to push on or return later |
| **Reward Chest** | Equipment drop for clearing last 10 floors |

### Sanctuary Visual

| Element | Description |
|---------|-------------|
| **Materials** | White marble, gold accents, soft ambient light |
| **Atmosphere** | Calm, safe, "breather" space |
| **Music** | Tranquil, contrasting with tower intensity |

---

## 9) Reward Scaling by Floor Bracket

### Clear Chest Payout (Guaranteed)

| Floors | Duckets | Rare Mat Rolls | Notes |
|--------|---------|----------------|-------|
| **1–20** | 50k–80k | 1 | Heat/Tide mats |
| **21–40** | 80k–110k | 2 | Tide/Growth mats |
| **41–60** | 110k–140k | 2 | Growth/Light/Motion mats |
| **61–80** | 140k–170k | 3 | Motion/Mass/Time mats |
| **81–100** | 170k–200k | 3 | Time/Shadow/Eclipse mats |

### Equipment Drops

| Milestone | Drop Type | Tier |
|-----------|-----------|------|
| **Every 10 floors** | Rare equipment | Tier 4–5 |
| **Every 20 floors** | Legendary equipment | Tier 5 + Summon Evolution item |
| **Floor 50** | Ultimate weapon | Character-specific random |
| **Floor 100** | Best-in-slot Legendary | Pick 1 of 12 characters |

### Anti-Brick Guarantees

| Rule | Implementation |
|------|----------------|
| **Every 10th floor** | Includes at least 1 Tier-5 material bundle |
| **Tower Tokens** | 1–3 per clear chest; exchangeable for specific mats at terminals |
| **No zero-progress floors** | Every floor gives something meaningful |

---

## 10) Quick Reference: Floor Overview

```
AURORA ASCENSION TOWER (100 FLOORS)

STRATUM 1 (Floors 1–10): HEAT
├─ F1–9: Random templates (Clear/Key/Trial/Hazard/Arena)
├─ F10: BOSS — Commander Dax Kaine
└─ Theme: Firepower, enforcement

STRATUM 2 (Floors 11–20): TIDE
├─ F11–19: Random templates
├─ F15: CAPTAIN — Ressa Vane (optional)
├─ F20: SAVE TERMINAL + Sanctuary
└─ Theme: Pressure, drowning corridors

STRATUM 3 (Floors 21–30): GROWTH
├─ F21–29: Random templates
├─ F25: BOSS — Dr. Yakov Thorne
└─ Theme: Living architecture, regen

STRATUM 4 (Floors 31–40): LIGHT
├─ F31–39: Random templates
├─ F35: CAPTAIN — Cael Rorr (optional)
├─ F40: SAVE TERMINAL + Sanctuary
└─ Theme: Visibility, refraction

STRATUM 5 (Floors 41–50): MOTION
├─ F41–49: Random templates
├─ F50: BOSS — High Cultist Mercer
│   └─ REWARD: Ultimate weapon (random)
└─ Theme: Turn order, conveyors

STRATUM 6 (Floors 51–60): MASS
├─ F51–59: Random templates
├─ F55: CAPTAIN — Bront Kessel (optional)
├─ F60: SAVE TERMINAL + Sanctuary
│   └─ Vendor now sells Tier 5 mats
└─ Theme: Gravity wells, knockback

STRATUM 7 (Floors 61–70): TIME
├─ F61–69: Random templates
├─ F65: CAPTAIN — Venn Holt (optional)
├─ F70: SAVE TERMINAL + Sanctuary
└─ Theme: Phase locks, rewind tiles

STRATUM 8 (Floors 71–80): SHADOW
├─ F71–79: Random templates
├─ F75: BOSS — The Sentinel
├─ F80: SAVE TERMINAL + Sanctuary
└─ Theme: Seen/Unseen, veil

STRATUM 9 (Floors 81–90): COMPOSITE WARP
├─ F81–89: Random templates (mixed mechanics)
├─ F85: CAPTAIN — Null-Scribe (optional)
├─ F90: BOSS — The Void Architect
└─ Theme: Elite density up, mixed hazards

STRATUM 10 (Floors 91–100): ECLIPSE
├─ F91–99: Random templates (clean arenas)
├─ F95: CAPTAIN — Seam Warden Prime (optional)
├─ F100: SAVE TERMINAL + BOSS — Alexander
│   └─ REWARD: Best-in-slot Legendary (pick 1 of 12)
│   └─ UNLOCK: Summon battle mode
└─ Theme: Brutal consistency, mastery test

TOTAL NAMED ENCOUNTERS:
├─ 6 Major Bosses (F10, 25, 50, 75, 90, 100)
├─ 6 Optional Captains (F15, 35, 55, 65, 85, 95)
└─ 12 Total named fights

SAVE POINTS: F20, 40, 60, 80, 100
ESTIMATED CLEAR TIME: 8–16 hours (resumable)
```

---

## Implementation Priority

### Phase 1 (Core Loop)
- [x] 5 floor templates (A–E)
- [x] Sanctuary template
- [x] Boss arena templates (6)
- [x] Stratum tileset variants (10)
- [x] Save/respawn system
- [x] Reward cadence system

### Phase 2 (Content)
- [x] 6 Boss encounters scripted
- [x] 6 Captain encounters scripted
- [x] Terminal vendor inventories
- [x] Tower Token exchange rates

### Phase 3 (Polish)
- [x] Stratum atmosphere audio
- [x] Boss intro cinematics
- [x] Floor clear VFX
- [ ] Leaderboards (optional)
