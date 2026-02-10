# Chroma's Edge — Grand Boulevard Micro-Map Sheet (v1)
## Old Lumencrest: The Long Street — "A Museum That Got Sealed Mid-Scream"

---

## 0) Technical Specs

| Parameter | Value |
|-----------|-------|
| **Sub-Map Name** | Grand Boulevard ("The Long Street") |
| **Type** | Field route micro-map |
| **Role** | Outer Wards hub connector → deeper city routes + elite hunts + rubble gating payoff |
| **Map Size** | 208 × 88 tiles (3328 × 1408 px) |
| **Encounters** | ON |
| **Encounter Band** | Lv 72–86 |
| **Time States** | Day / Night |
| **Night Atmosphere** | Thicker fog + wrong-sky reflections + higher elite chance |
| **Mounts** | Allowed on main boulevard lane; blocked in collapsed side lanes |
| **Traversal Systems** | Mass rubble gates (post-D6), Time phase bypass (post-D7), Light reveal secrets (post-D3), Tide underworks access (post-D5) |

---

## 1) Core Intent

1. **Give the player the "capital street shot"** — long perspective + Crown Spire in distance
2. **Provide 3 readable lanes:** main boulevard, side arcade, tram trench
3. **Add one mid-route setpiece** — collapsed statue + quarantine barricade
4. **Offer optional branches** that pay off relic synergies (Mass/Time/Tide/Light)

---

## 2) Visual Identity

| Element | Description |
|---------|-------------|
| **Terrain** | Cracked marble paving, gold-trimmed curb stones, dead planters, broken lamp posts |
| **Ambient** | Distant wind tunnel, occasional "tick" audio at night, fluttering paper seals |

### Landmarks

| Landmark | Description |
|----------|-------------|
| **Crown Spire** | Always visible far northeast |
| **Collapsed Regent Statue** | In the median; forces detour |
| **Quarantine Barricade** | Paper seals + iron plates |
| **Shattered Tram Loop** | Rails cutting across the street |

---

## 3) Layout Blocks (Districts)

### District 1: Wards Gate (Entry Apron)

| Property | Value |
|----------|-------|
| **Bounds** | x 0–44, y 52–84 |
| **Encounters** | Low for first 10–12 tiles |
| **Features** | Easy navigation from Outer Wards |

### District 2: Boulevard Run (Main Street)

| Property | Value |
|----------|-------|
| **Bounds** | x 44–156, y 42–76 |
| **Features** | Wide, straight, clear visual pull forward |

### District 3: Arcade Walk (Left Side)

| Property | Value |
|----------|-------|
| **Bounds** | x 34–132, y 18–42 |
| **Features** | Collapsed shopfronts + pillars; secrets and safe routing |

### District 4: Tram Trench (Right Side)

| Property | Value |
|----------|-------|
| **Bounds** | x 72–188, y 76–88 |
| **Features** | Lower lane with rails, puddles, underworks manhole access |

### District 5: Crownward Barricade (Exit Threshold)

| Property | Value |
|----------|-------|
| **Bounds** | x 156–208, y 18–76 |
| **Features** | Heavy gating + "you're not supposed to be here" energy |

---

## 4) Entrances / Exits (Edge Triggers)

Local coords (0–207, 0–87)

### Arrival / Return

| Exit To | Coordinates | Notes |
|---------|-------------|-------|
| **From Outer Wards** (entry) | (0, 70) | West edge |
| **Back to Outer Wards** | (0, 64) | West edge; bidirectional |

### Route Exits (Load Separate Maps)

| Exit To | Coordinates | Gate Condition |
|---------|-------------|----------------|
| **Crown District Approach** | (207, 22) | East edge; story + usually Mass clearance |
| **Archive District** (alternate) | (112, 0) | North edge; Time seated OR Phase Key |
| **Underworks** (sewer/transit) | (184, 86) | South edge; Tide seated OR "Seal-Cutter" |

---

## 5) Key Anchors & Coordinates

### Entry / Signage

| Feature | Coordinates | Description |
|---------|-------------|-------------|
| **Boulevard Marker Sign** | (18, 66) | "GRAND BOULEVARD — CROWN DISTRICT" |
| **Collapsed Map Kiosk** | (30, 60) | Flavor + hint |

### Main Setpiece

| Feature | Coordinates | Description |
|---------|-------------|-------------|
| **Regent Statue Collapse** | (104, 58) | Median; blocks straight line; detour left/right |
| **Elite spawn chance** | (104, 58) | Mini-elite at night |

