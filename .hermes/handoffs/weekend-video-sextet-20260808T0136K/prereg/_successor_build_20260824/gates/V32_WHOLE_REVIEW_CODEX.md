# V32 WHOLE-DOCUMENT REFEREE REVIEW — CODEX

## Verdict

**NOT CLEAR.** V32 repairs my V31 line-120 blocker: the antisymmetry algebra is correct, the extant inference path uses a non-interpolating tensor index reversal, and the revised paragraph no longer credits BS-3 with measuring sky-position dependence. I reread all 883 lines and found no retreat from the standing execution blocks. The newly refereed gain-gradient sidecar is not yet a freezeable control, however. Its injection statistic does not define the response of the sign-based production estimator; its “hemisphere” decision description conflicts with the beta-based inequality; its sampling, weights, and uncertainty contract leave post-measurement freedom; its 0.10 monopole ceiling is not supported by the two cited human-label quantities and is dimensionally ambiguous as written; and Longo's 0.011 published 1-sigma does not imply that a systematic below 0.011 cannot flip this preregistration's verdict. The blindness/provenance boundary also proves exclusion only from the 49,211 retained mask, not from the 65,060-object study parent or footprint. These defects must be repaired before this sidecar can supply the explicit control V32 correctly leaves DESIGN, UNFILLED.

## Digest and V31 → V32 comparison

Subject: `../PREREG_SUCCESSOR_DRAFT_V32_20260828.md`

- supplied V32 SHA-256: `02a922167bcb77082a72ef0b3da0642975c39c7fef4ebd75ca28fd8d8a708e95`
- independently recomputed V32 SHA-256: `02a922167bcb77082a72ef0b3da0642975c39c7fef4ebd75ca28fd8d8a708e95`
- comparison: **MATCH — exact 64-hex equality over the named V32 bytes**
- supplied V31 SHA-256: `ce1b6914eae0d36b38d5fc77bb0a8d17c3502d4a007611ad39efe7fe78f1349c`
- independently recomputed V31 SHA-256: `ce1b6914eae0d36b38d5fc77bb0a8d17c3502d4a007611ad39efe7fe78f1349c`
- comparison: **MATCH — the predecessor is the exact V31 byte state I reviewed as NOT CLEAR**

A direct unified diff and an independent `SequenceMatcher` decomposition found exactly four non-equal regions: title replacement; replacement of V31 line 120; insertion of the two-line §2.7 paragraph block at V32 lines 389–390; and insertion of the V30→V31 trace row at V32 line 862. No fifth region moved. V30 versus V32 lines 131–133 (the §1 scope block) are byte-identical at the same positions, and V30 versus V32 line 384 is byte-identical at the same position.

Sidecar identities used in this review:

- `GAIN_GRADIENT_CONTROL_DESIGN_20260828.md`: `2c91ee3e302245b7fa2b069aa159be112e5bc2d9e1178bbe6a33d8ab631d3a2c`
- `ref/gain_gradient_kernel.py`: `e8618bb8e2d6979218a95da1c836b42bddde3898c49899e4c4b075ff33b5c2d4`
- frozen `ref/successor_ref_v9.py`: `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148` — matches the kernel's pin

## Numbered findings

### 1. HIGH / BLOCKING — gain-gradient design lines 90–96 and 106–118 — the measured “gain” is not defined as the response of the production estimand

**Why it fails.** The design says to inject “synthetic spirals of known handedness and known amplitude,” recover an amplitude `Â`, define `ĝ = Â/A_inj`, and regress fractional gain on normalized seeing. It never defines whether `A_inj` and `Â` are image-level morphology/score amplitudes or population-level handedness/dipole amplitudes. That distinction is load-bearing. V32's production statistic is a centred slope of accepted sign outputs, with attenuation handled through sign accuracy and acceptance. A change in the magnitude of the network score `χ` does not in general multiply that estimator: it can move objects across `|χ| > τ`, change abstention, and change sign accuracy nonlinearly. Therefore the displayed propagation `A_spurious ≈ |μ|·|β|·K` is not derived from the statistic actually specified unless `g` is explicitly the response of the complete accepted-sign estimator, including thresholding and abstention.

This is not cured by the correct catalogue kernel. `K` only projects a valid quality-response slope onto the axis; it cannot make an undefined or wrong response quantity valid.

