# Runtime NW Log Audit Pass (2026-02-11)

## Scope
- Strengthen runtime smoke QA with actionable log diagnostics.
- Detect JS runtime exceptions and missing runtime assets/resources automatically.

## Tooling Added
- `tools/audit_nw_runtime_log.py`
  - Scans NW smoke logs for:
    - console exceptions (`TypeError`, `ReferenceError`, `SyntaxError`, `Uncaught`, `Error:`)
    - missing resources/files (`ERR_FILE_NOT_FOUND`, `Failed to load resource`, `ENOENT`)
    - fatal WebGL/gpu startup errors.
  - Filters known benign environment noise (for example, UPower/Widevine chatter).
- `tools/run_nw_playtest.sh`
  - Now invokes the log auditor automatically after each smoke run.
- `tools/README.md`
  - Added usage docs for NW log auditing.

## Validation
- `NW_RUNTIME_SECONDS=5 tools/run_nw_playtest.sh`
  - Smoke run stayed alive through timeout.
  - No fatal runtime findings.
  - Observed non-fatal VAAPI warnings in this environment.
- `python3 tools/audit_nw_runtime_log.py /tmp/nw_playtest_smoke.log`
  - Errors: `0`
  - Warnings: `3` (VAAPI backend availability; non-blocking for game runtime)
- `python3 tools/run_project_audit_gate.py --scope all`
  - Full pass maintained.

## Outcome
- NW smoke runs now include automatic runtime log diagnostics.
- Runtime-breaking issues should surface earlier without manual log inspection.
