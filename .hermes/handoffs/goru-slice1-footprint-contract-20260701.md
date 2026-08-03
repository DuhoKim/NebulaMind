# Goru Slice 1 Footprint Contract — 2026-07-01

## Status
COMPLETE

## Files Inspected
- `/Users/duhokim/NebulaMind/worktrees/wiki-papers-route-20260701/backend/app/routers/pages.py`
- `/Users/duhokim/NebulaMind/worktrees/wiki-papers-route-20260701/frontend/src/app/wiki/papers/[paperId]/PaperProfileClient.tsx`
- `/Users/duhokim/NebulaMind/worktrees/wiki-papers-route-20260701/frontend/src/app/wiki/papers/[paperId]/paperProfile.ts`
- `/Users/duhokim/NebulaMind/worktrees/wiki-papers-route-20260701/backend/tests/`
- `/Users/duhokim/NebulaMind/worktrees/wiki-papers-route-20260701/frontend/scripts/`

## Endpoint Contract
- **Endpoint Path**: `/api/pages/paper-profile` (Note: the backend defines both `paper-footprint` and `paper-profile`, but the frontend `[paperId]` route explicitly consumes `paper-profile`).
- **Request**: Query parameter `?paper_id=${encodeURIComponent(paperId)}`.
- **Response Fields Needed by UI**:
  - `schema_version`
  - `paper`: Contains `evidence_id`, `arxiv_id`, `doi`, `url`, `title`, `authors`, `year`, `summary`, `author_year_key`.
  - `page_count`, `claim_count`, `evidence_count`
  - `tone_counts`: Dictionary containing `support`, `counter`, `neutral` counts.
  - `trust_counts`: Dictionary mapping trust strings to counts.
  - `scope`: Object containing `label` and `caveat`.
  - `pages`: Array of page buckets.
  - `claims` (nested inside each page bucket): Array of claim objects containing `claim_id`, `claim_text`, `section`, `trust_level`, `evidence_id`, `stance`, `status`, `tone`, `href`, `votes_agree`, `votes_disagree`.

## Identifier Mapping
- The Next.js URL segment `[paperId]` is URI-decoded and passed directly to the backend API.
- Supported identifier schemas handled by the backend parser:
  - `arxiv:XXXXX`
  - `doi:XXXXX`
  - `url:XXXXX`
  - `evidence:XXXXX`
  - Unprefixed strings gracefully fallback to being treated as arXiv IDs.

## Required UI Markers
A finished and compliant React panel uses the following exact `data-testid` markers:
- `paper-profile-detail`
- `paper-profile-directory-link`
- `paper-profile-backlink`
- `paper-profile-status-chip`
- `paper-profile-scope-caveat`
- `paper-profile-truncation-disclosure`
- `paper-profile-error`
- `paper-profile-empty`
- `paper-profile-page-card`
- `paper-profile-claim-row`

## Existing Scripts/Tests
- **Backend Tests**:
  - `backend/tests/test_paper_profile_api.py`
  - `backend/tests/test_cross_page_paper_footprint_api.py`
- **Frontend Smoke Scripts**:
  - `frontend/scripts/test-wiki-paper-profile-browser.mjs`
  - `frontend/scripts/test-wiki-paper-profile-browser-contract.mjs`
  - `frontend/scripts/test-paper-profile-detail.mjs`

## Risks/Blockers
- None. The API contract matches the Typescript interface and the route identifier mapping is fully decoupled by prefix schemas.

## Suggested Verification Commands
```bash
# Backend validation
cd /Users/duhokim/NebulaMind/worktrees/wiki-papers-route-20260701
pytest backend/tests/test_paper_profile_api.py
pytest backend/tests/test_cross_page_paper_footprint_api.py

# Frontend static validation
node frontend/scripts/test-wiki-paper-profile-browser-contract.mjs
```
