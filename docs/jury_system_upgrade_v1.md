# NebulaMind Jury System Upgrade — Design v1

**Author:** Kun (Strategy) — claude-opus-4-7
**Date:** 2026-06-06 KST
**Status:** PROPOSED for Tori Implementation & Papa Review
**Target File:** `~/NebulaMind/NebulaMind/docs/jury_system_upgrade_v1.md`
**Sibling docs:** `ollama_model_policy_v1.md`, `pipeline_upgrade_design_v1.md`, `trust_calibration_design_v1.md`

---

## 1. Executive Summary / TL;DR

The NebulaMind "jury" is the evidence-evaluation organ of the platform: every
piece of evidence (arXiv abstract, ADS record, retrieved passage) is routed
through one or more LLM jurors that vote SUPPORTS / REFUTES / ABSTAIN before it
can be admitted to a wiki page, promoted by the validator, or surfaced in the
retrieval funnel. Today, that organ is **three different juries glued to three
different scripts**, sharing nothing but a vague resemblance to each other.

A backend audit of the current jury surface found **three structural defects**
that are now bottlenecking platform-wide trust quality:

| # | Defect | Where it hurts | Concrete file |
|---|---|---|---|
| 1 | **Hardcoded prompts.** `JURY_SYSTEM_PROMPT`, `ENTAILMENT_PROMPT_TEMPLATE`, `STANCE_JURY_SYSTEM`, and the well-posed-idea prompt are each duplicated inline. Strictness, synonym tolerance, and pronoun-resolution rules cannot be tuned globally. | Calibration A/B (strict vs. permissive) requires editing 4 scripts and a redeploy. | `targeted_ads_miner.py:129`, `retrieval_filter_v2.py:47`, `app/agent_loop/tasks.py:93`, `well_posed_jury.py:55` |
| 2 | **Naive `asyncio.gather` against one Ollama process.** Mima (Qwen3 30B), Buddle (Llama3.1 405B / Llama3.3 70B), Atom-7B, and Deepseek-r1 14b are fired concurrently against `localhost:11434`. The single Ollama daemon saturates VRAM bandwidth and starts returning `httpx.ReadTimeout` after ~45 s. | Jury batches silently downgrade to ABSTAIN; trust scores stall. | `targeted_ads_miner.py:449` (`run_jury_async`), `app/agent_loop/tasks.py:667` (`_chat_parallel`) |
| 3 | **Binary majority vote with equal weights.** `aggregate_jury` uses "≥ MIN_SUPPORT_VOTES, no REFUTES" as a flat rule, even though jurors range from a 7B SLM to a 70B/405B generalist. There is no scorecard, no per-juror weight, no confidence-aware aggregation. | A 405B Buddle abstain and a 7B Atom abstain count identically; the frontend has nothing to render except "supports / refutes / neutral." | `targeted_ads_miner.py:524` (`aggregate_jury`), `app/routers/jury.py:120` (binary `-1/0/+1`) |

This design closes all three:

1. **§3 — Centralized Prompt Template Engine.** A versioned, YAML-backed prompt
   registry lives at `app/config/prompts/jury/*.yaml`, surfaced via a single
   `PromptRegistry` API. Strictness ("strict_v1" vs. "permissive_v1"),
   synonym tolerance, equivalent-term matching, and multi-sentence pronoun
   resolution become **policy fields**, not source code. Existing call sites in
   `targeted_ads_miner.py`, `retrieval_filter_v2.py`, `tasks.py`, and
   `well_posed_jury.py` are migrated to `PromptRegistry.render("stance.v2",
   variables, policy="strict_v1")`.

2. **§4 — Ollama-Aware Inference Scheduler.** A new `InferenceScheduler`
   service serializes / throttles local-model calls based on the
   `ollama:health` Redis cache produced by the Liveness Monitoring Service
   (already specified in `pipeline_upgrade_design_v1.md §4.1`). Each model has
   a declared VRAM footprint and a Redis-backed semaphore; the scheduler
   admits at most one heavy model per GPU bank at a time, while letting the
   resident SLMs (Atom-7B, Deepseek-r1:14b) run wide. Cloud-hosted jurors
   (Gemini, Cerebras, Sambanova) bypass the scheduler. **Outcome:** no more
   `asyncio.gather`-induced timeouts under full load.

3. **§5 — Weighted Consensus & Multidimensional Scorecard.** The aggregator
   returns a 4-axis scorecard — **Relevance**, **Factual Entailment**,
   **Methodological Rigor**, **Confidence** — produced by weighted aggregation
   over each juror, where weights come from a JuryAgentProfile table
   (parameter-size tier × domain fit × reliability × per-juror calibration).
   Binary "supports / refutes" is retained as a derived field for backward
   compatibility, but the new scorecard becomes the data of record for trust
   recomputation, sitemap routing, and frontend chips.

§6 lists the (small) DB schema additions; §7 lays out a four-phase, low-risk
Tori rollout that keeps the existing jury operational while the new pipeline
is shadow-validated.

**One-line:** Decouple prompts → serialize Ollama → score richly. The visible
outcome is a unified, hardware-aware jury that we can re-tune in seconds
instead of redeploys, that never times out under heavy local load, and that
emits structured evidence quality the platform can actually reason over.

---

## 2. Current Jury System Gaps & Concurrency Bottlenecks

### 2.1 The four de-facto jury sites

The current platform has **four logically distinct juries** living in four
different files, with no shared prompt registry, no shared scheduler, no
shared aggregator, and no shared schema beyond `evidence_votes`:

| Site | Purpose | Models | Aggregation | Source |
|---|---|---|---|---|
| **A. Targeted ADS jury** | Decide if an ADS-retrieved paper SUPPORTS / REFUTES / ABSTAIN a wiki claim, *before* it is inserted as evidence. | Mima (Qwen3 30B), Buddle (Llama3.1 405B / Llama3.3 70B), Atom-7B — parallel | "≥ 2 SUPPORTS and no REFUTES" → `supports`; any REFUTES → `refutes`; else `neutral`. Confidence collapsed to a single 0.50–0.85 quality scalar. | `backend/scripts/targeted_ads_miner.py` (688 LOC) |
| **B. Stance jury (Celery beat)** | Re-evaluate already-attached evidence on a 30-min / hourly drain. | Gemini-2.5-flash + 3 local Studio models — parallel via `_chat_parallel` | Free-form: returns `{stance_correct, vote ∈ {-1,0,+1}, reason}`; reputation-weighted aggregation downstream. | `backend/app/agent_loop/tasks.py:93–124, 2569–2730` |
| **C. Retrieval entailment gate** | Decide if a retrieved paper's abstract entails a specific claim element during the v2 retrieval filter. | Single model: Gemini-2.5-flash default; Ollama llama3.1:8b alternate | Single-juror `yes/no/abstain`. | `backend/scripts/retrieval_filter_v2.py:47–60, 420–560` |
| **D. Well-posed jury** | Score how falsifiable a research-idea is on a 0.0–1.0 scale. | Single model: Buddle (llama3.1:405b) | Single-juror float. | `backend/app/agent_loop/research_ideas/well_posed_jury.py` |

