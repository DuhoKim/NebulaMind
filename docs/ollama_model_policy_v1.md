# Ollama Model Loading Policy — v1

**Status:** Draft for Papa review
**Author:** Kun (claude-opus-4-7)
**Date:** 2026-05-12
**Host:** Mac Studio M3 Ultra, 512 GB unified memory (32 cores: 24P + 8E)
**Backend repo:** `~/NebulaMind/NebulaMind/backend`
**Mirror copy:** `~/.openclaw/agents/kun/workspace/설계_OllamaModelPolicy_v1.md`

---

## 0. TL;DR

| Decision | Recommendation |
|---|---|
| **Resident set** | `astrosage-70b` + `deepseek-r1:14b` + `atom-astronomy-7b` (≈ 75 GB resident with capped ctx) |
| **On-demand set** | `llama3.3:70b`, `qwen3:30b`, `gemma3:27b`, `phi4:14b` (load → use → evict within minutes) |
| **`OLLAMA_KEEP_ALIVE`** | Change `-1` → `5m` system-wide; let app code pin the resident 3 via per-call `keep_alive=2h` |
| **`OLLAMA_MAX_LOADED_MODELS`** | Reduce `8` → `5` (caps worst-case to ~250 GB) |
| **`OLLAMA_NUM_PARALLEL`** | Keep `2` (allows concurrent autowiki tick + jury without queueing) |
| **Jury drain → 14b** | **Yes.** Replace the 4-model parallel fan-out with a single 14b call (+ Cerebras fallback). 4× faster, 10× cheaper RAM. |
| **Celery changes** | Rewrite `warm_models` to pin only the resident 3; add `num_ctx` to every Ollama call; simplify `STANCE_JURY_MODELS` |

**Safe RAM budget on 512 GB Mac Studio:** ≈ 440 GB usable (leave 72 GB for OS, FS cache, Postgres, Redis, Celery workers, sshd, etc.). The new policy targets a 60–80 GB resident baseline with up to ~180 GB peak (resident + 2 on-demand 70b-class). 60 % headroom is plenty.

---

## 1. Diagnosis — Why It Cascaded

### 1.1 Live state captured 2026-05-12 (post-emergency-unload)

```
$ ollama ps
NAME                              SIZE      CONTEXT    UNTIL
llama3.3:70b                      162 GB    131072     7 days from now
gemma3:27b                         42 GB    131072     7 days from now
phi4:14b                           19 GB     16384     7 days from now
astrosage-70b:latest               49 GB      8192     6 days from now
atom-astronomy-7b:latest          9.2 GB      4096     6 days from now
qwen3:30b                          71 GB    262144     27 minutes from now
deepseek-r1:14b                    82 GB    131072     Stopping...
                                  -----
                                  ≈434 GB
```

### 1.2 Three compounding root causes

**(a) `OLLAMA_KEEP_ALIVE=-1`.** Set at LaunchAgent level (`~/Library/LaunchAgents/ai.ollama.plist`). This pins every model that gets touched, forever — overriding any per-call `keep_alive` the application sets.

**(b) Default-context loads.** `qwen3:30b` weighs 18 GB on disk but loads at 71 GB resident because Ollama allocates the model's full default context (262 144 tokens). Same story for `deepseek-r1:14b` (9 GB → 82 GB at 131k ctx). KV-cache is the dominant cost, not weights.

**(c) Jury fan-out.** `STANCE_JURY_MODELS` in `app/agent_loop/tasks.py:96-101` lists 4 local models that run in parallel for every jury vote:
```python
qwen3:30b, gemma3:27b, deepseek-r1:14b, llama3.3:70b
```
Every jury batch wakes all four. With `KEEP_ALIVE=-1` they stay loaded forever. With each model carrying its full context, that's ≈ 357 GB tied up by jury alone.

