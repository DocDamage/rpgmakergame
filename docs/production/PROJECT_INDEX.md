# Chroma's Edge - Complete Project Index

## Quick Navigation

### Core Documentation
| File | Purpose |
|------|---------|
| `DESIGN_DOC_v2_13_party.md` | Master design document |
| `ORION_COMPLETION_MASTER_PLAN.md` | Completion roadmap |
| `ORION_GAME_BIBLE_PRE_SCRIPT_v1.md` | Pre-script bible |
| `MISSING_ITEMS_PUNCHLIST.md` | Task tracking (COMPLETE) |
| `FOLDER_STRUCTURE.md` | Organization guide |
| `PROJECT_INDEX.md` | This file |

---

## Content Folders

### `/archive/` - Legacy Files
- Superseded versions of design docs

### `/audio/` - Voice & Audio
- Character voice lines (15 characters)
- Voice sheets and blocks
- Audio implementation docs

### `/characters/` - Party & NPCs
- Character roster (all 13 party members)
- Summon rename master list
- Summon unlocks
- Mount/pet integration

### `/content/` - Narrative & Text (NEW)
| File | Size | Contents |
|------|------|----------|
| `content/content_msq_full_screenplay.md` | 22 KB | Main story (95 scenes, 158 flags) |
| `content/content_quest_journal.md` | 23 KB | Quest system, objectives, markers |
| `content/content_sidequests_town_life.md` | 16 KB | Sidequests, NPC barks, reactive dialogue |
| `content/content_party_banter.md` | 12 KB | Travel banter, camp scenes |
| `content/content_combat_text_vo.md` | 11 KB | Battle lines, boss callouts |
| `content/content_skills_statuses_tooltips.md` | 16 KB | Abilities, statuses, tooltips |
| `content/content_itemization_pack.md` | 14 KB | Items, gear, recipes |
| `content/content_world_lore.md` | 26 KB | Codex, plaques, terminals |
| `content/content_economy_tables.md` | 11 KB | Shops, drops, crafting costs |
| `content/content_ui_microcopy.md` | 43 KB | Errors, confirmations, tutorials |

### `/docs/` - Design Documents
- Alignment verification
- Consistency sweep notes
- Location bible
- Master plans

### `/dungeons/` - Dungeon Maps (22 files)
- D1-D8: Main dungeons
- Archive District
- Palace Interior
- Remnant Vault (all wings + core)

### `/fields/` - Field Maps (8 files)
- Connecting routes between major locations

### `/hidden/` - Hidden Areas (3 files)
- Dragon's Graveyard
- Sunken City
- Completion notes

### `/integration/` - QA & Testing (7 files)
- Flag traceability scripts
- Palace drop table checks
- Pacing integrity checks
- Execution logs

### `/overworld/` - World Maps (5 files)
- Eclipse state
- Overlay finalization
- Confluence map
- Orion map

### `/palace/` - Final Palace (8 files)
- Master sheet
- Floors 1-5 (bosses + rewards)
- Post-clear voice UI

### `/routes/` - Route Micro-Maps (24 files)
- R01-R17f: All micro routes
- S01-S02: Special routes

### `/scripts/` - Story Scripts (14 files)
- Parts 1-14: Complete narrative

### `/shrines/` - Foundation Shrines (8 files)
- All 8 Foundation shrines
- Growth, Motion, Heat, Tide, Light, Shadow, Time, Mass

### `/submaps/` - Submaps (4 files)
- Crown District approach/hub
- Grand Boulevard
- Old Lumencrest Outer Wards

### `/systems/` - Game Systems (10 files)
- Integrity/stabilization systems
- Unravel audio timelines
- HUD text packages

### `/tower/` - Chroma Tower (17 files)
- Master sheet
- Lobby map
- Captains (F15, 35, 55, 65, 85, 95)
- Boss arenas (F10, 25, 50, 75, 90, 100)
- Post-clear voice UI

### `/towns/` - Towns (23 files)
- 12 town maps
- 11 interior sheets

### `/zones/` - Zones (2 files)
- Old Lumencrest
- Crown Spire Conduit

---

## By Content Type

### Maps & Layouts
| Count | Type | Location |
|-------|------|----------|
| 22 | Dungeon maps | `/dungeons/` |
| 23 | Town maps | `/towns/` |
| 24 | Route micro-maps | `/routes/` |
| 17 | Tower floors | `/tower/` |
| 8 | Field maps | `/fields/` |
| 8 | Shrine maps | `/shrines/` |
| 8 | Palace floors | `/palace/` |
| 4 | Submaps | `/submaps/` |
| 5 | Overworld maps | `/overworld/` |
| 3 | Hidden areas | `/hidden/` |
| 2 | Zone maps | `/zones/` |
| **124** | **Total Maps** | |

### Narrative Content
| Count | Type | Location |
|-------|------|----------|
| 14 | Script parts | `/scripts/` |
| 95 | MSQ scenes | `content/content_msq_full_screenplay.md` |
| 13 | Character quests | `content/content_sidequests_town_life.md` |
| 86 | Party banters | `content/content_party_banter.md` |
| 563 | VO lines | `content/content_combat_text_vo.md` |

### Systems Documentation
| Count | Type | Location |
|-------|------|----------|
| 10 | System docs | `/systems/` |
| 26 | Abilities | `content/content_skills_statuses_tooltips.md` |
| 20+ | Status effects | `content/content_skills_statuses_tooltips.md` |
| 158 | Event flags | `content/content_msq_full_screenplay.md` |

### Items & Economy
| Count | Type | Location |
|-------|------|----------|
| 50+ | Consumables | `content/content_itemization_pack.md` |
| 30+ | Weapons | `content/content_itemization_pack.md` |
| 20+ | Armor pieces | `content/content_itemization_pack.md` |
| 15+ | Accessories | `content/content_itemization_pack.md` |
| 200+ | Recipes | `content/content_itemization_pack.md` |

---

## File Count Summary

| Category | Count |
|----------|-------|
| Maps (all types) | 124 |
| Scripts & Story | 14 |
| Content docs (NEW) | 10 |
| System docs | 10 |
| Character docs | 4 |
| Integration/QA | 7 |
| Audio docs | 2 |
| Archive | 2 |
| **TOTAL** | **170+** |

---

## Implementation Status

| Category | Status |
|----------|--------|
| World layout | ✅ Complete (124 maps) |
| Story script | ✅ Complete (14 parts) |
| Character roster | ✅ Complete (13 members) |
| Event flags | ✅ Complete (158 flags) |
| Quest system | ✅ Complete (MSQ + side) |
| Combat VO | ✅ Complete (563 lines) |
| Items/gear | ✅ Complete (full pack) |
| Economy | ✅ Complete (shops/drops) |
| UI text | ✅ Complete (tutorials/errors) |
| Lore/codex | ✅ Complete (all entries) |

---

## Next Steps for Development

1. **Engine Implementation**
   - Import map layouts
   - Implement flag system
   - Build dialogue system

2. **Asset Creation**
   - Sprites (player, enemy, NPC)
   - Tilesets per biome
   - UI elements
   - Music/SFX

3. **Programming**
   - Combat system
   - Quest system
   - Inventory/crafting
   - Save/load

4. **Testing**
   - Flag validation
   - Balance testing
   - Playthrough

---

*Last Updated: 2026-02-07*
*Status: Content Complete, Ready for Implementation*
