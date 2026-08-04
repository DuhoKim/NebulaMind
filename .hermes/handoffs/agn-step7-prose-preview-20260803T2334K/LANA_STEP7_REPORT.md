# LANA STEP-7 REPORT — AGN prose-preview packet (campaign lane L-B)

- Lane: `agn-step7-prose-preview-20260803T2334K` · compiled 2026-08-03T14:38–14:41Z (23:38–23:41 KST, 2026-08-03)
- Campaign gate honored: artifacts only; the P0 apply gate remains HELD — nothing landed on any page, DB, wiki, or git. No network, no DB, no reads of the C41 lane, f_esc dirs, or the campaign ledger.

## Deliverables (all in this lane dir)

1. `AGN_PROSE_PREVIEW.md` — reader-facing prose for all 5 map axes, 36 sentences, inline IDs `⟨s7_*⟩`.
2. `PROSE_SENTENCE_BINDINGS_STEP7.jsonl` — 36 rows, one per sentence; template-conformant fields plus additive extensions (`wording_template_ids`, `meta_sentence`, `reader_facing_preview`); `template_only_not_reader_facing: false` on every row.
3. `WORDING_CONTRACT_CHECK_STEP7.json` — self-check: **36/36 pass, 0 tier overflows, 0 orphan sentences, 16/16 ledger entries bound, 0 unbound**.
4. This report.

## Process

1. Read the brief, the post-patch map + `PATCH_LOG.md` (Step-6 lane), the ledger contract doc, `claim_status_ledger.jsonl` (all 16 entries re-read directly, not trusted from the map), `wording_contract_check.json`, both bindings files (identical 16 template rows), `ledger_enums.json`, and roadmap §Step 7 (+§Step 8 row shape, since the brief's deliverable 2 is that shape).
2. Built one Python generator (`_tmp_build_step7_packet.py`, kept in-lane) holding every sentence with its bindings once, emitting all three artifacts — guaranteeing byte-identical text between preview and binding rows (verified: 36/36 binding texts appear verbatim in the preview).
3. Mechanical verification: every `citation_span_ids` value exists in the ledger AND belongs to a bound entry of that sentence (0 violations); coverage 16/16; tier checks below.

## Rules applied (recorded in the check JSON as R-A…R-F)

- Modality law: per sentence, `actual_tier` must not outrank (a) the minimum contract `max_allowed_tier` over bound entries, and (b) any bound entry's ledger `modality` (with the template-actual escape for `clc_agn_005`, ambiguity #2). Declared rank: `is_are_does > commonly_probably > may_or_can > shows_can_occur > mixed_debated > in_model_only > reported_only`.
- Pending disclosure: the map header's pending-verification bullet is reproduced **verbatim** in the preview header and additionally as bound sentence `s7_H01` (bound to all 16 entries); every per-axis Status line repeats "(pending verification)".
- Countercase quota (all map-named countercases appear in prose): `clc_agn_008` vs the ejective side (`s7_A06`) and as Axis-C direct countercase (`s7_C08`); 009↔010 mutual bounding (`s7_C07`); 007's in-corpus tension (`s7_C09`); D'Eugenio case-not-prevalence guard (`s7_A03`, `s7_B05`).
- Contested-number guards: 17%/46% never appear without the do-not-average guard (`s7_B04`, restated `s7_B06`); no cross-channel dominance fraction anywhere (`s7_C10`); 3–100 M⊙/yr kept single-sample; case 10×SFR kept case-scoped; factor-~2 depletion kept central-kpc; all per-channel Axis-C numbers kept per-channel.
- Simulation cap: every sentence bound to `clc_agn_004`/`clc_agn_011` opens "In simulations"/names the cap and carries `in_model_only` (or `reported_only` meta).

## Ambiguities — reported, NOT fixed

1. **All 16 entries are `verification_status: pending`** (inherited from Step 6, ambiguity #1 there). This packet therefore previews prose whose every certainty label is unverified; disclosed as required, not resolved.
2. **`clc_agn_005` tier recording mismatch:** ledger `modality: may_or_can`, but the wording-contract row records both `max_allowed_tier` and `actual_tier` as `mixed_debated` (its `certainty_level` is `actively_debated`). I followed the contract's recorded tiers (sentences `s7_D01`/`s7_D02` = `mixed_debated`, matching the template row) rather than re-deriving; flagged for Kun.
3. **`reported_only` repurposed for meta sentences.** The enum's original use is abstract-only sourcing; I used it for 12 meta/guard/status sentences that only report ledger fields, links, notes, or enums (all flagged `meta_sentence: true`, several with empty `citation_span_ids` because notes/links/status fields have no evidence spans). Alternative would be leaving header/status/guard sentences unbound, which the brief forbids ("EVERY sentence carries a binding row").
4. **Contract tier vs ledger modality for `widely_supported` entries:** 007/009/010 carry ledger `modality: is_are_does` but contract ceiling `commonly_probably`, and the contract's own template texts ("are…/remain…") are recorded as `commonly_probably` tier. I mirrored the template texts and their recorded tier (`s7_C02`–`s7_C06`); not re-litigated.
5. **Modality enum is not a total order.** The check requires an ordering; I declared one explicitly in the check JSON (`tier_rank_declared`) so the check is reproducible. The placement of the capped tiers (`mixed_debated`, `in_model_only`) below the declaratives is my construction, not a ledger fact.
6. **Bindings filename/shape:** the roadmap Step-8 row shape has no "wording-contract template used" field; the brief requires one. Added additively as `wording_template_ids` (= the `template_<entry_id>` sentence IDs in `wording_contract_check.json`, one per bound entry) without altering any template-mandated field.

## Runtime

~7 minutes wall clock: inputs read 14:34–14:38Z; packet generated + mechanically verified 14:38–14:40Z; report 14:41Z. Temp file kept at `_tmp_build_step7_packet.py` (lane-scoped per protocol).

LANA_AGN_STEP7_COMPLETE_20260804
