MISSRATE_REFUTED_THREE_MISSES_IN_SAMPLE

# B29 adversarial verdict

**I re-read all eleven sampled papers from their pinned full texts.** Against the rule fixed in B28, the zero-miss adjudication is false. Entries **5 and 37 are clear theoretical obstructions**, and entry **49 contains the expressly targeted singularity obstruction**, though it delegates the full proof to the companion Farhi–Guth paper. On the rule as written, all three count as misses. The observed result is therefore **3 misses in 11**, not zero.

## 1. Independent adjudication of the eleven

I applied only the fixed rule:

> Does the paper prove that no member of a specified model class can satisfy a specified conjunction of conditions, with a counterexample in that domain as the refutation and not an observation?

I distinguished a genuine model-space exclusion from (a) an observational falsifier, (b) causal/technical uses of “cannot,” (c) a constructive existence result, and (d) an internal uniqueness step with no model-class exclusion.

| entry | independent verdict | source-level reason |
|---:|---|---|
| 5 | **OBSTRUCTION — MISS** | The paper formulates the class of pressureless closed-FRW interiors joined to Schwarzschild exteriors at the horizon/maximal-expansion null hypersurface, computes the jump in transverse extrinsic curvature, and concludes that the transition **can only** occur through a null shell with surface pressure. Thus no member of the stated junction setup has a smooth, shell-free matching. A smooth counterexample in that domain would refute it; no measurement is involved. This is the paper's central result, not an incidental word count. |
| 7 | **not an obstruction** | Brown, Lee, and Rho give neutron-star measurements that would falsify the Brown–Bethe/VM/kaon-condensation/CNS chain. The refutation condition is observational by design, so the fixed rule excludes it. |
| 10 | **not an obstruction** | Popławski derives a cusp-like nonsingular bounce in a closed homogeneous ECSK universe with Dirac matter. “Averts the singularity” is the property of the constructed solution/mechanism, not a paper-level no-go against a class of candidate models satisfying a desired conjunction. Reading every constructive avoidance mechanism as an obstruction would collapse the tier boundary. |
| 24 | **not an obstruction** | The paper constructs an outside-universe junction and argues incoming signals can leave CMB imprints. Statements that outgoing null rays cannot cross an event horizon are causal properties inside the construction, not a no-go over a model class. |
| 27 | **not an obstruction** | This is a BHU collapse/bounce review with constructive model advocacy and observational comparisons. It does not prove a class-wide incompatibility meeting the fixed rule. Shared impossibility vocabulary is not enough. |
| 36 | **not an obstruction** | Smoller and Temple construct an exact shock-wave cosmology and prove existence/uniqueness and physical bounds for its ODE solutions. Internal phase-plane statements such as two critical orbits being impossible are proof steps, not an exclusion of a cosmological model class under a stated physical conjunction. |
| 37 | **OBSTRUCTION — MISS** | The constructive framing does not erase explicit model-space theorems. The paper proves that its exact shock is everywhere subluminal **if and only if** `σ ≤ 1/3`; Theorem 3 gives zero, infinite, or light speed at the Big Bang according as `σ<1/3`, `σ>1/3`, or `σ=1/3`. Therefore no member of the stated exact shock family with `σ>1/3` can satisfy the everywhere-subluminal condition. It also derives that a classical TOV match beyond one Hubble length is impossible without continuing into a black hole. A `σ>1/3` everywhere-subluminal solution in the stated family would be a theoretical counterexample. This squarely satisfies the fixed rule even though the paper also constructs the allowed region. |
| 40 | **not an obstruction** | The paper constructs a collapsing spin-fluid model in which torsion and particle production generate a bounce, inflation, and later expansion. Under the tier's paper-level distinction, “torsion prevents a singularity” describes the constructed mechanism, not an obstruction paper. Its assumptions (no shear in the initial demonstration; phenomenological particle production to beat shear later) further prevent reading it as an unconditional class-wide no-go. |
| 46 | **not an obstruction** | Alfonso-Faus applies Bohr quantization to the universe and derives an information/entropy number. It constructs a quantization analogy and excludes no model class. |
| 49 | **OBSTRUCTION RESULT PRESENT — MISS under the fixed rule** | Blau, Guendelman, and Guth do much more than list bubble trajectories. In the discussion they state that every exact inflationary-bubble solution considered begins at an initial singularity and that, under exact spherical symmetry and the weak energy condition, **“the initial singularity cannot be avoided.”** They identify the proof method—the Penrose theorem—and explain the physical reason. Quantum violation of the weak energy condition is then named as the escape. This gives the required domain, impossibility, and evasion/counterexample structure. The detailed proof is cited to the companion Farhi–Guth paper (entry 48), so entry 49 should not be represented as the canonical proof source; nevertheless the obstruction result is unequivocally in this paper, contrary to B29's claim that its impossibility language consists only of technical asides. Under the audit's wording—“does the paper prove”—its application of the Penrose theorem counts. Under a stricter “full proof printed here” convention it would be a cited obstruction rather than a miss, but that convention was not preregistered. |
| 56 | **not an obstruction** | Gaztañaga says infinite-extent ΛCDM is inconsistent with the **observed** acceleration unless dark energy/Λ is supplied, then advocates a finite-mass BHU. The critique is conditional on measurement and the paper's operative contribution is constructive. It therefore fails the rule's “not by any measurement” limb. |

### Minimum result robust to the entry-49 proof-location issue

Even if entry 49 is excluded under a newly narrowed “full proof must appear in this document” convention, entries **5 and 37 remain two source-contained misses**. Zero is untenable either way. The qualitative result changes exactly as the brief warns.

