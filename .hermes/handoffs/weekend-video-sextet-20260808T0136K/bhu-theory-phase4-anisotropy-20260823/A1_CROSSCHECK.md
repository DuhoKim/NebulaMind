# A1 blind cross-check — Tori vs gpt1 (2026-08-24 ~09:28 KST)

Two implementations of the S1 ODE system, written blind to each other (mine:
`a1_shock_trajectory.py`, receipt `A1_RECEIPT.md`; gpt1's: `platoon/gpt1_blind_a1/`, launched
2026-08-23 23:35, completion marker present before my implementation existed). Blind phase for
my side ended 09:26:54 KST after my receipt was hashed; comparison run immediately after
(`_tmp_crosscheck_out.txt`).

## Independent choices that agree

- N's definition: gpt1 read N = 2M/r̄ from the A<0 metric section (their lines 95–97 cite);
  I read N = (r̄H)² from §6's "number of Hubble lengths √N". These are the same statement on
  the shock for k=0 FRW (2M = H²r̄³), and the numerics confirm it.
- Both implementations integrate the unique Theorem-1 branch; both anchor t = 1 at the N = 1
  horizon crossing (gpt1's normalization statement; my (6.1)-anchored choice) and gpt1's
  r̄(N=1) = 2 equals my identity r̄ = 2t√N at that anchor.

## Agreement (40,001 comparison points over S ∈ [1e-10, 1], log-interpolated)

| quantity | median rel. dev. | max ABS dev. | note |
|---|---|---|---|
| u  | 2.8e-07 | 5.4e-05 | max REL dev (4.6e-2) is at S=1 where u ~ 1.2e-9 (absdiff 6e-11) |
| v  | 1.1e-07 | 5.5e-05 | same endpoint artifact |
| s  | 3.5e-07 | ~2e-04  | |
| t  | 1.5e-04 | 4.6e-04 | dominated by interpolating gpt1's 601-pt grid (ΔS ≈ 0.035 near S=1) |
| r̄ | 4.0e-05 | ~2e-04  | after aligning normalizations (×2) |

Spot identity: gpt1's first row t(√N=1e5) = 2.7644109e-11 vs mine 2.7644e-11.

## Verdict

**A1 CONFIRMED by blind double-implementation.** All deviations are attributable to grid
density and endpoint smallness, none to the equations. The A1 deliverable (shock trajectory
r̄(t), √N(t), u, v, s profiles for σ = 1/3) stands verified and feeds A2.

Pins: my script 2ee881ea…, my CSV 3264de39…, my receipt 98c99f37… (full hashes via shasum in
the receipts); gpt1's dir committed as delivered, unmodified.

## Custody refresh (2026-08-24, amendment 1)

The pin line above cites the pre-addendum A1_RECEIPT prefix 98c99f37…. After the anchor-label
addendum and this amendment cycle, current hashes: A1_RECEIPT.md
7c4e96837fa255bb0bc415d7b49d5385a5bc630e4eb18688a839dd38fd448109; a1_shock_trajectory.py eb79b52746ebafe8e8b9bb7f1767a4b213a393a53e50a011bb0a02b171bb1984; a1_results.csv c00b26b0244b3cd649b45b117e9e95732972cb0fc256fb7b11bfddac5c8985c7.
