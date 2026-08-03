# LANA remaining-20 source-position judgment brief

Coordinator: Hwao/Fable. Relay/executor: Tori/Hermes. Lane: Lana.

User direction: finish the 20 remaining held 2929 rows as docs-only source-position / human-adjudication batches.

Hard locks:
- No queue edits by Lana.
- No SQL/apply/rollback files.
- No DB queries/connections/writes.
- No trust recompute.
- No prose/wiki publish.
- No runtime deploy/restart.
- No git commit/push/merge.
- No cron/cloud/account/secret changes.
- Gemini web quota held unless separately needed for a contested row; do not invoke it.

Inputs included below:
- Hwao remaining-20 batch plan.
- Pending rows context with summary snippets and candidate target claims.
- Public source-record/abstract probes captured by Tori from arXiv pages.
- Goru precheck PASS.

Task:
Produce a source-position + human-adjudication proposal for all 20 pending rows, grouped B4-B8. This is a proposal only; Tori will apply only after Hwao gate.

Decision rules:
- Use only allowed decision enums: relink, copy_source_fill, retire_reject, leave_archival, route_kinetic_radio.
- Prefer relink only when the snippet directly supports/challenges a scoped successor claim and duplicate/stacking risk is controlled.
- Use leave_archival/retire_reject for non-AGN, local cloud-scale, redundant, or topic-match-only rows that should not inflate successor evidence.
- Use route_kinetic_radio for real AGN jet/radio/kinetic rows better suited to 2947 than broad quenching/outflow claims.
- Cap every visible-successor row at accepted_limited unless the source context is directly pinned enough for accepted. Given current inputs, accepted_limited is expected.
- Use source_position_verification_status from: docs_verified, source_record_verified, abstract_only_verified, pdf_verified, not_applicable. Prefer docs_verified/source_record_verified if exact span comes from the queue snippet plus public source record/abstract, not full PDF pinning.
- Preserve product_publication_gate and write_lock.
- No source is a product/publication decision.

Output format:
1. Markdown report with per-batch/per-row reasoning.
2. Then a fenced block exactly named JSONL_PROPOSAL containing exactly 20 JSON objects, one per line.

Each JSON object must include:
- evidence_id
- batch_id
- decision_enum
- accepted_target_claim_id (number or null)
- accepted_target_stance
- accepted_for_docs_source_position
- source_position_verification_status
- accepted_support_role
- selected_role
- selected_stance_if_visible_successor
- human_decision
- decision_owner = Lana
- human_reviewer = Lana
- decision_reason
- decision_reason_plain_english
- source_accessed_url_or_path
- source_type
- exact_quote_or_paraphrase_source_span
- section
- paragraph_or_sentence_locator
- pdf_page
- figure_or_table
- source_position_note
- matched_terms (array)
- target_claim_id_if_any
- target_claim_text_if_any
- limitation_or_counter_reason
- dependency_handling_action
- duplicate_check_against_successor_evidence_ids
- anti_duplicate_check_status
- decision_confidence
- product_publication_gate = NO_GO_DB_OR_PRODUCT_PUBLICATION_UNDER_THIS_APPROVAL
- write_lock = NO_APPLY_SQL_NO_DB_WRITE_FROM_THIS_QUEUE
- proposal_marker = LANA_REMAINING20_SOURCE_POSITION_PROPOSAL_20260705T085714Z

End with standalone marker LANA_REMAINING20_SOURCE_POSITION_PROPOSAL_20260705T085714Z.


## Hwao plan

# HWAO Remaining-20 Coordination Plan

Marker anchor: HWAO_REMAINING20_PLAN_20260705T085714Z
Generated: 2026-07-05T08:57:14Z (planning only; no row decisions)
Active phrase: NO ACTIVE EXECUTION PHRASE

## Scope reminder (hard locks)
- Docs/JSONL/CSV/Markdown queue artifacts only.
- No SQL / apply / rollback files.
- No DB queries or DB writes.
- No trust recompute.
- No prose / wiki publish.
- No runtime deploy / restart.
- No git commit / push / merge.
- No cron / cloud / account / secret changes.
- Gemini web quota reserved: spend only on a specifically contested row, one packet, separately recorded, supervised.

State going in: 36-row queue, 16 completed, 20 pending. B3 gate says next is B4.

## Batch plan (20 pending -> 5 batches, grouped by source to keep same-source context together)

### B4 - arXiv:2512.05584 x4 + Perseus superbubble x4 (8 rows) [gate says this is next]
SN-/stellar-feedback context; expected outcomes are reject-or-qualifier against AGN claims.
- 28066 arXiv:2512.05584 -> primary 2945 (outflows fall back <100 kpc; gas-removal caution)
- 28069 arXiv:2512.05584 -> primary 2944 (stellar-feedback baryon deficiency; alternative)
- 28070 arXiv:2512.05584 -> primary 2944 (stellar-feedback gas ejection in sims; alternative)
- 28073 arXiv:2512.05584 -> primary 2944 (SFR-dependent stellar-feedback outflows; alternative)
- 28076 Perseus superbubble -> primary 2944 (massive-star clearing/compression, positive-feedback qualifier; kinetic_radio_candidate)
- 28080 Perseus superbubble -> primary 2944 (large-scale feedback on star-forming regions)
- 28083 Perseus superbubble -> primary 2944 (stellar-feedback-driven structures)
- 28084 Perseus superbubble -> primary 2944 (stellar feedback disrupts molecular clouds; SFE qualifier)

### B5 - stellar / non-AGN feedback singles + pair (5 rows)
More non-AGN alternative/qualifier candidates; expected reject-or-qualifier.
- 28082 arXiv:1507.06366 -> primary 2944 (massive-star feedback / GMC demise)
- 28088 arXiv:2605.03008 -> primary 2944 (stellar feedback insufficient to quench high-mass)
- 28114 arXiv:1203.2926 -> primary 2944 (radiation-pressure feedback in clusters)
- 28118 arXiv:1203.2926 -> primary 2944 (star-forming clump radiation-force model)
- 28075 arXiv:0901.1880 -> primary 2945 (winds insufficient to remove gas; gas-removal caution)

### B6 - arXiv:0901.1880 remainder incl. radio-mode (2 rows)
One gas-removal caution duplicate plus one explicit radio-mode row.
- 28110 arXiv:0901.1880 -> primary 2945 (duplicate low-z winds-insufficient caution)
- 28131 arXiv:0901.1880 -> primary 2946 ("radio mode" feedback; kinetic_radio_candidate, may need 2947 successor)

### B7 - arXiv:2508.06707 group (3 rows)
Mixed: one simulation-bounded need-for-AGN row, two scoped AGN-outflow rows.
- 28062 arXiv:2508.06707 -> primary 2943 (AGN disturbs ISM, weak kinetic transport; kinetic_radio_candidate)
- 28089 arXiv:2508.06707 -> primary 2946 (sims need AGN feedback; model-bounded)
- 28144 arXiv:2508.06707 -> primary 2943 (low-z AGN-host high-velocity outflows)

### B8 - AGN-outflow singles (2 rows)
Scoped AGN outflow evidence with model/broad-framing caveats.
- 28140 arXiv:2111.01801 -> primary 2943 (simulated inflows/outflows vs Seyfert obs)
- 28148 arXiv:2604.22922 -> primary 2943 (ultra-fast AGN outflows; broad-framing caution)

Coverage check: 8 + 5 + 2 + 3 + 2 = 20 pending rows, each exactly once.

## Lane order (per batch)
1. Goru - counts & locks first: confirm pending set matches this batch, verify hard locks in force, snapshot queue counts (docs-only read of the queue artifacts, no DB).
2. Lana - judgment review: source-position read on each row, propose decision_enum from the allowed set, flag any contested row.
3. Kun - reproducibility: confirm each proposed decision is reconstructable from the queue artifacts and snippet, record inputs so the call can be re-derived.
4. Tori - receipts & cockpit verification: write receipts, verify cockpit checkpoint text/marker, confirm counts moved as expected.
Hwao coordinates hand-offs and holds the stop authority between batches.

## Pre-dispatch cockpit checkpoint
Checkpoint text:
  "HWAO remaining-20 plan staged. 36-row queue: 16 completed, 20 pending across 5 batches (B4=8, B5=5, B6=2, B7=3, B8=2). Docs-only locks confirmed; NO ACTIVE EXECUTION PHRASE. Awaiting execution-phrase authorization before any row decision. B4 is next per B3 gate."
Checkpoint marker:
  HWAO_REMAINING20_COCKPIT_PREDISPATCH_20260705T085714Z

## Strict stop conditions
Stop immediately and hold if any of the following:
- No active execution phrase present when a row decision would be written (current state).
- Any action would touch SQL/apply/rollback, the DB (read or write), trust recompute, prose/wiki, deploy/restart, git, or cron/cloud/account/secret.
- Batch pending set does not match this plan's row list (Goru count mismatch).
- A row is contested between primary and alternate candidate and cannot be resolved from the queue artifacts alone.
- A kinetic_radio_candidate row (28076, 28131, 28062) would need a 2947-or-future narrow claim that does not yet exist.
- Any same-source sibling (e.g., 28066/28069/28070/28073) would be decided inconsistently within a batch.
- Gemini quota would be spent outside the single-contested-row exception.
On any stop: record the reason in the batch receipt, leave the row pending, escalate to Hwao/user.

## Gemini web decision
HOLD. Do not spend Gemini web quota now. Reserve it for a single specifically-contested row needing a separately-recorded supervised one-packet second opinion. Most likely candidates if contest arises: the kinetic_radio_candidate rows 28131 (radio mode) and 28062, and the model-bounded 28089 - but none are triggered yet.

## Handoff note
This is coordination/planning only. No decision_enum values are asserted; all 20 rows remain pending_source_position_and_human_adjudication. Execution requires an active phrase, which is not present.

HWAO_REMAINING20_PLAN_20260705T085714Z


## Goru precheck

**GORU PRECHECK REPORT**

**Status: PASS**
Hwao's 5 batches cover exactly the 20 pending rows in the queue, with each row appearing exactly once. No missing rows, no duplicates.

**Execution Locks Confirmed:**
- No product execution is unlocked (Active phrase is explicitly set to: NO ACTIVE EXECUTION PHRASE).
- All hard locks are in force: docs-only read, no DB read/writes, no SQL/apply/rollback, no trust recompute, no prose/wiki publish, no runtime deploy/restart, no git commit/push/merge, no cron/cloud/account/secret changes. Gemini web quota is held.

**Batch Counts:**
- **B4:** 8 rows
- **B5:** 5 rows
- **B6:** 2 rows
- **B7:** 3 rows
- **B8:** 2 rows
- **Total Pending Covered:** 20 rows

GORU_REMAINING20_PRECHECK_20260705T085714Z


## Pending rows context JSON

