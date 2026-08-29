SCOPE_NARROWED_COUNT_AND_CELL

# C-gate verdict — B24

I read the complete pinned source, including the statements and proofs of Proposition 1, Proposition 2, and Theorem 1, the redshift-function extension, the flat/open completeness discussion, the escape-routes section, and the conclusions. The source has a usable text layer.

## Claim 1 — narrowed; eleven is not an honest count of independent conditions

All eleven strings selected by the script occur in Theorem 1's statement, but they are not eleven independent hypotheses.

- `no-shell` and `no independent shell stress tensor` express the same matching restriction at two levels.
- `fixed by the parent metric profile` substantially overlaps `no additional late-time bulk component`: both prevent an independent daughter contribution from changing the inherited Friedmann equation.
- `modified asymptotics` is not itself an assumed condition; the assumption is **no** modified asymptotics, already encoded by the asymptotically flat, finite-ADM parent at the late-time end.
- `Darmois` and `no-shell` are not independent here. The paper uses Darmois–Israel continuity precisely as its no-surface-layer matching.
- “nondegenerate comoving spherical Darmois boundary” is one compound boundary ansatz, which the script counts as one while separately splitting other compound assumptions. The granularity is inconsistent.

My count for the **closed-branch construction** is eight meaningful hypothesis groups:

1. a static parent;
2. spherical symmetry;
3. asymptotic flatness with finite positive ADM mass;
4. the one-function parent class in Theorem 1;
5. an FRW daughter;
6. a nondegenerate, comoving spherical boundary;
7. Darmois/no-shell matching; and
8. daughter evolution inherited from the parent, without an independent late-time bulk sector.

“No modified asymptotics” and “no independent shell stress tensor” state what must be changed to leave groups 3 and 7; they should not be counted again. Eight is a reasoned grouping, not a uniquely canonical number—one could split the compound geometry assumptions more finely—but eleven overstates independence.

There is also no single eleven-condition list governing every branch of Theorem 1. The flat/open limb invokes a different general result and requires a non-static, curvature-regular flat/open FRW spacetime with regular affine ends, plus the simultaneous demands of null completeness and ANEC consistency. The B24 count obscures this branch-specific logic.

## Propositions 1 and 2

### Proposition 1 is a separate, simpler obstruction

Proposition 1 does not use finite ADM mass, asymptotic flatness, a matching surface, a shell assumption, or a daughter matter prescription. For a one-function static spherical parent with a trapped interval, its natural spatial slices are `R × S²`, with unequal sectional curvatures, so the trapped region is Kantowski–Sachs rather than exact FRW. The additional calculation shows that equal directional Hubble rates would require the special form `|f(T)| = C²T²`, and even that is necessary rather than sufficient for FRW geometry.

This proposition rules out only the simplest identification—the trapped band **in its natural slicing** is already the FRW daughter. It does not rule out a separately matched daughter, another slicing without further proof, or a non-FRW cosmology. Within its stated target it is structurally broad and its proof is transparent.

### Proposition 2 is broader than the B24 framing suggests

Proposition 2 proves closed-daughter boundedness from the asymptotic relation `F(R) → 1`, finite ADM mass, a nondegenerate comoving closed-FRW boundary, and no-shell matching. Because `E = cos²ψ_b < 1`, the physical condition `Ṙ_b² = E − F(R_b) ≥ 0` fails at sufficiently large radius. Equivalently, the negative `A⁻²` curvature term eventually dominates the finite-mass `A⁻³` term.

This result is independent of the detailed regular core and is not confined to Bardeen. The paper also explains that the angular matching equation, and hence this large-`A` argument, survives a static redshift function. Proposition 2 is therefore less restricted than Theorem 1's headline one-function formulation. Its no-shell and finite-ADM/asymptotically-flat assumptions remain essential.

## Claim 2 — confirmed, with redundancy noted

The proposed exits are genuine, author-identified escape routes. Section V.4 and the conclusion expressly name modified asymptotics, independent shell stress, non-FRW or non-comoving evolution, and an additional smooth bulk component. A positive vacuum-energy component is given as the simplest late-time support for a closed daughter. These are not merely degenerate mathematical loopholes; shells, altered asymptotics, and added stress-energy are standard ingredients in serious daughter-universe constructions.

But the three phrases are not three additional independent exclusions. They are ways to abandon existing hypothesis groups: modified asymptotics abandons finite-ADM asymptotic flatness; shell stress abandons Darmois/no-shell matching; an added bulk component abandons inheritance from the parent profile. Calling them escape routes is right. Counting them again to inflate the hypothesis total is not.

