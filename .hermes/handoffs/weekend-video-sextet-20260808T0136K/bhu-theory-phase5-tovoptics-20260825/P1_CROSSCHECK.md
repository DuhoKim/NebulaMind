# P1 blind double — CONFIRMED (2026-08-25)

Two independent implementations of the invariant optical depth, gpt1 briefed WITHOUT being
given the geometry result and explicitly forbidden to read the withdrawn S0 work.

| quantity (w = 0.2456, f_b = 1, Hubble anchor) | Tori | gpt1 |
|---|---|---|
| horizon location r̄_h / r̄_s | 5.179 | 5.179267 |
| τ | 5.8401e-2 | 5.83948e-2 |
| τ at f_b = 0.1 | 5.8401e-3 | 5.83948e-3 |
| τ at w = 0.001, f_b = 1 | 2.4502e-4 | 2.44480e-4 |
| convergence at N → 1 | shown (LC4) | shown, with an explicit cutoff-settlement table |

Agreement to ~4 significant figures throughout; residuals are integration-grid differences.
**P1 stands, and with it the finding that the exterior is optically THIN (τ ≤ 0.07) across the
entire authorised assumption range.**

**Method note, per METHOD_FINDING_BLIND_DOUBLES.md.** This double is worth more than the S0
one was: gpt1 was told the geometry PROBLEM (r̄ is timelike; do not assume a Euclidean column
length) but not the ANSWER, and it derived the invariant element independently — its README
lists an "invariant element, ODE reduction, endpoint proof" of its own. The agreement is
therefore on a derivation, not on an instructed assumption. It also added something I did not
produce: an explicit cutoff-settlement table showing the values stabilise by N−1 = 1e-6, which
is a stronger convergence demonstration than my single LC4 check.
