# NebulaMind Background Execution Pipeline Upgrade - Design v1

**Author:** Kun (Strategy) & Subagent (Architecture)
**Date:** 2026-06-06 13:30 KST
**Status:** PROPOSED for Tori Implementation & Papa Review
**Target File:** `~/NebulaMind/NebulaMind/docs/pipeline_upgrade_design_v1.md`

---

## 1. Executive Summary / TL;DR

The NebulaMind background execution pipeline automates our core "autowiki" loops, driving continuous page improvement and citation verification based on the Karpathy/autoresearch paradigm. However, a recent live audit of the backend system revealed three critical architectural bottlenecks that deadlocked the wiki-wide update loop, introduced race conditions, and silently degraded visible claim coverage.

This design document outlines a systematic, production-grade upgrade to resolve these gaps permanently. It introduces:
1. **A Model-Independent Liveness Monitoring Service (LMS):** Decouples health checks from specific models and resident memory statuses, tracking local and remote Ollama daemon health without deadlocking under idle-eviction policies.
2. **Sequential Celery Task Canvas & Transaction-Safe Stage Boundaries:** Decouples page generation/writing from vector marker re-embedding using formal Celery `chain` and `group` signatures. This guarantees that background workers only read fully committed database transactions, eliminating the "Ghost-Text Bug."
3. **Self-Healing, Local-First Embedding Client (SHLEC):** A resilient embedding router that defaults to ultra-fast local inference on the Mac Studio, detects local congestion/downtime, and gracefully routes requests through the Mac Pro SSH tunnel or fallback cloud APIs with dynamic circuit-breaking.
4. **Platoon Assignment Matrix:** Allocates models (AstroSage-70B, Qwen3-30B, Atom-7B, Nomic-Embed, Sonnet, Opus) to specific stages based on capability, latency, and cost-efficiency.

By transitioning from brittle, synchronous hotfixes to decoupled, state-managed execution canvases, we ensure 100% deterministic, race-condition-free, and self-healing execution of our core wiki workflows.

---

## 2. Current Architecture Gaps & Failure Analysis

### 2.1 The Liveness Probe Deadlock (Ollama Idle-Eviction)
* **Root Cause:** In `autowiki/tasks.py`, the `_rakon_probe()` function was verifying host health by checking if `settings.BUDDLE_MODEL` (`llama3.1:405b`) was currently loaded in active VRAM using Ollama’s `/api/ps` endpoint. 
* **Failure Cascade:** Ollama unloads inactive models from memory after a configured timeout (e.g., `5m` or `30m` idle). Once unloaded, the Autowiki tick skipped because the probe returned `False`. Because the tick skipped, the model was never requested, preventing it from ever being reloaded. The system entered a permanent deadlock where "the tick skipped because the model was unloaded, and the model remained unloaded because the tick was skipped."
* **The Hotfix:** Checked `/api/tags` (installed models) to ensure the model was registered on disk, bypassing the active-RAM check.
* **Brittle Gaps Remaining:** The hotfix remains hardcoded to string patterns inside task files and does not actively measure host responsiveness, queue length, or latency. If one Ollama host goes down completely, the check blocks synchronous execution loops.

### 2.2 The Post-Commit Race Condition (The Ghost-Text Bug)
* **Root Cause:** The `autowiki_tick` task triggered `emit_reembed(page_id)` asynchronously *inside* the active PostgreSQL database transaction, prior to calling `db.commit()`.
* **Failure Cascade:** 
  1. `autowiki_tick` generates a section rewrite.
  2. Before committing, it calls `emit_reembed(page_id).delay()`.
  3. Celery instantly spawns a background worker to run the embedding/alignment task.
  4. Due to PostgreSQL's default `Read Committed` isolation level, the Celery worker queries the DB but only sees the *old, un-rewritten page content* (since the parent transaction is still uncommitted).
  5. The embedding worker computes sentence/claim alignments on the *old text* and writes them.
  6. `autowiki_tick` then calls `db.commit()`.
  7. The new text is committed, but the claim markers have already been embedded on the old text, completely desynchronizing the anchors and wiping out new claims.
* **The Hotfix:** Removed the asynchronous trigger and ran `claim_marker_embed_page(page_id)` synchronously right after `db.commit()` in the same thread.
* **Brittle Gaps Remaining:** Running marker embedding synchronously inside the main tick defeats the concurrent design of Celery. It forces expensive embedding, sentence-splitting, and alignment calculations (which can take several seconds to minutes under heavy page loads) to block the main autowiki scheduler worker, increasing drift risk and stalling queue throughput.

