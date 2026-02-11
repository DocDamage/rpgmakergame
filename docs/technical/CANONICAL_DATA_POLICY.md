# Canonical Data Policy

## Canonical Runtime Layer

Use `assets/data/*` as the runtime source of truth for:
- maps and world graph
- quest IDs and progression
- NPC IDs
- item/enemy/boss IDs
- encounter references

## Authoring Layer

Use `content/*` as narrative authoring content (screenplay/dialog flavor) unless and until exported into canonical IDs.

## Integration Rule

Before implementation/testing signoff:
1. IDs referenced by playable quest/map flows must resolve in `assets/data/*`.
2. Any new authoring file in `content/*` that introduces IDs must be mapped or exported to canonical IDs.
3. Quest references must be explicit:
   - `prerequisites`/`unlocks` contain quest IDs only.
   - Non-quest gates use `prerequisite_flags`/`unlock_flags`.
4. Validation gates:
   - `python3 tools/validate_world_integrity.py`
   - `python3 tools/validate_content_integrity.py --scope core --strict-map-npc-anchors`
   - `python3 tools/audit_environment_sprite_coverage.py --strict-candidates`
   - `python3 tools/audit_story_cohesion.py --scope core`
5. Cohesion repair utility (when audit flags map NPC anchor drift):
   - `python3 tools/sync_map_npc_anchors_from_quests.py --scope all`
6. One-command gate runner:
   - `PATH="$HOME/.local/bin:$PATH" python3 tools/run_project_audit_gate.py --scope core`

## Runtime Map Bridge

- Canonical map metadata (`assets/data/maps/*.json`) is exported to RPG Maker runtime map stubs via:
  - `python3 tools/export_canonical_maps_to_rmmz.py`
- Export behavior includes:
  - canonical `connections` -> runtime transfer events
  - canonical `points_of_interest` -> runtime transfer events when target map exists
  - metadata-driven world dressing marker events (`landmarks`, `hazards`, `interiors`, `ambient_npcs`, `regions`, `puzzles`)
  - metadata-driven tile-layer geometry painting (paths, region texture patterns, anchor clusters) into runtime map `data` layers
  - map-type motif presets (`chromaMotifProfile`) for cohesive visual language across overworld/town/route/dungeon/tower/shrine categories
  - deterministic collision-safe placement and note tags for bridge/dressing auditing
- Bridge artifact:
  - `assets/data/system/runtime_map_bridge_generated.json`
- Bridge validation:
  - `python3 tools/validate_runtime_map_bridge.py`
  - includes runtime geometry consistency checks (`chromaPaintedTiles` vs non-zero z1/z2/z3 cells)
  - includes motif tag coverage checks (`chromaMotifProfile`)

## Runtime Quest Scope

- Curated runtime scope is `core` quest packs:
  - `quest_main_story.json`
  - `quest_side_stories.json`
  - `quest_generated_placeholders.json`
- Generated normalized content packs (`quest_content_main_normalized.json`, `quest_content_mini_normalized.json`) are opt-in via `ChromaEdge_QuestSystem` plugin parameter `includeContentPacks=true`.
- Reason: keep playable story/side-story progression cohesive by default while preserving expanded generated content for staged curation.

## Current Status

Stabilization pass notes: `docs/reports/cohesion_stabilization_pass_2026-02-10.md`.
Normalization pass notes: `docs/reports/content_id_normalization_pass_2026-02-10.md`.
