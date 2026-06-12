# Research Ideas — Karpathy-Style Gap Detection v2 Design

**Owner:** Kun 🔬  ·  **Implementer:** Tori  ·  **Status:** ✅ Papa-approved 2026-05-19 — ready for Tori implementation
**Date:** 2026-05-19 (KST)
**Filename:** `docs/research_ideas_karpathy_v2_design.md`
**Locked decisions (see §8):** Q3 = backfill all 42 existing ideas with Atom-7B classification · Q5 = Rakon temperature 0.7

**Companion docs (read first):**
- `docs/research_ideas_design_v1.md` — Phase 3 design (claim-anchored, dataset-verified layer). Baseline for this upgrade.
- `docs/research_ideas_tab_design_v1.md` — Phase 1/2 (UI tab, survey-combo prompts, 15 seed ideas).
- `docs/galev_quality_roadmap.md` — galaxy-evolution flagship work; pilot target.
- `docs/autowiki_surveys_v1.md` — autowiki beat system; model for the new beat task.

---

## 0. TL;DR

Current research ideas are **survey-combo anchored**: the LLM is handed a list of surveys and asked "what could you do with JWST + DESI?" The output is useful but generic — it doesn't read the *actual state of the page* before generating.

**Karpathy-style gap detection** flips the input: the LLM reads the full page — every section, every claim, every piece of evidence, and every existing idea — and generates new ideas by identifying what is **missing, contested, or needs bridging**. The concept mirrors Andrej Karpathy's LLM-as-wiki-reader mental model: an LLM that has read the current knowledge state and can say "here's the gap nobody has filled yet."

This doc designs the v2 pipeline to replace the survey-combo default with gap-detection-first generation.

---

## 1. Algorithm Overview

### 1.1 Conceptual model

The LLM reads the full page state as a structured document and produces research ideas classified by **gap type**:

| Gap Type | Definition | Example on galaxy-evolution |
|---|---|---|
| `gap` | A topic mentioned shallowly or not at all despite being adjacent to existing claims | Dust-obscured SFR at z>2 — JWST claims exist but no obscured tracers are discussed |
| `tension` | Two or more claims or sections give contradictory or hard-to-reconcile statements | Quenching timescale claims differ between merger and AGN-feedback sections |
| `bridge` | An implicit connection between two sections that is never made explicit | Morphology-quenching section and AGN-feedback section share physical scenarios but no cross-link claim exists |
| `frontier` | An open problem or "known unknown" within a section | Mass-quenching threshold: mechanism identified but no observational discriminant proposed |
| `synergy` | A specific combination of survey datasets that could test an existing claim but hasn't been proposed | DESI DR1 spectroscopic redshifts + JWST NIRCam morphologies at the same redshift slice |

### 1.2 Page-state input

Before the gap-detection call, the pipeline assembles the full page context:

```
page_context = {
  "slug": "galaxy-evolution",
  "sections": [
    {
      "heading": "Star Formation History",
      "body_markdown": "...",           # full rendered section text
      "claims": [
        {
          "id": 123,
          "text": "...",
          "trust_score": 0.82,
          "evidence_count": 14,
          "pro_count": 11,
          "con_count": 3
        }, ...
      ]
    }, ...
  ],
  "existing_ideas": [
    {
      "id": 7,
      "question": "...",
      "gap_type": "synergy",
      "anchor_claim_id": 123
    }, ...
  ]
}
```

Token budget estimate for galaxy-evolution (live page state, 2026-05-19):

The full page is 71,988 characters (~17,000 words ≈ 22,000 tokens for raw section bodies alone). Feeding it raw would dominate the prompt and crowd out claims/ideas. The pipeline therefore **pre-summarizes each section to a 250–400-word digest** (deterministic Python truncation by canonical-subtopic; no LLM call) before injection:

- 9 section digests × ~350 words avg ≈ 3,150 words ≈ ~4,200 tokens
- 41 claims × ~40 tokens avg ≈ 1,640 tokens
- 42 existing ideas × ~60 tokens avg ≈ 2,520 tokens
- Top 20 surveys × ~25 tokens avg ≈ 500 tokens
- System prompt + JSON skeleton ≈ 1,200 tokens
- **Total: ~10,000 tokens input** — comfortably inside Rakon's 64k context window with headroom for the JSON output.

