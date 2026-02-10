# Chroma's Edge — Brinegate to Abyss Entry Pier Transition Map Sheet (v1)
## Stormcage Pier — "The Last Dry Breath"

---

## 0) Map Technical Specs

| Parameter | Value |
|-----------|-------|
| **Map Name** | Stormcage Pier |
| **Type** | Field Transition Micro-Map (Brinegate → D5 approach) |
| **Size** | 160 × 72 tiles (2560 × 1152 px) |
| **Encounters** | ON (light near town) |
| **Encounter Band** | Lv 28–38 (scales to Lv 48 on revisit) |
| **Time States** | Day / Night |
| **Day Atmosphere** | Workers, busy cranes, prep activity |
| **Night Atmosphere** | Harsher wind, fewer workers, more Dominion silhouettes |
| **Mounts** | Allowed (D3+) but disabled on most piers; only on upper breakwater approach lane (optional shortcut) |

---

## 1) Core Intent

1. **Ritual ramp** from Brinegate → D5 with strong "port-to-deep" transition
2. **Teach Pressure Gauge** concept before entering D5 proper
3. **Small prep interactions:** equalizer station, supply crate, dive bell visuals
4. **Dominion tension** through customs + surveillance, not combat spam

---

## 2) Visual Identity

| Element | Description |
|---------|-------------|
| **Terrain** | Breakwater stones → wet planks → crane platforms → dive bell gantry |
| **Ambient** | Wave slam, gulls, chain clanks, sonar pings, distant low-frequency hum |

### Landmarks

| Landmark | Description |
|----------|-------------|
| **Storm Lantern Line** | Amber lights leading outward |
| **Sonar Bell Buoy** | Pings sync with distant "deep" groan |
| **Dive Cage Cranes** | Hanging over black water |
| **Airlock Door** | Framed by coral-stained metal ribs |

---

## 3) Layout Blocks (Districts)

### District 1: Breakwater Walk (Safe Apron)

| Property | Value |
|----------|-------|
| **Bounds** | x 54–106, y 0–14 |
| **Encounters** | OFF for first ~10 tiles |
| **Features** | Signposts, workers, prep hints |

### District 2: Crane Yard (Industrial Spine)

| Property | Value |
|----------|-------|
| **Bounds** | x 38–130, y 14–40 |
| **Features** | Wide turning pads, scaffolds, 2 optional loops for loot/gear |

### District 3: Storm Planks (Tight Pier Lane)

| Property | Value |
|----------|-------|
| **Bounds** | x 78–160, y 34–60 |
| **Features** | Narrower navigation, wave spray VFX, "commitment" vibe |

### District 4: Blackwater Threshold (Descent Gate)

| Property | Value |
|----------|-------|
| **Bounds** | x 120–160, y 56–72 |
| **Features** | Darker water, quieter, sound design shifts |

---

## 4) Entrances / Exits (Edge Triggers)

Local coords (0–159, 0–71)

| Exit To | Coordinates | Notes |
|---------|-------------|-------|
| **Brinegate Port** (town) | (80, 0) | North edge |
| **Abyss Entry Pier / D5 Airlock** | (156, 66) | East edge |
| **Coastal Overworld Node** (optional) | (0, 20) | West edge, locked until post-D5 or shipwright sidequest |

---

## 5) Key Anchors & Navigation Props

| Prop | Coordinates | Function |
|------|-------------|----------|
| **Signpost Cluster** | (82, 10) | "BRINEGATE" ← / "STORMCAGE PIER" ↑ / "COAST NODE" → (west, locked) |
| **No Mounts Sign + Gate Chain** | (96, 34) | Hard stops mounts from entering Storm Planks |
| **Sonar Buoy** (interactive) | (62, 18) | Plays ping + lore line; changes after D5 (calmer) |
| **Equalizer Station** (preview) | (44, 30) | Reduces Pressure Preview bar; teaches mechanic |
| **Supply Crate** (prep, 1-time) | (108, 26) | Pressure Patch ×1 + Silence Salts ×1 |

---

## 6) Mechanics

### A) Pressure Preview Bar (Soft)

| Aspect | Description |
|--------|-------------|
| **Active Zones** | Storm Planks + Blackwater Threshold |
| **Fill Rate** | ~25–30% of D5 speed |
| **Pressurized Threshold** | MP regen down |
| **Crush Threshold** (rare) | Tiny chip damage every ~12 seconds (optional) |

