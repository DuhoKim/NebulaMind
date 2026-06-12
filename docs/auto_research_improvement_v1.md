# Auto Research Improvement — Design v1 (rev 3) — **Papa-approved, ready for Tori**

**Owner:** Kun 🔬  ·  **Status:** ✅ Papa-approved 2026-05-13 — ready for Tori implementation  ·  **Implementer:** Tori
**Date:** 2026-05-13 (KST)
**Filename:** `docs/auto_research_improvement_v1.md`
**Builds on:** `docs/research_ideas_tab_design_v1.md`, `docs/surveys_directory_design_v1.md` (both shipped today)

**Revision history:**
- rev 1 (initial): time-based 14-day draft aging to `'stale'`.
- rev 2 (2026-05-13): per Papa's directive — drafts never age out. Replaced with (a) update-in-place text refresh on new evidence and (b) coverage-based retirement to `'covered'` when arXiv literature directly answers an idea.
- **rev 3 (this version, 2026-05-13)** — Papa-approved all open questions:
  - Q2: drafts publicly visible — no hiding gate. Open source = open everything.
  - Q3: Mima DR confidence floor 0.6 ✅
  - Q4: auto-apply LOW-STAKES survey fixes (URL 404s, simple typos) on high confidence. Mid- and high-stakes still go to proposal queue.
  - Q5: Rakon Sunday outage → Buddle fallback (32B), do not skip the weekly pass.
  - Q6: Nutty rate limit ≤ 8/hr ✅
  - Q1 (aging) and Q7 (refresh-edit `question`) were resolved in rev 2.

---

## 0. TL;DR

Make the two new features (Research Ideas tab, Surveys Directory) self-improving instead of static.

- **Auto Research Ideas Generator** — event-driven lightweight pipeline using **Nutty (deepseek-r1:14b)** for per-event idea generation, **Atom-7B** for scoring/dedup, into a `'draft'` tier. Weekly **Rakon → AstroSage-70B** deep pass promotes the best drafts to `'active'`. When new evidence/claims arrive that touch an existing draft, the draft's text is **refreshed in place** rather than a new duplicate written. Drafts never age out — they stay drafts until promoted or covered.
- **Coverage retirement (only retirement path)** — a weekly **Atom-7B** pass scans new arXiv abstracts against every active+draft idea. When a paper is found to directly address an idea's research question, the idea transitions to `status='covered'` with a link to the paper. This is the **only** automatic retirement mechanism. No time-based decay.
- **Auto Surveys Freshness** — daily **Mima** pass riding the existing news-curator window detects DR-class headlines. Weekly **Atom-7B** scans arXiv abstracts for survey-mention + DR-version mismatches. **Two-tier apply policy** (§3.5b): load-bearing metadata (DR string, status, sky_coverage_deg2, flagship_programs) is queued for Papa one-click approve. Low-stakes fixes (broken `archive_url`/`mission_url`, units-only `data_volume` typos, ≤5-char punctuation in `description`) auto-apply on high confidence.
- **Cross-feature integration** — (a) when a new Research Idea references an unknown survey, log to `surveys_orphans` for Papa review; (b) when a new survey is added, queue an `Atom-7B claim-scan` + `Nutty idea-generation` chain so the new survey lights up Research Ideas on relevant pages within hours.
- **Visibility** — drafts publicly visible (Papa Q2 ruling). Frontend renders a `draft` badge on cards that haven't survived Rakon curation, but readers see everything. Open source = open everything.
- **Resilience** — if Rakon is unavailable on a Sunday, the weekly pass falls back to **Buddle (32B)** rather than skipping (Papa Q5). Promoted ideas mark the chain (`promoted_by='buddle_weekly'`) so telemetry can compare quality across the two paths.
- **Cost philosophy** — cheap-first, expensive-last. Per-event Nutty (~30s, free local) refreshes or grows the draft pool; rare expensive Rakon promotes the best. Avoids both stale data and runaway compute.
- **Quality philosophy** — ideas are *living artifacts*. They get continuously refreshed as data accumulates and only retire when the literature has answered them. Re-emission by Rakon's weekly pass = promotion to active; Papa save = instant promotion; coverage by a new paper = retirement.

---

## 1. Three guiding principles

### 1.1 Cheap-first, expensive-last

Per-event triggers (a new claim insert, new evidence link, new arxiv paper) fire **Nutty** — a 14B reasoner, ~9 GB footprint, free local. Output goes to a draft pool, not directly to the UI.

The expensive **Rakon → AstroSage-70B** chain (already designed in `research_ideas_tab_design_v1.md` §3) keeps running **weekly only**, processing the top-10 most-active pages. Its job changes from "generate ideas from scratch" to "read existing drafts and curate."

This inverts the v1 design's "Rakon does everything, nightly batch." Rakon stays the gold standard but no longer the bottleneck for keeping the tab fresh.

### 1.2 Event-driven over schedule-driven

Cron-only systems waste cycles when nothing has changed and lag when everything changes at once. Auto-improvement runs primarily on signal:

- New claim on a page → consider new ideas for that page.
- New evidence settling a debate → consider new ideas for that debate's page.
- New survey created → consider new ideas across all pages mentioning it.

Schedule-driven work is reserved for batched compute that benefits from amortizing model cold-loads (weekly Rakon pass) or for slow-changing signals (daily surveys freshness sweep).

### 1.3 Ideas are living artifacts — no time-based decay

Papa's directive (2026-05-13): a research idea should not expire just because time passed. An idea is retired only when the topic has been answered — when a paper exists that directly addresses the research question. Otherwise the idea stays in the pool, continuously refreshed as new claims, evidence, and surveys land.

The draft tier exists to quarantine unreviewed content from the public UI, not to age it out. Drafts that don't get promoted simply remain drafts indefinitely; they accumulate anchors and get text refreshed as new evidence touches them.

| Signal | Effect on draft / active idea |
|---|---|
| Re-emitted by weekly Rakon pass | → promote draft to `active` |
| Papa save ★ on a draft (admin view) | → promote to `active` + `saved_by_papa=TRUE` |
| Atom-7B novelty ≥ 0.7 AND ≥3 anchors AND TF-IDF cosine < 0.6 against active | → soft-promote to `active` |
| New claim / evidence / arxiv paper anchors to an existing draft or active idea (overlap ≥ 2 shared anchors OR cosine ≥ 0.65 against question text) | → **refresh in place** (Nutty rewrites why_now / approach using new context; `last_refreshed_at` and `refresh_count` updated) |
| Weekly Atom-7B coverage scan detects a paper that directly addresses the question (§3.6) | → retire to `status='covered'` with `covered_by_arxiv_id` link |
| Duplicate of an already-active idea (cosine ≥ 0.75) at write time | → drop on write |
| Draft is N days old without promotion | → **no effect.** Drafts do not age out. |

Net effect: the tab shows curated content while the background pool grows and self-updates. The only thing that ever removes an idea from the rotation is the literature catching up to it.

---

## 2. System 1 — Auto Research Ideas Generator

### 2.1 Schema delta

Reuse the existing `research_ideas.status` enum. Add **`'draft'`** and **`'covered'`** as allowed values alongside the existing five (`active | saved | stale | superseded | rejected`). Zero schema change for status — `status` is `VARCHAR(20)`.

Default API list (`GET /api/research/ideas/{slug}`) returns `status IN ('active', 'saved', 'draft')` — **drafts are publicly visible** per Papa's Q2 ruling. Open source = open everything: visiting astronomers see the same content Papa does, including unreviewed lightweight-pipeline ideas. The `'covered'` set is exposed at a separate endpoint `GET /api/research/ideas/{slug}/covered` so visitors can see "questions the literature has answered" as a follow-the-leader retrospective. `'stale'` (manual-only via "Mark stale ⊘") and `'rejected'` / `'superseded'` remain excluded from the default list.

**UI hint:** the frontend Research Ideas tab should render a small `draft` badge on idea cards with `status='draft'` so the reader knows the idea has not yet survived Rakon's curation pass. Cards with `status='active'` (or `'saved'`) need no badge.

