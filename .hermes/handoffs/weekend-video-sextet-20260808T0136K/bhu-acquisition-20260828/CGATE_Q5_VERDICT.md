Q5_IMPL_NARROWED_RECALL_AND_DOMAIN

# Question-5 implementation verdict

The tier change is substantively sound: entry 5 is properly classified as `THEORETICAL-OBSTRUCTION` under the corpus's adopted operative-contribution convention, while entry 17 remains `CONSISTENCY-ONLY`. The implementation should nevertheless be narrowed in two places. First, entry 5's domain should print the Pathria parameter and boundary assumptions more exactly. Second, “measured recall is 1 of 2” is only the screen's observed hit rate on the two **currently known and adjudicated** obstruction papers, not a validated estimate of corpus-wide recall.

I read Khakshournia's full pinned note, including its derivation and conclusion, rather than relying on the brief's quotations. I also reread entry 17's complete pinned paper for attack 3 and checked the current bibliography, Q5 closure, B30 split, B38 adjudication, and Q1 recall audit.

## 1. Attack 1 — does entry 5 construct a model of its own?

No, not in the sense that controls the paper-level tier convention.

The note begins with Pathria's pre-existing proposal: a pressureless, positively curved FRW universe with `0 <= Lambda <= Lambda_c`, at maximum expansion, is identified with the interior of a Schwarzschild black hole modified by the same cosmological constant. Khakshournia's stated question is whether that identification satisfies the null junction conditions. The paper does not introduce a new cosmology, solve new interior dynamics, advocate a shell-bearing universe as an alternative scenario, or explore the resulting shell model's evolution.

It does calculate a mathematically consistent **description of the required junction**: the induced metric and angular transverse-curvature components agree, the `uu` component does not, and the Barrabès–Israel surface tensor is a pressure-only null shell. In that limited sense AGATE_B30 was right that the paper determines the properties of the join. But this does not turn the note into the entry-37 shape. The shell is the consequence of the attempted Pathria match, not an independently developed construction around which a subsidiary exclusion is drawn.

The conclusion is decisive. It says that, as a result of the matching conditions, the expansion-to-contraction transition at the Schwarzschild event horizon “can only be done through a null shell” with surface pressure. It does not endorse that shell as a developed cosmological model. The note-added discussion likewise contrasts Knutsen's timelike critique with this paper's null-horizon calculation; it does not claim to have rescued or constructed a new universe model.

Thus the operative result is precisely the exclusion of the desired conjunction:

`Pathria setup + null horizon identification + smooth/shell-free match`.

The paper owns the calculation, and one smooth counterexample within the same fixed assumptions would refute its result. On the adopted shape-not-rank convention, `THEORETICAL-OBSTRUCTION` is correct.

This must not be inflated into “the Pathria universe cannot exist.” The shell-bearing match remains available, and the paper does not exclude other hypersurfaces, matter models, interiors, exteriors, or BHU constructions.

## 2. Attack 2 — exact scope and derivation

The implemented domain note is directionally correct but should be more exact.

### Assumptions actually used

The calculation assumes:

- a homogeneous, pressureless, closed (`k=+1`) FRW interior;
- Pathria's range `0 <= Lambda <= Lambda_c`, for which the maximum radius and black-hole horizon used in the proposal exist;
- a vacuum Schwarzschild–de Sitter exterior with the **same** `Lambda`, written in the note as a Schwarzschild metric modified by the cosmological constant;
- the Pathria identification of the FRW maximum-expansion radius with the exterior event-horizon radius;
- a null matching hypersurface `Sigma` at that identification;
- the maximum-expansion/equatorial evaluation `chi=pi/2`; and
- the mass relation for the dust interior, `M=(4 pi/3) rho r^3|_Sigma`.

The notation “Schwarzschild(-Lambda)” is understandable shorthand, but “Schwarzschild–de Sitter with the same `Lambda`” is more precise. The current note also leaves the allowed `Lambda` range, `chi=pi/2`, and mass identification implicit. They matter because the source is not a theorem about arbitrary closed-FRW/vacuum null junctions.

### What is proved

Continuity of the induced metric yields equation (7). The transverse curvature then satisfies

`K_theta theta^- = K_theta theta^+ = r|_Sigma`,

while equations (14) and (16) give

`K_uu^- = -(1/2) f_,r + 2 pi rho a`,

`K_uu^+ = -(1/2) f_,r`.

Therefore `[K_uu]` is nonzero. Under the Barrabès–Israel null-shell formalism this entails a shell with zero surface energy density and nonzero surface pressure

`p = -(1/8 pi)[K_uu] = rho a/4 |_Sigma`.

So the existing statements that the `uu` component jumps, smooth shell-free matching is excluded, and the required surface pressure is computed are all supported. A slightly better final domain statement is:

> For Pathria's pressureless closed-FRW interior with `0 <= Lambda <= Lambda_c`, joined at its equatorial maximum-expansion surface (`chi=pi/2`) identified with the horizon of a Schwarzschild–de Sitter exterior carrying the same `Lambda` and the stated dust-mass relation, the Barrabès–Israel null junction is not smooth: `[K_uu] != 0`. The junction therefore carries a pressure-only null shell, `p=rho a/4`. This does not exclude shell-bearing realizations or other FRW/black-hole junction classes.

That is a narrowing of the printed domain, not a reversal of the tier.

## 3. Attack 3 — lattice consistency, ruled explicitly

