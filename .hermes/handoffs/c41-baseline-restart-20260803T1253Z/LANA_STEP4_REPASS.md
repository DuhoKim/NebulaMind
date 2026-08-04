# LANA STEP 4 RE-PASS — V4 ledger verification against LANA_STEP4_PASS.md findings

Lane: `c41-baseline-restart-20260803T1253Z` · Lana · 2026-08-04 11:0x KST
Inputs: `C41_LEDGER.jsonl` (V4, 80 entries), `STEP4_VALIDATION_RECEIPT.json`,
`STEP4_ZONE_ADJUDICATION.jsonl` (2 receipts), `SPAN_TABLE.jsonl` (V3 ground truth),
contract amendment v1.1 (`AMENDMENT_v1_1_unknown_zone.md`) + `ledger_enums_v1_1.json`,
`countercases.jsonl`. Checks programmatic over all 80 entries (span-table join on `span_id`,
receipt join, enum validation, stance×zone cross-tab, dimension audit) + manual reads of 15
sampled entries (c41_003/010/016/022/030/037/045/050/055/060/065/070/075/077/080) + targeted
reads (c41_001/002/004/005/006/011/027/038/039/051/064/078). Lane-only writes: this file,
`_tmp_lana_repass_check.py`, `lana_repass_run.log`.

## VERDICT: **FAIL_WITH_CORRECTIONS**

The two coordinator flags — the reasons V2 was ruled falsified — are **genuinely fixed and
verified**: zones are honest (zero casts), rule 7 as amended is obeyed by all 80 entries, and
certainty inflation is gone. V4 is an honest ledger. But it is honest about spans, not claims:
the 74-entry mechanical cohort still carries my Step-4 systemic findings 1–5 (assertions are
truncated span prefixes, table dumps, boilerplate metadata, zero links). Nothing here is
dishonest; the remaining failures are quality, not integrity, and are correctable without
another full rebuild.

## Verification against each LANA_STEP4_PASS finding

### Flag 1 — zone honesty (was: METADATA FALSIFICATION): **FIXED — VERIFIED PASS (80/80)**
Joined every ledger evidence span to `SPAN_TABLE.jsonl`. True source zones of the 80 spans:
4 `finding`, 76 `unknown`. Ledger records: 5 `finding`, 1 `interpretation`, 74 `unknown`.
The only two upgrades from `unknown` are exactly the two spans in
`STEP4_ZONE_ADJUDICATION.jsonl`, each with span id → adjudicated zone → one-line justification,
matching the amendment's receipt requirement (c41_004 → `interpretation`, c41_005 → `finding`).
**Zero un-receipted casts. `unknown` preserved on all 74 remaining spans.** `unknown` is
enum-valid under v1.1, so this is now contract-compliant, not just honest.
- Nit (receipt, not ledger): `STEP4_VALIDATION_RECEIPT.json`'s `zone_source_histogram`
  (finding 5 / interpretation 1 / unknown 74) is actually the *ledger-recorded post-adjudication*
  histogram; the true source histogram is finding 4 / unknown 76. Rename the key or add both.

### Rule 7 as amended — stance gating: **VERIFIED PASS (all 80 entries + ALL supports spans)**
Checked all 80 entries (superset of the required 15-entry sample) and every supports-stance
span individually. Stance distribution: **6 `supports`, 74 `qualifies`**, matching the report.
All 6 supports are eligible: c41_001, c41_002, c41_006 on native `finding` spans
(observational), c41_003 on a native `finding` span (single_case), c41_004 on the adjudicated
`interpretation` span, c41_005 on the adjudicated `finding` span — both receipts present and
used. **Zero supports on unadjudicated unknown-zone spans.** All 74 unknown-zone spans carry
`qualifies`, within the amendment's allowed set.

### Flag 2 — certainty inflation (was: 65/80 `widely_supported`): **FIXED — VERIFIED, minor residue**
Sampled 15 entries manually + full 80-entry programmatic audit. Histogram now
75 `emerging_sample_limited` / 2 `actively_debated` / 3 `contradicted_or_model_dependent`
(matches receipt). **Zero `widely_supported`/`established`**; every single-source entry
respects the `emerging_sample_limited` ceiling. The V2 assigned-not-derived pathology is gone.
Residue, two items:
1. **R4 incoherence persists on the 3 `contradicted_or_model_dependent` entries**
   (c41_027, c41_051, c41_078): `modality: in_model_only` + `epistemic_type:
   observational_sample` + `model_dependence: none` — the same rule-4 violation I flagged on 5
   V2 entries; reduced but not fixed. Correction: set `model_dependence: high` (or
   `epistemic_type: simulation`) with a span-grounded reason, else re-derive the level.
