# Monopole-subtracted Reading B: result

## Verdict

After imposing

\[
c=\frac{\int d^3r\,W(r)\xi_{\Lambda\mathrm{CDM}}(r)}
        {\int d^3r\,W(r)},\qquad
\xi_B(r)=[\xi_{\Lambda\mathrm{CDM}}(r)-c]W(r),
\]

the `k_min` sequence **converges**. At the smallest regulator tested,
`S_1/2 = 23,899.965 μK^4`; the final two decade steps change it by only
`6.086e-08` and `1.630e-09` fractionally. Therefore the previous conclusion
that Reading B has no regulator-independent number is **overturned** by
monopole subtraction.

Positivity also survives on the numerical grid. The global minimum is
`Delta_B^2 = 1.46326147e-25`, corresponding to
`P_B = 2.88836237e-03 Mpc^3`; both are positive.

The converged prediction remains much larger than the observed value:

`LCDM 34,924 | Reading A 6,897 | Reading B (subtracted) 23,900 | observed ~1,150`.

## Computation

The calculation used the cosmological parameters in the brief, the same
compact overlap window and convolution pipeline as the prior Reading B run,
and explicitly subtracted `c W_tilde(k)` from the convolved dimensional power.
The result was normalized to unchanged LCDM above `k = 0.006 Mpc^-1` and sent
to CAMB with `set_scalar_table`, `effective_ns_for_nonlinear=ns`,
`NonLinear_none`, no lensing, and `lmax=150`. `S_1/2` was evaluated by direct
Gauss-Legendre integration of the full-sky unlensed correlation function.

## Actual output of `python3 cutoffA_monopole.py`

```text
Monopole-subtracted Reading B calculation
chi_section = 14015.0 Mpc; k_section = 0.000448318609 1/Mpc
Condition: c=<W xi>/<W>, so P_B(0)=0; high-k spectrum joins unchanged LCDM above 0.006 1/Mpc.

k_min/k_section       k_min [1/Mpc]                 c    min(Delta_B^2)       min(P_B)       norm       S_1/2 [uK^4]
         1e-03     4.48318609e-07     1.59056193e-08     1.46326147e-25   2.888362e-03   1.04951        23899.833
         1e-04     4.48318609e-08     2.34785784e-08     1.46327288e-25   2.888385e-03   1.04951        23899.963
         1e-05     4.48318609e-09     3.16890163e-08     1.46327282e-25   2.888385e-03   1.04951        23899.965
         1e-06     4.48318609e-10     4.05905805e-08     1.46327253e-25   2.888384e-03   1.04951        23899.965

Numerical positivity check: PASS
Global grid minimum Delta_B^2 = 1.46326147e-25
Global grid minimum P_B = 2.88836237e-03 Mpc^3
Regulator spread in S_1/2 = 0.132 uK^4 (max/min=1.00000553).
Successive fractional changes = +5.472e-06, +6.086e-08, +1.630e-09
Comparison (smallest-k_min case): LCDM 34,924 | Reading A 6,897 | Reading B (subtracted) 23900 | observed ~1,150
```
