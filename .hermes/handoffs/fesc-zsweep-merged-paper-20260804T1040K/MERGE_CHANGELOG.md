# MERGE CHANGELOG — MERGED_FESC_ZSWEEP.tex

Lane: `fesc-zsweep-merged-paper-20260804T1040K`. Author: Lana. 2026-08-04 11:01 KST.
Sources: ovl6221700 (z=7), ovl6221701 (z=8), ovl6221702 (z=9) in
`.hermes/handoffs/galaxy-evolution/lab-runs/overnight-fesc-sweep-20260803T1330Z/`;
trend-grid runs ovl726800–ovl726808 (z=6.0–10.0, Δz=0.5) in this lane;
binding guidance: `KUN_LC_REFEREE.md` (F0–F5 + per-draft findings); context: `MERIT_PANEL_SCORES.md` (E1–E6).

## What came from which source draft

| Merged-paper element | Source | Re-verified against |
|---|---|---|
| Title hedging style ("apparent … shortfall", conditional clause) | ovl6221702 (z=9) title, per Kun "KEEP as spine" | — |
| Positive headline claim (z=9 row: Δ=+0.302, +0.087..+0.697, 93%) | ovl6221702 abstract/result | ovl6221702.json + ovl726806.json (identical) + lane MC |
| z=7 clean null (Δ=+0.035, −0.072..+0.145, 66%) as a sweep row | ovl6221700 result | ovl6221700.json + ovl726802.json + lane MC |
| z=8 boundary case (Δ=+0.130, −0.003..+0.343, 83%) as the pivot row | ovl6221701 result | ovl6221701.json + ovl726804.json + lane MC |
| Maintenance formalism + anchor description | shared Data-and-method skeleton of all three, expanded from `tools/nm_ionizing_budget.py` (read-only) | tool source, lines 24–101 |
| Non-circularity test (O32-only vs β-only medians) | shared across drafts; per-z values now tabulated | run JSONs delta_O32/delta_beta + lane MC |
| Reference list (5 shared entries) | identical list in all three drafts | run JSONs `lit_reflist` (bibcodes) |
| Intro crisis framing (Muñoz/Davies/Duncan/Park/Madau) | all three intros, rewritten; citations demoted to framing-only per F3 | run JSONs `lit_papers` bibcodes |

New content with no source draft (computed in this lane, `make_trend_figure.py`):
the trend analysis itself — Δ(z) and shortfall-fraction curves, closure crossing
z_c=8.045 (boot 16–84%: 8.030–8.059), median crossing z_m=6.328 (6.316–6.336),
the boost_mode=none corner sweep (z_c=7.615; z=9 Δ=+0.163..+0.854, 96%), the
z≥9.5 f_req>1 tail note, Table 1, and the two-panel figure `fesc_zsweep_trend.pdf/png`.
The lane MC reproduces all 9 trend-grid run JSONs to max abs deviation 2.2e-16.

## Which Kun findings were fixed where

