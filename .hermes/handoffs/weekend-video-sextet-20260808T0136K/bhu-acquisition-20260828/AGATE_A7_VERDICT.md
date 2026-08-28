A7_CONFIRMED_BOTH
REACHES_E25: YES
AUXILIARY: TIDY_STORY
PUBLISHED: NO

## CLAIM A: Tier Category Error
The tier gap is real. Entry 22 is a no-go theorem that constrains physical models by mathematical and geometric obstructions, not by observational testability. Since the current taxonomy (CALIBRATED-FALSIFIER, QUALITATIVE-DIRECTIONAL, CONSISTENCY-ONLY, PROSPECT) categorizes solely by predictive/observational criteria, a theoretical obstruction naturally falls outside its scope. Placing it in CONSISTENCY-ONLY ("shows compatibility with observation") is indeed a category error.

## CLAIM B: Theorem 1 Reaches Entry 25

**Attack 1 (Singular Parent):** The omission of regularity in Theorem 1 is deliberate generality, not an implicit assumption. In Section V.1, Easson explicitly strips away the regular core assumption, stating: "We now assume only that the parent geometry is asymptotically flat with finite ADM mass". The proof relies entirely on the asymptotic Schwarzschild falloff and the Darmois junction conditions, independent of the core's nature. Thus, Schwarzschild qualifies as a parent geometry.

**Attack 2 (No-shell Junction):** Gaztanaga's boundary is "no-shell" in Easson's exact sense. Gaztanaga's timelike junction (Section 2.2.1) is a comoving Darmois boundary ($R = a(\tau)\chi_*$) that perfectly matches the first and second fundamental forms ($K_{ij}^- = K_{ij}^+$ implies $\beta=1$ and $\dot{\beta}=0$). Furthermore, it is a *nondegenerate* (timelike) boundary everywhere along its finite path, even if it approaches the null horizon $r_S$ asymptotically at late times. It perfectly matches Easson's hypotheses.

**Attack 3 (Flat Branch Obstruction):** The flat branch of Easson's theorem states that a non-static curvature-regular flat FRW universe cannot be both null geodesically complete and ANEC-consistent. Gaztanaga's entry 26 proposes exactly this: a curvature-regular flat model (Big Bounce) supported by ANEC-respecting matter (neutron degeneracy pressure). Because Gaztanaga claims his bounce avoids the singularity, he is proposing a model that Easson's theorem proves impossible (unless he implicitly concedes incompleteness).

## Attack 4: Auxiliary Component (Tidy Story)
Check 5 is a TIDY_STORY. The two papers are talking about completely different mechanisms in different regimes:
- Easson notes that an additional bulk component (like vacuum energy, scaling $\le A^{-2}$) is needed to prevent the turnaround and recollapse of a **closed** ($k=+1$) daughter.
- Gaztanaga (whose model is **flat**, $k=0$) notes that observing $w \neq -1$ would imply the acceleration is not solely caused by the BHU horizon. His horizon naturally provides an effective $w=-1$.
You are conflating Easson's escape route for a closed universe with Gaztanaga's observational falsifier for a flat universe. They are not the same ingredient.

## Attack 5: Publication Status
A web search confirms that arXiv:2606.25023 is a preprint and is **not** published in *Phys. Rev. D* under that title. Easson has a related 2026 PRD publication ("Open case for a closed universe"), but entry 22 itself remains an unrefereed preprint. Your bibliography's metadata is incorrect.

## Attack 6: Script Predicate Audit
Several checks in `a7_entry22_nogo.py` claim far more than they test:
- **Check 3:** Claims "every stated hypothesis of Theorem 1 is satisfied" but only tests 4 of them (omitting static, spherically symmetric, finite mass, no late-time bulk component, etc.).
- **Check 5:** Claims the escape route and the auxiliary are "the same ingredient", but the predicate merely tests whether the textual strings exist in their respective documents (`easson_esc and gaz_aux`). It tests for string presence, not theoretical equivalence.
- **Check 1:** Claims the paper's results are "not compatibility demonstrations", but only checks `len(set(props)) >= 3`.
- **Check 2:** Claims it is a "published theorem" but only checks for a specific string `ks` in the text.
