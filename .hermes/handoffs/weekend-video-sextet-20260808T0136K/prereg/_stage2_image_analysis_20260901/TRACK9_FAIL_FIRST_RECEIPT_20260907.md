# TRACK 9 FAIL-FIRST RECEIPT (codex V28-1/2/3 — contradictions, repaired; Blanc 02:06 categories) — 2026-09-07 02:47 KST

## Run 1: against BYTE-COPIES of the V28 modules (import lines renamed only), BEFORE any repair
```
fd5b7eb5f3ce8efc  ../track2/provenance_designs_v9.py (copy)
b9942d86a68d591d  ../fourier_chirality/run_configurations_v13.py (copy)
test_precedence_survives_the_prechecks (test_track9_fail_first.V28_1_2_CompletePaths) ... FAIL
test_later_distinct_delivery_does_not_invalidate_the_earliest (test_track9_fail_first.V28_3_RuleIII) ... FAIL
test_names_pins_and_wording (test_track9_fail_first.V28_3_Text) ... ERROR
FileNotFoundError: [Errno 2] No such file or directory: '/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/_stage2_image_analysis_20260901/_optionA_dev/track1/coherent_attacks_v29.py'
    self.assertTrue(str(cm.exception).startswith("EVENT-FORGED"), str(cm.exception))
AssertionError: False is not true : RETRY-EVENTS-UNAVAILABLE: IDENTITY-WITNESS-COMMIT-UNDETERMINED: the push event's before..head delivery of the approval commit could not be established here (a git object missing locally, a failed or unlaunchable git command)
    self.assertIn("a later event does not invalidate an authentic earliest event", P.__doc__)
AssertionError: 'a later event does not invalidate an authentic earliest event' not found in 'TRACK 2 v8 — RECOMMENDED, UNADOPTED designs, repaired after codex\'s V27 review (V27-1, V27-2, V27-3) — Blanc 02:06 KST 09-07: these were CONTRADICTIONS between\nthe 
Ran 3 tests in 1.709s
FAILED (failures=2, errors=1)
```

## Run 2 (code cases; the text case waits for the V29 text): against the REPAIRED successors provenance_designs_v9 / run_configurations_v13. (A first attempt of this block ran with the driver edit not yet applied — the edit script had aborted on an already-renamed import line; harness error, removed. The v9 module was restored from the v8 copy and the edits re-applied in full.)
```
test_precedence_survives_the_prechecks (test_track9_fail_first.V28_1_2_CompletePaths) ... ok
test_later_distinct_delivery_does_not_invalidate_the_earliest (test_track9_fail_first.V28_3_RuleIII) ... ok
Ran 2 tests in 17.513s
OK
```

## Run 3 — text: the V29-specific text test FAIL-FIRST against V28, then V29; track 9's V28-3 text case against V28 (fail-first) and V29 + revised Q / T2 (revision 9). Disclosed corrections before this run, all test-side or wording-side, no code change: (1) the V28-3 text case had asserted that the v13 driver fixture header contains no 'driver v8' at all — the header keeps its inherited text marked as history, so the expectation was narrowed to 'the file OPENS by naming itself v13/V29' (codex's actual complaint); (2) the same case had sliced the questions file at its first 'FORGED', an earlier receipt sentence — it now asserts the revised contract phrase directly; (3) the V29 text's L-INH / L-AVAIL qualifications and its attribution sentence were re-generated to the exact phrases the V29-specific test asks for (same content). The test digests pinned in V29 are the corrected files'. Three earlier runs of this block preceded these corrections; removed.
```
[test_track9_text_v29 vs V28]
Ran 1 test in 0.001s
FAILED (failures=1)
[test_track9_text_v29 vs V29]
Ran 1 test in 0.001s
OK
[V28_3_Text vs V28]
Ran 1 test in 0.001s
FAILED (failures=1)
[V28_3_Text vs V29]
Ran 1 test in 0.001s
OK
```

## Run 4 — the complete aggregate on the V29 candidate (`_tmp_v29_all_suites_aggregate_RUN1.txt`): 136 tests in 22 suites, every block OK, warning-strict; attribution: track 5 → V25, track-6 text → V26, track-7 text → V27, track 8 (its V27-3 text case asserts the V28 counts) and the V28-specific text test → V28, version-agnostic tests + track 9 + the V29-specific test → V29.

