HOLD_TRACK_A_AMENDED_RECEIPT_RESIDUE

# Track A amendment regate

Scope was limited to the four blocking objections and three required corrections in `GATE_TRACKA_VERDICT.md`. The previously confirmed equations, derivations, numbers, and transcription were not relitigated.

## Disposition of the four blocking objections

1. **Not fully discharged — calibrated/necessary observable claims remain in the receipts.** Amendment 1 correctly withdraws the calibrated exclusion surface, replaces necessity with sufficiency, and demotes P3 to crossing geometry plus an angular-scale heuristic (`TRACK_A_VERDICT.md:37-43,62-66`). But the artifacts the gate required to be amended still say otherwise: `A3_RECEIPT.md:41-50,68-70` retains observational exclusion, “The calibrated statement,” and `consistent ⇔ no cap`; `A4_RECEIPT.md:20-28,42-45` retains `consistency ... ⇔`, calls the region strictly unobservable, and calls the cap the model’s only observable signature. Amendment 1 says it supersedes conflicting language “above” in `TRACK_A_VERDICT.md`; it does not supersede these separate receipt files.

2. **Not fully discharged — the blanket opacity/unobservability claim remains in A4.** Amendment 1 supplies the required photon-only scope, labels the z_ls=1100 screen approximate, and excludes unanalysed messengers (`TRACK_A_VERDICT.md:44-48`). However, `A4_RECEIPT.md:25-28` still states that below the surface the boundary is “strictly unobservable (opacity + interior exactness)” without the amendment’s channel and sharp-screen qualifications.

3. **Not fully discharged — the full H0 limb is still closed in A3/A4.** Amendment 1 correctly limits the exact null and `NOT-A-DISCRIMINANT` classification to wholly interior propagation and classifies boundary-crossing/boundary-influenced probes as uncalibrated (`TRACK_A_VERDICT.md:49-52`). But `A3_RECEIPT.md:11-19` still closes the H0-anisotropy limb as `NOT-A-DISCRIMINANT`, and `A4_RECEIPT.md:48-51` repeats that unrestricted handoff to Track B.

4. **Discharged.** Amendment 1 explicitly restricts all results to pre-horizon epochs, t_obs <= t_crit and N >= 1, and identifies the post-exit Schwarzschild-geodesic regime as not derived (`TRACK_A_VERDICT.md:53-55`).

## Disposition of the three required corrections

1. **Substantively executed, with one stale label residue.** `a1_shock_trajectory.py:79,90,101-102` and the delivered CSV header now use t/t_crit and `t_over_tcrit`; an isolated regeneration produced the same 40,001-row structure and values to numerical solver tolerance. However, the script’s emitted final check at `a1_shock_trajectory.py:97` still labels the value `t0`. The anchor-label correction is therefore not fully propagated through the script’s user-visible output.

2. **Discharged.** `A1_CROSSCHECK.md:39-43` records the current full hashes, independently reproduced as A1_RECEIPT `7c4e96837fa255bb0bc415d7b49d5385a5bc630e4eb18688a839dd38fd448109`, script `eb79b52746ebafe8e8b9bb7f1767a4b213a393a53e50a011bb0a02b171bb1984`, and CSV `c00b26b0244b3cd649b45b117e9e95732972cb0fc256fb7b11bfddac5c8985c7`.

3. **Discharged.** `A4_RECEIPT.md:22-24` now cites t=0.14 to the in-script `cap opens exactly at x_max(t)` check, explicitly says it is not in the delivered map, and labels 20% as one sample rather than a generic early-observer summary.

## Residue required to pass

Conform `A3_RECEIPT.md` and `A4_RECEIPT.md` to Amendment 1: geometry/sufficiency rather than calibrated exclusion/necessity; photon-only approximate-screen language rather than blanket strict unobservability; and a wholly-interior qualifier on the H0 null. Replace the remaining `t0` diagnostic label in `a1_shock_trajectory.py:97` with `t_crit`. No new physics calculation is required by this regate; this is unresolved artifact consistency and label propagation.
