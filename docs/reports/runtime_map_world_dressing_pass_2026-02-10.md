# Runtime Map World Dressing Pass (2026-02-10)

## Scope

Major bridge upgrade to make canonical map metadata visible/playable in runtime map exports:

- metadata-driven world dressing marker events
- POI-driven transfer portal synthesis
- deterministic coordinate scaling + collision-safe event placement

## Implementation

Updated: `tools/export_canonical_maps_to_rmmz.py`

### Canonical fields now consumed

- `connections` (existing transfer flow, now coordinate-aware when `coords` exist)
- `points_of_interest` (new transfer portals when target canonical maps resolve)
- `landmarks`
- `hazards`
- `interiors`
- `ambient_npcs`
- `regions`
- `puzzles`
- `events` (story-state markers)
- `key_npcs` (roster markers)
- `notes` (brief marker + map note tag)

### Runtime behavior added

- transfer events use tileset-based portal marker tile IDs (instead of always invisible graphics)
- world dressing events are emitted with stable `chromaWorldDress:*` note tags
- event placement is deterministic and avoids overlaps with existing generated events
- map notes now include:
  - `<chromaTransferEvents:N>`
  - `<chromaDressingEvents:N>`

## Export Outcome

Command:

```bash
python3 tools/export_canonical_maps_to_rmmz.py
```

Result:

- canonical maps exported: `98`
- runtime generated maps written: `98`
- bridge artifact refreshed: `assets/data/system/runtime_map_bridge_generated.json`

### Generated event totals

- transfer portals: `265`
- POI-derived portals: `8`
- world dressing events by category:
  - `ambient_npc`: `79`
  - `interior`: `55`
  - `key_npcs`: `54`
  - `story_events`: `54`
  - `landmark`: `29`
  - `notes`: `27`
  - `puzzle`: `16`
  - `region`: `9`
  - `poi` markers (non-transfer POI fallback): `8`
  - `hazard`: `1`

## Validation

```bash
python3 tools/validate_runtime_map_bridge.py
PATH="$HOME/.local/bin:$PATH" python3 tools/run_project_audit_gate.py --scope all
```

Status:

- runtime map bridge validation: pass (`Errors: 0`, `Warnings: 0`)
- full audit gate (`--scope all`): pass (`Passed: 31`, `Failed: 0`)

## Follow-Up

Tile-layer geometry pass:

- `docs/reports/runtime_map_tile_geometry_pass_2026-02-10.md`
- extends runtime export from event-only dressing to deterministic map `data` layer painting.

Motif preset pass:

- `docs/reports/runtime_map_motif_presets_pass_2026-02-10.md`
- extends geometry with map-type visual motif presets and motif validation tags.
