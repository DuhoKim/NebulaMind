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

---

# Reading notes, batch 4 (2026-08-23, Tori)

## Entry 44 — Pourhasan, Afshordi & Mann, "Out of the white hole," JCAP 04 (2014) 005
The universe as a 3-brane emerging from 5D Schwarzschild black-hole formation (DGP braneworld);
the earlier-found pressure singularity sits inside the white-hole horizon and "need not be real";
a thermal atmosphere at ~20% of the 5D Planck mass yields scale-invariant perturbations with no
inflation. **Rare self-honesty: the paper states its own base perturbation model is "already ruled
out by cosmological observations at >5σ"** (it predicts exact scale-invariance; the observed red
tilt needs corrections it only sketches). Prospects named: non-gaussianity bounds, GWs, BBN.
**Class: QUALITATIVE-DIRECTIONAL** — engages data directly, reports its own tension.
**Audit-worthiness: high** — branch 10's defining construction.

## Entry 45 — Firouzjahi & Talebian, "White hole cosmology and Hawking radiation…," PRD 106, 123505 (2022)
QFT in the white-hole interior treated as an anisotropic cosmological background; interior and
exterior observers share a vacuum; Hawking radiation from WH perturbations; non-vacuum initial
states deviate from Planckian. **Reading revises the triage: this is not a universe-origin claim**
— it borrows cosmology's language for the WH interior but its result is about radiation spectra.
Family-adjacent rather than on-claim; flagged for possible demotion to support in a future pass,
not unseated unilaterally. **Class: CONSISTENCY-ONLY.** **Audit-worthiness: low-medium** for BHU.

## Entry 43 — (…) & Olmo, "Birth of baby universes from gravitational collapse in a modified-gravity scenario," JCAP 06 (2023) 028
Numerical relativity: perturbed boson stars in Palatini f(R) = R + ξR². In the Einstein frame the
endpoint is an ordinary black hole; in the f(R) frame the innermost region forms a finite-size,
exponentially expanding baby universe joined to the parent by a throat, hidden inside a horizon at
all times. **The corpus's only numerical-relativity demonstration of baby-universe birth** —
everything else in branches 3/4 is analytic. Conditional on Palatini f(R).
**Class: CONSISTENCY-ONLY.** **Audit-worthiness: medium-high** — the simulation counterpart the
analytic line lacks.

## Entry 46 — Fullana i Alfonso & Alfonso-Faus, "Quantization of the universe as a black hole," ApSS 337, 19 (2012)
Two pages of Bohr-quantization dimensional analysis: R·λ̄ = 2ℓ_p², a "conjugate black hole" of
10⁻⁶⁵ g, 10¹²² bits, universe-as-quantum-computer. No dynamics, no derivation, no falsifier — a
large-numbers coincidence note. The gate's "scientific weight may be low, scope fit high" was
exactly right. **Class: CONSISTENCY-ONLY.** **Audit-worthiness: low.**

## Entry 42 — author resolved from the record
INSPIRE metadata names the author the harvest never returned: **P. F. González-Díaz** (PLB 261,
357, 1991). Filled in the entry from the record, not from recall. Text: no documents, paywalled —
needs-access queue.

---

# Reading notes, batch 5 — the last two readable (2026-08-23, Tori)

## Entry 51 — Popławski, "Nonsingular Dirac particles in spacetime with torsion," PLB 690, 73 (2010)

**What it does:** Papapetrou multipole expansion showing a Dirac field in ECKS cannot form
singular 1D/2D configurations — particles have spatial extent at least their Cartan radius
(electron: ~10⁻²⁷ m, proposed as a UV cutoff). Consequences with numbers: maximum matter density
~10⁵¹ kg/m³ (the Cartan density), hence a **minimum black-hole mass ~10¹⁶ kg**, hence "the LHC
cannot produce micro black holes" if ECKS holds.

