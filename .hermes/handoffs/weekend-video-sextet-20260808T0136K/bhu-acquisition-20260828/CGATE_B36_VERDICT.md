BATCH4_NARROWED_DRAW_PROVEN_NOT_BLINDNESS

# B36 adversarial verdict

I read all three pinned papers in full:

- entry 39, Popławski, *Big bounce from spin and torsion* (`1105.6127_clean.txt`, 451 lines);
- entry 21, Roupas, *Detectable universes inside regular black holes* (`2203.13295_clean.txt`, 1,508 lines, including all five appendices);
- entry 11, Popławski, *Universe in a black hole in Einstein–Cartan gravity* (`arxiv-1410.3881v2.txt`, 691 lines).

All three submitted paper-level `NOT-OBSTRUCTION` rulings are confirmed. Entry 21 does own a genuine but tightly scoped claim-level radial-stability exclusion, which should be retained in prose. It does not displace the paper's operative constructive/prospect contribution.

The draw itself reproduces exactly. What must be narrowed is the stronger claim that the code was committed “before the reads”: Git establishes ordering of repository artifacts, not the author's private reading history, and the bibliography already records earlier reads of these papers. The defensible statement is that the executable draw was committed before the B36 batch adjudication artifact.

## Separate rulings

| Entry | Ruling | Disposition |
|---:|---|---|
| 39 | **NOT-OBSTRUCTION** | Retain `CONSISTENCY-ONLY`. |
| 21 | **NOT-OBSTRUCTION at paper level; narrow internal no-mode result** | Retain `PROSPECT`; add the precise radial-stability scope to prose if absent. |
| 11 | **NOT-OBSTRUCTION** | Retain `CONSISTENCY-ONLY`. |

## 1. Independent execution of the committed draw

I executed the stored file directly:

`python3 b35_draw_batch4.py`

It printed:

`seed a2d70fd0c  batch 4: high=39, middle=21, low=11`

I also independently repeated its operations rather than trusting its output:

- seed integer: `int("a2d70fd0c"[:9], 16)`;
- ordered high pool: `[41,54,9,39]`;
- ordered middle pool: `[23,26,45,21,44,52,53]`;
- low pool: `[11]`;
- one shared `random.Random` instance, consuming one `sample(...,1)` from high and then one from middle, followed by the sole low member.

That independently returns `(39,21,11)`. The ordering is explicit and accords with the stated rule: descending B31 hit count, ties by ascending entry number. It avoids B34's unordered-pool defect.

The file is present in commit `a038e197b511d0f367df0cc4785bcd0f9433e891`, timestamped 2026-08-30 00:21:19 +09:00. Its seed is the preceding batch-3 gate commit `a2d70fd0cd86f8d02741c53dd8d34f93a745b927`, timestamped 00:16:33 +09:00. Thus the seed existed before the draw-code commit, and the checked-out committed code deterministically selects this batch.

Two qualifications remain:

1. The docstring says the rule is `int(SEED[:15],16)`, but the stored seed has only nine hex characters and the executable uses `int(SEED[:9],16)`. With the stored value these descriptions are extensionally equivalent—slicing it to 15 still returns all nine characters—so the result is unaffected. Still, the documentation should state plainly that the nine-character abbreviated SHA is the seed, rather than imply that fifteen committed digits were used.
2. Git cannot prove when a human read a source. It proves only that `b35_draw_batch4.py` was committed before the uncommitted/current B36 adjudication artifact. More importantly, the bibliography labels all three papers `READ 2026-08-23`, predating this draw. The draw can therefore be called preregistered before this **fresh batch adjudication**, but not blind in the literal sense that nobody had read or formed views on the papers. No repository predicate can establish that stronger claim.

This qualification does not alter which papers the committed code selects.

## 2. Entry 21: a real but internal and narrowly scoped exclusion

Appendix C supplies a derivation, not merely a stability expectation. Its domain is:

- first-order perturbations;
- spherically symmetric (radial) perturbations;
- about the paper's static equilibrium (4)–(7);
- with the special anisotropic-fluid equation of state `P_r = -rho c^2`.

Because the equilibrium has `rho c^2 + P_r = 0`, the first-order mixed stress-energy components vanish. The mixed Einstein equations (105) and (106) then give `dot(delta lambda)=0`; the time continuity equation (108) gives `dot(delta rho)=0`. Within that linear radial sector, density and the radial metric component can only be static, so an unstable radial mode cannot develop.

That is a counterexample-refutable, source-owned claim-level exclusion. Its scope must not be inflated:

- it is not a nonlinear stability proof;
- it does not cover nonradial modes—the paper expressly permits them;
- it does not prove stability under arbitrary equations of state, matter perturbations, rotating perturbations, or formation histories;
- the later positive axial scattering potential supports axial-mode stability for the constructed solutions, while polar/axial isospectrality is imported from another paper in the ultrathin-shell limit;
- several broader stability statements in the discussion are expectations, not results.

