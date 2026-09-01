# AGY Paper Referee Report: 2026-09-01

**Subject:** `STAGE1_PAPER_DRAFT_V1.md`
**Standard:** `PAPER_STRUCTURE_20260901.md` (the honesty contract)

## 1. Overclaim
The paper successfully avoids overclaiming and is exceptionally well-hedged. The abstract explicitly rules out any cosmological result or science image analysis ("This is not a handedness detection or a cosmological result: no galaxy image was analysed for science, no handedness statistic χ was measured, and the calibration parameter γ̂ remains unmeasured"). No sentence drift was found that a reader could extract as a physics claim. The claims remain strictly methodological and synthetic.

## 2. Numbers vs. Receipts (The Finding)
Every cited number was verified against its corresponding receipt, and almost all are perfectly accurate. However, there is one violation of the drafting rule ("Every number cites its receipt file. No number from memory or from an earlier draft's prose"). 

**FINDING (Lines 5, 37, 63):** The text cites `run/classp_candidates/BS-5p.json` as the source for the "frozen floor of 962 successes". While `BS-5p.json` does contain the 984 successes, it does *not* contain the number 962. The value 962 is lifted from the preregistration prose (the frozen `x >= 962` rule, visible in the `CODEX_BS6MAP_20260901.md` mapping), not from the cited candidate receipt. This is a misattribution of a prose constraint to an execution receipt.

All other numbers—including the 49,211 rows, 20,000-permutation null, 84 seat-rounds, 703 findings, the 5,049 evaluations, and the Stage 2 costing arithmetic (270, 850, 1860, 38)—perfectly match their cited files.

## 3. Scope Caveats Preserved
Scope caveats are properly preserved and not buried. The abstract explicitly identifies the robustness rehearsal as "fixture-only" and the antisymmetry tests as "synthetic instrument tests." Section 4.3 quotes the load-bearing machinery caveat verbatim, preserving the critical "NOT invariance_outcome = HELD" limitation.

## 4. Is There Actually a Contribution?
Yes. The paper makes a genuine methodological contribution. Rather than a mere project report, it rigorously details the costs of a hard preregistration, the dependencies exposed (e.g., the calibration cycle), and the strict boundary enforced by human-in-the-loop limits. The arithmetic demonstrating why the pre-image boundary is a forced halt (and why loosening deletes coverage rather than just adding noise) is a valuable result for future survey designs.

## 5. The Boundary Section
The boundary section (Section 5) is reported with complete honesty and mathematical precision. It does not soften the halt. It provides exactly what a future researcher needs: the absolute >=270 real label floor, the impossibility of closing the gap with the 38-person panel limit, the failure of external labels (Galaxy Zoo winding tightness vs. direction), and the explicit demonstration that budgets below 120 decisions fundamentally alter the estimand and abandon coverage.

## 6. What a Referee Would Reject On
If submitted to a methods journal, a referee might raise the following:
1. **Missing Image Execution:** A reviewer might argue the methodology is partially theoretical without an end-to-end science execution. 
   * *Disposition:* Fixable by revision. The paper must stand firm on its premise that the methodological boundary *is* the result.
2. **Citation Precision:** The misattribution of the 962 floor to a JSON receipt rather than the preregistration text (the finding above).
   * *Disposition:* Fixable by revision. Simply cite the frozen text or mapping document for the rule, and the receipt for the execution outcome.
3. **Cryptography in Astronomy:** The heavy emphasis on cryptographic custody (ed25519 signatures, escrow shares) might be viewed as overkill by a traditional astronomy referee. 
   * *Disposition:* Fixable by revision. Clarify in the introduction why standard reproducibility practices fail for this specific parameter (handedness).

SEAT: AGY
VERSION: PAPER-REFEREE-V1
VERDICT: MAJOR-REVISION
COUNT: 1
F-lines: 5, 37, 63