### B) Wave Spray Lanes (Timed Hazard, Non-lethal)

| Property | Description |
|----------|-------------|
| **Trigger** | Specific edge tiles |
| **Effect** | Knocks party 1 tile back |
| **Telegraph** | Foam + sound warning |
| **Purpose** | Make pier feel alive without being annoying |

### C) Rope Cleats (Safe Pads)

| Property | Description |
|----------|-------------|
| **Function** | Safe tiles where wave knockback can't trigger |
| **Purpose** | Helps readability and fairness |

---

## 7) Scripted Events

### A) One-Time "Last Dry Breath" Beat

| Property | Value |
|----------|-------|
| **Trigger Tile** | (92, 38) — first step onto Storm Planks |
| **Event** | Audio dips, sonar ping, water looks too black |
| **UI Tip** | "Pressure rises deeper—equalize when you can." |

### B) Dominion Customs Glimpse (No Forced Combat)

| Property | Value |
|----------|-------|
| **Active** | PHASE 1+ (Dominion pressure), Day only |
| **NPC Anchor** | (30, 22) |
| **Dialogue** | "Cargo sealed. Don't go where you're not charted." |
| **Outcome** | Leaves; adds permit placard prop after |

### C) Night Watcher Silhouette (Tension Only)

| Property | Value |
|----------|-------|
| **Active** | Night only, PHASE 1+ |
| **Silhouette Anchor** | (122, 44) — between crane shadows |
| **Behavior** | If approached, withdraws behind crane (no fight) |

---

## 8) Encounters & Zones

### Base Spawn Table (Lv 28–38)

| Enemy | Traits |
|-------|--------|
| **Glowjellies** | Silence chance |
| **Brine Leeches** | Poison |
| **Silt Skitters** | Fast |
| **Crane Skulkers** | Ambush; physical attacks |
| **Sonar Drone (Damaged)** | Rare mini-elite, PHASE 1+ |

### Encounter Zones

| Zone | Bounds | Type |
|------|--------|------|
| **Zone A** (light) | x 50–120, y 18–34 | Crane Yard edges |
| **Zone B** (main) | x 88–160, y 38–58 | Storm Planks |
| **Zone C** (harder) | x 128–160, y 58–71 | Blackwater Threshold |

---

## 9) Salvage / Gathering Nodes (Prep Value)

### Always-On Nodes

| Node | Coordinates | Loot |
|------|-------------|------|
| **Rope Bundle** | (74, 28) | Rope kit mat |
| **Saltglass Chunk** | (132, 56) | Brinecraft mat |
| **Oil Rag Cache** | (52, 36) | Sellable / craft |

### Night-Only Risk Node

| Node | Coordinates | Conditions | Loot |
|------|-------------|------------|------|
| **Fell Overboard Crate** | (150, 52) | Night only, PHASE 1+ | Pressure Patch ×1 + chance "Brineguard Cloth" |

---

## 10) Secrets & Optional Loop

### A) Crane Catwalk Loop (Loot + Lore)

| Step | Coordinates | Description |
|------|-------------|-------------|
| Ramp up | (60, 22) | Catwalk route start |
| Drop down | → (96, 18) | Return to main path |
| **Chest** | (78, 14) | "Storm Lantern" (anti-ambush consumable) |
| **Lore plaque** | (78, 12) | "Deep pings not matching Dominion charts" |

### B) Under-Pier Crawlspace (Shortcut)

| Property | Description |
|----------|-------------|
| **Entrance** | (118, 34) |
| **Exit** | (140, 58) |
| **Benefit** | Bypasses one wave-spray lane |

---

## 11) Story-State Phases (Set Dressing + Difficulty)

### PHASE 0 — First Time (pre-D5)

| Aspect | State |
|--------|-------|
| Atmosphere | Busy cranes, divers prepping, pressure preview mild |
| Dominion Presence | Minimal |

### PHASE 1 — Dominion Pressure Rising

| Aspect | State |
|--------|-------|
| Atmosphere | Permit placards appear, watcher silhouettes |
| Encounters | Slightly more drones at night |

### PHASE 2 — Post-D5 Clear

