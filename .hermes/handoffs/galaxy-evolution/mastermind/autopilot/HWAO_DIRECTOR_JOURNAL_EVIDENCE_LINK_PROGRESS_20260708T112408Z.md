# Hwao-director progress — journal evidence-link pass supervision

Marker: AUTOPILOT_RESEARCH_TOPICS_JOURNAL_EVIDENCE_LINK_PASS_20260708T112408Z
Role: Hwao-director — supervisor + final rollup (method teams revise; NOT director solo-author). Snapshot 2026-07-08T11:25Z (20:25 KST).

## User correction (treat prior specificity pass as insufficient)
Public research-topic pages still read too casual/general and the `What studies already show` sections lack **visible evidence links**. Revise the three `research-topics-from-wiki-20260708T090359Z` pages to **journal-prospectus quality**: every proposal's prior-evidence section must carry visible, resolving evidence links **inside that section** (not just a trailing provenance line).

## Minimum per-card structure (verify each)
`Research question` (explicit/testable) · `Prior evidence and constraints` (**linked** evidence statements — visible links required) · `Remaining uncertainty` (exact gap) · `Data and measurement plan` (named data → measurement; population/denominator/control) · `Analysis and decision criterion` (test + support/refute rule) · `Limitations` · `Provenance` (IDs here, but does NOT replace the visible links above).

## Link rules (no-invent — critical)
Links ONLY to existing local artifacts or arXiv already in local ledgers:
- M1: `…/packet-gated-…/prose-evidence-trust-deepening-…/` claim anchors `#claim-2931/2929/2946` + coverage-map evidence URLs (do NOT turn unbound-local into product evidence).
- M2: `…/source-first-…/p1-source-position-ledger.{jsonl,html}`, `p2-claim-status-ledger.{jsonl,html}`, `evidence-trust-deepening-map-…json`; arXiv IDs from the ledgers for rows 28141/28066/28075/28158/28095/28131/28108/28062/28074/28091/28155/28060/28069/28073/28088.
- M3: `…/debate-map-…/evidence-trust-rebuild/evidence-basis-20260708T014205Z.md#s…` anchors + coverage-map; debate-map axis links; existing bibcode provenance only (no invented external URLs).
Any prior-evidence statement that cannot be linked → narrow / delete / mark as an **unlinked local-method limitation** (not presented as prior evidence). No invented papers/DOI/ADS/IDs/numeric results/links.

## Verification before PASS (director independently checks)
- proposal count 5–8, matches JSON/manifest.
- every card's prior-evidence section has ≥1 visible link **in that section**.
- **all visible prior-evidence links RESOLVE** — local static files/anchors exist, or external arXiv returns HTTP 200.
- no unsupported prior-evidence sentence left unlinked/unlabeled.
- static-safe (0 script/fetch/XHR/WS/handlers/form); product claim/cite comments 0/0.
- formal tone (no casual/blog phrasing; no vague "studies show" without a link).
- no invented data.

## Plan
Method teams revise + write `method<N>/autopilot/RESEARCH_TOPICS_JOURNAL_EVIDENCE_LINK_PASS_M<N>_20260708T112408Z.md`. Director independently verifies (incl. link resolution) + writes final rollup. Public pages (currently the specificity version, mirrored) are **stale until re-verified + re-mirrored** by Tori (post-verification only; method lanes must not mirror).

## Boundaries (CLOSED)
Overwrite ONLY within the 3 `research-topics-from-wiki-20260708T090359Z/` dirs + `.hermes` receipts. NO method-lane live-root writes (Tori only, post-verification); NO restart/deploy, DB/SQL/API/`/api/pages`/page_versions/publish/trust-recompute, git, cockpit/global/shared-parent, cloud/OAuth/secrets, browser, cron, M3 P3. No director keystrokes; no solo authoring.

AUTOPILOT_RESEARCH_TOPICS_JOURNAL_EVIDENCE_LINK_PASS_20260708T112408Z