**Conclusion:** The cascade wasn't bad luck. It's a load-bearing assumption that "Mac Studio has plenty of RAM" colliding with three unbounded multipliers (no eviction × no ctx cap × parallel fan-out).

---

## 2. Workload Inventory (what actually runs)

From `app/agent_loop/worker.py` `beat_schedule`:

| Task | Frequency | Models touched | Notes |
|---|---|---|---|
| `autowiki-tick` | 15 min (96/day) | `astrosage-70b` (proposer), `deepseek-r1:14b` (judge) | Gated by `autowiki:enabled` Redis flag |
| `wake-agents` (agent loop) | 5 min (288/day) | Groq cloud primary, Cerebras fallback. Local `llama3.3:70b` only if both cloud paths fail. | "Agent loop prefers cloud" per HwaO |
| `jury-fast-drain` | 30 min (48/day) | `llama3.3:70b` (jury_fast role) + Cerebras + Sambanova fallbacks | Lightweight task (stance JSON ≤ 200 char reason) |
| `drain-stance-jury-hourly` | hourly (24/day) | **all 4 of `STANCE_JURY_MODELS`** in parallel | The actual cascade trigger |
| `settle-evidence-reputation-hourly` | hourly | DB-only, no LLM | |
| `dispatch-jury-webhooks-hourly` | hourly | DB-only, no LLM | |
| `sweep-council-tiers-hourly` | hourly | DB-only, no LLM | |
| `warm-models-every-20min` | 20 min (72/day) | Pings 5 Studio models with `keep_alive=30m` | Currently warms too many |
| `sonnet-judge-tick` | 20 min | Claude API (not Ollama) | |
| `opus-judge-tick` | 60 min | Claude API (not Ollama) | |
| `rakon-deep-pass` | 6 h | `deepseek-r1:671b` on **Mac Pro** | No Studio RAM impact |
| Daily (arxiv, newsletter, coverage, etc.) | 1×/day | Various — mostly cloud or one-off Studio calls | Load briefly, evict |
| `curate-news-daily` | 1×/day | Groq cloud | |
| `adversarial-pass-daily` | 1×/day | `deepseek-r1:671b` (Pro), fallback `nutty` (Studio) | One short Studio burst |

**Only two tasks generate sustained Studio load:** `autowiki-tick` (every 15 min) and the four hourly jury/stance/council sweeps.

---

## 3. Resident Set — What Should Always Be Loaded

### 3.1 Selection criteria

A model belongs in the resident set if **all three** hold:
1. It is called by a task that runs at least **once per hour**.
2. Its load time (cold) is high relative to the inter-call gap (re-loading on every call would dominate latency).
3. Its capped-ctx resident footprint is < 10 % of available RAM.

### 3.2 Resident set (3 models, ≈ 75 GB resident)

| Model | Role | Capped ctx | Resident @ cap | Calls/day | Justification |
|---|---|---:|---:|---:|---|
| `astrosage-70b` | autowiki proposer / drafter | 8 192 | ≈ 49 GB | 96 | Already capped; autowiki-tick every 15 min; cold load ≈ 40 s; reloading 96×/day = 64 min wasted |
| `deepseek-r1:14b` | autowiki judge **and** new jury role | 8 192 | ≈ 15 GB | 96 (judge) + ≥ 24 (jury) | Drop from 131k → 8k ctx saves 67 GB; reasoning-tuned, good at structured JSON |
| `atom-astronomy-7b` | evidence scoring (Vanta Research astronomy SLM) | 4 096 | ≈ 9 GB | TBD per scoring policy | Tiny, fast, astronomy-specialised; cheap to keep resident even at low call rate |

**Resident total: ≈ 73 GB** = 14 % of 512 GB. Massive headroom.

### 3.3 Why these three and not others

