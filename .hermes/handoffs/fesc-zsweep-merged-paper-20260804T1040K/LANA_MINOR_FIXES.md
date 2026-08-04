# LANA MINOR FIXES — Kun R1–R4 applied

Lane: `fesc-zsweep-merged-paper-20260804T1040K`. Author: Lana. 2026-08-04 11:16 KST.
Spec: `KUN_MERGED_REFEREE.md` § REQUIRED REVISIONS (verdict MINOR). Scope held: the four
fixes only — no numbers changed, no structure changed, lane-only writes.

## R1 — title clause accuracy

- Was: "…becomes robust to the stated systematics only at $z \gtrsim 8$"
- Now: "…becomes robust to the stated systematics only **above $z \approx 8$**"
- Kun's first suggested wording, verbatim. "≳ 8" included z=8.0, where the paper's own
  Table shows the 16th percentile still at −0.003; "above z ≈ 8" excludes it. The
  abstract, §3, and conclusion statements Kun verified as correct are untouched.

## R2 — pinning clause in §3 item 2

- Was: "By construction the shortfall fraction at $z_c$ is 84\%."
- Now: "By construction the shortfall fraction at $z_c$ is 84\% (i.e., the 16th
  percentile of $\Delta$ touches zero there)."
- Kun's exact requested clause, pinning the 84% as the geometric consequence of the
  crossing definition rather than a tautology or a coincidence left unexplained.

## R3 — rerun provenance in §3 closing paragraph

- Was: "The $z\sim9$ headline of the superseded drafts survives intact as one row of
  this trend: $\Delta = +0.302$…"
- Now: "…survives intact as one row of this trend --- the row is a rerun of that
  calculation whose outputs are bit-identical to the original run's, not the original
  run itself (consistent with the Data availability statement): $\Delta = +0.302$…"
- Half a sentence, making §3 consistent with the Data availability section. The
  underlying bit-identity (ovl726806 vs the overnight ovl6221702 line) was verified by
  Kun and is unchanged.

## R4 — figure y-label ("freq" → "req"), with a root-cause note

Finding on inspection: the `make_trend_figure.py` source **already** read
`f_{\rm esc}^{\rm req}` — including when the figure Kun refereed was generated
(mtimes: script 10:58:30 → figure 10:58:46 → Kun's report 11:10:54; no intervening
edit). Pixel-level zoom of the shipped PNG confirms the superscript is the three
glyphs "req" (same width as "inf"). What Kun saw is real, though: the italic mathtext
$f$ abuts the superscript so the label visually scans as the word "freq" at print
size — a journal referee could make the same read.

Fix: inserted a thin space between the base and the superscript in the y-label
(`f_{\rm esc}^{\,\rm req} - f_{\rm esc}^{\,\rm inf}`, symmetric on both terms) and
regenerated the figure via `make_trend_figure.py`. The label now shows clear daylight
between $f$ and "req" (verified by zoom of the new PNG). No LaTeX-side change was
needed: the manuscript's own math already used `^{\rm req}` correctly everywhere.

## Regeneration receipts (no numbers moved)

`python3 make_trend_figure.py` rerun in-lane (log: `lana_minor_run.log`), fixed seed
20260723, N=40,000. Output identical to the refereed version:

- verification vs the 9 trend-grid run JSONs: max abs deviation 2.220e-16
- closure crossing z_c = 8.045 (bootstrap 16–84%: 8.030–8.059)
- median crossing z_m = 6.328 (bootstrap 16–84%: 6.316–6.336)
- boost=none corner: z_c = 7.615; z=9 Δ16 = +0.163; shortfall survives: True
- `TREND_RESULTS.json` rewritten deterministically with the same values;
  `fesc_zsweep_trend.pdf/png` regenerated (only the y-label spacing differs)

## Files touched (all inside this lane)

- `MERGED_FESC_ZSWEEP.tex` — R1 (title), R2 (§3 item 2), R3 (§3 closing ¶)
- `make_trend_figure.py` — R4 y-label thin-space fix (+2-line comment)
- `fesc_zsweep_trend.pdf`, `fesc_zsweep_trend.png`, `TREND_RESULTS.json` — regenerated
- `MERGE_CHANGELOG.md` — R1–R4 entries appended
- `lana_minor_run.log` — regeneration output
- `LANA_MINOR_FIXES.md` — this report

LANA_MINOR_FIXES_COMPLETE_20260804
