# Chroma's Edge - Production Master Checklist
## Complete Pre-Coding Manifest: Maps, Sprites, Data, Conventions

## Audit Delta (2026-02-10)

- Data cohesion/integrity pass: complete (latest full audit reports `0` open integrity issues).
  - `docs/reports/full_project_audit_2026-02-09_non_audio_completion.md`
  - `docs/reports/full_project_audit_2026-02-09_non_audio_completion.csv`
  - `docs/reports/full_project_audit_2026-02-09_deep_pass_4.md`
  - `docs/reports/full_project_audit_2026-02-09_deep_pass_4.csv`
  - `docs/reports/full_project_audit_2026-02-09_super_deep_pass_6.md`
  - `docs/reports/full_project_audit_2026-02-09_super_deep_pass_6.csv`
- Non-audio content-lock pass: complete (`0` issues, `0` resize-required production enemy/boss sprites).
  - `docs/reports/non_audio_content_lock_pass_2026-02-09.md`
  - `docs/reports/non_audio_content_lock_pass_2026-02-09.csv`
  - Includes repair of `28` malformed content JSON files (`content/dialog`, `content/quests`) and full revalidation.
- Added authored baseline content where references were missing:
  - `assets/data/items/item_generated_placeholders.json`
  - `assets/data/quests/quest_generated_placeholders.json`
  - `assets/data/maps/map_generated_placeholders.json`
  - `assets/data/npcs/npc_seam_warden.json` and related missing NPC records
- UI icon coverage has been restored (`assets/sprites/ui` populated for all item icon references).
  - Placeholder icon set replaced with sheet-derived production icons.
  - Remap report: `docs/reports/ui_icon_remap_2026-02-09.csv`
- Audio reference coverage has been restored with temporary in-place files (see `assets/audio/README_PLACEHOLDER_AUDIO.md`).
  - Super-deep audio token sweep is fully covered with temporary files (`141/141` refs).
  - Missing token fill list used: `docs/reports/audio_missing_tokens_2026-02-09_super_deep_pass_5.txt` (`77` files generated).
- Generated content next pass completed:
  - item economy + equipment stat tuning for generated entries
  - quest narrative/progression tuning for generated entries
  - audio replacement queue generated at `docs/reports/audio_replacement_queue_2026-02-09.csv`
- NPC baseline authoring coverage completed:
  - portraits generated in `assets/sprites/portraits`
  - dialog baseline coverage in `assets/data/dialogs/dialog_npc_baseline.json`
- Dialogue personality/banter pass completed:
  - named NPC trees upgraded with rumor branches + character voice in `assets/data/dialogs/dialog_npc_baseline.json`
  - ambient NPC banter pack added in `assets/data/dialogs/dialog_ambient_banter_pack.json`
  - assignment map and pass notes: `docs/reports/npc_banter_pack_2026-02-09.md`, `docs/reports/dialog_tone_pass_2026-02-09.md`
- Ambient town population placement completed:
  - `52` ambient NPC records generated in `assets/data/npcs` (`npc_ambient_*.json`)
  - ambient placements wired into `assets/data/maps/map_towns_act1.json` and `assets/data/maps/map_towns_act2_3.json` via `ambient_npcs`
  - validation report: `docs/reports/ambient_npc_population_pass_2026-02-09.md`
- Ambient day/night weather schedules completed:
  - all `52` ambient NPCs now have moving `schedule.day/night/rain` coordinates
  - canonical spawn (`coords`) remains aligned to day schedule for compatibility
  - validation report: `docs/reports/ambient_npc_schedule_pass_2026-02-09.md`
- Story/dialog/location final deep pass completed:
  - added `12` explicit story setpiece map records in `assets/data/maps/map_story_setpieces.json`
  - mapped all `85/85` content main-quest stages to concrete `target_location_id` values
  - added cinematic alias registry for story-only NPC tokens: `content/dialog/story_npc_alias_registry.json`
  - final report + map matrix: `docs/reports/story_dialog_location_final_deep_check_2026-02-09.md`, `docs/reports/story_dialog_location_map_2026-02-09.csv`
- Story routing and progression gate pass completed:
  - main-quest stage hop connectivity is now complete (`0` missing links)
  - late-game access gates tightened for tower/palace/remnant/capital-void transitions
- Encounter integrity and pacing pass completed:
  - encounter table coverage synchronized (`0` map/table mismatches)
  - full-table pacing normalization applied across all encounter files
  - report: `docs/reports/encounter_pacing_pass_2026-02-10.md`
- Added automated world integrity validator:
  - `tools/validate_world_integrity.py` validates map graph, quest hops, encounter coverage, and gate token sanity
- Remaining tracked blocker is final mastered audio replacement (BGM/SFX/VO).

---

## 📚 QUICK LINKS - Asset Reference Docs

**New SNES Asset Documentation:**
- 📋 [MASTER_ASSET_INDEX](docs/asset_reference/MASTER_ASSET_INDEX.md) - Central hub for all asset docs
- 🗺️ [ZONE_ASSET_MAPPING](docs/asset_reference/ZONE_ASSET_MAPPING.md) - Zone-to-asset assignments
- 📐 [EXTRACTION_COORDINATES](docs/asset_reference/EXTRACTION_COORDINATES.md) - Pixel coordinates for extraction
- 🎨 [VISUAL_STYLE_GUIDE](docs/asset_reference/VISUAL_STYLE_GUIDE.md) - Color/style adaptation rules
- 📅 [IMPLEMENTATION_ROADMAP](docs/asset_reference/IMPLEMENTATION_ROADMAP.md) - 4-week implementation plan
- 🏛️ [PALACE_DUNGEON_LAYOUT](docs/asset_reference/PALACE_DUNGEON_LAYOUT.md) - Final dungeon design
- 🏚️ [CAPITAL_RUINS_ENCOUNTERS](docs/asset_reference/CAPITAL_RUINS_ENCOUNTERS.md) - Ruins encounter design

**Asset Analysis:**
- [SNES_ASSETS_ANALYSIS](docs/SNES_ASSETS_ANALYSIS.md) - Full SNES asset catalog
- [NEW_SNES_ASSETS_ANALYSIS](docs/NEW_SNES_ASSETS_ANALYSIS.md) - Terranigma, BoF2, Albert Odyssey

---

## 📊 PRODUCTION STATISTICS

### Content Overview:
| Category | Count | Status |
|----------|-------|--------|
| **Zones** | 15 | ✅ Designed |
| **NPCs** | 322 | ✅ Distributed |
| **Monsters** | 305 | ✅ Cataloged |
| **Dialog Files** | 180+ | ✅ Written |
| **Mini-Quests** | 200+ | ✅ Created |
| **Main Quests** | 15 | ✅ Written |

### NPC Breakdown:
| Source | Count |
|--------|-------|
| Original Quirky NPCs | 172 |
| Breath of Fire | 55 |
| Star Ocean | 35 |
| Tales of Phantasia | 30 |
| Dragon Quest 3 | 20 |
| Bakumatsu Kourinden Oni | 15 |

### Monster Breakdown:
| Tier | Count |
|------|-------|
| Critter | 59 |
| Hunter | 75 |
| Predator | 77 |
| Apex | 60 |
| Legendary | 32 |
| Boss | 2 |

---

# SECTION A: MAP MANIFEST

## Global Prompt Tag
*Prepend to every map generation prompt:*

