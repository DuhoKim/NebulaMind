# Targeted ADS Miner — Stalling Audit & Structural Fix Design v1

**Author:** Kun
**Date:** 2026-06-09 KST
**Host:** Duhoui-MacStudio.local
**Incident:** `targeted_ads_miner.py --page-id 57 --commit --min-claim-id 1732`, ~25 claims processed, stalled at claim 2107 on 2026-06-09 00:15 KST, slept 9h at 0% CPU. `lsof` showed an ESTABLISHED TCP connection to `localhost:11434` (Ollama). `httpx` `timeout=360` (6 min) inside `InferenceScheduler._make_http_call` never fired.

## 1. Executive verdict

The hang is **not** caused by httpx losing its read-timeout. It is caused by **synchronous Redis calls inside an `async` coroutine** (`InferenceScheduler.execute`) that block the entire event loop. When one of those sync calls hangs on a `recv()` from a flaky/saturated Redis, *every* other awaitable in the loop — including the `httpx` read-timeout future — never gets scheduled. The result is a wedged event loop with a dangling Ollama socket and no CPU activity.

There are also several secondary correctness/robustness issues — SQLAlchemy session lifecycle is chaotic, the script spawns multiple short-lived `asyncio.run()` loops, and there is no defensive watchdog on the juror call — but the event-loop starvation is the proximate cause.

## 2. Evidence trace

### 2.1 Call stack at the moment of stalling

`main()` → `process_claims()` → `run_jury_on_candidates()` → `asyncio.run(_jury_candidates_async(...))` → for each candidate (semaphore-limited): `run_jury_async()` → `asyncio.gather(_call_juror × 3 models)` → `_call_juror()` → `scheduler.execute()` → `_make_http_call()` → `client.post(.../v1/chat/completions, timeout=360)`.

With `INFERENCE_SCHEDULER_ENABLED = True` (verified in `app/config.py:201`) and `JURY_PAPER_CONCURRENCY = 2`, the steady state during processing of a single batch is:

- Up to **2 candidates** in flight (outer semaphore in `_jury_candidates_async`, `scripts/targeted_ads_miner.py:886`).
- For each candidate, **3 jurors** fire concurrently (`run_jury_async`, line 677–682), no internal semaphore.
- So up to **6 concurrent `scheduler.execute()` coroutines** are awaiting in the same loop.

### 2.2 The blocking-call problem in `InferenceScheduler.execute`

Look at `app/services/inference_scheduler.py:128–214`. Inside an `async def`, the scheduler calls:

```python
r = self._get_redis()                          # sync redis.from_url
health_str = r.get("ollama:health")            # SYNC blocking I/O on event loop
...
while time.time() - start_time < 240:
    if r:
        acquired = r.set(lock_key, "1", ex=ttl, nx=True)   # SYNC blocking I/O
        if acquired: break
    await asyncio.sleep(backoff)               # yields
```

The `redis` client returned by `redis.from_url(...)` is the **synchronous** redis-py client (not `redis.asyncio`). Each `r.get()` / `r.set()` call:

- Acquires the connection's socket (`socket.recv` / `socket.send`).
- Does **not** release the event loop while waiting.
- Has `socket_timeout=None` by default (`redis-py` default; not overridden in `_get_redis`).

Because `JURY_PAPER_CONCURRENCY=2` and 3 jurors per candidate share the **same** advisory lock key `ollama:lock:studio:heavy` (the key uses `:heavy` for both `medium` and `heavy` tiers — line 169), there is also heavy contention: at any moment up to ~5 jurors are spinning in the lock-acquisition loop, each issuing repeated synchronous `r.set(...)` calls back-to-back, separated only by an `await asyncio.sleep(backoff)`.

If Redis stalls for any reason — saturation, a TCP keepalive drop with no RST, a stop-the-world snapshot, etc. — even one sync `r.get()` or `r.set()` will block the **entire** event loop indefinitely.

While the loop is parked:

1. The httpx `timeout=360` is **not** a wall-clock alarm; it is an `asyncio.TimerHandle` scheduled on the loop. A parked loop never fires the handler.
2. The Ollama TCP connection already established by the winning juror stays in ESTABLISHED state on the OS — exactly what `lsof` showed.
3. CPU usage drops to 0 because no callbacks are being executed.

