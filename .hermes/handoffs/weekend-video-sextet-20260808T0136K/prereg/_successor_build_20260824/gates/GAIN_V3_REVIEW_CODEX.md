# GAIN CONTROL v3 REVIEW — CODEX

## Verdict

**NOT CLEAR.** The v3 rewrite repairs the finding that killed v2: the statistic is no longer a
response of `χ`, it is `2·â_b − 1` read positionally out of `inject_signs()`, `calibration_bins()`
and `accuracy_from_handcheck()` — machinery already frozen in `successor_ref_v9.py` and already
required by BS-8f. I verified that claim directly against the code and it holds: `calibration_bins()`
really does place its boundaries at count-weighted tertiles of `c`, and `accuracy_from_handcheck()`
really does return the same `a_b` that `inject_signs()`/`w_profile()`/`w_gradient()` consume, with a
full off-diagonal covariance that is load-bearing in `sigma_ours_profile()`. The endpoint-invariance
repair (a piecewise-constant-in-`Â` breakpoint test) is also exact and correctly reasoned given the
actual shape of `_decide_from()`. But §3's own statistic is not yet pinned tightly enough to freeze:
`ĝ_bar`, the divisor in `γ̂ = slope/ĝ_bar`, is left ambiguous between at least three non-equivalent
weighting conventions, and I show numerically that the choice moves `γ̂` by a few percent — small,
but exactly the kind of unpinned, answer-determining choice the design's own standard (line 35:
"attack that claim first") invites attacking. `σ_γ`'s "delta method" is named but not written down.
These are new, narrower defects than the ones that killed v2, and they block **freezing**, not
filling.

## Digest comparisons

- **Subject 1 — `GAIN_GRADIENT_CONTROL_DESIGN_20260828.md`**
  supplied: `25f6772c39f19b061b171c049cc7b88b48562e8988477060ff8ac9fd31e639b5`
  recomputed (`shasum -a 256`): `25f6772c39f19b061b171c049cc7b88b48562e8988477060ff8ac9fd31e639b5`
  comparison: **MATCH — exact 64-hex equality.**

- **Subject 2 — `verify_mu_gamma.py`**
  supplied: `43e31c262e205e79ee0157056d8c1bba2910d21b3422abc4b41297abf4c13b71`
  recomputed (`shasum -a 256`): `43e31c262e205e79ee0157056d8c1bba2910d21b3422abc4b41297abf4c13b71`
  comparison: **MATCH — exact 64-hex equality.**

- **Not the subject — `../PREREG_SUCCESSOR_DRAFT_V33_20260828.md`**
  supplied: `b247f40281df3c23282c5be8b8ca9970ba371c43ad74e4664a19a70c9ff2e6bb`
  recomputed (`shasum -a 256`): `b247f40281df3c23282c5be8b8ca9970ba371c43ad74e4664a19a70c9ff2e6bb`
  comparison: **MATCH — exact 64-hex equality, byte-identical to what I reviewed NOT CLEAR in
  `V33_WHOLE_REVIEW_CODEX.md`.**

**Custody.** `git status --porcelain` on all three paths returns nothing (clean) as of
2026-08-28T12:45:22Z; `git diff --stat HEAD` on all three is empty. All three files are tracked at
the same committed HEAD I already reviewed (`9088e2009880cf991d33694603ee5199a8061c6e`), so the
draft is not merely byte-identical, it is the same committed object — no working-tree edit exists
to credit or discredit. **Nothing in the sidecar or the script edits, references as fillable, or
otherwise touches the V33 draft's bytes; I found no new `nm_` credit, no new BS slot marked filled
in the draft, and no changed line anywhere in `PREREG_SUCCESSOR_DRAFT_V33_20260828.md`.** Confirmed:
the draft is unchanged and nothing has been credited to it by this round.

## The central claim (line 35 of the brief) — attacked and held

> "If the calibration bins are not what I say, or `Cov(â)` cannot support a three-point GLS slope, or
> hand-check accuracy is not the same `a` the estimator consumes, then §3 is wrong."

I read `successor_ref_v9.py` directly rather than trusting the sidecar's paraphrase:

- **`calibration_bins()` (v9:1359–1370):** boundaries are `q[floor(n/3)]` and `q[floor(2n/3)]` of the
  *sorted* `c` array — count-weighted tertiles, exactly as claimed. Refuses on any empty bin
  (`sizes.min()==0`). `assign_bins()` (v9:1373–1375) uses `side='left'`, so a boundary tie falls in
  the *higher* bin, matching the docstring. **Holds.**