Section digests are cached at `digest:section:{page_id}:{section_idx}:{section_hash}` (TTL 7d) so repeat ticks on an unchanged page skip the truncation work. Full section bodies are still available to AstroSage in §4.2 if it needs to verify a specific claim against source prose.

### 1.3 Generation logic

Rakon performs a single structured call with the page context. It is instructed to:

1. Read each section and its claims as a coherent knowledge block.
2. Identify the five gap types (one pass each, not interleaved).
3. For each identified gap, produce a candidate idea in the output schema.
4. Limit output to at most 15 candidates per run (quality gate downstream reduces to 10).

Gap-detection is a **reasoning-heavy synthesis task** — not a lookup or paraphrase — which is why Rakon (671B) handles it rather than a smaller model.

---

## 2. Prompt Design

### 2.1 System prompt skeleton

```
You are an expert astrophysics research strategist. Your role is to read the current knowledge state of a NebulaMind wiki page and identify high-value research ideas by detecting what is missing, contested, or needs bridging.

You will receive:
1. A structured JSON object representing the full page state (sections, claims with trust scores, and existing research ideas).
2. A list of active surveys available for observational follow-up.

Your task: identify and output up to 15 research ideas, each addressing a specific knowledge gap. Classify each idea by gap_type: gap | tension | bridge | frontier | synergy.

RULES:
- Every idea MUST anchor to exactly one claim (anchor_claim_id) from the page state.
- Every idea MUST specify at least one survey instrument from the active surveys list.
- Every idea MUST include a redshift range.
- Every idea MUST name at least one physical observable (e.g., stellar mass, SFR, Sérsic index, [OII] flux).
- Do NOT repeat any idea already present in existing_ideas (check semantically, not just lexically).
- Prioritize ideas where claim trust_score < 0.7 or pro_count/con_count ratio < 3 (contested claims).
- For gap and frontier types, prioritize sections with the fewest claims relative to their body_markdown length.
- For tension type, explicitly identify the two conflicting claims by ID.
- For bridge type, identify the two sections being connected.
- For synergy type, name at least two distinct survey datasets and explain the observational leverage.

OUTPUT FORMAT: Return a JSON array only. No prose before or after.
```

### 2.2 Output schema

Each idea in the output array must conform to:

```json
{
  "question": "string — one concise research question, ≤120 chars",
  "why_now": "string — 1-2 sentences explaining timeliness (new data, open debate, etc.)",
  "approach": "string — 2-4 sentences describing the methodology",
  "survey_combo": "string — comma-separated survey/instrument names (e.g., 'DESI DR1 BGS, JWST NIRCam')",
  "anchor_claim_id": "integer — primary claim this idea would test or extend",
  "secondary_claim_ids": "array of integers — optional, 0-3 additional claims",
  "gap_type": "string — one of: gap | tension | bridge | frontier | synergy",
  "conflicting_claim_ids": "array of two integers — required if gap_type = tension",
  "bridge_section_pair": "array of two strings — section headings, required if gap_type = bridge",
  "redshift_range": "string — e.g. 'z = 0.1 - 1.0' or 'z > 2'",
  "physical_observable": "string — primary observable (e.g. 'specific SFR, stellar mass')",
  "novelty": "float 0-1 — self-assessed novelty score",
  "feasibility": "float 0-1 — self-assessed feasibility score"
}
```

### 2.3 Active surveys injection

The prompt injects the top 20 surveys from the `surveys` table ranked by `impact_score DESC, status = 'active'`. Format:

```
ACTIVE SURVEYS (use these names exactly):
- DESI DR1 BGS (spectroscopic redshifts, z=0.01-0.6, 14M galaxies)
- JWST NIRCam (near-IR imaging, z=0-13, sub-arcsec resolution)
- LSST/Rubin Year 1 (optical photometry, z=0.1-3, 18000 deg²)
- Euclid DR1 (photometry + grism spectroscopy, z=0.9-1.8, 14000 deg²)
- SKA1-Mid (radio continuum + HI, z=0-3)
- ALMA Band 6/7 (submm dust continuum, z=1-6)
- HST 3D-HST (grism spectroscopy, z=0.7-3.5)
- eROSITA DR1 (X-ray, AGN + cluster catalog, z<1)
...
```

---

## 3. Autowiki Integration

### 3.1 New beat task: `generate_research_ideas_v2`

Add to `app/beat/tasks.py` (alongside existing research-ideas beat):

