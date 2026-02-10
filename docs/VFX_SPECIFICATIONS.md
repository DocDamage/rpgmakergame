# Visual Effects Specifications

## Elemental Hit Effects

### Fire/Heat Effects
| Effect | Frames | Size | Description |
|--------|--------|------|-------------|
| `fx_fire_burst` | 8 | 64x64 | Explosion with flame burst |
| `fx_fire_trail` | 6 | 32x32 | Burning trail for projectiles |
| `fx_ember_spark` | 4 | 16x16 | Small spark particles |
| `fx_heat_wave` | 12 | 96x96 | Distortion wave effect |
| `fx_magma_splash` | 8 | 48x48 | Lava impact |

### Ice Effects
| Effect | Frames | Size | Description |
|--------|--------|------|-------------|
| `fx_ice_shard` | 6 | 64x64 | Ice crystal burst |
| `fx_frost_breath` | 8 | 80x80 | Cold mist cloud |
| `fx_freeze_spread` | 10 | 64x64 | Freezing spread pattern |
| `fx_ice_spike` | 4 | 48x48 | Ground spike |

### Thunder Effects
| Effect | Frames | Size | Description |
|--------|--------|------|-------------|
| `fx_thunder_bolt` | 6 | 128x128 | Lightning strike |
| `fx_thunder_spark` | 4 | 32x32 | Electric spark |
| `fx_paralysis` | 8 | 48x48 | Electricity surrounding target |

### Water/Tide Effects
| Effect | Frames | Size | Description |
|--------|--------|------|-------------|
| `fx_water_splash` | 8 | 64x64 | Splash impact |
| `fx_bubble` | 6 | 32x32 | Bubble particles |
| `fx_wave_crest` | 10 | 96x32 | Wave motion |

### Earth/Mass Effects
| Effect | Frames | Size | Description |
|--------|--------|------|-------------|
| `fx_earth_spike` | 6 | 64x64 | Rock spike from ground |
| `fx_quake_crack` | 8 | 128x64 | Ground cracking |
| `fx_rock_debris` | 6 | 48x48 | Falling rocks |

### Wind/Motion Effects
| Effect | Frames | Size | Description |
|--------|--------|------|-------------|
| `fx_wind_slash` | 6 | 96x32 | Cutting wind lines |
| `fx_gust_spiral` | 8 | 64x64 | Tornado spiral |
| `fx_speed_lines` | 4 | 128x128 | Motion blur lines |

### Light/Shadow Effects
| Effect | Frames | Size | Description |
|--------|--------|------|-------------|
| `fx_light_beam` | 10 | 64x128 | Holy light beam |
| `fx_dark_burst` | 8 | 64x64 | Void explosion |
| `fx_shadow_claw` | 6 | 64x64 | Shadow strike |

## Buff/Debuff Overlays

| Effect | Target | Visual |
|--------|--------|--------|
| `fx_buff_protect` | Character | Rotating shield bubble |
| `fx_buff_haste` | Character | Speed lines on sprite |
| `fx_buff_regen` | Character | Green sparkles rising |
| `fx_buff_shell` | Character | Magic barrier shimmer |
| `fx_debuff_poison` | Character | Green drip effect |
| `fx_debuff_blind` | Character | Black cloud over eyes |
| `fx_debuff_silence` | Character | Muted symbol |
| `fx_debuff_sleep` | Character | Zzz particles |

## Environmental Effects

### Weather
| Effect | Type | Description |
|--------|------|-------------|
| `fx_weather_rain` | Particle | Falling rain drops |
| `fx_weather_snow` | Particle | Falling snowflakes |
| `fx_weather_ash` | Particle | Gray ash falling |
| `fx_weather_dust` | Particle | Brown dust particles |
| `fx_weather_fog` | Overlay | Mist layer |

### Interactive
| Effect | Trigger | Description |
|--------|---------|-------------|
| `fx_portal_activate` | Portal use | Swirling teleport |
| `fx_save_point` | Save crystal | Gentle glow pulse |
| `fx_chest_open` | Chest open | Light burst |
| `fx_level_up` | Level up | Ring explosion |
| `fx_limit_full` | Limit ready | Aura buildup |

## Battle UI Effects

| Effect | Description |
|--------|-------------|
| `fx_atb_fill` | ATB gauge filling |
| `fx_damage_number` | Damage popup |
| `fx_heal_number` | Heal popup |
| `fx_critical_hit` | Critical flash |
| `fx_weakness_hit` | Weakness indicator |
| `fx_resist_hit` | Resist indicator |

## Hazard Telegraphs

| Effect | Description |
|--------|-------------|
| `fx_telegraph_line` | Attack lane marker |
| `fx_telegraph_aoe` | Area of effect ring |
| `fx_telegraph_charge` | Enemy charging |
| `fx_telegraph_target` | Target lock-on |

## Technical Specifications

| Property | Value |
|----------|-------|
| Format | PNG sequence or sprite sheet |
| Frame rate | 12-15 FPS |
| Color depth | 32-bit (with alpha) |
| Blend mode | Additive for glows, Normal for solids |
| Pivot point | Center for hits, Bottom for ground effects |

## Folder Structure

```
assets/sprites/fx/
  elemental/
    fire/
    ice/
    thunder/
    water/
    earth/
    wind/
    light/
    dark/
  buffs/
  debuffs/
  environmental/
  battle_ui/
  hazards/
```

## Status: ☐ Not Started | ☐ In Progress | ☐ Complete