> "Top-down SNES/PS1-era JRPG pixel-art tilemap, 16x16 tiles, clean readable paths, no characters, no UI, consistent palette, crisp edges, slight ambient lighting, designed for gameplay navigation."

---

## 1) OVERWORLD

- [x] **OW_ORION_320x180** — Orion Overworld
  - **Display Name:** World Map
  - **Purpose:** Fast travel hub, shows all discovered locations
  - **Style Prompt:** "Large continent overworld with biome bands (dust flats SW, uplands W, mire basin W-central, prism highlands central, ember rim SE-central, tide coast SE, obsidian rift south, frostmarch north, chrono shelf NE, ruined capital far east), roads connecting major nodes, rivers, cliffs, ports, landmarks."
  - **Connections:** All towns, dungeons, routes
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

---

## 2) TOWNS (Primary)

- [x] **T_DUSTHAVEN_112x72** — Dusthaven
  - **Display Name:** Dusthaven
  - **Purpose:** First town, tutorial hub, Ironhawk Syndicate territory
  - **Style Prompt:** "Desert frontier town, sun-bleached wood and scrap metal, windmills, dusty main street, small plaza, town gate to outskirts."
  - **NPCs:** Broker Vane, Blacksmith Kellen, Weapon/Armor merchants, Gamblers
  - **Interiors:** Inn, Shop, Smith, 2 Houses, Secret Gambling Den
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **T_ASHVEIL_112x72** — Ashveil Sanctuary
  - **Display Name:** Ashveil Sanctuary
  - **Purpose:** First sanctuary, D1 quest hub, Korr recruitment
  - **Style Prompt:** "Stone sanctuary town in uplands, terraces, prayer garden, worn statues, warm lanterns, calm mood."
  - **NPCs:** Mira Thorn, Captain Varros, Sanctuary Keeper, Refugee family
  - **Interiors:** Mira's Rest (Inn), General Store, Heartroot Hall, Barracks, Houses
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **T_MIREWATCH_112x72** — Mirewatch
  - **Display Name:** Mirewatch
  - **Purpose:** D2 approach, Sister Amara quests, swamp atmosphere
  - **Style Prompt:** "Swamp town on stilts, boardwalks, lantern posts, moss, shallow water edges, watchtower."
  - **NPCs:** Sister Amara, Dock workers, Watch captain
  - **Interiors:** Infirmary, Apothecary, Houses, Watch platform
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **T_PRISMRIDGE_112x72** — Prismridge
  - **Display Name:** Prismridge
  - **Purpose:** D3 hub, crystal mining, Old Kell cartographer quests
  - **Style Prompt:** "Highland crystal town, prismatic stone, clean paths, reflective pools, light pylons, cliff edges."
  - **NPCs:** Old Kell, Mine Foreman, Crystal merchant
  - **Interiors:** Survey Office, Crystal Shop, Miner's Hall, Houses
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **T_CINDERSTEP_112x72** — Cinderstep
  - **Display Name:** Cinderstep
  - **Purpose:** D6 approach, Forge Master Grimjaw, Grit/Senna recruitment
  - **Style Prompt:** "Volcanic step-town, basalt, ember braziers, heat haze, switchback stairs, forge corner."
  - **NPCs:** Forge Master Grimjaw, Senna (pre-recruitment), Miners
  - **Interiors:** Master Forge, Supply Depot, Houses
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **T_BRINEGATE_112x72** — Brinegate Port
  - **Display Name:** Brinegate Port
  - **Purpose:** D5 access, maritime hub, Marinus recruitment
  - **Style Prompt:** "Coastal port town, docks, nets, salt-stained wood, lighthouse, tide pools, shipyard."
  - **NPCs:** Dockmaster Sarai, Marinus (pre-recruitment), Sailors
  - **Interiors:** Dock Market, Shipyard Office, Seaside Inn, Houses
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **T_GRAVEMARK_112x72** — Gravemark Outpost
  - **Display Name:** Gravemark Outpost
  - **Purpose:** Northern frontier, rail hub, D7 approach
  - **Style Prompt:** "Bleak northern outpost, stone walls, cairns, dead pines, cold lamps, supply yard."
  - **NPCs:** Rail Captain Dorsa, Supply officers, Workers
  - **Interiors:** Loading Yard office, Supply depot, Barracks
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **T_RIMEHOLD_112x72** — Rimehold
  - **Display Name:** Rimehold
  - **Purpose:** D7 hub, Archive District access, frozen atmosphere
  - **Style Prompt:** "Ice-fort town, snow-packed streets, frosted rooftops, warm windows, gate to citadel road."
  - **NPCs:** Archivist Velm, Townsfolk, Guards
  - **Interiors:** Ledger of Seasons, General Store, Houses, Warm halls
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **T_CHRONOWAKE_112x72** — Chronowake Pier
  - **Display Name:** Chronowake Pier
  - **Purpose:** Chrono access, time-themed, terminal hub
  - **Style Prompt:** "Chrono-coast pier town, pylons and terminals, weathered docks, faint clockwork motifs, sea mist."
  - **NPCs:** Terminal Operator, Dock workers, Time-keepers
  - **Interiors:** Terminal Hall, Pier Market, Houses
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **T_MERIDIAN_112x72** — Meridian Junction
  - **Display Name:** Meridian Junction
  - **Purpose:** Major hub, best shops in Act II, fast travel router
  - **Style Prompt:** "Transit town, clean stone platforming, signage, rails, terminals, 'hub' vibe."
  - **NPCs:** Various merchants, Terminal Operator, Quest givers
  - **Interiors:** Emporium, Armory, Alchemy Shop, Inn, Terminal
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **T_LUMENCREST_OUTER_112x72** — Old Lumencrest: Outer Wards
  - **Display Name:** Old Lumencrest Outer Wards
  - **Purpose:** Capital approach, Resistance contact, ruined atmosphere
  - **Style Prompt:** "Ruined capital outer wards, cracked boulevards, barricades, camp vendor corner, salvage tents, ominous skyline."
  - **NPCs:** Resistance Contact Varin, Refugees, Black market dealers
  - **Interiors:** Safe houses, Hidden basement, Ruined buildings
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **T_CROWN_HUB_112x72** — Crown District Hub
  - **Display Name:** Crown District Hub
  - **Purpose:** Final approach to Palace, Dominion high security
  - **Style Prompt:** "Crown district hub, palace perimeter, guarded plazas, banners, broken grandeur, multiple exits."
  - **NPCs:** Dominion officials (limited interaction), Resistance contacts
  - **Interiors:** Government offices, Restricted areas
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **T_AETHERREACH_112x72** — Aetherreach (Sky Town)
  - **Display Name:** Aetherreach
  - **Purpose:** Post-game hub, endgame shop, Seam Warden
  - **Style Prompt:** "Floating sky town, white stone and prisms, cloud bridges, terraces, quiet gardens, central spire."
  - **NPCs:** Seam Warden, Endgame merchants
  - **Interiors:** Endgame Emporium, Sky gardens, Vault access
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

---

## 3) TOWN INTERIORS (Reusable Set)