- **`astrosage-70b`** is the only frontier-class astronomy-tuned model that's both fast (autowiki proposer) and astronomy-specific. Non-substitutable.
- **`deepseek-r1:14b`** doubles as judge + jury once the policy lands (see §6). Reasoning-tuned 14b is the sweet spot for both structured-output tasks. Cheapest reasoning model to keep warm.
- **`atom-astronomy-7b`** is a candidate, contingent on evidence-scoring actually calling it routinely. **Open question for Papa:** is the evidence scorer wired up yet? If not (current state: zero call sites found via `grep`), drop atom from resident set until it is. Until then, resident set is 2 models @ 64 GB.

---

## 4. On-Demand Set — Load → Use → Evict

| Model | Used by | Trigger | Eviction |
|---|---|---|---|
| `llama3.3:70b` (Blanc) | `writer`, `synthesis`, `arxivbot` (fallback), `query_gen` (last resort) | Daily batch tasks or cloud-path failure | `keep_alive=30s` |
| `qwen3:30b` (Mima) | `writer` (2nd), `commenter`, `query_gen` (primary), `renovation_synth` (disabled) | Hourly council/query bursts | `keep_alive=30s` |
| `gemma3:27b` (Tera) | `commenter` (primary), `query_gen` (2nd) | Daily | `keep_alive=30s` |
| `phi4:14b` (Takji) | `commenter` (2nd), `evidence_linker` (2nd) | Daily | `keep_alive=30s` |

**Pattern:** explicit short `keep_alive` on every call site, so Ollama drops the model 30 s after the last token. This matters because once `OLLAMA_KEEP_ALIVE=-1` is gone, **per-call `keep_alive` is the only knob.**

**Important nuance:** with the new `OLLAMA_KEEP_ALIVE=5m` default (§5), an on-demand model loaded by a one-off call will linger for 5 min unless the call explicitly passes `keep_alive=30s`. We want it to linger 5 min when a burst of similar calls is likely (e.g., council sweep doing 3 consecutive query-gen calls), but evict fast when it's a one-shot. **Default behaviour is good enough; only override to 30 s in the daily-batch tasks** that finish their work and don't expect repeat calls.

---

## 5. KEEP_ALIVE Recommendation

### 5.1 Change

```diff
# ~/Library/LaunchAgents/ai.ollama.plist  (or env at ollama serve)
-OLLAMA_KEEP_ALIVE=-1
+OLLAMA_KEEP_ALIVE=5m

-OLLAMA_MAX_LOADED_MODELS=8
+OLLAMA_MAX_LOADED_MODELS=5

 OLLAMA_NUM_PARALLEL=2          # unchanged
```

### 5.2 Why `5m` not `30s`

- The autowiki tick runs every 15 min. If `astrosage-70b` evicted between ticks, every tick pays a 40 s cold-load penalty.
- The resident-set pin (per-call `keep_alive=2h` from `warm_models`) handles the long-lived case.
- `5m` gives on-demand models a natural reuse window for adjacent calls (e.g., council does 3-4 queries in a row) without locking them forever.
- `30s` is too aggressive for non-resident models because hourly sweeps would never benefit from warm cache between adjacent claims.

### 5.3 Why `5` not `3` for MAX_LOADED

- Resident set is 3 (or 2 if we defer `atom-7b`).
- A hot hour: autowiki tick (uses astrosage + deepseek-r1:14b), then jury fires using deepseek-r1:14b (already resident), then a council sweep loads qwen3:30b on demand, then a `writer` call loads llama3.3:70b for one task.
- Peak occupancy: 3 resident + 2 on-demand = 5. Setting MAX_LOADED=5 caps blast radius without throttling normal flow. Setting MAX_LOADED=3 would force evicting astrosage to load llama3.3:70b — disastrous.

### 5.4 Why we keep `NUM_PARALLEL=2`

`NUM_PARALLEL` is per-model in-flight requests, not total. `2` lets one autowiki tick run while a jury vote arrives, without serialising them. Going to `1` would cause queue build-up during the :00 hourly sweeps.

---

## 6. Jury Drain — Replace 4-model Fan-out With Single 14b

### 6.1 Current

