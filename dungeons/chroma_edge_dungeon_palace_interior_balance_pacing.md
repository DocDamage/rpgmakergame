# Chroma's Edge — Palace Interior Encounter Pacing + Chest Placement (v1)
## Supplemental Balance Document for Palace Interior Dungeon

---

## Overall Pacing Targets

| Metric | Target |
|--------|--------|
| **Mandatory path battles** | ~18–26 |
| **100% sweep battles** | ~28–38 |
| **Resource arrival at boss (explore)** | ~60–80% |
| **Resource arrival at boss (rush)** | ~40–60% |

---

## Encounter Rate Tuning (Step-Based RNG)

| Map | Rate | Expected Battles |
|-----|------|------------------|
| **Map 1** | Very light (or OFF after tutorial) | ~0–2 |
| **Map 2** | Medium | ~8–12 |
| **Map 3** | None in center, light on edges | ~0–2 |
| **Map 4** | Heavy | ~10–14 + 2 fixed trials |
| **Map 5** | OFF | 0 |

---

## MAP 1 — HALL OF BANNERS (128×72)

### Intent
Tone + tutorial + don't burn player resources here.

### Encounter Pacing by Zone

| Zone | Bounds | Rate |
|------|--------|------|
| **Zone A (Entry)** | x 0–30 | OFF |
| **Zone B (Tutorial chamber)** | Around plinth/dial | 0–1 max (optional) |
| **Zone C (Run to gate)** | x 90–118 | 0–1 (only if lingering) |

### Enemy Mix (Lv 82–86)

| Enemy | % |
|-------|---|
| Audit Drones | 60% |
| Seal-Leeches | 30% |
| Chrono Wisps | 10% |

**No elites in Map 1.**

### Chests (2 Total)

| Chest | Coordinates | Contents |
|-------|-------------|----------|
| **M1-A** | (24, 60) | Stasis Balm ×2, Seal-Breaker Wax ×1 |
| **M1-B** | (96, 50) | High Ether ×1, Crown Alloy Shard ×1 (low-tier) |

---

## MAP 2 — LEDGER HALLS (160×112)

### Intent
The "meat." Fight enough to feel pressure, but exploration pays back via chests.

### Encounter Pacing by Segment

| Segment | Bounds | Rate |
|---------|--------|------|
| **Segment 1: Central Rotunda** | x 60–100, y 40–70 | Medium RNG |
| **Segment 2: Wing corridors** | — | Higher RNG (longer, puzzle-y) |
| **Segment 3: Seal rooms** | — | RNG OFF inside seal chambers |

### Fixed Fights

| Fight | Location | Waves |
|-------|----------|-------|
| **F2-A (Compliance Check)** | (78, 64) | 1 wave: 2× Audit Drone + 1× Seal-Leech |
| **F2-B (Truth Wing Gatekeeper)** | (92, 20) [QUESTION only] | 1 wave: 1× Redaction Auditor + 2× Chrono Wisp |

### Enemy Mix (Lv 84–92)

| Enemy | % |
|-------|---|
| Crownshard Sentinels | 35% |
| Seal-Leeches | 25% |
| Chrono Wisps | 20% |
| Audit Drones | 20% |

**Elite chance:** Low (night-only or post-story pressure)

### Chests (8 Total)

#### Central / Neutral

| Chest | Coordinates | Contents |
|-------|-------------|----------|
| **M2-A** | (70, 88) | High Potion ×2, Seal-Breaker Wax ×1 |
| **M2-B** | (92, 88) | Clockseal ×1, Crown Alloy Shard ×1 |

#### ACCESS Wing (OBEY + PRESENT)

| Chest | Coordinates | Contents |
|-------|-------------|----------|
| **M2-C** | (20, 72) | Pressure Patch ×2, Seal Wax Scrap ×1 |
| **M2-D** | (12, 92) [seal room corner] | Crown Alloy Plate ×1 (mid-tier) |

#### TRUTH Wing (QUESTION + PAST)

