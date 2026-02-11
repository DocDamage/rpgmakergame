# Runtime Playtest + Fix Pass (2026-02-10)

## Scope
- Apply the requested side-view runtime transition.
- Execute full local audit gates.
- Run additional runtime-focused checks for battle asset readiness.

## Key Findings
1. Side-view was enabled successfully (`data/System.json` `optSideView: true`).
2. Main actor runtime bindings were valid for all party members (`1-13`):
   - Overworld character sheets present (`img/characters/$ce_*.png`)
   - SV battler sheets present (`img/sv_actors/ce_sv_*.png`)
3. Critical runtime gap identified and fixed:
   - `img/sv_enemies/` did not exist after enabling side-view.
   - With side-view on, enemy battlers load from `img/sv_enemies`, so battles would have missing enemy visuals.

## Fix Applied
- Added `tools/provision_runtime_enemy_battlers.py` to map runtime battler names from
  `data/Enemies.json` to curated production sprites and provision both:
  - `img/sv_enemies/<name>.png`
  - `img/enemies/<name>.png`
- Provisioned:
  - `Goblin.png`
  - `Gnome.png`
  - `Crow.png`
  - `Treant.png`
  - `Hi_monster.png`

## Validation
- `python3 tools/run_project_audit_gate.py --scope all` => all checks passed.
- Side-view enemy runtime check (`optSideView=true`, `data/Enemies.json` battlerName resolution)
  => no missing files.
- Story strict checks:
  - `python3 tools/audit_story_cohesion.py --scope all --strict-act-gating --strict-npc-anchors` => pass
  - `python3 tools/validate_content_integrity.py --scope all --strict-map-npc-anchors` => pass
- Extra runtime story checks documented in:
  - `docs/reports/story_runtime_cohesion_deep_pass_2026-02-10.md`

## Note
- A true interactive in-engine play session was not executed in this environment because
  `nw`/`nwjs` is not present in PATH. Static/runtime data and asset integrity checks were
  run to compensate.