- [ ] **I_INN_32x24** — Inn Interior
  - **Purpose:** Rest, save, rumors, party banter
  - **Layout:** Counter, 3-4 tables, stairs to rooms (implied), warm lighting
  - **Style Prompt:** "Top-down pixel interior, cozy lighting, readable furniture layout, clear walk lanes, inn atmosphere."
  - **Variations:** Desert (Dusthaven), Sanctuary (Ashveil), Swamp (Mirewatch), Port (Brinegate), etc.
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [ ] **I_ITEMSHOP_32x24** — Item Shop
  - **Purpose:** Buy/sell consumables, basic gear
  - **Layout:** Counter, shelves, display tables, storage
  - **Style Prompt:** "Top-down pixel interior, shop lighting, organized shelves, merchant counter, clear walk lanes."
  - **Variations:** General store, Apothecary, Dock market
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [ ] **I_SMITH_32x24** — Smith/Forge
  - **Purpose:** Weapons, armor, repairs, crafting
  - **Layout:** Forge (center/back), anvil, weapon racks, counter
  - **Style Prompt:** "Top-down pixel interior, forge glow lighting, industrial layout, tool stations, heat haze effect."
  - **Variations:** Basic forge, Master forge (Cinderstep)
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [ ] **I_HOUSE_A_24x18** — Residential House Variant A
  - **Purpose:** NPC homes, quest locations, lore
  - **Layout:** Main room, kitchen area, 1-2 bed spaces
  - **Style Prompt:** "Top-down pixel interior, home lighting, lived-in details, compact layout."
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [ ] **I_HOUSE_B_24x18** — Residential House Variant B
  - **Purpose:** Different layout for variety
  - **Layout:** Different arrangement of same elements
  - **Style Prompt:** "Top-down pixel interior, home lighting, different layout variant."
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [ ] **I_HALL_40x28** — Town Hall / Sanctuary / Captain's Office
  - **Purpose:** Major NPC meetings, quest turn-in, story scenes
  - **Layout:** Open floor, central desk/altar, seating, impressive scale
  - **Style Prompt:** "Top-down pixel interior, grand lighting, official/sanctified atmosphere, clear focal point."
  - **Variations:** Sanctuary (Ashveil), Town Hall, Command center
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [ ] **I_SECRET_24x18** — Secret Room / Backroom
  - **Purpose:** Black market, hidden quests, Resistance meetings
  - **Layout:** Cluttered, hidden entrance, suspicious atmosphere
  - **Style Prompt:** "Top-down pixel interior, dim lighting, cluttered secret space, hidden goods."
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

---

## 4) ROUTES / MICRO-MAPS

- [x] **MIC_R01A_48x32** — Dusthaven Outskirts
  - **Purpose:** Tutorial combat zone, approach to Ashveil
  - **Style Prompt:** "Top-down pixel route micro-map, clear pathing, 2–3 landmark setpieces, light hazard tiles visually distinct, desert edge transitioning to uplands."
  - **Exits:** N to R01B, S to Dusthaven
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **MIC_R01B_96x40** — Dustbelt Track
  - **Purpose:** Connect Dusthaven to Ashveil
  - **Style Prompt:** "Top-down pixel route micro-map, dust flats, wagon ruts, cliff edges, dust storm hazard zones."
  - **Exits:** W to R01A, E to Ashveil
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **MIC_R02_80x48** — Ashveil Fellpath
  - **Purpose:** Approach to D1
  - **Style Prompt:** "Top-down pixel route micro-map, upland scrub, dead trees, ancient stone markers, ominous approach to ruins."
  - **Exits:** W to Ashveil, E to D1
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **MIC_R03_104x56** — Marshroad Way
  - **Purpose:** Connect Ashveil region to Mirewatch
  - **Style Prompt:** "Top-down pixel route micro-map, transitional wetlands, boardwalk sections, mist pools."
  - **Exits:** Various
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **MIC_R04_56x36** — Fungal Threshold
  - **Purpose:** D2 approach
  - **Style Prompt:** "Top-down pixel route micro-map, fungus emergence, bioluminescent hints, wrong-color vegetation."
  - **Exits:** To D2
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **MIC_R05_112x56** — Glimmerfen Ridgepath
  - **Purpose:** Prismridge approach
  - **Style Prompt:** "Top-down pixel route micro-map, crystal formations begin, elevation gain, cleaner air."
  - **Exits:** To Prismridge
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **MIC_R06_64x36** — Crystal Gate Pass
  - **Purpose:** D3 approach
  - **Style Prompt:** "Top-down pixel route micro-map, crystal archway, refracted light effects, narrow pass."
  - **Exits:** To D3
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **MIC_R07_104x56** — Suncleft Switchbacks
  - **Purpose:** Cinderstep approach
  - **Style Prompt:** "Top-down pixel route micro-map, volcanic terrain begins, heat shimmer, obsidian shards."
  - **Exits:** To Cinderstep
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **MIC_R08_72x40** — Ember Stair Approach
  - **Purpose:** D6 approach
  - **Style Prompt:** "Top-down pixel route micro-map, lava flows visible, stair-cut rock, industrial mining presence."
  - **Exits:** To D6
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **MIC_R09_120x56** — Saltflare Coastway
  - **Purpose:** Brinegate approach
  - **Style Prompt:** "Top-down pixel route micro-map, coastal cliffs, salt spray, seabirds, descent to port."
  - **Exits:** To Brinegate
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **MIC_S01_72x40** — Brinegate Run (Sea Lane)
  - **Purpose:** Water approach, submersible launch
  - **Style Prompt:** "Top-down pixel route micro-map, dock extension, open water, submersible berths."
  - **Exits:** To D5 (underwater)
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **MIC_S02_80x44** — Abyss Descent Channel
  - **Purpose:** Underwater approach to D5
  - **Style Prompt:** "Top-down pixel route micro-map, underwater trench, pressure gates, bioluminescent depth markers."
  - **Exits:** To D5
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **MIC_R10_104x56** — Blackglass Haulroad
  - **Purpose:** Gravemark approach
  - **Style Prompt:** "Top-down pixel route micro-map, industrial rail line, cargo wagons, bleak landscape."
  - **Exits:** To Gravemark
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **MIC_R11_120x56** — Cairnwind Pass
  - **Purpose:** Rimehold approach
  - **Style Prompt:** "Top-down pixel route micro-map, elevation gain, wind-swept rocks, first snow patches."
  - **Exits:** To Rimehold
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **MIC_R12_112x56** — Frostmarch Iceway
  - **Purpose:** D7 approach
  - **Style Prompt:** "Top-down pixel route micro-map, frozen road, ice bridges, time-frozen anomalies."
  - **Exits:** To D7
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **MIC_R13_64x36** — Citadel Approach
  - **Purpose:** Final approach to D7
  - **Style Prompt:** "Top-down pixel route micro-map, frozen citadel visible, foreboding grandeur."
  - **Exits:** To D7
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **MIC_R14_128x56** — Glacier Shelfway
  - **Purpose:** Chronowake approach
  - **Style Prompt:** "Top-down pixel route micro-map, ice shelf, chrono-anomalies, clockwork debris."
  - **Exits:** To Chronowake
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **MIC_R15_72x40** — Phase-Lane Causeway
  - **Purpose:** Meridian Junction approach
  - **Style Prompt:** "Top-down pixel route micro-map, stabilized time-lane, phase-shifted architecture."
  - **Exits:** To Meridian
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **MIC_R16_136x56** — Meridian Ruinway
  - **Purpose:** Capital approach
  - **Style Prompt:** "Top-down pixel route micro-map, grand ruinway, fallen monuments, capital skyline."
  - **Exits:** To Old Lumencrest
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

