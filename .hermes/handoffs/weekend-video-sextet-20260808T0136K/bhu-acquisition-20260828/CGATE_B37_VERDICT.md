CENSUS_REFUTED_ENTRIES52_AND53

# B37 adversarial verdict — final census batch

The census read is complete, but the submitted “all nine NOT-OBSTRUCTION” result is false. Entries **52 and 53 each own a central theoretical obstruction**: below a derived threshold, no dynamical closed-universe solution exists within the paper's stated Einstein–Cartan cosmological model. These results are proved from the respective Friedmann system, are highlighted in each abstract and conclusion, and are refutable by a counterexample in the defined domain rather than by measurement.

Entries 52 and 53 should be re-tiered from `CONSISTENCY-ONLY` to `THEORETICAL-OBSTRUCTION`. The other seven submitted paper-level verdicts are confirmed.

## Reading declaration

I read these five required sources in full for this gate:

- entry 9, Popławski, *Cosmology with torsion: an alternative to cosmic inflation* (`arxiv_1007.0587.txt`, 575 lines);
- entry 41, Popławski, *A nonsingular, anisotropic universe in a black hole with torsion and particle production* (`2007.11556_clean.txt`, 609 lines);
- entry 45, Firouzjahi and Talebian, *White Hole Cosmology and Hawking Radiation from Quantum Cosmological Perturbations* (`2210.15186_clean.txt`, 1,136 lines, including Appendix A);
- entry 52, Unger and Popławski, *Big Bounce and Closed Universe from Spin and Torsion* (`1808.08327_clean.txt`, 716 lines);
- entry 53, Cubero and Popławski, *Analysis of big bounce in Einstein–Cartan cosmology* (`1906.11824_clean.txt`, 550 lines).

For the permitted refresher set, I re-read the decisive sections and relied on these earlier full-source gate reads:

- entry 23: current source abstract, derivation, and Discussion/Conclusions, supplemented by the earlier series audits;
- entry 26: the Pauli/nuclear-density derivation and full conclusion in the current source, plus my full-source A5 adjudication (`CGATE_A5_VERDICT.md`);
- entry 44: my full-source B17 adjudication (`CGATE_B17_VERDICT.md`), refreshed against its bibliography record;
- entry 54: the singularity-theorem/Birkhoff passages and conclusion in the current source, supplemented by the full-source B15 curvature adjudication.

## Separate rulings

| Entry | Paper-level ruling | Disposition |
|---:|---|---|
| 9 | **NOT-OBSTRUCTION** | Retain `PROSPECT`. |
| 23 | **NOT-OBSTRUCTION** | Retain `QUALITATIVE-DIRECTIONAL`. |
| 26 | **NOT-OBSTRUCTION** | Retain `QUALITATIVE-DIRECTIONAL`; characterize the Pauli halt as asserted/proposed, not proved. |
| 41 | **NOT-OBSTRUCTION at paper level; internal conditional limitation** | Retain `CONSISTENCY-ONLY`; preserve the shear/no-production result in prose. |
| 44 | **NOT-OBSTRUCTION** | Retain `CALIBRATED-FALSIFIER / FIRED`. |
| 45 | **NOT-OBSTRUCTION** | Retain `CONSISTENCY-ONLY`. |
| 52 | **THEORETICAL-OBSTRUCTION** | Re-tier; record the `C` threshold and its assumptions. |
| 53 | **THEORETICAL-OBSTRUCTION** | Re-tier; record its distinct Dirac-field threshold and double-bounce model. |
| 54 | **NOT-OBSTRUCTION** | Retain `QUALITATIVE-DIRECTIONAL`. |

## 1. Entry 26: the Pauli statement is not a proved halt theorem

The paper compares the black-hole mean density with an adopted nuclear-saturation density and notes that they coincide around `7 M_sun`. It then moves from this scale comparison to:

