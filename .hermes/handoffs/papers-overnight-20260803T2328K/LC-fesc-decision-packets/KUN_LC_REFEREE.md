# KUN L-C REFEREE — adversarial passes on the three f_esc REVIEW candidates

Lane: `papers-overnight-20260803T2328K/LC-fesc-decision-packets`
Reviewer: Kun (Kimi K3 via Nous). Date: 2026-08-04 ~00:30-01:10 KST.
Targets: `.hermes/handoffs/galaxy-evolution/lab-runs/overnight-fesc-sweep-20260803T1330Z/` runs ovl6221700 (z=7), ovl6221701 (z=8), ovl6221702 (z=9). Bar: the publishable bar that rejected the nine autopilot papers — grounded motivation, non-circular result, defensible conclusion, honest uncertainties. Constraints honored: read-only outside this lane; drafts untouched; all local; C41/AGN lanes not read.

I independently re-ran the Monte-Carlo from `tools/nm_ionizing_budget.py` (read in full, 193 lines) with the pipeline's own seed and constants, and re-derived the budget physics from first principles. Numbers below are my reproductions, not the drafts'.

---

## THE HEADLINE FINDING (applies to all three, decides the salami question)

**F0 (HIGH) — The three "studies" are one computation evaluated at three z-values, and the ONLY new information in the set is the trend the drafts don't analyze.** Each run re-executes the identical N=40,000 Monte-Carlo with identical inputs (same seed 20260723, same xi_ion/clumping/proxy anchors) differing only in `z0`. My reproduction confirms the outputs are exactly the same model: z=7 delta [−0.072, +0.035, +0.145] / 66.0% shortfall; z=8 [−0.004, +0.130, +0.343] / 83.4%; z=9 [+0.088, +0.303, +0.694] / 92.9% — matching each run's result JSON to within MC stream noise (they used fresh rng streams; distributions identical). The figure in each draft literally plots required-vs-inferred f_esc over z=5–9 — **each draft's own figure contains the other two drafts' entire result**. A referee shown all three would say "salami" within a minute, and would be right. The scientifically interesting content — the shortfall fraction rising 66%→83%→93% across z=7→9 and crossing closure between z=8 and z=9 — is nowhere computed or discussed in any draft; each is frozen at its own z. As three papers: reject twice, merge once. As one z-sweep paper: there is a genuine (if modest) contribution.

## PER-CANDIDATE PASSES

### ovl6221700 (z=7) — verdict: MERGE (weakest of the three standalone)

- Grounded motivation: ADEQUATE. Muñoz+2024 photon-budget crisis + Duncan2015 + Davies2021 anchors; the "is the shortfall robust to systematics" framing is a real question. But the lit-grounding is thin where it matters: the run's own citation-entailment gate reported **3 unsupported of 3 checked** — every citation the gate tested failed entailment (gate is non-blocking; it recorded and moved on). The intro's citations are real papers on the right topic, but the draft cites Muñoz2024 as "[Muoz2024]" in the reference list (mojibake key vs in-text [Muñoz2024] — the reference list key is MISSPELLED, so the link is broken in all three drafts).
- Non-circularity: PASSES the designed test, with headroom I attack below. The pipeline's test — median delta holds sign under O32-only (+0.021) and beta-only (+0.047) — is honestly computed (I reproduced both). But see F1: the test guards calibration choice, not proxy transportability, and the draft's "sign holds under both calibrations" is true of a test whose two arms share the same LzLCS low-z provenance.
- Defensible conclusion: YES, and this is the draft's best feature — at z=7 the 16–84 interval spans zero (−0.072 to +0.145) and the draft says "CLOSES within the systematic," i.e., it reports a null. The title ("shortfall … is not robust to systematics at z~7") matches the numbers. No overclaim in the headline.
- Honest uncertainties: PARTIAL. Caveats section exists but contains a false humility: "automated, single-selection, and uncalibrated measurements" — there ARE no measurements in this study (its own provenance guard says so); the sentence reads like boilerplate from a data study and misleads about what was done. Also absent: the biggest uncertainty of all — that the inferred side is a fixed lognormal around LzLCS medians (O32 0.08±0.45dex, beta 0.05±0.40dex) hard-coded in the tool, not refetched per-run despite the module docstring claiming values are "refetched/cited by the runner's grounding layer" (F2).

