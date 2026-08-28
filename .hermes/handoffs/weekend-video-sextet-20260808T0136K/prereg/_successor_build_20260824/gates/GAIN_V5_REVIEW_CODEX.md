# GAIN CONTROL v5 RE-REVIEW — CODEX

## Verdict

**NOT CLEAR.** The estimator-side v4 numerical repairs substantially hold: all four supplied digests match, the estimator self-test exercises all 9 of 9 G-codes with no exemption, G08 is reached by the denormal-covariance control, the scaled-covariance overflow and physical `c_bar` controls refuse, and the near-coincident design refuses instead of crashing. Those repairs close my v4 estimator finding for the exercised surface. They do not close the freeze. The new p-to-A reduction is false for the production one-sided permutation test: its null depends on the observed sign multiset, which a gain gradient can change, and production p is not a function of `|A|`. Separately, my v4 end-to-end recipe refusal defect remains present: `recipe_gamma()` still averages an invalid per-object probability into a valid bin probability and can still raise raw `ValueError`. These are definition/code defects and therefore block **FREEZING**, not merely **FILLING**.

## Digest comparisons

All comparisons were recomputed with `shasum -a 256` on the named absolute paths.

1. `ref/gain_gradient_estimator.py`
   - supplied: `af67230a310d3026378984f234c844dabed9fd38e9f950437572f091d6a15f1f`
   - recomputed: `af67230a310d3026378984f234c844dabed9fd38e9f950437572f091d6a15f1f`
   - comparison: **MATCH**, exact 64-hex equality.

2. `gates/verify_mu_gamma.py`
   - supplied: `d91fb2b2a894a8651c16a0380eeaeb8e56ba9efa62949255b9a2981da7917cbb`
   - recomputed: `d91fb2b2a894a8651c16a0380eeaeb8e56ba9efa62949255b9a2981da7917cbb`
   - comparison: **MATCH**, exact 64-hex equality.

3. `ref/verdict_breakpoints.py` (new)
   - supplied: `8f81eef77ea195f9404530f2b798e15a935b9af64ad58c17da8a07da290e676e`
   - recomputed: `8f81eef77ea195f9404530f2b798e15a935b9af64ad58c17da8a07da290e676e`
   - comparison: **MATCH**, exact 64-hex equality.

4. `gates/GAIN_GRADIENT_CONTROL_DESIGN_20260828.md`
   - supplied: `47b4ce87bc89d919200081ec0c3d9148cc09000aba8464946dccea394ecc45f6`
   - recomputed: `47b4ce87bc89d919200081ec0c3d9148cc09000aba8464946dccea394ecc45f6`
   - comparison: **MATCH**, exact 64-hex equality.

## Delta from CODEX v4

### v4 finding 1 — p-gated verdict completeness: attempted, but not repaired

`verdict_breakpoints.py` adds explicit loci for the two p gates, but it obtains them only after assuming a supplied `p_of_A` is non-increasing in `|A|` (lines 19–28, 38–40, 71–92, 116–132). That assumption does not describe production `perm_record()` and is answer-determining. Detailed attack below.

### v4 finding 2 — estimator refusal surface: repaired for the exercised controls

The current estimator:

- checks `c_bar` against `[-1,1]` as G09 (lines 92–93);
- checks finiteness after `S = 4*cov_a` (lines 101–108);
- conditions the whitened normal matrix (lines 130–146);
- catches failures in the Cholesky/solve block as G08 (lines 134–149);
- gives G08 a real denormal-covariance control and sets `UNREACHABLE = set()` (lines 181–205);
- computes coverage as 9 of 9 codes (lines 290–298).

The unmodified self-test exited 0 and printed `9 of 9 codes exercised by a control`, `[] declared unreachable`, and `self-test: 0 failure(s)`. The denormal control did emit NumPy overflow warnings from the whitened matrix products before returning G08, but no exception escaped.

One literal repair claim is overstated: not every `numpy.linalg` call is inside the `try`. `eigvalsh(S)` at line 113 and both `matrix_rank(X)` calls at lines 126–127 remain outside it. I did not produce a natural finite 3-bin input that makes those particular calls throw after the preceding guards, so I treat this as a contract-wording/code-hardening advisory rather than the freeze blocker.

