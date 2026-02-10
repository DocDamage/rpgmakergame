# Chroma's Edge — Crown District Approach Map Sheet (v1)
## Old Lumencrest: Crownward Perimeter — "Reality Behaving Like It Has a Security System"

---

## 0) Technical Specs

| Parameter | Value |
|-----------|-------|
| **Sub-Map Name** | Crown District Approach ("The Palace Ring") |
| **Type** | Field route micro-map |
| **Role** | Connects Grand Boulevard / Outer Wards → Crown District (inner hub / palace gate) |
| **Map Size** | 192 × 96 tiles (3072 × 1536 px) |
| **Encounters** | ON |
| **Encounter Band** | Lv 78–92 |
| **Time States** | Day / Night |
| **Night Atmosphere** | Heavier fog + higher elite chance + watchlights more dangerous |
| **Mounts** | Allowed only on outer service road; forced dismount at inner perimeter catwalks |
| **Traversal Systems** | Time (phase barriers), Mass (rubble), Tide (underworks), Light (reveal panels), Archive Key (final gate) |

---

## 1) Entry / Exit Links

Local coords (0–191, 0–95)

### Entrances

| From | Coordinates | Notes |
|------|-------------|-------|
| **Grand Boulevard** | (0, 22) | Main intended entry |
| **Outer Wards** (alternate) | (0, 74) | Later unlock or story convenience |

### Exits

| To | Coordinates | Gate Condition |
|----|-------------|----------------|
| **Crown District** (inner hub) | (191, 28) | **CROWN_ARCHIVE_KEY_ACQUIRED = TRUE** |
| **Underworks** (bypass) | (132, 95) | Tide seated OR Seal-Cutter item |

---

## 2) Visual Identity

| Element | Description |
|---------|-------------|
| **Terrain** | Cracked marble service road, iron quarantine plates, dead hedges, toppled fountains, watchtower silhouettes |

### Landmarks

| Landmark | Description |
|----------|-------------|
| **Crown Wall** | Massive curved fortification with gilded trim now blackened |
| **Watchlight Towers** | Sweep cones at night |
| **Sealed Garden Courtyards** | Beautiful and wrecked |
| **Phase Scar Creases** | Visible shimmer near gates |

---

## 3) Layout Blocks (Districts)

### District 1: Boulevard Spillway (Entry Apron)

| Property | Value |
|----------|-------|
| **Bounds** | x 0–44, y 10–38 |
| **Features** | Wide, readable; lets players orient before pressure starts |

### District 2: Quarantine Service Road (Outer Ring)

| Property | Value |
|----------|-------|
| **Bounds** | x 30–150, y 36–66 |
| **Features** | Main traversal lane (mount-allowed early); signage and sealed crates |

### District 3: Shattered Garden Cut (Inner Perimeter)

| Property | Value |
|----------|-------|
| **Bounds** | x 54–168, y 8–40 |
| **Features** | Narrower, prettier, more dangerous; first Phase Barrier |

### District 4: Wallwalk Catacomb (Underwall Segment)

| Property | Value |
|----------|-------|
| **Bounds** | x 80–176, y 66–96 |
| **Features** | Tight lanes + rubble + Underworks hatch; Mass/Tide payoff |

### District 5: Crown Gate Bastion (Final Threshold)

| Property | Value |
|----------|-------|
| **Bounds** | x 150–192, y 14–56 |
| **Features** | Last gate cluster + boss-lite encounter chance + key moment |

---

## 4) Core Setpieces & Anchors

### Entry Signage

| Feature | Coordinates | Text |
|---------|-------------|------|
| **Crownward Notice Board** | (18, 26) | "CROWN DISTRICT — RESTRICTED. AUTHORIZED RECORDS ONLY." |

### Watchlight Towers (Pressure Without Cheapness)

| Tower | Coordinates | Coverage |
|-------|-------------|----------|
| **Tower A** | (72, 18) | Shattered Garden Cut |
| **Tower B** | (122, 58) | Service Road midsection |
| **Tower C** | (168, 22) | Gate Bastion |

**Watchlight Rule:** Getting caught applies "Marked" for ~30 seconds:
- Encounter rate up
- Ambush chance up
- OR enemies start with buff

