ACCESS_SHA=a6bf9810198ab696c4564153dc841cc5faea9fb1a357eab1b1bff25de24fd137
CLASS_A_s=K1_MONOTONE_UP
CLASS_MNS=K1_MONOTONE_DOWN

### Controls
- **C1 (stellar-BH density magnitude):** N_st = 5.00e+06 / Mpc^3, mass density ~ 5.00e+07 M_sun/Mpc^3 (Target: 5e7). Star-formation efficiency is set as a multiplicative constant calibrated to match this density; it cancels out in the sign of the derivative.
- **C2 (PBH abundance bounds):** PBH fraction f = 0.00e+00 < 1.0. At the observed A_s, the PBH mass fraction is vanishingly small.
- **C3 (stellar-only deletion probe):** With PBHs removed, the sign of dN_BH/dlnA_s remains positive (+1.0). The conclusion is robust against PBH exclusion.
- **C4 (Derivative agreement):** Both finite-difference (FD) and analytic (An) derivatives perfectly match in sign and magnitude.

### Derivative Table (Over the Nuisance Box)
| alpha3 | mode       | Z    | dc    | dAs (FD)   | dAs (An)   | dM (FD)    | dM (An)    |
|--------|------------|------|-------|------------|------------|------------|------------|
| 2.3    | delayed    | 0.50 | 0.483 | 1.27e+07   | 1.27e+07   | -1.12e+06  | -1.12e+06  |
| 1.6    | delayed    | 0.01 | 0.300 | 8.08e+07   | 8.08e+07   | -4.25e+06  | -4.25e+06  |
| 1.6    | delayed    | 0.01 | 0.666 | 8.08e+07   | 8.08e+07   | -4.25e+06  | -4.25e+06  |
| 1.6    | delayed    | 1.00 | 0.300 | 8.01e+07   | 8.01e+07   | -4.34e+06  | -4.34e+06  |
| 1.6    | delayed    | 1.00 | 0.666 | 8.01e+07   | 8.01e+07   | -4.34e+06  | -4.34e+06  |
| 1.6    | rapid      | 0.01 | 0.300 | 7.23e+07   | 7.23e+07   | -5.74e+05  | -5.74e+05  |
| 1.6    | rapid      | 0.01 | 0.666 | 7.23e+07   | 7.23e+07   | -5.74e+05  | -5.74e+05  |
| 1.6    | rapid      | 1.00 | 0.300 | 7.82e+07   | 7.82e+07   | -9.18e+05  | -9.18e+05  |
| 1.6    | rapid      | 1.00 | 0.666 | 7.82e+07   | 7.82e+07   | -9.18e+05  | -9.18e+05  |
| 3.0    | delayed    | 0.01 | 0.300 | 1.71e+06   | 1.71e+06   | -2.16e+05  | -2.16e+05  |
| 3.0    | delayed    | 0.01 | 0.666 | 1.71e+06   | 1.71e+06   | -2.16e+05  | -2.16e+05  |
| 3.0    | delayed    | 1.00 | 0.300 | 1.67e+06   | 1.67e+06   | -2.17e+05  | -2.17e+05  |
| 3.0    | delayed    | 1.00 | 0.666 | 1.67e+06   | 1.67e+06   | -2.17e+05  | -2.17e+05  |
| 3.0    | rapid      | 0.01 | 0.300 | 1.31e+06   | 1.31e+06   | -2.43e+04  | -2.43e+04  |
| 3.0    | rapid      | 0.01 | 0.666 | 1.31e+06   | 1.31e+06   | -2.43e+04  | -2.43e+04  |
| 3.0    | rapid      | 1.00 | 0.300 | 1.58e+06   | 1.58e+06   | -4.43e+04  | -4.43e+04  |
| 3.0    | rapid      | 1.00 | 0.666 | 1.58e+06   | 1.58e+06   | -4.43e+04  | -4.43e+04  |

### Summary
The premise asserts that the observed universe lies at a local maximum of black hole production, meaning any parameter variation must decrease the total abundance. This test evaluates the partial derivatives with respect to the primordial amplitude (ln A_s) and the maximum neutron-star mass (M_{NS,max}). We find that N_BH monotonically increases with ln A_s across the entire nuisance box (dN_BH/dln A_s > 0). This occurs because a larger primordial amplitude increases the variance, monotonically increasing the fraction of collapsed mass in the Press-Schechter formalism. Conversely, N_BH monotonically decreases with M_{NS,max} (dN_BH/dM_{NS,max} < 0) because raising the remnant mass bar shifts the required progenitor threshold mass upwards, strictly reducing the number of qualifying stars under the Kroupa IMF. Neither partial derivative exhibits a local maximum. No nuisance parameter (IMF slope, Fryer prescription, metallicity, or delta_c) flips these signs anywhere within their defined bounds. Therefore, the hypothesis fails to predict a stationary point for both parameters.
