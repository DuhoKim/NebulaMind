# 2929 source-position / human-adjudication queue

Status: `DOCS_ONLY_SIX_VOTE_DEPENDENT_ROWS_REVIEWED_NO_ACTIVE_EXECUTION_PHRASE`  
Helper QA patch UTC: `2026-07-05T02:02:00Z`  
Six vote-dependent source-position edit UTC: `2026-07-05T03:37:35Z`  

Plain English: this is a 36-ticket checklist for humans/operators. Six vote-dependent rows now have docs-only source-position/human decisions; the other 30 remain pending. No rows are moved by this artifact.

Hard locks: no SQL, no DB writes, no trust recompute, no prose/wiki publish, no runtime deploy/restart, no git write/push/merge, active phrase `NO ACTIVE EXECUTION PHRASE`. SQL remains locked until all 36 rows have completed human/source decisions and a new operator-approved packet exists.

## Helper QA fixes applied

- Active queue is held-row-only: `36` rows; the four already-remapped rows are excluded from the active queue.
- Added exact decision slots: `decision_enum`, `decision_owner`, `decision_timestamp_utc`, `decision_reason`, `review_status`, confidence, second-review question.
- Added source-position slots: exact quote/span, PDF page, section, locator, matched terms, role, stance, limitation, source-position note.
- Added candidate-vs-accepted-decision separation: candidate targets stay hypotheses until `accepted_for_docs_source_position` is filled.
- Added full vote dependency rows and explicit vote-action slots for six human-voted rows.
- Added source-group duplicate controls and normalized display titles, including `arXiv:arXiv:0901.1880` display normalization for `28110` and `28131`.
- Kinetic/radio route is first-class for candidate rows instead of buried in prose.

## Counts

- queue tickets: `36`
- decision counts: `{'leave_archival': 1, 'pending': 30, 'relink': 3, 'route_kinetic_radio': 2}`
- source-position status counts: `{'abstract_only_verified': 6, 'pending': 30}`
- vote-dependent rows: `28060, 28091, 28095, 28111, 28141, 28155` — reviewed docs-only in this pass
- kinetic/radio route candidates: `28062, 28076, 28095, 28108, 28111, 28127, 28131, 28139, 28158`
- metadata normalization rows: `28110, 28131`

## Required decision enum

- `pending`
- `relink`
- `copy_source_fill`
- `retire_reject`
- `leave_archival`
- `route_kinetic_radio`

## Queue table