That matches every observed symptom (lsof connection, 0% CPU, 9-hour duration, ignored 360s timeout) with one cause.

### 2.3 Secondary contributing factors

These don't trigger the hang on their own, but each enlarges the blast radius:

**(a) Per-call `httpx.AsyncClient` instantiation.** `InferenceScheduler._make_http_call` at line 298 opens a new client per call, ignoring any client passed in. Each instantiation does fresh DNS, TCP, and TLS work, lengthening the window during which the loop is performing socket I/O. (It also reads the user-supplied `client` argument in `_call_juror` line 626 only on the non-scheduler path, so the scheduler path always paid this cost.)

**(b) Three `asyncio.run()` calls per claim batch.** `process_claims` invokes `asyncio.run(fast_screen_async(...))` (line 1075), then `asyncio.run(_jury_candidates_async(...))` for audit jurors (line 1111 via `run_jury_on_candidates`), then again for main jurors (line 1124). Each call instantiates a fresh loop and tears it down. Any cleanup mishandling, leaked `ClientSession`, or pending task in one loop becomes orphaned state for the next.

**(c) SQLAlchemy session lifecycle is incoherent.** The same `db` Session object is created in `main()` (line 1153), `db.close()`'d at line 1169, then handed to `process_claims(db, ...)`. `collect_candidates` calls `db.close()` *inside* its `for` loop on the first iteration (line 1031); subsequent iterations use the closed-but-auto-reattaching session. `_write_jury_result` calls `db.flush()`, then `db.commit()` or `db.rollback()`, then `db.close()` (lines 932–935). `ping_jury_agents` does `db.execute(...)` + `db.commit()`. The same session is recycled by 4+ different layers, repeatedly closed, and reopened. SQLAlchemy tolerates this (a closed `Session` will auto-acquire a fresh connection on next use), but:

- It depletes the engine pool quickly (each close-reopen churns connections).
- Default `QueuePool(size=5, overflow=10, timeout=30)` will eventually `pool_timeout` if a connection leaks anywhere.
- It makes it impossible to reason about transaction scope.

**(d) No defensive watchdog on the juror call.** `_call_juror` trusts that `scheduler.execute()` will return within `JURY_TIMEOUT_SECONDS=360`. There is no outer `asyncio.wait_for(...)` cap. If `scheduler.execute` is wedged for any reason (event-loop block, internal logic error, dropped exception), nothing forces cancellation.

**(e) `_LAST_PING_TIME` is module-global and not async-safe.** Not the cause of this hang, but a latent bug: if the script is ever moved into a long-running worker, two concurrent claims could race on `_LAST_PING_TIME` and miss the 60s throttle.

## 3. Hypothesis check vs. HwaO's framing

HwaO's hypothesis ("Single-Threaded Event Loop Starvation; sync SQLAlchemy ops starve the asyncio loop, preventing httpx timeout tasks from executing") is **directionally correct** — the diagnosis of event-loop starvation is the right frame. But the specific culprit is one layer lower:

- The synchronous SQLAlchemy work (`_write_jury_result`, `ping_jury_agents`) runs **after** `asyncio.run()` has already returned. It cannot starve the loop that contains the hung httpx call — that loop is already gone by then.
- The synchronous I/O that **does** run inside the active loop is the `redis-py` sync client used by `InferenceScheduler.execute`. That is the actual starvation source.

The SQLAlchemy session-lifecycle issues are real and need to be fixed, but they explain pool exhaustion / silent-corruption risks, not the 9-hour wedge.

## 4. Fix design

Two-tier fix: **(A) Minimal-diff stop-the-bleeding patch** so the script can be re-run reliably tonight, and **(B) Structural cleanup** done in a follow-up PR.

### 4.1 Tier A — minimal-diff hot fix (recommended for Tori first PR)

**A1. Make Redis I/O non-blocking inside `InferenceScheduler.execute`.**

The cleanest minimal change: wrap each sync Redis call with `asyncio.to_thread(...)`. This pushes the blocking socket I/O onto the default thread pool and keeps the event loop free to fire timeouts and dispatch other coroutines.

In `app/services/inference_scheduler.py`:

```python
# Replace:
health_str = r.get("ollama:health")
# With:
health_str = await asyncio.to_thread(r.get, "ollama:health")
```