| Chest | Coordinates | Contents |
|-------|-------------|----------|
| **M2-E** | (114, 10) | Paradox Glass ×1, High Ether ×1 |
| **M2-F** | (104, 26) [PAST catwalk only] | Palimpsest Crownband Core (accessory mat) |

#### SILENCE Wing (NULL + FUTURE)

| Chest | Coordinates | Contents |
|-------|-------------|----------|
| **M2-G** | (148, 74) | Seal-Breaker Wax ×2, Clockseal ×1 |
| **M2-H** | (152, 96) [deepest corner] | Umbral Ward (minor) ×1 |

### Optional Repeatable Salvage Nodes

| Node | Coordinates | Respawn |
|------|-------------|---------|
| Seal Wax scrap pile | (66, 28) | Per rest (small) |
| Clocksteel filings | (138, 56) | Per rest (small) |

---

## MAP 3 — JUDGMENT ATRIUM (112×80)

### Intent
Safety. This is where players breathe.

### Encounter Pacing

| Zone | Rate |
|------|------|
| **Center ring** | OFF |
| **Outer edges** | 0–2 (very light, if roaming) |

### Enemy Mix (Lv 86–90)

Mostly Audit Drones and Seal-Leeches (no constructs).

### Chests (2 Total)

| Chest | Coordinates | Contents |
|-------|-------------|----------|
| **M3-A** | (14, 18) | High Potion ×2, High Ether ×1 |
| **M3-B** | (96, 18) | Crown Alloy Shard ×2, Seal Wax Scrap ×1 |

**Note:** If 2 Crown Lamps activated, reward via "Lamp Cache" popup (not extra chests).

---

## MAP 4 — THRONE ENGINE (176×112)

### Intent
The actual gauntlet. Don't be shy here. This is where you earn the boss.

### Encounter Pacing by Lane

| Lane | Bounds | Rate | Expected |
|------|--------|------|----------|
| **Lane 1: Entry Run** | x 70–106, y 6–34 | Medium RNG | 1–2 fights |
| **Lane 2: Rib Lanes** | x 60–116, y 20–66 | High RNG + hazards | 3–5 fights |
| **Lane 3: Decree Trials** | — | Fixed encounters | 2 mandatory |
| **Lane 4: Pre-boss** | x 70–106, y 46–70 | Medium RNG, then OFF | 1–2 fights |

### Fixed Trial Encounters (Mandatory)

#### Trial Gate A (64, 32)

| Wave | Enemies |
|------|---------|
| 1 | 2× Crownshard Sentinel + 1× Audit Drone |
| **Reward** | Seal-Breaker Wax ×1 (auto-drop) |

#### Trial Gate B (112, 54)

| Wave | Enemies |
|------|---------|
| 1 | 1× Redaction Auditor + 2× Seal-Leech |
| 2 | 1× Crownshard Sentinel + 2× Chrono Wisp |
| **Reward** | Clockseal ×1 + High Ether ×1 |

### Optional Miniboss (1-Time)

| Property | Value |
|----------|-------|
| **Name** | "Bastion Prefect Unit" (elite flagged) |
| **Location** | (96, 60) |
| **Spawn** | First time crossing rib lanes after both trials cleared |
| **Reward** | Crown Alloy Plate ×1 + Paradox Glass ×1 |

### Enemy Mix (Lv 90–99)

| Enemy | % |
|-------|---|
| Crownshard Sentinels | 35% |
| Redaction Auditors | 25% |
| Chrono Wisps | 20% |
| Seal-Leeches | 20% |

**Elite chance:** Medium at night

### Chests (5 Total)

| Chest | Coordinates | Contents |
|-------|-------------|----------|
| **M4-A** | (18, 20) | High Potion ×3 |
| **M4-B** | (152, 24) | Paradox Glass ×1, Seal Wax Scrap ×2 |
| **M4-C** | (26, 64) [rib lane side pocket] | Umbral Ward (minor) ×1 |
| **M4-D** | (160, 66) [harder pocket] | Crown Seal of Continuity (mat or full accessory) |
| **M4-E** | (88, 54) [antechamber] | High Ether ×2, Clockseal ×1 |

---

## MAP 5 — SPIRE ROOT ACCESS (112×72)

