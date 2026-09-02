AUDIT_HOLDS_THEORETICAL_OBSTRUCTION

# Entry 4 deep audit — Codex seat

## 1. Matching conditions

Knutsen explicitly sets out to obtain the “sufficient and necessary conditions for smooth matching” of an FLRW perfect-fluid interior to a vacuum exterior (lines 516–525). The paper does not name the formalism Darmois, Israel, or Lichnerowicz. Operationally it uses the Darmois conditions: equality of the first fundamental forms (induced metrics) and equality of the second fundamental forms (extrinsic curvatures). It follows the procedure of Santos [10], also used by Bonnor et al. [11] (lines 518–525), and uses a unit-normal formula attributed to Bonnor and Vickers [12] (lines 695–719).

For the first fundamental form, the paper requires the same metric induced on the boundary from each side (lines 603–606), giving in particular

> `A(t) = a(t) r_b = R_b(T)`

(Eq. 22, lines 603–642), together with the time-coordinate relation Eq. 23 and the assumption that exterior `T` remains timelike, Eq. 24 (lines 644–689). It then calculates the extrinsic curvatures and imposes `K^-_{theta theta}=K^+_{theta theta}` and `K^-_{tt}=K^+_{tt}` (lines 790–820, 910–959). Combining those conditions with the FLRW field equation, it derives—not merely cites—that smooth matching is possible only if pressure vanishes at the surface (lines 966–1016). Because FLRW pressure is spatially homogeneous, surface pressure zero makes `p=0` identically, so the interior is dust (lines 1018–1020). Thus pressure zero is a derived physical consequence of the smooth matching in this setup.

## 2. Application to Pathria's `r_b = 1`

The crucial step is displayed algebra, followed by a short interpretation. Equality of the angular extrinsic curvatures gives Eq. 36,

> `dot T B = sqrt(1-r^2)`, with `B = 1 - 2m/R - (Lambda/3)R^2`

(lines 806–815 and 910–936). Therefore `r_b=1` makes the right-hand side zero, and the paper writes the resulting equation explicitly as Eq. 44:

> `1 - 2m/R_b(T) - (Lambda/3) R_b^2(T) = 0.`

(lines 1063–1082). This is the exterior horizon equation. Since `m` and `Lambda` are constants, `R_b(T)` is fixed at a root of that equation; with Eq. 22, `R_b=a r_b`, the boundary radius and hence `a` are static. Knutsen then states that the sphere is static, its surface merges with its event horizon, and “this particular model cannot describe our expanding universe” (lines 1084–1088). So the horizon equation is displayed; the final static inference is stated in words but follows directly from the displayed equation plus constant `m`, constant `Lambda`, and Eq. 22.

There is a coordinate subtlety: the derivation earlier assumes `T` is timelike (lines 652–689), whereas Eq. 44 places the boundary where the static exterior coordinate degenerates. This makes the limiting horizon interpretation delicate, but it does not reverse the obstruction: the assumed smooth timelike expanding boundary cannot persist at `r_b=1`.

## 3. Domain

The stamped domain is essentially exact.

- **Perfect fluid / FLRW:** required. The paper begins the junction section with an FLRW perfect-fluid interior (lines 516–523), and spatial homogeneity is what promotes boundary pressure zero to dust everywhere (lines 1013–1020).
- **Vacuum exterior:** required. The exterior is the false-vacuum Schwarzschild–(anti-)de Sitter/Kottler metric, with `Lambda` explicitly retained (lines 250–289), not only asymptotically flat Schwarzschild. Thus `Lambda != 0` is not an escape from the paper's result; it is already covered by Eq. 44.
- **Smoothness / no surface layer:** required. The stated target is smooth matching (lines 518–525), implemented by equality of both fundamental forms. The paper does not analyze Israel surface stress, shells, or null shells, so shell-bearing junctions remain outside the proof.
- **Specific boundary:** the static-horizon no-go depends on Pathria's `r_b=1`. The paper expressly calls it “this choice” and “this particular model” (lines 1063–1088). It does not rule out other `r_b`; indeed it says it has no objection to FLRW modeling of contracting spheres or matter distributions expanding into false vacuum when the surface remains outside the horizon (lines 491–504).
- **Closed-universe interpretation:** also material. After `r=sin psi`, `r_b=1` is the maximum-area equator enclosing only half the closed universe; this is where an isolated sphere in empty space and a closed Friedmann universe part ways (lines 1089–1125). The paper adds that there is no external platform for a distant observer and calls the global mass concept meaningless (lines 1127–1136).

