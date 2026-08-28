# V33 WHOLE-DOCUMENT REFEREE REVIEW — CODEX

## Verdict

**NOT CLEAR.** The V32 → V33 draft delta is narrow and correct: §2.7 no longer claims evidence about handedness-conditional independence, describes only the increased consequence of a possible violation, and expressly refuses threshold revision. The complete V33 reread found no new credit assigned to an unfilled gain result and no retreat from the standing execution blocks. The rewritten gain-gradient sidecar is still not freezeable, however: its recovery response remains on raw `χ` amplitude rather than the production accepted-sign estimand; its endpoint-only test is not an invariance test; and its allegedly frozen sampling/fit contract still defers answer-determining choices. Its background-subtraction language also overclaims exact cancellation in a nonlinear instrument. These are design defects that block freezing, not merely the later filling of unmeasured `β`.

## Digest comparisons and custody

### Subject 1 — V33 draft

- supplied SHA-256: `b247f40281df3c23282c5be8b8ca9970ba371c43ad74e4664a19a70c9ff2e6bb`
- independently recomputed SHA-256: `b247f40281df3c23282c5be8b8ca9970ba371c43ad74e4664a19a70c9ff2e6bb`
- comparison: **MATCH — exact 64-hex equality over `../PREREG_SUCCESSOR_DRAFT_V33_20260828.md`**

### Subject 2 — rewritten gain-gradient sidecar

- supplied SHA-256: `4cee2723bf8ce35d59f1f670bc9af11a57e25cc00a76192f04ae412dd97d6630`
- independently recomputed SHA-256: `4cee2723bf8ce35d59f1f670bc9af11a57e25cc00a76192f04ae412dd97d6630`
- comparison: **MATCH — exact 64-hex equality over `GAIN_GRADIENT_CONTROL_DESIGN_20260828.md`**

### Predecessor and delta

- supplied V32 SHA-256: `02a922167bcb77082a72ef0b3da0642975c39c7fef4ebd75ca28fd8d8a708e95`
- independently recomputed V32 SHA-256: `02a922167bcb77082a72ef0b3da0642975c39c7fef4ebd75ca28fd8d8a708e95`
- comparison: **MATCH — exact predecessor byte state reviewed NOT CLEAR in `V32_WHOLE_REVIEW_CODEX.md`**

A direct unified diff and an independent `SequenceMatcher` decomposition found exactly three non-equal regions: the V32→V33 title replacement; replacement of V32 line 390 by the repaired §2.7 paragraph; and insertion of the V31→V32 trace row at V33 line 863. No fourth region moved. V30 lines 131–133 (§1 scope) and V30 line 384 (§2.7 conditional-independence boundary) are byte-identical to V33 at the same line positions.

## Numbered findings

### 1. HIGH / BLOCKING — sidecar lines 91–100, especially 93–99 — the response still is not the response of the production estimand

**Why it fails.** V32 Finding 1 required the injection response to be defined at the same estimand boundary as production, including the complete acceptance/threshold/abstention behavior. The rewrite instead defines

`r(b,i) = χ(b ⊕ i) − χ(b)`, `ĝ = r/A_inj`,

then regresses `ĝ/ḡ − 1`. That remains a response of the continuous network score `χ`, not the response of V33's accepted sign estimator. V33 explicitly keeps instrument confidence and threshold handling at the production boundary (§2.7 lines 365–377 and the post-unblinding attempt states), and §3's estimand is built from accepted sign outputs. A quality-dependent change in score amplitude can move objects across the frozen confidence threshold, change abstention, and change sign accuracy nonlinearly. Subtracting `χ(b)` does not bridge those effects. The sidecar also does not define whether `A_inj` is signed for the two handedness signs, how opposite-sign injections are combined, or the numerator/denominator of a population-level accepted-sign response.

The vector kernel repair is correct but does not cure this mismatch: `K` projects a valid response slope; it cannot convert a score-amplitude response into an accepted-sign response.

