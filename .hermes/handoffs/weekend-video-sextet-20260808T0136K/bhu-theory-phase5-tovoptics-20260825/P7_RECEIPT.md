# P7 receipt — the signed sweep, the null located, and the headline corrected
(2026-08-26. p7_signed_sweep.py, 4/4 checks. Answers REGATE3 finding 1; finding 2 corrected
below.)

## The gate was right, and my check could not have caught it

`p6`'s dipole routine took `abs()` and sampled six w values, so "the dipole survives at every
computed opacity" proved only that six already-absolute samples were positive. A sign change
between samples was invisible to it by construction.

## The null, independently reproduced

Keeping the sign and decomposing the coefficient into its two competing parts reproduces the
gate's table to five digits:

| w | Doppler term | emergent term | signed total |
|---|---|---|---|
| 0.050 | +0.615301 | −0.917418 | **−0.302117** |
| 0.040 | +0.615301 | −0.586979 | +0.028322 |
| 0.030 | +0.615301 | −0.451920 | +0.163381 |
| 0.010 | +0.615301 | +0.613184 | +1.228485 |

(gate: +0.615263 / −0.917407 / −0.302144 — agreement to 5 digits.)

**Root, by root-finding rather than sampling: w = 0.0407786** (gate: 0.0407765).

## The width of the hole — the number the phase actually needed

Defining the exclusion as USELESS when the implied bound exceeds a tenth of the boundary radius
(|c₁| < 0.01358):

**No useful bound exists for w ∈ [0.040728, 0.040816] — a width of 8.9×10⁻⁵ in w**, about 0.22%
of the null's own value and roughly 0.01% of the authorised range. It is razor-thin, but it is
not empty, and inside it an observer could sit arbitrarily off-centre with no dipole signature.

## The corrected headline

**The exclusion holds across the authorised closure range EXCEPT in a narrow neighbourhood
around w = 0.04078, where the Doppler dipole and the epoch-varying exterior cancel exactly and
NO bound exists.**

Outside the null the bound ranges from **one part in 1964 (best) to one part in 21 (worst)** —
the worst values being those adjacent to the null, where cancellation is partial. So the honest
statement is not a single figure at all: **the bound is a function of the closure, degrading
continuously to nothing as w approaches 0.0408.** My earlier "one part in 120" was a sample, not
an envelope, and is withdrawn along with the others.

## Finding 2 — my λ-τ closure was wrong, and I have now read the code

`LAMBDA_TAU_CLOSURE.md` claimed the blind seat held the exterior fixed across directions. **It
does not.** `p6_blind_transfer.py:183-219` builds `tov_profile(w, ETA0−h)`, `tov_profile(w,
ETA0)` and the `+h` counterpart, and evaluates `transfer_temperature` at each — a finite
difference in the crossing epoch, exactly the epoch-varying exterior I claimed was mine alone.
I inferred "fixed exterior" from the flatness of its λ-surface instead of opening the file.
**That is the same failure as asserting a state without reading the artifact, applied to
someone else's work.** The explanation of the residual 20% is therefore WITHDRAWN and the gap is
open again; the flatness needs a different explanation, which I do not yet have.

## Status

- REGATE3 finding 1: **addressed** — signed sweep, root resolved, null width measured, headline
  corrected to an interval statement.
- REGATE3 finding 2: **conceded** — my closure was based on a misreading; withdrawn.
- Not yet blind-doubled. The null is the kind of feature a second implementation should confirm
  or refute before it is quoted.

---

# CORRECTION, 2026-08-27 — REGATE4 required-repair 4

## The result reproduces; the CLAIM ATTACHED TO IT does not survive

REGATE4 re-ran this artifact: "exit 0, 4/4 checks. Reproduced the conditional root w=0.0407786
and its narrow interval. **This reproduces the implementation, not the pinned model**, because
the source closure is inherited." Accepted without argument.

Re-verified today after the p6 ε-repair (p7 execs p6's prefix, so it inherits the change): the
root is **unchanged at w = 0.0407786**, band [0.040728, 0.040816], width 8.883e-05, and the run
is still exit 0, 4/4. The ε-termination did not move the null.

## What is withdrawn

The null's **existence as a property of the model**, and its **location**. Both are
closure-dependent. REGATE4's counterexample is one line: a source held constant across crossing
epochs has zero source-gradient, so the kinematic coefficient stays at **+0.615301** and never
crosses zero. Reproducing a root under two assumed source maps — mine, and the blind seat's
T ∝ ρ̄^[w/(1+w)] carried across distinct crossing events — proves robustness *within those two
maps*, not existence over the unrestricted set of positive source fields.

I built the phase headline on agreement between two closures. Two wrong closures agreeing is not
evidence about the thing they are both approximating.

**Permitted:** "the two tested closures each contain a cancellation, at different locations."
**Not permitted:** "the pinned model contains a silent configuration whose location alone is
unknown."

## What stands

The **method** finding is untouched and is the durable part of P7: p6's `dipole_and_bound()`
took `abs()` and sampled six w values, so `min(c1)>0` proved only that six absolute samples were
positive. Keeping the sign and root-finding every crossing is what exposed the cancellation.
A check that agrees with itself finds nothing — that lesson survives the withdrawal of the
result it produced.

## Standing conditionality

The script now carries a header banner and prints an explicit CONDITIONALITY block after its
headline, so the run itself states the limit rather than relying on a reader having found this
receipt. See `BHU_CLOSED_ROUTES.md` and `REGATE4_DISPOSITION.md`.

**Run record.** `python3 p7_signed_sweep.py` → exit 0, **4/4 checks**.
