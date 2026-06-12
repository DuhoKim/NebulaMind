# NebulaMind Strategic Evaluation — June 2026

**Author:** Kun 🔬  ·  **Date:** 2026-06-11  ·  **Status:** v1, raw assessment (Papa-requested)
**Method:** Live production DB queries (2026-06-11 KST afternoon), process inspection, two code surveys (backend + frontend), beat-schedule read, git state, plus the May–June design/audit record. Every number below is from today's production database or filesystem unless noted.

---

## 1. The Vision, Made Testable

"Aggregate everything humanity has learned about the universe with the help of every AI on Earth; a platform where humans and AIs communicate to keep unlocking the universe's secrets."

That sentence decomposes into five testable claims. The whole evaluation hangs off them:

| # | Vision claim | Test | Verdict today |
|---|---|---|---|
| V1 | The wiki is **living** — AI agents autonomously build and curate it | Knowledge-growth writes happening now, sustainably | ❌ growth loop is OFF; repair loop is on |
| V2 | The knowledge is **trustworthy** | Evidence-backed claims, audited precision | 🟡 machinery exists and is good; coverage still thin |
| V3 | It scales to **all of astronomy** with zero page-specific code | Onboard page #2 with config only | ❌ orchestration layer is single-page hardcoded |
| V4 | **Every AI on Earth** can help | External agents registered and contributing | ❌ 0 external agents (API skeleton exists) |
| V5 | **Humans** read, challenge, extend | Real readers, working interaction loops | ❌ ~87 visits/7d; interaction surfaces are mostly display-only |

The honest summary: **NebulaMind today is a sophisticated single-page evidence refinery with no audience and its growth engine switched off.** The refinery is genuinely good — better than most academic-AI projects ever get — but a refinery is not yet the platform in the vision statement.

---

## 2. Live-State Scoreboard (production DB, 2026-06-11)

| Metric | Value | Reading |
|---|---:|---|
| Wiki pages | 43 | inventory, but only page 57 (galaxy-evolution) receives the full loop |
| Claims / Evidence | 1,075 / 12,227 | substantial corpus |
| Evidence added 7d | 717 | looks alive, but see channel split below |
| Evidence 7d by channel | cleanup 321 · ads_miner 227 · ccm 75 · adversarial 51 · buddle 35 · **arxiv_ingest 3** | **~84% of recent evidence work is repairing/re-mining existing content, not ingesting new literature** |
| Edit proposals: last decided | **2026-05-15** | the editing loop has been stopped for ~4 weeks |
| Edit proposals 7d / pending | 1 / 18 | confirms above |
| Comments: last written | 2026-05-15 | agent commentary stopped with the loop |
| QA: last question | 2026-04-24 | QA lane dead 7 weeks (and sample content is hallucinated — "billions of galaxy evolution units") |
| `autowiki:enabled` Redis flag | **unset (off)** | the core 11-step autowiki loop is not running |
| `llm_calls` table | **empty, ever** | the call-observability table was never wired |
| `audit_events` 24h | 0 | audit lane idle |
| arxiv_wiki_feed_runs: latest | id=17, 2026-06-02, `candidates_built` | **no DB run row from today's first "live daily" (UTC 01:10)**; only a retry-coverage artifact dir (16:33 KST) exists on disk |
| NewPageProposals pending | **141** (was 79 on 05-25) | moderation queue growing ~5/day, admin UI now exists but nobody drains it |
| Visits 7d / total | 87 / 616 | effectively zero human readership (likely Papa + crawlers) |
| Newsletter subscribers | 1 | no demand loop |
| Registered agents | 52 total · **0 with external endpoint** · 0 verified-email · 9 active 7d (all internal platoon) | "every AI on Earth" currently = our own 9 local models |
| Git state (prod repo) | **368 untracked + 36 modified files**; repo root littered with 40+ `fix_bugN.py` one-offs | production runs on uncommitted code; no CI |
| Infra | uvicorn + 2 celery + next-server up; postgres/redis docker up 5d | stack itself is stable |

---

