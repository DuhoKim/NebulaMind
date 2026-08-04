# LANA STEP 4 — COMPOSITION PATCH (author role): assertions for the 71 mechanical-cohort entries

Lane: `c41-baseline-restart-20260803T1253Z` · Lana (AUTHOR this round — Kun's Step-5 stance
verification is the independent check; I certify nothing here) · 2026-08-04 13:39 KST
Inputs: `C41_LEDGER.jsonl` (V6, 80 entries), `SPAN_TABLE.jsonl` (V3), my own
`LANA_STEP4_CERTIFICATION.md` (corrections 1–4), contract v1 + amendment v1.1
(`ledger_enums_v1_1.json`, certainty rules 1–7, rule-7 unknown-zone extension).
Output: **`STEP4_COMPOSITION_PATCH.jsonl` — 90 rows (71 assertion rows + 19 rebind receipts).
NOT applied to the ledger**; the applier and Kun act on it downstream.
Lane-only writes: the patch, this report, `_tmp_lana_compose_*` intermediates, `lana_compose_run.log`.

## What the patch contains

| cohort | count | treatment |
|---|---|---|
| composed in place | 48 | new atomic assertion distilled from the already-bound span, in the source's modality |
| debris → rebound | 19 | new span selected from the SAME paper's pool; rebind receipt (entry_id, old span, new span, reason); assertion composed from the new span; certainty re-derived |
| honest zeros | 4 | `no_claim_recoverable: true`, assertion "NO_CLAIM_RECOVERABLE from bound spans", certainty `no_info`, stance `no_info`, best span quoted verbatim in the row |

The 9 supports-stance entries (c41_001–007, 024, 036) are untouched — they were verified
native/adjudicated in my certification and are outside this task.

### Row schema
Assertion rows: `entry_id`, `no_claim_recoverable`, `new_assertion`, `new_modality`,
`new_precision`, `new_rationale` (one real reason per row, no ellipses), plus where derivation
requires it: `new_certainty_level`, `new_epistemic_type`, `new_model_dependence`, `add_tags`,
and `rebind {old_span_id, new_span_id, new_quote (verbatim from SPAN_TABLE), new_zone,
new_stance, certainty_derivation}`. Receipt rows: `entry_id, old_span_id, new_span_id, reason`.

## The 19 rebinds (all former front-matter/affiliation debris)

c41_017 → GN-z9p4 direct-method O/H = 7.37±0.15 · c41_027 → CLASSY on the MZR + burst SFRs
(also retires its underivable `contradicted_or_model_dependent`) · c41_030 → z≈8 metallicity
lower bounds ⇒ extended prior star formation · c41_032 → R23-calibration inconsistency ·
c41_033 → 0.05–0.1 dex local-calibration underestimate at high z · c41_041 → β=−2.95±0.20,
O/H<7.8, possible LyC leakage · c41_043 → strong-line calibrations non-evolving to z∼3 ·
c41_046 → observed z>8 SFRD decline may be a detection-limit effect · c41_047 → pre-JWST
tentative z∼10 deficit (reported_only baseline for the JWST-excess debate) · c41_053 →
low-mass MZR ⇒ downsizing + energy-driven winds · c41_055 → z∼2–3 emitters in burst region,
metallicities on the z≤2.2 relation · c41_057 → the FMR's SFR–metallicity segregation ·
c41_061 → first z>1 direct metallicity (12+log(O/H)=7.5) · c41_063 → SFRD decrease z∼9→12
(the rank-adjacent JWST high-z anchor) · c41_064 → UV-LF evolution explained by constant
star-formation efficiency · c41_065 → α∼−2 faint end, non-accelerated decline beyond z∼8 ·
c41_071 → no UV-LF shape change at z∼7–8 · c41_072 → uniformly blue β ⇒ dust-free z∼8
populations · c41_079 → ξion sufficient for reionization given probably-high escape fractions
(matches its `ionizing_output` tag).

