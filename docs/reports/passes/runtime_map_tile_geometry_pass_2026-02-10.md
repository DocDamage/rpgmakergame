# Runtime Map Tile Geometry Pass (2026-02-10)

## Scope

Extended canonical runtime map export so canonical world anchors affect map tile layers, not only events.

Updated file:

- `tools/export_canonical_maps_to_rmmz.py`

## Implementation

Added deterministic tile painting pipeline for generated runtime maps:

- coordinate helpers:
  - canonical rect scaling (`canonical_rect_to_runtime`)
  - map layer index/set helpers for `data` array writes
- geometry painters:
  - line painter (for route links)
  - diamond cluster painter (for landmarks/hazards/interiors/puzzles)
  - region texture pattern painter (for region rectangles)
- bridge integration:
  - collects generated anchor points during event emission
  - paints geometry into z1/z2/z3 layers while preserving generated event cells
  - writes map-note metric tag:
    - `<chromaPaintedTiles:N>`

Validation hardening:

- `tools/validate_runtime_map_bridge.py` now verifies:
  - presence of `chromaPaintedTiles` and `chromaDressingEvents` tags
  - consistency between `chromaPaintedTiles` and actual non-zero tile counts in z1/z2/z3

## Regeneration

```bash
python3 tools/export_canonical_maps_to_rmmz.py
```

Artifacts refreshed:

- `data/Map002.json` .. `data/Map099.json`
- `data/MapInfos.json`
- `assets/data/system/runtime_map_bridge_generated.json`

## Geometry Metrics

- generated maps scanned: `98`
- total painted tiles (non-ground layers via exporter metric): `3119`
- average painted tiles per generated map: `31.83`
- max painted map:
  - `Map049.json` (`Orion Overworld`) -> `978`

Layer utilization totals (non-zero cells):

- z1: `336`
- z2: `2384`
- z3: `399`

## Validation

```bash
python3 tools/validate_runtime_map_bridge.py
PATH="$HOME/.local/bin:$PATH" python3 tools/run_project_audit_gate.py --scope all
```

Status:

- runtime map bridge validation: pass (`Errors: 0`, `Warnings: 0`)
- full audit gate: pass (`Passed: 31`, `Failed: 0`)

## Follow-Up

Motif preset pass:

- `docs/reports/runtime_map_motif_presets_pass_2026-02-10.md`
- adds map-type-specific geometry motifs and motif-tag validation.
