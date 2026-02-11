# Chroma's Edge — Master Tileset Specification

## Pixel Art Shot Sheet (v1.0)

---

## 0) Core Technical Specs

* **Tile Size:** 16×16 px
* **Palette:** Neo-Pixel JRPG (Rich saturation, dark outlines, dynamic lighting ready).
* **Layering:** Ground (Layer 0), Decoration (Layer 1), Collision/Walls (Layer 2), Overhead (Layer 3).
* **Animation:** 3-frame or 4-frame cycles for water/fire/lights.

---

## 1) UNIVERSAL TILESET (Used Everywhere)

**File Name:** `tileset_universal_core.png`

### A) UI / HUD Elements

* **Textbox Frame:** 9-slice scalable (Corners + Edges + Center fill). Dark metal with neon trim.
* **Cursor:** Animated pointer (bobbing up/down).
* **Interact Prompt:** "!" bubble, "?" bubble, "..." bubble.
* **Gauges:** HP Bar, MP Bar, Limit Break Meter (segmented).

### B) Common Objects (Scatter)

* **Chests:** Closed, Open (wood/metal variants).
* **Save Point:** Crystal shard (animates: floating/pulsing).
* **Doorway:** Black void tile (for transitions).
* **Ladders/Ropes:** Tiled vertical strips.
* **Shadows:** 50% opacity black blobs (small/med/large) for character grounding.

---

## 2) BIOME: SCRAP DESERT (Dusthaven / Badlands)

**File Name:** `tileset_biome_scrap_desert.png`

### A) Ground Tiles (Auto-tile compatible)

* **Sand:** Base layer (dull orange/tan). Variations with pebble details.
* **Hardpan:** Cracked earth (darker path).
* **Metal Plating:** Rusted squares buried in sand (transition tiles needed).

### B) Walls / Structures

* **Canyon Wall:** Red rock cliffs (Bottom, Mid, Top edge).
* **Scrap Walls:** Corrugated metal sheets, welded patches.
* **Roofs:** Canvas tarps (tan/grey), rusted metal slopes.

### C) Decor Objects

* **Junk Piles:** Gears, pipes, unidentifiable tech.
* **Cacti:** Spiky, dry green.
* **Fence:** Barbed wire or chain link.
* **Signage:** Neon "OPEN" sign (flickering animation), bounty board.

---

## 3) BIOME: ANCIENT RUINS (Ashveil / D1 Dungeon)

**File Name:** `tileset_biome_ancient_ruins.png`

### A) Ground Tiles

* **Stone Brick:** White/Grey protruding stones.
* **Mossy Brick:** Green tint variants.
* **Dirt Path:** Where stones are broken.
* **Overgrowth:** Vines creeping over stone edges.

### B) Walls / Structures

* **Ruin Walls:** White stone blocks, some cracked.
* **Pillars:** Intact and broken versions.
* **Arches:** Stone doorways.

### C) Animated / Special

* **Vines:** Thick roots that can block paths (anim: pulsating).
* **Bioluminescent Plants:** Glowing bulbs (blue/purple).
* **Water:** Clear pools with lily pads.

---

## 4) BIOME: INDUSTRIAL MAGMA (Cinderstep / D6 Quarry)

**File Name:** `tileset_biome_industrial_magma.png`

### A) Ground Tiles

* **Obsidian:** Dark black/purple jagged stone.
* **Grate Floor:** Metal mesh (see lava below).
* **Rails:** Minecart tracks (straight, curved, switch).

### B) Walls / Structures

* **Basalt Cliff:** Sharp, angular black rock.
* **Factory Walls:** Riveted iron plates.
* **Pipes:** Brass/Copper pipes running along walls.

### C) Animated / Special

* **Lava:** Molten flow (3-frame cycle: bubbling).
* **Steam Vents:** White puffs (anim: intermittent burst).
* **Conveyor Belts:** Arrows indicating direction (anim: scrolling texture).

---

## 5) BIOME: ABYSSAL TIDE (Brinegate / D5 Trench)

**File Name:** `tileset_biome_abyssal_tide.png`

### A) Ground Tiles

* **Wet Wood:** Planks (dark, slick).
* **Coral Rock:** Pink/Teal porous stone.
* **Sand (Underwater):** Rippled texture.

### B) Walls / Structures

* **Coral Formations:** Organic, towering shapes.
* **Shipwreck Wood:** Rotting timber walls.
* **Bubble Glass:** Translucent domes.

### C) Animated / Special

* **Water (Surface):** Dark blue churn (anim: waves).
* **Water (Deep):** Distortion effect overlay?
* **Bubbles:** Particle columns rising.
* **Currents:** Arrows indicating flow force.

---

## 6) BIOME: FROZEN TIME (Rimehold / D7 Citadel)

**File Name:** `tileset_biome_frozen_time.png`

### A) Ground Tiles

* **Snow:** White/Blue soft texture (footsteps leave marks?).
* **Ice:** Reflective blue/clear (slippery cue).
* **Clockwork Floor:** Gear patterns embedded in stone.

### B) Walls / Structures

* **Ice Spire:** Translucent crystal walls.
* **Frozen Metal:** Gears frozen mid-turn.
* **Stasis Fields:** Shimmering barriers.

### C) Animated / Special

* **Aurora:** Sky backdrop (anim: color shift).
* **Phased Objects:** Transparent/"Ghost" versions of platforms.

---

## 7) BIOME: VOID / SHADOW (D8 Nexus / Endgame)

**File Name:** `tileset_biome_void_shadow.png`

### A) Ground Tiles

* **Void Stone:** Dark grey with purple veins.
* **Null Space:** Starfield tile (parallax background).
* **Glitch Tile:** Pixels shifting/static (anim: noise).

### B) Walls / Structures

* **Floating Islands:** jagged edges, nothing below.
* **Geometric Shapes:** Cubes/Pyramids floating.

### C) Animated / Special

* **Rifts:** Tears in reality (anim: sucking effect).
* **Echo Mirrors:** Reflective surfaces.

---

## 8) OVERWORLD (World Map)

**File Name:** `tileset_overworld_scaled.png`
*Note: These tiles might be smaller or simpler (16x16 representing miles).*

* **Mountains:** High peaks (blocks movement).
* **Forest:** Dense tree clusters.
* **Town Icons:** Mini-sprites of Dusthaven, Ashveil, etc.
* **Roads:** Tan dirt paths connecting hubs.
* **Water:** Ocean boundary.

---

## 9) CHARACTERS / SPRITES (Reference)

**File Name:** `sprites_characters_master.png`

* **Base Template:** 24x32px (Taller than 16x16 tiles for detail).
* **Kade:** Trenchcoat, messy hair, pistol.
* **Nix-7:** Robot, glowing eyes, floating bits?
* **Nadia Korr:** Military uniform, stern face.
* **Renna:** Goggles on head, wrench, grease stains.
* **Monsters:**
  * *Slime/Rat:* Small (16x16).
  * *Humanoid:* Med (24x32).
  * *Boss:* Large (48x48 or 64x64 multi-tile).

---

## 10) PRODUCTION CHECKLIST

1. [ ] **Universal UI + Objects** (Done first ensures playable prototype).
2. [ ] **Scrap Desert Biome** (Need for Intro Town).
3. [ ] **Ancient Ruins Biome** (Need for Dungeon 1).
4. [ ] **Character Sprites** (Kade + Nix + Basic Enemies).
5. [ ] *...Remaining Biomes...*
