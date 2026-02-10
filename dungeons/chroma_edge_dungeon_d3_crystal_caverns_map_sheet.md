# Chroma's Edge — Crystal Caverns (D3) Dungeon Map Sheet (v1)
## Light Foundation Dungeon — "Illumination as Truth… and as Control"

---

## 0) Dungeon Technical Specs

| Parameter | Value |
|-----------|-------|
| **Dungeon Type** | Main Story Dungeon 3 |
| **Foundation Theme** | LIGHT (illumination as truth… and as control) |
| **Recommended Level** | Lv 12–22 |
| **Primary Outcome** | Light Relic acquired + seated + **TAMING/MOUNTS UNLOCK** (first real "ride the overworld" moment) |
| **Structure** | 4 submaps (clean pacing + distinct visual beats) |
| **Encounters** | ON (except in Pedestal Chamber) |
| **Save Points** | 1 (Luminant Cavern) + autosave at Pedestal |
| **Key Mechanics** | Beam Routing + Prism Mirrors + Glare Zones |
| **Return Loop** | Minecart Shortcut unlocks after boss → returns near entrance |

---

## 1) Macro Flow (How it Plays)

**Flow:** Prism Mine Mouth → Luminant Cavern (Save) → Prism Relay Galleries (Puzzle Hub) → Crystal Reliquary (Boss + Pedestal) → Minecart Shortcut → Exit

### Macro ASCII

```
[MAP 1 Prism Mine Mouth]
        |
        v
[MAP 2 Luminant Cavern] (SAVE)
        |
        v
[MAP 3 Prism Relay Galleries] --(beam puzzles)-> (locks clear)
        |
        v
[MAP 4 Crystal Reliquary]
   Boss Arena + Light Pedestal
        |
   Minecart Shortcut
        v
Back to Map 1 near entrance (fast return)
```

---

## CORE MECHANICS (Dungeon-Wide)

### A) Beam Routing (Light Lines)

**Beam Emitters** project light beams that can:
- Open Light Gates
- Power Prism Relays
- Reveal hidden walkways (fake floors become visible under correct beam color)

### B) Prism Mirrors (Rotatable)

- **Interactable mirrors** rotate in 90° increments
- Some mirrors are **color prisms** that split beam into 2 channels
- **Puzzle rule:** Beam must match gate color (White, Cyan, Gold)

### C) Glare Zones (Soft Hazard)

- Shimmer tiles that apply **"Blinded"** buildup
- Blinded reduces accuracy + increases crit received (the "truth hurts" theme)
- Glare can be reduced by powering **Shade Totems** (small side objective)

---

## SUBMAP 1 — PRISM MINE MOUTH

**Purpose:** Transition from town into dungeon + introduce beams safely

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 112 × 64 tiles |
| **Entry** | From Prismridge (or overworld edge) |
| **Exit** | To Luminant Cavern |
| **Encounter Band** | Lv 12–16 (light) |

### B) Visual / Tone
- Mining scaffolds, carts, crystal dust floating in sunbeams
- Early "pretty but sharp" vibe

### C) Anchors (Local Coords)

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **ENTRY** | (56, 6) | From Prismridge |
| **EXIT** to Submap 2 | (56, 62) | Leads to Luminant Cavern |
| **Tutorial Emitter** (hidden bridge) | (44, 22) | Beam reveals walkable path |
| **Hidden bridge reveal tiles** | x 52–60, y 24 | Invisible until beam hits |
| **Chest** (early) | (92, 18) | 2× Potion + "Lens Cloth" (craft mat) |

### D) One-time Script Beat (Recommended)

| Parameter | Value |
|-----------|-------|
| **Trigger** | (56, 16) |
| **Event** | Beam flashes across wall → glyphs appear → disappears when you move |
| **Takeaway** | Light here is selective, not "honest" |

---

## SUBMAP 2 — LUMINANT CAVERN (SAVE)

**Purpose:** Wide open "wow" chamber + save + first real glare threat

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 128 × 96 tiles |
| **Encounters** | ON (light), but central platform is low-encounter pocket |
| **Entry** | From Mine Mouth |
| **Exit** | To Prism Relay Galleries |

### B) Layout Concept

A big crystal lake cavern with:
- **Central island** (save node)
- **Two side ridges** (optional loot + shade totems)

### C) Mechanics Introduced

#### Shade Totems (2)
- Optional interactables
- Reduce glare tiles in this map + next corridor
- Teach "do side tasks to make main route easier"

