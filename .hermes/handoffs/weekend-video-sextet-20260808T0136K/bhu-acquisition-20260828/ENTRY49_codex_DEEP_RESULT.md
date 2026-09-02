AUDIT_HOLDS_CONSISTENCY_ONLY

## 1. Construction

The model is an exactly spherically symmetric false-vacuum interior joined across a timelike thin wall to a zero-cosmological-constant, asymptotically Schwarzschild exterior. The assumptions are explicit: spherical symmetry and a wall whose thickness is negligible relative to every other scale and whose scalar profile has relaxed to equilibrium (lines 127–140); regularity at the interior center selects de Sitter, while Birkhoff's theorem selects Schwarzschild outside, with `M` the mass measured at infinity (lines 149–158). The false vacuum has `T_{mu nu}=-rho_v g_{mu nu}`, the exterior has zero bulk stress, and the wall is a delta-function source (lines 251–264). The scalar-wall argument gives surface tension equal to surface energy density, `S^{mu nu}=-sigma h^{mu nu}` (lines 527–575). Thus positivity of `rho_v` and `sigma`, the vacuum equations of state, regular center, thin wall, and selected initial trajectory are inputs—not observationally derived facts.

The junction law itself is derived from Einstein's equations. With the normal directed from de Sitter to Schwarzschild, continuity of the induced metric and integration through the wall give the Israel condition

`[K^i_j] = K^i_j(Schwarzschild)-K^i_j(de Sitter) = -4 pi G sigma delta^i_j`,

as developed at lines 388–450 and specialized at lines 1220–1234. Writing

`beta_S = epsilon_S sqrt(rdot^2 + 1 - 2GM/r)`,

`beta_D = epsilon_D sqrt(rdot^2 + 1 - chi^2 r^2)`,

where `chi^2=8 pi G rho_v/3`, the angular junction condition is

`beta_D - beta_S = 4 pi G sigma r = kappa r`, with `kappa=4 pi G sigma`.

The paper derives the sign choices geometrically from the wall's direction in the maximally extended Schwarzschild/de Sitter diagrams (lines 1270–1407), rather than discarding them when squaring; it explicitly checks that squaring introduces no spurious solutions (lines 1746–1759).

With `chi_+^2=chi^2+kappa^2`, `gamma=2kappa/chi_+`, `z^3=chi_+^2 r^3/(2GM)`, and a rescaled proper time, the wall equation becomes the one-dimensional energy problem

`(dz/dtau')^2 + V(z) = E`,

`V(z)=-(z^2 + gamma^2/z + 1/z^4)`,

with `E=-4kappa^2/[(2GM)^(2/3) chi_+^(8/3)]`. The reduction and the single-maximum structure of `V` are at lines 1563–1694 and 1621–1642.

The resulting exhaustive trajectory classes are:

- For `M<M_cr`, bounded solutions begin at `r=0`, expand to a turning point, and return to `r=0`; a separate bounce branch comes from infinite radius, reaches a minimum, and re-expands (lines 1781–1786).
- The bounded A branch is an ordinary black-hole solution; the higher-mass bounded B branch runs through the other Schwarzschild exterior and is a wormhole solution (lines 2106–2156).
- Bounce C/D branches can contain an inflationary region, but their assumed past is already at arbitrarily large radius (lines 2157–2217).
- For `M>M_cr`, monotonic E solutions begin at `r=0` and grow without bound (lines 2218–2219). Their inflating de Sitter part lies beyond the horizon; a late slice separates into an exterior black-hole spacetime and an isolated closed universe (lines 2233–2275, 2309–2319).

Initial data choose which allowed branch is realized. In particular, neither the effective potential nor the mass alone supplies a nonsingular laboratory preparation.

## 2. Critical masses

The physical inputs are `rho_v` (called `rho_0` in the OCR), `sigma`, and `G`, equivalently `chi^2=8 pi G rho_v/3` and `kappa=4 pi G sigma`. The potential has one maximum, and `M_cr` is defined by `E(M_cr)=V_max` (lines 1621–1697). It is the separatrix mass: below it there are two-turning-point families (bounded and bounce), while above it the zero-radius branch is monotonic (lines 1781–1786, 2218–2219). Therefore the careful statement is: `M_cr` is the minimum Schwarzschild mass for the classically monotonic, child-universe-producing trajectory that starts at zero radius; it is also the upper edge of the recollapsing bounded family. It is not a universal claim that every subcritical bubble recollapses, because the subcritical bounce family arrives from infinite radius.

The paper also defines `M_S` and `M_D`, where `beta_S` and `beta_D` change sign. These locate crossings between Kruskal/de Sitter diagram regions, not additional laboratory energy thresholds (lines 1860–1881, 1905–2006). Figure 5's caption states exactly that `M_cr` crosses the potential maximum, while `M_S` and `M_D` cross the respective beta-zero lines (lines 1995–2006).

