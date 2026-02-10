# Orion (Chroma's Edge) - Master Completion Plan

**Document Version:** 1.1  
**Last Updated:** Current Session  
**Status:** Doc-layer execution complete; integration preflight complete; pending in-engine execution

---

## CURRENT STATE SUMMARY

### COMPLETED

| Category | Items Done |
|----------|------------|
| Shrines | 8 shrine map sheets complete |
| Overworld | Orion overworld master sheet + endgame overlay implementation references |
| Route Micro-Maps | R01-R17 complete (including R17a-R17f capital spine) |
| Systems | Stabilization field and Integrity package complete |
| Town Packages | 12/12 town or hub packages complete with interiors |
| Mainline Dungeon Docs | D1-D8 complete plus Archive District and Palace Interior |
| Endgame Hub Docs | Eclipse Confluence map sheet complete |
| Tower Verification | Tower package verified (lobby, floors, boss arenas, captain floors, reward/UI) |
| Final Palace Verification | F1-F5, reward sanctum, and post-clear voice/UI verified |
| Hidden Areas | Sunken City and Dragon's Graveyard complete |
| Consistency Sweep | D1/D2/D4/D6 terminology drift resolved in route-facing docs |
| Integration QA Scaffolding | Flag validation matrix and implementation parity runbook created |
| QA Automation Helper | Palace drop-table primary sum sanity script created and validated |
| Integration Preflight | Traceability, pacing/chest, and drop-sum static checks passed |

### COMPLETION METRICS

- Shrines: 8/8 (100%)
- Routes: 17/17 (100%)
- Towns/Hubs: 12/12 (100%)
- Dungeons and Endgame Hubs: 11/11 docs verified (`D1-D8`, `Archive`, `Palace Interior`, `Eclipse Confluence`)
- Hidden Areas: 2/2 (100%)
- Tower package: VERIFIED
- Final Palace package: VERIFIED
- Global consistency sweep: COMPLETE

---

## PHASE 1: CLOSE THE NAVIGATION LOOP (COMPLETE)

**Goal:** Make the game traversable from start to finish.

### 1.1 Overworld Completion

| Item | Status | Notes |
|------|--------|-------|
| R17 Capital Spine Pack | DONE | All 6 R17 micro segments complete |
| Endgame Overlay Final | DONE | Visual and unlock trigger implementation doc complete |

### 1.2 Core Town Sheets (Act 1-2 Hubs)

| Town | Status |
|------|--------|
| Dusthaven | DONE |
| Ashveil Sanctuary | DONE |
| Mirewatch | DONE |
| Prismridge | DONE |
| Cinderstep | DONE |
| Brinegate Port | DONE |

### 1.3 Northern, Junction, and Capital Town Sheets

| Town/Hub | Status |
|----------|--------|
| Gravemark Outpost | DONE |
| Rimehold | DONE |
| Chronowake Pier | DONE |
| Meridian Junction | DONE |
| Old Lumencrest Outer Wards | DONE |
| Crown District | DONE |

### 1.4 Interiors

All town/hub interior packages are complete and linked to their town docs.

**Phase 1 Deliverable:** Complete traversable route and town topology from early game through capital chain.

---

## PHASE 2: MAINLINE DUNGEONS (COMPLETE)

**Goal:** Buildable progression path from D1 through Palace.

### 2.1 Dungeon Coverage

| Dungeon / Hub | Status | Verification |
|---------------|--------|--------------|
| D1 Ruins of Ashveil | VERIFIED | Present and mapped |
| D2 Fungal Depths | VERIFIED | Present and mapped |
| D3 Crystal Caverns | VERIFIED | Present and mapped |
| D4 Skyspire Temple | VERIFIED | Present and mapped |
| D5 Abyssal Trench | VERIFIED | Present and mapped |
| D6 Obsidian Quarry | VERIFIED | Present and mapped |
| D7 Frozen Citadel | VERIFIED | Present and mapped |
| D8 Void Nexus | VERIFIED | Present and mapped |
| Archive District | VERIFIED | Present and mapped |
| Palace Interior | VERIFIED | Present and mapped |
| Eclipse Confluence | VERIFIED | Present and mapped |

### 2.2 Progression Wiring

Verified key handoff flags across archive, capital, and final approach:
- `CROWN_ARCHIVE_KEY_ACQUIRED`
- `CONDUIT_AUTHORIZED`
- `VOID_NEXUS_GATE_OPEN`
- `D8_CLEARED`
- `RELIC_SHADOW_SEATED`
- `FINAL_ACT_OPEN`

