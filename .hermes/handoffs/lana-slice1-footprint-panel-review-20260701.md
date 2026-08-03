# Lana Review — Slice 1 "Cited across NebulaMind" Footprint Panel (2026-07-01)

Ref: brief SLICE1-FOOTPRINT-PANEL-REVIEW-20260701 (review-only). Reviewer: Lana (Claude Code).
Author under review: Goru. Canonical status → Hermes Kanban; this is the detailed review.

## VERDICT: ISSUES
Non-blocking. The slice is **safe, compiles clean, and is well-tested for what it covers**, but there is **one real correctness/affordance defect** (404 → misleading error) plus two design/affordance concerns cockpit should rule on before merge. None are safety-boundary violations.

## Reviewed files (worktree: wiki-papers-route-20260701)
- `frontend/src/app/wiki/papers/[paperId]/PaperFootprintPanel.tsx` (new)
- `frontend/src/app/wiki/papers/[paperId]/paperFootprintQuery.ts` (new)
- `frontend/src/app/wiki/papers/[paperId]/PaperProfileClient.tsx` (mod — fetch + wiring)
- `frontend/src/app/wiki/papers/profile-fixture/page.tsx` (mod — footprint fixture)
- `frontend/scripts/test-wiki-paper-footprint-panel.mjs` (new — test)
- Reused (read-only): `frontend/src/app/wiki/[slug]/sources/crossPagePaperFootprint.ts`; backend `backend/app/routers/pages.py::get_cross_page_paper_footprint`

## Commands run (read-only)
- `git diff --stat / git diff` on the papers route → 2 files modified (+108/−2), 3 new files.
- `node scripts/test-wiki-paper-footprint-panel.mjs` → `wiki_paper_footprint_panel_ok` (green, re-run).
- `node scripts/test-cross-page-paper-footprint.mjs` → `cross_page_paper_footprint_ok` (green).
- `node scripts/test-paper-profile-detail.mjs` → `paper_profile_detail_ok` (green).
- `npx tsc --noEmit` → **exit 0, 0 errors** (whole worktree frontend typechecks, incl. new code + bracket-path import).

## Safety boundary: PASS
- Only read-only `GET /api/pages/paper-footprint`. No POST/PUT/DELETE anywhere in the diff. Backend endpoint is SELECT-only.
- Copy is correctly framed: "No labels are written from this panel" + scope caveat "not a final verdict." No label/trust/DB writes.
- `testOnly*` props are test-scoped and correctly gated (`testOnlyFootprintData !== undefined` distinguishes live vs fixture). Clean.

## Concerns (ranked)
1. **[ISSUE — correctness/affordance] 404 conflated with load failure.** `PaperProfileClient` footprint fetch does `if (!response.ok) throw` → `.catch` sets `footprintError` ("Couldn't load Cited across NebulaMind footprint. Retry."). But the endpoint **raises HTTP 404 when a paper has no footprint rows** (`if not rows: raise HTTPException(404)`). So an uncited paper — or one whose profile loaded with zero pages, or whose arXiv-id normalization differs between `paper-profile` and `paper-footprint` — shows the **error + Retry** state (and Retry keeps 404ing) instead of the panel's graceful empty state ("No wiki-wide citation footprint is available for this paper yet"). Net effect: the empty state is nearly unreachable for arXiv papers, and thin/empty-profile papers get a misleading error. **Recommended fix (Goru): treat `response.status === 404` as empty (`setFootprintPayload(null)`, no error), reserving the error state for 5xx/network.** ~1 line.
2. **[CONCERN — design redundancy] On-page duplication.** The footprint panel renders the paper's pages+claims, and the existing profile deck below (`buildPaperProfileDeck` over `paper-profile.pages`) renders essentially the same "where cited" content. The profile page now shows it **twice**. Cockpit call: make the panel a compact roll-up (counts + page chips) vs. a full second render, or have it replace the profile deck. Not a blocker.
3. **[CONCERN — minor affordance] No truncation cap.** The panel maps **all** pages and **all** claims with no cap or truncation disclosure, unlike the profile deck (which has `truncationDisclosure` for review safety). Low risk for a single paper, but inconsistent; a heavily-cited paper yields a long unbounded list.

## Tests: good, with gaps
- Strong: `buildPaperFootprintQuery` edge cases (arxiv:, evidence:, doi→profile-arxiv wins, doi→evidence fallback), panel selectors, helper-reuse assertion, truth-framing copy, fixture payload, and registration in `package.json:35` + aggregate `test-wiki-ux-smoke.mjs:24` (marker `wiki_paper_footprint_panel_ok`). All green; full tsc clean.
- Gaps: (a) **no coverage of the 404/empty runtime path** — ISSUE-1 is unguarded (smokes are transpile-only static/logic tests, not fetch/integration); (b) panel empty-state copy unasserted; (c) query builder bare-id and null-return branches untested. Acceptable for the smoke style, but ISSUE-1 has no regression guard.

## Recommended next action
1. Goru: apply the 404→empty fix (concern 1) and add a small assertion for the empty path; re-run `test:wiki-paper-footprint-panel`.
2. Cockpit/Papa: decide the duplication question (concern 2) — compact roll-up vs. full deck.
3. Before any merge (still gated): run full `npm run test:wiki-ux-smoke` + `npm run build`; then Papa merge-go. No DB/deploy implied by this slice.

## Ledger
- Task: review-only of Slice 1 footprint panel diff. Lane: Lana (review) — Goru (author) — Hermes (cockpit).
- Status: DONE. Verdict ISSUES (1 fix + 2 design calls; safe + compiles + green).
- Safety: no DB, migration, deploy/restart, commit/push/merge, OpenClaw, secrets. No files edited (review-only); wrote only this handoff.