**Smallest sufficient repair.** Define the injection ensemble and response at the same estimand boundary as production: fixed synthetic populations with preregistered sign-monopole/dipole perturbations, passed through the complete frozen instrument and `|χ| > τ` acceptance, with recovered accepted-sign response computed by the production estimator. State the exact numerator, denominator, sign convention, amplitude grid, morphology/S/N mixture, and first-order domain; derive or fixture-test the monopole × gain-gradient formula at the acceptance boundary. If score-amplitude gain is retained instead, supply a proved and tested bridge from score gain through threshold/abstention to the sign estimator.

### 2. HIGH / BLOCKING — gain-gradient design lines 98–124 — the frozen-binning claim and the actual acceptance statistic contradict each other, and the design leaves the result-sensitive sampling and uncertainty contract open

**Why it fails.** Lines 98–102 say the headline and acceptance decision read a two-hemisphere contrast, while the only estimator defined at lines 95–96 and used by the acceptance inequality at lines 118–124 is the WLS coefficient `β̂` from gain versus normalized `psfsize_r`. No hemisphere gain contrast, its uncertainty, or conversion to the inequality is defined. The eight equal-count `cos θ` bins are “shape only” and do not resolve that mismatch.

The control is also not frozen enough to make `β̂` unique. “Non-sample DR10 cutout backgrounds spanning the retained sample's range” does not bind the number or identities of backgrounds, their joint distribution in `psfsize_r` and `flux_ivar_r`, injections per background, amplitude/morphology/S/N allocation, WLS weights, repeated-background dependence, empty-bin handling, or whether `σ_β` is model-based, robust, clustered, or bootstrap uncertainty. These choices can materially move both `β̂` and `σ_β` after the cutouts are seen. A one-variable seeing slope can also absorb or cancel effects from the simultaneously varied `flux_ivar_r`; the sidecar prints a flux-ivar kernel but its acceptance rule ignores it.

**Smallest sufficient repair.** Choose one decision statistic. Either (a) make the preregistered WLS coefficient the headline and delete the claim that a hemisphere contrast decides acceptance, or (b) define the exact hemisphere contrast, standard error, and propagation coefficient used by the decision. Before acquisition, freeze an exact non-sample selection manifest or deterministic sampler, sample size and allocation, injection grid, joint quality design, fit covariates, weights, dependence-aware uncertainty, empty/failed recovery handling, and the multi-quality combination rule. Keep eight bins diagnostic only if their edges and population are explicitly instantiated.

### 3. HIGH / BLOCKING — gain-gradient design lines 104–128 and 146–148 — `|μ|max = 0.10` is not justified for the variable in the bound, and the 0.011 acceptance rationale is false

**Why it fails.** The design calls `μ` “the global monopole in χ,” but the cited comparisons are normalized human-label count asymmetries. Literal `χ` is the network score whose accepted magnitude exceeds `τ = 4.4006456017494235`; a 0.10 score ceiling is not made conservative by comparison with sign-count fractions. If the intended `μ` is instead the normalized mean accepted sign, it must be named that way and joined to the production estimand.

Even on that charitable sign-monopole reading, the two anchors do not defend 0.10 as a ceiling for this DESI-Legacy automated sample. Converting a 15% relative excess `(S−Z)/Z` to `(S−Z)/(S+Z)` gives `0.15/2.15 = 0.069767...`, but that remains a human Galaxy-Zoo annotation quantity with a different population and instrument. The lane's `≈0.095 ± 0.024` value is explicitly marked `[VERIFY]`, frame-unstated, and “quotable only as an instrument statistic” in `PAPER_DRAFT_SPIN_INSTRUMENT_20260812.md` lines 89–91 and 289–292; `RECORD_SPIN_PROGRAM_20260812.md` calls that route `DEAD-BUT-INSTRUCTIVE`. Neither establishes an upper bound on this study's realized monopole. The sidecar honestly calls 0.10 an assumption, but “generous” is not earned.

The right-side rationale is independently wrong. `0.011/0.0408 = 0.2696078`: the admitted systematic can be about 27% of the tested amplitude. More fundamentally, a published 1-sigma uncertainty is not a verdict-invariance budget. This preregistration has p-value, sign, amplitude-band, detection-floor, and rejection boundaries; a statistic arbitrarily close to any boundary can be moved across it by a systematic much smaller than 0.011. Thus lines 121–122 cannot claim such a systematic “cannot flip the verdict.” The algebraic equivalent `|β̂| + 1.96σ_β ≤ 0.2277367...` is numerically correct given the assumed constants; the interpretation is not.