### v4 finding 3 — verifier end-to-end refusal: not repaired

Parameter finiteness is now checked first in `simulate()` (lines 55–67), and the five published `simulate()` domain controls pass. But the v4 defect was specifically in `recipe_gamma()`, and that function still has no parameter-finiteness or per-object accuracy-domain check before it averages `a_true` by bin and calls `rng.binomial` (lines 93–115).

Using the real retained `c` array:

- `recipe_gamma(c, 0.251, 0.8)` returned `(0.26554805156413064, 0.02548139883001602)` even though the per-object accuracy field exceeds 1, reproducing the silent invalid-field-to-value path from v4.
- `recipe_gamma(c, 0.30, 0.8)` raised raw `ValueError: p < 0, p > 1 or p is NaN`.
- `recipe_gamma(c, nan, 0.8)` raised the same raw `ValueError`.

Thus “verifier parameter finiteness first” is true only of `simulate()`, not of the end-to-end recipe whose universal refusal behavior v4 attacked.

### v4 finding 4 — exact-zero covariance: unchanged and only a filling halt

G03 remains the correct fail-closed behavior for the all-perfect/zero-covariance hand-check realization. It can prevent a value from being filled on that realization, but it does not create post-result freedom and does not itself block freezing.

## Numbered findings

### 1. HIGH / BLOCKS FREEZING — the production p-value is not a function of `|A|`, and its null is not geometry-only

The reduction asserted in `verdict_breakpoints.py:19–28` fails in two independent ways.

**First, the permutation null moves with the observed sign multiset.** Production `successor_ref_v9.py:1138–1155` constructs every null draw by permuting the observed `m.s`. The geometry `m.c` is held fixed, but the null is conditional on the values and multiplicities in `m.s`, not on geometry alone. A gain gradient changes per-object flip probabilities; it can therefore change both the slope and the number of accepted `+1/-1` signs. “The null is a property of sample geometry and is not moved by a gain gradient” is false.

I verified this independently by exact enumeration on one fixed geometry `c=(-3,-2,-1,0,1,2,3)`. Two non-degenerate sign vectors had the same slope `beta=0.214285714286` but different sign sums and different exact one-sided permutation p-values:

- `s=(-1,-1,-1,-1,-1,-1,+1)`, sign sum `-5`: `p=1/7=0.142857142857...`;
- `s=(-1,-1,-1,-1,+1,+1,-1)`, sign sum `-3`: `p=4/21=0.190476190476...`.

With fixed calibration, equal beta means equal A, yet p differs. Therefore no single-valued `p_of_A` exists over the perturbations the gain-gradient argument permits.

**Second, production p is one-sided in signed amplitude, not symmetric in `|A|`.** Production counts `out >= b_obs` at v9:1154. On the same fixed geometry and one fixed non-degenerate sign multiset, reversing the sign pattern gave equal-magnitude slopes but:

- `beta=+0.428571428571...`: `p=0.028571428571...`;
- `beta=-0.428571428571...`: `p=1.0`.

`verdict_breakpoints.py` calls `p_of_A(abs(x))` in both its monotonicity scan and its verdict probes (lines 118 and 152), forcing an even function and erasing this production asymmetry. Its symmetric `±x` p-breakpoints therefore do not represent the production p gate, especially on the negative-A side used by the rejection branch.

**Consequence.** The two p thresholds cannot be converted to complete A-only breakpoints without a stronger state variable or a conservative joint bound over the changed sign vector/null. The v4 T-completeness blocker remains.

**Smallest sufficient repair.** Freeze an executable joint perturbation rule that carries enough state to recompute or conservatively bound production p under every allowed gain-gradient perturbation, including changes to the sign multiset, and derive verdict regions from that rule. An A-only map is acceptable only after a proof that p is uniquely determined by signed A over the allowed perturbation set; current production code supplies a counterexample to that premise.

### 2. HIGH / BLOCKS FREEZING — the new breakpoint artifact is a transcription plus an unfilled callable, not a derivation from the production branch

`verdict_at()` is a hand transcription (lines 61–68). The “production” side of its self-test retypes the same predicates locally at lines 178–183; it never calls `_decide_from()` or otherwise extracts the branch from `successor_ref_v9.py`. T03 is declared but never emitted. The test can therefore pass if both copies share the same omission, and it will not detect later production-branch drift.