---

## 5) DUNGEONS (Mainline)

- [x] **D1_RUINS_96x96** — Ruins of Ashveil
  - **Display Name:** Ruins of Ashveil
  - **Purpose:** First dungeon, Growth Foundation, tutorial
  - **Submaps:** D1_GATEHOUSE, D1_LOWER, D1_PUZZLE_WINGS, D1_PEDESTAL_CHAMBER
  - **Style Prompt:** "Ancient stone ruins, collapsed halls, moss, weight/grav motifs, puzzle doors, pedestal chamber."
  - **Boss:** The Bloom
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **D2_FUNGAL_96x96** — Fungal Depths
  - **Display Name:** Fungal Depths
  - **Purpose:** Motion Foundation, gravity puzzles
  - **Style Prompt:** "Bioluminescent fungus caverns, spores, roots, wet rock, growth nodes."
  - **Boss:** The Sporocyte
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **D3_CRYSTAL_96x96** — Crystal Caverns
  - **Display Name:** Crystal Caverns
  - **Purpose:** Light Foundation, prism puzzles
  - **Style Prompt:** "Crystal cave network, reflective walls, beam gates, shardfalls, bright + cold palette."
  - **Boss:** The Prism
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **D4_SKYSPIRE_96x96** — Skyspire Temple
  - **Display Name:** Skyspire Temple
  - **Purpose:** Heat Foundation, World Break trigger
  - **Style Prompt:** "High temple, wind channels, terraces, motion motifs, open shafts, gust puzzles."
  - **Boss:** The Inferno
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **D5_ABYSS_96x96** — Abyssal Trench
  - **Display Name:** Abyssal Trench
  - **Purpose:** Tide Foundation, underwater
  - **Style Prompt:** "Undersea trench ruins, kelp-dark, pressure locks, glowing fauna, sub-tech gates."
  - **Boss:** The Depthcaller
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **D6_OBSIDIAN_96x96** — Obsidian Quarry
  - **Display Name:** Obsidian Quarry / Molten Core
  - **Purpose:** Mass Foundation, industrial/mining
  - **Submap:** D6_CORE_80x80
  - **Style Prompt:** "Industrial quarry, mine rigs, lava vents, molten chambers, heat hazards."
  - **Boss:** The Colossus
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **D7_FROZEN_96x96** — Frozen Citadel
  - **Display Name:** Frozen Citadel
  - **Purpose:** Time Foundation, time puzzles
  - **Style Prompt:** "Ice fortress, time-frost shimmer, frozen halls, slow zones, blizzard courtyards."
  - **Boss:** Elder Mordai
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **D8_VOID_112x96** — Void Nexus
  - **Display Name:** Void Nexus
  - **Purpose:** Shadow Foundation, final pre-Tower dungeon
  - **Style Prompt:** "Shadow foundation dungeon, void architecture, glitch seams, null pylons, oppressive lighting."
  - **Boss:** The Voidhound
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

---

## 6) CAPITAL CHAIN

- [x] **MIC_GRAND_BOULEVARD_80x40** — Grand Boulevard Micro
  - **Purpose:** Connect Lumencrest to Archive
  - **Style Prompt:** "Ruined capital, edited-record motifs, time locks, palace perimeter grandeur, void seams."
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **D_ARCHIVE_112x96** — Archive District Dungeon
  - **Display Name:** Archive District
  - **Purpose:** Key acquisition, lore, Aurora Foundry
  - **Style Prompt:** "Ruined capital, edited-record motifs, time locks, palace perimeter grandeur, void seams."
  - **Boss:** Archive Guardian
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **MIC_CROWN_APPROACH_96x40** — Crown District Approach
  - **Purpose:** Final approach
  - **Style Prompt:** "Ruined capital, edited-record motifs, time locks, palace perimeter grandeur, void seams."
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **MIC_CROWN_TO_PALACE_56x32** — Crown District → Palace Entrance
  - **Purpose:** Final corridor
  - **Style Prompt:** "Ruined capital, edited-record motifs, time locks, palace perimeter grandeur, void seams."
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **MIC_CONDUIT_64x32** — Crown Spire Conduit
  - **Purpose:** Pre-Palace transition
  - **Style Prompt:** "Ruined capital, edited-record motifs, time locks, palace perimeter grandeur, void seams."
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **D_PALACE_128x96** — Palace Interior
  - **Display Name:** Palace Interior
  - **Purpose:** Final dungeon approach
  - **Style Prompt:** "Ruined capital, edited-record motifs, time locks, palace perimeter grandeur, void seams."
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **MAP_ECLIPSE_80x64** — Eclipse Confluence
  - **Display Name:** Eclipse Confluence
  - **Purpose:** 8 Relics seating, Tower unlock
  - **Style Prompt:** "Ruined capital, edited-record motifs, time locks, palace perimeter grandeur, void seams."
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

---

## 7) HIDDEN AREAS

- [x] **HID_SUNKEN_96x64** — Sunken City
  - **Display Name:** Sunken City
  - **Purpose:** Secret dungeon, legendary weapons
  - **Unlock:** After D5, aquatic travel
  - **Style Prompt:** "Sunken ancient city, coral-claimed architecture, treasure chambers, water pressure puzzles."
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **HID_DRAGON_96x64** — Dragon's Graveyard
  - **Display Name:** Dragon's Graveyard
  - **Purpose:** Secret dungeon, summon unlock
  - **Unlock:** After D6, flight/mountain access
  - **Style Prompt:** "Ancient dragon burial ground, massive bones, draconic energy, reverent atmosphere."
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

---

## 8) SHRINES

*Small shrine trial maps, symmetric layout, 1 main mechanic arena*

- [x] **SHR_HEAT_64x48** — Pyreheart Reliquary
  - **Boss:** Heat Elemental
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **SHR_GROWTH_64x48** — Verdant Covenant Grove
  - **Boss:** Growth Warden
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **SHR_LIGHT_64x48** — Prismwrit Chapel
  - **Boss:** Light Seraph
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **SHR_MOTION_64x48** — Kinetic Vow Atrium
  - **Boss:** Motion Sylph
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **SHR_MASS_64x48** — Gravestone Monad
  - **Boss:** Mass Golem
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **SHR_TIME_64x48** — Chronicle Loom
  - **Boss:** Time Weaver
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **SHR_SHADOW_64x48** — Umbral Ledger Sepulcher
  - **Boss:** Shadow Wraith
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **SHR_TIDE_64x48** — Marinus's Sanctum
  - **Boss:** Tide Leviathan
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

---

## 9) TOWER + FINAL PALACE

