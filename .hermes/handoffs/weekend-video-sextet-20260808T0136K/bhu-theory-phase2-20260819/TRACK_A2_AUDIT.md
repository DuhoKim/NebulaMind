# TRACK A2 — universe-in-a-black-hole audit (interior/collapse papers)

**Lana-2 (parallel science seat), 2026-08-19 16:05 KST.** Equation-by-equation audit of the
spine's two interior/collapse papers, per `PHASE2_BRIEF.md`. A1's papers (PLB 694; PRD 85) are
not audited here; where a step is *inherited* from them (the spin-fluid averaging) it is marked
as such and left to A1/Goru.

## 0. Sources and custody

| Paper | Journal record (verified in the Phase-A bibliography) | Audited text | SHA-256 (tarball) |
|---|---|---|---|
| **A** | Popławski, *Universe in a black hole in Einstein–Cartan gravity*, ApJ **832**, 96 (2016), DOI 10.3847/0004-637X/832/2/96 | arXiv:1410.3881**v2** TeX (`sources/1410.3881/Universe.tex`) | `bbe1b23bafe8fc089348fc25ac79e1fb65685f7d591835f4083a4c3006e985ff` |
| **B** | Popławski, *Gravitational collapse with torsion and universe in a black hole*, IJMPA **40** (32), 2544007 (2025), DOI 10.1142/S0217751X25440075 | arXiv:2509.11468**v2** TeX (`sources/2509.11468/Collapse.tex`) | `2b6a5ee65a0b9e0157b35b9e0cfa083bb52f7c1d6998624eb6c449064eb2ba55` |

**Custody caveats, stated up front.** (1) Both v2s are author-labeled "published version" and
carry the journal reference in the TeX header; the ApJ v2 was posted 2026-05-26 — ten years
after publication — and the paywalled ApJ PDF was not diffed against it. Claims below are about
the audited text. (2) Paper B is a HEPMAD24 conference talk published in an IJMPA proceedings
issue (footnote in the TeX); review depth of proceedings issues is typically lighter than a
regular article — weight accordingly.

**Receipts.** `receipts/a2_receipts.py` (sha256 `2f11294e…`), output `receipts/a2_receipts.out`
(sha256 `8389445b…`). R0–R7 referenced below; R3 is a full symbolic recomputation of the Tolman
Einstein tensor, R4 the homogeneous reduction, R0/R1 the closed forms and printed numbers.

## 1. Verdict table — Paper A (ApJ 832, 96)

