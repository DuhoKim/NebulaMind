# NebulaMind Non-Wiki Tabs Audit

**Author:** Kun | **Date:** 2026-06-13 | **Scope:** every route except `/wiki/*`
**Method:** full source reads of `frontend/src/app/` + live curl probes of every API endpoint each page calls (localhost:3000 / localhost:8000 / https://nebulamind.net). Every "broken" claim below cites an observed payload or a file:line. Audited on the production host (Mac Studio).

---

## 0. Route inventory

**Navbar** (`app/components/NavBar.tsx:5-21`): Wiki, Surveys, News, Council, Agents + More ▾ (Chat, Appeals, Contribute, Benchmark, Feedback) + **Join** (highlighted CTA).

**Orphans** (exist in code, zero navbar links): `/explore` (+cards/graph/qa), `/calendar`, `/directory`, `/leaderboard`, `/newsletter`, `/research`, `/autowiki`, `/ideas/[slug]`, `/april-fools`, `/admin/*` (llm, autowiki, audit, proposals), `/contact` (footer only).

---

## 1. Headline findings (ranked by improvement value)

### P0-1 — `/join` registration is dead in production
`join/page.tsx:5`: `API_BASE = process.env.NEXT_PUBLIC_API_URL || "http://localhost:8000"`. No `.env*` exists in `frontend/`, and the compiled prod bundle (`.next/static/chunks/app/join/page-a66a75ac16506ec3.js`) literally contains `localhost:8000`. A visitor on `https://nebulamind.net/join` clicking "Register Agent" fires a browser fetch to `http://localhost:8000/...` → mixed-content blocked / refused. **The site's highlighted CTA silently fails for every external visitor.** The backend endpoint itself works (`agents.py:116`, 422 on bad input verified).
**Fix:** change fetch to relative `/api/agents/register` (next.config.js rewrite already proxies it) + rebuild. 1 line. → Tori brief T1.

### P0-2 — `/admin/*` has no authentication, including mutating endpoints
No `middleware.ts` anywhere in frontend, no `app/admin/layout.tsx`, no auth string in any admin page (grep empty). Backend handlers have no auth `Depends`: `new_page_proposals.py:189` (approve/reject), `autowiki.py:262` (**kill-switch toggle**), `llm_admin.py`. Because `next.config.js` rewrites `/api/:path*` → backend, these mutating endpoints are callable on the public origin. Plain GETs to all four admin pages return 200 (observed).
**Fix:** shared-secret header dependency on the admin/kill-switch/decision routes + a token gate in an `admin/layout.tsx`. Medium-small. → Tori brief T2. **Papa decision D1** on mechanism (shared secret vs IP allowlist vs real login).

### P0-3 — `mcp.nebulamind.net/sse` → HTTP 502 (observed)
Breaks the MCP path on `/join` AND `/contribute`. The two pages also contradict each other (local stdio install with 8 tools at `contribute/page.tsx:116-119` vs remote SSE with 12 tools on `/join`). **Fix:** ops restart of the MCP service + unify the instructions to one source of truth. → Tori brief T3.

### P0-4 — `/api/feedback` publicly returns submitter IP addresses
`feedback.py:38` includes `ip_address` in `FeedbackOut`; observed live payload contains `"ip_address":"14.6.26.178"`. Frontend doesn't render it, but anyone can curl it. PII leak.
**Fix:** drop the field from the response model. 1 line. → Tori brief T1.

### P1-5 — 68 future-dated `arxiv_papers` rows poison three surfaces
DB has 68 rows with `submitted` > today (2026-07-01×41, 08-01×11, 09-01×14, 10-01×2) — past ingest date-parse corruption (e.g. `2604.11271`, an April paper, stored as `submitted='2026-09-01'`). Consequences observed live:
- Homepage `LatestResearch.tsx:17-22` renders "**-80d ago**" (negative `timeAgo`).
- `/research` (`research.py:30` orders by `submitted` desc) leads with corrupt rows, burying genuine 2026-06-11 papers.
- `/newsletter` archive's first "issues" are dated 2026-10-01/09-01/08-01 (`subscribe.py:88-116`).
**Fix:** one-shot SQL cleanup + date-sanity guard in the arXiv ingest task + clamp `timeAgo` at "today". → Tori brief T4.

### P1-6 — `/benchmark` qualification is mathematically impossible
Threshold is 50 votes/30 days, but only **20 tasks exist** and `/tasks` permanently excludes already-answered tasks per agent with no time window (`benchmark.py:110-118`). Max achievable = 20 < 50: **the leaderboard can never populate.** Live: `total_submissions: 0`, `rows: 0`. Methodology page also documents a wrong appeals endpoint (`challenge/{task_id}` vs actual `challenge/{claim_id}`, `council.py:226-240`) and claims "new tasks added continuously" (falsified). → **Papa decision D2**: lower floor to ≤20, or stand up task generation from consensus claims.

### P1-7 — `/explore/chat` ("Chat"): 78s time-to-first-byte, and it stalls the whole API
Observed: first probe timed out at 60s/0 bytes; retry TTFB 78.6s, total 97.7s (local Ollama synthesis). Worse: `chat.py:325-331` uses blocking `urllib.urlopen` inside an async generator — empirically confirmed that one running chat request made `/api/benchmark/tasks` time out (HTTP 000). **One chat user freezes the API for everyone.** Related cross-cutting: intermittent multi-second stalls on all routes during concurrent DB writes (`database.py:7` plain engine, no pool tuning).
Also: `propose-edit` has no auth and attributes to `db.query(Agent).first()` (`chat.py:429`); no conversation memory despite the banner promising it (`chat.py:310` passes empty history); evidence rows with DOIs stored in `arxiv_id` produce 404 arXiv links (`page.tsx:162-163`).
**Fix:** medium backend effort (async httpx / threadpool offload, model choice, client timeout UX). → **Papa decision D3** on priority: invest, or demote Chat in nav until fixed.

### P1-8 — `/news`: featured-flag inflation kills the 3-track layout
86/100 calendar items are `featured: true` → "Featured Today" renders an 86-card wall; the signature Data/Tools/Results tracks get 2/4/7 leftovers. 34 items have `kind: "refereed_paper"` which belongs to no track (`news/page.tsx:46-74`) and vanish under tab filters. Future events render "just now" (`page.tsx:96-104`); 80/100 items have `occurs_at: null` so most cards are dateless.
**Fix:** cap featured to ~5 in UI + add `refereed_paper` to a track + fix the curation cron's featured logic. → Tori brief T5 (frontend half); curation-job half needs a small pipeline patch.

---

## 2. Per-tab findings

### `/` Home
- All 9 widget APIs return 200 with sensible payloads (43 pages, 53 agents, 43-node graph, 10 featured cards).
- **Broken:** negative paper ages (see P1-5); "🔴 Live Activity" pulsing dot over a feed whose newest item is 6 days old (newest comment 2026-05-15) under copy claiming agents "wake up every 5 minutes" (`ActivityFeed.tsx:55-66`); debug `console.log` in prod (`StatsCounter.tsx:46,63`); featured cards render raw markdown (`page.tsx:158` slices `content` starting with `#`); "1 subscribers" social proof; dark hero vs light lower-section theme split.
- **Verdict:** small frontend polish pass (T4 covers dates; T6 covers the rest).

### `/surveys` + `/surveys/[slug]` — strongest tab
- `/api/surveys` → 50 surveys, 22ms. Detail pages already serve the new tables: 50/50 surveys have `data_releases` (88 rows), 41/50 have datasets (56, with catalog fields, DOIs, bibcodes). DESI: 3 releases, 4 datasets, 112 ideas. ReleaseTimeline renders (`SurveyDetailClient.tsx:193-276`). *Overhaul Step 3 in flight — not re-audited here.*
- **Issues:** footer hardcodes "(manual seed by Kun)" (`SurveyDetailClient.tsx:728`) — will be wrong post-loader; idea quality (DESI's top idea proposes measuring "wormhole mouths" — content-pipeline issue, surfaces prominently); 9/50 honest catalog empty-states (expected, in-flight).
- **Verdict:** smallest gap of any tab; footer text rides along with Step 3.

### `/news` — see P1-8. Header claims "Curated daily"; 6 items lack credibility scores.

### `/council` + `/council/history`
- Onboarding flow genuinely works end-to-end (`/api/jury/tasks` returns real claim+evidence tasks; register validates).
- **Broken:** "Active agents: 12+" is fabricated by truncation — `page.tsx:71` slices to 12 then `:121` prints `length + "+"` (actual: 53/48 active). Member grid never shows reputation because the list payload lacks the fields (`page.tsx:205-213` always falls back). `/council/history` is a permanently empty shell: `total_escalations: 0`, all six tier×status queries `[]`, default "resolved" filter shows nothing and the bootstrap notice only renders on "open". 531/560 jury tasks open (95% backlog) undercuts "Evidence tasks completed: 29".
- **Verdict:** small frontend (T7). History page needs **Papa decision D4**: hide until first escalation vs show Stage-1 jury closures.

### `/agents` + `/agents/[id]`
- Profiles rich and live (reputation, 40/40 jury votes for agent 59).
- **Broken:** severe dark/light theme break in `AgentProfileClient.tsx` (Tailwind `bg-white`/`text-gray-900` at `:143,212,268,308` against dark inline blocks at `:169,284`); directory cards show no reputation/specialty/last-active despite API having them; `ROLE_EMOJI` (`page.tsx:15-19`) misses the most common roles (jury×16, writer, drafter → all 🤖); jury-only agents show 0/0/0 stat cards because jury votes aren't counted in that row.
- **Verdict:** small frontend (T7).

### `/escalations` ("Appeals")
- Technically correct, permanently empty (`bootstrap_mode: true`, 0 escalations ever). No explainer of what an escalation is or how to file; E1-E5/S1-S5 legend unused (`page.tsx:20-31`).
- **Verdict:** small frontend explainer panel (T7). Whether escalations *should* have fired is a separate pipeline question.

### `/contribute` — decent static content; MCP contradiction with `/join` (P0-3); "three community votes approve" oversimplifies the actual jury machinery (`page.tsx:21-22`).

### `/benchmark` — see P1-6. Also "Register to compete →" links `/council` instead of `/join` (`page.tsx:84`).

### `/feedback`
- Works; 15 rows live. **Broken:** IP exposure (P0-4); rate limit is a no-op — `@limiter.limit` sits above `@router.post` (`feedback.py:92-93`) and uses a Limiter instance never wired to `app.state.limiter` (`main.py:8,63`) → unlimited anonymous spam; list polluted by "Wiki Vote:"/"April Fools Vote:" rows used as a ballot box; `is_ai` flag unreliable (`feedback.py:95`).
- **Verdict:** small backend (T1).

### `/join` — see P0-1, P0-3. `/contact` — fine (footer-linked, only route with its own `<title>`; rest of site has an SEO title gap).

### Orphans
| Route | State | Verdict |
|---|---|---|
| `/explore` | hard `redirect("/wiki")` (`explore/page.tsx:4`), yet homepage/FeaturedTopics/not-found link to it expecting the tab hub | point links at `/explore/cards` or make it a real index (T6) |
| `/explore/cards·graph·qa` | all healthy (43 cards, 171 questions, QA detail e2e 200); reachable only via Chat's tab bar | leave; note `/api/qa` POST/upvote unauthenticated (open write surface) |
| `/calendar` | healthy and current (307 events; Euclid Q2, JWST Cycle 5, DESI DR2 upcoming); **zero inbound links**, sitemap-only | **add to nav** — flagship of the locked News+Newsletter design (T6) |
| `/directory` | healthy SEO page, 7 categories | leave orphaned (intentional SEO surface) |
| `/leaderboard` | healthy (53 entries); countries/institutions tabs have only 2 rows each | leave (footer-discoverable); optionally hide thin tabs |
| `/newsletter` | works but archive led by future-dated corrupt rows (P1-5); 1 subscriber | fix data, then nav-link per locked design |
| `/research` | works; same data poisoning; `related_pages` empty | fixed by T4 |
| `/autowiki` (public) | **broken** — expects old schema (`tick_at/quality_score/accepted`, `page.tsx:6-18`) vs live payload (`started_at/q0/q1/decision`); all columns render "—", sparkline NaN; stale pipeline description (`:91`). Superseded by `/admin/autowiki` | **remove** (D5) |
| `/ideas/[slug]` | unconditional `notFound()` (`page.tsx:3-5`); zero inbound hrefs | **remove** (D5) |
| `/april-fools` | stale seasonal (June); votes POSTed into feedback table, totals only in component state — never aggregated | **remove/archive** (D5) |
| `/admin/*` | see P0-2; plus `/api/admin/proposals` shows **91 pending proposals** backing up; `/admin/audit` is a viewer over a 1-row table — nothing in backend constructs `AuditEvent` (grep empty) | auth (T2); **D6** wire-or-drop audit log; **D7** triage 91 proposals |

---

## 3. Tori dispatch briefs (straightforward fixes)

Staging: T1 → T2 → T3 → T4 → T5 → T6 → T7. T1/T3/T4 independent; T2 before any public announcement of admin URLs; verify each via curl + browser before next.

**T1 — One-line criticals (frontend rebuild + backend restart):**
1. `join/page.tsx:5` — replace `API_BASE` fetch with relative `/api/agents/register`; rebuild; verify register POST from https://nebulamind.net/join in a browser (watch devtools network tab).
2. `feedback.py:38` — remove `ip_address` from `FeedbackOut`; curl-verify field gone.
3. `feedback.py:92-93` — swap decorator order so `@router.post` wraps the limited fn, and use the `main.py` app-wired limiter instance; verify 429 on 11th rapid request (against a test instance, not prod traffic).
4. `benchmark/page.tsx:84` — "Register to compete →" → `/join`.

**T2 — Admin auth (after D1):** add `app/admin/layout.tsx` token gate + FastAPI dependency requiring `X-Admin-Token` on `new_page_proposals.py:189`, `autowiki.py:262` (kill-switch), `llm_admin.py` mutating routes. Token from env, never committed. Verify: unauthenticated POST to kill-switch → 401; authed → works.

**T3 — MCP path:** restart/redeploy `mcp.nebulamind.net` (502 observed); then make `/contribute` MCP section match `/join` (one canonical instruction set + one tool list).

**T4 — arXiv date corruption:** one-shot SQL fixing the 68 `submitted > CURRENT_DATE` rows (re-derive from arXiv ID YYMM where possible, else set to fetch date); add `submitted <= today` guard in the ingest task; clamp `timeAgo` to "today" floor in `LatestResearch.tsx:17-22` and `news/page.tsx:96-104`. Verify: homepage shows no negative ages; `/research` top item is genuinely recent; newsletter archive starts ≤ today.

**T5 — News layout:** cap Featured Today at 5 (sorted by credibility); add `refereed_paper` to the Results track `kinds` (`news/page.tsx:46-74`); date-less cards show pubdate fallback. Separately patch the curation cron to feature ≤5/day.

**T6 — Nav/orphan hygiene:** add `/calendar` to navbar (or footer at minimum); fix `/explore` inbound links (`app/page.tsx:53,135`, `FeaturedTopics.tsx:124`, `not-found.tsx:32,45`) → `/explore/cards`; remove `console.log` at `StatsCounter.tsx:46,63`; strip markdown in featured-card previews (`page.tsx:158`); soften "Live Activity" copy or compute the dot from actual recency.

**T7 — Council/Agents polish:** real agent count on `/council` (fetch full list length, drop the `+`); enrich member grid + `/agents` directory cards with reputation/specialty (extend list payload or join `/api/leaderboard`); add jury-vote count to profile stat cards; unify `AgentProfileClient.tsx` to dark theme (~15 Tailwind light classes); `/escalations` explainer panel (what/who/how + charter link); `/council/history` per D4.

**Not dispatched (needs design/decision):** chat latency & event-loop blocking (D3), benchmark task economics (D2), DB pool/stall tuning, idea-quality gating, audit-log wiring (D6).

---

## 4. Papa decisions needed

| # | Decision | Default recommendation |
|---|---|---|
| D1 | Admin auth mechanism | Shared-secret header + env token (cheapest credible gate; real login later) |
| D2 | Benchmark: lower 50-vote floor vs generate 30+ tasks | Generate tasks from consensus claims — keeps the bar meaningful |
| D3 | Chat: invest in async/model fix now, or demote from nav | Fix the event-loop blocking regardless (it stalls the whole API); demote nav link until TTFB < 15s |
| D4 | `/council/history`: hide until first escalation vs show Stage-1 closures | Show Stage-1 jury closures — real activity exists (997 votes) |
| D5 | Delete `/autowiki`, `/ideas/[slug]`, `/april-fools` | Yes to all three (broken / 404-stub / stale) — deletions held for explicit approval |
| D6 | Audit log: wire `AuditEvent` emission or drop the viewer | Drop viewer for now; wiring is a real design effort |
| D7 | 91 pending new-page proposals | Separate triage session — likely autowiki-pipeline output piling up |

---

*All findings live-verified 2026-06-13 on the production host. Subagent transcripts available on request (3 audit runs, 137 tool calls).*
