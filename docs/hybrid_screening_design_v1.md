# Hybrid Cloud-Local Fast-Screening Pass for `targeted_ads_miner` — Design v1

**Author:** Kun 🔬
**Date:** 2026-06-07 09:45 KST
**Status:** Draft for Tori implementation
**Live grounding:** Read against local repo on Mac Studio 2026-06-07. Code: `backend/scripts/targeted_ads_miner.py` (full read), `backend/app/utils/premium_dispatch.py`, `backend/app/config.py` (`BATCH_SAFE_MODELS`, premium caps), `backend/app/agent_loop/tasks.py` (`_chat_parallel`, Gemini client dict at :111). DB: Postgres `nebulamind` (Docker `nebulamind-postgres-1`, 127.0.0.1:5432) — `evidence` 11,567 rows.

---

## 1. Executive Summary

`targeted_ads_miner` runs a 3-model local GPU jury on every abstract that survives the deterministic pre-gate. The jury is the cost center: ~40 s/paper, serial across papers, ≈16 h to mine one large page. This design inserts a **cheap cloud fast-screen** between the existing deterministic `pre_gate()` and the expensive local jury. A batched Gemini 3.5 Flash call labels each abstract `KEEP`/`DISCARD`; only `KEEP` papers reach the local jury. Expected collapse: **16 h → ~15–50 min** depending on KEEP rate, at **< ₩400 (~$0.27)** cloud spend per full page. No new schema. The screen is **recall-biased** (false-DISCARD is the only dangerous error) and audited by a shadow sample.

**One correction to the task brief:** the live jury is **Mima + Nutty-Heavy + Atom-7B**, not "Pico" (`jury_models()`, miner lines ~330–360). Atom-7B is the astronomy classifier (`vanta-research/atom-astronomy-7b`). This design preserves that trio unchanged.

---

## 2. The Core Bottleneck

### 2.1 Where the time goes (live code)

The miner flow per claim (`retrieve_candidates` → `process_claim`):

1. `ads_search` returns ≤ `ROWS=8` papers (strict query, loosen if `< MIN_HITS=3`).
2. **Deterministic `pre_gate()`** keeps a paper only if it has an ID, an abstract, passes `EVIDENCE_REQUIRE_ARXIV`, has `term_overlap_count ≥ 2`, and is not already attached. This is free and already filters hard.
3. Survivors go to **`run_jury_async`**: 3 jurors (`Mima` qwen3:30b, `Nutty-Heavy` deepseek-r1:70b, `Atom-7B`) called via `asyncio.gather`. Within a paper the jurors run in parallel; **papers are processed serially** in the `for candidate in candidates` loop.

So wall-clock ≈ `N_jury_papers × max(juror_latency)`. With deepseek-r1:70b as the slow juror (`JURY_TIMEOUT_SECONDS=360`, typical 30–50 s), a page whose claims yield ~1,500 jury-bound abstracts costs ≈ 1,500 × 38 s ≈ **16 h**. This matches the reported figure.

### 2.2 Why the jury is overkill for most papers

The jury's job is **strict stance adjudication with verbatim-quote proof** (2-of-3 SUPPORTS, `MIN_SUPPORT_VOTES=2`). Most pre-gate survivors are topically adjacent but not genuine support — they ABSTAIN. Burning the full reasoning jury to reach ABSTAIN is the waste. A high-context cheap model can discard those in milliseconds-per-abstract amortized.

---

## 3. The Hybrid Solution

### 3.1 Insertion point (precise)

Insert the screen **after** `pre_gate()` survivors are collected and **before** the jury, at the page/batch level rather than per-paper. Rationale: the free deterministic pre-gate already kills obvious misses; paying cloud tokens upstream of it would waste budget. Run order:

```
ADS → pre_gate() [free] → CLOUD FAST-SCREEN [cheap, batched] → local jury [expensive] on KEEP only
```