- [x] **TWR_LOBBY_96x64** — Tower Lobby
  - **Purpose:** Entry, save point, shop, party management
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **TWR_REWARD_48x32** — Tower Reward Sanctum
  - **Purpose:** Post-boss rewards
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **TWR_ARENA_F10_48x48** — Dax Kaine Arena
  - **Boss:** Dax Kaine
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **TWR_ARENA_F15_48x48** — Ressa Vane Arena (Captain)
  - **Boss:** Captain Ressa Vane
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **TWR_ARENA_F25_48x48** — Yakov Thorne Arena
  - **Boss:** Yakov Thorne
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **TWR_ARENA_F35_48x48** — Cael Rorr Arena (Captain)
  - **Boss:** Captain Cael Rorr
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **TWR_ARENA_F50_64x64** — Mercer Arena
  - **Boss:** Mercer
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **TWR_ARENA_F55_48x48** — Bront Kessel Arena (Captain)
  - **Boss:** Captain Bront Kessel
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **TWR_ARENA_F65_48x48** — Venn Holt Arena (Captain)
  - **Boss:** Captain Venn Holt
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **TWR_ARENA_F75_64x64** — Sentinel Arena
  - **Boss:** Sentinel
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **TWR_ARENA_F85_48x48** — Null Scribe Arena (Captain)
  - **Boss:** Captain Null Scribe
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **TWR_ARENA_F90_64x64** — Void Architect Arena
  - **Boss:** Void Architect
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **TWR_ARENA_F95_48x48** — Seam Warden Prime Arena (Captain)
  - **Boss:** Seam Warden Prime
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **TWR_ARENA_F100_64x64** — Alexander Arena
  - **Boss:** Alexander the Gate
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **PAL_F1_64x64** — Final Palace Floor 1: Elemental Lords
  - **Boss:** Elemental Lords (4-phase)
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **PAL_F2_64x64** — Final Palace Floor 2: Chronowarden
  - **Boss:** Chronowarden
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **PAL_F3_64x64** — Final Palace Floor 3: Void Empress
  - **Boss:** Void Empress
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **PAL_F4_64x64** — Final Palace Floor 4: Ancient Drake
  - **Boss:** Ancient Drake
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **PAL_F5_80x80** — Final Palace Floor 5: Progenitor Engine
  - **Boss:** Progenitor Engine (8-phase final)
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **PAL_REWARD_48x32** — Final Palace Reward Sanctum
  - **Purpose:** Ending sequence, rewards
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

---

## 10) REMNANT VAULT (Post-Game)

- [x] **RV_GATEHOUSE_96x72** — Remnant Gatehouse Hub
  - **Purpose:** Entry hub, wing selection
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **RV_WING_A_96x64** — Cinder-Scar Gallery (Combat Focus)
  - **Purpose:** Combat challenges, super boss
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **RV_WING_B_96x64** — Edited Archive Annex (Puzzle Focus)
  - **Purpose:** Puzzle challenges, super boss
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **RV_WING_C_96x64** — Veilroot Catacombs (Exploration Focus)
  - **Purpose:** Exploration challenges, super boss
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

- [x] **RV_CORE_64x64** — Core Vault Arena
  - **Boss:** Remnant Custodian (Ultimate)
  - **Status:** ☐ Not Started | ☐ In Progress | ☐ Complete

---

# SECTION B: SPRITE MANIFEST

## 1) CHARACTER ART (Per Playable Character - 13 Total)

*For each character, minimum "ship it" bundle:*

### Base Required for All 13 Characters:
- [ ] **Overworld Sprite** — 4-direction, 3-frame walk + idle
  - Directions: North, South, East, West
  - Frames per direction: 3 (idle, step1, step2)
  - Size: 16x24 or 16x32 pixels
  - Pivot: Bottom center
  - Status per character:
    - [ ] Kade
    - [ ] Nix-7
    - [ ] Twist
    - [ ] Korr
    - [ ] Renna
    - [ ] Suresh
    - [ ] Sova
    - [ ] Grit
    - [ ] Ashka
    - [ ] Senna
    - [ ] Callum
    - [ ] Petra
    - [ ] Vex

- [ ] **Portrait (Dialogue)** — Bust/head shot
  - Size: 64x64 or 96x96
  - Expression variants: Neutral, Happy, Sad, Angry, Surprised
  - Status per character:
    - [ ] Kade
    - [ ] Nix-7
    - [ ] Twist
    - [ ] Korr
    - [ ] Renna
    - [ ] Suresh
    - [ ] Sova
    - [ ] Grit
    - [ ] Ashka
    - [ ] Senna
    - [ ] Callum
    - [ ] Petra
    - [ ] Vex

- [ ] **Battle Sprite** — Front or side view
  - Size: 32x48 or 48x64
  - Idle pose
  - Status per character:
    - [ ] Kade
    - [ ] Nix-7
    - [ ] Twist
    - [ ] Korr
    - [ ] Renna
    - [ ] Suresh
    - [ ] Sova
    - [ ] Grit
    - [ ] Ashka
    - [ ] Senna
    - [ ] Callum
    - [ ] Petra
    - [ ] Vex

- [ ] **Battle Animations**
  - Attack: 3-4 frames
  - Skill: 4-6 frames
  - Hurt: 2 frames
  - KO: 1 frame (down pose)
  - Victory: 3-4 frames
  - Status per character:
    - [ ] Kade
    - [ ] Nix-7
    - [ ] Twist
    - [ ] Korr
    - [ ] Renna
    - [ ] Suresh
    - [ ] Sova
    - [ ] Grit
    - [ ] Ashka
    - [ ] Senna
    - [ ] Callum
    - [ ] Petra
    - [ ] Vex

### Optional (Nice to Have):
- [ ] **Cutscene Bust** — Higher detail for major scenes
- [ ] **Run Animation** — Faster movement variant
- [ ] **Weapon/Equipment Variants** — Visual equipment changes
- [ ] **Limit Break Pose** — Special stance

---

## 2) NPC SPRITES (Templates for Palette Swap)

### Core Roles (Reusable Across Towns):
- [ ] **Townfolk A** — Civilian male, neutral clothing
- [ ] **Townfolk B** — Civilian female, neutral clothing
- [ ] **Townfolk C** — Child
- [ ] **Merchant** — Shopkeeper apron/outfit
- [ ] **Smith** — Forge-appropriate attire, muscular
- [ ] **Innkeeper** — Apron, welcoming pose
- [ ] **Guard** — Armor, helmet, spear/sword
- [ ] **Captain/Commander** — Distinguished uniform, no helmet
- [ ] **Priest/Attendant** — Robes, religious symbols
- [ ] **Scholar/Archivist** — Robes, glasses, books
- [ ] **Sailor/Dockhand** — Maritime clothing, weathered
- [ ] **Miner/Quarry Worker** — Practical work clothes, helmet
- [ ] **Refugee/Survivor** — Worn clothing, weary
- [ ] **Terminal/Robot/Drone** — Mechanical, capital/tower areas
- [ ] **Dominion Soldier** — Uniform, masked
- [ ] **Dominion Officer** — Distinguished uniform, visible face

### Unique Story NPCs (Named Characters):
- [ ] **Mira Thorn** — Innkeeper, Ashveil
- [ ] **Captain Varros** — Militia, Ashveil
- [ ] **Sanctuary Keeper** — Elder, wise
- [ ] **Broker Vane** — Information dealer
- [ ] **Blacksmith Kellen** — Dusthaven
- [ ] **Dockmaster Sarai** — Chronowake
- [ ] **Old Kell** — Cartographer, Prismridge
- [ ] **Forge Master Grimjaw** — Cinderstep
- [ ] **Sister Amara** — Healer, Mirewatch
- [ ] **Archivist Velm** — Rimehold
- [ ] **Rail Captain Dorsa** — Gravemark
- [ ] **Resistance Contact Varin** — Old Lumencrest
- [ ] **Seam Warden** — Post-game, Aetherreach

---

## 3) ENEMY SPRITES (By Biome Set)