> Higher densities cannot be reached because of the Pauli exclusion principle. This indicates that the collapse must be halted by neutron degeneracy pressure, causing the implosion to rebound as it happens in stars.

That wording is exclusion-shaped, but the paper does not derive it over a defined collapsing-matter class. In particular, it supplies no high-density equation of state, Tolman–Oppenheimer–Volkoff analysis, relativistic hydrodynamic solution through the halt, stability calculation, shock/rebound solution, or treatment of matter that collapses through neutron degeneracy into a black hole. The preceding arithmetic shows a coincident scale; it does not prove that Pauli pressure universally caps density or reverses a relativistic FLRW collapse.

The source repeatedly marks the step as a proposal or argument. Its abstract says “We argue” and “could be avoided”; the conclusion says “We propose” that the collapse bounces at nuclear saturation and explicitly says further work is needed to understand the bounce's details, perturbations, composition, and remnants. The analogy to core-collapse supernovae does not establish the claimed universal halt.

Thus entry 26 contains a strong asserted mechanism, and one whose stated universality is physically under-argued, but not a source-owned proof satisfying the fixed rule. It remains `QUALITATIVE-DIRECTIONAL`.

## 2. Entry 45: no concealed no-mode or no-continuation theorem

I read the entire white-hole perturbation calculation, including the background geometry, scalar mode equation, Bogoliubov transformations on both exterior sides, non-vacuum initial state, summary, and inner-product appendix.

The paper does not prove that a class of white-hole backgrounds lacks modes or cannot be continued. It does the opposite:

- it writes the scalar modes in the anisotropic Kantowski–Sachs white-hole interior;
- propagates right- and left-moving solutions through the past horizon using Kruskal coordinates;
- derives that the deep-white-hole and far exterior observers share the same vacuum;
- obtains the Planck spectrum for the selected vacuum and a non-Planck correction for a general initial state.

The apparent exclusions are background or approximation statements: no signal escapes a black-hole future horizon; white holes are believed unstable; the Kasner constraints require at least one negative exponent; and the exterior potential cannot always be neglected. None is a new paper-owned impossibility theorem over the target cosmological model class. The analysis assumes an eternal Schwarzschild manifold and explicitly leaves realistic potential scattering/greybody effects for future work.

Entry 45 remains `CONSISTENCY-ONLY`.

## 3. Entries 52 and 53: both contain central obstructions, but they are not duplicates

The submitted script notices only their shared phrase about “evading the singularity theorems.” That shared literature sentence is not the relevant result. Each paper later derives its own no-solution threshold.

### Entry 52

Entry 52 assumes a homogeneous, isotropic EC universe with an ultrarelativistic spin fluid whose effective variables satisfy

`epsilon_tilde = epsilon - alpha n_f^2`,

`p_tilde = p - alpha n_f^2`.

Adiabatic evolution gives `xy=C`, where `x=T/T_cr` and `y=a/a_cr`. For `k=1`, the Friedmann equation becomes

`dot(y)^2 + 1 = 3 C^4/y^2 - 2 C^6/y^4`.

At a turning point, the resulting quadratic in `y^2` has discriminant

`9 C^8 - 8 C^6`.

Real turning points therefore require

`C >= sqrt(8/9)`.

Equality gives only the stationary solution; an expanding closed universe requires the strict condition `C > sqrt(8/9)`. Hence no member of the stated closed, homogeneous/isotropic, adiabatic relativistic EC spin-fluid class is an expanding closed-universe solution with `C <= sqrt(8/9)`. A solution satisfying those conditions would be a mathematical counterexample.

This is not a side restriction hidden inside an unrelated construction. “A closed universe exists only when…” is in the abstract, introduction, central Section III analysis, and the paper's summary of its result. The paper also derives further conditional thresholds for avoiding a late turning point and reaching indefinite dark-energy expansion. The creation threshold alone already meets the obstruction rule.

Defensible record:

> In the paper's homogeneous/isotropic, ultrarelativistic, adiabatic EC spin-fluid model, a dynamical closed universe requires `C=aT/(a_cr T_cr) > sqrt(8/9)`; equality is stationary and smaller values yield no real closed-universe turning-point solution.

### Entry 53

Entry 53 is a companion, not a duplicate. It expressly distinguishes the spin-fluid approximation from the Dirac-field closure and uses

`epsilon_tilde = epsilon - alpha n_f^2`,

`p_tilde = p + alpha n_f^2`.

That sign change modifies the thermodynamics. Instead of `aT=constant`, integration yields

`y(x) = (C/x) exp(x^2/2)`.

For a closed universe, the turning-point equation is

`(3x^2 - 2x^4) exp(x^2) = 1/C^2`.

The left side has maximum `e` at `x=1`. Thus:

- `C > e^(-1/2)` gives two turning points and a dynamical closed universe;
- `C = e^(-1/2)` gives a stationary universe;
- `C < e^(-1/2)` gives no turning point, and the paper explicitly concludes that the closed universe “would not exist.”

Equivalently, its conclusion states the threshold as

`x y exp(-x^2/2) > e^(-1/2)`.

Again, this is a derived no-member result, announced in the abstract and conclusion and central to the paper's refinement of earlier bounce dynamics. A below-threshold dynamical closed-universe solution within those equations would refute it without any measurement.

Defensible record:

> In the paper's homogeneous/isotropic EC Dirac-field thermodynamic model, a dynamical closed universe requires `C > e^(-1/2)` (equivalently `xy exp(-x^2/2) > e^(-1/2)`); equality is stationary and smaller `C` admits no such closed-universe solution.

The two results must not be collapsed into one threshold. Entry 52 uses the spin-fluid pressure correction and conserved `aT`; entry 53 uses the Dirac-field pressure sign, exponential `a(T)` relation, and derives the double scale-factor bounce. Each owns its own proof.

Both papers therefore qualify for `THEORETICAL-OBSTRUCTION` under the bibliography's ownership rule and operative-contribution test.

## 4. Entry 9's “exotic fluid cannot exist alone”

Entry 9 rewrites the spin-torsion correction formally as an exotic component with `p=epsilon<0`, then immediately warns that this picture is “purely formal” because such a component cannot exist alone and the displayed relation is not a physical equation of state.

This is not a derived class exclusion. It clarifies that the negative term is not an independently realizable material fluid but an effective contribution tied to the underlying spin fluid. No domain of candidate standalone fluids is defined, no hypotheses are established, and no proof follows. The paper's operative work constructs the torsion-bounce evolution, flatness/horizon behavior, and a prospective rotating-parent signature. Entry 9 remains `PROSPECT`.

## 5. Remaining papers

### Entry 41

Entry 41 has more than a zero-hit constructive closing. It derives an important conditional limitation: in the adopted anisotropic Kantowski–Sachs spin-fluid model with conserved fermion number, shear grows faster than `a^-6` while `n_f^2` grows as `a^-6`; consequently the singularity-avoidance inequality eventually fails. Torsion alone is insufficient in that setup, and the paper introduces phenomenological `beta H^4` particle production to make the fermion term grow faster.

This is real claim-level obstruction content and belongs in prose. At paper level it is the diagnosed failure that motivates the paper's operative torsion-plus-production construction; the title, abstract, equations (33)–(38), and summary are organized around the proposed repair. The production rate remains phenomenological and the final bounce claim says “may.” Under the corpus's operative-contribution convention, entry 41 remains `CONSISTENCY-ONLY`, but it should not be summarized merely as “evading a cited theorem.”

### Entry 23

The “impossible to estimate” sentence says the causal scale cannot be inferred without unknown inflationary inputs, after which the author fits/estimates it by assuming the dark-energy construction. It is an epistemic underdetermination statement, not a theorem excluding a model class. The paper's main result is a boundary-condition construction and qualitative large-scale cutoff. No obstruction tier.

### Entry 44

