# Encounter Pacing Pass - 2026-02-10

## Scope
- Full-table pacing normalization across all encounter tables in `assets/data/encounters`.
- Goal: smoother act-to-act progression and lower grind pressure at gated story choke points.

## Files Updated
- `assets/data/encounters/encounter_capital.json`
- `assets/data/encounters/encounter_capital_threshold.json`
- `assets/data/encounters/encounter_chrono.json`
- `assets/data/encounters/encounter_d1_ruins.json`
- `assets/data/encounters/encounter_d2_fungal.json`
- `assets/data/encounters/encounter_dustbelt.json`
- `assets/data/encounters/encounter_ember.json`
- `assets/data/encounters/encounter_ember_trials.json`
- `assets/data/encounters/encounter_frost.json`
- `assets/data/encounters/encounter_frost_spire.json`
- `assets/data/encounters/encounter_mire.json`
- `assets/data/encounters/encounter_obsidian.json`
- `assets/data/encounters/encounter_obsidian_factory.json`
- `assets/data/encounters/encounter_prism.json`
- `assets/data/encounters/encounter_tide.json`
- `assets/data/encounters/encounter_tide_setpieces.json`
- `assets/data/encounters/encounter_uplands.json`
- `assets/data/encounters/encounter_uplands_story_route.json`
- `assets/data/encounters/encounter_void_nexus.json`

## Balancing Rules Applied
- Early-game zones keep moderate cadence (`~0.10-0.14`) with reduced early swarm spikes.
- Mid-game zones reduced from high-pressure cadence (`0.12-0.13`) to steadier pacing (`0.09-0.12`).
- Late-game zones reduced grind while preserving threat via composition, not frequency.
- Story setpiece tables now have lower encounter rates and wider step windows than adjacent free-roam tables.
- Rare 3-enemy spike packs had weight/xp trimmed where they distorted progression.

## Final Rate Snapshot
- `DUSTBELT_ENCOUNTERS`: `0.11`, steps `9-23`
- `UPLANDS_ENCOUNTERS`: `0.10`, steps `11-26`
- `MIRE_ENCOUNTERS`: `0.13`, steps `9-21`
- `PRISM_ENCOUNTERS`: `0.10`, steps `11-24`
- `D1_ENCOUNTERS`: `0.17`, steps `12-28`
- `D2_ENCOUNTERS`: `0.14`, steps `11-27`
- `EMBER_ENCOUNTERS`: `0.12`, steps `11-24`
- `TIDE_ENCOUNTERS`: `0.12`, steps `10-23`
- `OBSIDIAN_ENCOUNTERS`: `0.11`, steps `12-25`
- `FROST_ENCOUNTERS`: `0.10`, steps `13-27`
- `CHRONO_ENCOUNTERS`: `0.11`, steps `12-25`
- `CAPITAL_ENCOUNTERS`: `0.12`, steps `12-23`
- `UPLANDS_STORY_ROUTE_ENCOUNTERS`: `0.08`, steps `13-30`
- `EMBER_TRIAL_ENCOUNTERS`: `0.09`, steps `13-29`
- `TIDE_SETPIECE_ENCOUNTERS`: `0.10`, steps `12-27`
- `OBSIDIAN_FACTORY_ENCOUNTERS`: `0.09`, steps `13-28`
- `FROST_SPIRE_ENCOUNTERS`: `0.08`, steps `14-31`
- `VOID_NEXUS_ENCOUNTERS`: `0.09`, steps `13-31`
- `CAPITAL_THRESHOLD_ENCOUNTERS`: `0.08`, steps `15-34`

## Validation
- `python tools/validate_world_integrity.py` -> `Errors: 0`, `Warnings: 0`
- `python tools/validate_world_integrity.py --strict-gates` -> `Errors: 0`, `Warnings: 0`
- `python tools/validate_naming.py assets --validate-ids` -> `Invalid: 0`
- Full JSON parse sweep -> `721` valid, `0` invalid
