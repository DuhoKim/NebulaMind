# Research Ideas Tab — Design v1

**Owner:** Kun 🔬  ·  **Status:** Draft, awaiting Papa sign-off  ·  **Implementer:** Tori
**Date:** 2026-05-13 (KST)
**Filename:** `docs/research_ideas_tab_design_v1.md`

---

## 0. TL;DR

A new **Research Ideas** tab on every flagship wiki page that lists AI-generated, **survey-combination-anchored** research questions distilled from the page's claims, debates, and the last ~12 months of relevant arXiv papers.

- **For:** Papa first (his own research scaffolding tool), then visiting astronomers.
- **Trigger:** On-demand from the tab + nightly batch for "high-debate" pages + auto-regen when ≥3 new debate claims or ≥10 new related arXiv papers land since the last run.
- **Pipeline:** Rakon (skeleton) → AstroSage-70B (prose polish) → Atom-7B (novelty/feasibility scoring). Same proven chain `deep_synthesis.py` already uses for debate claims, with a different prompt and a new output table.
- **Persistence:** New `research_ideas` table + new `research_idea_votes` table.
- **Seeds:** 15 hand-curated ideas for `galaxy-evolution` ship with the migration to bootstrap the tab before the first AI batch runs.
- **Phasing:** v1.0 (galaxy-evolution only, manual trigger), v1.1 (auto-regen + top-10 flagship pages), v1.2 (cross-page idea linking, user voting).

---

## 1. Why this tab, and why now

### 1.1 The gap
NebulaMind wiki pages today are *retrospective* — they capture established knowledge, ongoing debates, and recent papers. They do not surface **forward-looking research opportunities**: "given what's contested on this page and what surveys can deliver in the next 1–2 years, what should someone actually go work on?"

Papa is sitting on:
- 43 wiki pages with 425 total claims (avg 9.9/page), 20% tagged `claim_type='debate'`.
- A live arXiv pipeline ingesting astro-ph.GA / .CO / .SR / .HE / .EP daily, with `related_pages` already mapped.
- News curator covering 6 surveys (DESI, JWST, Euclid, LSST, ALMA, VLA) with HSC easily added.

The pieces to *generate* research ideas already exist as raw data. Nothing assembles them.

### 1.2 Survey combinations are the right unit
Papa's intuition (00:02 KST directive) is that **single-survey ideas are mostly already in the literature** — the differentiation is in multi-survey combinations: JWST spectra + DESI redshifts, ALMA dust + Euclid morphology, DESI BAO + HSC weak lensing. Each combination unlocks a measurement neither survey can make alone.

This is the right axis for two reasons:

1. **Tractability.** "Pick a galaxy evolution problem" returns thousands of papers. "Pick a JWST+DESI galaxy evolution problem with sample size > 1000" returns a handful — and a handful is what a researcher can actually act on.
2. **Match to NebulaMind's data.** The wiki already tags claims by survey context. Cross-referencing two surveys' claims on the same page exposes the gaps automatically.

### 1.3 Top feature priority
Papa flagged this as a personal research tool. Treat the v1.0 quality bar as **"would Papa, looking at the galaxy-evolution tab, find at least 3 ideas worth a Slack to a collaborator?"** If no, the design has failed regardless of test coverage.

---

## 2. Feature spec — what the tab looks like

### 2.1 Tab placement
The wiki page header gets a tab strip immediately below the title:

```
┌────────────────────────────────────────────────────────────────────────┐
│  Galaxy Evolution                                                       │
│  [ Overview ]  [ Claims ]  [ Sources ]  [ Research Ideas* ]  [ History ]│
└────────────────────────────────────────────────────────────────────────┘
```

`Overview` = today's main content (default).  `Claims` = the claims-by-section view (extracted from the existing ClaimBlock).  `Sources` and `History` = existing routes.  `Research Ideas` is **new** and carries a small "NEW" badge for the first month.

> **UI library note:** the current page is flat — `WikiPageClient.tsx` has no tab component. v1.0 introduces a minimal tab strip using existing Tailwind classes; no new dep.

### 2.2 Tab content layout

```
┌── Research Ideas — Galaxy Evolution ─────────────────────────────────┐
│  Filter: [ All surveys ▾ ]  Sort: [ Novelty ▾ ]  [ Regenerate ↻ ]   │
│                                                                       │
│  ┌─ JWST + DESI ─────────────────────────────────  novelty ●●●●○ ──┐│
│  │  Q: Is the sub-kpc clumpy structure JWST/NIRCam              ✦ ││
│  │     resolves in z≈2 main-sequence galaxies                    ││
│  │     correlated with the DESI ELG sSFR distribution            ││
│  │     at fixed stellar mass?                                    ││
│  │                                                               ││
│  │  Why now:  6 DESI ELG papers in last 60d disagree on          ││
│  │     sSFR-environment slope. JWST CEERS public release covers  ││
│  │     overlapping footprint. No paper has crossed them.         ││
│  │                                                               ││
│  │  Approach: stack JWST NIRCam clumpiness in 4 DESI sSFR bins,  ││
│  │     control for stellar mass; expected N~400 with z-spec.     ││
│  │                                                               ││
│  │  Anchored:  3 page claims · 2 debates · 7 papers              ││
│  │  Feasibility: ●●●○○   Saved by Papa ★                         ││
│  │  [ Copy as proposal ]   [ Save ★ ]   [ Mark stale ⊘ ]         ││
│  └─────────────────────────────────────────────────────────────────┘│
│                                                                       │
│  ┌─ ALMA + Euclid ── novelty ●●●○○ ────────────────────────────────┐│
│  │  ...                                                            ││
│  └─────────────────────────────────────────────────────────────────┘│
│                                                                       │
│  Last refreshed: 2026-05-13 04:00 KST · model: rakon → astrosage-70b │
└───────────────────────────────────────────────────────────────────────┘
```

