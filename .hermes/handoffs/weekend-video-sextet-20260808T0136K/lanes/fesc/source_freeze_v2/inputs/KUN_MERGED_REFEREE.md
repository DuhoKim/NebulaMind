# KUN REFEREE — MERGED f_esc z-sweep draft

Lane: `fesc-zsweep-merged-paper-20260804T1040K`
Referee: Kun (Kimi K3 via Nous). Date: 2026-08-04 ~11:20-12:00 KST.
Target: `MERGED_FESC_ZSWEEP.tex` + `fesc_zsweep_trend.pdf/png` + `TREND_RESULTS.json` + `MERGE_CHANGELOG.md` + trend-grid runs ovl726800–808.
Posture: this merge implements MY OWN prescription (KUN_LC_REFEREE.md F0–F5 + per-draft notes). I re-verified everything from the model and run JSONs rather than trusting the changelog — including re-running the Monte-Carlo and the crossing computations independently.

## REFEREE VERDICT: MINOR

This is a different paper from the three I dissected, and it is the paper I asked for. The salami structure is gone (one draft, trend as central result, per-z material demoted to table rows). Every F-finding from my L-C review is addressed at the place the changelog claims — and I checked each against the text, not the changelog. The numbers are exact: the lane recomputation reproduces all nine trend-grid run JSONs to max abs deviation 2.2×10⁻¹⁶ (I recomputed this myself — same value), the trend-grid reruns at z=7/8/9 are bit-identical to the overnight runs I refereed (`fesc` dicts equal), and the headline crossing claims match TREND_RESULTS.json exactly (z_c=8.045, bootstrap 8.030–8.059; z_m=6.328, 6.316–6.336). My own independent re-execution of the model (dense z-scan, same seed/constants, fresh streams) gives z_c ≈ 8.06, z_m ≈ 6.34, none-corner z_c ≈ 7.61, none-corner z=9 interval +0.163/+0.412/+0.854 at 95.7% shortfall, boost ratio 1.283 — all within Monte-Carlo stream noise of the manuscript's values. The figure (visually inspected) matches its caption: dashed z_c line, dotted no-boost 16th-percentile curve, per-point shortfall annotations, z-independent inferred side labeled "by construction", no defects.

The MINOR verdict (not ACCEPT) rests on four required-but-small items below — none touches the science; all are precision-of-claim fixes a referee can verify in one pass.

## F-FINDING CLOSURE AUDIT (each verified against the .tex, not the changelog)

