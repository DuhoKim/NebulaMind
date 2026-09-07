# B7 — FILED: in the source's own curved scenario, collapse DOES turn around
**Tori, 2026-09-07 20:12 KST. Authorised by Duho ("as your rec", 19:39 KST). Authored by a research worker, independently challenged on a
different engine: `KIMI_B7_CHALLENGE_20260907.md`, **B7_REVIEW=RESULT_STANDS**, all five attacks failed. Filed by me.**

## The outcome
**`TURNS_OVER`** — in the Kantowski–Sachs geometry the source itself uses, with a Weyssenhoff spin fluid and the source's own
production law, collapse reaches a regular turning point for an **open set of admissible data**, in **both** determined closures.
The referee re-derived the turning-point condition, ran its own solver and twelve symbolic checks (all passed), and perturbed the
data itself rather than trusting the authored perturbation test.

This **answers the curved-scenario question directly**. It does not overturn B6: B1's comparison-of-constants conclusion still
FAILS to transfer and B3's guaranteed-bounce result is still UNDETERMINED *as transfers*. B7 does not transfer anything — it
solves the curved case on its own terms.

## Controls, because the outcome is positive and that is when controls matter most
- **Constraint propagation:** symbolic residual 0; max normalised residual ~1.1e-12 (closure b) and ~8.5e-12 (closure c).
  Verified both symbolically and numerically by the referee, independently of the authored script.
- **Zero-production control:** reported as `FINITE_CUTOFF_UNRESOLVED` with the Kretschmann invariant rising 2.5e11 → 2.5e14 →
  2.5e17 as the cutoff rises. **No singularity is claimed from it.** The referee judged this honest and correct, and found the
  production/no-production contrast sharp: the family still turns at production coefficient 1e-5, with the turn time approaching
  the control's blow-up time from below.
- **Openness, precisely stated:** open in the constraint manifold under constraint-preserving perturbations — the standard
  notion for a constrained system, and stated as such in the authored report rather than glossed.
- Inadmissible data and inadmissible parameters are rejected, not skipped.

## A finding about the source's own stated condition
The source's printed Eq. (35) is **not** the turning criterion. It compares absolute source terms; the turning condition is a
different inequality. **At every positive-Δ turnaround the expansion vanishes, so the left side of printed (35) vanishes while
its right side stays positive — the turnarounds produced by the source's own equations strictly violate the condition the source
states for avoiding a singularity, in both closures.** The referee verified this independently and byte-compared B7's quotation
of (35) against the publisher payload: exact match. This is a claim about the paper, and it is filed only because it was
independently confirmed against the publisher text; it says the stated criterion is not the operative one, not that the paper's
scenario fails.

## Scope
Kantowski–Sachs, Weyssenhoff fluid row, the source's production law, the two determined closures, coupling carried as an
interval, production coefficient carried as a parameter because the source supplies no value. **This is an existence result for
admissible constructed data — not a statement about all initial data, not a prediction for a particular physical collapse, and
not a claim about black-hole-universe cosmology.** The physical-validity limitations stand unchanged: the assumptions this
system rests on remain unestablished in the regime where the turn occurs, and B8 (unreviewed) leaves the unpolarised-spin
question open in both directions.