```python
# app/agent_loop/tasks.py:96-101
STANCE_JURY_MODELS = [
    {"model": "qwen3:30b"},
    {"model": "gemma3:27b"},
    {"model": "deepseek-r1:14b"},
    {"model": "llama3.3:70b"},
]
```

Every jury batch fires all four in parallel, expects at least 2 to succeed, takes the majority stance.

### 6.2 Problem

- The task is structured: `{"stance_correct": bool, "vote": -1|0|1, "reason": "≤200 char"}`. This is a **classification + short justification** problem, well within 14b capability.
- 4-way agreement on a 3-way categorical is statistical theatre when one of the four is a 162 GB elephant. The 70b doesn't disagree with the 14b on jury voting in any informative way the 14b couldn't catch alone — and the cost is 35× the RAM.
- Cold-load of all 4 from a fresh state takes 60-90 s of pure RAM thrashing.

### 6.3 New design

```python
STANCE_JURY_MODELS = [
    {"base_url": "http://localhost:11434/v1", "api_key": "ollama",
     "model": "deepseek-r1:14b", "label": "JuryDeepseek14b"},
]
STANCE_JURY_FALLBACKS = [
    # Used only if local 14b errors / times out — keeps service alive
    {"cerebras": "llama3.1-8b"},
    {"sambanova": "Meta-Llama-3.3-70B-Instruct"},
]
```

Also update `ROUTING["jury_fast"]` (in `app/services/llm_routing/routing.py:73-77`):

```diff
 "jury_fast": _compact([
-    _ollama(_STUDIO, "llama3.3:70b",     "blanc"),
+    _ollama(_STUDIO, "deepseek-r1:14b",  "nutty"),
     _cerebras("cerebras-fast"),
     _sambanova(),
 ]),
```

### 6.4 Risk + Mitigation

**Risk:** single-model jury loses ensemble robustness. A truly bad call from 14b is no longer caught by another LLM.

**Mitigation:**
- 14b reasoning is already the autowiki judge (validated by §11.3 of `autowiki_loop_v1.md`). Performance ceiling is known.
- **Spot-check policy:** every 10th jury vote, re-run on `qwen3:30b` (loaded on demand, 30 s warm window) and log disagreements. If disagreement rate > 15 % over a 200-vote window, escalate to Papa and revert.
- The cloud fallbacks (Cerebras, Sambanova) cover the failure case where 14b errors.

**Expected wins:**
- Jury RAM: 357 GB → 15 GB (when 14b is already resident).
- Jury latency: 60–90 s cold → 2–5 s warm.
- Cost: $0 (all fallbacks free-tier).

---

## 7. Celery Changes (Concrete)

### 7.1 `warm_models` — rewrite

```python
# app/agent_loop/tasks.py
@celery_app.task(name="app.agent_loop.tasks.warm_models")
def warm_models():
    """Keep resident-set models loaded. Runs every 20 min."""
    # Mac Pro (unchanged)
    _keep_alive_ollama("http://192.188.0.4:11434", "deepseek-r1:671b", "24h")  # Rakon
    _keep_alive_ollama("http://192.188.0.4:11434", "deepseek-r1:32b",  "2h")

    # Mac Studio — pin resident set only
    for model in ["astrosage-70b:latest", "deepseek-r1:14b"]:
        _keep_alive_ollama("http://localhost:11434", model, "2h")

    # Optional 3rd resident — gated on actual usage; flip via settings flag
    if settings.PIN_ATOM_ASTRONOMY_7B:
        _keep_alive_ollama("http://localhost:11434", "vanta-research/atom-astronomy-7b:latest", "2h")

    print("[warm_models] resident set pinned")
```

**Notable removals:** `llama3.3:70b` and `qwen3:30b` are NOT warmed any more. They load on demand via the routing fall-through.

### 7.2 `_keep_alive_ollama` — add `num_ctx`

