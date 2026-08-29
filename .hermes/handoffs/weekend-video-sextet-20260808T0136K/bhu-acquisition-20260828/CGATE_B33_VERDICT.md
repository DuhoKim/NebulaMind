BATCH2_CONFIRMED

# B33 adversarial verdict

I re-read **all three papers in full**: entry 8 (382 source lines), entry 43 (793 lines, including the numerical-method appendix), and entry 55 (1,855 lines, including the asymptotic derivation and both appendices). I defaulted against the submitted verdicts and specifically tried to reformulate each technical exclusion as the preregistered class/conjunction no-go. None warrants a paper-level `THEORETICAL-OBSTRUCTION` classification.

The three `NOT-OBSTRUCTION` verdicts are confirmed. Entries 8, 43, and 55 remain `CONSISTENCY-ONLY`. Entry 55 does contain the strongest internal parameter/branch exclusions of the batch, and those should not be erased from its prose, but they delimit the paper's constructive asymptotically-de-Sitter solution rather than constitute its operative result.

## Separate rulings

| Entry | Ruling | Reason |
|---:|---|---|
| 8 | **NOT-OBSTRUCTION** | The isotropic-coordinate sentence is a chart/domain distinction supporting a proposed Einstein–Rosen construction, not a no-go against a physical model class. |
| 43 | **NOT-OBSTRUCTION** | A numerical construction for a selected collapsing boson star; the body contains limitations and causal findings, but no theorem excluding every member of a specified class from a target conjunction. |
| 55 | **NOT-OBSTRUCTION at paper level** | Constructs an asymptotically de Sitter post-bounce interior and derives its allowed parameter surface. Its rejected algebraic branches are internal necessity conditions, not the paper's operative no-go. |

## 1. Entry 8: the isotropic-coordinate claim does not hide a model-class exclusion

The sentence under attack is:

> The Schwarzschild black hole solution, singular at the center, does not exist in isotropic coordinates.

Read against Sections I–III, that wording is shorthand for a coordinate-domain fact. The isotropic radial transformation maps each side of the isotropic throat to a Schwarzschild **exterior** sheet and becomes degenerate at the common horizon. The single isotropic chart used in the paper does not cover the ordinary Schwarzschild black-hole interior ending at `r_S=0`. Instead, extending the isotropic coordinate through its minimum represents a second exterior sheet. This does not show that the Schwarzschild spacetime cannot exist, that no atlas can represent it, or that no spherically symmetric vacuum metric can have the stated properties.

The paper explicitly uses Schwarzschild and Kruskal coordinates to describe the ordinary Schwarzschild solution. Its claim is therefore not a coordinate-invariant impossibility result. A different chart covering the Schwarzschild interior is not a counterexample to a physical no-go; it merely confirms that the limitation attaches to this isotropic coordinate representation.

There are other impossibility-shaped facts in the paper:

- a causal massive particle cannot pass from Kruskal exterior region I to exterior region III in the ordinary maximal Schwarzschild spacetime;
- distant exterior observers cannot distinguish the two proposed interiors;
- without the elliptic identification, the bridge has the familiar instability/traversability problem.

The first is a cited causal-structure fact used to contrast the author's construction, not a proof owned by this paper. The second is an observational-access statement, not the requested theoretical no-go. The third motivates the added identification. The paper's own derivation is constructive: it proposes a regular bridge with a distributional throat source and Rindler identification, derives complete radial geodesics, and speculates about a universe inside.

The source also acknowledges the price of the construction: the throat is not vacuum but requires a divergent energy-momentum source violating the energy conditions. That is a substantive consistency caveat, not a proof that the bridge class cannot satisfy a stated conjunction.

**Entry 8 remains `CONSISTENCY-ONLY`.** Its record may profitably state that the isotropic chart double-covers exterior sheets and does not represent the standard singular Schwarzschild interior.

## 2. Entry 43: body read, no concealed theorem-shaped obstruction

Entry 43 evolves one deliberately unstable spherical boson-star configuration in Palatini `f(R)=R+ξR²` gravity, using a 3% scalar-field perturbation and `ξ=0.1`. In the Einstein frame the simulation forms an ordinary black hole with a long-lived scalar cloud. In the Palatini frame a minimum-area sphere and exponentially expanding inner patch develop after the event horizon, which the paper interprets as a baby universe joined to its parent by a throat.

The collapse-dynamics body supplies several negative statements, but none meets the fixed rule:

- The simulation cannot follow the region between the maximum-area sphere and center beyond `t=91.8`; the authors therefore cannot confirm whether the radial null geodesics reconverge at the center. This is a numerical-access limitation, not a theorem of nonexistence.
- The simulated throat remains inside the event horizon, so light emitted from the baby-universe region cannot escape to the exterior during the simulated evolution. That is a causal property of the computed solution, not a proof that **all** members of a specified model class must hide every throat.
- External observers consequently cannot tell whether this simulated collapse produced an ordinary interior or the expanding inner patch. Again, this is observational degeneracy conditional on the computed horizon structure.
- The conformal map is well posed only while its matter-dependent factor remains nondegenerate and smooth. This is an assumption delimiting the method, not a derived no-go.

The paper does not prove a universal result over its broader parameter claims. Its Final Remarks say the behavior persists over tested values of `ξ`, central amplitudes on the unstable branch, and perturbations strong enough to trigger collapse, but the evidence is numerical and the main run described in detail is highly specific. The authors openly leave late-time throat closure, horizonless outcomes, other matter sources, and asymmetric models for future work.

