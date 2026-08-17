PASS_R1_MARGIN_COVERAGE

# Kun R1 margin-coverage re-gate

Date: 2026-08-17 KST
Scope: document and local evidence review only. No network, no HEAD, no TAP query, no download, no endpoint, no commit, no push.

## 1. Entailment And Lemma

The entailment is sound, and the lemma is table-wide from retained brick-level data, not sampled.

I recomputed the relevant facts from `_tmp_r1_margin_20260817/brick_features.csv`, which has 366,912 data rows:

- `nexphist_r sum > 0`: 330,618 bricks
- `nexphist_r sum = 0`: 36,294 bricks
- `cosky_r != 0`: 330,618 bricks
- `cosky_r == 0`: 36,294 bricks
- `nexphist_r` / `cosky_r` disagreements: 0
- `{nexphist_r sum = 0} ∩ {nexp_r > 0}`: 0
- `{nexphist_r sum = 0} ⊆ {nexp_r = 0}`: verified table-wide

Therefore, if a planned margin brick lacked `image-r`, the exact indicator would place it in `{hist = 0}`; the table-wide lemma places it in `{nexp_r = 0}`; and the prior R1 enumeration of planned margin bricks with `nexp_r = 0` would have included it. Those 138 distinct implicated bricks were HEAD-verified present. The contradiction closes the prior proxy-confidence hold.

## 2. Exhaustiveness Of Planned ∩ `nexp_r=0`

The prior enumeration is genuinely forward-derived from planned margin sets. `_tmp_margin_counts.py` imports the gated adapter, computes each object's planned margin set, flags objects whose planned set contains `nexp_r == 0`, and writes the implicated brick list from those planned flagged objects. `_tmp_implicated_head_recount.py` then consumes that implicated set and recounts with the same adapter predicate.

This is the same derivation I checked in the prior hold. No reverse derivation or convenience list is doing the work.

## 3. Indicator Exactness

The indicator's file-presence exactness remains sample-proven, not census-proven, and the finding says that plainly. For R1, that is enough because the table-wide lemma bounds the silent direction that mattered to the hold.

A residual error in the absent-but-predicted-present direction would not silently drop an object: it would make the manifest require a file that the harvest/retrieval cannot prove, yielding a terminal missing-file custody event. The dangerous silent direction for R1 is present/predicted-absent or absent hidden outside the enumerated set; the table-wide `{hist=0} ⊆ {nexp_r=0}` lemma plus the exhaustive 138/138 check closes that route for the frozen parent margin set.

## 4. R2 Recommendation

The R2 recommendation is acceptable: classify `absent-by-coverage` for planning with the exact indicator (`nexphist_r sum > 0` / `cosky_r != 0`), then let the checksum harvest ground-truth every classification from the survey `.sha256sum` listings.

That keeps the indicator in the planning role and the harvest in the proof role. It satisfies R2's distinction between absent-by-coverage and missing-unexpectedly, provided the manifest gate treats any checksum-list contradiction as terminal or reclassifying before approval, never as a silent skip.

## 5. Clause-4 Gap And Aggregate-Only Status

The clause-4 gap ruling stands unchanged. Missing pre-deletion SHA-256 digests for transient position CSVs remain a real recorded custody gap. Not re-materializing them was the right call because doing so would recreate the bounded exposure and would not recover byte-identical deleted files.

No positions were re-materialized for this repair. Local `find` shows no `positions_part*.csv` and no `_tmp_rless_implicated.txt` surviving in this workspace. The new repair is brick-level only.

No R1 receipt/evidence file is tracked by git. The retained evidence contains public brick metadata and sampled public brick labels, not object rows, per-object positions, or object identifiers. Query text files do contain the old ADQL selections, including `ra`, `dec`, `ls_id`, and `objid` in joins, but they are query texts, not result rows or identifiers; they remain uncommitted.

## 6. Pinned Checks

- `R1_EXACT_INDICATOR_20260817.md`: `dfc65b03a272d12129ca543d5aa0da1671da07a11bedaa6c91facf2b5e05648e`
- amended `R1_MARGIN_COVERAGE_20260817.md`: `2e27a414ced2a6ca091c52fcf851dd2bae7014136bfd99298fd6ff21dc7c69a7`
- prior HOLD `KUN_R1_MARGIN_COVERAGE_GATE_20260817.md`: `4562a0cfbdee84ff7b05efa481a62bf4bd9c0ab995b83988c1a6f1f82f447841`
- `exact_indicator_labels.json`: `a2aef3fd55057e54958708a9460563aa154e82f53bb75398282ed663c7f9faf1`
- `brick_features.csv`: `8cc77f6daaafafd1056eca00530a45c3da8cfbda9a9e350e3dcb9bec0a06aac3`
- adapter `adapter/nm_brick_cutout_adapter.py`: `267b2a93d2a61f65b281aeb3b04dd874d7add058797b10f593cb3efb4066006f`
- binding `TORI_ROUTE_BINDING_SUCCESSOR_20260817.md`: `1371b11094a2765228a7deb1bbe1367117c9452dbea4513519bf99b7ce23fe8b`, mode `444`
- prereg `PREREG_LONGO_AMPLITUDE_TEST_FROZEN_20260815_V3.md`: `b06901c8a0f3a0570af41262453670589d8dc0b20c79c7d4162853c7dfec42d7`, mode `444`

## Boundary

Network calls: 0. HEAD requests: 0. TAP queries: 0. Downloads: 0. Image bytes touched: 0. FITS files fetched: 0. Checksum harvest: 0. Manifests built: 0. Endpoints activated: 0. Commit/push/publication: 0.
