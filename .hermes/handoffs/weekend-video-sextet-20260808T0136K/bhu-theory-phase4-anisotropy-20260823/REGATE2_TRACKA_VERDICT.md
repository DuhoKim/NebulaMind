HOLD_TRACK_A_AMENDED_A3_RECEIPT_RESIDUE

# Phase 4 Track A — second regate

Scope was limited to the four residue items named in `REGATE_TRACKA_VERDICT.md`. No previously accepted mathematics, transcription, custody, or unrelated Track A claim was re-examined.

## Verification

1. **A3_RECEIPT.md conformance — HOLD residue remains.** The wholly-interior H₀ qualifier is now correctly in place at lines 13–20, and lines 46–54 now use sufficiency/uncalibrated-crossing and photon-channel language. However, conflicting unamended text remains:
   - lines 30–44 still say observed isotropy “requires” all rays to remain interior except an unmodeled TOV-side “conspiracy,” and classify the post-`t_1100` regime as “EXCLUDED”; this retains the calibrated-exclusion/necessity claim withdrawn by Amendment 1;
   - lines 69–73 still say the trichotomy “COLLAPSES TO A DICHOTOMY governed by one constraint surface” and explicitly state `consistent ⇔ no cap ⇔ x_off < x_max(t_obs)`, directly contradicting Amendment 1’s sufficient-but-not-necessary disposition;
   - line 69 still folds in opacity as a blanket premise without the approximate sharp-screen qualifier in that correction passage. The later photon-only wording does not supersede or strike these conflicting statements inside the same receipt.

2. **A4_RECEIPT.md conformance — PASS.** P2 now states sufficiency rather than necessity (lines 20–23), limits unobservability to direct post-recombination photons on wholly interior paths, marks the `z_ls` screen as a sharp approximation, and leaves other messengers unanalyzed (lines 27–31). P3 is crossing geometry plus an angular-scale heuristic, not a calibrated spectrum (lines 45–50).

3. **Wholly-interior H₀-null qualifier in both receipts — PASS.** `A3_RECEIPT.md:13–20` and `A4_RECEIPT.md:54–55` restrict the exact null / NOT-A-DISCRIMINANT classification to wholly-interior sources or complete light paths and leave boundary-influenced probes uncalibrated.

4. **A1 diagnostic label and clean rerun — PASS.** `a1_shock_trajectory.py:97` now emits `t_crit`, not `t0`. An isolated rerun in a temporary directory exited 0 with `12/12 checks passed; rows=40001`; its diagnostic printed `t(sqrtN=100000)=2.764e-11 t_crit`.

## Specific residue required to pass

Conform the remaining conflicting passages in `A3_RECEIPT.md`, especially lines 30–44 and 69–73, to Amendment 1: replace calibrated exclusion/necessity and `consistent ⇔ no cap` with the geometric sufficient hiding condition; describe crossing observables as uncalibrated; and carry the direct-post-recombination-photon plus approximate-`z_ls`-screen scope into the opacity correction passage. No residue remains in the other three named items.