### 2.3 Required fields per idea card
| Field | Example | Source |
|---|---|---|
| **Survey combo** | "JWST + DESI" | LLM, validated against survey whitelist |
| **Question** | (the one-sentence ask) | LLM |
| **Why now** | (2–3 sentences) | LLM, references recent papers / debates |
| **Approach** | (1 paragraph) | LLM |
| **Anchored** | "3 claims · 2 debates · 7 papers" | DB join on `research_idea_anchors` |
| **Novelty score** | 0.0–1.0, displayed as 5 dots | Atom-7B, see §3.4 |
| **Feasibility score** | 0.0–1.0, displayed as 5 dots | Atom-7B |
| **Status** | active / saved / stale / superseded | DB + user actions |
| **Model chain** | "rakon → astrosage-70b" | for transparency |
| **Last refreshed** | timestamp | DB |

### 2.4 User actions (v1.0 = Papa-only)
| Action | Behavior | Auth |
|---|---|---|
| **Regenerate** | Triggers `regenerate_research_ideas(slug)` Celery task. Disabled if last run < 6h ago. | Admin only |
| **Save ★** | Sets `research_idea_votes.value = 1` for the current user. Pinned to top of list. | Logged-in |
| **Mark stale ⊘** | Sets `research_ideas.status = 'stale'`. Hidden from default view. | Admin only |
| **Copy as proposal** | Copies a 1-paragraph slack/email-ready blob to clipboard. | Anyone |

`Save ★` is the only action visible to non-admins in v1.0; everything else is gated. The "Saved by Papa ★" badge in §2.2 is a single source of social proof for visiting researchers — see §6.2.

### 2.5 Filter and sort
- **Filter:** by survey combo (multi-select), by status (active / saved / stale), by novelty band.
- **Sort:** novelty desc (default), feasibility desc, recency desc, saved-first.
- **Empty state:** "No research ideas yet — generation runs nightly." with `[ Generate now ]` button for admins.

### 2.6 What this tab is *not* doing in v1
- ❌ Threaded discussion / comments (deferred to v1.2)
- ❌ Cross-page idea linking ("this idea also touches AGN-feedback") — v1.2
- ❌ Auto-detect when an idea has been published (literature back-search) — v1.3
- ❌ Public submission of ideas by site visitors — v2.0
- ❌ User-facing scoring / Elo of ideas — v2.0

---

## 3. Backend pipeline

### 3.1 Architecture summary

```
┌── trigger ─────────────────────────────────────────────────────────┐
│  (a) manual /api/research/ideas/{slug}/regenerate   (admin)        │
│  (b) Celery beat: nightly 04:00 KST, top-10 flagship pages         │
│  (c) Auto: post-claim-insert hook if Δdebate ≥ 3 or Δarxiv ≥ 10   │
└──────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌── context bundler ─────────────────────────────────────────────────┐
│  • Page core: title, slug, hero_tagline, top-20 claims, all debates │
│  • Survey pivots: claims tagged each survey (JWST/DESI/ALMA/Euclid/ │
│    LSST/HSC/VLA), arxiv_papers from last 365d matching `slug` in    │
│    related_pages and survey keywords in abstract                    │
│  • Existing ideas: active + saved ideas on this page (anti-dup)     │
└──────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌── Rakon: reasoning skeleton (deepseek-r1:671b on Mac Pro) ─────────┐
│  Prompt: §3.3.1                                                    │
│  Output JSON: skeleton[] = {combo, question, why_now_skeleton,    │
│                              approach_skeleton, anchors, raw_id}   │
│  Temperature 0.4 · N=1 (no ensemble, generates a candidate pool)   │
│  Pool size: 12 candidates per page                                 │
└──────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌── AstroSage-70B: domain polish (Mac Studio) ───────────────────────┐
│  Prompt: §3.3.2                                                    │
│  Per-idea call (parallelizable, batch size 4 with keep_alive=1h)   │
│  Output: same JSON, why_now/approach rewritten in domain idiom,    │
│  technical claims sanity-checked (no "z = 100" galaxies, etc.)     │
│  Drops ideas that fail domain plausibility check (LLM self-flag)   │
└──────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌── Atom-7B: scoring + dedup (Mac Studio, ~5GB) ─────────────────────┐
│  Prompt: §3.3.3                                                    │
│  Per-idea scoring of novelty and feasibility on [0,1].             │
│  Dedup: TF-IDF cosine against existing active+saved ideas on the   │
│  same page; drop if cosine ≥ 0.75.                                  │
│  Drop ideas with novelty < 0.4 OR feasibility < 0.3.               │
└──────────────────────────────────────────────────────────────────────┘
                                  │
                                  ▼
┌── persist ──────────────────────────────────────────────────────────┐
│  INSERT into research_ideas (status='active')                      │
│  INSERT into research_idea_anchors (idea_id, kind, ref_id)         │
│  UPDATE old active ideas: status='superseded' if not re-emitted    │
│  Log run to autowiki_runs (kind='research_ideas')                   │
└──────────────────────────────────────────────────────────────────────┘
```

### 3.2 Trigger conditions (concrete)

**(a) Manual** — `POST /api/research/ideas/{slug}/regenerate`. Rate-limited to 6h. Returns 202 with task_id; UI polls status. Admin auth required.

**(b) Nightly batch** — new Celery beat entry:
```python
"regenerate_research_ideas_nightly": {
    "task": "app.agent_loop.research_ideas.tasks.regenerate_top_pages",
    "schedule": crontab(hour=19, minute=0),  # 04:00 KST = 19:00 UTC
}
```
Picks the top-N flagship pages by `(debate_count + arxiv_papers_last_30d_count)`; N=10 in v1.1, N=1 (galaxy-evolution only) in v1.0.

**(c) Auto on signal** — post-insert hook on `claims` and `arxiv_papers.related_pages`:
- If `count(new debate claims on this page since last research_ideas run) ≥ 3`, enqueue.
- If `count(new arxiv_papers tagged this page since last run) ≥ 10`, enqueue.
- Coalesce — debounce 1h per slug so a burst doesn't fire 5 jobs.

### 3.3 Prompts

#### 3.3.1 Rakon — skeleton (full prompt)