```python
# Replace:
acquired = r.set(lock_key, "1", ex=ttl, nx=True)
# With:
acquired = await asyncio.to_thread(r.set, lock_key, "1", ex=ttl, nx=True)
```

And similarly for `r.delete(lock_key)` in the `finally` block (line 211).

**A2. Set explicit Redis socket timeouts.**

Bound the worst case if Redis itself goes silent. In `_get_redis`:

```python
return redis.from_url(
    settings.REDIS_URL,
    decode_responses=True,
    socket_timeout=5.0,
    socket_connect_timeout=3.0,
)
```

5 seconds is well below the 360 s juror budget; any Redis stall produces a clean exception instead of a wedge.

**A3. Add a hard `asyncio.wait_for` watchdog around `scheduler.execute`.**

In `scripts/targeted_ads_miner.py:_call_juror`, replace:

```python
content = await scheduler.execute(model, prompt, JURY_TIMEOUT_SECONDS, system_prompt=JURY_SYSTEM_PROMPT)
```

with:

```python
try:
    content = await asyncio.wait_for(
        scheduler.execute(model, prompt, JURY_TIMEOUT_SECONDS, system_prompt=JURY_SYSTEM_PROMPT),
        timeout=JURY_TIMEOUT_SECONDS + 120,  # juror budget + 2 min for lock-acquisition headroom
    )
except asyncio.TimeoutError:
    print(f"jury {model['label']} watchdog cancellation after {JURY_TIMEOUT_SECONDS + 120}s")
    return None
```

This is the belt-and-suspenders defense: even if some future regression reintroduces a blocking call, the watchdog forces cancellation in bounded time. The wrapped scheduler call will surface a `CancelledError` and clean up the open Ollama socket via `httpx`'s context-manager exit.

**A4. (Optional, same PR) Bound the per-juror lock budget below the watchdog.**

The advisory lock loop currently waits up to 240 s (`while time.time() - start_time < 240`, line 179). Combined with `JURY_TIMEOUT_SECONDS=360`, the worst-case execute is 600 s, which exceeds the 480 s watchdog above. Tighten one of the two so the watchdog is always strictly larger than the inner budget. Suggest: lower lock wait to 180 s and use watchdog = 360 + 180 + 60 = 600 s. Document the relationship as a comment.

**Estimated diff for Tier A:** ~30 LOC in two files. No SQLAlchemy or refactor risk. Ships independently of Tier B.

### 4.2 Tier B — structural cleanup (follow-up PR)

**B1. Eliminate the global `db` Session passed across layers.**

Adopt a per-unit-of-work session pattern. Helper:

```python
from contextlib import contextmanager

@contextmanager
def session_scope():
    db = SessionLocal()
    try:
        yield db
        db.commit()
    except Exception:
        db.rollback()
        raise
    finally:
        db.close()
```

Then:

- `select_claims`: open a scope, return a list of `ClaimSnapshot` dataclasses (already used elsewhere) — never return live ORM objects across the boundary.
- `retrieve_candidates`, `pre_gate`, `already_attached`: take a session as a parameter and assume it is live; do not call `.close()` on it.
- `_write_jury_result`: open its own short-lived scope per candidate.
- `ping_jury_agents`: own scope; wrap inside `asyncio.to_thread` when called from async code.
- `collect_candidates`: open one scope for the candidate-collection phase, never close it mid-iteration.

This removes every `db.close()` from inside business logic and makes ownership obvious.

**B2. Run synchronous DB writes via `asyncio.to_thread` from within a single async pipeline.**

Convert `run_jury_on_candidates` to async. After `asyncio.gather` over jurors, for each `(candidate, decision)` do:

```python
written = await asyncio.to_thread(_write_jury_result_sync, candidate, decision, commit=commit)
await asyncio.to_thread(ping_jury_agents_sync, [r.label for r in decision.results])
```

Result: one loop, one `asyncio.run()` at the program entry point, all blocking work explicitly executor-bound.

**B3. Consolidate to a single `asyncio.run()`.**

`main()` becomes:

```python
def main() -> int:
    args = parse_args()
    if not settings.ADS_API_KEY:
        raise SystemExit("ADS_API_KEY is not configured")
    return asyncio.run(main_async(args))
```