### Quarantine Barricade

| Feature | Coordinates | Description |
|---------|-------------|-------------|
| **Seal-Wall Segment** | (168, 46) | Non-passable until conditions met |

### Underworks Access

| Feature | Coordinates | Description |
|---------|-------------|-------------|
| **Manhole Ramp / Service Hatch** | (186, 84) | Access to Underworks sub-map |

### Optional Time Pocket

| Feature | Coordinates | Description |
|---------|-------------|-------------|
| **Phase Crack Door** | (72, 30) | Only visible in FUTURE |
| **Micro-room** | 24×14 | Returns at (140, 54) |

### Optional Light Secret

| Feature | Coordinates | Description |
|---------|-------------|-------------|
| **Reveal Wall Panel** | (58, 24) | Light required; hidden cache behind pillar |

---

## 6) Gating (So It Feels Designed)

### Gate 1 — "Statue Rubble"

| Property | Value |
|----------|-------|
| **Location** | (104, 58) |
| **Pre-Mass** | Detour exists, slow + higher encounter pressure |
| **Post-Mass** | Clear rubble pile to open straight boulevard run (QoL reward) |

### Gate 2 — "Quarantine Seal-Wall"

| Property | Value |
|----------|-------|
| **Location** | (168, 46) |
| **Option A** | Main story key (Dominion seal breaker quest) |
| **Option B** | Time phase bypass via FUTURE crack door |
| **Option C** | Underworks route (Tide) to emerge beyond barricade |

### Gate 3 — Crown District Roadblock

| Property | Value |
|----------|-------|
| **Exit** | (207, 22) |
| **Primary** | Story flag |
| **Secondary** | Requires Mass (move blockade) or Time (phase around) |

---

## 7) Mechanics (Micro-Map Level)

### A) "Wrong Sky" Reflection (Night)

| Property | Description |
|----------|-------------|
| **Location** | Mirror-like puddles |
| **Effect** | Show aurora where there shouldn't be any |
| **Purpose** | Hint that Time weirdness is stronger deeper in city |

### B) Patrol Spotlight (Optional)

| Property | Description |
|----------|-------------|
| **Behavior** | Slow moving cone light from distant tower (night only) |
| **Effect if caught** | Increases encounter chance for ~30 seconds (soft penalty) |

---

## 8) Encounters & Zones

### Base Spawn Table (Lv 72–86)

| Enemy | Traits |
|-------|--------|
| **Crownshard Sentinels** | Old guard constructs, high DEF |
| **Phase Skulkers** | Ambush + forced movement |
| **Chrono Wisps** | Speed/initiative manipulation |
| **Seal-Leeches** | Status drains; "paper curse" theme |
| **Dominion Salvage Captain** | Rare elite, night + PHASE pressure flags |

### Encounter Zones

| Zone | Bounds | Type |
|------|--------|------|
| **Zone A** (medium) | x 44–120, y 48–72 | Boulevard Run midsection |
| **Zone B** (high) | x 88–120, y 46–66 | Regent Statue area |
| **Zone C** (high) | x 150–208, y 28–70 | Crownward Barricade approach |
| **Zone D** (optional hard) | x 112–200, y 78–87 | Tram Trench |

---

## 9) Salvage / Nodes / Loot

### Always-On Nodes

| Node | Coordinates | Loot |
|------|-------------|------|
| **Clocksteel Filings** | (142, 62) | Pressworks mat |
| **Crown Sigil Fragment** | (96, 26) | Key item (rare node) |
| **Seal Wax Scrap** | (164, 58) | Craft "seal-cutter" refills |

### Chests

| Chest | Coordinates | Loot |
|-------|-------------|------|
| **Chest A** (Arcade Walk) | (46, 22) | Paradox Glass shard + Ether |
| **Chest B** (Tram Trench) | (160, 84) | Brine mat bundle / Kelp filter (if Tide) |

### Night-Only Cache

| Node | Coordinates | Conditions | Loot |
|------|-------------|------------|------|
| **Tower Shadow Cache** | (118, 40) | Night only | Chrono Band mat or "Clockseal" consumable |

---

## 10) Scripted Beats

### A) One-Time "Capital Still Breathes" Beat

| Property | Value |
|----------|-------|
| **Trigger** | (60, 62) |
| **Event** | Streetlamp flickers on for one second… then dies |
| **Optional Line** | "Someone's still feeding power." |

