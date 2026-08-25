HOLD_S0_OPTICAL_DEPTH_AND_S2_EXCLUSION_UNDERIVED

# Phase 5 S0–S2 adversarial gate verdict

## Blocking objections

### 1. `tau_R` is not yet an optical depth through this TOV region

The script computes

`tau_R = (sigma_T/m_p) rhobar rbar`

as if `rbar` were a spatial column length and as if an outward profile could be integrated at fixed time. The pinned source says the opposite for this branch: `rbar` is the **timelike** variable when `A=1-N<0` (`0210105_clean.txt:93-108`). The physical scattering depth along a null ray is an invariant line integral of the form

`tau = integral sigma_T n_e (-u.k) d lambda`,

with the TOV fluid four-velocity, photon tangent, and actual crossing-to-observer path. Neither implementation performs that integral. The blind seat's `rhobar proportional to rbar^-2` outward-column argument is explicitly an unsupplied assumption, not a property established by the gated orbit. Therefore the reported `tau_R=0.34` at a Hubble-time anchor and the `tau=1` anchor at `1.47e17 s` are arithmetic values of a dimensional proxy, not a derived optical depth.

This is not an order-unity path-length nit: treating a timelike coordinate as a spatial scale height is the exact geometric issue S0 had to resolve.

### 2. The electron density is not fixed by the matched stress-energy

The pinned quantities `rho` and `rhobar` are perfect-fluid energy/mass-energy densities. At the quoted crossing, `u/v = pbar/rhobar approximately 0.1056/0.4300 approximately 0.246`, so the exterior is not a cold proton rest-mass fluid for which `n_e=rhobar/m_p` follows. Saying “fully ionized hydrogen” fixes electrons per baryon; it does not fix baryon rest-mass density as a fraction of the total relativistic energy density, nor pair abundance or temperature. Setting `n_e=rhobar/m_p` is an additional thermodynamic/baryon-loading assumption and can be inconsistent with the matched equation of state.

Thus S0 needs at least one quantity not supplied by the pinned metric/matching system. Under K3/K4, this is a stop-and-brief modelling choice, not a derived one-parameter opacity result.

### 3. S2 does not implement the Phase 5 transfer function

The binding brief requires S2 to combine S1's crossing shift with S0 absorption and, after the freeze addendum, to carry partial absorption **with an emission term** when `tau` is order unity. `s2_transfer.py:10-15` instead declares a common radiation bath and computes only a local kinematic Doppler factor. The blind implementation likewise states that it includes no optical depth, scattering, emission, intrinsic, gravitational, or integrated contribution.

The receipt simultaneously adopts S0's `tau approximately 0.3`, where omission of transfer is not an optically-thin limiting case, and says the missing absolute TOV brightness is K4 and “NOT computed.” That K4 gap prevents the promised `T(mu; x_off,t_obs)` and prevents an exclusion. Agreement between two implementations of the same deliberately reduced kinematic problem does not validate the omitted transfer physics.

### 4. The `3.86e-6` exclusion uses the wrong observable normalization and the wrong frozen bound

The code compares the raw span of `D-1` to a generic `1e-5`. But if the common Doppler monopole is absorbed into the observed mean temperature, anisotropy must be formed relative to that mean, not to the unpredicted pre-crossing temperature. Using the script's own centered value `D0=1.5133957`, its raw small-offset slope `2.5925` becomes approximately `2.5925/D0 = 1.7130` after monopole normalization.

More importantly, the linear small-offset full-sky gradient is dipole-dominated. The frozen record expressly permits B2.2's intrinsic-dipole bound, `3.6-3.7 mK`, not an undifferentiated `1e-5` temperature-anisotropy number (`TRACK_B_FREEZE.md:54-61,99-103`). Relative to a 2.7255 K mean, B2.2 is `1.321e-3` to `1.358e-3`. Even before fixing opacity/emission, the script's normalized slope would give

`x_off/r_* approximately (7.71-7.92)e-4`,

not `3.86e-6`. The claimed four-parts-per-million exclusion is therefore too strong by about a factor of 200 under the applicable frozen dipole bound. A formal multipole projection and frozen-bound confrontation was assigned to S3 and has not occurred; S2's “EXCLUSION” language exceeds its stage and evidence.

### 5. The sign-convention caveat is not adequate

`S2_RECEIPT.md:16-18` says magnitudes and span are convention-independent. They are not for the reported raw quantity. Reversing the relative-velocity sign sends the centered Doppler factor from about `1.5134` to its reciprocal `0.6608`, changing `Delta T/T` from `+0.5134` to `-0.3392`; finite-offset raw spans likewise change. The emitter/receiver ordering and photon direction must be fixed physically and propagated consistently from S1. Calling this a frame convention cannot support convention-independent numerical claims.

### 6. The PINNED/DERIVED contract is violated

Concrete mislabels:

- `S0_DERIVATION.md:16-17` labels the Phase 4-derived light-cone law `z_c=sqrt(N)` as **PINNED**. A prior gated derivation is not a pinned published equation under this phase's definition.
- `s2_transfer.py:6` labels the A1 orbit, `r_*=eta sqrt(N)`, `eta=2 sqrt(t)`, and the crossing condition together as **PINNED**, without a source-and-line citation; the crossing condition is a Phase 4-derived geometry relation.
- `s1_crossing_shift.py:17-18` moves from the published Lipschitz matching to “photon 4-momentum is continuous” and “ALL of the shift” without marking those adapted geodesic claims DERIVED. The pinned source states Lipschitz continuity and Rankine-Hugoniot conservation (`0210105_clean.txt:140-148`); it does not state that optics conclusion.

The brief requires every equation to be either `DERIVED (no pinned source)` or `PINNED (source + line)`. These labels blur those categories.

### 7. S1's required source/limit verification is incomplete even though its central algebra is correct

The receipt cites Landau & Lifshitz only generically, with no edition/section/equation, contrary to the brief's requirement for a specific textbook equation. Its advertised no-jump check is also non-test: the run prints `beta_rel=-0.25` in the alleged no-jump case and passes merely because `abs(beta_rel)<1`. That does not test recovery of zero relative velocity.

These defects do not refute the algebraic identity, but they do refute the claim that the mandatory limiting/source regime has been completed.

## Attacks that did not break

- Independent symbolic substitution of pinned (4.3), (4.4), and (4.5) into the stated shock-frame product relation gives exactly `beta_rel=-1/sqrt(N)`; no sign or factor error was found in that algebra.
- The local textbook shock relation is applicable in principle to this timelike, subluminal perfect-fluid shock: the pinned construction enforces Rankine-Hugoniot conservation, and entropy condition (4.6) supplies the compressive branch (`0210105_clean.txt:140-160`). The fact that TOV `rbar` is timelike does not by itself remove a local shock rest frame. What remains missing is the exact textbook citation and a valid no-jump test.
- Re-running all three scripts reproduced their printed arithmetic, including the raw kinematic slope `2.5925` and raw root `3.857e-6`. The hold is on physical definition, omitted transfer, observable normalization/bound selection, provenance, and scope—not on reproducibility of those calculations.

## Required disposition

Do not carry the S0 opacity value or S2 four-ppm exclusion into S3. First define and compute invariant radiative transfer along the TOV-side null path, gate the additional plasma/source-function assumptions required by K3/K4, fix the physical Doppler orientation, normalize anisotropy after monopole removal, and project onto multipoles before applying the frozen B2/B3 rows.

HOLD_S0_OPTICAL_DEPTH_AND_S2_EXCLUSION_UNDERIVED
