PASS_PHASE6_OPENING

# CGATE Phase 6 Verdict

Seat: Codex / CGATE
Date: 2026-08-28 KST
Lane: `bhu-theory-phase6-curvature-20260827`

I read `KICKOFF_GATE_PHASE6.txt` in full, read the local artifacts, reran both scripts from this directory, and checked the critical quotations against the pinned target source and primary paper text. My verdict is PASS, with caveats below. The opening correction is sound enough to propagate: the record's prior "confirmed flat universe kills it" condition is wrong; the sign handling is sound; and the citation audit is fair in its revised, narrower form.

## Reproduction

- `python3 c1_curvature_constraints.py`: exit 0, `SELF-CHECKS: 7/7 passed`.
- `python3 c2_constraint_ledger.py`: exit 0, `SELF-CHECKS: 6/6 passed`.

## Source Checks

The pinned target text supports the core correction:

- Abstract line 39 states the compact bracket, `-0.07 +/- 0.02 <= Omega_k < 0`, so a reader can fairly see why the old record copied it as a calibrated window.
- Section VI line 306 states `chi_k > chi_*`.
- Eq. 27 at lines 329-333 gives `Omega_k = -(0.07 +/- 0.02)(chi_*/chi_k)^2`.
- Line 336 says the limits assume the homogeneity scale is due only to `chi_*`, then adds that if the homogeneity scale or low quadrupole has another origin, `Omega_k` could be smaller, and finally states: `Inflation preceded by a bounce requires Omega_k < 0`.

That makes the hard prediction a sign, not a calibrated finite lower-magnitude exclusion of near-flat closed curvature. The bracket is still real as a conditional scale/ceiling, and the abstract really does present it strongly, but the body does not license "flatness refutes it" in the practical finite-precision sense used by the bibliography.

I also checked the observational-support paragraph at pinned target lines 480-481. It cites Planck, ACT, and DESI exactly as the audit says.

## Attack Point Rulings

1. Dataset selection: principled, not the mirror image, if worded carefully. The CMB-alone rows should not be deleted; they are real Planck/Planck-like constraints and they are the target's best support. But setting them aside when judging robust curvature evidence is justified because Planck and ACT both identify the relevant CMB-alone closed preference as tied to lensing/geometric-degeneracy behavior, and because Planck+lensing/BAO are not arbitrary hostile datasets; they are the combinations Planck itself uses to break the curvature degeneracy. The audit's central pattern claim survives: closed support lives in the CMB-alone/anomaly-sensitive corner, while degeneracy-broken combinations sit near zero or on the open side.

2. Eq. 27: the "hard prediction is a sign" reading is right. The abstract bracket should remain recorded as a conditional magnitude scale, not erased, but `chi_k > chi_*` and the caveat in section VI make the bracket non-calibrated as a kill threshold near zero. Refutation is from a confirmed open universe, `Omega_k > 0`, or from a value too closed for the conditional ceiling; not from ordinary flat-consistent constraints.

3. Planck omission: the revised charge is right. The target's Planck number is accurate. Primary Planck text gives the same closed preference and supports the "well over 2 sigma" characterization. But the same Planck section attributes the pull to the same behavior as `A_L > 1`, notes likelihood fragility, and shows lensing/BAO returning the result to flat consistency. A theory paper need not reproduce every caveat, but using that Planck number as headline observational support while omitting Planck's own same-section interpretation is materially incomplete. "Omission" is the correct charge; "misquotation" would be wrong.

4. Sign handling: I find no inversion. The convention used throughout is consistent: `k > 0` means positive spatial curvature/closed and therefore `Omega_k < 0`; `Omega_k > 0` means open/negative spatial curvature. ACT's own wording, "positive spatial curvature, with Omega_K < 0", and Chen/Zaldarriaga's "negatively curved universe with Omega_k = +0.0023" both confirm the mapping. The conversion from `R_k = 21 H_0^-1` to `Omega_k = +1/21^2 = +0.00227` is correct for negative spatial curvature.

5. Scripts reproduced, as above.

6. Open items: none are load-bearing for PASS as stated. The unread DESI companion paper means the ledger should not be represented as an exhaustive DESI-release curvature audit, but it does not rescue the specific target citation to `2503.14738`, which assumes `Omega_K = 0` through most of the paper and derives no curvature preference. ACT v1 Figure 9 remains unchecked, so the figure-number criticism should remain caveated or omitted. The `chi_*` provenance question remains a good next attack, but it is not needed to adjudicate the opening correction.

## Caveat

I noticed a minor equation-numbering mismatch in the Planck references as rendered by arXiv HTML: the values corresponding to the audit's Planck Eq. 46b / 47a / 47b appear as 44b / 45a / 45b in the arXiv HTML view I checked. The numerical values and interpretive sentences match the audit. This is not load-bearing for the verdict, but future citations should pin the exact source version/format used for equation numbers.

Final ruling: PASS_PHASE6_OPENING.