### B) One-Time "Regent Face" Beat

| Property | Value |
|----------|-------|
| **Trigger** | (104, 58) |
| **Event** | Statue face half-buried, expression looks like it changed mid-fall |
| **Tone** | Time dread |

### C) Dominion Seal Flavor (PHASE 1+)

| Property | Description |
|----------|-------------|
| **Visual** | Paper seal props + "COMPLIANCE" stamps on barricade |
| **Audio** | Distant loudspeaker barks (no actual NPC needed) |

---

## 11) Implementation Notes

1. **Main lane:** Keep wide and readable; put clutter in side lanes
2. **Underworks hatch:** Visually obvious (ladder + steam + salt stain)
3. **Time crack bypass:** Optional and clearly signposted by subtle shimmer so Time-tech players notice instantly

---

## Quick Reference Map Overview

```
                        NORTH
                          ↑
    ┌───────────────────────────────────────────────────────────┐
    │                                                           │
    │    DISTRICT 3: Arcade Walk          DISTRICT 5:           │
    │    (x 34–132, y 18–42)            Crownward Barricade     │
    │    - Collapsed shopfronts         (x 156–208, y 18–76)    │
    │    - Light secret (58,24)         - Seal-Wall (168,46)    │
    │    - Chest A (46,22)              - Seal Wax (164,58)     │
    │                                   - Crown Exit (207,22)   │
    │                                                           │
    │    ═══════════════════════════════════════════            │
    │                                                           │
    │    DISTRICT 2: Boulevard Run (Main Street)                │
    │    (x 44–156, y 42–76)                                    │
    │                                                           │
    │    Wards Gate (0,70) →    "Capital Still Breathes"        │
    │                              (60,62)                      │
    │                               │                           │
    │    ═══════════════════════════╪══════════════════════     │
    │                               │                           │
    │    REGENT STATUE (104,58) ════► Collapsed median          │
    │    ├─ Forced detour left/right                            │
    │    ├─ Elite spawn [night]                                 │
    │    ├─ Crown Sigil (96,26)                                 │
    │    └─ "Regent Face" beat                                  │
    │                               │                           │
    │    ═══════════════════════════╪══════════════════════     │
    │                               │                           │
    │    Time Pocket Entrance (72,30) [FUTURE only]             │
    │        └─ returns at (140,54)                             │
    │                               │                           │
    │    Clocksteel Filings (142,62)                            │
    │    Night Cache (118,40) [night]                           │
    │                                                           │
    │    ═══════════════════════════════════════════            │
    │                                                           │
    │    DISTRICT 4: Tram Trench (Lower Lane)                   │
    │    (x 72–188, y 76–88)                                    │
    │    - Rails + puddles                                      │
    │    - Underworks hatch (186,84)                            │
    │    - Chest B (160,84)                                     │
    │                                                           │
    │    ═══════════════════════════════════════════            │
    │                                                           │
    │    Exits:                                                   │
    │    - Outer Wards ← (0,70) / (0,64)                        │
    │    - Crown District → (207,22)                            │
    │    - Archive District ↑ (112,0) [Time/Key]                │
    │    - Underworks ↓ (184,86) [Tide/Cutter]                  │
    │                                                           │
    │    Crown Spire visible in northeast skyline               │
    │                                                           │
    └───────────────────────────────────────────────────────────┘
```

**Key Anchors Summary:**

| Feature | Coordinates |
|---------|-------------|
| **Outer Wards Exit** | (0, 70) / (0, 64) |
| **Boulevard Sign** | (18, 66) |
| **Map Kiosk** | (30, 60) |
| **"Capital Still Breathes" Beat** | (60, 62) |
| **Regent Statue** | (104, 58) |
| **Crown Sigil Fragment** | (96, 26) |
| **Time Pocket Entrance** [FUTURE] | (72, 30) |
| **Time Pocket Exit** | (140, 54) |
| **Clocksteel Filings** | (142, 62) |
| **Night Cache** [night] | (118, 40) |
| **Seal-Wall** | (168, 46) |
| **Seal Wax Scrap** | (164, 58) |
| **Underworks Hatch** | (186, 84) |
| **Chest A** (Arcade) | (46, 22) |
| **Chest B** (Trench) | (160, 84) |
| **Light Secret** | (58, 24) |
| **Crown District Exit** | (207, 22) |
| **Archive Exit** [Time] | (112, 0) |
| **Underworks Exit** [Tide] | (184, 86) |
