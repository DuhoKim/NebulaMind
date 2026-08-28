# REFEREE BRIEF — V32. Your V31 blocker was answered by refutation, not by weakening. Test that.

Subject: **`../PREREG_SUCCESSOR_DRAFT_V32_20260828.md`**, sha256
`02a922167bcb77082a72ef0b3da0642975c39c7fef4ebd75ca28fd8d8a708e95`. **Verify and state the comparison.**

Predecessor: **V31**, `ce1b6914eae0d36b38d5fc77bb0a8d17c3502d4a007611ad39efe7fe78f1349c` — **NOT CLEAR
from both of you.** Your reports: `gates/V31_WHOLE_REVIEW_{GPT56,CODEX}.md`.

`diff` V31 → V32: the retitle, §1 line 120 replaced, a new §2.7 paragraph inserted at line 390, and
one §10 row appended. Four regions.

## 1. Your V31 blocker — and why the answer is a refutation, not a retreat

Both of you faulted line 120 for crediting BS-3's `antisymmetry_receipt` with bounding a
position-dependent component it does not measure. **You were right.** The instructed repair was to
stratify that receipt in `cos θ` so it would bound the gradient.

**That is not constructible, and this is the load-bearing claim of the whole revision.** From
`paper/PAPER_DRAFT_SPIN_INSTRUMENT_20260812.md` §2.1: `mirror(·)` is pure index reversal
(`np.fliplr`, no resampling) and `χ(x) = (w(x) − w(mirror(x)))/2`. So `χ(mirror(x)) = −χ(x)`
**algebraically, for any weights and any raster** — both sides reduce to the same two floating-point
values. §2 records `max|χ(mirror(x)) + χ(x)| = 0.0` exactly, 1000/1000 spirals.

Therefore `d(g) = χ(g) + χ(Mg) ≡ 0`, and **stratifying it returns 0.0 in every bin at every sample
size.** It is an identity, not a measurement.

**Attack that argument.** If it is wrong, V32's §1 is wrong and so is the design in finding 2 below.
Check the algebra, check that the deployed mirror really is non-interpolating, check whether any
real pipeline step could make `d ≠ 0` (§3.1 says an *interpolating* mirror breaks the identity by
0.058–0.944 — is that reachable here?).

Line 120 now says the Galaxy Zoo figure motivates the **architecture** rather than a calibration of
it, that the parity-even response is zero by construction, that the receipt verifies the identity
and **does not** measure sky-position dependence, and that the surviving §2.3 threats are bounded by
an explicit control that is **DESIGN, UNFILLED**. **Does it now under-claim?** If the paragraph no
longer motivates BS-3 at all, that is a finding too.

## 2. `gates/GAIN_GRADIENT_CONTROL_DESIGN_20260828.md` has never been refereed. It should be.

It is not an annex. It corrects `MIRROR_TEST_DESIGN_20260828.md` Q2, and it freezes:

- a **statistic** — recovered gain from synthetic injection into non-sample cutouts;
- a **binning** — two-hemisphere headline, deliberately non-tunable, with the 8 equal-count bins
  reported for shape only so bin choice cannot be revisited to change a verdict;
- an **acceptance rule** — `|μ|max · (|β̂| + 1.96·σ_β) · K ≤ 0.011`, the right side being **Longo's
  own published 1σ**, an external anchor;
- a **blindness claim** stronger than the mirror test's: the real sky is absent, not merely
  parity-protected.

Specific things to break:

- **`|μ|max = 0.10` is an assumption, not a measurement.** The design says so. **Is 0.10 defensible
  or merely convenient?** It is claimed to exceed Land's normalised asymmetry (~0.07) and this
  lane's own GZ1 flip-imbalance statistic (~0.095). Check both.
- **`K = +0.483014` and `Var(cos θ) = 0.751761`** are computed from catalogue metadata and the
  frozen `AXIS` at `successor_ref_v9.py:100`. **Recompute both yourselves** —
  `python3 ref/gain_gradient_kernel.py` and `--self-test` — they need no images, so they are
  checkable rather than assertable. Its null control shuffles the quality–position pairing and must
  collapse `K` to ~0.
- **`β` is unmeasured.** The control is DESIGN, defined, UNFILLED. **Check that neither the design
  nor V32 credits it with a bound it has not produced** — that is the exact over-credit shape you
  both caught at line 120, one layer out.
- The design claims it bounds §2.3 route (b) **only**, not (a) upstream chirality or (c)
  non-equivariant selection, and **does not close conditional independence**. Verify it does not
  quietly exceed that.

## 3. The new §2.7 paragraph — a finding that cuts against this study's own decision

Measured on the frozen axis: `corr(psfsize_r, cos θ)` = **+0.3659** parent, **+0.4188** retained,
**+0.0964** excluded. **Today's catalogue-quality cut raised the seeing–position coupling in the
sample that will actually be analysed.**

I tried to kill this as a range-restriction artefact of cutting on `psfsize_r` and failed: applying
only the `flux_ivar_r`/`nobs_r` criteria with `psfsize_r` unrestricted already gives **+0.4386** on
53,161, and the population those two remove sits at **+0.0589** on 11,899 with a *wider* `psfsize_r`
spread than the parent. **Re-run that decomposition.**

**The wording must not read as grounds to revisit the cut.** The predicate is frozen; re-choosing
thresholds after measuring the systematic would be the post-hoc selection the freeze exists to
prevent. The paragraph says so explicitly — **check that it says so clearly enough**, and check the
final sentences do not overstate what this implies for conditional independence (the coupling
measured is seeing-to-position; χ is unread).

## Standing state

**BS-2a DESIGN/UNFILLED** — its code gate is at round 5, NOT CLEAR from both seats, on
crash-instead-of-refuse rather than any false accept. **One of fifteen class-P slots filled.** BS-2v
UNRESOLVED; findings 1, 2, 2b, 3 UNRESOLVED; rows C2 and E cannot run; Stage P `SUPERSEDED`; BS-5p
unfillable; **BS-6 and the first image byte remain blocked.** The principal has authorised
**non-sample** DR10 cutouts for instrument characterisation only — that is not a study fetch and
does not unblock BS-6.

§1 scope block and §2.7 line 384 are byte- **and position**-identical to V30. Verify rather than
believe. Run `prereg_lint.py`, its `--self-test`, `prereg_trace.py --check` and its `--self-test`.
**My account of a tool result has been wrong repeatedly and you have caught it every time.**

Do not read `/Users/duhokim/NebulaMindData/`. No deadline.

## Verdict

`V32_WHOLE_REVIEW_<YOURSEAT>.md`. Numbered findings with severity, section and line, why it fails,
smallest sufficient repair. Unverified assertions under `Testimony`. Final line exactly `**CLEAR**`
or `**NOT CLEAR**`. **Judge independently; do not converge.**