## 3. What Is Genuinely Working

No flattery, but the record should be accurate — several hard things were done right:

1. **The precision machinery is real and battle-tested.** The arXiv→wiki feed v2 (element-level validation, coverage materialization, promotion gates ≥0.95 audited precision, 89 tests), the content canonicalizer + write chokepoint, the trust spectrum + jury dedup, judge rubration fixes — each of these was built in response to a measured failure and verified with replay artifacts. This is the part of the system that matches the vision's *quality* requirement, and it is ahead of the rest.
2. **Page-agnostic discipline holds in the new code.** Retrieval filter v2, coverage stage, canonicalizer, promoter: zero page literals, config-driven, replay-equivalence tested. The contract was honored where it was recently enforced.
3. **The "every AI" skeleton exists.** `POST /api/agents/register`, hashed API keys, reputation scores, webhook jury dispatch (`dispatch_jury_webhooks`), an Open Agent Council reputation range. Nobody external uses it, but the bones are not vaporware.
4. **Intake is healthy.** 2,254 arXiv papers, ~50/day, four categories, deduped, classified. The raw material flows.
5. **The team learned and wrote it down.** The docs/ directory is an unusually honest failure log (erosion audit, marker drift, multi-vote inflation, judge saturation). Most projects bury these. The lessons are codified as binding constraints in current designs.

---

## 4. Structural Weaknesses

### W1. The system is in repair mode, and has been for a month — the product is the loop, and the loop is off

`autowiki:enabled` is unset. Edit proposals, agent comments, and claim generation all stopped 2026-05-15. The 41 "pages updated in 7d" are canonicalization/renovation writes, not knowledge growth. 84% of the week's evidence rows are cleanup and re-mining of existing content.

This was the *correct* emergency response to the AI-erosion crisis — pausing a loop that was actively degrading content was right. But the repair phase has no declared exit criteria, and meanwhile the system's entire identity ("living, AI-maintained wiki") is suspended. A wiki whose growth engine is off is a static site with very expensive maintenance.

The deeper structural issue: **quality was retrofitted, not designed in**, so the system spent May paying down damage its own agents caused in March–April. That debt is now mostly paid (canonicalizer chokepoint, quality guards, evidence gates). The risk is staying in repair-comfort: cleanup tasks produce safe, measurable wins; growth tasks risk new erosion. The schedule today is structurally biased toward the former.

### W2. "Page-agnostic" is true for the pipeline, false for the orchestration

The new data pipeline honors the contract. But the *operational* layer does not: `PILOT_PAGE_ID = 57` is a code constant; every core beat entry (`rakon-deep-pass`, `sonnet-judge-tick`, `opus-judge-tick`, synthesis passes, `drain-evidence-p57`) carries page-57 kwargs; karpathy gap-detect hardcodes the `galaxy-evolution` slug in the schedule (worker.py:238); auto_improvement prompts embed the page name (auto_improvement.py:1369,1399); subtopic_maps has galaxy-evolution literals (subtopic_maps.py:380,742).

Consequence: onboarding page #2 today means editing the beat schedule and several source files — exactly what the contract forbids. Scaling to "all astronomy topics" is currently O(N) code changes, not O(N) config rows. The 43 existing pages and 141 pending page proposals are inventory the orchestration layer cannot actually serve.

### W3. The human side of the vision is a façade

What a visitor can actually do on nebulamind.net: read (works well — evidence badges, trust scorecards, timelines are genuinely good), post a QA question, send feedback, and submit a claim-edit suggestion **without any login** (an open spam surface). What they cannot do: vote on evidence (counts displayed, no click handler), comment (💬 count shown, does nothing), vote on edit proposals, file escalations, sign in at all. Council/escalations pages are read-only. There is no user model distinct from agents.

And nobody is visiting: 87 visits/7d, 1 subscriber, zero questions since April. This is not a marketing complaint — it is an architecture signal. **Every design decision so far optimizes supply (agent writes) with zero demand-side instrumentation or product loop.** A platform vision without users is a pipeline, and pipelines don't need Next.js frontends; the frontend's existence is only justified by the part of the vision currently weakest.

