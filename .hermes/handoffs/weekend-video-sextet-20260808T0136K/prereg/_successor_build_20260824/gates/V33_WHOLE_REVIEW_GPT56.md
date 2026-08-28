# V33 WHOLE-DOCUMENT AND GAIN-CONTROL V2 REFEREE REVIEW — GPT56

## Verdict

**NOT CLEAR.** Both dispatched subjects match their supplied SHA-256 pins. The V32→V33 draft delta is exactly the dispatched retitle, §2.7 replacement, and §10 trace row. The replacement at V33 line 390 correctly closes my only draft finding: it says the seeing–position coupling does not test conditional independence, distinguishes the consequence of a violation from its likelihood, and preserves the prohibition on revisiting the frozen cut. I reread all 884 lines; V33 does not credit the unfilled gain control with a produced bound and remains explicit that BS-2a is DESIGN/UNFILLED, BS-2v and Stage P are unresolved, Rows C2/E cannot run, and BS-6 plus the first study image byte remain blocked.

The rewritten sidecar closes the five V32 findings at the level those findings named: one continuous statistic replaces the incompatible observables; the false no-flip claim is withdrawn; the kernel is multivariate and the route claim is narrowed; `μ` is operationalized and `0.10` is no longer called generous; and non-sample provenance plus paired subtraction replace the false “real sky absent” claim. It nevertheless is not yet freezeable. Its claimed whole-interval invariance test evaluates only two endpoints and can accept while the interior changes verdict. Separately, the text says the sampling contract is frozen “in full” while leaving the grid, allocations, gain normalization, variance weights, CR2 implementation, and executable receipt bindings answer-determining at a later manifest/implementation stage. Those are freezing defects, not merely missing measurements. `β` being unmeasured is, separately, a filling blocker only.

## Exact subjects and digest comparisons

I recomputed all three relevant digests from the current bytes:

- V33 supplied: `b247f40281df3c23282c5be8b8ca9970ba371c43ad74e4664a19a70c9ff2e6bb`
- V33 recomputed: `b247f40281df3c23282c5be8b8ca9970ba371c43ad74e4664a19a70c9ff2e6bb`
- V33 comparison: **MATCH**, exact 64-hex equality.
- Rewritten gain-control sidecar supplied: `4cee2723bf8ce35d59f1f670bc9af11a57e25cc00a76192f04ae412dd97d6630`
- Rewritten gain-control sidecar recomputed: `4cee2723bf8ce35d59f1f670bc9af11a57e25cc00a76192f04ae412dd97d6630`
- Sidecar comparison: **MATCH**, exact 64-hex equality.
- V32 predecessor supplied: `02a922167bcb77082a72ef0b3da0642975c39c7fef4ebd75ca28fd8d8a708e95`
- V32 predecessor recomputed: `02a922167bcb77082a72ef0b3da0642975c39c7fef4ebd75ca28fd8d8a708e95`
- V32 comparison: **MATCH**, exact 64-hex equality.

## V32 → V33 delta judgement

The direct unified diff has exactly three semantic regions:

1. line 1 retitles V32 to V33;
2. V32 §2.7 line 390 is replaced by V33 line 390;
3. §10 adds the V31→V32 trace row.

No other byte region changed. The §10 row truthfully records the predecessor transition rather than pretending the sidecar changed the draft bytes.

The §2.7 replacement closes GPT56-V32-6. The old text first admitted that χ was unread and then said conditional independence “no longer rests on nothing.” The new text removes that contradiction. It states that a quality–position correlation says nothing about `selection ⟂ handedness | position`, calls the assumption untested, and limits the inference to a larger projection/consequence if a violation exists. Its final clause says the control is separately preregistered “rather than why the predicate should change,” while the preceding sentences retain the explicit ban on re-choosing thresholds. I find no residual invitation to revisit the frozen cut.

The two mandated V30 stability checks also hold at the required positions:

- V30 §1 scope lines 131–133 and V33 lines 131–133 are byte-identical. Both slices have SHA-256 `51d738df155f2d3a8ecbbc53aeb3ae7fa0f9a2b0957a56535fda34528156d8bc`.
- V30 line 384 and V33 line 384 are byte-identical and remain at line 384. Both line-byte slices have SHA-256 `69cca2922ea7470a8241288050eb6d7b985994099cd43133422f5aee5a296746`.

## Closure audit against my V32 findings