### Dustbelt Set:
- [ ] **Dust Skirmisher** — Humanoid, ragged
- [ ] **Dust Scavenger (Ranged)** — Crossbow/sling
- [ ] **Dust Wasp (Flier)** — Insect, stinger

### Uplands Set:
- [ ] **Rock Brute** — Large, slow
- [ ] **Wind Caster** — Mage, floating
- [ ] **Stray Wisp** — Small, glowing

### Mire Set:
- [ ] **Leechling** — Small, swarm
- [ ] **Sporeling** — Fungal, status inflictor
- [ ] **Mire Bully** — Large amphibian

### Prism Set:
- [ ] **Crystal Ranged** — Light beams
- [ ] **Refraction Image** — Clone/illusion

### Ember/Heat Set:
- [ ] **Ember Runner** — Fast, fire trail
- [ ] **Heat Caster** — Fire magic
- [ ] **Slag Mote** — Small, explosive

### Tide Set:
- [ ] **Scuttler** — Crab-like
- [ ] **Brine Caster** — Water magic
- [ ] **Lampjaw Eel** — Underwater, ambush

### Obsidian Set:
- [ ] **Quarry Brute** — Miner corrupted
- [ ] **Lava Hazard Unit** — Mechanical, heat

### Frost Set:
- [ ] **Frost Skirmisher** — Ice weapons
- [ ] **Chill Caster** — Ice magic
- [ ] **Frozen Watcher** — Stationary, detection

### Chrono/Phase Set:
- [ ] **Chrono Scribe** — Time magic
- [ ] **Phase Scuttler** — Teleporting
- [ ] **Drone** — Mechanical

### Capital/Void Set:
- [ ] **Record Sentry** — Dominion archive guard
- [ ] **Null Caster** — Void magic
- [ ] **Void Elite** — Powerful, late-game

---

## 4) BOSS SPRITES

### Tower Bosses:
- [ ] **Dax Kaine** (F10)
- [ ] **Yakov Thorne** (F25)
- [ ] **Mercer** (F50)
- [ ] **Sentinel** (F75)
- [ ] **Void Architect** (F90)
- [ ] **Alexander** (F100)

### Tower Captains:
- [ ] **Ressa Vane** (F15)
- [ ] **Cael Rorr** (F35)
- [ ] **Bront Kessel** (F55)
- [ ] **Venn Holt** (F65)
- [ ] **Null Scribe** (F85)
- [ ] **Seam Warden Prime** (F95)

### Dungeon Bosses (D1-D8):
- [ ] **The Bloom** (D1)
- [ ] **The Sporocyte** (D2)
- [ ] **The Prism** (D3)
- [ ] **The Inferno** (D4)
- [ ] **The Depthcaller** (D5)
- [ ] **The Colossus** (D6)
- [ ] **Elder Mordai** (D7)
- [ ] **The Voidhound** (D8)

### Final Palace Bosses:
- [ ] **Elemental Lords** (F1) — 4 forms
- [ ] **Chronowarden** (F2)
- [ ] **Void Empress** (F3)
- [ ] **Ancient Drake** (F4)
- [ ] **Progenitor Engine** (F5) — Multiple phases

### Remnant Vault:
- [ ] **Remnant Custodian** (Core Vault)

### Shrine Bosses:
- [ ] **Heat Elemental**
- [ ] **Growth Warden**
- [ ] **Light Seraph**
- [ ] **Motion Sylph**
- [ ] **Mass Golem**
- [ ] **Time Weaver**
- [ ] **Shadow Wraith**
- [ ] **Tide Leviathan**

---

## 5) TILESETS (For Map Assembly)

### Biome Tilesets:
- [ ] **Tileset_Dustbelt** — Desert, scrub, ruins
- [ ] **Tileset_AshveilStone** — Upland, ancient stone, worn
- [ ] **Tileset_MireStilts** — Swamp, boardwalks, water
- [ ] **Tileset_PrismHighland** — Crystal, reflective, elevated
- [ ] **Tileset_EmberBasalt** — Volcanic, lava, heat
- [ ] **Tileset_TideCoast** — Coastal, docks, water
- [ ] **Tileset_ObsidianIndustrial** — Mining, metal, machinery
- [ ] **Tileset_FrostCitadel** — Ice, snow, frozen
- [ ] **Tileset_ChronoPier** — Time-distorted, clockwork
- [ ] **Tileset_CapitalRuins** — Grand, ruined, ominous
- [ ] **Tileset_VoidNexus** — Shadow, glitch, abstract
- [ ] **Tileset_Tower** — Progenitor, mechanical, ascending
- [ ] **Tileset_Palace** — Grand, final, cosmic
- [ ] **Tileset_Aetherreach** — Floating, clouds, pristine
- [ ] **Tileset_RemnantGlitch** — Corrupted, unstable, dangerous

### Common Autotiles:
- [ ] **Water** — Animated surface
- [ ] **Deep Water** — Darker, impassable
- [ ] **Water Edge** — Animated transition
- [ ] **Cliffs N/E/S/W** — Directional cliff faces
- [ ] **Cliff Corners** — NE, NW, SE, SW
- [ ] **Roads** — Dirt, stone paths
- [ ] **Path Edges** — Transitions
- [ ] **Ladders** — Vertical connections
- [ ] **Stairs** — Elevation changes
- [ ] **Bridges** — Over water/chasms
- [ ] **Doors** — Town/building entrances
- [ ] **Portals** — Warp points, magical
- [ ] **Terminals** — Tech interactions
- [ ] **Chests** — Closed, open variants
- [ ] **Signs** — Readable markers

---

## 6) UI SPRITES/ICONS

### Item Icons:
- [ ] **Consumables** — Potions (red), Ethers (blue), Remedies (green)
- [ ] **Materials** — Ores, herbs, crystals (various)
- [ ] **Key Items** — Unique, story-critical

### Equipment Icons:
- [ ] **Weapons** — Sword, Axe, Spear, Staff, Gun, Dagger icons
- [ ] **Armor** — Light, Medium, Heavy chest icons
- [ ] **Accessories** — Ring, Amulet, Belt icons

### Status Icons:
- [ ] **STABILIZED** — Green shield
- [ ] **SYNCED** — Blue link
- [ ] **EXPOSED** — Red target
- [ ] **All standard statuses** — Poison, Burn, Freeze, etc.

### Minimap Icons:
- [ ] **Town** — House symbol
- [ ] **Dungeon** — Cave/entrance
- [ ] **Shrine** — Altar symbol
- [ ] **Tower** — Spire
- [ ] **Hidden** — Question mark
- [ ] **Player** — Arrow/dot
- [ ] **Quest Marker** — Exclamation
- [ ] **Exit** — Arrow

### UI Elements:
- [ ] **Dialogue Box Frames** — Multiple styles
- [ ] **Nameplate Frames** — Character/NPC names
- [ ] **Menu Backgrounds** — Various screens
- [ ] **Button Sprites** — Active/pressed states
- [ ] **Cursor/Selector** — Menu navigation
- [ ] **HP/MP Bars** — Fill graphics
- [ ] **ATB Gauge** — Timer graphic
- [ ] **Limit Break Meter** — Special gauge

---

## 7) VFX SPRITES