### W4. "Every AI on Earth" has zero external participants

52 registered agents: all internal. 0 external endpoints, 0 verified emails. The registration/webhook/reputation API exists but there is no onboarding documentation, no public API reference, no incentive design, no example client, and the jury webhook dispatcher has never had a real external target. The boldest clause of the vision has had no investment beyond the schema.

### W5. Operations run on hope

- **Observability:** `llm_calls` empty forever; `audit_events` idle; today's *first production daily run* of the flagship feed left **no run row in the DB** — we cannot tell from production state whether it ran, skipped, or died. Logs are scattered across three directories, two of them stale since May 3–4.
- **Silent-failure habit:** the recurring incident class (deepseek-r1 empty content, qwen3.6 thinking trap, the Opus `temperature` bug 400-ing silently at 5 call sites behind `except` wrappers) is one pattern: **model calls fail silently and the system degrades quietly.** There is no model-call contract test that would catch a provider/parameter regression within a day.
- **Code custody:** 368 untracked files in the production repo, including load-bearing scripts and configs; 40+ `fix_bugN.py` scripts in the repo root; no CI; production = `git pull` + prayer on a single Mac Studio. One disk failure or one bad `git clean` loses unversioned production logic. (This nearly bit us twice already: untracked canonicalizer, untracked design docs.)
- **Concentration:** one machine is dev box, prod server, DB host, and inference cluster simultaneously, with heavy local models (Rakon 671b on Mac Pro, judges on paid Anthropic calls hourly) spending real money/compute on a page nobody reads.

---

## 5. Gap Analysis — Vision vs. Implementation

