# Platoon Realignment v2 — Nutty-Heavy (deepseek-r1:70b) Integration

**Date:** 2026-06-07
**Owner:** Kun (architect) → HwaO (review) → Tori (implementer)
**Status:** Design — pre-implementation
**Supersedes:** None (extends `buddle_70b_realignment_v1.md`, 2026-06-06)
**Predicate:** `deepseek-r1:70b` is pulled and resident on Mac Studio (`ollama list` confirms 42 GB, modified 2026-06-07 ~00:13 KST).

---

## 1. Executive Summary / TL;DR

We are integrating `deepseek-r1:70b` (callsign **Nutty-Heavy**) into Tier 1 of NebulaMind's local-inference platoon as a **dedicated reasoning juror** in the 3-model evidence jury (`backend/scripts/targeted_ads_miner.py`) and as a future option for any task that benefits from explicit Chain-of-Thought (CoT) entailment.

**One-paragraph rationale.** Our 3-model jury currently runs `qwen3:30b` (Mima) + `llama3.3:70b` (Buddle/Blanc, after the 2026-06-06 405B downshift) + `vanta-research/atom-astronomy-7b` (Pico). Mima provides medium-context consensus; Pico provides astronomy-domain priors. The Buddle slot is held by a *generalist* 70B that contributes "second 70B vote" but no qualitatively different reasoning. **`deepseek-r1:70b` brings explicit CoT entailment** — exactly the capability stance-jury work rewards. Swapping Buddle → Nutty-Heavy in the jury raises adversarial robustness without changing VRAM footprint (both are 42 GB, both heavy-tier, both on `studio` host).

**Three concrete deliverables in this doc:**
1. Nutty-Heavy assumes the **heavy juror** seat in `targeted_ads_miner.py` (Buddle keeps its name and role as the general-purpose 70B drafter elsewhere; the jury slot is no longer named "Buddle").
2. A **unified `<think>` stripping standard** at the InferenceScheduler boundary so no downstream parser ever sees DeepSeek-R1 reasoning traces. Existing `strip_think_blocks` in `app/services/llm_utils.py` is extended to handle unclosed tags, `<thinking>` variants, and is invoked uniformly.
3. **InferenceScheduler footprint + advisory-lock calibration** that admits Nutty-Heavy alongside Mima + Pico + (optionally) Blanc without re-introducing the 405B-era thrash that triggered yesterday's emergency 70B downshift.

**Why not redirect existing Buddle/Blanc work to Nutty-Heavy entirely?** R1's `<think>` reasoning makes it ~2–3× slower at the same context size, bloats token counts, and is wasted on prose drafting (e.g. wiki sections, newsletters). Keep Buddle/Blanc on prose; promote Nutty-Heavy where reasoning quality is the binding constraint.

---

## 2. Nutty-Heavy Capability & Role Evaluation

### 2.1 Why Tier 1, and why specifically the jury

Three candidate roles were considered:

| Candidate role | Verdict | Why |
|---|---|---|
| **A. Replace Buddle/Blanc as default generalist (`NM_BUDDLE_MODEL`)** | ❌ Reject | R1's CoT bloat (2–3× more output tokens, longer wallclock) hurts every prose call. Generalist drafting does not benefit from explicit reasoning. |
| **B. Replace Pico for astronomy scoring** | ❌ Reject | Pico is 7B / 5 GB / sub-second and handles batch volume. Nutty-Heavy at 42 GB and 5–10 s/call would erase the relevance-scoring throughput budget for ~zero quality lift on simple alignment tasks. |
| **C. Heavy juror in `targeted_ads_miner.py` 3-model stance jury** | ✅ **Adopt** | Stance-jury accuracy is bottlenecked by adversarial entailment — exactly what CoT models are trained for. Footprint matches Buddle/Blanc (42 GB, same host, same tier). Loop cadence (10 min) tolerates per-pass 10–30 s easily. |

**Capability vs. speed vs. cost trade-off.** The jury runs three jurors in parallel inside one Celery task. The slowest juror dominates wallclock. Mima at 30B already takes ~45 s per call; Nutty-Heavy at 70B + CoT is expected at ~50–90 s. So Nutty-Heavy increases jury wallclock by ~10–40 s per candidate but adds an entirely independent reasoning signal that strict-mode AstroSage-style support detection has historically missed. The 10-minute autowiki cadence and `--limit` claim quotas absorb this comfortably. The 240-s `InferenceScheduler` advisory-lock wait already covers it.

