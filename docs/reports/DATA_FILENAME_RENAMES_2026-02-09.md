# Data Filename Renames (2026-02-09)

This map records normalized data filename changes for compatibility tracking.

## Renamed Files

- `assets/data/achievements.json` -> `assets/data/achievement_master.json`
- `assets/data/abilities/character_abilities.json` -> `assets/data/abilities/ability_character_abilities.json`
- `assets/data/system/credits.json` -> `assets/data/system/system_credits.json`
- `assets/data/system/debug_tools.json` -> `assets/data/system/system_debug_tools.json`
- `assets/data/system/localization_strings.json` -> `assets/data/system/system_localization_strings.json`
- `assets/data/system/save_system.json` -> `assets/data/system/system_save_system.json`
- `assets/data/system/settings_config.json` -> `assets/data/system/system_settings_config.json`

## Notes

- No in-repo references to the old filenames were detected at rename time.
- Validation category coverage was expanded to include data prefixes used by these files.
