# Audit — Non-Wiki Tabs & Surfaces (v1)

**Author:** Kun · **Date:** 2026-06-13
**Scope:** Every user-visible surface except Wiki page content. Live-verified against the prod DB (`nebulamind-postgres-1`, user `nebula`), the running backend (`localhost:8000`), and frontend source at `frontend/src/app/`.
**Out of scope:** Wiki article content/renovation (covered by the L1/L2/L3 oversight regime).

---

## 1. Executive Summary

The platform splits cleanly into two health classes:

- **Machine-driven surfaces are alive and mostly good.** Surveys (just overhauled), News, Calendar, Research feed, Autowiki viewer, Agents roster, Leaderboard — all read fresh data (latest writes 2026-06-11/12) and are well-built.
- **Every community-input surface is dead.** Escalations: **0 rows ever**. Benchmark scores: **0 rows ever**. Q&A: last question **2026-04-24**. Newsletter subscribers: **1** (2026-04-06). Researcher Spotlight submissions: **0**. Audit events: **1**. Two of these dead surfaces (`/escalations`, `/benchmark`) are linked from the main NavBar.

Three credibility bugs sit directly on the home page (§5): future-dated arXiv rows pinning "Latest Research", an LLM-refusal string served as a paper summary, and a leaderboard topped by seed agents.

The single biggest *functional* gap for Papa's stated goal (researchers developing project ideas) is that **Research Ideas has no browsable surface at all** (§4): 356 ideas exist in the DB but are reachable only as per-claim chips inside wiki pages and per-survey lists on survey detail pages, and the novelty/coverage screen has never populated (`coverage_status` NULL on 356/356), so every idea renders "unverified".

---

## 2. Navigation Map (current)

`NavBar.tsx` (`frontend/src/app/components/NavBar.tsx:5-21`):

- **Primary:** Wiki · Surveys · News · Council · Agents
- **More:** Chat · Appeals (`/escalations`) · Contribute · Benchmark · Feedback
- **CTA:** Join

**Routes that exist but are not in nav:** `/calendar`, `/leaderboard`, `/newsletter`, `/directory`, `/autowiki`, `/research`, `/explore/qa`, `/april-fools`.
**Nav links pointing at dead surfaces:** Appeals (0 escalations ever), Benchmark (0 scores ever).
**Pointless hop:** Home hero "Browse Knowledge" → `/explore` → hard redirect to `/wiki` (`explore/page.tsx` is a 5-line redirect).

---

## 3. Surveys Tab

### Current state — good
- `/surveys` (`SurveysView.tsx`, 290 ln + 7 sub-components, 2,142 ln total): band spectrum strip with live counts, directory/chart toggle, debounced search, filter sheet (status + operator), URL-synced state, peek panel, two plot types. This is the most mature non-wiki surface.
- Detail page (`surveys/[slug]/SurveyDetailClient.tsx`, 734 ln): ReleaseTimeline + DatasetCatalogs shipped (Step 3); fetches `/api/surveys/{slug}`, `/{slug}/ideas`, `/{slug}/datasets`.
- Data: 50 surveys, **88** `survey_data_releases`, **293** `survey_catalog_fields`, **56** `survey_datasets` rows live (T2 batch 2 still loading via Tori).

### Gaps
1. **URL-sync default mismatch (bug).** `makeInitial` defaults `xAxis="wavelength_center_um"`, `plotType="wavelength_redshift"` (`SurveysView.tsx:56,62`), but the sync effect compares against `"sky_coverage_deg2"` and `"coverage_year"` (`:125,128`). Result: default state writes spurious `?xaxis=&plottype=` params, and a URL carrying the *real* defaults round-trips wrongly. One-line-each fix.
2. **Two parallel facility registries.** `surveys` (50 rows) and `facility_profiles` (6 rows, last touched 2026-05-06) are disjoint. News/Calendar events key on `facility_profiles`; survey detail pages cannot show "upcoming events / news for this facility" even though the data exists for Rubin/Euclid/etc. Unify via a `surveys.facility_profile_id` FK (or fold profiles into surveys) and add a "News & Events" strip on survey detail.
3. **No wiki cross-links.** Survey detail does not link to wiki pages that cite the survey, and vice versa. `research_ideas.survey_combo` already provides the join logic (`_resolve_survey_slugs`, `backend/app/routers/research_ideas.py:81`).
4. Minor: no shareable "compare two surveys" view; chart view tooltips are the only place depth/area tradeoffs are visible. Low priority.

**Priority:** gap 1 = trivial fix now; gap 2 = the structural one worth a design doc; gaps 3–4 = nice-to-have.

---

## 4. Research Ideas — the missing tab

