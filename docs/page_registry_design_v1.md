# Page Registry Design v1

**Author:** Kun (analyst) · **Date:** 2026-06-11 · **Status:** DESIGN — for Tori to implement after P1 (observability + loop restart) is stable
**Goal:** Remove `PILOT_PAGE_ID = 57` and all per-page beat kwargs. After this refactor, onboarding a new page requires **one DB row + one calibration YAML** — zero code edits.

All file references verified against the live repo on Mac Studio, 2026-06-11. The `wiki_pages` table already holds **43 pages** (ids 1–57, sparse), so this design *extends* existing state rather than inventing a registry from scratch. Page 57 (galaxy-evolution) is the only orchestrated page today.

---

## 1. DB schema

### 1.1 Decision: new 1:1 table, not more columns on `wiki_pages`

`wiki_pages` (`app/models/page.py:10`) is a **content** table — title/slug/content plus a canonicalizer event hook on `content`. It already carries 43 rows of static pages that will never be orchestrated. Mixing orchestration state into it would (a) force every content query to drag orchestration columns, (b) make the canonicalizer hook fire on rows we touch for scheduling reasons, and (c) blur ownership (frontend reads `wiki_pages`; the agent loop should own its own table). So: a sibling table, 1:1 on `page_id`.

### 1.2 `page_orchestration` table

```python
class PageOrchestration(Base):
    __tablename__ = "page_orchestration"

    page_id: Mapped[int] = mapped_column(
        ForeignKey("wiki_pages.id", ondelete="CASCADE"), primary_key=True)
    status: Mapped[str] = mapped_column(String(20), default="dormant", index=True)
        # 'active' | 'paused' | 'onboarding' | 'dormant'
    enabled_lanes: Mapped[dict] = mapped_column(JSONB, default=dict)
        # {"autowiki": true, "deep_synthesis": true, ...} — see §1.3 lane taxonomy
    budget_caps: Mapped[dict] = mapped_column(JSONB, default=dict)
        # {"daily_llm_calls": {"autowiki": 144, "judges": 96}, "daily_usd": 2.0}
    calibration_config_path: Mapped[str | None] = mapped_column(Text, nullable=True)
        # explicit path; loader falls back to convention
        # config/page_retrieval_calibration.<slug>.v2.yaml
    model_assignments: Mapped[dict] = mapped_column(JSONB, default=dict)
        # per-lane seat overrides: {"judges.opus": "claude-opus-4-7"}
        # empty dict = inherit global platoon config (config.py / routing)
    notes: Mapped[str | None] = mapped_column(Text, nullable=True)
    created_at: Mapped[dt.datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[dt.datetime] = mapped_column(
        server_default=func.now(), onupdate=func.now())
```

**Status semantics**

| status | behavior |
|---|---|
| `active` | lanes run per `enabled_lanes` flags |
| `paused` | row exists, nothing runs — per-page operator kill switch |
| `onboarding` | only non-writing lanes run (Layer-2 retrieval dry-run, calibration, scorecard); all write lanes hard-blocked regardless of flags |
| `dormant` | legacy/static page, invisible to the dispatcher (default for the other 42 rows) |

The global Redis kill switch `autowiki:enabled` (`autowiki/tasks.py:81–86`) **stays** — it is the system-wide brake; `status='paused'` is the per-page brake. Both must be green for a write lane to fire.

### 1.3 Lane taxonomy

One flag per beat family. Names are stable identifiers used in `enabled_lanes`, `budget_caps`, `model_assignments`, and the dispatcher's lane→task map.

| lane | covers (current beat entries) |
|---|---|
| `autowiki` | autowiki-tick |
| `deep_synthesis` | rakon-deep-pass-2h |
| `judges` | sonnet-judge-tick, opus-judge-tick |
| `section_rewrite` | sonnet-section-rewrite-q30m, rakon-synthesis-pass-q8h |
| `coherence` | autowiki-coherence-weekly |
| `research_ideas` | buddle-claim-propose-q3h, rakon-draft-async-q4h, debated-claim-seeder-6h |
| `adversarial` | rakon-adversarial-probe-daily |
| `gap_detect` | karpathy-v2-gap-detect-daily |
| `evidence_drain` | drain-evidence-p57 |
| `verbatim_sync` | sync-verbatim-nightly-p57 |
| `arxiv_feed_l2` | Layer-2 element-validated feed (replaces `ARXIV_WIKI_FEED_V2_PAGES`) |