### Phase Barrier #1 (Tutorial-Level)

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Barrier** | (92, 24) | Blocks inner garden lane |
| **Bypass options** | — | Time seated → phase toggle, OR Phase Key consumable, OR outer service road (longer but safe) |
| **Phase Pylon** | (84, 30) | Toggle point |

### Mass Blockade (Payoff Gate)

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Blockade rubble** | (110, 78) | Wallwalk Catacomb |
| **Pre-Mass** | — | Detour through watchlight lane (riskier) |
| **Post-Mass** | — | Clear rubble → fast safe corridor to Underworks hatch + better loot |

### Underworks Access

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Hatch / collapse ramp** | (132, 94) | — |

### Final Gate Cluster (Key Moment)

| Feature | Coordinates | Requirement |
|---------|-------------|-------------|
| **Crown Gate Console** | (182, 28) | CROWN_ARCHIVE_KEY |
| **Alternate (late-game)** | — | Time + Mass combined can "phase-wedge" side door (optional) |

---

## 5) Mechanics (Gauntlet Flavor)

### A) "Compliance Seals" (Soft Hazard)

| Property | Description |
|----------|-------------|
| **Visual** | Paper seals flutter on walls |
| **Effect** | Crossing threshold tiles → tiny Confounded buildup |
| **Clear** | At "clean air" pads every ~12–16 tiles |

### B) Phase Flicker Slabs (Garden + Bastion)

| Property | Description |
|----------|-------------|
| **Behavior** | Some tiles exist only in PRESENT or FUTURE |
| **Telegraph** | Shimmer edges (always fair) |

### C) Patrol Chime (Night Only)

| Property | Description |
|----------|-------------|
| **Trigger** | Bell sound |
| **Effect** | Warns of watchlight sweep acceleration |

---

## 6) Encounters & Zones

### Enemy Table (Lv 78–92)

| Enemy | Traits |
|-------|--------|
| **Crownshard Sentinels** | Tank constructs, punish direct routes |
| **Phase Skulkers** | Ambush + forced movement setups |
| **Chrono Wisps** | Initiative/speed pressure |
| **Seal-Leeches** | Buff drain / confounded application |
| **Bastion Prefect Drone** | Rare elite, night + near Gate Bastion |

### Encounter Zones

| Zone | Bounds | Type |
|------|--------|------|
| **Zone A** (medium) | x 44–124, y 40–64 | Service Road midsection |
| **Zone B** (high) | x 70–160, y 10–34 | Shattered Garden Cut |
| **Zone C** (high) | x 96–176, y 70–95 | Wallwalk Catacomb |
| **Zone D** (very high) | x 152–192, y 16–52 | Gate Bastion |

---

## 7) Loot / Salvage / Secrets

### Always-On Nodes

| Node | Coordinates | Loot |
|------|-------------|------|
| **Seal Wax Scrap** | (60, 60) | Craft refills |
| **Clocksteel Filings** | (140, 50) | Pressworks mat |
| **Crown Alloy Plate** | (164, 82) | High-tier craft mat |

### Chests

| Chest | Coordinates | Loot |
|-------|-------------|------|
| **Chest A** (Garden alcove) | (74, 14) | Paradox Glass + Ether |
| **Chest B** (Catacomb dead end) | (154, 90) | Anchor plating mat + credits |
| **Chest C** (Bastion side room) | (176, 44) | "Bastion Seal" accessory mat (stasis/confounded resist) |

### Light Secret

| Feature | Coordinates | Requirement | Reward |
|---------|-------------|-------------|--------|
| **Reveal panel** | (52, 18) | Light | Crown Sigil Fragment OR lore key ("Quarantine Orders: Revision 3") |

---

## 8) Scripted Beats

### A) One-Time: "The Wall is Listening"

| Property | Value |
|----------|-------|
| **Trigger** | (64, 30) — first view of Crown Wall curve |
| **Event** | Watchlight pauses on party for one extra beat, like it "recognizes" something |

### B) One-Time: "Key Slot"

| Property | Value |
|----------|-------|
| **Trigger** | (182, 28) without Archive Key |
| **Event** | UI prompt shows key slot + line: "AUTHORIZED RECORD REQUIRED." |
| **Purpose** | Clean pointer back to Archive District |

### C) Phase Pressure Rising (Dominion Vibe)

| Property | Description |
|----------|-------------|
| **Visual** | More stamped seals |
| **Audio** | Louder "compliance" loudspeaker barks |
| **Effect** | Extra patrol sweep at night |