One recomputation of the quoted characteristic scale is clean and independent of the OCR-damaged closed form for `M_cr`. The paper defines

`Mbar = (4 pi/3) rho_v chi^(-3)`.

Using `rho_v=3chi^2/(8 pi G)` gives

`Mbar = (4 pi/3)[3chi^2/(8 pi G)]chi^(-3) = 1/(2Gchi)`.

For the GUT choice in the paper, this is `3.1 x 10^28 GeV`. With `1 GeV/c^2 = 1.7827 x 10^-27 kg`,

`3.1 x 10^28 x 1.7827 x 10^-27 kg = 55.26 kg`,

which rounds to the stated `56 kg` (lines 1773–1779). For the physically expected `gamma ~ 10^-3`, the dimensionless factor in `M_cr/Mbar` tends to one, so the monotonic threshold is of this order (lines 1760–1779). This is an internal trajectory scale conditional on a GUT false vacuum and wall tension—not an empirically inferred mass.

## 3. “Indistinguishable” and the few-kilograms argument

The direct statement occurs in the type-C discussion. After false-vacuum decay and reheating, the interior becomes a huge spacetime region “indistinguishable by local measurements from a flat Friedmann-Robertson-Walker universe” (lines 2203–2211). For the monotonic E solution, the late closed universe contains a de Sitter region that can inflate into the FRW universe observed today (lines 2309–2319), and the conclusion again says that the false-vacuum part decays into thermal radiation and behaves as a standard FRW universe (lines 2417–2427).

This is a derived causal/geometric consequence within the assumed model: the exterior measures only Schwarzschild `M`, while the interior false-vacuum volume can grow exponentially without expanding outward into the exterior (lines 2320–2340). Thus a roughly `56 kg` exterior mass scale can coexist with an enormous reheated interior; it does not mean that the interior's extensive energy is available to, or measured by, the parent exterior. The closed universe is causally disconnected: its observer can neither travel nor signal back to exterior region I (lines 2431–2446).

## 4. Observation-facing content

There is no calibrated observational test that our universe was produced this way: no predicted relic abundance, no present remnant mass distribution, no sky signature, and no likelihood tied to data. The paper conditionally discusses chaotic early-universe regions and says that, if this idealized model is indicative, the parent exterior sees a black hole while inflation occurs in a causally disconnected region (lines 2385–2410). Its closest “our universe” language is the model-dependent statement that the child de Sitter region might produce today's FRW universe (lines 2309–2319), not a discriminator between this origin and ordinary inflation.

The special `M=0` discussion likewise rejects a straightforward observational inference: if we are in region III a wall accelerates away from us; if in region I it is completely or causally disconnected (lines 3358–3375). That supplies no specified observable.

The laboratory question is answered classically in the negative under the stated assumptions. Every exact inflationary solution begins with an initial singularity; in exact spherical symmetry, with the weak energy condition, the Penrose theorem shows it cannot be avoided (lines 2522–2556). Quantum tunnelling is then proposed precisely because quantum fluctuations can violate that condition, but the paper calls the process conceivable, hypothetical, and “a matter of speculation” (lines 2557–2585). Moreover, its own footnote calls the laboratory question academic because the required energy—about `10^28 GeV`, the monotonic scale—is “totally inaccessible” (lines 3428–3469). The classical obstruction is operative context shared with the companion Farhi–Guth theorem, not an observation-facing result newly calibrated here.

## 5. Tier consequence

**CONSISTENCY-ONLY holds.** The paper's durable result is a mathematically derived consistency construction: under spherical symmetry, thin-wall dynamics, positive false-vacuum density/tension, and chosen singular or bounce initial data, general relativity permits an inflating child universe hidden behind a horizon and locally FRW after reheating. Its mass scales classify internal trajectories. No measured quantity is fitted, no accessible creation threshold is supplied, and no observation of our universe is predicted that would distinguish this history. The classical singularity/no-laboratory result is a genuine theorem-conditioned exclusion, but the paper itself frames laboratory production as a separate question and cites the companion proof; promoting this entry to THEORETICAL-OBSTRUCTION would make that adjacent no-go, rather than this entry's operative trajectory result, own the tier. The quantum route remains speculation, so it does not reach PROSPECT.

In plain language: the paper shows consistently how a small-looking black hole can hide an enormous inflating universe on the other side of a horizon, and it carefully maps which idealized bubbles collapse, bounce, or disconnect. It does not show that our universe began this way, offer a signal by which we could tell, or provide an accessible recipe for making one. The few-dozen-kilogram number labels the outside mass in a GUT-scale model; it is not a claim that a usable universe can be manufactured from a suitcase of matter.
