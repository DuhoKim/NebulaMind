# LANA MERGE REPORT — merged f_esc z-sweep paper

Lane: `fesc-zsweep-merged-paper-20260804T1040K`. Completed 2026-08-04 11:03 KST (02:03 UTC).
Direction: Duho — "go with the merged z-sweep paper" (logged in
`fesc-zsweep-photon-budget_history.json`, not edited). Binding guidance: `KUN_LC_REFEREE.md`.

## Deliverables (all in this lane dir)

1. `MERGED_FESC_ZSWEEP.tex` — single AASTeX (aastex631, twocolumn) manuscript; z=9 draft
   (ovl6221702) as spine per Kun, z=6.0–10.0 sweep with the trend as the central result;
   structure verified balanced (all environments matched, braces balanced, escapes checked).
   NOT compiled to PDF in-lane: no LaTeX toolchain on this host (`pdflatex` absent,
   `aastex631.cls` not in kpse; the source drafts were compiled by the Lab runner, which has
   its own toolchain). Figure is referenced as `fesc_zsweep_trend.pdf` alongside the .tex.
2. `fesc_zsweep_trend.pdf` + `fesc_zsweep_trend.png` — the central two-panel figure
   (required-vs-inferred f_esc bands over z; Δ(z) with 16–84% band, closure crossing marked,
   no-JWST-tail corner overlaid, per-run shortfall percentages). Palette CVD-validated.
3. `make_trend_figure.py` — lane script; imports the pipeline model read-only, reproduces
   the exact MC (seed 20260723, N=40000, identical rng stream order).
4. `TREND_RESULTS.json` — computed shortfall/Δ quantiles per grid z, closure crossing with
   bootstrap interval, median crossing, full boost_mode=none corner, verification record.
5. `MERGE_CHANGELOG.md` — source-draft provenance table + Kun-finding→fix location table +
   merit-panel E1–E6 repairs.

## Central computed results (lane MC, verified vs run JSONs at 2.2e-16 max deviation)

- **Closure crossing z_c = 8.045** (bootstrap 16–84%: 8.030–8.059) — where the 16–84%
  interval of Δ(required−inferred) detaches from zero. Kun bracketed it between z=8 and 9;
  on the fine grid it sits just above z=8. Shortfall fraction is 84% there by construction.
- **Median crossing z_m = 6.328** (6.316–6.336) — median deficit changes sign.
- **Trend:** shortfall fraction rises monotonically 41% → 97% over z=6→10 (66/83/93% at
  the original 7/8/9 points, matching the source drafts exactly).
- **Kun F1(c) corner (boost_mode=none):** the z=9 shortfall SURVIVES and strengthens —
  Δ interval +0.163..+0.854, 96% shortfall; crossing moves earlier to z_c=7.615
  (7.602–7.631). Direction note: the JWST-SFRD tail *increases* ρ_UV and so *lowers*
  required f_esc — the fiducial (crisis-correlated) prior is conservative for the shortfall
  claim. (Kun's F1 text implied the opposite sign of this shift; the corner run settles it,
  and the paper reports the computed direction.)
- z≥9.5 tail: 84th-percentile required f_esc exceeds 1 (unphysical) — stated in the paper
  as an anchor statement, not a claim.

## Kun findings — all addressed

F0 one-paper/trend-central (the whole draft), F1a/b/c (§2.3, §4, §5 items 1–2, corner run),
F2 anchors listed in full in §2.2 with the no-refetch statement, F3 gate failures disclosed
in §5 item 3 + [Munoz2024] key fixed + the failed Madau2017 ξ_ion attribution removed,
F4 boilerplate caveats replaced with study-specific limitations, F5 z=10 gate history
disclosed in §3. z=8 asymmetry stated exactly as Kun demanded ("closes only at the 1σ
boundary; 83% of the systematic mass shows a shortfall"). Merit-panel E1–E6 also repaired
(see changelog). New honesty item found in-lane: the z=6.5 grid point's non-circularity
flag is false (both arms ≈0 next to the sign change) — disclosed in Table 1 footnote.

## Constraints honored

No network. No git/DB writes. Writes confined to this lane dir. C41/AGN lanes not read.
Paper-history file read but not edited. Every number in the draft traces to the 9 trend-grid
run JSONs or `TREND_RESULTS.json`; nothing carried from the old drafts without
re-verification (the three source headline rows match their run JSONs and the trend-grid
reruns exactly).

## Verification hashes

- shasum MERGED_FESC_ZSWEEP.tex → recorded in lane log
- Lane MC vs 9 run JSONs: max abs deviation 2.220e-16 (all 9 match)

LANA_FESC_MERGE_COMPLETE_20260804