### D) Anchors

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **ENTRY** | (64, 6) | From Mine Mouth |
| **SAVE CRYSTAL** | (64, 42) | Midpoint safe zone |
| **Shade Totem #1** | (24, 58) | Reduces glare |
| **Shade Totem #2** | (104, 64) | Reduces glare |
| **Exit** to Submap 3 | (64, 90) | Locked until 1 Shade Totem OR brute-force through glare |
| **Chest** (ridge) | (18, 72) | Ether Drop ×1 |
| **Hidden cache** (crystal column) | (110, 34) | "Prism Charm" (reduces Blinded buildup) |

### E) Enemies

| Enemy | Traits |
|-------|--------|
| **Gleam Bats** | Chance to inflict Blinded |
| **Shard Crawlers** | Defense up when in beam light |
| **Prism Wisps** | Swap element/resist |
| **Dominion Surveyor** (rare) | Only if escalation flag active |

---

## SUBMAP 3 — PRISM RELAY GALLERIES (PUZZLE HUB)

**Purpose:** The "brain" of the dungeon — multi-step beam routing + locked wings

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 128 × 128 tiles |
| **Entry** | From Luminant Cavern |
| **Exit** | To Reliquary corridor (locked until puzzles complete) |
| **Encounter Band** | Lv 15–20 (medium) |

### B) Layout Concept

A hub with **3 wings**, each completing a relay:
- **WHITE Relay Wing** (basic reflection)
- **CYAN Relay Wing** (split-beam prism)
- **GOLD Relay Wing** (timed shutter / moving mirror)

Complete all 3 → opens the Reliquary Gate.

### C) Puzzle: PRISM RELAY TRIAD (3 Relays)

**Rules:**
- Start with one **White beam** from central emitter
- Use mirror arrays to:
  - Open the wing
  - Route beam through a prism to color it
  - Hit the relay receptor

**"No Pain" Version:**
- Each wing has a safe **"reset pedestal"** that returns mirrors to default

### D) Anchors

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **ENTRY** | (64, 10) | From Cavern |
| **Central Emitter** | (64, 60) | White beam source |
| **Reset Pedestal** | (64, 72) | Returns mirrors to default |
| **Reliquary Gate** (locked) | (64, 120) | Opens after all 3 relays |
| **White Wing door** | (24, 54) | — |
| **Cyan Wing door** | (104, 54) | — |
| **Gold Wing door** | (64, 28) | — |
| **White Relay receptor** | (12, 64) | — |
| **Cyan Relay receptor** | (116, 70) | — |
| **Gold Relay receptor** | (64, 16) | — |
| **Mirror A** | (52, 54) | Key interactable |
| **Mirror B** | (76, 54) | Key interactable |
| **Prism Splitter** | (94, 62) | Creates Cyan channel |
| **Shutter Gate Lever** | (64, 38) | Gold wing timing |

### E) Optional Side Wing: "Facet Vault"

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Entrance crack** | (14, 40) | Breakable wall |
| **Mini-elite** | — | Facet Guardian (harder fight) |
| **Loot** | — | "Refraction Band" (small crit + blind resist) |

---

## SUBMAP 4 — CRYSTAL RELIQUARY (FINAL)

**Purpose:** Tension hallway → boss arena → Light Pedestal + mount unlock + shortcut

### A) Specs

| Parameter | Value |
|-----------|-------|
| **Size** | 96 × 96 tiles |
| **Encounter Band** | Lv 18–22 (elite chance) |
| **Pre-boss antechamber** | No encounters |

### B) Corridor Hazards

| Hazard | Description |
|--------|-------------|
| **Shard Floor Tiles** | Step on them → minor damage + "Bleed" buildup |
| **Beam Traps** | Thin beams sweep every few seconds (safe spots telegraphed) |

### C) Anchors

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **ENTRY** | (48, 6) | From Galleries |
| **Chest A** | (18, 28) | Weapon mat + antidote |
| **Chest B** | (78, 28) | "Lensguard Cloak" (reduces glare and beam damage) |
| **Boss Door** | (48, 60) | — |
| **Boss Arena Center** | (48, 78) | Prism Stag |
| **Pedestal Chamber Door** (post-boss) | (48, 90) | Opens after victory |
| **Minecart Shortcut** (post-boss) | (86, 70) | Returns to Submap 1 near entrance |

---

## 2) MINIBOSS (Optional Gatekeeper) — "SHARD SENTINEL"

| Parameter | Value |
|-----------|-------|
| **Placement** | End of Gold Wing OR guarding Facet Vault |
| **Concept** | Crystal construct that refracts your own attacks |
| **Reward** | **"Mirror Pin"** (lets you rotate mirrors without walking to them once per puzzle — QoL) |