```python
@beat_task(name="generate_research_ideas_v2", schedule="0 4 * * *")  # 04:00 KST daily
async def generate_research_ideas_v2(page_slug: str = "galaxy-evolution"):
    """
    Karpathy-style gap-detection research idea generator.
    Idempotent: skips if the page hasn't changed since the last successful run.
    Lock contract: shares the global rakon:lock (per Mac Pro platoon mutex).
    """
    page = await Page.get_by_slug(page_slug)

    # Honor manual exclusion flag on the page.
    if page.do_not_renovate:
        logger.info(f"[ideas_v2] {page_slug} flagged do_not_renovate, skipping.")
        return

    run_key = f"research_ideas:karpathy_run_at:{page.id}"
    last_run = await redis.get(run_key)
    if last_run and page.updated_at <= datetime.fromisoformat(last_run):
        logger.info(f"[ideas_v2] {page_slug} unchanged since last run, skipping.")
        return

    # Cross-loop priority (Papa-approved 2026-05-13): surveys > wiki > karpathy_v2.
    # If surveys are running their AstroSage lock, wait up to 5 min then skip this tick.
    if await redis.get("astrosage:in_use") == "surveys":
        if not await wait_until_cleared("astrosage:in_use", timeout_sec=300):
            logger.info("[ideas_v2] surveys hold astrosage; deferring to tomorrow.")
            return

    # Acquire the global Rakon mutex (same key the seed/draft tasks use).
    # Value tags the holder so diagnostic tooling can identify the task. TTL 2h.
    acquired = await redis.set(
        "rakon:lock", "karpathy_v2", ex=7200, nx=True
    )
    if not acquired:
        logger.info(f"[ideas_v2] rakon:lock held by another task; skipping tick.")
        return

    try:
        context = await build_page_context(page)              # §1.2 (digested)
        candidates = await rakon_gap_detect(context)          # §4.1 (with fallback)
        prose_ideas = await astrosage_polish(candidates)      # §4.2 (read-only fields)
        scored_ideas = await atom_score(prose_ideas)          # §4.3 (default on outage)
        final_ideas = await nutty_dedup(scored_ideas, page.id)  # §4.4

        await persist_ideas(final_ideas, page.id, model_chain="karpathy_v2")
        await redis.set(run_key, datetime.utcnow().isoformat())
        logger.info(f"[ideas_v2] Saved {len(final_ideas)} new ideas for {page_slug}.")
    finally:
        # Always release — mirror the seed_debated_claim_ideas finally pattern.
        await redis.delete("rakon:lock")
```

Why `04:00 KST` (not 03:00): the wiki autowiki tick fires every 5 minutes around the clock — there is no quiet window, so the chosen slot just needs to be off-peak for Papa's interactive use. 04:00 also gives the daily news-digest beat (03:00) a clear runway on Mac Studio.

### 3.2 Redis keys

| Key pattern | Type | TTL | Purpose |
|---|---|---|---|
| `rakon:lock` (value=`karpathy_v2`) | string | 2h | **Shared global Mac Pro Rakon mutex.** Reused — do NOT introduce a per-page karpathy lock; the seed/draft/deep_pass tasks already serialize on this key. The value field identifies the current holder for ops diagnostics. |
| `astrosage:in_use` (value=`surveys`/`wiki`/`karpathy_v2`) | string | 30min | Cross-loop AstroSage-70B lock (Papa-approved 2026-05-13). Priority: surveys > wiki > karpathy_v2. Karpathy waits ≤5 min then skips tick. |
| `digest:section:{page_id}:{idx}:{hash}` | string (markdown) | 7d | Cached section digest (§1.2). Avoids re-truncating unchanged sections on repeat ticks. |
| `research_ideas:karpathy_run_at:{page_id}` | string (ISO datetime) | none | Last successful v2 run timestamp. Drives the idempotent-skip guard. |
| `research_ideas:karpathy_candidates:{page_id}` | string (JSON) | 24h | Raw Rakon output prior to AstroSage/Atom passes — kept for postmortem debugging. |

### 3.3 Trigger logic

The task runs at **03:00 KST daily** via Celery Beat. It is **idempotent**: if the page's `updated_at` timestamp has not advanced beyond `karpathy_run_at:{page_id}`, the task exits immediately without LLM calls. This prevents redundant generation on unchanged pages.