## Per-test classification (written against the SUCCESSORS; run 1 against byte-copies of the V28 modules)
| test | kind | run 1 (V28 copies) | run 2 (repaired) | codex clause |
|---|---|---|---|---|
| V28_1_2 precedence survives the prechecks — seven sub-cases on the COMPLETE composed path: approval undetermined + genuine same-id contradiction → EVENT-FORGED; + wrong repository (healthy feed / HTTP 503) → EVENT-INCONSISTENT; offline → IDENTITY-WITNESS-COMMIT-UNDETERMINED; undetermined, nothing contradicting → RETRY-EVENTS-UNAVAILABLE; open event undetermined + genuine same-id → HISTORY-CONTINUATION: OPEN-EVENT-FORGED; + wrong repo → OPEN-EVENT-INCONSISTENT-INPUT; nothing contradicting → RETRY … EVIDENCE-UNAVAILABLE | complete-path, behavioural | FAIL at sub-case 1 (`RETRY-EVENTS-UNAVAILABLE: IDENTITY-WITNESS-COMMIT-UNDETERMINED`, codex's exact V28-1 output); the later sub-cases were not reached by the lane's run 1 — codex's dispatched V28 report (seat B, category 2) executed each of them on the V28 bytes and is the evidence for those | ok | V28-1, V28-2 |
| V28_3 rule (iii): a later distinct qualifying push beside a verbatim earliest genuine event → AUTHENTIC; an EARLIER qualifying event → NOT-EARLIEST; the clause text in the module header | behavioural + text | FAIL (header phrase absent; behaviour already correct in v8) | ok | V28-3 |
| V28_3 names, pins and wording (historical builder-fixture clause, verifier digest, fixture header, inspection row-1 note, Q contract sentence, T2 outcomes row, L-INH/L-AVAIL qualifications, V28-1/2/3 labels) | text | ERROR (no coherent_attacks_v29) / FAIL vs V28 | ok vs V29 | V28-3 |

Test-expectation corrections between runs, all disclosed above: three text-side (fixture-header scope, Q slicing, phrase case/attribution wording) and none on the code cases. No code was changed to satisfy a test after run 2.

## Digests
```
cbebc41767149caa45ad97e57bfae8c9d37adb1b40cf46b4065ece04f10b49ae  _optionA_dev/track2/provenance_designs_v9.py
d59198d2342fb2d35d7ce2035c1a84d038645b16ba7b09d1dbf986a77f7b6ca3  _optionA_dev/fourier_chirality/run_configurations_v13.py
df4e04ea9546f780087afd3ae556a5dd6427518adb2d9b44684a991440a70f6e  _optionA_dev/fourier_chirality/test_run_configurations_v13.py
3e6bdc911eb078a0e7892149663f062db425216784bc2a7ba53d39f808d49808  _optionA_dev/corpus_identity/build_corpus_identity_v29.py
0d2992b4c1b0f5782baa807f5254086f53e9751608d5fdb3510ae071b1015a59  _optionA_dev/corpus_identity/test_build_corpus_identity_v29.py
e46b300852d430d7ddc7281b0390a5fa8537ed4b63c15c1b61c447d16295bb57  _optionA_dev/beacon_v2/beacon_record_drand_v29.py
6189f0a330889d26fc4156b3c08e1cfb1dbc2ca4ab492bef7f29c695f2ad6394  _optionA_dev/beacon_v2/test_beacon_record_drand_v29.py
ba4cb1ba251e5e7ea9dfdd1647a6954c42019c98104f88bf01a1291a6d92a371  _optionA_dev/track1/coherent_attacks_v29.py
c881060647240a9ddea37b209c2e5fd17685c657d444b47ed47e671ea97ba4ab  _optionA_dev/track9/test_track9_fail_first.py
9fa4b7bab11313360b0259e9341f15bf851e7fa37d1fc51fa5f00c83aae49f96  _optionA_dev/track9/test_track9_text_v29.py
4458b821e3a1249c0646ce2790491f4d04e7224d0ef60721144354e216450599  OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V29_20260907.md
b6d3d4137c3e57096b682c591c414a9baae941e635357e6271e1af5f1da09b69  V29_CANDIDATE_ATTACK_INSPECTION_20260907.md
d14d948c2741fd34f3e2b190df041220f00fec914500b8ce1470ed394bb5a17e  LIMITS_VS_CONTRADICTIONS_20260907.md
afb441ae8f9bb7e852472e53f61e00575fadff54cd93735e29d2080c4b28e81e  TRACK2_PROVENANCE_DESIGNS_UNADOPTED_20260906.md
4e6dc490485cf956a6471ccad6be73fb86bfe0dc0d60712343b18f3a162e8a52  QUESTIONS_FOR_DUHO_TRACK2_ORIGIN_AND_RECEIPTS_20260906.md
```

Closed 2026-09-07 02:57 KST. Nothing gated, adopted, signed or drawn.
