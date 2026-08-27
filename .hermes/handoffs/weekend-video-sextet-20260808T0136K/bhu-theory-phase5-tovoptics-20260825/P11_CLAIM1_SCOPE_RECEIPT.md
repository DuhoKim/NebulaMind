# P11 receipt — Claim 1's admissible-source scope, derived rather than asserted

(2026-08-27. `p11_claim1_boost.py`, **8/8 checks, exit 0**. REGATE4 required-repair 3.)

The gate's instruction was: *"Narrow claim 1 to regular finite-boost sources unless a general
emitter-velocity/source bound is derived."* I took the second branch. The narrowing stands, but
it is now derived and computed rather than conceded, and the threshold is sharp.

## The quantity actually at issue

p6 integrates a transmitted-background term `exp(-tau_tot) * Z_h**4`, where the 4th power is
Liouville (`I_nu/nu^3` invariant, so bolometric intensity carries `g^4`). The gate's objection
was precise: `g = (-k.u_rec)/(-k.u_emit)` depends on the emitter four-velocity, and the receipt
asserted the suppression "for a source that is not comoving" without bounding that dependence.

## 1. The comoving scaling is real, and measured here — not assumed

Fitting `Z ~ (N-1)^p` on the last 400 samples of this lane's own integrated column:

    p = 0.500033        (theory: 1/2)

`N-1` spans 1.000e-09 to 5.5013; `Z` spans 5.576940e-06 to 1.0000. Transmitted weight for a
comoving emitter: **Z_h^4 = 9.673505e-22**.

## 2. What a boost would have to do

Boosting the emitter by Lorentz factor `gam` relative to comoving multiplies the frequency by
at most the head-on Doppler factor `D_max = gam(1+beta) -> 2 gam`. To lift the transmitted
weight to order unity at our horizon offset requires

    D_max ~ 1/Z_h = 1.793098e+05   ->   gam ~ 8.965490e+04

verified exactly: `D_max(8.9655e4) * Z_h = 1.000000`.

## 3. The point that decides it — that requirement DIVERGES

| EPS_HZ | N−1 at end | Z_h | gam required |
|---|---|---|---|
| 1e-05 | 1.000e-05 | 5.576938e-04 | 8.965493e+02 |
| 1e-07 | 1.000e-07 | 5.576939e-05 | 8.965492e+03 |
| 1e-09 | 1.000e-09 | 5.576940e-06 | 8.965490e+04 |
| 1e-10 | 1.000e-10 | 1.763581e-06 | 2.835141e+05 |

The required boost grows **316.2x** as the offset falls five decades. At the true horizon no
*fixed* Lorentz factor suffices — which is exactly why the gate's "finite relative boost" is
the correct qualifier.

## 4. The sharp threshold, tested as a limit

For a boost family `gam = (N-1)^(-p)` the weight goes as `(N-1)^(2-4p)`:

| p | 1e-06 | 1e-12 | 1e-18 | 1e-21 | trend |
|---|---|---|---|---|---|
| 0.00 | 1.000e-12 | 1.000e-24 | 1.000e-36 | 1.000e-42 | → 0 |
| 0.45 | 1.010e+00 | 6.370e-02 | 4.019e-03 | 1.010e-03 | → 0 |
| 0.49 | 9.207e+00 | 5.298e+00 | 3.049e+00 | 2.313e+00 | → 0 |
| **0.50** | 1.600e+01 | 1.600e+01 | 1.600e+01 | 1.600e+01 | **flat** |
| 0.55 | 2.536e+02 | 4.019e+03 | 6.370e+04 | 2.536e+05 | diverges |
| 0.75 | 1.600e+07 | 1.600e+13 | 1.600e+19 | 1.600e+22 | diverges |

The knife edge sits exactly at p = 1/2, where the weight is pinned at 16.

**Threshold:** the suppression survives iff `gam^2 (N-1) -> 0`, i.e. `gam = o((N-1)^(-1/2))`.

## 5. Why the gate's coarser qualifier is the better one to publish

At p = 0.49 the limit is zero but the weight at `N-1 = 1e-9` is still **6.984**, converging as
`(N-1)^0.04`. The sharp threshold is correct and nearly useless near p = 1/2. **Bounded boost
is the qualifier worth stating**, and my sharper condition is a footnote to it, not a
replacement. For scale: a fast astrophysical jet (gam = 30) gives transmitted weight 1.2523e-14;
the most extreme blazar bulk flow (gam = 50) gives 9.6696e-14.

## A defect in my own first version of this test, recorded because it is the lane's recurring one

I first asked *"is the weight below 1e-3 at N−1 = 1e-9?"* and called that a threshold test. It
is not. The claim is about a **limit**, and a magnitude at a single point cannot see a limit —
the check reported FAIL on p = 0.49, a case the theory gets right. Same defect class as
REGATE3's finding: a test built so that it cannot see its own claim. Replaced with a trend test
down a six-decade ladder. (A second, duller bug in the same file: the naive
`sqrt((1+beta)/(1-beta))` divides by zero above gam ~ 1e8 because float64 rounds beta to
exactly 1; rewritten as the algebraically identical `gam(1+beta)`.)

## The defensible form of Claim 1, in two separable parts

**(i) CAUSAL — UNCONDITIONAL.** A true event horizon transmits nothing from its forbidden side,
for any source whatsoever. This is not a redshift argument; nothing above bears on it, and
nothing above is needed to support it.

**(ii) REDSHIFT SUPPRESSION — CONDITIONAL.** For sources at finite depth approaching the
horizon, the transmitted bolometric weight vanishes iff `gam = o((N-1)^(-1/2))`. Every emitter
of bounded boost satisfies this.

**NOT CLAIMED:** singular emissivity. A source whose emitted intensity diverges in its own frame
is not covered by anything above, was never derived, and is not bounded here. The gate named
this and it remains open.

## Consequence for the receipts

`P6_RECEIPT.md`'s unrestricted phrase "for a source that is not comoving" is **withdrawn** and
replaced by (i)+(ii) above. Claim 1 remains a CONDITIONAL PASS; this receipt supplies the
condition in computable form instead of leaving it as prose.
