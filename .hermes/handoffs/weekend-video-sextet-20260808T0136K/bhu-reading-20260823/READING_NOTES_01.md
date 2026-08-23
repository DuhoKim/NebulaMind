# Reading notes, batch 1 — the Popławski-branch additions (2026-08-23, Tori)

Read in full from ar5iv-cleaned texts pinned in `sources/`. Classes assigned from the read text,
per the discipline that nothing is classed second-hand.

## Entry 39 — Popławski, "Big bounce from spin and torsion," GRG 44, 1007 (2012)

**What it does:** refines the PLB 694 bounce estimate by including ALL standard-model thermal
degrees of freedom (g_b=28, g_f=90), not just photons+neutrinos. Results: ε_bounce = 15.4 ε_Planck
(eq 14), a_bb/a_0 = 1.7×10⁻³², a_bb ≈ 49 μm; refines a_bb/a_0 = √(−Ω_S/Ω_R) with g-factor
corrections (eq 22). Uses Ω_S = −8.6×10⁻⁷⁰ — the exact number Phase 2 re-derived — and cites both
PLB 694 AND the 701, 672(E) erratum we chased.

**The load-bearing points, in the author's own text:**
- the SM-only bounce lands ABOVE Planck density, and the paper says itself the classical theory
  "should be replaced by a quantum theory of gravity" there — our audit's Planck-validity concern,
  conceded at the source;
- the escape routes offered are (a) extra fermion degrees of freedom (preons, g_f=10⁵ brings the
  bounce to 0.014 ε_Pl) or (b) trans-Planckian classicality argued from GRB photon timing — both
  speculative, neither derived;
- the averaging step s² = (ħcn)²/8 (eq 4) is cited, not derived — A-2/H2 territory again.

**Class: CONSISTENCY-ONLY.** Quantitative interior numbers but no stated falsifier and no
observable confrontation (the Kashlinsky bulk-flow mention is suggestive only).
**Audit-worthiness: medium-high** — it is the quantitative refinement of the exact numbers Phase 2
confronted; any strict-model update should use eq (22).

## Entry 41 — Popławski, "…closed anisotropic universe born in a black hole," GRG 53, 18 (2021)

**What it does:** Schwarzschild interior rewritten as a Kantowski–Sachs anisotropic closed
universe; EC field equations with spin fluid; singularity avoided iff torsion+particle production
beat shear (Raychaudhuri condition, eq 32); post-bounce finite inflation isotropizes KS → FLRW.
Two free parameters: parent mass M and production rate β.

**The load-bearing points:**
- the paper PROVES, not just argues, that torsion alone loses: shear grows faster than a⁻⁶
  (eq 30) while the torsion term scales as a⁻⁶, so without production a singularity forms. This is
  the explicit form of the step our A2 audit marked heuristic (B-13) in the 2025 paper — the
  mathematics here concedes the audit's point and then patches it with production;
- the patch is phenomenological: β H⁴ production is "phenomenologically given" (eq 33), not
  derived from QFT; the singularity-avoidance conclusion inherits β as a free dial;
- Kerr/rotating parent explicitly deferred — the spin-inheritance question Phase 2 cared about is
  outside this paper's scope by its own statement.

**Class: CONSISTENCY-ONLY.** No falsifier, no data confrontation; "closed universe" evidence cited
as motivation only.
**Audit-worthiness: HIGH** — the derivational bridge between the 2016 ApJ paper and the audited
2025 IJMPA paper, and the sharpest statement of the shear-vs-production crux in the whole branch.

## Entry 40 — Popławski, "Gravitational collapse of a fluid with torsion…," JETP 132, 374 (2021)

**What it does:** Oppenheimer–Snyder-style collapse of a homogeneous spin-fluid sphere in the
Tolman metric; torsion bounces the collapse behind the horizon; the resulting closed universe
oscillates with growing cycles (R₀ → π asymptotically) until Λ ends the cycling; "the last bounce
is the big bang."

