# Kun wiki-page reproducibility/static consistency

Packet marker: HWAO_TEAMS_HOLD_REACTIVATION_PACKET_20260707T061500Z

Role: Kun / reproducibility and static-artifact consistency.

Overall status: ISSUES, no ROLE_TABLE_BLOCKER.

## Scope

Read-only reconciliation of each static `wiki-page.html` against its source draft, manifest, and verdict/receipt anchor. No page, draft, manifest, method-tree, or shared file was rebuilt or edited.

## Method1 — packet-gated reconciliation

Verdict: ISSUES.

Reconciled:
- Source draft exists: `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/pgr-same-format-draft-20260707T005045Z.md`.
- HTML page exists: `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/wiki-page.html`.
- Manifest status is consistent: top-level, method, and draft-prepared statuses read `DRAFT_PREPARED_STATIC_NOT_PUBLISHED`.
- Draft matches A1-A5 assertions: title `# Galaxy Evolution`; 9 binding H2s in order; 30 open/30 close claim markers; exact chip set `{2905-2923, 2925, 2926, 2929-2936, 2946}`; 0 cite markers; `2924` absent and `2946` present.
- Article body inside `wiki-page.html` renders the same 9 article H2s and the same 30 rendered claim IDs.

Issue:
- Strict whole-file HTML reconciliation does not have "same title / exactly 9 H2s" as the source draft. The raw page is an evaluation wrapper: it has an outer H1 `Galaxy Evolution — Method 1 wiki page` plus article H1 `Galaxy Evolution`, and 14 raw H2s because provenance/safety panels add 5 non-article H2s. This is not a content drift in the article body, but it is a static page-vs-draft wrapper drift relative to the packet's simple invariant.

## Method2 — source-first adjudication

Verdict: ISSUES.

Reconciled:
- Source draft exists: `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/galaxy-evolution-same-format-draft.md`.
- HTML page exists: `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/wiki-page.html`.
- Manifest status is consistent: top-level and method statuses read `DRAFT_PREPARED_STATIC_NOT_PUBLISHED`.
- Draft matches the v2 verdict and Tori v2 receipt: title `# Galaxy Evolution`; 9 binding H2s in order; 6 claim chips `{2942, 2943, 2944, 2945, 2946, 2947}`; 7 cite markers; 22 distinct evidence IDs `{28060, 28062, 28066, 28069, 28073, 28074, 28075, 28087, 28088, 28089, 28091, 28095, 28108, 28123, 28131, 28140, 28141, 28144, 28148, 28151, 28155, 28158}`.
- Article body inside `wiki-page.html` renders the same 9 article H2s, 6 claim IDs, and the same 22 article evidence IDs. The rejected/excluded IDs appear only in the evaluation panel, matching the verdict's statement that the page preserves held-out rows while not using them in article support.

Issue:
- Strict whole-file HTML reconciliation does not have "same title / exactly 9 H2s" as the source draft. The raw page is an evaluation wrapper: it has an outer H1 `Galaxy Evolution — Source-first adjudication` plus article H1 `Galaxy Evolution`, and 12 raw H2s because provenance/exclusion/method panels add 3 non-article H2s. Article-body reconciliation is clean.

## Method3 — debate-map rebuild

Verdict: ISSUES.

Reconciled:
- Source draft exists: `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/m3-p2-same-format-draft-20260707T050500Z.md`.
- HTML page exists: `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/wiki-page.html`.
- Draft and HTML page match the Method3 P2 verdict: title `# Galaxy Evolution`; 9 binding H2s in order; 0 claim markers; 0 cite markers; HTML renders one H1 and 9 H2s.
- P2 verdict lineage is internally consistent with P1.5: P1.5 opened P2 with 17 roles and P2 verdict reports `PASS_WITH_ISSUES`, non-binding, P3 closed.

Issues:
- Manifest drift: `frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/manifest.json` still reports status `9-H2 confirmed — M3 P1.5 GO issued` at the top level and under `method.status`, rather than a P2 static-not-published / evaluation-ready status matching `HWAO_M3_P2_WIKI_PAGE_VERDICT_RERUN_20260707T050900Z.md`.
- Page status wording is semantically safe (`P2 same-format narrative draft`, no live-wiki publish, no claim/citation binding), but it does not contain the literal `DRAFT_PREPARED_STATIC_NOT_PUBLISHED` status expected by the reactivation packet.
- Carried Method3 P3-only provenance issues remain as verdict-recorded issues, not new drift: PROV-1 source-list completeness for claim `2133`, PROV-2 broken claim anchor for claim `2374`, PROV-3 v1709-body-only IDs `2915`, `2921`, `2913`, plus I2/I3 trace/PENDING_RECHECK prerequisites.

## Cross-method consistency summary

| Method | Page vs draft article body | Manifest/status | Verdict-count reproduction | Consistency verdict |
|---|---|---|---|---|
| M1 | PASS | PASS | PASS | ISSUES: wrapper H1/H2 extras |
| M2 | PASS | PASS | PASS | ISSUES: wrapper H1/H2 extras |
| M3 | PASS | ISSUES | PASS | ISSUES: stale manifest/status |

No page was unreconcilable to its source. No `ROLE_TABLE_BLOCKER` was required.

## Files read

- `.hermes/handoffs/galaxy-evolution/mastermind/KUN_WIKI_PAGE_REPRO_CONSISTENCY_BRIEF_20260707T061500Z.md`
- `.hermes/handoffs/galaxy-evolution/mastermind/HWAO_TEAMS_HOLD_REACTIVATION_PACKET_20260707T061500Z.md`
- Method1 page, draft, manifest, A1-A5 chain files.
- Method2 page, draft, manifest, v2 verdict, and Tori v2 receipt.
- Method3 page, draft, manifest, P2 verdict rerun, and P1.5 re-verdict.

## Safety ledger

No live wiki/page_versions publish; no DB/SQL/trust recompute; no deploy/restart; no git; no Gemini/GCP API/config/billing changes; no cloud account/OAuth/token/credits action; no browser automation; no cron; no route/config/cockpit/global mutation; no P3 claim/citation binding; no edits to page/draft/manifest/method-tree files. Only this expected mastermind report was written.
