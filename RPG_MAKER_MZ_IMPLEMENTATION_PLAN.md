# RPG MAKER MZ - COMPLETE IMPLEMENTATION PLAN
## Chroma's Edge Game Development Roadmap

---

## CONTEXT

**Project Status:** Documentation 100% complete (all design documents, story scripts, character rosters, NPC integration guides, and act structure finalized).

**Next Phase:** Full game implementation in RPG Maker MZ.

**Challenge:** Transform 186 story scenes, 13 playable characters, 86 NPCs, 12 towns, 8 dungeons, and complex custom systems into a functioning RPG Maker MZ game.

**Technical Foundation:** RPG Maker MZ uses JavaScript for plugins and has a built-in Database for core game data (actors, skills, items, enemies, etc.). Custom systems require JavaScript plugin development.

**Estimated Total Implementation Time:** 400-550 hours (10-14 weeks full-time, 20-28 weeks half-time)

---

## IMPLEMENTATION ARCHITECTURE OVERVIEW

### Three-Tier Development Approach

**TIER 1: FOUNDATION (Weeks 1-4)**
- Database configuration (actors, skills, items, weapons, armor, enemies)
- Core plugin development (affinity, summons, limit breaks)
- Basic event scripting framework
- First playable Act 1 prototype

**TIER 2: SYSTEMS (Weeks 5-10)**
- Advanced plugin development (quests, dialogue trees, day/night)
- Full event scripting (Acts 1-3, all 186 scenes)
- Town and dungeon map creation
- NPC placement and dialogue implementation

**TIER 3: POLISH (Weeks 11-14)**
- Advanced systems (Tower progression, mercy choices, ending branches)
- Music/SFX integration
- Balance testing and bug fixing
- Postgame content implementation

---

## WEEK-BY-WEEK BREAKDOWN

[Complete week-by-week details from Weeks 1-14 - see full plan file for implementation details]

---

## FILE STRUCTURE & ORGANIZATION

### Project Folder Structure
```
ChromasEdge_RPGMZ/
├── audio/
│   ├── bgm/ (background music)
│   ├── bgs/ (background sounds)
│   ├── me/ (music effects)
│   └── se/ (sound effects)
├── data/
│   ├── Actors.json (13 party members)
│   ├── Classes.json (13 classes)
│   ├── Skills.json (200+ skills)
│   ├── Items.json (consumables)
│   ├── Weapons.json (65 weapons)
│   ├── Armors.json (130+ armor pieces)
│   ├── Enemies.json (150+ enemies)
│   ├── Troops.json (100+ battle formations)
│   ├── CommonEvents.json (summons, DLBs, quests)
│   ├── System.json (game system settings)
│   ├── Map001.json to Map200.json (all maps)
│   ├── DialogueTrees.json (NPC dialogue data)
│   └── NPCSchedules.json (NPC time schedules)
├── img/
│   ├── characters/ (character sprites)
│   ├── faces/ (character portraits)
│   ├── enemies/ (enemy sprites)
│   ├── sv_actors/ (sideview battle sprites)
│   ├── tilesets/ (map tiles)
│   └── ui/ (custom UI elements)
├── js/
│   ├── plugins/
│   │   ├── ChromaEdge_CharacterAffinity.js
│   │   ├── ChromaEdge_AffinityMenu.js
│   │   ├── ChromaEdge_SummonSystem.js
│   │   ├── ChromaEdge_DualLimitBreak.js
│   │   ├── ChromaEdge_QuestSystem.js
│   │   ├── ChromaEdge_QuestJournal.js
│   │   ├── ChromaEdge_DialogueTree.js
│   │   ├── ChromaEdge_DayNightSystem.js
│   │   ├── ChromaEdge_NPCScheduling.js
│   │   ├── ChromaEdge_MercyChoiceSystem.js
│   │   ├── ChromaEdge_TowerProgression.js
│   │   └── ChromaEdge_EndingBranch.js
│   └── rmmz_core.js, rmmz_managers.js, etc. (MZ core files)
├── maps/
│   ├── towns/ (12 town maps)
│   ├── dungeons/ (8 dungeon maps)
│   ├── tower/ (100 tower floor maps)
│   └── overworld/ (overworld maps)
└── package.json (project metadata)
```

