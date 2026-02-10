# Chroma's Edge — Dusthaven Town Map Sheet (v1)
## Starting Hub — "Scrap-Built Freedom"

---

## A) Technical Specs

| Parameter | Value |
|-----------|-------|
| Town Map Size | 96 × 96 tiles |
| Tile Size | 16×16 px |
| Full Texture | 1536×1536 px |
| Camera | Standard JRPG town camera (top-down / slight angle) |
| Encounter Rate | 0% (town safe zone) |
| Time States | Day / Night versions (lighting + NPC schedule + Dominion patrol density) |
| Town Terminal | Yes (Lattice node, early-game "map grid" foreshadow) |

---

## B) Visual Identity (Art Direction)

### Materials
- Patched metal walls
- Scavenged ship plating
- Canvas tarps
- Welded pipe arches

### Color Palette
- Rust orange
- Soot gray
- Dusty tan
- Neon scraps (signs)
- Occasional cobalt glow (Lattice tech)

### Signature Props
- **Busted broadcast screen** (plays Dominion advisories)
- **Jukebox** that crackles more than it plays (scene flavor)
- **Windchimes** made of shell casings
- **Water tank tower** (town silhouette landmark)

---

## C) Town Layout (District Blocks)

### District 1 — Cantina Row (Social + Main Story)
- **Bounds:** x 34–62, y 38–58
- **Vibe:** Loud, cramped, "every deal is half a joke and half a knife"
- **Key Building:** Dusthaven Cantina (Scene 001)

### District 2 — Market Square
- **Bounds:** x 46–72, y 56–76
- **Vibe:** Stalls, barter, salvage, medicine table, rumor NPCs
- **Connects:** All major exits

### District 3 — Scrapline (Outskirts) (Renna Zone)
- **Bounds:** x 16–40, y 62–88
- **Vibe:** Stacked containers, tools, engines, sparks at night
- **Key Building:** Renna's Scrap Garage (Scene 004)

### District 4 — Waterworks + Shanties
- **Bounds:** x 62–88, y 26–54
- **Vibe:** Civilian life, water rationing, kids, small clinic tent
- **Dominion pressure shows here first** (posters, inspections)

### District 5 — Ironhawk Cut (Back-lot)
- **Bounds:** x 18–34, y 38–58
- **Vibe:** Quiet alley, "business happens here"
- **Leads to:** Hidden backroom entrance (Ironhawk Broker optional reappear)

---

## D) Key Map Anchors (Tile Coordinates)

*All coordinates are town-map local (0–95).*

### Main Spawn Points

| Spawn | Location | Coordinates | Context |
|-------|----------|-------------|---------|
| **SPAWN A** | First arrival / new game | (50, 70) | Market edge, visible Cantina sign |
| **SPAWN B** | Night return | (54, 54) | Cantina row |
| **SPAWN C** | After Ashveil outing | (24, 80) | Near Renna's Garage |

### Lattice Terminal (Town)

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Dusthaven Terminal** | (76, 44) | Small, damaged |
| **Locked until** | — | After Scene 001 (Kade sees broadcast first) |
| **After activation** | — | Enables "Town Map Grid" + optional fast travel later |

### Main Buildings (Exterior Door Tiles)

| Building | Door Coordinates |
|----------|------------------|
| **Dusthaven Cantina** | (52, 46) |
| **Renna's Scrap Garage** | (26, 78) |
| **Inn "The Rusty Cot"** | (60, 62) |
| **General Goods "Dust & Bolt"** | (64, 70) |
| **Weapon/Parts "Edgeworks Stall"** | (48, 72) |
| **Clinic Tent** (tiny) | (80, 50) |
| **Quest Board** | (58, 66) — Market Square, next to Inn |
| **Broadcast Screen** (Dominion advisories) | (46, 44) — Cantina exterior wall |

### Exits to Overworld (Edge Triggers)

| Exit | Direction | Edge Trigger | Destination |
|------|-----------|--------------|-------------|
| **North Gate** | North | (52, 10) | Ashveil Road |
| **East Gate** | East | (95, 62) | Prismridge Road |
| **SE Track** | Southeast | (88, 95) | Mirewatch / Swamp Road |
| **West Spur** | West | (0, 58) | Coast Road |

---

## E) Interior Maps (Required)

### 1) Dusthaven Cantina (Scene 001)
- **Interior Size:** 32×24
- **Key Props:**
  - Booth #3 (Ironhawk Broker meeting) at (18, 12)
  - Busted screen visible from booth (Dominion advisory)
  - Jukebox near back wall
- **NPC Anchors:** Bartender, 2 gamblers, 1 Dominion informant (optional)

### 2) Renna's Scrap Garage (Scene 004)
- **Interior Size:** 40×28
- **Signature Prop:** Welded container-to-container shop, half-dismantled bike lift
- **Interaction Nodes:**
  - **Workbench** (upgrade) — becomes available after Nix joins
  - **"Lattice burn"** inspection cut-in spot at center lift

### 3) Inn "The Rusty Cot"
- **Interior Size:** 28×20
- **Features:** Innkeeper, rest/save, rumor board

