# Chroma's Edge — Asset Catalog

> **Quick Reference Guide for Time Fantasy (TF) Asset Mapping**  
> *Last Updated: 2026-02-07*  
> *Asset Source: `C:\Users\Doc\Desktop\game\assets\AssetsForMyGame`*

---

## Table of Contents

1. [Technical Specifications](#1-technical-specifications)
2. [Asset Inventory by Category](#2-asset-inventory-by-category)
3. [Zone-to-Asset Mapping](#3-zone-to-asset-mapping)
4. [Character & Enemy Assets](#4-character--enemy-assets)
5. [Props & Objects](#5-props--objects)
6. [Environmental Effects](#6-environmental-effects)
7. [Asset Gaps & Recommendations](#7-asset-gaps--recommendations)
8. [Cross-Zone Reuse Opportunities](#8-cross-zone-reuse-opportunities)

---

## 1. Technical Specifications

### Standard Format (Time Fantasy Assets)
| Property | Value |
|----------|-------|
| **Base Tile Size** | 16×16 px |
| **Sprite Scale** | 3× (48×48 px display) |
| **Character Size** | ~24×32 px base (72×96 px at 3×) |
| **File Naming** | `*_3.png` = 3× scale TF format |
| **Animation Frames** | 3-4 frame cycles typical |

### Asset Type Indicators
| Suffix | Meaning |
|--------|---------|
| `_3.png` / `_3x.png` | 3× scaled Time Fantasy asset |
| `_e_3.png` | Elements-style variant (compatible) |
| `_tf_3.png` | Time Fantasy specific format |
| `_rm_3.png` | RPG Maker MV/MZ compatible |

### Layering Convention
- **Layer 0**: Ground tiles (autotiles)
- **Layer 1**: Decoration/overlay
- **Layer 2**: Collision/Walls
- **Layer 3**: Overhead/foreground

---

## 2. Asset Inventory by Category

### 2.1 Biome Tilesets (Zip Archives)

| Asset File | Size | Biome Theme | Target Zone(s) |
|------------|------|-------------|----------------|
| `tf_ashlands.zip` | 3.29 MB | Volcanic, ash, fire | **Ember Basalt**, Cinderstep, Skyspire Temple |
| `tf_beach_tileset.zip` | 0.11 MB | Coastal, sand, water | **Tide Coast**, Brinegate Port |
| `tf_darkdimension_updated2020.zip` | 0.20 MB | Dark void, shadow realm | **Void Nexus**, Capital Ruins (corrupted areas) |
| `tf_final_tower_12.24.22.zip` | 0.97 MB | Ascending mechanical spire | **Chroma Tower** (all 100F) |
| `tf_jungle.zip` | 0.21 MB | Swamp, jungle, wetlands | **Mire**, Mirewatch, Fungal Depths |
| `tf_ruindungeons.zip` | 0.63 MB | Ancient ruins, stone | **Ashveil Ruins**, Ancient Ruins biome |
| `tf_sewers_2.20.zip` | 0.19 MB | Industrial, metal grates | **Obsidian Industrial**, Gravemark Outpost |
| `tiles_fourseasons.zip` | 0.69 MB | Seasonal variants | **Multiple biomes** (color variants) |
| `cloud_tileset.zip` | 0.24 MB | Clouds, sky platforms | **Aetherreach**, sky areas |

### 2.2 Cave/Crystal Tilesets (Folder)

| Asset File | Size | Contents | Target Zone(s) |
|------------|------|----------|----------------|
| `biocaves/biocaves_MV_A1.png` | 17 KB | Cave ground autotiles | **Prism Highland**, Crystal Caverns |
| `biocaves/biocaves_MV_A5.png` | 25 KB | Cave walls, formations | **Prism Highland**, Crystal Caverns |
| `biocaves/biocaves_MV_B.png` | 19 KB | Cave decorations | **Prism Highland**, Crystal Caverns |

### 2.3 Supplementary Tile Images (PNG)

| Asset File | Zone Application | Notes |
|------------|------------------|-------|
| `elem_caveA_A5_3x.png` | Prism Highland/Caverns | Elemental cave walls variant A |
| `elem_caveB_A5_3x.png` | Prism Highland/Caverns | Elemental cave walls variant B |
| `elem_caveC_A5_3x.png` | Prism Highland/Caverns | Elemental cave walls variant C |
| `catacombs_p_3x.png` | Void Nexus, Ruins | Catacomb/dungeon walls |
| `tf_newworld_RMA1_3x.png` | Overworld/Universal | RM A1 autotile format |
| `tf_newworld_RMA5_3x.png` | Overworld/Universal | RM A5 autotile format |
| `tf_newworld_wateredgetransition_3.png` | Tide Coast, Brinegate | Water edge transitions |
| `mirror-cliffside-3.png` | Various | Mirror/cliff tiles |
| `mirror-palace-addon_3.png` | Final Palace | Palace addon tiles |
| `underwater_tiles_3.png` | Abyssal Trench | Underwater environment |

### 2.4 World Map / Overworld

| Asset File | Application |
|------------|-------------|
| `overworld_mountains_3.png` | World map mountain ranges |
| `tf_newworld_chartiles_3x.png` | Overworld character/town tiles |
| `tf_newworld_jungle_3.png` | Overworld jungle/forest representation |

---

## 3. Zone-to-Asset Mapping

### Zone 1: Dustbelt (Desert Frontier) — Dusthaven
**Theme**: Scrap desert, frontier town, Ironhawk salvage

| Asset | Usage | Notes |
|-------|-------|-------|
| `tiles_fourseasons.zip` | Base ground tiles | Recolor for desert tones |
| `westerntowntiles_3.png` | Frontier buildings | Western/salvage aesthetic |
| `postapoc_*.png` set | Industrial scrap | `postapoc_buildings_3.png`, `postapoc_streets_3.png`, `postapoc_junkshack_3.png` |
| `neworld_windmilltower_3.png` | Windmills | Dustbelt landmarks |
| `radiotower_3.png` / `radiotower_tf_3.png` | Communication towers | Dominion infrastructure |

**⚠️ GAP**: No dedicated desert sand tileset. Consider `tf_beach_tileset.zip` with color modification.

---

### Zone 2: Uplands/Ashveil — Ashveil Sanctuary
**Theme**: Stone sanctuary, old stone + living vine-tech

| Asset | Usage | Notes |
|-------|-------|-------|
| `tf_ruindungeons.zip` | Primary tileset | Ancient stone ruins |
| `tf_lichcrusades_v2.zip` | Temple/sacred areas | Crusade/lich-themed structures |
| `neworld_churchgraveyard_full_3x.png` | Graveyard areas | Church/graveyard tiles |
| `neworld_churchgraveyard_tf_3x.png` | Alternate graveyard | TF-format variant |
| `statues_tilesheet_3.png` | Decorative statues | Ruin decorations |
| `bamboo_3.png` | Plant life | Vine/forest elements |

---

### Zone 3: Mire — Mirewatch
**Theme**: Swamp town on stilts, fungal medicine trade

| Asset | Usage | Notes |
|-------|-------|-------|
| `tf_jungle.zip` | **Primary tileset** | Swamp, jungle, wetlands |
| `tf_sewers_2.20.zip` | Underground areas | Sewer/pipe aesthetic for undercity |
| `glassmire` concepts | Bridge highways | See Glassmire Causeway POI |

---

### Zone 4: Prism Highland — Prismridge
**Theme**: Crystal formations, light-refraction streets

| Asset | Usage | Notes |
|-------|-------|-------|
| `biocaves/` folder | **Primary tileset** | Crystalline cave system |
| `elem_caveA/B/C_A5_3x.png` | Cave wall variants | Color variations for crystal types |
| `rockcrystals_floating_char_e_3.png` | Floating crystals | Animated crystal props |
| `rockcrystals_floating_char_tf_3.png` | Floating crystals | TF-format variant |

---

### Zone 5: Ember Basalt — Cinderstep
**Theme**: Volcanic terrain, heat vents, smiths

| Asset | Usage | Notes |
|-------|-------|-------|
| `tf_ashlands.zip` | **Primary tileset** | Volcanic ash, lava flows |
| `Red_Demon_Blue_Variant_TF.zip` | Demon enemies | Ember creatures (see enemies) |

---

### Zone 6: Tide Coast — Brinegate Port
**Theme**: Coastal cliffs, port town, deep-sea divers

| Asset | Usage | Notes |
|-------|-------|-------|
| `tf_beach_tileset.zip` | **Primary tileset** | Sand, water, coastal rocks |
| `seaship_sheet_3.png` | Ships/dockables | Port ships |
| `whirlpool_*.png` set | Ocean hazards | Animated whirlpools (various styles) |
| `underwater_tiles_3.png` | Underwater areas | Abyssal Trench sections |

---

### Zone 7: Obsidian Industrial — Gravemark Outpost
**Theme**: Industrial quarry, mass pressure, gravity strain

| Asset | Usage | Notes |
|-------|-------|-------|
| `tf_sewers_2.20.zip` | **Primary tileset** | Industrial metal, grates |
| `tf_ashlands.zip` | Quarry depths | Lava/obsidian sections |
| `postapoc_*.png` set | Industrial decay | Ruined industrial aesthetic |
| `buzzsaw_horz_3.png` / `buzzsaw_vert_3.png` | Hazards | Industrial machinery |
| `hazmat_3.png` | Enemies | Hazmat/industrial enemies |

---

### Zone 8: Frost Citadel — Rimehold
**Theme**: Ice fortress, frozen time

| Asset | Usage | Notes |
|-------|-------|-------|
| `tiles_fourseasons.zip` | **Primary base** | Winter/snow tiles |
| `catacombs_p_3x.png` | Frozen catacombs | Ice fortress interiors |

**⚠️ GAP**: No dedicated ice tileset. Heavy reliance on recoloring four seasons.

---

### Zone 9: Chrono Pier — Chronowake Pier
**Theme**: Time-distorted architecture, ships arrive early

| Asset | Usage | Notes |
|-------|-------|-------|
| `tf_ruindungeons.zip` | Base structures | Time-worn architecture |
| `mecha_war_pack.zip` | Time-tech elements | Mechanical/time aesthetic |
| `robots_sheet_3.png` | Time anomalies | Chrono enemies |

---

### Zone 10: Capital Ruins
**Theme**: Ruined capital, void corruption

| Asset | Usage | Notes |
|-------|-------|-------|
| `tf_darkdimension_updated2020.zip` | **Void corruption** | Dark dimension tiles |
| `tf_ruindungeons.zip` | Ruin structures | Base ruin architecture |
| `vamps_8_3.png` | Shadow enemies | Void-corrupted beings |

---

### Zone 11: Void Nexus
**Theme**: Shadow foundation, reality tears

| Asset | Usage | Notes |
|-------|-------|-------|
| `tf_darkdimension_updated2020.zip` | **Primary tileset** | Dark dimension, void tiles |
| `catacombs_p_3x.png` | Shadow catacombs | Dark underground |
| `vamps_8_3.png` | Shadow entities | Vampire/shadow enemies |

---

### Zone 12: Chroma Tower (100F)
**Theme**: Progenitor mechanical interior, ascending spire

| Asset | Usage | Notes |
|-------|-------|-------|
| `tf_final_tower_12.24.22.zip` | **Primary tileset** | Ascending tower, mechanical |
| `mecha_war_pack.zip` | Mecha enemies | Tower defenders |

---

### Zone 13: Palace (Final)
**Theme**: Grand final palace

| Asset | Usage | Notes |
|-------|-------|-------|
| `mirror-palace-addon_3.png` | Palace tiles | Palace-specific addon |
| `tf_ruindungeons.zip` | Base structure | Grand architecture base |
| `statues_tilesheet_3.png` | Decorative | Palace statues |

---

### Zone 14: Aetherreach (Sky Town)
**Theme**: Floating sky town, sky-salvage

| Asset | Usage | Notes |
|-------|-------|-------|
| `cloud_tileset.zip` | **Primary tileset** | Cloud platforms, sky tiles |
| `cloudfogs_3.png` | Atmospheric fog | Cloud/fog effects |
| `airshipA_3.png` | Airship sprites | Transport/ships |
| `airshipA_shadow_3.png` | Airship shadows | Ground shadows |
| `airships_full_diag_sheet_3.png` | Multiple airships | Fleet variations |
| `airship_baloon_big_e_3.png` | Large balloons | Airship variants |
| `airship_baloon_big_tf_3.png` | Large balloons TF | TF-format variant |
| `hotairballoons_rmA/B_3.png` | Hot air balloons | Transport options |

---

### Zone 15: Remnant Vault
**Theme**: Corrupted, unstable

| Asset | Usage | Notes |
|-------|-------|-------|
| `tf_darkdimension_updated2020.zip` | Corruption base | Dark/unstable aesthetic |
| `tf_ruindungeons.zip` | Vault structure | Ancient vault architecture |
| `mecha_war_pack.zip` | Corrupted mechs | Defense systems |

---

## 4. Character & Enemy Assets

### 4.1 Hero/Party Characters

| Asset | Description | Application |
|-------|-------------|-------------|
| `wotf_hero_3.png` | Main hero sprites | **Kade** (party lead) |
| `blackswordsman_3x.png` | Dark warrior | Reference/template for dark-type characters |

### 4.2 NPCs (Non-Combat)

| Asset | Description | Usage |
|-------|-------------|-------|
| `elf_sheet_1_3x.png` | Elf NPC set 1 | **Ashveil** (elven sanctuary theme) |
| `elf_sheet_2_3x.png` | Elf NPC set 2 | **Ashveil** additional NPCs |
| `quirky_npcs.zip` (1.25 MB) | Varied NPC set | **All towns** - general population |
| `npc-animations-8.20.zip` (2.35 MB) | Animated NPCs | **All towns** - detailed NPCs |
| `npc_crowd_3.png` | Background crowd | Crowd scenes, distant NPCs |
| `bellydancers_3.png` | Dancer NPCs | Entertainment districts |
| `dotd_dancers_3.png` | Festival dancers | Event/special scenes |
| `maledancers_3.png` | Male dancers | Entertainment districts |

### 4.3 Enemy Packs by Zone

#### Beast/Natural Enemies
| Asset | Description | Zone Application |
|-------|-------------|------------------|
| `beast_tribes.zip` (0.81 MB) | Beast tribe enemies | **Mire**, wilderness areas |
| `beast_tribes_2.zip` (3.41 MB) | Extended beast tribes | **All wilderness zones** |
| `farm_animals_4.18.24.zip` (0.55 MB) | Domestic animals | **Dusthaven**, towns |
| `goblinos_3.png` | Goblin enemies | **Dustbelt**, frontier areas |
| `mer_8_3.png` | Merfolk set 1 | **Tide Coast**, Brinegate |
| `mer_8_chars3.png` | Merfolk set 2 | **Tide Coast**, Brinegate |
| `merlocs_tf_3.png` | Mer-loc variants | **Tide Coast**, underwater |

#### Undead Enemies
| Asset | Description | Zone Application |
|-------|-------------|------------------|
| `elements_zombie_parts.zip` (30 KB) | Zombie parts | **Void Nexus**, corrupted areas |
| `coffins_3.png` | Coffin props | **Graveyards**, crypts |
| `mummy_3.png` | Mummy enemies | **Ancient ruins**, tombs |
| `vamps_8_3.png` | Vampire enemies | **Void Nexus**, shadow areas |

#### Industrial/Mechanical Enemies
| Asset | Description | Zone Application |
|-------|-------------|------------------|
| `hazmat_3.png` | Hazmat enemies | **Obsidian Industrial** |
| `robots_sheet_3.png` | Robot enemies | **Chrono Pier**, **Chroma Tower** |
| `mecha_war_pack.zip` (1.90 MB) | Mecha enemies | **Obsidian**, **Tower**, **Remnant Vault** |

#### Demon/Fire Enemies
| Asset | Description | Zone Application |
|-------|-------------|------------------|
| `Red_Demon_Blue_Variant_TF.zip` (2.38 MB) | Demon variants | **Ember Basalt**, fire zones |
| `demking_battler_3.png` | Demon King boss | **Ember Basalt** boss |
| `demon_3.png` | Demon sprite | **Ember Basalt** enemies |
| `demonking_3.png` | Demon King alt | Boss variant |

#### Void/Alien Enemies
| Asset | Description | Zone Application |
|-------|-------------|------------------|
| `alien_new_3.png` | Alien enemies | **Capital Ruins** (void corruption) |
| `OMEGA_ALIEN_BETA.zip` (0.44 MB) | Omega alien set | **Void Nexus**, endgame |
| `halloween_10.2022.zip` (5.84 MB) | Halloween horrors | **Void Nexus**, spooky areas |

#### Knight/Faction Enemies
| Asset | Description | Zone Application |
|-------|-------------|------------------|
| `knight_factions_3.png` | Knight groups | **Capital Ruins** (fallen knights), **Ashveil** |
| `goblinslayer_single_3.png` | Goblin Slayer ref | Easter egg/variant |

### 4.4 Boss Sprites

| Asset | Description | Zone/Boss |
|-------|-------------|-----------|
| `demking_battler_3.png` | Demon King | **Ember Basalt** - Fire boss |
| `demonking_3.png` | Demon King alt | Alternate boss sprite |
| `demon_3.png` | Demon general | **Ember Basalt** mini-boss |
| `giantworm_1_3x.png` | Giant Worm | **Mire** / **Dustbelt** boss |
| `giantworm_terrain_1_3x.png` | Worm terrain | Worm boss arena tiles |
| `horseman_a_3.png` | Horseman A | **Capital Ruins** / **Void Nexus** boss |
| `horseman_b_3.png` | Horseman B | Horseman variant |
| `horseman_c_3.png` | Horseman C | Horseman variant |
| `bossplant_tentable_A_3x.png` | Plant boss part A | **Mire** / Fungal Depths boss |
| `bossplant_tentable_B_3x.png` | Plant boss part B | Plant boss variant |
| `bossplant_tentable_C_3x.png` | Plant boss part C | Plant boss variant |
| `bossplant_tiles_3x.png` | Plant boss tiles | Boss arena/environment |

---

## 5. Props & Objects

### 5.1 Interactive Objects

| Asset | Description | Usage |
|-------|-------------|-------|
| `book_savepoint_3.png` | Save point (tan) | **Universal** - standard save |
| `book_savepoint_blue_3.png` | Save point (blue) | **Universal** - magic/frost save |
| `book_savepoint_purple_3.png` | Save point (purple) | **Void** areas - void-touched save |
| `sealedchests_tf_3.png` | Sealed chests | **Universal** - treasure containers |
| `secret_bookshelf_3.png` | Secret door | **Ashveil**, libraries |
| `questboard_3.png` | Quest board | **All towns** - quest hub marker |

### 5.2 Decorative Props

| Asset | Description | Zone Usage |
|-------|-------------|------------|
| `coffins_3.png` | Coffins | Graveyards, crypts |
| `holly_foliage_3.png` | Holly plants | **Frost Citadel** (winter) |
| `bamboo_3.png` | Bamboo | **Mire**, Asian-inspired areas |
| `scorch_3.png` | Scorch marks | **Ember Basalt**, fire areas |
| `statues_tilesheet_3.png` | Statues | **Ashveil**, **Palace** |
| `museum_*.png` set | Museum items | **Chrono Pier** (time artifacts) |
| `alchemist_jars_3.png` | Potion/jar props | **All towns** - shops |
| `butchershop_3.png` | Butcher shop | Town marketplaces |
| `kitchenovenfireplace_3.png` | Kitchen objects | Inns, houses |
| `int_kitchen_3.png` | Kitchen interior | House interiors |

### 5.3 Transportation

| Asset | Description | Zone Usage |
|-------|-------------|------------|
| `airshipA_3.png` | Airship sprite | **Aetherreach**, overworld |
| `airshipA_shadow_3.png` | Airship shadow | Ground shadow effect |
| `airships_full_diag_sheet_3.png` | Multiple airships | Fleet/variety |
| `hotairballoons_rmA/B_3.png` | Hot air balloons | **Aetherreach** |
| `seaship_sheet_3.png` | Seafaring ships | **Tide Coast**, Brinegate |
| `steamcar_3.png` | Steam car | **Dusthaven**, industrial areas |
| `steamcarb_3.png` | Steam car variant | Transportation variety |
| `steamtractor_3.png` | Steam tractor | **Dusthaven**, farms |
| `train_mv_a.png` / `train_mv_b.png` | Trains | **Chrono Pier**, rails |

### 5.4 Special Structures

| Asset | Description | Zone Usage |
|-------|-------------|------------|
| `neworld_windmilltower_3.png` | Windmill | **Dustbelt** landmarks |
| `radiotower_3.png` / `radiotower_tf_3.png` | Radio towers | Dominion infrastructure |
| `ferriswheel_tf_3.png` | Ferris wheel | **Dusthaven** (festival) |
| `ladder_unroll_rm_3.png` | Animated ladder | Dungeons, verticality |
| `jp-stairs-ext-3.png` | Japanese stairs | **Ashveil** aesthetic |
| `stairs_3.png` | Generic stairs | Universal |

---

## 6. Environmental Effects

### 6.1 Weather Effects

| Asset | Description | Application |
|-------|-------------|-------------|
| `wsheet_drop1_3.png` | Water drop/splash | Raindrops, splashes |
| `wsheet_rain1_3.png` | Rain effect 1 | Storms |
| `wsheet_rain2_3.png` | Rain effect 2 | Heavy rain variant |
| `wsheet_snow_3.png` | Snow effect | **Frost Citadel** |
| `try_this_raindrop_3x.png` | Alternate raindrop | Rain variant |

### 6.2 Atmospheric Effects

| Asset | Description | Application |
|-------|-------------|-------------|
| `cloudfogs_3.png` | Cloud/fog layers | **Aetherreach**, high areas |
| `whirlpool_16_ELEMENTS_3x.png` | Small whirlpool | **Tide Coast** hazard |
| `whirlpool_16_TFA_3x.png` | Small whirlpool A | Variant style |
| `whirlpool_16_TFB_3x.png` | Small whirlpool B | Variant style |
| `whirlpool_16_TFD_3x.png` | Small whirlpool D | Variant style |
| `whirlpool_32_ELEMENTS_3x.png` | Large whirlpool | Boss arena hazard |
| `whirlpool_32_TFA_3x.png` | Large whirlpool A | Variant style |
| `whirlpool_32_TFB_3x.png` | Large whirlpool B | Variant style |
| `whirlpool_32_TFD_3x.png` | Large whirlpool D | Variant style |

### 6.3 Animated Elements

| Asset | Description | Application |
|-------|-------------|-------------|
| `buzzsaw_horz_3.png` | Horizontal buzzsaw | **Obsidian Industrial** hazard |
| `buzzsaw_vert_3.png` | Vertical buzzsaw | **Obsidian Industrial** hazard |

---

## 7. Asset Gaps & Recommendations

### 7.1 Critical Gaps (High Priority)

| Gap | Affected Zones | Recommendation |
|-----|----------------|----------------|
| **Dedicated Desert Tileset** | Dustbelt | Use `tf_beach_tileset` with recolor; acquire dedicated desert set |
| **Dedicated Ice Tileset** | Frost Citadel | Use `tiles_fourseasons` winter; recolor cave tiles for ice caves |
| **Progenitor/Sci-Fi Tileset** | Chroma Tower (upper floors) | Extend `tf_final_tower` with custom sci-fi elements |
| **Gravity/Distortion Effects** | Sable Expanse | Custom shader work needed |

### 7.2 Medium Priority Gaps

| Gap | Affected Zones | Recommendation |
|-----|----------------|----------------|
| **Crystal formation variety** | Prism Highland | Recolor `biocaves` with different hues |
| **Void corruption overlays** | Capital Ruins | Create overlay tiles for `tf_ruindungeons` |
| **Time-distortion visual cues** | Chrono Pier | Animated shader + particle effects |
| **Specific shrine tilesets** | All shrines | Repurpose `tf_lichcrusades` with color variants |

### 7.3 Format/Technical Needs

| Need | Priority | Action |
|------|----------|--------|
| **Autotile conversion** | High | Convert key PNGs to RPG Maker autotile format |
| **Animation frame cleanup** | Medium | Standardize all animations to 3 or 4 frames |
| **Shadow sprites** | Medium | Extract/generate ground shadows for all characters |

---

## 8. Cross-Zone Reuse Opportunities

### 8.1 High-Value Reuse Pairs

| Primary Asset | Primary Zone | Secondary Use | Modification |
|---------------|--------------|---------------|--------------|
| `tf_ashlands.zip` | Ember Basalt | **Obsidian Quarry** (lower levels) | Reduce fire, add industrial |
| `tf_ruindungeons.zip` | Ashveil Ruins | **Capital Ruins** (pre-corruption) | Same tiles, different lighting |
| `tf_jungle.zip` | Mire | **Fungal Depths** (deeper areas) | Darker, more fungus |
| `beast_tribes_2.zip` | Mire | **All wilderness** | Recolor for zone themes |
| `quirky_npcs.zip` | All towns | **Universal population** | Clothing color per zone |

### 8.2 Color Palette Mapping

Use this mapping for quick recolors across zones:

| Base Asset | Ember Palette | Frost Palette | Void Palette |
|------------|---------------|---------------|--------------|
| `tf_ruindungeons` | +Orange overlay | +Blue overlay | +Purple overlay |
| `beast_tribes` | Fire effects | Ice effects | Shadow effects |
| `quirky_npcs` | Warm tones | Cool tones | Dark tones |

### 8.3 Component Reuse

| Component | Source Asset | Reuse In |
|-----------|--------------|----------|
| Metal grates | `tf_sewers_2.20` | Obsidian, Tower, Industrial |
| Stone bricks | `tf_ruindungeons` | All ruins, temples, vaults |
| Water edges | `tf_beach_tileset` | All water-adjacent areas |
| Cloud platforms | `cloud_tileset` | Aetherreach + high areas |
| Crystal formations | `biocaves` | Prism + Void (corrupted crystals) |

---

## Appendix A: Quick Lookup Tables

### By File Extension

| Pattern | Asset Type |
|---------|------------|
| `*_3.png` | 3× TF sprite |
| `*_3x.png` | 3× TF sprite (alt naming) |
| `*_e_3.png` | Elements RPG style |
| `*_tf_3.png` | Time Fantasy format |
| `*_rm_3.png` | RPG Maker MV/MZ format |
| `*_mv_*.png` | RPG Maker MV native |
| `*.zip` | Asset pack (extract to use) |

### By Asset Size (for loading priority)

| Size Tier | Assets | Priority |
|-----------|--------|----------|
| **Large** (>2 MB) | `2024patronbundle`, `2025pbundle`, `beast_tribes_2`, `halloween_10.2022`, `lobit_contents`, `tf_ashlands`, `Red_Demon_Blue_Variant` | Load per-zone |
| **Medium** (0.5-2 MB) | `2017patronbundle`, `2018patronbundle`, `mecha_war_pack`, `quirky_npcs`, `npc-animations-8.20` | Load per-biome |
| **Small** (<0.5 MB) | Most individual PNGs | Preload universal |

---

## Appendix B: Production Workflow Notes

### For Artists
1. All new assets should match 3× scale TF style
2. Maintain 16×16 base tile size for compatibility
3. Use existing palette from `tiles_fourseasons` for consistency

### For Programmers
1. `tf_*.zip` files contain RPG Maker formatted tilesets
2. `*_A1.png` = Ground autotiles (animated water/terrain)
3. `*_A5.png` = Ground/overlay tiles
4. `*_B.png` = Object/decor tiles (no autotile)

### For Level Designers
1. Reference this catalog before requesting new assets
2. Check "Cross-Zone Reuse" section for existing solutions
3. Note gaps in "Asset Gaps" for production priority

---

*Document Version: 1.0*  
*Maintained by: Development Team*  
*Update when: New assets added or zone requirements change*
