# Chroma's Edge - Production Tools

## Quick Start

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
