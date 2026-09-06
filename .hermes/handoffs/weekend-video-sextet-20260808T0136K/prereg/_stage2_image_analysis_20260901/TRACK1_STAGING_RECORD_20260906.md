# TRACK 1 — STAGED MECHANICAL REPAIRS (Blanc 20:45 KST; NOT GATED, NOT ADOPTED) — 2026-09-06 21:03 KST

Every repair below has a test that FAILED against byte-copies of the V21 modules before the repair and passes after: `TRACK1_FAIL_FIRST_RECEIPT_20260906.md` (run 1: 9 FAIL + 1 ERROR of 10; run 2: 10 OK). V15, V20 and V21 bytes are untouched; each successor sits beside its predecessor.

| codex V21 finding | repair (staged file) | fail-first test |
|---|---|---|
| C6 signature compared as hex strings | `beacon_record_drand_v22.py`: equality on DECODED signature bytes; seed = lowercase hex SHA-256 of those bytes | test_C6 (uppercase hex live signature → same value) |
| C5 6441904 not excluded | `EXCLUDED_ROUNDS = (6440756, 6441904, 6441924)` | test_C5 (collect and verdict for 6441904 refused by name) |
| C7/C8/C10 stale operative text | `OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V22_20260906.md` (digest `75eceb104b75ac614a0b3b0f1e4ee758913b0fbfdd6ae54848de49bce521e90a`): byte-equality clause and old token removed, V22 filename = builder/driver glob, seed stated as SHA-256 of the decoded signature, old fixture names removed | test_C7_C8_C10 (reads the rule text; FAILS on V21 text, passes on V22) |
| C4 "every path" false | builder v22: args refusal disclosed; the error boundary wraps `build()`; collector v22: argparse failures reach the sidecar (`--log` pre-scanned; module sidecar when absent) | test_C4a/b/c |
| C2 W4 not in the driver | driver v6: `Protocol.approval_glob`, exactly one record path in all history → `APPROVAL-NOT-FIRST`; fixture v6: ONE approval commit per repository | test_C2 |
| C3 (mechanical part) CLOSED not terminal; genesis existence-then-lock | `history_v2.py`: exclusive creation; `first_accept` reports a closure as a conflict; driver v6 `COLLECTION-CLOSED` | test_C3 ×2 |
| C9 sentinel journal incomplete | driver v6: refusal cause required; render-end required; count equal | test_C9 |
| C11 inherited: lists on trust | driver v6 `Protocol.verify_split` (UNADOPTED, default off): recompute the split from catalogue bytes; e2e test shows the default driver accepting a swapped list and verify_split refusing it | in `test_run_configurations_v6` (not fail-first: a new, off-by-default check) |
| E1 wrong test count | annotated in V22 as a FACTUAL ERRATUM of the signed V15 (not a design change); the signed source untouched | test_C7 family (text) |

NOT closed by track 1 (open boundaries, disclosed in V22 §3c; track 2 designs UNADOPTED): C1 forged-but-consistent event; C3 history rebuilt before the first freeze / suffix deletion that keeps an accept. `V22_CANDIDATE_ATTACK_INSPECTION_20260906.md` shows both still ACCEPTED by the candidate and REFUSED by the track-2 designs.

Suites on the candidate, warning-strict: 22 + 17 + 4 + 3 + 8 + 4 + 7 + 4 + 10 + 2 = 81 tests, all OK, no ResourceWarning (one inherited RuntimeWarning at `fourier_chirality.py:87`). Exhibit v22 twice: 2160fa75… (identical to v21's — the property exhibit's inputs do not exercise the case-folding path; test_C6 does).

Digests: see `OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V22_20260906.md` E3/§3b/§3c (every staged file pinned there). Diff `V21_TO_V22.diff` (46 lines).

## Addendum 21:09 KST — track 2 revised after codex's probe (21:00) and Blanc's orders (21:02, 21:04)
The history design's v1 validator trusted local HEAD (gap reproduced in `TRACK2_FAIL_FIRST_RECEIPT_20260906.md` run 1b); `provenance_designs_v2.py` asks the remote (`ls-remote`), enforces the push-acknowledgement boundary, and the event retrieval / pagination / error handling / expired-receipt paths are BUILT with fail-first tests (8 OK). Cost line corrected (one push per attempt, not per freeze). The attack inspection now carries rows 9c–9h on v2. Suites on the candidate: 89 tests OK. V22 staged text re-pinned: `75eceb104b75ac614a0b3b0f1e4ee758913b0fbfdd6ae54848de49bce521e90a`.

## Addendum 21:23 KST — Blanc 21:14 / 21:16: the three states on the production call path; the two false assumptions removed
Driver v6 gains `Protocol.provenance_mode` (default `offline`; `composed` = the track-2 v2 helpers inside `load_identity`), exhibited in `test_composed_mode_on_the_production_call_path` and attack rows 10a–10c. The origin label is the lane's proposal (`ops-witness`), not a user decision; the recommended default is the delegated witness workflow with no per-receipt human confirmation; the one Duho-only step (a second GitHub identity or custodian key) is named in `QUESTIONS_FOR_DUHO_TRACK2_ORIGIN_AND_RECEIPTS_20260906.md`. The track-2 receipt's run 1 is relabelled MISSING-INTERFACE; run 1b establishes the old behaviour. Suites: 90 tests OK. V22 staged text re-pinned: `75eceb104b75ac614a0b3b0f1e4ee758913b0fbfdd6ae54848de49bce521e90a`.
