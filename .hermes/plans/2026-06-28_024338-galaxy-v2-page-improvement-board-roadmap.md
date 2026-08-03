# Galaxy V2 Page Improvement Board Roadmap

> **For Hermes:** Use subagent-driven-development skill to implement this plan task-by-task. Keep production data/content mutations behind backup/rollback/exact-diff packets and explicit approval phrases.

**Goal:** Improve the live Galaxy Evolution V2 page from a verified best-effort publish into a polished, reader-facing, evidence-transparent science article.

**Architecture:** Separate three workstreams: reader-facing prose cleanup, evidence/trust readiness, and frontend/API UX reliability. Treat all live content/database publishes as gated mutation packets; code-only frontend/backend PRs can be handled separately but must avoid hidden DB writes from public page loads.

**Tech Stack:** NebulaMind FastAPI backend, PostgreSQL, Next.js/React frontend, public wiki API, static Hermes report artifacts under `frontend/public/human-cal/` and `frontend/public/agent-reports/`.

---

## Current Baseline

Live page:
- URL: `https://nebulamind.net/wiki/galaxy-evolution-v2`
- Page id: `58`
- Slug: `galaxy-evolution-v2`
- Latest version: `6`
- Content SHA256: `f48151f14150e9c5528a1573c46beb696eb08e20c6961563f1349e902f4e32ce`
- Claim markers: `8`
- Claims: `3 consensus`, `5 debated`
- Claim evidence links: `102`

Recent publish artifacts:
- Main content publish packet: `docs/galaxy_v2_content_publish_preflight_20260627T170527Z/`
- Disclaimer-fix publish packet: `docs/galaxy_v2_disclaimer_fix_publish_preflight_20260627T172833Z/`
- Post-confirmation readiness: `docs/galaxy_v2_post_confirmation_readiness_20260627T164022Z.md`
- Evidence map: `docs/galaxy_v2_best_effort_evidence_map_20260627T165252Z.csv`

Hard safety constraints:
- No trust-level or trust-score mutation without a separate claim/trust packet.
- No evidence/vote writes without row-level backup/diff/rollback approval.
- No threshold retune: current numeric score rows are `0`.
- Future live content edits require `APPROVE PUBLISH <packet_id>` after packet review.

---

## Board Consensus

The board agrees the current page is safe as a best-effort prose revision, but not yet a polished public article.

Top issues:
1. Public prose still exposes internal/editorial process language.
2. Raw evidence anchors read like pipeline artifacts, not science writing.
3. Citation/source UX promises paper sourcing but `/citations` and `/fact-sources` are empty.
4. Public page load may call `/api/pages/{slug}/health`, and that endpoint currently commits to DB from a GET route.
5. Ideas endpoint used by frontend returns `500`; legacy research ideas endpoint works.
6. Trust/evidence calibration is not representative enough for badge or threshold changes.

Recommended immediate next move:
- Stage 0: prepare a read-only UX/safety report packet.
- Stage 1: code-only PR to eliminate hidden public GET writes and fix reader trust affordances.
- Stage 2: prose-only cleanup publish packet to remove internal process language and raw evidence-anchor prose.

---

## Phase 0: Read-only Baseline and UX/Safety Report

**Objective:** Freeze the current version-6 baseline and produce a visual/report artifact before code or content changes.

**Files:**
- Read: `docs/galaxy_v2_disclaimer_fix_publish_preflight_20260627T172833Z/post_publish_verification_latest.json`
- Read: `docs/galaxy_v2_disclaimer_fix_publish_preflight_20260627T172833Z/proposed_content.md`
- Read: `frontend/src/app/wiki/[slug]/WikiPageClient.tsx`
- Read: `backend/app/routers/pages.py`
- Create: `docs/galaxy_v2_v6_board_baseline_<timestamp>.json`
- Create: `docs/galaxy_v2_v6_board_baseline_<timestamp>.md`
- Create: `frontend/public/human-cal/galaxy-v2-v6-board-baseline-latest.html`

