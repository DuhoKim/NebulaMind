LANA FIX RECHECK — remaining-20 proposal.
You previously reported ISSUES on 28088 and 28148. Review only the corrected lines below. Return PASS if the two issues are fixed; otherwise list exact fixes. No tools, no DB, no SQL, no edits. End with marker LANA_REMAINING20_FIX_RECHECK_20260705T085714Z.


## Previous Lana review
# LANA review — remaining-20 draft (source-position / methods)

**Verdict: ISSUES** — 2 rows need fixes before Hwao gates; the other 18 are safe. Most of the queue is well-routed (kinetic/radio routing correct, non-AGN rows not inflating AGN claims, all successors capped `accepted_limited`, no full-PDF-pin overclaim). Details below.

## Blocking issues (exact row fixes)

**28088 — reason/span mismatch, hold for supervised Gemini.**
The quoted span is *"Stellar feedback can regulate star formation in low- and intermediate-mass systems, but is generally insufficient to fully quench high-mass galaxies."* That is a **mixed / partly pro-AGN motivation** sentence. The `decision_reason` instead asserts *"low-mass high-redshift quenched galaxies are often environmental/satellite systems"* — content **not present in the span**. As written it both overclaims and risks reading a pro-AGN motivation as a non-AGN alternative.
- Replacement: `relink -> 2944 / limitation_or_caution / accepted_limited`, reason rewritten to the actual span (stellar feedback regulates low/intermediate-mass SF but is insufficient to quench high-mass systems). **If the source's true position cannot be pinned from the snippet alone, leave this row `pending` for the single supervised Gemini one-packet second opinion** — this is the row most in need of it. Do not gate it as `support` on the current reason.

**28148 — reason overclaims relative to span.**
`decision_reason` says the source *"reports strong detections of ultra-fast nuclear winds,"* but the quoted span is motivational/broad-framing (AGN feedback *"believed to be driven by powerful outflows … could be a promising mechanism … M_BH–σ"*). No detection is quoted.
- Replacement: keep `relink -> 2943 / accepted_limited`, but rewrite `decision_reason` to match the span (broad AGN-feedback framing, not a detection result) and keep `abstract_only_verified`. Tori's own `limitation_or_counter_reason` already flags the broad-framing caveat — make the reason field consistent with it, don't let "strong detections" stand.

## Caveats Hwao must preserve (not blocking)

- **28069 + 28073** are two `support` rows from the same source (2512.05584) to the same claim 2944. Role-distinction (observational baryon deficiency vs SFR-scaling) is genuine, so allow — but they must **not be counted as two independent corroborations** of 2944.
- **28131** (`route_kinetic_radio -> 2947`) rests on a *definitional* span ("often called radio mode"), not an efficacy result. Routing is correct and cap is right; treat as thin support / near-background. Secondary Gemini candidate if 28088 does not consume the packet.
- **28140** (`-> 2943`) rests on a section-preview methods sentence ("in Section 4 we present our results"), thin as direct evidence; acceptable only because it is capped and 2943 has stronger corroboration (28144).
- **28076** correctly **rejected** from 2947 despite a "radio" matched-term — supernova superbubble, not AGN jet. Preserve this; do not let a later pass re-route it.
- Verification labels are honest: every accepted row keeps `full text not DB-pinned`, `NO_GO` product gate, `accepted_limited` cap. No full-PDF-pin overclaim. Keep it that way.

## Summary
Safe to gate B4/B6/B7/B8 as drafted (with the 28148 reason fix folded in). **Hold B5's 28088** for a corrected role or the reserved Gemini second opinion before Hwao closes it. No SQL/DB/trust/prose/deploy touched by this review.

LANA_REMAINING20_REVIEW_20260705T085714Z


