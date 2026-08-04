# Tori C41 Step-3 blind 10% span spot-verification

Lane: `c41-baseline-restart-20260803T1253Z`
Verifier: Tori
Protocol: fixed ranks 5, 15, 25, …, 175 (18/180 records = 10%)

## Verdict: FAIL

Recall passes at 94.19%, but the supplied fail rule is conjunctive: any fabricated or mangled quote
is an automatic FAIL. In the seeded fidelity sample, 16 of 53 sampled quotes were hard-truncated to
600 characters and ended in an inserted literal `...` that does not occur in the cached extracted
source. Those quotes are mangled rather than verbatim. I found no invented scientific clause beyond
that truncation mechanism, but the truncation alone triggers FAIL.

Zone labeling also shows a repeated secondary defect: 10/53 sampled labels were not defensible from
context, including 5/14 sampled `finding` labels applied to obvious methods, captions, or a reference
transition. That pattern is systematic enough to require relabeling before Step 4 consumes the table.

## Blindness receipt

I followed the required order:

1. Selected only ranks 5, 15, 25, …, 175 from `SELECTION_INCLUDED.json`; there was no discretionary
   choice.
2. Resolved all 18 records through `STEP2_FULLTEXT_MANIFEST.json` and read their cached HTML/PDF full
   texts using the extraction functions in `tools/nm_fulltext_layer.py`.
3. Used the Step-1 axis lexicons from `step1_filter.py`, then independently retained 155
   axis-bearing quantitative/comparative sentences, between 2 and 11 per sampled record and never
   more than 15.
4. Wrote and sealed `_tmp_tori3_independent.jsonl` before the first read of `SPAN_TABLE.jsonl`.
5. Only after that seal did I open the sampled records' Goru spans. I did not open Goru's report
   conclusions.

Independent-file receipt, created and verified before comparison:

- File: `_tmp_tori3_independent.jsonl`
- SHA-256: `d5f73d0e51c33ec0b59c682fd8cb7b01eb60fe474bf1058618e6fef00f2cd9e0`
- Receipt: `_tmp_tori3_independent.sha256`
- Rows: 155

Pinned read-only inputs used in the check:

- `STEP2_FULLTEXT_MANIFEST.json` SHA-256:
  `fcc2ed2e8ca5b9e67339881c4fede7b14f29d04582b923848397b9d560dc72e8`
- `SPAN_TABLE.jsonl` SHA-256:
  `45bb0e237b9744464301f9bb969dbeb83f152ae335fabf7d02aaeeef113eb7cb`

## Comparison rules

Recall counted an independent sentence as covered when a Goru span covered at least 90% of its
source character range, or when normalized text containment established the same/overlapping text.
The range and containment tests agreed on the 146 covered rows; the nine misses had no overlap.

Fidelity sampling used one `random.Random(41)` stream, ascending sampled rank, with each record's
spans sorted by `span_id` before `sample`. Three unique spans were drawn per record where possible.
Rank 115 had only two spans, so both were checked; the total unique fidelity sample is 53 rather than
54.

For fidelity classes:

- `verbatim exact`: quote equals the cached extracted source at the claimed character range;
- `whitespace-only`: wording is preserved under whitespace normalization but is not literally
  verbatim;
- `ellipsis-truncated/mangled`: quote is cut to 600 characters and contains an inserted terminal
  `...` absent from the source.

For zone sanity, `unknown` was always accepted. Other labels were judged from the quote and local
source context; finding-on-method/caption text was counted as a miss.

## Per-record results

`V/W/T` = verbatim-exact / whitespace-only / ellipsis-truncated-mangled in the seeded fidelity
sample. `Z ok/miss` is zone sanity.

| Rank | Record | Independent | Covered | Recall | Goru spans | Fidelity n | V/W/T | Z ok/miss |
|---:|---|---:|---:|---:|---:|---:|---:|---:|
| 5 | `2024ApJ...962...24S` | 9 | 8 | 88.89% | 138 | 3 | 3/0/0 | 3/0 |
| 15 | `2024A&A...691A..19V` | 4 | 4 | 100.00% | 110 | 3 | 3/0/0 | 2/1 |
| 25 | `2020MNRAS.491.1427S` | 11 | 11 | 100.00% | 382 | 3 | 2/0/1 | 3/0 |
| 35 | `2017A&A...601A..95C` | 8 | 8 | 100.00% | 195 | 3 | 2/1/0 | 2/1 |
| 45 | `2013ApJ...765..140A` | 11 | 10 | 90.91% | 243 | 3 | 3/0/0 | 3/0 |
| 55 | `2010MNRAS.409..855B` | 9 | 9 | 100.00% | 58 | 3 | 0/0/3 | 3/0 |
| 65 | `2013MNRAS.432.2696M` | 6 | 5 | 83.33% | 17 | 3 | 2/0/1 | 3/0 |
| 75 | `2025ApJ...982...14H` | 11 | 11 | 100.00% | 114 | 3 | 1/2/0 | 3/0 |
| 85 | `2026MNRAS.546ag269C` | 10 | 10 | 100.00% | 59 | 3 | 1/0/2 | 1/2 |
| 95 | `2025ApJ...985...80R` | 10 | 10 | 100.00% | 59 | 3 | 1/2/0 | 2/1 |
| 105 | `2026JHEAp..5300626C` | 9 | 7 | 77.78% | 11 | 3 | 0/1/2 | 2/1 |
| 115 | `2026PhRvD.113h3007K` | 2 | 2 | 100.00% | 2 | 2 | 0/0/2 | 2/0 |
| 125 | `2024JCAP...07..078C` | 8 | 8 | 100.00% | 141 | 3 | 0/0/3 | 1/2 |
| 135 | `2023ApJ...943L..28K` | 9 | 7 | 77.78% | 24 | 3 | 2/1/0 | 1/2 |
| 145 | `2020MNRAS.493..580B` | 7 | 6 | 85.71% | 46 | 3 | 1/2/0 | 3/0 |
| 155 | `2015ApJ...808...25S` | 11 | 10 | 90.91% | 199 | 3 | 1/1/1 | 3/0 |
| 165 | `2009ApJ...697.1410L` | 10 | 10 | 100.00% | 34 | 3 | 0/3/0 | 3/0 |
| 175 | `2024ApJ...969L...2F` | 10 | 10 | 100.00% | 59 | 3 | 2/0/1 | 3/0 |
| **Total** | **18 records** | **155** | **146** | **94.19%** | **1,891** | **53** | **24/13/16** | **43/10** |

