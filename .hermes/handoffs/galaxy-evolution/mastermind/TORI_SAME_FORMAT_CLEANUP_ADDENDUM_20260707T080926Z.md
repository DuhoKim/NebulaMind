# Tori same-format cleanup addendum

Marker: `TORI_SAME_FORMAT_CLEANUP_ADDENDUM_20260707T080926Z`
Parent roll-up: `HWAO_AUTONOMOUS_SAME_FORMAT_REPAIR_FINAL_20260707T074231Z`
Written: 2026-07-07T08:09:26Z (2026-07-07 17:09:26 KST)
Status: PASS

## User prompt interpreted

User said: “and?” after the PASS_WITH_NOTES roll-up. I interpreted this as: do not stop with carried-forward notes when they are safe docs/static cleanup items; clear them inside the existing no-apply boundary.

## Changes made

1. Cleared N1 for M2.
   - File: `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/same-format-rebuild/page-content-20260707T064500Z.md`
   - Removed only the trailing non-rendering HTML comment ledger beginning with `HWAO_SAME_FORMAT_REBUILD_PACKET_20260707T064500Z` / `Unresolved citation ledger`.
   - Article prose, headings, claim markers, cite-unmatched markers, and source-first wording were not changed.

2. Cleared real N2 layout delta for M2.
   - File: `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/same-format-rebuild/wiki-format-preview-20260707T064500Z.html`
   - Changed article shell grid from `minmax(0, 1fr) 17rem` / `gap: 1.25rem` to canonical `minmax(0, 56rem) 240px` / `gap: 2rem`.
   - No article body, marker rendering, controls, History/Sources treatment, or old page artifact was changed.

3. Rechecked M3 N2 note.
   - M3 article grid already uses canonical `grid-template-columns: minmax(0, 56rem) 240px; gap: 2rem;`.
   - The earlier “first grid-template is repeat(3, …)” note referred to unrelated `.method-links` chrome, not the article grid. No M3 patch needed.

## Verification after cleanup

Disk verification after patch:

| Check | M1 | M2 | M3 |
|---|---:|---:|---:|
| Markdown H2 order exact | PASS | PASS | PASS |
| Raw preview `<h2` count | 9 | 9 | 9 |
| Reader control present | PASS | PASS | PASS |
| Evidence control present | PASS | PASS | PASS |
| Live History/Sources routes | 0 | 0 | 0 |
| Claim open/close match | PASS | PASS | PASS |
| Claim profile | 30 claims | 6 claims `{2942–2947}` | 0 claims |
| Numeric cite markers | 0 | 0 | 0 |
| Cite-unmatched markers | 0 | 7 | 0 |
| Old wrong-format page preserved | PASS | PASS | PASS |
| M2 trailing comment ledger present | — | NO | — |
| M2 article grid canonical | — | PASS | — |
| M3 article grid canonical | — | — | PASS |

## Remaining gates

Still closed and not touched: live wiki publish, `/api/pages`, `page_versions`, DB/SQL/trust recompute, deploy/restart, git, cockpit/global/shared-parent updates, Method3 P3 binding, cloud/GCP/Gemini API/billing/OAuth/token changes, browser automation, cron.

## Result

PASS: carried-forward docs/static notes N1 and the real article-grid part of N2 are cleared. No live/public mutation occurred.
