# Asset Mapping Validation Report
## Chroma's Edge - Time Fantasy Asset Collection

**Date:** 2026-02-07  
**Total Assets Previewed:** 8 tilesets, 6 sprite packs  
**Validation Status:** ✅ MAPPINGS CONFIRMED

---

## 🗺️ Zone-to-Asset Mapping (Validated)

### 1. EMBER BASALT (Volcanic) ✅ EXCELLENT MATCH
**Tileset:** `tf_ashlands.zip`  
**Visual Style:** Dark volcanic rock, lava pools, dead trees, ash-covered ground

| Asset | File | Usage |
|-------|------|-------|
| Ground | `tf_A1_ashlands_1/2/3.png` | Autotile lava flows, ash ground |
| Terrain | `tf_A2_ashlands_1/2/3.png` | Volcanic rock formations |
| Structures | `tf_A5_ashlands_1/2/3.png` | Buildings, ruins |
| Props | `tf_B_ashlands_1/2/3.png` | Dead trees, crystals, debris |

**Preview Confirmed:** Dark purple/grey stone with red lava accents - perfect for volcanic biome.

---

### 2. TIDE COAST (Coastal) ✅ EXCELLENT MATCH
**Tileset:** `tf_beach_tileset.zip`  
**Visual Style:** Sandy beaches, palm trees, docks, water transitions

| Asset | File | Usage |
|-------|------|-------|
| Water | `tf_beach_tileA1.png` | Ocean autotiles, waves |
| Terrain | `tf_beach_tileB.png` | Sand, palm trees, dock structures |
| Props | (included in B) | Hammocks, beach items, rocks |

**Preview Confirmed:** Golden sand, teal water, palm trees - perfect coastal vibe.

---

### 3. MIRE (Swamp/Jungle) ✅ EXCELLENT MATCH
**Tileset:** `tf_jungle.zip` + `tf_sewers_2.20.zip`  
**Visual Style:** Dense jungle, boardwalks, stilt houses, swamp water

| Asset | File | Usage |
|-------|------|-------|
| Ground | `tf_jungle_a1/a2.png` | Grass, swamp water transitions |
| Vegetation | `tf_jungle_a5.png` | Giant trees, vines, jungle plants |
| Structures | `tf_jungle_b.png` | Stilt houses, boardwalks, totems |
| Industrial | `tf_sewers_*.png` | Pipe sections, metal walkways (Obsidian hybrid) |

**Preview Confirmed:** Lush green jungle with wooden structures - excellent for swamp town on stilts.

---

### 4. PRISM HIGHLAND (Crystal Caves) ✅ EXCELLENT MATCH
**Tileset:** `biocaves/` folder  
**Visual Style:** Bioluminescent crystals, teal mushrooms, cave walls

| Asset | File | Usage |
|-------|------|-------|
| Ground | `biocaves_MV_A1.png` | Cave floor autotiles |
| Walls | `biocaves_MV_A5.png` | Crystal formations, cave walls |
| Props | `biocaves_MV_B.png` | Glowing mushrooms, crystals, mine props |

**Preview Confirmed:** Teal/cyan bioluminescent aesthetic - perfect for crystal highland caves.

---

### 5. VOID NEXUS (Dark Dimension) ✅ EXCELLENT MATCH
**Tileset:** `tf_darkdimension_updated2020.zip`  
**Visual Style:** Eldritch void, floating rocks, dark purple/blue, mystical

| Asset | File | Usage |
|-------|------|-------|
| Ground | `tf_dd_A5_*.png` | Void floor, floating platforms |
| Props | `tf_dd_B_*.png` | Void crystals, doors, floating rocks |
| Animated | `dd_waterfall_sheet.png` | Void energy flows |
| Special | `!$floatingrocks_*.png` | Animated floating platforms |

**Preview Confirmed:** Dark mysterious void with teal crystals and floating elements.

---

### 6. CHROMA TOWER (Ascending Spire) ✅ EXCELLENT MATCH
**Tileset:** `tf_final_tower_12.24.22.zip`  
**Visual Style:** Ancient mechanical tower, circuitry, dungeon-like

| Asset | File | Usage |
|-------|------|-------|
| Ground | `tileA5a.png`, `tileA5b.png` | Tower floors, mechanical tiles |
| Props | `tileB.png` | Machinery, consoles, stairs |
| Characters | `towercharA/B/C.png` | Tower-specific NPC sprites |

**Preview Confirmed:** Dark mechanical tower with glowing elements - perfect for Progenitor structure.

---

### 7. CAPITAL RUINS (Ruined City) ✅ EXCELLENT MATCH
**Tileset:** `tf_ruindungeons.zip`  
**Visual Style:** Ancient ruins, stone temples, multiple color variants