Currently the keep-alive ping uses no `options`, so when Ollama loads the model it picks the default context. Force the cap:

```python
def _keep_alive_ollama(base_url: str, model: str, keep_alive: str = "24h",
                      num_ctx: int = 8192) -> None:
    """Ping Ollama to keep a model loaded in memory with capped context."""
    try:
        httpx.post(
            f"{base_url.rstrip('/').rstrip('/v1')}/api/generate",
            json={"model": model, "keep_alive": keep_alive, "prompt": "",
                  "options": {"num_ctx": num_ctx}},
            timeout=10,
        )
    except Exception:
        pass
```

**Why this matters:** without `num_ctx` here, the very first `warm_models` ping after Ollama restart will load `deepseek-r1:14b` with its 131k default, eating 82 GB. Passing `num_ctx=8192` keeps it at ~15 GB from the first second.

### 7.3 Universal `num_ctx` in chat helper

`_call_one_async` in `tasks.py:557` already does `"options": {"num_ctx": 8192}` for any ollama-api call — **good**, but verify all other call sites match. Check:

```bash
grep -rn '"model":.*"llama3\|"model":.*"qwen\|"model":.*"gemma\|"model":.*"phi\|"model":.*"deepseek\|"model":.*"astrosage\|"model":.*"atom"' app/ --include='*.py' \
  | grep -v num_ctx
```

Any line without `num_ctx` is a leak. Add `"options": {"num_ctx": 8192}` to each. (Found in `judge.py:135`, `judge.py:158`, `proposers.py:137`, `proposers.py:165`, `deep_synthesis.py:64`, `deep_synthesis.py:89` from this audit — verify each call has explicit `num_ctx`.)

### 7.4 Worker startup hook

Add to `worker.py` (or a Celery `worker_ready` signal):

```python
from celery.signals import worker_ready

@worker_ready.connect
def _evict_non_resident_on_boot(sender, **_kwargs):
    """On Celery worker boot, evict any non-resident Ollama model that survived a restart."""
    keep = {"astrosage-70b:latest", "deepseek-r1:14b"}
    if settings.PIN_ATOM_ASTRONOMY_7B:
        keep.add("vanta-research/atom-astronomy-7b:latest")
    try:
        loaded = httpx.get("http://localhost:11434/api/ps", timeout=5).json().get("models", [])
        for m in loaded:
            name = m.get("name") or m.get("model")
            if name and name not in keep:
                httpx.post("http://localhost:11434/api/generate",
                           json={"model": name, "keep_alive": 0}, timeout=5)
                print(f"[boot-evict] requested unload of {name}")
    except Exception as e:
        print(f"[boot-evict] skipped: {e}")
```

This guarantees that after a Celery restart, the runtime state matches the policy without waiting for `warm_models` (20 min) or organic eviction (5 min).

### 7.5 Config additions

```python
# app/config.py
PIN_ATOM_ASTRONOMY_7B: bool = False   # flip to True once evidence-scoring call site exists
OLLAMA_MAX_CTX_DEFAULT: int = 8192    # used by helpers
```

---

## 8. Rollout Plan

1. **Land Celery changes first** (warm_models rewrite, num_ctx audit, worker_ready hook, jury fan-out collapse). **No env-var changes yet.** Celery restart on Mac Studio.
2. **Observe one full hourly cycle** (60 min) with `KEEP_ALIVE=-1` still in place — confirm jury simplification produces same-quality votes (run the spot-check loop) and no task failures.
3. **Flip env vars** in `ai.ollama.plist`: `KEEP_ALIVE=5m`, `MAX_LOADED_MODELS=5`. Reload LaunchAgent.
4. **Force-evict everything except resident set** via the boot hook or a one-shot script.
5. **Watch for 24 h.** Track `ollama ps` every 30 min, total RAM, task failure rates.

### Rollback

If anything breaks: revert env vars (`KEEP_ALIVE=-1`, `MAX_LOADED=8`), `launchctl unload && load`. Celery code can stay — it's strictly safer than the old code regardless of env-var state.

