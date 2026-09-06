# TEXT-TEST ATTRIBUTION — which document version each text test was WRITTEN AGAINST and RUN AGAINST (Blanc's order 01:05 KST; codex CODEX_V26_TEST_RECORD_SCOPE) — 2026-09-07 01:05 KST

The 15-suite aggregate log of the V26 candidate is PRESERVED unmodified as `_tmp_v26_all_suites_aggregate_PRESERVED.txt` (SHA-256 0bf47a9e81168aed…): 14 suites OK and `test_track5_fail_first` FAILED (1 failure: `test_N5_labels_and_sweep`, asserting the V25 self-label '3c. V25' against the V26 text). That log is the record of what happened when every text test was pointed at the V26 text. A later narrower run of track 5 against the V25 text (6 OK) does not replace it. Corrections here are lane-only; the active V26 review sandbox is untouched.

| test (file · case) | assertions WRITTEN AGAINST | RUN AGAINST in the aggregate | result | what the pass establishes |
|---|---|---|---|---|
| track1 · test_C7_C8_C10_rule_text_consistent | the V22 wording (no `REFUSE-LIVE-DIFFERS-BUT-VERIFIES`, no `APPROVAL_RECORD_SELRULE_V20_<date>`, builder glob prefix + `_<date>` present, no V20 byte-equality clause, 'SHA-256 of the DECODED signature bytes') | V26 text | OK | version-agnostic absences/presences: they hold in V26 |
| track3 · test_F_questions_text_states_30_days_and_option_B_not_implemented | the 09-06 questions file (no '90 days'; '30 days'; 'NOT IMPLEMENTED') | the current questions file (e676…→ now a73fcd59…) | OK | those three facts hold in the current file |
| track4 · test_M3_residual_stated_exactly | the V24 wording (no 'cannot hide a CLOSED witness state'; 'absence-based' present) in the rule text, the design doc, provenance_designs_v4 | V26 text, current design doc, v4 module | OK | holds in V26 (the covenant retains 'absence-based') |
| track4 · test_M6_text_sweep | the V24 wording (design-doc phrases absent; driver v8 without 'UNNAMED until Duho'; rule text names `build_corpus_identity_v24.py`, contains 'builder-control-refusal', not the V22 §9 header) | V26 text, current design doc, driver v8 | OK | the absences hold in V26; the presence of `build_corpus_identity_v24.py` is satisfied by V26's HISTORICAL mention of v24 — a weak assertion for V26, stated as such |
| track5 · test_N1_residual_is_the_covenant | the V25 wording ('between later publications', 'does not authenticate when') in the rule text, design doc, provenance_designs_v5 | V26 text (aggregate): OK; V25 text (rerun): OK | the covenant sentences hold in V26 too |
| track5 · test_N5_labels_and_sweep | the V25 wording ('3c. V25', 'coherent_attacks_v25.py', 'build_corpus_identity_v25.py', 'beacon_record_drand_v25.py collect', Q phrases, driver v9 comment absences) | V26 text (aggregate): FAILED on '3c. V25'; V25 text (rerun): OK | the rerun establishes only that the V25 text has V25's labels — NOTHING about V26; the aggregate failure is the true V26 result for this test |
| track6 · test_P3_sweep | the V26 wording (no 'on the V22 candidate'; design-doc phrases; driver v10 comment absences; inspection v26 header) | V26 text | OK | holds in V26 |
| track6 · test_P4_covenant_in_the_questions_file | the current questions file (covenant sentences) | current questions file | OK | holds |
| NEW track6 · test_track6_text_v26 (this order) | the V26 wording: 'DRAFT V26', '3c. V26', all v26/v10/v6 names, the v26 script in §9, covenant + absence sentences, '118 tests', no 'on the V22 candidate' | fail-first below | see below | the V26-specific labels — what the V25-era test could not establish |

## Fail-first for the NEW V26 text test
```
against the V25 text (expected to FAIL — labels differ):
AssertionError: 'DRAFT V26 — STAGED CANDIDATE' not found in '# OPTION (A) — INSTRUMENT SELECTION RULE, DRAFT V25 — STAGED CANDIDATE (NOT GATED, NOT ADOPTED, NOT
Ran 1 test in 0.001s
FAILED (failures=1)
against the V26 text (expected to pass):
Ran 1 test in 0.001s
OK
test file ed882a918e1ec34b  V25 d29aabac28d6d7de  V26 9a13afd1b496a7da
```

Correction of my own earlier phrasing: 'text tests green against V26' was true for the version-agnostic and V26-written tests and FALSE for track 5's label test; the V26 text's §3c note ('run with RULE_TEXT = the V25 text it was written for') describes a rerun that says nothing about V26. This file, the preserved log and the new test are the record; the V26 text itself (under active review) is not edited — the next permitted candidate carries the new test as a pin.
