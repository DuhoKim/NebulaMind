# InferenceScheduler Socket-Level Hang Postmortem + Harness-1 Platoon Assessment v1

**Date:** 2026-06-10
**Owner:** Kun (architect) → HwaO (review) → Tori (implementer)
**Status:** Design — pre-implementation
**Incident:** Page 57 Campaign r5 (PID 44871), galaxy-evolution full-page mine, froze at **04:16 KST 2026-06-10**, manually terminated at **06:45 KST** (~149 minutes wedged past the 480 s watchdog budget).
**Related docs:** `platoon_realignment_v2.md`, `jury_system_upgrade_v1.md`, `ollama_model_policy_v1.md`, `targeted_ads_miner_stalling_audit_v1.md`.

---

## 0. TL;DR

1. The hang was **not** a single bug. It was a four-layer failure: (a) httpx per-chunk read timeout is not a wall-clock budget; (b) `asyncio.wait_for` propagated `CancelledError` into a coroutine whose `finally` block then blocked on `asyncio.to_thread(redis.delete, …)` against a saturated Redis; (c) `asyncio.gather` of three jurors meant one wedged cleanup wedged the whole jury; (d) no page-level kill switch caught it.
2. The fix is a **five-layer hardening of the inference path**: hard wall-clock timeout, Ollama preflight, shielded-and-deadlined cleanup, page-level kill switch, and connection-pool discipline. Plus a circuit-breaker on `ollama:health` to stop sending traffic to a host that has already started failing.
3. **Harness-1** (UIUC/UC Berkeley/Chroma, gpt-oss-20b base, "Stateful Cognitive Offloading") is **architecturally aligned with NebulaMind's direction** but should not be dropped in as a model swap. **Recommendation: hybrid A + C, staged over 4 phases.** Build the harness-shim first (Phase 1), pilot the paradigm on Kun (Phase 2), then deploy a 20B "Helix" platoon member specifically as an arXiv evidence retriever (Phase 3), and only rotate it into the jury seat if it beats Nutty-Heavy on a held-out evaluation set (Phase 4).
4. **Do not block fix-1 on Harness-1.** They are independent. Tori implements the scheduler fix in Sprint 1. Kun + HwaO design the harness shim in Sprint 2.

---

## 1. Incident Reconstruction (04:16 → 06:45 KST)

### 1.1 Observed log tail
`backend/logs/galev_fullpage_mine_r5.log` (last 4 lines, all dated 04:16 KST):

```
[InferenceScheduler] Lock acquisition timed out for deepseek-r1:70b after 30s. Tripping circuit breaker and falling back.
[InferenceScheduler] Fallback triggered for deepseek-r1:70b. Reason: lock_timeout
[InferenceScheduler] Local execution of qwen3:30b failed: . Executing fallback.
[InferenceScheduler] Fallback triggered for qwen3:30b. Reason: execution_error: 
```

Notable: no `Released lock` message; no `watchdog cancellation` message; no third juror outcome (Atom-7B). The process never logged anything else for **149 minutes** until SIGTERM at 06:45 KST.

### 1.2 Failure path (annotated)

For one jury call (`backend/scripts/targeted_ads_miner.py:629-650`):

```python
content = await asyncio.wait_for(
    scheduler.execute(model, prompt, JURY_TIMEOUT_SECONDS, system_prompt=JURY_SYSTEM_PROMPT),
    timeout=JURY_TIMEOUT_SECONDS + 120,   # 480 s outer watchdog
)
```

Three jurors are dispatched in parallel via `asyncio.gather(*calls)` in `run_jury_async` (line 691). Two of the three logged their fallback within seconds of 04:16:01. The third must therefore be the wedge.

`scheduler.execute()` in `backend/app/services/inference_scheduler.py:133-219`:

1. **Lines 153-170 — host_online preflight.** Reads `ollama:health` from Redis. The check is **stale** by design: it reports state at the last healthchecker tick, not at this moment. Ollama's `pull_qwen3_api.log` and `pull_llama3_api.log` (in `~/NebulaMind/logs/`) show silent runner restarts around 04:14–04:18 KST. `ollama:health.local_online` was still `true` at the moment `execute()` ran, so we proceeded.
2. **Lines 173-205 — advisory lock.** All three jurors race `ollama:lock:studio:heavy`. Comment on line 203 says "after 30s" but the loop uses `while time.time() - start_time < 180`. The drift is a separate code-comment bug, but the relevant point here is: under saturated Redis, `r.set(lock_key, "1", ex=ttl, nx=True)` via `asyncio.to_thread` can block on the Redis socket up to its `socket_timeout=5.0`. A 5-second blocked thread is a 5-second yield gap on the event loop. With three concurrent jurors each retrying with backoff, the event loop spends most of its time blocked in `to_thread`-served Redis calls.
3. **Lines 207-219 — try / except / finally.** This is the failure crucible.

   ```python
   try:
       return await self._make_http_call(...)
   except Exception as e:
       return await self._execute_fallback(...)
   finally:
       if acquired and r:
           try:
               await asyncio.to_thread(r.delete, lock_key)
           except Exception as e:
               logger.warning(...)
   ```

   When the outer `asyncio.wait_for(..., 480)` fires, Python injects `CancelledError` into the running coroutine. **Cancellation enters the `finally` block.** The `finally` then does `await asyncio.to_thread(r.delete, lock_key)`. If Redis is wedged, this `to_thread` blocks on the OS thread that holds it. **`asyncio` cannot cancel a thread that is mid-syscall on a TCP socket.** The cleanup task hangs, the cancellation never completes, the outer `wait_for` never raises, the `gather` never returns.

4. **Lines 261-318 — `_make_http_call`.** Three independent bugs sit here:
   - **Bug A (per-chunk vs wall-clock).** `client.post(url, …, timeout=timeout)` with `timeout=360` (int) constructs `httpx.Timeout(connect=360, read=360, write=360, pool=360)`. `read=360` means "if no byte arrives for 360 s." If Ollama drips one byte every 359 s before crashing, the read does not raise. There is **no total elapsed budget on the call itself**.
   - **Bug B (per-call client lifecycle).** `async with httpx.AsyncClient() as client` is created and torn down per call. No keepalive pool. Each call must do a fresh TCP three-way handshake on `localhost:11434`. If the kernel queues an `accept()` to a freshly-restarted Ollama before the listener is bound, the SYN can stall in the listen queue for the kernel's full `tcp_keepidle` (default ~2 h on macOS).
   - **Bug C (no socket keepalive).** No `SO_KEEPALIVE` is set on the underlying transport. macOS will hold a half-open localhost socket for the kernel keepalive interval — well past any pipeline-relevant timescale.

### 1.3 Root-cause statement

> **The 480-second watchdog cannot rescue a task whose `finally` cleanup blocks on a Redis socket that is itself queued behind a saturated Ollama host. `asyncio.wait_for` delivers `CancelledError`; the coroutine accepts it; the `finally` then makes an uncancellable blocking syscall via `asyncio.to_thread`; the event loop is starved; the page never advances.**

The reason **149 minutes** passed without progress (not 480 s, not 600 s) is that this wedge has no upstream bound. The Celery task does not enforce a hard page-level deadline. SIGTERM was the only release.

### 1.4 Why "socket-level" is the right framing

Although the proximate code path is in the lock-cleanup `finally`, the underlying enabler is the absence of socket-level discipline at every layer that touches a TCP connection (Ollama HTTP, Redis, Gemini fallback). All three use the same default macOS keepalive behavior. **One half-open socket plus one `to_thread` cleanup is sufficient to wedge the entire jury.** Fixing only the cleanup hides the same class of bug in other code paths (citation_context miner, autowiki worker — both call `InferenceScheduler`).

---

## 2. Architectural Fix — Five-Layer Hardening

The goal: **no inference path can wedge the event loop for more than a bounded, declared budget.** Failure must be loud, fast, and observable.

### 2.1 Layer 1 — Wall-clock timeout on the actual HTTP call

Replace `client.post(..., timeout=timeout)` with an explicit total budget. In `_make_http_call`:

```python
TIMEOUT_CONFIG = httpx.Timeout(
    connect=2.0,
    read=30.0,           # gap between bytes; not total
    write=10.0,
    pool=2.0,
)

async with httpx.AsyncClient(
    timeout=TIMEOUT_CONFIG,
    limits=httpx.Limits(max_connections=8, max_keepalive_connections=0),
) as client:
    response = await asyncio.wait_for(
        client.post(url, headers=headers, json=payload),
        timeout=timeout,   # the caller-declared wall-clock budget
    )
```