## Corrected proposal lines for 28088/28148
{
  "accepted_for_docs_source_position": "accepted_limited",
  "accepted_support_role": "limitation_or_caution",
  "accepted_target_claim_id": 2944,
  "accepted_target_stance": "supports",
  "anti_duplicate_check_status": "resolved_same_source_stacking_or_not_applicable",
  "batch_id": "B5",
  "decision_confidence": "medium",
  "decision_enum": "relink",
  "decision_owner": "Tori draft for Lana/Hwao review",
  "decision_reason": "The quoted span says stellar feedback can regulate star formation in low- and intermediate-mass systems but is generally insufficient to fully quench high-mass galaxies; that is a non-AGN/stellar-feedback limitation that supports 2944 as an alternatives-and-qualifiers claim, not a broad AGN support row.",
  "decision_reason_plain_english": "The quoted span says stellar feedback can regulate star formation in low- and intermediate-mass systems but is generally insufficient to fully quench high-mass galaxies; that is a non-AGN/stellar-feedback limitation that supports 2944 as an alternatives-and-qualifiers claim, not a broad AGN support row.",
  "decision_timestamp_utc": "2026-07-05T09:10:00Z",
  "dependency_handling_action": "No human/evidence vote dependencies on this row; comments/element links/jury scorecards count zero in queue snapshot.",
  "duplicate_check_against_successor_evidence_ids": "kept as distinct environmental/satellite-quenching alternative evidence",
  "evidence_id": 28088,
  "exact_quote_or_paraphrase_source_span": "[page58_neutral_seed_v1 gold_id=stance2b-030] Stellar feedback can regulate star formation in low- and intermediate-mass systems, but is generally insufficient to fully quench high-mass galaxies (Ciotti et al. , 1991 ; Springel and Hernquist, 2003 ) .",
  "figure_or_table": "not_applicable",
  "human_decision": "relink",
  "human_decision_enum": "relink",
  "human_reviewed_at_utc": "2026-07-05T09:10:00Z",
  "human_reviewer": "pending_hwao_gate",
  "limitation_or_counter_reason": "Corrected after Lana review: role is limitation_or_caution, not generic support; reason is limited to the quoted span and does not rely on environmental/satellite content outside the span.",
  "matched_terms": [
    "stellar",
    "feedback",
    "AGN",
    "quenching"
  ],
  "paragraph_or_sentence_locator": "1fd0dab98ca0baffc2e9a487ae267683",
  "pdf_page": "not_applicable",
  "product_publication_gate": "NO_GO_DB_OR_PRODUCT_PUBLICATION_UNDER_THIS_APPROVAL",
  "proposal_marker": "TORI_CORRECTED_REMAINING20_SOURCE_POSITION_PROPOSAL_20260705T085714Z",
  "queue_id": "SPQ-2929-28088",
  "section": "public arXiv/source record plus queue source snippet; full text not DB-pinned",
  "selected_role": "limitation_or_caution",
  "selected_stance_if_visible_successor": "supports",
  "source_accessed_url_or_path": "https://arxiv.org/abs/2605.03008",
  "source_position_note": "Docs-only decision from queue source span plus public source-record/abstract probe. Full product evidence binding remains NO-GO until a later exact packet.",
  "source_position_verification_status": "abstract_only_verified",
  "source_type": "paper_pdf_or_authoritative_abstract_or_source_record",
  "target_claim_id_if_any": 2944,
  "target_claim_text_if_any": "AGN feedback is one quenching axis among several; central/bulge/black-hole predictors, halo/environment/satellite pathways, strangulation, stripping, gas retention, low star-formation efficiency, and star-formation-driven outflows remain alternatives or qualifiers.",
  "write_lock": "NO_APPLY_SQL_NO_DB_WRITE_FROM_THIS_QUEUE"
}
{
  "accepted_for_docs_source_position": "accepted_limited",
  "accepted_support_role": "support",
  "accepted_target_claim_id": 2943,
  "accepted_target_stance": "supports",
  "anti_duplicate_check_status": "resolved_same_source_stacking_or_not_applicable",
  "batch_id": "B8",
  "decision_confidence": "medium",
  "decision_enum": "relink",
  "decision_owner": "Tori draft for Lana/Hwao review",
  "decision_reason": "The quoted span frames AGN feedback as being driven by powerful accretion-disk outflows and as a plausible mechanism for host-galaxy coevolution correlations; it supports 2943 only as broad, limited AGN-outflow framing, not as the detection-result paragraph.",
  "decision_reason_plain_english": "The quoted span frames AGN feedback as being driven by powerful accretion-disk outflows and as a plausible mechanism for host-galaxy coevolution correlations; it supports 2943 only as broad, limited AGN-outflow framing, not as the detection-result paragraph.",
  "decision_timestamp_utc": "2026-07-05T09:10:00Z",
  "dependency_handling_action": "No human/evidence vote dependencies on this row; comments/element links/jury scorecards count zero in queue snapshot.",
  "duplicate_check_against_successor_evidence_ids": "kept as direct local AGN ultra-fast-outflow support, with broad-feedback framing caveat",
  "evidence_id": 28148,
  "exact_quote_or_paraphrase_source_span": "[page58_neutral_seed_v1 gold_id=stance2b-115] AGN feedback, which is believed to be driven by powerful outflows from the accretion disk ( Silk98 ; Zubova12 ) , could be a promising mechanism to account for some of the most significant unresolved issues in astronomy, such as the underlying reasons for the strong correlation between SMBH mass and the stellar bulge velocity dispersion of the host galaxy (the M B ​ H − σ",
  "figure_or_table": "not_applicable",
  "human_decision": "relink",
  "human_decision_enum": "relink",
  "human_reviewed_at_utc": "2026-07-05T09:10:00Z",
  "human_reviewer": "pending_hwao_gate",
  "limitation_or_counter_reason": "Corrected after Lana review: do not claim this quoted span reports strong detections; the public abstract reports detections elsewhere, but this row binding stays with the broad-framing span.",
  "matched_terms": [
    "outflow",
    "winds",
    "feedback",
    "AGN",
    "stellar"
  ],
  "paragraph_or_sentence_locator": "1cb28642ed01130487758572f6e270b0",
  "pdf_page": "not_applicable",
  "product_publication_gate": "NO_GO_DB_OR_PRODUCT_PUBLICATION_UNDER_THIS_APPROVAL",
  "proposal_marker": "TORI_CORRECTED_REMAINING20_SOURCE_POSITION_PROPOSAL_20260705T085714Z",
  "queue_id": "SPQ-2929-28148",
  "section": "public arXiv/source record plus queue source snippet; full text not DB-pinned",
  "selected_role": "support",
  "selected_stance_if_visible_successor": "supports",
  "source_accessed_url_or_path": "https://arxiv.org/abs/2604.22922",
  "source_position_note": "Docs-only decision from queue source span plus public source-record/abstract probe. Full product evidence binding remains NO-GO until a later exact packet.",
  "source_position_verification_status": "abstract_only_verified",
  "source_type": "paper_pdf_or_authoritative_abstract_or_source_record",
  "target_claim_id_if_any": 2943,
  "target_claim_text_if_any": "AGN activity can drive molecular, ionized, or neutral gas outflows capable of removing or depleting star-forming fuel in selected massive or AGN-host galaxies, with detection rates remaining tracer- and sample-dependent.",
  "write_lock": "NO_APPLY_SQL_NO_DB_WRITE_FROM_THIS_QUEUE"
}