| Aspect | State |
|--------|-------|
| Atmosphere | Sonar pings feel calmer, fewer "black water" distortions |
| Mechanics | Pressure preview fills slower (visual reward: stabilized tides) |

### PHASE 3 — Mid/Late Revisit

| Aspect | State |
|--------|-------|
| Optional Spawn | Mini-elite: "Deepwright Stolen Drone" in Zone C |
| Loot | High-tier brine mat |

---

## 12) Implementation Notes

1. **Airlock visibility:** Door should be visible from ~15 tiles away once on Storm Planks (strong "commitment" pull)
2. **Wave spray safety:** Never chain into unavoidable damage; cleats must be frequent
3. **Pressure preview:** Teach, not punish—keep it mild and readable

---

## Quick Reference Map Overview

```
                        NORTH
                          ↑
    ┌───────────────────────────────────────────────────────────┐
    │                                                           │
    │        DISTRICT 1: Breakwater Walk                        │
    │        (x 54–106, y 0–14)                                 │
    │        - Safe apron, encounters OFF first 10 tiles        │
    │        - Signpost (82,10): "BRINEGATE" ←                  │
    │                                                           │
    │    ═══════════════════════════════════════════            │
    │                                                           │
    │        DISTRICT 2: Crane Yard (Industrial Spine)          │
    │        (x 38–130, y 14–40)                                │
    │                                                           │
    │    Equalizer    Crane       Catwalk Loop (60,22)──►       │
    │    Station      Yard        Chest (78,14)                 │
    │    (44,30)      x                                           │
    │        │     Supply   Sonar Buoy (62,18)                  │
    │        │     Crate    │                                   │
    │        │    (108,26)  │                                   │
    │        ▼              ▼                                   │
    │    Rope Bundle     CUSTOMS NPC (30,22) [PHASE 1+]         │
    │    (74,28)                                                │
    │                                                           │
    │    ═══════════════════════════════════════════            │
    │                                                           │
    │        DISTRICT 3: Storm Planks (Tight Pier Lane)         │
    │        (x 78–160, y 34–60)                                │
    │                                                           │
    │    NO MOUNTS GATE (96,34) ════►                           │
    │        │                                                  │
    │    "Last Dry Breath" Trigger (92,38)                      │
    │        │                                                  │
    │    WAVE SPRAY LANES + ROPE CLEATS                         │
    │        │                                                  │
    │    Under-Pier Crawlspace: (118,34) → (140,58)             │
    │        │                                                  │
    │        ▼                                                  │
    │    ═══════════════════════════════════════════            │
    │                                                           │
    │        DISTRICT 4: Blackwater Threshold (Descent Gate)    │
    │        (x 120–160, y 56–72)                               │
    │                                                           │
    │    Saltglass Chunk (132,56)                               │
    │    Fell Overboard Crate (150,52) [night/PHASE 1+]         │
    │    WATCHER SILHOUETTE (122,44) [night/PHASE 1+]           │
    │        │                                                  │
    │        ▼                                                  │
    │    AIRLOCK DOOR → Abyssal Trench D5 (156,66)              │
    │                                                           │
    └───────────────────────────────────────────────────────────┘
```

**Key Anchors Summary:**

| Feature | Coordinates |
|---------|-------------|
| **Brinegate Exit** | (80, 0) |
| **Signpost Cluster** | (82, 10) |
| **Sonar Buoy** | (62, 18) |
| **Crane Catwalk Ramp** | (60, 22) |
| **Chest (Storm Lantern)** | (78, 14) |
| **Equalizer Station** | (44, 30) |
| **Rope Bundle** | (74, 28) |
| **Supply Crate** | (108, 26) |
| **No Mounts Gate** | (96, 34) |
| **"Last Dry Breath" Trigger** | (92, 38) |
| **Customs NPC** [PHASE 1+] | (30, 22) |
| **Under-Pier Entrance** | (118, 34) |
| **Under-Pier Exit** | (140, 58) |
| **Watcher Silhouette** [night] | (122, 44) |
| **Saltglass Chunk** | (132, 56) |
| **Fell Overboard Crate** [night] | (150, 52) |
| **D5 Airlock Door** | (156, 66) |
| **Coastal Node Exit** [post-D5] | (0, 20) |
