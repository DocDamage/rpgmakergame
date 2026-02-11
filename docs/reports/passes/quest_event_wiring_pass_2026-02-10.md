# Quest Event Wiring Pass (2026-02-10)

## Scope

Implemented event-level quest flow wiring on the RPG Maker runtime side:
- populated reusable quest common events
- connected them to `Map001` dev harness events
- reserved named switches/variables for quest debug state

## Files Updated

- `data/System.json`
- `data/CommonEvents.json`
- `data/Map001.json`

## Runtime Wiring Added

### Common Events

1. `CE_QUEST_BOOTSTRAP` (`CommonEvents[1]`)
- Reload quest data (`ReloadQuestData`)
- Force-start `Q_PROLOGUE`
- Snapshot status/step variables
- Check `Q_FIRST_RELIC` availability and `Q_PROLOGUE` completion switch

2. `CE_QUEST_ADVANCE_PROLOGUE` (`CommonEvents[2]`)
- Advance `Q_PROLOGUE` by one step
- Refresh status/step/completion variables

3. `CE_QUEST_COMPLETE_PROLOGUE_AND_UNLOCK` (`CommonEvents[3]`)
- Complete `Q_PROLOGUE`
- Check/start `Q_FIRST_RELIC` if available
- Refresh status/step variables for both quests

4. `CE_QUEST_STATUS_SNAPSHOT` (`CommonEvents[4]`)
- Script snapshot for active/completed counts
- Refresh status/step variables for `Q_PROLOGUE` and `Q_FIRST_RELIC`

### Dev Map Harness (`Map001`)

`Map001` display name updated to: `Dev Affinity + Quest Test`

Events added:
- `EV_QUEST_BOOT_AUTORUN` (id:1, autorun)
  - Calls `CE_QUEST_BOOTSTRAP` once, then self-switch A
- `EV_QUEST_ADVANCE_PROLOGUE` (id:2, action button at x=4,y=2)
  - Calls `CE_QUEST_ADVANCE_PROLOGUE`
- `EV_QUEST_COMPLETE_PROLOGUE` (id:3, action button at x=6,y=2)
  - Calls `CE_QUEST_COMPLETE_PROLOGUE_AND_UNLOCK`
- `EV_QUEST_STATUS_TERMINAL` (id:4, action button at x=8,y=2)
  - Calls `CE_QUEST_STATUS_SNAPSHOT`
  - Shows debug text with key quest variables/switches
- `EV_TARGET_BROKER_VANE` (id:5, action button at x=10,y=2)
  - Tagged with `<questTargetNpc:NPC_BROKER_VANE>` for target-marker testing

Map note tags:
- `<chromaDevMap:true>`
- `<chromaMapId:T_DUSTHAVEN_112x72>` (bridges runtime map to canonical quest target location ID)

## Debug Variable/Switch Allocation

### Switches
- `60`: `QUEST_BOOT_OK`
- `61`: `QUEST_LAST_CMD_OK`
- `62`: `QUEST_NEXT_AVAILABLE`
- `63`: `QUEST_PROLOGUE_COMPLETE`
- `64`: `QUEST_FIRST_RELIC_STARTED`

### Variables
- `10`: `QUEST_ACTIVE_COUNT`
- `11`: `QUEST_COMPLETED_COUNT`
- `12`: `QUEST_PROLOGUE_STATUS_CODE`
- `13`: `QUEST_PROLOGUE_STEP`
- `14`: `QUEST_FIRST_RELIC_STATUS_CODE`
- `15`: `QUEST_FIRST_RELIC_STEP`
- `16`: `QUEST_TOTAL_LOADED`

## Validation

- JSON parse checks passed for:
  - `System.json`
  - `CommonEvents.json`
  - `Map001.json`
- Existing project integrity gates remained green:
  - `python3 tools/validate_content_integrity.py` => `Errors: 0`, `Warnings: 0`
  - `python3 tools/audit_environment_sprite_coverage.py --strict-candidates` => `Errors: 0`, `Warnings: 0`
  - `python3 tools/validate_world_integrity.py` => `Errors: 0`, `Warnings: 0`
