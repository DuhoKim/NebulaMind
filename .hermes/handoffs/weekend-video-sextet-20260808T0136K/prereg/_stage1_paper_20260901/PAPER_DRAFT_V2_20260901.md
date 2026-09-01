<!-- ===================================================================
CANONICAL MANUSCRIPT — 2026-09-01. This file is THE paper. Referee it,
repair it, and cite it; do not edit the fragments.
  SUPERSEDES: STAGE1_PAPER_DRAFT_V1.md (pre-repair, REJECTED by
  AGY_FULL_REFEREE_20260901) and the per-seat fragments
  PAPER_SECTIONS_CODEX_/SECTION6_KIMI_/SECTION7_AGY_20260901.md, which were
  the assembly the first referee actually read.
  Carries: Duho's ratified title; the ratified Version A AI disclosure; the
  post-cut leverage figures (Var = 0.7517, N_eq = 110,983) for the analysed
  49,211-object mask, with any pre-cut value labelled as such.
=================================================================== -->

# A Preregistered, Blind-Validated Design for Re-Testing the Longo Spiral-Handedness Dipole — and the Human-Calibration Limit It Reveals

Duho Kim  
Department of Astronomy and Space Science, Chungnam National University

## Abstract

Galaxy-handedness measurements are unusually vulnerable to choices that can reverse a result without making a pipeline visibly fail. We therefore froze the population, geometry, exact-power procedure, antisymmetric instrument, sign convention, gain-gradient counterfactual and custody rules before reading any handedness label. The analysed pre-image sample was the executed post-quality-cut mask of 49,211 objects, with `Var(cos theta) = 0.7517` and equivalent count `N_eq = 110,983`; these are the figures for the sample actually analysed, not its pre-cut precursor. Receipt-backed validation gave 984 successes in 1,000 exact-power trials at the eligible prefix and 996 in 1,000 at final re-pass, above the frozen prose floor of 962. Synthetic-only tests gave 1,000/1,000 antisymmetry identities, 1,000/1,000 mirror involutions and maximum residual 0.0. A fixture-only gain-gradient counterfactual evaluated 5,049 cells with no verdict flip, but it was not the frozen invariance outcome and discharged no frozen edge. The machinery was executed; its failures were caught and recorded, and the pre-image validations completed under their stated scopes passed. Image analysis then halted because the required human calibration could not be supplied: the all-strata floor is 270 real labels, while a minimally overlapping panel requires 1,860 decisions and at least 38 checkers. No handedness label was read and no physics result is reported. The results are a validated pre-image design and a quantified human-calibration limit.

**Keywords:** Data Methods; statistical methods; image-processing validation; galaxy morphology; preregistration

## 1. Introduction

The long-running disagreement over spiral-galaxy handedness is as much a problem of measurement design as of data volume. Longo (2011) reported, in the primary paper's own terms, a dipole asymmetry of `-0.0408 ± 0.011` and a probability of occurring by chance of `7.9 × 10^-4`. Those are Longo's reported figures, not results reproduced or endorsed here. Longo also randomly mirrored images without a visual cue so that a checker's preference would exchange the apparent labels rather than remain aligned with the sky. The convention linking display orientation, winding direction and reported sign was therefore integral to the claim, not incidental metadata.

Land et al. (2008) used Galaxy Zoo classifications and found winding sense consistent with statistical isotropy after correcting classification bias, with no significant dipole. Their mirrored-image experiment identified the relevant mechanism: an excess did not exchange between class weights as an image-origin effect should, implicating a human or interface response preference. Shamir (2012) instead transformed images into radial-intensity plots and classified arm-peak slopes algorithmically; its reported positive result therefore located the consequential classification uncertainty in a different instrument, although one catalogue route inherited human spiral selection. Together these primary studies show why additional objects alone do not resolve the dispute. Selection freedom, checker response and convention mapping can each act on the signed quantity.

Ordinary reproducibility is insufficient for this parameter because a reproduced convention error remains wrong in exactly the same way. A reflection inserted at acquisition, a swapped verbal label, or an inconsistent screen-to-sky mapping can invert the final sign while file hashes, code reruns and aggregate diagnostics all remain internally consistent. Post-hoc selection or calibration choices can likewise change directional leverage after outcomes are visible. The relevant standard is therefore prospective identity: freeze every decidable operation, test sign-changing transformations at the instrument boundary, and make failed gates halt rather than invite reinterpretation.

This paper tests the thesis that a contested handedness claim can be prepared for re-examination without repeating those sources of discretion, and that doing so identifies the actual limiting resource. It reports a preregistered design and instrument, their pre-image validation results, and the costed calibration boundary at which execution stopped. No science image was classified for handedness, no handedness label was read, and no physics claim is made.

