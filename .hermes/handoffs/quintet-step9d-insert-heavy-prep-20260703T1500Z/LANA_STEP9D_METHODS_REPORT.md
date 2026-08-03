# Lana — Step 9D insert-heavy prep methods / claim-compatibility review

Task: Step 9D Quintet review · Lane: Lana (methods / claim-compatibility reviewer) · Read-only.
Written: 2026-07-04, repo `/Users/duhokim/NebulaMind/NebulaMind`. **No DB/SQL/API mutation, no apply, no git write, no apply-SQL authored.**

## Verdict: **PASS_WITH_PATCHES**

Excellent, disciplined prep packet: 6 claim skeletons with correctly non-inflated trust designs, a 25-source / 35-use split with differentiated per-claim stances, no evidence laundering, the Peng 2015 stance decision applying my Step 9C patch verbatim, and both my Step 9B patches (2917 duplicate consolidation, 2924 trust recompute) carried into the skeleton gates. All hard stops zero; design-only, nothing executable. Three small carry-forward patches to the Step 9E handoff — most importantly, apply the Peng stance-compatibility standard to **all** cross-claim citations, not just Peng.

## Answers

**1. Six skeletons + 25/35 split — scientifically/methodologically correct.** The skeletons mirror the Step 8/9 prose (already PASSed) and, crucially, carry **non-inflated trust designs** faithful to the Step 6 map:
- scoped-synthesis → `mixed_debated_or_reported_after_vote_review`; outflows → `reported_scoped_sample_not_universal`; dominance → `mixed_debated`; reservoir → `mixed_debated`; **heating → `model_bounded_or_simulation_bounded_not_consensus`** (the 2924 correction); kinetic → reuse existing 2915 (`keep_existing…until_operator_choice`).
The 35-use split assigns **differentiated stances** (supports 19, supports-with-scope-qualifier 9, qualifies 6, contradicts_or_qualifies 1) across five insert-claims — the same source correctly carries different stances toward different claims. No trust inflation, no all-"supports" flattening.

**2. Laundering attack — no laundering found.** The 35 claim-uses are all **new candidate inserts** (`insert_sql_status: DESIGN_ONLY_ROW`, `status_design: active_after_future_execution_only`, 0 rows reusing existing DB evidence), so paper existence is not being converted into claim-compatible evidence for the 25. The only reuse is Peng 2015 `6651`, which is stance-gated (Q3). Each use carries a claim-specific `stance_design` tied to a `target_claim_key`, not a generic topical attachment.

**3. Peng 2015 `6651` stance/proposition decision — sufficient; my Step 9C patch applied.** `stance_proposition_decision = CONDITIONALLY_COMPATIBLE_FOR_DOMINANCE_ALTERNATIVE_OR_STRANGULATION_QUALIFIER_ONLY`; `claim_context_caveat` states "Step 9E must not treat same-paper identity as sufficient"; `anti_row_17_rule` blocks a duplicate Peng insert; compatible ledger entries are exactly `dominance_debate` + `alternative_quenching_channels`; reuse `6651` not new insert. This is correct and matches the "same paper, different stance" discipline. *Minor:* the `compatible_step9_sentence_ids` also list P9S001/P9S002/P9S016 (framing/synthesis) — Peng-as-strangulation-alternative is a **looser** fit there than at P9S008/P9S009; Step 9E should confirm those looser bindings or restrict to P9S008/P9S009.

**4. Cross-claim citation refs — acceptable as Step 9E blockers (no Step 9D patch required).** 4 of 16 citation anchors carry `cross_claim_review_flags`; GO/NO-GO is explicitly `NO_GO` on "Cross-claim citation uses reviewed," and the flags carry the chosen source-claim-key and the Peng reuse decision. Since Step 9D authors no SQL and applies nothing, deferring cross-claim citation **review** to Step 9E (the SQL-resolution packet) is architecturally correct and the flags are explicit + gated, not silently accepted.

**5. Step 10 creep + claim workflow boundaries — clean.** `step10_unlocked: False`, `execution_authorized: False`, `product_apply_authorized: False`, all `insert_sql_status = NOT_AUTHORED_AS_EXECUTABLE_SQL; DESIGN_ONLY_ROW` — no Step 10 apply creep. Each existing claim's Step 9B disposition is carried into the skeleton lineage/gates: 2929 supersede/split; **2915 reuse (no new insert)**; **2917 rebind only after 2557/2572 consolidation** (my Step 9B Patch 2 — honored); 2921 out-of-AGN-section; **2924 nuance/retire + trust recompute required** (my Step 9B Patch 3 — honored); 2913 not resurrected. Every claim action is `NO_GO_UNTIL_…` gated.

## Patches (carry-forward to Step 9E handoff — concrete)

1. **Apply the Peng stance-compatibility standard to all 4 cross-claim citations, not just Peng.** Add to the Step 9E requirements: "Each of the 4 cross-claim-flagged citations must pass the same stance/proposition-compatibility check as Peng 2015 `6651` — confirm the cited source's role matches the target sentence's proposition; a mismatch requires a distinct citation, never reuse." (Prevents rubber-stamping the other 3 while only Peng is scrutinized.)
2. **Assign per-source `quality_design`, not a uniform placeholder.** The sampled uses show a uniform `0.78`; Step 9E must set quality per source and per claim-use consistent with Step 6 epistemic type (observational sample vs single case vs simulation vs review) and stance (a `qualifies`/`contradicts` use should not carry the same quality framing as a `supports` use).
3. **Confirm or restrict the looser Peng bindings** (P9S001/P9S002/P9S016) in Step 9E; the defensible core is P9S008/P9S009.

None of these require re-authoring Step 9D; they make the carry-forward requirements explicit so Step 9E cannot lose them. Step 9D may be marked review-complete / `PREPARED_ONLY` with these folded into its next-gate recommendation.

## Safety ledger

- DB writes: 0 · SQL authored/executed: 0 · API mutations: 0 · apply: 0 · git: 0 · deploy/restart: 0 · product publish: 0 · Step 10: locked · execution_authorized: False · DB mode: BEGIN READ ONLY + ROLLBACK
- Reads: summary, validation, skeletons, use matrix, citation anchor design, Peng decision, go/no-go (read-only). Files written by Lana: 1 (this report).

LANA_STEP9D_METHODS_DONE
