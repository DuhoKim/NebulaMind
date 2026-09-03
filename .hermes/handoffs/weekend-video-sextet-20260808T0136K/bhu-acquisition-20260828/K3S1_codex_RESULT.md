HEADLINE=CLOSURE_SCALING_FAILS
OBJECT_FLUID=CLOSURE_SCALING_FAILS
OBJECT_DIRAC=CLOSURE_SCALING_FAILS

## Controls (run before derivation)

- C1 PASS: `sum_i (sigma_i/2)^2 = (3/4) I`; rest-spinor Dirac bilinears project to `sigma_i/2`; value `3/4`.
- C2 PASS: `(<Sx>,<Sy>,<Sz>)=(0,0,1/2)`; `s_z=n/2`, `s_i s^i=n^2/4`.
- C3 PASS: restored fluid expression printed as `c^2*hbar^2*n^2/8=(hbar*c*n)^2/8`.
- C4 PASS: preregistered expectation was loss of the unpolarized class when orientations are made all `+z`; coherent term changed from `0` to `n^2/4`, so `SCALING_FAILS` changed to the polarized closure.

## Derived coefficients and scaling

- Uniform unpolarized ensemble: `<S>=0`, `<S_a S_b>_sym=delta_ab/4`, `<S^2>=3/4`.
- `E|sum_{A=1}^N S_A|^2 = 3N/4`; hence the macroscopic density gives `<s_i s^i>=3N/(4V^2)=3n/(4V)`, not `(3/4)n^2`. Its square of mean is zero.
- RMS continuum prescription: `n^2<S^2>=(3/4)n^2`, which reproduces the printed Dirac coefficient but is not the square-of-sum ensemble average.
- Dirac-dual fluid tensor: `(1/2)<s_ab s^ab>=3N/(4V^2)=3n/(4V)`. The same RMS prescription gives `(3/4)n^2`, not `(1/8)n^2`.
- To force the printed fluid coefficient while retaining a local RMS prescription requires `s_ab=(1/sqrt(6)) epsilon_abk s_k`; this relative normalization is not supplied by the pinned definitions.

## Identity

Contracting `s_ijk=-epsilon_ijkl s^l=s_ij u_k` with the rest-frame velocity gives `s_ab=-epsilon_ab0c s^c` up to orientation sign, and therefore

`(1/2)s_ab s^ab = delta_cd s^c s^d`.

Thus the two printed coefficients cannot describe tensors connected by the stated Dirac dual without an additional normalization/prescription.

## Derivation summary (157 words)

In the Dirac representation with metric `(+---)`, normalized rest spinors give the projected bilinear operators `A_i=(1/2)P^dag gamma^0 gamma^i gamma^5 P=sigma_i/2`. The maximally mixed state, equivalently the uniform orientation average, has zero vector mean, symmetric second moment `delta_ij/4`, and Casimir `3/4`. For `N` independent spins, expanding the square of the sum leaves only diagonal terms: `E|sum S_A|^2=N E(S^2)=3N/4`; division by `V^2` gives `3n/(4V)`. Cross terms vanish, while the square of the mean is zero. Consequently neither printed `n^2` closure follows from the specified unpolarized ensemble. The Dirac `3n^2/4` value follows only after choosing the local RMS continuum prescription `n^2 E(S^2)`. Dualizing the stated Dirac spin tensor to the rest-frame fluid tensor preserves the scalar square, so it gives the same coefficient. Obtaining `n^2/8` additionally requires an unpinned relative normalization `1/sqrt(6)`. The prescription choices are therefore local RMS replacement and, for the fluid coefficient, an independent tensor normalization.
