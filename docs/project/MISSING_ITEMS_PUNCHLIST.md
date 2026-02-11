# Chroma's Edge - Missing Items Punchlist
## Prioritized Gap List After Full Repo Audit

---

## Current Data/Asset Cohesion Status (2026-02-09)

- [x] Structural data integrity audit is clean (`0` open integrity issues).
- [x] Latest non-audio completion audit is clean (`0` issues): `docs/reports/full_project_audit_2026-02-09_non_audio_completion.md`.
- [x] Latest deep audit is clean (`0` issues): `docs/reports/full_project_audit_2026-02-09_deep_pass_4.md`.
- [x] Latest super-deep audit is clean (`0` issues): `docs/reports/full_project_audit_2026-02-09_super_deep_pass_6.md`.
- [x] Non-audio content lock pass is clean (`0` issues): `docs/reports/non_audio_content_lock_pass_2026-02-09.md`.
- [x] Full-repo JSON parse sweep is clean (`721/721` valid JSON files after latest world/encounter passes).
- [x] Repaired malformed content JSON set (`28` files in `content/dialog` + `content/quests`).
- [x] Story/dialog/location final deep pass completed (`0` structural quest/location/dialog graph errors): `docs/reports/story_dialog_location_final_deep_check_2026-02-09.md`.
- [x] Added explicit story setpiece location coverage (`12` new map records) in `assets/data/maps/map_story_setpieces.json`.
- [x] Anchored all main-story stage beats to map IDs (`85/85` stages with valid `target_location_id`).
- [x] Registered cinematic story-NPC dialog aliases (`59` aliases) in `content/dialog/story_npc_alias_registry.json`.
- [x] Missing item IDs were resolved with authored baseline records.
- [x] Missing quest IDs were resolved with authored baseline quest entries.
- [x] Missing map IDs were resolved with connected route/submap definitions.
- [x] Missing NPC references were resolved with authored baseline NPC records.
- [x] Missing item icon assets were resolved (`assets/sprites/ui` now populated).
- [x] UI icons were remapped from production icon sheets (`docs/reports/ui_icon_remap_2026-02-09.csv`).
- [x] Missing audio references were resolved with temporary in-place placeholder files.
- [x] Temporary audio token coverage is complete (`141/141` referenced tokens present; `77` generated from silence source).
- [x] Generated item economy/stats were tuned to match project rarity and equipment curves.
- [x] Generated quest text/progression was polished with act tags and tuned reward pacing.
- [x] NPC portrait assets and baseline dialog-tree coverage were generated for all current NPC records.
- [x] Residual placeholder dialog token removed (fallback dialog IDs normalized).
- [x] Main-quest map-hop connectivity is fully wired (`0` missing stage-to-stage links).
- [x] Encounter table coverage is synchronized (`0` map/table coverage mismatches).
- [x] Automated world-integrity validator added (`tools/validate_world_integrity.py`).

### Remaining Before Final Content Lock

- [ ] Replace temporary silent audio placeholders with final mastered BGM/SFX/VO.
  Queue available at `docs/reports/audio_replacement_queue_2026-02-09.csv`.
- [x] Replace generated UI icon placeholders with project icon-sheet art (`docs/reports/ui_icon_remap_2026-02-09.csv`).
- [x] Final narrative pass on newly added quest text/reward tuning.
- [x] Final combat economy pass on generated item values and rarity curves.
- [x] Add baseline NPC portrait assets and dialog-tree coverage for all NPC records.

---

## Must-Do (Blockers for Completion Signoff)

- [x] Execute runtime integration flag validation (`22` cases: `FLG-01` to `FLG-22`) and record outcomes in `chroma_edge_integration_execution_log.md:24`.
- [x] Execute runtime parity groups (`8` groups) and record outcomes in `chroma_edge_integration_execution_log.md:55`.
- [x] Close palace drop-table implementation checklist (`11` unchecked items) in `chroma_edge_dungeon_palace_interior_drop_tables.md:173`.
- [x] Close endgame overlay verification checklist (`8` unchecked items) in `chroma_edge_endgame_overworld_overlay_finalization.md:161`.
- [x] Resolve explicit TBD for shrine gate mapping in `chroma_edge_shrine_verdant_covenant_growth_map_sheet.md:320`.

---

## Should-Do (High-Value Implementation Follow-Through)

- [x] Close tower master implementation checklist (`13` items) in `chroma_edge_tower_aurora_ascension_master_sheet.md:393`. (Leaderboards remains optional)
- [x] Close system implementation checklists (`37` items total):
  - `chroma_edge_system_core_unravel_audio_timeline_implementation.md:211` (`8`)
  - `chroma_edge_system_integrity_meter_widget_text_package.md:245` (`11`)
  - `chroma_edge_system_integrity_stabilizer_state_machine_table.md:168` (`11`)
  - `chroma_edge_system_stabilization_field_hud_text_package.md:323` (`7`)

---

## Backlog / Legacy (Now Complete)

- [x] Legacy mega-design checklist (`83` items) in `DESIGN_DOC_v2_13_party.md:2524`.
- [x] Summon rename follow-through checklist (`5` items) in `SUMMON_RENAME_MASTER.md:112`.

---

## Notes

- Core content manifests are present (routes, towns/interiors, shrines, dungeons, tower, palace, hidden areas).
- Markdown file references are not broken.
- Remaining blocker tracked in this punchlist is final audio asset replacement.
