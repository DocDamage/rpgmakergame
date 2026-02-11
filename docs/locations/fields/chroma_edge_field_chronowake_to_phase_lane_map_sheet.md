# Chroma's Edge — Chronowake to Phase-Lane Crossing Transition Map Sheet (v1)
## The Liminal Span — "Time is Infrastructure"

---

## 0) Map Technical Specs

| Parameter | Value |
|-----------|-------|
| **Map Name** | The Liminal Span |
| **Type** | Field Transition Micro-Map (Chronowake → Phase-Lane tutorial) |
| **Size** | 176 × 80 tiles (2816 × 1280 px) |
| **Encounters** | ON (light + controllable) |
| **Encounter Band** | Lv 60–74 (scales to Lv 86 on revisit) |
| **Time States** | Day / Night |
| **Day Atmosphere** | Irregular buoy pings, deep fog horn |
| **Night Atmosphere** | Heavier fog + brighter buoy glow + more "frame skip" VFX |
| **Mounts** | Allowed (D3+) — 0% encounter rate while mounted; auto-dismount at Phase Gate pylons |

---

## 1) Core Intent

1. **Teach Phase Barrier traversal** cleanly (Past / Present / Future lanes)
2. **Introduce "phase routing"** as a 3-lane bridge puzzle with zero frustration
3. **Create a reusable map** that becomes a fast connector later
4. **Seed "time static" vibe** without becoming annoying

---

## 2) Visual Identity

| Element | Description |
|---------|-------------|
| **Terrain** | Wet pier planks → stone pylons → suspended span plates → fog gulf → opposite shore pylons |
| **Ambient** | Irregular buoy pings + deep fog horn + occasional ticking not synced to anything |

### Landmarks

| Landmark | Description |
|----------|-------------|
| **Phase Gate Pylons** | Trident structures with 3 icons (Past/Present/Future) |
| **Chrono Buoys** | Ping lights, act as breadcrumbs |
| **Span plates** | Blink in/out depending on phase |
| **Time foam** | Drifts backwards along edges |

---

## 3) Layout Blocks (Districts)

### District 1: Pierhead Apron (Safe Start)

| Property | Value |
|----------|-------|
| **Bounds** | x 70–110, y 0–16 |
| **Encounters** | OFF for first ~10 tiles |
| **Features** | Tutorial prompt + clear signage |

### District 2: Pylon Yard (Calibration Zone)

| Property | Value |
|----------|-------|
| **Bounds** | x 52–124, y 16–40 |
| **Features** | Main Phase Gate + optional side loop entrance |

### District 3: Phase Span (Three-Lane Bridge)

| Property | Value |
|----------|-------|
| **Bounds** | x 30–150, y 34–64 |
| **Features** | Core puzzle: three parallel lanes (Past / Present / Future) |

### District 4: Crossing Shore (Exit Platform)

| Property | Value |
|----------|-------|
| **Bounds** | x 120–176, y 50–80 |
| **Features** | Leads into next overworld region / node |

---

## 4) Entrances / Exits (Edge Triggers)

Local coords (0–175, 0–79)

| Exit To | Coordinates | Notes |
|---------|-------------|-------|
| **Chronowake Pier Town** | (88, 0) | North edge |
| **Overworld Phase-Lane Node** (new route) | (172, 70) | East edge — "phase barrier pass" connector |
| **Hidden Phase Pocket** [post-D7 + sidequest] | (0, 44) | West edge, locked |

---

## 5) Key Anchors & Navigation Props

| Prop | Coordinates | Function |
|------|-------------|----------|
| **Signpost Cluster** | (90, 10) | "CHRONOWAKE" ← / "PHASE-LANE CROSSING" ↑ / "RESTRICTED POCKET" → (locked) |
| **Main Phase Gate Pylon** (tutorial + dismount) | (88, 26) | Choose PAST / PRESENT / FUTURE for the span |
| **Span Entry Threshold** | (88, 36) | Auto-dismount + warning: "Time interference—mounts cannot maintain phase" |
| **Reset Pedestal** | (76, 24) | Restores span to PRESENT default + resets moving hazards |
| **Buoy Breadcrumb Line** | Every ~10 tiles | Visual guidance along safe lane edges |

---

## 6) Core Mechanic — The Three-Lane Phase Span

### A) Lane Rules (Simple + Fair)

The bridge has three parallel lanes:

| Lane | Position | Description |
|------|----------|-------------|
| **PAST** | Left | Stable plates, but one section blocked by intact "old barrier" |
| **PRESENT** | Center | Partially broken; gap must be bridged by switching briefly |
| **FUTURE** | Right | Fractured and icy; has stasis patches + "phase flicker" tiles |

**Goal:** Cross using at most 2 phase switches the first time.

