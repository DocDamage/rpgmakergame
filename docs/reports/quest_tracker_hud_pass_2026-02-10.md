# Quest Tracker HUD Pass (2026-02-10)

## Scope

Implemented map-time objective visibility by adding a quest tracker HUD tied to `ChromaEdge_QuestSystem`.

## Files Updated

- `js/plugins/ChromaEdge_QuestTrackerHUD.js` (new)
- `js/plugins.js` (enabled plugin entry)

## Runtime Features Added

1. Map HUD window
- Displays top tracked quest on `Scene_Map`.
- Prioritization:
  - first `active` quest
  - optionally first `available` quest when no active quest exists
- Displays:
  - status label (`ACTIVE`, `AVAILABLE`, `COMPLETED`, etc.)
  - quest name
  - current step text + target location/NPC (if present)
  - map-awareness hint:
    - `ON MAP` when current map note tag matches step target location
    - `GO: <target_location>` when objective is off-map

2. Target marker sprite layer
- Added on-map target marker sprite anchored to tagged events.
- Marker source resolution:
  - tracked quest step `target_npc` -> event note tag `<questTargetNpc:NPC_ID>`
  - fallback tracked quest ID -> event note tag `<questTargetQuest:QUEST_ID>`
- Marker only shows when current map canonical ID matches step `target_location`.
- Canonical map ID is read from map note tags:
  - `<chromaMapId:MAP_ID>`
  - or `<questMapId:MAP_ID>`

3. Save-persistent visibility state
- `Game_System` now stores HUD visibility (`chromaQuestHudVisible`).
- `Game_System` now stores marker visibility (`chromaQuestMarkerVisible`).
- Default visibility configurable by plugin parameter.

4. Plugin commands
- `SetQuestHudVisible`
- `ToggleQuestHud`
- `RefreshQuestHud`
- `SetQuestMarkerVisible`
- `ToggleQuestMarker`

5. Script API
- `ChromaEdge.QuestTracker.show()`
- `ChromaEdge.QuestTracker.hide()`
- `ChromaEdge.QuestTracker.toggle()`
- `ChromaEdge.QuestTracker.refresh()`
- `ChromaEdge.QuestTracker.markerShow()`
- `ChromaEdge.QuestTracker.markerHide()`
- `ChromaEdge.QuestTracker.markerToggle()`
- `ChromaEdge.QuestTracker.markerVisible()`

## Plugin Configuration

Enabled plugin entry:
- `ChromaEdge_QuestTrackerHUD` (`status: true`)

Default params:
- `enabledByDefault=true`
- `x=0`
- `y=42`
- `width=430`
- `lineCount=2`
- `opacity=192`
- `showAvailableWhenNoActive=true`
- `hideDuringMessage=true`
- `showTargetMarker=true`
- `markerEnabledByDefault=true`
- `markerYOffset=52`

## Validation

- `python3 tools/validate_content_integrity.py` => `Errors: 0`, `Warnings: 0`
- `python3 tools/audit_environment_sprite_coverage.py --strict-candidates` => `Errors: 0`, `Warnings: 0`
- `python3 tools/validate_world_integrity.py` => `Errors: 0`, `Warnings: 0`

## Notes

- Node-based JS syntax checks were not possible in this environment (`node` unavailable).
- Implementation follows existing MZ plugin alias patterns and uses only core runtime APIs.
