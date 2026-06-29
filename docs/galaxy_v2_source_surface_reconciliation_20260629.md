# Galaxy Evolution V2 source-surface reconciliation — 2026-06-29

Status: LOCAL_CODE_FIX_VERIFIED_NOT_DEPLOYED

This packet completes the source-surface reconciliation slice after the artifact-only element validation pass. It is not a promotion packet: no production DB rows were written, no claims were created, no `coverage_ready` flags were set, no promoter ran, and no service was restarted.

## Live baseline before local fix

Read-only probes against `https://nebulamind.net/api/pages/galaxy-evolution-v2` at `2026-06-29T10:39:48Z` showed:

- page id: `58`
- slug: `galaxy-evolution-v2`
- version_num: `7`
- content_length: `10265`
- content_sha256: `ab6502e572a6189b173b9be934a2f812091d5004a5cc2102211464bc4747190c`
- claim markers in page content: `8`
- `/api/pages/galaxy-evolution-v2/citations`: `0` citations
- `/api/pages/galaxy-evolution-v2/fact-sources`: `0` rows
- `/api/pages/paper-directory?q=galaxy-evolution-v2&limit=5`: `34` evidence-indexed papers, including page `58`
- `/api/pages/paper-footprint?arxiv_id=2604.03503`: evidence-linked footprint includes page `58`

## Root cause

The public page source surfaces were too narrowly coupled to materialized side tables:

1. `/citations` only read `page_citation_links`. For page 58 that table can be empty even when the page has indexed `claims` and `evidence` rows.
2. `/fact-sources` only read `fact_sources` rows for hero facts. Page 58 currently has no `hero_facts`, but it does have claim/evidence provenance that should still be visible as a source surface.
3. The `arxiv_papers.related_pages` mismatch remains a data-linkage finding for the arXiv feed candidate-builder path. I did not mutate `related_pages`; the safe read path is to expose existing claim/evidence provenance without pretending it is promotion-ready supply.

## Local code fix

Changed `backend/app/routers/pages.py`:

- Added read-only claim/evidence fallback helper for page source surfaces.
- `/api/pages/{slug}/citations` now keeps existing `page_citation_links` behavior when links exist, but falls back to page claim/evidence rows when links are empty.
- `/api/pages/{slug}/fact-sources` now keeps existing `fact_sources` behavior when rows exist, then falls back to inline `hero_facts[].source`, then finally to read-only claim/evidence source rows when both are empty.
- Fallback URLs are derived only from existing evidence `url`, `doi`, or `arxiv_id` fields.
- Fallbacks do not insert `page_citation_links`, do not insert `fact_sources`, do not edit page content, and do not modify `arxiv_papers.related_pages`.

## TDD proof

Added `backend/tests/test_page_source_surface_fallbacks.py`.

RED result before implementation:

- `test_citations_fall_back_to_page_claim_evidence_without_writing_links` failed because `citations == []`.
- `test_fact_sources_fall_back_to_claim_evidence_when_fact_source_table_is_empty` failed because `fact-sources == []`.

GREEN result after implementation:

- `python -m pytest tests/test_page_source_surface_fallbacks.py -q`
- Result: `5 passed`.

Post-cutoff recovery verification:

- `python -m py_compile app/routers/pages.py tests/test_page_source_surface_fallbacks.py`: pass.
- `python -m pytest tests/test_page_source_surface_fallbacks.py::test_fact_sources_keep_inline_hero_sources_before_claim_evidence_fallback -q`: `1 passed`.
- `python -m pytest tests/test_page_source_surface_fallbacks.py -q`: `5 passed`.
- `python -m pytest tests/test_page_source_surface_fallbacks.py tests/test_cross_page_paper_footprint_api.py tests/test_global_paper_directory_api.py tests/test_paper_profile_api.py tests/test_pages_api_hardening.py -q`: `15 passed`.
- `git diff --check`: pass.
- Diff-scoped security scan: no findings.
- Changed-route write scan: no `db.add`, `db.commit`, `INSERT`, `UPDATE`, or `DELETE` markers in the edited read routes.
- Independent reviewers: local Ollama/Qwen reviewer passed with no security concerns or logic errors; delayed background reviewer also passed, with non-blocking suggestions only. The inline `hero_facts[].source` coverage suggestion was addressed in this test file.

The tests assert both fallback behavior and precedence preservation:

- When `page_citation_links` is empty, `/citations` falls back to claim/evidence rows.
- When `page_citation_links` has rows, `/citations` keeps materialized-link ordering/keys.
- When `fact_sources` and inline hero fact sources are empty, `/fact-sources` falls back to claim/evidence rows.
- When inline `hero_facts[].source` records exist and `fact_sources` is empty, `/fact-sources` returns the inline source records instead of falling through to claim/evidence fallback.
- When `fact_sources` has rows, `/fact-sources` keeps materialized table rows.

The fallback tests also assert that the read paths do not write materialized rows:

- `page_citation_links` count remains `0`.
- `fact_sources` count remains `0`.

## Expected effect after deploy/restart

After this local branch is deployed and the API service is restarted, page 58 should no longer show empty source surfaces merely because materialized source tables are empty:

- `/api/pages/galaxy-evolution-v2/citations` should return claim/evidence-derived citations if `page_citation_links` is empty.
- `/api/pages/galaxy-evolution-v2/fact-sources` should return claim/evidence-derived source records if `fact_sources` and inline hero fact sources are empty.

## Side-effect ledger

- Production DB writes: `0`
- Claim creations: `0`
- Validator table writes: `0`
- Promoter runs: `0`
- Migrations: `0`
- Service restarts: `0`
- Deploys: `0`
- `coverage_ready` changes: `0`
- `promotion_eligible` changes: `0`
- `arxiv_papers.related_pages` mutations: `0`
- OpenClaw gateway use: `false`

## Remaining gated step

This branch still needs normal deploy/restart approval before the live `nebulamind.net` API reflects the local code fix. Promotion remains blocked until the live source-surface probes are green after deploy and the separate promotion gates are explicitly cleared.
