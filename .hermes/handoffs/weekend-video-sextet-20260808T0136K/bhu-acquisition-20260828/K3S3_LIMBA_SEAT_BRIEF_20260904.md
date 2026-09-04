# K3 step 3, limb A — blind seat brief (the cheap disqualifying check)

**Authority:** Duho, "K3 step 3, K5, K6 in order", relayed 2026-09-04 14:56 KST.
**Governing document:** `K3S3_SELFCONSISTENCY_PREREG_20260904.md` (frozen V2) — read it in full first; it binds you.

**BLIND.** Do NOT open, list, grep or infer the contents of any file whose name contains `K3S3_limbA`, `K3S3_LIMBA`,
`K3S3_ROUTE2`, `K3S3_RESULT`, `K3S3_CHECK` or `K3S3_RECONCIL`. You MAY read the prereg, `K3S2_RESULT_20260904.md`,
`K3S1_RESULT_20260903.md`, and the source `../bhu-reading-20260823/sources/1111.4595v2_poplawski_prd85_clean.txt`
("entry 10").

## The single question — limb A of the prereg §1

**Is the four-fermion interaction a small perturbation on the free Fermi gas, at the densities entry 10's bounce
actually invokes?**

Compute the dimensionless ratio of the spin contribution to the ordinary energy density, as a function of temperature,
from entry 10's own relations, and evaluate it at the bounce.

You will need, and must verify at the cited lines yourself:
- `ε̃ = −p̃ = −α n²` with `α = (9/16) κ` — entry 10 Eq. (10), **L116–118**;
- the ultrarelativistic kinetic-equilibrium relations `ε(T)` and `n(T)`, with the effective degree-of-freedom counts
  `g_*` and `g_n` — entry 10 **L152–L159**;
- the bounce/minimum-scale-factor condition — entry 10 **L179–L193**.

## What your script must do, in this order

1. **Restate the definitions you use, with their source lines**, before any algebra.
2. **Derive the dimensionless ratio** `R(T) ≡ |ε̃| / ε` symbolically in terms of `α`, `g_*`, `g_n`, `T` and `κ`.
   Print it. Show its temperature scaling explicitly.
3. **Evaluate `R` at the bounce.** State, from entry 10's own equations, what defines the bounce, and what `R` is
   there. If it is fixed by construction rather than computed, say so plainly and show why from the equations —
   do not dress a definition up as a measurement.
4. **Evaluate `R` away from the bounce**, at a temperature or density scale you name and justify from the source, and
   say whether the interaction is perturbative there.
5. **Apply the prereg's declared threshold:** limb A fires — file `K3S3_NOT_PERTURBATIVE` — if `|R| ≥ 0.1` at the
   bounce. State whether it fires. The threshold is declared in the prereg, not yours to move.
6. **Print the control code** `C4_EXPANSION_PARAMETER_COMPUTED=PASS` (or `=FAIL`) — the parameter must be computed and
   printed, never asserted.
7. **State explicitly which of the prereg's other controls you did NOT run**, by name, and that they are NOT RUN rather
   than passed. Limb A does not reach C1, C2, C3, C5, C6 or C7.

## Deliverables — exactly two files, nothing else changed

1. `K3S3_limbA_<seat>.py` — self-contained, runs under `python3`, prints everything it claims. **Run it.** A claim your
   script does not print is not a claim you have made.
2. `K3S3_LIMBA_<seat>_RESULT.md` — first line exactly one of:
   `LIMBA_NOT_PERTURBATIVE` · `LIMBA_PERTURBATIVE` · `LIMBA_UNDETERMINED`
   and nothing else on that line. Then the derivation, with your script's printed lines as receipts.

## Rules

- **Do not manufacture a number.** If the ratio cannot be evaluated without a prescription the sources do not fix, file
  `LIMBA_UNDETERMINED` and name the freedom exactly.
- If your answer is that the ratio is fixed at 1 by the definition of the bounce, **say that plainly** — it is a
  legitimate and expected finding, and the useful part is then what `R` does away from the bounce.
- Every numeral traces to a source line you cite or to a quantity your script printed.
- Inherit and restate entry 10's own stated regime (ultrarelativistic matter in kinetic equilibrium, L152).
- You have no authority over any tier, warrant token, standing or stamp.

K3S3_LIMBA_SEAT_BRIEF_COMPLETE
