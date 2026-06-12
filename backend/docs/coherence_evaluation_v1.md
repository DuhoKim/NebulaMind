# Coherence Pass — Three-Option Evaluation

**Author:** Kun 🔬
**Date:** 2026-05-17 09:45 KST
**Context:** `run_coherence_pass.py` failed 3× because deepseek-r1:671b is a reasoning model that emits ~5 k chars of `<think>` summary instead of 65–80 k chars of prose. Before wiring coherence into the tick permanently, evaluate 3 alternative approaches head-to-head on the real page (id=57, 89,003 chars, 41 claims).
**Companion files:** `~/.openclaw/agents/tori/workspace/eval_coherence.py` (the harness), `~/.openclaw/agents/tori/workspace/run_coherence_pass.py` (the failed standalone — reuse prompts verbatim).
**Audience:** HwaO (decision), Tori (implementation).

---

## 0. Why the original Rakon call failed (root-cause beyond "reasoning model")

The standalone script set **`num_ctx = 32768`** (32 k tokens). The prompt + output requires far more:

- System + user template + 89 k page content ≈ **25 k input tokens** at ~3.5 chars/token (English mix)
- Target 65-80 k char output ≈ **20 k output tokens**
- deepseek-r1's `<think>` trace typically adds 2-5× the final answer length internally ≈ **40-100 k thinking tokens**

Total context needed: **80-150 k tokens.** At `num_ctx=32768` Ollama silently truncates — Rakon sees a partial input AND has no room to think AND no room to emit. Result: a 5 k-char meta-response.

This is **not** a fundamental Rakon limitation. deepseek-r1:671b supports up to 128 k context. But raising `num_ctx` is necessary, not sufficient — even at 131 k Rakon's reasoning-trace burn can starve output. Hence the three-option search.

---

## 1. Option A — Section-by-section Rakon (9 calls)

### 1.1 Approach
Decompose the rewrite into 9 independent Rakon calls, one per target H2 section. Each call:
- Receives **only the source content that maps to that target section** (per the merge map below) — typically 6-15 k chars
- Receives the **prior section's last paragraph** (for transition-in)
- Receives the **next section's first paragraph** (for transition-out)
- Emits **just that one section** (7-10 k chars target)

After 9 calls, the harness assembles the 9 outputs into a single page with the standard `## References` footer appended (consolidated from inline citations across the 9 sections).

### 1.2 Source → target mapping (used by the section picker)

```
TARGET                                                SOURCES (current ## sections)
─────────────────────────────────────────────────────────────────────────────────────
1. Overview & Historical Foundations               ← §1
2. Physical Mechanisms                             ← §2 + §11's "Star-Forming Regions" H3
3. Dark Matter, Halos & Structure Formation        ← §3 + §11 (minus the H3 reassigned to §2)
4. Star Formation, Quenching & Color Bimodality    ← §4 + §9 + §12's "Bimodal Color" H3
5. AGN Feedback & Quenching Debates                ← §5 + §7's "Contested Claims: AGN" H3
6. Environmental Effects                           ← §6
7. Galaxy Scaling Relations & Size Evolution       ← §8 + §10
8. Observational Evidence & Multi-Wavelength       ← §7 (minus AGN H3) + §12's "High-z" H3
9. Open Questions & Frontier Debates               ← §12 (debate content only)
References (footer)                                ← all 3 ref-list dumps + inline cites
```

### 1.3 Call parameters

```python
httpx.post("http://169.254.100.1:11435/v1/chat/completions", json={
    "model": "deepseek-r1:671b",
    "messages": [
        {"role": "system", "content": SECTION_SYSTEM_PROMPT},
        {"role": "user", "content": SECTION_USER_PROMPT.format(
            target_header=...,
            target_h3_list=...,
            source_content=...,        # 6-15k chars
            prior_section_ending=...,  # 200-500 chars
            next_section_opening=...,  # 200-500 chars
        )},
    ],
    "temperature": 0.3,
    "num_ctx": 65536,                   # 64k — plenty for per-section prompt + think + output
    "options": {"num_predict": 12000},  # cap output at ~10k chars/section
    "stream": False,
}, timeout=10800, headers={"Authorization": "Bearer ollama"})
```

