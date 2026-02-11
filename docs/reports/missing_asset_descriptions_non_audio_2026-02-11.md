# Missing Asset Descriptions (Non-Audio) (2026-02-11)

## Scope
This file lists every non-audio runtime placeholder image that still needs final production art.

## Count
- Total non-audio placeholder runtime assets: **16** (reduced from 33)
- ✅ Tilesets: **0 remaining** (all 17 replaced via extraction tool)
- ⚠️ Remaining: 13 UI/System + 3 Battle/Title/Vehicle

## ✅ COMPLETED: Tilesets (17/17)

All tilesets have been extracted from source spritesheets using `tools/extract_tilesets.py`:

### Dungeon Tilesets (6)
- ✅ Dungeon_A1.png - Ashveil Stone (crop)
- ✅ Dungeon_A2.png - Ashveil Stone (crop)
- ✅ Dungeon_A4.png - Capital Ruins (crop)
- ✅ Dungeon_A5.png - Capital Ruins (crop)
- ✅ Dungeon_B.png - Interior Generic (direct copy)
- ✅ Dungeon_C.png - Void Nexus (crop)

### Outside Tilesets (7)
- ✅ Outside_A1.png - Dustbelt (resize)
- ✅ Outside_A2.png - Dustbelt (resize)
- ✅ Outside_A3.png - Uplands (crop)
- ✅ Outside_A4.png - Ember Basalt (resize)
- ✅ Outside_A5.png - Prism Highland (resize)
- ✅ Outside_B.png - Mire Stilts (resize)
- ✅ Outside_C.png - Tide Coast (resize)

### World Tilesets (4)
- ✅ World_A1.png - Orion Overworld (tile)
- ✅ World_A2.png - Orion Overworld (tile)
- ✅ World_B.png - Tower (crop)
- ✅ World_C.png - Palace (crop)

---

## Remaining Placeholders (16 files)

## 1) Battlebacks / Title / Vehicle

### `img/titles1/Ruins.png` (816x624)
- Purpose: Main title screen background.
- Needed art: Signature key art for the game world (ruined-tech + chroma energy tone), with clear visual hierarchy.
- Composition notes: Keep center-upper area suitable for logo lockup and lower-left/center-left area readable for command menu.
- Technical constraints: Exact canvas `816x624`, no transparent gaps, avoid noisy contrast behind menu text.

### `img/battlebacks1/GrassMaze.png` (1000x740)
- Purpose: Battleback layer 1 (ground/near plane) for grass-maze encounters.
- Needed art: Ground surface and near-environment texture that supports side-view battle readability.
- Composition notes: Ground perspective should feel walkable and align with battler footing.
- Technical constraints: Exact canvas `1000x740`; color values must keep actor/enemy silhouettes readable.

### `img/battlebacks2/GrassMaze.png` (1000x740)
- Purpose: Battleback layer 2 (far/background plane) paired with `battlebacks1/GrassMaze`.
- Needed art: Mid/far scenery (trees/ruins/cliffs/sky haze) matching the same biome and lighting.
- Composition notes: Horizon depth should complement, not fight, layer 1.
- Technical constraints: Exact canvas `1000x740`; keep contrast moderate to avoid visual clutter.

### `img/characters/Vehicle.png` (576x384)
- Purpose: Vehicle character sheet (boat/ship/airship slots in MV sheet layout).
- Needed art: Final world-appropriate vehicle sprites with matching palette and silhouette clarity.
- Composition notes: Distinct silhouettes between each vehicle type; readable at overworld scale.
- Technical constraints: Exact canvas `576x384`, preserve RPG Maker character-sheet cell arrangement.

## 2) System Sheets

### `img/system/Window.png` (192x192)
- Purpose: Global window skin for message boxes and menus.
- Needed art: Final UI frame/gradient/selection style consistent with game tone.
- Composition notes: Text legibility is priority; border style can be ornate but not busy.
- Technical constraints: Exact `192x192`; preserve MV windowskin slicing regions.

