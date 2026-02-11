#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
PROJECT_DIR="${1:-$ROOT_DIR}"
RUNTIME_SECONDS="${NW_RUNTIME_SECONDS:-45}"
LOG_PATH="${NW_LOG_PATH:-/tmp/nw_playtest_smoke.log}"
USER_DATA_DIR="${NW_USER_DATA_DIR:-/tmp/nw-playtest-$$}"

if ! command -v nw >/dev/null 2>&1; then
  echo "ERROR: 'nw' is not available in PATH."
  exit 2
fi

mkdir -p "$USER_DATA_DIR"
cleanup() {
  rm -rf "$USER_DATA_DIR"
}
trap cleanup EXIT

CMD=(
  nw
  "--user-data-dir=$USER_DATA_DIR"
  "--no-sandbox"
  "--ignore-gpu-blocklist"
  "--use-angle=swiftshader"
  "--enable-unsafe-swiftshader"
  "--enable-webgl"
  "--enable-logging=stderr"
  "--v=1"
  "$PROJECT_DIR"
)

echo "Running NW smoke playtest..."
echo "Project: $PROJECT_DIR"
echo "Log: $LOG_PATH"

if command -v timeout >/dev/null 2>&1; then
  set +e
  timeout "${RUNTIME_SECONDS}s" "${CMD[@]}" >"$LOG_PATH" 2>&1
  CODE=$?
  set -e
else
  set +e
  "${CMD[@]}" >"$LOG_PATH" 2>&1
  CODE=$?
  set -e
fi

FATAL_PATTERNS=(
  "Error: Your browser does not support WebGL."
  "TypeError:"
  "ReferenceError:"
  "Uncaught"
)

FAIL=0
for pattern in "${FATAL_PATTERNS[@]}"; do
  if rg -q "$pattern" "$LOG_PATH"; then
    echo "Detected runtime error pattern: $pattern"
    FAIL=1
  fi
done

if [[ -f "$ROOT_DIR/tools/audit_nw_runtime_log.py" ]]; then
  set +e
  python3 "$ROOT_DIR/tools/audit_nw_runtime_log.py" "$LOG_PATH"
  LOG_AUDIT_CODE=$?
  set -e
  if [[ "$LOG_AUDIT_CODE" -ne 0 ]]; then
    FAIL=1
  fi
fi

if [[ "$CODE" -eq 124 ]]; then
  echo "NW stayed alive for ${RUNTIME_SECONDS}s (timeout reached)."
elif [[ "$CODE" -eq 0 ]]; then
  echo "NW exited cleanly before timeout."
else
  echo "NW exited with code: $CODE"
  FAIL=1
fi

echo
echo "Key log lines:"
rg -n "CONSOLE|WebGL|TypeError|ReferenceError|Uncaught|Error:" "$LOG_PATH" | head -n 40 || true

if [[ "$FAIL" -ne 0 ]]; then
  echo
  echo "NW smoke playtest FAILED. See log: $LOG_PATH"
  exit 1
fi

echo
echo "NW smoke playtest PASSED."