### Element Hits:
- [ ] **Heat/Fire** — Explosion, flame burst
- [ ] **Growth/Nature** — Thorns, vines
- [ ] **Light** — Beam, flash, holy burst
- [ ] **Motion/Wind** — Slash, gust, speed lines
- [ ] **Mass/Earth** — Rock spike, quake
- [ ] **Time** — Clock overlay, rewind effect
- [ ] **Shadow/Void** — Dark burst, null zone
- [ ] **Tide/Water** — Splash, wave, bubble

### Hazard Telegraphs:
- [ ] **Lane Lines** — Attack zone indicators
- [ ] **Rings** — AoE markers
- [ ] **Vents** — Fire/steam eruption warning
- [ ] **Flicker Grid** — Unstable zones
- [ ] **Target Markers** — Lock-on indicators

### Environmental Effects:
- [ ] **Portal/Warp** — Teleportation swirls
- [ ] **Save Point** — Glow, particles
- [ ] **Relic Glow** — Foundation energy
- [ ] **Weather** — Rain, snow, ash particles

### Buff/Debuff Overlays:
- [ ] **Protect** — Shield bubble
- [ ] **Haste** — Speed lines on character
- [ ] **Poison** — Green drip effect
- [ ] **Regen** — Heal particles

---

# SECTION C: DATA SCHEMAS

## Map Data Schema (JSON)

```json
{
  "id": "D1_RUINS_96x96",
  "display_name": "Ruins of Ashveil",
  "type": "dungeon",
  "dimensions": {"width": 96, "height": 96, "tile_size": 16},
  "tileset": "Tileset_AshveilStone",
  "encounter_table": "D1_ENCOUNTERS",
  "boss": "THE_BLOOM",
  "music": "dungeon_ruins_theme",
  "connections": [
    {"direction": "west", "target": "MIC_R02", "coords": [0, 48]},
    {"direction": "special", "target": "D1_LOWER", "trigger": "puzzle_solved"}
  ],
  "events": ["RELIC_GROWTH_ACQUIRED", "D1_CLEARED"],
  "lighting": "dim_bioluminescent",
  "weather": "none",
  "loot_table": "D1_CHESTS"
}
```

## NPC Data Schema (JSON)

```json
{
  "id": "NPC_MIRA_THORN",
  "name": "Mira Thorn",
  "location": "T_ASHVEIL_112x72",
  "coords": [58, 62],
  "schedule": {"day": [58, 62], "night": [58, 62]},
  "sprite": "NPC_INNKEEPER_F",
  "dialog_tree": "DT_MIRA_MAIN",
  "shop": "SHOP_MIRA_REST",
  "quests": ["Q_MISSING_SCAVENGERS", "Q_DEBT_COLLECTORS", "Q_FAMILY_HEIRLOOM"],
  "faction": "ASHVEIL_SANCTUARY",
  "attitude": "friendly",
  "flags": {
    "unlocked_by": null,
    "disappears_on": "Q_FAMILY_HEIRLOOM_COMPLETE"
  }
}
```

## Dialog Data Schema (JSON)

```json
{
  "id": "DT_MIRA_MAIN",
  "entries": [
    {
      "id": "GREET_DEFAULT",
      "condition": {"flag": null, "quest": null},
      "text": "Welcome to Mira's Rest. Beds are clean, food is hot...",
      "choices": [
        {"text": "I'd like a room.", "action": "OPEN_INN"},
        {"text": "Tell me about the ruins.", "action": "DIALOG_Q_START"},
        {"text": "Goodbye.", "action": "EXIT"}
      ]
    },
    {
      "id": "GREET_POST_D1",
      "condition": {"flag": "D1_CLEARED"},
      "text": "You cleared the ruins? Maybe things can get better.",
      "choices": [...]
    }
  ]
}
```

## Item Data Schema (JSON)

```json
{
  "id": "ITEM_POTION",
  "name": "Potion",
  "type": "consumable",
  "rarity": 1,
  "icon": "icon_potion",
  "description": "Restore 200 HP to one ally.",
  "flavor": "Basic healing for basic wounds.",
  "effect": {"type": "heal", "target": "single", "amount": 200},
  "buy_price": 50,
  "sell_price": 25,
  "stack_size": 99,
  "usable_in": ["battle", "field"],
  "recipe": {"requires": [{"item": "HERB", "count": 2}, {"item": "WATER", "count": 1}], "alchemy_level": 1}
}
```

## Enemy Data Schema (JSON)

```json
{
  "id": "ENEMY_DUST_SKIRMISHER",
  "name": "Dust Skirmisher",
  "family": "dustbelt",
  "sprite": "spr_dust_skirmisher",
  "stats": {"hp": 120, "mp": 0, "atk": 15, "def": 8, "mag": 0, "spr": 5, "spd": 10},
  "weaknesses": {"fire": 1.5, "ice": 1.0, "thunder": 1.0},
  "resists": {"earth": 0.5},
  "abilities": ["attack", "dust_toss"],
  "loot": [{"item": "LEATHER_SCRAP", "chance": 0.25, "count": [1, 2]}],
  "gil": [10, 25],
  "xp": 30
}
```

## Quest Data Schema (JSON)

```json
{
  "id": "Q_MISSING_SCAVENGERS",
  "name": "Missing Scavengers",
  "type": "side",
  "giver": "NPC_MIRA_THORN",
  "prerequisites": [],
  "steps": [
    {"id": 1, "description": "Search the Supply Depot", "target_location": "MIC_R01B", "objective": "investigate"},
    {"id": 2, "description": "Find the missing scavengers", "target_location": "D1_RUINS_96x96", "objective": "rescue"},
    {"id": 3, "description": "Return to Mira", "target_location": "T_ASHVEIL_112x72", "objective": "talk"}
  ],
  "rewards": {"xp": 500, "gil": 200, "items": [{"item": "POTION", "count": 3}]},
  "unlocks": ["Q_DEBT_COLLECTORS"],
  "flags_set": ["Q_MISSING_SCAVENGERS_COMPLETE"]
}
```

## Encounter Table Schema (JSON)

```json
{
  "id": "D1_ENCOUNTERS",
  "maps": ["D1_RUINS_96x96", "D1_LOWER", "D1_PUZZLE_WINGS"],
  "encounter_rate": 0.15,
  "entries": [
    {"enemies": ["ENEMY_GROWTH_LURKER"], "weight": 40, "min_steps": 5},
    {"enemies": ["ENEMY_GROWTH_LURKER", "ENEMY_GROWTH_LURKER"], "weight": 30, "min_steps": 8},
    {"enemies": ["ENEMY_VINE_SNAKE"], "weight": 20, "min_steps": 10},
    {"enemies": ["ENEMY_BLOOM_SPROUT"], "weight": 10, "min_steps": 15, "rare": true}
  ],
  "special": {
    "boss_trigger": {"condition": "at_coords", "coords": [48, 48], "boss": "THE_BLOOM"}
  }
}
```

## Drop Table Schema (JSON)

```json
{
  "id": "DROPS_AUDIT_DRONE",
  "entries": [
    {"item": "SEAL_WAX_SCRAP", "chance": 0.30, "count": 1},
    {"item": "CROWN_ALLOY_SHARD", "chance": 0.10, "count": 1},
    {"item": "PARADOX_GLASS", "chance": 0.02, "count": 1},
    {"nothing": true, "chance": 0.58}
  ],
  "bonus_roll": {
    "chance": 0.12,
    "reward": {"item": "SEAL_WAX_SCRAP", "count": 1}
  }
}
```

---