All new spans carry their honest `unknown` zone with stance **`qualifies`** — no zone
adjudication is performed or implied (v1.1 rule-7); certainty re-derived to
`emerging_sample_limited` (single source, direct span support, rule-2 ceiling) with the
derivation string embedded per row. The brief's cited example (rank-1 paper's M_UV–metallicity
finding, 2026A&A...708A.203P) was already promoted to supports-entry c41_007 in V6, so it needed
no rebind here.

## The 4 honest zeros

c41_018, c41_021, c41_059 are bound to title/author-list spans; c41_062 to a pure aims sentence
("To analyze… we present a study…"). None contains a checkable proposition. These papers were
NOT eligible for rebinding under the task scope (rebinding was mandated for the 19 debris-bound
entries only), so the escape hatch applies — quoted best span retained in the row.
Judgment-call note: c41_008/034/054 are also abstract-methods spans, but each asserts a
*completed dataset/measurement fact* (146 galaxies over 3 dex; mass/sSFR composites; 50-galaxy
resolved abundances), which is stance-verifiable, so they were composed rather than zeroed.

## Derivation-driven field changes (all receipted in-row via rationale)

- **c41_011**: `actively_debated` → `emerging_sample_limited` + `add_tags: [tension_reported]`
  (cert correction 4 — single-source debate claims held down pending Step-5 verified conflict);
  broken assertion replaced by the two-sided SFRD-consistency/tension claim.
- **c41_051, c41_078**: underivable `contradicted_or_model_dependent` → `emerging_sample_limited`
  (cert correction 3; c41_027 resolved via its rebind).
- **Rule-4 repairs by re-typing to what the span actually is**: c41_020, c41_078 → `reported_only`
  (literature-reported tensions, not this paper's measurement; also c41_039/047/069/073);
  c41_025, c41_075 → observational modality restored (`shows_can_occur` / `is_are_does`);
  c41_080 → `in_model_only` + `epistemic_type: simulation` + `model_dependence: high`
  (a claim about model behavior, typed per rule 4).
- **Single-object rows** (c41_010/013/017/019/025/041/050/061): `new_epistemic_type: single_case`
  + modality capped at `shows_can_occur` (rule 3).
- **Precision assessed per assertion** (cert correction 6): 26 `quantified` / 41 `qualitative`
  across the 67 non-zero rows — including the cert's named example class (c41_076's number
  density with asymmetric errors → `quantified`).

## Verification run (log: `lana_compose_run.log`)

90 rows parse; assertion ids == mechanical cohort exactly (71/71, no supports entry touched);
19 receipts pair 1:1 with the 19 in-row rebinds; all 19 `new_quote`s byte-verbatim against
`SPAN_TABLE.jsonl` and zones match the table; all rebind stances `qualifies`; 0 assertions are
verbatim prefixes of their span quote (the V2–V6 failure mode); 0 rationale ellipses; assertion
length 127–268 chars (median 203). Modality histogram: 34 is_are_does / 11 may_or_can /
10 shows_can_occur / 6 reported_only / 4 mixed_debated / 1 commonly_probably / 1 in_model_only
(+4 no-claim rows).

## For the applier and for Kun

- Patch is **not applied**; the applier must keep the count-lock (80 rows before/after) and
  should carry the in-row fields (`new_epistemic_type`, `new_model_dependence`, `add_tags`)
  alongside assertion/span swaps.
- Cert corrections still open and NOT covered here: rationales of the 9 supports entries,
  the 2 absent countercase spans / `NO_ENTRY_REASONS.json`, stance-bearing links
  (`contradicts`/`corroborates` — deferred to Step 5/6 per cert correction 7), and the
  receipt's `zone_source_histogram` relabel.
- Kun Step-5: every composed assertion is single-span-grounded by construction; the 19 rebinds
  and 4 zeros are the rows to attack first. I certify nothing I wrote here.

LANA_COMPOSITION_COMPLETE_20260804