### 2.2 Defect #1 — Prompt strictness cannot be tuned globally

The audit-relevant facts:

- `JURY_SYSTEM_PROMPT` in `targeted_ads_miner.py:129` is a 27-line hardcoded
  string. The strictness rule ("topical overlap, same subfield, or 'related
  work' without specific evidence is NOT support") is duplicated **as English
  text only**, with no machine-readable knob to make it more permissive.
- `ENTAILMENT_PROMPT_TEMPLATE` in `retrieval_filter_v2.py:47` is a separate
  hardcoded string with subtly *different* equivalence rules ("equivalent
  words", "naming the same measurable factor"). When the v2 retrieval funnel
  diverges from the targeted-ADS jury's notion of "support," the divergence is
  invisible because nobody is comparing the two prompts side by side.
- `STANCE_JURY_SYSTEM` in `tasks.py:93` defines yet a third "support" rule
  ("findings are consistent with and reinforce the claim").
- The verdict-format spec (`###VERDICT: …`) and the regexes that parse it
  (`VERDICT_RE`, `SENTENCE_RE`, `CONF_RE`) are also hardcoded.

Practical consequence: when Papa asks "make the jury 10 % more permissive on
synonym matches" — the smallest such tuning today touches **four files and a
redeploy.** The arXiv-Wiki Feed v1 calibration A/B is currently running
against this exact pain.

### 2.3 Defect #2 — `asyncio.gather` saturates the GPU bank

Both Site A and Site B fire jurors with naive parallelism:

```python
# targeted_ads_miner.py:449
async with httpx.AsyncClient() as client:
    calls = [_call_juror(client, model, prompt) for model in jury_models()]
    results = await asyncio.gather(*calls)
```

```python
# tasks.py:667 (_chat_parallel)
async with httpx.AsyncClient() as client:
    tasks = [_call_one_async(client, m, system, user_msg, timeout) for m in models]
    results = await asyncio.wait_for(asyncio.gather(*tasks, return_exceptions=False), timeout=90)
```

Both pre-suppose that fanning out 3–4 concurrent requests is harmless. On the
Mac Studio M3 Ultra (single Ollama daemon, single unified-memory GPU), it is
not:

- **VRAM contention.** Qwen3-30B (Mima) needs ~22 GB at `num_ctx=8192`; Atom-7B
  needs ~9 GB; Deepseek-r1:14b needs ~15 GB. Fired together, they exceed
  Ollama's `OLLAMA_NUM_PARALLEL=2` admission limit and start queueing inside
  the daemon. The client sees opaque timeouts.
- **HTTP timeouts.** `_call_juror` uses `JURY_TIMEOUT_SECONDS=180`, but when
  three heavy models are loaded sequentially by the same daemon, the third
  spends 60–90 s waiting for slot 0 to evict slot 1, then another 30 s on
  cold weight upload, blowing past the timeout.
- **Cascade.** Gemini-2.5-flash + Atom-7B can finish in ~3 s; the run still
  waits 90 s for the gather() ceiling, then drops Mima / Deepseek, so the
  consensus collapses to ABSTAIN.
- **No back-pressure.** No call site checks `ollama:health` (newly available
  per `pipeline_upgrade_design_v1.md §4.1`) before dispatching.

The result is a class of failure that looks like "jury just kind of stops
working" under heavy load — exactly what an audit observed during the recent
stance-jury drain on the 5 low-health pages.

### 2.4 Defect #3 — Binary majority with equal weights

`aggregate_jury` in `targeted_ads_miner.py:524`:

```python
support_count = sum(1 for r in parsed if r.verdict == "SUPPORTS")
refute_count = sum(1 for r in parsed if r.verdict == "REFUTES")
if refute_count:
    stance = "refutes"
elif support_count >= MIN_SUPPORT_VOTES:
    stance = "supports"
else:
    stance = "neutral"
```

This treats Atom-7B and Buddle-405B as equal voters. It also throws away the
LOW / MEDIUM / HIGH confidence axis except as a coarse 0.50–0.85 quality
scalar. There is no distinction between:

- 3 jurors all say SUPPORTS with HIGH confidence and quote the same sentence.
- 2 jurors say SUPPORTS with LOW confidence, 1 abstains.

Both currently collapse to `stance="supports", quality≈0.55`. Downstream
trust scoring, sitemap routing, and the frontend "trust chip" all have to
guess what that means.

The frontend has been asking for a richer signal for two sprints. This
upgrade delivers it.

---

## 3. Unified Prompt Decoupling & Config Layer Specification

### 3.1 Goals

- One prompt registry, one source of truth, one tuning surface.
- Versioned: every prompt has a semver-style id (`stance.v2`, `entailment.v1`,
  `well_posed.v1`) so calibration runs can pin a version and reproduce.
- Policy-parameterized: strictness, synonym tolerance, equivalent-term
  matching, pronoun resolution become *fields* (`PromptPolicy`), not source
  text edits.
- Backward-compatible: existing parsers (`VERDICT_RE` etc.) continue to work
  by virtue of the prompt continuing to emit `###VERDICT: …` format.

### 3.2 Layout

```
app/config/prompts/
├── jury/
│   ├── stance.v1.yaml          ← legacy, frozen
│   ├── stance.v2.yaml          ← new, policy-parameterized
│   ├── entailment.v1.yaml
│   ├── well_posed.v1.yaml
│   └── scorecard.v1.yaml       ← multi-axis prompt (§5)
├── policies/
│   ├── strict_v1.yaml
│   ├── permissive_v1.yaml
│   └── calibration_AB.yaml
└── registry_index.yaml         ← maps semantic name → file path + checksum
```

### 3.3 Prompt file schema (YAML)

```yaml
# app/config/prompts/jury/stance.v2.yaml
id: stance.v2
inherits: stance.v1                # delta-encoded; full text materialized on load
description: |
  Stance juror that emits a structured ###VERDICT / ###SENTENCE / ###CONFIDENCE
  block, with policy-controlled synonym tolerance and pronoun resolution.

variables:                          # interpolation slots, validated at render
  - claim_text
  - paper_title
  - paper_year
  - paper_abstract

verdict_schema:
  format: tagged_block              # parsed by shared VERDICT_RE etc.
  tags:
    - VERDICT: [SUPPORTS, REFUTES, ABSTAIN]
    - SENTENCE: verbatim_or_NONE
    - CONFIDENCE: [LOW, MEDIUM, HIGH]
  scorecard:                        # used only by scorecard.v1.yaml
    axes: [relevance, entailment, rigor]
    range: [0.0, 1.0]

policy_hooks:                       # policies override these blocks
  strictness_block: |
    {{policy.strictness_text}}
  synonym_block: |
    {{policy.synonym_text}}
  pronoun_block: |
    {{policy.pronoun_text}}

system_template: |
  You are a rigorous scientific evidence juror for an astronomy knowledge base.
  Your job is to decide whether a paper's ABSTRACT explicitly supports,
  explicitly refutes, or does neither, for a single CLAIM.

  {{strictness_block}}
  {{synonym_block}}
  {{pronoun_block}}

  Hard rules:
  1. Vote SUPPORTS only with a verbatim sentence quoted from the abstract.
  2. Vote REFUTES only with a verbatim sentence.
  3. Otherwise vote ABSTAIN.
  4. Do not use outside knowledge.

  Emit your decision as the LAST lines:
  ###VERDICT: <SUPPORTS|REFUTES|ABSTAIN>
  ###SENTENCE: <verbatim sentence, or NONE>
  ###CONFIDENCE: <LOW|MEDIUM|HIGH>

user_template: |
  CLAIM:
  {{claim_text}}

  PAPER:
  Title: {{paper_title}}
  Year: {{paper_year}}
  Abstract:
  {{paper_abstract}}
```

### 3.4 Policy file schema

```yaml
# app/config/prompts/policies/strict_v1.yaml
id: strict_v1
description: Default 2026-06 strict policy. Used by Targeted ADS jury post-2026-05-26.

strictness_text: |
  Be rigorous. The paper supports the claim ONLY if it asserts the same physical
  relationship or measurable factor. Topical overlap, same subfield, or
  "related work" without specific evidence is NOT support.

synonym_text: |
  Equivalent terms are acceptable: e.g., "stellar mass function" ≡
  "galaxy mass distribution" when used with the same operational meaning.
  Do not accept loose paraphrases that drop a key qualifier (e.g., "at z>2").

pronoun_text: |
  When the supporting sentence contains a pronoun ("it", "they", "this"),
  scan the preceding 2 sentences for the antecedent. Quote the sentence with
  the pronoun, not the antecedent.

# Numeric knobs surfaced to the aggregator (§5):
aggregation:
  support_threshold: 0.65          # entailment axis required for SUPPORTS
  refute_threshold: 0.65
  abstain_band: [0.35, 0.65]       # everything in between → ABSTAIN
  min_quoted_sentence_chars: 25
```

```yaml
# app/config/prompts/policies/permissive_v1.yaml
id: permissive_v1
description: Calibration A/B looser policy, 2026-05-26 onward.

strictness_text: |
  Be reasonable. The paper supports the claim if its findings are consistent
  with the same physical mechanism, even when reported under a different
  observational tracer.

synonym_text: |
  Accept synonyms and equivalent operational definitions liberally.

pronoun_text: |
  Resolve pronouns by simple antecedent scan; if the antecedent is in the
  preceding sentence, quote that sentence instead.

aggregation:
  support_threshold: 0.55
  refute_threshold: 0.55
  abstain_band: [0.40, 0.55]
  min_quoted_sentence_chars: 20
```

### 3.5 The `PromptRegistry` API

```python
# app/services/prompt_registry.py
class PromptRegistry:
    """Versioned, policy-parameterized prompt loader.

    Reads YAML once at process boot, caches in-memory. A SHA-256 of each
    materialized prompt is stored alongside the rendered text and emitted
    with every juror call (see §6) so any verdict can be traced to the exact
    prompt+policy revision that produced it.
    """

    def __init__(self, root: Path = Path("app/config/prompts")):
        self._prompts: dict[str, PromptSpec] = self._load_all(root / "jury")
        self._policies: dict[str, PolicySpec] = self._load_all(root / "policies")

    def render(
        self,
        prompt_id: str,         # e.g. "stance.v2"
        variables: dict[str, str],
        policy: str = "strict_v1",
    ) -> RenderedPrompt:
        ...

@dataclass(frozen=True)
class RenderedPrompt:
    prompt_id: str            # "stance.v2"
    policy_id: str            # "strict_v1"
    prompt_sha256: str        # hash of materialized system+user
    system: str
    user: str
    verdict_schema: dict      # for the aggregator
    aggregation: dict         # threshold knobs from policy
```

### 3.6 Migration of the four call sites

| Site | Old | New |
|---|---|---|
| Targeted ADS jury | inline `JURY_SYSTEM_PROMPT`, `user_prompt(...)` | `registry.render("stance.v2", {claim_text, paper_title, paper_year, paper_abstract}, policy=settings.JURY_POLICY)` |
| Stance jury (Celery) | inline `STANCE_JURY_SYSTEM` | `registry.render("stance.v2", …, policy=settings.JURY_POLICY)` — single rendered prompt for all jurors |
| Retrieval entailment gate | inline `ENTAILMENT_PROMPT_TEMPLATE` | `registry.render("entailment.v1", {claim_text_snapshot, element_text, paper_abstract_snapshot}, policy=settings.RETRIEVAL_POLICY)` |
| Well-posed jury | inline f-string in `_score_idea` | `registry.render("well_posed.v1", {question, why_now, approach}, policy=settings.WELL_POSED_POLICY)` |

Critically, **stance.v2 is shared across Sites A and B.** That is the *whole
point* — one definition of "support" across the platform.

### 3.7 Tuning workflow

Before: edit Python, redeploy, restart Celery, hope.

After:
1. Edit `app/config/prompts/policies/strict_v1.yaml`.
2. `python -m app.services.prompt_registry validate strict_v1` (CI gate too).
3. `SIGHUP` Celery workers — registry hot-reloads, new prompt hash emitted
   with the next jury vote, `prompt_sha256` change visible in
   `evidence_votes.prompt_sha256` for retro analysis.

---

## 4. Ollama-Aware Inference Pacing & Serialization Architecture

### 4.1 Why a scheduler, not just more retries

The intuitive fix to "Ollama times out" is "add timeout + retry." Don't. The
GPU bank's pain isn't transient — it's structural saturation. Adding retries
just amplifies the cascade. The right primitive is **admission control**: a
scheduler that decides, *before* the call, whether the target Ollama daemon
has the headroom to take the job, and if not, either serializes it onto a
queue or routes it to a cloud fallback.

### 4.2 Architectural shape

```
            ┌────────────────────────────────────┐
            │ jury sites (targeted_ads_miner,    │
            │ tasks.py _chat_parallel,           │
            │ retrieval_filter_v2, well_posed)   │
            └──────────────────┬─────────────────┘
                               │  schedule(model, est_tokens, prompt)
                               ▼
            ┌────────────────────────────────────┐
            │       InferenceScheduler           │
            │  • reads ollama:health (Redis)     │
            │  • per-model VRAM footprint table  │
            │  • per-host semaphore (Redis)      │
            │  • policy: serialize / parallel /  │
            │    fallback-to-cloud               │
            └────────┬──────────────────┬────────┘
       acquire slot  │                  │  no slot, fallback
                     ▼                  ▼
         Mac Studio Ollama        Cerebras / Gemini /
         (port 11434)             Sambanova (cloud)
                     ▲
                     │ updates every 30 s
                ┌────┴────┐
                │   LMS   │  (already in pipeline_upgrade_design_v1.md §4.1)
                └─────────┘
```

### 4.3 Model footprint registry

A single YAML, loaded once:

```yaml
# app/config/inference/model_footprints.yaml
hosts:
  studio_11434:
    base_url: http://localhost:11434
    vram_total_gb: 440          # safe budget per ollama_model_policy_v1.md §0
    num_parallel: 2             # matches OLLAMA_NUM_PARALLEL

  pro_11435:
    base_url: http://localhost:11435   # SSH tunnel
    vram_total_gb: 96
    num_parallel: 1

models:
  "astrosage-70b:latest":
    host: studio_11434
    resident: true
    footprint_gb: 49
    cold_load_s: 40

  "deepseek-r1:14b":
    host: studio_11434
    resident: true
    footprint_gb: 15
    cold_load_s: 8

  "vanta-research/atom-astronomy-7b:latest":
    host: studio_11434
    resident: false             # optional resident; gated by settings flag
    footprint_gb: 9
    cold_load_s: 3

  "qwen3:30b":
    host: studio_11434
    resident: false
    footprint_gb: 22            # at num_ctx=8192
    cold_load_s: 12

  "gemma3:27b":
    host: studio_11434
    resident: false
    footprint_gb: 20
    cold_load_s: 10

  "llama3.3:70b":
    host: studio_11434
    resident: false
    footprint_gb: 49
    cold_load_s: 40

  "llama3.1:405b":              # Buddle, runs on Pro
    host: pro_11435
    resident: false
    footprint_gb: 240
    cold_load_s: 120
```

### 4.4 Redis-backed admission

Per host, a single Redis key tracks current load:

```
ollama:load:studio_11434  →  sorted set of {model_name: slots_in_use, expire_ts}
ollama:load:pro_11435     →  …
```

Each scheduled call:

1. Reads `ollama:health.{host}.status`. If `CONGESTED` or `DEGRADED`, jumps to
   step 5 (fallback).
2. Computes required slots: `1` for resident models, `2` for non-resident
   heavy models (40 GB+), and bumps the in-use sum.
3. If `in_use + required ≤ num_parallel`, atomic ZADD claims the slot with a
   TTL = `cold_load_s + timeout`.
4. Issues the HTTP call. On success/failure, ZREM the slot.
5. If admission fails: scheduler picks the next juror's fallback path
   (declared per-juror in the JuryAgentProfile, §5.4). For Targeted-ADS Mima,
   the fallback chain is `Mima(local) → Cerebras-llama3.1-8b → Gemini-flash`.

```python
# app/services/inference_scheduler.py
class InferenceScheduler:
    def __init__(self, redis_client, footprints: ModelFootprints, lms_key="ollama:health"):
        self.r = redis_client
        self.fp = footprints
        self.lms_key = lms_key

    async def execute(self, juror_spec: JurorSpec, rendered: RenderedPrompt,
                      timeout: int) -> JurorCallResult:
        """Atomically schedule + run a juror call.

        Returns JurorCallResult with the final endpoint actually used (may be
        cloud fallback) and a `scheduled_via` audit trail.
        """
        host = self.fp.host_of(juror_spec.model)
        if juror_spec.is_cloud:
            return await self._cloud_call(juror_spec, rendered, timeout)

        # 1. health gate
        health = self._health(host)
        if not health.permits_inference():
            return await self._fallback(juror_spec, rendered, timeout,
                                        reason="host_unhealthy")

        # 2-3. admission
        slots = self._slots_required(juror_spec.model)
        admitted = self._claim_slots(host, juror_spec.model, slots,
                                     ttl=self.fp.cold_load_s(juror_spec.model) + timeout)
        if not admitted:
            # Serialize: wait in a small queue (max 30 s) for a slot,
            # else fall back.
            admitted = await self._queue_wait(host, slots, max_wait=30)
            if not admitted:
                return await self._fallback(juror_spec, rendered, timeout,
                                            reason="no_slot")

        try:
            return await self._local_call(juror_spec, rendered, timeout, host)
        finally:
            self._release_slots(host, juror_spec.model)
```

### 4.5 Per-juror parallelism policy

Inside the scheduler, the **jury batch** itself (3 jurors per evidence) is
still issued via `asyncio.gather`, but each individual coroutine is now an
`await scheduler.execute(...)` that may serialize itself behind a Redis
semaphore. The net effect:

- Resident SLM (Atom-7B) + 1 resident reasoning model (Deepseek-r1:14b) can
  both run truly in parallel — they fit in VRAM, `num_parallel=2` permits it.
- A heavy non-resident model (Mima Qwen3-30B) waits its turn, runs
  sequentially against the resident pair, then releases.
- The Buddle 405B juror is routed to `pro_11435` (Mac Pro), which has its own
  semaphore (`num_parallel=1`) — Buddle is effectively serialized but doesn't
  block the Studio jurors.

### 4.6 Hooked into the existing LMS

The `ollama:health` schema from `pipeline_upgrade_design_v1.md §4.1` already
emits `congested: bool, latency_ms, available_models`. The scheduler reuses
these fields verbatim. **No new health probes are introduced** — the
scheduler is a *consumer* of LMS, not a parallel monitor.

### 4.7 Observability

The scheduler logs three Prometheus counters per call:

```
nm_jury_scheduler_admit_total{host,model,outcome}    # outcome: admitted|queued|rejected
nm_jury_scheduler_fallback_total{from_model,to_model,reason}
nm_jury_scheduler_queue_wait_seconds{host}           # histogram
```

These let Tori see at a glance whether the scheduler is doing its job — under
a healthy load profile, `fallback_total` should be small and `queue_wait`
p99 should be < 5 s. Anything above warrants policy tuning.

### 4.8 Pseudocode summary

```
async def juror_call(juror_spec, rendered_prompt, timeout):
    if juror_spec.is_cloud:
        return await cloud_call(juror_spec, rendered_prompt, timeout)

    host = footprints.host_of(juror_spec.model)
    health = redis.hget("ollama:health", host)

    if not health.permits_inference():
        return await fallback(juror_spec, rendered_prompt, timeout,
                              reason="host_unhealthy")

    slots = slots_required(juror_spec.model)
    admitted = atomically_claim(host, slots,
                                ttl=cold_load_s + timeout)
    if not admitted:
        admitted = await queue_wait(host, slots, max_wait=30)
        if not admitted:
            return await fallback(juror_spec, rendered_prompt, timeout,
                                  reason="no_slot")
    try:
        return await local_call(host, juror_spec, rendered_prompt, timeout)
    finally:
        release(host, juror_spec.model)
```

---

## 5. Weighted Consensus & Multidimensional Scoring Algorithms

### 5.1 Why a scorecard

A binary supports/refutes vote was the right MVP, but the platform now has
*three* downstream consumers that all want more:

1. **Trust scoring (`recalculate_trust_v2`)** wants a confidence axis to
   distinguish "weakly attested" from "well-attested."
2. **Sitemap / retrieval router** wants methodological-rigor information to
   downrank trash papers without throwing out their topical hits.
3. **Frontend** wants four chips (Relevance, Entailment, Rigor, Confidence)
   to render a richer evidence card.

### 5.2 The four axes

| Axis | Definition | Range | Derived from juror? |
|---|---|---|---|
| **Relevance** (R) | Does the paper address the same physical question / observational subject as the claim? | 0.0–1.0 | Yes — explicit `RELEVANCE` tag |
| **Factual Entailment** (E) | Does the abstract actually entail the claim, not merely touch on it? | 0.0–1.0 | Yes — explicit `ENTAILMENT` tag; SUPPORTS = ≥ policy.support_threshold, REFUTES = ≤ −policy.refute_threshold |
| **Methodological Rigor** (M) | Is the paper's methodology adequate (sample size, controls, reproducibility) to settle the claim? | 0.0–1.0 | Yes — explicit `RIGOR` tag |
| **Confidence** (C) | How confident is the juror in its own judgment? | 0.0–1.0 | Yes — `CONFIDENCE: LOW|MEDIUM|HIGH` mapped to 0.33 / 0.66 / 1.00 |

The new `scorecard.v1.yaml` prompt instructs jurors to emit:

```
###VERDICT: <SUPPORTS|REFUTES|ABSTAIN>
###SENTENCE: <verbatim or NONE>
###RELEVANCE: <0.00-1.00>
###ENTAILMENT: <-1.00 to 1.00>          # signed: negative = refutes
###RIGOR: <0.00-1.00>
###CONFIDENCE: <LOW|MEDIUM|HIGH>
```

The VERDICT line remains because it is the lowest-common-denominator
backward-compatible signal; the four numeric axes are the new data of record.

### 5.3 Per-juror weights

Each juror has a `JuryAgentProfile` row (§6) with:

| Field | Meaning |
|---|---|
| `tier_weight` | Function of parameter count: 7B → 0.4, 14B → 0.7, 27–32B → 0.9, 70B → 1.0, 405B+ → 1.05. Capped at 1.05 to prevent giants from dominating. |
| `domain_weight` | 1.0 for astronomy-tuned (AstroSage, Atom); 0.85 for generalist; 0.7 for unrelated SLM. |
| `reliability_weight` | `agreed_jury_votes / max(total_jury_votes, 25)`, exponentially smoothed; defaults to 0.6 with prior. Drawn from existing `agents` table fields. |
| `calibration_temperature` | Per-axis Platt-scaling temperature learned from historical scorecards (`temperature = 1.0` initially). |

Per-juror raw weight:

```
w_raw(j) = tier_weight(j) * domain_weight(j) * reliability_weight(j)
```

Normalized within the jury batch:

```
w(j) = w_raw(j) / Σ_k w_raw(k)
```

### 5.4 Aggregation algorithm

For a jury batch `J = {j_1, ..., j_n}` returning scorecards
`s_j = (R_j, E_j, M_j, C_j)`, the consensus scorecard is:

```
R̄ = Σ_j w(j) * C_j * R_j  /  Σ_j w(j) * C_j
Ē = Σ_j w(j) * C_j * E_j  /  Σ_j w(j) * C_j     # signed
M̄ = Σ_j w(j) * C_j * M_j  /  Σ_j w(j) * C_j
```

Confidence is *not* itself confidence-weighted (avoiding the self-referential
loop); instead, ensemble confidence is:

```
C̄ = mean(C_j)                                    # central tendency
σ²_E = Σ_j w(j) * (E_j - Ē)²                     # disagreement on entailment

CON_index = C̄ * (1 - sqrt(σ²_E))                 # high when jurors agree confidently
```

Then the binary derived verdict (for backward compat / DB column `stance`)
is:

```
if Ē ≥ policy.support_threshold AND CON_index ≥ 0.50:
    stance = SUPPORTS
elif Ē ≤ -policy.refute_threshold AND CON_index ≥ 0.50:
    stance = REFUTES
else:
    stance = ABSTAIN
```

And the legacy `evidence.quality` scalar is replaced by:

```
quality_v2 = 0.35*R̄ + 0.40*|Ē| + 0.15*M̄ + 0.10*CON_index
```

This is fully backward compatible: `recalculate_trust_v2` already reads
`evidence.quality`, and the new value lives in `[0, 1]` like the old one.

### 5.5 Pseudocode

```python
def aggregate_scorecards(
    jurors: list[JurorScorecard],          # one per juror call
    policy: PolicySpec,
    profiles: dict[int, JuryAgentProfile], # by agent_id
) -> ConsensusScorecard:
    valid = [j for j in jurors if j.verdict != "ERROR"]
    if not valid:
        return ConsensusScorecard.empty(reason="no_jurors")

    raw_w = {j.agent_id: profile_weight(profiles[j.agent_id]) for j in valid}
    total = sum(raw_w.values()) or 1.0
    w = {aid: w_raw / total for aid, w_raw in raw_w.items()}

    c_sum = sum(w[j.agent_id] * j.C for j in valid)
    if c_sum == 0:
        return ConsensusScorecard.empty(reason="zero_confidence")

    R_bar = sum(w[j.agent_id] * j.C * j.R for j in valid) / c_sum
    E_bar = sum(w[j.agent_id] * j.C * j.E for j in valid) / c_sum
    M_bar = sum(w[j.agent_id] * j.C * j.M for j in valid) / c_sum

    C_mean = mean(j.C for j in valid)
    var_E = sum(w[j.agent_id] * (j.E - E_bar) ** 2 for j in valid)
    CON = C_mean * (1.0 - math.sqrt(min(1.0, var_E)))

    if E_bar >= policy.support_threshold and CON >= 0.50:
        stance = "supports"
    elif E_bar <= -policy.refute_threshold and CON >= 0.50:
        stance = "refutes"
    else:
        stance = "neutral"

    quality_v2 = 0.35 * R_bar + 0.40 * abs(E_bar) + 0.15 * M_bar + 0.10 * CON

    return ConsensusScorecard(
        relevance=R_bar,
        entailment=E_bar,
        rigor=M_bar,
        confidence=CON,
        stance=stance,
        quality=quality_v2,
        var_entailment=var_E,
        weights=w,
        jurors=valid,
    )
```

### 5.6 Calibration & monitoring

Every aggregated scorecard is logged to `jury_scorecards` (§6.3). A nightly
Celery task `recalibrate_juror_weights` reads the last 14 days of scorecards
and:

1. For each juror, computes its **bias** (mean deviation of its E from the
   ensemble E excluding itself).
2. Updates `reliability_weight` via exponential smoothing
   (α = 0.2): `new = 0.8*old + 0.2*observed`.
3. Fits a per-axis Platt-scaling temperature so individual juror outputs
   align with consensus.

Drift alarms fire if a juror's bias exceeds ±0.30 on the entailment axis
over a rolling 200-vote window — Papa is paged, juror is auto-demoted to
`weight=0` pending review.

### 5.7 What we keep for backward compat

- `evidence.stance` (`supports / refutes / neutral`) — derived from `Ē`.
- `evidence.quality` (float) — replaced by `quality_v2`.
- `evidence_votes` rows — still written per juror, with new optional columns
  (§6.2).
- `recalculate_trust_v2` — unchanged inputs. The richer scorecard feeds it
  through `evidence.quality` and a new `evidence.consensus_scorecard_id` FK.

---

## 6. Database Schema Additions

We add **three new tables** and **four columns**, all backward-compatible
with the existing trust / jury machinery.

### 6.1 New table: `prompt_revisions`

Audit trail for every materialized prompt+policy combination, so any vote
can be replayed against the exact text that produced it.

```sql
CREATE TABLE prompt_revisions (
    id             BIGSERIAL PRIMARY KEY,
    prompt_id      VARCHAR(80)   NOT NULL,        -- "stance.v2"
    policy_id      VARCHAR(80)   NOT NULL,        -- "strict_v1"
    prompt_sha256  CHAR(64)      NOT NULL UNIQUE, -- SHA of system+user merged
    system_text    TEXT          NOT NULL,
    user_template  TEXT          NOT NULL,
    aggregation    JSONB         NOT NULL,        -- thresholds from policy
    created_at     TIMESTAMPTZ   NOT NULL DEFAULT now()
);
CREATE INDEX idx_prompt_rev_prompt_policy ON prompt_revisions(prompt_id, policy_id);
```

### 6.2 New columns on `evidence_votes`

```sql
ALTER TABLE evidence_votes
    ADD COLUMN prompt_revision_id  BIGINT NULL REFERENCES prompt_revisions(id),
    ADD COLUMN relevance           REAL   NULL,             -- [0, 1]
    ADD COLUMN entailment          REAL   NULL,             -- [-1, 1]
    ADD COLUMN rigor               REAL   NULL,             -- [0, 1]
    ADD COLUMN confidence          REAL   NULL,             -- [0, 1]
    ADD COLUMN scheduled_via       VARCHAR(40) NULL,        -- "local|queued|fallback_cerebras"
    ADD COLUMN latency_ms          INTEGER NULL;

CREATE INDEX idx_evidence_votes_prompt_rev ON evidence_votes(prompt_revision_id);
```

The legacy `value` and `weight` columns remain — they continue to mean
"signed integer vote" and "reputation weight at vote time" — but new readers
should prefer the four-axis fields.

### 6.3 New table: `jury_scorecards`

The consensus output for an evidence item, one row per jury run.

```sql
CREATE TABLE jury_scorecards (
    id                  BIGSERIAL PRIMARY KEY,
    evidence_id         BIGINT NOT NULL REFERENCES evidence(id) ON DELETE CASCADE,
    prompt_revision_id  BIGINT NOT NULL REFERENCES prompt_revisions(id),
    relevance           REAL   NOT NULL,
    entailment          REAL   NOT NULL,
    rigor               REAL   NOT NULL,
    confidence          REAL   NOT NULL,
    var_entailment      REAL   NOT NULL,         -- juror disagreement
    quality_v2          REAL   NOT NULL,         -- denormalized for fast reads
    stance              VARCHAR(20) NOT NULL,    -- supports|refutes|neutral
    jurors_used         JSONB  NOT NULL,         -- list of {agent_id, model, weight, scheduled_via}
    policy_id           VARCHAR(80) NOT NULL,
    created_at          TIMESTAMPTZ NOT NULL DEFAULT now()
);
CREATE INDEX idx_jury_scorecards_evidence ON jury_scorecards(evidence_id, created_at DESC);
```

`evidence.consensus_scorecard_id` is added as a FK to the most recent row:

```sql
ALTER TABLE evidence
    ADD COLUMN consensus_scorecard_id BIGINT NULL REFERENCES jury_scorecards(id);
```

### 6.4 New table: `jury_agent_profiles`

The weight inputs for §5.3, separated from the `agents` table so they can be
recalibrated nightly without lock contention on the agents row.

```sql
CREATE TABLE jury_agent_profiles (
    agent_id                INTEGER PRIMARY KEY REFERENCES agents(id) ON DELETE CASCADE,
    tier_weight             REAL NOT NULL DEFAULT 0.7,    -- by parameter count
    domain_weight           REAL NOT NULL DEFAULT 0.85,   -- astronomy fit
    reliability_weight      REAL NOT NULL DEFAULT 0.6,    -- ensemble agreement rate
    calibration_temperature REAL NOT NULL DEFAULT 1.0,    -- Platt scaling
    fallback_chain          JSONB NOT NULL DEFAULT '[]',  -- ordered list of fallback juror_specs
    last_calibrated_at      TIMESTAMPTZ NULL,
    notes                   TEXT NULL
);
```

### 6.5 Alembic migration plan

A single migration file `add_jury_v2_scorecards.py`:

```python
revision = "j2v1"
down_revision = "p2trust1"

def upgrade():
    op.create_table("prompt_revisions", ...)
    op.add_column("evidence_votes", ... 6 columns)
    op.create_table("jury_scorecards", ...)
    op.add_column("evidence", sa.Column("consensus_scorecard_id", sa.BigInteger,
                                        sa.ForeignKey("jury_scorecards.id"),
                                        nullable=True))
    op.create_table("jury_agent_profiles", ...)
    op.execute("INSERT INTO jury_agent_profiles (agent_id) "
               "SELECT id FROM agents WHERE role = 'jury'")

def downgrade():
    # Pure additive — drops are safe.
    ...
```

No data is rewritten; all new columns are nullable; existing readers ignore
them by virtue of SQLAlchemy mapping.

---

## 7. Step-by-step Implementation & Rollout Plan

Four phases, **each independently shippable and reversible by feature flag.**
Tori executes them sequentially; HwaO and Kun review at the end of each
phase. The legacy jury keeps running until Phase 4 cuts over.

### Phase 0 — Pre-flight (½ day)

1. Confirm `pipeline_upgrade_design_v1.md §4.1` LMS is live and writing to
   `ollama:health` Redis hash. If not, this design depends on it landing
   first.
2. Snapshot the current Targeted-ADS jury hit rate (supports / refutes /
   neutral over the last 7 days) for comparison.
3. Tag the current state as `pre-jury-v2`.

### Phase 1 — Prompt Registry (1.5 days, Tori solo)

1. **Create** `app/services/prompt_registry.py` (`PromptRegistry`,
   `PromptSpec`, `PolicySpec`, `RenderedPrompt`) with YAML loader and
   SHA-256 hashing.
2. **Author** the initial six YAML files: `stance.v1.yaml` (verbatim copy of
   today's `JURY_SYSTEM_PROMPT`, frozen), `stance.v2.yaml` (new
   policy-parameterized), `entailment.v1.yaml`, `well_posed.v1.yaml`,
   `scorecard.v1.yaml`, plus `strict_v1.yaml` and `permissive_v1.yaml`.
3. **Wire** Alembic migration for `prompt_revisions` and the
   `evidence_votes` column additions. Run `upgrade head` on dev DB.
4. **Migrate** `targeted_ads_miner.py` to call `registry.render("stance.v2",
   ..., policy=settings.JURY_POLICY)`. Old constants kept behind
   `if settings.USE_PROMPT_REGISTRY else JURY_SYSTEM_PROMPT` for instant
   rollback. Default flag: `False` in prod, `True` in dev.
5. **Migrate** `retrieval_filter_v2.py` `evaluate_entailment_gate*` to use
   `entailment.v1`.
6. **Migrate** `well_posed_jury.py` to use `well_posed.v1`.
7. **Migrate** `tasks.py` `STANCE_JURY_SYSTEM` → `stance.v2`.
8. **Tests** (`tests/services/test_prompt_registry.py`): renders match
   golden files; SHA-256 deterministic; policy switch changes rendered text
   in the expected blocks; invalid variable raises.
9. **Ship + monitor.** Enable in dev for 24 h, then flip flag in prod.

**Exit criterion:** all four jury sites emit identical prompt text to
pre-Phase-1 when `policy=strict_v1`, byte-for-byte except trailing
whitespace (golden tests verify this); `prompt_sha256` appears on every new
`evidence_votes` row.

### Phase 2 — Inference Scheduler (2 days)

1. **Create** `app/config/inference/model_footprints.yaml` with the table
   from §4.3.
2. **Create** `app/services/inference_scheduler.py`
   (`InferenceScheduler`, `ModelFootprints`, `JurorSpec`,
   `JurorCallResult`). Redis ZADD-based admission, fallback chain,
   Prometheus counters.
3. **Refactor** `_call_juror` and `_call_one_async` to delegate scheduling
   to `InferenceScheduler.execute(...)`. **Critically:** the existing
   `asyncio.gather` over the jury batch *stays*; only each individual
   coroutine now goes through the scheduler. No call site loses
   parallelism for cloud jurors.
4. **Add** scheduler bypass flag `INFERENCE_SCHEDULER_ENABLED=true|false`
   for instant revert.
5. **Tests** (`tests/services/test_inference_scheduler.py`): two heavy
   models cannot both acquire slots when `num_parallel=2` and slots=2 each;
   queue wait works; fallback fires on `congested`; cloud jurors bypass;
   Redis loss degrades gracefully (admit all = legacy behavior).
6. **Soak** in dev under simulated load (replay last week's jury batches).
   Compare end-to-end latency p50/p95 with and without the scheduler. Goal:
   p95 ≤ pre-Phase-2; zero `httpx.ReadTimeout` over a 24 h soak.

**Exit criterion:** Prometheus counter `nm_jury_scheduler_fallback_total`
< 5 % of total juror calls under normal load; zero `ReadTimeout` errors in
the jury logs.

### Phase 3 — Scorecard & Weighted Consensus (2 days)

1. **Create** `app/services/jury_scorecard.py` (`JurorScorecard`,
   `ConsensusScorecard`, `aggregate_scorecards` per §5.5).
2. **Alembic** migration for `jury_scorecards`, `jury_agent_profiles`, and
   `evidence.consensus_scorecard_id`.
3. **Seed** `jury_agent_profiles`: bulk-insert one row per agent with
   `role='jury'`, with `tier_weight` filled from a model→tier lookup table
   keyed off `agents.model_name`.
4. **New prompt** `scorecard.v1.yaml` (extends `stance.v2` with the three
   numeric axis tags).
5. **Refactor** `aggregate_jury` in `targeted_ads_miner.py`: produce a
   `JurorScorecard` for each parsed result, then aggregate with the new
   service. Legacy binary `JuryDecision` is now a derived view over the
   `ConsensusScorecard`.
6. **Wire** `recalculate_trust_v2` to read `quality_v2` from the new
   scorecard (unchanged column name, new value).
7. **Frontend opt-in:** add `consensus_scorecard` block to the evidence
   response in `app/routers/claims.py` and `app/routers/jury.py`. Old
   `stance` / `quality` fields remain present.
8. **Nightly calibration task** `recalibrate_juror_weights` (Celery beat,
   03:30 KST). Initial run produces a baseline; subsequent runs apply
   exponential smoothing per §5.6.
9. **Tests:** scorecard math (golden cases); weighted consensus equivalent
   to legacy majority when all weights = 1.0; calibration converges on
   synthetic biased juror.

**Exit criterion:** every new `evidence_votes` row gets a populated
`(relevance, entailment, rigor, confidence)` tuple; every new evidence row
has a non-null `consensus_scorecard_id`; trust score recomputation matches
pre-Phase-3 to ±0.05 on the 5 low-health pages (no regression).

### Phase 4 — Cutover & Cleanup (1 day)

1. **Flip** `USE_PROMPT_REGISTRY=true` and
   `INFERENCE_SCHEDULER_ENABLED=true` and `JURY_SCORECARD_ENABLED=true` in
   prod simultaneously, after a 48 h dev soak.
2. **Decommission** the inline `JURY_SYSTEM_PROMPT`,
   `ENTAILMENT_PROMPT_TEMPLATE`, `STANCE_JURY_SYSTEM`, well-posed inline
   prompt, and the bare `asyncio.gather` jury batches. Replace with a
   `# Removed: see jury_system_upgrade_v1.md §3, §4` comment only where a
   reader will need it.
3. **Documentation:** update `AGENT_GUIDE.md`, `DESIGN_GUIDE.md`, and the
   jury-related Discord doc to point at this design.
4. **Frontend:** wire the four-axis chips into the evidence card. Confidence
   chip color graded by `CON_index` (green ≥ 0.7, amber 0.4–0.7, red < 0.4).
5. **Backfill** (optional): re-score the most recent 1 000 evidence items
   through the new pipeline, populating `jury_scorecards`. Run as a
   one-shot Celery task `backfill_scorecards_v2`, rate-limited to 60/min so
   it doesn't starve live jury calls.

**Exit criterion:** all four legacy jury code paths are gone; one prompt
registry; one inference scheduler; one consensus algorithm; one schema.
Calibration A/B can now be run by editing a single YAML file.

### Rollout Risk Register

| Risk | Likelihood | Mitigation |
|---|---|---|
| Prompt registry hot-reload races with in-flight calls | Low | Render is pure; in-flight call carries its `prompt_sha256` in the coroutine state |
| Scheduler over-throttles and drops jury throughput | Medium | `INFERENCE_SCHEDULER_ENABLED=false` flag; Prometheus alarm on queue_wait p95 > 30 s |
| Weighted consensus disagrees with legacy majority on edge cases | Medium | Phase 3 ships in shadow: both algorithms run; if `stance` differs > 5 % of the time, hold cutover |
| Calibration drift demotes a juror unfairly | Low | ±0.30 demotion threshold + Papa-paged before auto-demote; manual override possible by updating `jury_agent_profiles` directly |
| LMS not yet live | Hard dependency | Phase 0 gates Phase 2 on LMS availability |

---

## Appendix A — Mapping of Existing Files to New Components

| Existing file | New component | Status post-Phase-4 |
|---|---|---|
| `backend/scripts/targeted_ads_miner.py` | Uses `PromptRegistry`, `InferenceScheduler`, `aggregate_scorecards` | Refactored, ~200 LOC shorter |
| `backend/app/agent_loop/tasks.py` `_chat_parallel` | Each call delegates to `InferenceScheduler.execute` | Same surface, new internals |
| `backend/scripts/retrieval_filter_v2.py` | `evaluate_entailment_gate*` use registry | Surface preserved |
| `backend/app/agent_loop/research_ideas/well_posed_jury.py` | Uses registry + scheduler | Surface preserved |
| `backend/app/routers/jury.py` | Adds `consensus_scorecard` to responses; `cast_jury_vote` accepts an optional 4-axis body | Backward-compatible |
| `backend/app/models/jury.py` / `models/claim.py` | New columns + 3 new tables (§6) | Additive only |

## Appendix B — Open Questions for Papa

1. **Atom-7B residency.** `ollama_model_policy_v1.md` left this as
   conditional. The scheduler assumes Atom is *not* resident by default; if
   Papa pins it (`PIN_ATOM_ASTRONOMY_7B=true`), drop `slots_required("atom")`
   from 1 to 0 (Atom always available).
2. **Cloud-fallback policy.** Should fallback to Cerebras / Gemini /
   Sambanova be the *same* juror identity (same `agent_id`, different
   `scheduled_via`), or a distinct "JuryGeminiFallback" agent? Current
   design assumes same identity; flip if a separate audit trail is needed.
3. **Permissive policy gating.** §3.4 ships both `strict_v1` and
   `permissive_v1`. Which one is the default `JURY_POLICY` in prod
   post-rollout? Current proposal: `strict_v1` everywhere except
   well-posed-idea jury, which uses a custom `permissive_well_posed_v1`.
4. **Sampling-mode parallelism.** Some jurors (Mima Qwen3-30B) emit a
   noticeably better scorecard at `temperature=0.3, n=3` than at
   `temperature=0.6, n=1`. Should the scheduler grant a single juror
   multiple slots for self-consistency? Current design says no
   (parallelism budget belongs to the batch, not the juror); deferred to
   v2.

---

**End of design v1.**
