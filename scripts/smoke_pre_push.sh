#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT/backend"

PY="${PYTHON:-.venv/bin/python}"

if [[ "$PY" == */* ]]; then
  if [[ ! -x "$PY" ]]; then
    echo "Python interpreter is not executable: $PY" >&2
    echo "Create backend/.venv, or run: PYTHON=/path/to/python scripts/smoke_pre_push.sh" >&2
    exit 127
  fi
elif ! command -v "$PY" >/dev/null 2>&1; then
  echo "Python interpreter is not executable: $PY" >&2
  echo "Create backend/.venv, or run: PYTHON=/path/to/python scripts/smoke_pre_push.sh" >&2
  exit 127
fi

"$PY" -m py_compile \
  app/agent_loop/tasks.py \
  app/agent_loop/worker.py \
  app/agent_loop/registry.py \
  app/services/model_canary.py \
  app/services/page_registry.py \
  app/services/pipeline_runs.py \
  app/utils/premium_dispatch.py

"$PY" - <<'PY'
from app.agent_loop.worker import celery_app, _SCHEDULE_NAMES_BY_TASK
from app.services.model_canary import platoon_canary_seats

assert celery_app.conf.beat_schedule["model-call-canary-daily"]["task"] == "app.services.model_canary.run_model_call_canary"
assert "app.agent_loop.tasks.arxiv_wiki_feed_daily" in _SCHEDULE_NAMES_BY_TASK
assert celery_app.conf.beat_schedule["autowiki-tick"]["task"] == "app.agent_loop.registry.dispatch_lane"
assert celery_app.conf.beat_schedule["autowiki-tick"]["kwargs"]["lane"] == "autowiki"
assert {seat.label for seat in platoon_canary_seats()} == {
    "Buddle", "Nutty", "Mima", "Tera", "Pico", "Vera", "Blanc", "Rakon-proxy"
}
PY

PAGE57_DEFAULT_PATTERN='PILOT_PAGE_ID|Query\(default=57\)|def .*page_id: int = 57|page_slug: str = "galaxy-evolution"'
if command -v rg >/dev/null 2>&1; then
  if rg -n "$PAGE57_DEFAULT_PATTERN" app --glob '!**/*.bak*'; then
    echo "Page registry grep gate failed: remove page-57 defaults from active app code." >&2
    exit 1
  fi
else
  if grep -RInE --exclude='*.bak*' "$PAGE57_DEFAULT_PATTERN" app; then
    echo "Page registry grep gate failed: remove page-57 defaults from active app code." >&2
    exit 1
  fi
fi

"$PY" -m pytest -q \
  tests/test_llm_utils.py \
  tests/test_validator_coverage.py \
  tests/test_arxiv_wiki_feed_v2_retrieval_filter.py \
  tests/test_arxiv_wiki_feed_v2_validate_elements.py \
  tests/test_arxiv_wiki_feed_v2_phase3_promote.py \
  tests/test_arxiv_wiki_feed_second_page_acceptance.py \
  tests/test_inference_scheduler_hardening.py