### 2.2 Concrete role assignment (final)

| Slot | Before (2026-06-06 post-downshift) | After (this doc) |
|---|---|---|
| Jury Slot 1 (consensus / medium-context) | `qwen3:30b` — Mima | `qwen3:30b` — Mima (unchanged) |
| Jury Slot 2 (heavy / reasoning) | `llama3.3:70b` — Buddle (label) | **`deepseek-r1:70b` — Nutty-Heavy** |
| Jury Slot 3 (astronomy domain) | `vanta-research/atom-astronomy-7b` — Pico | `vanta-research/atom-astronomy-7b` — Pico (unchanged) |

Buddle (the 70B generalist) is **not removed from the platoon** — it remains the default for `NM_BUDDLE_MODEL` consumers (autowiki tick generalist drafting, newsletter prose, second-opinion synthesis). It is only displaced from the *jury* seat.

---

## 3. The DeepSeek `<think>` Tag Parsing Standard

### 3.1 The threat model

DeepSeek-R1 (all sizes) emits explicit reasoning traces wrapped in `<think>...</think>` before the actual answer. Three failure modes can break our jury:

1. **VERDICT regex picks up the wrong line.** Our jury system prompt instructs the model to end with `###VERDICT: <SUPPORTS|REFUTES|ABSTAIN>`. If R1 writes "I'm going to vote ###VERDICT: SUPPORTS" inside its `<think>` block and then "###VERDICT: ABSTAIN" outside, `targeted_ads_miner.parse_juror._last_match` saves us. But if the model only writes the verdict line *inside* `<think>` (truncation, formatting drift), the parser fails or — worse — extracts a misleading verdict. The `_last_match` helper at `targeted_ads_miner.py:480-482` is a partial defense, not a complete one.
2. **`response_text_union` re-injects reasoning.** `targeted_ads_miner.py:394-412` explicitly concatenates the `thinking` and `reasoning_content` fields from the OpenAI-compatible response into the parse stream. This is *worst-case behavior* for a CoT model: it guarantees every regex sees the full reasoning trace, including any draft verdicts the model considered and rejected.
3. **JSON parsers downstream.** Any future caller that does `json.loads(content)` against R1 output will reliably fail because `<think>...</think>` is not JSON.

### 3.2 The standard: strip at the scheduler boundary, defense-in-depth at the call site

**Rule 1 — `InferenceScheduler._make_http_call` strips before returning.** This is the canonical chokepoint for local Ollama calls. Every downstream caller gets clean text. Cloud calls (Claude, Gemini, GPT) are unaffected because they don't emit `<think>`. Implementation: post-extract the assistant message content, run it through `strip_think_blocks`, return the cleaned string.

**Rule 2 — `targeted_ads_miner.response_text_union` no longer concatenates `thinking` / `reasoning_content`.** Those fields are *provider-side leakage of the reasoning trace*; they are not assistant output. Drop them. Only `choices[*].message.content` and `choices[*].text` are user-facing.

**Rule 3 — `parse_juror` defensively re-strips before regex.** Belt-and-suspenders. Cheap (single regex) and catches the case where a different code path bypassed the scheduler.

**Rule 4 — `strip_think_blocks` is extended** to handle three production failure modes the current implementation misses.

### 3.3 The hardened `strip_think_blocks`

Current implementation at `backend/app/services/llm_utils.py:6-13` only strips closed `<think>...</think>` pairs. Extend to:

```python
# backend/app/services/llm_utils.py
"""Shared helpers for local and hosted LLM responses."""
from __future__ import annotations

import re

# Match <think>…</think> or <thinking>…</thinking>, case-insensitive, dot-all.
_THINK_BLOCK_RE = re.compile(
    r"<think(?:ing)?>.*?</think(?:ing)?>",
    re.DOTALL | re.IGNORECASE,
)

# Match an UNCLOSED <think> that runs to end-of-string (truncated CoT, common
# when the model hits max_tokens mid-reasoning). Without this, an unclosed
# think block leaks the entire reasoning trace into downstream parsing.
_UNCLOSED_THINK_RE = re.compile(
    r"<think(?:ing)?>.*\Z",
    re.DOTALL | re.IGNORECASE,
)

# Match a leading JSON markdown fence the model sometimes wraps structured
# output in: ```json ... ``` or ``` ... ```.
_JSON_FENCE_RE = re.compile(
    r"^\s*```(?:json)?\s*(.*?)\s*```\s*\Z",
    re.DOTALL | re.IGNORECASE,
)


def strip_think_blocks(text: str | None) -> str:
    """Remove DeepSeek/Qwen-style reasoning traces.

    Handles three production cases:
      1. Closed `<think>…</think>` (the original case).
      2. Closed `<thinking>…</thinking>` variant emitted by some prompt
         configurations.
      3. Unclosed `<think>` that runs to end-of-text (token truncation).
    """
    if not text:
        return ""
    cleaned = _THINK_BLOCK_RE.sub("", text)
    cleaned = _UNCLOSED_THINK_RE.sub("", cleaned)
    return cleaned.strip()


def clean_llm_response(text: str | None) -> str:
    """Canonical wrapper for any local LLM response before parsing.

    Order matters: strip reasoning first (it may itself contain code fences
    the model considered then discarded), THEN strip a single outer JSON
    fence if present. Use this at every parse site that consumes the
    `choices[0].message.content` field.
    """
    cleaned = strip_think_blocks(text)
    m = _JSON_FENCE_RE.match(cleaned)
    if m:
        cleaned = m.group(1).strip()
    return cleaned
```

### 3.4 Where to apply it

| Call site | Action |
|---|---|
| `app/services/inference_scheduler.py::InferenceScheduler._make_http_call` (line 304 — the `return content`) | Wrap: `return strip_think_blocks(content)` |
| `scripts/targeted_ads_miner.py::response_text_union` (lines 394–412) | Remove the `thinking` / `reasoning_content` keys from the concat list; wrap the final return value in `strip_think_blocks` |
| `scripts/targeted_ads_miner.py::parse_juror` (line 485 entry) | Re-strip defensively: `raw = strip_think_blocks(raw)` as the first line |
| Any future `json.loads` against local-model output | Use `clean_llm_response` instead of bare `strip_think_blocks` |

### 3.5 Acceptance test for the parser standard

Unit tests (add to `backend/tests/test_llm_utils.py`):