**Smallest sufficient repair.** Define each injection cell as a frozen population passed through the complete frozen production instrument and acceptance path. Define the recovered quantity from the accepted sign outputs with exact handling of threshold crossings, abstentions, failed recoveries, both injected signs, denominator, sign convention, and amplitude grid. Then derive or fixture-test the first-order `μ × γ` propagation for that exact estimator. If continuous-score gain is retained, provide a proved and executable bridge through the threshold and abstention boundary.

### 2. HIGH / BLOCKING — sidecar lines 117–129 — testing only `−Γ` and `+Γ` does not establish invariance over the interval

**Why it fails.** The text says the verdict must be invariant across the whole signed interval, but operationally evaluates only `δ ∈ {−Γ,+Γ}` and accepts when the endpoint verdicts are identical. V33's decision regions are not monotone in amplitude: REPRODUCED is a bounded band around `0.0408`, REJECTED is a different low-amplitude region gated by a different p-value condition, and the remainder is INCONCLUSIVE. Equal endpoint labels therefore do not imply the same label inside the interval, nor do they imply equality to the unshifted study verdict.

A direct counterexample using the written V33 geometry is:

- unshifted `A = 0.0408`, `p = 0.0005`, zero floor, and `σ_comb = 0.011` → `REPRODUCED-LONGO`;
- choose `Γ = 0.0400`;
- `A−Γ = 0.0008` → `INCONCLUSIVE`;
- `A+Γ = 0.0808` → `INCONCLUSIVE`.

The endpoints are identical, so the sidecar's test passes, while the central verdict differs. This directly defeats the claimed invariance property. The failure is independent of whether `Γ` was conservatively estimated.

**Smallest sufficient repair.** Require the unshifted verdict and every decision predicate to remain unchanged for all `δ ∈ [−Γ,+Γ]`. Implement this analytically by checking every interval crossing of every decision boundary (p condition held fixed only if that is explicitly justified), or evaluate the complete finite set consisting of both endpoints, zero, and all decision-boundary crossing points. Fixture-test at least the counterexample above and each REPRODUCED/REJECTED/INCONCLUSIVE boundary.

### 3. HIGH / BLOCKING — sidecar lines 85–108 — the answer-determining sampling, weighting, and uncertainty choices are promised for later, not frozen here

**Why it fails.** The rewrite says the sampling contract “is frozen here in full,” but it does not instantiate the three-dimensional cell boundaries, number or identity rule for backgrounds, sample size, allocation algorithm, actual per-cell counts, injection amplitudes, morphology/orientation support, replicate counts, failed-recovery handling, zero-variance cells, or the exact support-refusal predicate. It says allocation counts will be “in the manifest,” but supplies neither a completed manifest nor a frozen deterministic producer/schema that uniquely generates it. A digest added later proves the bytes chosen later; it does not make those choices answer-independent now.

The fit is likewise under-specified. “Inverse recovery variance per cell” does not state whether weights attach to cell means or individual injections, how variances are pooled, or how zero/undefined estimates terminate. “CR2” does not uniquely bind an implementation, leverage adjustment, finite-cluster degrees of freedom, or critical-value rule; nevertheless the decision uses a fixed normal `1.96`. These choices can move both `γ̂` and `σ_γ` and can change the sensitivity verdict. Freezing before cutout fetch is necessary but is not the same as freezing a unique executable contract in this sidecar.

**Smallest sufficient repair.** Before this design is frozen, either attach and hash a completed pre-fetch manifest plus injection schedule, or freeze a deterministic manifest/allocation producer with exact inputs and schema. Instantiate all grid edges, counts, injection values, allocation/tie rules, failed/empty-cell semantics, WLS row unit and weight formula, and a pinned CR2 implementation including degrees of freedom and critical-value convention. Add fixtures in which each refusal and each covariance choice is load-bearing.

### 4. MEDIUM / REPAIR REQUIRED — sidecar lines 93–96 and 163–168 — background subtraction removes an additive baseline, not every first-order background-chirality contribution