### 1.4 Estimated cost / time

| | Per call | × 9 calls |
|---|---|---|
| Wall time (Rakon median 1.34 h, see job_schedule_v1.md §7.1.1) | ~1.5 h | **~13.5 h** |
| Wall time (Rakon worst tail) | ~6 h | **~54 h** (unrealistic, use mutex) |
| Output chars | 7-10 k | 60-90 k assembled |
| Cost | $0 (local) | $0 |
| Mac Pro mutex held | 1.5 h | **9 × 1.5 h, sequential** |

### 1.5 Failure modes
- One section call returns a `<think>` blob → 1 of 9 sections missing → assembly fails validation
- Per-section `num_ctx=65536` still too small for Rakon's `<think>` on dense sections (e.g., AGN Feedback)
- Sections don't transition cleanly because each was generated in isolation — the "next section opening" hint may not match what the next call actually produced
- 13.5 h wall-time blocks Mac Pro for half a day — every other Rakon lane (rakon_deep_pass, rakon_draft_async, etc.) starves
- Source-to-target mapping picks the wrong source chars if H3 grep is fragile

### 1.6 Pros
- Per-call input fits cleanly in 64 k context — no truncation
- Per-call output is bounded (10 k cap) — Rakon can't run away with prose
- Each section is independent → can retry just the failed section, not the whole rewrite

---

## 2. Option B — AstroSage-70B full rewrite (single call)

### 2.1 Approach
Single call to `astrosage-70b:latest` on Mac Studio (`localhost:11434`). AstroSage's context window per Ollama show: **`llama.context_length = 131072`** (128 k). Plenty for 89 k input + 80 k output.

AstroSage is the astronomy-prose finetune already used as the autowiki_tick proposer. It's domain-aware and tuned for paragraph-scale astronomy writing — which is exactly what the coherence pass needs. **And it's not a reasoning model**: no `<think>` trace burn. Output is direct prose.

### 2.2 Call parameters

```python
httpx.post("http://localhost:11434/v1/chat/completions", json={
    "model": "astrosage-70b:latest",
    "messages": [
        {"role": "system", "content": SYSTEM_PROMPT},        # reuse from run_coherence_pass.py
        {"role": "user", "content": USER_PROMPT_TEMPLATE
                                       .format(full_page_content=current_content)},
    ],
    "temperature": 0.3,
    "num_ctx": 131072,                  # full 128k — fits input + output + slack
    "options": {"num_predict": 28000},  # ~80k chars output cap
    "stream": False,
}, timeout=14400, headers={"Authorization": "Bearer ollama"})
```

### 2.3 Estimated cost / time

| | Single call |
|---|---|
| Wall time (AstroSage 70B on Mac Studio M3 Ultra GPU, ~30-50 tok/s) | **15-30 min** for 25k output tokens |
| Output chars | 60-80 k target |
| Cost | $0 (local) |
| Mac Studio GPU occupied | 15-30 min |