Restructure: `process_claim` currently retrieves + juries one claim at a time. Add a **page-level collection phase** that gathers all `(claim_snapshot, candidate)` pairs across claims, screens them in batches, then runs the jury only on KEEP. This also unlocks paper-level jury concurrency (§6.3).

### 3.2 Batching contract

- Batch up to **`SCREEN_BATCH=25`** `(claim, abstract)` items per cloud call (tunable 20–50; 25 keeps each call < ~14k input tokens, safely inside Flash context and well clear of `max_tokens`).
- Group items by `claim_id` so the claim text is stated **once** per claim block, then list its abstracts — saves repeated claim tokens.
- Each item carries a caller-assigned integer `ref` (stable index into the candidate list), the paper title, year, and abstract truncated to `ABSTRACT_LIMIT=1800` chars (reuse the existing constant).

**Prompt skeleton** (system + user):

```
SYSTEM: You are a fast relevance pre-screener for an astronomy evidence pipeline.
For each (claim, abstract) pair decide if the abstract could plausibly SUPPORT or
REFUTE the claim's specific physical assertion. This is a RECALL gate, not a verdict:
when uncertain, choose KEEP. Only choose DISCARD when the abstract is clearly off-topic
or unrelated to the claim's specific mechanism/quantity. Do not require verbatim proof.
Return ONLY a JSON array, one object per ref, no prose.

USER:
CLAIM 1471: "<claim text, normalized, ≤600 chars>"
  [ref 0] "<title>" (2024) — <abstract ≤1800c>
  [ref 1] ...
CLAIM 1472: "..."
  [ref 7] ...

Return: [{"ref": 0, "pre_filter": "KEEP"}, {"ref": 1, "pre_filter": "DISCARD"}, ...]
```

### 3.3 Short-circuit logic

- Parse the JSON array; map `ref → pre_filter`.
- `DISCARD` → record the paper as `screened_out` (counter + optional ledger note), **skip jury entirely**.
- `KEEP` → forward to `run_jury_async` unchanged.
- **Fail-open:** if a `ref` is missing from the response, the JSON is malformed, or the cloud call errors/times out, default that item to **KEEP** (never silently drop a paper because the cheap screen failed). Log `screen_parse_fallback`.

### 3.4 Local jury on KEEP (unchanged semantics)

The jury, aggregation (`aggregate_jury`), verbatim-quote enforcement (`parse_juror`), `merge_eligible` rule, evidence insert (`insert_evidence`), and shadow validation (`execute_shadow_validation`) are **untouched**. The screen only changes *which* papers enter the jury, preserving all downstream trust guarantees.

---

## 4. Premium Dispatch & Budget Integration

### 4.1 Model choice routes around the premium gate (by design)

`gemini-3.5-flash` is in `BATCH_SAFE_MODELS` (`config.py:231`) and is `BATCH_SAFE_DEFAULT_MODEL`. In `dispatch_premium`, `model_tier()` returns `BATCH_SAFE`, so the function **returns immediately** before the whitelist, `N_PREMIUM=5` items cap, `PREMIUM_DISPATCH_ENABLED`, and rolling 24h/30d caps. The screen therefore runs at high volume without tripping premium controls — exactly the intended lane for batch-safe models.

**Ledger discipline:** still call `log_llm_spend(job_name="targeted_ads.fast_screen", model="gemini-3.5-flash", prompt_tokens=..., completion_tokens=...)` after each call. `_rolling_cost` only sums `tier IN ('PREMIUM','STANDARD')`, so BATCH_SAFE spend is **visible in the ledger but does not consume the premium budget**. This gives Papa an audit trail of screening cost without starving the premium pool.

### 4.2 Cost projection — 1,500 abstracts

Price (`MODEL_PRICE_TABLE`): `gemini-3.5-flash` = **140 KRW / 1M input, 560 KRW / 1M output**.