`main_async(args)` does everything currently in `main()` + `process_claims()`. Eliminates the three nested `asyncio.run()` calls and removes any chance of cross-loop resource leaks.

**B4. Reuse one `httpx.AsyncClient` per pipeline run.**

Create a single `AsyncClient` in `main_async`, pass it down. `InferenceScheduler._make_http_call` should accept it instead of instantiating its own. Reduces TLS handshakes and lets httpx pool connections cleanly.

**B5. Bound DB pool wait explicitly.**

In `app/database.py`:

```python
engine = create_engine(
    settings.DATABASE_URL,
    pool_size=10,
    max_overflow=20,
    pool_timeout=15,
    pool_recycle=1800,
    pool_pre_ping=True,
)
```

`pool_pre_ping` catches stale connections; `pool_timeout=15` ensures a pool-exhaustion bug surfaces as an exception, not a hang. This is a global concern — coordinate with anyone else using `SessionLocal` before changing defaults.

**B6. Make `_LAST_PING_TIME` async-safe.**

Move it inside the `run_jury_on_candidates` (now async) function as a local, or use a `threading.Lock` if it must remain module-global. Not urgent.

### 4.3 Optional: move the miner under Celery (out of scope for this fix)

A Celery-task-per-claim version isolates each claim in its own worker process, gives natural retries, and removes the "one hang kills the batch" problem entirely. This is the right end-state but is a larger redesign and should not block the immediate fix.

## 5. Validation plan for Tori

After Tier A is applied:

1. **Reproduce the failure mode synthetically.** Use a fault-injection wrapper around `redis.Redis.set` that sleeps 600 s on the first call inside the process to simulate Redis stall. Confirm the watchdog fires and the script proceeds (juror returns `None`, fallback path runs).
2. **Run end-to-end on a small subset.** Re-run with `--page-id 57 --commit --min-claim-id 2107 --limit 5`. Confirm completion within expected wall-clock time and no orphaned `lsof` connections to 11434 after exit.
3. **Run the full resumption batch.** `--page-id 57 --commit --min-claim-id 2107` (no `--limit`). Monitor with `ps`, `lsof`, and the Mac Studio Ollama queue length. If any stall exceeds `JURY_TIMEOUT_SECONDS + 120 = 480 s` on a single juror, log the event and abort — that indicates the watchdog is still not catching something.
4. **Capture metrics for follow-up.** Total juror calls, lock-acquisition timeouts, watchdog cancellations, and fallback rate. Feed into the Tier B design.

## 6. Platoon assignment

This is one-shot fixup code, not a recurring job — no model-platoon assignment applies. The miner itself continues to dispatch jurors against the existing platoon (Mima=qwen3:30b, Nutty-Heavy=deepseek-r1:70b, Atom-7B=vanta-research/atom-astronomy-7b) per `scripts/targeted_ads_miner.py:576–602`. No changes to model selection in this audit.

## 7. Open questions / things I did not verify

- I did not confirm that Redis was actually stalled at the time of the hang. The case for the diagnosis rests on: (a) the symptom pattern is exactly what a parked event loop produces, (b) the only blocking I/O on the loop is sync Redis, (c) every other proposed cause (httpx losing timeout, async->sync DB starvation across `asyncio.run`) does not survive a careful trace. A Redis-side log scan around 2026-06-09 00:15 KST (slow log, latency monitor) would close the loop. **Action:** Tori, please pull `redis-cli SLOWLOG GET 128` and any host-level dmesg/iostat from that window if available.
- I did not measure how many candidates were queued at the moment of the stall — that affects the precise number of jurors contending on the advisory lock. A workspace-side replay (read the script's stdout log if it was preserved by `python -u`) would tell us.
- Tier B requires coordination with anyone else writing to `SessionLocal` (autowiki loop, jury_shadow, etc.) before changing pool defaults.

## 8. Recommended sequence

1. Tori implements Tier A (4 small edits + 1 new helper) → unblocks the page-57 resumption tonight.
2. Re-run the miner with the watchdog + thread-offloaded Redis. Confirm completion.
3. Tier B planned for follow-up PR, scope-checked with whatever else depends on `SessionLocal`.

— Kun, 2026-06-09
