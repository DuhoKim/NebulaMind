# GORU BRIEF — C41 Step 3: mechanical candidate-span extraction

Lane: `c41-baseline-restart-20260803T1253Z` (write ONLY here; temps `_tmp_goru_*` here).
Gate: Duho — "APPROVE C41 STEP 3". You are Goru (Antigravity/Gemini seat) — the MECHANICAL lane.
Your output is CANDIDATE spans: over-extraction is acceptable, silent omission is not. Semantic
judgment (what becomes a ledger claim) happens downstream in Steps 4–5, not here. Tori will
blind-spot-verify 10% of your table against the source texts afterward.

## Inputs (read-only)

- `STEP2_FULLTEXT_MANIFEST.json` — 180 records with `cache_path` per record (PDFs + HTMLs under
  the engine `fulltext_cache/`). Verify its input-seal shas before starting.
- Text extraction: use `tools/nm_fulltext_layer.py` (`extract_text` for PDFs,
  `extract_html_structured` for HTML) — tracked on main as of PR #133.
- Axis lexicons, verbatim from the sealed Step-1 filter (`step1_filter.py`) — reuse ITS term
  lists (three axes + strict-tension terms) so Step 3's notion of "axis-bearing" is identical to
  Step 1's. Do not invent new vocabulary.
- Span schema reference: the AGN pilot's span rows in
  `docs/claim_ledger_contract_v1_agn_20260703T0830Z/artifacts/` (span id format, zone vocabulary).

## Method (deterministic driver, not hand-reading)

Author `step3_extract.py` in the lane dir and run it:
1. Per record: extract text; segment into sentences/blocks with character offsets and (for PDFs)
   page estimates; classify each block's **rhetorical zone** by mechanical heuristics
   (heading proximity: abstract/intro/method/result-finding/discussion-interpretation/conclusion;
   fall back to `unknown`, never guess semantically).
2. Emit a candidate span for every sentence window that (a) hits an axis lexicon term AND
   (b) contains a quantitative or comparative signal (number, %, dex, σ, "higher/lower/consistent/
   rules out/cannot explain", strict-tension term). Window = the sentence ± one neighbor;
   quote capped at 600 chars.
3. Per span: `span_id` (deterministic from identity+offset), record identity, quote, char range,
   page estimate, zone, axis tags, trigger terms, extraction flags (e.g. `pdf_text_noisy`).
4. Per record with ZERO spans: emit a `no_span_record` row with the reason
   (extraction_failed / no_axis_sentence) — these are shrink-ladder and no_info inputs, not
   silent drops.

## Deliverables (lane dir)

1. `step3_extract.py` — deterministic (fixed ordering, no randomness), stdlib + nm_fulltext_layer.
2. `SPAN_TABLE.jsonl` — all candidate spans; plus `STEP3_SUMMARY.json` (per-record span counts,
   zone histogram, axis-tag histogram, no-span records, total), with an input-manifest block
   sha-pinning the Step-2 manifest and your own driver.
3. `GORU_STEP3_REPORT.md` — counts, runtime, extraction-quality notes (how many PDFs were noisy),
   anomalies; safety-boundary statement. End with marker: `GORU_STEP3_COMPLETE_20260804`.

## Hard constraints

No network (all texts are local). Writes only in this lane dir. No git, no DB, no product
surfaces. Do not modify the fulltext cache, the sealed selection, or any Step-1/2 artifact.
Do not read the AGN map lane, the f_esc sweep dir, or the excluded-papers list. If extraction
fails on >20% of records, STOP and report the blocker rather than shipping a hollow table.