2. **2 single-source `actively_debated`** (c41_004, c41_011; V2 had 1). Both quotes genuinely
   describe tension with theoretical models, so this is defensible under the V4 brief
   ("actively_debated for tension spans"), but under the frozen question's rule ("disputed only
   when stance-verified sources conflict") debate status on one source with zero links remains
   premature. Correction: hold at `emerging_sample_limited` with a `tension_reported` tag, or
   let Step-5 stance verification elevate them — do not leave them pre-elevated.

### Countercases present: **PARTIAL (2 of 5 mined)**
`countercases.jsonl` holds 5 strict-tension spans. Two are first-class ledger entries with
receipts (c41_004, c41_005) — genuine countercase representation, which V2 had zero of. Three
are absent (2024A&A...684A..75C_65175_65699, 2024ApJ...960...56H_81091_81250,
2024ApJ...962...24S_67569_68015); the brief said "mine the strict-tension spans" and budgeted
20–40 adjudications, of which 2 were spent. c41_011's quote is also a real tension span
(SFRD vs constant-SFE models) but its assertion is broken (below). Correction: adjudicate and
add the 3 remaining countercase spans, or record a named reason per span.

### Systemic findings 1–6 status (the non-flag findings of my pass)
1. **Assertions not atomic — NOT FIXED for the mechanical cohort (74/80).** Every one of the 74
   new entries' `assertion` is a **truncated prefix of its span quote** (typically cut at ~600
   chars, some mid-token). Three are outright garbage: c41_038 `"00, No."`, c41_039 `"4  A."`,
   c41_064 `"2012)."`. c41_011 (`actively_debated`) asserts the non-claim "If we compare our
   observations to the predicted SFRD of Harikane et al." Only the 6 V3-seed entries have
   authored atomic assertions (c41_001–006; verified clean, plus a few short spans that happen
   to be single sentences). Modality labels stamped over table prefixes remain meaningless.
2. **Table/equation/figure spans — NOT FIXED: 45/80 spans** have numeric-token fraction > 0.35
   (raw tables c41_010/016/037/075/080, figure-axis debris c41_045, section headers c41_022).
   A `qualifies` stance from a data table is as undefined as a `supports` was.
3. **Placeholder metadata — NOT FIXED: 74/80** share the identical rationale "Automated ledger
   composition based on score." and an identical scope block; `source_title` is real for the
   new cohort (a V2→V4 improvement) but "Unknown Title" on the 6 seed entries.
4. **Zero links — NOT FIXED (0 links, 80 unique bibcodes, 1 entry/paper).** Still a per-paper
   span catalog; corroboration/contradiction structure for the Step-6 debate map still absent.
5. **`precision: qualitative` stamped — NOT FIXED: 78/80** (2 quantified), including heavily
   quantified spans (c41_037, c41_060, c41_080).
6. **Provenance/quote fidelity — PASS with a benign nit.** 80/80 span_ids resolve; 77/80 quotes
   verbatim. The 3 seed-entry "mismatches" (c41_004/005/006) are light cleanup — LaTeX render
   duplicates stripped, a leading sentence fragment and a list numeral dropped, ligature
   normalized — content-preserving and re-verifiable via `char_range`; acceptable, but note
   quotes are cleaned, not verbatim, for those three.

## Counts

| check | V2 (my pass) | V4 (this re-pass) |
|---|---|---|
| Z — zone cast without receipt | 80 | **0** |
| R7 — ineligible `supports` | 80 | **0** |
| C — certainty above single-source ceiling | 65 | **0** |
| M — rule-4 incoherence | 5 | 3 (c41_027/051/078) |
| D — single-source debate claim | 1 | 2 (c41_004/011) |
| A — assertion not atomic (span-prefix dump) | 80 | 74 (incl. 3 garbage) |
| T — table/figure span content | 57 | 45 |
| links present | 0 | 0 |
| countercase entries | 0 | 2 (of 5 candidates) |
| entries fully clean | 0 | 9 (c41_001/002/003/017/032/040/055/061/062) |

## Corrections required (no rebuild — targeted repair)

1. **Assertion distillation pass over the 74 mechanical entries**: author one atomic assertion
   per entry from the span (drop or re-span the 3 garbage-assertion entries c41_038/039/064 and
   the worst table-only spans); this is editorial, zones/stances/certainty stay as-is.
2. Fix the 3 rule-4 entries' `model_dependence`/`epistemic_type` coherence.
3. Downgrade or Step-5-gate the 2 single-source `actively_debated` entries.
4. Adjudicate-and-add (or name reasons for) the 3 unmined countercase spans.
5. Replace the 74 boilerplate rationales with one span-specific sentence each; assess
   `precision` per span.
6. Links remain the structural gap for Step 6; acceptable to defer to Step 5/6 where stance
   verification will surface the cross-paper pairs, but say so explicitly in the receipt.
7. Receipt nit: relabel `zone_source_histogram` (it is post-adjudication).

Steps 1–2 of the pipeline are unaffected; the V4 zone/stance/certainty layer is sound and can
carry the repair in place.

LANA_STEP4_REPASS_COMPLETE_20260804
