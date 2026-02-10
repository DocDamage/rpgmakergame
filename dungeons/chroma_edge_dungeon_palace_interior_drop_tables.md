# Chroma's Edge — Palace Interior Drop Tables (v1)
## Clean, Exact, Non-Brickable Drop System

---

## Drop Rules Overview

| Rule | Description |
|------|-------------|
| **Primary Roll** | Roll once on enemy's table (sums to 100%) |
| **Bonus Roll** | Roll once on enemy's bonus table (separate; can add extra mats) |
| **Elites** | Primary Roll ×2 (can win both) + Bonus Roll ×1 |
| **Boss** | Fixed drops (no RNG) |

---

## Base Drop Tables (Primary Roll)

### Audit Drone

| Result | % | Drop |
|--------|---|------|
| Seal Wax Scrap ×1 | 30% | — |
| Crown Alloy Shard ×1 | 10% | — |
| Paradox Glass ×1 | 2% | — |
| Nothing | 58% | — |
| **Bonus Roll** | 12% | Seal Wax Scrap ×1 |

### Seal-Leech

| Result | % | Drop |
|--------|---|------|
| Seal Wax Scrap ×1 | 40% | — |
| Seal Wax Scrap ×2 | 15% | — |
| Crown Alloy Shard ×1 | 8% | — |
| Paradox Glass ×1 | 1% | — |
| Nothing | 36% | — |
| **Bonus Roll** | 8% | Seal Wax Scrap ×1 |

### Chrono Wisp

| Result | % | Drop |
|--------|---|------|
| Paradox Glass ×1 | 18% | — |
| Seal Wax Scrap ×1 | 12% | — |
| Crown Alloy Shard ×1 | 8% | — |
| Nothing | 62% | — |
| **Bonus Roll** | 6% | Paradox Glass ×1 |

### Crownshard Sentinel

| Result | % | Drop |
|--------|---|------|
| Crown Alloy Shard ×1 | 28% | — |
| Crown Alloy Shard ×2 | 14% | — |
| Seal Wax Scrap ×1 | 10% | — |
| Paradox Glass ×1 | 3% | — |
| Crown Alloy Plate ×1 | 2% | — |
| Nothing | 43% | — |
| **Bonus Roll** | 10% | Crown Alloy Shard ×1 |

### Redaction Auditor

| Result | % | Drop |
|--------|---|------|
| Paradox Glass ×1 | 22% | — |
| Seal Wax Scrap ×1 | 18% | — |
| Crown Alloy Shard ×1 | 12% | — |
| Crown Alloy Plate ×1 | 4% | — |
| Nothing | 44% | — |
| **Bonus Roll** | 10% | Seal Wax Scrap ×1 |

### Bastion Prefect Unit (Elite)

| Guaranteed | Crown Alloy Plate ×1 |
|------------|----------------------|
| **Primary Roll** (×2 because Elite): | |
| Paradox Glass ×1 | 35% |
| Seal Wax Scrap ×2 | 35% |
| Crown Alloy Shard ×2 | 20% |
| Nothing | 10% |
| **Bonus Roll** | 25% | Seal Wax Scrap ×2 |

---

## Boss Fixed Drops (The Crown Protocol)

**No RNG — anti-brick anchor.**

| Drop | Amount |
|------|--------|
| Crown Alloy Plate | ×2 |
| Paradox Glass | ×2 |
| Seal Wax Scrap | ×4 |
| Paradox Glass (bonus) | 25% chance ×1 |

---

## Simple Modifiers (Optional)

### Map 4 (Throne Engine) "Forge-Heavy" Bonus

| Applicable Enemies | Effect |
|-------------------|--------|
| Crownshard Sentinels, Redaction Auditors | Move +5% from Nothing → Crown Alloy Shard ×1 |

### Night Bonus (Capital's "Wrong Sky")

| Applicable Enemies | Effect |
|-------------------|--------|
| Chrono Wisps only | Move +5% from Nothing → Paradox Glass ×1 |

### Protocol State Bonus (Optional)

| Protocol | Effect |
|----------|--------|
| **OBEY** | +5% from Nothing → Seal Wax Scrap ×1 (all non-elite) |
| **QUESTION** | +5% from Nothing → Paradox Glass ×1 (Wisps + Auditors only) |
| **NULL** | +3% to each mat line (Seal Wax / Crown Alloy Shard / Paradox) = +9% total. If Nothing < 9%, cap at 0 and distribute remainder. |

---

## Anti-Brick Safeguards

### A) Paradox Glass Pity System

| Condition | Action |
|-----------|--------|
| Track `PALACE_PARADOX_STREAK` | Kills of Wisps + Auditors without Paradox |
| Streak reaches 10 | Next Wisp/Auditor kill **guarantees** Paradox Glass ×1 |
| Then | Reset streak to 0 |

### B) Conversion at Bolt & Bind (Workshop)

| Conversion | Rate |
|------------|------|
| 6× Crown Alloy Shard → 1× Crown Alloy Plate | 100% |
| 8× Seal Wax Scrap → 1× Paradox Glass | 100% |

**Lore justification:** Wax "seals" get refined into a "glass record."

---

## Drop Rate Summary by Enemy

| Enemy | Paradox Glass | Crown Alloy | Seal Wax | Nothing (Base) |
|-------|--------------|-------------|----------|----------------|
| Audit Drone | 2% | 10% | 42% | 58% |
| Seal-Leech | 1% | 8% | 63% | 36% |
| Chrono Wisp | 24% (18+6) | 8% | 12% | 62% |
| Crownshard Sentinel | 3% | 52% (28+14+10) | 10% | 43% |
| Redaction Auditor | 22% | 16% (12+4) | 18% | 44% |
| Bastion Prefect (Elite) | 70% (35×2) | 20% (20) | 60% (35+25) | 10% |

---

## Expected Mats Per 10 Kills (Normal Playthrough)

| Enemy Type | Kills | Expected Paradox | Expected Alloy Shards | Expected Wax Scraps |
|------------|-------|------------------|----------------------|---------------------|
| Audit Drones | 10 | 0.2 | 1.0 | 4.2 |
| Seal-Leeches | 10 | 0.1 | 0.8 | 6.3 |
| Chrono Wisps | 10 | 2.4 | 0.8 | 1.2 |
| Crownshard Sentinels | 10 | 0.3 | 5.2 | 1.0 |
| Redaction Auditors | 10 | 2.2 | 1.6 | 1.8 |

**Note:** Actual yields higher due to Bonus Rolls and chests.

---

## Implementation Checklist

- [x] Implement Primary Roll tables (sum to 100% each)
- [x] Implement Bonus Roll tables (separate rolls)
- [x] Elite double-primary system for Bastion Prefect
- [x] Boss fixed drop table (no RNG)
- [x] Map 4 Forge-Heavy modifier (+5% Alloy from Nothing)
- [x] Night modifier for Wisps (+5% Paradox from Nothing)
- [x] Protocol State modifiers (optional)
- [x] Paradox pity counter (`PALACE_PARADOX_STREAK`)
- [x] Bolt & Bind conversion recipes (6:1 Alloy, 8:1 Paradox)
- [x] Test: 20-kill simulation should never yield zero Paradox
- [x] Test: Boss kill alone guarantees minimum craft materials