**The load-bearing points:**
- the no-singularity result is derived FOR THE SHEAR-FREE CASE — homogeneous collapse has no shear
  by construction, so the hard problem (shear) is absent by symmetry, and the paper says plainly
  that inhomogeneous and rotating collapse are open ("further complications would appear");
- the R₀ → π cycle asymptotics is the resolved, explicit version of the closure behaviour whose
  compressed form in the 2025 paper produced our audit's B-14 contradiction finding — the lineage
  of that defect traces here;
- same phenomenological β H⁴ production as entry 41, same free-dial caveat.

**Class: CONSISTENCY-ONLY.** **Audit-worthiness: HIGH** — direct precursor of the audited 2025
collapse paper; B-14's subject matter in its uncompressed form.

## What batch 1 changes

Nothing in these three contradicts Phase 2/3; all three *strengthen* the audits' load-bearing
findings by conceding them in the mathematics (Planck validity in 39, shear-defeat in 41,
shear-free idealization in 40) and patching them with underived ingredients (preons, β). The
branch's honest summary after reading: **the bounce is conditional on an averaging step nobody
derives and a production rate nobody computes, and the authors' own equations say so.**

---

# Reading notes, batch 2 (2026-08-23, Tori)

## Entry 37 — Smoller & Temple, "Shock-wave cosmology inside a black hole," PNAS 100, 11216 (2003)

**What it does:** exact GR solutions (no torsion, no exotic ingredients) matching k=0 FRW to a
TOV-form metric *inside* a black hole across a subluminous shock beyond one Hubble length. The big
bang is a localized explosion inside the black hole of an asymptotically flat Schwarzschild
spacetime; the entropy condition breaks time symmetry and selects the explosion; the universe
eventually exits through a WHITE-hole horizon. σ = 1/3 is uniquely selected as the equation of
state for which the shock emerges from the big bang at light speed. Theorem-level results with
concrete bounds (shock ≤ 4.5 Hubble lengths when first visible; t_crit ≤ 4.5 t₀). One free
parameter.

**Distinctives:** the ONLY paper read so far with theorem-grade rigor and no underived physical
ingredient — no averaging step, no production rate. The trade: its claim is a possible exact model,
not a mechanism; no falsifier stated; the distinguishing structure lies beyond stated observational
reach ("details will appear in a forthcoming paper").

**Class: CONSISTENCY-ONLY.** **Audit-worthiness: medium-high** — branch 9's defining construction,
and the natural comparison standard for rigor when auditing the softer branches.

## Entry 52 — Unger & Popławski, "Big Bounce and Closed Universe from Spin and Torsion," ApJ 870, 78 (2019)

**What it does:** redoes the closed-universe EC bounce keeping k=1 (the audited 2016 ApJ paper's
bounce values "de facto considered a flat universe" — a published approximation-correction to the
paper our A2 audit covered). Results: a closed EC universe exists only above a threshold in
C ~ aT (C > √(8/9)); to reach dark-energy acceleration C must grow to 1.9×10⁴⁸.

**The load-bearing point:** the required C-growth QUANTIFIES the branch's dependence on particle
production — the free βH⁴ dial must deliver ~48 orders of magnitude in aT between bounce and
Λ-domination. The dial now has a required range, still with no derivation of the mechanism.

**Class: CONSISTENCY-ONLY.** **Audit-worthiness: HIGH** — direct published correction to an
audited paper's approximation, and the quantifier of the production requirement.

## Entry 53 — Cubero & Popławski, "Analysis of big bounce in Einstein–Cartan cosmology," CQG 37, 025011 (2019)

**RECORD CORRECTION:** the entry carried kimi's triage line "outside the Popławski authorship
line". FALSE — Popławski is the second author; same UNH group, companion to entry 52. Corrected in
the entry; the mistake is left noted here because a triage line became a bibliography claim without
an authorship check.

**What it does:** same closed-universe threshold analysis (x y e^{−x²/2} > e^{−1/2}) plus one new
structural result: the scale-factor bounce is DOUBLE — a single temperature bounce with two scale-
factor bounces and "a little crunch" between them, symmetric if C is constant.