| Finding | Fix location in MERGED_FESC_ZSWEEP.tex |
|---|---|
| **F0** (salami; trend never analyzed; one z-sweep paper) | The entire paper: single draft, trend as central result (§3, Fig. 1, Table 1); no per-z repetition — z=7/8 appear only as sweep rows; Intro ¶2 discloses the supersession. |
| **F1(a)** proxies low-z-calibrated, transportability unvalidated | §2.3 (test-scope caveat) + §5 item 1 (dominant systematic, outside the MC; shortfall fractions stated as conditional). |
| **F1(b)** boost prior motivated by the same JWST observations | §5 item 2 names the structural circularity; §4 gives the direction argument (prior makes closure easier → cannot manufacture the shortfall). |
| **F1(c)** run the boost_mode=none corner, report if z=9 shortfall survives | Ran in lane (`make_trend_figure.py`): survives and strengthens (Δ16=+0.163, 96%); reported in abstract, §4, §5 item 2, Table 1 last column, Fig. 1 dotted curve. |
| **F2** docstring overpromise / anchors hard-coded, values not stated | §2.2 lists every frozen constant (proxy medians 0.08/0.05, scatters 0.45/0.40 dex, ξ_ion, C, boost forms, κ_UV, α_B) and states nothing is refetched at run time. |
| **F3** citation gate failed 3/3, 2/2, 1/1; broken [Muoz2024] key | §5 item 3 discloses the gate failures; all numerical inputs attributed to pipeline constants, literature cited for framing/formalism only; ξ_ion no longer attributed to Madau2017 (the failed entailment) but hedged as a representative anchor (e.g. Simmonds2024/Bouwens+16); reference key fixed to [Munoz2024] matching in-text usage (mojibake removed). |
| **F4** boilerplate caveats from a different study type | Old caveat sentences dropped entirely; §5 written for what this study is (item 4: "contains no measurements", named unpropagated systematics). |
| **F5** z=10 gate kill worth noting | §3 item 4 includes z=10 as boundary case with the expected-value-gate shelving disclosed; f_req>1 tail stated as an anchor statement, not a claim. |
| z=8 "least honest sentence" (CLOSES over 83% shortfall) | §3 item 3 + abstract: "closes only at the 1σ boundary; 83% of the systematic mass on the shortfall side" (Kun's demanded asymmetry statement). |
| z=6.5 non-robust flag in the trend grid (new, not in Kun's set) | Table 1 footnote a: both arms ±0.02 of zero adjacent to the median crossing z_m=6.33 — expected near a sign change, disclosed rather than hidden. |

## Merit-panel weaknesses shored up (E1–E6)

- E1 (identical figure in all drafts) → new lane-computed figure, z-specific by construction.
- E2 (JWST data contradiction) → §2.4 Provenance: no survey catalog data; the old "from public data (jwst)" abstract line is explicitly retracted.
- E3 (z-independent inferred side hidden) → stated in abstract, §2.2, Fig. 1 label ("z-independent by construction"), §3 ("the deficit rises monotonically because…").
- E4 (z=8 verdict tension, criterion never stated) → closure criterion defined explicitly (§3 item 2: interval detaches from zero); z=8 asymmetry stated.
- E5 (overlap with shipped landscape paper) → framing narrowed to the one question the landscape paper does not answer: locating z_c. (Not fully resolvable in-lane; flagged for the panel.)
- E6 ("dex-frac" unit ill-defined; caption=title duplication) → Δ defined as a linear escape-fraction difference with the old unit retired (§2.2); figure caption is descriptive, not a title copy.

## Numbers policy

Every number in the draft traces to (a) the 9 trend-grid run JSONs (verified
identical to the lane MC at 2.2e-16) or (b) `TREND_RESULTS.json` computed by the
lane script from the pipeline's own model/seed. Nothing was carried from the old
drafts' prose: the three source headline rows were re-verified against their run
JSONs (they match the trend-grid reruns exactly). The one number type NOT carried:
the old drafts' "dex-frac" phrasing and the z=8 "CLOSES" verdict sentence.

## Kun minor-revision fixes (R1–R4, KUN_MERGED_REFEREE.md) — Lana, 2026-08-04 11:16 KST

| Revision | Fix |
|---|---|
| **R1** (title's "$z \gtrsim 8$" includes z=8.0, where the interval still touches zero) | Title now reads "…robust to the stated systematics only **above $z \approx 8$**" (Kun's first suggested wording). Abstract/§3/conclusion untouched — Kun verified those as correct. |
| **R2** ("shortfall fraction at z_c is 84%" risks reading as tautology) | §3 item 2: appended Kun's pinning clause "(i.e., the 16th percentile of $\Delta$ touches zero there)". |
| **R3** ("survives intact" could read as "the same run") | §3 closing paragraph: added the half-sentence "— the row is a rerun of that calculation whose outputs are bit-identical to the original run's, not the original run itself (consistent with the Data availability statement)". |
| **R4** (bottom-panel y-label reads "freq") | Root cause: the .py source already said `^{\rm req}` (and did when Kun's figure was generated — mtimes: script 10:58:30 < figure 10:58:46 < referee 11:10:54); the rendered italic mathtext $f$ abutted the superscript and visually scanned as the word "freq". Fixed in `make_trend_figure.py` by inserting a thin space (`f_{\rm esc}^{\,\rm req}`, and symmetrically `^{\,\rm inf}`) and regenerating the PDF/PNG. |

Figure regeneration receipts (fixed seed 20260723, `lana_minor_run.log`): all numbers
bit-identical to the refereed version — verification vs 9 run JSONs max abs deviation
2.220e-16; z_c=8.045 (boot 8.030–8.059); z_m=6.328 (boot 6.316–6.336); none corner
z_c=7.615, z=9 Δ16=+0.163, shortfall survives. No numbers or structure changed anywhere.