---

## 3) FINAL BOSS — "PRISM STAG" (Mount Unlock Boss)

### Arena
Circular chamber, 4 beam pillars around the rim + reflective floor segments

**Identity:** A luminous creature formed by Light instability—beautiful, dangerous, not evil

### Phase Mechanics

| Phase | HP Threshold | Mechanics |
|-------|--------------|-----------|
| **Phase 1** | 100–60% | Charges + beam pillar activations (telegraphed lanes) |
| **Phase 2** | 60–25% | **"Refraction Burst"** — creates mirror clones (decoys) |
| **Phase 3** | 25–0% | **"True Beam"** — one pillar becomes lethal until you rotate a mirror to diffuse it |

### Boss Outcomes

- Boss is **subdued, not murdered** (sets up taming tone)
- **RELIC ACQUIRED: LIGHT FRAGMENT** (alt: "Prism Core")

---

## 4) PEDESTAL CHAMBER — Light Seat

- **No encounters**
- Clean stone, crystal ribs, soft white hum

### Anchors

| Feature | Coordinates | Notes |
|---------|-------------|-------|
| **Pedestal** | (48, 92) | Light seat location |
| **Interact prompt** | — | "Seat relic?" |
| **Cutscene vibe** | — | Light stops being "blinding" and becomes "revealing" |

### Suggested System Outputs

| Output | Effect |
|--------|--------|
| **RELIC SEATED — LIGHT** | Canon flag |
| **WORLD EFFECT** | Hidden paths become visible near Prismridge routes (small overworld reveals) |
| **NEW FIELD PASSIVE** | "Gleam Sense" (reveals secrets on minimap in Light zones) |

---

## 5) TAMING + MOUNT UNLOCK (Primary System Event)

**Timing:** Immediately after pedestal seating (or immediately after boss, depending on pacing)

### Cutscene Beat
- The Prism Stag returns, calmer
- It bows its head (**consent-coded**)
- Party receives first **Taming Kit / Harness Pattern**

### System Unlocks

| Unlock | Details |
|--------|---------|
| **MOUNT SYSTEM UNLOCKED** | Core flag |
| **FIRST MOUNT** | Luminous Strider (or Prism Stag as mount identity) |
| **RULE** | Mounted overworld travel = 0% encounter rate |

### Practical UI Unlocks

Stable posts appear in:
- **Dusthaven** (Beast Handler Post)
- **Ashveil** (Stable Perch)
- **Mirewatch** (Hitch)
- **Prismridge** (Main Stable)

### Flags

| Flag | Value |
|------|-------|
| **D3_CLEARED** | TRUE |
| **RELIC_LIGHT_ACQUIRED** | TRUE |
| **RELIC_LIGHT_SEATED** | TRUE |
| **MOUNTS_UNLOCKED** | TRUE |
| **FIRST_MOUNT_OBTAINED** | LUMINOUS_STRIDER |

---

## 6) Shortcut / Return Loop (QoL)

**After boss + pedestal:**
- **Minecart Shortcut** activates at (86, 70)
- **Drop point:** Submap 1 at (84, 48) near mine exit (fast return to Prismridge)

---

## Quick Reference: Dungeon Overview

```
PRISMRIDGE (Town)
       |
       v
[SUBMAP 1: PRISM MINE MOUTH]
   Size: 112×64 | Lv 12–16 | Tutorial: Beam reveals hidden bridge
   Entry: (56, 6) | Exit: (56, 62) | Emitter: (44, 22)
       |
       v
[SUBMAP 2: LUMINANT CAVERN]
   Size: 128×96 | Lv 12–16 | Save: (64, 42)
   Shade Totems: (24, 58) & (104, 64) | Exit: (64, 90)
       |
       v
[SUBMAP 3: PRISM RELAY GALLERIES]
   Size: 128×128 | Lv 15–20 | Puzzle: 3 Relays (White/Cyan/Gold)
   Emitter: (64, 60) | Reliquary Gate: (64, 120)
   Optional: Facet Vault at (14, 40)
       |
       v
[SUBMAP 4: CRYSTAL RELIQUARY]
   Size: 96×96 | Lv 18–22
   Boss Door: (48, 60) | Prism Stag at (48, 78)
   Pedestal: (48, 92) | Minecart: (86, 70)
   
   MOUNT UNLOCK: Luminous Strider
       |
       v
   (Shortcut back to Submap 1 near entrance)
       |
       v
PRISMRIDGE (Town Return)
```
