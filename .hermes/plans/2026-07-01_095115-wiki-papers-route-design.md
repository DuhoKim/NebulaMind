# Frontend `/wiki/papers` route design / scaffold plan

> **For Hermes:** This is a design artifact only. Do not implement until the user separately approves implementation.

**Goal:** Add frontend pages that consume the existing read-only paper directory/profile APIs so users can open `/wiki/papers/...` links without a missing route.

**Architecture:** Add static App Router segments under `frontend/src/app/wiki/papers/` so they outrank the existing dynamic `/wiki/[slug]` route. The pages call existing backend APIs only; they do not write DB rows, materialize source links, promote claims, or change trust badges.

**Tech Stack:** Next.js App Router, React client components where search/filter state is needed, existing NebulaMind API base/fetch patterns, existing wiki visual language.

---

## Current context

- Backend tests already define `profile_href` as `/wiki/papers/arxiv%3A2606.990101`.
- Goru/Hermes scans found no frontend `/wiki/papers` route by path heuristic.
- Backend contracts are read-only:
  - `GET /api/pages/paper-directory?q=<query>&limit=<n>`
  - `GET /api/pages/paper-profile?paper_id=<profile_id>`

## Proposed files

- Create: `frontend/src/app/wiki/papers/page.tsx`
- Create: `frontend/src/app/wiki/papers/PaperDirectoryClient.tsx`
- Create: `frontend/src/app/wiki/papers/[paperId]/page.tsx`
- Create: `frontend/src/app/wiki/papers/[paperId]/PaperProfileClient.tsx`
- Create: `frontend/src/app/wiki/papers/types.ts`
- Create tests/smokes:
  - `frontend/scripts/test-wiki-papers-route-contract.mjs`
  - `frontend/scripts/test-wiki-papers-profile-contract.mjs`

## UI behavior

### Directory page: `/wiki/papers`

- Search box maps to API `q`.
- Result cards show paper title, author-year key, page count, claim count, evidence count, tone counts, source gap count, and triage status.
- Clicking a result opens `profile_href` from the API.
- Empty search returns a friendly empty deck, not an error.
- Copy/citation buttons should be client-only and non-mutating.

### Profile page: `/wiki/papers/[paperId]`

- Decode the dynamic segment before passing it as `paper_id`.
- Show paper summary, triage status, pages containing the paper, claim snippets, stance/tone, vote counts, and source gaps.
- Link every claim back to the canonical wiki anchor using API-provided `href`.
- Display caveat text from `scope.caveat`: this is not a final verdict.

## TDD implementation steps for later approval

1. Add contract smoke for directory payload shape and route expectation.
2. Add `types.ts` matching `global_paper_directory.v1` and `paper_profile.v1` fields used by the UI.
3. Create `/wiki/papers/page.tsx` plus `PaperDirectoryClient.tsx` with loading/error/empty states.
4. Create `/wiki/papers/[paperId]/page.tsx` plus `PaperProfileClient.tsx` with profile loading/error states.
5. Verify route precedence: `/wiki/papers` and `/wiki/papers/arxiv%3A...` must not fall through to `/wiki/[slug]`.
6. Run frontend contract smokes and targeted build/type checks.

## Acceptance checks for later implementation

```bash
node frontend/scripts/test-wiki-papers-route-contract.mjs
node frontend/scripts/test-wiki-papers-profile-contract.mjs
npm --prefix frontend run build
```

Expected: route contract tests pass; build succeeds; no backend/API changes; no DB writes.

## Risks / open questions

- URL decoding: dynamic segment must preserve `arxiv:...` / `evidence:...` profile IDs.
- Large directories: keep API limit/search explicit and disclose truncation.
- Trust semantics: triage status is a review aid, not a promotion badge.
- Product wording: claim profile pages need caveats so readers do not confuse source aggregation with scientific consensus.

## Explicitly out of scope until separately approved

- Implementing files above.
- Backend API changes.
- DB writes/materialization.
- Deploy/restart.
- Trust badge or claim promotion changes.
