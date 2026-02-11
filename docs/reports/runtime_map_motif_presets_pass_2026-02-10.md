# Runtime Map Motif Presets Pass (2026-02-10)

## Scope

Added map-type motif presets so runtime tile geometry follows consistent visual language by environment class.

Updated files:

- `tools/export_canonical_maps_to_rmmz.py`
- `tools/validate_runtime_map_bridge.py`

## Implementation

### Exporter motif profiles

Added `MotifProfile` selection and map-type routing:

- `overworld_regional`
- `town_plaza`
- `route_lane`
- `dungeon_corridor`
- `spire_corridor` (tower/palace/post-game)
- `shrine_ring`
- `default`

Motif behaviors include:

- profile-specific path thickness and hub radius
- profile-specific landmark/hazard/interior/puzzle paint radii
- optional cross-spokes from center
- optional anchor loop linking
- optional region border painting
- profile-specific region texture density (`region_stride`)

### Runtime traceability

Exporter now writes:

- `<chromaMotifProfile:...>` on each generated runtime map note.

### Bridge validator hardening

`tools/validate_runtime_map_bridge.py` now checks:

- required motif tag coverage (`chromaMotifProfile`)
- existing geometry consistency checks remain enforced:
  - `chromaPaintedTiles`
  - `chromaDressingEvents`
  - non-zero z1/z2/z3 consistency

## Regeneration

```bash
python3 tools/export_canonical_maps_to_rmmz.py
```

Artifacts refreshed:

- `data/Map002.json` .. `data/Map099.json`
- `data/MapInfos.json`
- `assets/data/system/runtime_map_bridge_generated.json`

## Metrics

- generated maps: `98`
- total painted tiles: `6786`
- average painted tiles/map: `69.24`

Layer non-zero totals:

- z1: `448`
- z2: `5812`
- z3: `526`

Motif profile distribution:

- `default`: `2`
- `dungeon_corridor`: `23`
- `overworld_regional`: `1`
- `route_lane`: `23`
- `shrine_ring`: `10`
- `spire_corridor`: `25`
- `town_plaza`: `14`

## Validation

```bash
python3 tools/validate_runtime_map_bridge.py --strict
PATH="$HOME/.local/bin:$PATH" python3 tools/run_project_audit_gate.py --scope all
```

Status:

- runtime map bridge strict validation: pass (`Errors: 0`, `Warnings: 0`)
- full project audit gate: pass (`Passed: 31`, `Failed: 0`)
