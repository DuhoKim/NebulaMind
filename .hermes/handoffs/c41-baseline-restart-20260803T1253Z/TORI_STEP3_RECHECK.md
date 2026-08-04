# Tori C41 Step-3 V2 fidelity and zone re-check

Lane: `c41-baseline-restart-20260803T1253Z`
Verifier: Tori
V2 summary protocol: `C41_STEP3_V2`
Record sample: the same fixed ranks 5, 15, 25, …, 175
Fidelity seed: 41

## Verdict: FAIL

V2 fully repairs quote fidelity: all 53 seeded quotes, including all 16 sampled rows marked
`truncated: true`, are exact verbatim source substrings at their claimed character ranges.

The zone repair does not pass. The V1 defect class remains systematic in the V2 seeded sample: 6 of
14 sampled `finding` labels are still applied to methods, captions, or reference-transition text.
Three additional rows are clearly mislabeled `references`, and one clear figure caption is labeled
`method`. The total is 10 clear zone misses in 53 sampled rows. Because the brief requires the V1
finding-on-method/caption/reference class to be gone and makes systematic mislabeling a FAIL, the
combined V2 re-check verdict is FAIL.

Recall was not re-measured. None of the 18 sampled records lost any spans from V1 to V2, so the prior
146/155 = 94.19% recall result stands.

## Pinned inputs and reuse receipt

I reused the original blind record sample, cached source extraction, seed machinery, and independent
artifact. No new record or sentence was chosen.

- Original independent file: `_tmp_tori3_independent.jsonl`
- Original independent SHA-256:
  `d5f73d0e51c33ec0b59c682fd8cb7b01eb60fe474bf1058618e6fef00f2cd9e0`
- Step-2 manifest SHA-256:
  `fcc2ed2e8ca5b9e67339881c4fede7b14f29d04582b923848397b9d560dc72e8`
- Preserved V1 span-table SHA-256:
  `45bb0e237b9744464301f9bb969dbeb83f152ae335fabf7d02aaeeef113eb7cb`
- Current V2 span-table SHA-256:
  `8c517bcf79d8795406ca4a3869af58bae49e76f99f9d9793b0e496cd6c55ff55`

The V2 fidelity draw used one `random.Random(41)` stream, ascending sampled rank, with V2 rows
stable-sorted by `span_id`; file order breaks duplicate-ID ties. Three unique rows were drawn per
record where available. Rank 115 still has only two spans, so both were checked rather than
duplicating one. The final sample is 53 unique rows and contains no repeated selected `span_id`.

Verifier-local evidence:

- `_tmp_tori3_recheck_raw.json`
- `_tmp_tori3_recheck_sample.md`
- `_tmp_tori3_recheck_zone_adjudication.json`

## Fidelity re-check: PASS

Every sampled quote was tested against the same locally cached full-text extraction used in the
blind V1 check.

- Seeded rows checked: 53
- Verbatim substrings anywhere in source: 53/53 (100.00%)
- Exact at claimed `char_range`: 53/53 (100.00%)
- Maximum nearest-source-start distance: 0 characters
- Sampled `truncated: true` rows: 16
- Truncated rows still exact verbatim source substrings: 16/16 (100.00%)
- Inserted ellipses or other non-source characters: 0
- Non-substring quotes: 0

This is a complete repair of the V1 fidelity defect. V1 had 24 exact quotes, 13 whitespace-only
representations, and 16 ellipsis-mangled quotes in the same-size seed sample; V2 has 53 exact quotes
and zero mangled quotes.

## Sampled span-count comparison

V2 did not shrink coverage for any sampled record.

| Rank | Record | V1 spans | V2 spans | Delta | Loss | Fidelity n | Verbatim | Truncated/verbatim |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 5 | `2024ApJ...962...24S` | 138 | 138 | 0 | 0.00% | 3 | 3 | 0/0 |
| 15 | `2024A&A...691A..19V` | 110 | 110 | 0 | 0.00% | 3 | 3 | 0/0 |
| 25 | `2020MNRAS.491.1427S` | 382 | 382 | 0 | 0.00% | 3 | 3 | 1/1 |
| 35 | `2017A&A...601A..95C` | 195 | 195 | 0 | 0.00% | 3 | 3 | 0/0 |
| 45 | `2013ApJ...765..140A` | 243 | 243 | 0 | 0.00% | 3 | 3 | 0/0 |
| 55 | `2010MNRAS.409..855B` | 58 | 58 | 0 | 0.00% | 3 | 3 | 3/3 |
| 65 | `2013MNRAS.432.2696M` | 17 | 17 | 0 | 0.00% | 3 | 3 | 1/1 |
| 75 | `2025ApJ...982...14H` | 114 | 114 | 0 | 0.00% | 3 | 3 | 0/0 |
| 85 | `2026MNRAS.546ag269C` | 59 | 59 | 0 | 0.00% | 3 | 3 | 2/2 |
| 95 | `2025ApJ...985...80R` | 59 | 59 | 0 | 0.00% | 3 | 3 | 0/0 |
| 105 | `2026JHEAp..5300626C` | 11 | 11 | 0 | 0.00% | 3 | 3 | 2/2 |
| 115 | `2026PhRvD.113h3007K` | 2 | 2 | 0 | 0.00% | 2 | 2 | 2/2 |
| 125 | `2024JCAP...07..078C` | 141 | 141 | 0 | 0.00% | 3 | 3 | 3/3 |
| 135 | `2023ApJ...943L..28K` | 24 | 24 | 0 | 0.00% | 3 | 3 | 0/0 |
| 145 | `2020MNRAS.493..580B` | 46 | 46 | 0 | 0.00% | 3 | 3 | 0/0 |
| 155 | `2015ApJ...808...25S` | 199 | 199 | 0 | 0.00% | 3 | 3 | 1/1 |
| 165 | `2009ApJ...697.1410L` | 34 | 34 | 0 | 0.00% | 3 | 3 | 0/0 |
| 175 | `2024ApJ...969L...2F` | 59 | 59 | 0 | 0.00% | 3 | 3 | 1/1 |
| **Total** | **18 records** | **1,891** | **1,891** | **0** | **0.00%** | **53** | **53** | **16/16** |