- **`accuracy_from_handcheck()` (v9:1446–1489):** returns `a_b = (raw_b-eps)/(1-2eps)` per bin *and*
  the full `cov` matrix, with off-diagonal terms `d_eps(b)·d_eps(b')·sigma_eps²` from the shared
  synthetic-error term — not a diagonal, not an additive constant. **Holds.**
- **Same `a` the estimator consumes:** `inject_signs()` (v9:1199–1215) is the production model, and
  its docstring/body use exactly `a_obj = av[m.bin]` sourced from a `(N_CAL_BINS,)`-shaped accuracy
  array — the same shape `accuracy_from_handcheck()`'s `a_b` returns. `w_profile()`/`w_gradient()`
  (v9:1506–1530) and `sigma_ours_profile()` (v9:1543–1557) already consume `cal["a_b"]` and
  `cal["cov_a"]` **with the off-diagonal terms mattering** (`quad = Σ_ij g_i C_ij g_j`, not a diagonal
  sum) for the production `PROFILE` decision path. This is the same object graph the sidecar proposes
  reusing. **Holds.**

So the foundational claim — that the machinery to measure the gradient is already frozen and
requires no new images or fetch — is correct. That is real and non-trivial: it repairs
CODEX-V33-1 in full (the recovered quantity is now `2a−1`, computed on the accepted-sign estimator's
own inputs, not on `χ`). The defects below are about the *new* statistic layered on top of that
correct foundation, not about the foundation itself.

## Numbered findings

### 1. MEDIUM–HIGH / BLOCKING FREEZE — sidecar §3, lines 51–57 — `ĝ_bar`'s weighting convention is unpinned and moves `γ̂`

**Why it fails.** §3 writes `ĝ_bar = Σ_b n_b ĝ_b / Σ_b n_b` and `γ̂ = slope / ĝ_bar`, but never states
what `n_b` is. At least three readings are live in the surrounding text and all are "count-weighted"
in some sense:

1. the **population** count per calibration bin (the ~16,400-object tertile populations calibration
   bins are built on);
2. the **hand-check sample** count per bin (the `allocate_handcheck()` cell totals actually used to
   compute `a_b`, which are deliberately *not* population-proportional — floors `HC_MIN_PER_CELL≥10`
   and `HC_MIN_PER_STRATUM≥30` per live stratum, v9:1378–1443, distort the sample away from
   population shares whenever any stratum is thin);
3. the GLS fit's own implied pivot — since `γ̂ = slope/ĝ_bar` divides the fitted slope by a *separate*
   scalar not itself derived from the same inverse-`Cov(ĝ)` weights the GLS slope uses, the intercept
   a 2-parameter weighted fit would return is a fourth, different number again.

I tested this numerically against the real retained sample (N=49,211, calibration tertiles built
with the frozen `calibration_bins()`), with a synthetic accuracy gradient and two allocation
regimes — one exactly population-proportional, one skewed the way `allocate_handcheck()`'s floors
actually skew it:

```
n_hc == population-proportional (167,167,167):
  gbar (population-weighted) = 0.842067   gbar (handcheck-weighted) = 0.842066   GLS intercept = 0.834484
  gamma_hat (pop)  = -0.061253
  gamma_hat (hc)   = -0.061253
  gamma_hat (GLS intercept) = -0.061810     (0.9% relative shift from the count-weighted values)

n_hc == floor-skewed (170,170,160):
  gbar (population-weighted) = 0.844823   gbar (handcheck-weighted) = 0.845833   GLS intercept = 0.837009
  gamma_hat (pop)  = -0.061734
  gamma_hat (hc)   = -0.061661             (0.1% shift between the two count conventions here)
  gamma_hat (GLS intercept) = -0.062311    (0.9% shift from either count convention)
```

The population-vs-handcheck-count difference is small at this illustrative allocation, but it is not
guaranteed to stay small — `allocate_handcheck()`'s floors bind harder exactly when a stratum is
thin, which is a property of the *catalogue*, not of anything frozen by this design, so the size of
this ambiguity is itself unbounded by §3. The GLS-intercept-vs-either-count-convention gap is
consistently the larger of the two and does not shrink with balanced allocation. Either way, this is
precisely a choice "made after the data is visible" in the sense the freeze-discipline standard this
lane applies elsewhere condemns: a later operator has genuine room to pick the convention that puts
`γ̂` on the favorable side of a Γ-band. §4's own text ("Γ = |μ_ceiling|·(|γ̂|+1.96σ_γ)") is a hard
function of exactly this ambiguous number.

