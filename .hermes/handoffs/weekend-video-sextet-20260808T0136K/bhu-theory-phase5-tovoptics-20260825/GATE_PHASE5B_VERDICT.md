HOLD_A3_A5_A6_RANGES_AND_P2_TRANSFER_NOT_CARRIED

# Phase 5b adversarial gate — P1 through P4

## Blocking objections

### 1. P1 does not carry the authorized A1–A6 range, so `tau <= 0.07` is not an established upper bound

Fact: the frozen brief makes thermal pairs A3 (`none -> full LTE pairs at Tbar`) and the temperature closure A5 (`radiation-carried -> ideal-gas`) mandatory ranges, and says every finding must survive all ranges (`PHASE5B_PLASMA_BRIEF.md:21-31`). The production implementation instead hard-codes

`n_e = f_b * Y_e * rhobar / m_p`

and varies only `w`, `f_b`, and implicitly `Y_e` (`p1_optical_depth.py:65-74, 92-95`). It has no pair-density or temperature calculation. The blind-double record explicitly admits: “pairs ... and post-shock microphysical evolution are not modeled” (`platoon/gpt1_blind_p1/README.md:37-42`). Therefore both implementations agree only on the baryonic-electron subcase; they do not test A3 or the ideal-gas side of A5. No finite all-range upper bound follows from those runs.

This is load-bearing: P2 selects the thin branch solely from that unsupported all-range bound (`P1_RECEIPT.md:40-52`; `p2p4_transfer_confront.py:24`).

### 2. The A6 scan is neither a defined full range nor junction-consistent away from one row

The addendum authorizes `w` from zero to an “entropy-allowed maximum” but never gives or derives that maximum (`PHASE5B_ADDENDUM_A.md:21-24`). Both calculations merely sample `{0.001, 0.05, 0.2456, 0.30}` (`p1_optical_depth.py:92`; `platoon/gpt1_blind_p1/compute_blind_p1.py:19`). Calling `0.30` “the largest allowed equation-of-state parameter” in `P1_RECEIPT.md:42-43` is therefore unsupported by the authorized record.

Independent integration of the same reduced ODE gives `tau=0.07021415996` at `w=1/3, f_b=Y_e=1`, versus `0.06644422661` at `w=0.30`. Because the authorized maximum is undefined, the scan cannot prove the literal `tau <= 0.07` claim even within its baryon-only model.

There is also a boundary-condition conflict. The matched crossing fixes both `pbar_s=u rho` and `rhobar_s=v rho`, so a constant closure `pbar=w rhobar` requires `w=u/v=0.2456375314` at the crossing. The production scan holds `rhobar_s` fixed but sets `pbar_s=w rhobar_s` (`p1_optical_depth.py:28-32, 47-51`), discarding the pinned pressure for every other `w`. The blind double acknowledges exactly this (`platoon/gpt1_blind_p1/README.md:33-35`). Thus the off-midpoint rows are sensitivity models, not profiles satisfying the pinned junction, and cannot constitute the authorized A6 range without a declared EOS parameterization that preserves the shock value.

### 3. P2 is a single constant-source toy case, not the required transfer integral over A4/A5

The brief requires

`I_obs = I_bg exp(-tau) + integral S exp(-tau') d tau'`

with source function spanning LTE blackbody through pure scattering and temperature spanning the A5 range (`PHASE5B_PLASMA_BRIEF.md:26-27, 38-39`). The implementation replaces the integral by

`exp(-tau) * I_shifted + (1-exp(-tau)) * T_ratio`

with one constant `T_ratio=0.8098` (`p2p4_transfer_confront.py:47-61, 70-72, 87`). That reduction is valid only for a constant scalar source function. It does not propagate the exterior temperature profile, evaluate the ideal-gas endpoint, or implement a Thomson-scattering source function/angular redistribution. Consequently the quoted 9.2% is correct for the one chosen ray/source case, but it is not a bound over A4/A5 and cannot support the assumption-robust P4 conclusion.

The brief also mandates a blind double PRIMARY on P1 and P2 (`PHASE5B_PLASMA_BRIEF.md:65-69`). The lane contains a blind P1 packet but no blind P2 artifact. P2 therefore also fails its stated verification regime.

### 4. The primary P1 script is not currently reproducible under its declared unpinned dependencies

On the current lane environment (`numpy 1.26.4`), `python3 p1_optical_depth.py` exits 1 at line 74 because `numpy` has no attribute `trapezoid`; only LC1–LC3 run. This contradicts the executable 5/5 posture in `P1_RECEIPT.md:1-4`. The independent blind script remains usable, so this is not the physics hold by itself, but the production artifact is not presently executable as delivered.

## Failed attacks / points not used as hold bases

- Re-derivation confirms `d tau = sigma n_e |drbar|/sqrt(N-1)` for any future-directed null ray. Angular components do not spoil the cancellation because the comoving four-velocity has only the timelike `rbar` component and every causal ray is monotone in that coordinate.
- The constant-`w>0` endpoint genuinely converges: `rhobar ~ (N-1)^((1+w)/(2w))`, while `N' -> -1/rbar_h`, so the tail is integrable. The horizon is reached at finite `rbar`. For exact `w=0`, the stated equations force vacuum unless the field equation is abandoned.
- P3’s observable normalization `(T-<T>)/<T>` is correct. Independent quadrature reproduces `c1=0.85652 (x_off/r_*)`.
- P4 arithmetic is correct for the kinematic pattern: `(3.7e-3/2.7255)/0.8565 = 1.584996e-3` (one part in 630.9). B2.2 is the right frozen row: `TRACK_B_FREEZE.md:97-103` explicitly allows it for a photon-channel statement, while the unresolved B2.5–B2.11 dispute remains unadjudicated.
- Freeze custody passes: the current brief hash is exactly `51c3452aa359f1c9e297c7bfaf16a41a30b8ccb1ff2ee24da16a6b9ed8f76ef0`. Git history shows the bad state was a pure append, and the 900-byte appended body is byte-identical to the relocated addendum body; the restoration did not alter frozen brief bytes.

The gate remains held until A3/A5 are actually closed and scanned, A6 is made boundary-consistent with an explicit authorized maximum, and P2 carries the full A4/A5 transfer range with its required independent double.
