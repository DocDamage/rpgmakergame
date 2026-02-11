# Chroma's Edge - Documentation Hub

Complete documentation for the Chroma's Edge RPG Maker MZ project.

---

## 📁 Documentation Structure

```
docs/
├── README.md                          # This file
├── FOLDER_STRUCTURE.md                # Complete folder organization guide
├── assets/                            # Asset specifications & catalogs
│   ├── ASSET_CATALOG.md
│   ├── TILESET_REPLACEMENT_GUIDE.md
│   ├── UI_ASSET_SPECS.md
│   └── ... (13 files)
├── asset_reference/                   # SNES asset extraction guides
│   ├── MASTER_ASSET_INDEX.md
│   ├── ZONE_ASSET_MAPPING.md
│   ├── EXTRACTION_COORDINATES.md
│   └── ... (14 files)
├── characters/                        # Character design & sprites
│   ├── CHROMA_EDGE_SPRITE_LIST.md
│   ├── PROTAGONIST_SHEET_ANALYSIS.md
│   └── ... (5 files)
├── design/                            # Game design documents
│   ├── ITEM_COMPENDIUM.md
│   ├── MONSTER_ECOLOGY_COMPENDIUM.md
│   └── ... (14 files)
├── guides/                            # Production guides
│   └── PRODUCTION_GUIDE.md
├── locations/                         # Map documentation (125 files)
│   ├── dungeons/                      # D1-D8, Archive, Palace, Remnant (22)
│   ├── fields/                        # Field routes (8)
│   ├── hidden/                        # Secret areas (3)
│   ├── overworld/                     # World maps (5)
│   ├── palace/                        # Final Palace (8)
│   ├── routes/                        # Micro routes R01-R17f (24)
│   ├── shrines/                       # 8 Foundation shrines (8)
│   ├── tower/                         # Aurora Tower (17)
│   ├── towns/                         # 13 towns + interiors (23)
│   └── zones/                         # Zone maps (2)
│   └── [root level]                   # Location specs (5)
├── production/                        # Production tracking
│   └── PROJECT_INDEX.md
├── project/                           # Project planning & master docs
│   ├── ORION_GAME_BIBLE_PRE_SCRIPT_v1.md
│   ├── ORION_COMPLETION_MASTER_PLAN.md
│   └── ... (6 files)
├── reports/                           # Audit & validation reports (117)
│   ├── assets/                        # Asset reports (6)
│   ├── audits/                        # Deep audit passes (5)
│   ├── audio/                         # Audio reports (1)
│   ├── data/                          # Data integrity (1)
│   ├── passes/                        # Validation passes (50)
│   └── story/                         # Story/dialog reports (2)
│   └── [root level]                   # Latest summaries
├── story/                             # Story scripts (14 parts)
│   └── chroma_edge_script_part_01.md through part_14.md
└── technical/                         # Technical documentation
    ├── ENGINE_RECOMMENDATION.md
    ├── DESIGN_DOC_v2_13_party.md
    └── ... (24 files)
```

---

## 🚀 Quick Navigation

### For Developers
- [Technical Documentation](technical/) - Engine specs, implementation
- [Asset Reference](asset_reference/) - SNES asset extraction guides
- [Reports](reports/) - Audit results and validation passes

### For Designers
- [Game Design](design/) - Monster ecology, items, NPCs
- [Locations](locations/) - Map sheets for all areas
- [Story](story/) - Full screenplay parts 1-14

### For Artists
- [Asset Specifications](assets/) - Tilesets, UI, VFX specs
- [Characters](characters/) - Sprite lists, sheet analysis
- [Asset Reference](asset_reference/) - Extraction coordinates

### For Producers
- [Project Planning](project/) - Game bible, master plans
- [Production](production/) - Project tracking
- [Guides](guides/) - Production guide

---

## 📊 Documentation Stats

| Category | Files | Description |
|----------|-------|-------------|
| **Locations** | 125 | Map sheets for all game areas |
| **Reports** | 117 | Audit and validation reports |
| **Technical** | 24 | Engine and implementation docs |
| **Design** | 14 | Game design documents |
| **Assets** | 27 | Asset specs and reference |
| **Story** | 14 | Script parts 1-14 |
| **Characters** | 5 | Character design docs |
| **Project** | 6 | Planning and master docs |
| **Guides/Production** | 2 | Production guides |
| **TOTAL** | **334+** | **Complete documentation** |

---

## 🔍 Key Documents

### Getting Started
1. [ORION_GAME_BIBLE_PRE_SCRIPT_v1.md](project/ORION_GAME_BIBLE_PRE_SCRIPT_v1.md) - Core game design
2. [FOLDER_STRUCTURE.md](FOLDER_STRUCTURE.md) - Complete organization
3. [PRODUCTION_GUIDE.md](guides/PRODUCTION_GUIDE.md) - How to work with this project

### Current Status
- [FULL_DEEP_AUDIT_NON_AUDIO_2026-02-11.md](reports/FULL_DEEP_AUDIT_NON_AUDIO_2026-02-11.md) - Latest full audit
- [ASSET_STATUS_DASHBOARD.md](assets/ASSET_STATUS_DASHBOARD.md) - Asset completion tracker

### Latest Reports
- All [pass reports](reports/passes/) - Validation results
- All [audit reports](reports/audits/) - Deep analysis

---

## 📝 Naming Conventions

### Map Sheets
- `chroma_edge_dungeon_*.md` - Dungeon content
- `chroma_edge_town_*.md` - Town content
- `chroma_edge_route_micro_*.md` - Route content
- `chroma_edge_field_*.md` - Field content
- `chroma_edge_shrine_*.md` - Shrine content
- `chroma_edge_tower_*.md` - Tower content
- `chroma_edge_final_palace_*.md` - Palace content
- `chroma_edge_hidden_*.md` - Hidden areas
- `chroma_edge_overworld_*.md` - Overworld maps
- `chroma_edge_zone_*.md` - Zone maps

### Reports
- `*_pass_YYYY-MM-DD.md` - Validation passes
- `*_audit_YYYY-MM-DD.md` - Audit reports
- `*_YYYY-MM-DD.md` - Dated reports

### Scripts
- `chroma_edge_script_part_##.md` - Story parts 01-14

---

## ✅ Documentation Maintenance

All documentation is validated through:
- `tools/run_project_audit_gate.py` - Full project validation
- `tools/validate_runtime_image_references.py` - Image checks
- `tools/validate_world_integrity.py` - Map connectivity

Run these tools after any documentation changes to ensure consistency.

---

*Last Updated: 2026-02-11*
*Documentation Version: 2.0 - Reorganized*
