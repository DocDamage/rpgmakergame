# Chroma's Edge — Cinderstep to Skyspire Temple Transition Map Sheet (v1)
## Ember Stair Approach — "The mountain is alive, the air is hot, and the temple is already singing"

---

## 0) Map Technical Specs

| Parameter | Value |
|-----------|-------|
| **Map Name** | Ember Stair Approach |
| **Type** | Field Transition Micro-Map |
| **Purpose** | Bridge from Cinderstep town into Skyspire Temple (D4) dungeon |
| **Size** | 160 × 80 tiles |
| **Pixel Dimensions** | 2560 × 1280 px (16×16 px tiles) |
| **Encounters** | ON |
| **Encounter Band** | Lv 20–30 (scales to Lv 40 on revisit) |
| **Time States** | Day / Night |
| **Mounts** | Allowed (D3+) — 0% encounter rate while mounted |
| **Path Restriction** | Narrow stair lanes + steam bursts discourage speed running |

---

## 1) Core Intent

1. **Transition** from "town safety" into "temple danger" with vertical climb feel
2. **Teach Heat Gauge basics gently** before D4 proper
3. **Add 1 optional loop** for coolant loot + lore
4. **Foreshadow Dominion presence** as "permits + surveillance," not open warfare

---

## 2) Visual Identity

| Element | Description |
|---------|-------------|
| **Terrain** | Basalt steps, broken stair terraces, copper pipe rails, vent grates |
| **Ambient** | Low furnace hum + periodic exhale steam roar every ~18 seconds |

### Landmarks

| Landmark | Description |
|----------|-------------|
| **Spire Silhouette** | Visible from bottom third of map |
| **Cooling Trough Shrine** | Local survival tech, safe node |
| **Heat Hymn Bell** | Stone bell that pulses light on rhythm |
| **Dominion Permit Stakes** | Phase-based set dressing |

---

## 3) Layout Blocks (Districts)

### District 1: Ventgate Ramp (Safe Apron)

| Property | Value |
|----------|-------|
| **Bounds** | x 64–96, y 0–14 |
| **Encounters** | OFF for first ~8 tiles |
| **Features** | Signposts + tutorial hint object |

### District 2: Basalt Switchbacks (Main Climb)

| Property | Value |
|----------|-------|
| **Bounds** | x 46–124, y 14–52 |
| **Features** | Zig-zag stair lanes with 2 choke points and 1 side overlook |

### District 3: Steamcut Ledges (Heat Preview Zone)

| Property | Value |
|----------|-------|
| **Bounds** | x 20–70, y 26–62 |
| **Features** | Vent grates + Heat Gauge preview + coolant pickups |

### District 4: Spire Threshold (Dungeon Gate)

| Property | Value |
|----------|-------|
| **Bounds** | x 96–160, y 48–80 |
| **Features** | Architecture shifts from "mountain" to "temple"; huge arch frames D4 entrance |

---

## 4) Entrances / Exits (Edge Triggers)

Local coords (0–159, 0–79)

| Exit To | Coordinates | Notes |
|---------|-------------|-------|
| **Cinderstep Town** | (80, 0) | South edge |
| **Skyspire Temple (D4) Entry** | (156, 70) | East edge |
| **Overworld Ridge Pass** (optional) | (0, 38) | West edge, locked until post-D4 or sidequest |

---

## 5) Navigation Props & Anchors

| Prop | Coordinates | Function |
|------|-------------|----------|
| **Signpost Cluster** | (82, 10) | "CINDERSTEP" (back) / "SKYSPIRE" (up) / "RIDGE PASS" (west, locked) |
| **Cooling Trough** (safe node) | (58, 44) | Safe node, health regen |
| **Heat Hymn Bell** | (110, 58) | Pulses in sync with dungeon rhythm |
| **Vent Valve** (preview interact) | (72, 40) | Reduces a hot lane for 30s |

---

## 6) Mechanics

### A) Heat Gauge Preview (Soft)