Rationale:
- `connect=2.0` distinguishes "Ollama not listening" from "Ollama thinking" in 2 s, not 360.
- `read=30.0` catches Ollama-crashed-mid-stream in 30 s.
- `max_keepalive_connections=0` for localhost prevents reuse of a stale half-open connection from a previous Ollama restart.
- The outer `asyncio.wait_for(..., timeout=timeout)` is the wall-clock hard stop. With caller-supplied `timeout=360`, the entire HTTP exchange must complete in 360 s of real time, byte-arrival pattern be damned.

### 2.2 Layer 2 — Ollama preflight (lightweight, ~50 ms)

Before acquiring the advisory lock for a heavy/medium-tier model, hit `GET /api/tags` with a 500 ms budget. If it fails, skip the lock entirely and go to fallback. Costs ~50 ms on the happy path, saves 30 s of futile lock-acquisition retries when Ollama is dead.

```python
async def _ollama_preflight(self, host: str, timeout_s: float = 0.5) -> bool:
    base = ModelFootprints.HOSTS[host]
    try:
        async with httpx.AsyncClient(timeout=httpx.Timeout(connect=0.3, read=timeout_s, write=0.3, pool=0.3)) as c:
            r = await c.get(f"{base.rstrip('/v1')}/api/tags")
            return r.status_code == 200
    except Exception:
        return False
```

Insert in `execute()` between the `ollama:health` Redis check and the lock acquisition. If `False`, skip lock and call `_execute_fallback(reason="preflight_failed")`. **Also update `ollama:health` immediately to reflect the live observation**, which feeds Layer 4's circuit breaker.

### 2.3 Layer 3 — Shielded, deadlined cleanup

Rewrite the `finally` block so cleanup cannot wedge:

```python
finally:
    if acquired and r:
        try:
            await asyncio.wait_for(
                asyncio.shield(asyncio.to_thread(r.delete, lock_key)),
                timeout=2.0,
            )
        except asyncio.TimeoutError:
            logger.warning(f"[InferenceScheduler] Lock {lock_key} delete timed out; leaking lock TTL={ttl}s")
        except Exception as e:
            logger.warning(f"[InferenceScheduler] Failed to release lock {lock_key}: {e}")
```

Two behaviours:
- **`asyncio.shield`** protects the delete from being re-cancelled if the parent task is already in the middle of a cancellation pass. We want cleanup to either succeed or time out cleanly.
- **`wait_for(..., 2.0)`** bounds the cleanup. If Redis is wedged, we leak the lock — but the lock has a TTL of `cold_load + timeout`, so it self-expires. We log the leak and move on. **The parent coroutine can now propagate its `CancelledError` to completion.**

The same pattern applies anywhere `asyncio.to_thread` runs Redis or filesystem work inside an exception-handling path.

### 2.4 Layer 4 — Page-level kill switch + circuit breaker

In `targeted_ads_miner.py` `run_jury_async` (line 687), wrap the gather in a hard deadline:

```python
async def run_jury_async(claim: Claim | ClaimSnapshot, record: PaperRecord) -> list[dict[str, Any]]:
    prompt = user_prompt(claim, record)
    PAGE_HARD_DEADLINE = JURY_TIMEOUT_SECONDS + 240   # 600 s — never exceed this per claim
    async with httpx.AsyncClient() as client:
        calls = [_call_juror(client, model, prompt) for model in jury_models()]
        try:
            async with asyncio.timeout(PAGE_HARD_DEADLINE):
                results = await asyncio.gather(*calls, return_exceptions=True)
        except TimeoutError:
            print(f"jury HARD DEADLINE {PAGE_HARD_DEADLINE}s exceeded — abandoning claim")
            return []
    return [r for r in results if isinstance(r, dict) and r]
```

Notes:
- `asyncio.timeout()` (Python 3.11+) is preferable to `wait_for` because it cancels the whole `gather` cleanly.
- `return_exceptions=True` prevents one wedged juror from poisoning the others' results — we get back what we can.
- `PAGE_HARD_DEADLINE = 600s` is the **absolute upper bound** any single claim can consume. No matter what hangs inside, the page advances within 10 minutes per claim.

