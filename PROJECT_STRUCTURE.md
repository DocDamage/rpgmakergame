# Chroma's Edge - Project Folder Structure
## Complete Organization for RPG Maker MZ

---

## 📁 ROOT DIRECTORY

```
C:/Users/Doc/Desktop/game/
├── audio/                    # All audio files
├── data/                     # JSON database files
├── docs/                     # Documentation
├── img/                      # All images
├── js/                       # JavaScript plugins
├── movies/                   # Video files (if any)
├── scripts/                  # Python helper scripts
└── Game.exe                  # Game executable (when built)
```

---

## 🎨 IMG/ DIRECTORY STRUCTURE

```
img/
├── animations/               # Battle animations (VFX)
│   ├── impacts/
│   ├── magic/
│   ├── physical/
│   └── status/
├── battlebacks1/            # Battle backgrounds (bottom layer)
│   ├── palace/
│   ├── capital_ruins/
│   ├── frost/
│   ├── ember/
│   ├── tide/
│   ├── uplands/
│   ├── aetherreach/
│   ├── chrono/
│   ├── mire/
│   ├── prism/
│   ├── obsidian/
│   ├── void/
│   └── tower/
├── battlebacks2/            # Battle backgrounds (top layer)
├── characters/              # Character sprites
│   ├── actors/             # Party members (13)
│   ├── npcs/               # NPC sprites
│   └── enemies/            # Monster sprites
├── enemy_battlers/          # Side-view enemy sprites
│   ├── dustbelt/
│   ├── uplands/
│   ├── mire/
│   ├── prism/
│   ├── ember/
│   ├── tide/
│   ├── frost/
│   ├── chrono/
│   ├── capital/
│   ├── void/
│   └── bosses/
├── faces/                   # Face portraits
│   ├── actors/
│   └── npcs/
├── parallaxes/              # Parallax backgrounds
│   ├── gloomwood_forest.png
│   ├── whitewood_vale.png
│   ├── ice_castle.png
│   ├── clouds.png
│   └── fog.png
├── pictures/                # Picture folder (CGs, etc.)
├── sv_actors/              # Side-view actor battlers
├── sv_enemies/             # Side-view enemy battlers
├── system/                 # System graphics
│   ├── IconSet.png         # Item/weapon icons
│   ├── Window.png          # Window skin
│   └── etc.
├── tilesets/               # Map tilesets
│   ├── time_fantasy/
│   ├── ice_cavern/
│   ├── lava_cavern/
│   ├── steampunk/
│   └── etc.
└── titles1/                # Title screen backgrounds
```

---

## 🎵 AUDIO/ DIRECTORY STRUCTURE

```
audio/
├── bgm/                    # Background music
│   ├── towns/
│   ├── dungeons/
│   ├── battle/
│   └── special/
├── bgs/                    # Background sounds
├── me/                     # Musical effects (victory, gameover)
├── se/                     # Sound effects
└── voice/                  # Voice acting (if any)
```

---

## 📊 DATA/ DIRECTORY STRUCTURE

```
data/
├── Actors.json             # Party members (Kade, Nix-7, etc.)
├── Animations.json         # Animation definitions
├── Armors.json             # Armor database
├── Classes.json            # Character classes
├── CommonEvents.json       # Common events
├── Enemies.json            # Monster database
├── Items.json              # Item database
├── Map001.json             # Individual maps
├── Map002.json
├── ...
├── MapInfos.json           # Map metadata
├── Skills.json             # Skill database
├── States.json             # Status effects
├── System.json             # System settings
├── Troops.json             # Enemy groups
├── Weapons.json            # Weapon database
└── ...
```

---

## 📚 DOCS/ DIRECTORY STRUCTURE

```
docs/
├── asset_reference/        # Asset guides
│   ├── ZONE_ASSET_MAPPING.md
│   ├── EXTRACTION_COORDINATES.md
│   ├── VISUAL_STYLE_GUIDE.md
│   └── ...
├── design/                 # Design documents
│   ├── STORY_ARC.md
│   ├── CHARACTERS.md
│   └── QUESTS.md
├── technical/              # Technical docs
│   ├── ENGINE_SETUP.md
│   └── SCRIPTING_GUIDE.md
└── production/             # Production tracking
    └── PRODUCTION_CHECKLIST_MASTER.md
```

---

## 📝 NAMING CONVENTIONS

### Battle Backgrounds
```
[zone]_[location]_[variant].png

Examples:
palace_throne_room_main.png
capital_ruins_town_square.png
frost_ice_cave_entrance.png
ember_fire_temple_main.png
tide_harbor_dock.png
```

### Enemy Sprites
```
[zone]_[monster_name]_[tier].png

Examples:
dustbelt_sand_worm_predator.png
frost_ice_dragon_apex.png
void_void_horror_hunter.png
boss_extinguisher_final.png
```

### Animation Sheets
```
[type]_[element]_[effect].png

Examples:
magic_fire_fireball.png
magic_ice_blizzard.png
physical_slash_sword.png
impact_hit_critical.png
```

### Parallax Backgrounds
```
[zone]_[layer]_[description].png

Examples:
aetherreach_bg_clouds.png
frost_bg_ice_castle.png
remnant_bg_gloomwood.png
```

### Weapon Icons
```
[weapon_type]_[name].png

Examples:
sword_iron_blade.png
axe_battle_axe.png
staff_crystal_rod.png
dagger_assassin_shank.png
```

---

## 🗂️ CURRENT ASSET ORGANIZATION