### B) Intended First-Time Path

| Step | Action |
|------|--------|
| 1 | Start in PRESENT (default) |
| 2 | Walk to first gap |
| 3 | Switch to PAST to cross "intact plates" segment |
| 4 | Switch back to PRESENT to reach exit platform |

### C) Anti-Frustration Design

| Feature | Description |
|---------|-------------|
| **Falling off** | Warps to last pylon pad with small penalty (HP chip or time cost) |
| **Anchor Pads** | Frequent safe squares that stop forced movement and reduce stasis buildup |

---

## 7) Hazards (Tutorial-Level)

### A) Phase Flicker Tiles (Right lane)

| Property | Description |
|----------|-------------|
| **Location** | FUTURE lane |
| **Behavior** | Exist only in FUTURE; blink off briefly every few seconds |
| **Telegraph** | Glow → dim → blink |

### B) Stasis Mist Patches (Right lane)

| Property | Description |
|----------|-------------|
| **Effect** | Mild stasis buildup |
| **Avoidable** | Via left/center lanes |
| **Lesson** | "Future is costly" |

### C) "Time Slip" Push (Rare)

| Property | Description |
|----------|-------------|
| **Location** | One narrow segment |
| **Effect** | Shimmer pushes you 1 tile forward (not into danger) |
| **Telegraph** | Foam flows backward before trigger |

---

## 8) Scripted Events

### A) One-Time Tutorial Prompt

| Property | Value |
|----------|-------|
| **Trigger** | (88, 18) |
| **Event** | Tooltip: "Phase Gates change which path exists. Choose a phase." |

### B) "Arrival Board Lies" Beat

| Property | Value |
|----------|-------|
| **Trigger** | (96, 22) near sign prop |
| **Event** | Posted time flips rapidly (flavor) |
| **Optional Line** | "This schedule… is arguing with itself." |

### C) Dominion "Compliance Seal" (Tension Only)

| Property | Value |
|----------|-------|
| **Active** | PHASE 1+ (pressure rising), Day only |
| **Silhouette Anchor** | (60, 28) |
| **Behavior** | Approaching causes it to leave; next visit a seal placard appears on the pylon |

---

## 9) Encounters & Zones

### Base Spawn Table (Lv 60–74)

| Enemy | Traits |
|-------|--------|
| **Chrono Wisps** | Speed/initiative manipulation |
| **Rime Stalkers** | Stasis buildup |
| **Hourglass Mites** | Debuff nuisance |
| **Phase Skulkers** | Ambush + forced movement |

### Encounter Zones

| Zone | Bounds | Type |
|------|--------|------|
| **Zone A** (light) | x 60–116, y 18–34 | Pylon Yard edges |
| **Zone B** (main) | x 46–140, y 40–60 | Span midsection |
| **Zone C** (harder) | x 126–176, y 56–78 | Exit platform approach |

*(For pure traversal tutorial, set encounter rate very low here.)*

---

## 10) Salvage / Gathering Nodes

### Always-On

| Node | Coordinates | Loot |
|------|-------------|------|
| **Buoycore Brass scrap** | (70, 40) | Timecraft mat |
| **Clocksteel filings** | (118, 52) | Pressworks mat |
| **Paradox Glass shard** | (34, 58) | Rare chance |

### One-Time Prep Crate

| Node | Coordinates | Loot |
|------|-------------|------|
| **Supply Crate** | (102, 18) | Stasis Balm ×2 + "Clockseal" ×1 |

### Night-Only Cache

| Node | Coordinates | Conditions | Loot |
|------|-------------|------------|------|
| **Aurora Drift Cache** | (26, 70) | Night only | Chrono Band mat or Phase Key (single-use) |

---

## 11) Secrets & Optional Side Loop

### A) Left-Side Maintenance Walk (Small Secret Pocket)

| Step | Coordinates | Description |
|------|-------------|-------------|
| **Entrance** | (58, 34) | Ladder down |
| **Path** | Hugs cliff base | Returns near mid-span |
| **Chest** | (22, 46) | "Chrono Band" upgrade mat |
| **Lore plaque** | (20, 50) | "They built lanes so the world would stop arguing." |

### B) Post-D7 Shortcut Stabilization

| Feature | Description |
|---------|-------------|
| **Visual reward** | PRESENT lane gap gets smaller after D7 clear |
| **Gameplay benefit** | Straight run with only 1 switch needed |

---

## 12) Story-State Phases (Set Dressing + Difficulty)

### PHASE 0 — First Access (post-D7 recommended)

| Aspect | State |
|--------|-------|
| Tutorial | Clean |
| Hazards | Minimal |
| Buoy pings | Steady |

### PHASE 1 — Dominion Pressure Rising

