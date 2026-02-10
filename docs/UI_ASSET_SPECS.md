# UI Asset Specifications

## Item Icons

### Consumables (16x16, 32x32 variants)
| Icon | Description | Color |
|------|-------------|-------|
| `icon_potion` | Round flask, red liquid | #FF4444 |
| `icon_hi_potion` | Larger flask, red liquid | #FF4444 |
| `icon_mega_potion` | Ornate flask, red liquid | #FF6666 |
| `icon_ether` | Round flask, blue liquid | #4444FF |
| `icon_hi_ether` | Larger flask, blue liquid | #4444FF |
| `icon_elixir` | Dual-chamber flask, gold | #FFD700 |
| `icon_megaelixir` | Star-shaped flask, rainbow | #FFFFFF |
| `icon_phoenix_down` | Feather, golden | #FFD700 |
| `icon_antidote` | Vial with green cross | #44FF44 |
| `icon_echo_screen` | Bell symbol | #CCCCCC |
| `icon_eye_drops` | Eye dropper | #44CCFF |
| `icon_remedy` | Star medical symbol | #FFAA44 |

### Equipment Icons (32x32)
| Icon | Description |
|------|-------------|
| `icon_iron_sword` | Straight blade, silver |
| `icon_steel_sword` | Ornate blade, steel sheen |
| `icon_axe` | Double-bitted axe |
| `icon_spear` | Long spear with tip |
| `icon_staff` | Wooden staff with crystal |
| `icon_dagger` | Curved blade |
| `icon_gun` | Pistol silhouette |
| `icon_rifle` | Long rifle |
| `icon_leather_armor` | Brown chest piece |
| `icon_chainmail` | Metallic mesh pattern |
| `icon_plate_armor` | Full steel plate |
| `icon_robe` | Flowing garment |
| `icon_shield` | Heater shield shape |

### Accessory Icons (16x16)
| Icon | Description | Color |
|------|-------------|-------|
| `icon_ring_bronze` | Simple band | #CD7F32 |
| `icon_ring_silver` | Detailed band | #C0C0C0 |
| `icon_ring_gold` | Ornate band | #FFD700 |
| `icon_amulet` | Pendant on chain | varies |
| `icon_bracelet` | Wrist band | varies |
| `icon_belt` | Waist sash | varies |

## Status Effect Icons (16x16)

| Icon | Effect | Visual |
|------|--------|--------|
| `icon_status_poison` | Poison | Green skull |
| `icon_status_blind` | Blind | Eye with X |
| `icon_status_silence` | Silence | Muted mouth |
| `icon_status_sleep` | Sleep | Zzz symbol |
| `icon_status_confuse` | Confuse | Swirly spiral |
| `icon_status_berserk` | Berserk | Red fist |
| `icon_status_haste` | Haste | Speed lines |
| `icon_status_protect` | Protect | Shield glow |
| `icon_status_shell` | Shell | Magic barrier |
| `icon_status_regen` | Regen | Green plus |
| `icon_status_stabilized` | STABILIZED | Green shield |
| `icon_status_synced` | SYNCED | Blue link |
| `icon_status_exposed` | EXPOSED | Red target |

## Minimap Icons (8x8, 16x16)

| Icon | Description | Color |
|------|-------------|-------|
| `icon_map_player` | Arrow pointing direction | #00FF00 |
| `icon_map_town` | House symbol | #FFFF00 |
| `icon_map_dungeon` | Cave entrance | #FF8800 |
| `icon_map_shrine` | Altar symbol | #00FFFF |
| `icon_map_tower` | Spire | #FF00FF |
| `icon_map_hidden` | Question mark | #888888 |
| `icon_map_shop` | Coin bag | #FFD700 |
| `icon_map_quest` | Exclamation | #FF0000 |
| `icon_map_save` | Crystal | #00FF88 |
| `icon_map_exit` | Arrow | #FFFFFF |

## Menu UI Elements

### Frame Assets (9-slice ready)
```
ui_frame_dialog.png          - Dialogue box border
ui_frame_menu.png            - Menu window border
ui_frame_tooltip.png         - Tooltip background
ui_frame_status.png          - Status panel
ui_frame_command.png         - Battle command window
```

### Button Sprites
```
ui_button_normal.png         - Default button state
ui_button_hover.png          - Mouse hover state
ui_button_pressed.png        - Clicked state
ui_button_disabled.png       - Inactive state
```

### Cursor/Selector
```
ui_cursor_hand.png           - Finger pointer
ui_cursor_arrow.png          - Menu selector
ui_cursor_target.png         - Battle target
```

### Bars and Gauges
```
ui_bar_hp.png                - Health bar (red gradient)
ui_bar_mp.png                - Mana bar (blue gradient)
ui_bar_limit.png             - Limit gauge (rainbow gradient)
ui_bar_atb.png               - ATB gauge (yellow fill)
ui_bar_exp.png               - EXP bar (green)
```

### Font Specifications

| Usage | Font | Size | Style |
|-------|------|------|-------|
| Dialogue text | Pixel font | 16px | Regular |
| Menu headers | Pixel font | 24px | Bold |
| Stats/numbers | Pixel font | 14px | Monospace |
| Button labels | Pixel font | 18px | Regular |

## Screen Layouts

### Battle Screen
```
┌─────────────────────────────────────┐
│  [Party Status: HP/MP/ATB bars]     │
├─────────────────────────────────────┤
│                                     │
│      [Battle Background]            │
│      [Enemy sprites]                │
│      [Player battle sprites]        │
│                                     │
├──────────────────┬──────────────────┤
│ [Command Window] │ [Enemy/Info]     │
│ - Attack         │                  │
│ - Magic          │                  │
│ - Item           │                  │
│ - Limit          │                  │
└──────────────────┴──────────────────┘
```

### Menu Screen
```
┌─────────────────────────────────────┐
│ [Gil] [Location]        [Playtime]  │
├──────────┬──────────────────────────┤
│          │                          │
│ [Menu]   │   [Submenu content]      │
│ - Items  │                          │
│ - Equip  │                          │
│ - Status │                          │
│ - Save   │                          │
│          │                          │
└──────────┴──────────────────────────┘
```

## Status: ☐ Not Started | ☐ In Progress | ☐ Complete