### Why entries 10 and 40 are not counted while entries 5 and 37 are

There is a genuine duality problem: proving a bounce can be phrased as proving no singularity, and constructing allowed solutions can accompany a theorem excluding other parameter regions. The stable boundary is the fixed rule's **model-class/conjunction** structure:

- Entries 10 and 40 establish a mechanism and exhibit its outcome; their “prevents” language is constructive.
- Entry 5 establishes the impossibility of smooth matching throughout its stated junction class.
- Entry 37 explicitly partitions a parameterized solution class and proves an `iff` exclusion of the `σ>1/3` region from the subluminal conjunction.

Without that boundary, virtually any existence/uniqueness paper could be relabeled an obstruction by negating its result.

## 2. Frame audit

B28's frozen frame has 31 entries after excluding flags 6, 22, and 25 from a 34-paper readable set. Unlike the earlier broken inventory, its explicit readable list already **includes entry 41 and excludes entry 1**, which are the two identities CGATE B27 found swapped by the title matcher. Thus the B27 correction changes the provenance explanation but not B28's explicit 34-paper set or its 31-paper unflagged frame.

The deterministic draw also reproduces exactly from the stated seed:

```text
[5, 7, 10, 24, 27, 36, 37, 40, 46, 49, 56]
```

The frame is therefore usable for this finite audit, subject to two qualifications:

1. “Unflagged” is relative to the frozen B1 implementation and paper-level labels, not an independently complete corpus truth.
2. Readability remains a current-repository state; later acquisitions enlarge the population to which any operational screen would be applied.

Neither qualification rescues B29's zero labels.

## 3. Hypergeometric calculation and statement

Conditional on `N=31`, `n=11`, and **zero** observed misses, B29's probability calculation is arithmetically correct:

```text
P(X=0 | K misses) = C(31-K, 11) / C(31, 11)
```

`P0(6)=5.3%` and `P0(7)<5%`, so inversion gives the conventional exact one-sided 95% upper confidence limit `K≤6`. Two wording corrections would still be needed even in that counterfactual:

- `6/31 = 19.35%`, so “below 19%” is false; say “at most 19.4%” or “approximately 19%.”
- A confidence bound is not a 95% posterior probability that the realized finite population literally contains at most six misses.

But the conditioning event is false. With the rule-bound adjudication above, `X=3`, so the zero-event bound cannot be reported. For orientation only, exact one-sided inversion using `P(X≤3 | K)` gives an upper limit of **16/31 (51.6%)**; the hypergeometric likelihood is maximized near **8/31**. If entry 49 is conservatively excluded and `X=2`, the corresponding upper limit is **13/31 (41.9%)**, with the likelihood maximized near **5/31**. Either result leaves a gross miss rate open rather than excluding it.

## 4. Weight of the finding

B29's intended caution about a clean sample would have been appropriate: zero in eleven could exclude a very high miss prevalence while leaving rare misses plausible. It neither over- nor under-hedges that hypothetical by much.

The actual reread reverses the result. Two source-contained misses—and a third obstruction result explicitly present—are direct evidence that the screen leaks at a consequential rate on this draw. This does not prove the exact corpus-wide recall is poor, but it destroys the proposed evidentiary basis for treating screening alone as a safe shortlist. Hand verification of flags still cannot repair these false negatives.

## 5. The “free observation” is refuted

The claim that ten sampled papers are constructive, one is a measurement falsifier, and none proves an impossibility is factually wrong after source reading. Entry 5 is centrally a matching obstruction; entry 37 includes an explicit parameter-space no-go theorem; entry 49 states the laboratory-creation singularity obstruction.

Even had the labels been zero, eleven papers sampled from the **unflagged** stratum cannot establish that the full literature has approximately one obstruction. The sample is conditional on what the screen did not flag, and “consistent with one” is not evidence that one is the true prevalence. The proposed story confuses a compatibility statement with an estimate and should be deleted.

## 6. Predicate audit

B29 never opens or scores any of the eleven source files. Its scientific result is hardcoded:

```python
N, n, found = 31, 11, 0
```

The docstring supplies all eleven adjudications, with no executable connection to their texts.

### Check 1

The predicate is only `k95 >= 5`. It does not check:

- that `k95 == 6`;
- that zero misses were actually found;
- any paper classification;
- that the result “excludes a gross rate”; or
- the correctness of the percentage wording.

It would pass for many unrelated or erroneous bounds.

### Check 2

The predicate `True is (found == 0)` merely rechecks the literal zero assigned three lines above. It does not inspect git history, verify commit `932250d2c`, reproduce B28's sample, establish that reading occurred after commitment, or test blinding. I verified separately that commit `932250d2c` exists and contains only the preregistration file, but B29's predicate does not.

### Missing predicates

There is no check for:

- equality between B28's frame/sample and B29's constants;
- source existence and identity for all eleven;
- independent adjudication or reviewer blinding;
- the fixed rule being applied consistently;
- the fact that entry 49 contains the singularity theorem passage;
- the exact upper-bound boundary `P0(6)≥0.05>P0(7)`.

Thus `2/2` validates a combinatorial calculation conditional on a hardcoded outcome, not the outcome.

## Disposition

Withdraw “zero misses in eleven,” the 6-of-31/19% bound, the claim that gross recall failure is excluded, and the literature-prevalence story. Record the sample as:

> Independent reread: entries 5 and 37 are definite misses under the preregistered rule; entry 49 contains the targeted singularity obstruction and counts as a third under the rule as written, with the full proof located in the companion Farhi–Guth paper. The screen therefore missed substantive obstruction material in the random unflagged sample.