Entry 44's decisive result is a constructed 5D atmosphere model whose exact scale-invariant spectrum is observationally fired. My full B17 read found additional parameter bounds and prospects but no source-owned theoretical no-go of the required paper-level kind. Its empirical rejection is refuted by measurement and belongs in `CALIBRATED-FALSIFIER / FIRED`, not `THEORETICAL-OBSTRUCTION`.

### Entry 54

Entry 54 invokes the Hawking–Penrose singularity theorems to explain why its positive-curvature/quantum-exclusion setup sidesteps their energy-condition hypotheses. Its Birkhoff corollary is a cited decoupling fact used in the finite spherical-collapse construction. Neither is a theorem newly proved by this paper. The paper constructs a bounce and supplies the already-adjudicated curvature direction; retain `QUALITATIVE-DIRECTIONAL`.

## 6. Is a draw needed for the final batch?

No. Taking the entire fixed remainder removes selection among remainder members, so randomization has no role. The arithmetic is reproducible:

- B31 froze 20 unflagged readable papers outside the 11-paper B28 sample.
- Before B37, the adjudicated remainder was `{38,57,8,43,55,51,31,12,39,21,11}`: 11 papers.
- The set difference is exactly `{9,23,26,41,44,45,52,53,54}`: these nine papers.
- `11 + 9 = 20`; together with B28/B29's 11 sampled papers, all 31 papers in the frozen unflagged readable frame have been adjudicated under the rule.
- Adding the three B1 screen flags accounts for the 34-paper frozen readable frame.

Thus B37 closes the **frozen B28/B31 readable census**. That scope should be stated. It does not prove that no new readable source has since entered the repository, that every bibliography entry was in the frozen frame, or that every prior gate verdict was correct. It means every member of the preregistered unflagged readable frame received an adjudication.

## 7. Predicate audit of `b37_census_final.py`

The script's 4/4 score fails as an adjudication instrument.

1. **Entry 41 predicate:** it checks only the tentative closing phrase “may together violate the strong energy condition.” It misses the paper's actual shear-growth derivation, the no-production failure, the necessary inequality, and the phenomenological nature of the repair.
2. **Entries 52/53 predicate:** it loads only entry 52 and checks only the shared literature phrase “thus evading the singularity theorems.” It never loads entry 53 at all. Most seriously, it ignores the abstracts, the closed-universe turning-point analyses, the discriminant/maximum arguments, and the explicit “exists only when” conclusions that refute the submitted verdicts.
3. **Entry 26 predicate:** substring presence proves only that the strong sentence was printed. It cannot distinguish assertion from derivation and does not test the missing equation of state, collapse dynamics, or the conclusion's “we propose” and “further work” qualifications.
4. **Coverage predicate:** `len([nine literals]) == 9` is tautological. It does not compare against B31's frozen remainder, subtract earlier adjudicated sets, detect duplicates, validate entry identities, or verify that sources were read.

The script loads only entries 41, 52, and 26. It does not load six of the nine sources, does not read the bibliography or current tiers, and never encodes the fixed obstruction rule or operative-contribution test. Its most consequential miss is ironic: it treats a cited theorem-evasion phrase as dispositive while failing to inspect the same paper's own central no-solution theorem.

## Census disposition

- The reading census closes at 20/20 of the frozen B31 remainder and 31/31 of the frozen unflagged readable frame.
- The final batch result is **seven NOT-OBSTRUCTION and two THEORETICAL-OBSTRUCTION**, not nine NOT-OBSTRUCTION.
- Re-tier entries **52 and 53** to `THEORETICAL-OBSTRUCTION`, with separate, assumption-scoped threshold statements.
- Preserve entry 41's conditional shear/no-production limitation in prose without changing its paper-level tier.
- Make no tier changes to entries 9, 23, 26, 41, 44, 45, or 54.
- Replace the coverage tautology with set arithmetic against the frozen B31 frame and prior adjudicated-entry manifests.