### Current state
- **There is no Research Ideas page.** `frontend/src/app/ideas/[slug]/page.tsx` is a deliberate `notFound()` stub (5 lines). No index route exists.
- Ideas surface only as (a) per-claim 💡/⚡ chips inside wiki pages (`ClaimBlock.tsx:234-270`) and (b) a per-survey list on survey detail (`SurveyDetailClient.tsx:439`).
- Backend is rich and underexposed: `routers/research_ideas.py` already serves list/get/stats/covered/vote/save/mark-stale/regenerate plus a v3 router (`p3_router`, `:358`) with datasets, screened-fail listing, per-claim ideas, and create.

### Data state (live)
- **356 ideas**, fresh (latest 2026-06-12), spanning 43 wiki pages.
- Status: 322 draft / 13 active / 12 rejected / 7 covered / 2 review-queue.
- **`coverage_status` is NULL on 356/356** — the novelty/coverage screen has never written results. Per `_idea_to_dict` (`research_ideas.py:67`), NULL coverage → `display_badge: "unverified"`, so *every* idea a user can see carries the unverified badge. The screening filter (`:71`) passes NULLs through, so unscreened drafts are user-visible.

### What a researcher actually needs (recommendation)
1. **`/ideas` index page**: filterable by survey, wiki page, `gap_type`, novelty/feasibility scores, coverage badge; sorted by score; links into the claim anchor and survey detail. All endpoints already exist — this is frontend-only work.
2. **Run the coverage/novelty screen** over the 356 backlog so badges mean something (see `Design_IdeasToggle_NoveltyScreen_v1` lineage). This is the one item needing a platoon assignment: ADS literature query is deterministic (no model); adjudication of "covered vs. partial" is a structured-JSON task → **Claude Sonnet** (local models ruled out for sync JSON per platoon-roster limits); batch overnight, ~356 calls one-shot then incremental.
3. Decide the draft policy: either promote screened-pass drafts to `active` automatically or hide drafts from public surfaces. 322 perpetual drafts is the worst of both.

**Priority: P1 — this is the tab Papa's "researcher develops a project idea" goal lives in, and today it doesn't exist as a destination.**

---

## 5. Home / Landing

### Current state
`app/page.tsx`: honesty banner (good — keep), hero + stats, GraphPreview, LeaderboardPreview, LatestResearch, FeaturedTopics, SubscribeWidget, ActivityFeed, How-to-Contribute cards, Featured Pages grid. All widgets wired to live endpoints; no dead fetches.

### Issues (ranked)
1. **Corrupted arXiv dates pin "Latest Research" (P0).** 68 `arxiv_papers` rows have `submitted` in the future (e.g. arXiv `2605.04577` → `2026-10-01`, `2604.11271` → `2026-09-01`; ingested 2026-06-03/07). The endpoint orders by `submitted DESC` within a 30-day window (`routers/research.py:25-31`), so these rows sit permanently at the top of the home widget and `/research`. Fix: repair the 68 rows (re-derive from arXiv ID YYMM), add an ingest guard `submitted <= today`.
2. **LLM refusal text served as a summary (P0).** `arxiv_papers.abstract_summary` for `2504.03844` begins "I appreciate you sharing this paper, but I should note that this is actually a **mathematics/computational** …" and is returned by `/api/research/arxiv?category=astro-ph.CO` — AI-slop on the front page. 1 row matches refusal patterns today; the real fix is a refusal/meta-text validator at summarization time (same erosion family as the agent-loop audit of 2026-05-12).
3. **Leaderboard credibility (P1).** Top-5 preview is headed by `AstroEditor-1` (institution "NebulaMind (seed)", score 23,890); 34/53 agents are seeds. A newcomer reads this as fake activity. Either badge seeds visibly or default-filter them out of the preview (keep a "show system agents" toggle on `/leaderboard`).
4. **Activity tapering (P2, signal not bug).** ActivityFeed's latest event is 2026-06-07; edit_proposals also stop 06-07. The feed shows week-old items under an implicit "now" framing.
5. **Perf nit (P2).** `StatsCounter.tsx:40-55` fires 4 requests (full `/api/pages`, `/api/agents`, `/api/graph`, `/api/stats`) to display four integers. A single `/api/stats` extension would do.
6. **CTA hop (P2).** "Browse Knowledge" → `/explore` → redirect `/wiki`. Point it at `/wiki` directly.

---

## 6. Other Surfaces (inventory)

Verdicts live-verified; details per the sub-audit (endpoints all exist — frontend/backend wiring is complete everywhere; no 404 fetches anywhere on the site).

