# LANA STEP 4 — no-overclaim pass over C41_LEDGER.jsonl V2 (80 entries)

Lane: `c41-baseline-restart-20260803T1253Z` · Lana · 2026-08-04 10:46 KST
Ground truth used: `SPAN_TABLE.jsonl` (V3, sha `c438c95d…` per STEP4_VALIDATION_RECEIPT), the
Claim Ledger Contract v1 (`docs/claim_ledger_contract_v1_agn_20260703T0830Z/CLAIM_LEDGER_CONTRACT_V1.md`,
Certainty derivation rules 1–7) and `artifacts/ledger_enums.json`. No ledger edits made; report-and-propose only.

## VERDICT: **FAIL_WITH_CORRECTIONS**

Goru's structural validation (PASS) is real but vacuous: the schema is satisfied while the
semantics are not. Every one of the 80 entries fails at least two contract requirements. This
ledger cannot proceed to Kun's Step-5 stance verification as-is — there are no stances to verify,
because there are no atomic assertions to take a stance on.

## Ruling on the two coordinator flags

### Flag 1 — Zone recast (`unknown` → `interpretation`): **METADATA FALSIFICATION — REVERT**

Verified against the V3 span table: **80/80** ledger spans carry `zone: "unknown"` in
`SPAN_TABLE.jsonl` (which holds 15,546 unknown / 272 caption / 252 references / 32 finding spans).
All 80 were recast to `interpretation` in the ledger. This is not a neutral relabel: contract
rule 7 gates the `supports` stance on `finding`/`interpretation` zones, and all 80 spans carry
`stance: supports` — the cast **manufactures stance eligibility** that the ground truth denies.
Goru's own report concedes it was done "to strictly adhere to the V1 contract enum … without
forcing a speculative zone" — but casting unknown to a specific zone *is* forcing a speculative
zone, chosen to be the one that unlocks `supports`. Tori's Step-3 recheck explicitly adjudicated
`unknown` as an *accepted honest label* ("unknown accepted or label defensible from local
context"), so the honest value existed and was overwritten.

**Disposition (choose one, gated):**
1. **Revert** each ledger span to its V3 zone. Since `unknown` is not in the contract enum,
   propose a **docs-only enum extension** adding `unknown` to `rhetorical_zone`, with the rule:
   unknown-zone spans may carry `qualifies`/`mixed`/`no_info` but never `supports` for
   observational entries. (Contract change → needs a gate.)
2. Or: per-span **genuine zone adjudication with receipts** (the Tori-recheck pattern) before any
   span keeps `interpretation` — a blanket cast is not adjudication.

Either way, the V1 honest core — the **32 true `finding` spans** that produced Goru's 4-entry V1 —
is the only currently supports-eligible material.

### Flag 2 — Certainty inflation (65/80 `widely_supported`): **CONFIRMED — SYSTEMATIC OVERCLAIM**

Checked against the definition (derivation rule 1: *direct, consistent, multi-source support with
critics/countercases represented*):

- All 65 `widely_supported` entries have **exactly 1 evidence span, 1 source**, and their own
  `certainty_dimensions.consistency = "single_source"`.
- **0/80 entries have any `links`** — no `contradicts`/`qualifies` links anywhere, so
  critics/countercases are represented in zero entries.
- Rule 2 defaults single-sample scoped claims to `emerging_sample_limited`; rule 6 makes
  certainty a deterministic function of the dimensions. The determinism claim is **demonstrably
  false in V2**: all 80 entries share the *identical* dimension vector
  (`direct / single_source / qualitative / sample-specific / none`) yet map to **four different**
  certainty levels. Certainty was assigned, not derived.
- 64 of the 65 also carry the strongest modality (`is_are_does`) — in the #1 contested cluster,
  where the frozen question's interpretation contract says disputed status requires stance-verified
  multi-source conflict. A compliant V2 of this cluster should be dominated by
  `emerging_sample_limited` + genuine `actively_debated` link structures, not `widely_supported`.

**Corrections:** all 65 `widely_supported` → `emerging_sample_limited`. The single
`actively_debated` entry (c41_007 — the one genuinely tension-describing prose span in the
ledger) also cannot stand on one source under the frozen-question rule ("disputed only when
stance-verified sources conflict"): → `emerging_sample_limited`, flagged for Step-5 re-elevation
if verified conflict emerges. The 5 `contradicted_or_model_dependent` entries are internally
incoherent (modality `in_model_only` + `epistemic_type: observational_sample` +
`model_dependence: none` violates rule 4), and 3 of the 5 are table/equation dumps — drop or
re-derive.

## Systemic findings beyond the two flags

1. **Assertions are not assertions (80/80).** Every `assertion` field is the verbatim span text
   (median 600 chars), violating the schema requirement "atomic assertion, not prose paragraph".
   c41_001's "assertion" is a raw measurement table; others contain LaTeX debris ("italic_z",
   "\lambda"). Modality labels over these are meaningless — you cannot grade the modality of a
   table.
2. **57/80 spans are table/equation/figure content**, not propositional prose (numeric-token
   fraction > 0.35). A `supports` stance from a data table is undefined; these entries need
   re-spanning to the prose finding that interprets the table, or dropping.
3. **Placeholder metadata (80/80):** scope = "extracted population"/"source-specific" everywhere;
   every span rationale is the identical boilerplate "Automated ledger composition based on
   score." — the schema requires a one-sentence *reason*.
4. **One entry per paper, 80 unique bibcodes, zero links.** This is a per-paper span catalog, not
   a claim ledger: no claim is corroborated, contradicted, or connected. The Step-6 debate map
   cannot be built from it.
5. `precision: "qualitative"` on 80/80 while most spans are heavily quantified — further evidence
   the dimension vector was stamped, not assessed.
6. Quote fidelity to the V3 span table is **clean (0 mismatches, 80/80 span_ids resolve)** — the
   provenance layer is sound; the failure is entirely semantic.

## Counts

| check | entries affected |
|---|---|
| A — assertion verbatim / not atomic | 80 |
| Z — zone recast unknown→interpretation | 80 |
| C — `widely_supported` fails R1/R2/R6 → `emerging_sample_limited` | 65 |
| T — span is table/equation/figure dump | 57 |
| M — `in_model_only` vs observational/`model_dependence: none` (R4) | 5 |
| D — `actively_debated` on a single source | 1 |
| entries with zero issues | 0 |

## Recommended V3 path (for Goru; I do not edit the ledger)

1. Rebuild from the 32 genuine `finding` spans (the honest V1 core) + Tori-adjudicated spans;
   every other span needs receipts-backed zone adjudication or the `unknown` enum extension.
2. Distill one atomic assertion per claim (not per paper); merge multi-paper support into shared
   entries so `consistency`/links can be real.
3. Derive certainty deterministically: single-source observational → `emerging_sample_limited`
   ceiling; `widely_supported` only with ≥2 corroborating sources *and* a critic/qualifier link.
4. Accept the honest shortfall. "Dozens" was a coverage floor on *eligible* entries, not a licence
   to inflate; a 4→~25-entry honest ledger beats an 80-entry falsified one.

## Per-entry findings table

Issue codes: **A** assertion verbatim/not atomic · **Z** zone recast · **C** certainty inflated →
`emerging_sample_limited` · **T** table/equation span, no extractable claim · **M** rule-4
incoherence · **D** single-source debate claim.

| entry_id | certainty (V2) | modality (V2) | issues | proposed correction |
|---|---|---|---|---|
| c41_001 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_002 | contradicted_or_model_dependent | in_model_only | A M T Z | drop or re-span; label unsupported by dims; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_003 | widely_supported | is_are_does | A C Z | certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_004 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_005 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_006 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_007 | actively_debated | mixed_debated | A D Z | certainty → `emerging_sample_limited` (pending Step-5 verified conflict); rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_008 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_009 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_010 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_011 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_012 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_013 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_014 | emerging_sample_limited | may_or_can | A T Z | drop or re-span to prose finding; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_015 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_016 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_017 | widely_supported | is_are_does | A C Z | certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_018 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_019 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_020 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_021 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_022 | widely_supported | commonly_probably | A C Z | certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_023 | contradicted_or_model_dependent | in_model_only | A M T Z | drop or re-span; label unsupported by dims; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_024 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_025 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_026 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_027 | widely_supported | is_are_does | A C Z | certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_028 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_029 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_030 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_031 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_032 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_033 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_034 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_035 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_036 | widely_supported | is_are_does | A C Z | certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_037 | widely_supported | is_are_does | A C Z | certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_038 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_039 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_040 | widely_supported | is_are_does | A C Z | certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_041 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_042 | emerging_sample_limited | shows_can_occur | A T Z | drop or re-span to prose finding; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_043 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_044 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_045 | widely_supported | is_are_does | A C Z | certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_046 | emerging_sample_limited | shows_can_occur | A T Z | drop or re-span to prose finding; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_047 | contradicted_or_model_dependent | in_model_only | A M Z | fix `model_dependence`→high + epistemic basis, else re-derive; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_048 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_049 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_050 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_051 | widely_supported | is_are_does | A C Z | certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_052 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_053 | widely_supported | is_are_does | A C Z | certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_054 | widely_supported | is_are_does | A C Z | certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_055 | emerging_sample_limited | may_or_can | A Z | rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_056 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_057 | emerging_sample_limited | may_or_can | A Z | rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_058 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_059 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_060 | widely_supported | is_are_does | A C Z | certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_061 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_062 | widely_supported | is_are_does | A C Z | certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_063 | emerging_sample_limited | may_or_can | A Z | rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_064 | emerging_sample_limited | shows_can_occur | A T Z | drop or re-span to prose finding; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_065 | widely_supported | is_are_does | A C Z | certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_066 | emerging_sample_limited | shows_can_occur | A Z | rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_067 | emerging_sample_limited | may_or_can | A Z | rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_068 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_069 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_070 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_071 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_072 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_073 | widely_supported | is_are_does | A C Z | certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_074 | contradicted_or_model_dependent | in_model_only | A M T Z | drop or re-span; label unsupported by dims; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_075 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_076 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_077 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_078 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_079 | widely_supported | is_are_does | A C T Z | drop or re-span to prose finding; certainty → `emerging_sample_limited`; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |
| c41_080 | contradicted_or_model_dependent | in_model_only | A M Z | fix `model_dependence`→high + epistemic basis, else re-derive; rewrite assertion as atomic claim; zone: revert per Flag-1 ruling |

---
Checks were programmatic over all 80 entries (span-table join on `span_id`, dimension/level
cross-tab, links scan, numeric-content classifier) plus manual reads of c41_001, c41_002, c41_007,
c41_022, c41_023, c41_047, c41_074, c41_080. Lane-only writes: this file +
`_tmp_lana_step4_table.md`/`.json`.

LANA_STEP4_PASS_COMPLETE_20260804