## Recall findings

Overall recall is 146/155 = 94.19%, above the 70% gate. Per-record recall ranges from 77.78% to
100%; no sampled record falls below 70%.

The nine uncovered independent sentences were:

- rank 5 `r005-i08`: FMR metallicity decreases with increasing SFR at fixed stellar mass;
- rank 45 `r045-i03`: model avoidance of MZR normalization because of yield/calibration-scale
  uncertainty;
- rank 65 `r065-i02`: the LF's importance to earliest-galaxy evolution and reionization;
- rank 105 `r105-i04`: the open astrophysical interpretation of the large inferred efficiency;
- rank 105 `r105-i08`: negative correlation between structure growth and star-formation efficiency;
- rank 135 `r135-i04`: future z~11 mass-function constraints could strengthen or remove the tension;
- rank 135 `r135-i08`: simulations reproduce low-redshift population statistics;
- rank 145 `r145-i05`: ionizing-field shape is unlikely to cause the BPT offset;
- rank 155 `r155-i01`: the M*-Z-SFR relation is not invariant because of systematic high-mass
  metallicity differences.

These are isolated misses rather than a recall-system failure.

## Fidelity findings

Seeded sample: 53 unique spans.

- 24/53 (45.28%) are byte-for-byte verbatim at the claimed range.
- 13/53 (24.53%) preserve wording under whitespace normalization only.
- 37/53 (69.81%) therefore preserve the full sampled wording if whitespace normalization is allowed.
- 16/53 (30.19%) are hard-truncated/mangled: each is 600 characters long, ends with an inserted
  literal `...`, and omits remaining source text inside the published `char_range`.
- 0 sampled spans contained invented scientific wording apart from the truncation/ellipsis behavior.

The 16 mangled quotes occur across nine sampled records (ranks 25, 55, 65, 85, 105, 115, 125,
155, and 175). `extraction_flags` is empty for every sampled span, including these truncations, so a
consumer cannot identify them as non-verbatim from the row metadata.

Because the brief defines any mangled quote as an automatic failure, this defect alone fixes the
verdict at FAIL even though recall passes.

## Zone-sanity findings

- Zone-sane: 43/53 (81.13%).
- Zone misses: 10/53 (18.87%).
- Sampled `finding` labels: 14; clear finding-on-method/caption/reference misses: 5/14 (35.71%).

The ten misses were:

1. `2024A&A...691A..19V_53795_54090`: figure/map-construction caption labeled `finding`.
2. `2017A&A...601A..95C_96589_96889`: section-background framing labeled `method`.
3. `2026MNRAS.546ag269C_22884_23518`: explicit model prescription labeled `interpretation`.
4. `2026MNRAS.546ag269C_26180_27257`: model equations/calculation labeled `finding`.
5. `2025ApJ...985...80R_35284_35608`: SED-template generation labeled `finding`.
6. `2026JHEAp..5300626C_8239_8395`: reference footnote/section transition labeled `finding`.
7. `2024JCAP...07..078C_15111_16061`: model equation/procedure labeled `background`.
8. `2024JCAP...07..078C_47154_47761`: analysis calculation/figure description labeled `background`.
9. `2023ApJ...943L..28K_9870_10325`: simulation-resolution text plus figure caption labeled
   `finding`.
10. `2023ApJ...943L..28K_11053_11408`: a simulation result labeled `method`.

The repeated finding-on-method/caption pattern is systematic rather than one ambiguous boundary.

## Anomalies

- The current `SPAN_TABLE.jsonl` contains 16,178 unique span rows over all 180 record identities,
  not the 16,177 rows and one no-span record stated in the brief summary. The table has no duplicate
  `span_id`; its minimum is one span for a record. I did not inspect non-sampled span content during
  this aggregate count.
- Sampled rank 115 has only two spans, so the fidelity check used both rather than duplicating one to
  force a nominal third draw.
- A first attempt to re-extract the already-selected independent sentences in the isolated
  `execute_code` environment lacked `bs4` and stopped before writing the independent file. I reran
  the same frozen selection with the project Python used by the full-text tool, then wrote and
  SHA-sealed the file. No Step-3 table had been opened at that point.

## Required repair before Step 4

Step 4 should not consume the current table as a verbatim quote source. Regenerate each quote from an
exact source slice with no inserted ellipsis and with a character range that covers exactly the
published quote; if excerpts must be shortened, shorten at a source boundary while preserving exact
text. Then rerun zone labeling with an explicit guard against `finding` on method/caption/reference
text and repeat this blind spot-check. The recall extractor itself does not need broadening based on
this sample.

Boundary held: read-only outside the lane, no network, no model/Deep Research call, no modification
to Goru artifacts, and no Step-4 ledger/prose action.

TORI_STEP3_SPOTCHECK_COMPLETE_20260804
