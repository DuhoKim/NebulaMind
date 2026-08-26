HOLD_CONTINUOUS_CANCELLATION_NULL

# REGATE3 Phase 5b verdict

The withdrawn P5/P6 statements were not used as live claims. The current P6 implementation does support the depth redshift and bolometric fourth-power correction, and both delivered scripts execute under the exact pinned environment. The requested exclusion, however, is not established over the stated continuous closure range.

## Blocking finding 1 — the coarse six-point sweep misses a dipole null inside the authorised w range

Fact from `p6_path_transfer.py`: `dipole_and_bound()` takes `abs(...)` at line 140, and the only gate sweep is the six values at line 147. The survival check at lines 154-158 therefore proves only that six already-absolute sampled values are positive. It is not a lower bound over the interval.

I independently retained the sign and decomposed the first-order coefficient into the junction Doppler part and the epoch-varying emergent-transfer part. At `f=1e-4`:

| w | Doppler slope | emergent-factor slope | signed total |
|---:|---:|---:|---:|
| 0.050 | +0.615263 | -0.917407 | -0.302144 |
| 0.040 | +0.615263 | -0.586943 | +0.028320 |
| 0.030 | +0.615263 | -0.451920 | +0.163343 |
| 0.015 | +0.615263 | +0.076609 | +0.691872 |
| 0.010 | +0.615263 | +0.613094 | +1.228357 |

Thus the reported low-w rise is not merely endpoint noise: by `w=0.01` the exterior term has changed sign and adds to the Doppler term. But the same sign change forces a cancellation before that rise. A direct signed angular projection gave:

- `w=0.04075`: `c1_signed = +9.8955e-3` (8-point Gauss-Legendre)
- `w=0.04080`: `c1_signed = -8.7121e-3`
- root search: `w = 0.0407765402`, `|c1| = 4.0e-8` at the numerical root

The broad sign bracket is quadrature-stable: at `w=0.0397035361`, 8/16/24-point projections were `+0.0314285`, `+0.0314523`, `+0.0314190`; at `w=0.0417035361` they were `-0.3616269`, `-0.3616254`, `-0.3616262`. Endpoint coefficients at `w=0.03` and `w=0.01` were also stable as `f` varied from `3e-5` through `1e-3`.

For a continuous physical closure family, this is a real null. At the root the dipole bound is absent, not one part in 120. If the sharp local behaviour is instead attributed to a solver branch artifact, that still blocks the gate until the artifact is resolved and a certified interval bound is produced. Either way, `min(c1)>0` over the authorised range has not been established.

Required repair: preserve the signed coefficient, perform an adaptive/interval sweep across continuous `w`, resolve every sign change, and prove a nonzero lower envelope (or withdraw the exclusion claim for the cancellation neighbourhood). A six-row point sample cannot support the headline.

## Major finding 2 — `LAMBDA_TAU_CLOSURE.md` misidentifies the blind calculation as a fixed-exterior control

The physical geometry does require different crossing epochs for different directions, so P6's per-direction `eta_e` is the more complete geometry in principle. But the claimed reconciliation is not demonstrated by the cited comparison.

`platoon/gpt1_blind_p6/p6_blind_transfer.py` does not hold the exterior profile fixed across directions. In its dipole calculation it explicitly constructs

- `pm = tov_profile(w, ETA0-h)`
- `p0 = tov_profile(w, ETA0)`
- `pp = tov_profile(w, ETA0+h)`

(lines 218-220), and `tov_profile()` calls `shock(eta)` and rebuilds `N0`, `C0`, the profile, and the redshift field for that epoch. What it holds fixed is the dimensionless opacity parameter `lambda` as normalised by `d(tau)/dz=lambda` at the shock (lines 126-128), not the exterior itself.

Therefore the statements that the seat's dipole is pure-Doppler “by construction,” that it supplies a fixed-exterior control, and that the entire residual is explained by fixed versus epoch-varying structure exceed the scripts. The two implementations change several things at once: physical density-derived opacity versus fixed shock-normalised lambda, interpolation/profile formulation, and source normalisation. A matched ablation is still required: run the same P6 functional once with only `eta_e` frozen and once varying it, while holding every other transfer choice identical.

## Reproducibility and guard findings

1. Exact pins reproduce the current P6 six rows and headline discrete values. Command:

   `uv run --no-project --python 3.11 --with numpy==2.4.3 --with scipy==1.17.1 python p6_path_transfer.py`

   Result: 5/5 checks, including `c1 = 0.50616, 0.31116, 0.16327, 1.22741` for the four rows highlighted in the current documents. This reproduces the sampled output but does not cure finding 1.

2. Exact pins do not reproduce every P1c receipt table entry. The corresponding pinned run exits 0 with 7/7 checks, but prints `n/a` at `w=0.999`, whereas `P1C_RECEIPT.md` reports `tau=0.037` for that row and the current kickoff says the receipt's numbers reproduce from the delivered file. The checks never require the high-w endpoint to compute. The important low-w values do reproduce: `tau(0.03)=0.928627`, `tau(0.01)=2.59367`, and the low-pressure extreme is `20.7256`.

3. The stated runtime enforcement “no check can be hard-coded (`chk()` rejects non-computed predicates)” is false. Both `chk()` implementations accept any Python `bool`, including literal `True`; runtime type inspection cannot distinguish a computed boolean from a hard-coded one. I found no literal-boolean predicate in the current check calls, so this is a false enforcement claim rather than evidence that the present calls are hard-coded.

4. Under this host's default Python 3.9.6 / NumPy 1.26.4 / SciPy 1.13.1, both scripts exit 0, but P6 prints `nan` for the centre `tau_tot` at `w=0.03` while still reporting 5/5. The exact pinned environment removes that nan. The pin is therefore load-bearing beyond the advertised trapezoid/trapz naming shim.

## Attacks that did not break

- The metric-frequency relation is consistent with the implemented comoving frame: `omega = E/sqrt(|B|)` and therefore `Z = sqrt(|B_depth|/|B_junction|)`.
- Bolometric Liouville transport requires a fourth-power frequency weight. P6 now uses `Z**4` for both the transmitted intensity (line 120) and every emitted source contribution (line 122), then takes the fourth root only after summing intensities. The exponent and placement are consistent.
- With cumulative optical depth measured outward from the junction, the emitted integrand's `exp(-tau)` attenuates each depth by the optical depth between that depth and the junction; its orientation is consistent.
- The horizon-side term is negligible in the numerical cutoff (`Z_horizon = 5.5769e-6`, hence an intensity weight of order `1e-21`) and vanishes in the horizon limit. The no-background conclusion survives this gate.
- The corrected low-pressure P1c branch and its opaque values reproduce under the exact pins; the old `tau=2.594` failure is repaired for that branch.

## Honest headline allowed now

The current artifacts establish, conditional on the stated source ceiling and sampled closures, that depth-resolved transfer can produce a substantial dipole and that the horizon-side transmitted background vanishes. They do not establish exclusion throughout the authorised continuous closure range. The strongest honest statement is that exclusion holds at the six reported sample points, with an unresolved (and numerically located) cancellation neighbourhood near `w≈0.04078` where the dipole constraint disappears.

HOLD_CONTINUOUS_CANCELLATION_NULL