## 2. Directional leverage and sample choice

For a dipole-design problem, sensitivity depends on the distribution of objects along the tested axis, not on catalogue size alone. The analytic isotropic all-sky reference is `Var(cos theta) = 1/3`, while the count-weighted full brick universe gave `0.445201`. The frozen planning selection before the later quality cut contained 53,005 objects with `Var(cos theta) = 0.754664` and `N_eq = 120,002.9`. After that cut, the sample actually analysed in this pre-image study contained 49,211 objects with `Var(cos theta) = 0.7517` and receipt value `N_eq = 110,982.5`, conventionally reported as `110,983` (Preregistration lines 274–278 and 487; `acquire/quality_cut_receipt.json`). The pre-cut and post-cut figures describe successive populations; only the latter pair describes this paper's analysed mask.

The selection principle had already rejected a superficially more attractive design. A predecessor contained 208,407 objects but had `Var(cos theta) = 0.0580`, `N_eq = 36,253`, and a projected image volume of 735.9 GB (Preregistration lines 277–278). It was declined before unblinding because its additional objects contributed little leverage along the tested axis. That negative result is evidence for the design thesis: prospective geometry can rule out a larger sample before the temptation to rescue it with outcome-dependent choices arises.

The retained catalogue-quality mask began from 65,060 parent objects and ended with 49,211 objects in 6,104 bricks (`acquire/quality_cut_receipt.json`). A fresh Stage-P planning route represented 6,446 bricks and reported a blocked closure check because it compared that planning set with the post-cut artifact (`run/stagep_plan_20260901.json`). The two counts are not interchangeable. The later cut can empty represented bricks, and the authenticated mask is the object set used for the pre-image results below.

## 3. The preregistration as an instrument

The preregistration was constructed as an author–referee system rather than as narrative intent. Prose defined rules; pinned executables implemented them; receipts recorded outcomes. A ruling that changed execution order was recorded with the provision it superseded rather than silently folded into the frozen text. This matters because a preregistration constrains inference only if later readers can distinguish what was decided in advance from what was learned during execution.

The audit inventory contains 703 findings across 84 referee seat-rounds. Their dispositions are deliberately not compressed into a success count: 177 were repaired under the strict per-finding convention, 192 were mapped by citation, and 334 remain disclosed pre-convention audit debt (`gates/KNOWN_DEBT_APPENDIX.md`). The appendix also preserves its two FORM-echo limitations verbatim. The residue is part of the instrument's uncertainty description. A document that identifies what it could not close is more informative than one that declares completeness.

The frozen package comprised 30 files. Its manifest SHA-256 is `d1be4a3b61975c79f75d6bfafa75e117f69ae86e00dc81ea139a4884f62dc72a`, and the signature uses `ssh-ed25519` in namespace `nmpr-p0` (`P0_PACKAGE_MANIFEST_20260831.txt`; `P0_FREEZE_SIGNATURE_20260831.md`). Cryptography does not certify scientific truth. It establishes which bytes later execution and criticism must address, preventing an apparently harmless edit from changing a rule after labels become available.

## 4. Methods

### 4.1 Population, selection and exact-power planning

The release rule selected Branch B under a disclosed early-resolution ruling while retaining the frozen executable's date-gated behaviour. The quality cut followed selection: the planning population of 53,005 became the executed 49,211-object mask. This ordering reconciles the counts and prevents the pre-cut leverage from being presented as the analysed geometry.

Stage-P tested whether the authenticated design met its prospective power criterion. Each trial was judged against its own 20,000-permutation null; a shared reference null was prohibited by the frozen text (Preregistration lines 302–310). The prose rule required at least 962 successes among 1,000 trials (Preregistration lines 443–447). An initial planner closure check returned `FAIL` because its expected brick set came from a different stage, and the plan was blocked. The closure relation was then examined without reading labels, and eligible checkpoint batteries were executed. Thus the machinery was executed, its failures were caught and recorded, and only the pre-image validations completed under their stated rules are claimed to have passed.

### 4.2 Antisymmetric instrument and sign anchor

Instrument correctness was defined at the transformation boundary: mirroring an input must reverse the signed output, and mirroring twice must return the identical bytes. The test battery used synthetic fixtures only; no real-image path was touched (`run/CODEX_BS6MAP_20260901.md`). A separate synthetic sign anchor required the negative control to be inconclusive and the powered convention fixture to return the stored label `REPRODUCED-LONGO` (`run/classp_candidates/BS-4.json`). That stored label names a convention test; it is not an observational reproduction.

### 4.3 Gain-gradient counterfactual

