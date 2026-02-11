# Chroma's Edge - Production Tools

## Quick Start

### Run Project Audit Gate
```bash
python tools/run_project_audit_gate.py --scope all
# strict hard gate:
python tools/run_project_audit_gate.py --scope all --strict
```

Runs the full cohesion/integrity/runtime pipeline in one command.
`--strict` enables stricter checks where supported (story gating, runtime bridge
strictness, transfer contract strictness, gate-token strictness, etc.).

### Validate Asset Naming
```bash
python tools/validate_naming.py
# Windows wrapper:
tools\validate_naming.bat
```

Validates production asset filenames under `assets/`.

### Validate World Integrity
```bash
python tools/validate_world_integrity.py
# Strict gate-token mode:
python tools/validate_world_integrity.py --strict-gates
```

Validates map graph links, quest stage hops, encounter-table coverage,
and connection trigger/condition sanity.

### Slice Imports Then Pad
```bash
python tools/slice_imports_then_pad.py --off-grid-only --overwrite
```

Scans `assets/sprites/*/_imports`, slices source sheets, and writes outputs to:
`assets/sprites/*/_slices/<source_stem>/`

Each exported slice is padded to 16px multiples (transparent canvas, no resample).
Reports are written to `docs/reports/`.

### Build Heroes99 Overworld Sheets
```bash
python tools/build_heroes99_overworld_sheets.py
```

Composes layered Heroes99 parts into provisional RPG Maker MZ `$` character sheets
for all 13 protagonists, writes runtime sheets into `img/characters/`, mirrors source
copies into `assets/sprites/characters/*/overworld/`, and updates `data/Actors.json`
`characterName` bindings.

### Build Heroes99 SV Actor Sheets
```bash
python tools/build_heroes99_sv_actor_sheets.py
```

Composes layered Heroes99 parts into provisional RPG Maker MZ side-view actor sheets
for all 13 protagonists, writes runtime sheets into `img/sv_actors/`, mirrors source
copies into `assets/sprites/characters/*/battle/`, and updates `data/Actors.json`
`battlerName` bindings.

### Validate Party Sprite Coverage
```bash
python tools/validate_party_sprite_coverage.py
# strict:
python tools/validate_party_sprite_coverage.py --strict
```

Validates that all 13 protagonists have complete runtime + source sprite sheets:
- overworld `$` sheets (`144x256`, no blank frame cells)
- side-view actor sheets (`864x576`, no blank motion frames)
- actor bindings in `data/Actors.json` (`characterName`, `characterIndex`, `battlerName`)
- actor face image references exist

### Provision Runtime Enemy Battlers
```bash
python tools/provision_runtime_enemy_battlers.py --overwrite
```

Maps starter runtime enemy battler names from `data/Enemies.json` to curated
production enemy sprites, writes resolved files into both `img/sv_enemies/`
and `img/enemies/`, and upscales with nearest-neighbor for runtime readability.

### Provision Runtime Image Placeholders
```bash
python tools/provision_runtime_image_placeholders.py
# preview only:
python tools/provision_runtime_image_placeholders.py --dry-run
```

Creates missing core runtime image files (system sheets, title, battlebacks,
used map tilesets, vehicle character sheet, map parallaxes) as deterministic
placeholder PNGs so the project can run without hard missing-image crashes.
Existing files are preserved by default.

### Validate Runtime Image References
```bash
python tools/validate_runtime_image_references.py
# strict:
python tools/validate_runtime_image_references.py --strict --strict-effects
```

Scans runtime image/effect/movie references from system, actors, enemies,
animations, events, command lists, and map-used tilesets, then validates they
resolve to real files under `img/`, `effects/`, and `movies/`.

### Validate Runtime Audio References
```bash
python tools/validate_runtime_audio_references.py
# strict:
python tools/validate_runtime_audio_references.py --strict
```

