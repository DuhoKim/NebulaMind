# Reading B result: compact primordial correlation

## Construction and positivity

I used

\[
\xi_B(r)=\xi_{\Lambda\mathrm{CDM}}(r)W(r),\qquad
W(r)=\frac{(1-r/a)^2(2+r/a)}{2}\quad(0\le r\le a),
\]

with `W=0` beyond `a=chi_section=14015 Mpc`. The Fourier transform of the window is

\[
\widetilde W(k)=V_a\left[\frac{3j_1(ka)}{ka}\right]^2\ge0,
\qquad V_a=4\pi a^3/3.
\]

Consequently, transforming the real-space product is equivalently a convolution of
`P_LCDM` with the nonnegative `W_tilde`. This is the Schur/Bochner positive-definiteness
guarantee: `xi_LCDM` and `W` are positive definite, their product is positive definite,
and hence `P_B >= 0`. The calculation evaluates this positive convolution directly. The
minimum tabulated dimensionless power was positive in every regulator run, as shown in
the actual output below. The spectrum is smoothly joined to the exact, unchanged LCDM
primordial power by `k=0.006/Mpc`; thus high-ell power is held fixed and is not refitted.

CAMB was run full-sky and unlensed through `ell_max=150`, with the specified cosmology,
`set_scalar_table`, `effective_ns_for_nonlinear=ns`, `NonLinear_none`, and
`lens_potential_accuracy=0`. `S_1/2` was evaluated by 1200-point Gauss-Legendre integration
of the Legendre sum on `-1 <= cos(theta) <= 1/2`.

## Central result

Reading B does **not** predict a regulator-independent `S_1/2`. Lowering `k_min` through
three decades below `k_section` changes `S_1/2` monotonically from `252,066` to `900,646
microK^4`, a factor of `3.573`. This is not treated as a numerical bug: the infrared
constant in `xi_LCDM`, ordinarily an unobservable monopole, is multiplied by `W` and is
therefore converted into physical low-k power. The paper supplies no prescription for
that constant or its regulator. Reading B therefore has no unique numerical prediction.

For the smallest displayed regulator, the requested comparison is:

`LCDM 34,924 | Reading A 6,897 | Reading B 900,646 | observed ~1,150`.

Reading A and every displayed Reading B result lie on the **same** (high) side of 1,150;
the computed Reading B result does not confirm the prediction that they would be on
opposite sides.

## Actual pasted output

```text
Reading B compact-correlation calculation
chi_section = 14015.0 Mpc; k_section = 0.000448318609 1/Mpc
W(r)=(1-r/a)^2(2+r/a)/2 for r<=a, zero otherwise
W_tilde=V[3 j1(ka)/(ka)]^2 >= 0; convolution with P_LCDM>=0 guarantees P_B>=0.
High-k normalization: P_B is joined to the unchanged LCDM spectrum above 0.006 1/Mpc.

k_min/k_section       k_min [1/Mpc]      min(Delta_B^2)    norm       S_1/2 [uK^4]
         1e-03     4.48318609e-07     8.21242852e-18   1.13140       252066.304
         1e-04     4.48318609e-08     1.16924294e-17   1.17302       422587.809
         1e-05     4.48318609e-09     1.51967211e-17   1.21814       638775.597
         1e-06     4.48318609e-10     1.87140187e-17   1.26706       900645.605

Numerical positivity check: PASS
Reading-B regulator spread in S_1/2 = 648579.301 uK^4 (max/min=3.57305).
Comparison (smallest-k_min case): LCDM 34,924 | Reading A 6,897 | Reading B 900646 | observed ~1,150
A and B are on the same sides of 1,150.
```

The runnable source that produced this output is `cutoffA_readingB.py` in this directory.
