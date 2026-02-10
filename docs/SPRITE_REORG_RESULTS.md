# Sprite Reorg Results

Generated: 2026-02-09

## Completed Actions

- Moved all queued external candidates into `assets/sprites/preview/import_queue/` (118 files).
- Promoted approved PNG assets from import queue to production category imports.
- Triaged remaining queue files and promoted usable PNG assets (`fx`, `npcs`, `bosses`).
- Converted a remaining GIF source to PNG for import and archived the original GIF under `assets/sprites/preview/source_archive/bosses/`.
- Cleared import queue (`0` files remain).
- Moved blacksmith NPC sheets from preview/tileset staging into production NPC imports.

## Production Import Counts (Current)

- `assets/sprites/characters/_imports`: 52
- `assets/sprites/npcs/_imports`: 30
- `assets/sprites/enemies/_imports`: 1
- `assets/sprites/bosses/_imports`: 40
- `assets/sprites/fx/_imports`: 1
- Total imports: **124**

## Queue / Archive State

- `assets/sprites/preview/import_queue/`: 0 files
- `assets/sprites/preview/source_archive/`: 1 file
  - `assets/sprites/preview/source_archive/bosses/dracula_final_fantasy_6_style.gif`

## Current Grid Audit (Imports)

- Imports audited: **124**
- Already on 16px grid: **81**
- Off-grid (not multiple of 16): **43**
- Prior direct padding action: `spr_boss_import_dracula_final_fantasy_6_style.png` from `567x399` to `576x400` (no resampling)

## Slice Then Pad Pass

Command used:

```bash
python tools/slice_imports_then_pad.py --off-grid-only --overwrite
```

Results:

- Off-grid imports processed: **43**
- Auto-sliced imports: **43**
- Manual-review imports: **0**
- Slices written: **2164**
- Padded slices: **2133**
- All generated slices are now 16-grid compliant (`off_grid_slice_count=0`).

Output locations:

- Slices: `assets/sprites/<category>/_slices/<source_stem>/`
- CSV report: `docs/reports/sprite_slice_pad_audit_2026-02-08.csv`
- Markdown report: `docs/reports/sprite_slice_pad_audit_2026-02-08.md`

Manual review items:

- None

## Notes

- Originals under `_imports` were not modified.
- Auto-slicing strategy uses explicit sheet-layout hints first, then alpha/background component extraction.
- Naming validation remains clean after this pass (`python tools/validate_naming.py assets/sprites` => `Invalid: 0`).