The robustness machinery is termed the **gain-gradient counterfactual** throughout. Its named **gamma grid** is the parameter grid over which the counterfactual is evaluated, not a separate method. Common random numbers compare each perturbed fixture outcome with its own zero-gradient baseline. The rehearsal used fixture mask and fixture calibration only and therefore could test serialization, mapping and verdict stability without standing in for the frozen real-data invariance result.

### 4.4 Custody and validation gates

Custody separated provisioning, mediation, event enumeration, verification and terminal review. Artifacts advanced only when their identities and transition evidence were derivable from signed or receipted bytes. Two go-live attempts were voided: one encoded a monotonic time value in the wrong unit, and the other bound a public key inconsistent with the escrow-derived key (`run/bs2k/chain/ABORTED_golive_attempt1/WHY.md`; `run/bs2k/chain/ABORTED_golive_attempt2/WHY.md`). Post-hoc verification caught both before downstream consumption. These events are failures of attempted transitions and successes of containment; neither should be erased by saying that every stage passed.

### Methods disclosure

> **Use of AI systems in this work.** This study was executed by a human
> principal directing a set of AI coding agents, and the division of
> responsibility was as follows.
>
> The AI agents drafted preregistration text and sections of this paper;
> implemented, fixtured and verified the pinned software tools; executed the
> gate ladder, the verification passes and the cryptographic custody
> operations; performed the literature and catalogue searches underlying the
> calibration analysis of Section [6]; and acted as adversarial referees of one
> another's work. That adversarial process is recorded rather than summarised:
> the frozen preregistration's known-debt appendix enumerates 703 findings
> raised across 84 referee seat-rounds, with dispositions given as 177 repaired
> under the strict per-finding convention, 192 mapped by citation, and 334
> retained as pre-convention audit debt. Agents also produced the findings that
> stopped work: a dependency cycle in the frozen text, two defective
> instrument-custody transitions voided before any downstream consumption, and
> fixtures that passed for the wrong reason.
>
> The human author made every decision that shaped the science. This includes
> the design rulings recorded in the preregistration history (the gradient
> range, the terminal-signature protocol, the stopping rule, the mapping
> conventions, the operating constants, the release-branch resolution, the
> execution-order supersession, and the decision to halt before image
> analysis); the choice to decline the larger predecessor design before
> unblinding, on the grounds that it lacked axis leverage; the scope and claims
> of this paper; and the Ed25519 signature under which the 30-file
> preregistration package was frozen. Where an agent's proposal conflicted with
> the frozen text, the text governed and the conflict was recorded.
>
> No AI system is an author of this work. Responsibility for its content,
> including its errors, rests with the human author.

## 5. Pre-image validation results

Direct counting of checkpoint records gave 984 successes among 1,000 trials at the first eligible prefix and 996 among 1,000 at final re-pass. Both exceeded the frozen prose floor of 962; because every trial used its own 20,000-permutation null, these outcomes validate the implemented exact-power route within the authenticated pre-image design (`run/stagep_checkpoints/prefix_05024.json`; `run/stagep_checkpoints/final_repass.json`). They are not evidence about galaxy handedness.

On synthetic inputs only, the instrument passed 1,000/1,000 antisymmetry identities and 1,000/1,000 byte-exact mirror involutions, with maximum absolute residual 0.0 (`run/CODEX_BS6MAP_20260901.md`). The synthetic sign-anchor battery also passed, including its named positive convention fixture. Neither result touched a science image or supplies an observational measurement.

On fixture mask and fixture calibration only, the gain-gradient counterfactual evaluated `5,049 = 99 × 51` cells and found zero verdict flips. The receipt states that this was machinery `HELD`, not the frozen `invariance_outcome = HELD`; it filled no slot and discharged no BS-6 edge (`gates/CALIBRATION_ROBUSTNESS_REHEARSAL_RECEIPT_20260831.md`). The caveat is part of the result.

Finally, the custody evidence consists not only of an accepted chain but of two preserved void attempts caught before consumption. Combined with the blocked planner and retained audit debt, these outcomes show that validation was discriminating: completed pre-image checks passed under bounded scopes, while invalid transitions and unresolved edges remained visible.

## 6. The human-calibration limit

The terminal constraint follows from the estimator's need for a real-object human reference. The same checker rule must be evaluated both on accepted-population objects and on blind known-answer synthetics; machine output, repeat consistency or crowd consensus alone cannot replace that calibration. The allocation crosses nine strata with three calibration bins. A minimum of 30 real labels per stratum and 10 per live cell therefore imposes the all-strata floor `9 × max(30, 3 × 10) = 270` real first-presentation labels (`CODEX_LOOSENING_COST_20260901.md`). Reducing that floor removes strata or bins and changes the supported population rather than merely widening an interval.