Page-57 seed flags at migration: everything above `true` **except** `coherence` (see §3, the `if page_id == 57` exclusion is policy, and policy belongs in the registry, not in code).

### 1.4 Budget caps

`budget_caps` is enforced by the dispatcher (§2) by counting today's rows in `llm_calls` for `(page_id, lane)`. **Hard dependency on P1:** `llm_calls` is empty today; until Tori's P1 observability lands, the dispatcher must treat caps as advisory (log-only). Ship the check behind a config flag `REGISTRY_ENFORCE_BUDGETS` defaulting to false; flip after P1 verifies `llm_calls` is populated. Schema for the JSONB:

```json
{"daily_llm_calls": {"autowiki": 144, "judges": 96, "research_ideas": 60},
 "daily_usd": 2.50}
```

Missing key = uncapped. `daily_usd` requires cost columns in `llm_calls` (P1 scope decision — if absent, only call-count caps apply).

---

## 2. Beat schedule refactor — dispatcher pattern

### 2.1 Principle

Beat entries become **page-agnostic lane triggers**. Cadence stays in code (celery beat, static, reviewable in git). Page selection moves to the DB. We do **not** adopt dynamic beat backends (RedBeat etc.) — per-page cadence is a non-goal for v1; all active pages share each lane's cadence.

New module `app/agent_loop/registry.py`:

```python
LANE_TASKS = {
    "deep_synthesis": "app.agent_loop.autowiki.deep_synthesis.rakon_deep_pass",
    "judges.sonnet":  "app.agent_loop.autowiki.judge_panel.sonnet_judge_tick",
    # ... full map, one entry per concrete task
}

@celery_app.task(name="app.agent_loop.registry.dispatch_lane")
def dispatch_lane(lane: str, task_key: str, extra_kwargs: dict | None = None):
    pages = active_pages_for(lane)   # SELECT po.page_id, wp.slug FROM page_orchestration po
                                     # JOIN wiki_pages wp ON wp.id = po.page_id
                                     # WHERE po.status = 'active'
                                     #   AND (po.enabled_lanes ->> :lane)::bool
    for i, page in enumerate(pages):
        if budget_exhausted(page.page_id, lane):      # §1.4; log-only until P1
            continue
        celery_app.send_task(
            LANE_TASKS[task_key],
            kwargs={"page_id": page.page_id, **(extra_kwargs or {})},
            countdown=i * STAGGER_SECONDS,            # default 120s — avoids
        )                                             # multi-page thundering herd
```

Slug-parameterized tasks (`generate_research_ideas_v2`) get `{"page_slug": page.slug}` via a per-entry `param` field in `LANE_TASKS` values (`("task.path", "page_id"|"page_slug")`).

Routing is unchanged: `send_task` without explicit queue honors the existing `task_routes` map (`worker.py:274+`), so autowiki-queue isolation is preserved.

`onboarding` pages are excluded by `status='active'` filter; a separate `dispatch_lane(lane, ..., include_onboarding=True)` flag is used only by the non-writing lanes (`arxiv_feed_l2` dry-run, scorecard).

### 2.2 Every current beat entry carrying page-57 literals, and its generalization

All in `app/agent_loop/worker.py` unless noted. ✱ = task also has a `=57`/slug default that must be stripped (§3).