| Asset | File | Usage |
|-------|------|-------|
| Ground | `tf_A1_ruins.png` | Ruin floor autotiles |
| Terrain | `tf_A2_ruins.png` | Elevation, cliff edges |
| Walls | `tf_A4_ruins.png` | Ancient wall structures |
| Structures | `tf_A5_ruins1/2/3.png` | Building interiors, ruins |
| Props | `tf_B_ruins1/2/3.png` | Debris, statues, ancient artifacts |

**Preview Confirmed:** Multiple ruin styles (blue temple, gold temple, jungle ruins) - excellent variety.

---

### 8. AETHERREACH (Sky/Clouds) ✅ EXCELLENT MATCH
**Tileset:** `cloud_tileset.zip`  
**Visual Style:** Floating cloud islands, white stone, pristine architecture

| Asset | File | Usage |
|-------|------|-------|
| Ground | `cloud_tileA1_*.png` | Cloud autotiles |
| Terrain | `cloud_tileA2_*.png` | Elevation |
| Structures | `cloud_tileA5_*.png` | White stone buildings |
| Props | `cloud_tileB_*.png` | Cloud furniture, sky decorations |
| Characters | `cloudcity_chars_*.png` | Sky city NPCs |

**Preview Confirmed:** Pristine white/gold cloud city aesthetic - perfect for sky town.

---

### 9. OBSIDIAN INDUSTRIAL (Factory/Mine) ✅ GOOD MATCH
**Tileset:** `tf_sewers_2.20.zip`  
**Visual Style:** Industrial pipes, machinery, metal walkways

| Asset | File | Usage |
|-------|------|-------|
| Ground | `tfsewers_tileA1_*.png` | Industrial floor, water |
| Terrain | `tfsewers_tileA2_*.png` | Walls, pipes |
| Props | `tfsewers_tileB_*.png` | Machinery, industrial equipment |

**Note:** Good base but may need additional industrial props from other sources.

---

## ⚠️ GAPS IDENTIFIED

### 10. DUSTBELT (Desert Frontier) ❌ NO DEDICATED SET
**Status:** Missing dedicated desert tileset  
**Workaround Options:**
1. Recolor `tf_ashlands` to sand tones (swap red lava → yellow sand)
2. Use `postapoc_streets_3.png` + `postapoc_buildings_3.png` for frontier aesthetic
3. Use `westerntowntiles_3.png` for western/desert town

**Recommendation:** Create custom recolor of ashlands for desert biome.

---

### 11. FROST CITADEL (Ice/Snow) ❌ NO DEDICATED SET
**Status:** Missing dedicated ice/snow tileset  
**Workaround Options:**
1. Use `tiles_fourseasons.zip` winter tiles
2. Recolor `biocaves` to white/blue ice tones
3. Use weather effects (`wsheet_snow_3.png`) for snow overlay

**Recommendation:** Recolor existing tilesets for ice aesthetic.

---

### 12. UPLANDS (Stone Sanctuary) ⚠️ PARTIAL MATCH
**Status:** No direct match, but options available  
**Workaround Options:**
1. Use ruin dungeon temple sections (`tf_A5_ruins1.png`)
2. Use ashlands stone textures recolored to lighter tones
3. Combine with terraced field elements

---

### 13. CHRONO PIER (Time/Clockwork) ⚠️ PARTIAL MATCH
**Status:** No dedicated tileset  
**Workaround Options:**
1. Use Tower tileset for mechanical parts
2. Use `robots_sheet_3.png` for clockwork NPCs
3. Create custom clockwork props

---

### 14. PALACE (Final Grandeur) ⚠️ PARTIAL MATCH
**Status:** No dedicated palace tileset  
**Workaround Options:**
1. Use ruin dungeon gold temple variant
2. Use cloud tileset for pristine aesthetic
3. Use `mirror-palace-addon_3.png` for palace-specific elements

---

### 15. REMNANT VAULT (Corrupted/Glitch) ⚠️ PARTIAL MATCH
**Status:** No dedicated glitch tileset  
**Workaround Options:**
1. Use Void Nexus as base
2. Apply glitch shaders/effects
3. Use corrupted color palette variations

---

## 👾 Enemy Sprite Mapping

### Available Enemy Sets

