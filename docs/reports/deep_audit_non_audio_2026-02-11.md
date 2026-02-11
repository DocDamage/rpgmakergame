# Deep Project Audit (Non-Audio) (2026-02-11)

## Scope
This pass audits project cohesion/integrity/runtime readiness **excluding audio validation**.

### Explicitly excluded
- `tools/validate_runtime_audio_references.py`
- Any audio content quality review

## Audit Commands Executed
1. `python3 tools/validate_party_sprite_coverage.py --strict`
2. `python3 tools/validate_runtime_image_references.py --strict --strict-effects`
3. `python3 tools/validate_content_integrity.py --scope all --strict-map-npc-anchors --strict-mainline`
4. `python3 tools/audit_story_cohesion.py --scope all --strict-act-gating --strict-npc-anchors`
5. `python3 tools/audit_quest_route_pacing.py --scope all --strict`
6. `python3 tools/validate_runtime_map_bridge.py --strict`
7. `python3 tools/validate_runtime_transfer_contract.py --strict`
8. `python3 tools/validate_runtime_world_dressing.py --warn-surplus --strict`
9. `python3 tools/validate_world_integrity.py --strict-gates`
10. `python3 tools/audit_environment_sprite_coverage.py --strict-candidates --strict-world-dressing`
11. JS syntax sweep: `node --check` across all `js/**/*.js`
12. Runtime smoke: `NW_RUNTIME_SECONDS=16 tools/run_nw_playtest.sh`

## Result Summary
- Total checks: **12**
- Passed: **12**
- Failed: **0**
- Overall status: **PASS (non-audio hard gate)**

Raw artifacts:
- `docs/reports/artifacts/non_audio_deep_audit_2026-02-11/summary.tsv`
- `docs/reports/artifacts/non_audio_deep_audit_2026-02-11/*.log`

## Cohesion and Story Findings
- Story cohesion (`scope=all`) passed with:
  - Maps scanned: **98**
  - Quests scanned: **251**
  - Steps scanned: **816**
  - Errors/Warnings: **0/0**
- Quest route pacing (`scope=all`) passed with:
  - Quest packs: **5**
  - Quests with locations: **251**
  - Quest transitions checked: **113**
  - First-target overworld checks: **251**
  - Errors/Warnings: **0/0**

Conclusion: Mainline and side-story progression are internally consistent in current canonical/runtime data.

## Runtime/Data Integrity Findings
- Content integrity passed in strict mode (errors/warnings: **0/0**).
- World integrity passed with strict gate token checking (errors/warnings: **0/0**).
- Runtime map bridge passed (errors/warnings: **0/0**).
- Runtime transfer contract passed with perfect parity:
  - Canonical maps: **98**
  - Runtime maps validated: **98**
  - Expected transfers: **265**
  - Actual transfer events: **265**
- Runtime world dressing passed with perfect parity:
  - Expected tags: **354**
  - Actual tags: **354**

Conclusion: Canonical data and runtime export are synchronized for map graph, transfers, and world-dressing anchors.

## Sprite / Environment Coverage Findings
- Party sprite coverage strict pass:
  - Actors checked: **13**
  - Overworld sheets: **26**
  - SV sheets: **26**
  - Errors/Warnings: **0/0**
- Runtime image reference validation strict pass:
  - References scanned: **188**
  - Unique references: **174**
  - Errors/Warnings: **0/0**
- Environment sprite coverage strict pass:
  - Maps scanned: **98**
  - Towns scanned: **14**
  - Tilesets referenced by maps: **16**
  - Tilesets with source PNGs/READMEs/curation candidates: **16/16/16**
  - Errors/Warnings: **0/0**

Conclusion: Required runtime image bindings and environment sprite source coverage are complete.

## JS/Runtime Engine Findings
- JS syntax sweep passed for **26** JS files.
- NW smoke playtest passed; no runtime error findings.
- NW log had **3 VAAPI warnings** (environmental GPU/video accel warnings), non-blocking.

## Remaining Non-Audio Risks (Quality, not runtime blockers)
No hard non-audio integrity failures were found. Remaining work is production-art quality replacement of placeholder runtime images already cataloged in:
- `docs/reports/missing_asset_descriptions_non_audio_2026-02-11.md`
- `docs/reports/missing_image_backlog_2026-02-11.md`

These are visual polish gaps, not cohesion/runtime validity failures.
