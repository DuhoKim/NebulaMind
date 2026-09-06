# TRACK 4 — reconciliation of the failed aggregate suite log with the passing receipt (codex note 2026-09-06T14:55:31Z) — 2026-09-06 23:56:27 KST

## 1. The failed log, preserved verbatim
Copied as `_tmp_v24_all_suites_aggregate_FAILED_PRESERVED.txt` (SHA-256 90b8abebbb9cd5a7…). Its last block: 12 suites OK, then `track4/test_track4_fail_first`: Ran 7, FAILED (errors=2) — `test_M3_residual_stated_exactly`, `test_M6_text_sweep`. The aggregate log is NOT all-green and is not called so anywhere; the V24 text's '107 tests' count was taken from the per-suite `Ran` lines (107 executed), not from a claim that every result was OK.

## 2. Cause, exact
The aggregate runner was a shell function `run <dir> <module> <interpreter> <extra>` that executed `env $extra PYTHONDONTWRITEBYTECODE=1 PYTHONPATH=... <interpreter> -W error::ResourceWarning -m unittest <module>`. For track 4 the fourth argument was the single string `RULE_TEXT=<path> DESIGN_TEXT=<path>` (passed quoted), so `env` received ONE assignment whose value contained a space and `DESIGN_TEXT` was never set; both text tests read `os.environ["DESIGN_TEXT"]` and raised KeyError → ERROR. Codex's guess (missing exports) is confirmed: an environment-quoting defect of the runner, not of the tests or the candidate.

## 3. The correcting run — same final bytes, explicit environment, executed now
```
candidate: f3987cbe0d31b7c5eb5a72c7018c624175d60cd8b4c3e374335cb6f19c3d2992  OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V24_20260906.md
design:    b7c4fa6dd0845ff46e44ed01a7607b73d70c7cd815576e3f32f18eefb6f5917a  TRACK2_PROVENANCE_DESIGNS_UNADOPTED_20260906.md
tests:     f101e956ab92ae2853bb7545cd6f432d1d1b3b057663e609e9ec94cfbfacfb7b  _optionA_dev/track4/test_track4_fail_first.py
module:    ddcfa7227c3510a2e8cd1b039d7e9f932e2ff2a093d4a6d9fce9c769c02c8c7a  _optionA_dev/track2/provenance_designs_v4.py
command:   cd _optionA_dev/track4 && RULE_TEXT="/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_stage2_image_analysis_20260901/OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V24_20260906.md" DESIGN_TEXT="/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_stage2_image_analysis_20260901/TRACK2_PROVENANCE_DESIGNS_UNADOPTED_20260906.md" PYTHONDONTWRITEBYTECODE=1 PYTHONPATH="/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_stage2_image_analysis_20260901/_optionA_dev/_venv_bls/lib/python3.9/site-packages" /usr/bin/python3 -W error::ResourceWarning -m unittest -v test_track4_fail_first
time:      2026-09-06T14:56:28Z
test_M1_one_push_per_commit_validates_and_ordering_is_checked (test_track4_fail_first.M1_PerEntryAcknowledgment) ... ok
test_M1_single_entry_commits_pushed_together_are_refused (test_track4_fail_first.M1_PerEntryAcknowledgment) ... ok
test_M2_collector_cli_publishes_outer_error_and_reconciles_on_restart (test_track4_fail_first.M2_ProducerRecovery) ... ok
test_M2_publish_entry_retries_an_existing_pending_commit (test_track4_fail_first.M2_ProducerRecovery) ... ok
test_M2_reconcile_before_operating_and_error_entries_published (test_track4_fail_first.M2_ProducerRecovery) ... ok
test_M3_residual_stated_exactly (test_track4_fail_first.M3_M6_Text) ... ok
test_M6_text_sweep (test_track4_fail_first.M3_M6_Text) ... ok
Ran 7 tests in 4.945s
OK
exit status: 
```
The digests above equal those of the earlier 7/7 receipt run 2 in `TRACK4_FAIL_FIRST_RECEIPT_20260906.md` (test file f101e956…; the V24 text and modules unchanged since), so that receipt is the correcting run for the same bytes; this file links them. The review sandbox (`/Users/duhokim/.claude/jobs/5b2f0371/tmp/selrule_v24_gate__5z2g1c8/_stage2_image_analysis_20260901`) was NOT touched: this file and the preserved log are lane-only additions.

## 4. Cause PROVEN by three executions (Blanc's order: with and without) — 23:58:54 KST
```
(a) EXACTLY the aggregate runner's form — both variables passed to env as ONE argument:
    raise KeyError(key) from None
KeyError: 'DESIGN_TEXT'
    raise KeyError(key) from None
KeyError: 'DESIGN_TEXT'
Ran 2 tests in 0.001s
FAILED (errors=2)
    exit status: 1
(b) WITHOUT the variables:
    raise KeyError(key) from None
KeyError: 'RULE_TEXT'
    raise KeyError(key) from None
KeyError: 'DESIGN_TEXT'
Ran 2 tests in 0.003s
FAILED (errors=2)
    exit status: 1
(c) WITH both variables set separately:
Ran 2 tests in 0.001s
OK
    exit status: 0
(d) the full track-4 suite WITH both variables (section 3 above printed an empty exit status: zsh's array is `pipestatus`, not PIPESTATUS — my receipt bug, corrected here):
Ran 7 tests in 4.899s
OK
    exit status: 0
```
What actually happened: the twelve suites passed; the track-4 suite was invoked by the aggregate runner with a malformed environment (one `env` argument carrying two assignments), so `DESIGN_TEXT` was unset and the two text tests raised KeyError (errors=2); the same tests on the same bytes pass with the variables set (c, d) and fail identically without them (a, b). The failing log is preserved unmodified; the candidate, tests and the active review sandbox were not edited.