### Entry 17 does **not** move

Entry 17 has a closely analogous claim-level result, but a different paper-level operative contribution.

Chakrabarty et al. assume a quantum-corrected collapsing homogeneous interior and a classical Schwarzschild exterior. Their first fundamental forms can be matched, but their calculated second fundamental forms differ; within that fixed ansatz a delta-like boundary stress tensor is required. Their later cases likewise show that different-mass Schwarzschild regions require a massive layer, that the Schwarzschild/de Sitter match is generally nonsmooth away from `R_0=2M`, and that a separate interpolating semiclassical geometry is needed for the third continuation.

Those are real, source-owned exclusions and should remain in the claim-level prose. But the paper's abstract announces a dynamical toy model; its body constructs the collapsing-to-expanding match, develops three continuation geometries, calculates apparent horizons, and its conclusion again says “we constructed a dynamical model.” The layer/interpolating-region necessities delimit and repair that construction. This is exactly the constructive-family side of the adopted entry-37 line.

Accordingly:

- entry 5: **move/retain `THEORETICAL-OBSTRUCTION`** because testing and excluding the smooth Pathria identification is the note's operative result;
- entry 17: **retain `CONSISTENCY-ONLY`** because the junction exclusion is internal to the paper's operative baby-universe construction.

The Q5 ruling therefore does not drag entry 17 with it. This is not a distinction between “important” and “unimportant” mathematics; it is a distinction in paper-level logical role under the one-label convention.

### Other lattice cases

The same rule remains coherent for the already adjudicated cases:

- entry 37 constructs an exact shock family; its subluminality bound partitions that family;
- entries 52/53 construct closed EC bounce/cycle scenarios; their existence inequalities are strong claim-level exclusions but remain subsidiary under the fixed Q7 disposition;
- entry 22 is organized around no-go results and therefore remains an obstruction;
- entry 49 does not own the cited proof and cannot receive the tier by citation alone.

Entry 4, Knutsen's critical Pathria re-examination, is the obvious unresolved comparison. Its current bibliography record is only a characterization and says it still needs a due-diligence read. Q5 cannot promote it second-hand, but the new entry-5 disposition makes entry 4 a priority tier-audit candidate. If its own operative contribution and derivation exclude a junction/model class, it may presently be misfiled. That is an acquisition/audit obligation, not evidence for moving it without the source.

## 4. Attack 4 — recall consequence

The raw arithmetic is correct on the current adjudicated labels:

- currently known obstruction papers: entries 22 and 5 (`2`);
- screen-flagged among them: entry 22 (`1`);
- screen-unflagged among them: entry 5 (`1`);
- observed hit fraction: `1/2 = 50%`.

But “the screen's measured recall now stands at one of two” overstates what this denominator establishes. The two positives are the **currently discovered/adjudicated** obstructions, not an independently established complete set of all corpus obstructions. Entry 5 entered the denominator because the random negative-pile audit found it; unread and unlocated papers remain, and entry 4 is an explicit unaudited critical candidate. The estimate is also extremely small-sample and discovery-conditioned.

The defensible wording is:

> Among the two papers currently adjudicated as `THEORETICAL-OBSTRUCTION`, the screen flagged one and missed one: observed recall on known positives is `1/2`. This demonstrates at least one false negative and ratifies Q1's recall concern; it is not a validated estimate or lower bound for corpus-wide recall.

Calling it “measured recall” is acceptable only with that qualification. It must not be presented as proof that the screen's true recall is 50% or that the obstruction census is complete.

## 5. Attack 5 — stale state and arithmetic

The headline class tally is internally arithmetically correct:

`4 + 7 + 3 + 31 + 2 + 4 = 51`.

The obstruction members are correctly named as entries 22 and 5. Moving entry 5 from the immediately preceding state reduces `CONSISTENCY-ONLY` by one and increases `THEORETICAL-OBSTRUCTION` by one. The Q5 closure is marked closed, and entry 5 points back to the ruling.

Remaining defects:

1. Replace the unqualified “measured recall stands at 1 of 2” in both the bibliography and Q5 closure with “observed recall on the two currently adjudicated positives is 1 of 2.”
2. Expand entry 5's domain with the `Lambda` range, same-`Lambda` Schwarzschild–de Sitter exterior, equatorial `chi=pi/2` evaluation, and stated mass relation; record zero surface energy density and `p=rho a/4` if space permits.
3. Do not say the note excludes Pathria's shell-bearing model. It excludes the smooth, shell-free form of the stipulated identification and calculates the shell that would be required.
4. Queue entry 4 for a source-based paper-level tier audit. Do not change it before that read.
5. The Q5 closure says questions 6 and 7 “matured” the rule. That is acceptable as a retrospective synthesis, but Q6's claimed generic priority precedent was refuted by `CGATE_Q6_VERDICT.md`, and Q7's original threshold characterization was refuted by `CGATE_Q7_VERDICT.md`. The operative-contribution convention should be cited directly rather than relying on either closure's corrected factual premise.

## Final ruling

The first delegated, seat-split tier change survives the hard check. Entry 5 owns a narrow theoretical obstruction and is not a constructive-family paper in the sense relevant to entries 17, 37, 52, and 53. Attack 3 is expressly rejected as a reason to move entry 17. The implementation is narrowed only because its domain can be made materially more exact and its recall statement currently claims more statistical authority than two discovery-conditioned positives support.
