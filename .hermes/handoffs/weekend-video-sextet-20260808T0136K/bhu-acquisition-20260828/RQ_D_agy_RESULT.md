# RQ-D Easson Obstruction Map

## 1. The Map

| entry | KILLS / RESTRICTS / SPARES | deciding Easson clause (Prop1/Prop2/Thm1) | deciding interior property | source receipt (quote + file) |
|---|---|---|---|---|
| **11** | **SPARES** | Sec. V.4 escape / Theorem 1 (added bulk stress) | Bounces via Einstein-Cartan torsion (spin-fluid repulsion) acting as a bulk stress. | **Easson `2606.25023`**: "...an additional smooth bulk component whose density redshifts no faster than $A^{-2}$."<br>**Popławski 2016 `1410.3881`**: "Gravitational repulsion induced by spin and torsion... prevents singularities..." |
| **18** | **RESTRICTS** | Proposition 1 | The interior is simply the trapped region of a one-function static metric, which is anisotropic. | **Easson `2606.25023`**: "Proposition 1... the trapped interior is not an exact FRW cosmology in its natural slicing."<br>**Dymnikova 1992 `gr-qc/0201058`**: "A static spherically symmetric line element can be written in the standard form" |
| **19** | **SPARES** | Sec. V.4 escape (shell) / Missing hypothesis (classical matching) | The classical models reviewed use thin shells; her smooth model creates a universe via non-classical quantum tunneling. | **Easson `2606.25023`**: "...an independent shell stress tensor..."<br>**Dymnikova 2019 `universe5050111`**: "...direct matching of the Schwarzschild and the de Sitter metrics using the thin shell approach..." |
| **20** | **SPARES** | Sec. V.4 escape (non-FRW geometry) | The expanding "black universe" interior is an anisotropic Kantowski-Sachs cosmology. | **Easson `2606.25023`**: "...a non-FRW or non-comoving daughter geometry..."<br>**Bronnikov 2007 `gr-qc/0611022`**: "...nonstatic, homogeneous (T) regions whose geometry is that of a Kantowski-Sachs anisotropic..." |
| **21** | **SPARES** | Sec. V.4 escape (shell) | Employs an anisotropic pressure fluid shell to fuse the horizons. | **Easson `2606.25023`**: "...an independent shell stress tensor..."<br>**Roupas 2022 `2203.13295`**: "...assuming quantum indeterminacy of the localization of the horizon, which behaves as an anisotropic fluid shell." |
| **25** | **SPARES** | Theorem 1 / Sec. V.4 escape (non-comoving boundary) | The matching boundary is dynamic and non-comoving with the FLRW fluid. | **Easson `2606.25023`**: "Attach an FRW daughter across a nondegenerate comoving spherical Darmois boundary."<br>**Gaztañaga 2022 `2505.23877`**: "...the radius of the junction is no longer a fixed comoving radial coordinate but evolves dynamically, i.e., $\chi_* = \chi_*(\tau)$" |
| **26** | **SPARES** | Theorem 1 / Sec. V.4 escape (non-comoving boundary) | Same as 25 (non-comoving boundary). | Same as 25 |

## 2. Ownership-of-Proof Discipline & Verification
- **Entry 11:** The inclusion of torsion introduces an effective bulk stress tensor that overrides Easson's standard-GR late-time balance condition.
- **Entry 18:** Dymnikova's static regular black hole is constrained by Prop 1: its trapped region cannot be mapped exactly to FRW. It survives strictly as a non-FRW Kantowski-Sachs region.
- **Entry 19:** Classical FRW births reviewed in the paper rely on a thin shell. The smooth regular-core variant relies on Wheeler-DeWitt quantum tunneling, bypassing classical Darmois matching bounds.
- **Entry 20:** Bronnikov explicitly defines the black universe interior as Kantowski-Sachs, cleanly taking Easson's non-FRW escape.
- **Entry 21:** Roupas's horizon acts as a physical anisotropic fluid shell, avoiding the no-shell Darmois matching hypotheses.
- **Entries 25 & 26:** Easson's obstruction (Prop 2 & Thm 1) is strictly bound to a **comoving** Darmois boundary (fixed $\chi_b$). Gaztañaga explicitly sets his pressure boundary to evolve dynamically ($\chi_*(\tau)$) relative to the comoving fluid, cleanly evading the core hypothesis of the closed-FRW boundedness proof.

## 3. The Meta-Count
Based on a rigorous per-row verification of Easson's hypotheses and explicitly stated escape routes:
- **KILLS:** 0 
- **RESTRICTS:** 1 (Entry 18 is restricted to non-FRW interpretations)
- **SPARES:** 6 (Entries 11, 19, 20, 21, 25, 26 take one of the explicit escapes: added bulk stress, non-FRW geometry, shell matching, or non-comoving boundaries).