| # | beat entry (line) | today | after |
|---|---|---|---|
| 1 | `autowiki-tick` (:137) | no kwargs; task hardcodes `PILOT_PAGE_ID` internally ✱ | `dispatch_lane("autowiki", "autowiki_tick")`; task takes required `page_id` |
| 2 | `rakon-deep-pass-2h` (:145) | `{"page_id": 57}` | `dispatch_lane("deep_synthesis", ...)` |
| 3 | `sonnet-judge-tick` (:152) | `{"page_id": 57}` ✱ | `dispatch_lane("judges", "judges.sonnet")` |
| 4 | `opus-judge-tick` (:159) | `{"page_id": 57}` ✱ | `dispatch_lane("judges", "judges.opus")` |
| 5 | `buddle-claim-propose-q3h` (:173) | `{"page_id": 57}` | `dispatch_lane("research_ideas", "buddle_claim_propose")` |
| 6 | `rakon-draft-async-q4h` (:186) | `{"page_id": 57}` | `dispatch_lane("research_ideas", "rakon_draft_async")` |
| 7 | `rakon-synthesis-pass-q8h` (:191) | `{"page_id": 57}` | `dispatch_lane("section_rewrite", "rakon_synthesis_pass")` |
| 8 | `rakon-adversarial-probe-daily` (:196) | `{"page_id": 57}` | `dispatch_lane("adversarial", ...)` |
| 9 | `sonnet-section-rewrite-q30m` (:201) | `{"page_id": 57}` ✱ | `dispatch_lane("section_rewrite", "sonnet_section_rewrite")` |
| 10 | `debated-claim-seeder-6h` (:232) | `{"page_id": 57, "target_per_claim": 3}` ✱ | `dispatch_lane("research_ideas", "seed_debated_claim_ideas", extra_kwargs={"target_per_claim": 3})` |
| 11 | `karpathy-v2-gap-detect-daily` (:238) | `{"page_slug": "galaxy-evolution"}` ✱ | `dispatch_lane("gap_detect", ...)` — slug-parameterized |
| 12 | `autowiki-coherence-weekly` (:254) | `{"page_id": 57}` ✱ + in-task skip | `dispatch_lane("coherence", ...)`; page 57 simply has `coherence: false` |
| 13 | `drain-evidence-p57` (:257–260) | `{"page_id": 57}` ✱ | rename `drain-evidence`; `dispatch_lane("evidence_drain", ...)` |
| 14 | `sync-verbatim-nightly-p57` (:263–266) | `{"page_id": 57}` ✱ | rename `sync-verbatim-nightly`; `dispatch_lane("verbatim_sync", ...)` |

Lanes with no page parameter today (`judge_idea_pool`, `buddle_evidence_pair`, `mima_cross_page_synthesis`, `tera_*`, `takji_*`, `nutty_trust_recompute`, news/DOI/surveys) are **out of scope** — they are either genuinely global or already page-agnostic. Do not touch them in this refactor.

The per-page Redis lock already in `autowiki_tick` (`_acquire_lock(page_id)`, `autowiki/tasks.py:859`) is page-scoped — it generalizes for free and protects the migration overlap window (§6).

---

## 3. Code literals to remove

Verified against live files (backups `*.bak*` ignored — Tori should not patch backups).

| file:line | literal | replacement |
|---|---|---|
| `app/agent_loop/autowiki/tasks.py:50` | `PILOT_PAGE_ID = 57` | **delete constant** |
| `autowiki/tasks.py:857` | `page_id = PILOT_PAGE_ID` in `autowiki_tick` | `autowiki_tick(page_id: int)` — required arg from dispatcher |
| `autowiki/tasks.py:1593` | `sonnet_section_rewrite(page_id=PILOT_PAGE_ID, ...)` | required arg, no default |
| `autowiki/tasks.py:1890` | `run_rakon_coherence_pass(page_id=57)` | required arg |
| `autowiki/tasks.py:1902–1904` | `if page_id == 57: skip` exclusion | **delete** — encode as `coherence: false` in page-57 registry row (§1.3) |
| `autowiki/judge_panel.py:221, 230` | `sonnet_judge_tick(page_id=57)`, `opus_judge_tick(page_id=57)` | required args |
| `app/agent_loop/tasks.py:1815` | `drain_evidence_for_page(page_id=57)` | required arg |
| `app/agent_loop/tasks.py:1871` | `sync_verbatim_markers_nightly(page_id=57)` | required arg |
| `research_ideas/auto_improvement.py:1369` | prompt text “…for a **galaxy-evolution** wiki page” | template var: `…for the {page_title} wiki page` — title/slug fetched from `wiki_pages` by `page_id` already in scope |
| `auto_improvement.py:1399` | same embed in coverage-analyst prompt | same templating |
| `auto_improvement.py:3011` | `seed_debated_claim_ideas(page_id=57, ...)` | required arg |
| `auto_improvement.py:3741` | `generate_research_ideas_v2(page_slug="galaxy-evolution")` | required arg (slug-parameterized lane) |
| `app/routers/autowiki.py:20, 67, 143, 197` | `Query(default=57)` × 4 | `Query(...)` **required** — an API default of 57 silently misreports once page #2 exists |
| `app/config.py:100` | `ARXIV_WIKI_FEED_V2_PAGES = "galaxy-evolution"` (consumed in `arxiv_fetch.py:35`) | delete setting; `arxiv_fetch` selects pages via registry: `status IN ('active','onboarding') AND arxiv_feed_l2` |
| `app/services/subtopic_maps.py:380` | `"galaxy-evolution": "galaxy"` in slug→family dict | replace whole dict lookup with `wiki_pages.category` (column exists, populated for all 43 rows — verified in live DB). The hardcoded dict cannot cover future pages; the DB column already does. Keep dict as fallback for one release, log on fallback hit. |
| `app/services/subtopic_maps.py:742` | `"galaxy-evolution": {"extra": {...}}` per-page synonym bands | move into the page's calibration YAML under a `synonym_band:` section (the feed-v2 calibration format already carries per-page query policy — same file, same review path). Loader: YAML section wins; dict fallback for one release. |