**Class: QUALITATIVE-DIRECTIONAL** — a stated, numbered, falsifiable consequence (a black hole
below 10¹⁶ kg refutes it), not confronted with the discriminating dataset. **My inference, marked
as mine:** the discriminator is not the LHC (standard physics also predicts no LHC micro-BHs) but
primordial black holes — standard physics permits sub-10¹⁶-kg PBHs, ECKS+this analysis forbids
them, so a PBH evaporation detection would be a clean kill. The paper does not press this.
**Audit-worthiness: high** — the microphysical foundation of the branch's singularity avoidance,
and the mechanism paper behind entry 39's citation chain.

## Entry 38 — Smoller & Temple, "Cosmology, black holes and shock waves beyond the Hubble length," MAA 11, 77 (2004)

**What it does:** the full-detail companion to entry 37 (PNAS) — the theorems, proofs and
construction behind the letter: exact entropy-satisfying shock-wave solutions extending
Oppenheimer–Snyder to nonzero pressure inside the black hole; the entropy condition selects the
white-hole explosion over the collapse and determines a unique solution; p = ρ/3 uniquely
distinguished at the big bang.

**The authors' own caveat, worth quoting because the family rarely writes like this:** the
solutions are "only rough qualitative models because the equation of state on the TOV side is
determined by the equations, and therefore cannot be imposed" — only loose bounds 0 < p̄ < ρ̄
hold. Rigor about the mathematics, and equal rigor about its limits.
**Class: CONSISTENCY-ONLY.** **Audit-worthiness: medium** — entry 37's proofs live here.

# CAMPAIGN CLOSE — the readable floor is reached

15 of 23 unread entries read and classed in one day (batches 1–5). The remaining 8 — entries 31,
36, 42, 47–50, 57 — are unobtainable on every free route (Elsevier/APS/Springer paywalls; two with
no digital records at all) and constitute the needs-institutional-access queue. No entry was
classed from memory, citation, or triage; every class traces to a read text pinned in `sources/`.

---

# Watch-driven read #1 — arXiv:2512.09486 against the live falsifier (2026-08-23, Tori)

**Paper:** Yadav, Dixit, Barak & Pradhan, "Constraints on Spatial Curvature and Dark Energy
Dynamics in the wCDM Model from DESI DR1 and DR2." **Not a DESI Collaboration paper** — an
independent group fitting wCDM+Ω_k to DESI BAO data with BBN/OHD/Pantheon+. No journal ref on the
preprint; prose quality modest. Weight its numbers accordingly.

**Its Ω_k constraints, verbatim from §III:**

| combination | Ω_k |
|---|---|
| DR1+BBN | +0.094 ± 0.080 |
| DR1+BBN+OHD | +0.075 +0.070/−0.054 |
| DR2+BBN | +0.003 ± 0.048 |
| DR2+BBN+OHD | +0.002 ± 0.045 |

**Against entry 54's window (−0.07 ± 0.02 ≤ Ω_k < 0): NO VERDICT, and no kill.**

- The DR2-based fits (the better data) are flat-centred; the window's centre (≈ −0.05) sits ~1.1σ
  below their posterior centre — inside, not excluded.
- The DR1-based fits pull *open* (+0.09), the OPPOSITE direction from the falsifier — ~1.8σ
  against the window — but DR1 is superseded by DR2 within the paper's own analysis.
- Everything is sub-2σ. The paper itself claims only "mild preference for an open universe."

**The structural point worth keeping:** this is the geometric tug-of-war the falsifier lives in.
Entry 54 leans on CMB-lensing's ~3σ *closed* preference (Planck PR3); BAO-side combinations like
these pull flat-to-open. The falsifier's fate will be decided by exactly this tension resolving —
which is why the watch watches BAO releases, not CMB reanalyses. When a DESI **Collaboration**
Ω_k posterior tightens below ~0.02 around zero, the window starts dying; if it tightens around
−0.04, the window starts winning. Neither has happened.

Not seated in the bibliography: it is adjudication literature, one of many Ω_k fits, not a BHU
paper and not a canonical instrument. Logged here and in the watch hits file only.

