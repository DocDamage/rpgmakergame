# Chroma's Edge — Rimehold to Frozen Citadel Transition Map Sheet (v1)
## Rime Causeway — "From Winter to Stasis With Intent"

---

## 0) Map Technical Specs

| Parameter | Value |
|-----------|-------|
| **Map Name** | Rime Causeway |
| **Type** | Field Transition Micro-Map (Rimehold → D7 approach) |
| **Size** | 176 × 80 tiles (2816 × 1280 px) |
| **Encounters** | ON (light near town) |
| **Encounter Band** | Lv 58–70 (scales to Lv 82 on revisit) |
| **Time States** | Day / Night |
| **Day Atmosphere** | Snow, wind, distant bell |
| **Night Atmosphere** | Denser fog + aurora bands + more "frame-skip" VFX |
| **Mounts** | Allowed (D3+) — 0% encounter rate while mounted; auto-dismount at Phase Threshold Gate |

---

## 1) Core Intent

1. **Transition** from "warm town" to "time-stained ice" with strong tone shift
2. **Teach Phase Shift** (Past/Present/Future) once in a safe, obvious way
3. **Preview Stasis Fields** (mild) without punishing the player
4. **Give 1 optional loop** with Time mats + lore + a shortcut for revisits

---

## 2) Visual Identity

| Element | Description |
|---------|-------------|
| **Terrain** | Stone road → snow-packed causeway → ice bridge plates → fractured citadel forecourt |
| **Ambient** | Wind + distant bell + occasional "reverse snow" drifting upward |

### Landmarks

| Landmark | Description |
|----------|-------------|
| **Heat Pipe Line** | From Rimehold (warm steam) that fades out mid-map |
| **Frozen Mile Marker Clocks** | Hands twitch at night |
| **Chrono Altar** | First phase shift interactable |
| **Citadel Silhouette** | Visible from middle third onward |

---

## 3) Layout Blocks (Districts)

### District 1: Hearthline Outwalk (Safe Apron)

| Property | Value |
|----------|-------|
| **Bounds** | x 70–108, y 0–14 |
| **Encounters** | OFF for first ~10 tiles |
| **Features** | Signpost + "last warm" props (steam pipe, lanterns) |

### District 2: Snowspan Bridge (Main Route)

| Property | Value |
|----------|-------|
| **Bounds** | x 52–140, y 14–44 |
| **Features** | Straight lane with broken spans and mild stasis patches |

### District 3: Clockbreak Bend (Phase Tutorial Zone)

| Property | Value |
|----------|-------|
| **Bounds** | x 24–92, y 32–70 |
| **Features** | First Chrono Altar; optional side loop branches here |

### District 4: Citadel Forecourt (Threshold)

| Property | Value |
|----------|-------|
| **Bounds** | x 112–176, y 44–80 |
| **Features** | Progenitor stone + ice ribs + time shimmer; D7 entry gate clearly framed |

---

## 4) Entrances / Exits (Edge Triggers)

Local coords (0–175, 0–79)

| Exit To | Coordinates | Notes |
|---------|-------------|-------|
| **Rimehold Town** | (88, 0) | North edge |
| **Frozen Citadel (D7)** Entry | (172, 70) | East edge |
| **Phase Barrier Pass** [post-D7] | (0, 40) | West edge, locked until Time seated |

---

## 5) Key Anchors & Navigation Props

| Prop | Coordinates | Function |
|------|-------------|----------|
| **Signpost Cluster** | (90, 10) | "RIMEHOLD" ← / "FROZEN CITADEL" ↑ / "PHASE PASS" → (west, locked) |
| **Heat Pipe Breakpoint** | (88, 22) | Steam line ends; air looks "dry" despite snow |
| **First Chrono Altar** (tutorial) | (62, 54) | "Shift Phase?" — defaults to PRESENT |
| **Phase Threshold Gate** | (126, 54) | Triple-prong pylon; mount dismount point |
| **Stasis Field Preview Strip** | x 104–122, y 34 | Mild buildup; avoidable via side snowbank lane |

---

## 6) Mechanics

### A) Phase Shift (One Clean Tutorial)

**Required once to progress:**