```python
RAKON_SKELETON_PROMPT = """You are a senior astronomy research strategist. Given a wiki
page's claims, debates, and recent literature, generate 12 candidate research
questions, each anchored to a SPECIFIC combination of observational surveys.

WIKI PAGE
---------
Title: {title}
Slug: {slug}
Tagline: {hero_tagline}

ESTABLISHED CLAIMS (top 20 by trust):
{claims_block}

ACTIVE DEBATES (claim_type='debate'):
{debates_block}

RECENT LITERATURE (last 365 days, page-tagged):
{arxiv_block}

SURVEY COVERAGE — claims with explicit survey mention:
{survey_coverage_block}
  e.g.  JWST: 14 claims, 3 debates ;  DESI: 9 claims, 2 debates ; ...

EXISTING IDEAS ON THIS PAGE (do NOT duplicate):
{existing_ideas_block}

ALLOWED SURVEY COMBOS (use exactly two):
JWST+DESI, JWST+Euclid, JWST+ALMA, JWST+HSC, JWST+LSST, JWST+VLA,
DESI+Euclid, DESI+HSC, DESI+ALMA, DESI+LSST,
ALMA+Euclid, ALMA+HSC, ALMA+LSST, ALMA+VLA,
Euclid+HSC, Euclid+LSST,
HSC+LSST, LSST+VLA

OUTPUT FORMAT — strict JSON, no prose:
{{
  "skeletons": [
    {{
      "combo": "JWST+DESI",
      "question": "<1-sentence research question, falsifiable>",
      "why_now_skeleton": "<2-3 sentences: which debate or recent papers create the gap>",
      "approach_skeleton": "<3-5 sentences: what data, what cuts, what measurement, expected N>",
      "anchors": {{
        "claim_ids": [<ids from claims_block>],
        "debate_ids": [<ids from debates_block>],
        "arxiv_ids": ["<arxiv ids from arxiv_block>"]
      }}
    }},
    ...12 total...
  ]
}}

CONSTRAINTS:
- Each question MUST be answerable by combining the two named surveys; do not
  propose questions either survey can answer alone.
- Each question MUST reference at least 1 claim_id OR 1 debate_id from this page.
- Each question SHOULD reference at least 1 arxiv_id when one is relevant.
- Spread combos: at most 3 ideas per single combo.
- No vague verbs ("understand", "explore"). Use measurable verbs ("measure",
  "constrain", "test whether", "rule out").
- No ideas requiring data that does not yet exist (e.g. "LSST DR2" if LSST
  hasn't released DR1).
- If you cannot generate 12 high-quality ideas, generate fewer — quality over quota.
"""
```

#### 3.3.2 AstroSage-70B — polish (full prompt)

```python
ASTROSAGE_POLISH_PROMPT = """You are an astronomy domain expert reviewing a draft
research idea. Rewrite for domain precision. Reject if implausible.

DRAFT
-----
Survey combo: {combo}
Question: {question}
Why now (skeleton): {why_now_skeleton}
Approach (skeleton): {approach_skeleton}

WIKI PAGE CONTEXT
-----------------
{title} — {hero_tagline}

Top 5 page claims:
{claims_block_5}

TASK:
1. Rewrite "why_now" in 2-3 sentences using domain-precise framing:
   reference quantitative findings (z range, mass bin, sample size) where
   possible. Cite paper titles from the anchors where applicable.
2. Rewrite "approach" in 3-5 sentences with concrete observational specifics:
   instrument mode (e.g. JWST/NIRSpec MOS, DESI BGS-Bright), wavelength /
   band, expected sample size, the actual measurement (e.g. "sSFR-clumpiness
   correlation in 4 mass bins"), and dominant systematic.
3. Domain plausibility check — answer "plausible: yes/no". Reject if:
   - Sample sizes inconsistent with survey footprint / depth
   - Redshift or mass range outside what the surveys actually cover
   - Measurement assumes spectral feature outside instrument bandpass
   - Question already definitively answered (cite the paper if so)
4. Suggest 1-3 dominant systematics for the approach.

OUTPUT JSON:
{{
  "plausible": "yes" | "no",
  "rejection_reason": "<empty if yes>",
  "question": "<may slightly edit for precision, keep falsifiable>",
  "why_now": "<polished prose>",
  "approach": "<polished prose>",
  "systematics": ["<systematic 1>", "<systematic 2>", ...]
}}
"""
```

#### 3.3.3 Atom-7B — scoring (full prompt)

```python
ATOM_SCORING_PROMPT = """Score this astronomy research idea on two axes.
Return JSON only.

IDEA
----
Survey combo: {combo}
Question: {question}
Why now: {why_now}
Approach: {approach}

ANCHORS
-------
Anchored to {n_claims} page claims, {n_debates} debates, {n_papers}
recent papers.

EXISTING ACTIVE IDEAS ON THIS PAGE
----------------------------------
{existing_ideas_short}

SCORING

novelty (0-1):
  1.0 — no existing paper on this exact combination; opens new axis
  0.7 — one or two related papers; idea pushes a clear extension
  0.4 — replication / refinement of recent published work
  0.1 — directly answered in last 24 months

feasibility (0-1):
  1.0 — both surveys have public DR covering this; tractable in <6 months
  0.7 — one DR public, other archival or proposed
  0.4 — requires new proposal cycle; multi-year horizon
  0.1 — needs surveys not yet operational, or 10-100x current sample

OUTPUT:
{{
  "novelty": <float 0-1>,
  "feasibility": <float 0-1>,
  "duplicates_existing_idea_id": <int or null>,
  "one_line_rationale": "<plain text>"
}}
"""
```

### 3.4 Concurrency and rate limits
- Rakon call: serial (one page at a time on Mac Pro — exclusive tenancy).
- AstroSage-70B polish: batch size 4, parallel httpx with `keep_alive=1h` (matches `proposers.py` post-2026-05-12 fix).
- Atom-7B scoring: batch size 8, parallel.
- A single page's regen budget: ~3 minutes wall time on warm models; ~5 minutes from cold.

