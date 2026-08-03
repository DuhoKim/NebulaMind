**PASS** — both blocking issues are fixed.

**28088** — The `decision_reason` / `decision_reason_plain_english` now track the actual span (stellar feedback regulates SF in low/intermediate-mass systems but is insufficient to quench high-mass systems); the fabricated "environmental/satellite" assertion is gone from the reason. Role correctly downgraded to `limitation_or_caution`, cap `accepted_limited`, target 2944 as alternatives/qualifiers. The overclaim is resolved.

**28148** — The `decision_reason` no longer asserts "strong detections"; it now reads as broad AGN-outflow framing and explicitly says "not as the detection-result paragraph." `limitation_or_counter_reason` is now consistent ("do not claim this quoted span reports strong detections"). Cap `accepted_limited`, `abstract_only_verified` preserved. Consistent with Tori's caveat.

Two non-blocking residuals (do not gate on these):
- 28088 `duplicate_check_against_successor_evidence_ids` still says *"kept as distinct environmental/satellite-quenching alternative evidence"* — leftover environmental/satellite wording that contradicts the corrected span-limited reason. Cosmetic; not in the reason field, but worth scrubbing for consistency.
- 28148 `matched_terms` still lists `"winds"`, but the bound span says "outflows," not winds. Harmless routing artifact.

Neither changes the verdict. Both rows are safe for Hwao to gate as corrected.

LANA_REMAINING20_FIX_RECHECK_20260705T085714Z