**Rule for all defaults:** stripping `=57` (not re-pointing it) is deliberate — a forgotten call site then fails loudly with `TypeError` instead of silently writing to page 57.

---

## 4. Onboarding flow — adding page #N with zero code edits

Precondition (one-time, part of this P2 implementation, not per-page): `scripts/retrieval_filter_v2_production_apply.py` currently pins `LIVE_CONFIG` to the galaxy-evolution YAML (`:33`); it gains a `--slug` argument. The acceptance test for a second page already exists (`tests/test_arxiv_wiki_feed_second_page_acceptance.py`).

Per-page steps, all data/config:

1. **Page row.** If the slug is not among the 43 existing `wiki_pages` rows: `INSERT INTO wiki_pages (title, slug, category, summary, ...)`. `category` is mandatory — it now drives subtopic-family resolution (§3).
2. **Calibration YAML.** Run the feed-v2 calibration harness for the slug; review and commit `config/page_retrieval_calibration.<slug>.v2.yaml` (same format as the existing galaxy-evolution v2 file: semantic band, category policy, score policy, query policy, synonym band).
3. **Registry row.**
   ```sql
   INSERT INTO page_orchestration (page_id, status, enabled_lanes, calibration_config_path)
   VALUES (<id>, 'onboarding',
           '{"arxiv_feed_l2": true}',
           'config/page_retrieval_calibration.<slug>.v2.yaml');
   ```
4. **Observe.** Onboarding status admits only non-writing lanes: Layer-2 retrieval dry-runs and the P1 page-health scorecard accumulate for ~1 week. Review precision/volume.
5. **Activate.**
   ```sql
   UPDATE page_orchestration
   SET status = 'active',
       enabled_lanes = '{"autowiki": true, "judges": true, "evidence_drain": true,
                         "arxiv_feed_l2": true, "research_ideas": true, ...}'
   WHERE page_id = <id>;
   ```
   Next dispatcher firing picks it up — no restart, no deploy.

Ends exactly as briefed: **row in registry + calibration YAML + lane flags.**

---

## 5. Pages #2 and #3 proposal

Both candidates already have `wiki_pages` rows and `subtopic_maps` family entries — onboarding cost is the calibration YAML only.

**Page #2 (adjacent): `active-galactic-nuclei` (id 9).** AGN–environment interplay is inside Papa's DESI BGS research domain (sSFR/morphology/AGN environment dependence), so he can judge output quality directly — the stated criterion. Scientifically adjacent but with a *distinct* core literature (accretion physics, unification, feedback), which exercises the interesting failure mode for a second page: claim-routing at the boundary with galaxy-evolution (feedback/quenching papers legitimately belong to both). I considered `galaxy-formation` (id 17) and rejected it — its boundary with galaxy-evolution is so blurred that misroutes would be unscorable; AGN gives a measurable boundary.

**Page #3 (distant, stress test): `exoplanets` (id 11).** Different arXiv primary category (astro-ph.EP vs astro-ph.GA), different jargon, different object classes, fast-moving observational literature (JWST atmospheres). If the pipeline's "page-agnostic" claim is real, the TF-IDF/embedding retrieval, synonym bands, and claim generation must survive a domain where none of the galaxy-tuned priors help. It is also a featured page with the broadest reader appeal, which serves P3 (audience) for free. Failure here is informative, not embarrassing — that is what a stress test is for.

---

## 6. Migration plan — page 57 into the registry, zero downtime

The loop is currently OFF (`autowiki:enabled` unset, per the 2026-06 strategic evaluation), which makes this migration *easier* — but the plan below does not assume it stays off, since Tori's P1 may restart the loop first. Order with P1: **registry phases A–B can land while P1 runs; phase C (beat flip) must not land in the same restart as P1's loop re-enable** — one variable at a time.

**Phase A — schema + backfill (no behavior change).**
Alembic migration creates `page_orchestration`; data migration inserts:
- page 57: `status='active'`, lanes per §1.3 (coherence false), `calibration_config_path` → existing galaxy-evolution v2 YAML;
- all other 42 pages: `status='dormant'`.
No code reads the table yet. Deploy, verify row counts.