---

## 9) Revisit QoL (Rewards for Progress)

| Condition | Benefit |
|-----------|---------|
| **Post-Archive Key** | Gate opens normally; route becomes reliable connector |
| **Post-Mass** | Rubble blockade clears → shorter path + safer loot access |
| **Post-Time** | Phase barrier bypass becomes trivial (1 switch), reducing watchlight exposure |
| **Post-Tide** | Underworks hatch becomes "skip half the map" connector |

---

## 10) Implementation Notes

1. **Outer service road:** Keep wide and readable (sprint-through option)
2. **Inner garden:** Risky but rewarding (best loot + fastest line)
3. **Watchlights:** Pressure zones that raise encounter heat, not stealth game

---

## Quick Reference Map Overview

```
                        NORTH
                          ↑
    ┌───────────────────────────────────────────────────────────┐
    │                                                           │
    │    DISTRICT 3: Shattered Garden Cut                       │
    │    (x 54–168, y 8–40)                                     │
    │    - Narrow, dangerous, pretty                            │
    │    - Phase Barrier (92,24)                                │
    │    - Phase Pylon (84,30)                                  │
    │    - Chest A (74,14)                                      │
    │    - Watchlight Tower A (72,18)                           │
    │    - Light Secret (52,18) [Light]                         │
    │                                                           │
    │    ═══════════════════════════════════════════            │
    │                                                           │
    │    DISTRICT 2: Quarantine Service Road                    │
    │    (x 30–150, y 36–66)                                    │
    │    - Main lane (mounts allowed early)                     │
    │    - Notice Board (18,26)                                 │
    │    - Seal Wax Scrap (60,60)                               │
    │    - Watchlight Tower B (122,58)                          │
    │    - Clocksteel Filings (140,50)                          │
    │                                                           │
    │    ═══════════════════════════════════════════            │
    │                                                           │
    │    DISTRICT 4: Wallwalk Catacomb                          │
    │    (x 80–176, y 66–96)                                    │
    │    - Tight lanes + rubble                                 │
    │    - Mass Blockade (110,78) [Mass clears]                 │
    │    - Underworks Hatch (132,94) [Tide]                     │
    │    - Chest B (154,90)                                     │
    │    - Crown Alloy Plate (164,82)                           │
    │                                                           │
    │    ═══════════════════════════════════════════            │
    │                                                           │
    │    DISTRICT 5: Crown Gate Bastion                         │
    │    (x 150–192, y 14–56)                                   │
    │    - Final gate cluster                                   │
    │    - Watchlight Tower C (168,22)                          │
    │    - Chest C (176,44)                                     │
    │    - CROWN GATE CONSOLE (182,28)                          │
    │      [Requires CROWN_ARCHIVE_KEY]                         │
    │                                                           │
    │    Exits:                                                   │
    │    - Grand Boulevard ← (0,22) [main entry]                │
    │    - Outer Wards ← (0,74) [alternate]                     │
    │    - Crown District → (191,28) [key required]             │
    │    - Underworks ↓ (132,95) [Tide/Cutter]                  │
    │                                                           │
    │    Crown Wall curves through entire map                   │
    │                                                           │
    └───────────────────────────────────────────────────────────┘
```

**Key Anchors Summary:**

| Feature | Coordinates |
|---------|-------------|
| **Grand Boulevard Entry** | (0, 22) |
| **Outer Wards Entry** | (0, 74) |
| **Notice Board** | (18, 26) |
| **"Wall is Listening" Beat** | (64, 30) |
| **Light Secret Panel** [Light] | (52, 18) |
| **Phase Barrier** | (92, 24) |
| **Phase Pylon** | (84, 30) |
| **Chest A** | (74, 14) |
| **Tower A** | (72, 18) |
| **Seal Wax Scrap** | (60, 60) |
| **Tower B** | (122, 58) |
| **Clocksteel Filings** | (140, 50) |
| **Mass Blockade** [Mass] | (110, 78) |
| **Underworks Hatch** [Tide] | (132, 94) |
| **Chest B** | (154, 90) |
| **Crown Alloy Plate** | (164, 82) |
| **Tower C** | (168, 22) |
| **Chest C** | (176, 44) |
| **Crown Gate Console** [Key] | (182, 28) |
| **Crown District Exit** | (191, 28) |
| **Underworks Exit** | (132, 95) |
