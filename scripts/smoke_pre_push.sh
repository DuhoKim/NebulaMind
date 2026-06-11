#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT/backend"

PY="${PYTHON:-.venv/bin/python}"

"$PY" -m py_compile \
  app/agent_loop/tasks.py \
  app/agent_loop/worker.py \
  app/services/model_canary.py \
  app/services/pipeline_runs.py \
  app/utils/premium_dispatch.py

"$PY" - <<'PY'
from app.agent_loop.worker import celery_app, _SCHEDULE_NAMES_BY_TASK
from app.services.model_canary import platoon_canary_seats

assert celery_app.conf.beat_schedule["model-call-canary-daily"]["task"] == "app.services.model_canary.run_model_call_canary"
assert "app.agent_loop.tasks.arxiv_wiki_feed_daily" in _SCHEDULE_NAMES_BY_TASK
assert "app.agent_loop.autowiki.tasks.autowiki_tick" in _SCHEDULE_NAMES_BY_TASK
assert {seat.label for seat in platoon_canary_seats()} == {
    "Buddle", "Nutty", "Mima", "Tera", "Pico", "Vera", "Blanc", "Rakon-proxy"
}
PY

"$PY" -m pytest -q \
  tests/test_llm_utils.py \
  tests/test_validator_coverage.py \
  tests/test_arxiv_wiki_feed_v2_retrieval_filter.py \
  tests/test_arxiv_wiki_feed_v2_validate_elements.py \
  tests/test_arxiv_wiki_feed_v2_phase3_promote.py \
  tests/test_arxiv_wiki_feed_second_page_acceptance.py \
  tests/test_inference_scheduler_hardening.py