| Element | Description |
|---------|-------------|
| **Location** | Around (96, 40) |
| **PAST** | Bridge intact (crossable) |
| **PRESENT** | Bridge cracked (not crossable) |
| **FUTURE** | Bridge collapsed |

**Lesson:** Use Chrono Altar to shift to PAST to cross.

### B) Stasis Field Preview (Soft)

| Aspect | Description |
|--------|-------------|
| **Active Zones** | Snowspan Bridge and Forecourt |
| **Build Rate** | ~35–40% of D7 intensity |
| **Counterplay** | Warm Stone Plates every ~8–10 tiles |

### C) "Time Static" (Flavor)

| Aspect | Description |
|--------|-------------|
| **Trigger** | Night only |
| **Effect** | Occasional "frame skip" visual pulse |
| **Gameplay Impact** | None — pure atmosphere |

---

## 7) Scripted Events

### A) One-Time "Hands Move Wrong" Beat

| Property | Value |
|----------|-------|
| **Trigger** | (76, 30) — first clock marker |
| **Event** | Clock hand ticks backward once |
| **Party Line** (optional) | "That… was backward." |

### B) Phase Tutorial Prompt (One-Time)

| Property | Value |
|----------|-------|
| **Trigger** | Entering Clockbreak Bend (60, 48) |
| **Event** | Tooltip: "Chrono Altars shift the world's phase." |

### C) Dominion Glimpse (Tension Only)

| Property | Value |
|----------|-------|
| **Active** | PHASE 1+ (pressure rising), Day only |
| **Silhouette Anchor** | (40, 18) near west path sign |
| **Behavior** | If approached: leaves; adds "compliance seal" placard next visit |

---

## 8) Encounters & Zones

### Base Spawn Table (Lv 58–70)

| Enemy | Traits |
|-------|--------|
| **Rime Stalkers** | Ambush + stasis buildup |
| **Chrono Wisps** | Speed/initiative debuffs |
| **Frost Sentinels** | Slow, tanky |
| **Hourglass Mites** | Annoying debuffers |
| **Dominion Chrono Surveyor** | Rare, PHASE pressure flags |

### Encounter Zones

| Zone | Bounds | Type |
|------|--------|------|
| **Zone A** (light) | x 70–110, y 10–18 | Hearthline Outwalk edge |
| **Zone B** (main) | x 70–150, y 18–44 | Snowspan Bridge |
| **Zone C** (harder) | x 120–176, y 52–78 | Forecourt |

---

## 9) Salvage / Gathering Nodes

### Always-On Nodes

| Node | Coordinates | Loot |
|------|-------------|------|
| **Clocksteel Filing Pile** | (118, 28) | Timecraft mat |
| **Paradox Glass Shard** | (34, 62) | Rare-ish, 1 per visit chance |
| **Frost Resin** | (150, 60) | Craft mat |

### One-Time Prep Crate

| Node | Coordinates | Loot |
|------|-------------|------|
| **Supply Crate** | (82, 16) | Stasis Balm ×2 + Ether Drop ×1 |

### Night-Only Risk Node

| Node | Coordinates | Conditions | Loot |
|------|-------------|------------|------|
| **Aurora Cache** | (20, 70) | Night only | Chrono Band mat or rare filing bundle |

---

## 10) Secrets & Optional Loop

### A) "Old Watch Post" Side Loop (Lore + Loot)

| Step | Coordinates | Description |
|------|-------------|-------------|
| **Branch start** | (54, 58) | Near altar |
| **Lore Tablet** | (24, 64) | "The Citadel didn't freeze. It paused." |
| **Chest** | (18, 58) | Timeguard Wrap mat / Paradox Glass |

### B) Shortcut for Revisits (Post-D7)

| Property | Description |
|----------|-------------|
| **Shortcut crack** | (132, 38) — cracked wall becomes passable |
| **Exit point** | (160, 62) — near D7 gate |
| **Benefit** | Cuts traversal time on re-entry |

---

## 11) Story-State Phases (Set Dressing + Difficulty)

### PHASE 0 — First Approach (pre-D7)

| Aspect | State |
|--------|-------|
| Warm pipe line | Visible early |
| Clocks | Subtle |
| Stasis | Mild |

