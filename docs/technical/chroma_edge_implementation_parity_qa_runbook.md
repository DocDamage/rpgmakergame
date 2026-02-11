# Chroma's Edge - Implementation Parity QA Runbook (v1)
## Encounter, Chest, and Drop Parity Validation for Palace and Endgame Loops

---

## 0) Scope

This runbook validates that implementation behavior matches current doc-layer tuning for:
- Palace interior encounter pacing
- Palace chest distribution
- Palace drop tables and pity safeguards
- Post-clear sanctum option gating

Primary references:
- `chroma_edge_dungeon_palace_interior_balance_pacing.md`
- `chroma_edge_dungeon_palace_interior_drop_tables.md`
- `chroma_edge_dungeon_palace_interior_map_sheet.md`
- `chroma_edge_final_palace_post_clear_voice_ui_barks.md`

---

## 1) Test Data and Setup

- Use a save at palace entry with stable combat instrumentation enabled.
- Enable event logging for:
  - encounter triggers
  - chest open events
  - enemy drops (primary and bonus roll detail)
  - flag mutation events
- Record RNG seed per run when available.
- Run the drop-table sum sanity helper before manual combat QA:
  - `powershell -ExecutionPolicy Bypass -File .\check_palace_drop_table_sums.ps1`
- Run the pacing/chest integrity preflight before manual route QA:
  - `powershell -ExecutionPolicy Bypass -File .\check_palace_pacing_integrity.ps1`

---

## 2) Encounter Pacing Parity

Target ranges from tuning doc:

| Map | Mandatory Battles Target | Full Sweep Target |
|-----|--------------------------|-------------------|
| Map 1 | 0-2 | 0-2 |
| Map 2 | 8-12 | 10-14 |
| Map 3 | 0 | 0-2 |
| Map 4 | 10-14 | 12-16 |
| Map 5 | 0 | 0 |
| Total | 18-28 | 22-34 |

Execution:
1. Run a direct-path route once (mandatory focus).
2. Run a full-clear route once (sweep focus).
3. Compare observed counts against target windows.

Pass criteria:
- Both route profiles remain inside target windows.
- No RNG encounters trigger in documented OFF zones.

---

## 3) Chest Placement Parity

Expected distribution:
- Map 1: 2 chests
- Map 2: 8 chests
- Map 3: 2 chests
- Map 4: 5 chests
- Map 5: 3 chests
- Total: 20 chests

Execution:
1. Traverse each map with fog reveal or debug map visibility.
2. Count spawned chest interactables and IDs.
3. Confirm no duplicate IDs and no inaccessible placements.

Pass criteria:
- Chest counts match expected distribution exactly.
- All required chest spots are reachable under intended route logic.

---

## 4) Drop Table Integrity

Validation checks:
1. Each enemy primary table sums to 100%.
2. Bonus roll is independent and executed separately from primary.
3. Elite behavior executes double primary plus one bonus.
4. Boss drops are fixed and always granted.
5. Optional modifiers apply only in documented conditions.

Specific system checks:
- Forge-Heavy modifier active only in map-4 conditions.
- Night modifier affects chrono wisps only.
- Protocol modifiers apply to intended enemy subsets.

Pass criteria:
- No table sum errors.
- No missing mandatory roll path.
- No condition bleed between modifier contexts.

---

## 5) Anti-Brick Safeguard Checks

### 5.1 Paradox pity counter

Expected behavior:
- `PALACE_PARADOX_STREAK` increments on wisp/auditor kills without paradox drop.
- At threshold, next qualifying kill guarantees paradox and resets streak.

Execution:
1. Force or replay controlled kills without paradox drops.
2. Verify streak increments each qualifying kill.
3. At threshold kill, verify forced paradox drop.
4. Verify streak reset after guaranteed drop.

### 5.2 Conversion recipes

Expected behavior:
- 6 alloy shards -> 1 alloy plate
- 8 seal wax scraps -> 1 paradox glass

Execution:
1. Seed inventory with exact recipe quantities.
2. Perform conversion.
3. Verify output and inventory decrement.

Pass criteria:
- Pity system cannot deadlock and always resolves at threshold.
- Both conversion recipes execute with exact ratios.

---

## 6) Post-Clear Sanctum Parity

Check dependencies:
- Base post-clear lines require `FINAL_PALACE_F5_CLEARED=TRUE`.
- Unfinished seams bark depends on vault clear triplet.
- Confluence return option depends on `ECLIPSE_CONFLUENCE_DISCOVERED=TRUE`.

Execution:
1. Enter sanctum with all vault flags false.
2. Confirm unfinished seams bark and unavailable confluence option if undiscovered.
3. Set discovered/cleared combinations and retest option and bark behavior.

Pass criteria:
- Voice/UI options strictly follow documented flag gates.
- No option appears prematurely.

---

## 7) Reporting Template

| Test Group | Case | Result | Notes | Defect ID |
|------------|------|--------|-------|-----------|
| Encounter Pacing | Direct path range |  |  |  |
| Encounter Pacing | Full sweep range |  |  |  |
| Chest Placement | Count and reachability |  |  |  |
| Drop Integrity | Table sums and rolls |  |  |  |
| Drop Integrity | Modifiers and contexts |  |  |  |
| Safeguards | Pity counter behavior |  |  |  |
| Safeguards | Conversion recipes |  |  |  |
| Post-Clear Sanctum | Voice/UI gate parity |  |  |  |

---

## 8) Exit Criteria

Implementation parity pass is complete when:
- All test groups pass, or
- Remaining fails are logged with owner, severity, and retest date.