```python
import pytest
from app.services.llm_utils import strip_think_blocks, clean_llm_response

def test_strip_closed_think_block():
    raw = "<think>chain of thought</think>###VERDICT: SUPPORTS"
    assert strip_think_blocks(raw) == "###VERDICT: SUPPORTS"

def test_strip_thinking_variant():
    raw = "<thinking>...</thinking>final answer"
    assert strip_think_blocks(raw) == "final answer"

def test_strip_unclosed_think_block():
    # Truncated CoT mid-reasoning — must NOT leak the reasoning trace.
    raw = "<think>I am thinking but ran out of tokens"
    assert strip_think_blocks(raw) == ""

def test_strip_multiple_think_blocks():
    raw = "<think>a</think>middle<think>b</think>end"
    assert strip_think_blocks(raw) == "middle\nend".replace("\n", "")

def test_strip_decoy_verdict_inside_think_does_not_survive():
    raw = (
        "<think>tentatively ###VERDICT: REFUTES, but reconsidering</think>"
        "###VERDICT: SUPPORTS\n###SENTENCE: NONE\n###CONFIDENCE: HIGH"
    )
    out = strip_think_blocks(raw)
    assert "REFUTES" not in out
    assert "###VERDICT: SUPPORTS" in out

def test_clean_llm_response_unwraps_json_fence():
    raw = "<think>x</think>```json\n{\"a\": 1}\n```"
    assert clean_llm_response(raw) == '{"a": 1}'
```

---

## 4. VRAM Footprint & InferenceScheduler Calibration

### 4.1 Add Nutty-Heavy to `ModelFootprints.FOOTPRINTS`

Insert into `backend/app/services/inference_scheduler.py` immediately after the `llama3.3:70b` entry:

```python
"deepseek-r1:70b": {
    "host": "studio",
    "tier": "heavy",
    "vram_gb": 42,
    "slots": 1,
    "cold_load": 30,
},
```

This sits on the **same host (`studio`) and same tier (`heavy`)** as `llama3.3:70b` and `astrosage-70b`, which means it shares the existing advisory lock `ollama:lock:studio:heavy`. **This is intentional** — only one heavy-tier 70B+ should be actively generating at any moment on Mac Studio to avoid the swap/thrash that killed the 405B-as-Buddle experiment. The serialization is correct.

### 4.2 Updated Mac Studio co-residency map

The driving constraint remains the ~256 GB practical VRAM budget on Mac Studio (out of 512 GB unified, with Celery + OS + Postgres + Redis taking the rest). Heavy-tier serialization (one of {Blanc, AstroSage-70B, Nutty-Heavy} actively generating at a time) keeps us inside it.

| Scenario | Co-resident models | Est. peak VRAM | Verdict |
|---|---|---|---|
| Idle baseline | Mima + Pico + Nutty (14B) | ~32 GB | ✅ |
| Standard 3-model jury (this design's target state) | Mima + Pico + Nutty-Heavy (one heavy active) | ~65 GB | ✅ |
| Jury + autowiki drafter (Blanc swap-in) | Mima + Pico + Nutty-Heavy + Blanc (alternating) | ~107 GB serialized, ~65 GB at any instant | ✅ — serialized by `ollama:lock:studio:heavy` |
| Jury + AstroSage synthesis (alternating) | Mima + Pico + Nutty-Heavy + AstroSage-70B (alternating) | ~107 GB serialized | ✅ — serialized by lock |
| ⚠️ Three 70B+ simultaneous | Nutty-Heavy + Blanc + AstroSage-70B concurrent | ~126 GB + Celery | ❌ Forbidden by advisory lock (only one heavy-tier holds the lock at a time) |
| ⚠️ Buddle escalation to 405B + jury | `llama3.1:405b` + Mima + Pico + Nutty-Heavy | ~410 GB | ❌ Forbidden — explicit human-initiated only per `buddle_70b_realignment_v1.md`; do not run during a jury cycle |

**Cold-load tax.** First-call latency: Nutty-Heavy ~30 s (matches Blanc/AstroSage at 70B). Steady-state: 5–10 s per pass. Budgeted for under the 180 s jury timeout in `targeted_ads_miner.py:JURY_TIMEOUT_SECONDS`.

### 4.3 Advisory-lock behavior under this design

The current `InferenceScheduler.execute` at `inference_scheduler.py:120-206`:

- Acquires `ollama:lock:studio:heavy` for heavy and medium tiers (line 163).
- TTL = `cold_load + timeout` (line 164) — for Nutty-Heavy that's `30 + 180 = 210 s`, well above expected per-pass latency.
- Waits up to **240 s** for the lock (line 171) — sufficient for one previous Blanc or AstroSage to finish.
- Falls back to Gemini-flash on timeout (line 191 → `_execute_fallback`).

**Conclusion: no scheduler config change beyond the FOOTPRINTS dict entry is required.** The existing locking shape was designed exactly for this case (multiple 70B models, one host, one slot).

### 4.4 Concurrency interaction with the rest of the jury

Mima (medium tier, qwen3:30b) **also takes `ollama:lock:studio:heavy`** because of the `tier in ("heavy", "medium")` check at line 163. Pico (light tier, atom-7b) does **not** take the lock. So a jury call executes:

1. Mima acquires → runs → releases (≈45 s)
2. Nutty-Heavy acquires → runs → releases (≈50–90 s)
3. Pico runs concurrently with both of the above (no lock)

Total wallclock dominated by `max(Mima, Nutty-Heavy) + Pico_overlap ≈ 60–95 s`. Well under the 180 s timeout.

---

## 5. Unified Platoon Roster & Task Assignments

This section is the source for the corresponding update to `~/.openclaw/workspace/memory/platoon-roster.md`. Diff intent (not literal file diff):

### 5.1 New roster entry

```markdown
### 🧠 Nutty-Heavy _(NEW — 2026-06-07)_
- **Machine:** Mac Studio (deepseek-r1:70b via Ollama at localhost:11434)
- **Primary role:** Heavy reasoning juror — explicit chain-of-thought for adversarial entailment in 3-model stance jury (`targeted_ads_miner.py`)
- **Best for:** Stance-jury heavy seat, factual coherence passes that need explicit reasoning, single-shot adversarial review of a difficult claim/abstract pair
- **Avoid:** Prose drafting (use Buddle/Blanc — R1 inflates token counts with `<think>` traces); high-volume relevance scoring (use Pico — 7B is 8× faster); structured JSON without `clean_llm_response` post-processing
- **Speed/Cost:** Medium-slow (5–10 s per pass, 30 s cold-load) / Free (local)
- **Hardware footprint:** ~42 GB on Mac Studio. Shares the `ollama:lock:studio:heavy` advisory lock with Blanc and AstroSage-70B — serialized one-at-a-time across these three.
- **Parser requirement:** All callers MUST consume responses via `InferenceScheduler` or call `app.services.llm_utils.strip_think_blocks` / `clean_llm_response` before parsing. Bypassing this WILL break VERDICT regex and JSON parsers.
- **Config keys:** `TARGETED_ADS_BUDDLE_MODEL=deepseek-r1:70b` in `backend/.env` to activate as jury heavy seat (replaces Buddle label; the variable name is historical).
- **Note:** Disambiguation from Nutty (deepseek-r1:14b): "Nutty" remains the fast 14B reasoner for hero-fact generation; "Nutty-Heavy" is the 70B reasoner for jury work.
```

### 5.2 Updated routing table additions

| Decision | Route to |
|---|---|
| 3-model stance jury (heavy seat) | **Nutty-Heavy** |
| Adversarial single-claim entailment review | **Nutty-Heavy** |
| Reasoning-heavy passes that fit in 70B context | **Nutty-Heavy** (if Rakon cold-load is unacceptable) |
| Quick CoT for hero facts | **Nutty** (14B, unchanged) |

### 5.3 Updated RAM footprint table addition

| Model | Host | Est. RAM | Cold-load |
|---|---|---|---|
| Nutty-Heavy (deepseek-r1:70b) | Mac Studio | ~42 GB | ~30 s |

### 5.4 Updated co-existence forbidden list

- ❌ Nutty-Heavy + Blanc + AstroSage-70B concurrently active → ~126 GB + Celery → advisory lock prevents this; do not force-bypass.
- ❌ Nutty-Heavy + `llama3.1:405b` escalation in same Celery window → ~286 GB → schedule 405B work off-cycle from any jury run.

---

## 6. Step-by-step Tori Implementation Plan

All steps are dry-run by default. Each ends with a verifiable observation. No DB migration required.

### Step 1 — Add scheduler footprint
**File:** `backend/app/services/inference_scheduler.py`
**Change:** Insert the `deepseek-r1:70b` dict entry into `ModelFootprints.FOOTPRINTS` (see §4.1).
**Verify:** Python REPL — `from app.services.inference_scheduler import ModelFootprints; print(ModelFootprints.get_info("deepseek-r1:70b"))` returns the dict.

### Step 2 — Harden `strip_think_blocks` and add `clean_llm_response`
**File:** `backend/app/services/llm_utils.py`
**Change:** Replace current content with the hardened version in §3.3.
**Verify:** Add the six tests from §3.5 to `backend/tests/test_llm_utils.py` and run `pytest backend/tests/test_llm_utils.py -v`. All six pass.

### Step 3 — Strip `<think>` at the scheduler boundary
**File:** `backend/app/services/inference_scheduler.py`
**Change:** At line 304 (`return content`), replace with:
```python
from app.services.llm_utils import strip_think_blocks
return strip_think_blocks(content)
```
(Hoist the import to module top.)
**Verify:** Manual one-shot — call `InferenceScheduler().execute({"model": "deepseek-r1:70b", "base_url": "http://localhost:11434/v1", "api_key": "ollama"}, "Output ###VERDICT: SUPPORTS", 60)` from a Python script; returned string contains no `<think>` substring.

### Step 4 — Remove `thinking`/`reasoning_content` leakage in jury parser
**File:** `backend/scripts/targeted_ads_miner.py`
**Change:** In `response_text_union` (lines 394–412):
- Drop `"thinking"` from the top-level keys loop.
- Drop `"reasoning_content"` and `"thinking"` from the per-choice loop.
- Wrap final `"\n".join(parts)` in `strip_think_blocks(...)`.

In `parse_juror` (line 485): add `raw = strip_think_blocks(raw)` as the very first line of the function body. (Defense-in-depth — the scheduler already stripped, but the `_call_juror` non-scheduler path at lines 431–463 may bypass.)

**Verify:** Run `pytest backend/tests/ -k jury` — no regression. Then manual: feed `parse_juror` a synthetic raw string with `<think>###VERDICT: REFUTES</think>###VERDICT: SUPPORTS\n###SENTENCE: ...` and confirm output verdict is `SUPPORTS`.

### Step 5 — Wire Nutty-Heavy into the jury via env override
**File:** `backend/.env`
**Change:** Add line `TARGETED_ADS_BUDDLE_MODEL=deepseek-r1:70b`.
**Note:** No code change — the `jury_models()` function at `targeted_ads_miner.py:365-391` already reads this env var (line 383). The variable name is historical; the *label* sent to the DB / jury aggregator remains `"Buddle"` for now to avoid breaking `Agent` row history (renamed in Step 7).
**Verify:** `python -c "from scripts.targeted_ads_miner import jury_models; import json; print(json.dumps(jury_models(), indent=2))"` — second entry's `model` is `deepseek-r1:70b`.

### Step 6 — End-to-end dry-run on 3 claims
**Command:** `cd backend && python scripts/targeted_ads_miner.py --page-id 57 --limit 3` (no `--commit`, so read-only).
**Verify:** stdout shows three claims processed; for each candidate, jury line of the form `jury stance=... quality=... [Mima:..., Buddle:..., Atom-7B:...]` where the `Buddle:` slot's verdict is a real `SUPPORTS|REFUTES|ABSTAIN` (not empty, not raw `<think>` text). Check Redis for `ollama:lock:studio:heavy` — no orphaned lock at end of run.

### Step 7 — Rename the jury slot label (optional, cosmetic)
**File:** `backend/scripts/targeted_ads_miner.py:380` (`"label": "Buddle"`).
**Change:** `"Buddle"` → `"Nutty-Heavy"`. **Side effect:** `agent_id_for_label` (line 564) will create a new `Agent` row `TargetedADS-Nutty-Heavy` rather than reuse the existing `TargetedADS-Buddle`. Historical EvidenceVote rows under the Buddle agent_id remain valid — they were that model at that point in time. Tori must confirm with HwaO before running so jury weight profiles in `jury_scorecard.py` get the new agent_id seeded.
**Verify:** First post-rename run creates the new Agent row; check `SELECT id, name FROM agents WHERE name LIKE 'TargetedADS-%'`.

### Step 8 — Acceptance smoke (15-min observation window)
**Command:** Tail `tail -F /tmp/celery-autowiki.log` (or the appropriate log path) while a normal autowiki cycle runs (or trigger `celery -A app.tasks call ...` for the targeted-ads task).
**Acceptance criteria:**
- ✅ Zero lock timeouts (`Lock acquisition timed out` does NOT appear in logs).
- ✅ Zero `Fallback triggered for deepseek-r1:70b` lines.
- ✅ At least one jury cycle completes within 180 s wallclock end-to-end.
- ✅ At least one Nutty-Heavy verdict is parsed (Mima, Nutty-Heavy, Pico all return a `SUPPORTS|REFUTES|ABSTAIN`, none `None`).
- ✅ No `<think>` substring leaks into any DB column (spot-check `EvidenceVote.reason` for the most recent inserted vote).

### Step 9 — Roster propagation
**Owner:** HwaO updates `~/.openclaw/workspace/memory/platoon-roster.md` per §5 of this doc (done in same commit as the design doc itself in this realignment).

### Rollback path
If Nutty-Heavy proves to break jury quality (e.g. over-confident SUPPORTS rate spikes, lock timeouts re-emerge):
```diff
- TARGETED_ADS_BUDDLE_MODEL=deepseek-r1:70b
+ TARGETED_ADS_BUDDLE_MODEL=llama3.3:70b
```
followed by `launchctl kickstart -k system/com.nebulamind.celery-autowiki`. No code change. Footprint dict entry can stay (no cost). `strip_think_blocks` hardening should NOT be rolled back regardless — it benefits Rakon and Nutty (14B) calls today.

---

## Appendix A — Why we didn't pick a different parser strategy

Two alternatives were considered and rejected:

1. **"Ask DeepSeek to skip `<think>` blocks via system prompt."** Empirically unreliable. R1 was trained with mandatory reasoning emission; prompt-based suppression succeeds intermittently and fails silently. Strip-at-boundary is more robust.
2. **"Parse with a JSON-mode forced schema."** Ollama's OpenAI-compatible endpoint does not enforce `response_format: json_object` against R1's `<think>` prefix (the prefix is emitted before the JSON, so the response is "not valid JSON" but Ollama returns it anyway). The existing free-text VERDICT format is more forgiving.

## Appendix B — Open question for HwaO

The `targeted_ads_miner.py` jury label remains "Buddle" if Step 7 is skipped. This means logs and DB rows label Nutty-Heavy's votes as Buddle's. Recommend Step 7 be executed in the same change to avoid telemetry confusion, but it requires confirming no downstream dashboard hardcodes the `TargetedADS-Buddle` agent name. HwaO to confirm.