| Aspect | Description |
|--------|-------------|
| **Active Zones** | Steamcut Ledges + Spire Threshold |
| **Build Rate** | ~50% of full dungeon rate |
| **Warm Threshold** | Tiny MP regen down |
| **Hot Threshold** | Tiny chip damage every ~10 seconds (optional debuff only variant) |

### B) Steam Burst Hazards (Timed)

| Property | Description |
|----------|-------------|
| **Cycle** | ~18 seconds |
| **Trigger** | Standing on vent grate when it exhales |
| **Effect** | Knockback 1 tile + burn buildup (small) |
| **Telegraph** | Sound + 1-second glow warning |

### C) Vent Valve Tutorial

| Property | Description |
|----------|-------------|
| **Location** | (72, 40) |
| **Effect** | Redirects steam, opens safe crossing lane |
| **Duration** | 30 seconds |
| **Teaching** | Introduces "valves matter" concept before D4 puzzles |

---

## 7) Scripted Events

### A) One-Time "Temple Sings" Beat

| Property | Value |
|----------|-------|
| **Trigger Tile** | (96, 30) — first clear view of spire silhouette |
| **Event** | Low hum rises; torches flare in rhythm |
| **UI Tip** | "Heat responds to the Spire's pulse." |

### B) Dominion Permit Check (Non-Combat Tension)

| Property | Value |
|----------|-------|
| **Active** | PHASE 1+ (Dominion pressure), Day only |
| **NPC Anchor** | (92, 18) |
| **Dialogue** | "No permit? Don't linger." |
| **Outcome** | No fight, just hostility + adds signage |

### C) Night Silhouette Patrol (No Forced Combat)

| Property | Value |
|----------|-------|
| **Active** | Night only, PHASE 1+ |
| **Silhouette Anchor** | (126, 54) |
| **Behavior** | If approached, backs away into steam (foreshadow) |

---

## 8) Encounters & Zones

### Base Spawn Table (Lv 20–30)

| Enemy | Traits |
|-------|--------|
| **Ash Stalkers** | Ambush; weak to water/tide |
| **Cinder Wisps** | Burn buildup |
| **Forge Scarabs** | Armor up; drops upgrade mats |
| **Vent Skulkers** | Knockback attacks |

### Encounter Zones

| Zone | Bounds | Type |
|------|--------|------|
| **Zone A** (light) | x 56–110, y 16–30 | Basalt Switchbacks lower half |
| **Zone B** (main) | x 34–120, y 30–58 | Switchbacks upper half + Steamcut |
| **Zone C** (harder) | x 104–160, y 54–78 | Spire Threshold (slightly higher rate) |

---

## 9) Salvage / Gathering Nodes

### Always-On Nodes (respawn daily or per load)

| Node | Coordinates | Loot |
|------|-------------|------|
| **Ash Resin Lump** | (44, 56) | Craft mat |
| **Copper Pipe Scrap** | (88, 34) | Upgrade mat |
| **Coolant Flask Pickup** | (60, 46) | 1× Coolant Pod (low chance) |

### Night-Only Risk Node

| Node | Coordinates | Conditions | Loot |
|------|-------------|------------|------|
| **Abandoned Supply Crate** | (18, 60) | Night only, PHASE 1+ | Coolant Pod ×1 + chance "Heatguard Cloth" |

---

## 10) Secrets & Optional Loop

### A) Overlook Ledge → Lore Tablet

| Step | Coordinates | Description |
|------|-------------|-------------|
| Ramp up | (40, 22) → | Small staircase |
| Ledge | → (30, 16) | Overlook point |
| Lore tablet | (24, 14) | "Heat was meant to temper. Dominion used it to brand." |

### B) Cooling Alcove Shortcut (QoL)

| Property | Description |
|----------|-------------|
| **Hidden Path** | Behind pipe rack at (66, 52) |
| **Emerge Point** | (98, 44) |
| **Benefit** | Bypasses a steam burst choke once noticed |