### 2.4 Failure modes
- AstroSage may not respect structural instructions as well as Claude (it's prose-tuned, not instruction-tuned at the same level as RLHF-aligned cloud models). Risk of structural drift — wrong H2 headers, missing sub-sections, no References footer
- AstroSage may rewrite at lower fidelity to source — paraphrasing too liberally and dropping claim-specific phrasing
- 80 k output token budget on Ollama may run out of memory at peak; AstroSage rarely runs this size of output in one shot in production
- Mac Studio GPU is shared with autowiki_tick (every 10 min) and stance jury — 15-30 min occupation will delay other ticks

### 2.5 Pros
- Single call — no assembly logic, no inter-section transition problems
- Not a reasoning model — output tokens are all prose
- Already on the GPU — no model load cost
- Same architecture as the existing tick proposer — predictable behavior

---

## 3. Option C — Claude Sonnet 4.6 (single API call)

### 3.1 Approach
Single Anthropic API call to `claude-sonnet-4-6`. Same model already used by `sonnet-judge-tick` and `sonnet_section_rewrite` in the tick. Reuse the same prompts from `run_coherence_pass.py` verbatim.

### 3.2 Call parameters

```python
import anthropic
client = anthropic.Anthropic()  # picks up ANTHROPIC_API_KEY env
resp = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=32000,                 # ~100k chars output budget (plenty)
    system=SYSTEM_PROMPT,             # reuse from run_coherence_pass.py
    messages=[{
        "role": "user",
        "content": USER_PROMPT_TEMPLATE.format(full_page_content=current_content),
    }],
    temperature=0.3,
)
output = "".join(block.text for block in resp.content if block.type == "text")
```

### 3.3 Estimated cost / time

| | Single call |
|---|---|
| Wall time | **1-3 min** |
| Output chars | 60-80 k target |
| Cost (input: 89k chars ≈ 25k tokens × $3/M) | $0.075 |
| Cost (output: 75k chars ≈ 22k tokens × $15/M) | $0.33 |
| **Total cost** | **~$0.40** (Papa's estimate $0.50-1.00 covers retries) |
| Cloud quota usage | counted against `ANTHROPIC_API_KEY` budget |

### 3.4 Failure modes
- API rate limit (multiple coherence runs per day across other Anthropic-using lanes)
- Network blip → retry → cost doubles
- Claude may decline to produce 80 k tokens in one response if it judges the task too long — sometimes outputs a "here is the first half, ask me to continue" pattern (mitigated by tight prompt)
- Claim drift / citation hallucination — Sonnet is more careful than Rakon but not immune (validation gate catches this)
- Vendor dependency — outage = no coherence pass that day

### 3.5 Pros
- Fastest (1-3 min vs hours)
- Single call, no assembly
- 200 k context, 64 k output — no truncation concerns
- Already in the tick — operational familiarity, monitoring already set up
- Highest baseline quality for instruction-following + multi-section structural rewrites
- Doesn't burn Mac Pro or Mac Studio GPU — frees local compute for everything else

---

## 4. Evaluation harness design

`~/.openclaw/agents/tori/workspace/eval_coherence.py` (separate file). Runs all 3 options sequentially against the real page, captures metrics, writes `/tmp/coherence_eval_results.json`. **Read-only on the DB.** Does not write `page_versions`, `wiki_pages`, or `autowiki_runs`.

### 4.1 Metrics captured per option

| Metric | How computed |
|---|---|
| `wall_time_s` | `time.monotonic()` around the call(s) |
| `output_chars` | `len(output)` |
| `section_completeness` (0-10) | count of `EXPECTED_SECTIONS` H2 headings + References footer present in output |
| `claim_preservation_rate` (0-1) | fraction of the 41 claims whose ≥3 most-distinctive keywords ALL appear in output (substring match, case-insensitive). Distinctive keywords = words >5 chars not in a stopword list, picked by TF-IDF-ish rarity vs whole-page baseline |
| `citation_count_preserved` | count of `(Author Year)` patterns in output ÷ count in source |
| `banned_phrase_count` | count of "interestingly" / "remarkably" / "in this section we" / "as we discussed" in output |
| `meets_validation` | bool — same gates as `run_coherence_pass.validate()` (≥50k chars + all 10 sections + no banned phrases) |
| `error` (if applicable) | exception text |

The keyword-based claim preservation is intentionally simpler than the Atom-7b cosine validation in `j1_fix_v1.md` — for **evaluation** we just need a rough signal that scales linearly with quality across the three options. The strict cosine check belongs in the production post-write validation.

### 4.2 Run order

1. **Option C (Sonnet) first** — cheapest + fastest. If it succeeds, anchors a quality baseline against which A and B can be compared.
2. **Option B (AstroSage) second** — local, no cost, fast. Runs while no other lane needs Mac Studio.
3. **Option A (Rakon) last** — most expensive in time. Acquires `rakon:lock` per-call, releases between, so other Rakon work can interleave at section boundaries.

If Option C succeeds with high scores, the harness still runs A and B — the data point matters even if it'll be the loser. Don't short-circuit.

### 4.3 Locking behavior
- **Option A** sets `rakon:lock` (Redis NX SET, TTL 7200 s) before each per-section Rakon call, releases in `finally`. If another Rakon job has the lock, this call waits (with a 30-min cap, then skips that section).
- **Option B** does NOT lock Mac Studio — it just calls the local Ollama. autowiki_tick may delay during AstroSage's 15-30 min occupation, which is acceptable for a one-shot eval.
- **Option C** does NOT need a lock — cloud call.

### 4.4 Output format

`/tmp/coherence_eval_results.json`:

```json
{
  "ran_at": "2026-05-17T10:30:00Z",
  "page_id": 57,
  "source_chars": 89003,
  "source_claim_count": 41,
  "source_citation_count": 187,
  "options": {
    "A_rakon_per_section": {
      "wall_time_s": 49213.0,
      "output_chars": 71284,
      "section_completeness": 10,
      "claim_preservation_rate": 0.85,
      "citation_count_preserved": 0.78,
      "banned_phrase_count": 0,
      "meets_validation": true,
      "per_section_results": [
        {"target": "Overview & Historical Foundations", "wall_s": 4521, "chars": 7234, "ok": true},
        ...
      ],
      "error": null
    },
    "B_astrosage_full": { ... },
    "C_sonnet_full": { ... }
  },
  "winner_by_score": "C_sonnet_full",
  "winner_rationale": "Highest claim_preservation_rate AND meets_validation in <5 min wall time"
}
```

### 4.5 Composite score (for ranking)

```
score = meets_validation          * 100      # 100 for pass, 0 for fail (gate)
      + claim_preservation_rate   *  40      # 0..40 (most important quality metric)
      + (citation_count_preserved *  20)     # 0..20 (caps at 1.0)
      + section_completeness                 # 0..10 (raw count)
      + (output_chars >= 50000)   *  10      # 10 if hits length floor
      - banned_phrase_count       *   5      # penalty
      - (wall_time_s / 600)                  # -1 per 10 min wall time (cost-of-time soft penalty)
```

Max ≈ 180. Sonnet running cleanly in 3 min hits ~175. Rakon running cleanly in 13 h gets penalty of -78 from wall-time alone → ~100 even on perfect output. Built-in bias toward speed, intentional.

---

## 5. Recommendation: Option C (Sonnet) for production wiring

Before the eval runs, my prior:

| Criterion | A (Rakon ×9) | B (AstroSage) | C (Sonnet) |
|---|:-:|:-:|:-:|
| Wall time | 9-30 h | 15-30 min | **1-3 min** |
| Cost | $0 | $0 | $0.40 |
| Single-call simplicity | ✗ (9 calls + assembly) | ✓ | ✓ |
| Structural instruction-following | medium | medium-low | **high** |
| Reasoning-model trap | medium (mitigated by per-section bounding) | none | none |
| Free Mac Pro for other lanes | ✗ (9× mutex contention) | ✓ | ✓ |
| Free Mac Studio for other lanes | ✓ | ✗ (15-30 min) | ✓ |
| Already in tick | n/a | yes (proposer) | yes (judge + section_rewrite) |
| Operational familiarity | low | high | high |
| Cost predictability (per page) | bounded by mutex but variable | low variance | **flat $0.40** |

**Recommendation: production coherence lane = Sonnet 4.6 via Anthropic API.** Reasons in priority order:

1. **Coherence is a quarterly-to-monthly action** per page (not every tick) — at $0.40/page × top-15 pages × 1×/month = **$6/month**. Trivial relative to the $185/month total cloud budget in `beat_schedule_v3.md`.
2. **Speed enables iteration.** A 1-3 min coherence pass means Tori can test, observe q1 delta, re-run with prompt tweaks all within a single working session. A 13-h Rakon pass means one shot per day.
3. **Mac Pro stays free for the producer lanes.** R1/R2/R3/B3 (idea drafts, evidence pairs, adversarial probes) are the high-throughput Mac Pro lanes whose cumulative output drives the +0.12 q1 gap closure. Spending Mac Pro time on monthly coherence is the wrong allocation.
4. **Best instruction-following for structural rewrites.** Anthropic models reliably emit the exact target structure asked for. AstroSage (Option B) is prose-tuned, not RLHF-aligned for strict-format output.
5. **Validation catches all the risks.** Citation hallucination, claim drift — the same `validate()` + post-write `sonnet-judge-tick` gates that protect every other write path catch Sonnet's failures too.

**Option B as fallback** if cloud is down: AstroSage at `astrosage-70b` with 128 k context is the only local alternative with the context window to do this in one shot. Acceptable degraded mode but expect lower section-structure fidelity.

**Option A is the wrong tool for this job.** Rakon is the structural-reasoning model for hypothesis generation (R2 idea drafts) and adversarial probing (R3) — using it for prose restructuring underutilizes its depth and oversubscribes its time. Recommend Rakon stays on the producer lanes per `job_schedule_v1.md` §9 and is NOT wired into coherence.

---

## 6. Platoon Assignment — production coherence lane

| Step | Model | Why | Fallback |
|---|---|---|---|
| **Coherence rewrite** | **Claude Sonnet 4.6** (cloud) | speed + structural fidelity + frees Mac Pro/Studio for higher-value local work | AstroSage-70B (Mac Studio, 128k context) if cloud down |
| Pre-write snapshot | none (Python SQL) | `INSERT INTO page_versions SELECT FROM wiki_pages` | — |
| Post-write structural validation | none (Python regex) | `validate()` from existing `run_coherence_pass.py` | — |
| Post-write claim preservation | **Atom-7b** (Mac Studio) | cosine embeddings per claim against rewrite, ≥0.7 threshold | keyword fallback (used in eval) |
| Post-write quality audit | **sonnet-judge-tick** (existing 20-min cadence) | authoritative q1 score on the new page; auto-rollback if < 0.60 (per `delta_q_fix_v1.md` discipline) | opus-judge-tick |
| Cadence | **monthly per page**, on-demand | coherence drift is slow; daily is overkill, quarterly is too sparse | — |
| Trigger | manually invoked or weekly Sunday 03:00 KST if sonnet-judge-tick rolling q1 < 0.65 | self-healing | — |

---

## 7. What to do if the eval contradicts the recommendation

The eval should confirm Option C wins. But if it doesn't:

- **C fails (Sonnet refuses or hallucinates badly)**: switch to B as primary. Rerun with tighter prompt.
- **B beats C on claim_preservation_rate**: surprising; would mean AstroSage's astronomy fine-tune compensates for weaker instruction-following. Worth investigating but probably means our claim-preservation metric is too forgiving — re-eval with Atom-7b cosine instead of keyword match.
- **A beats both on output_chars but fails section_completeness**: confirms the reasoning-model assembly problem — A is structurally fragile, even tightened.
- **All three fail validation**: page is too fragmented for any single-pass coherence rewrite. Fall back to manual section-by-section edits by Kun.

---

## 8. Acceptance criteria for this evaluation

Tori runs `python3 ~/.openclaw/agents/tori/workspace/eval_coherence.py`. Within ~14 h (worst case dominated by Option A):

1. `/tmp/coherence_eval_results.json` exists and contains three `options` entries (no crashes)
2. At least 2 of 3 options have `meets_validation=true`
3. `winner_by_score` matches §5 recommendation (Sonnet) OR has a defensible reason for deviating
4. HwaO reads the JSON + this doc and confirms or overrides the recommendation
5. Tori wires the winning option into the tick per §6 (cadence: monthly per page on-demand; trigger: manual or q1 < 0.65 drift)

— 🔬 Kun, 2026-05-17 09:45 KST
