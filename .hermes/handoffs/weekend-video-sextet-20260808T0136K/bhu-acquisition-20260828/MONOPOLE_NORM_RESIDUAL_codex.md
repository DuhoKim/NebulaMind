# Monopole normalization residual

The calculation uses the fixed overlap window made from balls of radius
`A/2 = 7007.5 Mpc`, hence support `A = 14015 Mpc`, and only the deepest
regulator, `k_min = 4.48318609e-10 Mpc^-1`.

For the no-splice branch, the raw finite-regulator monopole-subtracted
spectrum is evaluated through the convolution input-grid top
`k = 2 Mpc^-1`. Above that point its endpoint ratio to LCDM is tapered from
`1.00064412` to exactly one with the cubic smoothstep `h(u)=u^2(3-2u)`,
where `u=(k-2)/(2.5-2)`, over `2 < k < 2.5 Mpc^-1`. Exact LCDM is then used
from `k=2.5` to the CAMB spline-table top `k=5 Mpc^-1`.

## Actual output of `python3 cutoffA_norm_residual.py`

```text
Residual normalization test: fixed support and deepest regulator
support = 14015.0 Mpc; ball radius = 7007.5 Mpc; k_min = 4.48318609e-10 1/Mpc

SPLICED: original fixed prescription (divide by norm; smooth join 0.0045--0.006; LCDM above 0.006).
c = 4.23706726e-08; norm = 1.07478744
min(P_B) before the join = 8.60208254e-05 Mpc^3
min(P_B) on the full spliced CAMB table = 2.82123344e-10 Mpc^3
min(Delta_B^2) before the join = 4.35786593e-27
S_1/2 spliced = 8776.675 uK^4

NO-SPLICE: raw finite-k_min monopole-subtracted P_B, with no norm divide and no low-k join.
Above the q-grid top k=2, its endpoint ratio is continued with a cubic smoothstep to ratio 1
over 2 < k < 2.5 1/Mpc, and exact LCDM is used from 2.5 through the CAMB table top k=5.
P_B/P_LCDM at q-grid top k=2 = 1.00064412
P_B/P_LCDM probe ratios:
  k = 0.01 1/Mpc : 1.05328598
  k = 0.05 1/Mpc : 1.01732362
  k = 0.20 1/Mpc : 1.00439061
  k = 1.00 1/Mpc : 1.00139526
  k = 2.00 1/Mpc : 1.00064412
min(P_B) on the raw CAMB grid through k=2 = 4.55518887e-09 Mpc^3
min(P_B) on the full extended no-splice CAMB table = 2.82123344e-10 Mpc^3
min(Delta_B^2) on the raw CAMB grid through k=2 = 4.68378304e-27
S_1/2 no-splice = 10132.383 uK^4

Percent difference (no-splice - spliced)/spliced = +15.447%
```

**Verdict:** `S_1/2 = 8776.675 uK^4` (spliced) versus `10132.383 uK^4` (no-splice), a `+15.447%` difference; normalization is therefore a real freedom that must be reported as an error band, not a convention.