**Steps:**
1. Fetch public API state with a browser-like User-Agent.
2. Record page id, slug, version, content length, SHA256, heading count, claim marker count.
3. Read claims API and count consensus/debated/challenged/unverified claims and evidence links.
4. Verify `/citations`, `/fact-sources`, and `/ideas` behavior without causing writes.
5. Inspect whether public page load still triggers `/health`.
6. Generate a static HTML report showing current top fold, trust summary, evidence/source mismatch, ideas endpoint status, and hidden-write risk.

**Acceptance criteria:**
- Report states `DB writes executed: 0`.
- Live API remains version `6`, SHA `f48151f...e32ce` after report generation.
- Report includes a clear warning if `/health` public GET still writes.

---

## Phase 1: Code-only Safety and UX Reliability PR

### Task 1.1: Remove hidden page-load DB writes from health display

**Objective:** Ensure ordinary public page loads do not commit to the database.

**Files:**
- Modify: `frontend/src/app/wiki/[slug]/WikiPageClient.tsx`
- Modify: `backend/app/routers/pages.py`
- Test: add or update a frontend/backend smoke test if test harness exists.

**Recommended approach:**
- Short term: stop auto-fetching `/api/pages/${slug}/health` from the public wiki page.
- Use `page.health_score` already returned by `/api/pages/{slug}` if available.
- Longer term: split health into read-only public endpoint and explicit admin/cache-refresh endpoint.

**Validation commands:**
- `cd frontend && npm run build`
- `cd frontend && npm run test:wiki-trust-visibility`
- Backend route grep/check: public GET routes used by wiki page should not call `db.commit()`.

**Acceptance criteria:**
- Loading `/wiki/galaxy-evolution-v2` performs no write-intended public GET.
- Health badge still degrades gracefully if score is absent.

### Task 1.2: Fix Sources/Evidence mismatch

**Objective:** Stop promising sentence-level citations when the page has zero citation records but 102 claim evidence links.

**Files:**
- Modify: `frontend/src/app/wiki/[slug]/WikiPageClient.tsx`
- Modify: `frontend/src/app/wiki/[slug]/sources/WikiSourcesClient.tsx`
- Possibly modify: `backend/app/routers/pages.py`
- Possibly read/use: `backend/app/routers/claims.py`

**Recommended approach:**
- Update UI copy from “Each sentence is sourced…” to “Highlighted claims are linked to paper evidence. Click a trust badge to inspect supporting/countering papers.”
- Sources page should show claim/evidence-derived sources when fact sources are empty.
- If full backend aggregation is too large, add a frontend empty state that links users to claim evidence panels and states the evidence layer has 102 links.

**Validation commands:**
- `cd frontend && npm run build`
- Manual/local visual check: Galaxy V2 Sources page must not say “No source records found” without explanation.

**Acceptance criteria:**
- Page no longer overpromises sentence-level citations.
- Sources/Evidence view acknowledges claim evidence count.

### Task 1.3: Fix Ideas endpoint fallback

**Objective:** Make “Show Ideas” reliable or visibly unavailable.

**Files:**
- Modify: `frontend/src/app/wiki/[slug]/WikiPageClient.tsx`
- Possibly modify: `backend/app/routers/research_ideas.py`

**Recommended approach:**
- If `/api/pages/${slug}/ideas?per_page=100` fails, fallback to `/api/research/ideas/${slug}?per_page=100`.
- Add a non-alarming empty/error state.

**Acceptance criteria:**
- Galaxy V2 no longer silently fails ideas loading.
- The legacy endpoint’s 4 ideas are reachable until backend route is fixed.

### Task 1.4: Fix edit proposal false success

**Objective:** Prevent unauthenticated readers from seeing a false “success” message for edit proposals that fail auth.

**Files:**
- Modify: `frontend/src/app/wiki/[slug]/WikiPageClient.tsx`
- Possibly modify: `backend/app/routers/pages.py`

**Recommended approach:**
- Check `response.ok` before showing success.
- If auth is required, hide the form or show “sign in/API key required” messaging.

**Acceptance criteria:**
- 401/403 is shown honestly.
- No false success state on failed submission.

