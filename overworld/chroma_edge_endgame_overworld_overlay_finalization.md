# Chroma's Edge - Endgame Overworld Overlay Finalization (v1)
## Phase 1.1 Completion Layer (Post-R17)

---

## 0) Scope

This file is the implementation contract that closes the `Endgame Overlay Final` task in `ORION_COMPLETION_MASTER_PLAN.md`.

It finalizes:
- Visual overlay behavior (rift suppression + scar lines)
- Route/node unlock triggers
- Encounter table swap flags
- Aetherreach + Remnant Vault integration
- R17a-R17f endgame behavior

Related sheets:
- `chroma_edge_endgame_overworld_eclipse_state.md`
- `chroma_edge_overworld_eclipse_confluence_map_sheet.md`
- `chroma_edge_route_micro_r17a_old_lumencrest_to_grand_boulevard.md`
- `chroma_edge_route_micro_r17b_grand_boulevard_to_archive_entry.md`
- `chroma_edge_route_micro_r17c_archive_district_approach.md`
- `chroma_edge_route_micro_r17d_crown_district_approach.md`
- `chroma_edge_route_micro_r17e_crown_hub_connector.md`
- `chroma_edge_route_micro_r17f_palace_entrance_micro.md`

---

## 1) World State Machine (Authoritative)

| State | Activation | Deactivation | Priority |
|-------|------------|--------------|----------|
| `ACT2_RIFT_OVERLAY` | `D4_CLEARED = TRUE` | Never (superseded visually) | 1 |
| `ECLIPSE_OVERLAY_ACTIVE` | `D8_CLEARED = TRUE` and `RELIC_SHADOW_SEATED = TRUE` | `ECLIPSE_CONFLUENCE_STABILIZED = TRUE` | 2 |
| `RIFT_SUPPRESSION_ACTIVE` | `ECLIPSE_CONFLUENCE_STABILIZED = TRUE` | Never | 3 |

Resolution rules:
1. Highest active priority owns final visual package.
2. `RIFT_SUPPRESSION_ACTIVE` preserves scar lines as non-hazard visual memory.
3. Route locks still obey story flags even when overlay state changes.

---

## 2) Visual Overlay Final Package

### A) Overlay Layers

| Layer | `ACT2_RIFT_OVERLAY` | `ECLIPSE_OVERLAY_ACTIVE` | `RIFT_SUPPRESSION_ACTIVE` |
|------|----------------------|--------------------------|---------------------------|
| Rift tears | On (high) | Replaced by seam scars | Off |
| Scar lines | Off | On (high contrast) | On (faint) |
| Fog density | Medium | High | Low |
| Wrong-sky reflections | Low | High | Medium |
| Shock pulse VFX | On near rifts | On near seams | Off |

### B) Region Intensity Scalars

| Region | Scalar | Notes |
|--------|--------|-------|
| Early towns/routes | 0.35 | Cosmetic only, no punitive hazards |
| Mid routes | 0.65 | Clear readability preserved |
| Capital chain (R16-R17) | 1.00 | Full overlay package |
| Eclipse Confluence | 1.20 | Unique knot visuals |

---

## 3) Route + Node Unlock Trigger Matrix

### A) Capital Spine (R17)

| Segment | Unlock Flag(s) | Additional Gate(s) | Endgame Overlay Behavior |
|---------|----------------|--------------------|--------------------------|
| `R17a` | `R16_COMPLETE = TRUE` | None | Scar lines + elite chance bump in Eclipse |
| `R17b` | `CROWN_CHAIN_STARTED = TRUE` | `ARCHIVE_DISTRICT_ACCESS_GRANTED = TRUE` for forward gate | Redaction haze replaced by seam haze |
| `R17c` | `ARCHIVE_DISTRICT_ACCESS_GRANTED = TRUE` | None | Ink trenches gain seam edge VFX |
| `R17d` | Route available in Act 2 | `CROWN_ARCHIVE_KEY_ACQUIRED = TRUE` to enter Crown hub | Watchlights retinted to eclipse palette |
| `R17e` | Entered from `R17d` | `CROWN_ARCHIVE_KEY_ACQUIRED = TRUE` for Conduit path | Non-combat atmospheric overlay only |
| `R17f` | `D8_CLEARED = TRUE` and `RELIC_SHADOW_SEATED = TRUE` | `FINAL_ACT_OPEN = TRUE` for Palace gate | Synchrony pulse visuals intensified |

### B) Endgame Nodes

| Node | Unlock Flag(s) | Notes |
|------|----------------|-------|
| Eclipse Confluence | `SHADOWWALK_UNLOCKED = TRUE` and first seam traversal | Sets `ECLIPSE_CONFLUENCE_DISCOVERED = TRUE` |
| Confluence Seam Router | First terminal use | Sets `SEAM_ROUTER_UNLOCKED = TRUE` |
| Aetherreach Route | `FINAL_PALACE_CLEARED = TRUE` and `PROGENITOR_ENGINE_DEFEATED = TRUE` and `ECLIPSE_CONFLUENCE_STABILIZED = TRUE` | Sets `AETHERREACH_ROUTE_OPEN = TRUE` |
| Remnant Vault | `AETHERREACH_ROUTE_OPEN = TRUE` | Sets `REMNANT_VAULT_UNLOCKED = TRUE` on first board interaction |