### ovl6221701 (z=8) — verdict: MERGE

- Same skeleton; the marginal call. delta 16% = −0.003, kissing zero; 83% shortfall. The draft says "CLOSES within the systematic" — defensible but the least honest sentence of the set: with the lower 16th percentile at −0.003, "closes" is technically inside the interval but the mass is 83% on the shortfall side. A careful referee would demand the asymmetry be stated ("closes only at the 1σ boundary; five-sixths of the systematic space shows a shortfall"). The z=7 draft's null is cleaner than this one.
- Citations: **2 unsupported of 2 checked** (gate). Same broken [Muoz2024] key. Same boilerplate caveat ("does not account for potential systematic errors" — in a study that is ONLY systematic-error propagation; the sentence is self-contradictory boilerplate).
- Numbers independently reproduced (my MC: median delta +0.130, 83.4% shortfall, dO32 +0.112, dβ +0.146 — matches result JSON to 3 decimals).

### ovl6221702 (z=9) — verdict: KEEP (as the spine of the merged paper; not standalone)

- The strongest draft: the only one whose conclusion is a positive claim, and it is honest — delta interval [+0.087, +0.697] excludes zero, 93% shortfall, title says "A residual … shortfall at z~9" (correctly weaker than "the shortfall is real"). At z=9 the claim "CLOSES" would have been indefensible; the pipeline's own `closes` logic (d_med≤0 or interval spans 0) flips the verdict and the title correctly follows. The machine's verdict logic is sound; I checked it against my reproduction.
- BUT the positive claim carries the largest circularity headroom (F1 below), and the draft does not discuss that at z=9 the required f_esc median (0.39, 84% = 0.78) exceeds what any neutral-IGM model permits — the draft says "bounded by systematic, not statistics" but never notes that at this z the answer is driven almost entirely by the SFRD-tail boost assumption (the JWST-tail boost mode contributes up to 1.5× on half the draws; without it, f_req median drops ~12% — my calculation: implied C×boost shift is a uniform 0.88× factor at all three z, i.e. the boost prior moves every number in the same direction). The z=9 shortfall is robust to O32/β swap but NOT stated to be robust to the SFRD-tail choice — and the tool supports a `boost_mode=none` corner that was never run.
- Citations: 1 unsupported of 1 checked. Same broken reference key.

## CROSS-CUTTING FINDINGS (ranked)

