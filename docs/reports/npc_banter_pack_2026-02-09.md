# NPC Banter Pack (2026-02-09)

## What Was Added

- Rewrote all named NPC dialogue trees in `assets/data/dialogs/dialog_npc_baseline.json` with:
  - Character-specific tone
  - New `n_rumor` node
  - Less placeholder-style exits/routes
- Added a reusable ambient dialogue bank in:
  - `assets/data/dialogs/dialog_ambient_banter_pack.json`

## Ambient Dialogue IDs

- `DT_AMBIENT_BROKER`
- `DT_AMBIENT_GUARD_CAPTAIN`
- `DT_AMBIENT_INNKEEPER`
- `DT_AMBIENT_MASTER_SMITH`
- `DT_AMBIENT_PRIESTESS`
- `DT_AMBIENT_RESISTANCE_SCOUT`
- `DT_AMBIENT_SAILOR`
- `DT_AMBIENT_SCHOLAR`
- `DT_AMBIENT_SCHOLAR_ELDER`
- `DT_AMBIENT_SMITH`
- `DT_AMBIENT_SCAVENGER`
- `DT_AMBIENT_DOCKWORKER`
- `DT_AMBIENT_CARAVANER`
- `DT_AMBIENT_MECHANIC`
- `DT_AMBIENT_COURIER`
- `DT_AMBIENT_SCRIBE`
- `DT_AMBIENT_STREET_PROPHET`
- `DT_AMBIENT_WARD_TECH`
- `DT_AMBIENT_TRACKER`
- `DT_AMBIENT_BOUNTY_CLERK`

## Recommended Sprite -> Dialogue Mapping

- `NPC_BROKER_M` -> `DT_AMBIENT_BROKER`
- `NPC_GUARD_CAPTAIN` -> `DT_AMBIENT_GUARD_CAPTAIN`
- `NPC_INNKEEPER_F` -> `DT_AMBIENT_INNKEEPER`
- `NPC_MASTER_SMITH` -> `DT_AMBIENT_MASTER_SMITH`
- `NPC_PRIESTESS` -> `DT_AMBIENT_PRIESTESS`
- `NPC_RESISTANCE` -> `DT_AMBIENT_RESISTANCE_SCOUT`
- `NPC_SAILOR_F` -> `DT_AMBIENT_SAILOR`
- `NPC_SCHOLAR` -> `DT_AMBIENT_SCHOLAR`
- `NPC_SCHOLAR_ELDER` -> `DT_AMBIENT_SCHOLAR_ELDER`
- `NPC_SMITH` -> `DT_AMBIENT_SMITH`

## Wiring Pattern

For each new NPC record in `assets/data/npcs/*.json`, set:

- `sprite`: one of your production sprite IDs
- `dialog_tree`: one of the ambient dialogue IDs above

This keeps your large NPC roster coherent without forcing unique authored dialogue for every single actor.