**Phase 2 Deliverable:** Full documented dungeon progression from D1 through palace/endgame routing.

---

## PHASE 3: TUNING + ENDGAME (COMPLETE)

**Goal:** Close tuning and endgame documentation passes.

### 3.1 Palace Interior Tuning

| Pass | Status | Evidence |
|------|--------|----------|
| Encounter pacing | DONE | `chroma_edge_dungeon_palace_interior_balance_pacing.md` |
| Chest placement | DONE | `chroma_edge_dungeon_palace_interior_balance_pacing.md` |
| Drop tables | DONE | `chroma_edge_dungeon_palace_interior_drop_tables.md` |

### 3.2 Tower and Palace Verification

| Component | Status |
|-----------|--------|
| Tower package | VERIFIED |
| Final Palace package | VERIFIED |
| Post-clear tower/palace voice UI | VERIFIED |

### 3.3 Hidden Areas

| Area | Status | Evidence |
|------|--------|----------|
| Sunken City | DONE | `chroma_edge_hidden_sunken_city_map_sheet.md` |
| Dragon's Graveyard | DONE | `chroma_edge_hidden_dragons_graveyard_map_sheet.md` |

### 3.4 Final Consistency Sweep

Status: DONE  
Evidence: `chroma_edge_global_consistency_sweep_notes.md`

**Phase 3 Deliverable:** Complete endgame and hidden-area documentation set with normalized terminology.

---

## MASTER CHECKLIST

### A) Overworld

- [x] R17 Capital Spine pack (6 micro segments)
- [x] Endgame overlay finalization

### B) Towns (12 Total)

- [x] Dusthaven (town + interiors)
- [x] Ashveil Sanctuary (town + interiors)
- [x] Mirewatch (town + interiors)
- [x] Prismridge (town + interiors)
- [x] Cinderstep (town + interiors)
- [x] Brinegate Port (town + interiors)
- [x] Gravemark Outpost (town + interiors)
- [x] Rimehold (town + interiors)
- [x] Chronowake Pier (town + interiors)
- [x] Meridian Junction (town + interiors)
- [x] Old Lumencrest Outer Wards (hub + interiors)
- [x] Crown District (hub + interiors)

### C) Dungeons and Endgame Hubs (11 Total)

- [x] D1 Ruins of Ashveil
- [x] D2 Fungal Depths
- [x] D3 Crystal Caverns
- [x] D4 Skyspire Temple
- [x] D5 Abyssal Trench
- [x] D6 Obsidian Quarry
- [x] D7 Frozen Citadel
- [x] D8 Void Nexus
- [x] Archive District
- [x] Palace Interior (5 floors)
- [x] Eclipse Confluence

### D) Hidden Areas

- [x] Sunken City
- [x] Dragon's Graveyard

### E) Tower (Verification)

- [x] Verify all boss arenas present (10/25/50/75/90/100)
- [x] Verify captain floors (15/35/55/65/85/95)
- [x] Verify reward sanctum UI and post-clear lines

### F) Final Palace (Verification)

- [x] Verify F1-F5 boss sheets complete
- [x] Verify post-clear reward sanctum
- [x] Verify post-clear voice and route barks

---

## EVIDENCE INDEX

- Dungeon chain verification: `chroma_edge_dungeon_chain_verification_notes.md`
- Tower and palace verification: `chroma_edge_tower_final_palace_verification_notes.md`
- Hidden area completion: `chroma_edge_hidden_areas_completion_notes.md`
- Global consistency sweep: `chroma_edge_global_consistency_sweep_notes.md`
- Integration flag matrix: `chroma_edge_integration_flag_validation_matrix.md`
- Implementation parity runbook: `chroma_edge_implementation_parity_qa_runbook.md`
- Drop-table sum checker: `check_palace_drop_table_sums.ps1`
- Flag traceability checker: `check_integration_flag_traceability.ps1`
- Pacing/chest checker: `check_palace_pacing_integrity.ps1`
- Preflight results: `chroma_edge_integration_preflight_results.md`
- Runtime execution log: `chroma_edge_integration_execution_log.md`

---

## NEXT IMMEDIATE ACTIONS

1. Execute FLG-01 through FLG-22 in-engine using `chroma_edge_integration_flag_validation_matrix.md`.
2. Execute runtime parity groups using `chroma_edge_implementation_parity_qa_runbook.md`.
3. Lock this plan at v1.1 after user signoff.

---

**Plan Author:** Assistant  
**Review Status:** Pending user confirmation