Thus the paper constructs and numerically exhibits a model; it neither states nor proves that no member of a defined class can satisfy a target conjunction.

**Entry 43 remains `CONSISTENCY-ONLY`.** The zero lexical count played no role in this ruling.

## 3. Entry 55: the strongest adversarial case still does not change tier

Entry 55 deserved the closest attack. It is not merely a survey. Sections III–V derive a QRLG effective Hamiltonian with inverse-volume and coherent-state corrections and obtain its homogeneous interior dynamics. Section VI and Appendix B then impose an asymptotic Laurent ansatz and solve the Hamiltonian constraint and evolution equations order by order.

That derivation contains genuine exclusions and necessity statements:

- the asymptotically Schwarzschild–de Sitter conditions admit two reported parameter sets, with `γ≈0.227` and `γ≈0.274`;
- black-hole-like initial data numerically select the positive-sine branch and hence `γ≈0.274`, while the other branch is not dynamically excluded in general;
- consistency forces several subleading coefficients to vanish and fixes the coherent-state parameters;
- the alternative zero-sine branch implies `ξ=1` and leads to equations that cannot be satisfied;
- without coherent-state subleading corrections, the metric can reproduce de Sitter-like curvature invariants but fails the required stress-tensor falloff conditions;
- the derived effective spacetime has no inner or cosmological horizon in the relevant post-bounce patch.

These are not mere survey phrases. They are source-owned algebraic results. But under the corpus's one-label-per-paper convention, they are parameter and branch restrictions **inside a construction**. The operative question of the paper is whether its QRLG effective dynamics admits an asymptotically de Sitter interior; the paper answers yes, constructs the asymptotic metric, verifies the Ashtekar et al. falloff criteria, and computes the emergent cosmological constant. Rewriting “only these parameter choices work within the adopted ansatz and truncation” as “all other parameter choices are impossible” would be the same promotion-by-negation rejected for entry 37.

The result is also narrower than a general no-go:

- it is conditional on the particular QRLG Hamiltonian, fixed-graph/coherent-state construction, simplicity relation, homogeneous interior reduction, asymptotic Laurent form, and retained correction order;
- Appendix B expressly says more complicated asymptotic solutions are possible;
- the paper does not prove that the displayed interior arises globally from an event horizon—the event horizon is assumed because an interior-only analysis cannot establish it;
- the asserted attractor property is not proved;
- the cosmological-constant estimate relies on a speculative spin-renormalization mechanism left for future work.

The bibliography should record the important claim-level restriction: within the paper's adopted effective Hamiltonian and asymptotic ansatz, satisfying the full asymptotically-de-Sitter criteria fixes the quantum parameters and yields the two reported `γ` branches, with the black-hole evolution selecting `γ≈0.274`; coherent-state subleading terms are necessary for the required falloffs. That is a strong constructive selection result, not a paper-level obstruction.

**Entry 55 remains `CONSISTENCY-ONLY`.**

## 4. Draw discipline

The batch composition is reproducible and does implement the B32 alternation rather than count descent.

- Commit `83e85765b1e304eda6d0b238ced44171cf406b86` exists locally and is the stated pre-draw `check.py` commit.
- Applying the lane's recorded B28 convention—`random.Random(int(SHA[:15],16)).sample(...)`—to the low-count stratum `[8,11,12,43]` reproduces `[8,43]`.
- Entry 55 was the highest-hit unadjudicated paper after entries 38 and 57 were handled in B32.

Thus `{8,43}` is a seeded low-stratum draw and adding entry 55 alternates a low-stratum probe with the top remaining lexical candidate. It is not simple count descent.

This conclusion comes from my independent recomputation. The script's own fourth check does **not** prove it.

## 5. Predicate audit of `b33_census_batch2.py`

The script passes 4/4, but all four predicates are inadequate as adjudication tests.

1. **Entry 8 predicate:** checking only “will be the subjects of further study” establishes one constructive closing sentence. It does not inspect the coordinate claim, the distributional throat source, the causal-region argument, or proof ownership.
2. **Entry 43 predicate:** “robust and persist for all values” verifies a broad conclusion phrase, not the body. It does not encode that the detailed simulation uses `ξ=0.1`, distinguish tested robustness from proof, or inspect the horizon-hidden throat and numerical-access limitation.
3. **Entry 55 predicate:** finding “a possibility not excluded by the dynamics” checks the weaker branch sentence only. It misses the central parameter-selection algebra, the inconsistent zero-sine branch, the necessary coherent-state corrections, and all of Appendix B. The script's docstring also says “10 hits” while B31 reports 12, showing that even its narrative count is not a stable warrant.
4. **Draw predicate:** `True is (int("83e85765b1e304e",16) > 0)` is a tautological positivity check. It never samples the declared stratum, never verifies the commit, never applies the established seed convention, and cannot distinguish `{8,43}` from any other asserted draw.

The script does not read the bibliography, verify current tiers, encode the preregistered paper-level convention, or test any no-go's domain/conjunction/proof. Its 4/4 score establishes only that three selected snippets exist and the hexadecimal literal is positive.

## Disposition

- Confirm all three submitted `NOT-OBSTRUCTION` verdicts.
- Make no tier changes for entries 8, 43, or 55.
- Preserve entry 55's source-owned parameter/branch restrictions in claim-level prose.
- Replace the draw check with an actual SHA existence check and deterministic resampling from `[8,11,12,43]` using the recorded first-15-hex convention.