---

## 9. Open Questions for Papa

1. **Atom-astronomy-7b**: should it be in the resident set, or kept on-demand until the evidence-scoring caller actually exists? (Default in draft: on-demand, flag-gated.)
2. **Jury single-model**: comfortable with 14b solo + cloud fallbacks, with the 10 % spot-check on 30b? (Reverts trivially if disagreement > 15 %.)
3. **Should `llama3.3:70b` be uninstalled** from Mac Studio entirely if the agent loop always uses Groq cloud? Saves 42 GB on disk. Or keep as cold standby for cloud-outage days?

---

## 10.5 arXiv Pipeline Model Assignments (Phase D addition — 2026-05-20)

| Step | Model | Nickname | Why |
|---|---|---|---|
| `paper_search.verify_for_claim` — LLM stance pre-judge | `deepseek-r1:14b` | Nutty | Called inside `verify_for_claim` via direct Ollama HTTP (`/api/generate`). R1 chain-of-thought reliably distinguishes supports/refutes/neutral from a claim + abstract excerpt. Heuristic fallback (`_stance_hint`) activates when Ollama is unavailable. |
| `process_pending_verify_retries` — re-verify after ADS lag | n/a (re-calls `verify_for_claim`) | — | Task itself is pure Python; the LLM call happens inside `verify_for_claim` → Nutty again. |
| `handle_page_extension` LLM draft | `ArxivBot` (`qwen2.5:7b` via `arxivbot` role) | ArxivBot | Unchanged from Phase C. |

**Call site:** `app/services/paper_search.py:_llm_stance_verify()` — Ollama at `http://localhost:11434/api/generate`, model `deepseek-r1:14b`, `num_ctx=4096`, `temperature=0`.

---

## 10. Platoon Assignment (per `feedback_platoon_assignment.md`)

| Step | Cron | Model owner | Why |
|---|---|---|---|
| autowiki proposer (every 15 min) | `astrosage-70b` (AstroSage) | astronomy-specialist 70b, fast token rate on M3 Ultra, sole capable proposer in stable |
| autowiki judge (every 15 min) | `deepseek-r1:14b` (Nutty) | reasoning-tuned, structured-JSON reliable, cheap to keep resident |
| jury drain (hourly) | `deepseek-r1:14b` (Nutty) | same model already pinned; classification + 200-char reason is well within 14b |
| jury fast drain (30 min) | `deepseek-r1:14b` (Nutty) → Cerebras fallback | replaces llama3.3:70b (Blanc); same task, smaller footprint |
| warm pings (20 min) | n/a — orchestration only | Celery worker |
| boot evict | n/a | Celery worker_ready signal |
| evidence scoring | `atom-astronomy-7b` (Tato) when wired | astronomy SLM, fast, on-demand pending caller |
| writer / synthesis (daily) | `llama3.3:70b` (Blanc) on-demand → Gemini/SambaNova fallback | best local quality when needed; tolerates 40 s cold-load for daily tasks |
| commenter / query_gen (daily) | `qwen3:30b` (Mima) on-demand | balanced; doesn't need to be resident |
| renovation synth (disabled) | n/a | old pipeline retired |
| Rakon deep pass (6h) | `deepseek-r1:671b` on **Mac Pro** | not Studio RAM |

---

## 11. Closing Note

The 437 GB cascade wasn't an emergent surprise — it was a foreseeable outcome of three orthogonal "be generous" defaults compounding. The policy here doesn't add complexity; it removes a `-1` from a plist and collapses one duplicated jury panel. The result is a smaller, more predictable, and easier-to-reason-about runtime, with most of the 512 GB of Mac Studio RAM **actually available** for things that need it (Postgres buffer pool, FS cache for the 50 GB+ wiki+claims+evidence dataset, future bigger models when Papa wants them resident).

—Kun