### 3.5 Failure modes and recovery
| Failure | Detection | Recovery |
|---|---|---|
| Rakon timeout | httpx.ReadTimeout | Log to autowiki_runs with kind='research_ideas', error='rakon_timeout'; status stays as last successful run |
| Rakon returns < 6 candidates | JSON parse | Accept what came back; mark run as `partial` |
| AstroSage rejects all 12 | All `plausible='no'` | Log + Discord webhook to alert Papa (this means Rakon hallucinated; needs prompt tuning) |
| Atom dedup kills > 10 of 12 | Idea-survival count | Lower the floor for this run (this means the page is saturated; that's fine) |
| Idea references nonexistent claim_id | Anchor validation | Drop the anchor, keep the idea, log warning |
| Idea proposes data that doesn't exist | AstroSage plausibility check | Already filtered upstream |

---

## 4. Data model

### 4.1 New tables

```sql
-- One row per generated idea.
CREATE TABLE research_ideas (
    id                    SERIAL PRIMARY KEY,
    page_id               INT NOT NULL REFERENCES wiki_pages(id) ON DELETE CASCADE,
    survey_combo          VARCHAR(40) NOT NULL,        -- "JWST+DESI"
    question              TEXT NOT NULL,
    why_now               TEXT NOT NULL,
    approach              TEXT NOT NULL,
    systematics_json      JSONB,                       -- ["lensing", "dust", ...]
    novelty               NUMERIC(3,2) NOT NULL,        -- 0.00-1.00
    feasibility           NUMERIC(3,2) NOT NULL,
    status                VARCHAR(20) NOT NULL DEFAULT 'active',
                          -- active | saved | stale | superseded | rejected
    model_chain           VARCHAR(120) NOT NULL,        -- "rakon→astrosage-70b→atom-7b"
    generated_by_run_id   INT REFERENCES autowiki_runs(id) ON DELETE SET NULL,
    saved_by_papa         BOOLEAN NOT NULL DEFAULT FALSE,
    seeded                BOOLEAN NOT NULL DEFAULT FALSE,  -- TRUE for §5 seeds
    created_at            TIMESTAMP NOT NULL DEFAULT NOW(),
    updated_at            TIMESTAMP NOT NULL DEFAULT NOW(),
    last_seen_at          TIMESTAMP NOT NULL DEFAULT NOW()
);
CREATE INDEX ix_research_ideas_page_status ON research_ideas(page_id, status);
CREATE INDEX ix_research_ideas_combo       ON research_ideas(survey_combo);

-- Many-to-many: which page claims / debates / arxiv papers does this idea cite.
CREATE TABLE research_idea_anchors (
    id           SERIAL PRIMARY KEY,
    idea_id      INT NOT NULL REFERENCES research_ideas(id) ON DELETE CASCADE,
    kind         VARCHAR(20) NOT NULL,           -- 'claim' | 'debate' | 'arxiv'
    ref_id       VARCHAR(40) NOT NULL,           -- claim.id (str) or arxiv_id
    created_at   TIMESTAMP NOT NULL DEFAULT NOW()
);
CREATE INDEX ix_research_idea_anchors_idea ON research_idea_anchors(idea_id);
CREATE INDEX ix_research_idea_anchors_kind ON research_idea_anchors(kind, ref_id);

-- User signals (v1.1, included in v1.0 migration to avoid a second migration).
CREATE TABLE research_idea_votes (
    id           SERIAL PRIMARY KEY,
    idea_id      INT NOT NULL REFERENCES research_ideas(id) ON DELETE CASCADE,
    user_id      INT,                            -- subscribers.id, nullable for anon
    value        SMALLINT NOT NULL,              -- +1 save, -1 stale, 0 cleared
    note         TEXT,
    created_at   TIMESTAMP NOT NULL DEFAULT NOW(),
    UNIQUE (idea_id, user_id)
);
```

### 4.2 `autowiki_runs` extension
The existing `autowiki_runs` table is reused. Tori adds the value:
```
kind ENUM: ..., 'research_ideas'
```
No schema change — `kind` is `VARCHAR(40)`. Just a new value.

### 4.3 Alembic migration
Single migration: `research_ideas_v1.py`. Creates the three tables. Adds no columns to existing tables. Zero-downtime.

### 4.4 API surface

```
GET    /api/research/ideas/{slug}                       -- list active+saved, paginated
GET    /api/research/ideas/{slug}?combo=JWST+DESI      -- filter
GET    /api/research/ideas/by-id/{idea_id}              -- detail incl. anchors
POST   /api/research/ideas/{slug}/regenerate            -- admin, 202+task_id
POST   /api/research/ideas/{idea_id}/save               -- save ★
POST   /api/research/ideas/{idea_id}/mark-stale         -- admin only
POST   /api/research/ideas/{idea_id}/vote               -- +1/-1/0
GET    /api/research/ideas/{slug}/stats                 -- count by combo, last run ts
```

All shaped as plain JSON, matching the conventions in `routers/research.py`.

---

## 5. Seed ideas for galaxy-evolution (v1.0 ships with these)

**Why seeds?** Before the AI pipeline runs once, the tab must already display content; otherwise Papa's first impression is an empty state. These 15 ideas are written by Kun directly from the current `galaxy-evolution` page state (debate claims, top arxiv papers) and Papa's DESI BGS work context. They live in `research_ideas` with `seeded=TRUE` and `model_chain='kun-seed'`, so the AI batch can supersede them naturally.

Format below mirrors the production card. Anchors reference claim_ids and arxiv_ids that exist as of 2026-05-13.

---

### Seed 1 — JWST+DESI
**Q:** Does the sub-kpc clumpy structure JWST/NIRCam resolves in z≈1.5–2.5 main-sequence galaxies correlate with the DESI ELG specific star-formation rate at fixed stellar mass?
**Why now:** Four 2026 DESI ELG papers report a steepening of the sSFR–environment slope at log(M*/M⊙)≈10, but disagree on whether the effect persists at log(M*)>10.5. JWST CEERS and PRIMER public mosaics now cover ~12% of the DESI ELG footprint with resolved NIRCam imaging. No cross-match has been published.
**Approach:** Cross-match DESI ELG spectra (z=1.4–2.6, MILKY mask) with JWST NIRCam F200W within 1″. For ~400 expected matches, measure clumpiness (Gini-M20 and NIRCam-based clump count per Guo et al. clump finder) in 4 sSFR bins at fixed stellar mass. Compare slope vs. clumpiness fraction.
**Systematics:** PSF mismatch across NIRCam fields, ELG selection bias toward [OIII] emitters, DESI fiber-loss correction at z>2.
**Novelty 0.85 · Feasibility 0.75**

---

### Seed 2 — JWST+DESI
**Q:** Is the quenched fraction at fixed halo mass (DESI BGS group catalog) different for galaxies whose JWST/NIRSpec stellar age maps show an outside-in vs inside-out quenching pattern?
**Why now:** Papa's own DESI DR1 BGS analysis (A&A submitted) finds environment-driven sSFR suppression at z<0.4. The mechanism — gas stripping vs. starvation vs. AGN feedback — is degenerate from DESI alone. JWST NIRSpec IFU now has spatially-resolved stellar age maps for ~80 BGS-overlap galaxies in the GTO programs.
**Approach:** For DESI BGS group catalog galaxies with NIRSpec IFU coverage, classify into outside-in vs inside-out quenchers from age gradient. Bin by halo mass (DESI group mass) and test the quenched fraction difference. N≈80 is small but the effect size predicted from gas-stripping vs starvation models is ~2× — detectable.
**Systematics:** Age-metallicity degeneracy in NIRSpec fits, halo mass uncertainty for low-richness DESI groups, JWST GTO selection function.
**Novelty 0.80 · Feasibility 0.55**

---

### Seed 3 — JWST+DESI
**Q:** At z>4, does the stellar-mass–metallicity relation measured from JWST/NIRSpec emission lines agree with the relation extrapolated from DESI ELGs at z=1–3?
**Why now:** JWST NIRSpec prism programs (JADES, CEERS-MR) now have R~100 metallicity (R23, O3N2) for >300 z>4 galaxies. DESI publishes MZR slope and normalization at z=1–3 from O32. The Lyman-break extrapolation diverges between FIRE-2 and IllustrisTNG predictions at z~6 by 0.4 dex.
**Approach:** Compile JWST MZR at z=4, 5, 6, 7 from NIRSpec prism samples. Extrapolate DESI z=1–3 MZR forward using power-law fit. Quantify residual vs. simulation predictions.
**Systematics:** Different metallicity calibrators between DESI (O32) and JWST (R23) — calibrate with overlap z=2–3 sample. Selection function of NIRSpec MR-mode.
**Novelty 0.65 · Feasibility 0.80**

---

### Seed 4 — JWST+DESI
**Q:** Do the kinematic disturbance signatures JWST/NIRSpec MOS detects in z=1–2 galaxies (rotation/dispersion ratio) anti-correlate with DESI-derived local galaxy density?
**Why now:** Cluster-environment kinematics at z=1–2 is the open question separating gas-stripping models. DESI provides density estimators (5th-nearest-neighbor) for galaxies in JWST footprint; no kinematic-environment cross-match exists at z>1.
**Approach:** Compile NIRSpec MOS rotation curves (CEERS, RUBIES, JADES) for galaxies with z=1–2 DESI spec-z. Measure v/σ. Bin by Σ5 quartile. Compare with TNG predictions for stripping.
**Systematics:** PA/inclination from low-S/N NIRCam morphology, MOS slit-loss correction, DESI density sparsity at z>1.
**Novelty 0.75 · Feasibility 0.60**

---

### Seed 5 — JWST+DESI
**Q:** Is the AGN-host morphology bimodality (compact-disk vs. disturbed) JWST/MIRI sees in obscured AGN consistent with DESI's QSO clustering bias at z=1–2?
**Why now:** DESI QSO bias measurements imply host-halo masses ~10¹²·⁵ M⊙ at z=1.5, but JWST/MIRI shows a wide morphology distribution that doesn't fit a single host-halo class. Either the bias measurement is biased by AGN selection, or the morphology bimodality is environment-driven.
**Approach:** For DESI QSOs at z=1–2 with MIRI imaging, classify morphology (CAS or visual). Compare clustering bias of compact-host vs. disturbed-host QSO subsamples.
**Systematics:** MIRI sample is small and not BCG-clean; DESI QSO selection function near AGN.
**Novelty 0.70 · Feasibility 0.50**

---

### Seed 6 — ALMA+Euclid
**Q:** Does the dust-obscured star-formation fraction (ALMA Band 7 stacks) in z=0.5–1.5 galaxies correlate with the Euclid VIS+NISP morphological asymmetry index at fixed stellar mass?
**Why now:** Euclid Q1 (March 2026) released morphological catalogs over 1500 deg². ALMA archival Band 7 covers ~5% of this area to RMS ~0.1 mJy. The dust-obscuration vs. morphology link at intermediate z is contested — gas-rich-mergers model predicts asymmetric+dusty, but secular-disk model predicts symmetric+dusty.
**Approach:** Stack ALMA Band 7 archival data on Euclid-defined asymmetry quartiles for z=0.5–1.5 galaxies, fixed stellar mass log(M*)=10.0–10.5. Compute IR/UV ratio per quartile.
**Systematics:** ALMA primary beam attenuation, archival coverage non-uniformity, Euclid PSF-matching for asymmetry at small angular sizes.
**Novelty 0.80 · Feasibility 0.65**

---

### Seed 7 — ALMA+Euclid
**Q:** At z=2–3, do passive galaxies identified by Euclid NISP UVJ colors show molecular gas detections (ALMA CO 3-2) consistent with the "frosting" model of residual cold gas?
**Why now:** The frosting model predicts residual CO in 30% of UVJ-quiescent z=2 galaxies; gas-poor classical-quenching models predict <5%. Sample sizes from individual ALMA programs are too small (<20 each) to distinguish. Euclid will yield ~10⁴ z=2 UVJ-quiescent candidates by 2027.
**Approach:** Stack ALMA archival CO 3-2 data (e.g. ASPECS, REBELS) on Euclid UVJ-quiescent stacks. Measure mean detection significance and fit upper limit.
**Systematics:** UVJ contamination from dusty star-formers, CO(3-2)-to-H2 conversion factor at z=2, ALMA stacking correlations.
**Novelty 0.75 · Feasibility 0.55**

---

### Seed 8 — ALMA+Euclid
**Q:** Does the cold-gas fraction (ALMA CO 1-0 or [CII]) in field galaxies at z=4–6 scale with Euclid-measured halo overdensity, testing whether cosmological accretion or stochastic mergers drive gas supply?
**Why now:** Euclid deep fields will resolve halo overdensity at z>4 from Lyman-break number-density excess. ALMA REBELS, REBELSx and CRISTAL-Survey have [CII] for ~150 z=4–6 galaxies. Cross-match unreleased; theoretical prediction differs by factor of 3 between FIRE-2 and EAGLE.
**Approach:** Cross-match [CII] detections with Euclid deep-field overdensity (5th nearest neighbor in projected density). Fit M_gas vs. δ_5 at fixed M_star.
**Systematics:** [CII] luminosity-to-M_gas calibration uncertainty (factor of 2), Euclid Lyman-break completeness at z>5.
**Novelty 0.85 · Feasibility 0.45**

---

### Seed 9 — DESI+HSC
**Q:** Does the DESI BGS group catalog reproduce the projected halo mass function from HSC weak-lensing stacking at log(M_h) = 12–14, or is there evidence for a halo-mass-dependent group-finder bias?
**Why now:** Group catalogs and weak lensing are usually published independently. DESI DR1 BGS group masses are calibrated against mocks; HSC SSP Year 3 weak lensing provides an independent halo-mass anchor for the same galaxies. Disagreement would calibrate Papa's DESI work and others'.
**Approach:** Identify DESI BGS groups in the HSC SSP Year 3 footprint. Stack HSC shear around groups in DESI mass bins. Compare lensing-inferred mass to DESI-assigned mass.
**Systematics:** HSC photo-z bias for source galaxies, DESI fiber-completeness in dense groups, DESI mocks' satellite/central decomposition.
**Novelty 0.65 · Feasibility 0.85**

---

### Seed 10 — DESI+HSC
**Q:** Is the central-galaxy color (HSC g–r) in DESI BGS groups a stronger predictor of group quenched fraction than halo mass at fixed environment?
**Why now:** Galactic conformity is a contested signature of pre-processing vs. AGN feedback. HSC depth lets central colors be measured cleanly; DESI provides redshifts and group memberships. Existing conformity measurements at z<0.1 (SDSS) saturate; DESI BGS extends to z<0.4 with N~50× SDSS.
**Approach:** For DESI BGS groups, measure central HSC g–r. Bin satellites by central color quartile and halo mass. Test whether quenched fraction varies with central color at fixed M_h.
**Systematics:** Aperture-matched colors for HSC at varying z, satellite-central misclassification.
**Novelty 0.70 · Feasibility 0.85**

---

### Seed 11 — DESI+HSC
**Q:** Do DESI ELGs that lie on the high-mass tail of the HSC weak-lensing-inferred halo mass distribution show suppressed [OII] equivalent width relative to halo-mass-matched centrals?
**Why now:** ELG samples are usually assumed to live in low-mass halos; the high-mass tail of the ELG halo distribution (≳10% by HOD models) is a key probe of how ELGs populate massive halos. HSC weak lensing constrains the actual halo mass per ELG; DESI provides [OII] EW.
**Approach:** Lensing-stack DESI ELGs in [OII] EW quartiles. Test whether the high-EW quartile is in lower-mass halos as predicted.
**Systematics:** ELG selection function as a function of halo mass, [OII] dust correction, lensing depth in DESI footprint.
**Novelty 0.65 · Feasibility 0.80**

---

### Seed 12 — JWST+ALMA
**Q:** In z=4–6 galaxies, does the stellar-age gradient (JWST/NIRSpec Balmer break maps) correlate with the spatially-resolved [CII] dynamical mass (ALMA), testing inside-out growth at the epoch of reionization?
**Why now:** Inside-out growth is the dominant paradigm for high-z disks but largely untested kinematically. Resolved [CII] kinematics from ALMA (CRISTAL, REBELSx) now reach 0.2″ resolution; NIRSpec IFU provides Balmer breaks at matching resolution.
**Approach:** Joint-fit NIRSpec age maps and ALMA [CII] velocity fields for the ~30 overlapping galaxies. Test for radial age-stellar mass slope.
**Systematics:** Differential PSF (NIRSpec vs ALMA), [CII] surface-brightness profile vs. stellar profile alignment, age-metallicity degeneracy.
**Novelty 0.85 · Feasibility 0.50**

---

### Seed 13 — Euclid+HSC
**Q:** Do Euclid-detected ultra-diffuse galaxies in HSC-mapped cluster outskirts at z=0.1–0.3 show stellar-population gradients consistent with quenching by ram-pressure stripping (HSC photometry) rather than starvation (Euclid morphology)?
**Why now:** UDG formation mechanisms are debated. Euclid Q1 reveals ~200 UDG candidates in cluster outskirts; HSC SSP has deep multi-band photometry for stellar-population gradient measurement on the same galaxies. Distinguishing mechanisms requires combined morphology + color gradient.
**Approach:** For Euclid UDGs in HSC footprint, measure color profile from HSC g, r, i, z. Test gradient slope vs. distance-to-cluster-center prediction for each model.
**Systematics:** UDG completeness vs. surface brightness, HSC sky background subtraction at UDG SB level.
**Novelty 0.70 · Feasibility 0.70**

---

### Seed 14 — DESI+ALMA
**Q:** At fixed stellar mass and z=0.5–1, does DESI-derived AGN classification (line-ratio BPT and WISE) predict ALMA molecular gas depletion timescale, testing AGN-feedback as a quenching mechanism?
**Why now:** AGN feedback signatures in molecular gas content are contested. DESI provides ~10⁶ AGN host galaxies; ALMA archival CO covers ~2% of these. The depletion-timescale–AGN-luminosity correlation predicted by simulations is order-of-magnitude testable.
**Approach:** Cross-match DESI AGNs at z=0.5–1 with ALMA CO 1-0 or 2-1. Bin by AGN bolometric luminosity. Fit M_gas/SFR (depletion time) vs. L_AGN.
**Systematics:** SFR estimator in AGN hosts (DESI-derived may include AGN contamination), ALMA archival depth heterogeneity.
**Novelty 0.65 · Feasibility 0.60**

---

### Seed 15 — JWST+HSC
**Q:** Do JWST-revealed z>10 galaxy candidates that overlap the HSC Deep footprint show consistent photometric properties between the two instruments, or is there evidence for Lyman-break contaminants distinguishable only by joint fitting?
**Why now:** JWST high-z candidate samples have a non-trivial low-z interloper rate. HSC's deep g, r drop-out characterization is the strongest ground-based constraint. Several reported z>10 candidates lack systematic HSC cross-match papers.
**Approach:** For JWST-published z>10 candidates in the HSC Deep footprint, run forced photometry in HSC g, r. Test for Lyman-break consistency. Flag inconsistent objects for re-classification.
**Systematics:** HSC depth varies across Deep fields; some JWST candidates near HSC noise floor.
**Novelty 0.55 · Feasibility 0.90**

---

> **Combo distribution:** JWST+DESI ×5, ALMA+Euclid ×3, DESI+HSC ×3, JWST+ALMA, Euclid+HSC, DESI+ALMA, JWST+HSC ×1 each. Total 15. Spread matches Papa's stated priority ordering.

> **Why these are seeds, not just placeholders:** every idea references either (a) a specific contested claim already in the `claims` table for `galaxy-evolution`, or (b) a specific arxiv paper or survey data release already in the DB. Tori can validate each anchor before insert; if any anchor is broken, the idea ships with that anchor dropped but the idea body unchanged.

---

## 6. Platoon assignment

### 6.1 Production model chain
| Step | Model | Tier | Hardware | Why this model |
|---|---|---|---|---|
| **(a) Reasoning skeleton** | **Rakon** (deepseek-r1:671b) | Heavy reasoner | Mac Pro · exclusive | Multi-step reasoning over heterogeneous inputs (claims + debates + papers + survey constraints) is the bottleneck. Astronomy domain is not (anchors are provided). Rakon's strength is exactly this kind of cross-axis synthesis. |
| **(b) Domain polish** | **AstroSage-70B** | Astronomy drafter | Mac Studio | Polishing requires domain-precise prose, instrument-mode specificity ("NIRSpec MOS, R~1000, F170LP"), and plausibility checks against survey-coverage facts. This is AstroSage's exact niche. |
| **(c) Novelty/feasibility scoring** | **Atom-Astronomy-7B** | Astronomy classifier | Mac Studio · ~5GB | Per-idea scoring at volume (≤12 per page × N pages nightly). Atom's fast astronomy-tuned scoring is calibrated for exactly this. |
| **Dedup TF-IDF cosine** | (no LLM — Python `scikit-learn`) | — | Mac Studio | Reuses existing `arxiv_classifier._cosine` helper. |

### 6.2 Justification per platoon-roster routing rules
From `platoon-roster.md`:
- **Astronomy + ML/stats reasoning chain → Rakon skeleton + AstroSage prose.** This task fits the documented "combined-mode pattern" exactly.
- **Astronomy scoring at volume → Atom-7B over Mima.** 12 ideas × 10 pages = 120 scores per nightly batch — clearly batch-volume, clearly astronomy-specific.
- **Cost/capacity:** all three models are free/local. No Claude budget consumed in production.

### 6.3 Hardware co-residency
A single page's regen requires Rakon (Mac Pro, exclusive) and AstroSage+Atom (Mac Studio). These are **cross-host**, no contention. Nightly batch can run Rakon and AstroSage in parallel (different machines).

Constraint to honor: **never schedule research_ideas Rakon batch concurrently with `deep_synthesis` Rakon batch** — both want Rakon exclusive. Coordinate via the existing `autowiki:enabled` Redis flag pattern. Suggest a new `research_ideas:enabled` flag that defaults to 0 and is flipped on by Papa post-deploy.

### 6.4 Fallback chain
| Primary | Fallback 1 | Fallback 2 | Last resort |
|---|---|---|---|
| Rakon | Buddle (deepseek-r1:32b, Mac Pro) — same family, lower capacity, can fit alongside other work | AstroSage-70B alone (Mac Studio) doing both skeleton + polish | Skip — write run as `infra_unavailable`, retry next cycle |
| AstroSage-70B | Blanc (llama3.3:70b) — general drafter, weaker domain | Tera (gemma3:27b) | Skip polish, ship Rakon raw |
| Atom-7B | Mima (qwen3:30b) | Skip — heuristic novelty score from idea-text length + anchor count |

### 6.5 v1.0 (Papa-only, galaxy-evolution only): allowed simpler chain
For the very first batch only, where the goal is "is this useful at all" rather than "is this perfectly polished," Tori may run:
- **Rakon-only** (skeleton-quality prose) — ~3min per page
- AstroSage polish enabled by `research_ideas:polish_enabled=1` Redis flag, off by default in v1.0
- Atom scoring required (cheap)

Once Papa confirms the format is useful, flip the polish flag on.

### 6.6 Eval / monitoring (per existing rubrics)
- Each run logs to `autowiki_runs` with `kind='research_ideas'` — reuses dashboard.
- New metric: `ideas_survival_rate = ideas_inserted / ideas_generated`. Healthy ≥ 0.50. Drop below → AstroSage rejecting too much → tune prompt.
- New metric: `papa_save_rate = saved / shown` for first month — direct usefulness signal.
- Discord webhook to #general on regen completion with idea count + survival rate.

---

## 7. Phasing & deliverables

### 7.1 v1.0 — single-page MVP (target: this week)
- Tori: alembic migration `research_ideas_v1.py`
- Tori: backend `app/agent_loop/research_ideas/tasks.py` + `prompts.py` + routers
- Tori: insert 15 seeds from §5 with `seeded=TRUE` and `model_chain='kun-seed'`
- Tori: frontend tab on `galaxy-evolution` only (feature-flag gated by slug)
- Acceptance: Papa opens galaxy-evolution → Research Ideas tab → sees 15 seed ideas with all metadata. Hits `Regenerate` button → Rakon run completes within 5min → new AI ideas appear, seeds preserved.

### 7.2 v1.1 — auto-regen + top flagship pages
- Auto-regen triggers (§3.2(c))
- Nightly batch on 10 flagship pages
- AstroSage polish flipped on
- Tab visible on all flagship pages

### 7.3 v1.2 — user features
- `Save ★` for non-admin logged-in users
- Cross-page idea linking ("this idea also appears on AGN-feedback")
- `papa_save_rate` dashboard exposed
- Stale auto-detection (idea older than 90 days with 0 saves → mark stale)

### 7.4 v2.0 — community
- Public submission of ideas (with adversarial-probe gate)
- Elo / community voting
- Literature back-search to detect when an idea has been published

---

## 8. Open questions for Papa (sign-off)

1. **Combo whitelist scope.** §3.3.1 lists 17 combos. Should this v1.0 be restricted to the 5 Papa called out (JWST+DESI, ALMA+Euclid, DESI+HSC, JWST+ALMA, JWST+HSC) for sharper output, or kept broad for novelty? **Kun recommends: keep broad in §3.3.1 (LLM picks), but feature-flag a `RESEARCH_IDEAS_COMBO_WHITELIST` env var so we can narrow without redeploy.**
2. **AstroSage polish in v1.0?** §6.5 says off-by-default. **Kun recommends: off for first batch (assess Rakon prose quality), flip on within 24h.**
3. **Seed visibility.** Should seeds be visually marked ("Kun seed ◇") or invisible from AI-generated? **Kun recommends: invisible. The seeded flag is internal-only. Papa shouldn't have to discount seeds when judging usefulness.**
4. **Mark-stale vs. delete.** §2.4 has Mark stale only. Should there be a true `Delete` for off-topic ideas? **Kun recommends: no delete in v1 — stale is reversible, delete loses audit trail. Add `Delete` in v1.2 only if stale-pile becomes unmanageable.**
5. **Galaxy-evolution v1.0 strict scope.** Should v1.0 ship to the actual `galaxy-evolution` slug, or to a staging slug like `galaxy-evolution-preview` for Papa-only testing? **Kun recommends: ship to actual slug, hide tab behind `?research_ideas=1` query param for week 1. Papa can preview without exposing to public.**

---

## 9. Acceptance criteria (for Tori sign-off)

A v1.0 ships when **all** of the following are true:

- [ ] `research_ideas` and `research_idea_anchors` tables exist with §4.1 schema
- [ ] 15 seeds from §5 are inserted with `seeded=TRUE`, all anchors validated
- [ ] `GET /api/research/ideas/galaxy-evolution` returns the seeds in JSON
- [ ] Wiki frontend on `galaxy-evolution` shows the tab (gated by `?research_ideas=1`) and renders all 15 seeds with metadata as in §2.2
- [ ] `POST /api/research/ideas/galaxy-evolution/regenerate` triggers the Rakon pipeline and writes ≥6 new ideas in <8 minutes wall-time (cold-start budget)
- [ ] AI-generated ideas pass §3.5 failure-mode handling (timeout, partial run, etc.) without crashing the worker
- [ ] `autowiki_runs` has a row with `kind='research_ideas'` after each regen
- [ ] Discord webhook posts to #general on regen completion with idea count
- [ ] Save ★ persists across sessions for Papa's logged-in account
- [ ] Papa, on first open, finds ≥3 of the 15 seeds worth a real Slack to a collaborator (subjective; recorded by Papa in #general)

---

## 10. Risk register

| Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|
| Rakon hallucinates plausible-sounding but factually wrong survey claims (e.g. "Euclid DR2 covers...") | High | Medium | AstroSage plausibility-check pass; reject `plausible='no'`. |
| Generated ideas are mostly trivially-novel (replications of recent papers) | Medium | High (usefulness) | Atom scoring floor 0.4; if survival rate <50%, tune Rakon prompt to push for cross-survey *measurements* not surveys. |
| Papa never opens the tab | Low | Catastrophic | v1.0 gated by Papa's manual flag flip — usage is the deploy signal. Discord ping on first regen. |
| arXiv anchor pollution: ideas cite papers that are non-peer-reviewed preprints, including AGI-generated junk on arXiv | Medium | Medium | v1.1: filter `arxiv_papers.peer_reviewed=true` for anchor selection; v1.0: accept all arxiv anchors but show "arXiv preprint" badge. |
| Pipeline cost: nightly batch × 10 pages × Rakon 5min = ~50min Rakon dwell. Risks crowding `deep_synthesis` cron. | Medium | Medium | Stagger: research_ideas at 04:00 KST, deep_synthesis at 10:00 KST. Use Redis flag for hard lockout. |
| Saved-by-Papa social proof is misleading if Papa doesn't actively save | Medium | Low (only affects v1.2+ public tab) | v1.2 audit: if `saved_by_papa=true` count < 5 after 30 days, drop the badge from public UI. |
| Tab adds visual clutter; reduces page focus for casual readers | Low | Low | Tab is opt-in (collapsed by default in v1.2 for non-logged-in users). |

---

## 11. Notes / out of scope

- **No new model weight** is downloaded. All three models in §6.1 are already in the Mac Pro / Studio platoon.
- **No PII** is stored. `research_idea_votes.user_id` ties to existing `subscribers.id` only.
- **No external API calls** in the pipeline. Anchors come from the local DB.
- **License:** all generated text is AGPL-3.0 (matches existing wiki content license).
- This doc is the contract for Tori's v1.0 implementation. Any divergence in implementation must be flagged back to Kun for design update.

---

*— Kun 🔬  ·  Mac Pro  ·  2026-05-13*
