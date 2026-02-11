# Full Project Audit (2026-02-09 deep_pass_3)

## Summary

- issues_critical: **0**
- issues_high: **21**
- issues_medium: **0**
- issues_info: **0**
- total_issues: **21**

## Coverage

- maps: **89**
- encounters: **12**
- drops: **18**
- items: **186**
- enemies_total: **77**
- bosses: **34**
- quests: **38**
- npcs: **17**
- shops: **8**
- dialogs: **20**

## Findings

- [HIGH] `drop_item_ref` (DROPS_BOSS_THE_BLOOM): Unknown first_clear_bonus item: ITEM_GROWTH_RING (`assets/data/drops/drop_bosses.json`)
- [HIGH] `map_boss_ref` (D_ARCHIVE_112x96): Unknown boss ID: BOSS_ARCHIVE_GUARDIAN (`assets/data/maps/map_capital_chain.json`)
- [HIGH] `map_encounter_ref` (D_ARCHIVE_112x96): Unknown encounter_table: ARCHIVE_ENCOUNTERS (`assets/data/maps/map_capital_chain.json`)
- [HIGH] `map_encounter_ref` (D_PALACE_128x96): Unknown encounter_table: PALACE_ENCOUNTERS (`assets/data/maps/map_capital_chain.json`)
- [HIGH] `map_encounter_ref` (MIC_CONDUIT_64x32): Unknown encounter_table: CONDUIT_ENCOUNTERS (`assets/data/maps/map_capital_chain.json`)
- [HIGH] `map_encounter_ref` (MIC_CROWN_TO_PALACE_56x32): Unknown encounter_table: PALACE_APPROACH_ENCOUNTERS (`assets/data/maps/map_capital_chain.json`)
- [HIGH] `map_encounter_ref` (D3_CRYSTAL_96x96): Unknown encounter_table: D3_ENCOUNTERS (`assets/data/maps/map_dungeons_main.json`)
- [HIGH] `map_encounter_ref` (D4_SKYSPIRE_96x96): Unknown encounter_table: D4_ENCOUNTERS (`assets/data/maps/map_dungeons_main.json`)
- [HIGH] `map_encounter_ref` (D5_ABYSS_96x96): Unknown encounter_table: D5_ENCOUNTERS (`assets/data/maps/map_dungeons_main.json`)
- [HIGH] `map_encounter_ref` (D6_OBSIDIAN_96x96): Unknown encounter_table: D6_ENCOUNTERS (`assets/data/maps/map_dungeons_main.json`)
- [HIGH] `map_encounter_ref` (D7_FROZEN_96x96): Unknown encounter_table: D7_ENCOUNTERS (`assets/data/maps/map_dungeons_main.json`)
- [HIGH] `map_encounter_ref` (D8_VOID_112x96): Unknown encounter_table: D8_ENCOUNTERS (`assets/data/maps/map_dungeons_main.json`)
- [HIGH] `map_encounter_ref` (HID_DRAGON_96x64): Unknown encounter_table: DRAGON_GRAVEYARD_ENCOUNTERS (`assets/data/maps/map_hidden_shrines.json`)
- [HIGH] `map_encounter_ref` (HID_SUNKEN_96x64): Unknown encounter_table: SUNKEN_ENCOUNTERS (`assets/data/maps/map_hidden_shrines.json`)
- [HIGH] `map_encounter_ref` (MIC_R01A_48x32): Unknown encounter_table: R01A_ENCOUNTERS (`assets/data/maps/map_routes_act1.json`)
- [HIGH] `map_encounter_ref` (MIC_R01B_96x40): Unknown encounter_table: R01B_ENCOUNTERS (`assets/data/maps/map_routes_act1.json`)
- [HIGH] `map_encounter_ref` (MIC_R02_80x48): Unknown encounter_table: R02_ENCOUNTERS (`assets/data/maps/map_routes_act1.json`)
- [HIGH] `map_encounter_ref` (MIC_R03_104x56): Unknown encounter_table: R03_ENCOUNTERS (`assets/data/maps/map_routes_act1.json`)
- [HIGH] `map_encounter_ref` (MIC_R04_56x36): Unknown encounter_table: R04_ENCOUNTERS (`assets/data/maps/map_routes_act1.json`)
- [HIGH] `map_encounter_ref` (MIC_R05_112x56): Unknown encounter_table: R05_ENCOUNTERS (`assets/data/maps/map_routes_act1.json`)
- [HIGH] `map_encounter_ref` (TWR_ARENA_F10_48x48): Unknown encounter_table: TOWER_F10_ENCOUNTERS (`assets/data/maps/map_tower_palace_remnant.json`)