**Smallest sufficient repair.** One sentence: state which `n_b` populates `ĝ_bar` — most naturally
the same weights the GLS fit already uses (i.e. define `ĝ_bar` as the GLS fit's own zeroth moment,
not a separately-computed count-weighted mean), and state explicitly whether that's population
counts or hand-check sample counts if a count-weighted mean is intended instead. Add a fixture that
would fail if the wrong one were substituted.

### 2. MEDIUM / BLOCKING FREEZE — sidecar §3, line 57 — `σ_γ`'s "delta method" propagation is named, not written down

**Why it fails.** "`σ_γ = propagated from Cov(ĝ) by the delta method`" names a method but not a
formula. `γ̂` is a ratio of two correlated quantities derived from the same `Cov(ĝ)` (the GLS slope
and `ĝ_bar`), so the delta-method expression needs the **cross term** between them
(`Cov(slope, ĝ_bar)`), not just each one's marginal variance — and that cross term is nonzero
whenever `ĝ_bar` is itself computed from the same `ĝ_b` the slope regresses on (true under every
reading in Finding 1 except pure population-count weighting, which is independent of the fit). A
formula that silently drops the cross term is smaller than reality; the design does not say which
formula it uses.

**Smallest sufficient repair.** Write the exact expression (a 2-vector delta method through
`[slope, ĝ_bar]` with their joint covariance derived from `Cov(ĝ)` via the same linear map used for
the GLS fit), and a fixture with a known non-zero cross-covariance case where dropping the cross
term would visibly change `σ_γ`.

### 3. LOW / ADVISORY — sidecar §4, line 116, and §8 — the "receipt records `T` and its digest" completeness check is not yet code, and `T`'s completeness for the *p-gated* boundaries is unaddressed

**Why it matters, narrowly.** I searched the whole build tree for any implementation token
(`gain_gradient`, `sensitivity_gradient`, `INCONCLUSIVE-BY-SENSITIVITY`, `enumerate_thresholds`) and
found none — the §4 rule is a correct piece of *reasoning* (I independently verified it against the
actual `_decide_from()` code: every boundary in `REPRODUCED-LONGO`/`REJECTED-AT-LONGO-AMPLITUDE`
(`A_LONGO±3σ_comb`, `floor=FLOOR_MULT·sig_floor`, `A_LONGO−3σ_band`) is indeed a fixed value
computable pre-unblinding from mask/cal alone, so the piecewise-constant argument is sound), but
there is no code instantiating `T`, no digest, and no control that "asserts the rule fires when a
threshold is placed inside the interval." That is consistent with §3 being DESIGN/UNFILLED and is
not by itself a defect. What §4 does **not** address: two of the four production breakpoints are
gated by a p-value condition (`p < P_REPRODUCED`, `p > P_REJECT_MIN`) that the Γ-sweep holds fixed
while perturbing only `Â`. A real gain-gradient bias large enough to shift the amplitude estimate by
`Γ` plausibly also perturbs the permutation-test statistic that produces `p`, since both `A` and `p`
come from the same observed sign vector. §4 does not establish that this second-order channel is
negligible, only that the *amplitude*-indexed breakpoints are complete. This is a real, if narrower,
gap in the "T is complete" claim.

**Smallest sufficient repair.** State explicitly that `T`'s enumeration covers amplitude-indexed
breakpoints only, and either bound or explicitly declare out of scope the effect of the same
gain-gradient bias on `p`.

## Two self-corrections, verified against the code

- **`κ = Cov(c²,c)/Var(c)`, `A·κ` as an effective monopole at `μ=0`.** I re-derived
  `E[s|c] = ḡ(1+γc)(μ+Ac)` and expanded `Cov(s,c)/Var(c)` symbolically (`sympy`, exact, no
  truncation): the c² term contributes `A·γ·κ` exactly where `κ` is the third standardized moment
  ratio the script computes. Running the script independently gave
  `κ = +0.005104, A·κ = +0.000208` on the real retained sample — matches the design's stated value
  bit-for-bit. **Holds. Correctly derived, correctly labeled as algebraic (not simulation-verified).**
- **The domain refusal.** `inject_signs()` (v9:1208) requires `a_obj.min() > 0.5` and
  `a_obj.max() <= 1.0`. `verify_mu_gamma.py`'s `simulate()` (line 57) checks the identical bound on
  its own locally-computed `a` before running, and refuses (returns `None, None`) rather than
  clamping. I ran the script's own battery and independently re-derived both `OUT_OF_DOMAIN` cases by
  hand (`(0.05,0.40,0.80)` puts `a` at `c=+1` to `1.06 > 1.0`; `(0.00,0.60,0.80)` similarly). **Holds.**

