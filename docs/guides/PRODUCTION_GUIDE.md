# Production Guide

## Getting Started

1. **Read the checklist**: `PRODUCTION_CHECKLIST_MASTER.md`
2. **Check status**: `docs/ASSET_STATUS_DASHBOARD.md`
3. **Validate naming**: Run `tools/validate_naming.bat`
4. **Use templates**: Copy from `tools/templates/`

## Workflow

### Creating a New Map

1. Copy template: `cp tools/templates/map_template.json assets/data/maps/`
2. Rename: `map_my_map.json`
3. Fill in data
4. Validate: `python tools/validate_naming.py`
5. Update dashboard status

### Creating a New Character

1. Create directory: `assets/sprites/characters/[name]/`
2. Copy README from `assets/sprites/characters/kade/`
3. Follow the asset checklist
4. Update `docs/ASSET_STATUS_DASHBOARD.md`

### Creating Placeholders

See `docs/PLACEHOLDER_ASSET_GUIDE.md`.

Use colored rectangles to make the game playable while art is in progress.

## Directory Quick Reference

```text
assets/
|-- maps/           # Map data and layouts
|-- sprites/        # All visual assets
|   |-- characters/ # Playable characters
|   |-- npcs/       # Non-playable characters
|   |-- enemies/    # Combat enemies
|   |-- bosses/     # Boss sprites
|   |-- tilesets/   # Environment tiles
|   |-- fx/         # Visual effects
|   `-- ui/         # Interface elements
|-- audio/          # Music and sounds
`-- data/           # JSON data files
    |-- maps/
    |-- npcs/
    |-- items/
    |-- enemies/
    |-- quests/
    |-- dialogs/
    |-- encounters/
    `-- drops/
```

## Naming Rules

### Maps
`{TYPE}_{NAME}_{SIZE}.json`
- Types: `OW_`, `T_`, `I_`, `MIC_`, `D1-D8_`, `SHR_`, `TWR_`, `PAL_`, `RV_`, `HID_`
- Example: `D1_RUINS_96x96.json`

### Sprites
`{TYPE}_{NAME}_{VARIANT}.png`
- Types: `spr_`, `icon_`, `tileset_`, `fx_`, `ui_`
- Variants: `_walk`, `_idle`, `_attack`, `_hurt`, `_ko`, `_N`, `_S`, `_E`, `_W`
- Example: `spr_kade_walk_S.png`

### Audio
`{TYPE}_{NAME}_{VARIANT}.ogg`
- Types: `bgm_`, `sfx_`, `vo_`, `amb_`
- Example: `bgm_dungeon_ruins_theme.ogg`

### Data
`{CATEGORY}_{NAME}.json`
- Categories: `map_`, `npc_`, `item_`, `enemy_`, `quest_`, `dialog_`, `encounter_`, `drop_`
- Extended categories: `achievement_`, `ability_`, `audio_`, `cutscene_`, `boss_`, `shop_`, `system_`, `tutorial_`
- Example: `item_consumables.json`

## Support

- Check `PRODUCTION_CHECKLIST_MASTER.md` for full specs
- Run validator before committing
- Update dashboard when status changes