# SECTION D: FILE & ID CONVENTIONS

## Naming Conventions

### Maps:
```
{TYPE}_{NAME}_{SIZE}.{ext}

Types:
- OW_ = Overworld
- T_ = Town
- I_ = Interior
- MIC_ = Micro/Route
- D#_ = Dungeon (D1-D8)
- SHR_ = Shrine
- TWR_ = Tower
- PAL_ = Palace
- RV_ = Remnant Vault
- HID_ = Hidden Area

Example: D1_RUINS_96x96.json
```

### Sprites:
```
{TYPE}_{NAME}_{VARIANT}.{ext}

Types:
- spr_ = Sprite
- icon_ = Icon
- tileset_ = Tileset
- fx_ = Effect
- ui_ = UI element

Variants:
- _walk, _idle, _attack, _hurt, _ko
- _N, _S, _E, _W (directions)
- _frame0, _frame1, etc.

Example: spr_kade_walk_S.png
```

### Audio:
```
{TYPE}_{NAME}_{VARIANT}.{ext}

Types:
- bgm_ = Background music
- sfx_ = Sound effect
- vo_ = Voice over
- amb_ = Ambience

Example: bgm_dungeon_ruins_theme.ogg
```

### Data:
```
{CATEGORY}_{NAME}.json

Categories:
- map_ = Map data
- npc_ = NPC definitions
- item_ = Item database
- enemy_ = Enemy database
- quest_ = Quest definitions
- dialog_ = Dialog trees
- encounter_ = Encounter tables
- drop_ = Drop tables
- achievement_ = Achievement/progression data
- ability_ = Character ability definitions
- audio_ = Audio metadata/specification tables
- cutscene_ = Cutscene timeline/index data
- boss_ = Boss encounter set definitions
- shop_ = Shop inventory/economy tables
- system_ = System-level configuration
- tutorial_ = Tutorial prompt/system data

Example: item_consumables.json
```

## Folder Structure Conventions

```
/assets
  /maps
    /overworld
    /towns
    /dungeons
    /routes
    /tower
    /palace
  /sprites
    /characters
      /kade
      /nix
      ...
    /npcs
    /enemies
    /tilesets
    /fx
    /ui
  /audio
    /bgm
    /sfx
    /vo
    /ambience
  /data
    /maps
    /npcs
    /items
    /enemies
    /quests
    /dialogs
```

---

# SECTION E: ANIMATION SPECS

## Sprite Sizes

| Category | Size | Notes |
|----------|------|-------|
| **Overworld Characters** | 16x24 or 16x32 | 4-direction |
| **NPCs** | 16x24 or 16x32 | Match player scale |
| **Enemies (Overworld)** | 16x16 to 24x24 | Varies by size |
| **Enemies (Battle)** | 48x48 to 96x96 | Bosses larger |
| **Bosses (Battle)** | 128x128+ | Screen presence |
| **Tileset Tiles** | 16x16 | Standard |
| **UI Icons** | 16x16, 32x32 | Small and large |
| **Portraits** | 64x64 or 96x96 | Dialogue |

## Frame Counts

| Animation | Frames | Notes |
|-----------|--------|-------|
| **Idle** | 1-2 | Subtle breathing |
| **Walk** | 3-4 | Step cycle |
| **Run** | 3-4 | Faster cycle |
| **Attack** | 3-6 | Strike + recovery |
| **Skill** | 4-8 | Varies by complexity |
| **Hurt** | 2 | Hit + recoil |
| **KO** | 1 | Down pose |
| **Victory** | 3-6 | Celebration |

## Pivot Points

| Sprite Type | Pivot | Reason |
|-------------|-------|--------|
| **Overworld** | Bottom center | Ground alignment |
| **Battle** | Bottom center | Ground alignment |
| **Effects** | Center | Expansion point |
| **UI** | Top-left | Screen alignment |

## Timing Standards

| Action | Frame Duration | Notes |
|--------|----------------|-------|
| **Idle cycle** | 500ms per frame | Slow, subtle |
| **Walk cycle** | 150ms per frame | 4 FPS |
| **Run cycle** | 100ms per frame | 6 FPS |
| **Attack hit** | 50ms on strike frame | Impact emphasis |
| **Effect duration** | 300-1000ms | Varies by effect |

---

# SECTION F: COLLISION & LAYERS

## Layer Stack (Bottom to Top)

```
0. Background (parallax, non-interactive)
1. Ground (walkable tiles)
2. Ground Detail (decoration, walkable)
3. Elevation 1 (cliffs, stairs - blocks movement)
4. Objects Lower (tables, crates - blocks movement)
5. Characters (player, NPCs, enemies)
6. Objects Upper (roofs, trees - player walks under)
7. Effects (weather, particles)
8. Lighting Overlay (darkness, glow)
9. UI (always top)
```

## Collision Types

| Type | Behavior | Examples |
|------|----------|----------|
| **NONE** | Walkable | Ground, floors |
| **FULL** | Blocks all | Walls, cliffs, objects |
| **HEIGHT** | Blocks if elevation differs | Stairs, ledges |
| **WATER** | Slows, swimming | Rivers, pools |
| **HAZARD** | Damages | Lava, void, spikes |
| **INTERACT** | Triggers event | Doors, chests, NPCs |
| **ENCOUNTER** | Triggers battle | Tall grass, danger zones |

## Interaction Triggers

| Trigger | Activation | Use Case |
|---------|------------|----------|
| **on_enter** | Player steps on | Zone transitions, hazards |
| **on_interact** | Button press near | NPCs, doors, chests |
| **on_approach** | Player within radius | Auto-talk, detection |
| **on_leave** | Player exits zone | Cleanup, despawn |

## Z-Depth Rules

```
// Characters sort by Y position within layer
sort_order = layer_priority * 1000 + y_position

// Objects with "upper" flag render above characters
if (object.upper && player.y > object.y) {
    object.render_layer = LAYER_UPPER_OBJECTS;
} else {
    object.render_layer = LAYER_LOWER_OBJECTS;
}
```

---

# COMPLETION CHECKLIST SUMMARY

## Maps: 97 Total
- [x] Overworld: 1
- [x] Towns: 13
- [ ] Interiors: 7
- [x] Routes: 18
- [x] Story Setpieces: 12
- [x] Dungeons: 8
- [x] Capital Chain: 7
- [x] Hidden: 2
- [x] Shrines: 8
- [x] Tower: 14
- [x] Palace: 6
- [x] Remnant Vault: 5

## Sprites: 300+ Total
- [ ] Characters: 13 × 5 sets = 65 (directory scaffolds present; full production sets still pending)
- [x] NPCs: 20+ templates
- [ ] Enemies: 40+ types (32 combat IDs currently authored in data)
- [x] Bosses: 30+ (35 map-linked boss IDs; sprite pool populated)
- [x] Tilesets: 15 (16 tilesets currently referenced by maps)
- [x] UI: 100+ icons
- [ ] VFX: 50+ effects

## Data: 15+ Schema Types
- [x] Map data format
- [x] NPC data format
- [x] Dialog tree format
- [x] Item database format
- [x] Enemy database format
- [x] Quest format
- [x] Encounter tables
- [x] Drop tables
- [x] World integrity validator (`tools/validate_world_integrity.py`)

---

*Last Updated: 2026-02-10*
*Status: Non-audio production pass complete; remaining blocker is final mastered audio replacement*