---

## PLUGIN LOAD ORDER (CRITICAL)

1. ChromaEdge_CharacterAffinity.js (foundation for DLB)
2. ChromaEdge_SummonSystem.js (independent)
3. ChromaEdge_DualLimitBreak.js (depends on Affinity)
4. ChromaEdge_QuestSystem.js (independent)
5. ChromaEdge_DialogueTree.js (independent)
6. ChromaEdge_DayNightSystem.js (foundation for Scheduling)
7. ChromaEdge_NPCScheduling.js (depends on DayNight)
8. ChromaEdge_MercyChoiceSystem.js (independent)
9. ChromaEdge_TowerProgression.js (independent)
10. ChromaEdge_EndingBranch.js (independent)
11. ChromaEdge_AffinityMenu.js (depends on Affinity)
12. ChromaEdge_QuestJournal.js (depends on Quest)

---

## PLUGIN OVERVIEW

### 12 Custom JavaScript Plugins

1. **CharacterAffinity.js** - Relationship tracking (1-10 levels per pair)
2. **AffinityMenu.js** - UI for viewing relationships
3. **SummonSystem.js** - 13 summons with owner mechanics
4. **DualLimitBreak.js** - 78 unique 2-character ultimates (Affinity 10+ required)
5. **QuestSystem.js** - Quest tracking and progression
6. **QuestJournal.js** - Quest UI menu
7. **DialogueTree.js** - Branching dialogue with conditional branches
8. **DayNightSystem.js** - 24-hour time cycle with environmental changes
9. **NPCScheduling.js** - NPC location changes based on time
10. **MercyChoiceSystem.js** - Boss spare/kill choices
11. **TowerProgression.js** - 100-floor tower with difficulty scaling
12. **EndingBranch.js** - Free Prime vs Anchor ending branches

---

## TIMELINE SUMMARY

| Week | Focus | Hours | Deliverables |
|------|-------|-------|--------------|
| 1 | Database Foundation | 24 | Actors, Classes, System setup |
| 2 | Skills & Abilities | 24 | 200+ skills, Limit Breaks |
| 3 | Items & Equipment | 24 | 65 weapons, 130+ armor |
| 4 | Enemies & Troops | 24 | 150+ enemies, troop formations |
| 5 | Plugin: Affinity | 32 | Relationship tracking system |
| 6 | Plugin: Summon | 32 | 13 summons, Callum special case |
| 7 | Plugin: Dual Limit Break | 40 | 78 unique DLBs |
| 8 | Plugin: Quest System | 32 | Quest tracking & journal |
| 9 | Plugin: Dialogue Trees | 32 | Branching dialogue system |
| 10 | Plugin: Day/Night | 32 | Time system & NPC scheduling |
| 11 | Plugin: Mercy Choice | 20 | Boss choice mechanics |
| 12 | Plugin: Tower | 28 | 100-floor dungeon |
| 13 | Plugin: Ending Branch | 24 | Ending choice & postgame |
| 14 | Testing & Polish | 40 | Bug fixes, balance, music |

**Total:** ~408 hours (10-14 weeks full-time)

---

## SUCCESS CRITERIA

### Minimum Viable Product
- All 13 party members playable
- Affinity & Summon systems working
- First 4 dungeons playable
- Act 1 fully scripted
- 4 core towns implemented

### Full Game Release
- All 12 plugins implemented
- All 186 story scenes scripted
- All 12 towns with NPCs
- All 8 dungeons playable
- Tower 100 floors complete
- Both ending branches playable
- Postgame content accessible
- Music/SFX integrated
- Game fully balanced

---

## NEXT STEPS

1. Set up RPG Maker MZ project (Week 1)
2. Initialize Git repository
3. Create Database entries for all actors
4. Begin plugin development (start with Affinity)
5. Create test maps for plugin testing
6. Implement Act 1 prototype

---

**Plan Status:** ✅ APPROVED & READY FOR IMPLEMENTATION
**Estimated Timeline:** 10-14 weeks (full-time) or 20-28 weeks (half-time)
**Budget:** ~$100-300 (RPG Maker MZ license + asset packs)