**Why it fails.** `χ(b ⊕ i) − χ(b)` cancels the literal additive baseline `χ(b)` exactly. For a nonlinear instrument, however, the first-order injection response is the derivative at the particular background, `Dχ_b[i]`; it can depend on the background's morphology and chirality. Thus the stronger statement that background chirality “cannot contribute to the recovered amplitude at first order” is not established by subtraction alone. Opposite handedness at every grid point helps only after an exact signed pairing/combination estimator is defined; Finding 1 shows that estimator is absent.

This does not make the use of real external backgrounds non-blind with respect to this study: exclusion from the full parent/footprint and pre-recovery manifest freezing are meaningful repairs. It means the cancellation claim must be narrowed and the residual background-conditioned response must be represented in the sampling and clustering design rather than declared absent.

**Smallest sufficient repair.** Replace the claim with “the paired difference removes the background's additive `χ(b)` baseline exactly; recovery remains conditional on the background.” Define the signed opposite-hand pairing and test chirality-conditioned residuals. If exact first-order cancellation is required, prove it for the frozen response estimator or add the residual as an explicitly bounded term.

## V32 findings adjudicated

1. **CODEX-V32-5 (§2.7 overreach): repaired.** V33 line 390 now says the coupling does not test conditional independence because handedness is unread, and distinguishes consequence from likelihood. It ends by saying this motivates the separate preregistered control, not a threshold change. The paragraph no longer reads as evidence for revisiting the frozen cut.
2. **CODEX-V32-2 (incompatible headline observables): repaired as far as observable selection goes.** `γ̂ = β̂ᵀK` is now the sole acceptance statistic; hemisphere and 8-bin outputs are diagnostic only. Finding 3 shows the data/fit contract behind that statistic is not yet unique.
3. **CODEX-V32-3 (false no-flip claim): the false claim is honestly withdrawn, but the replacement endpoint rule fails.** See Finding 2.
4. **CODEX-V32-3 (`μ` definition / ceiling): substantially repaired within the stated first-order finite-sample model.** `μ_obs` is now operationally tied to the accepted population and `max(0.10, |μ_obs|)` is automatic before operator display. The document correctly withdraws the claim that 0.10 is empirically generous. This attack does not independently block freezing; the response-estimator and interval-rule defects do.
5. **CODEX-V32-4 (parent/footprint provenance and overbroad blindness): provenance repaired.** “Non-sample” now means outside both the full 65,060 parent and forbidden footprint, with manifest freeze before recovery. The “no real sky” claim is withdrawn. The narrower paired-subtraction claim needs the repair in Finding 4.
6. **CODEX-V32-1 (production-estimand response): not repaired.** See Finding 1.

## Whole-document attacks that held

1. I reread all 884 lines of V33. The standing status remains explicit: BS-2a DESIGN/UNFILLED; one of fifteen class-P slots filled; BS-2v UNRESOLVED; Rows C2 and E unable to run; Stage P SUPERSEDED/NON-APPLICABLE to the 49,211 mask; BS-6 and the first image byte blocked.
2. V33 does not claim that the sidecar has measured `β`, produced a bound, or closed conditional independence. The sidecar itself opens and closes with DESIGN/UNFILLED status.
3. §1 lines 131–133 remain exactly scoped to Longo's amplitude and fixed axis and continue to exclude A≈0.02, Shamir, BHU, and an isotropy test.
4. §2.7 line 384 remains byte- and position-identical to V30 and expressly says conditional independence is not established.
5. The repaired line 390 raises the consequence of a possible violation, not its probability, and is not stated as grounds to move a frozen threshold.
6. The sole-statistic choice is less gameable than the old undefined hemisphere decision in one important respect: the visible diagnostic bins no longer determine acceptance, and the full vector kernel prevents a univariate seeing slope from absorbing correlated quality axes. The attack fails only because the manifest/fit details underneath the statistic are still not frozen.
7. The two withdrawn claims are withdrawn plainly rather than renamed: no claim that `<0.011` cannot flip a verdict remains, and no claim that real sky is absent remains.