Companion circuit breaker on `ollama:health`:

```python
# After 3 consecutive failures (lock_timeout, preflight_failed, execution_error)
# within a 60s window on a host, mark host_down=true with a 300s TTL.
# All subsequent scheduler.execute() calls for that host skip straight to fallback.
```

Implement as a Redis key `ollama:circuit:{host}` with a 300 s TTL; increment a separate `ollama:fails:{host}` counter with a 60 s TTL; on 3+ fails, set the circuit key. The `ollama:health` Redis layer already exists; the new keys live alongside it.

### 2.5 Layer 5 — Connection-pool discipline + socket keepalive

Stop creating `httpx.AsyncClient` per call. Inject one client per page run, with:

```python
transport = httpx.AsyncHTTPTransport(
    retries=0,
    verify=False,         # localhost only
    socket_options=[
        (socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1),
        (socket.IPPROTO_TCP, 0x10, 30),    # TCP_KEEPALIVE on macOS, 30s
    ],
)

client = httpx.AsyncClient(
    transport=transport,
    timeout=TIMEOUT_CONFIG,
    limits=httpx.Limits(max_connections=8, max_keepalive_connections=0),
)
```

For Gemini (cloud) calls, a separate client with `verify=True`, normal TCP_KEEPALIVE, and `max_keepalive_connections=4` is appropriate. The cloud and local paths should not share a transport.

### 2.6 Behavioral contract after the fix

| Failure mode | Detection latency | Wall-clock budget consumed |
|---|---|---|
| Ollama listener down | 2 s (preflight) | ≤ 2 s before fallback |
| Ollama mid-stream crash | 30 s (read gap) | ≤ 30 s before fallback |
| Redis socket wedged | 2 s (shielded cleanup) | ≤ 2 s; lock TTL-expires |
| One juror lock-times-out | 30 s (lock loop, post-fix) | other two jurors unaffected |
| Gemini DNS / TLS stuck | 360 s (wall-clock wait_for) | hard cap |
| All three jurors stuck | 600 s (page hard deadline) | hard cap; claim abandoned |
| Host has 3 fails in 60 s | next call (circuit open) | immediate fallback for 300 s |

**Worst case end-to-end per claim: 600 s. Previously: unbounded.**

### 2.7 Code change footprint