**Phase B — shadow dispatchers.**
Add `registry.py` + `dispatch_lane` with `REGISTRY_SHADOW_MODE=true`: beat gains *parallel* shadow entries that run the registry query, log the page set and would-be task dispatches, and send **nothing**. Run ≥48h; assert shadow logs select exactly `{57}` for every lane that currently fires, and that lane-12 (coherence) selects `{}`. This proves selection equivalence before any traffic moves.

**Phase C — atomic beat flip.**
One commit: replace the 14 old beat entries with dispatcher entries (same cadences, same `:15/:30/:45` offsets), strip task `=57` defaults, restart `celery beat` + workers. Safety properties during the restart window:
- in-flight tasks carry explicit `page_id=57` kwargs from the old schedule — unaffected;
- the page-scoped Redis lock (`autowiki/tasks.py:859`) makes an old-schedule tick and a first new-schedule tick mutually exclusive on page 57;
- judge/idea lanes are idempotent per existing design (scores/proposals, no destructive writes).
Zero-downtime requirement is met because beat restart only affects *future* schedule firings; no migration step touches live request paths or the DB rows the frontend reads.

**Phase D — literal removal + API tightening.**
Delete `PILOT_PAGE_ID`, the §3 fallbacks' deadline starts, routers go to required `page_id`, `ARXIV_WIKI_FEED_V2_PAGES` removed. Grep-gate in CI (P1 brings CI hooks): `git grep -nE 'page_id.*=.*57|"galaxy-evolution"' app/` must return only `subtopic_maps` fallback (until its one-release window closes) and test fixtures.

**Rollback.** Phases A–B: drop nothing, just stop. Phase C: the old beat dict is kept for one release as `BEAT_SCHEDULE_LEGACY`; env var `BEAT_SCHEDULE_MODE=legacy` + beat restart reverts in <1 min. Phase D commits only after C has run clean for a week.

---

## 7. Platoon Assignment

The registry itself adds **no LLM stages** — `dispatch_lane` is pure Python/SQL (sub-second, no model seat needed; assigning a model here would be waste). What changes is *where seat ownership is recorded*: lane→seat moves from implicit task-name convention into `model_assignments` (registry override) falling back to global config. Current owners, unchanged by this design:

| lane | seat (model) | why it stays |
|---|---|---|
| `autowiki` proposer | Vera (AstroSage-70B) | domain-tuned writer, judge-gated; 90s budget unchanged |
| `deep_synthesis`, `adversarial`, `coherence` | Rakon (deepseek-r1:70b → per platoon_overhaul_v2 transition) | long-context reasoning passes, async (r1 JSON defect irrelevant here) |
| `judges` | HwaO seat (claude-sonnet-4-6) + Kun seat (claude-opus-4-7) | independent audit tier; API JSON reliability required |
| `section_rewrite` | Sonnet + Rakon (existing split) | cost/quality split already tuned in beat v3 |
| `research_ideas` | Buddle (gpt-oss:120b) + Rakon | per platoon overhaul §4 canonical roster |
| `gap_detect` | Karpathy-v2 pipeline (Blanc, llama3.3:70b) | reliable structured JSON locally |
| `arxiv_feed_l2` | per arxiv_wiki_feed_design_v1 §platoon | unchanged; registry only selects *which pages* it serves |
| `evidence_drain`, `verbatim_sync` | non-LLM (DB/script lanes) | no seat |

Per-page `model_assignments` overrides exist for the day a page needs a different writer (e.g., exoplanets may warrant a non-astro-galaxy-tuned proposer if Vera underperforms there — measurable via the P1 scorecard before any switch).

---

## 8. Non-goals (v1)

- Per-page cadence (all active pages share lane cadence; revisit only if page count × tick cost forces it).
- Dynamic beat backends (RedBeat/DB-driven schedules) — static schedule + DB page selection gives the needed flexibility with none of the operational risk.
- Admin UI for the registry — SQL is acceptable at current scale; a read-only `/registry` endpoint can ride along with P1 observability if cheap.
- Touching global (non-page) lanes listed at the end of §2.2.

## 9. Open questions for Papa / Tori

1. **Budget enforcement flip date** — gated on P1 `llm_calls` being verifiably populated (§1.4). Tori decides when.
2. **Phase-B shadow duration** — 48h proposed; extend if the loop is still off (shadow logs are only meaningful for lanes that fire).
3. Does Papa want `galaxy-formation` instead of AGN as page #2? §5 argues no, but it's his quality-judgment seat.