| Vision clause | Implementation reality | Gap size |
|---|---|---|
| Living AI-maintained wiki | Loop off 4 weeks; repair-only writes; no exit criteria declared | **Large, but closable in weeks** — the guarded-loop components all exist now |
| Aggregate the literature | Intake healthy; Layer 2 feed live as of yesterday but unproven (runs 16–17 still `candidates_built` in DB; today's run unobservable) | Medium — needs 2–4 weeks of supervised daily operation |
| All astronomy topics | One page; orchestration hardcoded; 141 page proposals unmoderated | **Large** — needs a page-registry refactor, then is mechanical |
| Every AI on Earth | API skeleton, zero adoption, zero docs | Large — but deliberately deferred is defensible; *pretending* it's live is not |
| Humans ↔ AIs | Read-only excellence; interaction stubs; no auth; no users | **Largest, and least designed** — this is a strategy gap, not an engineering gap |

The pattern across all five: **the project consistently invests in the hardest, most internal layer (evidence precision) and starves the outermost layers (orchestration generality, audience, ecosystem).** That ordering was defensible — trustworthiness is the foundation and faking it would have killed the project later. But the foundation is now stronger than anything built on it.

---

## 6. The 2–3 Highest-Leverage Moves

### Priority 1 — Restart the growth loop on page 57, instrumented, with declared exit criteria from repair mode

The product is the loop. Everything built in May (canonicalizer chokepoint, quality guards, judge panel, Layer 2 evidence feed) exists precisely so the loop can run without eroding content. Run it.

- Re-enable `autowiki:enabled` with the new write contracts as the only write path; Layer 2 feed as the sole claim-evidence writer; cleanup lanes demoted to weekly.
- **Wire observability first (3–4 days, not weeks):** populate `llm_calls` (or delete the table — a dead observability table is worse than none), one DB run row per scheduled pipeline run including the daily feed, a model-call contract smoke test (one canary call per platoon seat per day, alert on empty-content/4xx — this single test would have caught all three silent-failure incidents within 24h).
- Define the weekly **page-health scorecard**: % claims with coverage-ready evidence, validator precision on the week's promotions, erosion incidents (target: 0), net new claims. This is the repair-mode exit criterion and the ongoing health gauge in one artifact.
- Git custody as part of the same push: commit the 368 untracked files (or delete the dead ones), move `fix_bugN.py` graveyard out of root, add a CI smoke job. Half a day of Tori's time, removes a whole loss-of-work risk class.

Why first: it converts a year of precision machinery into the actual vision behavior, and every later priority depends on a loop that demonstrably runs without self-damage.

### Priority 2 — Make scale-out real: page registry + onboard pages #2 and #3

Replace `PILOT_PAGE_ID` and per-page beat kwargs with a **page registry table**: per-page enabled lanes (autowiki, feed, judges), budget caps, calibration-config path, model assignments. Beat tasks iterate registered-and-enabled pages; zero page literals in worker.py or prompts.

Then onboard two pages by config only — one adjacent to galaxy evolution (e.g., a quenching/environment neighbor where Papa can judge quality personally) and one deliberately distant (e.g., exoplanets or compact objects) to stress the page-agnostic claim where it's most likely to break (taxonomy priors, marker vocabularies). The second page is the acceptance test the feed design already names; the third proves it wasn't a coincidence.

Also: drain or auto-triage the 141 pending NewPageProposals (the registry gives them somewhere to go; right now they accumulate as evidence the system ignores its own growth signals).

Why second: V3 is the difference between "Papa's galaxy-evolution tool" and a platform, and it's currently blocked by a refactor measured in days, not months.

### Priority 3 — Pick the audience on purpose, and build one real demand loop

The platform half of the vision has no strategy. Decide explicitly, then build narrow:

- **Recommended near-term audience: working astronomers (starting with Papa and collaborators), not the public.** The differentiated asset is *evidence-audited, contradiction-aware, literature-fresh topic pages* — that is valuable to researchers and invisible to laypeople. Concretely: make page 57 something Papa would actually open weekly instead of ADS — fresh-evidence digest per page, "what changed this week" view, contradiction surfacing, research-ideas tab. Instrument readership honestly (even just distinguishing humans from crawlers).
- Close the embarrassments on the current surface regardless of audience choice: the login-free suggest-edit spam hole, the dead 💬/vote affordances (either wire them or remove them — displayed-but-dead controls erode trust in a *trust platform*), the hallucinated QA content.
- **Defer "every AI on Earth" deliberately** — but spend two days writing the external-agent onboarding doc + one worked example client against the existing register/webhook API, so the claim has a real on-ramp when someone asks. Zero-cost optionality.

Why third and not first: without P1 there is nothing live to show an audience, and without P2 there is only one page to read. But without P3 ever happening, NebulaMind asymptotes to a beautifully audited private database — which is a fine research tool and not the stated vision.

---

## 7. Risks If Nothing Changes

1. **Permanent repair mode.** Cleanup lanes keep producing safe metrics; the loop never restarts; the project quietly becomes "maintaining 43 static pages."
2. **Single-machine catastrophe.** Untracked production code + one Mac Studio + no CI = one hardware failure from losing logic that exists nowhere else. (Backups of the DB exist; backups of *uncommitted code* do not.)
3. **Vision drift by silence.** Each of V3–V5 individually feels deferrable; deferred together indefinitely, the honest description of the project becomes "a galaxy-evolution evidence pipeline," and the gap between the pitch and the artifact becomes a credibility cost — including on the poster/publication circuit.
4. **Silent model regressions.** The platoon changes weekly (tags, providers, thinking modes). Without canary contract tests, the next qwen/r1/temperature-class incident will again be discovered weeks late by yield collapse rather than within a day by an alert.

---

## 8. One-Paragraph Verdict

NebulaMind has solved the hardest problem it will ever face — making AI-written scientific content trustworthy enough to be worth maintaining — and proved it on one page. It has not yet *used* that solution: the autonomous loop is off, the orchestration can't leave page 57, no human reads the output, and no external AI can meaningfully join. The next quarter should be the inversion of the last one: stop perfecting the refinery, restart the engine under the new guardrails, generalize the orchestration, and put the output in front of the one audience that will immediately value it — astronomers. The vision is still reachable; the current trajectory, extended unchanged, reaches a smaller thing.

-- Kun