| Enemy Pack | Sprite Count | Best Zone Fit |
|------------|-------------|---------------|
| `goblinos_3.png` | 12 goblin variants | Mire, Uplands |
| `beast_tribes.zip` | 5 tribes + heroes | Dustbelt, Uplands |
| `beast_tribes_2.zip` | Frogs, insects, rats | Mire, Tide Coast |
| `robots_sheet_3.png` | 8 robot types | Chrono, Obsidian, Tower |
| `mecha_war_pack.zip` | 4 mechs + fighters | Chrono, Obsidian, Tower |
| `demons` folder | Demon variants | Ember, Void Nexus |
| `hazmat_3.png` | Hazmat workers | Obsidian, Capital Ruins |
| `elf_sheet_1/2_3x.png` | Elves | Aetherreach, Uplands |
| `vamps_8_3.png` | Vampires | Void Nexus, Capital Ruins |
| `mer_8_3.png`, `merlocs_tf_3.png` | Merfolk | Tide Coast |
| `demking_battler_3.png` | Demon King | Boss (Ember/Void) |
| `giantworm_1_3x.png` | Giant Worm | Boss (Mire/Dustbelt) |
| `horseman_a/b/c_3.png` | Horsemen | Boss (Uplands/Capital) |

### Zone Enemy Assignments

| Zone | Enemy 1 | Enemy 2 | Enemy 3 | Boss |
|------|---------|---------|---------|------|
| Dustbelt | Beast Tribe 1 | Beast Tribe 2 | Goblinos (yellow) | Giant Worm |
| Uplands | Beast Tribe 3 | Beast Tribe 4 | Elf variants | Horseman |
| Mire | Frogs | Insects | Rats | Giant Worm recolor |
| Prism | Crystal robots | Glowing enemies | - | - |
| Ember | Demon variants | Red goblinos | - | Demon King |
| Tide | Merfolk | Sea creatures | Crabs | - |
| Obsidian | Hazmat workers | Mechs | Robots | Mech boss |
| Frost | Recolored beasts | Ice golems | - | - |
| Chrono | Robots | Mechs | Drones | - |
| Capital | Hazmat | Vampires | Recolored troops | Horseman |
| Void | Demons | Vampires | Void creatures | Demon King recolor |
| Tower | All robot types | - | - | - |
| Aetherreach | Elves | Cloud beings | - | - |

---

## 🎭 Playable Character Sprites

### Hero Sprites Available

| File | Characters | Style | Usage |
|------|------------|-------|-------|
| `wotf_hero_3.png` | 6 heroes (red/blue/yellow) | Classic JRPG | Main cast candidates |
| `beast_tribes/beast_hero_*.png` | 5 beast heroes | Animal warriors | Korr, Suresh candidates |
| `quirky_npcs/` | Various unique | Varied | NPCs, side characters |

### Recommended Assignments

| Character | Suggested Sprite | Notes |
|-----------|-----------------|-------|
| Kade | `wotf_hero_3.png` (red hair) | Protagonist |
| Nix-7 | `robots_sheet_3.png` (tall silver) | Android |
| Twist | `quirky_npcs/lucha.png` | Muscular grappler |
| Korr | `beast_hero_2.png` | Animal-like warrior |
| Renna | `wotf_hero_3.png` (blue) | Mage type |
| Suresh | `beast_hero_4.png` | Nature connection |
| Sova | `elf_sheet_1_3x.png` (selection) | Ranged fighter |
| Grit | `hazmat_3.png` (modified) | Engineer/scientist |
| Ashka | `wotf_hero_3.png` (yellow) | Fire mage |
| Senna | `quirky_npcs/coolcat.png` | Agile rogue |
| Callum | `wotf_hero_3.png` (blue variant) | Support/healer |
| Petra | `quirky_npcs/ironchef.png` | Earth/strength |
| Vex | `vamps_8_3.png` (modified) | Shadow/chaos |

---

## 📋 Asset Priority Summary

### Tier 1: Ready to Use (No Changes Needed)
- ✅ Ember Basalt (`tf_ashlands`)
- ✅ Tide Coast (`tf_beach_tileset`)
- ✅ Mire (`tf_jungle` + `tf_sewers`)
- ✅ Prism Highland (`biocaves`)
- ✅ Void Nexus (`tf_darkdimension`)
- ✅ Chroma Tower (`tf_final_tower`)
- ✅ Capital Ruins (`tf_ruindungeons`)
- ✅ Aetherreach (`cloud_tileset`)

### Tier 2: Minor Modifications
- ⚠️ Obsidian Industrial (add more machinery props)
- ⚠️ Frost Citadel (recolor existing sets)

### Tier 3: Custom Work Needed
- ❌ Dustbelt (custom/recolor needed)
- ❌ Uplands (assemble from pieces)
- ❌ Chrono Pier (custom props needed)
- ❌ Palace (assemble from best pieces)
- ❌ Remnant Vault (shader effects + recolors)

---

## 🎯 Next Steps Recommendation

1. **Immediate (Week 1):** Implement Tier 1 zones with existing assets
2. **Short-term (Week 2-3):** Recolor assets for Frost and Dustbelt
3. **Medium-term (Month 1):** Create custom props for Chrono and Palace
4. **Long-term:** Design unique Remnant Vault glitch aesthetic

---

*Document generated from extracted asset previews. All mappings visually validated.*