## Adversarial pass on `verify_mu_gamma.py` — attempts to force a false result

I ran the script unmodified from the assigned `gates` directory:

```
N = 49,211   A_LONGO = 0.0408   Var(cos theta) = 0.751761
kappa = Cov(c^2,c)/Var(c) = +0.005104   A*kappa = +0.000208
... (all 10 in-domain rows OK) ...
domain control — these MUST be refused, not clamped:
  OK   mu=0.05 gamma=0.4 gbar=0.8: refused
  OK   mu=0.0 gamma=0.6 gbar=0.8: refused
10 in-domain cases, 2 domain controls, 0 failure(s)
```
Matches the brief's "expect 10 in-domain cases, 2 domain controls, 0 failures" exactly.

I then imported the module directly (not just running `main()`) and probed the domain guard with
values the design's stated CASES table never tries:

- **Held:** every published `(μ,γ,ḡ)` case reproduced its `exact` formula inside the printed
  tolerance (`4·SE` or `0.002`), for both signs of `μ` and `γ`.
- **Broke, but harmlessly (finding, not a false-result exploit):** the domain guard in `simulate()`
  checks only the *accuracy* array `a = (1+ḡ(1+γc))/2`, never the *latent-signal probability*
  `(1+μ+A·c)/2` used one line later to draw `lat`. Calling `simulate(c, mu=2.0, gamma=0.0, gbar=0.8)`
  runs to completion instead of refusing, even though the implied latent probability at `c=−1` is
  `(1+2.0+0.0408·(−1))/2 ≈ 1.48` — outside `[0,1]`. `numpy.random.default_rng().random() < 1.48` is
  always `True`, so this silently clamps exactly the failure mode the script's own docstring says it
  refuses to allow, just on the other input. **This did not produce a false PASS/FAIL verdict** on
  any of the script's own `CASES`/`OUT_OF_DOMAIN` rows — none of them exercises `μ` anywhere near this
  range (max `|μ|` tested is `0.10`), and production `inject_signs()` hardcodes `μ` structurally at
  `0` (it never accepts a free `μ` argument — the `μ` in this script is a pure simulation input for
  exploring the bias formula, not a production parameter), so this gap cannot corrupt the real
  pipeline. It is a real, disclosed-nowhere gap in the verification tool's own domain completeness
  relative to its stated purpose ("out-of-domain parameters are now REFUSED, not clamped"), scoped
  narrowly to a parameter the tool itself never needs to sweep past ~0.15 in practice. I could not
  turn this into a false **PASS** result inside the script's own CASES/OUT_OF_DOMAIN battery — the
  `main()` entry point that the brief asks to be run reports `0 failure(s)` correctly and I did not
  find an input inside its own table that mismatches. **Failed attack overall; the gap is real but
  does not reach a reportable false result from `main()`.**
- **Held:** reran the whole script with an out-of-tree perturbation of the retained-sample loader
  (confirmed `load_cos_theta()` reads `positions_selected.csv`/`quality_selected.csv` through
  `bs2a_quality_gate.verified_bytes()`, which hashes against `G.PARENT_SHA256` — a tampered source CSV
  would be caught at load time, before `simulate()` ever runs). Did not attempt to actually corrupt
  the CSVs (out of scope: I did not modify any file).

## What remains open (from the design's own §8, verified consistent with the code)

- `γ̂` is unmeasured; nothing here fills it. Confirmed: no run artifact, receipt, or BS slot in the
  build tree names a filled `γ̂`.
- Three tertile points support a slope only, no curvature — true by construction of
  `calibration_bins()` (`N_CAL_BINS = 3`, v9:88).