### 4) Ironhawk Backroom (Optional)
- **Interior Size:** 20×16
- **Hidden Entrance:** Via Ironhawk Cut alley
- **Used For:**
  - Early black-market items
  - Later "Broker check-in" dialogue after major beats

---

## F) Shops + Services (What's Available When)

### Base (Start / Pre-D1)

| Shop | Inventory |
|------|-----------|
| **General Goods** | Potions, basic cure, smoke bomb (escape), taming stones NOT yet |
| **Parts/Weapon Stall** | Basic upgrades + ammo packs |
| **Inn** | Rest + save |
| **Clinic Tent** | Status cures (limited) |

### After D1 (Growth Seat / Early Stabilization)

| Change | Details |
|--------|---------|
| **Clinic expands** | More cures available |
| **Quest board upgrades** | 2–3 new sidequests |
| **Dominion posters increase** | Visual escalation |

### After D3 (Taming Unlock in Crystal Caverns)

| New Feature | Location |
|-------------|----------|
| **Beast Handler Post** | (70, 78) near Market Square |
| **Stable access** | Mount cosmetics |
| **Behavior** | "Auto-stable mounts in town" |

*Matches mount system unlock timing from design doc.*

---

## G) NPC List (Placement + Function)

### Story-Critical

| NPC | Location | Notes |
|-----|----------|-------|
| **Ironhawk Broker** | Cantina booth at night | Vanishes after Scene 001 |
| **Renna Kyte** | Garage + later Market appearances | — |
| **Dominion Patrol Pair** | Outside Waterworks district at night | Increases over time |

### Utility NPCs

| NPC | Function |
|-----|----------|
| **Innkeeper** | Rest/save |
| **Parts Vendor** | Equipment |
| **Medic** | Healing/items |
| **Rumor Kid** | Points toward "Ashveil ruins feel wrong" |
| **Scrap Diver** | Introduces salvage / crafting |

### Flavor

| NPC Type | Details |
|----------|---------|
| **Gambler Trio** | — |
| **Jukebox Dancer** | — |
| **"Anti-Dominion Preacher"** | Quiet, not cult |

---

## H) Quest Hooks (Dusthaven-Specific)

### Main Story Hooks

| Quest | Scene | Trigger |
|-------|-------|---------|
| **"The Contract"** | Scene 001 | Triggers Ashveil Ruins route |
| **"Renna's Garage"** | Scene 004 | Party recruitment + Nix repair foreshadow |

### Sidequests (Early)

| Quest | Type | Reward |
|-------|------|--------|
| **Water Filter Run** | Fetch | Parts from Coast Spur wreckage |
| **Scrap Shipment** | Delivery | Unlock vendor discount at Prismridge |
| **Dominion Poster Sabotage** | Stealth-ish | Reputation + items |

### Sidequests (Later Return)

| Quest | Purpose |
|-------|---------|
| **Refugee Registry** | Ties postgame Halcyon tone early |
| **"Old Lattice Ping"** | Terminal flickers → tiny lore breadcrumb |

---

## I) Story-State Changes (Town "Phases")

Use these to swap NPCs + set dressing without rebuilding the whole map.

### PHASE 0 — Neutral Dusthaven
- Fewer patrols
- Normal market noise

### PHASE 1 — After Scene 001 (Dominion Broadcast Active)
- Broadcast screen loops advisories
- 1 patrol pair appears near Waterworks

### PHASE 2 — After Nix Arrives
- Renna's Garage gains upgrade options
- Cantina chatter shifts to "asset fugitive" rumors

### PHASE 3 — After D3 (Taming Unlock)
- Beast Handler Post appears
- Stable signage + "mount docking" spot added

### PHASE 4 — Late Game
- Dominion presence higher
- Optional "curfew" feel at night (more guards, fewer civilians outdoors)

---

## J) Collision / Navigation Notes

- **Market Square:** Keep open for readability (players shouldn't get stuck in clutter)
- **Scrap piles:** Soft blockers (1-tile gaps for secrets)
- **Ironhawk Cut:** Narrow but not maze-like (it's a vibe corridor)

---

## K) Secrets / Collectibles (Map-Ready)

| Secret | Location | Contents |
|--------|----------|----------|
| **Chest 1** (early) | Behind junk pile (22, 66) | "Spare Capacitor" |
| **Hidden Stash** | Cantina back wall loose panel (30, 14 interior) | Ironhawk note |
| **Pet Sniff Spot** | Near Waterworks (84, 44) | Buried crafting mat (after tame system) |

---

## L) Quick Reference: Dusthaven at a Glance

```
+------------------+
|   NORTH GATE     |  → Ashveil Road
|    (52, 10)      |
+------------------+
         |
   CANTINA ROW (District 1)
   [Cantina] [Terminal] [Broadcast Screen]
         |
   MARKET SQUARE (District 2)
   [Inn] [Quest Board] [General Goods] [Weapon Stall]
         |
   +----------+----------+
   |          |          |
WEST      SCRAPLINE   EAST GATE
SPUR      (District 3)  → Prismridge
(0, 58)   [Renna's]     (95, 62)
          (26, 78)
                     SE TRACK
                     → Mirewatch
                     (88, 95)
```
