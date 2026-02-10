# Chroma's Edge - Integration Flag Validation Matrix (v1)
## In-Engine Verification Checklist for Progression, Capital Handoffs, and Endgame Gates

---

## 0) Scope

This matrix validates runtime behavior for:
- Mainline dungeon clear and relic-seat flags
- Capital chain handoff gates
- Palace and final-act route gates
- Endgame confluence and vault gates
- Hidden-area unlock and completion flags
- Post-clear palace voice/UI gate dependencies

This is an execution checklist for implementation QA, not a design spec.

---

## 1) Execution Rules

- Run on a clean profile unless a case explicitly requires seeded state.
- After each step, capture both:
  - player-visible outcome (gate opens, route appears, option appears)
  - raw flag snapshot from debug/state inspector
- Log each case as PASS, FAIL, or BLOCKED.
- Run traceability preflight before engine pass:
  - `powershell -ExecutionPolicy Bypass -File .\check_integration_flag_traceability.ps1`

---

## 2) Test Matrix

| ID | Area | Preconditions | Action | Expected Result |
|----|------|---------------|--------|-----------------|
| FLG-01 | D1 clear | Reach D1 boss | Clear D1 and seat relic | `D1_CLEARED=TRUE`, `RELIC_GROWTH_SEATED=TRUE` |
| FLG-02 | D2 clear | Reach D2 boss | Clear D2 and seat relic | `D2_CLEARED=TRUE`, `RELIC_MOTION_SEATED=TRUE` |
| FLG-03 | D3 clear | Reach D3 boss | Clear D3 and seat relic | `D3_CLEARED=TRUE`, `RELIC_LIGHT_SEATED=TRUE`; mount unlock path fires |
| FLG-04 | D4 clear | Reach D4 boss | Clear D4 and seat relic | `D4_CLEARED=TRUE`, `RELIC_HEAT_SEATED=TRUE` |
| FLG-05 | D5 clear | Reach D5 boss | Clear D5 and seat relic | `D5_CLEARED=TRUE`, `RELIC_TIDE_SEATED=TRUE`, `AQUATIC_TRAVEL_UNLOCKED=TRUE` |
| FLG-06 | D6 clear | Reach D6 boss | Clear D6 and seat relic | `D6_CLEARED=TRUE`, `RELIC_MASS_SEATED=TRUE` |
| FLG-07 | D7 clear | Reach D7 boss | Clear D7 and seat relic | `D7_CLEARED=TRUE`, `RELIC_TIME_SEATED=TRUE` |
| FLG-08 | D8 clear | All required prior states for D8 entry | Clear D8 and seat relic | `D8_CLEARED=TRUE`, `RELIC_SHADOW_SEATED=TRUE` |
| FLG-09 | Archive key | Reach Archive final boss | Clear Archive | `CROWN_ARCHIVE_KEY_ACQUIRED=TRUE` |
| FLG-10 | Crown hub auth | `CROWN_ARCHIVE_KEY_ACQUIRED=TRUE` | Enter Crown hub and run key auth flow | `CONDUIT_AUTHORIZED=TRUE` |
| FLG-11 | Nexus gate | `CONDUIT_AUTHORIZED=TRUE` | Complete hub gate-open sequence | `VOID_NEXUS_GATE_OPEN=TRUE` |
| FLG-12 | R17f gate | `D8_CLEARED=TRUE` and `RELIC_SHADOW_SEATED=TRUE` | Enter R17f palace entrance | R17f route open condition satisfied |
| FLG-13 | Final act gate | Endgame story state reached | Trigger final-act open event | `FINAL_ACT_OPEN=TRUE`; palace gate condition passes |
| FLG-14 | Palace conduit install | Palace interior clear path complete | Use Spire Root console | `SPIRE_ACTUATOR_INSTALLED=TRUE`, `SPIRE_CONDUIT_ROUTE_OPEN=TRUE` |
| FLG-15 | Confluence discovery | `RELIC_SHADOW_SEATED=TRUE` | Perform first seam traversal | `ECLIPSE_CONFLUENCE_DISCOVERED=TRUE` |
| FLG-16 | Confluence final gate | Confluence discovered | Clear all 3 vaults | `VAULT_QUIET_GLASS_CLEARED=TRUE`, `VAULT_BONEWEIGHT_CLEARED=TRUE`, `VAULT_DEEP_SALT_CLEARED=TRUE`, `FINAL_ECLIPSE_GATE_OPEN=TRUE` |
| FLG-17 | Sunken City unlock | `AQUATIC_TRAVEL_UNLOCKED=TRUE` | Attempt Sunken City entry | Entry allowed and `SUNKEN_CITY_DISCOVERED=TRUE` |
| FLG-18 | Sunken City completion | Sunken City discovered | Open vault core; optionally beat boss | `SUNKEN_CITY_VAULT_OPENED=TRUE`, `SUNKEN_CITY_FLOODGATE_UNLOCKED=TRUE`; optional `SUNKEN_CITY_BOSS_DEFEATED=TRUE` |
| FLG-19 | Dragon's Graveyard unlock | `RELIC_MASS_SEATED=TRUE` | Attempt Dragon's Graveyard entry | Entry allowed and `DRAGONS_GRAVEYARD_DISCOVERED=TRUE` |
| FLG-20 | Dragon's Graveyard completion | Dragon's Graveyard discovered | Collect sigils and open vault; optionally beat boss | `DRAGONS_GRAVEYARD_VAULT_OPENED=TRUE`; optional `GRAVEWYRM_ECHO_DEFEATED=TRUE`, optional `FOSSIL_DRAKE_UNLOCKED=TRUE` |
| FLG-21 | Post-clear sanctum options | `FINAL_PALACE_F5_CLEARED=TRUE` | Re-enter post-clear sanctum | Confluence option requires `ECLIPSE_CONFLUENCE_DISCOVERED=TRUE`; unfinished seams bark depends on vault clear flags |
| FLG-22 | Palace pity counter | Palace combat enabled | Kill wisps/auditors without paradox drops | `PALACE_PARADOX_STREAK` increments, then guarantees paradox at threshold |

