# TORI BRIEF — C41 Step 3 blind spot-verification (10%)

Lane: `c41-baseline-restart-20260803T1253Z`. You are Tori. Temps `_tmp_tori3_*` here only.
Purpose: blind quality check of Goru's mechanical span extraction (16,177 candidate spans, 180
records, 1 no-span record) before Step 4 builds the ledger on top of it.

## Blind protocol (order is the whole point)

1. **Sample first**: the 18 records at ranks 5, 15, 25, …, 175 of `SELECTION_INCLUDED.json`
   (deterministic, no choice).
2. **Independent pass BEFORE looking**: for each sampled record, read its cached full text
   (`cache_path` in `STEP2_FULLTEXT_MANIFEST.json`, extract via `tools/nm_fulltext_layer.py`)
   and write YOUR OWN list of axis-bearing quantitative/comparative sentences
   (`_tmp_tori3_independent.jsonl`) using the same Step-1 lexicons (`step1_filter.py`). Cap ~15
   per record — you are sampling recall, not re-doing the stage. Sha-stamp this file and record
   the sha in your report BEFORE step 3.
3. **Only then** open `SPAN_TABLE.jsonl` for those 18 records and compare:
   - **Recall**: how many of your independent sentences does Goru's table cover (same or
     overlapping text)? Report per-record and overall coverage %.
   - **Fidelity**: for 3 random spans per record (seed 41), verify the quote appears VERBATIM in
     the source text at (approximately) the claimed location. Report any fabricated/mangled quote
     — that is an automatic FAIL.
   - **Zone sanity**: for the same spans, is the zone label defensible from context? (`unknown` is
     always acceptable; a `finding` label on obvious methods text is a miss.)

## Deliverable

`TORI_STEP3_SPOTCHECK.md`: verdict **PASS / PASS_WITH_NOTES / FAIL** (FAIL = any fabricated quote,
or overall recall < 70%, or systematic zone mislabeling), the stats above, your independent-file
sha, anomalies. End with marker: `TORI_STEP3_SPOTCHECK_COMPLETE_20260804`.

## Constraints

Read-only outside the lane; no network; do not modify Goru's artifacts; do not read his report's
conclusions before your independent pass (the summary counts you already know are fine).