| # | Claim / step | Verdict | Evidence |
|---|---|---|---|
| A-1 | §2 ECSK field equations (Cartan eq.; combined GR-form with spin-squared terms) | **CHECK** | Standard Hehl–von der Heyde–Kerlick form; identical in both papers |
| A-2 | §3 spin-fluid closure: random orientation kills the divergence term; ⟨s²⟩ = (ħcn_f)²/8 survives | **ASSUMED-FROM-CITATION** | Cited to Hehl+74, Gasperini 86, Nurgaliev–Ponomariev 83. This is the known critique target (Kerlick-class objections); it lives in A1's papers — cross-seat: **A1/Goru must adjudicate**; everything downstream is conditional on it |
| A-3 | §4 Friedmann eqs with torsion; conservation law; d(aT)/dt = 0 | **CHECK** | Receipt R4 (metric reduction); hand-verified conservation algebra |
| A-4 | §5 T_max = (h★/αh_nf²)^{1/2} = √(2π⁵/15)·g★^{1/2}/(ζ(3)(3/4)g_f)·T_P; 1.15×10³² K | **CHECK** | R0 exact symbolic; R1 numeric 1.152e32 K |
| A-5 | §5 τ = (αh_nf²/c)√(3/κh★³) = (45/4)√(5/π¹³)·ζ²(3)((3/4)g_f)²/g★^{3/2}·t_P; 4.75×10⁻⁴⁵ s | **CHECK** | R0 exact; R1 numeric 4.751e-45 s |
| A-6 | §5 \|H\|max = √(4/27)τ⁻¹ at T = √(2/3)T_max; 8.1×10⁴³ s⁻¹ | **CHECK** | R0 exact; R1 numeric |
| A-7 | §5 Ω_min − 1 = 4cτ/a_i at T = T_max/√2 (given κεa_i²/3 = 1) | **CHECK** | R0 exact, conditional on the stated initial condition |
| A-8 | §5 "N ≈ (ȧ/c)³ = (Ω−1)⁻³" | **ERROR** | With Ω−1 = c²/ȧ² (k=1, the paper's own relation), (ȧ/c)³ = (Ω−1)^{−3/2}. R0. The paper's own numeric N_max ≈ 10⁵² is computed with the *correct* −3/2 (R1: (5.7e-36)^{−3/2} = 7.4e52), so the printed exponent is a typo-class error that the numbers silently correct |
| A-9 | Eq. (28) block: Ω_min−1 = 5.7×10⁻³⁶ and N_max ≈ 10⁵² | **ERROR (undeclared a_i)** | Ω_min−1 = 4cτ/a_i depends on a_i; 4cτ = 5.7×10⁻³⁶ **m**, so the printed values hold only for a_i = 1 m — never declared, and inconsistent with the "typical stellar black hole a_i = 10⁴ m" adopted two lines later (which gives 5.7×10⁻⁴⁰ and N_max ≈ 10⁵⁹; R1). The companion formula "N_max ≈ (a_i/l_P)³" matches neither (gives 10¹⁰⁴–10¹¹⁶). Flatness/horizon *conclusions* survive at any a_i; the printed numbers do not cohere |
| A-10 | §5 T_i = 1.38×10¹² K, a_min = 1.19×10⁻¹⁶ m for a_i = 10⁴ m | **CHECK** | R1: 1.375e12 K, 1.193e-16 m |
| A-11 | §6 expand-to-infinity condition D > 2/(3√Λ) | **CHECK-AS-STANDARD** | Classical closed-Λ threshold (cited to Lord); not re-derived (time-boxed) |
| A-12 | §6 ã_i/a_i > 10¹⁰ (T_eq = 8820 K, Λ/κ = 5.24×10⁻¹⁰ Pa) | **CHECK** | R2: 9.99×10⁹, at a_i = 10⁴ m |
| A-13 | §6 Ω̃_min−1 < 10⁻⁵⁵ | **POST-HOC-MIX** | Multiplies the a_i = 1 m value of Ω_min−1 (5.7e-36) by the a_i = 10⁴ m bound (10⁻²⁰). Done consistently at either a_i the result is 5.7×10⁻⁶⁰. Conclusion (flatness solved) survives; the printed 10⁻⁵⁵ is an artifact of mixing two different a_i |
| A-14 | §6 production law K = β(κε̃)², vanishing at bounce | **MODEL-CHOICE (author-flagged)** | "Simplest form"; author states K "should be derived from quantum field theory in Riemann–Cartan spacetime". Produced species are massive spin-1 *bosons* (n₁) — production does not feed the fermion density n_f that sources torsion; thermal equilibrium is implicitly assumed to repopulate n_f |
| A-15 | §6 β_cr = (√6/32)h_n1h_nf³(ħc)³/h★³ = … ≈ 1/929 | **CHECK** | R0 exact both forms; R1 numeric 1.076e-3 = 1/929 |
| A-16 | §7 inflation as special case; Ht_infl ≳ 23 | **CHECK** | 10·ln10 = 23.03 from ã_i/a_i > 10¹⁰; conditional on one-bounce scenario |
| A-17 | §1 trapped surfaces → wormhole throats merge → event horizon = new closed universe | **CONJECTURE (author's word)** | "we conjecture that eventually the wormholes will merge"; no matching calculation anywhere in the paper — see §3 below |
| A-18 | §8 dynamics insensitive to a_i, depends effectively on β only | **CITED-NUMERICS** | Desai–Popławski PLB 755, 183 (2016) — Goru ingredient; if it holds, it is load-bearing *against* parent inheritance (§4 below) |

## 2. Verdict table — Paper B (IJMPA 40, 2544007)

| # | Claim / step | Verdict | Evidence |
|---|---|---|---|
| B-1 | §1 EC equations + spin-fluid effective ε̃, p̃ | **CHECK / ASSUMED-FROM-CITATION** | Same as A-1/A-2; B additionally drops the spin-divergence term from G^ij without displaying the averaging step (cited) |
| B-2 | §2 Einstein tensor of the Tolman metric, eq. (3): G₀⁰, G₁¹, G₂², G₃³, G₀¹ | **CHECK** | **Receipt R3: full symbolic recomputation — all five components reproduce exactly** (G₀¹ up to index placement) |
| B-3 | §2 conservation relations (grav4) | **CHECK** | Standard LL; consistent with R3/R4 chain |
| B-4 | (grav7) e^λ = r′²/(1+f) | **CHECK** | Direct integration of the G₀¹ = 0 equation |
| B-5 | (grav8)/(grav10) first integrals of motion | **CHECK** | Hand-verified integration; homogeneous limit confirmed symbolically (R4) |
| B-6 | (spin2) r²r′T³ = g(R) from the first law | **CHECK** | Hand: for ε̃(T), p̃(T) ultrarelativistic, Ẋ/X = −3Ṫ/T exactly |
| B-7 | Separable solution r = a(τ)sinR, f = −sin²R ⇒ closed FLRW; (spin8) Friedmann form | **CHECK** | **R4: symbolic — G₀⁰ → 3(ȧ²+1)/a², G₁¹ → (2aä+ȧ²+1)/a² exactly** |
| B-8 | (size) sinR₀ = (r_g/r₀)^{1/2}, a₀ = (r₀³/r_g)^{1/2} | **CHECK** | From f(R₀) = −r_g/r₀ and r(0,R₀) = r₀; internally consistent with §5's sin³R₀ = r_g/a₀ |
| B-9 | Mc² = (4π/3)r₀³h★T₀⁴; horizon at a = (r_gr₀)^{1/2} | **CHECK** | Hand-verified; consistent with r_g = κ∫ε̃r²r′dR |
| B-10 | Two turning points iff r₀³/r_g > (3πG/8)ħ⁴h_nf⁴/h★³ ~ l_P² | **CHECK** | **R5: exact symbolic match of the threshold**; numeric 3.25×10⁻⁷¹ m² vs l_P² = 2.61×10⁻⁷⁰ m² — same order ✓ |
| B-11 | §4 bounce: a never reaches 0 (RHS sign) | **CHECK** | Follows from (spin9); elliptic-integral solution cited to Unger–Popławski ApJ 870, 78 |
| B-12 | §4 Raychaudhuri condition 2καn_f² > 2σ² + κε | **CHECK** | Trace algebra hand-verified (R7 for the trace identity) |
| B-13 | §4 shear vs particle production: n_f ~ a^{−(3+δ)}, δ ~ −a^δȧ³ ⇒ "singularity avoided" | **UNSUPPORTED (heuristic)** | A scaling argument bolted onto a *shear-free, homogeneous* exact solution. The coupled shear+torsion+production system is never solved; no anisotropic (Bianchi/Tolman-with-shear) solution is exhibited. As a theorem this is open; as published it is a plausibility argument. **This is the step that decides whether the bounce survives realistic collapse** |
| B-14 | §5 "sinR₀ decreases and R₀ → π (completely closed universe)" | **ERROR / CONTRADICTION** | (i) §4 states "The value of R₀ does not change"; §5 recomputes R₀ per cycle from sin³R₀ = r_g/a(0) with no dynamics for the comoving boundary. (ii) On the collapse branch R₀ < π/2 (sinR₀ = (r_g/r₀)^{1/2} ≪ 1), so sinR₀ → 0 gives **R₀ → 0** (a shrinking cap), not R₀ → π; reaching π silently jumps the arcsin branch. The "completely closed universe" closure is asserted, not derived — this is the semiclosed-world problem (Frolov–Markov–Mukhanov) left unsolved |
| B-15 | §5 eternal-inflation avoidance: max of βH³/(3c³h_nfT³) < 1 | **CHECK** | Mirrors A-15; consistent |
| B-16 | §5 spectrum "consistent with the astronomical data" | **CITED** | Desai–Popławski (Goru ingredient) |
| B-17 | §5 "would still be valid for … inhomogeneous and rotating fluid" | **UNSUPPORTED** | One sentence, zero calculation. **This is the only sentence in the published chain that touches rotating (parent-spin) collapse** |
| B-18 | §4 production rate (1/c√−g)d(√−g n_f)/dτ = βH⁴/c⁴; (part2) | **CHECK internally / INCONSISTENT-ACROSS-CHAIN** | (part2) follows from (part1) with dots = d/d(cτ) (hand-verified). But vs Paper A: A produces massive spin-1 **bosons** with rate cβ(κε̃)² (= 9βH⁴/c³ near bounce); B produces **fermions** with rate βH⁴/c³. Species differ (only B's version feeds the torsion term n_f) and β normalizations differ by ×9 — neither change is remarked in B |
| B-19 | §3 g_b = 29 (A: g_b = 28) | **ERROR (typo-class)** | Standard-model bosons: 2+16+9+1 = 28. R6: effect on T_max < 0.5% — negligible but real internal inconsistency in the chain |

## 3. Focus 1 — the matching at the horizon/bounce

The chain's weakest joint, and it is weak in both papers in different ways:

- **Paper A** handles the interior→universe transition entirely at the level of §1's prose:
  trapped surfaces form, "multiple dynamical wormhole throats" appear, and "we **conjecture**
  that eventually the wormholes will merge into one wormhole" whose throat asymptotically
  coincides with the event horizon (A-17). No junction conditions, no exterior metric, no
  demonstration that the post-bounce expansion is causally hidden from the parent — the
  infinite-redshift statement is asserted from the Schwarzschild picture.
- **Paper B** exhibits an exact interior: the collapsing homogeneous spin-fluid sphere *is* a
  patch 0 ≤ R ≤ R₀ of a closed FLRW universe (B-7, receipt R4). But for stellar parameters
  sinR₀ = (r_g/r₀)^{1/2} ≪ 1 — e.g. r_g/r₀ ~ 10⁻⁵ gives R₀ ≈ 0.003 — i.e. the "new universe"
  at formation is a **tiny cap of the 3-sphere**, a semiclosed world in the
  Frolov–Markov–Mukhanov sense. The promotion of that cap to a "completely closed universe"
  (R₀ → π) is the contradictory, branch-jumping step B-14. No exterior (Schwarzschild) matching
  across the surface R = R₀ is displayed in the paper (it is inherited from the classical
  Tolman/Oppenheimer–Snyder literature for the *pre-bounce* phase only); what the exterior
  spacetime does *through and after the bounce* — the actual horizon/bounce matching the brief
  asks about — is not computed anywhere in the published chain.

## 4. Focus 2 — what of the parent is claimed to imprint

The finding that matters for the Track B transfer-function mission:

1. **Mass M — yes, and only M.** The parent black hole's mass enters through r_g, fixing the
   baby universe's initial data: a₀ = (r₀³/r_g)^{1/2}, T₀ from Mc² = (4π/3)r₀³h★T₀⁴, and R₀
   (B-8/B-9, all CHECK). This is the entire published inheritance channel.
2. **…and the chain claims M is then washed out.** Paper A §8 (A-18) reports that the numerics
   (Desai–Popławski) show the dynamics "is insensitive to the value of a_i … and effectively
   depends on the particle production coefficient β only." β is a microphysics constant, not a
   parent property. So the chain's own authors state that the one inherited parameter leaves no
   fingerprint in the interior dynamics beyond existence and cycle count.
3. **Spin a★ — absent.** Both papers treat non-rotating collapse. The word "rotating" occurs
   once in the two papers combined, in B-17: "would still be valid for a more realistic
   gravitational collapse of an inhomogeneous and rotating fluid" — an unsupported closing
   sentence with no calculation. **There is no parent-spin variable, no Kerr collapse, no
   angular-momentum transport, and no interior vorticity/axis quantity anywhere in the audited
   chain.** Any parent-spin→interior-axis transfer function must therefore be built, not
   audited, and the published chain provides no equation to start from.
4. **Anisotropy/shear — actively erased by design.** The one anisotropic quantity that does
   appear (shear σ², B-12/B-13) is treated as an obstacle that torsion + particle production
   must *defeat* for the bounce to occur, and subsequent cycles "could make [the universe] more
   homogeneous and isotropic" (A §1). To the extent the mechanism works, it suppresses
   anisotropic memory of the parent rather than transmitting it — and the suppression argument
   itself is heuristic (B-13).

**Consequence:** Phase 1's ε/f_b ignorance-parameterization is *not* superseded by anything in
these two papers for spin/axis inheritance — there is nothing here to derive it from. What the
papers do determine (and Track B can use): the M→(a₀, T₀, R₀) map (exact), T_max and the bounce
kinematics (exact), and the β-window for finite inflation (exact). The inheritance step beyond
M remains parameterization, and must be named as such per the brief.

## 5. Focus 3 — every stated observable consequence

| Observable claim | Where | Status after audit |
|---|---|---|
| Flatness: Ω̃_min − 1 < 10⁻⁵⁵ | A §6 | Order-of-magnitude survives at any a_i (consistent value 5.7×10⁻⁶⁰); printed number is an a_i-mix artifact (A-13). **CONSISTENCY-ONLY** — no measurement can distinguish this from inflation's prediction |
| Horizon: N_max ≈ 10⁵² causal patches | A §5 | Exponent identity misprinted (A-8), value assumes undeclared a_i = 1 m (A-9). Conclusion class: **CONSISTENCY-ONLY** |
| Inflation without scalar field; Ht ≳ 23; finite duration for β < β_cr ≈ 1/929 | A §6–7, B §5 | Algebra CHECK (A-15, A-16). β is free within (0, β_cr); no prediction of N_e, n_s, or r **in these papers** — spectrum consistency is delegated to Desai–Popławski PLB 755 (Goru) |
| Oscillatory universe, cycles growing until Λ-escape; "last bounce = big bang" | A §5–6, B §5 | Mechanism CHECK given closure; closure step itself is B-14 (ERROR-class) |
| Every astrophysical BH is a wormhole to a new universe | A §1, B §5 | **CONSISTENCY-ONLY / untestable from outside** — the papers themselves note the interior is invisible (infinite redshift) |
| Arrow of time, information paradox, matter–antimatter asymmetry, UV finiteness | A §6/§8, B §5 | Interpretive claims, cited elsewhere; no observable with a magnitude in the audited texts |
| **Axis / handedness / any anisotropy forecast** | — | **Absent from both papers.** Confirms Phase 1: the published interior chain makes no sky-statistics prediction of any amplitude |

## 6. Bottom line for Gate 1

The two interior/collapse papers are **algebraically solid where they compute** — every closed
form and printed number I could recompute checks out (receipts R0–R5, R7), with four defects:
the (Ω−1)⁻³ exponent misprint (A-8), the undeclared-a_i number block (A-9, propagating into
A-13), the R₀ → π closure contradiction (B-14), and the g_b 28/29 inconsistency (B-19); plus
one cross-paper inconsistency in the production law (B-18). The papers are **thin exactly where
the mission needs them thick**: horizon/bounce matching is conjecture (A-17) or
branch-inconsistent (B-14), the shear-defeat argument is heuristic (B-13), and parent
inheritance beyond M is one unsupported sentence (B-17). Nothing in the audited chain supplies
a parent-spin → interior observable transfer function or any finite-amplitude signature; the
strongest Track-B-usable results are the exact M→(a₀, T₀, R₀) map, T_max, τ, and the β-window.

Cross-seat handoffs: spin-fluid averaging validity → **A1/Goru**; Desai–Popławski numerics
(insensitivity claim + spectrum consistency) and any published rotating-ECSK-collapse work →
**Goru ingredients**.

— Lana-2, 2026-08-19 16:05 KST. Audit only; nothing derived beyond verification algebra,
nothing committed. Miru Gate 1 next.