**Smallest sufficient repair.** Define `μ` in production units. Either provide a defensible pre-data upper envelope for that same variable, with a sensitivity table extending to the physical maximum, or freeze an automated post-unblinding rule that uses the realized monopole and terminates conservatively without analyst choice. Replace the 0.011 rationale with an explicitly chosen systematic budget and demonstrate by boundary sweeps that the budget preserves the intended decision property; otherwise state honestly that it limits contamination to one published standard error, not that it prevents verdict flips.

### 4. HIGH / BLOCKING — gain-gradient design lines 3–6, 90–92, 130–135 and 155–156 — the “non-sample” proof and blindness claim do not match the authorized boundary

**Why it fails.** The design requires only exact-key exclusion from the 49,211 retained mask. The study parent has 65,060 objects. That check permits any of the 15,849 catalogue-quality exclusions, and it does not prove that a cutout lies outside “this study's footprint,” which line 5 says is unauthorized. It therefore does not prove the cutout is non-sample under the sidecar's own authorization statement.

The claim that “the real sky is simply absent” is also literally too strong. Real DR10 background cutouts, their observing conditions, their sky positions, and catalogue metadata are inputs. What is absent is the study's real per-object `χ` and retained-mask galaxy signal. That is a useful outcome-blindness property, but it is not absence of the real sky. Because cutout selection and real quality structure remain visible, the design must guard against choosing backgrounds or allocations after inspecting recoveries.

**Smallest sufficient repair.** Define “non-sample” against the complete 65,060 parent and the forbidden footprint, then require a pre-fetch manifest and exact-key/spatial proof against those frozen sets. Restate blindness narrowly: no study-parent image and no real study `χ` enters; the statistic is synthetic-signal instrument characterization on preregistered external DR10 backgrounds. Bind background selection before recovery results exist.

### 5. MEDIUM / REPAIR REQUIRED — V32 §2.7 line 390 — the final sentence claims evidence about conditional independence after correctly admitting none was measured

**Why it fails.** The decomposition itself reproduces exactly and the paragraph clearly forbids revisiting the frozen cut. It also correctly says the measured coupling is seeing-to-position and “not evidence of dependence on handedness.” But it then says the conditional-independence assumption “no longer rests on nothing” and calls this evidence “about that predicate that points in any direction.” A correlation between quality and position does not test whether selection is independent of handedness conditional on position. It measures the leverage or consequence of a possible violation, not the conditional dependence itself. The final wording therefore overstates precisely after drawing the right boundary.

**Smallest sufficient repair.** Replace the last two sentences with: “This does not test conditional independence, because handedness remains unread. It shows that any violation of that assumption would project through a stronger seeing–position coupling in the retained mask, increasing the importance of a separately preregistered check or explicit risk statement.” Do not revisit the cut.

## V31 blocker and changed-region adjudication

1. **CODEX-V31-1: repaired in V32.** For `χ(x) = (w(x)−w(Mx))/2` and an involutive pure index reversal `M`, `χ(Mx) = (w(Mx)−w(x))/2 = −χ(x)`. Therefore `d(x)=χ(x)+χ(Mx)=0` algebraically. The paper's source definition at lines 75–82 matches this, and the extant inference runner uses `torch.flip(..., dims=[3])` inside `chi_tensor`, not interpolation. Its separate `mirror_tensor` uses width-axis `torch.flip(..., dims=[2])`. The cutout runner's optional mirror is likewise `np.fliplr` on the final tensor. An interpolating mirror can produce the reported 0.058–0.944 violation, but that operation is not reachable inside the inspected χ implementation. The successor still requires BS-9 input-path rebinding, so this verifies the architecture and extant implementation rather than declaring the future production path filled.
2. **V32 line 120 under-claim attack failed.** The Galaxy-Zoo figure still supplies a defensible motivation for parity-antisymmetric architecture while being denied calibration status. V32 explicitly says the receipt verifies an identity, not sky-position dependence, names all three surviving §2.3 routes, and marks the required explicit control DESIGN, UNFILLED. It does not credit unmeasured `β` with a bound.
3. **V32 §2.7 decomposition: numbers reproduce; inference needs the narrow repair in Finding 5.** Independent recomputation gave parent `(N=65,060, corr=+0.36588135, sd=0.17601798)`, flux-ivar/nobs-only pass `(N=53,161, corr=+0.43861896)`, and removed `(N=11,899, corr=+0.05889925, sd=0.23516696)`, with exact count closure `53,161 + 11,899 = 65,060`. The retained kernel run independently reproduced `corr=+0.4188`, hemisphere delta `+0.8104 sigma`, and retained counts 20,063/29,148. These results defeat the range-restriction attack described in the brief. They do not test handedness-conditional independence.
4. **Trace row: repaired.** The V30→V31 row is present, and the trace checker validates the V31→V32 sidecar mapping without making V32 self-referential.

