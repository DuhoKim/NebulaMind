# TRACK 12 — THE ORIGINAL RUN 1 (nine multi-assertion methods), PRESERVED — reconstructed verbatim from the session's captured output (2026-09-07 05:11 KST)

DISCLOSURE: the receipt file that held this log was OVERWRITTEN at 05:07 KST when the per-subcase re-run was started (a `>` redirect), before Blanc's 05:09 order not to alter it arrived. The log below is the exact output the session captured from that run (the test lines, the assertion lines, the summary); the two digest lines are the copies' digests at that moment — the v12 copy was byte-identical to v11 (4d4a2a439765d394…) and the v16 copy byte-identical to v15 (a9ffae72071fbd5d…) except for import renames, BEFORE the INDEPENDENCE table was appended. Run at 05:0x KST against the unrepaired copies with the first (nine-method) test file, since replaced.

```
test_malformed_remote_event_and_receipt_exception (test_track12_fail_first.V31_4_RemoteAndReceipt) ... FAIL
test_stage_states_and_reasons (test_track12_fail_first.V31_5_Bookkeeping) ... ERROR
test_claims_match_the_code (test_track12_fail_first.V31_Text) ... FAIL
    missing = sorted(c for c in codes if c not in P.CLASS_ALLOWLIST and not c.endswith("-")); self.assertEqual(missing, [], f"codes raised but not in the allowlist: {missing}")
    missing = sorted(c for c in codes if c not in P.CLASS_ALLOWLIST and not c.endswith("-")); self.assertEqual(missing, [], f"codes raised but not in the allowlist: {missing}")
AttributeError: module 'provenance_designs_v12' has no attribute 'CLASS_ALLOWLIST'
    st = rc.LAST_STAGES; self.assertEqual(st["S5-history"]["state"], "blocked", st); self.assertIn("open", st["S5-history"]["why"].lower())
AttributeError: module 'run_configurations_v16' has no attribute 'LAST_STAGES'
    self.assertTrue(msg.startswith("EVENT-FORGED"), msg); self.assertGreaterEqual(len(calls), 1, "no retrieval was made")
AssertionError: False is not true : WITNESS-FETCH-FAILED: fixture transport unavailable
    self.assertTrue(msg.startswith("EVENT-INCONSISTENT"), msg)                                                       # (d) the local type/repository/ref sweep needs no git
AssertionError: False is not true : IO-UNAVAILABLE: OSError: fixture: git cannot launch
    msg = self.refusal(ident, cTP, feed(page1, page2=lambda cmd: (1, "", "gh: HTTP 503: Service Unavailable"))); self.assertTrue(msg.startswith("EVENT-FORGED"), msg)
AssertionError: False is not true : RETRY-EVENTS-UNAVAILABLE: SERVER-ERROR: gh: HTTP 503: Service Unavailable
    msg = self.refusal(ident, cTP, feed([ev, evs[0], batch])); self.assertIn("HISTORY-PUBLICATION-BATCH", msg); self.assertFalse(msg.startswith("RETRY-"), msg)
AssertionError: 'HISTORY-PUBLICATION-BATCH' not found in 'RETRY-HISTORY-CONTINUATION: EVIDENCE-INCOMPLETE: history commit b68e09529980 (entry 1) has no push event of its own in the retrieved feed and no evidence of batching — retry within the feed window'
    o, why = P.authenticate_event(retained, [genuine], REPO, REF, commit, root=tmp); self.assertEqual(o, "FORGED", why)
AssertionError: 'UNAVAILABLE' != 'FORGED'
    msg = self.refusal(ident, cTP, feed([ev, bad] + evs)); self.assertIn("MALFORMED-REMOTE-EVIDENCE", msg); self.assertNotIn("MALFORMED-RETAINED-INPUT", msg)
AssertionError: 'MALFORMED-REMOTE-EVIDENCE' not found in "MALFORMED-RETAINED-INPUT: AttributeError: 'str' object has no attribute 'get'"
    for k in ("(V31-1)", "(V31-2)", "(V31-3)", "(V31-4)", "(V31-5)", "run_configurations_v16", "provenance_designs_v12", "CLASS_ALLOWLIST", "MALFORMED-REMOTE-EVIDENCE", "blocked", "partial", "coherent_attacks_v32.py"): self.assertIn(k, r, k)
Ran 9 tests in 14.021s
FAILED (failures=7, errors=2)
```
(The captured output was a `tail -24`; the first four test lines of the nine — V31_1_IndependentStages ×2, V31_2_PartialPages, V31_3_Loops ×2 — scrolled above the capture; their FAIL status is established by the assertion lines above, which belong to them.)

## What this run actually reached (Blanc 05:09, item 1) — per subcase
| method | subcases it held | reached and shown failing | NOT reached (no evidence from this run) |
|---|---|---|---|
| test_a_failed_witness_fetch_does_not_suppress_obtainable_findings | (a) same-id contradiction + fetch failure; (b) wrong schema_version + fetch failure; (c) rewrite + fetch failure | (a) only — WITNESS-FETCH-FAILED | (b), (c) |
| test_local_sweep_does_not_depend_on_launching_git_and_the_helper_import_is_classified | (d) git launch failure + wrong repository; (e) helper import unavailable | (d) only — IO-UNAVAILABLE | (e) |
| test_a_failed_later_page_keeps_the_obtained_contradiction | 503 on page 2; malformed page 2; partial without contradiction | the 503 case only | the other two |
| test_per_entry_loop_does_not_stop_before_a_proven_batch | one | reached — EVIDENCE-INCOMPLETE where BATCH was derivable | — |
| test_same_commit_arm_before_availability_and_standalone_local_sweep | same-commit arm; standalone sweep | the same-commit arm only — UNAVAILABLE | the standalone sweep |
| test_table_is_total_over_the_sources_and_provenance_is_respected | allowlist totality; SPLIT codes; unknown flagged; provenance | NONE — ERROR on the new name CLASS_ALLOWLIST: demonstrates nothing (Blanc item 2) | all |
| test_malformed_remote_event_and_receipt_exception | malformed remote payload; receipt origin as a list | the malformed remote payload only — MALFORMED-RETAINED-INPUT | the receipt case |
| test_stage_states_and_reasons | blocked state; reasons | NONE — ERROR on the new name LAST_STAGES: demonstrates nothing | all |
| test_claims_match_the_code | text | reached (V31 text lacks the V32 tokens) | — |

## What replaced it (Blanc 05:02 item 3 and 05:09)
The test file was rewritten so that EVERY subcase is its own method: 66 controls DERIVED FROM THE INDEPENDENCE TABLE (one per (prerequisite, check) pair, whole-outcome assertions, verdict asserted FIRST so the old behaviour is exercised before any new name is touched) + 17 regressions from codex's V31 constructions (one subcase each; codex's own executions of them remain codex's evidence, seat B, category 2 — they are not folded into this lane's run) + 1 text test. The allowlist-totality test is rewritten to exercise the OLD classification through `classify_refusal` (present in v11) so it FAILS genuinely on the old bytes; the bookkeeping test (LAST_OUTCOME) is a NEW-INTERFACE test with NO fail-first standing and is marked so. The per-subcase run 1 is `TRACK12_FAIL_FIRST_RECEIPT_20260907.md`.