```json
{
  "pending_count": 20,
  "completed_count": 16,
  "pending_rows": [
    {
      "queue_id": "SPQ-2929-28062",
      "evidence_id": 28062,
      "title": "arXiv:2508.06707",
      "arxiv_id": "2508.06707v1",
      "url": "https://arxiv.org/abs/2508.06707",
      "summary_snippet": "[page58_neutral_seed_v1 gold_id=stance2b-002] These studies have demonstrated that AGN feedback can disturb the ISM gas to varying degrees, but the kinetic energy transport is almost always measured to be below 0.1% of the AGN bolometric luminosity.",
      "candidate_targets": [
        2943,
        2942
      ],
      "primary_candidate": 2943,
      "candidate_rationale": "AGN disturbs ISM but kinetic transport is weak; fits scoped outflow capability and caution against universal strength",
      "review_target_texts": {
        "2942": "AGN or SMBH feedback is a real but scoped quenching pathway in galaxy evolution, not a universal explanation for why galaxies stop forming stars.",
        "2943": "AGN activity can drive molecular, ionized, or neutral gas outflows capable of removing or depleting star-forming fuel in selected massive or AGN-host galaxies, with detection rates remaining tracer- and sample-dependent.",
        "2947": "Kinetic/radio-mode AGN feedback can mechanically couple jets or outflows to surrounding gas and inject kinetic or thermal energy in radio galaxies, galaxy groups/clusters, and simulations, but current evidence supports a context-dependent mechanism rather than a population-wide quenching channel."
      },
      "kinetic_radio_candidate": true,
      "same_source_other_held_evidence_ids": [
        28089,
        28144
      ],
      "status": "pending_source_position_and_human_adjudication",
      "decision_enum": "pending",
      "allowed_decisions": [
        "RELINK_EXISTING_ROW_TO_SCOPED_SUCCESSOR",
        "COPY_OR_SOURCEFILL_NEW_ROW_TO_SUCCESSOR_KEEP_PARENT_ARCHIVAL",
        "RETIRE_OR_REJECT_NON_AGN_GENERIC_DUPLICATE_OR_OUT_OF_SCOPE",
        "LEAVE_ARCHIVAL_ON_HIDDEN_PARENT_2929",
        "ROUTE_TO_KINETIC_RADIO_MODE_REVIEW_CANDIDATE_2947_OR_FUTURE_NARROW_CLAIM"
      ]
    },
    {
      "queue_id": "SPQ-2929-28066",
      "evidence_id": 28066,
      "title": "arXiv:2512.05584",
      "arxiv_id": "2512.05584v2",
      "url": "https://arxiv.org/abs/2512.05584",
      "summary_snippet": "[page58_neutral_seed_v1 gold_id=stance2b-007] We find that although the launch velocity of outflows in massive galaxies is higher, the gas cannot travel further than 100 kpc before falling back into the galaxy.",
      "candidate_targets": [
        2945,
        2943
      ],
      "primary_candidate": 2945,
      "candidate_rationale": "outflows in massive galaxies fall back within ~100 kpc; best as gas-removal/recycling caution, secondarily outflow scope",
      "review_target_texts": {
        "2943": "AGN activity can drive molecular, ionized, or neutral gas outflows capable of removing or depleting star-forming fuel in selected massive or AGN-host galaxies, with detection rates remaining tracer- and sample-dependent.",
        "2945": "Gas-reservoir language requires caution: central-kiloparsec depletion can occur in some AGN hosts, while other quenched systems retain large gas reservoirs or show low star-formation efficiency, so gas removal alone cannot explain every quenching pathway."
      },
      "kinetic_radio_candidate": false,
      "same_source_other_held_evidence_ids": [
        28069,
        28070,
        28073
      ],
      "status": "pending_source_position_and_human_adjudication",
      "decision_enum": "pending",
      "allowed_decisions": [
        "RELINK_EXISTING_ROW_TO_SCOPED_SUCCESSOR",
        "COPY_OR_SOURCEFILL_NEW_ROW_TO_SUCCESSOR_KEEP_PARENT_ARCHIVAL",
        "RETIRE_OR_REJECT_NON_AGN_GENERIC_DUPLICATE_OR_OUT_OF_SCOPE",
        "LEAVE_ARCHIVAL_ON_HIDDEN_PARENT_2929",
        "ROUTE_TO_KINETIC_RADIO_MODE_REVIEW_CANDIDATE_2947_OR_FUTURE_NARROW_CLAIM"
      ]
    },
    {
      "queue_id": "SPQ-2929-28069",
      "evidence_id": 28069,
      "title": "arXiv:2512.05584",
      "arxiv_id": "2512.05584v2",
      "url": "https://arxiv.org/abs/2512.05584",
      "summary_snippet": "[page58_neutral_seed_v1 gold_id=stance2b-010] Through combined analysis of Mg ii absorption in the CGM surrounding those galaxies using background QSOs, we for the first time provide observational evidence that stellar feedback drives strong enough outflows to cause the baryon deficiency in low-mass galaxies.",
      "candidate_targets": [
        2944
      ],
      "primary_candidate": 2944,
      "candidate_rationale": "stellar-feedback outflow/baryon-deficiency row is an alternative/qualifier, not AGN evidence",
      "review_target_texts": {
        "2944": "AGN feedback is one quenching axis among several; central/bulge/black-hole predictors, halo/environment/satellite pathways, strangulation, stripping, gas retention, low star-formation efficiency, and star-formation-driven outflows remain alternatives or qualifiers."
      },
      "kinetic_radio_candidate": false,
      "same_source_other_held_evidence_ids": [
        28066,
        28070,
        28073
      ],
      "status": "pending_source_position_and_human_adjudication",
      "decision_enum": "pending",
      "allowed_decisions": [
        "RELINK_EXISTING_ROW_TO_SCOPED_SUCCESSOR",
        "COPY_OR_SOURCEFILL_NEW_ROW_TO_SUCCESSOR_KEEP_PARENT_ARCHIVAL",
        "RETIRE_OR_REJECT_NON_AGN_GENERIC_DUPLICATE_OR_OUT_OF_SCOPE",
        "LEAVE_ARCHIVAL_ON_HIDDEN_PARENT_2929",
        "ROUTE_TO_KINETIC_RADIO_MODE_REVIEW_CANDIDATE_2947_OR_FUTURE_NARROW_CLAIM"
      ]
    },
    {
      "queue_id": "SPQ-2929-28070",
      "evidence_id": 28070,
      "title": "arXiv:2512.05584",
      "arxiv_id": "2512.05584v2",
      "url": "https://arxiv.org/abs/2512.05584",
      "summary_snippet": "[page58_neutral_seed_v1 gold_id=stance2b-011] In numerical simulations of galaxy formation and evolution, gas ejection launched by stellar feedback is introduced to explain the low baryon retention fraction in galaxies ( ? , ? , ? , ? ).",
      "candidate_targets": [
        2944
      ],
      "primary_candidate": 2944,
      "candidate_rationale": "stellar-feedback gas ejection in simulations is an alternative pathway/qualifier",
      "review_target_texts": {
        "2944": "AGN feedback is one quenching axis among several; central/bulge/black-hole predictors, halo/environment/satellite pathways, strangulation, stripping, gas retention, low star-formation efficiency, and star-formation-driven outflows remain alternatives or qualifiers."
      },
      "kinetic_radio_candidate": false,
      "same_source_other_held_evidence_ids": [
        28066,
        28069,
        28073
      ],
      "status": "pending_source_position_and_human_adjudication",
      "decision_enum": "pending",
      "allowed_decisions": [
        "RELINK_EXISTING_ROW_TO_SCOPED_SUCCESSOR",
        "COPY_OR_SOURCEFILL_NEW_ROW_TO_SUCCESSOR_KEEP_PARENT_ARCHIVAL",
        "RETIRE_OR_REJECT_NON_AGN_GENERIC_DUPLICATE_OR_OUT_OF_SCOPE",
        "LEAVE_ARCHIVAL_ON_HIDDEN_PARENT_2929",
        "ROUTE_TO_KINETIC_RADIO_MODE_REVIEW_CANDIDATE_2947_OR_FUTURE_NARROW_CLAIM"
      ]
    },
    {
      "queue_id": "SPQ-2929-28073",
      "evidence_id": 28073,
      "title": "arXiv:2512.05584",
      "arxiv_id": "2512.05584v2",
      "url": "https://arxiv.org/abs/2512.05584",
      "summary_snippet": "[page58_neutral_seed_v1 gold_id=stance2b-014] On the other hand, M ˙ out \\dot{M}_{\\rm out} and η \\eta have strong dependence on SFR \\rm SFR , confirming the stellar feedback-driven outflow scenario ( ? ).",
      "candidate_targets": [
        2944
      ],
      "primary_candidate": 2944,
      "candidate_rationale": "SFR-dependent stellar-feedback-driven outflows belong to alternatives/qualifiers",
      "review_target_texts": {
        "2944": "AGN feedback is one quenching axis among several; central/bulge/black-hole predictors, halo/environment/satellite pathways, strangulation, stripping, gas retention, low star-formation efficiency, and star-formation-driven outflows remain alternatives or qualifiers."
      },
      "kinetic_radio_candidate": false,
      "same_source_other_held_evidence_ids": [
        28066,
        28069,
        28070
      ],
      "status": "pending_source_position_and_human_adjudication",
      "decision_enum": "pending",
      "allowed_decisions": [
        "RELINK_EXISTING_ROW_TO_SCOPED_SUCCESSOR",
        "COPY_OR_SOURCEFILL_NEW_ROW_TO_SUCCESSOR_KEEP_PARENT_ARCHIVAL",
        "RETIRE_OR_REJECT_NON_AGN_GENERIC_DUPLICATE_OR_OUT_OF_SCOPE",
        "LEAVE_ARCHIVAL_ON_HIDDEN_PARENT_2929",
        "ROUTE_TO_KINETIC_RADIO_MODE_REVIEW_CANDIDATE_2947_OR_FUTURE_NARROW_CLAIM"
      ]
    },
    {
      "queue_id": "SPQ-2929-28075",
      "evidence_id": 28075,
      "title": "arXiv:0901.1880",
      "arxiv_id": "0901.1880v2",
      "url": "https://arxiv.org/abs/0901.1880",
      "summary_snippet": "[page58_neutral_seed_v1 gold_id=stance2b-016] At lower redshifts, efficient feedback is also needed in low mass objects, but winds are less likely to be sufficient to remove gas from galaxies ( maclow99 ; ferrara00 ) owing to their lower star formation rates.",
      "candidate_targets": [
        2945
      ],
      "primary_candidate": 2945,
      "candidate_rationale": "winds less sufficient to remove gas; supports gas-removal caution",
      "review_target_texts": {
        "2945": "Gas-reservoir language requires caution: central-kiloparsec depletion can occur in some AGN hosts, while other quenched systems retain large gas reservoirs or show low star-formation efficiency, so gas removal alone cannot explain every quenching pathway."
      },
      "kinetic_radio_candidate": false,
      "same_source_other_held_evidence_ids": [
        28110,
        28131
      ],
      "status": "pending_source_position_and_human_adjudication",
      "decision_enum": "pending",
      "allowed_decisions": [
        "RELINK_EXISTING_ROW_TO_SCOPED_SUCCESSOR",
        "COPY_OR_SOURCEFILL_NEW_ROW_TO_SUCCESSOR_KEEP_PARENT_ARCHIVAL",
        "RETIRE_OR_REJECT_NON_AGN_GENERIC_DUPLICATE_OR_OUT_OF_SCOPE",
        "LEAVE_ARCHIVAL_ON_HIDDEN_PARENT_2929",
        "ROUTE_TO_KINETIC_RADIO_MODE_REVIEW_CANDIDATE_2947_OR_FUTURE_NARROW_CLAIM"
      ]
    },
    {
      "queue_id": "SPQ-2929-28076",
      "evidence_id": 28076,
      "title": "A large, long-lived, slowly-expanding superbubble across the Perseus Arm",
      "arxiv_id": "2512.21927v1",
      "url": "https://arxiv.org/abs/2512.21927v1",
      "summary_snippet": "[page58_neutral_seed_v1 gold_id=stance2b-017] This supports a feedback cycle in which massive star explosions initially clear surrounding gas to create the cavity, while subsequent shockwaves compress nearby clouds, triggering new star formation.",
      "candidate_targets": [
        2944,
        2942
      ],
      "primary_candidate": 2944,
      "candidate_rationale": "massive-star feedback clears/compresses gas and can trigger star formation; alternative plus positive-feedback qualifier",
      "review_target_texts": {
        "2942": "AGN or SMBH feedback is a real but scoped quenching pathway in galaxy evolution, not a universal explanation for why galaxies stop forming stars.",
        "2944": "AGN feedback is one quenching axis among several; central/bulge/black-hole predictors, halo/environment/satellite pathways, strangulation, stripping, gas retention, low star-formation efficiency, and star-formation-driven outflows remain alternatives or qualifiers.",
        "2947": "Kinetic/radio-mode AGN feedback can mechanically couple jets or outflows to surrounding gas and inject kinetic or thermal energy in radio galaxies, galaxy groups/clusters, and simulations, but current evidence supports a context-dependent mechanism rather than a population-wide quenching channel."
      },
      "kinetic_radio_candidate": true,
      "same_source_other_held_evidence_ids": [
        28080,
        28083,
        28084
      ],
      "status": "pending_source_position_and_human_adjudication",
      "decision_enum": "pending",
      "allowed_decisions": [
        "RELINK_EXISTING_ROW_TO_SCOPED_SUCCESSOR",
        "COPY_OR_SOURCEFILL_NEW_ROW_TO_SUCCESSOR_KEEP_PARENT_ARCHIVAL",
        "RETIRE_OR_REJECT_NON_AGN_GENERIC_DUPLICATE_OR_OUT_OF_SCOPE",
        "LEAVE_ARCHIVAL_ON_HIDDEN_PARENT_2929",
        "ROUTE_TO_KINETIC_RADIO_MODE_REVIEW_CANDIDATE_2947_OR_FUTURE_NARROW_CLAIM"
      ]
    },
    {
      "queue_id": "SPQ-2929-28080",
      "evidence_id": 28080,
      "title": "A large, long-lived, slowly-expanding superbubble across the Perseus Arm",
      "arxiv_id": "2512.21927v1",
      "url": "https://arxiv.org/abs/2512.21927v1",
      "summary_snippet": "[page58_neutral_seed_v1 gold_id=stance2b-021] The fragmentation process highlights the role of feedback in dynamically influencing the formation and dispersal of star-forming regions on large scales.",
      "candidate_targets": [
        2944
      ],
      "primary_candidate": 2944,
      "candidate_rationale": "stellar/large-scale feedback influences star-forming regions; alternative axis",
      "review_target_texts": {
        "2944": "AGN feedback is one quenching axis among several; central/bulge/black-hole predictors, halo/environment/satellite pathways, strangulation, stripping, gas retention, low star-formation efficiency, and star-formation-driven outflows remain alternatives or qualifiers."
      },
      "kinetic_radio_candidate": false,
      "same_source_other_held_evidence_ids": [
        28076,
        28083,
        28084
      ],
      "status": "pending_source_position_and_human_adjudication",
      "decision_enum": "pending",
      "allowed_decisions": [
        "RELINK_EXISTING_ROW_TO_SCOPED_SUCCESSOR",
        "COPY_OR_SOURCEFILL_NEW_ROW_TO_SUCCESSOR_KEEP_PARENT_ARCHIVAL",
        "RETIRE_OR_REJECT_NON_AGN_GENERIC_DUPLICATE_OR_OUT_OF_SCOPE",
        "LEAVE_ARCHIVAL_ON_HIDDEN_PARENT_2929",
        "ROUTE_TO_KINETIC_RADIO_MODE_REVIEW_CANDIDATE_2947_OR_FUTURE_NARROW_CLAIM"
      ]
    },
    {
      "queue_id": "SPQ-2929-28082",
      "evidence_id": 28082,
      "title": "arXiv:1507.06366",
      "arxiv_id": "1507.06366v1",
      "url": "https://arxiv.org/abs/1507.06366",
      "summary_snippet": "[page58_neutral_seed_v1 gold_id=stance2b-023] It is widely believed that “feedback” from massive stars is responsible for the demise of GMCs , but exactly how this works is still poorly understood.",
      "candidate_targets": [
        2944
      ],
      "primary_candidate": 2944,
      "candidate_rationale": "massive-star feedback/GMC disruption is a non-AGN alternative/qualifier",
      "review_target_texts": {
        "2944": "AGN feedback is one quenching axis among several; central/bulge/black-hole predictors, halo/environment/satellite pathways, strangulation, stripping, gas retention, low star-formation efficiency, and star-formation-driven outflows remain alternatives or qualifiers."
      },
      "kinetic_radio_candidate": false,
      "same_source_other_held_evidence_ids": [],
      "status": "pending_source_position_and_human_adjudication",
      "decision_enum": "pending",
      "allowed_decisions": [
        "RELINK_EXISTING_ROW_TO_SCOPED_SUCCESSOR",
        "COPY_OR_SOURCEFILL_NEW_ROW_TO_SUCCESSOR_KEEP_PARENT_ARCHIVAL",
        "RETIRE_OR_REJECT_NON_AGN_GENERIC_DUPLICATE_OR_OUT_OF_SCOPE",
        "LEAVE_ARCHIVAL_ON_HIDDEN_PARENT_2929",
        "ROUTE_TO_KINETIC_RADIO_MODE_REVIEW_CANDIDATE_2947_OR_FUTURE_NARROW_CLAIM"
      ]
    },
    {
      "queue_id": "SPQ-2929-28083",
      "evidence_id": 28083,
      "title": "A large, long-lived, slowly-expanding superbubble across the Perseus Arm",
      "arxiv_id": "2512.21927v1",
      "url": "https://arxiv.org/abs/2512.21927v1",
      "summary_snippet": "[page58_neutral_seed_v1 gold_id=stance2b-024] It represents an extreme example of stellar feedback-driven structures in disk galaxies.",
      "candidate_targets": [
        2944
      ],
      "primary_candidate": 2944,
      "candidate_rationale": "stellar feedback-driven structures, non-AGN alternative",
      "review_target_texts": {
        "2944": "AGN feedback is one quenching axis among several; central/bulge/black-hole predictors, halo/environment/satellite pathways, strangulation, stripping, gas retention, low star-formation efficiency, and star-formation-driven outflows remain alternatives or qualifiers."
      },
      "kinetic_radio_candidate": false,
      "same_source_other_held_evidence_ids": [
        28076,
        28080,
        28084
      ],
      "status": "pending_source_position_and_human_adjudication",
      "decision_enum": "pending",
      "allowed_decisions": [
        "RELINK_EXISTING_ROW_TO_SCOPED_SUCCESSOR",
        "COPY_OR_SOURCEFILL_NEW_ROW_TO_SUCCESSOR_KEEP_PARENT_ARCHIVAL",
        "RETIRE_OR_REJECT_NON_AGN_GENERIC_DUPLICATE_OR_OUT_OF_SCOPE",
        "LEAVE_ARCHIVAL_ON_HIDDEN_PARENT_2929",
        "ROUTE_TO_KINETIC_RADIO_MODE_REVIEW_CANDIDATE_2947_OR_FUTURE_NARROW_CLAIM"
      ]
    },
    {
      "queue_id": "SPQ-2929-28084",
      "evidence_id": 28084,
      "title": "A large, long-lived, slowly-expanding superbubble across the Perseus Arm",
      "arxiv_id": "2512.21927v1",
      "url": "https://arxiv.org/abs/2512.21927v1",
      "summary_snippet": "[page58_neutral_seed_v1 gold_id=stance2b-025] Stellar feedback disrupts molecular clouds, thereby influencing the efficiency of star formation [ 14 , 15 ] .",
      "candidate_targets": [
        2944
      ],
      "primary_candidate": 2944,
      "candidate_rationale": "stellar feedback disrupts molecular clouds; star-formation-efficiency qualifier",
      "review_target_texts": {
        "2944": "AGN feedback is one quenching axis among several; central/bulge/black-hole predictors, halo/environment/satellite pathways, strangulation, stripping, gas retention, low star-formation efficiency, and star-formation-driven outflows remain alternatives or qualifiers."
      },
      "kinetic_radio_candidate": false,
      "same_source_other_held_evidence_ids": [
        28076,
        28080,
        28083
      ],
      "status": "pending_source_position_and_human_adjudication",
      "decision_enum": "pending",
      "allowed_decisions": [
        "RELINK_EXISTING_ROW_TO_SCOPED_SUCCESSOR",
        "COPY_OR_SOURCEFILL_NEW_ROW_TO_SUCCESSOR_KEEP_PARENT_ARCHIVAL",
        "RETIRE_OR_REJECT_NON_AGN_GENERIC_DUPLICATE_OR_OUT_OF_SCOPE",
        "LEAVE_ARCHIVAL_ON_HIDDEN_PARENT_2929",
        "ROUTE_TO_KINETIC_RADIO_MODE_REVIEW_CANDIDATE_2947_OR_FUTURE_NARROW_CLAIM"
      ]
    },
    {
      "queue_id": "SPQ-2929-28088",
      "evidence_id": 28088,
      "title": "Environmental Quenching of High-Redshift Galaxies: Interpreting JWST Observations with Simulations",
      "arxiv_id": "2605.03008v1",
      "url": "https://arxiv.org/abs/2605.03008",
      "summary_snippet": "[page58_neutral_seed_v1 gold_id=stance2b-030] Stellar feedback can regulate star formation in low- and intermediate-mass systems, but is generally insufficient to fully quench high-mass galaxies (Ciotti et al. , 1991 ; Springel and Hernquist, 2003 ) .",
      "candidate_targets": [
        2944
      ],
      "primary_candidate": 2944,
      "candidate_rationale": "stellar feedback limits and high-mass quenching context fit alternatives/qualifiers",
      "review_target_texts": {
        "2944": "AGN feedback is one quenching axis among several; central/bulge/black-hole predictors, halo/environment/satellite pathways, strangulation, stripping, gas retention, low star-formation efficiency, and star-formation-driven outflows remain alternatives or qualifiers."
      },
      "kinetic_radio_candidate": false,
      "same_source_other_held_evidence_ids": [],
      "status": "pending_source_position_and_human_adjudication",
      "decision_enum": "pending",
      "allowed_decisions": [
        "RELINK_EXISTING_ROW_TO_SCOPED_SUCCESSOR",
        "COPY_OR_SOURCEFILL_NEW_ROW_TO_SUCCESSOR_KEEP_PARENT_ARCHIVAL",
        "RETIRE_OR_REJECT_NON_AGN_GENERIC_DUPLICATE_OR_OUT_OF_SCOPE",
        "LEAVE_ARCHIVAL_ON_HIDDEN_PARENT_2929",
        "ROUTE_TO_KINETIC_RADIO_MODE_REVIEW_CANDIDATE_2947_OR_FUTURE_NARROW_CLAIM"
      ]
    },
    {
      "queue_id": "SPQ-2929-28089",
      "evidence_id": 28089,
      "title": "arXiv:2508.06707",
      "arxiv_id": "2508.06707v1",
      "url": "https://arxiv.org/abs/2508.06707",
      "summary_snippet": "[page58_neutral_seed_v1 gold_id=stance2b-031] Cosmological simulations have also shown that without AGN feedback, massive galaxies would continue to form stars rather than quench, leading to inconsistencies with the observed galaxy luminosity function and bimodal color distribution at z ∼ \\sim 0 (Di Matteo et al., 2005 ; Croton et al., 2006 ; Hopkins & Elvis, 2010 ) .",
      "candidate_targets": [
        2946,
        2942
      ],
      "primary_candidate": 2946,
      "candidate_rationale": "cosmological-simulation need for AGN feedback is model-bounded; secondarily scoped real pathway",
      "review_target_texts": {
        "2942": "AGN or SMBH feedback is a real but scoped quenching pathway in galaxy evolution, not a universal explanation for why galaxies stop forming stars.",
        "2946": "Preventive or maintenance feedback is distinct from ejective outflows; current maintenance/heating support in this source set remains model-dependent or simulation-bounded rather than a measured prevalence result."
      },
      "kinetic_radio_candidate": false,
      "same_source_other_held_evidence_ids": [
        28062,
        28144
      ],
      "status": "pending_source_position_and_human_adjudication",
      "decision_enum": "pending",
      "allowed_decisions": [
        "RELINK_EXISTING_ROW_TO_SCOPED_SUCCESSOR",
        "COPY_OR_SOURCEFILL_NEW_ROW_TO_SUCCESSOR_KEEP_PARENT_ARCHIVAL",
        "RETIRE_OR_REJECT_NON_AGN_GENERIC_DUPLICATE_OR_OUT_OF_SCOPE",
        "LEAVE_ARCHIVAL_ON_HIDDEN_PARENT_2929",
        "ROUTE_TO_KINETIC_RADIO_MODE_REVIEW_CANDIDATE_2947_OR_FUTURE_NARROW_CLAIM"
      ]
    },
    {
      "queue_id": "SPQ-2929-28110",
      "evidence_id": 28110,
      "title": "arXiv:0901.1880",
      "arxiv_id": "0901.1880",
      "url": "https://arxiv.org/abs/arXiv:0901.1880",
      "summary_snippet": "[page58_neutral_seed_v1 gold_id=stance2b-053] At lower redshifts, efficient feedback is also needed in low mass objects, but winds are less likely to be sufficient to remove gas from galaxies ( maclow99 ; ferrara00 ) owing to their lower star formation rates.",
      "candidate_targets": [
        2945
      ],
      "primary_candidate": 2945,
      "candidate_rationale": "duplicate low-redshift winds-insufficient-to-remove-gas caution",
      "review_target_texts": {
        "2945": "Gas-reservoir language requires caution: central-kiloparsec depletion can occur in some AGN hosts, while other quenched systems retain large gas reservoirs or show low star-formation efficiency, so gas removal alone cannot explain every quenching pathway."
      },
      "kinetic_radio_candidate": false,
      "same_source_other_held_evidence_ids": [
        28075,
        28131
      ],
      "status": "pending_source_position_and_human_adjudication",
      "decision_enum": "pending",
      "allowed_decisions": [
        "RELINK_EXISTING_ROW_TO_SCOPED_SUCCESSOR",
        "COPY_OR_SOURCEFILL_NEW_ROW_TO_SUCCESSOR_KEEP_PARENT_ARCHIVAL",
        "RETIRE_OR_REJECT_NON_AGN_GENERIC_DUPLICATE_OR_OUT_OF_SCOPE",
        "LEAVE_ARCHIVAL_ON_HIDDEN_PARENT_2929",
        "ROUTE_TO_KINETIC_RADIO_MODE_REVIEW_CANDIDATE_2947_OR_FUTURE_NARROW_CLAIM"
      ]
    },
    {
      "queue_id": "SPQ-2929-28114",
      "evidence_id": 28114,
      "title": "arXiv:1203.2926",
      "arxiv_id": "1203.2926v2",
      "url": "https://arxiv.org/abs/1203.2926",
      "summary_snippet": "[page58_neutral_seed_v1 gold_id=stance2b-081] On subgalactic scales, Krumholz & Matzner ( 2009 ) and Fall et al. ( 2010 ) argue that radiation pressure is the dominant feedback mechanism for massive young star clusters, and that winds driven by radiation momentum set the star formation efficiency in clusters and the cluster mass function.",
      "candidate_targets": [
        2944
      ],
      "primary_candidate": 2944,
      "candidate_rationale": "radiation-pressure feedback in star clusters is non-AGN stellar-feedback alternative",
      "review_target_texts": {
        "2944": "AGN feedback is one quenching axis among several; central/bulge/black-hole predictors, halo/environment/satellite pathways, strangulation, stripping, gas retention, low star-formation efficiency, and star-formation-driven outflows remain alternatives or qualifiers."
      },
      "kinetic_radio_candidate": false,
      "same_source_other_held_evidence_ids": [
        28118
      ],
      "status": "pending_source_position_and_human_adjudication",
      "decision_enum": "pending",
      "allowed_decisions": [
        "RELINK_EXISTING_ROW_TO_SCOPED_SUCCESSOR",
        "COPY_OR_SOURCEFILL_NEW_ROW_TO_SUCCESSOR_KEEP_PARENT_ARCHIVAL",
        "RETIRE_OR_REJECT_NON_AGN_GENERIC_DUPLICATE_OR_OUT_OF_SCOPE",
        "LEAVE_ARCHIVAL_ON_HIDDEN_PARENT_2929",
        "ROUTE_TO_KINETIC_RADIO_MODE_REVIEW_CANDIDATE_2947_OR_FUTURE_NARROW_CLAIM"
      ]
    },
    {
      "queue_id": "SPQ-2929-28118",
      "evidence_id": 28118,
      "title": "arXiv:1203.2926",
      "arxiv_id": "1203.2926v2",
      "url": "https://arxiv.org/abs/1203.2926",
      "summary_snippet": "[page58_neutral_seed_v1 gold_id=stance2b-085] In their approach, the code identifies contiguous star-forming clumps and then applies an outward radiation force to the gas in them.",
      "candidate_targets": [
        2944
      ],
      "primary_candidate": 2944,
      "candidate_rationale": "star-forming clump radiation-force model is non-AGN alternative/qualifier",
      "review_target_texts": {
        "2944": "AGN feedback is one quenching axis among several; central/bulge/black-hole predictors, halo/environment/satellite pathways, strangulation, stripping, gas retention, low star-formation efficiency, and star-formation-driven outflows remain alternatives or qualifiers."
      },
      "kinetic_radio_candidate": false,
      "same_source_other_held_evidence_ids": [
        28114
      ],
      "status": "pending_source_position_and_human_adjudication",
      "decision_enum": "pending",
      "allowed_decisions": [
        "RELINK_EXISTING_ROW_TO_SCOPED_SUCCESSOR",
        "COPY_OR_SOURCEFILL_NEW_ROW_TO_SUCCESSOR_KEEP_PARENT_ARCHIVAL",
        "RETIRE_OR_REJECT_NON_AGN_GENERIC_DUPLICATE_OR_OUT_OF_SCOPE",
        "LEAVE_ARCHIVAL_ON_HIDDEN_PARENT_2929",
        "ROUTE_TO_KINETIC_RADIO_MODE_REVIEW_CANDIDATE_2947_OR_FUTURE_NARROW_CLAIM"
      ]
    },
    {
      "queue_id": "SPQ-2929-28131",
      "evidence_id": 28131,
      "title": "arXiv:0901.1880",
      "arxiv_id": "0901.1880",
      "url": "https://arxiv.org/abs/arXiv:0901.1880",
      "summary_snippet": "[page58_neutral_seed_v1 gold_id=stance2b-098] This type of feedback from AGN is often called “radio mode” feedback, since it is believed to operate in massive radio galaxies.",
      "candidate_targets": [
        2946
      ],
      "primary_candidate": 2946,
      "candidate_rationale": "radio-mode feedback in massive radio galaxies maps to maintenance/preventive mode but may need kinetic-mode successor",
      "review_target_texts": {
        "2946": "Preventive or maintenance feedback is distinct from ejective outflows; current maintenance/heating support in this source set remains model-dependent or simulation-bounded rather than a measured prevalence result.",
        "2947": "Kinetic/radio-mode AGN feedback can mechanically couple jets or outflows to surrounding gas and inject kinetic or thermal energy in radio galaxies, galaxy groups/clusters, and simulations, but current evidence supports a context-dependent mechanism rather than a population-wide quenching channel."
      },
      "kinetic_radio_candidate": true,
      "same_source_other_held_evidence_ids": [
        28075,
        28110
      ],
      "status": "pending_source_position_and_human_adjudication",
      "decision_enum": "pending",
      "allowed_decisions": [
        "RELINK_EXISTING_ROW_TO_SCOPED_SUCCESSOR",
        "COPY_OR_SOURCEFILL_NEW_ROW_TO_SUCCESSOR_KEEP_PARENT_ARCHIVAL",
        "RETIRE_OR_REJECT_NON_AGN_GENERIC_DUPLICATE_OR_OUT_OF_SCOPE",
        "LEAVE_ARCHIVAL_ON_HIDDEN_PARENT_2929",
        "ROUTE_TO_KINETIC_RADIO_MODE_REVIEW_CANDIDATE_2947_OR_FUTURE_NARROW_CLAIM"
      ]
    },
    {
      "queue_id": "SPQ-2929-28140",
      "evidence_id": 28140,
      "title": "arXiv:2111.01801",
      "arxiv_id": "2111.01801v2",
      "url": "https://arxiv.org/abs/2111.01801",
      "summary_snippet": "[page58_neutral_seed_v1 gold_id=stance2b-107] In Section 4 we present our results, examining the inflows and outflows produced in our simulations as well as providing comparisons to recent observations of AGN-driven outflows in Seyfert galaxies.",
      "candidate_targets": [
        2943,
        2946
      ],
      "primary_candidate": 2943,
      "candidate_rationale": "simulated inflows/outflows compared to Seyfert observations; outflow claim with model caveat",
      "review_target_texts": {
        "2943": "AGN activity can drive molecular, ionized, or neutral gas outflows capable of removing or depleting star-forming fuel in selected massive or AGN-host galaxies, with detection rates remaining tracer- and sample-dependent.",
        "2946": "Preventive or maintenance feedback is distinct from ejective outflows; current maintenance/heating support in this source set remains model-dependent or simulation-bounded rather than a measured prevalence result."
      },
      "kinetic_radio_candidate": false,
      "same_source_other_held_evidence_ids": [],
      "status": "pending_source_position_and_human_adjudication",
      "decision_enum": "pending",
      "allowed_decisions": [
        "RELINK_EXISTING_ROW_TO_SCOPED_SUCCESSOR",
        "COPY_OR_SOURCEFILL_NEW_ROW_TO_SUCCESSOR_KEEP_PARENT_ARCHIVAL",
        "RETIRE_OR_REJECT_NON_AGN_GENERIC_DUPLICATE_OR_OUT_OF_SCOPE",
        "LEAVE_ARCHIVAL_ON_HIDDEN_PARENT_2929",
        "ROUTE_TO_KINETIC_RADIO_MODE_REVIEW_CANDIDATE_2947_OR_FUTURE_NARROW_CLAIM"
      ]
    },
    {
      "queue_id": "SPQ-2929-28144",
      "evidence_id": 28144,
      "title": "arXiv:2508.06707",
      "arxiv_id": "2508.06707v1",
      "url": "https://arxiv.org/abs/2508.06707",
      "summary_snippet": "[page58_neutral_seed_v1 gold_id=stance2b-111] Multiple studies at lower redshifts (z ∼ \\sim 0–1) have now detected powerful, high-velocity gas outflows in AGN host galaxies (Xu et al., 2019 , 2020 ; Villar Martín et al., 2021 ; Cicone et al., 2015 ; Morganti et al., 2021 ; Speranza et al., 2021 ; Harrison et al., 2014 ; Mullaney et al., 2013 ; Roy et al., 2021a ) .",
      "candidate_targets": [
        2943
      ],
      "primary_candidate": 2943,
      "candidate_rationale": "lower-redshift AGN-host high-velocity gas outflows fit scoped outflow claim",
      "review_target_texts": {
        "2943": "AGN activity can drive molecular, ionized, or neutral gas outflows capable of removing or depleting star-forming fuel in selected massive or AGN-host galaxies, with detection rates remaining tracer- and sample-dependent."
      },
      "kinetic_radio_candidate": false,
      "same_source_other_held_evidence_ids": [
        28062,
        28089
      ],
      "status": "pending_source_position_and_human_adjudication",
      "decision_enum": "pending",
      "allowed_decisions": [
        "RELINK_EXISTING_ROW_TO_SCOPED_SUCCESSOR",
        "COPY_OR_SOURCEFILL_NEW_ROW_TO_SUCCESSOR_KEEP_PARENT_ARCHIVAL",
        "RETIRE_OR_REJECT_NON_AGN_GENERIC_DUPLICATE_OR_OUT_OF_SCOPE",
        "LEAVE_ARCHIVAL_ON_HIDDEN_PARENT_2929",
        "ROUTE_TO_KINETIC_RADIO_MODE_REVIEW_CANDIDATE_2947_OR_FUTURE_NARROW_CLAIM"
      ]
    },
    {
      "queue_id": "SPQ-2929-28148",
      "evidence_id": 28148,
      "title": "Discovery of ultra-fast outflows with v$_{\\rm out}>0.3 \\rm c$ in local bright active galactic nuclei",
      "arxiv_id": "2604.22922",
      "url": "https://arxiv.org/abs/2604.22922",
      "summary_snippet": "[page58_neutral_seed_v1 gold_id=stance2b-115] AGN feedback, which is believed to be driven by powerful outflows from the accretion disk ( Silk98 ; Zubova12 ) , could be a promising mechanism to account for some of the most significant unresolved issues in astronomy, such as the underlying reasons for the strong correlation between SMBH mass and the stellar bulge velocity dispersion of the host galaxy (the M B ​ H − σ",
      "candidate_targets": [
        2943,
        2942
      ],
      "primary_candidate": 2943,
      "candidate_rationale": "ultra-fast AGN outflows as feedback mechanism; scoped outflow support with broad-framing caution",
      "review_target_texts": {
        "2942": "AGN or SMBH feedback is a real but scoped quenching pathway in galaxy evolution, not a universal explanation for why galaxies stop forming stars.",
        "2943": "AGN activity can drive molecular, ionized, or neutral gas outflows capable of removing or depleting star-forming fuel in selected massive or AGN-host galaxies, with detection rates remaining tracer- and sample-dependent."
      },
      "kinetic_radio_candidate": false,
      "same_source_other_held_evidence_ids": [],
      "status": "pending_source_position_and_human_adjudication",
      "decision_enum": "pending",
      "allowed_decisions": [
        "RELINK_EXISTING_ROW_TO_SCOPED_SUCCESSOR",
        "COPY_OR_SOURCEFILL_NEW_ROW_TO_SUCCESSOR_KEEP_PARENT_ARCHIVAL",
        "RETIRE_OR_REJECT_NON_AGN_GENERIC_DUPLICATE_OR_OUT_OF_SCOPE",
        "LEAVE_ARCHIVAL_ON_HIDDEN_PARENT_2929",
        "ROUTE_TO_KINETIC_RADIO_MODE_REVIEW_CANDIDATE_2947_OR_FUTURE_NARROW_CLAIM"
      ]
    }
  ],
  "source_groups": {
    "arXiv:2508.06707": [
      28062,
      28089,
      28144
    ],
    "arXiv:2512.05584": [
      28066,
      28069,
      28070,
      28073
    ],
    "arXiv:0901.1880": [
      28075,
      28110,
      28131
    ],
    "A large, long-lived, slowly-expanding superbubble across the Perseus Arm": [
      28076,
      28080,
      28083,
      28084
    ],
    "arXiv:1507.06366": [
      28082
    ],
    "Environmental Quenching of High-Redshift Galaxies: Interpreting JWST Observations with Simulations": [
      28088
    ],
    "arXiv:1203.2926": [
      28114,
      28118
    ],
    "arXiv:2111.01801": [
      28140
    ],
    "Discovery of ultra-fast outflows with v$_{\\rm out}>0.3 \\rm c$ in local bright active galactic nuclei": [
      28148
    ]
  },
  "completed_rows": [
    {
      "queue_id": "SPQ-2929-28060",
      "evidence_id": 28060,
      "title": "Surveying the Whirlpool at Arcseconds with NOEMA (SWAN). IV. Extent of active galactic nucleus feedback on the interstellar medium",
      "arxiv_id": "2604.15438",
      "url": "https://arxiv.org/abs/2604.15438",
      "summary_snippet": "[page58_neutral_seed_v1 gold_id=stance2b-000] Gas can be compressed along and at the peak of these massive outflows, leading to star formation activity known as positive AGN feedback ( Cresci2015TheMUSE ; Maiolino2017StarOutflow ; Gallagher2019WidespreadOutflows ; Shin2019Positive5728 ) .",
      "candidate_targets": [
        2942
      ],
      "primary_candidate": 2942,
      "candidate_rationale": "positive-feedback/compression row maps to scoped/non-universal feedback-sign language",
      "review_target_texts": {
        "2942": "AGN or SMBH feedback is a real but scoped quenching pathway in galaxy evolution, not a universal explanation for why galaxies stop forming stars."
      },
      "kinetic_radio_candidate": false,
      "same_source_other_held_evidence_ids": [
        28074,
        28091,
        28155
      ],
      "status": "reviewed_docs_only_no_sql",
      "decision_enum": "leave_archival",
      "allowed_decisions": [
        "RELINK_EXISTING_ROW_TO_SCOPED_SUCCESSOR",
        "COPY_OR_SOURCEFILL_NEW_ROW_TO_SUCCESSOR_KEEP_PARENT_ARCHIVAL",
        "RETIRE_OR_REJECT_NON_AGN_GENERIC_DUPLICATE_OR_OUT_OF_SCOPE",
        "LEAVE_ARCHIVAL_ON_HIDDEN_PARENT_2929",
        "ROUTE_TO_KINETIC_RADIO_MODE_REVIEW_CANDIDATE_2947_OR_FUTURE_NARROW_CLAIM"
      ]
    },
    {
      "queue_id": "SPQ-2929-28074",
      "evidence_id": 28074,
      "title": "Surveying the Whirlpool at Arcseconds with NOEMA (SWAN). IV. Extent of active galactic nucleus feedback on the interstellar medium",
      "arxiv_id": "2604.15438",
      "url": "https://arxiv.org/abs/2604.15438",
      "summary_snippet": "[page58_neutral_seed_v1 gold_id=stance2b-015] Unlike multiple indicators of kinetic feedback, the AGN is not in a radiative efficient mode of feedback, based on Chandra and the Nuclear Spectroscopic Telescope Array (NuSTAR) observations that point to a Compton thick accretion with an Eddington ratio of 10 4 10^{4} ( Brightman2018ANuSTAR ) .",
      "candidate_targets": [
        2942
      ],
      "primary_candidate": 2942,
      "candidate_rationale": "feedback-mode detail supports scoped/heterogeneous AGN-feedback framing, not a universal claim",
      "review_target_texts": {
        "2942": "AGN or SMBH feedback is a real but scoped quenching pathway in galaxy evolution, not a universal explanation for why galaxies stop forming stars."
      },
      "kinetic_radio_candidate": false,
      "same_source_other_held_evidence_ids": [
        28060,
        28091,
        28155
      ],
      "status": "reviewed_docs_only_no_sql",
      "decision_enum": "relink",
      "allowed_decisions": [
        "RELINK_EXISTING_ROW_TO_SCOPED_SUCCESSOR",
        "COPY_OR_SOURCEFILL_NEW_ROW_TO_SUCCESSOR_KEEP_PARENT_ARCHIVAL",
        "RETIRE_OR_REJECT_NON_AGN_GENERIC_DUPLICATE_OR_OUT_OF_SCOPE",
        "LEAVE_ARCHIVAL_ON_HIDDEN_PARENT_2929",
        "ROUTE_TO_KINETIC_RADIO_MODE_REVIEW_CANDIDATE_2947_OR_FUTURE_NARROW_CLAIM"
      ]
    },
    {
      "queue_id": "SPQ-2929-28087",
      "evidence_id": 28087,
      "title": "arXiv:2009.11175",
      "arxiv_id": "2009.11175v1",
      "url": "https://arxiv.org/abs/2009.11175",
      "summary_snippet": "[page58_neutral_seed_v1 gold_id=stance2b-029] However, the AGN feedback effect is likely to be complex, involving a range of physical mechanisms on different spatial scales.",
      "candidate_targets": [
        2942
      ],
      "primary_candidate": 2942,
      "candidate_rationale": "complex multi-mechanism AGN feedback supports scoped/non-universal framing",
      "review_target_texts": {
        "2942": "AGN or SMBH feedback is a real but scoped quenching pathway in galaxy evolution, not a universal explanation for why galaxies stop forming stars."
      },
      "kinetic_radio_candidate": false,
      "same_source_other_held_evidence_ids": [
        28095,
        28108,
        28111,
        28133
      ],
      "status": "reviewed_docs_only_no_sql",
      "decision_enum": "relink",
      "allowed_decisions": [
        "RELINK_EXISTING_ROW_TO_SCOPED_SUCCESSOR",
        "COPY_OR_SOURCEFILL_NEW_ROW_TO_SUCCESSOR_KEEP_PARENT_ARCHIVAL",
        "RETIRE_OR_REJECT_NON_AGN_GENERIC_DUPLICATE_OR_OUT_OF_SCOPE",
        "LEAVE_ARCHIVAL_ON_HIDDEN_PARENT_2929",
        "ROUTE_TO_KINETIC_RADIO_MODE_REVIEW_CANDIDATE_2947_OR_FUTURE_NARROW_CLAIM"
      ]
    },
    {
      "queue_id": "SPQ-2929-28091",
      "evidence_id": 28091,
      "title": "Surveying the Whirlpool at Arcseconds with NOEMA (SWAN). IV. Extent of active galactic nucleus feedback on the interstellar medium",
      "arxiv_id": "2604.15438",
      "url": "https://arxiv.org/abs/2604.15438",
      "summary_snippet": "[page58_neutral_seed_v1 gold_id=stance2b-033] But increased turbulence from outflows can also prevent the collapse of cold dense gas into stars, regulating star formation on longer timescales ( Choi2018TheGalaxies ; Wylezalek2020IonizedNuclei ; Gatto2024TheAGN ) .",
      "candidate_targets": [
        2943,
        2942
      ],
      "primary_candidate": 2943,
      "candidate_rationale": "AGN/outflow turbulence regulating star formation fits scoped outflow mechanism and mixed sign",
      "review_target_texts": {
        "2942": "AGN or SMBH feedback is a real but scoped quenching pathway in galaxy evolution, not a universal explanation for why galaxies stop forming stars.",
        "2943": "AGN activity can drive molecular, ionized, or neutral gas outflows capable of removing or depleting star-forming fuel in selected massive or AGN-host galaxies, with detection rates remaining tracer- and sample-dependent."
      },
      "kinetic_radio_candidate": false,
      "same_source_other_held_evidence_ids": [
        28060,
        28074,
        28155
      ],
      "status": "reviewed_docs_only_no_sql",
      "decision_enum": "relink",
      "allowed_decisions": [
        "RELINK_EXISTING_ROW_TO_SCOPED_SUCCESSOR",
        "COPY_OR_SOURCEFILL_NEW_ROW_TO_SUCCESSOR_KEEP_PARENT_ARCHIVAL",
        "RETIRE_OR_REJECT_NON_AGN_GENERIC_DUPLICATE_OR_OUT_OF_SCOPE",
        "LEAVE_ARCHIVAL_ON_HIDDEN_PARENT_2929",
        "ROUTE_TO_KINETIC_RADIO_MODE_REVIEW_CANDIDATE_2947_OR_FUTURE_NARROW_CLAIM"
      ]
    },
    {
      "queue_id": "SPQ-2929-28095",
      "evidence_id": 28095,
      "title": "arXiv:2009.11175",
      "arxiv_id": "2009.11175v1",
      "url": "https://arxiv.org/abs/2009.11175",
      "summary_snippet": "[page58_neutral_seed_v1 gold_id=stance2b-038] Although this feedback mode is often linked to winds driven by the radiation pressure of the central AGN (King & Pounds, 2015 ) , relativistic jets may play a significant role, even in cases in which the radio luminosity is relatively modest ( L 1.4 ​ GHz < 10 24 subscript 𝐿 1.4 GHz superscript 10 24 L_{1.4\\leavevmode\\nobreak\\ \\rm{GHz}}<10^{24} W Hz -1 ).",
      "candidate_targets": [
        2943,
        2946
      ],
      "primary_candidate": 2943,
      "candidate_rationale": "winds/jets mechanism; maps weakly to outflow claim but jet/radio-mode aspect may require separate kinetic-mode claim",
      "review_target_texts": {
        "2943": "AGN activity can drive molecular, ionized, or neutral gas outflows capable of removing or depleting star-forming fuel in selected massive or AGN-host galaxies, with detection rates remaining tracer- and sample-dependent.",
        "2946": "Preventive or maintenance feedback is distinct from ejective outflows; current maintenance/heating support in this source set remains model-dependent or simulation-bounded rather than a measured prevalence result.",
        "2947": "Kinetic/radio-mode AGN feedback can mechanically couple jets or outflows to surrounding gas and inject kinetic or thermal energy in radio galaxies, galaxy groups/clusters, and simulations, but current evidence supports a context-dependent mechanism rather than a population-wide quenching channel."
      },
      "kinetic_radio_candidate": true,
      "same_source_other_held_evidence_ids": [
        28087,
        28108,
        28111,
        28133
      ],
      "status": "reviewed_docs_only_no_sql",
      "decision_enum": "route_kinetic_radio",
      "allowed_decisions": [
        "RELINK_EXISTING_ROW_TO_SCOPED_SUCCESSOR",
        "COPY_OR_SOURCEFILL_NEW_ROW_TO_SUCCESSOR_KEEP_PARENT_ARCHIVAL",
        "RETIRE_OR_REJECT_NON_AGN_GENERIC_DUPLICATE_OR_OUT_OF_SCOPE",
        "LEAVE_ARCHIVAL_ON_HIDDEN_PARENT_2929",
        "ROUTE_TO_KINETIC_RADIO_MODE_REVIEW_CANDIDATE_2947_OR_FUTURE_NARROW_CLAIM"
      ]
    },
    {
      "queue_id": "SPQ-2929-28108",
      "evidence_id": 28108,
      "title": "arXiv:2009.11175",
      "arxiv_id": "2009.11175v1",
      "url": "https://arxiv.org/abs/2009.11175",
      "summary_snippet": "[page58_neutral_seed_v1 gold_id=stance2b-051] However, we do not yet fully understand how this feedback mechanism – jets acting on the cooler phases of the ISM – works in detail; there also remain considerable uncertainties about the masses and kinetic powers of the resulting jet-induced outflows, and the extent to which they can truly affect the evolution of the host galaxies.",
      "candidate_targets": [
        2942,
        2946
      ],
      "primary_candidate": 2942,
      "candidate_rationale": "uncertainties in jet-induced outflows support scoped/model-bounded caution",
      "review_target_texts": {
        "2942": "AGN or SMBH feedback is a real but scoped quenching pathway in galaxy evolution, not a universal explanation for why galaxies stop forming stars.",
        "2946": "Preventive or maintenance feedback is distinct from ejective outflows; current maintenance/heating support in this source set remains model-dependent or simulation-bounded rather than a measured prevalence result.",
        "2947": "Kinetic/radio-mode AGN feedback can mechanically couple jets or outflows to surrounding gas and inject kinetic or thermal energy in radio galaxies, galaxy groups/clusters, and simulations, but current evidence supports a context-dependent mechanism rather than a population-wide quenching channel."
      },
      "kinetic_radio_candidate": true,
      "same_source_other_held_evidence_ids": [
        28087,
        28095,
        28111,
        28133
      ],
      "status": "reviewed_docs_only_no_sql",
      "decision_enum": "route_kinetic_radio",
      "allowed_decisions": [
        "RELINK_EXISTING_ROW_TO_SCOPED_SUCCESSOR",
        "COPY_OR_SOURCEFILL_NEW_ROW_TO_SUCCESSOR_KEEP_PARENT_ARCHIVAL",
        "RETIRE_OR_REJECT_NON_AGN_GENERIC_DUPLICATE_OR_OUT_OF_SCOPE",
        "LEAVE_ARCHIVAL_ON_HIDDEN_PARENT_2929",
        "ROUTE_TO_KINETIC_RADIO_MODE_REVIEW_CANDIDATE_2947_OR_FUTURE_NARROW_CLAIM"
      ]
    },
    {
      "queue_id": "SPQ-2929-28111",
      "evidence_id": 28111,
      "title": "arXiv:2009.11175",
      "arxiv_id": "2009.11175v1",
      "url": "https://arxiv.org/abs/2009.11175",
      "summary_snippet": "[page58_neutral_seed_v1 gold_id=stance2b-054] Recent numerical simulations have also demonstrated that, despite their highly collimated nature, the relativistic jets of radio-loud AGN can inflate extensive bubbles of outflowing gas as they fight their way through the dense and inhomogeneous ISM in the central regions of galaxies (Wagner et al., 2013 ; Mukherjee et al., 2016 , 2018 ) .",
      "candidate_targets": [
        2946
      ],
      "primary_candidate": 2946,
      "candidate_rationale": "radio-loud AGN jets inflate bubbles in simulations; model/maintenance-bounded",
      "review_target_texts": {
        "2946": "Preventive or maintenance feedback is distinct from ejective outflows; current maintenance/heating support in this source set remains model-dependent or simulation-bounded rather than a measured prevalence result.",
        "2947": "Kinetic/radio-mode AGN feedback can mechanically couple jets or outflows to surrounding gas and inject kinetic or thermal energy in radio galaxies, galaxy groups/clusters, and simulations, but current evidence supports a context-dependent mechanism rather than a population-wide quenching channel."
      },
      "kinetic_radio_candidate": true,
      "same_source_other_held_evidence_ids": [
        28087,
        28095,
        28108,
        28133
      ],
      "status": "reviewed_docs_only_no_sql",
      "decision_enum": "route_kinetic_radio",
      "allowed_decisions": [
        "RELINK_EXISTING_ROW_TO_SCOPED_SUCCESSOR",
        "COPY_OR_SOURCEFILL_NEW_ROW_TO_SUCCESSOR_KEEP_PARENT_ARCHIVAL",
        "RETIRE_OR_REJECT_NON_AGN_GENERIC_DUPLICATE_OR_OUT_OF_SCOPE",
        "LEAVE_ARCHIVAL_ON_HIDDEN_PARENT_2929",
        "ROUTE_TO_KINETIC_RADIO_MODE_REVIEW_CANDIDATE_2947_OR_FUTURE_NARROW_CLAIM"
      ]
    },
    {
      "queue_id": "SPQ-2929-28123",
      "evidence_id": 28123,
      "title": "arXiv:2403.17145",
      "arxiv_id": "2403.17145v1",
      "url": "https://arxiv.org/abs/2403.17145",
      "summary_snippet": "[page58_neutral_seed_v1 gold_id=stance2b-090] While the inclusion of AGN feedback into hydrodynamical simulations allowed, for the first time, the reproduction of a wide range of properties of the galaxy populations, the choice of the feedback scheme in state-of-the-art hydrodynamical simulations vastly differs from one simulation to the other.",
      "candidate_targets": [
        2946,
        2942
      ],
      "primary_candidate": 2946,
      "candidate_rationale": "hydrodynamical simulation feedback-scheme dependence is model-bounded and supports caution",
      "review_target_texts": {
        "2942": "AGN or SMBH feedback is a real but scoped quenching pathway in galaxy evolution, not a universal explanation for why galaxies stop forming stars.",
        "2946": "Preventive or maintenance feedback is distinct from ejective outflows; current maintenance/heating support in this source set remains model-dependent or simulation-bounded rather than a measured prevalence result."
      },
      "kinetic_radio_candidate": false,
      "same_source_other_held_evidence_ids": [
        28127,
        28139,
        28143,
        28151,
        28158
      ],
      "status": "reviewed_docs_only_no_sql",
      "decision_enum": "relink",
      "allowed_decisions": [
        "RELINK_EXISTING_ROW_TO_SCOPED_SUCCESSOR",
        "COPY_OR_SOURCEFILL_NEW_ROW_TO_SUCCESSOR_KEEP_PARENT_ARCHIVAL",
        "RETIRE_OR_REJECT_NON_AGN_GENERIC_DUPLICATE_OR_OUT_OF_SCOPE",
        "LEAVE_ARCHIVAL_ON_HIDDEN_PARENT_2929",
        "ROUTE_TO_KINETIC_RADIO_MODE_REVIEW_CANDIDATE_2947_OR_FUTURE_NARROW_CLAIM"
      ]
    },
    {
      "queue_id": "SPQ-2929-28127",
      "evidence_id": 28127,
      "title": "arXiv:2403.17145",
      "arxiv_id": "2403.17145v1",
      "url": "https://arxiv.org/abs/2403.17145",
      "summary_snippet": "[page58_neutral_seed_v1 gold_id=stance2b-094] Cooling of the hot atmosphere supplies the central regions with fresh gas, igniting active galactic nuclei (AGN) with long duty cycles.",
      "candidate_targets": [
        2946,
        2945
      ],
      "primary_candidate": 2946,
      "candidate_rationale": "cooling hot atmosphere/AGN duty cycle belongs to maintenance/hot-gas context and gas-reservoir caution",
      "review_target_texts": {
        "2945": "Gas-reservoir language requires caution: central-kiloparsec depletion can occur in some AGN hosts, while other quenched systems retain large gas reservoirs or show low star-formation efficiency, so gas removal alone cannot explain every quenching pathway.",
        "2946": "Preventive or maintenance feedback is distinct from ejective outflows; current maintenance/heating support in this source set remains model-dependent or simulation-bounded rather than a measured prevalence result.",
        "2947": "Kinetic/radio-mode AGN feedback can mechanically couple jets or outflows to surrounding gas and inject kinetic or thermal energy in radio galaxies, galaxy groups/clusters, and simulations, but current evidence supports a context-dependent mechanism rather than a population-wide quenching channel."
      },
      "kinetic_radio_candidate": true,
      "same_source_other_held_evidence_ids": [
        28123,
        28139,
        28143,
        28151,
        28158
      ],
      "status": "reviewed_docs_only_no_sql",
      "decision_enum": "leave_archival",
      "allowed_decisions": [
        "RELINK_EXISTING_ROW_TO_SCOPED_SUCCESSOR",
        "COPY_OR_SOURCEFILL_NEW_ROW_TO_SUCCESSOR_KEEP_PARENT_ARCHIVAL",
        "RETIRE_OR_REJECT_NON_AGN_GENERIC_DUPLICATE_OR_OUT_OF_SCOPE",
        "LEAVE_ARCHIVAL_ON_HIDDEN_PARENT_2929",
        "ROUTE_TO_KINETIC_RADIO_MODE_REVIEW_CANDIDATE_2947_OR_FUTURE_NARROW_CLAIM"
      ]
    },
    {
      "queue_id": "SPQ-2929-28133",
      "evidence_id": 28133,
      "title": "arXiv:2009.11175",
      "arxiv_id": "2009.11175v1",
      "url": "https://arxiv.org/abs/2009.11175",
      "summary_snippet": "[page58_neutral_seed_v1 gold_id=stance2b-100] This has important implications for estimates of key outflow parameters such as the mass outflow rates, kinetic powers, and AGN feedback efficiencies.",
      "candidate_targets": [
        2943
      ],
      "primary_candidate": 2943,
      "candidate_rationale": "outflow parameters/feedback efficiencies fit scoped outflow evidence",
      "review_target_texts": {
        "2943": "AGN activity can drive molecular, ionized, or neutral gas outflows capable of removing or depleting star-forming fuel in selected massive or AGN-host galaxies, with detection rates remaining tracer- and sample-dependent."
      },
      "kinetic_radio_candidate": false,
      "same_source_other_held_evidence_ids": [
        28087,
        28095,
        28108,
        28111
      ],
      "status": "reviewed_docs_only_no_sql",
      "decision_enum": "leave_archival",
      "allowed_decisions": [
        "RELINK_EXISTING_ROW_TO_SCOPED_SUCCESSOR",
        "COPY_OR_SOURCEFILL_NEW_ROW_TO_SUCCESSOR_KEEP_PARENT_ARCHIVAL",
        "RETIRE_OR_REJECT_NON_AGN_GENERIC_DUPLICATE_OR_OUT_OF_SCOPE",
        "LEAVE_ARCHIVAL_ON_HIDDEN_PARENT_2929",
        "ROUTE_TO_KINETIC_RADIO_MODE_REVIEW_CANDIDATE_2947_OR_FUTURE_NARROW_CLAIM"
      ]
    },
    {
      "queue_id": "SPQ-2929-28139",
      "evidence_id": 28139,
      "title": "arXiv:2403.17145",
      "arxiv_id": "2403.17145v1",
      "url": "https://arxiv.org/abs/2403.17145",
      "summary_snippet": "[page58_neutral_seed_v1 gold_id=stance2b-106] Their gravitational potential well is strong enough to retain a substantial hot gaseous atmosphere (the IntraGroup Medium, hereafter IGrM), whereas the outflows generated by the central SMBH are energetic enough to produce clearly discernable effects in the surrounding medium.",
      "candidate_targets": [
        2946
      ],
      "primary_candidate": 2946,
      "candidate_rationale": "hot gaseous atmosphere plus SMBH outflows affecting surrounding medium is maintenance/hot-gas bounded",
      "review_target_texts": {
        "2946": "Preventive or maintenance feedback is distinct from ejective outflows; current maintenance/heating support in this source set remains model-dependent or simulation-bounded rather than a measured prevalence result.",
        "2947": "Kinetic/radio-mode AGN feedback can mechanically couple jets or outflows to surrounding gas and inject kinetic or thermal energy in radio galaxies, galaxy groups/clusters, and simulations, but current evidence supports a context-dependent mechanism rather than a population-wide quenching channel."
      },
      "kinetic_radio_candidate": true,
      "same_source_other_held_evidence_ids": [
        28123,
        28127,
        28143,
        28151,
        28158
      ],
      "status": "reviewed_docs_only_no_sql",
      "decision_enum": "leave_archival",
      "allowed_decisions": [
        "RELINK_EXISTING_ROW_TO_SCOPED_SUCCESSOR",
        "COPY_OR_SOURCEFILL_NEW_ROW_TO_SUCCESSOR_KEEP_PARENT_ARCHIVAL",
        "RETIRE_OR_REJECT_NON_AGN_GENERIC_DUPLICATE_OR_OUT_OF_SCOPE",
        "LEAVE_ARCHIVAL_ON_HIDDEN_PARENT_2929",
        "ROUTE_TO_KINETIC_RADIO_MODE_REVIEW_CANDIDATE_2947_OR_FUTURE_NARROW_CLAIM"
      ]
    },
    {
      "queue_id": "SPQ-2929-28141",
      "evidence_id": 28141,
      "title": "arXiv:1706.08987",
      "arxiv_id": "1706.08987v2",
      "url": "https://arxiv.org/abs/1706.08987",
      "summary_snippet": "[page58_neutral_seed_v1 gold_id=stance2b-108] Several SINFONI/VLT observations of z ∼ 1.5 − 2.5 similar-to 𝑧 1.5 2.5 z\\sim 1.5-2.5 QSOs indicate the presence of fast, galaxy-wide ionised outflows with a conical morphology that are spatially anti-correlated with the brightest actively star forming region in the host galaxy (Cano-Díaz et al., 2012 ; Carniani et al., 2015b ; Cresci et al., 2015 ; Carniani et al., 2016 )",
      "candidate_targets": [
        2943
      ],
      "primary_candidate": 2943,
      "candidate_rationale": "z~1.5–2.5 QSO galaxy-wide ionized outflows anti-correlated with star formation fits scoped outflow claim",
      "review_target_texts": {
        "2943": "AGN activity can drive molecular, ionized, or neutral gas outflows capable of removing or depleting star-forming fuel in selected massive or AGN-host galaxies, with detection rates remaining tracer- and sample-dependent."
      },
      "kinetic_radio_candidate": false,
      "same_source_other_held_evidence_ids": [],
      "status": "reviewed_docs_only_no_sql",
      "decision_enum": "relink",
      "allowed_decisions": [
        "RELINK_EXISTING_ROW_TO_SCOPED_SUCCESSOR",
        "COPY_OR_SOURCEFILL_NEW_ROW_TO_SUCCESSOR_KEEP_PARENT_ARCHIVAL",
        "RETIRE_OR_REJECT_NON_AGN_GENERIC_DUPLICATE_OR_OUT_OF_SCOPE",
        "LEAVE_ARCHIVAL_ON_HIDDEN_PARENT_2929",
        "ROUTE_TO_KINETIC_RADIO_MODE_REVIEW_CANDIDATE_2947_OR_FUTURE_NARROW_CLAIM"
      ]
    },
    {
      "queue_id": "SPQ-2929-28143",
      "evidence_id": 28143,
      "title": "arXiv:2403.17145",
      "arxiv_id": "2403.17145v1",
      "url": "https://arxiv.org/abs/2403.17145",
      "summary_snippet": "[page58_neutral_seed_v1 gold_id=stance2b-110] We can see that for low-mass (i.e. low-temperature) systems, the available BH energy largely exceeds the binding energy of gas particles in halo cores, such that the energy supplied by AGN feedback is sufficient to unbind gas particles and eject them from the halo.",
      "candidate_targets": [
        2946,
        2943
      ],
      "primary_candidate": 2946,
      "candidate_rationale": "BH energy unbinding halo-core gas in simulations is model-bounded; secondarily gas ejection/outflow",
      "review_target_texts": {
        "2943": "AGN activity can drive molecular, ionized, or neutral gas outflows capable of removing or depleting star-forming fuel in selected massive or AGN-host galaxies, with detection rates remaining tracer- and sample-dependent.",
        "2946": "Preventive or maintenance feedback is distinct from ejective outflows; current maintenance/heating support in this source set remains model-dependent or simulation-bounded rather than a measured prevalence result."
      },
      "kinetic_radio_candidate": false,
      "same_source_other_held_evidence_ids": [
        28123,
        28127,
        28139,
        28151,
        28158
      ],
      "status": "reviewed_docs_only_no_sql",
      "decision_enum": "leave_archival",
      "allowed_decisions": [
        "RELINK_EXISTING_ROW_TO_SCOPED_SUCCESSOR",
        "COPY_OR_SOURCEFILL_NEW_ROW_TO_SUCCESSOR_KEEP_PARENT_ARCHIVAL",
        "RETIRE_OR_REJECT_NON_AGN_GENERIC_DUPLICATE_OR_OUT_OF_SCOPE",
        "LEAVE_ARCHIVAL_ON_HIDDEN_PARENT_2929",
        "ROUTE_TO_KINETIC_RADIO_MODE_REVIEW_CANDIDATE_2947_OR_FUTURE_NARROW_CLAIM"
      ]
    },
    {
      "queue_id": "SPQ-2929-28151",
      "evidence_id": 28151,
      "title": "arXiv:2403.17145",
      "arxiv_id": "2403.17145v1",
      "url": "https://arxiv.org/abs/2403.17145",
      "summary_snippet": "[page58_neutral_seed_v1 gold_id=stance2b-118] In terms of the sensitivity to AGN feedback, galaxy groups occupy a transitional regime between isolated galaxies and massive galaxy clusters, as the total feedback energy is comparable to the gravitational binding energy of the gas.",
      "candidate_targets": [
        2946
      ],
      "primary_candidate": 2946,
      "candidate_rationale": "groups as transitional feedback-energy/binding-energy regime is model/maintenance bounded",
      "review_target_texts": {
        "2946": "Preventive or maintenance feedback is distinct from ejective outflows; current maintenance/heating support in this source set remains model-dependent or simulation-bounded rather than a measured prevalence result."
      },
      "kinetic_radio_candidate": false,
      "same_source_other_held_evidence_ids": [
        28123,
        28127,
        28139,
        28143,
        28158
      ],
      "status": "reviewed_docs_only_no_sql",
      "decision_enum": "relink",
      "allowed_decisions": [
        "RELINK_EXISTING_ROW_TO_SCOPED_SUCCESSOR",
        "COPY_OR_SOURCEFILL_NEW_ROW_TO_SUCCESSOR_KEEP_PARENT_ARCHIVAL",
        "RETIRE_OR_REJECT_NON_AGN_GENERIC_DUPLICATE_OR_OUT_OF_SCOPE",
        "LEAVE_ARCHIVAL_ON_HIDDEN_PARENT_2929",
        "ROUTE_TO_KINETIC_RADIO_MODE_REVIEW_CANDIDATE_2947_OR_FUTURE_NARROW_CLAIM"
      ]
    },
    {
      "queue_id": "SPQ-2929-28155",
      "evidence_id": 28155,
      "title": "Surveying the Whirlpool at Arcseconds with NOEMA (SWAN). IV. Extent of active galactic nucleus feedback on the interstellar medium",
      "arxiv_id": "2604.15438",
      "url": "https://arxiv.org/abs/2604.15438",
      "summary_snippet": "[page58_neutral_seed_v1 gold_id=stance2b-122] Contemporary theoretical works point to AGNs as an essential modulator for galaxy growth and the cessation of star formation, requiring some form of AGN feedback to reproduce observed galaxy populations ( Somerville2015SouthSciences ; Leslie2016QuenchingSequence ; Husemann2018RealityFeedback ) .",
      "candidate_targets": [
        2942,
        2946
      ],
      "primary_candidate": 2942,
      "candidate_rationale": "theoretical/simulation need for AGN feedback supports real-but-scoped pathway and model-boundedness",
      "review_target_texts": {
        "2942": "AGN or SMBH feedback is a real but scoped quenching pathway in galaxy evolution, not a universal explanation for why galaxies stop forming stars.",
        "2946": "Preventive or maintenance feedback is distinct from ejective outflows; current maintenance/heating support in this source set remains model-dependent or simulation-bounded rather than a measured prevalence result."
      },
      "kinetic_radio_candidate": false,
      "same_source_other_held_evidence_ids": [
        28060,
        28074,
        28091
      ],
      "status": "reviewed_docs_only_no_sql",
      "decision_enum": "relink",
      "allowed_decisions": [
        "RELINK_EXISTING_ROW_TO_SCOPED_SUCCESSOR",
        "COPY_OR_SOURCEFILL_NEW_ROW_TO_SUCCESSOR_KEEP_PARENT_ARCHIVAL",
        "RETIRE_OR_REJECT_NON_AGN_GENERIC_DUPLICATE_OR_OUT_OF_SCOPE",
        "LEAVE_ARCHIVAL_ON_HIDDEN_PARENT_2929",
        "ROUTE_TO_KINETIC_RADIO_MODE_REVIEW_CANDIDATE_2947_OR_FUTURE_NARROW_CLAIM"
      ]
    },
    {
      "queue_id": "SPQ-2929-28158",
      "evidence_id": 28158,
      "title": "arXiv:2403.17145",
      "arxiv_id": "2403.17145v1",
      "url": "https://arxiv.org/abs/2403.17145",
      "summary_snippet": "[page58_neutral_seed_v1 gold_id=stance2b-125] Bubbles of outflowing material associated with successive outbursts of the central SMBH expand into the surrounding medium, producing pairs of cavities in the hot gas distribution (Bîrzan et al., 2008 ) .",
      "candidate_targets": [
        2946
      ],
      "primary_candidate": 2946,
      "candidate_rationale": "SMBH outburst bubbles/cavities in hot gas are maintenance/hot-atmosphere evidence",
      "review_target_texts": {
        "2946": "Preventive or maintenance feedback is distinct from ejective outflows; current maintenance/heating support in this source set remains model-dependent or simulation-bounded rather than a measured prevalence result.",
        "2947": "Kinetic/radio-mode AGN feedback can mechanically couple jets or outflows to surrounding gas and inject kinetic or thermal energy in radio galaxies, galaxy groups/clusters, and simulations, but current evidence supports a context-dependent mechanism rather than a population-wide quenching channel."
      },
      "kinetic_radio_candidate": true,
      "same_source_other_held_evidence_ids": [
        28123,
        28127,
        28139,
        28143,
        28151
      ],
      "status": "reviewed_docs_only_no_sql",
      "decision_enum": "relink",
      "allowed_decisions": [
        "RELINK_EXISTING_ROW_TO_SCOPED_SUCCESSOR",
        "COPY_OR_SOURCEFILL_NEW_ROW_TO_SUCCESSOR_KEEP_PARENT_ARCHIVAL",
        "RETIRE_OR_REJECT_NON_AGN_GENERIC_DUPLICATE_OR_OUT_OF_SCOPE",
        "LEAVE_ARCHIVAL_ON_HIDDEN_PARENT_2929",
        "ROUTE_TO_KINETIC_RADIO_MODE_REVIEW_CANDIDATE_2947_OR_FUTURE_NARROW_CLAIM"
      ]
    }
  ]
}

```