Add new columns and a refresh-log table (single migration `auto_research_improvement_v1`):
```sql
ALTER TABLE research_ideas
  ADD COLUMN promoted_at         TIMESTAMP,
  ADD COLUMN promoted_by         VARCHAR(40),    -- 'rakon_weekly' | 'papa_save' | 'atom_soft' | 'manual'
  ADD COLUMN last_refreshed_at   TIMESTAMP,
  ADD COLUMN refresh_count       INT NOT NULL DEFAULT 0,
  ADD COLUMN covered_by_arxiv_id VARCHAR(30),    -- e.g. '2511.04217'
  ADD COLUMN covered_at          TIMESTAMP,
  ADD COLUMN covered_confidence  NUMERIC(3,2);   -- Atom-7B score 0.00-1.00
CREATE INDEX ix_research_ideas_status_created  ON research_ideas(status, created_at);
CREATE INDEX ix_research_ideas_last_refreshed  ON research_ideas(last_refreshed_at);

-- Audit log: every text refresh writes one row. Lets us reconstruct an idea's
-- evolution and roll back if a refresh ever degrades the text.
CREATE TABLE research_idea_refresh_log (
    id              SERIAL PRIMARY KEY,
    idea_id         INT NOT NULL REFERENCES research_ideas(id) ON DELETE CASCADE,
    refreshed_at    TIMESTAMP NOT NULL DEFAULT NOW(),
    trigger_kind    VARCHAR(40) NOT NULL,    -- 'claim_inserted' | 'evidence_linked' | 'new_arxiv' | 'manual'
    trigger_ref_id  VARCHAR(40),             -- e.g. claim_id or arxiv_id
    model_chain     VARCHAR(120) NOT NULL,   -- 'nutty→atom-7b'
    old_question    TEXT NOT NULL,           -- pre-refresh snapshot
    old_why_now     TEXT NOT NULL,
    old_approach    TEXT NOT NULL,
    new_question    TEXT NOT NULL,
    new_why_now     TEXT NOT NULL,
    new_approach    TEXT NOT NULL,
    anchors_added   JSONB                    -- list of new anchor ref_ids
);
CREATE INDEX ix_research_idea_refresh_log_idea ON research_idea_refresh_log(idea_id);
```

`promoted_at`, `promoted_by`, `last_refreshed_at`, `refresh_count`, `covered_*` are all NULL/0 for drafts at creation and for `seeded=TRUE` legacy rows. Populated when the relevant transition fires.

### 2.2 Trigger conditions

The auto-generator listens on four signals.

**T1 — Claim inserted (`post-claim-insert` hook):**
- Debounce: 1 hour per `page_id`. Multiple claim inserts in the same hour collapse to a single regeneration.
- Skip if page has ≥5 drafts already (the pool is full; let the weekly pass curate first).
- Action: queue `process_lightweight_event(page_id, trigger='claim_inserted', cause_id=<claim_id>)`.

**T2 — Evidence-linking step settles a new debate (jury hook):**
- Debounce: 6 hours per `page_id`.
- Trigger only when `claim.trust_level` transitions to `'debated'` (fresh conflict surfaced).
- Action: same task, with `trigger='evidence_linked'`.

**T3 — Page health crosses below 0.65:**
- Already computed by the renovation pipeline; subscribe to `health_score` updates.
- Debounce: 24 hours per page.
- Action: same task, with `trigger='health_drop'`.

**T4 — New survey added:**
- See §4.2 (cross-feature). Triggers a different, cross-page task.

**T5 — New arXiv paper tagged to a page (`post-arxiv-related-page` hook):**
- Debounce: 6 hours per `page_id`.
- Fires whenever the arxiv ingest writes a paper with `slug` in its `related_pages`.
- Action: same task, with `trigger='new_arxiv'` and `cause_id=<arxiv_id>`.
- Rationale: a new paper is exactly the kind of context that should refresh existing ideas' `why_now` or unlock new ideas.

**Why no time-based cron for lightweight generation?** Pages with no activity don't need new ideas; pages with activity already trigger T1/T2/T3/T5. A blind schedule wastes compute on dead pages.

**Update-in-place check (runs FIRST in every per-event task):** before generating new candidates, the task identifies existing draft+active ideas on the same page whose anchors overlap with the trigger's cause (e.g. the new claim shares a debate context with an existing draft's anchored debate, or the new arxiv paper is on the same survey-combo and subtopic as an existing idea). For each matched idea, the task runs a Nutty refresh (§2.3) instead of a fresh-generation. New-candidate generation runs only on the remaining "no-match" slack.

### 2.3 Lightweight pipeline (per-event, Nutty + Atom-7B)

Every per-event task forks at the start into a **refresh path** and a **generate path**, sharing the same context bundle.

```
┌── context bundler ────────────────────────────────────────────────┐
│  • Page title + hero_tagline                                      │
│  • Top-10 claims by trust (not top-20)                            │
│  • Active debates (all)                                           │
│  • Recent arxiv: last 90 days, page-tagged                        │
│  • Trigger context: which signal fired, the cause ref id          │
│  • Existing draft+active+saved ideas on this page WITH anchors    │
└─────────────────────────────────────────────────────────────────────┘
                              │
              ┌───────────────┴────────────────┐
              ▼                                ▼
┌── REFRESH PATH ────────────────┐  ┌── GENERATE PATH ─────────────┐
│  For each existing idea whose  │  │  Only if refresh path didn't │
│  anchors overlap the cause     │  │  consume the event AND page  │
│  (shared debate, shared survey │  │  has <5 drafts already.      │
│  combo + subtopic, shared      │  │                              │
│  arxiv id) OR whose question   │  │  Nutty (deepseek-r1:14b):    │
│  cosine ≥ 0.65 against the     │  │  generate 3 candidate ideas. │
│  cause text:                   │  │  Temperature 0.5, ~20-30 s   │
│                                │  │  warm. Same JSON schema as   │
│  Nutty refresh prompt (§2.5b)  │  │  the v1 Rakon output.        │
│  rewrites why_now + approach   │  │                              │
│  using the new context.        │  │                              │
│  question text changes only if │  │                              │
│  the cause materially expands  │  │                              │
│  scope; default is preserve.   │  │                              │
│                                │  │                              │
│  Snapshot old text → write     │  │                              │
│  research_idea_refresh_log     │  │                              │
│  row. Update research_ideas:   │  │                              │
│    last_refreshed_at = NOW()   │  │                              │
│    refresh_count += 1          │  │                              │
│  Insert new anchors (NEVER     │  │                              │
│  remove existing anchors).     │  │                              │
└─────────────────────────────────┘  └───────────────────────────────┘
              │                                │
              ▼                                ▼
              └──────────────►◄────────────────┘
                              │
                              ▼
┌── Atom-7B: novelty + feasibility + dedup ──────────────────────────┐
│  Applies to the GENERATE path only (refresh path skips scoring —   │
│  the idea already passed it once).                                 │
│  Score each new candidate on (novelty, feasibility).               │
│  TF-IDF cosine dedup against existing draft+active+saved.          │
│  Drop if cosine ≥ 0.75 (duplicate; usually means the refresh path  │
│  should have caught it — log) OR novelty < 0.4 OR feasibility<0.3. │
└─────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌── persist ──────────────────────────────────────────────────────────┐
│  REFRESH path: UPDATE research_ideas (already done above), INSERT  │
│    new anchors into research_idea_anchors / research_idea_surveys, │
│    INSERT research_idea_refresh_log audit row.                     │
│  GENERATE path: INSERT research_ideas (status='draft',             │
│    model_chain='nutty→atom-7b', generated_by_run_id=<run>),        │
│    INSERT anchors + surveys.                                       │
│  Log run to autowiki_runs (kind='research_ideas_lightweight')      │
│  with metrics: refreshed_count, generated_count, dropped_count.    │
└─────────────────────────────────────────────────────────────────────┘
```

Wall-time budget: ~30 s for refresh-only (faster — no Atom scoring), ~60 s for refresh+generate warm, ~120 s cold.

**Anchor-merge rule:** the refresh path never *removes* anchors. An idea's anchor list only grows. The refresh log carries the diff (`anchors_added` column) so a future reader can see "this idea originally cited 3 claims and 1 arxiv paper; over 9 refreshes it has accumulated 14 claims and 11 arxiv papers." That trail is the visible evidence that the idea is alive.

### 2.4 Heavy weekly pass (Rakon, repurposed)

The v1 design's nightly batch becomes a **weekly Sunday batch**. Same Rakon → AstroSage-70B → Atom-7B chain. Its scope changes:

- **Inputs**: top-10 pages by `(debate_count + arxiv_papers_last_30d_count + draft_count)` (note: draft count now weights selection).
- **For each page**: Rakon reads existing active + draft ideas, then emits a curated set of 12 candidates.
- **Promotion logic**:
  - If Rakon's candidate matches an existing draft (cosine ≥ 0.65) → that draft is **promoted** to `active`, with `promoted_at=NOW(), promoted_by='rakon_weekly'`. Rakon's emission is dropped (it's redundant).
  - If Rakon emits a candidate that doesn't match any draft → it lands as a normal `active` idea via the existing v1 path.
- **No demotion of un-promoted drafts.** Per §1.3, drafts do not age out. A draft un-touched by Rakon this week stays a draft for next week's pass. The only automatic retirement path is §3.6 (coverage detection by literature).

**Why Sunday?** Lowest activity window globally; lowest contention with `deep_synthesis` cron (10:00 KST other days); easy for Papa to spot-check the diff Monday morning.

**Fallback if Rakon is unavailable on a Sunday (Papa Q5 ruling).** Do **not** skip the pass. Fall back to **Buddle (deepseek-r1:32b)** for the skeleton step. The chain becomes: Buddle (skeleton) → AstroSage-70B (polish) → Atom-7B (scoring/promotion). Buddle is ~20 GB on Mac Pro; can co-run with Mac Studio AstroSage; cold-load is ~30 s vs Rakon's several minutes. Quality is lower than Rakon — Buddle's reasoning depth is less — but Papa's directive is to move swiftly at lower quality rather than wait a week. The run is logged with `model_chain='buddle→astrosage-70b→atom-7b'` and `fallback_reason='rakon_unavailable'` so the next-week Rakon pass can re-emit and reinforce. Drafts promoted by a Buddle-skeleton run are marked `promoted_by='buddle_weekly'` (distinct from `'rakon_weekly'`) so telemetry can compare promotion-quality across the two chains.

**Time slot:** Rakon weekly pass starts at **03:00 KST Sunday**. AstroSage-70B polish runs on the promoted batch at **04:00 KST Sunday** (Mac Studio; coordinates with Blanc — see §6).

### 2.5 Nutty prompt (full)

```python
NUTTY_LIGHTWEIGHT_PROMPT = """You are an astronomy research strategist generating
SHORT-FORM research ideas in response to a recent change on a wiki page.

WIKI PAGE
---------
Title: {title}
Slug: {slug}
Tagline: {hero_tagline}

TRIGGER
-------
A {trigger_kind} just fired. Context:
{trigger_context}

TOP CLAIMS (by trust):
{claims_block_10}

ACTIVE DEBATES:
{debates_block}

RECENT LITERATURE (last 90d):
{arxiv_block_15}

EXISTING IDEAS ON THIS PAGE (do NOT duplicate):
{existing_ideas_short}

ALLOWED SURVEY COMBOS (use exactly two):
JWST+DESI, JWST+Euclid, JWST+ALMA, JWST+HSC, JWST+LSST, JWST+VLA,
DESI+Euclid, DESI+HSC, DESI+ALMA, DESI+LSST,
ALMA+Euclid, ALMA+HSC, ALMA+LSST, ALMA+VLA,
Euclid+HSC, Euclid+LSST, HSC+LSST, LSST+VLA

OUTPUT — strict JSON, NO prose. Generate 3 candidate ideas (or fewer if
quality dictates):
{{
  "skeletons": [
    {{
      "combo": "JWST+DESI",
      "question": "<1-sentence research question, falsifiable>",
      "why_now": "<1-2 sentences anchored to the trigger>",
      "approach": "<2-3 sentences: data, cuts, measurement, expected N>",
      "anchors": {{
        "claim_ids": [...],
        "debate_ids": [...],
        "arxiv_ids": [...]
      }}
    }},
    ...
  ]
}}

CONSTRAINTS:
- Each question MUST be answerable only by combining the two named surveys.
- Each question MUST reference at least 1 claim_id OR 1 debate_id.
- Quality over quota — emit 1 good idea rather than 3 weak ones.
- No vague verbs ("understand", "explore"); use ("measure", "constrain",
  "test whether", "rule out").
"""
```

Atom-7B's scoring prompt is unchanged from `research_ideas_tab_design_v1.md` §3.3.3.

### 2.5b Nutty refresh prompt (full)

```python
NUTTY_REFRESH_PROMPT = """You are an astronomy research strategist UPDATING an
existing research idea in response to a new piece of evidence. You are NOT
generating a new idea.

EXISTING IDEA (do not change the question unless the new evidence materially
expands its scope; default is to preserve the question text verbatim)
---------------------------------------------------------------------
Question:   {question}
Why now:    {why_now}
Approach:   {approach}
Anchors:    {anchors_summary}     (e.g. "5 claims, 1 debate, 7 arxiv papers")

WIKI PAGE
---------
{title} — {hero_tagline}

NEW EVIDENCE (the trigger)
--------------------------
Kind:        {trigger_kind}       ('claim_inserted' | 'evidence_linked' |
                                   'new_arxiv' | 'health_drop' | 'new_survey')
Reference:   {trigger_ref_summary} (e.g. claim text, arxiv title + abstract)

TASK:
1. Decide whether the new evidence STRENGTHENS, COMPLICATES, or is TANGENTIAL
   to the existing question.
2. If STRENGTHENS or COMPLICATES, rewrite `why_now` (2-3 sentences) to weave
   in the new evidence — citing the specific claim text or paper title. Keep
   `why_now` length similar to the original.
3. If STRENGTHENS, optionally update `approach` (3-5 sentences) only if the
   new evidence changes data availability, sample size, or required cuts.
4. Only edit `question` if the new evidence makes the original question too
   narrow (e.g. a debate around the same axis now requires a follow-up the
   original didn't anticipate). Default: keep verbatim.
5. If TANGENTIAL, return {{"action": "skip"}} — no rewrite, no row touched.

OUTPUT JSON:
{{
  "action": "refresh" | "skip",
  "verdict": "strengthens" | "complicates" | "tangential",
  "question":  "<question text, usually unchanged>",
  "why_now":   "<rewritten>",
  "approach":  "<rewritten or unchanged>",
  "rationale": "<one sentence explaining the rewrite for the audit log>"
}}
"""
```

### 2.6 Failure modes

| Failure | Detection | Recovery |
|---|---|---|
| Nutty timeout | httpx.ReadTimeout | Log to autowiki_runs; trigger stays armed; retry on next signal |
| Nutty emits 0 valid candidates | JSON parse | Log + skip — page just doesn't need new ideas right now |
| Atom dedup drops all 3 | survival count | Log; this is healthy noise filtering |
| Refresh-path text rewrite drops a key constraint from the question (regression) | Pre/post diff in `research_idea_refresh_log` | Papa can revert via `POST /api/admin/research/ideas/{id}/revert-refresh/{log_id}` (v1.1); v1.0 — manual SQL using the log's `old_*` columns |
| Page has no `survey_combo` matches in surveys table | research_idea_surveys join | Log orphan to `surveys_orphans` (see §4.1), keep the idea — orphan link doesn't block insert |
| Renovation campaign saturates Nutty | rate-limit hit | Defer per-event ideas: queue with delay 1h |

### 2.7 Rate limits

- **Nutty lightweight pipeline:** ≤ 8 calls / hour globally (one per page, debounced). With ~43 wiki pages and the debounce, steady-state is ~30-40 calls / day.
- **Rakon weekly pass:** 10 pages × ~5 min each = ~50 min Rakon dwell. Stays within the existing `deep_synthesis` budget envelope; staggered to Sunday only.
- **AstroSage-70B polish:** batched across the Rakon-promoted set, batch size 4, ~20-30 min total Sunday window.

---

## 3. System 2 — Auto Surveys Freshness

### 3.1 What changes about a survey?

Survey metadata is mostly stable, but a few fields drift:

| Field | Frequency of change | Detectable signal |
|---|---|---|
| `current_data_release` | Quarterly–yearly | Press-release headlines, arxiv abstract DR-string mentions |
| `flagship_programs[]` | Yearly (cycle release) | Press releases |
| `description` | Rare | Manual on Papa request |
| `sky_coverage_deg2` | Once per survey | Press release on survey completion |
| `data_volume` | Continuous | Out of scope for v1.0 — too granular |
| `status` | Lifecycle events (launched, retired) | News + arxiv |
| `archive_url`, `mission_url` | Almost never | Manual fix on 404 |

v1 freshness focuses on the **current_data_release** field (highest-frequency drift) and **status** (highest-impact drift).

### 3.2 Detection signal 1 — Daily news headline pass (Mima)

Mima already runs the news-curator at KST 01:00. Extend her existing pipeline (do NOT add a new cron — fold into the existing window).

After the standard news-curation pass, run a **survey-DR classifier** pass:

```python
# Pseudocode for the additional Mima pass
for headline in news_last_24h:
    for survey in surveys:
        # Match: survey acronym OR survey name in headline
        if survey.name in headline.title or survey.full_name in headline.title:
            # Look for DR-class language
            if re.search(r'(DR\d+|Data Release|first[- ]?light|public release|retired)', headline.title, re.I):
                # Mima classification call: is this a DR announcement?
                if mima.classify(headline, prompt=DR_CLASSIFIER_PROMPT) == 'yes_dr_announcement':
                    queue_survey_update_proposal(survey, headline)
```

Mima's classifier prompt:

```python
MIMA_DR_CLASSIFIER_PROMPT = """You are classifying a news headline for whether it
announces a new astronomical survey data release or status change.

Headline: {title}
URL: {url}
Survey: {survey_name} ({survey_acronym})
Current DR in our records: {current_dr}

QUESTION: Does this headline announce one of the following?
1. A new data release (e.g. "DR2", "Data Release 3", "Q1 release")
2. A status change (first light, commissioning end, retirement)
3. A new flagship program / observing cycle

Answer JSON:
{{
  "is_announcement": "yes" | "no",
  "kind": "dr" | "status" | "program" | "other",
  "extracted_dr_string": "<new DR string if kind=dr, else empty>",
  "extracted_status": "<new status if kind=status, else empty>",
  "confidence": <0-1>
}}

ONLY classify as 'yes' if the announcement is the canonical event (not a
recap, anniversary, or paper that references the DR).
"""
```

When `is_announcement='yes'` AND `confidence ≥ 0.6`, write a proposal row:

```sql
CREATE TABLE survey_update_proposals (
    id              SERIAL PRIMARY KEY,
    survey_id       INT NOT NULL REFERENCES surveys(id) ON DELETE CASCADE,
    field           VARCHAR(40) NOT NULL,    -- 'current_data_release' | 'status' | ...
    current_value   TEXT,
    proposed_value  TEXT NOT NULL,
    source_kind     VARCHAR(20) NOT NULL,    -- 'mima_news' | 'atom_arxiv' | 'manual'
    source_url      TEXT,
    source_excerpt  TEXT,
    confidence      NUMERIC(3,2),
    status          VARCHAR(20) NOT NULL DEFAULT 'pending',
                    -- pending | approved | rejected | superseded
    created_at      TIMESTAMP NOT NULL DEFAULT NOW(),
    reviewed_at     TIMESTAMP,
    reviewed_by     VARCHAR(40)
);
CREATE INDEX ix_survey_update_proposals_status ON survey_update_proposals(status);
```

A pending proposal triggers a Discord webhook to #general with the diff + an admin URL.

**Apply policy — two-tier (Papa Q4 ruling).** Load-bearing fields always queue for Papa one-click approve. Low-stakes fields auto-apply on high confidence. See §3.7 for the field tiers and the confidence floors. The default for any survey field not explicitly classified as low-stakes is "queue for review."

### 3.3 Detection signal 2 — Weekly arxiv abstract cross-scan (Atom-7B)

Mondays 02:00 KST, an Atom-7B pass reads new arxiv abstracts from the last 7 days and checks for DR-version mismatches:

```python
# Pseudocode
for paper in arxiv_papers_last_7d:
    for survey in surveys:
        if survey.name in paper.abstract or any(prog in paper.abstract for prog in survey.flagship_programs):
            # Atom scores: does the abstract reference a DR string newer than ours?
            score = atom.score(paper.abstract, survey, prompt=ATOM_DR_DETECTION_PROMPT)
            if score.newer_dr_mentioned:
                queue_survey_update_proposal(survey, paper, source_kind='atom_arxiv')
```

Atom is the right model here: he's already the domain classifier for arxiv content (per his charter), and a 7B model on ~5 GB is appropriate for an abstract scan.

**Why weekly, not daily?** Arxiv abstracts lag press releases by days to weeks. Weekly cadence catches DRs that didn't get news-curator coverage (smaller surveys), without burning daily Atom cycles on a near-empty signal.

### 3.4 Status changes

Surveys transitioning from `commissioning → operational` (e.g. Rubin/LSST first-light expected 2026) need the field flipped. Both Mima and Atom signals catch this — high-impact when it lands. Same `survey_update_proposals` flow with `field='status'`.

### 3.5 Description rewrites

Not automated. Marked here for completeness:

- Trigger: Papa flags a survey description as stale via Discord.
- Owner: Blanc (general-domain drafter) — mission/operational text is not science synthesis.
- Cadence: on-demand only. Not on a schedule.

### 3.5b Low-stakes auto-apply (Papa Q4 ruling)

Some survey-metadata corrections carry near-zero downside risk if auto-applied: a broken `archive_url`, a typo in `data_volume`. Papa's Q4 ruling: auto-apply these on high confidence, no proposal queue review.

**Field-tier classification:**

| Field | Tier | Auto-apply rule |
|---|---|---|
| `archive_url`, `mission_url` | **LOW** | Auto-apply if (current value 404s OR is invalid URL) AND proposed value is a working URL (HEAD 200 response) AND `source_kind='atom_arxiv'` OR `source_kind='link_check'`. No confidence floor needed — the URL works or doesn't. |
| `data_volume` | **LOW** | Auto-apply if change is a units / formatting fix (e.g. "50TB" → "~50 TB/yr") and proposed string parses to the same numeric value as current. Confidence ≥ 0.85. |
| `description` punctuation / grammar | **LOW** | Auto-apply if diff is ≤ 5 character-level edits AND no word added or removed. Confidence ≥ 0.90. |
| `current_data_release` | **HIGH** (queue) | Always queue — this drives every Research Idea card. |
| `status` | **HIGH** (queue) | Always queue — lifecycle transition (operational/retired) affects all dependent UI. |
| `sky_coverage_deg2` | **HIGH** (queue) | Always queue — numeric facts about a survey. |
| `flagship_programs[]` | **HIGH** (queue) | Always queue — Papa's research context depends on accuracy. |
| `instruments[]` | **HIGH** (queue) | Always queue — same. |
| `wavelength_range`, `wavelength_band`, `redshift_range` | **HIGH** (queue) | Always queue — same. |
| Any other field | (default) **HIGH** (queue) | Conservative default for any future field added to `surveys`. |

**Pipeline change:** when Mima (J6) or Atom (J7) detects a candidate field change, the proposal-writer now branches:

```python
def queue_survey_update_proposal(survey, source, field, proposed_value, confidence):
    tier = classify_field_tier(field)
    if tier == 'LOW' and meets_low_stakes_floor(field, source, proposed_value, confidence):
        apply_directly(survey, field, proposed_value, source)         # no queue
        log_to_autowiki_runs(kind='surveys_freshness_autoapply', ...)
        # Discord webhook: informational, post-fact ("auto-applied X → Y on jwst")
    else:
        insert_survey_update_proposal(...)                            # queue for Papa
        # Discord webhook: pending review
```

**Auditability:** every auto-apply writes:

```sql
CREATE TABLE survey_autoapply_log (
    id              SERIAL PRIMARY KEY,
    survey_id       INT NOT NULL REFERENCES surveys(id) ON DELETE CASCADE,
    field           VARCHAR(40) NOT NULL,
    old_value       TEXT,
    new_value       TEXT NOT NULL,
    source_kind     VARCHAR(20) NOT NULL,
    source_url      TEXT,
    source_excerpt  TEXT,
    confidence      NUMERIC(3,2),
    applied_at      TIMESTAMP NOT NULL DEFAULT NOW(),
    reverted_at     TIMESTAMP,
    reverted_by     VARCHAR(40)
);
```

If a low-stakes auto-apply turns out to have been wrong, Papa or HwaO can revert via `POST /api/admin/surveys/autoapply/{id}/revert` (v1.1) or by setting the old value via SQL. The Discord webhook on each auto-apply gives Papa a passive review channel without forcing him into the loop.

**Why this is safe:**
- URL fixes are objectively checkable (HEAD requests verify the proposed URL works).
- Numeric-equivalence checks on `data_volume` guarantee no factual change.
- ≤5-char punctuation fixes can't lose information.
- Every auto-apply is logged with full source context — fully revertable.
- Discord post-fact notification = passive Papa oversight without active review burden.

**Why nothing else qualifies as low-stakes:** A wrong DR string mis-labels every Research Idea card site-wide. A wrong sample-size fact gets quoted by a researcher. A wrong status (showing "operational" for a retired mission) leads someone to plan around it. The asymmetric cost says: queue everything except objectively-checkable maintenance fixes.

### 3.6 Coverage detection — the only automatic Research Ideas retirement path

Per §1.3, a research idea retires only when the literature has answered it. This section defines that detection.

**When:** Tuesday 02:00 KST. Separate day from J7 (Monday) so two Atom-7B weekly passes don't collide.

**Who:** Atom-7B (job **J11**).

**Inputs:** all `research_ideas` with `status IN ('draft', 'active', 'saved')` AND not already `covered`. Each idea provides `(question, why_now, approach, survey_combo, page_slug, anchors)` to the matcher.

**Source pool:** `arxiv_papers` submitted in the last **180 days** that share at least one survey-name match with the idea's combo, scoped to the idea's `page_slug` in `related_pages`. (180 days because a paper that addresses an idea takes weeks to months to surface in citations; a narrower window misses near-coverage.)

**Two-step pipeline:**

1. **TF-IDF + embedding pre-filter** (no model call): for each idea × paper pair in the page-scoped pool, compute cosine similarity between the idea's `(question + approach)` text and the paper's `(title + abstract)`. Keep pairs with cosine ≥ 0.55. Empirically this drops 95%+ of pairs before the Atom call.

2. **Atom-7B coverage classifier** on the surviving pairs:

```python
ATOM_COVERAGE_PROMPT = """You are determining whether an astronomy paper directly
addresses a previously-posed research question.

RESEARCH QUESTION
-----------------
{question}

CONTEXT FROM THE IDEA
---------------------
Why posed: {why_now}
Proposed approach: {approach}
Survey combo: {combo}

CANDIDATE PAPER
---------------
Title:    {paper_title}
Authors:  {paper_authors}
Abstract: {paper_abstract}
Submitted: {paper_date}
arXiv ID:  {arxiv_id}

CLASSIFY (be conservative — false positives retire a still-valuable idea):

answers_question:
  "fully"    — paper measures the exact quantity proposed, on the same data
               combination, with results that conclude the question
  "partial"  — paper makes a related measurement but doesn't close the
               question (different sample, different survey combo, only
               correlative, etc.)
  "no"       — paper is on the same topic but doesn't address THIS question

confidence: 0.0 - 1.0 — your certainty in the classification

OUTPUT JSON:
{{
  "answers_question": "fully" | "partial" | "no",
  "confidence": <float>,
  "one_line_rationale": "<plain text>"
}}
"""
```

**Retirement rule:** an idea transitions to `status='covered'` only when **both**:

- `answers_question == 'fully'`
- `confidence ≥ 0.70`

For `'partial'` matches or `'fully'` matches with confidence 0.5–0.7, write a row to a `research_idea_coverage_candidates` review queue (similar pattern to `survey_update_proposals` — Papa approves the retirement via Discord). For confidence < 0.5, drop silently.

**Grace period:** even at confidence ≥ 0.70, the transition is not immediate. The pipeline writes `covered_at = NOW() + INTERVAL '24 hours'` and posts to Discord: *"Atom-7B believes idea #N is fully covered by arXiv:XXXX.YYYYY. Auto-retires in 24h. Reply `!keep N` to override."* Papa or HwaO has 24h to reply. If overridden, the idea returns to `status='active'` (or its prior status) with an `overrides_log` entry. If no reply, the cron transitions it.

**Database transitions on retirement:**
```sql
UPDATE research_ideas
SET status              = 'covered',
    covered_by_arxiv_id = '<arxiv_id>',
    covered_at          = NOW(),
    covered_confidence  = <atom_confidence>
WHERE id = <idea_id>;
```

The idea stays visible at `GET /api/research/ideas/{slug}/covered` (per §2.1) — a follow-the-leader retrospective: "questions we asked, that the literature has now answered, with a paper link to the answer." This is genuinely valuable signal for Papa and for visiting researchers; it's NOT a hide-and-forget.

**Why this is the only retirement path:** Papa's directive (2026-05-13). A question doesn't expire because time passed — it expires because the field has answered it. Anything else is opinion-based decay, and the system would lose ideas to silence rather than to progress.

**Why human-in-loop?** Like surveys metadata, coverage retirement is load-bearing — wrongly retiring an active research direction sends bad signal to anyone reading the page. The 24h grace period + Discord ping is the cheapest possible review mechanism that preserves Papa's veto.

**Storage of coverage candidates that don't yet pass the bar:**
```sql
CREATE TABLE research_idea_coverage_candidates (
    id              SERIAL PRIMARY KEY,
    idea_id         INT NOT NULL REFERENCES research_ideas(id) ON DELETE CASCADE,
    arxiv_id        VARCHAR(30) NOT NULL,
    answers_kind    VARCHAR(10) NOT NULL,   -- 'fully' | 'partial'
    confidence      NUMERIC(3,2) NOT NULL,
    rationale       TEXT,
    status          VARCHAR(20) NOT NULL DEFAULT 'pending',
                    -- pending | approved | rejected | superseded | retired
    detected_at     TIMESTAMP NOT NULL DEFAULT NOW(),
    reviewed_at     TIMESTAMP,
    reviewed_by     VARCHAR(40),
    UNIQUE (idea_id, arxiv_id)
);
CREATE INDEX ix_coverage_candidates_status ON research_idea_coverage_candidates(status);
```

This table holds (a) the 24h-grace-period transitions (status='pending', auto-flip to 'approved' on the cron tick), (b) partial/low-confidence matches (status='pending', Papa decides), (c) historical audit. The auto-retire path writes here first, then atomically promotes to `research_ideas.status='covered'` when the grace period elapses.

**Cadence telemetry to watch:** if J11 retires more than ~5% of active ideas per week, that's surprising and suggests the threshold is too loose. If it retires <0.5% per week sustained, the threshold is too tight. Tunable via env var `COVERAGE_CONFIDENCE_FLOOR`.

---

## 4. Cross-feature integration

### 4.1 Unknown-survey detection (idea → survey gap)

When the lightweight or heavy pipeline writes an idea whose `survey_combo` references a survey not in the directory, the `research_idea_surveys` backfill (per surveys directory v1 §3.2) logs it. Extend that path:

```sql
CREATE TABLE surveys_orphans (
    id                SERIAL PRIMARY KEY,
    raw_token         VARCHAR(40) NOT NULL,        -- "Spitzer" — failed lookup
    idea_id           INT REFERENCES research_ideas(id) ON DELETE CASCADE,
    first_seen_at     TIMESTAMP NOT NULL DEFAULT NOW(),
    last_seen_at      TIMESTAMP NOT NULL DEFAULT NOW(),
    occurrence_count  INT NOT NULL DEFAULT 1,
    resolved_to_survey_id INT REFERENCES surveys(id),
    UNIQUE (raw_token)
);
```

Behavior:
- On every idea insert that fails the lookup, increment `occurrence_count` and update `last_seen_at` for the existing row, or insert a new one.
- When `occurrence_count ≥ 3` AND `resolved_to_survey_id IS NULL` AND no Discord ping in the last 7 days for this token, post to #general: *"3 ideas have referenced unknown survey 'Spitzer' — consider seeding."*
- Papa adds the survey via SQL (or v1.1 admin endpoint), sets `resolved_to_survey_id`, the join table is back-patched.

**No auto-stub of surveys.** A row with only a slug and no metadata is worse than no row — it would corrupt the directory's quality. Human-curated only.

### 4.2 New survey added → cross-page idea scan

When a new survey is INSERTed into `surveys`, queue:

```python
# Celery chain
scan_claims_for_survey.delay(survey_id) \
    .then(generate_ideas_for_matching_pages.delay)
```

Steps:

1. **`scan_claims_for_survey`** (Atom-7B, single batch over all 425 claims):
   - For each claim, Atom scores: "Does this claim's research mention or rely on {survey.name} (or its instruments/programs)?"
   - Threshold: relevance ≥ 0.7. Stores results in a transient `surveys_claim_matches` table (kept for 30 days as an audit aid).
   - Wall time: ~3-5 min for the full set; one-shot per new survey.

2. **`generate_ideas_for_matching_pages`** (Nutty per page):
   - Group matched claims by `page_id`.
   - For each page with ≥3 matches, fire one lightweight idea-generation pass (same `generate_lightweight_ideas` task as §2.3) with `trigger='new_survey'` and the new survey's slug as `cause_id`.
   - Result: a handful of new draft ideas across relevant pages within ~10-15 min of the survey being added.

The new ideas land as drafts and follow the standard promotion path.

**Why this matters:** without this hook, a newly-added survey (say Roman in 2027) would sit there unreferenced until Papa or the Rakon weekly pass eventually surfaced it. With the hook, the system actively integrates new infrastructure into existing wiki context.

### 4.3 Survey deletion / merge

Out of scope for v1. If a survey row is ever removed, `research_idea_surveys` cascades; orphan ideas keep their `survey_combo` string and the deep-link falls back to plain text per surveys directory v1 §5.4.

---

## 5. Schema deltas summary

Single migration: `auto_research_improvement_v1.py`.

```sql
-- 5.1 Extend research_ideas
ALTER TABLE research_ideas
  ADD COLUMN promoted_at         TIMESTAMP,
  ADD COLUMN promoted_by         VARCHAR(40),
  ADD COLUMN last_refreshed_at   TIMESTAMP,
  ADD COLUMN refresh_count       INT NOT NULL DEFAULT 0,
  ADD COLUMN covered_by_arxiv_id VARCHAR(30),
  ADD COLUMN covered_at          TIMESTAMP,
  ADD COLUMN covered_confidence  NUMERIC(3,2);
CREATE INDEX ix_research_ideas_status_created
  ON research_ideas(status, created_at);
CREATE INDEX ix_research_ideas_last_refreshed
  ON research_ideas(last_refreshed_at);

-- 5.2 Audit log for in-place refreshes (§2.1)
CREATE TABLE research_idea_refresh_log (...);
-- full schema in §2.1

-- 5.3 Survey update proposals (§3.2)
CREATE TABLE survey_update_proposals (...);
-- full schema in §3.2

-- 5.3b Survey auto-apply log (§3.5b) — Papa Q4 ruling
CREATE TABLE survey_autoapply_log (...);
-- full schema in §3.5b

-- 5.4 Coverage retirement candidates (§3.6)
CREATE TABLE research_idea_coverage_candidates (...);
-- full schema in §3.6

-- 5.5 Surveys orphans (§4.1)
CREATE TABLE surveys_orphans (...);
-- full schema in §4.1

-- 5.6 Transient claim-matches audit table (§4.2)
CREATE TABLE surveys_claim_matches (
    id          SERIAL PRIMARY KEY,
    survey_id   INT NOT NULL REFERENCES surveys(id) ON DELETE CASCADE,
    claim_id    INT NOT NULL REFERENCES claims(id) ON DELETE CASCADE,
    score       NUMERIC(3,2) NOT NULL,
    matched_at  TIMESTAMP NOT NULL DEFAULT NOW(),
    UNIQUE (survey_id, claim_id)
);
-- v1.2: nightly cleanup of rows older than 30 days
```

`research_ideas.status` does NOT require an enum/schema change (already `VARCHAR(20)`); two new allowed values `'draft'` and `'covered'` documented in the model docstring.

---

## 6. Platoon Assignment

Per `feedback_platoon_assignment.md`: every scheduled or real-time job names its owner with capability + cost + speed justification.

| # | Job | Owner | Machine | RAM | Frequency | Why this member |
|---|---|---|---|---|---|---|
| J1 | Per-event idea generation (T1–T4) | **Nutty** (deepseek-r1:14b) | Mac Studio | ~9 GB | Per event, ≤8/hr global | Fast reasoner with chain-of-thought; right size for "1-3 candidate ideas per page from a small context." AstroSage-70B is overkill (40 GB + 20 s cold-load per event = thrash). Rakon at 404 GB cold-load is absurd for per-event. Atom-7B is a scorer not a generator. |
| J2 | Atom scoring + dedup after J1 | **Atom-7B** | Mac Studio | ~5 GB | Per event, paired with J1 | Domain-aware astronomy scoring is exactly his charter. Co-runs with Nutty without conflict. |
| J3 | Weekly heavy pass — skeleton (primary) | **Rakon** (deepseek-r1:671b) | Mac Pro | ~404 GB | Sunday 03:00 KST, top-10 pages | Multi-step adversarial synthesis to curate the draft pool. No other model can do the depth. Sunday lowest-contention slot. Exclusive Mac Pro tenancy. |
| J3-fallback | Weekly heavy pass — skeleton (fallback) | **Buddle** (deepseek-r1:32b) | Mac Pro | ~20 GB | Sunday 03:00 KST only if Rakon is unavailable | Per Papa Q5: do not skip the weekly pass. Buddle's reasoning depth is lower, but the run completes; promoted ideas get `promoted_by='buddle_weekly'`. Next-week Rakon pass reinforces. |
| J4 | Weekly polish on promoted ideas | **AstroSage-70B** | Mac Studio | ~42 GB | Sunday 04:00 KST | Domain prose polish on the Rakon-promoted set. Batched (size 4). Coordinate with Blanc — see roster check §6.5. |
| J5 | Atom-7B novelty/feasibility on weekly batch | **Atom-7B** | Mac Studio | ~5 GB | Sunday 04:30 KST | Same as J2, same charter, batched over the weekly output. |
| J6 | Daily surveys-DR news classifier | **Mima** (qwen3:30b) | Mac Studio | ~18 GB | KST 01:00 (rides news-curator window) | Already loaded at this hour for news curation. DR-classification is non-astronomy press-release parsing — her charter (general scorer/classifier). Adds ~1-2 min to her existing pass. |
| J7 | Weekly arXiv DR-mismatch scan | **Atom-7B** | Mac Studio | ~5 GB | Monday 02:00 KST | Astronomy-abstract scanning is exactly his charter. ~10-15 min on the last 7d arxiv set. |
| J8 | New-survey claim cross-scan | **Atom-7B** | Mac Studio | ~5 GB | On-demand (new survey INSERT) | Same as J7 — astronomy-domain classification at volume over the claim corpus. |
| J9 | New-survey idea generation across matched pages | **Nutty** | Mac Studio | ~9 GB | On-demand, chained after J8 | Same charter as J1, just batched over multiple pages from one trigger. |
| J10 | Survey description rewrite (rare) | **Blanc** (llama3.3:70b) | Mac Studio | ~42 GB | On-demand only | Non-astronomy mission/operational prose — Blanc's charter. AstroSage-70B reserved for science prose. |
| J11 | Weekly coverage detection (idea ↔ arxiv) | **Atom-7B** | Mac Studio | ~5 GB | Tuesday 02:00 KST | Two-step pipeline: cheap TF-IDF pre-filter (no model) then Atom classification of survivors. Domain-aware astronomy abstract reading is exactly his charter. Separate day from J7 (Monday) so weekly Atom passes don't collide. |

**Members explicitly NOT used in v1.0 as primary owners:**

- **Buddle** — assigned as the **Rakon fallback for J3 only** (Papa Q5). Otherwise no scope fit.
- **Tera** — Mima covers the general-classifier role at the right hour; no second slot needed.
- **Takji** — already saturated on agent loop; would only be considered if Nutty is unavailable.

### 6.5 Roster check

Per `feedback_platoon_assignment.md`: read the live roster before locking the design.

**Snapshot from `~/.openclaw/workspace/memory/platoon-roster.md` at 2026-05-13 KST.**

Roster file last updated 2026-05-11 — most recent inter-session signal places member states as below (re-verify before implementation):

| Member | Status | Current load | Conflict with this design? |
|---|---|---|---|
| 🦖 Rakon | ACTIVE | Galaxy Evolution synthesis (final section was 00:28 KST May 11; may be done by now) | **J3 (Sun 03:00 KST):** uses Rakon exclusively. Galaxy-evolution synthesis is on-demand, not recurring. If Papa fires a Rakon synthesis on a Sunday, queue it for Monday — design holds. |
| Buddle | ACTIVE | Stance jury drain | **J3-fallback** (Sun 03:00 KST when Rakon unavailable). Conditional only. Buddle's stance-jury work yields if a fallback is needed — jury drain pauses ~50 min Sunday. Acceptable. |
| Blanc | ACTIVE | Biblio mining (continuous, 8 thin-evidence pages) | **J4 (Sun 04:00 KST):** AstroSage-70B + Blanc both 70B; **cannot co-run** on Mac Studio. Mitigation: Blanc pauses biblio during the AstroSage Sunday window (~20-30 min). Coordinate with HwaO. **J10 on-demand:** Blanc serial with biblio (already-running pattern, fine). |
| 📊 Mima | ACTIVE | Evidence linking + agent loop | **J6 (KST 01:00):** rides her existing news-curator slot. Adds 1-2 min to a window she already occupies. Compatible. |
| ⚡ Nutty | ACTIVE | Renovation synthesis | **J1 / J9:** rate-limited to ≤8 calls/hr. Renovation synthesis is bursty per-page; per-event ideas add ~5-8 short calls/day. Coexist on Mac Studio (combined <60 GB total load with Mima + Atom). If renovation campaign saturates Nutty's queue, per-event ideas defer to a 1h queue — that's by design. |
| ⚡ Tera | ACTIVE | Renovation synthesis | No conflict (not assigned). |
| ⚡ Takji | ACTIVE | Agent loop (writer/reviewer) | No conflict (not assigned). |
| 🔭 Atom-7B | (assumed available per charter; not in 2026-05-11 snapshot but unrelated to renovation) | Astronomy scoring on-demand | **J2 / J5 / J7 / J8 / J11:** Atom is the smallest local model and co-runs with everything. No conflict. Three weekly Atom slots (Mon 02:00 J7, Tue 02:00 J11, Sun 04:30 J5) are well-separated. |
| 🔭 AstroSage-70B | (assumed available per charter; not in 2026-05-11 snapshot) | Astronomy synthesis on-demand | **J4 (Sun 04:00 KST):** conflicts with Blanc 70B at same hour — addressed above. |
| 🔧 Tori | ACTIVE | Tasks 14 & 15 + Surveys + Research Ideas implementation | Tori implements this design after the roster shifts (current load is just-shipped features). Compatible. |
| 🧠 Groq | ACTIVE | Primary agent loop | Not assigned. |

**Net summary:** Three real conflicts to manage:

1. **AstroSage-70B vs Blanc on Sunday 04:00** — both 70B on Mac Studio. Resolution: AstroSage gets the Sunday window; Blanc biblio mining pauses 20-30 min. HwaO orchestrates the swap.
2. **Rakon weekly pass vs ad-hoc Galaxy Evolution synthesis** — both want exclusive Mac Pro tenancy. Resolution: Sunday 03:00 KST is reserved for the weekly pass; Galaxy Evolution synthesis (which is on-demand) defers if Papa fires one on a Sunday morning.
3. **Nutty per-event vs renovation synthesis** — both want Nutty time. Resolution: rate limit ≤8 calls/hr; per-event ideas are queued when renovation has burst priority.

**Re-evaluation rule (per `feedback_platoon_assignment.md`):** if the roster shifts before this design is implemented, re-check §6.5 in particular. Roster signals to watch for: (a) AstroSage-70B getting a permanent recurring slot that collides with Sunday 04:00; (b) Nutty getting a heavy continuous assignment (would force per-event ideas to a different small model — Takji is the only fallback and that lowers quality); (c) Mima getting reassigned off news-curator (would force J6 to a new owner — Tera is the second-best fit).

---

## 7. Rollout

### 7.1 v1.0 — Auto Research Ideas + Surveys Freshness MVP
- Schema delta migration `auto_research_improvement_v1.py` (includes refresh log, coverage candidates, autoapply log, surveys freshness tables)
- Hooks T1, T3, T5 (claim, health, arxiv) — not T2 yet (wait for stance-jury hook stability)
- Nutty lightweight pipeline with **refresh-path** + **generate-path** (J1) + Atom-7B scoring (J2)
- Weekly Rakon promotion pass (J3 + J4 + J5) — promotion only, no demotion
- **Rakon-down Buddle fallback for J3** (Papa Q5)
- Mima daily DR-classifier (J6) with two-tier apply: low-stakes auto-apply, high-stakes proposal queue (Papa Q4)
- Weekly Atom-7B coverage detection (J11) with 24h Discord grace period
- Drafts publicly visible (Papa Q2) — frontend renders `draft` badge
- `survey_update_proposals`, `survey_autoapply_log`, `research_idea_coverage_candidates` tables + Discord webhooks
- Manual SQL apply (no admin endpoint yet) for high-stakes proposals

### 7.2 v1.1 — Stance-jury hook + admin proposals
- Enable T2 hook (post stance-jury settle)
- Atom-7B weekly arxiv DR cross-scan (J7)
- Admin endpoints:
  - `POST /api/admin/surveys/proposals/{id}/approve`
  - `POST /api/admin/research/ideas/{id}/revert-refresh/{log_id}`
  - `POST /api/admin/research/ideas/coverage-candidates/{id}/{approve|reject}`
- Frontend admin views

### 7.3 v1.2 — Cross-feature integration
- `surveys_orphans` table + Discord ping on threshold
- New-survey hook: J8 (Atom claim-scan) + J9 (Nutty cross-page idea generation)
- Nightly cleanup of `surveys_claim_matches` rows > 30 days
- Public `/research-ideas/covered` retrospective page

### 7.4 v2.0 — Quality telemetry
- Track promotion rates per page, per signal, per model chain
- Track refresh rates: ideas with `refresh_count ≥ 3` are the "living core"
- Track coverage-detection precision (Papa override rate)
- A/B test: Nutty-only vs Nutty + brief Buddle review pass

---

## 8. Decisions log (all resolved 2026-05-13)

All open questions raised during design review have been resolved by Papa. This section records the final decisions for future reference; nothing here is open.

| # | Question | Papa's decision | Implementation locus |
|---|---|---|---|
| Q1 | Draft aging window (14 days → `stale`?) | **Removed entirely.** Drafts never age out. Only retirement path is coverage (§3.6). | §1.3, §2.4 |
| Q2 | Hide drafts from non-admin users? | **No — drafts publicly visible.** Open source = open everything. Frontend renders `draft` badge so readers know it hasn't survived curation. | §2.1 (API default) |
| Q3 | Mima DR confidence floor | **0.6** ✅ (Kun rec approved) | §3.2 |
| Q4 | Auto-apply low-stakes survey fixes? | **Yes** for objectively-checkable fixes: URL 404 repair, units/format-only `data_volume` adjustment, ≤5-char punctuation in `description`. Everything else queues. Full tier classification + auditing in §3.5b. | §3.5b (new section), §5 schema |
| Q5 | Rakon down on Sunday → behavior | **Use Buddle (32B) fallback** — do not skip. Move swiftly at lower quality rather than wait a week. Promoted ideas marked `promoted_by='buddle_weekly'` so telemetry can compare. | §2.4 fallback paragraph, §6 J3-fallback row |
| Q6 | Nutty rate limit | **≤ 8 calls/hr** ✅ (Kun rec approved). Revisit after first month of telemetry. | §2.7 |
| Q7 | Refresh path edits `question` text? | **No, preserve verbatim.** `question` is the user-facing identity of an idea; silent rewrites would degrade trust. Refresh edits only `why_now` and `approach`. (Decided in rev 2.) | §2.5b prompt |
| Q8 | Coverage retirement confidence floor | **≥ 0.70** for auto-retire; 0.5–0.7 to review queue. 24h Discord grace period regardless. (Decided in rev 2.) | §3.6 |

---

## 9. Acceptance criteria (for Tori sign-off)

v1.0 ships when **all** of the following are true:

- [ ] Migration `auto_research_improvement_v1.py` runs clean on a fresh DB and on the current prod DB (no data loss).
- [ ] `research_ideas.status` accepts `'draft'` and `'covered'` as values; API list endpoint default-filters drafts/stale/covered out.
- [ ] `research_idea_refresh_log`, `research_idea_coverage_candidates`, `survey_update_proposals` tables exist with the §2.1 / §3.2 / §3.6 schemas.
- [ ] **No code path writes `status='stale'` automatically.** A linter check or manual code review confirms this. Manual `'stale'` via the existing "Mark stale ⊘" admin action is preserved per the original Research Ideas v1 design.
- [ ] Celery beat entries for (J3) Sunday 03:00 KST Rakon pass, (J6) daily Mima DR-classifier ride existing news-curator schedule, and (J11) Tuesday 02:00 KST coverage detection.
- [ ] T1 hook (post-claim-insert) fires the Nutty pipeline. The pipeline first attempts the **refresh path** against existing draft+active ideas (overlap rule §2.2); only generates new candidates if refresh path didn't consume the event.
- [ ] T3 hook (page health drop) fires the same pipeline.
- [ ] T5 hook (new arxiv paper tagged to a page) fires the same pipeline.
- [ ] Refresh path correctly writes `research_idea_refresh_log` rows with pre/post text snapshots, increments `refresh_count`, and updates `last_refreshed_at`.
- [ ] Rakon weekly pass correctly promotes drafts that match its emissions (`promoted_at`, `promoted_by='rakon_weekly'` populated).
- [ ] J11 coverage pipeline: TF-IDF pre-filter executes; Atom-7B classifies survivors; matches with `answers_question='fully'` AND `confidence ≥ 0.70` schedule a 24h-grace retire via `research_idea_coverage_candidates`.
- [ ] Discord grace-period webhook fires on each scheduled retirement with `!keep` override syntax.
- [ ] Cron tick after 24h elapsed: scheduled retirements without override flip `research_ideas.status='covered'` with full provenance columns populated.
- [ ] `survey_update_proposals` row is written when Mima's classifier returns `is_announcement='yes'` with confidence ≥ 0.6 **AND** field is HIGH-tier per §3.5b.
- [ ] `survey_autoapply_log` row is written AND the corresponding `surveys` field is updated when a LOW-tier signal meets its threshold (URL HEAD 200, numeric equivalence, etc.).
- [ ] Discord webhook fires for both: pending high-stakes proposal AND post-fact auto-applied low-stakes fix.
- [ ] Drafts return in the default `GET /api/research/ideas/{slug}` response (no admin gate). Frontend renders `draft` badge on those cards.
- [ ] If Rakon is unreachable when Sunday J3 fires, the job auto-falls-back to Buddle and completes; run logs `model_chain='buddle→astrosage-70b→atom-7b'` and `fallback_reason='rakon_unavailable'`.
- [ ] `GET /api/research/ideas/{slug}/covered` returns covered ideas with their `covered_by_arxiv_id` + `covered_confidence`.
- [ ] Manual SQL pattern documented in `docs/runbooks/apply_survey_proposal.md` and `docs/runbooks/revert_idea_refresh.md` (one-page runbooks by Tori).
- [ ] No co-run conflicts observed in the first Sunday run (Rakon Mac Pro exclusive; AstroSage-Blanc swap completes).
- [ ] Logs in `autowiki_runs` show `kind='research_ideas_lightweight'`, `kind='research_ideas_coverage'`, and `kind='surveys_freshness'` entries.
- [ ] Papa, reviewing the first weekly Rakon promotion pass, accepts ≥ 50% of the auto-soft-promoted ideas (i.e. the lightweight pipeline isn't producing junk).
- [ ] Papa, reviewing the first 5 coverage retirements, accepts ≥ 4 of them (i.e. the coverage classifier isn't firing on tangential papers).

---

## 10. Risk register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Nutty produces plausible-sounding but science-wrong ideas (no AstroSage polish in lightweight path) | High | Medium | Drafts are quarantined (not visible to public). Rakon weekly pass + AstroSage polish runs on promoted ones only. |
| Per-event volume spikes (e.g. claim-insert storm during renovation) saturate Nutty | Medium | Medium | Rate limit ≤8/hr global + debounce 1h/slug. Excess events drop (lightweight regen on every claim is not required for correctness). |
| Refresh path degrades an idea's text (loses a constraint, weakens question) | Medium | Medium | Every refresh writes pre/post snapshot to `research_idea_refresh_log`. v1.1 admin endpoint allows one-click revert to any prior version. Refresh prompt (§2.5b) defaults to preserving question text. |
| Refresh path runs every event but always classifies "tangential" — wastes Nutty cycles | Medium | Low | The "skip" action is cheap (single Nutty call ~10 s, no DB write). Acceptable cost; monitor via autowiki_runs and tune the overlap heuristic if `skip` rate exceeds 80%. |
| Coverage detection (J11) false-positive: retires a still-active idea | High | High | Two-step pipeline (TF-IDF pre-filter + Atom classifier); confidence floor 0.70; **24h Discord grace period with `!keep` override**; partial/low-confidence matches go to the review queue, not auto-retire. Papa veto recorded in `overrides_log`. |
| Coverage detection false-negative: a paper has clearly answered an idea but it stays in the active pool | Medium | Low | Acceptable. The cost of a stale idea is small (idea is still relevant context); the cost of a wrong retirement is high. Asymmetric — bias toward false-negative. Papa can manual-retire via "Mark stale ⊘" if obvious. |
| Mima false-positive DR detections clog Papa's review queue | Medium | Low | Confidence floor 0.6; auto-supersede a proposal if a higher-confidence proposal arrives for the same field. After 30 days, prune `status='pending'` proposals older than 30 days into `status='superseded'`. DR-class fields are HIGH-tier so they always queue (low-stakes auto-apply does not apply). |
| Low-stakes auto-apply (§3.5b) flips a field to a wrong value | Low | Low | Tier classification is conservative — only objectively-checkable fixes qualify. URL fixes require HEAD 200; numeric fixes require value-equivalence; description fixes are ≤5 chars and word-preserving. Every auto-apply logs to `survey_autoapply_log` with full provenance and is revertable. Discord notification on each auto-apply gives Papa passive review. |
| Rakon weekly pass conflicts with ad-hoc Rakon work on a Sunday | Medium | Medium | Sunday 03:00 is reserved. Ad-hoc Rakon requests on Sunday queue. HwaO enforces. |
| Rakon completely unavailable on a Sunday (404 GB cold-load failure, host reboot, model corruption) | Low | Medium | Buddle (32B) fallback per Papa Q5; chain becomes Buddle → AstroSage-70B → Atom-7B. Lower-quality skeleton but the pass completes; promoted ideas marked `promoted_by='buddle_weekly'`. Buddle's stance-jury work pauses ~50 min Sunday. |
| Draft pool grows unbounded (drafts now never auto-retire — Papa's directive) | Medium | Medium | Per-page cap of 5 drafts at T1 skip (§2.2). At cap, new claims trigger refresh-only on existing drafts. Pool size capped at ~5 × 43 pages = ~215 drafts site-wide. Acceptable. |
| AstroSage-70B Sunday window collides with Blanc indefinitely | Medium | Medium | HwaO orchestrates the swap. If Blanc biblio mining is critical-path, defer the AstroSage polish a few hours; draft promotions still complete via Rakon. |
| Surveys orphan signal never reaches threshold (the same survey is referenced but always under different acronyms) | Low | Low | Slug-resolution layer uses fuzzy match (Levenshtein) at lookup time; `surveys_orphans.raw_token` retains the original spelling for human disambiguation. |
| New-survey claim-scan (J8) runs on a flagship survey (e.g. Roman 2027 launch) and queues 100+ Nutty calls | Low | High | Cap J9 at top-10 matched pages per new survey. Remaining pages get re-scanned by the next weekly Rakon pass. |
| Promotion logic loops: a draft re-emitted by Rakon, then re-emitted again next week, double-counted | Low | Low | Once a draft is `status='active'` it's no longer a draft target; Rakon weekly pass re-matches only against drafts and active. Cosine ≥ 0.65 against active is treated as redundant emission (drop), not double promotion. |

---

## 11. Notes / out of scope

- **No new model weights** downloaded. All eight platoon members in §6 are already installed.
- **No new external API calls.** All signals come from existing pipelines (claims, evidence, news-curator, arxiv ingest).
- **No PII** stored.
- **License:** all generated text (drafts included) is AGPL-3.0 — same as wiki content.
- This doc is the contract for Tori's v1.0 implementation. Any divergence in implementation must be flagged back to Kun for design update.
- Sibling design docs (`research_ideas_tab_design_v1.md`, `surveys_directory_design_v1.md`) are the v1.0 baseline; this doc only adds on top.

---

*— Kun 🔬  ·  Mac Pro  ·  2026-05-13*
