# Stub Systems Implementation Pass (2026-02-11)

## Scope
Implemented and enabled all previously disabled/stub systems in `js/plugins.js`:
- `ChromaEdge_SummonSystem`
- `ChromaEdge_DualLimitBreak`
- `ChromaEdge_DialogueTree`
- `ChromaEdge_DayNightSystem`
- `ChromaEdge_NPCScheduling`
- `ChromaEdge_MercyChoiceSystem`
- `ChromaEdge_TowerProgression`
- `ChromaEdge_EndingBranch`
- `ChromaEdge_AffinityMenu`

## What Was Added
- Save-persistent runtime state for each system in `Game_System`.
- Plugin commands for eventing for all nine systems.
- Script APIs under `ChromaEdge.*` namespaces for all nine systems.
- Core runtime hooks:
  - summon skill gating by owner/unlock
  - DLB skill gating by affinity/party/TP
  - dialogue scene + conditional response handling + ambient event auto-hook
  - day/night clock update + hour variable sync + map tint
  - NPC schedule application to tagged map events
  - mercy choice scoring and branch-ready metrics
  - tower floor unlock/clear logic + switch/flag sync
  - ending branch auto-evaluation + route persistence/switch sync
  - affinity menu scene + main menu command

## Plugin Enablement
Updated `js/plugins.js` to set all nine systems to `status:true` with explicit runtime parameters.

## Validation
```bash
python3 tools/run_project_audit_gate.py --scope all --strict
NW_RUNTIME_SECONDS=14 tools/run_nw_playtest.sh
```

Results:
- Audit gate: `37/37` pass.
- NW smoke: pass (no JS runtime errors); only non-fatal VAAPI environment warnings.

## Related Output
- Visual replacement backlog: `docs/reports/missing_image_backlog_2026-02-11.md`