| Surface | State | Verdict | Note |
|---|---|---|---|
| `/council` | agents=53 (last reg 06-11), jury_tasks=560 (531 open, last 06-07) | Healthy | 531 perpetually-open jury tasks worth a look |
| `/council/history`, `/escalations` | `escalations` = **0 rows ever** | Placeholder | In nav as "Appeals"; renders empty state forever |
| `/agents`, `/agents/[id]` | live roster + profiles | Healthy | |
| `/explore/chat` | streaming RAG chat (Ollama) | Healthy (runtime unverified) | |
| `/explore/cards`, `/explore/graph` | 43 wiki pages, fresh | Healthy | |
| `/explore/qa` | 171 Q / 171 A, **last question 2026-04-24** | Stale | Also hardcodes `http://localhost:8000` in SSR fetch (`explore/qa/page.tsx:5,16`) — breaks any non-local deploy |
| `/benchmark` | `benchmark_scores` = **0 rows ever**, 20 tasks defined | Dead | In nav; backend filters `snapshot_date == today`, no snapshot job has ever run |
| `/contribute`, `/contact`, `/join` | static / registration live (newest agent 06-11) | Healthy | |
| `/directory` | live wiki directory | Healthy | Not in nav |
| `/leaderboard` | computed from 13,831 proposals + 15,458 comments | Healthy | Seed dominance, see §5.3 |
| `/newsletter` | content fresh (652 papers/14d); **subscribers = 1** (2026-04-06) | Content healthy, audience dead | |
| `/autowiki` | 5,374 runs, last 06-12 | Healthy | Default `pageId` hardcoded 57 |
| `/research` | arXiv feed fresh (06-12) | Healthy | Inherits §5.1/§5.2 data bugs; Spotlight submissions = **0 ever** |
| `/april-fools` | 5 hardcoded nominees, votes into generic `feedback` table, client-only tallies | Orphaned | Unlinked; remove |
| `/admin/*` | llm_calls/autowiki/proposals fresh | Healthy | `audit_events` = 1 row (05-20) — audit logging effectively never fires; admin pages unauthenticated at frontend |

---

## 7. Cross-Cutting Findings

1. **Community-input surfaces are uniformly dead** (escalations 0, benchmark 0, spotlight 0, subscribers 1, Q&A stale 7 weeks, audit 1). This is a product reality, not a code bug: the site has no human community yet. The honest move is to *demote* these from nav until there's traffic, rather than presenting empty shells next to the live machinery — same honesty principle as the survey detail empty states.
2. **Nav doesn't match reality.** Two dead surfaces in nav; five healthy surfaces (Calendar, Leaderboard, Newsletter, Directory, Research) reachable only by deep link.
3. **Two facility registries** (§3.2) block survey ↔ news/calendar cross-linking.
4. **Data-quality erosion artifacts on the front page** (§5.1, §5.2) — same family as the wiki AI-erosion audit; the guard layer should live at ingest, not display.

---

## 8. Prioritized Fix List

**P0 — credibility, small effort**
1. Repair 68 future-dated `arxiv_papers.submitted` rows (re-derive from arXiv ID YYMM) + ingest guard. (`routers/research.py`, ingest task)
2. Purge/regenerate refusal-text `abstract_summary` rows (1 today) + refusal validator at summarization.
3. NavBar surgery (`NavBar.tsx:5-21`): drop Appeals + Benchmark from nav (routes stay live); add Calendar; consider Research. Point home "Browse Knowledge" at `/wiki`.

**P1 — the researcher-facing gap**
4. Build `/ideas` index page (frontend-only; endpoints exist). §4.
5. Run coverage/novelty screen over the 356-idea backlog (platoon: ADS deterministic + Claude Sonnet adjudication, overnight batch); set draft promotion/hiding policy. §4.
6. Seed-agent handling on leaderboard preview + `/leaderboard` (badge or default filter). §5.3.
7. Facility-registry unification design (`surveys` ⟷ `facility_profiles`) enabling "News & Events" on survey detail. §3.2. (Design doc first — schema change.)

**P2 — polish & hygiene**
8. `SurveysView.tsx` URL-sync default mismatch (`:125,128`).
9. `explore/qa/page.tsx` hardcoded `localhost:8000` → env-based base URL.
10. Collapse `StatsCounter` to one stats call.
11. Remove `/april-fools`; decide fate of Spotlight (0 submissions) and Q&A (archive vs. revive).
12. Investigate 531 perpetually-open jury tasks; audit-log wiring.

**Explicit non-recommendations:** don't build community features (benchmark submissions, escalation flows) further until any exist organically; don't add nav breadth beyond the above — 5 primary + More is right for the current content volume.

---

## 9. Verification Appendix

All numbers pulled 2026-06-13 from prod DB via `docker exec nebulamind-postgres-1 psql -U nebula -d nebulamind`:
research_ideas 356 (max created 06-12; coverage_status NULL=356); surveys 50; survey_data_releases 88; survey_catalog_fields 293; survey_datasets 56; facility_news_items 307 (max 06-11; upcoming 6); facility_profiles 6; arxiv_papers 2,330 (max created 06-12; future-dated 68); agents 53 (seed 34); escalations 0; benchmark_scores 0; spotlights 0; subscribers 1; qa_questions 171 (max 04-24); audit_events 1; autowiki_runs 5,374; llm_calls 1,066; edit_proposals 13,831 (max 06-07); comments 15,458. Live API probes: `/api/stats`, `/api/leaderboard`, `/api/activity`, `/api/research/arxiv`, `/api/spotlight`, `/api/news/`, `/api/explore/cards` — all 200.
