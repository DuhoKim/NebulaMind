# Autowiki Surveys v1 — autoresearch loop adapted for the Surveys Directory

**Owner:** Kun 🔬 (design) → Tori (implementation)
**Status:** Papa-approved 2026-05-13 (KST) — Q1/Q2/Q3 locked; surveys-priority flip per Q3
**Date:** 2026-05-13 (KST)
**Filename:** `docs/autowiki_surveys_v1.md`
**References:**
- `docs/autowiki_loop_v1.md` — the wiki-page version of this loop. **Reused vocabulary, mechanics, and rollback substrate; this doc only states the deltas.**
- `docs/surveys_directory_design_v1.md` — schema, fields, and 18-row seed for what we're improving.

---

## 0. The one-paragraph version

The Surveys Directory is **mostly-static metadata about facilities** — wavelength, sky coverage, instruments, current DR, archive URL. It needs a loop because (a) data releases land, (b) URLs rot, (c) hand-seeded prose ages, and (d) `primary_science_goals` for active facilities drifts faster than v1.0 hand-curation can keep up. Same autoresearch shape as wiki: propose a small scoped change, score before/after, commit-if-better, rollback otherwise. The deltas from autowiki_loop_v1 are: **finer-grained edit types (field-level, not section-level)**, **a composite metric tuned for metadata accuracy not synthesis depth**, **a much slower cadence (weekly + event-driven, not 5-min)**, and **the entire loop runs on Mac Studio** so it never contends with the wiki loop on Mac Pro.

---

## 1. The metric — what makes a survey entry "good"

A survey entry is high quality if a **working astronomer planning a proposal or paper** can read the detail page and:

1. **Pick the right survey for their science** — wavelength, redshift range, depth, sky coverage are all present, specific, and accurate.
2. **Cite the data correctly** — `current_data_release` names the version + reference paper + public release date.
3. **Reach the data in one click** — `archive_url` works, points to where queries actually happen.
4. **Find the flagship sub-programs** — CEERS, JADES, BOSS, eBOSS, MaNGA, VLASS named when they exist.

This is **planner utility**, narrower than the wiki's "researcher utility" (which also wants debate framing and frontier signal). For surveys, the win is **completeness + accuracy + verifiability**, not synthesis.

### 1.1 Two-component composite

```
quality = 0.55 * structural_score / 100   # 0..1, deterministic (heavier than wiki)
        + 0.45 * utility_score / 10       # 0..1, LLM-judged
```

**Why structural weighs more than wiki's 0.35:** Survey quality is largely computable — fields are either populated or not, URLs either validate or not, `current_data_release` either contains a date or doesn't. The LLM judge adds value on prose quality (description, science_goals) but most of the metric is mechanical. Inverting wiki's split.

### 1.2 Structural score components

Pure-Python `compute_survey_health()` (lives at `app/services/survey_health.py`):