| evidence | decision | review | source-position | vote action | candidates | source group | normalized title | first human step |
|---:|---|---|---|---|---|---|---|---|
| 28060 | leave_archival | reviewed | abstract_only_verified | leave_archival (1) | 2942 | arxiv:2604.15438 / same: 28074,28091,28155 | Surveying the Whirlpool at Arcseconds with NOEMA (SWAN). IV. Extent of active ga | Honors human vote 5048 (value -1, confirm_weakening) by classifying this row limitation_or_caution and leave_archival on the retired 2929 pa |
| 28062 | pending | pending | pending | pending (0) | 2943,2942,2947 | arxiv:2508.06707 / same: 28089,28144 | arXiv:2508.06707 | Open source; capture exact quote/page/section; then decide. |
| 28066 | pending | pending | pending | pending (0) | 2945,2943 | arxiv:2512.05584 / same: 28069,28070,28073 | arXiv:2512.05584 | Open source; capture exact quote/page/section; then decide. |
| 28069 | pending | pending | pending | pending (0) | 2944 | arxiv:2512.05584 / same: 28066,28070,28073 | arXiv:2512.05584 | Open source; capture exact quote/page/section; then decide. |
| 28070 | pending | pending | pending | pending (0) | 2944 | arxiv:2512.05584 / same: 28066,28069,28073 | arXiv:2512.05584 | Open source; capture exact quote/page/section; then decide. |
| 28073 | pending | pending | pending | pending (0) | 2944 | arxiv:2512.05584 / same: 28066,28069,28070 | arXiv:2512.05584 | Open source; capture exact quote/page/section; then decide. |
| 28074 | pending | pending | pending | pending (0) | 2942 | arxiv:2604.15438 / same: 28060,28091,28155 | Surveying the Whirlpool at Arcseconds with NOEMA (SWAN). IV. Extent of active ga | Open source; capture exact quote/page/section; then decide. |
| 28075 | pending | pending | pending | pending (0) | 2945 | arxiv:0901.1880 / same: 28110,28131 | arXiv:0901.1880 | Open source; capture exact quote/page/section; then decide. |
| 28076 | pending | pending | pending | pending (0) | 2944,2942,2947 | arxiv:2512.21927 / same: 28080,28083,28084 | A large, long-lived, slowly-expanding superbubble across the Perseus Arm | Open source; capture exact quote/page/section; then decide. |
| 28080 | pending | pending | pending | pending (0) | 2944 | arxiv:2512.21927 / same: 28076,28083,28084 | A large, long-lived, slowly-expanding superbubble across the Perseus Arm | Open source; capture exact quote/page/section; then decide. |
| 28082 | pending | pending | pending | pending (0) | 2944 | arxiv:1507.06366 / same: none | arXiv:1507.06366 | Open source; capture exact quote/page/section; then decide. |
| 28083 | pending | pending | pending | pending (0) | 2944 | arxiv:2512.21927 / same: 28076,28080,28084 | A large, long-lived, slowly-expanding superbubble across the Perseus Arm | Open source; capture exact quote/page/section; then decide. |
| 28084 | pending | pending | pending | pending (0) | 2944 | arxiv:2512.21927 / same: 28076,28080,28083 | A large, long-lived, slowly-expanding superbubble across the Perseus Arm | Open source; capture exact quote/page/section; then decide. |
| 28087 | pending | pending | pending | pending (0) | 2942 | arxiv:2009.11175 / same: 28095,28108,28111,28133 | arXiv:2009.11175 | Open source; capture exact quote/page/section; then decide. |
| 28088 | pending | pending | pending | pending (0) | 2944 | arxiv:2605.03008 / same: none | Environmental Quenching of High-Redshift Galaxies: Interpreting JWST Observation | Open source; capture exact quote/page/section; then decide. |
| 28089 | pending | pending | pending | pending (0) | 2946,2942 | arxiv:2508.06707 / same: 28062,28144 | arXiv:2508.06707 | Open source; capture exact quote/page/section; then decide. |
| 28091 | relink | reviewed | abstract_only_verified | relink (1) | 2943,2942 | arxiv:2604.15438 / same: 28060,28074,28155 | Surveying the Whirlpool at Arcseconds with NOEMA (SWAN). IV. Extent of active ga | Honors human vote 5049 (value +1, confirm_support) by relinking this row as support to successor 2943; the +1 gold judgment is preserved and |
| 28095 | route_kinetic_radio | reviewed | abstract_only_verified | route_kinetic_radio (1) | 2943,2946,2947 | arxiv:2009.11175 / same: 28087,28108,28111,28133 | arXiv:2009.11175 | Honors human vote 5050 (value +1, confirm_support) by routing this row to kinetic/radio successor 2947 (route_kinetic_radio) and relinking a |
| 28108 | pending | pending | pending | pending (0) | 2942,2946,2947 | arxiv:2009.11175 / same: 28087,28095,28111,28133 | arXiv:2009.11175 | Open source; capture exact quote/page/section; then decide. |
| 28110 | pending | pending | pending | pending (0) | 2945 | arxiv:0901.1880 / same: 28075,28131 | arXiv:0901.1880 | Open source; capture exact quote/page/section; then decide. |
| 28111 | route_kinetic_radio | reviewed | abstract_only_verified | route_kinetic_radio (1) | 2946,2947 | arxiv:2009.11175 / same: 28087,28095,28108,28133 | arXiv:2009.11175 | Honors human vote 5051 (value +1, confirm_support) by routing this row to kinetic/radio successor 2947 (route_kinetic_radio) and relinking a |
| 28114 | pending | pending | pending | pending (0) | 2944 | arxiv:1203.2926 / same: 28118 | arXiv:1203.2926 | Open source; capture exact quote/page/section; then decide. |
| 28118 | pending | pending | pending | pending (0) | 2944 | arxiv:1203.2926 / same: 28114 | arXiv:1203.2926 | Open source; capture exact quote/page/section; then decide. |
| 28123 | pending | pending | pending | pending (0) | 2946,2942 | arxiv:2403.17145 / same: 28127,28139,28143,28151,28158 | arXiv:2403.17145 | Open source; capture exact quote/page/section; then decide. |
| 28127 | pending | pending | pending | pending (0) | 2946,2945,2947 | arxiv:2403.17145 / same: 28123,28139,28143,28151,28158 | arXiv:2403.17145 | Open source; capture exact quote/page/section; then decide. |
| 28131 | pending | pending | pending | pending (0) | 2946,2947 | arxiv:0901.1880 / same: 28075,28110 | arXiv:0901.1880 | Open source; capture exact quote/page/section; then decide. |
| 28133 | pending | pending | pending | pending (0) | 2943 | arxiv:2009.11175 / same: 28087,28095,28108,28111 | arXiv:2009.11175 | Open source; capture exact quote/page/section; then decide. |
| 28139 | pending | pending | pending | pending (0) | 2946,2947 | arxiv:2403.17145 / same: 28123,28127,28143,28151,28158 | arXiv:2403.17145 | Open source; capture exact quote/page/section; then decide. |
| 28140 | pending | pending | pending | pending (0) | 2943,2946 | arxiv:2111.01801 / same: none | arXiv:2111.01801 | Open source; capture exact quote/page/section; then decide. |
| 28141 | relink | reviewed | abstract_only_verified | relink (1) | 2943 | arxiv:1706.08987 / same: none | arXiv:1706.08987 | Honors human vote 5052 (value +1, confirm_support) by relinking this row as support to successor 2943; the +1 gold judgment is preserved on  |
| 28143 | pending | pending | pending | pending (0) | 2946,2943 | arxiv:2403.17145 / same: 28123,28127,28139,28151,28158 | arXiv:2403.17145 | Open source; capture exact quote/page/section; then decide. |
| 28144 | pending | pending | pending | pending (0) | 2943 | arxiv:2508.06707 / same: 28062,28089 | arXiv:2508.06707 | Open source; capture exact quote/page/section; then decide. |
| 28148 | pending | pending | pending | pending (0) | 2943,2942 | arxiv:2604.22922 / same: none | Discovery of ultra-fast outflows with v$_{\rm out}>0.3 \rm c$ in local bright ac | Open source; capture exact quote/page/section; then decide. |
| 28151 | pending | pending | pending | pending (0) | 2946 | arxiv:2403.17145 / same: 28123,28127,28139,28143,28158 | arXiv:2403.17145 | Open source; capture exact quote/page/section; then decide. |
| 28155 | relink | reviewed | abstract_only_verified | relink (1) | 2942,2946 | arxiv:2604.15438 / same: 28060,28074,28091 | Surveying the Whirlpool at Arcseconds with NOEMA (SWAN). IV. Extent of active ga | Honors human vote 5053 (value +1, confirm_support) by relinking this row as support to successor 2942; the +1 gold judgment is preserved on  |
| 28158 | pending | pending | pending | pending (0) | 2946,2947 | arxiv:2403.17145 / same: 28123,28127,28139,28143,28151 | arXiv:2403.17145 | Open source; capture exact quote/page/section; then decide. |