### Battle Backgrounds (68 files)
```
img/battlebacks1/
├── palace/
│   ├── palace_throne_room_main.png
│   ├── palace_throne_room_alt.png
│   ├── palace_guard_stations.png
│   ├── palace_royal_lounge.png
│   ├── palace_throne_side.png
│   └── palace_castle_hallway.png
├── capital_ruins/
│   ├── capital_ruins_entry_plaza.png
│   ├── capital_ruins_ruined_shop_a.png
│   ├── capital_ruins_ruined_shop_b.png
│   ├── capital_ruins_destroyed_home_a.png
│   ├── capital_ruins_destroyed_home_b.png
│   ├── capital_ruins_apartment_building.png
│   ├── capital_ruins_town_square.png
│   ├── capital_ruins_market_stalls.png
│   ├── capital_ruins_memorial_hall.png
│   ├── capital_ruins_sewer_tunnel.png
│   ├── capital_ruins_underground_chamber.png
│   └── capital_ruins_palace_gate.png
├── bof_generic/
│   ├── bof_grassland.png
│   ├── bof_forest.png
│   ├── bof_desert.png
│   ├── bof_mountain.png
│   ├── bof_cave.png
│   ├── bof_water.png
│   ├── bof2_city.png
│   ├── bof2_ruins.png
│   ├── bof2_sea.png
│   ├── bof2_underwater.png
│   ├── bof2_castle.png
│   └── bof2_dark.png
├── interiors/
│   ├── interior_aretha_house.png
│   ├── interior_bof_oldhouse.png
│   ├── interior_bof2_house.png
│   ├── interior_lastbible_house.png
│   ├── interior_rudra_church.png
│   ├── interior_rudra_temple.png
│   ├── interior_top_house_01.png
│   ├── interior_top_house_02.png
│   ├── interior_top_church.png
│   └── interior_terranigma_house.png
├── dungeons/
│   ├── dungeon_arabian_cave.png
│   ├── dungeon_arabian_quicksand.png
│   ├── dungeon_bof_temple.png
│   ├── dungeon_bof2_cave.png
│   ├── dungeon_dq6_cave.png
│   ├── dungeon_tengai_cavern.png
│   ├── dungeon_top_alvanista.png
│   ├── dungeon_rudra_tower.png
│   └── dungeon_rudra_undersea.png
├── towns/
│   ├── town_so_astral.png
│   ├── town_so_van.png
│   ├── town_top_midgard.png
│   ├── town_tengai_dragon.png
│   ├── town_tengai_katana.png
│   └── town_tengai_royal_dragon.png
├── tide/
│   ├── tide_harbor_main.png
│   ├── tide_ship_deck.png
│   ├── tide_dock_area.png
│   └── tide_warehouse.png
├── uplands/
│   ├── uplands_village_center.png
│   ├── uplands_stone_houses.png
│   └── uplands_mountain_overlook.png
├── aetherreach/
│   ├── aetherreach_floating_plaza.png
│   ├── aetherreach_cloud_bridge.png
│   └── aetherreach_sky_dock.png
└── tower/
    ├── tower_base.png
    ├── tower_mid.png
    └── tower_top.png
```

### Parallax Backgrounds (7 files)
```
img/parallaxes/
├── parallax_gloomwood_forest.png      # Remnant, Mire, Capital
├── parallax_whitewood_vale.png         # Uplands, mountains
├── parallax_ice_castle.png             # Frost zone
├── parallax_clouds_star_ocean.png      # Aetherreach
├── parallax_fog_star_ocean.png         # Transition zones
├── parallax_gote_clouds_day.png        # Aetherreach day
└── parallax_gote_clouds_noon.png       # Aetherreach noon
```

### Animation Packs (17 folders)
```
img/animations/
├── anim_slash/
│   └── slash_spritesheet.png
├── anim_warrior/
│   └── warrior_spritesheet.png
├── anim_paladin/
│   └── paladin_spritesheet.png
├── anim_halloween/
│   └── halloween_spritesheet.png
├── anim_lightning/
│   └── lightning_spritesheet.png
├── vfx_fire_mage/
│   └── fire_mage_spritesheet.png
├── vfx_frost_knight/
│   └── frost_knight_spritesheet.png
├── vfx_necromancer/
│   └── necromancer_spritesheet.png
├── vfx_priest/
│   └── priest_spritesheet.png
├── vfx_rogue/
│   └── rogue_spritesheet.png
├── vfx_starcaller/
│   └── starcaller_spritesheet.png
├── vfx_vampire/
│   └── vampire_spritesheet.png
├── vfx_warlock/
│   └── warlock_spritesheet.png
├── vfx_impacts/
│   └── impacts_spritesheet.png
└── npc_animations/
    └── npc_spritesheets/
```

### Weapon Icons (Organized by type)
```
img/system/IconSet.png (contains all weapon icons)

OR separate for easier management:

img/icons/weapons/
├── swords/
│   ├── sword_iron.png
│   ├── sword_steel.png
│   ├── sword_silver.png
│   ├── sword_mythril.png
│   └── sword_legendary/
├── axes/
├── spears/
├── staves/
├── bows/
├── daggers/
└── guns/
```

---

## 🚀 ORGANIZATION SCRIPT

The Python script `scripts/organize_project.py` will:
1. Create all necessary folders
2. Rename files to follow conventions
3. Move assets to proper locations
4. Generate inventory reports

---

## ✅ POST-ORGANIZATION CHECKLIST

After running organization:
- [ ] All 68 battle backgrounds in battlebacks1/
- [ ] All 7 parallax in parallaxes/
- [ ] All 17 animation packs in animations/
- [ ] Weapon icons in system/ or icons/
- [ ] Documentation in docs/
- [ ] Scripts in scripts/
- [ ] Ready for RPG Maker MZ import

---

*"Organization is the foundation of efficient development."*
