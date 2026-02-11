# Chroma's Edge - Document Organization

## Overview

This document describes the complete folder structure for the Chroma's Edge RPG Maker MZ project documentation.

---

## 📁 Root-Level Organization

| Folder | Contents | File Count |
|--------|----------|------------|
| `docs/` | All documentation | 334+ files |
| `data/` | RPG Maker JSON databases | 113 files |
| `img/` | Runtime images | 4,501 files |
| `audio/` | Audio assets | 144 files |
| `js/` | JavaScript plugins | 27 files |
| `tools/` | Python helper scripts | 28 files |
| `assets/` | Source assets & data | 9,700+ files |
| `content/` | Dialog, quests, lore | 501 files |

---

## 📚 Documentation Structure (`docs/`)

### Core Files
| File | Purpose |
|------|---------|
| `README.md` | Documentation hub and navigation |
| `FOLDER_STRUCTURE.md` | This document - organization guide |

### Subfolders

#### `docs/assets/` - Asset Specifications (13 files)
Asset catalogs, specifications, and replacement guides.

| File | Description |
|------|-------------|
| ASSET_CATALOG.md | Complete asset inventory |
| ASSET_STATUS_DASHBOARD.md | Live completion tracker |
| TILESET_REPLACEMENT_GUIDE.md | Tileset extraction mapping |
| UI_ASSET_SPECS.md | UI element specifications |
| VFX_SPECIFICATIONS.md | Visual effects specs |
| ... | 8 additional asset files |

#### `docs/asset_reference/` - SNES Asset Guides (14 files)
Reference documentation for SNES asset extraction.

| File | Description |
|------|-------------|
| MASTER_ASSET_INDEX.md | Central asset hub |
| ZONE_ASSET_MAPPING.md | Zone-to-asset assignments |
| EXTRACTION_COORDINATES.md | Pixel coordinates for extraction |
| VISUAL_STYLE_GUIDE.md | Color/style adaptation rules |
| ... | 10 additional reference files |

#### `docs/characters/` - Character Design (5 files)
Character sprite and design documentation.

| File | Description |
|------|-------------|
| CHROMA_EDGE_SPRITE_LIST.md | Complete sprite manifest |
| PROTAGONIST_SHEET_ANALYSIS.md | Character sheet breakdowns |
| ... | 3 additional character files |

#### `docs/design/` - Game Design (14 files)
Core game design documents.

| File | Description |
|------|-------------|
| ITEM_COMPENDIUM.md | Complete item database |
| MONSTER_ECOLOGY_COMPENDIUM.md | Monster families & behaviors |
| WORLD_NPC_DISTRIBUTION.md | NPC placement strategy |
| ... | 11 additional design files |

#### `docs/guides/` - Production Guides (1 file)
How-to guides for working with the project.

| File | Description |
|------|-------------|
| PRODUCTION_GUIDE.md | Master production guide |

#### `docs/locations/` - Map Documentation (125 files)
**Complete map sheet organization:**

| Subfolder | Count | Contents |
|-----------|-------|----------|
| `dungeons/` | 22 | D1-D8, Archive District, Palace Interior, Remnant Vault |
| `towns/` | 23 | 13 towns + interior sheets |
| `routes/` | 24 | Micro routes R01-R17f, S01-S02 |
| `fields/` | 8 | Field route connectors |
| `overworld/` | 5 | World maps, eclipse state, endgame |
| `palace/` | 8 | Final Palace 5 floors + reward sanctum |
| `shrines/` | 8 | 8 Foundation shrines |
| `hidden/` | 3 | Dragon's Graveyard, Sunken City |
| `tower/` | 17 | Aurora Tower 100 floors |
| `zones/` | 2 | Zone micro maps |
| *(root)* | 5 | Location specs (tileset, visual map list, etc.) |

#### `docs/production/` - Production Tracking (1 file)

| File | Description |
|------|-------------|
| PROJECT_INDEX.md | Master project index |

#### `docs/project/` - Project Planning (6 files)
High-level project documentation.

| File | Description |
|------|-------------|
| ORION_GAME_BIBLE_PRE_SCRIPT_v1.md | Core game design bible |
| ORION_COMPLETION_MASTER_PLAN.md | Master completion roadmap |
| MISSING_ASSETS.md | Missing asset tracking |
| MISSING_ITEMS_PUNCHLIST.md | Production punchlist |
| ... | 2 additional project files |

#### `docs/reports/` - Audit Reports (117 files)
**Organized by type:**

