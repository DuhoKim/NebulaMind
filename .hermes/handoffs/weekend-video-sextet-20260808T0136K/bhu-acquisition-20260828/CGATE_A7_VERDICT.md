A7_CONFIRMED_TIER_ONLY
REACHES_E25:  NO
AUXILIARY:    TIDY_STORY
PUBLISHED:    YES

## Ruling

Claim A is sustained. `CONSISTENCY-ONLY`, as defined here, describes an observational evidential role: compatibility without a stated falsifier. Easson's central results instead exclude combinations of mathematical assumptions. The paper says, for example, that the flat/open class “cannot be both null geodesically complete and ANEC-consistent,” and concludes that a construction “must give up at least one” of a list of structural conditions. Calling that `CONSISTENCY-ONLY` does not merely coarsen its evidential strength; it misstates the kind of work the result does. If the four tiers are exclusively observational-testability tiers, the schema lacks a field for a theoretical no-go/constraint. That is a real representational gap.

Claim B is not sustained. The literal statement of Theorem 1 does not list regularity of the parent, so Schwarzschild is not excluded merely because its vacuum extension has a singular center. Section II does assume “an asymptotically flat exterior and a regular core,” and the paper's framing and conclusion repeatedly concern regular black holes, but Section V deliberately broadens the result: it calls the theorem “a structural statement about asymptotically flat constructions,” says the closed result follows from asymptotic flatness and finite ADM mass, and says the flat/open result follows from general FRW completeness constraints. For the flat/open clause, parent regularity is not the decisive problem.

The decisive problem is the junction and the daughter actually claimed by Gaztanaga. Easson assumes a “nondegenerate comoving spherical Darmois boundary,” no shell, and evolution fixed by the parent profile without an additional late-time bulk component. Gaztanaga presents two different junction regimes. His Section 2.2.1 starts with a timelike surface “fixed in co-moving coordinates,” but the BHU boundary used for the acceleration claim is the event horizon. Section 2.2.3 expressly says: “A null junction has degeneracies that require more elaborate consideration,” and its radial coordinate is not generally comoving (`chi_*` “is not always constant”). Later he identifies the physical BHU junction as an event horizon, `R = R_*`, and states that the interior becomes de Sitter only asymptotically as `R -> r_S`. Thus the load-bearing horizon junction is null/degenerate and non-comoving in precisely the ways excluded by Easson's hypothesis. “There are no surface terms” is a no-shell claim, but it cannot cure the nondegenerate/comoving mismatch.

There is a second mismatch. Easson's minimal flat matching gives the large-scale law `H^2 ~ 2M/(A^3 chi_b^3)` and `A(tau) proportional to tau^(2/3)`. Gaztanaga instead attributes asymptotic de Sitter acceleration to the event-horizon/action-boundary mechanism. One cannot simultaneously treat that mechanism as nothing beyond Easson's parent-profile Darmois evolution and use its accelerated asymptotics. The script never tests this hypothesis.

Accordingly, Theorem 1 may diagnose what a genuinely nondegenerate, comoving, minimal Schwarzschild-to-FRW matching would have to sacrifice, but it does not directly reach the event-horizon construction described in entry 25.

## Flat/open branch and bounce

The applicable curvature class would indeed be `k=0`. But entry 25 explicitly concedes incompleteness in the relevant sense at the level available here: “the BHU (or the FLRW*) metric is not static and has a past singularity.” It does not claim the neutron-degeneracy-pressure nonsingular bounce attributed by the script to entry 26; it says formation is deferred to paper II. No pinned entry-26 source was supplied, so the script's assertion that entry 26 supplies an ANEC-respecting, geodesically complete bounce is not tested. In any event, “nonsingular bounce” alone does not establish null geodesic completeness or regular affine ends. Entry 25 is therefore consistent with the flat/open obstruction, not shown to be forbidden by it.

## Auxiliary correspondence

This is `TIDY_STORY`. Easson's “additional smooth bulk component whose density redshifts no faster than A^-2,” with positive vacuum energy as an example, is specifically introduced as an escape from the *closed-branch* late-time balance. Entry 25 is flat. Gaztanaga's statement that `w != -1` would indicate acceleration is “not solely caused by the BHU event horizon” does not name a smooth bulk component, its redshift law, or vacuum energy; it permits any additional or alternative cause. The two sentences can be narratively aligned, but they do not establish identity of a technical ingredient.

## Publication status

Publication is verified from APS: Damien A. Easson, “Obstructions to minimal regular black hole cosmologies,” *Physical Review D* **114**, 044077, published 24 August 2026, DOI `10.1103/qs86-npwk`. APS records receipt on 25 June and acceptance on 31 July 2026: https://journals.aps.org/prd/abstract/10.1103/qs86-npwk

## Reproduction and predicate audit

`python3 a7_entry22_nogo.py` reproduced `SELF-CHECKS: 5/5 passed` and exit status 0. The five checks do not warrant their displayed names:

1. The predicate only counts three proposition/theorem labels. It does not test that the paper is not a compatibility demonstration.
2. The predicate only searches for one sentence. It tests neither publication nor “independently confirms,” nor the claimed Phase-5 consequences.
3. The predicate checks a numerical Schwarzschild identity and three phrase occurrences. It omits finite positive ADM mass, nondegeneracy, comoving character, actual Darmois second-fundamental-form matching, parent-fixed daughter evolution, and absence of extra late-time structure. Equating “no defects or discontinuities” with the complete technical hypothesis is invalid. This is the load-bearing false positive.
4. The predicate only finds two phrases in Easson. It does not inspect entry 26, ANEC of its matter, curvature regularity, regular affine ends, or geodesic completeness.
5. The predicate only finds phrases in each text. It does not show that the phrases denote the same ingredient; they do not do so with the required specificity.

The pinned entry-25 extraction visibly fragments equations across many lines, and the Easson extraction sometimes duplicates rendered and TeX forms. The prose quotations used above remain intelligible and the decisive null/degenerate/comoving statements are intact. I did not rely on reconstructing a damaged equation to reach the verdict.