| Aspect | State |
|--------|-------|
| Compliance | Seals appear |
| Surveillance | Occasional watcher silhouette |
| Encounters | Slightly higher rate at exit platform |

### PHASE 2 — Late Revisit

| Aspect | State |
|--------|-------|
| Lane plates | Stabilize more |
| Traversal | Smoother (progression reward) |
| Optional spawn | Mini-elite: Paradox Warden Scout at night (drops rare mat) |

---

## 13) Implementation Notes

1. **Phase Gate Pylon:** Keep centered and obvious
2. **Lane color-coding:** Subtle prop variation (not hard UI):
   - Past = older stone + moss
   - Present = cracked gray plates
   - Future = ice ribs + violet shimmer
3. **Fail-safe:** "Warp-back" if player steps into void tile

---

## Quick Reference Map Overview

```
                        NORTH
                          ↑
    ┌───────────────────────────────────────────────────────────┐
    │                                                           │
    │    DISTRICT 1: Pierhead Apron                             │
    │    (x 70–110, y 0–16)                                     │
    │    - Signpost (90,10): "CHRONOWAKE" ←                     │
    │    - Supply Crate (102,18)                                │
    │    - Tutorial trigger (88,18)                             │
    │    - "Arrival Board Lies" (96,22)                         │
    │                                                           │
    │    ═══════════════════════════════════════════            │
    │                                                           │
    │    DISTRICT 2: Pylon Yard (Calibration Zone)              │
    │    (x 52–124, y 16–40)                                    │
    │                                                           │
    │    Phase Gate Pylon (88,26) ════►                         │
    │    ├─ Choose: PAST / PRESENT / FUTURE                     │
    │    ├─ Span Threshold (88,36) — auto-dismount              │
    │    └─ Reset Pedestal (76,24)                              │
    │                                                           │
    │    Maintenance Walk Entrance (58,34) ──┐                  │
    │                                          ▼                  │
    │    DOMINION SILHOUETTE [PHASE 1+] (60,28)                 │
    │                                                           │
    │    ═══════════════════════════════════════════            │
    │                                                           │
    │    DISTRICT 3: Phase Span (Three-Lane Bridge)             │
    │    (x 30–150, y 34–64)                                    │
    │                                                           │
    │    ┌─────────┬─────────┬─────────┐                        │
    │    │  PAST   │ PRESENT │ FUTURE  │                        │
    │    │  Lane   │  Lane   │  Lane   │                        │
    │    │ (left)  │(center) │ (right) │                        │
    │    │         │  [gap]  │ [flicker│                        │
    │    │[barrier]│         │ +stasis]│                        │
    │    └─────────┴─────────┴─────────┘                        │
    │                                                           │
    │    Phase Gate at (88,26) controls all lanes               │
    │    Buoy breadcrumbs every ~10 tiles                       │
    │    Anchor Pads on each lane for safety                    │
    │                                                           │
    │    Side loop: (58,34) → (22,46) chest / (20,50) lore      │
    │                                                           │
    │    ═══════════════════════════════════════════            │
    │                                                           │
    │    DISTRICT 4: Crossing Shore (Exit Platform)             │
    │    (x 120–176, y 50–80)                                   │
    │                                                           │
    │    Exit to Overworld: (172,70) ═══════════════►           │
    │                                                           │
    │    Hidden Pocket Exit [locked]: (0,44)                    │
    │                                                           │
    │    ═══════════════════════════════════════════            │
    │                                                           │
    │    GATHERING NODES:                                       │
    │    - Buoycore Brass (70,40)                               │
    │    - Clocksteel Filings (118,52)                          │
    │    - Paradox Glass (34,58)                                │
    │    - Aurora Cache [night] (26,70)                         │
    │                                                           │
    └───────────────────────────────────────────────────────────┘
```

**Key Anchors Summary:**

| Feature | Coordinates |
|---------|-------------|
| **Chronowake Exit** | (88, 0) |
| **Signpost Cluster** | (90, 10) |
| **Tutorial Trigger** | (88, 18) |
| **Supply Crate** | (102, 18) |
| **Arrival Board** | (96, 22) |
| **Phase Gate Pylon** | (88, 26) |
| **Reset Pedestal** | (76, 24) |
| **Dominion Silhouette** | (60, 28) |
| **Maintenance Walk Entrance** | (58, 34) |
| **Side Loop Chest** | (22, 46) |
| **Lore Plaque** | (20, 50) |
| **Span Threshold** | (88, 36) |
| **Buoycore Brass** | (70, 40) |
| **Clocksteel Filings** | (118, 52) |
| **Paradox Glass** | (34, 58) |
| **Aurora Cache** [night] | (26, 70) |
| **Phase-Lane Exit** | (172, 70) |
| **Hidden Pocket** [locked] | (0, 44) |
