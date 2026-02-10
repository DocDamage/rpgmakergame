# Non-Audio Content Lock Report (2026-02-09)

## Status
- non_audio_content_lock: **PASS**
- issues_critical: **0**
- issues_high: **0**
- issues_medium: **0**
- issues_info: **0**
- total_issues: **0**

## Cohesion Metrics
- checklist_checked: **102**
- checklist_unchecked: **190**
- checklist_completion: **34.9%**
- json_files_parsed: **652**
- json_parse_errors: **0**
- dialog_trees_validated: **38**
- dialog_graph_errors: **0**
- npc_records: **144**
- map_records: **85**
- encounter_tables: **12**
- enemy_ids: **32**
- boss_ids: **35**
- reference_errors: **0**
- sprite_reference_errors: **0**
- sprites_requiring_resize: **0**

## Sprite Folder + Sizing Audit
- npc_sprite_ids_used: **10** (all mapped and present)
- enemy_sprite_refs: **32**; production_files: **32**; missing: **0**
- boss_sprite_refs: **34**; production_files: **34**; missing: **0**
- resize_candidates: none (all production enemy/boss sprites are 16px-multiple dimensions).

## This Pass Fixes
- Repaired 28 malformed JSON files in `content/quests` + `content/dialog` (broken quotes, line breaks inside strings, malformed keys, extra brace).
- Revalidated full repo JSON parse and all core non-audio reference links.

## Remaining Blockers
- none for non-audio content lock.
- audio mastering/replacement remains intentionally out of scope for this pass.

## Artifacts
- detail_csv: `docs/reports/non_audio_content_lock_pass_2026-02-09.csv`
- naming_validation: `python tools/validate_naming.py assets --validate-ids` (Invalid: 0)