### 2.3 The Embedding Timeout Bottleneck (GPU Saturation)
* **Root Cause:** The embedding client (`app/agent_loop/marker_embed/embed_index.py`) was hardcoded to proxy all vector requests over the SSH tunnel to the Mac Pro (port 11435).
* **Failure Cascade:** Whenever Rakon (DeepSeek-R1 671B) was active on the Mac Pro, the dual GPUs became 100% saturated. The massive inference workload blocked the Ollama daemon on the Mac Pro, causing embedding requests (which shared the same Ollama server) to time out (>10s). Lacking fallback routing, the aligner silently discarded claims, keeping visible claim coverage extremely low.
* **The Hotfix:** Added environment variables to route embedding traffic locally to `localhost:11434` (Mac Studio), where `nomic-embed-text:v1.5` runs warm under 10ms with zero timeouts.
* **Brittle Gaps Remaining:** If the local Ollama instance on the Mac Studio crashes, restarts, or is occupied by a heavy 70B model loading sequence, the embedding client fails completely. It lacks dynamic host failover, latency tracking, or retry backoffs.

---

## 3. Proposed Systematic Pipeline Architecture

To address the race condition while preserving concurrency, we design a formal Celery **Signature Canvas Chain** that strictly decouples the writing (rewrite) stage and the alignment (embedding) stage into distinct, sequential, and transaction-safe boundaries.

```
 [ autowiki_propose_and_commit ]
               │
               ▼  (On Success / Transaction Committed)
   [ claim_marker_embed_page ]
               │
               ▼  (On Success)
  [ autowiki_post_pipeline_notify ]
```

### 3.1 Celery Signature Canvas Chain Design
The autowiki loop will be dispatched as a sequential Celery `chain`. Under the hood, Celery handles this by passing the result of each stage as an argument to the next, executing them only upon the clean completion of the preceding task.

```python
from celery import chain
from app.agent_loop.worker import celery_app

def dispatch_autowiki_pipeline(page_id: int):
    # Construct a sequential transaction-safe canvas chain
    pipeline = chain(
        # Stage 1: Run generation, score composite, and COMMIT to DB
        autowiki_propose_and_commit.s(page_id),
        
        # Stage 2: Embed and align markers (only runs if Stage 1 commits successfully)
        claim_marker_embed_page_task.s(),
        
        # Stage 3: Post-pipeline notifications and metrics tracking
        autowiki_post_pipeline_notify.s(page_id)
    ).on_error(autowiki_pipeline_rollback.s(page_id))
    
    pipeline.delay()
```

### 3.2 Transactional Boundaries & Lock States
To prevent concurrent modifications or mid-pipeline reads from corrupting the wiki page:
1. **Advisory Lock Scope:** A Redis advisory lock `autowiki:page:<page_id>` is acquired at the very beginning of Stage 1 (`autowiki_propose_and_commit`). The TTL is set to `400` seconds (covering the worst-case latency of the entire chain).
2. **Lock Release:** The lock is strictly released in Stage 3 (`autowiki_post_pipeline_notify`) or within the error callback (`autowiki_pipeline_rollback`). No other tasks can acquire this page lock while the chain is running.
3. **PostgreSQL Isolation Level:** Stage 1 completes with a formal `db.commit()` and closes its SessionLocal database session. Only after the transaction is fully committed and visible to all other PostgreSQL connections does Stage 2 (`claim_marker_embed_page_task`) begin.
4. **Optimistic Content-Hash Check:** Stage 2 reads the latest `PageVersion` and matches its content hash against the output generated in Stage 1. If a manual user edit was committed in the millisecond window between Stage 1 commit and Stage 2 execution, Stage 2 aborts cleanly without rewriting the user's manual change.

### 3.3 Rollback and Recovery Mechanisms
If an unhandled exception or model timeout occurs during Stage 2 (Marker Embedding):
- **Error Callback Activation:** Celery's `.on_error(autowiki_pipeline_rollback.s(page_id))` captures the failure.
- **Automated Rollback Task:** The rollback task:
  1. Loads the prior `PageVersion` from before Stage 1 ran.
  2. Resets the `wiki_pages.content` column to this safe, stable pre-image.
  3. Deletes any dirty `Claim` or `Evidence` rows inserted by Stage 1 (queryable via `editor_agent_id` or the run log).
  4. Cleans up any incomplete metadata files in the cache.
  5. Releases the Redis advisory lock `autowiki:page:<page_id>`.
  6. Logs a detailed pipeline traceback to `logs/autowiki_pipeline_errors.log`.