- §6's injection campaign is explicitly not claimed frozen; its balanced-accuracy cancellation claim
  (`p⁺+p⁻−1`) is now correctly scoped to first order only (I re-derived: for an additive background
  bias `δ` in the classification probability, correct-rate(+injection) ≈ base+δ,
  correct-rate(−injection) ≈ base−δ, so `p⁺+p⁻−1 = 2·base−1`, `δ` cancels **exactly to first order**
  — matching V33 Finding 4's repair, not overclaiming exact nonlinear cancellation). Not
  freeze-relevant since §6 is explicitly deferred.

## Failed-attacks section

- Tried to make `verify_mu_gamma.py`'s own `main()` report a false `OK`/refusal inside its published
  CASES/OUT_OF_DOMAIN table — held, `0 failure(s)` reproduced.
- Tried to break the `calibration_bins()`/tertile claim by reading the function body rather than
  trusting the docstring — held, exact match.
- Tried to break the "`accuracy_from_handcheck()` supplies the same `a` the estimator consumes" claim
  by tracing `inject_signs()`'s and `w_profile()`'s actual argument shapes back to `a_b`'s shape —
  held, identical `(N_CAL_BINS,)` object graph.
- Tried to find hard-coded/mock results or a fabricated `simulate()` return path — held, the function
  genuinely draws random signs per replicate and computes `Cov(s,c)/Var(c)` from them; reran with a
  different seed via direct import and got a different (still-consistent) mean/SE.
- Tried to find an existing implementation of the §4 threshold-set `T` and its completeness control to
  see whether it is already vacuous by construction — found no implementation at all (consistent with
  DESIGN/UNFILLED, reported as Testimony below, not as a defect on its own).
- Tried to move the domain-guard exploit (Finding above) into an actual false PASS on the script's own
  battery — did not succeed; the gap exists but the script's stated CASES never exercise it.

## The question asked plainly: does any remaining defect block freezing, or only filling?

**Blocks freezing**, narrowly. The foundational repair — reading `2a−1` off already-frozen
calibration/accuracy machinery instead of a `χ`-response — is real and closes CODEX-V33-1. But §3's
own new statistic, specifically `ĝ_bar`'s weighting convention (Finding 1) and `σ_γ`'s exact
propagation formula (Finding 2), remain answer-determining choices a later operator could still make
after seeing data, which is exactly what "freezeable" is supposed to rule out. Finding 3 is a smaller,
disclosure-level gap in the invariance test's completeness claim. None of these three findings requires
new images, cutouts, or fetches to repair — they are one or two sentences and a fixture each — and none
of them reopens the estimand question CODEX-V33-1 raised. `γ̂` itself remains correctly unmeasured
(DESIGN/UNFILLED) and nothing here should be read as license to fill it.

## Testimony / limits

- I did not read `/Users/duhokim/NebulaMindData/`.
- I did not fetch any image, execute inference on study data, unblind any result, or modify the two
  subjects, the V33 draft, any reference code, or any tool.
- I did not exhaustively search for a `T`-enumeration implementation outside the paths I searched
  (`gates/`, `ref/`, the build-dir root, and repo-wide content greps for `gain_gradient`,
  `sensitivity_gradient`, `INCONCLUSIVE-BY-SENSITIVITY`); absence there is evidence, not proof of
  global absence.
- The numeric magnitude of Finding 1's ambiguity (≤~1% relative in my illustrative allocation) is
  demonstrative, not a bound — I did not search for a worst-case allocation/gradient combination that
  would maximize the divergence between weighting conventions; the design itself provides no such
  bound either, which is part of the finding.
- This report is the only intended durable write.

## Evidence ledger

Content read: `BRIEF_GAIN_V3_REVIEW.md` (89 lines); `GAIN_GRADIENT_CONTROL_DESIGN_20260828.md` (188
lines); `verify_mu_gamma.py` (119 lines); `successor_ref_v9.py` lines 60–260, 850–1080, 1180–1650
(calibration, mask, injection, decision-rule regions); relevant matched spans of
`PREREG_SUCCESSOR_DRAFT_V33_20260828.md` (§6.1 table rows A–S, §6.3 clauses, §3 uncertainty
paragraph) via targeted grep + line reads; my own prior `V33_WHOLE_REVIEW_CODEX.md`.

Independent executions: `shasum -a 256` on both subjects and the V33 draft; `git status --porcelain`
and `git diff --stat HEAD` on all three paths (clean); `python3 gates/verify_mu_gamma.py` from the
assigned `gates` directory (0 failures, matches brief's expectation exactly); direct module import of
`verify_mu_gamma.py` to call `simulate()`/`load_cos_theta()`/`kappa_of()` outside `main()` with values
outside its published CASES table (domain-guard gap found, documented above); a `sympy` symbolic
re-derivation of `Cov(s,c)/Var(c)`'s c² term confirming the `A·κ` monopole; a from-scratch Python
recomputation of `accuracy_from_handcheck()`/`calibration_bins()` outputs on the real 49,211-row
retained sample under two allocation regimes to quantify Finding 1's `ĝ_bar`-convention sensitivity;
manual re-verification of every breakpoint in `_decide_from()` (v9:1560–1588) against the design's §4
threshold-set claim.

**NOT CLEAR**