### C) Optional Chest

| Property | Value |
|----------|-------|
| **Location** | (22, 32) |
| **Loot** | Heat Buffer Kit (consumable) OR Coolant Pods ×2 |

---

## 11) Story-State Phases (Set Dressing + Difficulty)

### PHASE 0 — First Approach (pre-D4)

| Aspect | State |
|--------|-------|
| Atmosphere | Few permit stakes, more climbers, "hard but fair" vibe |
| Heat Preview | Mild |
| NPCs | Friendly climbers, local guides |

### PHASE 1 — Dominion Pressure Rising

| Aspect | State |
|--------|-------|
| Atmosphere | Permit boards, patrol silhouettes, harsher signage |
| Encounters | Slightly increased frequency near Threshold |
| NPCs | Dominion permit inspector, wary locals |

### PHASE 2 — Post-D4 Clear

| Aspect | State |
|--------|-------|
| Visual Reward | Vents pulse steadier; fewer steam bursts |
| Signage | Banner: "PATH STABILIZED" (local pride) |
| Heat Preview | Reduced |

### PHASE 3 — Mid/Late Revisit

| Aspect | State |
|--------|-------|
| Optional Spawn | Mini-elite: "Purifier Scout" in Zone C at night |
| Loot | "Tempered Seal" mat (forge tier) |

---

## 12) Implementation Notes

1. **Visibility:** Keep D4 entrance arch visible from top half (player always knows "up")
2. **Telegraphing:** Steam bursts must have audio + visual warning
3. **Safety:** Knockback must never chain into unavoidable damage—always provide safe tiles nearby
4. **Phase Triggers:** Document which global flags toggle each phase for QA testing

---

## Quick Reference Map Overview

```
                    NORTH
                      ↑
    ┌─────────────────────────────────────────────────────────┐
    │                                                         │
    │  DISTRICT 3: Steamcut Ledges              DISTRICT 4:   │
    │  (x 20–70, y 26–62)                      Spire Threshold│
    │  - Vent grates + Heat preview            (x 96–160)     │
    │  - Coolant pickups                         - D4 arch    │
    │                                                          │
    │  OVERLOOK (22,32)──Chest     COOLING SHORTCUT (66,52)──►│
    │       │                          │                    │
    │       └──Lore tablet (24,14)     │                    │
    │                                  ▼                    │
    │                          EMERGENCE (98,44)            │
    │                                                       │
    │  ┌───────────────────────────────────────────────┐   │
    │  │         DISTRICT 2: Basalt Switchbacks        │   │
    │  │      (x 46–124, y 14–52) zig-zag climb       │   │
    │  │                                               │   │
    │  │    Zone A (light)        Zone B (main)       │   │
    │  │   (lower half)           (upper half)        │   │
    │  └───────────────────────────────────────────────┘   │
    │                        │                              │
    │  DISTRICT 1: Ventgate Ramp                           │
    │  (x 64–96, y 0–14) — Safe apron                      │
    │  Signs at (82,10): "CINDERSTEP" ← "SKYSPIRE" ↑       │
    │                        │                              │
    └────────────────────────┼──────────────────────────────┘
                             │
                      EXIT: Cinderstep Town (80, 0)
```

**Key Anchors Summary:**

| Feature | Coordinates |
|---------|-------------|
| **Cinderstep Exit** | (80, 0) |
| **Skyspire Temple Entrance** | (156, 70) |
| **Signpost Cluster** | (82, 10) |
| **Cooling Trough (Safe)** | (58, 44) |
| **Vent Valve (Tutorial)** | (72, 40) |
| **Steam Burst Tiles** | x 20–70, y 26–62 |
| **Chest** | (22, 32) |
| **Lore Tablet** | (24, 14) |
| **Heat Hymn Bell** | (110, 58) |
| **Night Silhouette** | (126, 54) |
| **Abandoned Supply Crate** | (18, 60) |
