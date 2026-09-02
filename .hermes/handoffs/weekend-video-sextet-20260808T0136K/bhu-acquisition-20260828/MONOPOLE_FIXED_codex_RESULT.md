# Monopole-subtracted Reading B: fixed-support result

## Result

The corrected overlap window uses balls of radius `A/2 = 7,007.5 Mpc`, so
its real-space support is the intended `A = chi_S = 14,015 Mpc`. The
four-regulator sequence converges to `S_1/2 = 8,776.675 uK^4` (the displayed
three-decimal result); its last successive fractional change is
`+7.672e-11`.

The corrected `c` values, in increasing regulator depth, are
`1.76857019e-08`, `2.52586704e-08`, `3.34691084e-08`, and
`4.23706726e-08`. The global numerical-grid minimum is
`P_B = 8.60207584e-05 Mpc^3`, so positivity is `PASS`. The infrared sanity
ratio is `|P_B(k_tiny)|/|P_B(k_S)| = 1.85197446e-07 < 1e-3` (`PASS`).

The independent noisy-transform cross-check of approximately `10,063
uK^4` is not confirmed by this run; the fixed production calculation is
about 12.8% lower.

`LCDM 34,924 | Reading A 6,897 | Reading B fixed 8,777 | observed ~1,150`

## Support audit

`wtilde()` now evaluates `[3 j_1(s A/2)/(s A/2)]^2` and uses the prefactor
`4 pi (A/2)^3/3`. The `c` integral calls this corrected transform directly.
There is no separate real-space grid in the script; therefore no additional
real-space endpoint required correction. `k_section = 2 pi/A` remains tied
to the intended support `chi_S=A`.

## Actual output of `python3 cutoffA_monopole_fixed.py`

```text
Monopole-subtracted Reading B calculation (fixed support)
chi_section/support = 14015.0 Mpc; ball_radius = 7007.5 Mpc; k_section = 0.000448318609 1/Mpc
Condition: c=<W xi>/<W>, so P_B(0)=0; high-k spectrum joins unchanged LCDM above 0.006 1/Mpc.

k_min/k_section       k_min [1/Mpc]                 c    min(Delta_B^2)       min(P_B)       norm       S_1/2 [uK^4]
         1e-03     4.48318609e-07     1.76857019e-08     4.35786253e-27   8.602076e-05   1.07479         8776.664
         1e-04     4.48318609e-08     2.52586704e-08     4.35787059e-27   8.602092e-05   1.07479         8776.675
         1e-05     4.48318609e-09     3.34691084e-08     4.35786987e-27   8.602090e-05   1.07479         8776.675
         1e-06     4.48318609e-10     4.23706726e-08     4.35786664e-27   8.602084e-05   1.07479         8776.675

Numerical positivity check: PASS
Global grid minimum Delta_B^2 = 4.35786253e-27
Global grid minimum P_B = 8.60207584e-05 Mpc^3
Sanity |P_B(k_tiny=1e-7)|/|P_B(k_S=0.000448318609)| = 1.85197446e-07 (< 1e-3: PASS)
Regulator spread in S_1/2 = 0.010 uK^4 (max/min=1.00000117).
Successive fractional changes = +1.162e-06, +1.254e-08, +7.672e-11
Comparison (smallest-k_min case): LCDM 34,924 | Reading A 6,897 | Reading B fixed 8777 | observed ~1,150
```