The single-checker route requires the inherited 850-presentation stream: 500 real first presentations, 200 blind synthetics and 150 mirrored repeats. The 850 are presentations, not independent real calibration objects, and no available checker could complete the role (`CODEX_LOW_HUMAN_OPTIONS_20260901.md`). A three-vote panel at the 270-real floor requires 1,860 decisions and at least 38 checkers when each is capped at 50 decisions. These are optimistic minima excluding training, replacements and dropout (`CODEX_PANEL_DESIGN_20260901.md`). The result is quantitative: preserving the accepted population transforms a seemingly modest real-label floor into a recruitment-scale calibration instrument.

Published labels do not remove that requirement. Modern Galaxy Zoo products reviewed here encode winding tightness rather than winding direction. Galaxy Zoo 1 contains direction votes but does not probability-sample the accepted southern population, supplies no blind known-answer controls for the required checker-error correction, and lacks a pinned mapping from its display-relative sign to this study's celestial convention. The Galaxy Zoo DESI catalogue reviewed contained 8.67 million rows, but those rows are model-predicted morphology vote fractions and not human chirality labels (`CODEX_EXTERNAL_LABELS_20260901.md`).

Nor does a small-budget relaxation preserve the study. The examined breakpoint of 120 total decisions supports at most a prospectively redefined two-stratum calibration-feasibility or restricted upper-limit design; it does not support the original nine-stratum estimand, and budgets below it were judged unable to supply a standalone scientific answer (`CODEX_LOOSENING_COST_20260901.md`). The pre-image halt is therefore not a shortage of catalogue objects or sky leverage. It is the inability to procure verified human calibration at the coverage demanded by the frozen population.

## 7. Discussion

The research result is a separation between technical readiness and inferential readiness. The sample, exact-power route, synthetic antisymmetry instrument and bounded fixture counterfactual have receipt-backed validation. That does not license image analysis because the human reference is part of the measurement instrument, not optional follow-up labour. Treating calibration capacity as an input fixed before population scope would prevent a future design from discovering this mismatch only after its machine components are complete.

Hard preregistration also imposed real costs. The frozen text contained a dependency cycle; an executable and a ruling disagreed about execution order; fixtures sometimes passed for reasons unrelated to the property they purported to test; and two custody transitions were voided. The system did not eliminate silent convention flips in the abstract. It made specified convention changes testable and caused several concrete failures to leave records. Some edges remain undischarged, and the known-debt appendix prevents their conversion into an aggregate claim of completeness.

A successor study should secure the checker capacity before freezing the supported strata and bins, freeze the display-to-sky sign anchor as an executable fixture, and preserve the distinction between planning geometry and the final quality-cut mask. It should also simplify custody where a lighter mechanism provides the same prospective identity. These changes retain the central discipline—no label-dependent redesign—while reducing machinery that does not directly protect the signed estimand.

## 8. Conclusions

This work has two results, neither of them a physics result. First, it provides a validated pre-image design for a future handedness re-test: the actual 49,211-object post-quality-cut mask has documented directional leverage, the exact-power route passed its frozen threshold, and the antisymmetric instrument passed synthetic transformation tests, all with their scopes and failures retained. Second, it quantifies the terminal human-calibration limit: preserving all nine strata requires at least 270 real labels, and the minimally overlapping panel design expands to 1,860 decisions and at least 38 checkers under the stated cap. No handedness label was read. The appropriate conclusion is therefore readiness of specified pre-image components together with a justified halt before image analysis.

## Acknowledgements

The author acknowledges the adversarial review process recorded in the frozen known-debt appendix. No external funding is declared in this manuscript.

## Data availability

The frozen preregistration text, debt inventory, 30-file manifest, signature, pinned reference tools, acquisition receipts, Stage-P checkpoints, instrument receipts, custody records and terminal records are contained in the archived project package described by `P0_PACKAGE_MANIFEST_20260831.txt` and `P0_FREEZE_SIGNATURE_20260831.md`. No science handedness-result table exists because no handedness label was read. A public repository identifier should be inserted before submission.

## Conflict of interest

The author declares no conflict of interest.

## References

Land K. et al., 2008, MNRAS, 388, 1686, *Galaxy Zoo: the large-scale spin statistics of spiral galaxies in the Sloan Digital Sky Survey*, doi:10.1111/j.1365-2966.2008.13490.x

Longo M. J., 2011, Phys. Lett. B, 699, 224, *Detection of a dipole in the handedness of spiral galaxies with redshifts z ~ 0.04*, doi:10.1016/j.physletb.2011.04.008

Shamir L., 2012, Phys. Lett. B, 715, 25, *Handedness asymmetry of spiral galaxies with z < 0.3 shows cosmic parity violation and a dipole axis*, doi:10.1016/j.physletb.2012.07.041

SEAT: CODEX  
VERSION: PAPER-V2  
VERDICT: REPAIRED  
COUNT: 11
