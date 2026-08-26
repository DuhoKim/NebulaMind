# P1c receipt — the thin-exterior claim is WITHDRAWN. The ranges ARE load-bearing.
(2026-08-26. Cluster A repair of REGATE_PHASE5B_VERDICT.md. This receipt overturns my own
P1_RECEIPT.md headline; the gate's suspicion was right and my conclusion was wrong.)

## What I attempted, and how it failed

Finding A2 said my one-parameter power law did not exhaust the closure space. I replaced it
with a bang-bang bracket, reasoning that driving w to its extremes immediately after the
junction would bound every admissible closure.

**My own optimiser refuted it within the same run:** the power-law optimum gave τ = 0.167 while
the "bound" gave 0.055. A bracket that its own interior exceeds is not a bracket. Cause: the
low-w extreme never computed at all — every w → 0 run failed on the 1/w term in the ρ̄ equation
and returned n/a — so what I had labelled a supremum was **the maximum of the high-w side
alone**. Same failure family as everything the gates have caught: a bound asserted from an
incomplete computation.

## The reformulation, and what it found

Integrating p̄ instead of ρ̄ removes the singularity entirely: with ρ̄ = p̄/w, equation (3.2)
becomes p̄′ = p̄(1 + 1/w)/2 · N′/(N−1), which has no w′ term and where p̄ → 0 damps the 1/w.
The low-w direction then computes:

| w in the exterior | r_h/r_s | τ |
|---|---|---|
| 0.999 | 3.28 | 0.037 |
| 0.500 | 4.06 | 0.058 |
| **0.2456 (junction value)** | 5.18 | **0.132** |
| 0.100 | 6.07 | 0.308 |
| 0.030 | 6.37 | **0.929** |
| 0.010 | 6.44 | **2.594 — OPAQUE** |
| ≤ 0.003 | — | integration fails |

(The junction-value row reproduces P1b's 0.133, so the two formulations agree where both work.)

## The finding, stated against my own prior claim

**τ exceeds 1 inside the authorised range.** A low-pressure exterior is a DENSE one, because
ρ̄ = p̄/w grows as w falls, and dense means opaque. Therefore:

- **WITHDRAWN: "the exterior is optically thin across the entire authorised assumption range."**
  It is thin for w ≳ 0.05 and thick for w ≲ 0.03, and both lie inside the authorised band.
- **WITHDRAWN: "the plasma unknowns are not load-bearing."** They are load-bearing. That was
  P1's most satisfying claim and it is false.
- **WITHDRAWN: "there is no photosphere, and S2b's emitting branch is the wrong regime."**
  The emitting branch is live again for low-w closures.

## What survives, and why the phase is not lost

The conclusion the phase exists to reach may survive the opacity question being reopened,
because **both branches were computed and both exclude**: S2b found the opaque branch gives an
order-0.6 sky contrast (6×10⁴ times the anisotropy scale), and P2b/P4 found the thin branch
requires centring to one part in ~560–1700. If that holds under scrutiny, the exclusion is
robust to an unknown we cannot currently determine — which is a weaker but honest position, and
it is exactly the structure S2b was written to test before P1 wrongly retired it.

## Still owed on Cluster A

A1 (analytic admissible set), A3 (true maximisation — now moot in its old form, since τ is
unbounded within the computable region and the real question is where the closure space ends),
A4 (pair ceiling now uses local w — done in this formulation), A5 (pins written to
requirements-pinned.txt; the trapezoid/trapz shim is the likely cause of the gate's execution
failure), A6 (P2b transfer over the full range, and it must now cover the opaque regime too).
