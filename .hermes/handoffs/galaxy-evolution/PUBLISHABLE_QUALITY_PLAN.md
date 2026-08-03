# How to reach publishable quality — Trio synthesis (2026-07-20 KST)

## The one-line diagnosis (all three agree)
Every frontier draft does the same thing: **measures an offset and describes it**, stopping exactly where
the paper starts — the confrontation. They **caveat** the two make-or-break systematics (JWST emission-line
selection; the metallicity calibration scale) instead of **forward-modelling / reconciling** them, quote bare
point estimates with **no CIs**, and never **quantitatively confront** the published measurements they cite.
The z>7 study (overnight-z7-mzr-20260720, referee MINOR) is the existence proof that the bar is passable on
this exact data — it forward-modelled selection, reconciled calibration with the mass-DEPENDENT KE08 cubic,
mass-matched inside a stated overlap, bootstrapped + LOO, and pre-registered a 7-test scorecard.

## Per-paper verdict
| Draft | Referee | Fate |
|---|---|---|
| mzr-fmr (z=0 MZR + FMR) | REJECT | Anchor + a self-inflicted FMR null (wrong SFR aperture). SHELVE; fold aperture-matched FMR test into A if wanted. |
| highz-scaling (SFMS+MZR evo) | REJECT | MZR half superseded by z7; SFMS +1.94 dex is uncorrected selection. ABSORB into Pick #1/#2. |
| tng-validation (calibration≠validation) | MAJOR | Best framing (two-level differencing) but inherits uncorrected selection + mass mismatch + no CI. → Pick #2. |
| massive-galaxies (SMF stress) | MAJOR→REJECT | z=6 = N=1 Poisson vs 0.3-dex masses already reconciled w/ LCDM. Salvage the native-efficiency result. → Pick #2. |
| z7 MZR deficit | MINOR | Closest by far — the template. → Pick #1. |

## The two highest-leverage papers (mutually reinforcing)
**Pick #1 — Finish z>7 MZR → validated detection.** Add independent samples (Curti+24 via DR, Heintz+23),
an orthogonally-selected (lensed/continuum) subsample, a Te-independent calibration transfer; pre-commit the
rule to lift the "descriptive" cap only if the deficit's sign + CI-excludes-zero survives ≥2 surveys, ≥2
transfers, 1 orthogonal selection. Fastest path to NebulaMind's first bar-clearing paper.
**Pick #2 — ONE unified TNG-vs-JWST star-formation-EFFICIENCY confrontation** (drafts C+D): two-level
differencing (D) + native central efficiency epsilon(M200c,z) as the headline (C) + forward-model the JWST
selection ONTO TNG + TNG300 for volume. Bonus: **produces the z>7 sim comparator Pick #1 is missing.**

## The gate — make future papers clear the bar BY CONSTRUCTION
Pre-register BEFORE any number exists; a claim is a *validated detection* only if all FATAL items pass, else
DESCRIPTIVE (name the failed test in the abstract).

FATAL (any fail => not a paper):
1. One stated, falsifiable, NEW claim (not a z=0 anchor re-derivation).
2. Headline number carries a bootstrap CI that excludes the null (not 16-84 scatter).
3. Dominant systematic FORWARD-MODELLED and bounded, not caveated (emission-line selection => a real MC model).
4. Claim survives its budget: |signal| - sigma_sys > 0 AND CI excludes null AFTER correction. [pre-reg rule]
5. No claim relies on the simulation's own calibration (two-level differencing; sim observable on the DATA scale).
6. All abundances/masses on ONE stated scale first (metallicity Te-anchored; same IMF + aperture; the ~0.24 dex
   Tremonti offset is mass-DEPENDENT — use KE08 cubic, not a flat shift).

REQUIRED: 7 quantitative comparison to >=3 published measurements · 8 motivation cites the live debate (>=3
primary sources) · 9 selection residual reported as a fraction of signal · 10 every number reproducible from a
public query, matches results file · 11 small-N/Poisson/cosmic-variance flagged with actual N · 12 the RIGHT
experiment was run, not a convenient proxy · 13 interpretation bounded by evidence (mechanisms = hypotheses).

HONESTY GUARDRAIL: quantify the limiting systematic IN THE SAME SENTENCE as the claim; "not significant" must be
computed not asserted; a disowned proxy can't support a claim; separate defensible direction from unproven
magnitude; the pre-registered two-sided decision rule is the anti-overclaim device. "Publishable" is reached by
RAISING the evidence, never by LOWERING the disclosure.

## The single institutional fix
The four drafts fail identically; z7 succeeds because it reconciles calibration + forward-models selection +
mass-matches + confronts on a common scale BEFORE it interprets. Make the FATAL gate a pre-write checklist the
pipeline must pass — then papers clear the bar by construction, not by overnight heroics.
