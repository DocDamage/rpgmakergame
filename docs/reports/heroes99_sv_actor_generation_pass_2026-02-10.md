# Heroes99 SV Actor Generation Pass (2026-02-10)

## Scope
- Built provisional RPG Maker MZ side-view actor sheets for all 13 party actors from `Heroes99 v1.2` layered sources.
- Wired runtime actor battler bindings in `data/Actors.json`.

## Outputs
- Runtime sheets: `img/sv_actors/ce_sv_<slug>.png` (13 files)
- Source mirrors:
  - `assets/sprites/characters/kade/battle/spr_kade_sv_actor_sheet.png`
  - `assets/sprites/characters/nix-7/battle/spr_nix7_sv_actor_sheet.png`
  - `assets/sprites/characters/renna/battle/spr_renna_sv_actor_sheet.png`
  - `assets/sprites/characters/twist/battle/spr_twist_sv_actor_sheet.png`
  - `assets/sprites/characters/suresh/battle/spr_suresh_sv_actor_sheet.png`
  - `assets/sprites/characters/sova/battle/spr_sova_sv_actor_sheet.png`
  - `assets/sprites/characters/grit/battle/spr_grit_sv_actor_sheet.png`
  - `assets/sprites/characters/ashka/battle/spr_ashka_sv_actor_sheet.png`
  - `assets/sprites/characters/senna/battle/spr_senna_sv_actor_sheet.png`
  - `assets/sprites/characters/callum/battle/spr_callum_sv_actor_sheet.png`
  - `assets/sprites/characters/petra/battle/spr_petra_sv_actor_sheet.png`
  - `assets/sprites/characters/vex/battle/spr_vex_sv_actor_sheet.png`
  - `assets/sprites/characters/korr/battle/spr_korr_sv_actor_sheet.png`
- Preview board:
  - `docs/reports/heroes99_sv_actor_party_preview_2026-02-10.png`

## Runtime Mapping
- Updated actor IDs `1-13` `battlerName` to:
  - `ce_sv_kade`, `ce_sv_nix7`, `ce_sv_renna`, `ce_sv_twist`, `ce_sv_suresh`, `ce_sv_sova`, `ce_sv_grit`, `ce_sv_ashka`, `ce_sv_senna`, `ce_sv_callum`, `ce_sv_petra`, `ce_sv_vex`, `ce_sv_korr`

## Implementation Notes
- MZ SV actor sheet layout requires `9x6` cells (18 motions x 3 patterns).
- Heroes99 atlas poses were mapped into the 18 MZ motion rows and normalized into
  `96x96` frames.
- This is a provisional runtime-safe pass and should be replaced later with bespoke
  hand-authored per-character combat motion sheets.

## Validation
- Actor IDs `1-13` have existing files in `img/sv_actors/` matching bound `battlerName`.
- Existing overworld bindings remain intact (`characterName` points to `$ce_*` files).