For flat/open daughters, those three are not the complete escape list. The paper says an evasion must give up at least one of curvature regularity, null completeness, ANEC consistency, the FRW ansatz, or the flat/open curvature class.

## Claim 3 — confirmed, but “real but narrow” is unfairly pejorative

“Minimal” is doing real scope work in the title and is explicitly defined in the introduction. The paper repeatedly says that it does not exclude more elaborate black-hole-universe constructions.

That is normal mathematical rigor, not evidence of a weak theorem. Inside the minimal class, the results have substantial reach:

- Proposition 1 is independent of matching and asymptotics;
- Proposition 2 is independent of core type and extends beyond the one-function metric via the redshift analysis; and
- the flat/open limb is independent of the black-hole matching construction, conditional instead on the general completeness theorem's hypotheses.

The fair characterization is **“explicitly scope-bounded, with structurally broad results inside each stated branch,”** not “real but narrow.” The latter invites readers to mistake declared domain for a defect.

## Proposed warrant cell — refuted as written

The proposed cell

> SCOPE-LIMITED BY CONSTRUCTION — eleven stated conditions, three of them explicit exclusions; the author's own title says 'minimal'. Derivation not independently checked.

should not be used. It contains the inflated eleven-count, double-counts escape routes as independent restrictions, ignores Propositions 1 and 2's broader reach, and makes ordinary theorem hypotheses sound like adverse warrant evidence. “Derivation not independently checked” is honest, but scope is not a warrant defect unless the bibliography has advertised a broader conclusion than the source proves.

A defensible cell would be:

> **EXPLICITLY DOMAIN-BOUNDED —** Proposition 1 excludes identifying the natural trapped slicing with exact FRW; Proposition 2 bounds nondegenerate comoving no-shell closed-FRW daughters of static asymptotically flat finite-ADM parents; the flat/open limb additionally assumes curvature regularity, regular affine ends and ANEC. Shells, modified asymptotics, non-FRW/non-comoving evolution, or added bulk stress-energy are expressly outside the result. Proof skeleton checked against the source; external completeness theorem not independently verified.

That records the scope without calling it disputed or sound. Entry 22 remains `THEORETICAL-OBSTRUCTION`; no tier change follows.

## Israel-junction follow-up — false connection as presently framed

“Uses Israel junction conditions” does **not** mean “uses a shell.” Darmois–Israel junction theory covers both cases: a discontinuity in extrinsic curvature produces a surface stress tensor, while continuous first and second fundamental forms give a no-shell match. Easson's own minimal construction explicitly cites Israel and calls its conditions “Darmois–Israel no-shell conditions.”

The pinned Gaztañaga-series text makes the distinction decisive: after invoking Israel matching conditions, it says the joint metric has **“no surface terms in the junction.”** Therefore that series is not outside Easson's obstruction merely because it uses Israel formalism.

There may still be a worthwhile model-by-model comparison, but on different predicates: whether the parent is in the relevant static asymptotically flat finite-ADM class, whether the boundary is comoving and nondegenerate, whether the daughter is FRW, whether its evolution is inherited from the parent, and whether it carries vacuum energy or another bulk sector. The cited Gaztañaga construction includes a Λ/false-vacuum component, which is an author-named route outside the minimal inherited-source setup. No corpus-wide “Israel means shell” link should be recorded.

## Predicate audit

Whitespace normalization correctly fixes matching across wrapped lines, but `4/4` remains only a lexical check.

- Predicate 1 proves that ten selected strings occur in a 900-character window. It does not prove that they are independent conditions, restrictive rather than definitional, or the complete hypotheses of both theorem branches. Its list also strips the negation from “modified asymptotics.”
- Predicate 2 proves the three exclusions occur in one sentence. It does not establish their independence, seriousness, or effect on Propositions 1 and 2.
- Predicate 3 finds the title in the bibliography and the word `minimal` somewhere in the source. It does not prove what “minimal” means; the manual definition in the introduction does.
- Predicate 4 verifies the bibliography's generic tier-definition sentence, not that entry 22 accurately states the theorem's domain.

No predicate reads either proposition, follows either proof, checks the flat/open assumptions, assesses the proposed warrant cell, or tests the Israel-series connection.

## Final rulings

- **Claim 1:** narrowed/refuted as a count. I find eight meaningful closed-construction hypothesis groups, not eleven independent conditions; the full theorem has branch-specific hypotheses.
- **Claim 2:** confirmed as escape routes, not as three extra independent conditions.
- **Claim 3:** confirmed that “minimal” scopes the result; refuted that this warrants a damning “real but narrow” gloss.
- **Proposed cell:** refuted and replaced above.
- **Israel follow-up:** false as framed; Israel formalism does not imply a shell, and the pinned series expressly claims no surface term.