| Subfolder | Count | Contents |
|-----------|-------|----------|
| `audits/` | 5 | Deep audit reports |
| `passes/` | 50 | Validation pass reports |
| `assets/` | 6 | Asset-specific reports |
| `data/` | 1 | Data integrity reports |
| `story/` | 2 | Story/dialog reports |
| `audio/` | 1 | Audio reports |
| *(root)* | 52 | Latest reports and summaries |

#### `docs/story/` - Story Scripts (14 files)
Full screenplay parts 1-14.

| File | Description |
|------|-------------|
| chroma_edge_script_part_01.md | Part 1: The Ironhawk Contract |
| chroma_edge_script_part_02.md | Part 2: The Ashveil Ruins |
| ... | Parts 3-13 |
| chroma_edge_script_part_14.md | Part 14: The Final Palace |

#### `docs/technical/` - Technical Documentation (24 files)
Engine specs and implementation details.

| File | Description |
|------|-------------|
| DESIGN_DOC_v2_13_party.md | Technical design document |
| ENGINE_RECOMMENDATION.md | Engine selection rationale |
| VFX_EFFECTS_INVENTORY.md | Effects catalog |
| CANONICAL_DATA_POLICY.md | Data policy specification |
| ... | 20 additional technical files |

---

## 📄 File Naming Conventions

### Map Sheets
```
chroma_edge_{type}_{name}_map_sheet.md
```

| Type Prefix | Description | Example |
|-------------|-------------|---------|
| `dungeon_` | Dungeon maps | `chroma_edge_dungeon_d1_ruins_of_ashveil_map_sheet.md` |
| `town_` | Town maps | `chroma_edge_town_dusthaven_map_sheet.md` |
| `route_micro_` | Route micro-maps | `chroma_edge_route_micro_r01_dustbelt_track.md` |
| `field_` | Field maps | `chroma_edge_field_dusthaven_outskirts_map_sheet.md` |
| `shrine_` | Shrine maps | `chroma_edge_shrine_pyreheart_reliquary_heat_map_sheet.md` |
| `tower_` | Tower maps | `chroma_edge_tower_aurora_lobby_map_sheet.md` |
| `final_palace_` | Palace maps | `chroma_edge_final_palace_floor_1_elemental_lords.md` |
| `hidden_` | Hidden areas | `chroma_edge_hidden_dragons_graveyard_map_sheet.md` |
| `overworld_` | World maps | `chroma_edge_overworld_orion_map_sheet.md` |
| `zone_` | Zone maps | `chroma_edge_zone_old_lumencrest_map_sheet.md` |
| `system_` | System docs | `chroma_edge_system_integrity_meter_widget_text_package.md` |

### Reports
```
{topic}_{type}_YYYY-MM-DD.md
```

| Type Suffix | Description | Example |
|-------------|-------------|---------|
| `_pass_` | Validation pass | `full_project_audit_2026-02-09.md` |
| `_audit_` | Deep audit | `sprite_slice_pad_audit_2026-02-08.md` |
| No suffix | General report | `missing_asset_descriptions_non_audio_2026-02-11.md` |

### Scripts
```
chroma_edge_script_part_{##}.md
```

Example: `chroma_edge_script_part_01.md` through `chroma_edge_script_part_14.md`

---

## 📊 Statistics Summary

| Category | Files | Description |
|----------|-------|-------------|
| Locations | 125 | Map sheets for all game areas |
| Reports | 117 | Audit and validation reports |
| Technical | 24 | Engine and implementation docs |
| Design | 14 | Game design documents |
| Assets | 27 | Asset specs and reference |
| Story | 14 | Script parts 1-14 |
| Characters | 5 | Character design docs |
| Project | 6 | Planning and master docs |
| Guides | 1 | Production guide |
| **TOTAL** | **334+** | **Complete documentation** |

---

## 🔧 Maintenance

### Validation Tools
Run these after documentation changes:

```bash
# Full project validation
python tools/run_project_audit_gate.py --scope all

# Image reference validation
python tools/validate_runtime_image_references.py

# World integrity check
python tools/validate_world_integrity.py
```

### Adding New Documentation

1. Choose appropriate folder based on content type
2. Follow naming conventions
3. Update relevant index files
4. Run validation tools
5. Commit with descriptive message

---

## 🗂️ Archive

Obsolete files are moved to `archive/` with cross-references to replacements:

| Old Location | New Location |
|--------------|--------------|
| `archive/CHARACTER_ROSTER_COMPLETE.md` | `characters/CHARACTER_ROSTER_COMPLETE_v2_13_party.md` |
| `archive/DESIGN_DOC.md` | `technical/DESIGN_DOC_v2_13_party.md` |

---

*Last Updated: 2026-02-11*
*Structure Version: 2.0 - Reorganized Documentation*