**Class: CONSISTENCY-ONLY.** **Audit-worthiness: medium** — refines the same-group picture; no
independent check of anything, contrary to what our record briefly claimed.

## Batch-2 standing

Unreadable without institutional access, recorded not skipped: branch 11 (entries 47–50 — no
INSPIRE documents, no eprints, Elsevier/APS paywalls) joins Smolin 2004 (entry 31) in the
needs-access queue. Entries 36 and 57 (Smoller–Temple CMP/ARMA) have no INSPIRE record at all;
38 (MAA 2004) has an eprint and is fetched for batch 3, alongside 54, 55, 56.

---

# Reading notes, batch 3 (2026-08-23, Tori)

## Entry 56 — Gaztañaga, "The mass of our observable Universe," MNRAS Lett. 521, L59 (2023)

**What it does:** the BHU thesis in compact form — the universe has finite mass M_T ≈ 6×10²² M☉
inside its own gravitational radius r_S = 2GM_T; a GHY boundary term at r_S generates an effective
Λ = 3/r_S² ≈ 2.1 H₀², so observed acceleration is a *measurement of r_S* with no dark energy and
no fundamental Λ. Read from the PUBLISHED MNRAS PDF (open access via INSPIRE) — the first entry
read from its journal version rather than a preprint.

**Testability, in its own words:** "The smoking gun of the BHU is a cut-off in the scale of the
largest perturbations, which has already been measured in cosmic microwave background maps." A
stated directional signature with cited measurements.
**Class: QUALITATIVE-DIRECTIONAL.** **Audit-worthiness: high** — the sharpest statement of the
branch-6 claim, and the natural target if the Gaztañaga series is ever audited Phase-2-style.
Also useful context: it distinguishes Zhang 2018's same-named model as postulate-based — bearing
on kimi's R9 triage.

## Entry 54 — Gaztañaga, Kumar, Pradhan & Gabler, "Gravitational bounce from the quantum exclusion principle," PRD 111, 103537 (2025)

**What it does:** relativistic spherical collapse with an equation of state transitioning to a
ground-state density ρ_G (motivated by the exclusion principle, as in core-collapse supernovae) →
analytic bounce at R_B; the bounce stays inside r_S, which acts as Λ = 3/r_S² outside; unifies
inflation and dark-energy origin in one mechanism.

**The find: the family's only LIVE numeric falsifier.** Predicted closed curvature
**−0.07 ± 0.02 ≤ Ω_k < 0**, from χ* ≈ 15.9 Gpc tied to the CMB low-quadrupole anomaly; a confirmed
flat universe refutes it. The paper cites Planck PR3's 3σ preference for Ω_k ≈ −0.04 ± 0.01, and
ACT/DESI mild same-direction trends. **Class: CALIBRATED-FALSIFIER** — the third in the family
(after Smolin 1992 and BLR 2008), and the only one not yet fired.

**Branch correction:** the integration mis-seated this in branch 3 (torsion bounce). It is
Gaztañaga-line GR + quantum exclusion — no torsion anywhere. Moved to branch 6, number unchanged.

## Entry 55 — Alesci, Bahrami & Pranzetti, "Asymptotically de Sitter universe inside a Schwarzschild black hole," PRD 102, 066010 (2020)

**What it does:** LQG effective Hamiltonian for the Schwarzschild interior (beyond minisuperspace,
with inverse-volume and coherent-state corrections); the classical singularity is replaced by a
bounce; for Barbero–Immirzi γ ≈ 0.274 the post-bounce interior is asymptotically de Sitter — a Λ
generated purely by quantum gravity. The γ value coincides exactly with LQG's independent SU(2)
black-hole-entropy determination.

**Class: CONSISTENCY-ONLY** — the coincidence is suggestive, the Λ–mass relation is flagged by the
authors as "intriguing", and no falsifier is stated. **Audit-worthiness: medium** — the
quantum-gravity partner to entry 39's Planck-validity concession: where the ECSK bounce hits the
Planck wall, this is what the wall's other side might look like.