---

# Batch 6 — the recovered three (2026-08-23 evening, Tori)

Prompted by Duho asking whether I could fetch the paywalled queue myself. A second sweep found
free, legitimate copies of 3 of the 8: entry 31 (published PDF on a VU Amsterdam academic
collection), entry 36 (arXiv astro-ph/9812063 — missed during the campaign because the eprint
checks ran into arXiv throttling and I wrongly recorded "no free route"), entry 57 (self-archived
on Temple's UC Davis page). **The campaign's "16% irreducible floor" claim was therefore wrong;
the true floor is 5 papers ≈ 10%** (42, 47–50 — Elsevier + APS only). Corrected in the
bibliography tally.

## Entry 31 — Smolin 2004, Physica A 340, 705 (CNS) — CALIBRATED-FALSIFIER

The paper the whole CNS audit leaned on, now read in the original. What the text actually says:

- The falsifier (§4, "Why a single heavy neutron star would refute S"): kaon-condensate cores
  (Bethe–Brown [52–54]) cap M_max at "approximately 1.5 M☉" **if** the strange-quark mass is
  below a critical value; conventional EOS otherwise, limit "almost certainly above 2".
  Refutation: "Sufficiently high is certainly 2.5 M☉, although if one is completely confident of
  Bethe and Brown's upper limit of 1.5 solar masses, any value higher than this would be
  troubling."
- **Track C is confirmed from the primary text**: CNS does not predict 1.5 M☉ (that is
  Brown–Bethe's number, used as an instrument), and Smolin's own clean bar is 2.5 M☉. The
  published-record basis Track C used matches the primary source exactly, including the
  "troubling" sentence verbatim.
- Footnote 6 concedes ad-hoc rescues exist and disclaims them absent independent theory support —
  the author states his own demarcation.
- Footnote 1 credits Rothman & Ellis [13] and Ellis [14] for the open-universe correction —
  corroborates appendix A0's citation trail (their text itself still unread).
- §2 is explicit that the low-energy parameter "successes" are explanations, not predictions
  ("selection effects prevent us from claiming these as unique predictions").
- Reader's note (mine): the Λ argument in §3 ends in a stated conjecture, not a result; and the
  1.5-vs-2.5 gap means the falsifier's live status depends on which bar you hold — C08 broke the
  instrument limb (≥8σ), the author's stated bar stands unreached (heaviest well-measured masses
  sit below 2.5).

Consequence for the family: **a second live calibrated falsifier** joins entry 54. Yesterday's
"exactly one live falsifier" line is amended — it counted only classed entries, and 31 was UNREAD.

## Entry 36 — Smoller & Temple 2000, CMP 210, 275 — CONSISTENCY-ONLY

The shock-wave programme's founding cosmology paper. Constructs the simplest exact solution with
a true shock at the leading edge of a k=0 FRW region inside a static TOV exterior, tuned to the
observed H₀ and CMB temperature; the derived shock position comes out comparable to the Hubble
length with no free parameters — the paper's own headline result. It is candid that the model
violates the Copernican principle and that shock entropy destroys memory of the initial explosion.
No observational discriminant is derived; the cosmological reading is posed as a question and the
solution offered as "a starting point". The horizon is not crossed anywhere in this paper — the
inside-a-black-hole step is entry 37 (PNAS 2003).

## Entry 57 — Smoller & Temple 1997, ARMA 138, 239 — CONSISTENCY-ONLY

Method precursor: simplified FRW/Oppenheimer–Tolman shock-matching ODEs, Lax admissibility,
speed formulas for numerics. Explicitly restricted to shocks outside the Schwarzschild radius;
§6 shows these solutions model explosions, not collapse. Pure mathematics; one sentence of
cosmological framing. Nothing here bears on observables.

Pins: smolin sha256 46e57c43…, smoller-temple-2000 ef904904…, smoller-temple-1997 6e709a9c…
(full hashes with the PDFs in `sources/`).
