# Content ID Normalization Pass (2026-02-10)

## Summary
- Main quests normalized: **15**
- Mini quests normalized: **200**
- Quest alias entries: **215**
- NPC alias entries: **191**
- Item alias entries: **269**
- Generated story reward items: **269**
- State token references (non-quest prereq/unlock): **65**

## Outputs
- `assets/data/quests/quest_content_main_normalized.json`
- `assets/data/quests/quest_content_mini_normalized.json`
- `assets/data/items/item_content_story_generated.json`
- `assets/data/system/content_id_aliases_generated.json`

## Notes
- `content/quests/*` text and structure remain untouched (authoring source).
- Normalized quests use canonical IDs and runtime-compatible location/item/NPC references where possible.
- `prerequisites`/`unlocks` contain quest IDs only.
- Non-quest gate tokens are preserved in `prerequisite_flags`/`unlock_flags`.
- Original quest/item/NPC tokens are preserved as metadata fields (`source_*`, `*_alias`).
- Generated mini quests without explicit gates receive zone-based default quest prerequisites to preserve act progression cohesion.
