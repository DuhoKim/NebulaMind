# Tori C41 Step-3 V3 round-3 re-check

Lane: `c41-baseline-restart-20260803T1253Z`
Verifier: Tori
Protocol: `C41_STEP3_V3`
Record sample: the same fixed ranks 5, 15, 25, …, 175
Seed: 41

## Verdict: PASS_WITH_NOTES

The V3 gate passes all requested blocking checks:

- The targeted finding-on-methods/captions/references class is gone from the seeded zone sample.
- The quick fidelity reconfirmation passes 18/18 quotes, including 7/7 truncated quotes.
- No sampled record loses more than 20% of its spans from V2 to V3; the maximum loss is 3.45%.
- V3 removes the V2 duplicate-`span_id` regression: all 16,103 JSONL rows now have unique IDs.

One isolated non-blocking zone note remains. The only non-`unknown` row in the 53-row zone sample
is labeled `caption`, but its local context is ordinary result prose containing “Figure 12 shows,”
not a caption block. This is a conservative false-positive rather than a false scientific `finding`,
so under the supplied rule it supports PASS_WITH_NOTES rather than FAIL.

## Pinned inputs and sampling

- Original independent sample SHA-256:
  `d5f73d0e51c33ec0b59c682fd8cb7b01eb60fe474bf1058618e6fef00f2cd9e0`
- Step-2 manifest SHA-256:
  `fcc2ed2e8ca5b9e67339881c4fede7b14f29d04582b923848397b9d560dc72e8`
- Preserved V2 span-table SHA-256:
  `8c517bcf79d8795406ca4a3869af58bae49e76f99f9d9793b0e496cd6c55ff55`
- Current V3 span-table SHA-256:
  `c438c95d61a464ea9252b3215949d9cf305b6dd08de40ea0ca7c9a81500f1afc`

Zone sampling reinitialized `random.Random(41)`, visited the 18 fixed ranks in ascending order,
stable-sorted each record's V3 rows by the now-unique `span_id`, and drew three rows where available.
Rank 115 has only two spans, so both were checked; total zone sample: 53 rows.

Fidelity used a separate reinitialized `random.Random(41)` with the same rank order and sorted V3
rows, drawing one row per record; total fidelity sample: 18 rows.

Verifier-local evidence:

- `_tmp_tori3_recheck3.py`
- `_tmp_tori3_recheck3_raw.json`
- `_tmp_tori3_recheck3_nonunknown.md`
- `_tmp_tori3_recheck3_zone_adjudication.json`

## Zone re-check: PASS_WITH_NOTES

Seeded V3 zone distribution:

- `unknown`: 52/53 — accepted unconditionally by the controlling instruction
- `caption`: 1/53
- `finding`: 0/53
- `references`: 0/53

Adjudication:

- Passes: 52
- Clear misses: 0
- Notes: 1
- Targeted finding-on-method/caption/reference misses: 0

The V2 seeded sample had six targeted false-`finding` rows across six records. V3 has none. The
redesigned conservative zoning therefore removes the blocking defect class on the same seeded record
sample.

The one note is:

- `2013ApJ...765..140A_81127_81499`, rank 45 — labeled `caption`; the quote and context are a result
  paragraph containing “Figure 12 shows,” not an actual figure-caption block. This is an isolated
  conservative-label error and does not promote method/caption/reference text into a scientific
  finding.

## Fidelity spot-reconfirmation: PASS

One seeded V3 quote per sampled record was checked against the same locally cached full-text
extraction used in the earlier blind pass.

- Records checked: 18/18
- Quote is a verbatim source substring: 18/18 (100.00%)
- Quote equals the source at its claimed `char_range`: 18/18 (100.00%)
- Maximum nearest-source-start distance: 0 characters
- Sampled `truncated: true` rows: 7
- Truncated rows still exact verbatim source substrings: 7/7
- Non-substring, mangled, or inserted-character quotes: 0

The V2 fidelity repair remains intact after V3 regeneration.

## V2-to-V3 coverage guard

| Rank | Record | V2 spans | V3 spans | Delta | Loss |
|---:|---|---:|---:|---:|---:|
| 5 | `2024ApJ...962...24S` | 138 | 138 | 0 | 0.00% |
| 15 | `2024A&A...691A..19V` | 110 | 110 | 0 | 0.00% |
| 25 | `2020MNRAS.491.1427S` | 382 | 376 | -6 | 1.57% |
| 35 | `2017A&A...601A..95C` | 195 | 195 | 0 | 0.00% |
| 45 | `2013ApJ...765..140A` | 243 | 239 | -4 | 1.65% |
| 55 | `2010MNRAS.409..855B` | 58 | 56 | -2 | 3.45% |
| 65 | `2013MNRAS.432.2696M` | 17 | 17 | 0 | 0.00% |
| 75 | `2025ApJ...982...14H` | 114 | 113 | -1 | 0.88% |
| 85 | `2026MNRAS.546ag269C` | 59 | 59 | 0 | 0.00% |
| 95 | `2025ApJ...985...80R` | 59 | 58 | -1 | 1.69% |
| 105 | `2026JHEAp..5300626C` | 11 | 11 | 0 | 0.00% |
| 115 | `2026PhRvD.113h3007K` | 2 | 2 | 0 | 0.00% |
| 125 | `2024JCAP...07..078C` | 141 | 137 | -4 | 2.84% |
| 135 | `2023ApJ...943L..28K` | 24 | 24 | 0 | 0.00% |
| 145 | `2020MNRAS.493..580B` | 46 | 46 | 0 | 0.00% |
| 155 | `2015ApJ...808...25S` | 199 | 199 | 0 | 0.00% |
| 165 | `2009ApJ...697.1410L` | 34 | 34 | 0 | 0.00% |
| 175 | `2024ApJ...969L...2F` | 59 | 59 | 0 | 0.00% |
| **Total** | **18 records** | **1,891** | **1,873** | **-18** | **0.95%** |

No sampled record crosses the greater-than-20% loss threshold. The 18-row sampled reduction occurs
only in the six records that contained V2 duplicate IDs; all other sampled record counts are
unchanged.

## V3 integrity check

- Normal span rows: 16,102
- Explicit no-span marker rows: 1
- JSONL lines: 16,103
- Unique `span_id` values: 16,103
- Duplicate-ID extra rows: 0
- Records with normal spans: 179
- No-span record: `2024ApJ...972..143C`
- V3 summary protocol marker: `C41_STEP3_V3`

V2 had 16,177 normal rows and 75 conflicting duplicate IDs. V3's reduction to 16,102 normal rows is
exactly consistent with removing those 75 duplicate-ID rows; there is no additional aggregate loss.

## Gate boundary

This PASS_WITH_NOTES clears only this V3 span-table re-check. It does not itself authorize claim/status
ledger mutation, prose, DB writes, publication, deploy/restart, or git operations.

Boundary held: lane-only verifier writes, read-only cached sources elsewhere, no network, no model or
Deep Research call, and no modification to Goru artifacts.

TORI_STEP3_RECHECK3_COMPLETE_20260804
