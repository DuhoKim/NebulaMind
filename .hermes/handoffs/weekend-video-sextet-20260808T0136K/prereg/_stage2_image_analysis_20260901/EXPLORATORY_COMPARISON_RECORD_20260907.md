# The machine–human comparison Duho asked for, in plain numbers — descriptive only
2026-09-07 23:36 KST, stamped from `date`. HWAO, recording Codex's completed diagnostic in the lane.
Duho approved the limited 400-object exploratory comparison with **"sounds good"**. Codex ran it
directly — no worker, no new study. Completion 2026-09-07T14:34:42Z, 554.8 s.

## The answer, in ordinary words
Of the 400 galaxies whose human classifications this run had already exposed, the machine produced a
usable spin sign for **388** (12 refused on data-integrity grounds, not on anything to do with the
answer). Comparing those 388 to the human labels:

* the machine's sign convention is **opposite** to the humans' — with the raw convention it agrees
  **77/388 = 19.85%**;
* flipping that one global convention, it agrees **311/388 = 80.15%** (**77.75%** if the 12 refusals
  are counted as misses, i.e. 311/400).

**80.15% is the number to quote**, with the flip stated alongside it, and it is a *descriptive* number
on development data — not a validated instrument, not an unseen-data result.

## What I verified myself, from `per-object.jsonl` (`6d38f983…`)
Recomputed independently rather than taken on trust: 400 rows, 400 distinct object IDs, **388 SCORED /
12 RENDER-REFUSED** (9 `F exceeds 5% ceiling`, 3 `flagged pixel inside protected region`), one single
`config_id`, raw **77** and flipped **311** summing exactly to 388, human labels **195 negative / 193
positive**, all 388 same-process repeat evaluations bit-identical, 388 distinct tensor digests.
Every figure in the completion notice reproduces.

Two checks of my own that the notice did not carry:

| check | value |
|---|---|
| confusion (human, machine) | (−1,−1) 44 · (−1,+1) **151** · (+1,−1) **160** · (+1,+1) 33 |
| majority-class baseline | 195/388 = **50.26%** |
| flipped agreement, descriptive Wilson 95% | **[75.90%, 83.82%]** |
| by human class, flipped | negative 77.44% · positive 82.90% |

So the agreement is **not** an artefact of class imbalance — the sample is near-balanced and the
majority baseline is 50.26% — and it holds at similar strength in both human classes.

## The honest caveats, stated once
* **The sign flip is one bit fitted on this same data.** It is a single global convention, not a
  per-object choice, so it costs exactly one binary parameter — but 80.15% is therefore the better of
  two conventions chosen after looking. Say "80.15% after one global sign convention", never "80.15%
  accuracy".
* **These 400 are development data.** Their labels were exposed to this lane. Nothing here is an
  unseen-data measurement.
* **Historical attempt 2 stays void and option (A) stays closed.** This diagnostic neither restores an
  attempt nor licenses Tier-C. Its records and the closure records are preserved separately.
* Codex's reconciliation was a separate deterministic script — verification, **not** a separate
  scientific review, and I do not present it as one.

Source records (kept where they are, not copied in): `REPORT.md`, `summary.json` (`3c056330…`),
`per-object.jsonl` (`6d38f983…`), baseline manifest (`04640a2b…`) under
`/Users/duhokim/work/Trio/EXPLORATORY_COMPARISON_20260907/`.