---

## 4) Encounter Table Swap Flags

### A) Global Switches

| Flag | Function |
|------|----------|
| `ECLIPSE_ROUTE_TABLES_ACTIVE` | Enables eclipse route tables where defined |
| `RIFT_SUPPRESSED_TABLES_ACTIVE` | Uses stabilized post-eclipse tables |

Activation:
- `ECLIPSE_ROUTE_TABLES_ACTIVE = TRUE` when `ECLIPSE_OVERLAY_ACTIVE = TRUE`
- `RIFT_SUPPRESSED_TABLES_ACTIVE = TRUE` when `RIFT_SUPPRESSION_ACTIVE = TRUE`

### B) Route Table Mapping

| Route/Map | Base Table | Eclipse Table | Stabilized Table |
|-----------|------------|---------------|------------------|
| `R05` | `EN_R05_BASE` | `EN_R05_ECLIPSE` | `EN_R05_STABLE` |
| `R07` | `EN_R07_BASE` | `EN_R07_ECLIPSE` | `EN_R07_STABLE` |
| `R09` | `EN_R09_BASE` | `EN_R09_ECLIPSE` | `EN_R09_STABLE` |
| `R12` | `EN_R12_BASE` | `EN_R12_ECLIPSE` | `EN_R12_STABLE` |
| `R16` | `EN_R16_BASE` | `EN_R16_ECLIPSE` | `EN_R16_STABLE` |
| `R17a` | `EN_R17A_BASE` | `EN_R17A_ECLIPSE` | `EN_R17A_STABLE` |
| `R17b` | `EN_R17B_BASE` | `EN_R17B_ECLIPSE` | `EN_R17B_STABLE` |
| `R17c` | `EN_R17C_BASE` | `EN_R17C_ECLIPSE` | `EN_R17C_STABLE` |
| `R17d` | `EN_R17D_BASE` | `EN_R17D_ECLIPSE` | `EN_R17D_STABLE` |
| `Eclipse Confluence Rim` | `EN_CONF_RIM_BASE` | `EN_CONF_RIM_ECLIPSE` | `EN_CONF_RIM_STABLE` |

Notes:
- `R17e` remains non-combat.
- `R17f` uses scripted checks; random encounter table swap is not required.

---

## 5) Aetherreach + Remnant Vault Integration

### A) Route Activation Flow

1. Player clears Final Palace and defeats Progenitor Engine.
2. Confluence stabilization event sets `ECLIPSE_CONFLUENCE_STABILIZED = TRUE`.
3. Chronowake and Confluence terminals expose `ASCEND: AETHERREACH`.
4. First arrival to Aetherreach sets `AETHERREACH_ROUTE_OPEN = TRUE`.
5. Aetherreach Notice Board exposes Remnant Vault warp and sets `REMNANT_VAULT_UNLOCKED = TRUE`.

### B) UI/Prompt Package

| Location | Prompt |
|----------|--------|
| Chronowake Terminal | `AETHERLIFT VECTOR AVAILABLE` |
| Confluence Terminal | `SKYBOUND ROUTE STABILIZED` |
| Aetherreach Board | `REMNANT VAULT: ACTIVE BREACH` |

### C) Failure-safe Backfills (Existing Saves)

On load, if:
- `FINAL_PALACE_CLEARED = TRUE`
- `PROGENITOR_ENGINE_DEFEATED = TRUE`
- `ECLIPSE_CONFLUENCE_STABILIZED = TRUE`
- `AETHERREACH_ROUTE_OPEN = FALSE`

Then auto-set:
- `AETHERREACH_ROUTE_OPEN = TRUE`

If additionally `AETHERREACH_ROUTE_OPEN = TRUE` and `REMNANT_VAULT_UNLOCKED = FALSE`,
show board tutorial ping and unlock on first interaction.

---

## 6) QA Checklist (Ship Blockers)

- [x] Verify `ACT2_RIFT_OVERLAY` -> `ECLIPSE_OVERLAY_ACTIVE` transition on existing saves
- [x] Verify `ECLIPSE_OVERLAY_ACTIVE` -> `RIFT_SUPPRESSION_ACTIVE` transition after stabilization event
- [x] Verify `R17a-R17f` gates match this matrix and current route sheets
- [x] Verify `R17e` remains non-combat in all overlay states
- [x] Verify table swaps occur only where mappings exist
- [x] Verify Aetherreach route appears from both Chronowake and Confluence
- [x] Verify Remnant Vault unlock path from Aetherreach board
- [x] Verify no softlock when loading post-palace saves from older builds

---

## 7) Completion Note

This file closes the `Endgame Overlay Final` requirement from Phase 1.1 and is intended to be the single reference for implementation flags and integration behavior.