**F1 (HIGH) — The non-circularity test guards the calibration CHOICE, not the calibration itself — the headroom the brief asked me to attack.** Both arms (O32, β) are LzLCS low-z (z~0.3) calibrations transported to z>6 with a hard-coded scatter. "Sign holds under both" therefore means "the shortfall is not an artifact of picking one of two siblings," NOT "the inferred side is trustworthy." The genuine circularity risk is one level deeper: the required side uses a JWST-era SFRD-tail boost justified by the same JWST bright-galaxy abundance that motivates the crisis — i.e., the study partially presupposes the high-z abundance excess whose implication (photon budget) it tests. The drafts never name this. It does not make the result circular in the fatal autopilot sense (inputs are published literature values, not the study's own output), but at the publishable bar the merged paper MUST state: (a) proxies are low-z-calibrated, transportability unvalidated at z≳6; (b) the boost prior is motivated by the same observations the budget tests; (c) run the `boost_mode=none` corner and report whether the z=9 shortfall survives.

**F2 (MEDIUM) — Provenance docstring overpromises; anchors are hard-coded.** `nm_ionizing_budget.py`'s header says exact numbers are "refetched/cited by the runner's ADS/arXiv grounding layer." They are not: `_PROXY` medians/scatters, xi_ion=25.5±0.15, C∈[2,5], κ_UV, α_B are constants in the file; the grounding layer only decorates the manuscript text. This is fine for reproducibility (all inputs frozen — I could reproduce every number) but the docstring's claim is false, and the drafts inherit the ambiguity (they say "adopt published values" without giving the actual anchor values for the proxy medians — a reader cannot learn that inferred f_esc=0.062 comes from O32-median 0.08/β-median 0.05 lognormals without reading the tool source).

**F3 (MEDIUM) — Citation integrity failed its own gate in all three runs** (3/3, 2/2, 1/1 unsupported) and shipped anyway. The gate is intentionally non-blocking, but three-for-three runs with zero entailed citations means the intro literature sentences are decoratively anchored. Compounded by the broken `[Muoz2024]` reference key in all three drafts (in-text [Muñoz2024], list [Muoz2024]) — a one-character mojibake that severs every draft's primary citation.

**F4 (LOW-MEDIUM) — Caveat sections are boilerplate from a different study type.** "Automated, single-selection, uncalibrated measurements" (z=7), "does not account for potential systematic errors" (z=8, in a systematics-propagation study). These read as template text, weakening the honest-uncertainty leg of the bar. The z=9 caveat is the best of the three and still generic.

**F5 (LOW) — Determinism/reproducibility is good.** Fixed seed, all constants in-file, figures regenerate, my independent re-derivation of the maintenance formalism (n_crit ∝ C·n_H²·(1+z)³, f_req = n_crit/(xi·ρ_UV)) matches the pipeline's medians to ~12% (fully explained by the boost prior), and my full MC re-execution matches all published quantiles to ≤0.002 in fraction and ≤0.003 in delta. The z=10 sibling run's death at the expected-value gate (f_req 0.68 median, 97% shortfall → gate killed it as CONTRADICTS) is worth noting: the gate's kill was arguably WRONG-headed (a large shortfall at z=10 is the expected extrapolation of this very sequence, not a pipeline error — the gate read the trend as contradiction), but it correctly forced human review, which is its job.

## CROSS-CANDIDATE: ONE PAPER OR THREE? — MERGE_CANDIDATES

Three papers would be salami: identical method/inputs/figure, one new scalar per z. ONE z-sweep paper is the honest unit, and it has a real result none of the three drafts states: **the photon-budget shortfall is systematic-robust at z≳8.5–9 but not at z≲8; the closure boundary sits between z=8 (83% shortfall mass, interval grazing zero) and z=9 (interval excludes zero).** Recommended shape: one draft, required-vs-inferred bands over z=5–9 (the figure already exists), per-z table of the six quantiles + shortfall fractions (all computed tonight), the z=10 point included as the boundary case with its gate history disclosed, the F1 circularity paragraph, and the `boost_mode=none` corner run before anyone calls it a paper. Merit-panel scoring should see the merged draft, not these three.

Disposition summary: ovl6221700 MERGE (its clean null becomes the z=7 row), ovl6221701 MERGE (its boundary case becomes the pivot), ovl6221702 KEEP as the merged paper's spine (its positive-but-bounded conclusion is the headline). None of the three should proceed standalone.

## Evidence ledger

Read in full: all three `draft.tex`; all three result JSONs (`ovl622170{0,1,2}.json` + ovl6221703.json for the gated sibling); `ovl6221700/review_loop.md`; `STATUS.md`; `loop_console.log` (tail); `tools/nm_ionizing_budget.py` (all 193 lines — constants, MC, non-circularity test, closes logic, figure); `tools/lab_runner_worker.py` gate functions (novelty/expected/citations — lines 390–440).
Computed independently: first-principles re-derivation of n_crit and f_req at z=7/8/9 (matches pipeline to ~12%, direction and factor identified as the boost prior); full re-execution of the 40,000-draw MC at all three z with the pipeline's seed/constants (all quantiles within MC noise of the result JSONs); delta_O32/delta_beta reproduction for all three z; SFRD and (1+z)³ trend decomposition; boost-prior sensitivity (uniform 0.88× factor); z=10 extrapolation context from the gated sibling's result JSON.
Not done (per constraints): no network, no edits to drafts, no reads of the C41 or AGN lanes. Literature claims about LzLCS/Muñoz were evaluated as internal-consistency only (I did not refetch the papers; the drafts' own citation gate failing 3/3, 2/2, 1/1 is the internal evidence).

## Uncertainties

- Whether the grounding layer's 6 papers/5 passages per run contained the correct LzLCS anchor values (logs say lit-grounded; the proxy constants are nonetheless hard-coded — the grounding text and the numbers may disagree in detail I cannot see without reading the passages).
- The expected-value gate's kill of z=10: my reading (trend-consistent, wrongly killed) is inference from the gate log line and the z=7→9 trend; the gate's internal similarity evidence was not in the run JSON.
- MC stream equality: runs used fresh rngs; I verified distributional identity, not bit-identity. All comparisons within documented tolerance.

---

KUN_LC_REFEREE_COMPLETE_20260804
