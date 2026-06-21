# Runtime Hygiene Report
Generated: 2026-06-21T11:19:00.715191+00:00
Classification: RUNTIME_HYGIENE_PARTIAL

## Issues
- evidence_votes_settled: fixed — sweep_council_tiers safety-net referenced stale evidence_votes.settled column and EvidenceVote.settled ORM attr; current schema stores settlement on Evidence.consensus_settled_at. Fix: Use Evidence.consensus_settled_at >= window to find recent settled evidence and fetch all EvidenceVote rows for trigger evaluation. No migration created.
- gemini_2_0_404: fixed — llm_routing._gemini hard-coded gemini-2.0-flash for OpenAI-compatible endpoint while other code already uses gemini-2.5-flash. Fix: Route generic Gemini fallback through BATCH_SAFE_DEFAULT_MODEL, currently gemini-2.5-flash. Gemini 2.5 Pro coherence path left unchanged.
- tera_readtimeout: parked_diagnosed — qwen3.6:27b-nvfp4 is present in local Ollama tags and configured in model footprints; Tera paths already use long 1800s timeouts for gap/coverage jobs. Observed ReadTimeout is more likely resource contention or prompt/model runtime saturation than model-name drift or too-short timeout. Fix: No code change. Recommend observing after Gemini/council noise reduction; if it repeats, add queue/skip policy for Tera when local heavy lock or Ollama ps shows active models.
- celery_descriptor_leak: instrumented — Exact descriptor leak not proven. InferenceScheduler keeps persistent async cloud HTTP clients per event loop; many loops or uncollected loops could increase open sockets over time. Fix: Added persistent_client_count() and warning when live persistent clients exceed threshold 8. Existing local Ollama generations already use fresh clients, so call semantics were not broadened.
- arxiv_id_normalization_followup: fixed_previous_same_tree — ADS identifier resolver strings could flow to Evidence.arxiv_id varchar(30). Fix: normalize_arxiv_id and tests remain included in current touched-file set; no new DB mutation.

## Checks
- pytest: 15 passed: backend/tests/test_runtime_hygiene.py backend/tests/test_inference_scheduler_hardening.py backend/tests/ccm/test_paper_search_ccm.py
- py_compile: passed for touched Python modules/tests
- api_health: HTTP 200 {status: ok, service: NebulaMind API, version: 0.2.0, pages: 44}
- stage2a_monitor: STAGE2A_MONITOR_NO_UPDATE; containment ok; evidence 11675/27096; page_versions 5780; Page57 candidate SHA live; Page58 unchanged; runtime enforce allow_partial false

## Runtime Actions
- db_writes: False
- page_or_evidence_mutation: False
- redis_flush_or_autowiki_enable: False
- service_restart: False

Restart recommendation: Restart Celery workers only after deploying these code changes so sweep_council_tiers, Gemini routing, and descriptor instrumentation load into worker memory. No immediate restart was performed.