Scans audio tokens referenced by `data/System.json`, `data/CommonEvents.json`,
`data/Troops.json`, and `data/Map###.json`, then verifies each token resolves
in runtime folders `audio/bgm|bgs|me|se`.

### Provision Runtime Audio Placeholders
```bash
python tools/provision_runtime_audio_placeholders.py
# preview only:
python tools/provision_runtime_audio_placeholders.py --dry-run
```

Creates missing runtime audio token files in `audio/bgm|bgs|me|se` using
`assets/audio/_placeholder_silence.ogg` as a source, so default/system audio
references cannot fail due to missing files.

### NW Runtime Smoke Playtest
```bash
tools/run_nw_playtest.sh
# or
npm run playtest:nw
```

Launches NW.js with software WebGL fallback flags suitable for this environment,
records a smoke-test log, and fails fast when common runtime blockers are detected
(for example, `"Your browser does not support WebGL."`).

### Audit NW Runtime Log
```bash
python tools/audit_nw_runtime_log.py /tmp/nw_playtest_smoke.log
```

Scans NW smoke logs for actionable runtime failures (console exceptions,
missing resources/files, WebGL fatal startup failures) while filtering common
benign environment noise.

### Validate Runtime World Dressing
```bash
python tools/validate_runtime_world_dressing.py
# include surplus detection:
python tools/validate_runtime_world_dressing.py --warn-surplus
# strict (warnings become errors):
python tools/validate_runtime_world_dressing.py --warn-surplus --strict
```

Compares canonical map world-dressing anchors (`landmarks`, `hazards`, `puzzles`,
POIs, regions, notes, story/key NPC anchors) against runtime `Map###.json` event tags
to catch export drift where overworld/environment objects exist in data but not in-game.

### Validate Runtime Transfer Contract
```bash
python tools/validate_runtime_transfer_contract.py
```

Verifies runtime transfer events map back to canonical expectations per map
(target + gate token), including transfer note tags (`<chromaPortalTarget>`,
`<chromaPortalGate>`), gate branch structure, and missing/extra transfer drift.

### Audit Quest Route Pacing
```bash
python tools/audit_quest_route_pacing.py --scope core
# deep pass:
python tools/audit_quest_route_pacing.py --scope all
```

Checks quest step travel flow against the canonical map graph, including:
- missing target map references in quest steps
- unreachable step-to-step transitions
- directionality-only route issues
- long hop chains that may create navigation friction

## Templates

Copy a template when creating new data assets:

```bash
# New map
cp tools/templates/map_template.json assets/data/maps/map_my_new_map.json

# New NPC
cp tools/templates/npc_template.json assets/data/npcs/npc_my_npc.json

# New quest
cp tools/templates/quest_template.json assets/data/quests/quest_my_quest.json
```

## Templates Available

| Template | Use For |
|---|---|
| `map_template.json` | Map data files |
| `npc_template.json` | NPC definitions |
| `dialog_template.json` | Dialog trees |
| `item_template.json` | Items (consumables, gear) |
| `enemy_template.json` | Enemy definitions |
| `quest_template.json` | Quest definitions |
| `encounter_table_template.json` | Random encounter tables |
| `drop_table_template.json` | Enemy loot tables |

## Tool Layout

```text
tools/
|-- README.md
|-- validate_naming.py
|-- validate_naming.bat
|-- validate_world_integrity.py
|-- slice_imports_then_pad.py
|-- run_nw_playtest.sh
`-- templates/
    |-- map_template.json
    |-- npc_template.json
    |-- dialog_template.json
    |-- item_template.json
    |-- enemy_template.json
    |-- quest_template.json
    |-- encounter_table_template.json
    `-- drop_table_template.json
```

## CI/CD Integration

```yaml
# .github/workflows/assets.yml
- name: Validate Asset Naming
  run: python tools/validate_naming.py
```

## Troubleshooting

- `Directory not found`: run from project root, or pass an explicit path.
- `Module PIL not found`: install Pillow.

```bash
pip install Pillow
```