### Intent
Reward + unlock + exit. Zero combat.

### Chests (3 Total)

| Chest | Coordinates | Contents |
|-------|-------------|----------|
| **M5-A** | (22, 26) | Crown Alloy Plate ×1, Seal Wax Scrap ×2 |
| **M5-B** | (90, 22) | Paradox Glass ×1, High Ether ×1 |
| **M5-C** | (56, 56) [near lift] | Smoke Bomb ×2, High Potion ×1, Clockseal ×1 |

---

## Boss Map (Throne Engine) — Loot Sanity Check

### Player Entry State (Minimum)

| Resource | Target |
|----------|--------|
| High Potions | ~5–7 |
| High Ethers | ~4–6 |
| Anti-veil items | 3–5 (Wax/Clockseal/Umbral Ward) |

### Exploration Bonus

| Craft Materials | Enough For |
|-----------------|------------|
| Crown Alloy Plate + Paradox Glass + Seal Wax | One meaningful craft upgrade |

---

## Loot Totals Summary (Entire Dungeon)

| Category | Count/Amount |
|----------|--------------|
| **Total Chests** | 20 (2+8+2+5+3) |
| **Seal-Breaker Wax** | ~6–8 |
| **Clockseal** | ~4–6 |
| **Umbral Ward (minor)** | ~2–3 |
| **Crown Alloy Plates** | ~3–4 |
| **Paradox Glass** | ~3–4 |
| **Seal Wax Scrap** | ~5–8 |

---

## Quick Implementation Notes

### RNG Encounters OFF Inside:

- Each seal chamber (Map 2)
- Trial rooms (Map 4)
- Pre-boss antechamber (Map 4)

### Cleanse Pads (Tile-Based, Not Rooms)

| Location | Coordinates |
|----------|-------------|
| **Primary** | (88, 46) [Map 4] (already placed) |
| **Optional backup** | (96, 46) [Map 4] (if gauntlet feels too spiky) |

---

## Encounter Summary by Map

| Map | Battles (Mandatory) | Battles (100%) | Chests |
|-----|---------------------|----------------|--------|
| Map 1 | 0–2 | 0–2 | 2 |
| Map 2 | 8–12 | 10–14 | 8 |
| Map 3 | 0 | 0–2 | 2 |
| Map 4 | 10–14 | 12–16 | 5 |
| Map 5 | 0 | 0 | 3 |
| **TOTAL** | **18–28** | **22–34** | **20** |

---

## Chest Reference Quick-List

### Map 1 (Hall of Banners)
- M1-A: (24, 60) — Stasis Balm ×2, Wax ×1
- M1-B: (96, 50) — High Ether, Alloy Shard

### Map 2 (Ledger Halls)
- M2-A: (70, 88) — High Potion ×2, Wax ×1
- M2-B: (92, 88) — Clockseal, Alloy Shard
- M2-C: (20, 72) — Pressure Patch ×2, Wax Scrap
- M2-D: (12, 92) — Alloy Plate
- M2-E: (114, 10) — Paradox Glass, High Ether
- M2-F: (104, 26) — Crownband Core [PAST]
- M2-G: (148, 74) — Wax ×2, Clockseal
- M2-H: (152, 96) — Umbral Ward [deep corner]

### Map 3 (Judgment Atrium)
- M3-A: (14, 18) — High Potion ×2, High Ether
- M3-B: (96, 18) — Alloy Shard ×2, Wax Scrap

### Map 4 (Throne Engine)
- M4-A: (18, 20) — High Potion ×3
- M4-B: (152, 24) — Paradox Glass, Wax Scrap ×2
- M4-C: (26, 64) — Umbral Ward
- M4-D: (160, 66) — Crown Seal mat/accessory
- M4-E: (88, 54) — High Ether ×2, Clockseal

### Map 5 (Spire Root Access)
- M5-A: (22, 26) — Alloy Plate, Wax Scrap ×2
- M5-B: (90, 22) — Paradox Glass, High Ether
- M5-C: (56, 56) — Smoke Bomb ×2, High Potion, Clockseal