### PHASE 1 — Dominion Pressure Rising

| Aspect | State |
|--------|-------|
| Compliance seals | Appear |
| Surveyor | Occasional silhouette |
| Encounters | Slightly higher rate in Zone C |

### PHASE 2 — Post-D7 Clear

| Aspect | State |
|--------|-------|
| Stasis fields | Thin slightly |
| Clock hands | Stop "skipping" as often |
| Shortcut crack | Becomes active |

### PHASE 3 — Late Revisit

| Aspect | State |
|--------|-------|
| Optional spawn | Mini-elite: Paradox Warden Scout at night in Forecourt |
| Loot | Rare Time mat |

---

## 12) Implementation Notes

1. **D7 gate visibility:** Make visible from at least ~18 tiles away in Forecourt (strong pull)
2. **Phase tutorial bridge:** Unmissable — put it on the main path
3. **Stasis avoidance:** Provide "no-stasis" side lane for players who hate slow fields

---

## Quick Reference Map Overview

```
                        NORTH
                          ↑
    ┌───────────────────────────────────────────────────────────┐
    │                                                           │
    │    DISTRICT 1: Hearthline Outwalk                         │
    │    (x 70–108, y 0–14)                                     │
    │    - Signpost (90,10): "RIMEHOLD" ←                       │
    │    - Supply Crate (82,16)                                 │
    │    - Heat Pipe Breakpoint (88,22) ════►                   │
    │        Steam ends here                                    │
    │                                                           │
    │    ═══════════════════════════════════════════            │
    │                                                           │
    │    DISTRICT 2: Snowspan Bridge      DISTRICT 3:           │
    │    (x 52–140, y 14–44)            Clockbreak Bend         │
    │    - Main route                   (x 24–92, y 32–70)      │
    │    - Stasis preview strip         - Chrono Altar (62,54)  │
    │    - Clock marker (76,30)         - Clock ticks backward  │
    │        "Hands move wrong"         - Old Watch Post branch │
    │    - Paradox Glass (34,62)          ├─ Lore (24,64)       │
    │                                       └─ Chest (18,58)    │
    │    ═══════════════════════════════                        │
    │                                                           │
    │    DISTRICT 4: Citadel Forecourt                          │
    │    (x 112–176, y 44–80)                                   │
    │                                                           │
    │    Phase Threshold Gate (126,54)                          │
    │    ├─ Triple-prong pylon                                  │
    │    ├─ Mount auto-dismount                                 │
    │    └─ "Time interference" flavor                          │
    │                                                           │
    │    Frost Resin (150,60)                                   │
    │    Clocksteel Filing (118,28)                             │
    │                                                           │
    │    SHORTCUT CRACK [post-D7] (132,38) →► (160,62)          │
    │                                                           │
    │    D7 ENTRY GATE (172,70) ═══════════════►                │
    │                                                           │
    │    DOMINION SILHOUETTE [PHASE 1+] (40,18)                 │
    │    AURORA CACHE [night] (20,70)                           │
    │    PHASE PASS EXIT [post-D7] (0,40)                       │
    │                                                           │
    └───────────────────────────────────────────────────────────┘
```

**Key Anchors Summary:**

| Feature | Coordinates |
|---------|-------------|
| **Rimehold Exit** | (88, 0) |
| **Signpost Cluster** | (90, 10) |
| **Supply Crate** | (82, 16) |
| **Heat Pipe Breakpoint** | (88, 22) |
| **Clock Marker** | (76, 30) |
| **Chrono Altar** | (62, 54) |
| **Paradox Glass** | (34, 62) |
| **Old Watch Post Entrance** | (54, 58) |
| **Lore Tablet** | (24, 64) |
| **Watch Post Chest** | (18, 58) |
| **Aurora Cache** [night] | (20, 70) |
| **Dominion Silhouette** | (40, 18) |
| **Phase Threshold Gate** | (126, 54) |
| **Clocksteel Filing** | (118, 28) |
| **Frost Resin** | (150, 60) |
| **Shortcut Crack** [post-D7] | (132, 38) → (160, 62) |
| **D7 Entry Gate** | (172, 70) |
| **Phase Barrier Pass** [post-D7] | (0, 40) |
