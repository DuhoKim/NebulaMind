ACCESS_SHA=79a025231548887c2f7f94ac3c958a622ec5d07c5014c85e1124f8b4f6ca4d0e
GATE=PREREG_SOUND_WITH_REPAIRS

1.
Quoted sentence: "The Hehl–Datta equation of entry 10 L87–88, iγ^k ψ_{:k} = mψ − (3/8) κ (ψ̄ γ^k γ⁵ ψ) γ_k γ⁵ ψ, the contortion it comes with, C_ijk = S_ijk = ½ κ e_ijkl s^l (Eq. (5), L80–82), and the spin contribution ¼ κ (2 s^i s^k + s_l s^l g^ik) to U^ik (Eq. (6), L84–86), whose trace part the source carries into Eq. (9) (L104–106) as (3/4) κ s_l s^l g_ik."
Defect: Rule 1 (Numeral Tracing). The citation L80-82 for Eq. (5) misses line 83 of the source, which is the line that actually contains the denominator '2' for the numeral '½'.
Replacement wording: "The Hehl–Datta equation of entry 10 L87–88, iγ^k ψ_{:k} = mψ − (3/8) κ (ψ̄ γ^k γ⁵ ψ) γ_k γ⁵ ψ, the contortion it comes with, C_ijk = S_ijk = ½ κ e_ijkl s^l (Eq. (5), L80–83), and the spin contribution ¼ κ (2 s^i s^k + s_l s^l g^ik) to U^ik (Eq. (6), L84–86), whose trace part the source carries into Eq. (9) (L104–106) as (3/4) κ s_l s^l g_ik."

2.
Quoted sentence: "- **What is delivered.** A symbolic or numerically converged evaluation, with the spinor traces shown, of both contractions in both the degenerate and classical limits and in both mass regimes."
Defect: Rule 2 (Falsifier Exactness). "Numerically converged" is a vague deferral of a tolerance threshold; it is neither exact nor explicitly deferred to a receipted pin.
Replacement wording: "- **What is delivered.** A symbolic or numerically converged evaluation (with convergence tolerance explicitly deferred to a receipted pin), with the spinor traces shown, of both contractions in both the degenerate and classical limits and in both mass regimes."

3.
Quoted sentence: "2. **K3S2_EXCHANGE_OTHER_POWER** — the exchange contraction survives but scales as a different power of n (for example a power set by p_F rather than by n²). Report the power and coefficient. CLOSURE_SCALING_FAILS stands and is strengthened."
Defect: Rule 6 (Scope and Standing). Declaring "CLOSURE_SCALING_FAILS stands and is strengthened" inside an outcome class violates the rule against declaring a standing outcome on the document's own authority.
Replacement wording: "2. **K3S2_EXCHANGE_OTHER_POWER** — the exchange contraction survives but scales as a different power of n (for example a power set by p_F rather than by n²). Report the power and coefficient."

4.
Quoted sentence: "3. **K3S2_EXCHANGE_NEGLIGIBLE** — the exchange contraction is sub-leading to step 1's n/V term throughout the density range the bounce papers use (pinned at step 1 from entries 9–11). CLOSURE_SCALING_FAILS stands and is strengthened."
Defect: Rule 3 (Outcome Classes) and Rule 6 (Scope and Standing). There is a logical gap: an exchange term scaling at the exact same order as step 1's n/V term would vanish in the thermodynamic limit (missing classes 1 and 2) but is not "sub-leading" (missing class 3). Additionally, declaring the standing outcome violates Rule 6.
Replacement wording: "3. **K3S2_EXCHANGE_NEGLIGIBLE** — the exchange contraction vanishes in the thermodynamic limit, scaling at the same order as or sub-leading to step 1's n/V term throughout the density range the bounce papers use (pinned at step 1 from entries 9–11)."

Justification:
The preregistration successfully specifies the many-fermion state, maintains strict non-circularity, and tightly bounds the required calculation to the target equations. However, it fails four criteria. (1) The numeral tracing for Eq. (5) misses the line containing the '2' denominator. (2) The tolerance for numerical convergence is not explicitly pinned. (3) The outcome classes have a logical gap for an exchange term that is exactly of order n/V. (4) Classes 2 and 3 illegitimately declare standing changes on their own authority. The supplied repairs enforce strict rule adherence while preserving the test design.

K3S2_PREREG_GATE_COMPLETE