---

## Phase 2: Reader-first Frontend Polish

**Objective:** Make Galaxy V2 read like a science page, not an internal pilot artifact, without changing DB content yet.

**Likely files:**
- `frontend/src/app/wiki/[slug]/WikiPageClient.tsx`
- `frontend/src/app/wiki/[slug]/TOCSidebar.tsx`
- `frontend/src/app/wiki/[slug]/DebateEvidencePanel.tsx`
- `frontend/src/app/wiki/[slug]/trustVisibility.ts`
- Optional new components:
  - `frontend/src/app/wiki/[slug]/WikiHero.tsx`
  - `frontend/src/app/wiki/[slug]/RevisionNote.tsx`
  - `frontend/src/app/wiki/[slug]/TrustGuide.tsx`

**Design changes:**
1. Display reader title as “Galaxy Evolution”; move “Intro-Synthesis V2 Pilot” into provenance.
2. Move the long live-revision disclaimer into a collapsible “About this revision” box.
3. Add a plain-language one-sentence summary.
4. Replace jargon labels:
   - `Citation View` → `Evidence view`
   - `Raw Text` → `Reader view`
   - `Colors On` → `Reduce highlights` / `Show highlights`
5. Redesign trust summary:
   - 8 trust-bearing claims
   - 3 consensus
   - 5 debated
   - 102 evidence links
   - “Jump to debated claims”
   - “Open evidence table”
6. Improve inline claim affordance with hover/focus explainer and copy-link anchor.
7. Upgrade evidence panel with support/counter filters, year/source metadata, and clearer empty states.

**Validation:**
- `cd frontend && npm run build`
- `cd frontend && npm run test:wiki-trust-visibility`
- Keyboard/focus check for trust badges and evidence panels.
- Static visual report under `frontend/public/human-cal/`.

**Acceptance criteria:**
- A reader can understand the page topic, uncertainty level, and evidence affordances in the first screen.
- No hidden public GET writes.
- No source/citation promise mismatch.

---

## Phase 3: Prose-only Public Cleanup Packet

**Objective:** Remove internal process language from live content and convert raw evidence anchors into readable scientific prose.

**Scope:** Content publish only. No trust/evidence/threshold mutation.

**Files to use:**
- Baseline: live version 6 content from API/DB.
- Prior content: `docs/galaxy_v2_disclaimer_fix_publish_preflight_20260627T172833Z/proposed_content.md`
- Evidence map: `docs/galaxy_v2_best_effort_evidence_map_20260627T165252Z.csv`
- Readiness: `docs/galaxy_v2_post_confirmation_readiness_20260627T164022Z.md`

**Text to remove or rewrite:**
- `best-effort`
- `confirmation pass`
- `write-ready counted support`
- `stop asking for more calibration`
- `count as support`
- `count as weakening`
- raw candidate/evidence notes like `c2929-e28095 ... count as support`

**Recommended replacements:**
- Convert AGN evidence anchors into a short “Evidence snapshot” paragraph.
- Convert environmental anchors into readable satellite/cosmic-web prose.
- Replace `Best-effort editorial conclusion` with `Synthesis: What Regulates Galaxy Evolution?` or `Open Questions`.

**Packet requirements:**
- Backup JSON and markdown snapshot.
- Exact diff patch and JSON.
- Rendered preview HTML.
- Apply SQL with drift guards on current version 6 SHA.
- Rollback SQL.
- Approval phrase: `APPROVE PUBLISH <packet_id>`.

**Acceptance criteria before approval:**
- No internal pipeline/process terms remain in public prose.
- Claim markers remain balanced and still exactly 8 unless packet explicitly changes claim metadata.
- Trust levels/scores/evidence/votes/thresholds remain excluded.

---

## Phase 4: Scientific Scaffold Expansion

**Objective:** Expand the article into a stronger broad Galaxy Evolution explainer.

**New/expanded sections to draft:**
1. `Cosmic Timeline`
   - first galaxies/reionization
   - cosmic noon
   - star-formation decline
   - red sequence growth