| Component | Weight | Definition |
|---|---:|---|
| `field_completeness` | 0.25 | Fraction of 18 §2.4 required fields with non-empty values. JSONB arrays count if `len ≥ 1`. |
| `description_richness` | 0.15 | `min(1, len(description) / 600)` × paragraph_count_factor. Floor 0 if `< 150` chars (a one-liner is worse than nothing because it implies "done"). |
| `science_goals_specificity` | 0.15 | Regex-counts: ≥2 distinct science targets (galaxy/exoplanet/dark matter/BAO/etc) AND ≥1 quantitative (wavelength range, mag depth, # objects). Bool → {0, 0.5, 1}. |
| `url_validity` | 0.15 | Score = `(archive_ok + mission_ok) / 2` where `*_ok ∈ {0, 1}` from HEAD probe ≤7 days old. |
| `dr_freshness` | 0.15 | Parse year from `current_data_release`; if absent, 0. If parsed: `score = max(0, 1 − (today − dr_date) / 3yr)`. Retired-status surveys exempt (always 1.0). |
| `instruments_count` | 0.10 | `min(1, len(instruments_json) / 4)`. Cap at 1.0 — eight named instruments isn't 2× better than four. |
| `programs_count` | 0.05 | `min(1, len(flagship_programs_json) / 3)`. Retired exempt. |

Sum to 1.0, multiply by 100. Same shape as wiki's `health_score`, different weights.

### 1.3 Utility score (LLM judge, 0–10)

Five dimensions, weighted, with a noise penalty — analogous to wiki's §11.1 but tuned to planner-utility:

| Dim | Range | What it measures |
|---|---|---|
| `parameter_clarity` | 0..3 | Are wavelength, redshift range, sky coverage stated unambiguously and consistent with the survey's actual facility? Vague ranges, missing units → low. |
| `data_access_clarity` | 0..2 | Can the astronomer get to the archive in one click? `archive_url` named, queryable form not blocked by login wall, current DR cited with version string. |
| `science_specificity` | 0..2 | `primary_science_goals` names specific astrophysics (e.g. "BAO at z<1", "exoplanet atmospheres of sub-Neptunes"), not category-level ("study the universe"). |
| `program_breadth` | 0..2 | `flagship_programs` lists the actually-cited sub-programs an astronomer would recognize from the literature. Empty/wrong → 0. |
| `noise_penalty` | -2..0 | Per-pattern deductions, each -1, cap at -2: (a) marketing voice ("revolutionary", "groundbreaking"); (b) hallucinated DR strings or paper refs; (c) instrument names that don't match the facility's mission documents; (d) date format errors ("DR 2025-ish"). |

```
raw          ∈ [-2, 9]
utility_0_10 = max(0, min(10, (raw + 2) * 10 / 11))
```

Same normalization as wiki to keep `compute_quality()` reusable across both loops.

### 1.4 Commit threshold

Edit-type-conditional, not a single Δq cutoff. The wiki used a uniform `Δq ≥ 0.02`; surveys are too varied for one number to make sense. See §2.2 for the per-type commit rules.

### 1.5 Noise floor for utility

Survey utility is **less noisy than wiki utility** because the rubric items are mostly checkable (parameter clarity, URL working, DR string parseable). N=1 judge call by default is enough for FieldPatch / URLHealth / DRRefresh; N=3 median only for ProseEnrich (where prose-quality stochasticity is real). Calibration §11.3 wiki-flow still applies: stddev across 3 baseline calls must be ≤0.7 before the loop runs unattended.

---

## 2. Experiment unit — what one iteration *is*

### 2.1 Edit types (4, ranked by blast radius)

| # | Type | Touches | Rollback unit | Typical cost |
|---|---|---|---|---|
| 1 | **URLHealth** | replaces one URL field (`archive_url` / `mission_url`) | column write | <5s |
| 2 | **FieldPatch** | patches one structured field: `wavelength_range`, `sky_coverage_deg2`, `redshift_range`, `data_volume`, `operator`, `status`, single new entry in `instruments_json` / `flagship_programs_json` | column write OR JSONB array append | ~15s |
| 3 | **DRRefresh** | updates `current_data_release` to a newer version | column write | ~20s |
| 4 | **ProseEnrich** | rewrites `description` (1–2 paragraphs) or `primary_science_goals` (2–3 sentences) | column write, full snapshot in `survey_revisions` | 60–120s |

**Out of scope for v1:** adding new survey rows (still HwaO/Papa direct per `surveys_directory_design_v1.md` §7), deleting fields, schema migrations.

### 2.2 Per-type commit rules

URLHealth and FieldPatch are **mostly deterministic** — they commit on verification pass, not on Δq judgment. DRRefresh and ProseEnrich are scored.

| Type | Commit rule |
|---|---|
| **URLHealth** | New URL must: (a) return HTTP 200 on HEAD, (b) belong to the survey's `operator` domain (e.g. `nasa.gov`/`stsci.edu` for HST), (c) Atom-7B alignment ≥0.60 against `survey.name + survey.full_name`. If yes → commit. Δq doesn't matter; this is a repair, not an improvement. |
| **FieldPatch** | (a) New value passes type/format validator (regex for `wavelength_range`, numeric for `sky_coverage_deg2`, enum for `status`), (b) supporting URL/citation in the proposer output validates per URLHealth path, (c) Atom-7B alignment ≥0.55 of new value text vs survey context. Commit on pass. No Δq required because patching a null field is unambiguous improvement. **Anti-overwrite guard:** if the existing field is non-empty AND differs from the proposed value, require Δq_struct ≥ +0.01 OR a 2nd corroborating source URL — otherwise treat as "disagreement, escalate to HwaO". |
| **DRRefresh** | Source URL must be in the survey's mission/archive operator domain. Atom-7B alignment ≥0.60. Δq_struct ≥ +0.005 (the freshness bump). If `current_data_release` was non-empty, require the new DR's parsed year > old DR's year. |
| **ProseEnrich** | Δq_utility ≥ +0.5 on the 0–10 scale (sharper than wiki's +0.2 equivalent — we run rarely, each commit should be material). AND no structural-component drop >0.05. AND Atom-7B alignment ≥0.55 between new prose and existing structured fields (catches "the prose says optical but `wavelength_band=xray`"). |

### 2.3 Rollback — new table `survey_revisions`

Surveys don't have the equivalent of `page_versions` today. v1 adds it:

```sql
CREATE TABLE survey_revisions (
    id           SERIAL PRIMARY KEY,
    survey_id    INT NOT NULL REFERENCES surveys(id) ON DELETE CASCADE,
    snapshot     JSONB NOT NULL,            -- full row pre-edit
    edit_type    VARCHAR(20) NOT NULL,      -- 'urlhealth' | 'fieldpatch' | 'drrefresh' | 'proseenrich'
    field_path   VARCHAR(80),               -- e.g. 'description', 'instruments_json[2]', 'archive_url'
    editor_agent VARCHAR(60) NOT NULL,      -- e.g. 'autowiki_surveys:proposer'
    autowiki_run_id INT REFERENCES autowiki_surveys_runs(id) ON DELETE SET NULL,
    created_at   TIMESTAMP NOT NULL DEFAULT NOW()
);
CREATE INDEX ix_survey_revisions_survey ON survey_revisions(survey_id, created_at DESC);
```

Every edit (committed OR rolled-back-as-experiment) writes a `survey_revisions` row before mutating `surveys`. Rollback = restore the row from snapshot. Retention: keep last 50 revisions per survey, archive older to `survey_revisions_archive` quarterly.

### 2.4 Idempotency / no-op guard

Same shape as wiki §2.4: read `surveys.updated_at` before proposing; re-read before committing; mismatch → discard (concurrent edit landed). The `bulk_insert` migration sets `updated_at` to `NOW()` per row; subsequent writes must bump it.

---

## 3. The `program.md` equivalent — per-wavelength-band

Wiki uses per-page programs (`autowiki/programs/<slug>.md`) because each topic has its own subtopic map. Surveys group naturally by **wavelength band** — radio vs optical-spectroscopic vs X-ray surveys have different "what counts as good metadata" bars. Per-band programs are a tighter fit than per-slug.

### 3.1 Layout

```
backend/app/agent_loop/autowiki_surveys/
  programs/
    program.default.md         # generic fallback
    radio.md                   # VLA, SKA-future
    sub_mm.md                  # ALMA
    infrared.md                # JWST, 2MASS, WISE, Spitzer
    optical.md                 # SDSS, DESI, HSC-SSP, Rubin/LSST imaging+spec
    uv.md                      # GALEX (when added)
    xray.md                    # Chandra, XMM, eROSITA
    astrometric.md             # Gaia
    multi.md                   # HST (UV+optical+NIR)
  programs/slugs/
    jwst.md                    # optional per-slug override
    desi.md                    # optional per-slug override
```

Resolution order at proposer time: `slugs/<slug>.md` → `<wavelength_band>.md` → `program.default.md`. First-found wins.

### 3.2 Example — `optical.md` (abridged)

```markdown
# AutoWiki Surveys Program — optical band

## Reader persona
A working observational astronomer (postdoc-level) is selecting a survey
for a science case: galaxy clustering at z<2, weak lensing, or stellar
populations.

## Priorities
1. `wavelength_range` MUST cite μm or nm with both endpoints; SDSS-style
   "ugriz + IR" is acceptable IF the filter set is named.
2. `sky_coverage_deg2` MUST be the **public footprint at the cited DR**,
   not the planned final survey area. Imaging vs spectroscopic coverage
   may differ — state both if so.
3. `current_data_release` MUST contain: DR version + release year + URL
   to the release notes. Example: "DR1 (Mar 2025) — data.desi.lbl.gov".
4. `flagship_programs` MUST list the main sub-programs astronomers cite
   (e.g. BOSS / eBOSS / MaNGA for SDSS, BGS / LRG / ELG / QSO / LyA for
   DESI). Omitting these is a planner-utility loss.
5. Imaging-only surveys: state typical depth (e.g. "i~26 mag at 5σ in
   HSC-SSP Deep"); spectroscopic surveys: state wavelength resolution
   and multiplexing.

## Hard rules
- `redshift_range` is only meaningful for spectroscopic surveys. For
  imaging-only, prefer `null` over a guessed value.
- Never use "approximately" or "around" before a numeric — give the
  number or omit. The judge penalizes hedged numbers.

## Banned moves
- Marketing voice ("the world's most ambitious...", "revolutionary").
- Citing a DR by year only ("the 2024 release") — version string required.
- Listing instruments by generic class only ("optical cameras") instead
  of by name (`Mosaic-3`, `Mayall-DESI`, `Hyper Suprime-Cam`).
```

Per-band programs land as part of v1.0 implementation. Per-slug overrides are optional and only authored when a survey has unusual conventions (e.g. JWST cycles vs traditional DRs).

---

## 4. Loop architecture

### 4.1 Cadence — three triggers, all on Mac Studio

The wiki loop runs every 5 min (288 ticks/day). Surveys change at DR pace (months). v1 has **three triggers**, all converging on the same `autowiki_surveys_tick` Celery task:

| Trigger | Schedule | Edit types eligible |
|---|---|---|
| **DAILY_URL_HEALTH** | Celery beat, 04:00 KST | URLHealth only — sweeps all 18 surveys, runs HEAD probes, only invokes proposer on a survey if a URL fails |
| **WEEKLY_AUDIT** | Celery beat, Sunday 03:00 KST | All types — picks 3 lowest-`quality` surveys, runs one tick each |
| **EVENT_DR_REFRESH** | Triggered by news-curator (Mima, KST 01:00) when a DR-class headline matches a known survey slug | DRRefresh only |

**Total scheduled load:** ~21 ticks/week on average (7 daily-health + 3 weekly-audit + ~1 event/week). Two orders of magnitude lighter than wiki — no Celery contention, no warm-model burden.

### 4.2 Tick algorithm

```
1. Resolve trigger context: (survey_id, edit_type_hint, source_url?)
   - DAILY_URL_HEALTH → survey_id from failed-probe list, edit_type='urlhealth'
   - WEEKLY_AUDIT     → survey_id from lowest-quality queue, edit_type=None
   - EVENT_DR_REFRESH → survey_id from news-curator FK, edit_type='drrefresh',
                        source_url from news item

2. Compute Q0:
   - H0_struct = compute_survey_health(survey)  (pure Python, <500ms)
   - U0 from cache keyed on (survey_id, content_hash). Cache miss for
     ProseEnrich/DRRefresh ticks → 1 judge call (Atom-7B for non-prose,
     AstroSage-70B for prose). For URLHealth/FieldPatch, U0 is not
     computed (commit rule is verification-based).

3. Pick edit_type if not hinted (WEEKLY_AUDIT only):
   - urlhealth   if any URL failed in last DAILY_URL_HEALTH for this survey
   - elif drrefresh   if dr_freshness < 0.5
   - elif fieldpatch  if field_completeness < 0.85
   - elif proseenrich if description_richness < 0.7 OR science_goals_specificity < 0.7
   - else: skip tick (logged decision='skip:saturated')

4. Pick proposer (see §5).

5. Run proposer. Time budget: 90s for ProseEnrich, 30s for others.

6. Atom-7B alignment gate:
   - For FieldPatch / DRRefresh / URLHealth: alignment(new_value_text,
     {survey.name, survey.full_name, survey.wavelength_band}) ≥ thresholds
     per §2.2.
   - For ProseEnrich: alignment(new_prose, {existing structured fields
     concatenated}) ≥ 0.55.

7. Source-URL verification (FieldPatch / DRRefresh / URLHealth only):
   - HEAD probe on source URL → must return 200.
   - Domain must be in survey's operator allow-list (built per survey
     in seed data; see §7).

8. Apply candidate as a *pending* transaction (write survey_revisions
   row with snapshot, mutate surveys row).

9. Recompute H1_struct. Hard guard:
   - If any structural component dropped by >0.05 → ROLLBACK.

10. (ProseEnrich only) Judge call:
    - AstroSage-70B with the per-band program prompt + new prose.
    - N=3 calls, median U1. Same content-hash cache key shape as wiki.

11. Commit decision per §2.2 per-type rules.

12. Write autowiki_surveys_runs row (schema §4.3).
```

### 4.3 Persistence — `autowiki_surveys_runs`

```sql
CREATE TABLE autowiki_surveys_runs (
    id              SERIAL PRIMARY KEY,
    survey_id       INT NOT NULL REFERENCES surveys(id) ON DELETE CASCADE,
    started_at      TIMESTAMP NOT NULL DEFAULT NOW(),
    finished_at     TIMESTAMP,
    trigger         VARCHAR(20) NOT NULL,   -- 'daily_url' | 'weekly_audit' | 'event_dr'
    edit_type       VARCHAR(20) NOT NULL,
    field_path      VARCHAR(80),

    model_proposer  VARCHAR(40) NOT NULL,
    model_judge     VARCHAR(40),            -- nullable: not all ticks judge

    h0_struct       NUMERIC(5,2),
    h1_struct       NUMERIC(5,2),
    components_before JSONB,
    components_after  JSONB,

    u0_median       NUMERIC(4,2),           -- nullable
    u1_median       NUMERIC(4,2),           -- nullable
    u0_runs         JSONB,                  -- nullable: 3 raw scores for prose ticks
    u1_runs         JSONB,
    judge_rationale TEXT,                   -- nullable
    judge_prompt_version VARCHAR(20),       -- e.g. 'surveys_judge_v1'

    q0              NUMERIC(4,3),
    q1              NUMERIC(4,3),
    delta_q         NUMERIC(4,3),

    source_url      TEXT,                   -- the URL the proposer cited (if any)
    url_probe_status SMALLINT,              -- HEAP HTTP status

    decision        VARCHAR(20) NOT NULL,   -- 'commit'|'rollback'|'skip'|'gate_reject'|'guard_reject'|'error'
    reject_reason   TEXT,
    revision_id     INT REFERENCES survey_revisions(id) ON DELETE SET NULL,

    latency_ms_breakdown JSONB,
    error_text      TEXT
);
CREATE INDEX ix_aws_runs_survey_started ON autowiki_surveys_runs(survey_id, started_at DESC);
CREATE INDEX ix_aws_runs_decision       ON autowiki_surveys_runs(decision);
```

Volume estimate: ~21 ticks/week × 52 = ~1,100 rows/year. Keep raw indefinitely (it's a fraction of the wiki `autowiki_runs` table).

### 4.4 Concurrency & cross-loop coordination

- **Per-survey lock:** Redis advisory `autowiki:surveys:survey:<id>` — one tick per survey at a time.
- **Cross-host:** Surveys loop runs exclusively on Mac Studio; wiki autowiki uses Rakon on Mac Pro. Cross-host parallelism is free.
- **Co-residency rule:** ProseEnrich uses **Blanc** (proposer) then **AstroSage-70B** (judge). Per roster these two 70B-class are **never simultaneous** on Studio. Tick serializes them: draft → unload Blanc → load AstroSage → judge. Add ~45s for the model swap; absorbed by the slow cadence.
- **Wiki contention (establishing-stage priority — surveys win):** AstroSage-70B is the wiki drafter on Studio. During the establishing stage, the surveys ProseEnrich tick acquires the Redis `astrosage:in_use` lock with priority. Wiki autowiki must acquire the same lock to draft; if held by surveys, **wiki waits up to 5 min, then skips the tick** (next wiki tick fires 5 min later anyway). Rationale: Surveys Directory completeness/accuracy is higher-leverage right now — flagship wiki pages depend on a trustworthy survey index to link into. Cost: ~3 wiki skips/week against ~3 ProseEnrich events/week, out of 2016 wiki ticks/week — negligible. Revisit at steady state (~v1.6).

### 4.5 Kill switch

`autowiki:surveys:enabled` Redis flag (default `false`). Separate from `autowiki:enabled` (wiki) so Papa can flip them independently.

---

## 5. Platoon Assignment

Per `feedback_platoon_assignment.md`: every step names the owner with capability + cost + speed justification. Roster snapshot 2026-05-13 (from `~/.openclaw/workspace/memory/platoon-roster.md`).

| Step | Model | Host | Why this member |
|---|---|---|---|
| 5.1 Trigger orchestration (cadence, queue, locks) | **Pure Python / Celery beat** | n/a | Deterministic scheduling — no model judgment. Cost: 0. |
| 5.2 URLHealth proposer (fetch alternative archive/mission URL) | **Mima** (`qwen3:30b`, Mac Studio, ~18GB) | Studio | Per roster: "news/calendar event triage" + non-astronomy classification is Mima's lane. Survey URL-hunting is pattern-recognition over operator pages, not astronomy synthesis. Atom-7B is too small for the multi-page web reasoning this requires; AstroSage-70B is overkill for "find the current MAST URL". Co-resident with Atom-7B (~5GB) for the alignment gate — ~23GB combined, comfortable. |
| 5.3 FieldPatch proposer (extract structured value from authoritative source) | **Mima** (default) → **Atom-7B** verification | Studio | Mima parses press-release / operator-page text for structured values (`"14,000 deg²"`, `"DR1, March 2025"`). Atom-7B verifies the extracted value against the survey's wavelength_band + name. Per-roster: Mima for non-astronomy extraction; Atom-7B for astronomy-context alignment. Speed: Mima ~15s + Atom ~5s = ~20s total. Both co-resident comfortably. |
| 5.4 DRRefresh proposer (parse DR-class news item, build new `current_data_release` string) | **Mima** | Studio | Already does this in `surveys_directory_design_v1.md` §7 v1.2 hook. We're just plugging it into the autoresearch loop. Cost: free. Speed: ~15s. |
| 5.5 ProseEnrich proposer (rewrite `description` or `primary_science_goals`) | **Blanc** (`llama3.3:70b`, ~42GB) | Studio | Per `surveys_directory_design_v1.md` §7: descriptions are mission/facility framing, not science synthesis. AstroSage-70B's astronomy-tuned head is wasted here (and reserving it for wiki autowiki keeps cross-loop contention manageable). Blanc is the default non-astronomy long-form drafter. Speed: ~60–90s. |
| 5.6 Judge — URLHealth / FieldPatch / DRRefresh | **Atom-7B** + **Python URL validator** | Studio | These edits are factual; the validator (regex on format + HEAD probe + domain allow-list) does most of the gating. Atom-7B adds the astronomy-context alignment score (claim ↔ context). No CoT needed for "does '14,000 deg²' match a known DESI parameter?". Cost: free. Speed: <5s. |
| 5.7 Judge — ProseEnrich | **AstroSage-70B** | Studio | The only case where we need real synthesis judgment ("does this description actually capture what makes this survey distinctive?"). Different weights from Blanc proposer → no author-bias. Per-tick cost: 30s × 3 calls (N=3 median) ≈ 90s. Cold-load 45–60s on the first ProseEnrich tick of the day (Blanc unload, AstroSage load); subsequent ProseEnrich ticks reuse warm. Co-residency: NEVER with Blanc → drafter unloaded before judge loaded (handled by Celery task serialization within the tick). **Cross-loop priority (establishing stage):** surveys ProseEnrich wins the `astrosage:in_use` lock over the wiki drafter — wiki waits 5 min then skips. See §4.4. |
| 5.8 Judge fallback | **Tera** (`gemma3:27b`, ~16GB) | Studio | If AstroSage-70B fails to load (Studio under wiki pressure) for >2 retries, fall back to Tera with the same rubric. Tera lacks Blanc/AstroSage depth but is calibrated for the "is this prose specific or hedged?" question. Logged in `model_judge` so fallback rate is observable. |
| 5.9 Rollback decision logic | **Pure Python** | n/a | Threshold checks per §2.2. Deterministic. |
| 5.10 Periodic audit / per-band program tuning | **Kun (Claude Opus)** — quarterly | cloud | Cross-cutting: are commits actually improving survey usability? Does any band's program.md need rewriting? Same role as wiki §5.9 but quarterly cadence (matches the slower loop). |
| 5.11 News-curator integration (DR-class headline detection) | **Mima** — already runs at KST 01:00 | Studio | Reuses existing news pipeline. Adds a "matches a known survey slug" check; emits `EVENT_DR_REFRESH` to the surveys queue. Per `surveys_directory_design_v1.md` §7 — same assignment, now wired to the autoresearch loop. |

### 5.1 Members explicitly NOT assigned

- **Rakon** — Mac Pro exclusive, reserved for wiki autowiki judge. Surveys judgments don't need 671B reasoning; AstroSage-70B is enough for prose, Atom-7B is enough for facts. Co-running Rakon with the wiki loop on Pro is full saturation; surveys can't piggyback.
- **Buddle** — Mac Pro, evicted whenever Rakon is loaded. Surveys loop is Studio-only by design.
- **AstroSage-70B as proposer** — reserved for wiki drafting where domain depth is the gain; using it for "rewrite the JWST mission paragraph" wastes the wiki keep-warm budget.
- **Takji / Nutty** — too small to judge prose quality; Atom-7B already covers the lighter judging at higher domain calibration.
- **HwaO / Tori / Kun as in-loop models** — cloud cost × 21 ticks/week is fine if any of them was uniquely needed, but no step here requires Claude-level reasoning beyond Kun's quarterly audit.

### 5.2 Hardware co-residency table (per tick)

| Edit type | Studio resident | Studio peak | Pro |
|---|---|---:|---|
| URLHealth | Mima + Atom-7B | ~23GB | (idle for wiki) |
| FieldPatch | Mima + Atom-7B | ~23GB | (idle for wiki) |
| DRRefresh | Mima + Atom-7B | ~23GB | (idle for wiki) |
| ProseEnrich (draft phase) | Blanc + Atom-7B | ~47GB | — |
| ProseEnrich (judge phase) | AstroSage-70B + Atom-7B | ~47GB | — |

All comfortably within Studio's pool, all respecting the roster rule "never AstroSage + Blanc simultaneously."

### 5.3 Roster check

Live roster snapshot (2026-05-13 KST, from `~/.openclaw/workspace/memory/platoon-roster.md`):

| Member | Status | v1 conflict? |
|---|---|---|
| Mima | 🔄 ACTIVE — evidence linking, agent loop | Compatible — surveys ticks are rare (~21/week) and fit between heavier jobs. |
| Atom-7B | 🔄 ACTIVE — always-resident | Compatible — always-on candidate. |
| Blanc | 🔄 ACTIVE — biblio mining | Compatible — surveys ProseEnrich runs ≤3×/week. Roster rule "never with AstroSage" enforced by tick serialization. |
| AstroSage-70B | 🔄 ACTIVE — wiki drafter | **Coordination required (surveys priority during establishing stage)** — wiki autowiki uses AstroSage as drafter; surveys uses it as ProseEnrich judge. Redis lock `astrosage:in_use` handles ordering. **Wiki defers if surveys is mid-tick** (waits 5 min then skips; see §4.4). |
| Rakon | 🔄 ACTIVE — wiki judge on Pro | No surveys conflict — Pro is wiki-only. |

Net: zero new hardware contention v1. Coordinating AstroSage between wiki-drafter and surveys-judge roles requires the Redis lock; cheap to add, robust to expand.

---

## 6. Test plan — DESI pilot

### 6.1 Why DESI

DESI has the most active linked-research-ideas in v1.0 seeds (6 ideas per §6 of surveys directory design), the freshest DR (DR1 March 2025) needing periodic refresh, and a well-known flagship-program list (BGS / LRG / ELG / QSO / LyA) that exercises the `flagship_programs` field path. URLs (`data.desi.lbl.gov`, `desi.lbl.gov`) are stable and operator-owned.

### 6.2 Starting state — eyeball estimate

After v1.0 hand-seed, DESI's structural score should be ~92–95 (all fields populated, fresh DR, valid URLs). Utility score TBD on first calibration call; estimated 7.5–8.5 / 10 given the hand-curation quality.

Composite Q0 estimate: `0.55 × 0.93 + 0.45 × 0.80 = 0.87`. Already high — the pilot tests the loop's behavior near the ceiling, which is the realistic operating regime for v1.0-seeded surveys.

### 6.3 Success criteria

| Window | Target |
|---|---|
| First DAILY_URL_HEALTH sweep | All 18 surveys probed; ≤1 false-positive URL failure; ≤30s wall time. |
| First WEEKLY_AUDIT | One queue-pick → one tick → one commit OR justified skip:saturated. Round-trip ≤5 min. |
| First EVENT_DR_REFRESH (DESI DR2 mock-injection) | News item parsed, DR string updated, archive URL probed, commit landed within 3 min of event arrival. |
| 4-week pilot | All 18 surveys hit at least 2 tick attempts; ≥80% of attempts result in `commit` OR `skip:saturated` (i.e. no flapping rollbacks); judge stddev ≤0.7 on calibration set. |
| Voice check | Manual: descriptions still read as Wikipedia-style factual prose. No marketing voice introduced. |

### 6.4 Pre-loop calibration (§11.3 wiki-flow, adapted)

1. Run AstroSage-70B ProseEnrich judge against current DESI description. Capture rationale.
2. Kun reads rationale; does it identify the right strengths/weaknesses? If yes → proceed.
3. Run judge 3× on unchanged content. Stddev ≤0.7 → pass. Otherwise revise prompt to `surveys_judge_v2`.
4. Lock prompt version in `judge_prompt_version` field.
5. Flip `autowiki:surveys:enabled` to true.

### 6.5 Anti-flap guard

Surveys are static enough that **commit/rollback flapping** (same field oscillating across ticks) is a strong loop-pathology signal. Add a check: if the same `(survey_id, field_path)` has had ≥2 rollbacks in the last 4 weeks, the proposer for that survey-field combo is suppressed for the next 30 days and logged for Kun's quarterly review.

---

## 7. Implementation handoff to Tori

Build in dependency order. Surveys directory v1.0 ships first (per `surveys_directory_design_v1.md`); this loop ships in v1.5 after the directory has live data.

1. **Migration: `autowiki_surveys_v1.py`**
   - `survey_revisions` table (§2.3).
   - `autowiki_surveys_runs` table (§4.3).
   - Add `operator_url_allowlist` JSONB column on `surveys` (default `[]`; seed per-survey in the bulk_insert — JWST: `["nasa.gov", "stsci.edu", "esa.int"]`, DESI: `["lbl.gov", "kpno.noirlab.edu"]`, etc.). Used by the source-URL verifier in §4.2 step 7.

2. **Module: `app/agent_loop/autowiki_surveys/`**
   - `tasks.py` — `autowiki_surveys_tick(survey_id, trigger, edit_type_hint, source_url)` per §4.2.
   - `daily_url_health.py` — Celery beat task, 04:00 KST, runs HEAD probes across all 18 surveys; enqueues URLHealth ticks for any survey with a 4xx/5xx archive or mission URL.
   - `weekly_audit.py` — Celery beat task, Sunday 03:00 KST; computes structural scores, picks 3 lowest-quality, enqueues one tick each.
   - `proposers.py` — `propose_urlhealth`, `propose_fieldpatch`, `propose_drrefresh`, `propose_proseenrich`.
   - `judge.py` — `judge_survey_prose(survey, prose, prompt_version='surveys_judge_v1')`.
   - `programs/` — per-band markdown files (§3).
   - `prompts/surveys_judge_v1.md` — judge rubric prompt (§1.3 rubric in prompt form).

3. **Service: `app/services/survey_health.py`**
   - `compute_survey_health(survey) -> SurveyHealthResult` per §1.2.
   - `compute_quality(survey, utility=None) -> float` per §1.1.
   - Reuse wiki's `health_score.py` patterns; keep the two services parallel but separate.

4. **Beat entries in `worker.py`**
   ```python
   "autowiki-surveys-daily-url-health": {
       "task": "app.agent_loop.autowiki_surveys.daily_url_health.run",
       "schedule": crontab(minute=0, hour=4),
   },
   "autowiki-surveys-weekly-audit": {
       "task": "app.agent_loop.autowiki_surveys.weekly_audit.run",
       "schedule": crontab(minute=0, hour=3, day_of_week=0),  # Sunday 03:00
   },
   ```
   Both behind the `autowiki:surveys:enabled` Redis flag.

5. **News-curator hook**
   - Extend Mima's KST 01:00 task to scan headlines against `surveys.slug` (case-insensitive substring + name + acronym variants).
   - On match + DR-class keyword (`"data release"`, `"DR"`, `"public"`, `"DP"`): enqueue `autowiki_surveys_tick.delay(survey_id, trigger='event_dr', edit_type_hint='drrefresh', source_url=news_item.url)`.

6. **Redis locks**
   - `autowiki:surveys:survey:<id>` — per-survey, single in-flight tick.
   - `astrosage:in_use` — shared with wiki loop. **Establishing-stage priority: surveys ProseEnrich judge acquires with priority over wiki drafter.** Wiki drafter must `acquire(timeout=300s)` and skip the tick on timeout (see §4.4). Surveys side acquires before judging; releases on tick exit. TTL: 5 min, refreshed during use.

7. **Dashboard (v1.5 scope)**
   - Add `/admin/autowiki/surveys` route, mirroring wiki's dashboard spec. Per-survey: current Q, last-tick decision, recent rollbacks, URL probe history.
   - Kill switch toggle for `autowiki:surveys:enabled`.

8. **Disabled-by-default invariant**
   - Migration + module + beat + dashboard merge as one PR with `autowiki:surveys:enabled=false`. Calibration §6.4 gates the flip.

---

## 8. Risks & mitigations

| Risk | Likelihood | Mitigation |
|---|:-:|---|
| **URL false-negative** (archive temporarily down → loop marks healthy URL as broken → "fixes" it to a wrong URL) | Medium | HEAD probe retries 3× over 60s before flagging. Source-URL verifier on replacement URL must be in `operator_url_allowlist`. Same-domain replacement only without HwaO escalation. |
| **DR string hallucination** (proposer invents a DR version) | Medium | Source-URL required for all DRRefresh; URL must be in operator domain; Atom-7B alignment gate ≥0.60. News-curator origin path is even stricter (link already verified upstream). |
| **ProseEnrich author-bias** (Blanc → AstroSage-judge cycle drifts toward shared training distribution) | Low | Different weight families (llama3.3 vs astrosage-fine-tuned), serialized loading (judge never sees draft via shared state). Judge rubric forbids "well-written" as a criterion. |
| **AstroSage contention with wiki loop** | Medium | Redis lock; **wiki defers up to 5 min then skips tick** (establishing-stage priority — surveys win). Wiki tick budget is 2016/week; at ≤3 surveys ProseEnrich events/week wiki loses ≤3 ticks — negligible against the gain of a trustworthy survey index. Revisit priority at steady state (~v1.6). |
| **Survey-revisions table bloat** | Low | Retention policy: keep last 50 per survey, archive older quarterly. ~1,100 rows/year base case. |
| **Anti-overwrite guard fires on legitimate corrections** (e.g. seed had wrong wavelength_range) | Low | Escalation path to HwaO/Papa when guard fires; never silently rejects. |
| **Flapping commit/rollback on same field** | Low | §6.5 anti-flap guard: 2 rollbacks in 4 weeks → 30-day suppression for that (survey, field) pair. |
| **News-curator false match** (e.g. "JWST" mentioned in unrelated press release) | Medium | Match requires survey slug + DR-class keyword; first proposer step also validates URL domain. Two filters before commit. |
| **Loop saturates immediately** (v1.0 seeds are too good) | Medium | Expected. `decision='skip:saturated'` is the right answer. Anti-flap doesn't count skips. Kun's quarterly audit verifies surveys are genuinely good, not loop-blind. |

---

## 9. What we are NOT building in v1

- **Coverage map / Aitoff projection synthesis** — deferred to surveys directory v2.0 per its §9.4.
- **Adding new survey rows via the loop** — admin-only per surveys directory §7; the autoresearch loop only improves existing rows.
- **Cross-survey consistency** ("this new ALMA flagship overlaps with VLA's") — needs a separate cross-entity reasoning pass; out of scope.
- **Per-instrument detail pages** (e.g. `/surveys/jwst/nirspec`) — surveys directory §2.5 explicitly out of scope; loop respects that.
- **Auto-creation of new flagship_programs entries from arXiv mentions** — too noisy; manual addition by HwaO/Papa for v1.
- **Multi-language descriptions** — English only.

---

## 10. Acceptance criteria

v1.5 ships when **all** of the following are true:

- [ ] `survey_revisions` and `autowiki_surveys_runs` tables exist.
- [ ] `operator_url_allowlist` column populated for all 18 surveys.
- [ ] `compute_survey_health()` returns 0..100 and matches manual scoring on 3 hand-checked surveys.
- [ ] Per-band program.md files exist for all bands present in seed data (radio, sub_mm, infrared, optical, uv, xray, astrometric, multi).
- [ ] `autowiki:surveys:enabled` Redis flag exists, defaults to false.
- [ ] DAILY_URL_HEALTH beat probes all 18 surveys in <60s, posts results to `autowiki_surveys_runs` (decision=`skip:url_ok` or `commit` for replacements).
- [ ] WEEKLY_AUDIT beat picks 3 lowest-quality surveys and runs one tick each, all completing within 15 min total.
- [ ] News-curator detects a mock DR headline ("DESI DR2 public release announced") and enqueues an `event_dr` tick.
- [ ] Calibration §6.4 passes (judge stddev ≤0.7) before flag flip.
- [ ] Dashboard at `/admin/autowiki/surveys` renders Q per survey + last-tick rationale + kill switch.
- [ ] Rollback path tested: a deliberately-bad ProseEnrich proposal is rejected by the judge AND `surveys` row matches pre-tick `survey_revisions.snapshot`.

---

## Appendix A — Mapping wiki autowiki → surveys autowiki

| autowiki (wiki) | autowiki_surveys |
|---|---|
| `wiki_pages.content` | `surveys` row (structured fields + description + science_goals) |
| 4 edit types (EvidenceLink / ClaimInsert / HeroFactUpgrade / SectionRewrite) | 4 edit types (URLHealth / FieldPatch / DRRefresh / ProseEnrich) |
| `page_versions` (text snapshots) | `survey_revisions` (full-row JSONB snapshots) |
| 5-min cadence, 288 ticks/day | Daily URL + Weekly audit + event-driven, ~21 ticks/week |
| Proposer: AstroSage-70B (Studio) | Proposer: Mima for facts (Studio) / Blanc for prose (Studio) |
| Judge: Rakon (Pro) | Judge: Atom-7B for facts (Studio) / AstroSage-70B for prose (Studio) |
| Pure prose synthesis judging | Composite verification (URL probe + format regex + LLM rubric) |
| Composite weight: 0.35 struct + 0.65 utility | Composite weight: 0.55 struct + 0.45 utility (more deterministic) |
| `Δq ≥ 0.02` uniform commit | Per-type commit rules; verification-based for URL/Field/DR, Δq_utility ≥ +0.5 for ProseEnrich |
| Cross-loop contention: none (Pro alone) | Cross-loop contention: AstroSage shared with wiki via Redis lock |

---

*— Kun 🔬 · Mac Pro · 2026-05-13*