### `img/system/IconSet.png` (512x512)
- Purpose: Global icon atlas used by items, skills, states, etc.
- Needed art: Cohesive icon language across combat, elemental effects, key items, quests, crafting.
- Composition notes: High silhouette clarity at small size.
- Technical constraints: Exact `512x512`; preserve icon grid alignment across full sheet.

### `img/system/Balloon.png` (768x384)
- Purpose: Balloon emotes above characters (surprise, anger, heart, etc.).
- Needed art: Full finalized emote set matching world tone (can be stylized but readable instantly).
- Composition notes: Strong shape language and high readability against mixed map backgrounds.
- Technical constraints: Exact `768x384`; preserve MV balloon frame layout.

### `img/system/ButtonSet.png` (768x48)
- Purpose: Touch/button prompt sheet.
- Needed art: Finalized button glyphs and prompt styling.
- Composition notes: Minimal, clean glyphs with strong contrast.
- Technical constraints: Exact `768x48`; preserve button slice locations.

### `img/system/States.png` (768x384)
- Purpose: Battle status overlays/markers.
- Needed art: Final state visuals (poison, stun, buffs/debuffs, special status families).
- Composition notes: Effects should be readable without obscuring battler sprites.
- Technical constraints: Exact `768x384`; preserve frame ordering and spacing.

### `img/system/Weapons1.png` (768x256)
- Purpose: Weapon animation sprite sheet page 1.
- Needed art: Final slash/thrust/blunt weapon animation frames for assigned IDs.
- Composition notes: Distinct swing arcs and impact rhythm.
- Technical constraints: Exact `768x256`; preserve MV weapon frame indexing.

### `img/system/Weapons2.png` (768x256)
- Purpose: Weapon animation sprite sheet page 2.
- Needed art: Additional weapon class animations (advanced blades/polearms/exotics as needed).
- Composition notes: Maintain timing/pixel density parity with `Weapons1`.
- Technical constraints: Exact `768x256`; preserve frame indexing.

### `img/system/Weapons3.png` (768x256)
- Purpose: Weapon animation sprite sheet page 3.
- Needed art: Remaining high-tier/special weapon visual set.
- Composition notes: FX intensity can increase, but motion readability must stay clear.
- Technical constraints: Exact `768x256`; preserve frame indexing.

### `img/system/Shadow1.png` (128x64)
- Purpose: Primary actor/enemy ground shadow sprite.
- Needed art: Soft-edged shadow tuned for your battler proportions.
- Composition notes: Neutral opacity that works across bright and dark battlebacks.
- Technical constraints: Exact `128x64`; centered, with clean alpha.

### `img/system/Shadow2.png` (64x64)
- Purpose: Secondary/smaller shadow sprite.
- Needed art: Companion shadow variant for alternate scale use.
- Composition notes: Same visual language as `Shadow1`.
- Technical constraints: Exact `64x64`; centered, clean alpha.

### `img/system/Splash.png` (816x624)
- Purpose: Boot/splash screen.
- Needed art: Final splash illustration or branding plate.
- Composition notes: Clear branding focal point and clean load-time appearance.
- Technical constraints: Exact `816x624`; avoid tiny text.

### `img/system/GameOver.png` (816x624)
- Purpose: Game over screen artwork.
- Needed art: Final fail-state visual with narrative tone continuity.
- Composition notes: Strong mood shift without reducing text readability.
- Technical constraints: Exact `816x624`; keep command text zone readable.

## 3) Runtime Tilesets (All Placeholder -> Replace with Final)

### `img/tilesets/Dungeon_A1.png` (768x576)
- Purpose: Dungeon animated autotiles (water/lava/falls equivalents).
- Needed art: Dungeon liquid/energy animated surfaces aligned to dungeon palette.
- Technical constraints: Preserve MV A1 autotile block structure exactly.

### `img/tilesets/Dungeon_A2.png` (768x576)
- Purpose: Dungeon ground autotiles.
- Needed art: Seamless floor families (stone, cracked stone, wet, mossed, etc.) with transitions.
- Technical constraints: Preserve MV A2 autotile structure exactly.

### `img/tilesets/Dungeon_A4.png` (768x768)
- Purpose: Dungeon wall autotiles.
- Needed art: Wall variants with proper upper/lower transition behavior.
- Technical constraints: Preserve MV A4 wall layout exactly.