More importantly, the answer-determining `p_of_A` callable is not derived or frozen at all. The self-test supplies an invented exponential `_p_step()` (lines 159–168), while production uses a finite empirical permutation distribution conditional on `m.s`. The new artifact thus moves the missing decision content into a filling-time callable rather than closing it pre-result.

The design document is also not reconciled to the new contract: it still says the future receipt will enumerate `T` (design lines 145–157), does not name or pin `verdict_breakpoints.py`, and still documents G08 as unreachable with only G01–G08 (design lines 80–94), contradicting the reviewed estimator's nine-code/no-exemption contract. Because the design says the code is authoritative, these stale sentences do not undo the estimator implementation, but they do prevent the four-file freeze packet from being internally truthful and complete.

### 3. MEDIUM / BLOCKS FREEZING OF THE VERIFIER CONTRACT — `recipe_gamma()` still accepts or crashes on invalid generative fields

The direct outputs above reproduce v4 finding 3 exactly. A test helper that silently turns an invalid per-object probability field into a value cannot support the claimed refusal contract, and a raw NumPy exception is not a named fail-closed result.

**Smallest sufficient repair.** In `recipe_gamma()`, check finiteness of `gamma_true` and `gbar`, then check every `a_true` against `(0.5,1.0]` before bin averaging; return a named refusal shape; add controls for `gamma=0.251`, `gamma=0.30`, and NaN. Do not infer recipe safety from `simulate()` controls, because they are separate functions.

## Official executions

1. `python3 ../ref/gain_gradient_estimator.py --self-test`
   - exit `0`;
   - exact five-fixture gamma recovery held;
   - all named refusal controls held;
   - 9/9 G-codes exercised, no exemption;
   - 0 failures.

2. `python3 verify_mu_gamma.py`
   - exit `0`;
   - 10 in-domain simulation cases held;
   - 5 `simulate()` domain controls held;
   - 3 in-domain recipe cases held;
   - 0 reported failures.
   - This official suite does not contain the failing out-of-domain `recipe_gamma()` probes.

3. `python3 ../ref/verdict_breakpoints.py --self-test`
   - exit `0`;
   - 0 reported failures on the invented exponential `p_of_A` fixtures.
   - The suite does not exercise production `perm_record()`, sign-multiset dependence, or signed one-sided p asymmetry.

## Failed attacks / claims that held

- All four supplied SHA-256 pins matched exactly.
- The prior `diag(1e308)` overflow input now returns G01 after the 4x scaling check.
- `c_bar=[-2,0,2]` now returns G09.
- The formally rank-2 near-coincident-centre fixture returns G05 instead of crashing.
- The denormal covariance reaches and returns G08; the exemption is genuinely withdrawn in estimator code.
- No G-code is left uncovered by the estimator self-test.
- NaN, infinite-domain, and latent-probability controls in `simulate()` refuse.
- All normalisation recovery fixtures and the three in-domain end-to-end recipe fixtures still pass.
- The static amplitude-only equality loci in `verdict_breakpoints.py` correspond to the literal predicates transcribed from v9:1579–1584. The failure is the attempted reduction of production p to `p(|A|)`, not those static loci.

## FREEZING versus FILLING, plainly

Remaining defects **block FREEZING**. The p-gate map is still not defined for the real production perturbation, `p_of_A` remains an answer-determining future input, and the verifier still has an invalid-input-to-value/exception path. Only the absence of measured `gamma_hat`, and a legitimate G03 halt on an exact-zero covariance realization, are **FILLING-only** conditions.

## Evidence ledger and limits

Read in full: the four pinned subjects and `gates/_gain_v4_reports/GAIN_V4_REVIEW_CODEX.md`. Read the relevant production implementations in `ref/successor_ref_v9.py`, including `beta_slope`, `perm_record`, the calibration covariance, and `_decide_from` at lines 1120–1155 and 1446–1588. Ran the three unmodified self-tests/verifiers, the three real-geometry `recipe_gamma()` adversarial probes, and exact small-sample permutation enumerations. I did not read NebulaMindData, fetch images, form a science result, fill `gamma_hat`, or modify any reviewed subject. The only intended durable write is this report.

**NOT CLEAR**