Manual re-trigger (admin): `POST /api/admin/ideas/regenerate-v2?page_slug=galaxy-evolution&force=true`

---

## 4. Model Assignment (Platoon)

Per platoon-assignment rule, every step names an owning model with capability / cost / speed justification:

| # | Step | Owner | Host | Capability — why this model | Cost | Speed (typical) |
|---|---|---|---|---|---|---|
| 0 | Page-state digest assembly | Python (no model) | Mac Studio | Deterministic markdown truncation + DB read; no inference needed | $0 | <100ms |
| 1 | Gap-detection synthesis (5-lens) | **Rakon** (`deepseek-r1:671b`) | Mac Pro (exclusive) | 671B MoE reasoning over the full page state — cross-section synthesis, contradiction detection. Buddle-32B is too shallow for multi-lens planning; AstroSage-70B is a domain stylist, not a planner. | Free local | 45–120s/tick warm; cold-load minutes |
| 1f | Rakon fallback (if Mac Pro down) | **Buddle** (`deepseek-r1:32b`) → **Mima** (`qwen3:30b`) | Mac Pro → Mac Studio | Mirrors the `seed_debated_claim_ideas` chain. Buddle gives ~70% of Rakon depth at 20% latency; Mima is last-resort throughput. Tagged `model_chain="karpathy_v2_buddle"` / `_mima` so post-hoc filtering is possible. | Free | 8–20s (Buddle) / 5–10s (Mima) |
| 2 | Prose polish + physics audit | **AstroSage-70B** | Mac Studio | Astronomy-fine-tuned; catches wrong survey specs, unit errors, implausible z-ranges. Generic 70Bs hallucinate survey capabilities. Read-only fields enforced (§4.2). | Free | 20–40s for batch of ≤15 |
| 3 | Novelty / feasibility scoring | **Atom-Astronomy-7B** | Mac Studio | Astronomy-tuned 7B; fast structured scoring; trivial RAM footprint. Default to `0.5 / 0.5` on Atom outage (don't drop candidates because scorer is flaky). | Free | 1–3s/idea |
| 4 | Dedup vs existing page ideas | **Nutty** (`deepseek-r1:14b`) embeddings (no LLM call beyond embed) | Mac Studio | Fast embedding for cosine similarity; reasoning depth wasted on mechanical similarity check. | Free | <100ms/batch |
| 5 | Quality gate (conjunctive) | Python rule (§5.2) | Mac Studio | Deterministic — survey-name match, observable keyword, redshift parse. No LLM call needed; conjunctive gates avoid the additive-saturation anti-pattern. | $0 | <50ms |
| 6 | Volume-cap ranking (top 10) | Python (§5.3 additive blend) | Mac Studio | Ranking only — promotion is governed by §5.2 conjunctive checks. The additive formula here is for tie-breaking when more than 10 ideas survive §5.2, not for promotion decisions. | $0 | <10ms |
| 7 | Persistence to `research_ideas` | Python ORM | Mac Studio | DB write with anchor rows + `gap_type` + `conflicting_claim_ids` / `bridge_section_pair`. | $0 | <200ms |

Co-residency check (Mac Studio): the v2 pipeline only loads AstroSage-70B + Atom-7B + Nutty simultaneously — a comfortable combo (≈56 GB) per the platoon-roster cheat-sheet. Conflicts with wiki autowiki AstroSage usage are serialized via `astrosage:in_use`.

### 4.1 Rakon (671B) — Gap Detection Synthesis

**Role:** Primary gap-detection call. Reads full page context (sections + claims + existing ideas) and produces up to 15 candidate ideas in JSON.

**Why Rakon:** This is a reasoning-intensive synthesis task requiring the model to hold the entire page state in working memory, identify non-obvious absences, and reason about contradictions across sections. 671B parameters + long-context reasoning make this the right model.

**Prompt:** Full system prompt from §2.1 + page_context JSON + active surveys list.

**Temperature:** `0.7` (Papa-locked — see §8 Q5). Gap-detection benefits from controlled creativity; 0.7 sits at the conservative end of the 0.7–0.9 synthesis band. Pass via Ollama `options.temperature` on the per-request payload — no separate endpoint config needed (the existing factual-claim pipeline keeps its 0.3 default; v2 overrides per-call).

**Expected latency:** ~45–90s for galaxy-evolution page size.

**Output:** JSON array of up to 15 candidates (§2.2 schema).

**Fallback chain (Mac Pro unreachable or Rakon timeout > 1800s):**

1. Try Buddle (`deepseek-r1:32b`, Mac Pro) — same prompt, max 10 candidates instead of 15. Tag `model_chain="karpathy_v2_buddle"`.
2. If Buddle also fails, try Mima (`qwen3:30b`, Mac Studio) — max 8 candidates. Tag `model_chain="karpathy_v2_mima"`.
3. If all three fail, log the tick as `decision="no_commit", reject_reason="all_models_failed"` in `autowiki_runs` and exit cleanly. Lock is released by the outer `finally` block.

The fallback chain mirrors the production `seed_debated_claim_ideas` pattern (`research_ideas/auto_improvement.py:_generate_ideas_for_claim`) so ops behavior stays consistent across the two tasks.

### 4.2 AstroSage-70B — Prose Polish

**Role:** Converts Rakon's structured JSON fields (`question`, `why_now`, `approach`) into fluent, domain-accurate astrophysics prose. Catches physics errors Rakon may introduce (incorrect units, wrong survey capabilities, implausible redshift claims).

**Why AstroSage-70B:** Domain fine-tuned for astrophysics. Prose quality matters for the public-facing wiki; generic 70B models hallucinate survey specs.

**Prompt per idea:**
```
You are an astrophysicist reviewing a research idea draft. Polish the
listed prose fields for scientific accuracy and fluency. Fix any incorrect
survey specifications, units, or physically implausible claims.

EDITABLE FIELDS (you may rewrite these):
  - question
  - why_now
  - approach

READ-ONLY FIELDS (return EXACTLY as given — do not paraphrase, renumber,
or "polish" these; the pipeline depends on them as identifiers/anchors):
  - anchor_claim_id
  - secondary_claim_ids
  - gap_type
  - conflicting_claim_ids
  - bridge_section_pair
  - survey_combo (you MAY correct a clearly-wrong instrument name, but
                  not change the survey set itself)
  - redshift_range
  - physical_observable
  - novelty
  - feasibility

If you detect an unsalvageable physics error (e.g., observing 21cm at
z=12 with an instrument that doesn't reach that band), set
`question` to "" and add `"reject_reason": "<one-line explanation>"`.
The pipeline will treat empty-question ideas as drops.

IDEA (JSON): {idea_json}

Return the same JSON structure with polished editable-field text only.
```

**Batching:** Process candidates in groups of 5 to bound AstroSage context per call (15 candidates × ~400 tokens each ≈ 6k tokens per batch — comfortable). One sequential pass; AstroSage does not need to see other candidates to polish a given one.

### 4.3 Atom-7B — Novelty / Feasibility Scoring

**Role:** Assigns final `novelty` (0–1) and `feasibility` (0–1) scores. Also flags ideas that are too similar to existing arXiv papers (semantic overlap check against the page's evidence corpus).

**Why Atom-7B:** This is a fast classification/scoring task, not synthesis. Atom-7B throughput is 10–20× Rakon; running 15 scoring calls is inexpensive.

**Prompt per idea:**
```
Score this astrophysics research idea on two axes:
- novelty (0-1): how new is the specific combination of survey + observable + redshift range?
- feasibility (0-1): can this be executed with currently available data and standard methods?

Consider the existing evidence corpus (provided as titles + bibcodes).

Return JSON: {"novelty": float, "feasibility": float, "flag": "ok"|"too_similar"|"infeasible"}
```

**Threshold for rejection:** `flag = "too_similar"` → discard candidate.

**Atom outage / scoring failure:** If Atom returns empty / malformed JSON or the service is unreachable, default to `novelty=0.5, feasibility=0.5, flag="ok"` and log a warning (`[ideas_v2] atom score failed for idx=N, persisting with default 0.5/0.5`). Do **not** drop candidates because the scorer is flaky — that's the same defensive pattern `seed_debated_claim_ideas` uses, and the §5 quality gate plus the §5.3 volume cap will still filter low-novelty ideas using the trust-score term.

### 4.4 Nutty (14B) — Deduplication Check

**Role:** Final dedup pass. Computes semantic similarity between each surviving candidate and all existing `research_ideas` for the page. Discards candidates with cosine similarity > 0.85 against any existing idea.

**Why Nutty:** 14B model with fast embedding generation. Dedup is a mechanical similarity task, not a reasoning task — using Rakon here would waste compute.

**Implementation:**
```python
async def nutty_dedup(candidates: list[dict], page_id: int) -> list[dict]:
    existing = await ResearchIdea.get_embeddings_for_page(page_id)
    surviving = []
    for candidate in candidates:
        emb = await nutty_embed(candidate["question"] + " " + candidate["approach"])
        max_sim = max((cosine_sim(emb, e) for e in existing), default=0.0)
        if max_sim < 0.85:
            surviving.append(candidate)
    return surviving
```

---

## 5. Quality Gate

Three criteria must pass for an idea to be persisted:

### 5.1 Dedup threshold

- Computed by Nutty (§4.4): cosine similarity > 0.85 against any existing idea → **discard**.
- Embedding computed over `question + approach` (not just question, to catch paraphrases with different wording).

### 5.2 Specificity check

Each surviving idea must pass all three:

1. **Survey check:** `survey_combo` must name at least one survey from the active surveys list (exact string match after normalization).
2. **Observable check:** `physical_observable` must be non-empty and contain at least one recognized observable keyword (stellar mass, SFR, sSFR, Sérsic index, velocity dispersion, [OII] flux, Hα flux, FIR luminosity, HI mass, X-ray luminosity — configurable list in `app/constants/observables.py`).
3. **Redshift check:** `redshift_range` must parse to a valid numeric range using `parse_redshift_range()`.

Ideas failing any check are logged to `idea_rejections` table for review and discarded.

### 5.3 Volume cap (ranking, not promotion)

Maximum **10 new ideas per run** per page. If Nutty returns more than 10 survivors of §5.1+§5.2, select the top 10 ranked by:

```
rank_score = 0.4 × novelty + 0.4 × feasibility + 0.2 × (1 − anchor_claim_trust_score)
```

The trust-score term deprioritizes ideas anchored to well-established claims (high trust = already well-supported), favouring ideas that address contested or poorly-evidenced claims.

**Important:** this additive formula is used **only for tie-breaking** when more than 10 ideas pass the conjunctive §5.2 gates — it is *not* a promotion criterion. Promotion is governed entirely by §5.1 (dedup) AND §5.2 (specificity), per the judge-saturation rule: additive integer rubrics saturate and become game-able, so the "go/no-go" decision stays purely conjunctive and the additive blend is confined to ordering survivors.

If fewer than 10 ideas survive §5.2, all of them persist — no minimum.

---

## 6. DB Schema Changes

### 6.1 Add `gap_type` and `gap_type_source` columns to `research_ideas`

```sql
-- Migration: add_gap_type_to_research_ideas
ALTER TABLE research_ideas
  ADD COLUMN gap_type VARCHAR(20)
    CHECK (gap_type IN ('gap', 'tension', 'bridge', 'frontier', 'synergy'))
    DEFAULT NULL,
  ADD COLUMN gap_type_source VARCHAR(20)
    CHECK (gap_type_source IN ('karpathy_v2', 'atom_backfill', 'manual'))
    DEFAULT NULL;

-- Initial state: every row NULL. The §6.5 one-shot backfill populates
-- the 42 existing rows with gap_type_source='atom_backfill'. New v2 beat
-- ticks write gap_type_source='karpathy_v2'. Papa overrides via admin
-- panel write 'manual'.
```

### 6.2 Add `karpathy_v2` to `model_chain` enum

```sql
ALTER TYPE model_chain_enum ADD VALUE 'karpathy_v2';
```

If `model_chain` is a VARCHAR column rather than a Postgres enum:

```sql
-- No migration needed; karpathy_v2 is a valid new string value
-- Update the CHECK constraint if one exists:
ALTER TABLE research_ideas
  DROP CONSTRAINT IF EXISTS research_ideas_model_chain_check;

ALTER TABLE research_ideas
  ADD CONSTRAINT research_ideas_model_chain_check
    CHECK (model_chain IN (
      'rakon_v1', 'astrosage_combo', 'manual', 'seed', 'karpathy_v2'
    ));
```

### 6.3 Add `conflicting_claim_ids` and `bridge_section_pair` columns

```sql
ALTER TABLE research_ideas
  ADD COLUMN conflicting_claim_ids  INTEGER[]  DEFAULT NULL,
  ADD COLUMN bridge_section_pair    TEXT[]     DEFAULT NULL;
```

These nullable arrays store the structured gap-detection metadata for tension and bridge types respectively.

### 6.4 Full migration file name

`migrations/versions/20260519_001_add_gap_type_karpathy_v2.py`

### 6.5 One-shot backfill — classify all 42 existing ideas with Atom-7B

**Decision:** Papa-locked (§8 Q3) — run Atom-7B classification on every existing `research_ideas` row (15 seeds + 27 LLM-generated = 42 ideas as of 2026-05-19) and persist a non-NULL `gap_type` for each.

**Script:** `scripts/backfill_gap_type_v2.py` (one-shot, idempotent — skips rows where `gap_type IS NOT NULL`).

**Per-idea Atom-7B prompt:**
```
Classify this astrophysics research idea into exactly one gap_type bucket:
  - gap       : addresses a topic mentioned shallowly or not at all
  - tension   : addresses contradiction between two existing claims
  - bridge    : connects two sections never linked explicitly
  - frontier  : tackles an open / known-unknown problem
  - synergy   : combines specific survey datasets to test an existing claim

Return JSON: {"gap_type": "<one of the five>", "confidence": float 0-1, "reason": "<≤20 words>"}.

IDEA:
  question:     {question}
  why_now:      {why_now}
  approach:     {approach}
  survey_combo: {survey_combo}
  anchor_claim: {anchor_claim_text}
```

**Confidence handling:**
- `confidence ≥ 0.6` → write `gap_type` to DB, tag with `gap_type_source = 'atom_backfill'`.
- `confidence < 0.6` → write `gap_type` but additionally flag the row in a transient `idea_review_queue` table for Papa's admin-panel review (one-time triage list, dropped after v2.1).

**Failure handling:** Atom outage → log warning, leave `gap_type = NULL`, exit nonzero so Tori can re-run later. The script is safe to re-invoke.

**Performance budget:** 42 ideas × ~1.5s/Atom call ≈ 1 minute total — runs once during the v2.0 cutover window. Holds the `astrosage:in_use` lock briefly but does not block the autowiki loop (Atom-7B does not contend with AstroSage).

**Verification:** After run, `SELECT gap_type, COUNT(*) FROM research_ideas GROUP BY gap_type;` should show zero NULLs (or, if Atom flaked on a few, the flagged rows live in `idea_review_queue` for manual fix).

**New column:** `gap_type_source VARCHAR(20)` on `research_ideas` (values: `'karpathy_v2'` for new v2 generations, `'atom_backfill'` for the one-shot pass, `'manual'` for Papa overrides). Folded into the §6.1 migration.

---

## 7. Phasing

### v2.0 — Galaxy-Evolution Pilot (target: 2026-06-01)

- Beat task `generate_research_ideas_v2` runs for `galaxy-evolution` only.
- DB migrations applied (including `gap_type_source` column — §6.1).
- **One-shot backfill executed (§6.5):** all 42 existing ideas classified by Atom-7B before the first v2 beat tick fires. Verification SQL run, low-confidence rows triaged.
- Quality gate live (dedup + specificity + volume cap).
- Rakon called with `temperature=0.7` (per §4.1 / §8 Q5).
- Admin UI shows `gap_type` badge on idea cards.
- No public UI change yet (ideas appear in existing Research Ideas tab).
- Success metric: ≥10 new ideas generated with `gap_type != NULL` after first run; ≤2 human-rejected on Papa review.

### v2.1 — All Flagship Pages (target: 2026-07-01)

- Beat task parameterized: runs for all pages with `is_flagship = true`.
- Redis key pattern unchanged (`{page_id}` already parameterized).
- Specificity observable list expanded per page type (e.g., `exoplanet-atmospheres` gets transmission spectroscopy observables).
- Public UI: gap_type filter chips added to Research Ideas tab.

### v2.2 — Cross-Page Idea Linking (target: 2026-08-01)

- New beat task `link_cross_page_ideas`: identifies ideas on different pages that address the same physical mechanism.
- New join table `cross_page_idea_links(idea_id_a, idea_id_b, link_type, similarity_score)`.
- UI: "Related ideas on other pages" section below each idea card.
- Model: Nutty (14B) for similarity scoring; Rakon for narrative link description.

---

## 8. Decisions — Papa Sign-Off (2026-05-19)

Status: Q3 and Q5 explicitly locked by Papa. Q1, Q2, Q4 carry the proposed defaults forward — Tori implements as written; if Tori needs an override during build, escalate to Papa before deviating.

1. **Rakon API concurrency** — *implement as proposed.* Galaxy-evolution v2 call (~9k tokens input) targets <2min latency. If the Rakon mutex is held at 03:00 KST, the beat task retries after 10min, up to 3 attempts, then logs `decision="no_commit", reject_reason="rakon_busy"` and releases cleanly.

2. **`idea_rejections` admin visibility** — *defer admin UI to v2.1.* For v2.0, all rejections write to the `idea_rejections` table (programmatic access only). Papa can SQL-query during pilot if curious; full admin panel ships with v2.1's public-UI work.

3. ✅ **`gap_type` backfill — LOCKED (Papa, 2026-05-19):** Run Atom-7B classification on **all 42 existing ideas** (15 hand-written seeds + 27 LLM-generated). Implementation in §6.5. Confidence < 0.6 rows flagged to `idea_review_queue` for one-time Papa triage. Backfill runs once during the v2.0 cutover, before the first v2 beat tick.

4. **`observables.py` editing workflow** — *manual PR for v2.0.* Tori does not stub an admin UI in v2.0. The keyword list is small (~50 entries), changes are infrequent, and a tracked PR keeps the source of truth in git. If Papa later requests inline editing, an admin UI can be added in v2.1 alongside the public-UI work.

5. ✅ **Rakon prompt temperature — LOCKED (Papa, 2026-05-19):** `temperature = 0.7`. Implementation in §4.1. Passed per-request via Ollama `options.temperature` on the gap-detection call — no separate endpoint config required. The factual-claim pipeline retains its 0.3 default unchanged.

---

## 8b. Handoff to Tori

This doc is now **ready for Tori implementation.** Suggested build order:

1. **DB migration** (§6.1, §6.3, §6.5 column additions) — single Alembic file `20260519_001_add_gap_type_karpathy_v2.py`.
2. **Backfill script** (§6.5) — run end-to-end on staging first; verify the `gap_type` distribution looks plausible (no single bucket >70% on the existing 42 ideas would be reassuring).
3. **Pipeline scaffolding** — adapt `seed_debated_claim_ideas` skeleton (§4.1 fallback chain mirrors it). Hard-code `temperature=0.7` on the Rakon call.
4. **Quality gate** (§5) — dedup → specificity → volume cap, in that order.
5. **Beat task wiring** (§7) — register `generate_research_ideas_v2` for `galaxy-evolution` only; do not enable other flagship pages until v2.1.
6. **Admin UI badge** (§7) — `gap_type` chip on idea cards.

Open items Tori should surface back to Papa before merge:
- Confirm the `idea_review_queue` table name / lifecycle (drop after v2.1 vs. keep) — Kun's call is "drop with v2.1 migration".
- Any post-backfill `gap_type` distribution that looks pathological (e.g., 40/42 as `gap`) → ping Papa before lighting up the v2 beat task.

---

## Appendix A: Example Output

Illustrative (not real Rakon output) — shows what a high-quality gap-detection idea looks like:

```json
{
  "question": "Does dust-obscured star formation dominate quenching at z=1-2 in massive galaxies?",
  "why_now": "JWST NIRCam morphologies now overlap with ALMA Band 6 dust continuum catalogs at the same redshift slices for the first time, enabling direct SFR comparison between UV and FIR tracers.",
  "approach": "Cross-match JWST CEERS NIRCam sources (F277W + F356W) with ALMA GOODS-S Band 6 detections at z=1-2. Compute UV-derived SFR vs. IR-derived SFR as a function of stellar mass. Fit quenching fraction vs. dust obscuration fraction using a Bayesian mixture model.",
  "survey_combo": "JWST NIRCam CEERS, ALMA Band 6 GOODS-S",
  "anchor_claim_id": 237,
  "secondary_claim_ids": [241, 189],
  "gap_type": "gap",
  "conflicting_claim_ids": null,
  "bridge_section_pair": null,
  "redshift_range": "z = 1.0 - 2.0",
  "physical_observable": "SFR (UV + FIR), stellar mass, dust obscuration fraction",
  "novelty": 0.81,
  "feasibility": 0.74
}
```

---

*End of document — v2 design for Papa review.*