---

## 4. Resilient Liveness & Dynamic Fallback Routing Design

### 4.1 Centralized Liveness Monitoring Service (LMS)
Instead of embedding custom HTTP checks directly inside individual tasks, we establish a centralized, model-independent `LivenessMonitor` class. The monitor runs periodically as a Celery beat task every 30 seconds or as a background service thread, saving verified health states to Redis.

```
                        ┌───────────────────┐
                        │  LivenessMonitor  │
                        └─────────┬─────────┘
         ┌────────────────────────┴────────────────────────┐
         ▼ (Port 11434)                                    ▼ (Port 11435)
┌─────────────────┐                               ┌─────────────────┐
│  Mac Studio M3  │                               │   Mac Pro GPU   │
└─────────────────┘                               └─────────────────┘
```

The LMS tracks health using a multi-tiered validation approach:
1. **Daemon Ping:** Checks if the Ollama service port is open and responding to GET `/` in < 50ms.
2. **Model Availability:** Checks GET `/api/tags` to verify if required models (e.g., `astrosage-70b`, `nomic-embed-text`) are registered on disk, avoiding active-RAM checks.
3. **Active Load Estimation:** Checks GET `/api/ps`. It uses this *strictly for telemetry* (e.g. tracking queue size and loaded models) to estimate queue congestion, but never as a hard block to skip tasks.
4. **Active Inference Probe:** Performs a 1-token diagnostic prompt (using a lightweight 7B model) to verify the host can compile weights and return tokens without timeouts.

The state is written to Redis under the hash `ollama:health` with the following schema:
```json
{
  "studio_11434": {
    "status": "HEALTHY",
    "latency_ms": 12,
    "daemon_active": true,
    "congested": false,
    "last_checked": "2026-06-06T13:30:00Z",
    "available_models": ["astrosage-70b", "atom-astronomy-7b", "nomic-embed-text:v1.5"]
  },
  "pro_11435": {
    "status": "CONGESTED",
    "latency_ms": 4500,
    "daemon_active": true,
    "congested": true,
    "last_checked": "2026-06-06T13:30:00Z",
    "available_models": ["deepseek-r1:671b"]
  }
}
```

### 4.2 Self-Healing, Local-First Embedding Client (SHLEC)
The embedding client (`app/agent_loop/marker_embed/embed_index.py`) is upgraded to use a resilient, self-healing routing protocol.

```
                     [ SHLEC Request ]
                             │
                             ▼
             Is Local (Mac Studio) Healthy?
                     /               \
              (Yes) /                 \ (No / Congested)
                   ▼                   ▼
       [ Route to Local Studio ]    [ Fallback to Mac Pro ]
       (nomic-embed-text, <10ms)    (If down, use Cloud API)
```

