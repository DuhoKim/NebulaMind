# Page 58 Locked Stance Gold Local Gate Score

Dry-run report only. Papa locked the gold; this report does not certify pass/fail.

## Scored Gate

- Stage 1: cosine relatedness gate, tau_rel=0.53.
- Stage 2: local_panel_provisional_no_claude_for_full_pass via local Ollama models qwen3.6:27b-nvfp4 + gpt-oss:20b; no Claude or paid lane.

## Stage 1

- Macro-F1: 0.7349
- Per-class: `{"related": {"f1": 0.9116, "precision": 0.9333, "recall": 0.8909, "support": 110}, "unrelated": {"f1": 0.5581, "precision": 0.5, "recall": 0.6316, "support": 19}}`
- Confusion matrix: `{"related": {"related": 98, "unrelated": 12}, "unrelated": {"related": 7, "unrelated": 12}}`

## Stage 2

- Rows: 110
- Macro-F1 excluding contradicts sentinel: 0.6241
- Per-class: `{"related_different_facet": {"f1": 0.592, "precision": 1.0, "recall": 0.4205, "support": 88}, "supports": {"f1": 0.6562, "precision": 0.4884, "recall": 1.0, "support": 21}}`
- Confusion matrix: `{"contradicts": {"contradicts": 1, "no_stage2_prediction": 0, "related_different_facet": 0, "supports": 0}, "no_stage2_prediction": {"contradicts": 0, "no_stage2_prediction": 0, "related_different_facet": 0, "supports": 0}, "related_different_facet": {"contradicts": 17, "no_stage2_prediction": 12, "related_different_facet": 37, "supports": 22}, "supports": {"contradicts": 0, "no_stage2_prediction": 0, "related_different_facet": 0, "supports": 21}}`
- Contradicts sentinel: `{"base_sentence": "Satellite galaxies experience environmental quenching after infall into groups or clusters, distinct from mass-driven quenching in centrals.", "correct": true, "gold_id": "stance2b-001", "intro_sentence": "In Bluck et al. ( 2020b ) , the quiescence of high mass satellites is shown to behave much like centrals, i.e. exhibiting a strong correlation with central velocity dispersion, although with the notable difference of a weak secondary dependence on environmental parameters.", "pred_stage1_label": "related", "pred_stage2_label": "contradicts", "true_stage1_label": "related", "true_stage2_label": "contradicts"}`

## Containment

- HEAD 4ba9675; db_write_count=0; paid_lane_touched=false; /api/health=200.