## Kernel reproduction

Required executions from the assigned absolute `gates` directory:

1. `python3 ../ref/gain_gradient_kernel.py` — exit 0.
   - retained N: `49,211`
   - Var(cos θ): `0.751761`
   - `K[flux_ivar_r] = −0.270181`
   - `K[psfsize_r] = +0.483014`
   - `K[nobs_r] = −0.317419`
   - retained correlation `+0.4188`; hemisphere delta `+0.8104σ`
2. `python3 ../ref/gain_gradient_kernel.py --self-test` — exit 0.
   - baseline `+0.483014`
   - reversed axis `−0.483014`
   - unnormalised quality `+0.059666`
   - shuffled pairing `+0.001795`
   - v9 freeze intact; `4 controls, 0 failure(s)`

I independently recomputed all three kernels from authenticated retained evidence and v9 `cos_theta()` without importing `gain_gradient_kernel.py`:

- `flux_ivar_r`: `−0.270181189248` → displayed `−0.270181` — **MATCH**
- `psfsize_r`: `+0.483013647131` → displayed `+0.483014` — **MATCH**
- `nobs_r`: `−0.317418688332` → displayed `−0.317419` — **MATCH**

The kernel arithmetic is sound. The blocking findings concern the response supplied to it, the decision rule after propagation, and the still-open sampling/fit contract.

## Required lint and trace runs

The repository tools live at `/Users/duhokim/NebulaMind/NebulaMind/tools`, so I ran them from the repository root with absolute subject/gate paths:

1. `python3 tools/prereg_lint.py <absolute V33 path> --gates <absolute gates path>` — exit 0: 23 §7 rows, 15 class P, 8 class E, 22 with BS identifiers; no inconsistencies.
2. Same with `--self-test` — exit 0: all six controls fire; `6 controls, 0 failure(s)`.
3. `python3 tools/prereg_trace.py <absolute build dir> --check <absolute V33 path>` — exit 0: `32 computed transition(s); 0 problem(s)`.
4. Same with `--self-test` — exit 0: all three scope controls fire; `3 scope rules, 0 failure(s)`.

Initial literal invocations from `gates` as `tools/...` failed because no `gates/tools` directory exists, and initial `--check V33` invocations failed because this installed checker expects a file path rather than a version token. The corrected absolute-path executions above are the completed required runs. Passing structural tools do not exercise Findings 1–4.

## Testimony / limits

- I did not read `/Users/duhokim/NebulaMindData/`.
- I did not fetch any image, run Stage P/C, execute inference on study data, unblind any result, or modify either subject, any reference code, or any tool.
- I did not independently rerun the Land or lane GZ1 human-label analyses. Their values are not needed for this verdict because the rewrite no longer calls 0.10 an empirical upper bound.
- The assertion that no recovery has been computed and the historical principal authorization remain **Testimony**. The local bytes prove DESIGN/UNFILLED wording, not the absence of off-path work elsewhere.
- This report is the only intended durable write.

## Evidence ledger

Content read: `BRIEF_V33_REVIEW.md`; all 884 lines of V33; the complete V32→V33 diff; `V32_WHOLE_REVIEW_CODEX.md`; all 183 lines of the rewritten sidecar; all 217 lines of `ref/gain_gradient_kernel.py`; the relevant V33 decision implementation at `ref/successor_ref_v9.py` lines 1560–1588.

Independent executions: both required subject SHA-256 comparisons; V32 and V30 hashes; direct V32→V33 diff; independent three-region sequence comparison; V30/V33 same-position byte comparisons; kernel report and self-test; independent three-variable kernel recomputation; endpoint-invariance counterexample; lint, lint self-test, trace check, and trace self-test. Failed path-shape invocations are disclosed above and were corrected rather than treated as test results.

**NOT CLEAR**