## Public source contexts JSON

```json
{
  "0901.1880": {
    "abstract": "We compare the properties of galaxies that form in a cosmological simulation without strong feedback to observations at z=0. We confirm previous findings that models without strong feedback overproduce the observed galaxy baryonic mass function, especially at the low and high mass extremes. Through post-processing we investigate what kinds of feedback would be required to reproduce observed galaxy masses and star formation rates. To mimic an extreme form of &#34;preventive&#34; feedback (e.g., AGN radio mode) we remove all baryonic mass that was originally accreted via &#34;hot mode&#34; from shock-heated gas. This does not bring the high mass end of the galaxy mass function into agreement with observations because much of the stellar mass in these systems formed at high redshift from baryons that originally accreted via &#34;cold mode&#34; onto lower mass progenitors. An efficient &#34;ejective&#34; feedback mechanism, such as supernova driven winds, must reduce the masses of these progenitors. Feedback must also reduce the masses of lower mass z=0 galaxies, which assemble at lower redshifts and have much lower star formation rates. If we monotonically re-map galaxy masses to reproduce the observed mass function, but retain the simulation&#39;s predicted star formation rates, we obtain fairly good agreement with the observed sequence of star-forming galaxies but fail to recover the observed population of passive, low star formation rate galaxies. Suppressing all hot mode accretion improves agreement for high mass galaxies but worsens the agreement at intermediate masses. Reproducing these z=0 observations requires a feedback mechanism that dramatically suppresses star formation in a fraction of galaxies, increasing with mass, while leaving star formation rates of other galaxies essentially unchanged.",
    "bytes": 46329,
    "http_status": 200,
    "ok": true,
    "title": "Galaxies in a Simulated $Λ$CDM Universe II: Observable Properties and Constraints on Feedback",
    "url": "https://arxiv.org/abs/0901.1880"
  },
  "1203.2926": {
    "abstract": "[abridged] The pressure exerted by the radiation of young stars may be an important feedback mechanism in forming star clusters and the disks of starburst galaxies. However, there is great uncertainty in how efficiently radiation couples to matter in these high optical depth environments. In particular, it is unclear what levels of turbulence the radiation can produce, and whether the infrared radiation trapped by the dust opacity can give rise to heavily mass-loaded winds. In this paper we report a series of two-dimensional flux-limited diffusion radiation-hydrodynamics calculations performed with the code ORION in which we drive strong radiation fluxes through columns of dusty matter confined by gravity. We consider both systems where the radiation flux is sub-Eddington throughout the gas column, and where it is super-Eddington at the midplane but sub-Eddington in the atmosphere. In the latter, we find that the radiation-matter interaction gives rise to radiation-driven Rayleigh-Taylor instability, which drives supersonic turbulence at a level sufficient to fully explain the turbulence seen in Galactic protocluster gas clouds, and to make a non-trivial contribution to the turbulence observed in starburst galaxy disks. However, the instability also produces a channel structure in which the radiation-matter interaction is reduced because the radiation field is not fully trapped. For astrophysical parameters relevant to forming star clusters and starburst galaxies, we find that this effect reduces the net momentum deposition rate in the dusty gas by a factor of ~2-6 compared to simple analytic estimates, and that in steady state the Eddington ratio reaches unity and there are no strong winds. We provide an approximation formula, appropriate for implementation in analytic models and non-radiative simulations, for the force exerted by the infrared radiation field in this regime.",
    "bytes": 46342,
    "http_status": 200,
    "ok": true,
    "title": "Direct Numerical Simulation of Radiation Pressure-Driven Turbulence and Winds in Star Clusters and Galactic Disks",
    "url": "https://arxiv.org/abs/1203.2926"
  },
  "1507.06366": {
    "abstract": "Radiation feedback from young star clusters embedded in giant molecular clouds (GMCs) is believed to be important to the control of star formation. For the most massive and dense clouds, including those in which super star clusters (SSCs) are born, pressure from reprocessed radiation exerted on dust grains may disperse a significant portion of the cloud mass back into the interstellar medium (ISM). Using our radiaton hydrodynamics (RHD) code, Hyperion, we conduct a series of numerical simulations to test this idea. Our models follow the evolution of self-gravitating, strongly turbulent clouds in which collapsing regions are replaced by radiating sink particles representing stellar clusters. We evaluate the dependence of the star formation efficiency (SFE) on the size and mass of the cloud and $\\kappa$, the opacity of the gas to infrared (IR) radiation. We find that the single most important parameter determining the evolutionary outcome is $\\kappa$, with $\\kappa \\gtrsim 15 \\text{ cm}^2 \\text{ g}^{-1}$ needed to disrupt clouds. For $\\kappa = 20-40 \\text{ cm}^2 \\text{ g}^{-1}$, the resulting SFE=50-70% is similar to empirical estimates for some SSC-forming clouds. The opacities required for GMC disruption likely apply only in dust-enriched environments. We find that the subgrid model approach of boosting the direct radiation force $L/c$ by a &#34;trapping factor&#34; equal to a cloud&#39;s mean IR optical depth can overestimate the true radiation force by factors of $\\sim 4-5$. We conclude that feedback from reprocessed IR radiation alone is unlikely to significantly reduce star formation within GMCs unless their dust abundances or cluster light-to-mass ratios are enhanced.",
    "bytes": 45524,
    "http_status": 200,
    "ok": true,
    "title": "Numerical Simulations of Turbulent Molecular Clouds Regulated by Reprocessed Radiation Feedback from Nascent Super Star Clusters",
    "url": "https://arxiv.org/abs/1507.06366"
  },
  "2111.01801": {
    "abstract": "Recent observations of Seyfert galaxies indicate that low power, misaligned jets can undergo significant interaction with the gas in the galactic disc and may be able to drive large-scale, multiphase outflows. We apply our novel sub-grid model for Blandford-Znajek jets to simulations of the central regions of Seyferts, in which a black hole is embedded in a dense, sub-kpc circumnuclear disc (CND) and surrounded by a dilute circumgalactic medium (CGM). We find that the variability of the accretion flow is highly sensitive both to the jet power and to the CND thermodynamics and, ultimately, is determined by the complex interplay between jet-driven outflows and backflows. Even at moderate Eddington ratios, AGN jets are able to significantly alter the thermodynamics and kinematics of CNDs and entrain up to 10% of their mass in the outflow. Mass outflow rates and kinetic powers of the warm outflowing component are in agreement with recent observations for black holes with similar bolometric luminosities, with outflow velocities that are able to reach 500 km/s. Depending on their power and direction, jets are able to drive a wide variety of large-scale outflows, ranging from light, hot and collimated structures to highly mass-loaded, multiphase, bipolar winds. This diversity of jet-driven outflows highlights the importance of applying physically motivated models of AGN feedback to realistic galaxy formation contexts. Such simulations will play a crucial role in accurately interpreting the wealth of data that next generation facilities such as JWST, SKA and Athena will provide.",
    "bytes": 45435,
    "http_status": 200,
    "ok": true,
    "title": "Blandford-Znajek jets in galaxy formation simulations: exploring the diversity of outflows produced by spin-driven AGN jets in Seyfert galaxies",
    "url": "https://arxiv.org/abs/2111.01801"
  },
  "2508.06707": {
    "abstract": "We present spatially resolved maps of morphology, kinematics, and energetics of warm ionized gas in six powerful radio galaxies at z=3.5-4, using JWST/NIRSpec IFU to quantify jet-driven feedback in the early universe. All sources exhibit broad [OIII] emission-line profiles with W80 (line width) values of 950-2500 km/s across $\\sim$10s of kpc, signifying large-scale outflows. The outflowing nebulae are preferentially aligned with the radio jet axis, suggesting jet-driven origin. On average, the regions with the broadest lines and highest velocities are co-spatial with radio lobes or cores, and exhibit the strongest kinetic power. Ionized gas masses associated with the outflows span 1 to 8 $\\times 10^{9} \\ M_\\odot$, with total mass outflow rates of 80-950 Msun/yr and kinetic powers between 10^{43.2} and 10^{45.0} erg/s. The outflow kinetic power corresponds to 0.15%-2% of the AGN bolometric luminosity, sufficient to impact galaxy evolution. However, only $\\lesssim 1$\\% of the jet mechanical energy couples to the warm ionized gas via outflows, consistent with predictions from hydrodynamic simulations. A large fraction of the jet energy may instead reside in shock-heated hot gas, supported by X-ray detection, or used to thermalize the gas and produce the observed emission-line nebulae. Our results demonstrate that radio jets in massive, gas-rich systems at high-redshift can inject significant kinetic and thermal energy to the surroundings, providing direct evidence for jet-driven feedback operating during the peak epoch of galaxy formation.",
    "bytes": 43528,
    "http_status": 200,
    "ok": true,
    "title": "Mapping Jet-Gas Coupling and energetic ionized outflows in High-Redshift Radio Galaxies with JWST/NIRSpec",
    "url": "https://arxiv.org/abs/2508.06707"
  },
  "2512.05584": {
    "abstract": "Stellar feedback, as a key process regulating the baryon cycle, is thought to greatly redistribute baryonic material inside and outside the dark matter halos (DMHs), however the observational evidences are lacking. Through stacking analyses of ~400,000 galaxy spectra from Dark Energy Spectroscopic Instrument (DESI), we find star formation driven cool outflows in Mg II absorption line. Assuming only gravity acts on the launched gas, our calculations reveal that outflows from low mass galaxies ($M_*&lt;10^{10}\\,\\rm M_\\odot$) are capable of escaping beyond the DMHs, which aligns well with our finding in the circumgalactic medium (CGM) absorption along the minor-axes of galaxies using background quasars. This research offers indirect evidence that stellar feedback drives the low baryon retention rate in low-mass haloes, implicating that baryonic processes within galaxies are connected with the diffuse matter beyond the DMHs.",
    "bytes": 42836,
    "http_status": 200,
    "ok": true,
    "title": "Stellar feedback drives the baryon deficiency in low-mass galaxies",
    "url": "https://arxiv.org/abs/2512.05584"
  },
  "2512.21927": {
    "abstract": "Stellar feedback is a crucial mechanism in galactic evolution, as demonstrated by the widespread bubbles observed with JWST. In this study, we combine data from Gaia and LAMOST to obtain a sample of young O-B2 stars with full three-dimensional velocity information. Focusing on the largest known superbubble in the Milky Way, we identify groups of O-B2 stars at its periphery, exhibiting a transverse velocity of 25.8 km/s and an expansion velocity of 6.2 km/s. Using these velocities, we calculate a crossing time t_cross ~ 20 Myr and an expansion timescale t_expansion ~ 80 Myr. We estimate a survival timescale t_survival ~ 250 Myr and a supernova interval t_SN ~ 0.1 Myr. Together with the Galactic shear timescale t_shear ~ 30 Myr, these values satisfy t_SN &lt; t_shear &lt; t_survival. The energy and momentum from supernovae are sufficient to sustain the bubble&#39;s growth against ambient pressure. This indicates that repeated supernovae replenish energy faster than shear and turbulent distort the cavity. Our analysis classifies the Giant Oval Cavity as a large, quasi-stationary superbubble, similar to the Phantom Bubble observed by JWST, stabilised by the interplay between stellar feedback and Galactic disk dynamics.",
    "bytes": 44810,
    "ok": true,
    "status": 200,
    "title": "A large, long-lived, slowly-expanding superbubble across the Perseus Arm",
    "url": "https://arxiv.org/abs/2512.21927"
  },
  "2604.22922": {
    "abstract": "Ultra-fast outflows (UFOs) are mildly relativistic (outflow velocity $v_{out}&gt;0.1c$) nuclear winds detected as blueshifted absorption lines from highly ionized, dense gas in the X-ray spectra of active galactic nuclei. The AGN feedback mechanism is believed to be powered by these outflows, which can inject a large amount of energy and momentum into the surrounding interstellar medium, shaping the coevolution of the AGNs and their host galaxies. We performed a systematic search and rigorous statistical assessment of the presence of UFOs in the 7-12 keV band, in a sample of bright local AGNs. This study also aims to understand whether the presence and characteristics of UFOs depend on the state of the sources, by studying the relations between the incidence of UFOs and the accretion properties of AGNs. We collected X-ray spectroscopic flux-limited XMM data of 33 observations of local (z&lt;0.2) type 1 AGNs. We modeled their spectra in the 2-12 keV band using a combination of direct-continuum and reflection components and searched for absorption features. This represents the first systematic search for UFOs up to 12 keV. We performed Monte Carlo simulations to assess the statistical significance of the detected lines. We report strong detections of UFOs in six sources of the sample at the &gt;95% confidence level via MC simulations, corresponding to a fraction of 18% in our sample. From the observed energies of each absorption line, we evaluated the respective wind velocities, which in some cases exceed 40\\% of the speed of light. The velocity distribution found in this work is therefore shifted to higher energies than those found in previous searches for UFOs in local sources, which were limited to 10 keV. Moreover, our analysis shows no correlation between the accretion properties of the SMBHs and the presence of winds. Furthermore, our study highlights the temporal variability of UFOs.",
    "bytes": 45917,
    "http_status": 200,
    "ok": true,
    "title": "Discovery of ultra-fast outflows with v$_{\\rm out}&gt;0.3 \\rm c$ in local bright active galactic nuclei",
    "url": "https://arxiv.org/abs/2604.22922"
  },
  "2605.03008": {
    "abstract": "Recent observations of the high-redshift Universe, particularly with JWST, have revealed a population of quenched galaxies that challenges current galaxy formation models, which systematically underpredict their abundance. This discrepancy has been extensively studied for massive systems, motivating revisions to internal quenching mechanisms such as AGN feedback. However, the origin of quenching in lower-mass galaxies at high-z has received far less attention, largely due to previous observational limitations. JWST has now identified low-mass quenched galaxies (${M_{\\star}}&lt;10^{10}{\\rm M_{\\odot}}$). Given this emerging observational evidence, we investigate the viability of environmental quenching as the primary mechanism suppressing star formation in low-mass galaxies at $z&gt;3$. We analyze several simulations, including L-GALAXIES, IllustrisTNG, SIMBA, and TNG-Cluster, jointly comprising more than half a million galaxies at z=5. Across all simulations, quenched systems are overwhelmingly satellites, despite representing less than 10\\% of the total galaxy population. Satellite quenching increases with host halo mass and decreases with both stellar mass and halocentric distance, showing strong correlations with enhanced ram-pressure exposure and gas depletion. The simulations, particularly L-GALAXIES, produce low-mass quenched galaxies broadly consistent with those observed by JWST. Our results suggest that the recently discovered high-redshift quenched low-mass galaxies are possibly environmentally quenched systems residing in the vicinity of massive halos. According to the simulations, these galaxies are often only temporarily quenched: nearly 90\\% of them merge within a few hundred megayears, and a small fraction rejuvenate and resume star formation. Extended samples from future observations will enable robust tests of the environmental origin of galaxy quenching in the early Universe.",
    "bytes": 44508,
    "http_status": 200,
    "ok": true,
    "title": "Environmental Quenching of High-Redshift Galaxies: Interpreting JWST Observations with Simulations",
    "url": "https://arxiv.org/abs/2605.03008"
  }
}

```