## Independent kernel reproduction

Both required commands ran from the assigned absolute `gates` directory without reading any image:

1. `python3 ../ref/gain_gradient_kernel.py` — exit 0
   - retained N `49,211`
   - pre-cut correlation `+0.3659`
   - retained correlation `+0.4188`
   - **Var(cos theta) `0.751761` — MATCH**
   - **K(psfsize_r) `+0.483014` — MATCH**
   - hemisphere delta `+0.8104 sigma` (`n+ 20,063`, `n- 29,148`)
2. `python3 ../ref/gain_gradient_kernel.py --self-test` — exit 0
   - baseline `+0.483014`
   - reversed axis `−0.483014`
   - unnormalised quality `+0.059666`
   - shuffled pairing `+0.001795`, which collapses to approximately zero as required
   - v9 freeze intact; `4 controls, 0 failure(s)`

The kernel arithmetic and null control hold. The findings concern what response is propagated and how the control makes a decision, not the computed catalogue geometry.

## Whole-document attacks that held

1. The complete 883-line reread retains BS-2a DESIGN/UNFILLED; one of fifteen class-P slots filled; BS-2v UNRESOLVED; findings 1, 2, 2b and 3 UNRESOLVED; Rows C2 and E unable to run; Stage P SUPERSEDED/NON-APPLICABLE to the 49,211 mask; BS-5p unfillable; and BS-6 plus the first image byte blocked.
2. §1 lines 131–133 still limit the claim to Longo's published amplitude at the fixed published axis and explicitly exclude Shamir, BHU, A≈0.02, and an isotropy test.
3. §2.7 line 384 still states that handedness conditional independence is not established and requires a preregistered check or a stated assumption with risk.
4. V32 does not silently adopt the gain-gradient design. Line 120 says its statistic, sample, stratification, uncertainty, bound, acceptance rule, and failure consequence are not bound by V32 and must be bound before BS-6. That honesty prevents the defective sidecar from becoming a false completed receipt, but it does not make the sidecar itself clear.
5. No β value or completed gain bound appears in either V32 or the sidecar; both label it DESIGN, defined, UNFILLED.

## Required lint and trace runs

All four assigned commands were run from the absolute `gates` directory:

1. `python3 tools/prereg_lint.py V32 --gates .` — exit 0: `23` §7 rows (`15` class P, `8` class E), `22` with BS identifiers; no inconsistencies.
2. Same command with `--self-test` — exit 0: all six controls `OK`; `6 controls, 0 failure(s)`.
3. `python3 tools/prereg_trace.py .. --check V32` — exit 0: `31 computed transition(s); 0 problem(s)`.
4. Same command with `--self-test` — exit 0: all three scope controls `OK`; `3 scope rules, 0 failure(s)`.

Passing these structural tools does not test or cure Findings 1–5.

## Testimony / limits

- I did not read `/Users/duhokim/NebulaMindData/`.
- I did not fetch or authorize any image byte, run Stage P/C, execute inference on real study data, unblind anything, or modify V31, V32, the gain-gradient design, or reference code.
- The historical authorizations, external custody events, survey provenance beyond the authenticated local acquire artifacts, and statements that no study image has ever been fetched remain **Testimony**.
- The Land/McAdam historical quantities were assessed here only for whether they justify `|μ|max`; I did not rerun either published human-label analysis.
- This report is my only intended durable write.

## Evidence ledger

Content read: binding `BRIEF_V32_REVIEW.md`; exact V31 CODEX report; all 883 lines of V32; the complete V31→V32 diff; complete `GAIN_GRADIENT_CONTROL_DESIGN_20260828.md`; complete `ref/gain_gradient_kernel.py`; relevant §2–§3 portions of `paper/PAPER_DRAFT_SPIN_INSTRUMENT_20260812.md`; production-estimator appendix architecture and mirror receipts; mirror-test predecessor design; extant inference runner mirror/χ functions; cutout-runner mirror implementation; GZ1 programme-record lines carrying the 0.095 status.

Independent executions: V31/V32 and sidecar/tool/source SHA-256; four-region diff decomposition; same-position V30/V32 byte checks; gain-kernel report and self-test; independent flux-ivar/nobs decomposition with count closure; conversion of 15% relative excess to normalized asymmetry; 0.011/0.0408 and beta-limit arithmetic; all four required lint/trace commands and self-tests.

**NOT CLEAR**