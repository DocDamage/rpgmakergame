# Chroma's Edge — Ashveil Sanctuary Town Map Sheet (v1)
## Growth Refuge Town — "The World Can Heal"

---

## A) Technical Specs

| Parameter | Value |
|-----------|-------|
| Town Map Size | 112 × 112 tiles |
| Tile Size | 16×16 px |
| Full Texture | 1792×1792 px |
| Encounter Rate | 0% (safe zone) |
| Time States | Day / Night |
| Town Terminal | Yes (cleaner than Dusthaven's, but still scarred) |
| Mounts | Allowed after D3 (stable node appears); otherwise "no mounts inside garden ring" rule |

---

## B) Visual Identity

### Materials
- Pale stone
- Living vine lattices
- Moss lanterns
- Wood bridges
- Woven cloth banners

### Color Palette
- Sage green
- Warm cream stone
- Amber lantern light
- Faint cyan lattice-glow

### Signature Props
- **Root-arches** that form doorways
- **Bioluminescent "seed-lamps"** hanging from branches
- **Water channel** that runs through town like a calm vein
- **Old Progenitor glyph-stone** half-reclaimed by vines (foreshadow)

---

## C) Town Layout (District Blocks)

### District 1 — Sanctuary Circle (Central Hub)
- **Bounds:** x 38–76, y 42–76
- **Vibe:** Open circular plaza with a living tree at center ("Heartroot")
- **Function:** Primary NPC congregation, story cutscenes

### District 2 — Healer's Walk (Clinic + Herbalists)
- **Bounds:** x 76–108, y 46–74
- **Vibe:** The "functional" side of town: medicine, bandages, antidotes, status cures

### District 3 — Seed Market (Food + Craft)
- **Bounds:** x 40–74, y 76–104
- **Vibe:** Small stalls, seed exchange, simple gear, crafting mats

### District 4 — Quiet Terraces (Residences + Elder)
- **Bounds:** x 10–40, y 28–74
- **Vibe:** Calm steps, prayer stones, kids, "life continues" feel

### District 5 — Gategrove (Overworld Exit)
- **Bounds:** x 44–74, y 0–22
- **Vibe:** Main gate + signposts + a "guardian vine arch" that visually frames leaving

### District 6 — Ruinpath Trailhead (Dungeon Access)
- **Bounds:** x 0–22, y 74–104
- **Vibe:** Dirt trail + broken stone + warning totem
- **Leads to:** Ruins of Ashveil (D1)

---

## D) Key Anchors & Coordinates (Local 0–111)

### Main Spawn Points

| Spawn | Location | Coordinates | Context |
|-------|----------|-------------|---------|
| **SPAWN A** | Arrival from overworld | (58, 18) | Gategrove interior |
| **SPAWN B** | After resting at Inn | (62, 64) | Near Heartroot plaza |
| **SPAWN C** | Return from Ruins | (18, 88) | Ruinpath Trailhead |

### Town Terminal

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Ashveil Lattice Terminal** | (96, 56) | Looks "tended" (not broken), but faintly unstable after certain story beats |
| **Activation** | — | On first arrival or during first sanctuary scene |

### Exits (Edge Triggers)

| Direction | Edge Trigger | Destination |
|-----------|--------------|-------------|
| **To Overworld (Gategrove)** | (58, 0) | Ashwold Shelf overworld |
| **To Ruins of Ashveil (D1)** | (0, 92) | Dungeon entrance |
| **To Primordial Grove** | (110, 60) | Postgame only (locked until late game) |

---

## E) Main Buildings (Exterior Door Tiles)

| Building | Door Coordinates | Function |
|----------|------------------|----------|
| **Sanctuary Hall ("Heartroot Hall")** | (58, 54) | Town leader + main story dialogues + "sanctuary choices" |
| **Inn ("Mosslight Rest")** | (54, 86) | Rest/save |
| **Healer's Clinic ("Green Thread Clinic")** | (90, 62) | Status cures |
| **Herbalist Stall ("Root & Resin")** | (86, 74) | Herbs/potions |
| **General Goods ("Kindling & Clay")** | (66, 94) | Basic supplies |
| **Craft Bench Shed ("Vinework Bench")** | (44, 92) | Crafting |
| **Quest Board** | (62, 82) | Near Inn, under hanging lanterns |
| **Memorial Stone** | (30, 58) | Quiet terrace; used for character beats |
| **Watch Post** (non-military) | (72, 22) | Scouts, not soldiers |

---

## F) Interior Maps (Required)

### 1) Heartroot Hall (Story HQ)
- **Interior Size:** 36×28
- **Key Props:**
  - Circular meeting rug
  - "Glyph-stone" half-covered in vines (lore)
- **NPC Anchors:**
  - Sanctuary Elder
  - Scout Captain
  - Refugee families (changes by phase)

### 2) Green Thread Clinic
- **Interior Size:** 32×22
- **Function:** Status cures, post-fight triage, small cutscene space for Suresh later
- **Signature Prop:** Hanging herb bundles + sterilized stone table

### 3) Mosslight Rest (Inn)
- **Interior Size:** 30×20
- **Function:** Save/rest + rumor
- **Flavor:** Soft biolight, quiet guitar/handpan ambiance

### 4) Vinework Bench (Craft Shed)
- **Interior Size:** 28×18
- **Function:** Early crafting tutorial (Growth mats), later upgrade hooks

---

## G) Shops + Services (Inventory by Progress)

### Base (First Visit / Pre-D1 Clear)

| Shop | Inventory |
|------|-----------|
| **General Goods** | Basic potions, antidote, bandage kit, "seed salve" |
| **Clinic** | Poison cure + minor status cures |
| **Craft Shed** | Craft basic Growth resist (low tier) using local mats |

### After D1 Clear (Growth Stabilization)

| Change | Details |
|--------|---------|
| **Clinic expands** | Bleed/burn cures, better med kits |
| **Market unlock** | "Vinewrap Charm" (small DEF/regen accessory) |
| **Terminal** | New "lattice lore" prompt appears (foreshadow Prime network) |

### After D3 (Mount/Taming Unlock)

| New Feature | Location |
|-------------|----------|
| **Stable Perch** | (70, 14) near Gategrove |
| **Adds** | Mount feed/cosmetics, "sanctuary saddle" (non-combat QoL) |

---

## H) NPC Roster (Placement + Function)

### Story-Critical

| NPC | Location | Notes |
|-----|----------|-------|
| **Sanctuary Elder Maelin** | Heartroot Hall / plaza (day), terraces (night) | Town leader |
| **Scout Captain Rooke Vale** | Watch Post (day), Gategrove (night patrol) | Non-Dominion scouts |

### Utility

| NPC | Function |
|-----|----------|
| **Innkeeper** | Rest/save, rumor lines update per phase |
| **Clinic Medic** | Introduces "Growth ≠ cure-all" line, sets tone for Foundation danger |
| **Craftsman** | Upgrades + "vine-lattice" gear mods |

### Flavor

| NPC Type | Details |
|----------|---------|
| Kids chasing glowbugs | — |
| Gardener NPC | — |
| Refugee storyteller | — |
| "Wind-listener" mystic | Not cult |

---

## I) Quest Hooks (Ashveil-Specific)

### Main Story

| Quest | Purpose |
|-------|---------|
| **"Sanctuary Contract"** | Confirms mission into Ruins of Ashveil (D1) |
| **"The Vines Remember"** | Lore scene (optional) that foreshadows pedestals |

### Sidequests (Early)

| Quest | Type | Reward |
|-------|------|--------|
| **Seedlamp Repair** | Fetch | Glow resin from edge tiles (teaches gathering) |
| **Lost Scout** | Rescue | Short rescue at Ruinpath outskirts (mini-combat outside town) |
| **Water Channel Blockage** | Puzzle | Move debris → crafting mat |

### Sidequests (Later Return)

| Quest | Purpose |
|-------|---------|
| **Refugee Ledger** | Track missing civilians (ties into Dominion cruelty) |
| **Primordial Grove Key** | Unlocks postgame gate to Grove content |

---

## J) Story-State Phases (Town "Evolution")

### PHASE 0 — First Arrival (Calm, Guarded Optimism)
- More civilians
- Gentle music
- Scouts visible but relaxed

### PHASE 1 — Post-Scene 001 / Dominion Pressure Rising
- Warning posters appear at Gategrove
- Refugees increase
- Scouts more tense

### PHASE 2 — After D1 Clear
- Vines "bloom" in plaza (visual reward)
- New vendor line: "the air feels lighter"

### PHASE 3 — Midgame
- Quiet evacuation drills (not panic, preparedness)
- Optional "Dominion spy" NPC appears (sidequest)

### PHASE 4 — Late Game
- Fewer civilians (sent to Halcyon/safer zones)
- Memorial stone gets new offerings (tone shift)

---

## K) Navigation / Collision Notes

- Keep the central Sanctuary Circle very open (first "breathing room" town)
- Use water channel as a natural "path guide" from Gategrove → plaza → market
- Ruinpath Trailhead should look visibly unsafe compared to the town's calm

---

## L) Secrets / Collectibles

| Secret | Location | Contents |
|--------|----------|----------|
| **Hidden herb cache** | Behind terrace vine wall (24, 46) | Rare heal herb |
| **Lore stone** | (34, 40) | Reads Progenitor glyph hint (one-time) |
| **Pet sniff spot** (after tame system) | (82, 50) | "Resin Knot" crafting mat |

---

## M) Quick Reference: Layout Overview

```
    NORTH GATE (GATEGROVE)
    [Watch Post at 72, 22]
           |
    +------+------+
    |             |
    |  SANCTUARY  |         HEALER'S WALK
    |   CIRCLE    |        [Clinic at 90, 62]
    |  [Heartroot |        [Herbalist at 86, 74]
    |   at 58,54] |
    |             |
    +------+------+-------------+
           |                    |
           v                    v
    [Inn at 54, 86]      SEED MARKET
    [Quest at 62, 82]    [Goods at 66, 94]
                         [Craft at 44, 92]

    QUIET TERRACES (West)      RUINPATH TRAILHEAD (SW)
    [Memorial at 30, 58]       [Exit at 0, 92]
    [Elder pacing]             → To Ruins of Ashveil (D1)
```
