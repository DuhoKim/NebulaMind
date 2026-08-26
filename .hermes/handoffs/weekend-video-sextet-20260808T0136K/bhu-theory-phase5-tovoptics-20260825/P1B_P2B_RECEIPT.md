# P1b / P2b receipt — the ranges actually swept, and the bound they give
(2026-08-26, stamped at commit. p1b_range_sweep.py + p2b_transfer_sweep.py, logs
_tmp_p1b_run.txt / _tmp_p2b_run.txt, 6/6 and 4/4 checks. Answers gate objections 1–4 of
GATE_PHASE5B_VERDICT.md. Dependency pins, obj 4: python 3.11.15, numpy 2.4.3, scipy 1.17.1.)

## The gate was right, and the number moved

**τ ≤ 0.07 was never established.** It came from a four-point grid, not a sweep. Swept properly:

**τ_max = 0.133** — 2.3× the withdrawn figure, attained at q = −0.475 in the A6 family.

Two things I had left out did the work:

1. **A6 made junction-consistent (obj 2).** A constant w is inconsistent at the junction for
   every value except u/v. The family is now w(r̄) = w_s(r̄/r̄_s)^q with w_s = u/v = 0.245638
   fixed *by construction*, and the **authorised maximum is derived, not chosen**: q is swept
   over exactly the interval keeping 0 < w < 1 from shock to horizon per pinned bound (5.5),
   which turns out to be **q ∈ [−0.75, 0.90]** (33 admissible of 61 trialled).
2. **A3/A5 pairs, bounded by the energy budget (obj 1).** Scatterers cannot carry more energy
   than ρ̄ holds. A cold neutral plasma ceilings at n_e = ρ̄/m_p; a relativistic pair gas does
   better, at most ρ̄c²/(3kT̄). At the crossing the ideal-gas sub-case has kT̄ = 138 MeV, giving
   **2.26× more scatterers than full baryon loading** — the corner the old grid omitted.

## P2b — the transfer swept over A4/A5 (obj 3), and a distinction P2 had blurred

The exterior cannot radiate more than its energy density supports: aT⁴ ≤ ρ̄c², so the source
ceiling is v^(1/4)·T_FRW. **A5's ideal-gas sub-case raises the KINETIC temperature and hence
the pair census, but cannot raise the radiation source** — P2's single case did not separate
these. The authorised source range is therefore S/T_FRW ∈ [0, v^(1/4)]: pure scattering to full
LTE at the ceiling.

Swept across τ × A4:

| | pure scattering | half | full LTE |
|---|---|---|---|
| τ = 0 | 1.585e-3 | 1.585e-3 | 1.585e-3 |
| τ = 0.066 | 1.585e-3 | 1.632e-3 | 1.680e-3 |
| τ = 0.133 | 1.585e-3 | 1.684e-3 | **1.787e-3** |

**Bound across the entire authorised range: x_off/r_* < 1.585e-3 to 1.787e-3** — one part in
631 at the strongest corner, one part in 560 at the weakest. The transfer never becomes a
competitor to the kinematic term (weakest/strongest = 1.13).

## What this does and does not change

- **Changed:** the optical-depth ceiling (0.058 → 0.133) and the quoted bound, which is now a
  RANGE across swept assumptions rather than a single figure from one corner.
- **Unchanged:** the exterior is optically THIN across the whole authorised range (0.133 ≪ 1),
  so there is still no photosphere; and the conclusion still holds — a boundary inside our
  last-scattering sphere requires the observer centred to better than one part in ~560.
- **Still owed:** P2b's independent blind double, which the brief requires and the gate
  demanded. Dispatched with this receipt.
