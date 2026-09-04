# K3 step 1 — what a critic gets

Tori note, 2026-09-04 01:36 KST. NOTE ONLY — NO STUDY STARTED.

## Strongest remaining objection

K3 step 1 exactly answers the ensemble it preregistered: N uncorrelated, randomly oriented spin-1/2 particles represented as a sum of single-particle spins. In that ensemble the cross terms factor through the zero one-body spin mean and the squared macroscopic density scales as n/V, not n² (`K3S1_RESULT_20260903.md` §§2–3).

A critic's strongest response is that this may not be the quantum operator and state that Einstein-Cartan theory actually needs. Entry 10's Hehl-Datta equation contains a local axial-current self-interaction (`1111.4595v2_poplawski_prd85_clean.txt` L87–100), and its effective source contains the local quadratic spin term before the paper states either macroscopic closure (L100–121). For identical fermions, an unpolarized one-body state does not by itself make the coincident two-body expectation factorize: Fock/exchange contractions, contact-term subtraction, normal ordering, species content and the coarse-graining prescription can change both the density power and coefficient even when the one-body spin mean is zero.

Therefore the surviving objection is narrow but real: `CLOSURE_SCALING_FAILS` rules out the uncorrelated product-ensemble derivation of 1/8 n² and 3/4 n²; it does not yet rule out a regulator-stable n² contribution in the correctly defined local axial-current four-fermion expectation. Gasperini does not answer this—his full text states the closure without that calculation—and Nurgaliev & Ponomariev remains unread.

## Evidence that would settle it

A settling calculation must do all of the following without taking either printed coefficient as input:

1. Start from the same local axial current/spin tensor that enters the torsion-eliminated Dirac equations, and derive the exact map to `⟨s_i s^i⟩` and `1/2⟨s_ij s^ij⟩`, including sign, projection and normalization.
2. Specify the many-fermion state: at minimum an unpolarized free Fermi gas with occupation numbers, species/antiparticle content, temperature and chemical potential fixed.
3. Evaluate the coincident quadratic operator with the exchange/Wick contractions shown separately from the direct term, using an explicit normal-ordering or renormalization prescription and a stated coarse-graining scale.
4. Report the leading density power and coefficient in the thermodynamic limit. The high-temperature/classical limit must reproduce K3 step 1's n/V result; deleting antisymmetrization must delete the exchange contribution; the polarized limit must reproduce n²/4 at leading order.
5. Map the result back to both printed relations: spin-fluid 1/8 and Dirac 3/4. A regulator-independent n² term for the same audited object would narrow or overturn the general closure claim according to its coefficient. Only n/V or a different power would strengthen `CLOSURE_SCALING_FAILS`. Dependence on state, regulator or coarse-graining would yield `CLOSURE_PRESCRIPTION_DEPENDENT`, not a derived universal coefficient.

A readable Nurgaliev full text could close the historical citation question, but only an explicit same-object operator calculation can settle the scientific objection.

**ANSWERED. K3 step 2 was ordered by Duho at 2026-09-04 09:57 KST and completed the same morning (`K3S2_RESULT_20260904.md`, class `K3S2_EXCHANGE_N2_RESTORED`).** The objection recorded above was well founded: the coincident-point exchange contraction of the correct local operator does produce an n² term. It is −(3/8)n²/N_f non-relativistically and −(3/16)n²/N_f ultrarelativistically — negative, and regime- and species-dependent — so it matches neither printed coefficient and contradicts both in sign. The five conditions listed above as "evidence that would settle it" were carried into `K3S2_EXCHANGE_PREREG_20260904.md` as binding deliverables. K4, K5 and K6 were all ordered and completed on 2026-09-04. Paper HOLD; nothing outward.

K3S1_CRITIC_NOTE_COMPLETE
