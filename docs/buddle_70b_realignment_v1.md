# Buddle 70B Realignment — Two-Tier Local Model Plan (v1)

**Date:** 2026-06-06
**Owner:** HwaO + Tori (subagent-executed)
**Status:** Live (config swap + Celery restart complete)

## 1. Why we are downshifting Buddle to `llama3.3:70b` (Blanc)

The 2026-06-05 "Buddle = `llama3.1:405b`" assignment was correct in principle (heaviest local generalist available, 405B param frontier model) but proved unworkable in steady-state production:

- **Memory thrash on shared GPU:** 405B's 344 GB VRAM footprint forced eviction of every co-resident model on the Mac Studio. Concurrent inference alongside Mima (qwen3:30b, ~18 GB) and Pico (atom-astronomy-7b, ~5 GB) caused the Ollama runner to repeatedly swap weights, producing 10+ minute per-token-pass times and intermittent `lock_timeout` fallbacks in `InferenceScheduler`.
- **Loop incompatibility:** Our autowiki tick and `targeted_ads_miner.py` run on a 10-minute cadence with a 3-model jury (Buddle + Mima + Pico). 405B cold-load alone is ~120 s and the per-pass generation routinely exceeded the 240 s queue wait set in `inference_scheduler.py`, defeating the local-first design.
- **Empirically validated swap:** The 19:15 KST 2026-06-06 emergency switch to `llama3.3:70b` (Blanc) as a Buddle override (see `memory/2026-06-06.md`) confirmed the 70B fits comfortably with Mima + Pico, runs **~10× faster (5–10 s per token pass)** with **zero timeouts**, and is sufficient for the jury role (consensus voting + relaxed-prompt entailment).

## 2. The Two-Tier Local Model Strategy

| Tier | Role | Default Model | Footprint | Use |
|------|------|---------------|-----------|-----|
| **Tier 1 — Daily Generalist ("Buddle")** | Day-to-day jury/drafter, 10-min autowiki + miner loops | `llama3.3:70b` (Blanc) | 42 GB VRAM, ~30 s cold load, studio host | Default for all `NM_BUDDLE_MODEL` consumers |
| **Tier 2 — Heavy Weapon** | Reserved manual escalation only | `llama3.1:405b` | 344 GB VRAM, ~120 s cold load, pro host | On-demand only — single-shot deep reasoning, not on any cron |

**Disk preservation:** `llama3.1:405b` remains pulled and resident on Mac Studio's Ollama (`ollama list` continues to show it). It is **not** deleted. It is simply removed from the default `NM_BUDDLE_MODEL` slot and excluded from any auto-firing loop.

**Loop exclusion:** No scheduled task (Celery beat, cron, autowiki tick, `targeted_ads_miner.py`) will reference `llama3.1:405b`. Invocation must be explicit and human-initiated (e.g. a one-off `juror_spec` override in an ad-hoc script) so Papa always knows when the 405B cold-load tax is being paid.

**Inference scheduler:** `ModelFootprints.FOOTPRINTS` in `app/services/inference_scheduler.py` already enumerates both models with correct host/tier/VRAM/slots/cold-load values — no schema change required. The 70B routes to `studio` (port 11434), the 405B routes to `pro` (port 11435). The advisory lock + fallback logic continues to work for whichever model is requested.

## 3. Concrete expected gains

| Metric | Before (405B as Buddle) | After (70B as Buddle) | Delta |
|--------|-------------------------|------------------------|-------|
| VRAM occupancy on Mac Studio | ~344 GB (sole resident) | ~42 GB | **~302 GB freed** for Mima + Pico + headroom |
| Per-pass jury latency | 5–10 min (with thrash) | 5–10 s | **~60× faster steady-state, 10× faster typical** |
| Lock timeouts / circuit-breaker fallbacks per loop | 1–3 | 0 | **0 timeouts** measured 19:15 → 22:15 KST 2026-06-06 |
| Cold-load tax | ~120 s | ~30 s | 4× faster |
| Concurrent co-resident models supported | 1 (Buddle alone) | 3 (Buddle + Mima + Pico) | Full 3-model jury fits in VRAM simultaneously |

## 4. Changes shipped in this realignment

- `backend/.env`: `NM_BUDDLE_MODEL=llama3.1:405b` → `llama3.3:70b`
- `backend/app/config.py`: `BUDDLE_MODEL: str = "llama3.1:405b"` → `"llama3.3:70b"`
- `backend/app/services/inference_scheduler.py`: no edits required (both footprints already present)
- Celery services: `com.nebulamind.celery`, `com.nebulamind.celery-autowiki` reloaded via `launchctl` to pick up new env

## 5. Reversion path (if 70B proves insufficient)

If Tier-1 work demands frontier-tier quality, the path back is single-line:

```diff
- NM_BUDDLE_MODEL=llama3.3:70b
+ NM_BUDDLE_MODEL=llama3.1:405b
```

followed by `launchctl kickstart -k` of the two Celery agents. No code change. The 405B model remains on disk indefinitely.