- **F0 (salami/trend unanalyzed) — FIXED.** Single manuscript; Intro ¶2 discloses the supersession and states the three drafts contained no independent information; the trend IS the paper (Fig 1, Table 1, §3's four enumerated results). The 66→83→93% sequence I named as the unanalyzed content is now the spine, with the crossing quantified.
- **F1(a) proxy transportability — FIXED, and strengthened past my ask.** §5 item 1 states the proxies are z~0.3 calibrations transported unchanged, that the shortfall fractions are *conditional probabilities given the frozen anchors, not the probability a real shortfall exists*, and the Conclusion names proxy transport failure as "the only remaining escape route." This is the honest framing I demanded.
- **F1(b) prior–motivation coupling — FIXED.** §5 item 2 names the structural circularity explicitly (boost motivated by the same JWST abundances whose budget the study examines). §4 adds the direction argument (boost lowers f_req → removing it strengthens the shortfall → the coupling cannot manufacture the result, only mask a larger one). That direction argument is correct: removing the boost raises required f_esc (my ratio check: 1.283 at z=9).
- **F1(c) run the none corner — FIXED.** Full corner sweep executed, not a token check: z_c moves earlier (7.615 vs 8.045), z=9 interval +0.163..+0.854 at 96%, shortfall strengthens everywhere (Table 1 last column). Reported in abstract, §4, §5, Table, and figure. My independent rerun confirms every one of those numbers.
- **F2 (anchors undisclosed/docstring overpromise) — FIXED.** §2.2 lists every frozen constant (SFRD fit, xi_ion 25.5±0.15, C∈[2,5], boost forms, proxy medians 0.08/0.05 with 0.45/0.40 dex scatters, κ_UV, α_B) and states nothing is refetched at run time. A reader can now reproduce every number from the paper alone — I effectively did.
- **F3 (citation gate failures + broken key) — FIXED.** §5 item 3 discloses the 3/3, 2/2, 1/1 gate failures; numerical inputs attributed to pipeline constants; literature demoted to framing/formalism; the [Muoz2024] mojibake is gone — reference list key [Munoz2024] matches in-text usage in all 4 occurrences. xi_ion attribution hedged exactly as required ("representative anchor… not a number extracted verbatim").
- **F4 (boilerplate caveats) — FIXED.** The old "automated, single-selection, uncalibrated measurements" sentences are gone; §5 item 4 states what the study is ("contains no measurements") and names unpropagated systematics (He II, κ_UV IMF dependence, SFRD faint-end truncation).
- **F5 + z=8 "least honest sentence" + z=10 gate note — FIXED.** §3 item 3 states the z=8 asymmetry verbatim in my demanded form (interval spans zero only at the edge; 83% of mass in deficit; "closes only at the 1σ boundary"). §3 item 4 includes z=10 with the expected-value-gate shelving disclosed and the correct re-frame (smooth trend continuation, boundary case). The retired "dex-frac" unit is gone — Δ is defined as a linear f_esc difference.
- **z=6.5 non-robust flag (new in the grid)** — handled honestly (Table footnote: both arms ±0.02 of zero adjacent to the median crossing; expected near a sign change, disclosed not hidden).

## REQUIRED REVISIONS (why MINOR, not ACCEPT)

**R1 (accuracy of one clause, abstract).** The abstract says the crossing is "at a closure-crossing redshift z_c=8.05 (bootstrap 16–84%: 8.03–8.06)" — correct — but the TITLE says the shortfall "becomes robust to the stated systematics only at z ≳ 8" while §3 item 2 and the figure anchor z_c=8.05, i.e. the interval detaches from zero only ABOVE z=8. At z=8.0 exactly the manuscript's own Table shows the interval still touching zero (−0.003). "z ≳ 8" is defensible as ≈8.05-rounded, but a referee will note the title's ≳8 includes 8.0 where the claim is false by the paper's own criterion. Suggest: "…robust to the stated systematics only above z ≈ 8" or "…at z ≳ 8.05". One word.

**R2 (conditional-probability framing leaks in one spot).** §3 item 2 says "By construction the shortfall fraction at z_c is 84%" — true and a nice check (it is, 0.839975) — but the sentence risks being read as a definitional tautology rather than an empirical coincidence of the construction; one clause ("i.e., the 16th percentile touches zero") would pin it. Trivial.

**R3 (z=9 headline provenance sentence).** §3's closing paragraph says the superseded drafts' z=9 headline "survives intact as one row of this trend" — true numerically (verified bit-identical), but the row is a RERUN (ovl726806), not the original run; the changelog is transparent about this, and the manuscript should be too, in half a sentence, because "survives intact" could be read as "the same run." The Data availability section almost says this ("the lane computation reproduces all nine run JSONs"); make §3 consistent with it.

**R4 (figure y-axis label typography).** The bottom panel's y-label reads "Δ = f_esc^freq − f_esc^inf" — "freq" (frequency) for "req" (required). Cosmetic, but it's the central quantity of the paper; fix before the panel sees it. (Top-panel inline labels are fine.)

## ATTACKS THAT FAILED (what I tried and could not break)

1. **Number fabrication attack.** Recomputed every grid row against the nine run JSONs (2.2e-16 max deviation — same value they claim, independently obtained). Re-ran the model: fiducial z_c ≈ 8.06 (theirs 8.045, bootstrap includes it), z_m ≈ 6.34 (theirs 6.328), none-corner z_c ≈ 7.61 (theirs 7.615), none-corner z=9 quantiles identical to 3 decimals, shortfall-fraction monotonicity holds (41→97%), median-delta monotonicity holds. z=7/8/9 trend-grid runs bit-identical to the overnight runs I already refereed.
2. **Circularity escape attack.** I tried to construct a reading where the none-corner result still leaves the boost manufacturing the shortfall — it cannot: removing the boost moves every number AGAINST closure. The conservative-direction argument is airtight on the model's own algebra (boost only enters ρ_UV's denominator of f_req).
3. **Modality creep attack.** Hunted for overclaims: "apparent shortfall" hedged in title and conclusion; conditional-probability framing in §5.1; z≥9.5 f_req>1 tail stated as an anchor statement, not a detection; no new measurement claimed anywhere; the old "from public data (jwst)" abstract line explicitly retracted in §2.4. The one soft spot is R1 (title's ≳8) — captured above.
4. **Salami-residue attack.** Checked for per-z padding: the three source drafts appear only as table rows + one provenance paragraph each in the supersession disclosure and §3 items 3–4. No recycled intro/caveat text (the caveats are new). The merge is real.
5. **Figure-text mismatch attack.** Visual inspection: caption claims (dashed z_c, dotted no-boost 16th pctl, shortfall annotations, z-independent inferred label) all present and accurate; values on the figure consistent with Table 1. Only defect: the "freq" typo (R4).
6. **Gate-history laundering attack.** The z=10 shelving disclosure is accurate against the ovl6221703.json I read in the L-C pass (status gated-expected, gate log line matches what §3 item 4 reports). Human-direction history file exists and matches reality (Duho's "go with the merged z-sweep paper" recorded in nm_paper_history format).
7. **Changelog-vs-text attack.** Every "Fix location" claim in MERGE_CHANGELOG.md spot-checked against the .tex — all present where claimed (F1(a)→§2.3+§5.1; F1(c)→§4+Table+Fig; F2→§2.2; F3→§5.3+refs; F4→§5.4; F5→§3.4; z=8→§3.3+abstract).

## WHAT THIS PAPER IS WORTH (referee's summary for the panel)

A bounded, honestly-scoped systematics reconciliation whose contribution is a NUMBER with an uncertainty: the closure-crossing redshift z_c=8.05 (8.03–8.06) under frozen, fully-disclosed literature anchors, with the none-corner showing the shortfall conclusion strengthens under the most crisis-correlated prior's removal. Its limitations are stated in the right places with the right prominence (proxy transportability as the dominant untested systematic, named as the only remaining escape route). It does not overreach. With R1–R4 (all one-line fixes) this clears the publishable bar the nine autopilot papers failed: grounded motivation, non-circular-with-headroom-disclosed result, defensible conclusion, honest uncertainties.

## Evidence ledger

Read in full: `MERGED_FESC_ZSWEEP.tex` (126 lines), `TREND_RESULTS.json` (508 lines), `MERGE_CHANGELOG.md`, `fesc-zsweep-photon-budget_history.json`, figure PNG (visual inspection).
Recomputed independently: (a) grid-vs-run-JSON deviation for all 9 runs → 2.220446049250313e-16 (their claim reproduced, not trusted); (b) trend-grid ovl726802 `fesc` dict == overnight ovl6221700 `fesc` dict (bit-equal); (c) model re-execution from `tools/nm_ionizing_budget.py` (read-only import): dense z-scan crossing z_c ≈ 8.0625, z_m ≈ 6.3375; none-corner crossing ≈ 7.6125; none-corner z=9 delta [+0.163, +0.412, +0.854], frac 0.957; boost ratio 1.283 (vs their 1.288 — MC stream difference, both consistent); fiducial quantiles at z=6/6.5/7 within stream noise; monotonicity checks on both sequences. (d) Table 1 row-by-row vs TREND_RESULTS.json grid_fiducial: all 9 rows' 8 numeric fields match at printed precision. (e) Reference-key scan: [Munoz2024] consistent in-text and in list; no [Muoz remnants.
Constraints held: read-only outside this report; no edits to the draft; all local.

## Uncertainties

- Bootstrap methodology (their resampling scheme) was not re-implemented — I verified the crossing locations independently by direct dense scan; the bootstrap INTERVALS (8.030–8.059 etc.) are plausible given my stream variation but not independently re-derived.
- The claim "percentile sampling error negligible" is supported by my stream comparisons (crossings stable to ±0.02 across fresh streams) — consistent, not exhaustive.
- R3's concern is presentational; the underlying rerun-vs-original equality is verified bit-identical, so no scientific issue.

---

KUN_MERGED_REFEREE_COMPLETE_20260804