At paper level, however, this is a property delimiting and supporting the constructed cosmological-black-hole spectrum. The operative contribution constructs an infinite family of regular de-Sitter-core/Schwarzschild-exterior solutions, derives their entropy and quasinormal modes, and points to LISA detectability. The radial no-mode result is not the paper's organising no-go. Under the same paper-level operative-contribution convention used for internal branch or parameter restrictions, entry 21 remains `PROSPECT`.

Suggested prose:

> For linear spherically symmetric perturbations about the paper's special `P_r=-rho c^2` static equilibria, Eqs. (105)–(108) force the density and radial metric perturbations to be time-independent, excluding unstable radial modes; this is not a general nonlinear or nonradial stability theorem.

## 3. Entry 39: classical pre-emption of a quantum bounce

Entry 39 is a constructive parameter calculation. For a closed homogeneous isotropic spin fluid it derives the torsion-bounce condition, evaluates the bounce density and minimum scale factor, and compares the result with the Planck regime.

Its quantum-bounce sentence is conditional. If sufficiently many extra fermionic degrees of freedom make the ECSK bounce occur below the Planck density, then contraction reverses before matter reaches the density at which an LQG bounce would occur. In that case LQG would not supply cosmological signatures. This is causal pre-emption inside the exhibited dynamics: once `a-dot=0` and contraction reverses at the lower threshold, the trajectory does not continue to a higher-density bounce.

It is not a general no-go against quantum-bounce models:

- for Standard Model degrees of freedom the paper obtains `epsilon_bb = 15.4 epsilon_Pl` and concedes that classical ECSK should then be replaced by quantum gravity;
- sub-Planckian pre-emption requires the conditional extra-fermion example;
- the alternative claim that spacetime remains classical above the Planck scale is motivated by gamma-ray observations, not derived;
- the paper does not quantify a class of all hybrid ECSK/LQG models or prove that none can retain quantum effects or signatures.

The statement is therefore a conditional mechanism comparison downstream of a constructed bounce, not the operative class-exclusion result demanded by the census rule. Entry 39 remains `CONSISTENCY-ONLY`.

## 4. Entry 11

Entry 11 constructs the homogeneous/isotropic spin-fluid dynamics with a phenomenological particle-production law. Its equations yield:

- a nonsingular torsion bounce for the adopted FLRW spin fluid;
- an oscillatory universe without particle production;
- a threshold `D > 2/(3 sqrt(Lambda))` for indefinite late expansion;
- a critical production coefficient separating cyclic, finite-inflation, and eternal-inflation behaviors.

These are conditions and branches internal to the construction, not a proof that no member of an externally specified model class can meet a target conjunction. The transition from a realistic black-hole interior to one closed universe is explicitly conjectural: the paper says it expects local bounces, conjectures wormhole merger, assumes homogeneity/isotropy for the calculation, and closes with “every black hole may create a new universe.” Its final “cannot be solved” sentence is a philosophical regress question, not a physical theorem.

Entry 11 remains `CONSISTENCY-ONLY`.

## 5. Predicate audit of `b36_census_batch4.py`

The script reports 4/4, but none of its predicates establishes the adjudication asserted in its label.

1. **Draw predicate:** `os.path.exists(.../b35_draw_batch4.py)` proves only that a path exists. It does not execute or import the draw, check the committed blob, validate either commit, verify pool order, seed a PRNG, or compare the output with `(39,21,11)`. A different or modified file at the same path would pass.
2. **Entry 39 predicate:** phrase presence for “prevents the formation of singularities” does not examine the derivation, the Standard Model result above Planck density, the extra-fermion condition, or the quantum-bounce pre-emption claim under attack.
3. **Entry 21 predicate:** finding “cannot develop unstable radial modes” verifies only a conclusion sentence. It does not encode the linear/radial/special-equilibrium domain, equations (105)–(108), the nonradial caveat, or the operative-contribution convention.
4. **Entry 11 predicate:** “may create a new universe” is useful evidence of tentative framing but cannot clear the equations elsewhere for hidden no-go content. It ignores the expansion threshold, critical `beta`, and conjectural bridge from generic collapse to FLRW dynamics.

The script does not read the bibliography, verify current tiers, implement the preregistered obstruction rule, or distinguish paper-level operative classification from claim-level restrictions. Its 4/4 is therefore not an adjudication test.

## Disposition

- Confirm `NOT-OBSTRUCTION` for entries 39, 21, and 11 at paper level.
- Make no tier changes.
- Preserve entry 21's narrow, source-owned linear radial-stability exclusion in prose.
- Accept `(39,21,11)` as the deterministic output of the committed B35 code.
- Replace “committed before the reads” with “committed before the B36 fresh adjudication”; the former is neither established by Git nor literally compatible with the bibliography's earlier-read records.
- Repair the B36 draw predicate so that it loads the committed rule or independently recomputes the two seeded samples and validates the ordered pools and commit identities.