#### Routing and Circuit-Breaker Policies:
1. **Tier 1 (Local First):** Routes embeddings to `http://localhost:11434`. Latency expectation is < 15ms.
2. **Tier 2 (Remote Fallback):** If the local endpoint is down or times out twice, the client trips the circuit breaker, logs a warning, and routes requests over the SSH tunnel to the Mac Pro (`http://localhost:11435`).
3. **Tier 3 (Cloud Fallback):** If both local and remote Ollama instances are unavailable, the client routes embedding requests to a public API (such as OpenAI's `text-embedding-3-small` or Jina AI Embeddings) using an emergency API key in `.env`. This guarantees zero dropped claims during local infrastructure updates.
4. **Automatic Recovery (Fail-Back):** After 5 minutes in a tripped state, the client sends a single "probe" embedding request to the local host. If it succeeds and returns in < 50ms, the circuit breaker resets, and Tier 1 local-first routing is restored.

#### Connection Pooling and Timeouts:
- **Local Timeout:** Strict `2.0` second timeout. Local embeddings should be instantaneous; if they stall, fail fast and fall back.
- **Remote Timeout:** `15.0` second timeout to accommodate cold-starts or queue congestion on the Mac Pro.
- **Client Pooling:** Uses an `httpx.Client` with a connection pool limit of 50 concurrent connections to prevent socket exhaustion during heavy background load.

---

## 5. Platoon Assignment Matrix

To maximize inference performance, maintain resident model stability, and control API spending, models are assigned to specific roles based on their strengths, parameter size, and cost.

| Stage | Task Name | Assigned Model | Primary Host | Why This Model / Justification |
| :--- | :--- | :--- | :--- | :--- |
| **Stage 1a** | Missing Subtopic Mining & Taxonomy Mapping | **Qwen3-30B (Mima)** | Mac Studio (On-Demand) | Excellent at structured instruction following and fast text parsing. Perfect for identifying coverage gaps and mapping wiki taxonomies. |
| **Stage 1b** | Draft Section Generation & Claim Ingestion | **AstroSage-70B** | Mac Studio (Resident Set) | Astronomy-specific 70B model with exceptional domain expertise. Drafts technically rigorous content but runs locally and fast. |
| **Stage 1c** | Lightweight Evidence Quality Gate | **Atom-7B (Atom-Astronomy)** | Mac Studio (Resident Set) | Extremely lightweight and fast (sub-10ms latency). Acts as a cheap sanity-check filter to weed out mismatched research papers early. |
| **Stage 2** | Sentence & Claim Vector Embeddings | **Nomic-Embed (v1.5)** | Mac Studio (Local First) | Local 137M parameter embedding model running under 10ms with highly dense retrieval representation. |
| **Stage 3a** | Bi-Hourly Standard Quality Evaluation | **Claude 3.5 Sonnet** | Anthropic Cloud | Exceptionally high reasoning score and consistent rubric adherence. Used for regular, fast evaluation ticks without local GPU loading. |
| **Stage 3b** | Full-Page Coherence Synthesis | **Claude 3 Opus** | Anthropic Cloud | The gold standard in long-form prose synthesis. Used selectively for high-level full-page coherence rewrites to unify separate section drafts into a professional tone. |
| **Stage 4** | Deep-Pass Multi-Page Audit (6h loop) | **DeepSeek-R1 (671B / Rakon)** | Mac Pro (Dedicated GPU) | 671B Mixture-of-Experts reasoning model. Solves complex cross-page contradictions and provides the ultimate authority on facts, running asynchronously. |

---

## 6. Step-by-Step Implementation & Rollout Plan

To ensure zero downtime, Tori will execute the implementation across four phased, low-risk stages.

### Phase 1: Establish the Liveness Monitoring Service (LMS)
1. **Create Utility Service:** Build `app/services/liveness_monitor.py` containing the `OllamaLivenessMonitor` class.
2. **Setup Redis Storage:** Implement Redis hash reading/writing for liveness metrics under `ollama:health`.
3. **Register Celery Beat Task:** Add `check_ollama_hosts_liveness` to the Celery beat schedule in `app/agent_loop/worker.py` to run every 30 seconds.
4. **Integrate into Autowiki Tick:** Replace the hardcoded `_rakon_probe` in `autowiki/tasks.py` with a simple check to the LMS Redis key.

### Phase 2: Refactor the Embedding Client (SHLEC)
1. **Modify `embed_index.py`:** Update `_embed()` to implement the circuit-breaker pattern.
2. **Add Multi-Host Routing:** Integrate the fallback chain (Mac Studio -> Mac Pro -> Jina/OpenAI Cloud API).
3. **Configure HTTPX Connection Pool:** Limit connections to 50 and set strict timeouts (2s local, 15s remote).
4. **Deploy Unit Tests:** Write `tests/marker_embed/test_shlec.py` simulating local connection failures and verifying automatic failover and recovery.

### Phase 3: Implement Sequential Canvas Chains in Celery
1. **Decouple Task Code:** Separate `autowiki_tick` inside `autowiki/tasks.py` into `autowiki_propose_and_commit` and `claim_marker_embed_page_task`.
2. **Implement Signature Chains:** Wrap the tasks inside a Celery `chain` with explicit `on_error` callbacks.
3. **Deploy Rollback Logic:** Add `autowiki_pipeline_rollback` to handle DB restoration and Redis lock release in the event of pipeline errors.
4. **Verify Transaction Boundaries:** Test with heavy loads to ensure the embedding worker never reads an uncommitted transaction.

### Phase 4: Model Platoon Realignment & Calibration
1. **Resident Config Tuning:** Adjust `OLLAMA_KEEP_ALIVE` and `OLLAMA_MAX_LOADED_MODELS` in `/Library/LaunchAgents/ai.ollama.plist`.
2. **Pin Resident Models:** Update the model-warmer task to keep `astrosage-70b` and `deepseek-r1:14b` resident with a capped context limit of `8192`.
3. **Monitor Latency & Claim Coverage:** Track the `/docs` logs to ensure claim marker coverage stays above 85% and background latency remains steady.
