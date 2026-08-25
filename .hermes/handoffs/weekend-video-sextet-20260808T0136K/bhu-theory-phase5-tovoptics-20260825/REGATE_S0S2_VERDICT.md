HOLD_OPTICS_INFERENCE_STILL_UNLABELLED

# Phase 5 S0–S2 re-gate verdict

## Blocking objection

The claimed optics-label fix is not in the current `s1_crossing_shift.py`. Lines 25–26 still read:

> The metric matching is Lipschitz (PINNED, ARMA 138 / CMP 210), so the photon 4-momentum is
> continuous across the junction: ALL of the shift comes from the fluid-velocity discontinuity.

That is the exact adapted optics inference which both prior disposition and kimi §5 required to be labelled **DERIVED**. The nearby DERIVED labels cover the shock-variable adaptation, relativistic velocity subtraction, and Doppler formula (lines 19–23); they do not label the separate Lipschitz-to-optics inference on lines 25–26. The inference is physically reasonable, but the provenance contract requires the label, and fix 3 explicitly claimed it was present. It is not.

## Verification of the other repairs

1. **Withdrawal pointers: verified.** `S0_RECEIPT.md`, `S2_RECEIPT.md`, and `S3_RECEIPT.md` each contain a dated WITHDRAWAL POINTER stating that every numeric bound in the withdrawn line is NOT CLAIMED and pointing to `P1_RECEIPT.md` and `P2_P4_RECEIPT.md`. `S0_RECEIPT.md` therefore no longer leaves its old optical-depth numbers live when read through the appended disposition.

2. **Monopole normalisation and 1.585e-3: independently verified, not accepted by coincidence.** From the current pattern, the raw full-span coefficient is 2.5925, so the raw dipole-amplitude coefficient is 2.5925/2 = 1.29625. With centred-sky mean factor D0 = 1.513395725020, the observable coefficient is

   1.29625 / 1.513395725020 = 0.85651755094.

   Frozen B2.2 gives 0.0037 K / 2.7255 K = 0.00135754907. Their ratio is

   0.00135754907 / 0.85651755094 = 0.00158496352,

   i.e. **1.585e-3**, one part in 630.93. A fresh run of `p2p4_transfer_confront.py` independently returned coefficient 0.8565, dipole bound 1.585e-3, quadrupole bound 5.502e-3, and 6/6 checks passed.

3. **Normalisation rule itself: sound for the stated temperature observable.** If `vals = T(mu)/T_FRW - 1` and `mono = <vals>`, then the measured sky mean is `T_FRW(1+mono)` and the fractional anisotropy is exactly `(vals-mono)/(1+mono)`. The current `p2p4_transfer_confront.py` implements precisely that expression before projecting l>=1. It divides the whole monopole-subtracted pattern, not merely one coefficient.

4. **Stale S2 printout: adequately withdrawn.** A fresh run of `s2_transfer.py` still prints 3.857e-6, but immediately under an explicit `WITHDRAWN OUTPUT — ... SUPERSEDED and NOT CLAIMED` banner which explains both the dipole/span error and missing monopole normalisation and points to the live receipt. This meets the re-gate instruction as written; the number is not presented as live.

5. **Taub derivation: correct line by line.** In the shock frame, conservation gives `J = w_i gamma_i^2 v_i`, and momentum-flux equality gives `J(v1-v2)=p2-p1`. Solving the first relation gives `w_i=J(1-v_i^2)/v_i`; substituting `e_i=w_i-p_i` and the pressure jump yields `e2-e1=J(v1-v2)/(v1 v2)`, hence `(p2-p1)/(e2-e1)=v1 v2`. No sign, factor, or hidden textbook dependency was found. A fresh run of `s1_crossing_shift.py` passed 6/6 checks and reproduced the exact-law residual profile.

6. **Blind-double method finding: core claim sound, with the right evidentiary boundary.** Because `BRIEF_GPT1_BLIND_S0.md` explicitly instructed fully ionised hydrogen and `README.md` says `n_e=rhobar/m_p` was used “as directed,” agreement cannot validate that closure; it validates only arithmetic conditional on it. The double did independently reproduce the crossing/root arithmetic and supplied a conditional argument that `rho_bar proportional to r_bar^-2` makes the one-radius column exact, while explicitly stating that profile was not supplied. It did not establish that the exterior actually has that profile or that the timelike-radius proxy is a physical optical depth. `METHOD_FINDING_BLIND_DOUBLES.md` does not claim those stronger conclusions.

## Disposition

Apply an explicit **DERIVED** label to the lines 25–26 optics inference in `s1_crossing_shift.py`. No other defect was found in the four stated repairs or in the two newly requested attacks.

HOLD_OPTICS_INFERENCE_STILL_UNLABELLED