The rhetoric is broader than the theorem. The abstract says “this interpretation is wrong” and “our expanding universe cannot be inside the event horizon of the vacuum metric” (lines 9–15), and the conclusion calls Pathria's model confused (lines 1140–1145). But the actual derivation supports the narrower stamped proposition: a smooth FLRW perfect-fluid/false-vacuum junction at Pathria's `r_b=1` collapses to a static horizon boundary. It does not establish that no universe can ever be described as a black hole under all matter models, junction types, or boundary choices.

## 4. Ownership of proof

The operative no-go is proved in this paper. Knutsen cites Santos and Bonnor et al. for the matching procedure and Bonnor–Vickers for the normal formula (lines 518–525 and 695–719), but carries out the induced-metric and extrinsic-curvature calculation through Eqs. 22–44. In particular, it derives surface pressure zero (lines 1009–1020), confirms the mass relation (lines 1022–1055), and applies `r_b=1` to obtain the horizon equation and static conclusion (lines 1063–1088). It is not presented as a restatement of a cited no-go theorem.

## 5. Relation to entry 5 and entry 1

On the characterizations supplied in the audit brief, entry 5's null-shell result at maximum expansion is **consistent and adjacent, but not the same proof**. Knutsen assumes a smooth junction, uses timelike-boundary induced/extrinsic curvature conditions, and leaves surface layers untreated. A null-shell analysis addresses precisely a junction class beyond this proof, so it can refine what occurs when smooth matching fails without contradicting Knutsen's restricted obstruction.

Entry 1's FIRED standing is **independent of this derivation** on the permitted evidence. This source neither identifies entry 1 nor supplies evidence bearing on its standing. Knutsen does, however, warn against promoting Pathria's mathematical analogy into a global universe-as-black-hole claim (lines 1140–1145), which is consistent with keeping this entry's negative result tightly domain-stamped rather than using it to alter a separate entry's status.

## 6. Tier consequence

**THEORETICAL-OBSTRUCTION holds with the stamped domain.** The operative exclusion is derived: under an FLRW perfect-fluid interior, a smooth matching to a false-vacuum exterior forces dust, and Pathria's `r_b=1` forces the boundary onto a fixed exterior horizon, so that particular construction cannot represent an expanding universe. `DOMAIN_WIDER` is inappropriate because shells, non-FLRW/non-perfect-fluid interiors, and other boundary choices are not excluded. `DOMAIN_NARROWER` is also inappropriate: the stamp already names the decisive assumptions, and its “vacuum exterior” may include the cosmological-constant vacuum actually used by Knutsen. This is not merely `CONSISTENCY-ONLY`, because the exclusion itself—not just a consistency check—is the paper's operative derived result.

In plain language: Knutsen does not prove that every possible “universe as a black hole” idea is impossible. He proves that Pathria's particular clean gluing does not work as an expanding-universe model. If a homogeneous perfect-fluid FLRW region is joined smoothly to the paper's vacuum exterior, the fluid must be dust; and if Pathria's special boundary `r_b=1` is chosen, that boundary sits at a fixed horizon, making the sphere static. Different boundaries or junctions carrying a shell are separate cases, so the existing narrow theoretical-obstruction label is the right one.