### `img/tilesets/Dungeon_A5.png` (768x768)
- Purpose: Dungeon fixed non-autotile base tiles.
- Needed art: Utility/static tiles (trim strips, hazard plates, cracked slabs, marker tiles).
- Technical constraints: Standard A5 48x48 tile grid; no layout drift.

### `img/tilesets/Dungeon_B.png` (768x768)
- Purpose: Dungeon object/detail sheet B.
- Needed art: Props and interactables (pillars, chains, braziers, debris, sigils, levers).
- Technical constraints: Standard B-sheet tile grid; keep collision silhouettes clean.

### `img/tilesets/Dungeon_C.png` (768x768)
- Purpose: Dungeon object/detail sheet C.
- Needed art: Additional decoration sets, puzzle motifs, encounter dressing, rare landmarks.
- Technical constraints: Standard C-sheet grid; style-match `Dungeon_B`.

### `img/tilesets/Outside_A1.png` (768x576)
- Purpose: Outdoor animated autotiles.
- Needed art: Rivers/coast ripples/falls/swamp/energy channels matching overworld biomes.
- Technical constraints: Preserve MV A1 layout exactly.

### `img/tilesets/Outside_A2.png` (768x576)
- Purpose: Outdoor ground autotiles.
- Needed art: Grass/dirt/sand/snow/ash ground families with clean transitions.
- Technical constraints: Preserve MV A2 layout exactly.

### `img/tilesets/Outside_A3.png` (768x768)
- Purpose: Outdoor building autotiles.
- Needed art: Roof/wall structure autotiles for settlement exteriors.
- Technical constraints: Preserve MV A3 layout exactly.

### `img/tilesets/Outside_A4.png` (768x768)
- Purpose: Outdoor wall/cliff autotiles.
- Needed art: Cliff faces, retaining walls, vertical terrain transitions.
- Technical constraints: Preserve MV A4 layout exactly.

### `img/tilesets/Outside_A5.png` (768x768)
- Purpose: Outdoor fixed utility tiles.
- Needed art: Roads, pavement fragments, transitions, route accents, edge helpers.
- Technical constraints: Standard A5 grid.

### `img/tilesets/Outside_B.png` (768x768)
- Purpose: Outdoor prop/detail sheet B.
- Needed art: World objects (fences, signs, crates, vegetation clusters, machinery props).
- Technical constraints: Standard B grid; prioritize map readability and collision clarity.

### `img/tilesets/Outside_C.png` (768x768)
- Purpose: Outdoor prop/detail sheet C.
- Needed art: Secondary biome props and region-specific world dressing objects.
- Technical constraints: Standard C grid; style-match `Outside_B`.

### `img/tilesets/World_A1.png` (768x576)
- Purpose: Overworld animated autotiles.
- Needed art: Macro water/ocean animation sets for world map scale.
- Technical constraints: Preserve MV A1 world-map layout.

### `img/tilesets/World_A2.png` (768x576)
- Purpose: Overworld base terrain autotiles.
- Needed art: Distinct macro biomes (plains, deserts, tundra, blight, chroma zones).
- Technical constraints: Preserve MV A2 world-map structure exactly.

### `img/tilesets/World_B.png` (768x768)
- Purpose: Overworld detail sheet B.
- Needed art: Landmarks, mountain forms, forests, route markers, structural map symbols.
- Technical constraints: Standard world B grid; maintain landmark readability at map scale.

### `img/tilesets/World_C.png` (768x768)
- Purpose: Overworld detail sheet C.
- Needed art: Additional landmark/biome detail set and late-game world features.
- Technical constraints: Standard world C grid; style-match `World_B`.

## 4) Existing Source Material You Already Have
- Environment source basis exists at `assets/sprites/tilesets/tileset_*_source_primary.png`.
- This should accelerate completion of all `img/tilesets/*` runtime replacements.

## 5) What This Means Practically
- You are not blocked by missing filenames; all runtime targets exist.
- The remaining non-audio art workload is replacing placeholder content in the 33 files above with final production-quality sheets.