| File | Change | Risk |
|---|---|---|
| `app/services/inference_scheduler.py` | preflight, shielded cleanup, wall-clock timeout in `_make_http_call`, connection pooling, circuit-breaker keys | Medium — central path, but each layer is independently testable |
| `scripts/targeted_ads_miner.py` | page hard deadline around `gather`, `return_exceptions=True` | Low |
| `app/agent_loop/citation_context/miner.py` | same hardening (it's another caller) | Low |
| `app/agent_loop/citation_context/dynamic_miner.py` | same | Low |
| `app/agent_loop/tasks.py` | same | Low |
| New: `app/services/scheduler_circuit.py` | small helper for the circuit-breaker keys | Low — pure utility |

### 2.8 Test plan

1. **Synthetic Ollama crash test.** Mock httpx transport that accepts the connection, returns 1 byte, then sleeps forever. Verify scheduler returns `None` or falls back in ≤ 60 s (was: never).
2. **Saturated Redis test.** Inject a 30 s sleep on `r.delete`. Verify cleanup gives up at 2 s and the coroutine returns. (Was: indefinite wedge.)
3. **Three-juror gather race.** Spin up 3 jurors where juror[1] takes 10 s, juror[2] takes 60 s, juror[3] takes 700 s. Verify the page deadline at 600 s cancels juror[3] and returns juror[1]+juror[2]'s results.
4. **Circuit breaker exercise.** Force 3 failures on `studio` within 60 s. Verify the 4th call skips the lock entirely. Verify recovery after 300 s.
5. **Replay the Page 57 r5 incident.** Inject the exact log sequence (lock_timeout + execution_error: "") + a stuck Ollama; verify the page advances within 600 s.

### 2.9 Observability hooks

Add structured log lines (not just `print`) for each layer's outcome — they become the primary debugging surface next time:

```
sched.preflight host=studio ok=true latency_ms=42
sched.lock host=studio model=deepseek-r1:70b acquired=true wait_ms=180
sched.execute model=deepseek-r1:70b host=studio tier=heavy elapsed_s=24.1 ok=true
sched.fallback from=deepseek-r1:70b to=gemini-2.5-flash reason=lock_timeout
sched.cleanup lock=ollama:lock:studio:heavy released=true latency_ms=3
sched.circuit host=studio state=open fails=3 ttl_s=300
jury.page_deadline claim_id=2068 elapsed_s=600.2 status=abandoned
```

These are cheap, line-discoverable, and survive log rotation. Add a one-off `tools/sched_log_analyzer.py` that summarises `sched.*` lines into per-host fail rates — useful for HwaO's daily ops.

---

## 3. Harness-1 Assessment

### 3.1 The paper in one paragraph

Harness-1 (UIUC, UC Berkeley, Chroma, 2026) is an open-source agentic search agent built on `gpt-oss-20b`. Headline result: it outperforms GPT-5.4 and Claude 3.5 Sonnet on agentic search benchmarks while using **~4,400 SFT + RL trajectories** (compared to hundreds of thousands for legacy retrieval agents). The architectural primitive is **Stateful Cognitive Offloading**: the LLM never holds long-horizon agent state in its own context window. A separate **Stateful Search Harness** owns query history, evidence stack, citation graph, validation flags, and "what have I verified" bookkeeping. Each LLM turn receives a minimal delta — typically a single question of the form "given the current evidence stack, what should you query next?" or "does evidence E support claim C?" — and returns a structured action. The harness applies the action, mutates state, and decides the next turn.

The mental model: the LLM is a **policy network over a state-machine**, not a stateful agent in its own right.

### 3.2 Why this is interesting to NebulaMind specifically

NebulaMind already runs an evidence-verification pipeline that conceptually maps to this paradigm:

| Harness-1 component | NebulaMind equivalent | Current state |
|---|---|---|
| Stateful Search Harness | Claim Marker Persistence + Dynamic Citations + Citation Context Mining | Built, in production |
| Query history / evidence stack | `targeted_ads_miner.py` candidate list + ADS search results | Built |
| Validation flags | `claims.stance`, `claims.confidence`, jury votes | Built |
| LLM "reasoning policy" | Mima + Nutty-Heavy + Atom-7B 3-model jury | Built, runs full context per call |
| RL trajectory store | (none) | Missing — we have logs but no labeled trajectories |

The gap is in **how we feed the LLMs**. Today we stuff the entire claim text + entire abstract + entire system prompt into each juror's context every call. Each juror is independent and reads no history. We pay the full context tax on every call and we cannot do long-horizon reasoning across claims.

Harness-1's paradigm says: **feed only the delta**. Track state externally. Ask one focused question per turn.

### 3.3 Three integration options

#### Option A — Add as new platoon member ("Helix")

- Pull `gpt-oss-20b` to Mac Studio (~12 GB Q4_K_M).
- Build the Stateful Search Harness wrapper to mediate every call.
- Role: dedicated **arXiv evidence retrieval agent** for borderline claims (where the jury votes ABSTAIN×3 and would normally trigger an escalation to Rakon or simply commit-as-neutral).
- Fits in the existing Mac Studio RAM budget: jury (Mima 18 + Nutty-Heavy 42 + Pico 5 = 65 GB) + Helix 12 GB = 77 GB. Comfortable.
- Does **not** share `ollama:lock:studio:heavy` because it is light-tier; runs concurrent with the jury.

**Pros:** open-weights, hardware fits, slots into the highest-leverage gap (borderline-claim recovery).
**Cons:** building the harness wrapper is the real work, not pulling the model. The paper's RL/SFT trajectory data is general-purpose; for astronomy-specific behavior we need ~4,000 astronomy trajectories — they can be **bootstrapped from existing jury logs + ADS query history**, but cleaning + labeling is 1–2 weeks.
**Effort:** 4–6 weeks engineering + 2 weeks data prep.

#### Option B — Substitute for an existing platoon member

Candidates we considered:

| Existing member | Substitute with Helix? | Verdict |
|---|---|---|
| Nutty-Heavy (deepseek-r1:70b, jury heavy seat) | Possible after Phase 4 evaluation | **Conditional adopt** — only if Helix beats Nutty-Heavy on a held-out claim entailment benchmark |
| Atom-7B (astronomy scorer) | No | Different role (volume scoring vs. agentic retrieval); Atom-7B is astronomy-fine-tuned, Helix is general |
| Mima (qwen3:30b general scorer) | No | Different role; Mima handles non-astronomy too |
| Buddle (llama3.3:70b general drafter) | No | Different role (long-form drafting) |

The only candidate is Nutty-Heavy, and only conditionally on benchmark results. **Do not commit to substitution before measurement.**

#### Option C — Import the Stateful Cognitive Offloading paradigm into Tori/Kun

Don't pull a new model — instead wrap Claude calls in a Stateful Reasoning Harness. Each Tori/Kun turn gets:
- The current page-level state delta (what changed since last turn).
- A single focused question.
- A structured action schema as the expected reply.

**Pros:**
- Immediate token reduction → cheaper Opus turns for Kun, currently the biggest API line item.
- Better long-horizon behavior on multi-step design jobs.
- No new model to maintain.

**Cons:**
- Claude already has Memory + context management features; some overlap.
- Requires engineering on the harness layer, but that's the same layer Option A needs anyway.

**Effort:** 3–4 weeks (sharing the harness shim with Option A).

### 3.4 Comparison matrix

| Dimension | A: Add Helix | B: Substitute | C: Paradigm only |
|---|---|---|---|
| Capability gain | High (new retrieval agent) | Conditional (must beat Nutty-Heavy) | Medium (Kun/Tori better at long-horizon) |
| Risk | Medium (new model, harness build) | High (regression on jury) | Low (additive wrapper) |
| Cost (engineering) | 4–6 wk + 2 wk data | 1–2 wk after A | 3–4 wk (shared with A) |
| Cost (operational) | Free (local) | Free (local) | Token-cost reduction |
| Reversibility | High (just unload model) | Low after rollout | High |
| Time to first signal | 6–8 wk | 8–10 wk after A | 4–5 wk |

### 3.5 Recommendation — Hybrid A + C, staged in 4 phases

Build the harness shim once, get value from it in two places, defer the substitution decision until we have data.

| Phase | Duration | Owner | Deliverable | Gate to next phase |
|---|---|---|---|---|
| **1. Shim** | 2–3 wk | Tori implementer, Kun designer | `app/services/cognitive_harness/` — generic external state store: `query_log`, `evidence_stack`, `validation_state`, `next_action_context`. Backed by Redis + Postgres. | Shim unit-tested; integration test against jury logs passes |
| **2. Pilot on Kun** | 3–4 wk | Kun, HwaO | Kun design-doc workflow routed through harness. Measure: tokens/doc, accuracy on multi-source synthesis (use existing design-doc archive as held-out set). | ≥30% token reduction AND ≤5% quality regression on doc review by HwaO |
| **3. Helix deployment** | 4–6 wk + 2 wk data | Tori implementer, Kun architect | Pull `gpt-oss-20b`. Wire Helix as agentic retriever for ABSTAIN×3 jury verdicts. Bootstrap SFT data from 4,000 cleaned jury+ADS trajectories. Run side-by-side with current escalation for 2 weeks. | Helix recovers ≥40% of ABSTAIN×3 claims into SUPPORT/REFUTE with ≥75% jury-correlated quality |
| **4. Substitution decision** | 2 wk | Kun, HwaO | Held-out 200-claim benchmark: Helix-20B-as-juror vs Nutty-Heavy-70B-as-juror. F1 on stance, latency, RAM. If Helix wins: rotate Nutty-Heavy to second-opinion seat; promote Helix to heavy jury slot. If Nutty-Heavy wins: keep Helix as retrieval-only. | Quantitative jury benchmark publishes a verdict |

### 3.6 Why not faster

- **Phase 1 is non-negotiable prerequisite for everything.** The shim is the load-bearing piece. Without it, Helix is just another local model — the value is the paradigm, not the weights.
- **Phase 2 before Phase 3** because Kun's workflow is **observable and reversible** (we keep design-doc logs; if it regresses, rollback is one config flag). Pilot the paradigm where the blast radius is small.
- **Phase 4 is gated on measurement, not vibes.** Nutty-Heavy was just promoted (2026-06-07). Rotating it out 8 weeks later without a benchmark would be churn.

### 3.7 Risks and what to watch

| Risk | Mitigation |
|---|---|
| `gpt-oss-20b` licence not actually permissive enough for our commercial use | Verify before Phase 3. If blocked, drop in `qwen3-coder-30b` or stay on the paradigm-only path. |
| Harness shim becomes a leaky abstraction (state stored both in shim AND in claim DB) | Treat the shim as a **view** over `claim_markers` + `dynamic_citations`, not a parallel store. No write-back to the shim from anything other than the agent loop. |
| Helix astronomy quality is worse than Atom-7B for scoring | Helix is not a scoring replacement. Keep Atom-7B. |
| Phase 2 pilot shows no token reduction | Likely means our prompts were already lean; abandon Option C, keep Phase 1 + 3 for the retrieval-agent value. |
| RL trajectories from jury logs are too noisy | Hand-curate the first 500 from highest-confidence jury verdicts; bootstrap the rest. |

---

## 4. Sequencing and Dependencies

```
Sprint 1 (Week 1-2)     Sprint 2 (Week 3-5)         Sprint 3+ (Week 6+)
───────────────────     ────────────────────       ─────────────────────────
[ Scheduler fix    ]    [ Harness shim (Ph 1) ]     [ Kun pilot (Ph 2)        ]
[ 5-layer hardening]    [ shared infra        ]     [ → token + quality data  ]
[ Tori implements  ]    [ Kun + Tori          ]     [                         ]
[ Unit tests       ]                                [ Helix pull + wire (Ph 3)]
[ Live replay      ]                                [ Tori + Kun              ]
       │                          │                            │
       ▼                          ▼                            ▼
   Closes the                  Unblocks                    Decision gate
   socket-hang                 Phase 2 + 3                 to Phase 4
   incident class              (paradigm + agent)          (substitute?)
```

**Critical path:** scheduler fix → harness shim → pilot → Helix → substitution decision. Scheduler fix is **independent** of all Harness work and ships first.

---

## 5. Open Questions for Papa

1. **Greenlight scheduler fix for Sprint 1?** Tori can start tomorrow. ~3 days code + 2 days replay tests. No model changes, no platoon impact.
2. **Greenlight harness-shim design (Phase 1) for Sprint 2?** Kun produces a follow-up design doc with the shim's data model; Tori implements. ~3 weeks total.
3. **Helix Phase 3 — pull the trigger?** Defer until Phase 2 data is in hand. Pre-decide the success criterion now (≥30% token reduction on Kun pilot) so the gate decision is fast.
4. **Substitution gate (Phase 4) — accept blind benchmark?** Confirm that a quantitative held-out F1 on 200 claims is the gate, not Papa's taste. Otherwise we'll be relitigating Nutty-Heavy's promotion every quarter.

---

## 6. Appendix — Files Referenced

- `backend/app/services/inference_scheduler.py` — central scheduler, all 5 fix layers land here
- `backend/scripts/targeted_ads_miner.py:629-691` — jury call site, gets page deadline + `return_exceptions=True`
- `backend/app/agent_loop/citation_context/{miner,dynamic_miner}.py` — same scheduler consumers, same fix
- `backend/logs/galev_fullpage_mine_r5.log` — incident log tail (lines 80-84 are the smoking gun)
- `~/.openclaw/workspace/memory/2026-06-10.md` — Papa's narrative log of the incident
- `~/.openclaw/workspace/memory/platoon-roster.md` — current model lineup, hardware budget, fallback chains
- `docs/platoon_realignment_v2.md` — Nutty-Heavy promotion context (relevant to Phase 4)
- `docs/jury_system_upgrade_v1.md` — prior jury architecture decisions
- `docs/targeted_ads_miner_stalling_audit_v1.md` — prior stall analysis (predecessor incident class)
- `docs/ollama_model_policy_v1.md` — policy for local-model selection

---

_Drafted by Kun on Mac Pro (Claude Opus 4.7) at 07:0X KST 2026-06-10. Awaits HwaO routing and Papa greenlight on Sprint 1 (scheduler fix) and Sprint 2 (harness shim Phase 1)._
