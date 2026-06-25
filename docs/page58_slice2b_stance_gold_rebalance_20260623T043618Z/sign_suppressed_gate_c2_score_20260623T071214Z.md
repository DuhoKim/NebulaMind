# Page 58 Sign-Suppressed Gate C2 Score

Draft for Kun only. No live write, no seed apply, no pass/fail certification by implementer.

## Configuration

- Stage 1: cosine relatedness gate, tau_rel=0.53.
- Stage 2 auto pass: every Stage-1-related row renders as `related_different_facet` with explicit evidence stance `none`.
- Local supports and contradicts are queued for human review and do not create trust-bearing writes.
- Future human-confirmed contradictions must write stance `challenges`, not `contradicts`.

## Stage 1

- Macro-F1: 0.7349
- Per-class: `{"related": {"f1": 0.9116, "precision": 0.9333, "recall": 0.8909, "support": 110}, "unrelated": {"f1": 0.5581, "precision": 0.5, "recall": 0.6316, "support": 19}}`
- Confusion matrix: `{"related": {"related": 98, "unrelated": 12}, "unrelated": {"related": 7, "unrelated": 12}}`

## Stage 2

- Rows: 110
- Macro-F1 excluding contradicts sentinel: 0.4086
- Per-class: `{"related_different_facet": {"f1": 0.8172, "precision": 0.7755, "recall": 0.8636, "support": 88}, "supports": {"f1": 0.0, "precision": 0.0, "recall": 0.0, "support": 21}}`
- Confusion matrix: `{"contradicts": {"contradicts": 0, "no_stage2_prediction": 0, "related_different_facet": 1, "supports": 0}, "no_stage2_prediction": {"contradicts": 0, "no_stage2_prediction": 0, "related_different_facet": 0, "supports": 0}, "related_different_facet": {"contradicts": 0, "no_stage2_prediction": 12, "related_different_facet": 76, "supports": 0}, "supports": {"contradicts": 0, "no_stage2_prediction": 0, "related_different_facet": 21, "supports": 0}}`
- Contradicts sentinel: `{"auto_seed_stage2_label": "related_different_facet", "auto_trust_bearing_write": false, "correct_as_contradiction": false, "gold_id": "stance2b-001", "human_queue": true, "local_stage2_label_suppressed": "contradicts", "note": "The sign-suppressed auto pass intentionally renders the sentinel as neutral rdf and queues the local contradict for human review.", "pred_stage1_label": "related", "safe_suppression": true, "true_stage1_label": "related", "true_stage2_label": "contradicts"}`

## Seed Plan

- Counts: `{"auto_seed_rows": 105, "auto_trust_bearing_writes": 0, "evidence_stance_for_write": {"no_seed": 24, "none": 105}, "human_queue": {"local_contradicts_suppressed_for_human_review": 18, "local_support_suppressed_for_human_review": 43, "not_queued": 68}, "no_seed_rows": 24}`
- C1 guard: `{"confirmed_contradiction_write_stance_if_later_human_approved": "challenges", "neutral_seed_can_move_trust": false, "no_hardcoded_contradicts_write_stance": true, "rdf_auto_seed_evidence_stance": "none", "trust_model_counts_only": ["supports", "challenges"]}`

## Containment

- HEAD 4ba9675; db_write_count=0; paid_lane_touched=false; /api/health=200.
