# GAIN CONTROL v3 — you said it measured the wrong thing. It did. Most of it is now gone.

Subjects:

- **`GAIN_GRADIENT_CONTROL_DESIGN_20260828.md`**, sha256
  `25f6772c39f19b061b171c049cc7b88b48562e8988477060ff8ac9fd31e639b5`
- **`verify_mu_gamma.py`**, sha256
  `43e31c262e205e79ee0157056d8c1bba2910d21b3422abc4b41297abf4c13b71`

**Verify both and state the comparisons.** The draft **`../PREREG_SUCCESSOR_DRAFT_V33_20260828.md`**
(`b247f402…`) is **unchanged and not the subject** — you both cleared it last round, and GPT56
marked its remaining findings BLOCKING FREEZE rather than blocking the draft. Confirm V33 is
byte-identical and that nothing here has been credited to it.

## CODEX-V33-1 was right, and it collapsed the design rather than extending it

The statistic is no longer invented. It is **read out of the frozen code.** `inject_signs()` at
v9:1199 is the production model:

    lat = +1  w.p. (1 + A_LONGO·c)/2 ;   s = −lat w.p. (1 − a_b)
    ⇒  E[s] = (2·a_b − 1)·E[lat]

**The production gain is `2a − 1`, the sign-accuracy attenuation.** Your point that `K` could not
convert a score response into an accepted-sign response is accepted in full.

**The consequence you may not expect: the injection campaign is largely unnecessary.**
`calibration_bins()` at v9:1359 places its boundaries at the **count-weighted tertiles of `c`** — the
calibration bins are already positional bins in `cos θ` — and `accuracy_from_handcheck()` at v9:1446
already returns `a_b` per bin **with a full covariance matrix**, off-diagonals included.

**So the gradient is measurable from machinery already frozen in v9 and already required by BS-8f,
with no images, no cutouts and no fetch.** §6's injection campaign is demoted to a secondary check
and **declared not freezeable**, rather than claiming a frozen contract as v2 did.

**Attack that claim first.** If the calibration bins are not what I say, or `Cov(â)` cannot support a
three-point GLS slope, or hand-check accuracy is not the same `a` the estimator consumes, then §3 is
wrong and the rest does not matter.

## The other three findings

- **Endpoint invariance (both seats).** Replaced by an exact rule: the verdict is piecewise-constant
  in `Â`, so it is invariant on an interval **iff no preregistered threshold lies inside it**. No
  sampling. **Is the threshold set `T` complete, and is the receipt's completeness check real?**
- **Contract not frozen in full (both seats).** §3 needs no sampling contract. §6 is declared
  unfreezeable instead of claimed frozen. **Check I have not simply relocated the deferral.**
- **Subtraction overclaim (both seats).** Withdrawn. §6 now uses balanced accuracy
  `p⁺ + p⁻ − 1`, a cancellation in the estimator's own quantity. **Does that actually cancel an
  additive sign bias, or have I repeated v2's mistake in a new place?**

## Two corrections I made against myself — verify both, and look for what I missed

**1. The bias is `γ·(μ + A·κ)`, not `γ·μ`.** `κ = Cov(c²,c)/Var(c) = +0.005104` on the retained
sample, so `A·κ = +0.000208` is an effective monopole present even at `μ = 0`. **`κ` is derived
algebraically and the design says so** — the simulation *cannot* resolve `0.000208` against a
standard error of `≈0.001`, and the naive form passes every case. An earlier draft claimed the
script had falsified the naive form; **it had not, and the claim is withdrawn.** Check the expansion
of `Cov(s,c)/Var(c)` yourselves.

**2. The script's first run failed on a domain violation, not on physics.** `a = (1 + ḡ(1+γc))/2`
exceeded v9's own `(0.5, 1.0]` accuracy rule (v9:1207), numpy clamped the flip probability, and it
reported a false mismatch against the *correct* formula. It now **refuses** out-of-domain parameters
and ships two controls asserting the refusal. **Try to make it clamp again, or find another way to
make it report a false result.**

Run it: `python3 gates/verify_mu_gamma.py` → expect 10 in-domain cases, 2 domain controls,
0 failures. **Do not take that from me.**

## The question I want answered plainly

**Is §3 freezeable now?** Not whether `γ̂` has been measured — it has not, the control is
**DESIGN, defined, UNFILLED**, and nothing may be filled against it. Whether the *statistic, its
uncertainty, its decision rule and its failure consequence* are pinned tightly enough that a later
operator has no room to choose. Say plainly whether any remaining defect blocks **freezing** or only
**filling**.

## Standing state

**BS-2a DESIGN/UNFILLED**, code gate round 5 NOT CLEAR ×2, both findings since repaired, robustness
limit recorded in the module docstring. One of fifteen class-P slots filled. BS-2v UNRESOLVED; rows
C2 and E cannot run; **BS-6 and the first image byte remain blocked.** Non-sample DR10 cutouts remain
authorised for instrument characterisation only — and on this design are no longer needed for §3.

Do not read `/Users/duhokim/NebulaMindData/`. No deadline.

## Verdict

`GAIN_V3_REVIEW_<YOURSEAT>.md`. Numbered findings with severity, file and line, why it fails,
smallest sufficient repair. Anything asserted but not executed under `Testimony`. Final line exactly
`**CLEAR**` or `**NOT CLEAR**`. **Budget your iterations so the report file is written.**
