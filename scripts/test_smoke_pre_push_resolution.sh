#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

MISSING_PY="/tmp/nebulamind-missing-python-$$"
set +e
OUTPUT=$(PYTHON="$MISSING_PY" scripts/smoke_pre_push.sh 2>&1)
STATUS=$?
set -e

if [ "$STATUS" -ne 127 ]; then
  echo "expected missing Python to exit 127, got $STATUS" >&2
  echo "$OUTPUT" >&2
  exit 1
fi

if [[ "$OUTPUT" != *"Python interpreter is not executable"* ]]; then
  echo "expected actionable Python interpreter error" >&2
  echo "$OUTPUT" >&2
  exit 1
fi

if [[ "$OUTPUT" != *"PYTHON=/path/to/python"* ]]; then
  echo "expected PYTHON override guidance" >&2
  echo "$OUTPUT" >&2
  exit 1
fi

if [[ "$OUTPUT" == *"line 9"* ]]; then
  echo "unexpected raw shell line-number failure leaked" >&2
  echo "$OUTPUT" >&2
  exit 1
fi

echo smoke_pre_push_resolution_ok