2. `The Baryon Cycle`
   - inflow, cooling, star formation, enrichment, outflows, recycling
   - CGM/IGM reservoirs
3. `Morphology and Dynamics`
   - disk growth, spheroids, mergers, secular evolution, bars
   - morphological quenching as stabilization
4. `Chemical Enrichment and Dust`
   - metals as fossil records
   - dust as physical component and observational bias
5. `Simulations and Models`
   - ΛCDM, hydrodynamical simulations, semi-analytic models, abundance matching
   - subgrid feedback uncertainty
6. `Frontiers and Open Questions`
   - JWST high-z massive candidates
   - AGN coupling efficiency
   - quenching timescales
   - environmental quenching at high redshift
   - CGM baryon accounting

**Acceptance criteria:**
- Each section answers: mechanism, target, observations, caveats.
- JWST/high-z discussion is conditional, not “ΛCDM falsified.”
- AGN feedback remains mode-, phase-, scale-, and environment-dependent.
- Environment claims distinguish satellites/low-mass systems from generic density correlations.

**Gate:**
- Publish through a prose-only packet unless trust/evidence changes are separately scoped.

---

## Phase 5: Evidence and Trust Readiness Program

**Objective:** Move from best-effort prose to defensible claim/trust decisions.

**Artifacts to use:**
- `docs/galaxy_v2_post_confirmation_audit_queue_20260627T164022Z.csv`
- `docs/galaxy_v2_post_confirmation_assistant_disagreements_20260627T164022Z.csv`
- `docs/galaxy_v2_post_confirmation_human_counted_candidates_20260627T164022Z.csv`
- `docs/galaxy_v2_representative_candidate_queue_20260627T130801Z.csv`
- `docs/galaxy_v2_representative_queue_manifest_20260627T130801Z.json`

**Plan:**
1. Close all `needs_discussion` rows before they anchor public support.
2. Review the 12 assistant-counted-but-human-noncount rows.
3. For claim 2929, second-review all support and weakening anchors.
4. Expand to representative claim review.
5. Produce one read-only claim readiness packet per claim.

**Claim posture:**
- `2929`: strongest but mixed; keep nuanced, no trust mutation until second review.
- `2930`: no human-counted support in confirmation pass; prose caveat only.
- `2931`: no counted support; debated framing only.
- `2932`: contextual morphology/environment evidence; no strengthening.
- `2933`: needs fresh review.
- `2934`: one support plus one discussion; too sparse for trust change.
- `2935`: one support but only two candidate rows; evidence-limited.
- `2936`: no confirmed counted anchors; evidence-limited.

**Acceptance criteria for any trust-bearing conclusion:**
- Prefer `>=20` representative human-reviewed rows per claim where available.
- Sparse claims: review all rows and label evidence-limited.
- At least 3 independent source families for a claim being strengthened.
- `needs_discussion = 0` for anchors used in trust decisions.
- Weakening rows for consensus claims get second-human review.

**Hard gate:**
- No threshold retune until numeric score rows exist and a representative human-gold sample is complete.

---

## Phase 6: Future Publish/Mutation Gate Template

Every future packet must declare exactly one scope:
1. Prose-only content publish.
2. Claim metadata alignment.
3. Evidence/vote mutation.
4. Trust badge/score mutation.
5. Threshold retune.
6. Code/frontend deploy.

Required fields:
- Current live page id/slug/version/SHA.
- Exact diff.
- Backup and rollback.
- Apply script with drift guards.
- Expected row counts.
- Forbidden write list.
- Unique approval phrase.
- Post-publish DB/API/DOM verification.

Reject mixed packets unless explicitly requested and separately reviewed as high-risk.

---

## Recommended Next Action

Start with Phase 0, then Phase 1.

Reason:
- Phase 0 is read-only and gives a stable baseline/report.
- Phase 1 removes hidden write risk and fixes reader trust affordance problems before more visual automation or public polish.
- Phase 3 prose cleanup should follow after source/evidence UI language is honest.

No production data/content mutation should happen until a packet is prepared and the user approves the exact phrase.
