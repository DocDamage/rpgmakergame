# Chroma's Edge — Crownfall Viaduct Micro-Map Sheet (v1)
## Arrival Runway to Old Lumencrest — "Crossed a Reality Agreement"

---

## 0) Technical Specs

| Parameter | Value |
|-----------|-------|
| **Map Name** | Crownfall Viaduct |
| **Type** | Field Transition Micro-Map (Liminal Span → Old Lumencrest) |
| **Purpose** | Arrival runway framing the capital skyline + teaching "Time + Ruins" traversal |
| **Size** | 192 × 80 tiles |
| **Encounters** | ON (light at start) |
| **Encounter Band** | Lv 64–78 |
| **Time States** | Day / Night |
| **Night Atmosphere** | Heavier fog + more phase flicker |
| **Mounts** | Auto-dismount at first ruin barricade (narrow + debris + time interference) |

---

## 1) Core Intent

1. **Frame the capital skyline** as a visual "call"
2. **Teach "Time + Ruins" traversal language** — phase rubble navigation
3. **Sell the feeling:** "You didn't just travel distance — you crossed a reality agreement"
4. **The capital isn't destroyed like a warzone** — it's paused, edited, and hollowed

---

## 2) Layout Blocks (Districts)

### District 1: Spanhead Platform (Safe Apron)

| Property | Value |
|----------|-------|
| **Bounds** | x 78–114, y 0–14 |
| **Encounters** | OFF for first ~10 tiles |
| **Features** | Clean arrival from Liminal Span |

### District 2: Collapsed Aqueduct Run (Main Lane)

| Property | Value |
|----------|-------|
| **Bounds** | x 60–160, y 14–40 |
| **Features** | Main lane, skyline reveal point |

### District 3: Wreckline Switchbacks (Optional Loop)

| Property | Value |
|----------|-------|
| **Bounds** | x 28–92, y 30–68 |
| **Features** | Optional loot loop + first "phase rubble" tutorial |

### District 4: Crownfall Gate (City Threshold)

| Property | Value |
|----------|-------|
| **Bounds** | x 140–192, y 44–80 |
| **Features** | Massive arch + sealed signage |

---

## 3) Entrances / Exits

| Exit To | Coordinates | Notes |
|---------|-------------|-------|
| **The Liminal Span** | (96, 0) | North edge |
| **Old Lumencrest: Outer Wards** | (188, 70) | East edge — city entrance |

---

## 4) Mechanics (Preview, Not Annoying)

### A) Phase Rubble (Time Tech)

| Element | Description |
|---------|-------------|
| **Location** | One rubble choke in Wreckline Switchbacks |
| **PAST** | Intact side-stair (passable) |
| **PRESENT** | Blocked by rubble |
| **FUTURE** | Collapsed gap becomes climb-down path |

### B) Stasis Mist Patches

| Property | Description |
|----------|-------------|
| **Location** | Near optional loot |
| **Intensity** | Mild, avoidable |

### C) Warp-Back Failsafe

| Property | Description |
|----------|-------------|
| **Trigger** | Stepping into void tile |
| **Effect** | Returns to last stable plate |
| **Penalty** | Small HP chip (optional) |

---

## 5) Key Anchors

| Prop | Coordinates | Function |
|------|-------------|----------|
| **Chrono Pylon** (phase toggle) | (90, 28) | Switch Past/Present/Future |
| **Skyline Reveal Spot** (script beat) | (120, 24) | Capital silhouette reveal |
| **Optional Chest Loop entrance** | (64, 44) | Wreckline side path |
| **Crownfall Gate Arch** | (176, 66) | City threshold |

---

## 6) Encounters (Ruins-Flavored)

| Enemy | Traits |
|-------|--------|
| **Phase Skulkers** | Ambush + forced movement |
| **Chrono Wisps** | Initiative/speed pressure |
| **Crownshard Sentinels** | Old guard constructs, tanky |
| **Dominion Salvage Captain** | Rare elite, PHASE pressure flags |

---

## 7) Loot / Salvage Nodes

