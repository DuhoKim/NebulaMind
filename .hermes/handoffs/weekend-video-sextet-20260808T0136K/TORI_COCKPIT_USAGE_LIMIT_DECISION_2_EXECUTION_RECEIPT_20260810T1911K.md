# Decision 2 execution receipt — stale provider cards remain visible

- Marker: `TORI_COCKPIT_USAGE_LIMIT_DECISION_2_EXECUTION_RECEIPT_20260810T1911K`
- Authority: Duho verbatim `approve both`, interpreted by Hwao as Decision 2 source/test apply approval and wallet-packet authoring approval only
- Governing preflight: `TORI_COCKPIT_USAGE_LIMIT_DECISION_2_STALE_VISIBILITY_EXACT_DIFF_PREFLIGHT_20260810T1807K.md`
- State: `VERIFIED_IN_WORKTREE_NOT_ACTIVATED`
- User-acceptance label: **not asserted**

## Verdict

`PASS_RED_GREEN_DECISION_2_SOURCE_SCOPE`

The private renderer source now fails closed without hiding provider cards: a stale wrapper produces visible historical/unknown provider cards, strips current percentages, preserves old values only as explicit history, and leaves the fresh branch unchanged.

## Bound scope

Changed:

- `tools/render_ge_autopilot_dashboard_v2.py`
- new focused test: `tools/tests/test_private_usage_stale_visibility.py`

Not changed:

- `tools/live_provider_usage_monitor.py`
- `tools/moonshot_balance_usage.py`
- generated private/public HTML or JSON by Tori
- wallet-card canonicalisation
- live headline population
- provider/account/browser sources

The renderer already had unrelated pre-existing worktree edits outside this slice. The Decision 2 target region matched `HEAD` before this apply; Tori changed only the historicalisation helper and stale branch described below.

## RED — observed before production edit

Command:

`PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -p no:cacheprovider tools/tests/test_private_usage_stale_visibility.py -q`

Result: expected RED, exit 1.

- 1 failed, 1 passed
- failing assertion: stale snapshot returned only the three private Kimi/Flow/YouTube cards instead of six provider cards plus those three
- failure was the intended missing behavior, not an import, fixture, syntax, provider, or network error

The precondition therefore established the exact old defect. No unexpected RED failure occurred.

## GREEN — minimal source behavior

Added `historicalize_usage_card()` in `tools/render_ge_autopilot_dashboard_v2.py:1138-1215` and changed only the stale flow in `build_public_usage_snapshot()` at `tools/render_ge_autopilot_dashboard_v2.py:1495-1599`.

When the wrapper age exceeds one hour:

- all six retained provider cards remain in `cards`;
- private Kimi, Flow, and YouTube remain unchanged, for nine records total;
- old provider values become `STALE HISTORICAL OBSERVATION` or `UNAVAILABLE / UNKNOWN`;
- top-level and sub-gauge `percent` values become `None`;
- old labels move to `historical_value_label` and `Last observed — ...` copy;
- source timestamps/ages are retained without advancing observation time;
- `cache_state` becomes `stale-source-visible`;
- monitor status becomes `STALE_PROVIDER_FEED_CARDS_VISIBLE`;
- exact current-percent source count becomes zero;
- the hidden-card count is replaced by visible-stale/unknown/planning counts;
- fresh-branch behavior remains unchanged.

## GREEN verification

Focused command:

`PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -p no:cacheprovider tools/tests/test_private_usage_stale_visibility.py -q`

Result: 2 passed in 0.02s.

Focused plus adjacent command:

`PYTHONDONTWRITEBYTECODE=1 python3 -m pytest -p no:cacheprovider tools/tests/test_private_usage_stale_visibility.py tools/tests/test_provider_usage_quota_parsing.py -q`

Result: 9 passed in 0.23s.

A pre-existing Python/LibreSSL `urllib3` compatibility warning was emitted; it did not affect collection or assertions and no dependency/config change was authorized.

Static checks:

- Python AST parse: PASS for source and test
- `git diff --check`: PASS
- source SHA-256 before: `a246d502b0af1a494460b10a43bb4aa9692f3cf2dba855ecd2c9a6f24bceead4`
- source SHA-256 after: `1c46d1890c2559b6ffcc3696f5961d3ef3a05031bba3f37f3d1503c598053168`
- focused-test SHA-256: `12d03b309b0b929d23edb230dc2de476c544afc66651b96da5747150a1e52b44`

## Activation boundary

The running private renderer remains PID `31235`, started 2026-08-08 14:09:54 KST, so it still has the pre-change module loaded.

No restart was performed. Restarting this process can execute the unchanged private `kimi_direct_balance_card()` path, which may attempt the Moonshot endpoint when an in-memory credential is present. The unchanged gate permits no provider call beyond the approved monitor, and the wallet packet—not Decision 2—owns that duplicate private path. Activating by restart before resolving or explicitly containing that call path would silently widen scope.

Therefore the source/test apply is complete and verified, but live activation remains held. A later activation order must either:

1. explicitly authorize the existing private Moonshot read during restart, or
2. first apply an independently approved wallet-canonicalisation change that removes the duplicate private live-read path.

## Safety ledger

- provider/account/OAuth-page calls by Tori: 0
- browser captures: 0
- monitor restarts: 0
- renderer restarts: 0
- generated/public cockpit writes by Tori: 0
- deploys: 0
- Git commit/push/merge: 0
- cron/config/secret actions: 0
- DB/wiki/product mutations: 0