| prior finding | rewritten location | independent judgement |
|---|---|---|
| GPT56-V32-1, incompatible observables and unfrozen sampling | sidecar §§4, lines 82–108 | **Core finding closed.** `γ̂ = β̂ᵀK` is the sole acceptance statistic; hemisphere and 8-bin displays are diagnostic-only. The listed sampling items answer the omissions I named, but Finding 2 below shows they are not yet frozen “in full.” |
| GPT56-V32-2, false no-flip claim and signed propagation | sidecar §5, lines 112–129 | **Withdrawal accepted; replacement defective.** The false claim is expressly withdrawn and absolute values are used. The endpoint-only invariance rule has a new logical hole (Finding 1). |
| GPT56-V32-3, univariate slope overclaim | sidecar §§2–3, lines 34–74 | **Closed.** The fit uses all three authenticated quality variables and the claim is limited to the first-order linear component. Nonlinearity, interactions, other position-coupled properties, and routes (a)/(c) are explicitly left unbounded. |
| GPT56-V32-4, unsupported generous ceiling and non-executable fallback | sidecar §5, lines 131–145 | **Closed as stated.** `μ_obs` is defined on the accepted-sign population; the producer precedes operator display; the deterministic rule is `max(0.10, |μ_obs|)`; and `0.10` is correctly called an assumed working ceiling rather than empirical generosity. |
| GPT56-V32-5, false “real sky absent” blindness | sidecar §§6–7, lines 147–172 | **Core finding closed.** Non-sample excludes the full 65,060 parent and footprint, the manifest precedes recovery, and the unchanged additive background term is subtracted. The stronger first-order wording still overstates what subtraction proves (Finding 3). |

## Numbered findings

### 1. HIGH / BLOCKING FREEZE — sidecar §5 lines 117–129 — two equal endpoints do not establish invariance across the whole signed interval

**Why it fails.** The sidecar first requires the verdict to be invariant “across the whole interval,” then defines its implemented check as evaluations only at `δ ∈ {−Γ,+Γ}`. Equality at the endpoints is not equivalent to constancy on the interval because the preregistered decision function has three regions. In particular, two endpoints can both be `INCONCLUSIVE` while an interior point is `REPRODUCED-LONGO` or `REJECTED-AT-LONGO-AMPLITUDE`.

A concrete counterexample using the draft's own reproduced threshold shape is enough. Hold `p=0.0001`, a powered floor of `0.01`, `Â=0.0408`, `Γ=0.04`, and the minimum published contribution `σ_comb=0.011`. The two endpoints are `0.0008` and `0.0808`; both are outside the `|A−0.0408| ≤ 3·0.011` reproduction band and return `INCONCLUSIVE`, while the interior `A=0.0408` returns `REPRODUCED-LONGO`. The endpoint rule therefore declares invariance precisely where the stated whole-interval condition is false.

There is a second executable ambiguity at the same seam. The frozen helper `_decide_from()` accepts `beta`, `p`, `sigma_beta`, mask and calibration, derives `A`, and makes `sigma_ours` depend on `beta` (reference lines 1561–1588). The sidecar instead says a shift is applied to “the estimated amplitude” without saying whether `beta`, `p`, and the beta-dependent uncertainty are held fixed, transformed, or recomputed. There is no current decision-function input called shifted amplitude. Different choices can change the branch.

**Smallest sufficient repair.** Define one executable sensitivity function over the actual frozen decision inputs. Check every decision boundary/breakpoint that intersects `[-Γ,+Γ]`, plus the endpoints, rather than only the endpoints; or prove and machine-test monotonic/convex membership separately for every verdict class and return `INCONCLUSIVE-BY-SENSITIVITY-GRADIENT` whenever that proof does not apply. State exactly how `δ` maps to `beta`, `p`, `sigma_beta`, `A`, and the beta-dependent uncertainty. Add a fixture with equal inconclusive endpoints and a reproduced interior; it must emit the sensitivity-gradient inconclusive result.

### 2. HIGH / BLOCKING FREEZE — sidecar §4 lines 85–108 and §8 lines 174–183 — the sampling/estimation contract is not frozen “in full” and the receipt cannot authenticate the missing choices

**Why it fails.** The sidecar correctly identifies allocation, weights, covariance, and support as answer-determining, but then defers their numerical and algorithmic definitions:

- “a fixed stratified grid” has no number of cells, boundaries, tie/edge rules, or exact per-cell counts;
- the amplitude × morphology × orientation injection grid has no enumerated values, counts, serialization, or digest binding;
- `ĝ/ḡ − 1` does not define which observations and weights form `ḡ`, or its failure behavior;
- “inverse recovery variance per cell” does not define the cell, variance estimator, finite/zero-variance treatment, or whether the same data determine both weights and response;
- “a CR2 estimator” does not pin an implementation, finite-sample degrees of freedom/critical value, singular-cluster behavior, or the minimum number of backgrounds, while the rule uses a fixed 1.96 multiplier;
- support refusal refers to “quality cells” whose cells and occupancy requirement have not been defined.

The exact receipt list carries `manifest_sha256` and aggregate outputs, but no injection-grid digest, estimator/code digest, design/weight/covariance specification digest, or authenticated failure/coverage details from which a gate can prove that the stated analysis was the one run. `n_injections` is not a binding to which injections they were. Line 182's claim that `SLOT_SCHEMA` is frozen therefore exceeds what lines 106–108 specify.

Freezing a manifest before recovery prevents recovery-driven background substitution, which is an improvement over v1, but it does not freeze these choices now and does not turn them into value-only filling. They can move `β̂`, `Cov(β̂)`, `σ_γ`, and the verdict. The visible hemisphere bins were traded for a continuous statistic, but several invisible freedoms remain.

**Smallest sufficient repair.** Before declaring the design frozen, enumerate or digest-bind the exact quality-cell construction and allocation counts, full injection grid and ordering, `ḡ` normalization, WLS/weight formula and failure rules, CR2 implementation including degrees of freedom/critical value and minimum clusters, support predicate, canonical serialization, and executable producer/verifier bytes. Extend the authenticated receipt to bind all those inputs and implementations and add adversarial fixtures that change each one and are refused. This finding blocks **freezing**. Once repaired and frozen, the still-unmeasured `β` would block only **filling**.

### 3. MEDIUM / NON-BLOCKING WORDING — sidecar §4 lines 93–96 and §7 lines 163–172 — paired subtraction cancels the additive background value, not every first-order contribution of a real background

**Why it fails.** The identity `r(b,i)=χ(b⊕i)−χ(b)` exactly subtracts the unchanged baseline `χ(b)`. That is sufficient to refute the old assertion that no real sky is present, and the use of backgrounds outside the complete parent prevents study-outcome leakage. It does not prove line 168's stronger statement that “a real background galaxy cannot contribute to the recovered amplitude at first order.” For a nonlinear instrument,

`χ(b⊕i)−χ(b) = Dχ_b[i] + O(||i||²)`,

and the first-order derivative `Dχ_b` can depend on the real morphology in `b`. The background's additive chirality cancels; background-dependent blending and response interactions do not. Those interactions may be exactly what a background-based injection control should sample, so acknowledging them does not invalidate the control.

**Smallest sufficient repair.** Say that paired subtraction cancels the additive baseline `χ(b)` exactly while background-dependent interactions remain in the measured incremental response and are averaged under the frozen manifest. Delete “a real background galaxy cannot contribute ... at first order,” unless a separate equivariance/additivity proof or fixture establishes it.

## Kernel recomputation

`python3 ref/gain_gradient_kernel.py` exited 0 and independently recomputed the requested vector:

- `K[flux_ivar_r] = −0.270181`
- `K[psfsize_r] = +0.483014`
- `K[nobs_r] = −0.317419`

It also reported retained `N=49,211`, `Var(cos θ)=0.751761`, pre-cut correlation `+0.3659`, retained correlation `+0.4188`, and hemisphere delta `+0.8104σ` (`n+=20,063`, `n−=29,148`). No vector mismatch was reported.

`python3 ref/gain_gradient_kernel.py --self-test` exited 0:

- baseline `K=+0.483014`;
- reversed axis `K=−0.483014`;
- unnormalised quality `K=+0.059666`;
- shuffled pairing `K=+0.001795`;
- v9 freeze intact;
- 4 controls, 0 failures.

These executions establish the three displayed kernel values and the implemented controls. They do not fill `β` or repair the decision and freeze-contract defects above.

## Required lint and trace executions

All four required invocations were rerun against the digest-matched V33 bytes and exited 0:

1. `python3 tools/prereg_lint.py <V33> --gates <gates>`: 23 §7 rows (15 class P, 8 class E), 22 with a BS identifier; no inconsistencies; all six checks demonstrated they can fail.
2. The same command with `--self-test`: all six controls `OK`; 0 failures.
3. `python3 tools/prereg_trace.py <build-root> --check <V33>`: 32 computed transitions; 0 problems.
4. The same command with `--self-test`: in-band removal detection `OK`; V32→V33 sidecar mapping `OK`; synthetic V34 out-of-scope rule `OK`; 3 controls, 0 failures.

My first attempt addressed the tools under `<build-root>/tools`, which does not exist, and exited 2 for each invocation. I located the repository tools at `/Users/duhokim/NebulaMind/NebulaMind/tools/` and reran the exact required operations successfully as reported above. No failed invocation is being represented as a passing check.

## Failed attacks and held boundaries

1. **Subject substitution — failed.** Both in-scope files and V32 match their supplied full SHA-256 pins.
2. **Hidden V33 delta — failed.** The diff contains only the retitle, one §2.7 replacement, and one §10 row.
3. **Residual conditional-independence overclaim in V33 — failed.** V33 now says the assumption is untested and limits the coupling's meaning to consequence, not likelihood.
4. **Frozen-cut reopening — failed.** V33 expressly rejects threshold revision and gives the control—not predicate change—as the consequence.
5. **Scope/position drift — failed.** V30 §1 lines 131–133 and line 384 remain byte- and position-identical in V33.
6. **Control over-credit in V33 — failed.** The whole-document reread found no claim that `β` or a gain bound has been measured; all standing blockers remain disclosed.
7. **Incompatible-observable persistence — failed.** Only `γ̂=β̂ᵀK` enters a threshold; both binned displays are diagnostic.
8. **Univariate-route overclaim — failed.** Three variables enter the vector model, and omitted nonlinear/interacting/other-property routes are named.
9. **No-flip claim persistence — failed.** It is withdrawn outright. Finding 1 attacks the replacement rule, not the withdrawn claim.
10. **“Generous 0.10” persistence — failed.** The point comparisons and their limits are disclosed, and the constant is now labeled an assumption.
11. **49,211-only provenance — failed.** Exclusion is against the full 65,060 parent and forbidden footprint.
12. **Mechanical checker failure — failed.** Kernel, kernel self-test, lint, lint self-test, trace check, and trace self-test all exit 0 on their successful invocations.

## Freeze versus fill ruling

The sidecar is **not yet freezeable** because Findings 1 and 2 leave the decision semantics and answer-determining estimation contract unresolved. Those defects must be repaired before a frozen producer can lawfully fetch or recover control cutouts. Finding 3 is a wording correction and does not by itself block freeze.

After Findings 1 and 2 are repaired, implemented, digest-bound, fixture-gated, and frozen, the absence of measured `β` will remain a **filling** blocker only: the design can be frozen while UNFILLED, but it cannot produce `γ̂`, `Γ`, or an invariance result until the authorized non-parent control is executed. Nothing in this report authorizes that execution or any image fetch.

## Testimony, limits, and evidence ledger

- I did not read `/Users/duhokim/NebulaMindData/`.
- I did not fetch or inspect any image, run the control, measure `β`, execute Stage P, run real-data inference, unblind anything, or modify V33, V32, V30, the sidecar, reference code, lint/trace tools, or data.
- The principal-authorization quotation and historical custody/authorization chronology remain **Testimony**. I verified only the current bytes, code statements, deterministic outputs, and document comparisons described above.
- I read content from `BRIEF_V33_REVIEW.md`; V33 in full; V32 through its direct diff and supplied predecessor/report context; V30's required comparison regions; `V32_WHOLE_REVIEW_GPT56.md`; the rewritten `GAIN_GRADIENT_CONTROL_DESIGN_20260828.md`; `FINDINGS_MAP.md`; `ref/gain_gradient_kernel.py`; and the relevant decision-helper region of `ref/successor_ref_v9.py`.
- Commands/executions: initial absolute `cd`/`pwd`; SHA-256 computation; direct unified V32→V33 diff; byte-slice equality and SHA computations against V30; kernel report and self-test; all four required lint/trace runs; one executable endpoint/interior counterexample; repository tool-location lookup; and read-only `git status --short`.
- The repository was already broadly dirty/untracked before this report write. The only intended write by GPT56 is this report file.

**NOT CLEAR**