| Node | Coordinates | Loot |
|------|-------------|------|
| **Paradox Glass Shard** | (52, 58) | Rare Time mat |
| **Clocksteel Filings** | (148, 32) | Pressworks mat |
| **Crown Sigil Fragment** | (172, 50) | Key item for later door inside city |

---

## 8) Scripted Events

### A) Skyline Reveal Beat

| Property | Value |
|----------|-------|
| **Trigger** | (120, 24) |
| **Event** | Camera pans to reveal Old Lumencrest skyline |
| **Atmosphere** | Fog parts, Crown Spire visible, silence |
| **Optional Line** | "The city didn't fall. It just... stopped agreeing with itself." |

### B) Crownfall Gate Approach

| Property | Value |
|----------|-------|
| **Trigger** | (160, 60) |
| **Event** | Dominion quarantine seals visible on arch |
| **UI Tip** | "Old Lumencrest — Travel Advisory: Phase Instability" |

---

## 9) Phase-Based Story States

### PHASE 0 — First Arrival

| Aspect | State |
|--------|-------|
| Atmosphere | Heavy silence, distant Crown Spire visible |
| Phase rubble | Requires active switching |
| Dominion presence | Minimal (seals only) |

### PHASE 1 — Dominion Pressure Rising

| Aspect | State |
|--------|-------|
| Seals | More compliance placards |
| Patrols | Occasional surveyor silhouettes |
| Salvage Captain | Higher spawn rate |

### PHASE 2 — Post-Archive District Clear

| Aspect | State |
|--------|-------|
| Route | Smoother (phase rubble stabilizes slightly) |
| Shortcut | New climb-path opens in Wreckline |

---

## Quick Reference Map Overview

```
                        NORTH
                          ↑
    ┌───────────────────────────────────────────────────────────┐
    │                                                           │
    │    DISTRICT 1: Spanhead Platform                          │
    │    (x 78–114, y 0–14)                                     │
    │    - Safe apron, encounters OFF                           │
    │    - Liminal Span exit (96,0)                             │
    │                                                           │
    │    ═══════════════════════════════════════════            │
    │                                                           │
    │    DISTRICT 2: Collapsed Aqueduct Run                     │
    │    (x 60–160, y 14–40)                                    │
    │                                                           │
    │    Chrono Pylon (90,28) ════►                             │
    │    Phase toggle point                                     │
    │                                                           │
    │    ═══════════════════════════════════════════            │
    │                      │                                    │
    │    ══════════════════╪══════════════════════              │
    │                      │                                    │
    │    DISTRICT 3: Wreckline Switchbacks                      │
    │    (x 28–92, y 30–68)                                     │
    │    - Optional loop entrance (64,44)                       │
    │    - Phase rubble tutorial zone                           │
    │    - Paradox Glass (52,58)                                │
    │                                                           │
    │    DISTRICT 4: Crownfall Gate                             │
    │    (x 140–192, y 44–80)                                   │
    │                                                           │
    │    Clocksteel Filings (148,32)                            │
    │                                                           │
    │    Crown Sigil Fragment (172,50)                          │
    │                                                           │
    │    CROWNFALL GATE ARCH (176,66)                           │
    │    ├─ Massive stone arch                                  │
    │    ├─ Dominion quarantine seals                           │
    │    ├─ Crown Spire visible beyond                          │
    │    └─ OLD LUMENCREST EXIT (188,70)                        │
    │                                                           │
    │    Skyline Reveal (120,24) ════►                          │
    │    "The city didn't fall. It just stopped                 │
    │       agreeing with itself."                              │
    │                                                           │
    └───────────────────────────────────────────────────────────┘
```

**Key Anchors Summary:**

| Feature | Coordinates |
|---------|-------------|
| **Liminal Span Exit** | (96, 0) |
| **Chrono Pylon** | (90, 28) |
| **Skyline Reveal** | (120, 24) |
| **Wreckline Entrance** | (64, 44) |
| **Paradox Glass** | (52, 58) |
| **Clocksteel Filings** | (148, 32) |
| **Crown Sigil Fragment** | (172, 50) |
| **Crownfall Gate Arch** | (176, 66) |
| **Old Lumencrest Exit** | (188, 70) |
