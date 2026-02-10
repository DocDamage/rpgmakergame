# Dialog Tone Pass (2026-02-09)

## Scope

- Applied a full pass to named NPC dialogue for tone and cohesion.
- Added broad ambient banter support for large NPC sprite pools.

## Named NPC Improvements

- File: `assets/data/dialogs/dialog_npc_baseline.json`
- Updated all named trees to include:
  - More character-specific voice
  - One `n_rumor` branch per NPC
  - Stronger route/exploration warnings tied to world instability
  - Cleaner quest/shop wording (`Active leads`, `Stock ledger`)

## Ambient Banter Pack

- File: `assets/data/dialogs/dialog_ambient_banter_pack.json`
- Added 20 reusable archetype trees (`DT_AMBIENT_*`) for quick assignment to non-quest NPCs.

## Validation

- JSON parse check: pass
- Dialogue node/link integrity: `DIALOG_REF_ERRORS 0`
- Asset naming and ID validation: pass (`Invalid: 0`)