No record approached the brief's greater-than-20% loss flag. The prior recall result therefore
stands without a new recall pass.

## Zone re-check: FAIL

Sampled V2 zone distribution:

- `unknown`: 21 — accepted by contract
- `method`: 10
- `finding`: 14
- `background`: 3
- `interpretation`: 2
- `references`: 3
- `caption`: 0

Adjudication totals:

- Clearly defensible or `unknown`: 37/53
- Clear zone misses: 10/53 (18.87%)
- Additional boundary/judgment notes: 6/53 (11.32%)
- Clear V1-class misses among sampled `finding`: 6/14 (42.86%)
- False-positive `references` labels: 3/3 sampled `references` rows

The six persistent V1-class failures are:

1. `2024A&A...691A..19V_53541_53718` — figure/map caption labeled `finding`.
2. `2025ApJ...982...14H_56408_56727` — Figure 9 abundance-plot caption labeled `finding`.
3. `2026MNRAS.546ag269C_26180_26632` — equations and UVLF calculation procedure labeled
   `finding`.
4. `2025ApJ...985...80R_35284_35608` — SED-template generation method labeled `finding`.
5. `2026JHEAp..5300626C_8239_8395` — reference footnote and section transition labeled `finding`.
6. `2023ApJ...943L..28K_9870_10325` — simulation-resolution text and Figure 2 caption labeled
   `finding`.

Four additional clear zone failures are:

7. `2026JHEAp..5300626C_37177_37578` — efficiency benchmark/result transition labeled
   `references`.
8. `2020MNRAS.493..580B_6160_6413` — sample-selection method labeled `references`.
9. `2020MNRAS.493..580B_12274_12683` — methods-to-results transition labeled `references`.
10. `2024JCAP...07..078C_35072_35479` — Figure 2 UVLF caption labeled `method` instead of
    `caption`.

The six non-gating judgment notes are preserved in
`_tmp_tori3_recheck_zone_adjudication.json`. They cover mixed or boundary passages where I would
prefer a different label but did not use the difference to determine the verdict.

V2 therefore does not improve the sampled zone gate relative to V1. The V1 spot-check had 10 clear
zone misses and 5/14 finding-on-method/caption/reference misses; V2 again has 10 clear misses, with
the targeted finding defect appearing in 6/14 sampled findings across six records.

## V2 integrity note

This was not one of the two requested re-check dimensions, but it is relevant to downstream stable
indexing:

- V2 has 16,177 normal span rows plus one explicit no-spans marker row (16,178 JSONL lines).
- The 16,177 normal span rows contain 75 conflicting duplicate `span_id` values across 43 records;
  V1 had unique span IDs.
- Six sampled records contain 18 extra rows whose `span_id` duplicates another V2 row.
- None of the 53 seeded rows selected for this re-check shares a selected ID, so the fidelity and
  zone measurements above are not double-counted.

The duplicate-ID regression should be repaired before any ledger uses `span_id` as a unique key,
even after the zone gate is fixed.

## Required next repair

The quote-field repair can be retained unchanged. Repair zoning specifically at the extracted-span
level rather than relying only on broad heading proximity:

- recognize caption text even when the triggering span starts after `Figure N` or drops the `Fig.`
  prefix;
- veto `finding` for equation/model-construction, SED-template, sample-selection, and
  footnote/section-transition spans;
- prevent ordinary citation-bearing prose from becoming `references` unless it is actually inside a
  bibliography/reference block;
- resolve duplicate `span_id` generation and rerun the same seed-41 re-check.

Boundary held: lane-only verifier writes, read-only cached sources elsewhere, no network, no model or
Deep Research call, no Goru-artifact modification, and no Step-4 ledger/prose action.

TORI_STEP3_RECHECK_COMPLETE_20260804