---

## 3) Traceability (Source References)

| Flag / Condition | Source Reference |
|------------------|------------------|
| `D1_CLEARED`, `RELIC_GROWTH_SEATED` | `chroma_edge_dungeon_d1_ruins_of_ashveil_map_sheet.md:300`, `chroma_edge_dungeon_d1_ruins_of_ashveil_map_sheet.md:302` |
| `D2_CLEARED`, `RELIC_MOTION_SEATED` | `chroma_edge_dungeon_d2_fungal_depths_map_sheet.md:311`, `chroma_edge_dungeon_d2_fungal_depths_map_sheet.md:313` |
| `D3_CLEARED`, `RELIC_LIGHT_SEATED` | `chroma_edge_dungeon_d3_crystal_caverns_map_sheet.md:337`, `chroma_edge_dungeon_d3_crystal_caverns_map_sheet.md:339` |
| `D4_CLEARED`, `RELIC_HEAT_SEATED` | `chroma_edge_dungeon_d4_skyspire_temple_map_sheet.md:327`, `chroma_edge_dungeon_d4_skyspire_temple_map_sheet.md:329` |
| `D5_CLEARED`, `RELIC_TIDE_SEATED`, `AQUATIC_TRAVEL_UNLOCKED` | `chroma_edge_dungeon_d5_abyssal_trench_map_sheet.md:340`, `chroma_edge_dungeon_d5_abyssal_trench_map_sheet.md:342`, `chroma_edge_dungeon_d5_abyssal_trench_map_sheet.md:343` |
| `D6_CLEARED`, `RELIC_MASS_SEATED` | `chroma_edge_dungeon_d6_obsidian_quarry_map_sheet.md:348`, `chroma_edge_dungeon_d6_obsidian_quarry_map_sheet.md:350` |
| `D7_CLEARED`, `RELIC_TIME_SEATED` | `chroma_edge_dungeon_d7_frozen_citadel_map_sheet.md:367`, `chroma_edge_dungeon_d7_frozen_citadel_map_sheet.md:369` |
| `D8_CLEARED`, `RELIC_SHADOW_SEATED` | `chroma_edge_dungeon_d8_void_nexus_map_sheet.md:368`, `chroma_edge_dungeon_d8_void_nexus_map_sheet.md:370` |
| `CROWN_ARCHIVE_KEY_ACQUIRED` | `chroma_edge_dungeon_archive_district_map_sheet.md:331` |
| `CONDUIT_AUTHORIZED`, `VOID_NEXUS_GATE_OPEN` | `chroma_edge_submap_crown_district_hub_map_sheet.md:283`, `chroma_edge_submap_crown_district_hub_map_sheet.md:284` |
| `FINAL_ACT_OPEN`, R17f gate conditions | `chroma_edge_route_micro_r17f_palace_entrance_micro.md:105` |
| `SPIRE_ACTUATOR_INSTALLED`, `SPIRE_CONDUIT_ROUTE_OPEN` | `chroma_edge_dungeon_palace_interior_map_sheet.md:307`, `chroma_edge_dungeon_palace_interior_map_sheet.md:308` |
| `ECLIPSE_CONFLUENCE_DISCOVERED` | `chroma_edge_overworld_eclipse_confluence_map_sheet.md:263` |
| Vault clear triplet + final eclipse gate | `chroma_edge_overworld_eclipse_confluence_map_sheet.md:266`, `chroma_edge_overworld_eclipse_confluence_map_sheet.md:267`, `chroma_edge_overworld_eclipse_confluence_map_sheet.md:268`, `chroma_edge_overworld_eclipse_confluence_map_sheet.md:269` |
| Sunken City flags | `chroma_edge_hidden_sunken_city_map_sheet.md:309`, `chroma_edge_hidden_sunken_city_map_sheet.md:310`, `chroma_edge_hidden_sunken_city_map_sheet.md:311`, `chroma_edge_hidden_sunken_city_map_sheet.md:312` |
| Dragon's Graveyard flags | `chroma_edge_hidden_dragons_graveyard_map_sheet.md:357`, `chroma_edge_hidden_dragons_graveyard_map_sheet.md:359`, `chroma_edge_hidden_dragons_graveyard_map_sheet.md:360`, `chroma_edge_hidden_dragons_graveyard_map_sheet.md:362` |
| Post-clear sanctum dependency flags | `chroma_edge_final_palace_post_clear_voice_ui_barks.md:120`, `chroma_edge_final_palace_post_clear_voice_ui_barks.md:122`, `chroma_edge_final_palace_post_clear_voice_ui_barks.md:124` |
| `PALACE_PARADOX_STREAK` | `chroma_edge_dungeon_palace_interior_drop_tables.md:129` |

---

## 4) Execution Log Template

| ID | Result (PASS/FAIL/BLOCKED) | Build/Branch | Notes | Defect ID |
|----|----------------------------|--------------|-------|-----------|
| FLG-01 |  |  |  |  |
| FLG-02 |  |  |  |  |
| FLG-03 |  |  |  |  |
| FLG-04 |  |  |  |  |
| FLG-05 |  |  |  |  |
| FLG-06 |  |  |  |  |
| FLG-07 |  |  |  |  |
| FLG-08 |  |  |  |  |
| FLG-09 |  |  |  |  |
| FLG-10 |  |  |  |  |
| FLG-11 |  |  |  |  |
| FLG-12 |  |  |  |  |
| FLG-13 |  |  |  |  |
| FLG-14 |  |  |  |  |
| FLG-15 |  |  |  |  |
| FLG-16 |  |  |  |  |
| FLG-17 |  |  |  |  |
| FLG-18 |  |  |  |  |
| FLG-19 |  |  |  |  |
| FLG-20 |  |  |  |  |
| FLG-21 |  |  |  |  |
| FLG-22 |  |  |  |  |
