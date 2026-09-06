# TRACK 7 FAIL-FIRST RECEIPT (codex V26-1/2/3) — 2026-09-07 01:28 KST

## Run 1: against BYTE-COPIES of the V26 modules (import lines renamed only), BEFORE any repair; per-test classification follows.
```
02b9fb4291bc4ae0  ../track2/provenance_designs_v7.py (copy)
1af7a835d09e475d  ../fourier_chirality/run_configurations_v11.py (copy)
2cb68a31f8ed68fc  ../corpus_identity/build_corpus_identity_v27.py (copy)
201b18599cbb0a96  ../beacon_v2/beacon_record_drand_v27.py (copy)
test_same_event_different_before_is_forged (test_track7_fail_first.V26_1_Contradiction) ... FAIL
test_delivery_is_tri_state (test_track7_fail_first.V26_2_TriStateDelivery) ... ERROR
test_missing_objects_are_retry_not_forged (test_track7_fail_first.V26_2_TriStateDelivery) ... FAIL
test_sweep (test_track7_fail_first.V26_3_Text) ... FAIL
    self.assertEqual(P.delivery(self.anc, self.commit, REF, self.work), "DELIVERED")
AttributeError: module 'provenance_designs_v7' has no attribute 'delivery'
    self.assertEqual(o, "FORGED", why)
AssertionError: 'INCOMPLETE' != 'FORGED'
    o, why = P.authenticate_event(self.anc, [self.anc], REPO, REF, self.commit, root=self.stale); self.assertEqual(o, "UNAVAILABLE", why); self.assertNotEqual(o, "FORGED")
AssertionError: 'FORGED' != 'UNAVAILABLE'
    self.assertNotIn("FORGED (absent from the live feed", t2); self.assertIn("INCOMPLETE", t2.split("## (b)")[0])
AssertionError: 'FORGED (absent from the live feed' unexpectedly found in '# TRACK 2 — RECOMMENDED, UNADOPTED DESIGNS for the two provenance boundaries (Blanc\'s order 20:45 KST; codex\'s note 20:43) 
Ran 4 tests in 1.089s
FAILED (failures=3, errors=1)
```

## Run 1b: codex's V26-1 and V26-2 cases against the V26 functions — the OLD behaviour, executed
```
V26-1 v6, same event id + head, different before: INCOMPLETE — WRONG (an affirmative contradiction called incomplete)
V26-2 v6, before..head delivery, full clone: AUTHENTIC
V26-2 v6, same event and feed, clone missing the descendant object: FORGED — WRONG (unavailable git objects called forgery)
```

## Run 1 classification (per test): V26-1 → BEHAVIOURAL (the copy's authenticate_event said INCOMPLETE); V26-2 delivery tri-state → MISSING-INTERFACE (no `delivery`); V26-2 missing-objects → BEHAVIOURAL (the copy said FORGED); V26-3 → BEHAVIOURAL (text). Totals: 1 missing-interface, 3 behavioural. Between runs one expectation in the missing-objects test was corrected (a same-id event with different bytes IS a contradiction; the wrong-repository case is asserted as INCONSISTENT-INPUT) — disclosed.

## Run 2: the SAME tests (one expectation corrected as disclosed) against the REPAIRED successors and the V27 staged text — 01:33 KST
```
8c20a5d3370b4c91  ../track2/provenance_designs_v7.py (repaired)
abf9bd9424448ba2  ../fourier_chirality/run_configurations_v11.py (repaired)
58499a486be21ab7  ../corpus_identity/build_corpus_identity_v27.py (repaired)
d380cb8824a2ca5e  ../beacon_v2/beacon_record_drand_v27.py (repaired)
test file dec20a7c678b00c6
test_same_event_different_before_is_forged (test_track7_fail_first.V26_1_Contradiction) ... ok
test_delivery_is_tri_state (test_track7_fail_first.V26_2_TriStateDelivery) ... ok
test_missing_objects_are_retry_not_forged (test_track7_fail_first.V26_2_TriStateDelivery) ... ok
test_sweep (test_track7_fail_first.V26_3_Text) ... ok
Ran 4 tests in 0.819s
OK
    exit status: 0
```
