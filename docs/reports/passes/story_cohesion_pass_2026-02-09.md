# Story Cohesion Pass (2026-02-09)

## Summary

- Performed continuity audit across main quest chain, side character arcs, NPC quest hooks, and dialog quest pointers.
- Adjusted progression gates to enforce Act 2 -> Act 3 narrative order and Korr liberation arc.
- Normalized Mira relationship content from romance framing to confidant/trust framing to match canon tone.
- Removed an early unlock pointer that surfaced Korr's recruitment chain before the World Break.
- No broken quest/map/NPC/item/boss references after edits.

## Key Narrative Chain

- `Q_FOURTH_RELIC` -> pre: ['Q_THIRD_RELIC'] | unlocks: ['Q_WORLD_BREACHED', 'Q_FIFTH_RELIC']
- `Q_WORLD_BREACHED` -> pre: ['Q_FOURTH_RELIC'] | unlocks: ['Q_RECRUIT_KORR', 'Q_RESISTANCE_PLOT']
- `Q_RECRUIT_KORR` -> pre: ['Q_WORLD_BREACHED'] | unlocks: ['Q_KORR_LIBERATION']
- `Q_SIXTH_RELIC` -> pre: ['Q_FIFTH_RELIC'] | unlocks: ['Q_KORR_LIBERATION', 'Q_SEVENTH_RELIC', 'Q_DRAGONS_GRAVEYARD']
- `Q_KORR_LIBERATION` -> pre: ['Q_RECRUIT_KORR', 'Q_SIXTH_RELIC'] | unlocks: ['Q_SEVENTH_RELIC']
- `Q_SEVENTH_RELIC` -> pre: ['Q_SIXTH_RELIC', 'Q_KORR_LIBERATION'] | unlocks: ['Q_EIGHTH_RELIC', 'Q_LOST_HISTORY']
- `Q_EIGHTH_RELIC` -> pre: ['Q_SEVENTH_RELIC'] | unlocks: ['Q_ALL_RELICS']
- `Q_ALL_RELICS` -> pre: ['Q_EIGHTH_RELIC', 'Q_KORR_LIBERATION'] | unlocks: ['Q_TOWER_ASCENT']
- `Q_TOWER_ASCENT` -> pre: ['Q_ALL_RELICS'] | unlocks: ['Q_PALACE_OF_FATE']
- `Q_PALACE_OF_FATE` -> pre: ['Q_TOWER_ASCENT'] | unlocks: ['Q_EPILOGUE', 'POST_GAME']
- `Q_EPILOGUE` -> pre: ['Q_PALACE_OF_FATE'] | unlocks: []

## Updated Story Beats

- World Break now explicitly frames Omega pedestal destabilization and Nix stabilization.
- Korr is no longer recruitable in early Act 1; recruitment now occurs post-World Break in Act 2.
- Added dedicated liberation quest to sever Korr's Omega tether before late Act 2/Act 3 escalation.
- Tower ascent now requires full attunement (`Q_ALL_RELICS`) rather than direct skip after `Q_EIGHTH_RELIC`.
- Removed incorrect `REMNANT_VAULT_CLEARED` flag from tower completion.
- Mira's side progression now resolves as a confidant/trust arc (`MIRA_CONFIDANT_PATH`) instead of an explicit romance route.
- Achievement and NPC affinity data now reinforce non-romance relationship tone while preserving affinity progression.

## Files Updated

- `assets/data/quests/quest_main_story.json`
- `assets/data/quests/quest_side_stories.json`
- `assets/data/quests/quest_generated_placeholders.json`
- `assets/data/npcs/npc_captain_varros.json`
- `assets/data/npcs/npc_seam_warden.json`
- `assets/data/dialogs/dialog_npc_baseline.json`
- `assets/data/npcs/npc_mira_thorn.json`
- `assets/data/achievement_master.json`