Batch 25 → **60 calls**. Per call: system ~250 tok + claim blocks + 25 abstracts × (~450 abstract + ~50 framing) ≈ **~13.5k input tok**; output JSON ~25 × ~15 tok ≈ **~400 tok**.

| Component | Tokens | KRW |
|---|---|---|
| Input | 60 × 13.5k = 810k | 810k/1M × 140 = **113** |
| Output | 60 × 400 = 24k | 24k/1M × 560 = **13** |
| **Subtotal** | | **≈ 126 KRW (~$0.09)** |
| With 3× safety margin (longer abstracts, retries) | | **≈ 380 KRW (~$0.27)** |

Both are far under the **₩2,000 / $1.50** gate. Even at `SCREEN_BATCH=20` (75 calls) the figure stays < ₩500.

---

## 5. Performance Projection

### 5.1 Screening phase

60 calls at ~2–4 s each. Run with bounded concurrency (e.g. 5 in flight via `asyncio.gather` over batches, mirroring `_chat_parallel`'s pattern): **≈ 1–2 min total**.

### 5.2 Jury phase — KEEP-rate sensitivity (honest range)

Local jury wall-clock is `N_keep × 38 s` ÷ paper-concurrency. The task's two anchors are mildly inconsistent ("save 95%" → ~48 min; "15–20 min" → ~98%); I reconcile them explicitly rather than quoting one:

| KEEP rate | N_keep (of 1,500) | Serial (1×) | 3-way paper concurrency |
|---|---|---|---|
| 15 % | 225 | ~2.4 h | **~48 min** |
| 8 % | 120 | ~76 min | **~25 min** |
| 5 % | 75 | ~48 min | **~16 min** |

**To hit the 15–20 min target requires both (a) KEEP ≈ 5 % and (b) ~3-way paper-level jury concurrency.** The restructure in §3.1 already collects all candidates first, so adding a bounded `asyncio.Semaphore(3)` around `run_jury_async` is a small, safe change (RAM permitting — deepseek-r1:70b is the binding resource; verify GPU headroom before raising concurrency above 2). Recommend shipping with **concurrency=2** first, measuring the real KEEP rate on page 57, then tuning.

### 5.3 End-to-end

Screening (~2 min) + jury (16–48 min) = **~18–50 min/page**, vs 16 h. The dominant variable is the measured KEEP rate; everything else is bounded.

---

## 6. Quality Gates & Risks

### 6.1 False-DISCARD is the only dangerous error (lead concern)

A wrongly-DISCARDed paper is **invisible**: it never reaches the jury, so a real supporting paper is silently lost and the claim looks less supported than it is. This is strictly worse than a false-KEEP (which the strict jury catches by ABSTAIN). Mitigations:

1. **Recall-biased prompt** — "when uncertain, KEEP" (§3.2). The screen's job is to remove *clearly* off-topic papers only.
2. **Shadow audit** — sample **K=20 DISCARDs per run** (or 2 %, whichever larger) and run them through the full jury anyway. Record `false_discard_rate` = (DISCARDs that would have been `merge_eligible`) / sampled. Alert if > 2 %.
3. **Abort gate** — if a calibration run shows `false_discard_rate > 5 %`, disable the screen (env flag `TARGETED_ADS_FAST_SCREEN_ENABLED=false`) and fall back to jury-on-all-pre-gate-survivors. The screen must be a pure accelerator, never a correctness regression.

### 6.2 Fail-open everywhere

Cloud error, timeout, malformed JSON, or missing `ref` → that paper defaults to **KEEP**. The pipeline degrades to current behavior (slower, never wrong) under cloud failure.

### 6.3 No double-counting / idempotency

The screen adds a counter `screened_out` to the run totals; it does not write evidence. Re-running is safe (deterministic pre-gate's `already_attached` still guards inserts).

---

## 7. Platoon Assignment

| Step | Owner | Host | Why | Cost |
|---|---|---|---|---|
| Fast-screen batched call | **Gemini 3.5 Flash** (BATCH_SAFE) | Cloud | High context, cheap, JSON-clean, routes around premium gate | ~₩130/page |
| Local jury (Mima + Nutty-Heavy + Atom-7B) | local Ollama | Mac Studio | Strict stance + verbatim proof; unchanged | $0 |
| Restructure + screen integration + concurrency | **Tori** | Mac Studio | Deterministic refactor, testable | Cloud-paid |
| Shadow false-discard audit + calibration | **Kun** | Mac Studio | Threshold tuning, correctness gate | Cloud-paid |
| Cost-ledger review | HwaO | — | Confirms BATCH_SAFE spend stays logged & off premium budget | — |

### 7.1 Hardware note

All inference is local on Mac Studio except the Flash screen. deepseek-r1:70b (Nutty-Heavy) is the GPU-binding juror; do not raise paper-level jury concurrency past what VRAM allows (start at 2, measure). The screen itself adds no local GPU load.

---

## 8. Implementation Checklist for Tori (10 steps)

1. **Config:** add `TARGETED_ADS_FAST_SCREEN_ENABLED: bool = True`, `SCREEN_BATCH: int = 25`, `SCREEN_CONCURRENCY: int = 5`, `JURY_PAPER_CONCURRENCY: int = 2` to `config.py` (env-overridable).
2. **Cloud client:** add a `screen_models()` helper returning the Gemini dict shape used at `tasks.py:111` (`base_url=https://generativelanguage.googleapis.com/v1beta/openai`, `api_key=settings.GEMINI_API_KEY`, `model="gemini-3.5-flash"`, `max_tokens=2048`).
3. **Refactor `process_claim` → two phases:** (a) `collect_candidates(claims)` returns all `(claim_snapshot, candidate)` pairs; (b) screen; (c) jury on KEEP. Keep the single-claim path working when the flag is off.
4. **Build batches:** group candidates by `claim_id`, chunk to `SCREEN_BATCH`, assign stable `ref` indices, truncate abstracts to `ABSTRACT_LIMIT`.
5. **`fast_screen_async(batches)`:** bounded-concurrency Gemini calls; parse JSON array; build `ref → KEEP/DISCARD`; **fail-open to KEEP** on any error/missing ref; `log_llm_spend("targeted_ads.fast_screen", "gemini-3.5-flash", ...)` per call.
6. **Short-circuit:** filter candidates to KEEP; increment `totals["screened_out"]`; pass KEEP list to the jury phase unchanged.
7. **Jury concurrency:** wrap `run_jury_async` calls in `asyncio.Semaphore(JURY_PAPER_CONCURRENCY)`; preserve serial-commit semantics (commit per inserted evidence as today).
8. **Shadow audit hook:** with prob = max(20/N, 0.02), also jury a DISCARD sample; record `false_discard` when a DISCARD would have been `merge_eligible`; print to run totals JSON.
9. **CLI flags:** `--no-fast-screen` (force off), `--screen-batch N`, `--screen-audit-frac F`. Default run uses the screen.
10. **Tests + calibration:** `tests/targeted_ads/test_fast_screen.py` (batch build, JSON parse, fail-open, ref mapping); then a **dry calibration on page 57** (`--no-commit`) reporting KEEP rate, screen cost, and shadow false-discard rate. Hand results to Kun before enabling commit at scale.

---

## 9. Final Position

The bottleneck is spending strict-jury GPU time to reach ABSTAIN on topically-adjacent papers. A recall-biased, batched, BATCH_SAFE cloud screen removes that waste for cents per page and routes cleanly around the premium budget while staying ledger-visible. The single risk that matters is **false-DISCARD**, and it is contained by a KEEP-biased prompt, a shadow audit, fail-open behavior, and a hard abort gate — so the screen can only make the miner faster, never less correct. Ship with conservative concurrency (2) and a real page-57 KEEP-rate measurement before scaling.

— 🔬 Kun
