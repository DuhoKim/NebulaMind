# Track A1 — core-mechanism audit: the ECSK bounce papers (spine entries 9 and 10)

**Lana (science seat), 2026-08-19, Phase 2 per `PHASE2_BRIEF.md`.** Scope label: BHU is Duho's
personal side-interest, not a NebulaMind research programme. External-theorist review required
before any publication claim.

**Bibliography gate disclosure, stated first.** The kickoff instructs verifying the
bibliography's gate first line; **no Miru gate file exists in
`../bhu-published-bibliography-20260819/` at audit time** (only `KICKOFF_MIRU_BIB.txt` — the
gate was dispatched, not yet delivered). Mitigation: both spine citations this audit rests on
were **re-verified first-hand this session** against the Crossref registry
(`sources/crossref_plb694.json`, `sources/crossref_prd85.json`, plus the erratum record via a
Crossref bibliographic query, `sources/crossref_erratum_query.json`):
- **Entry 9 / "PLB":** Popławski, *Cosmology with torsion: An alternative to cosmic inflation*,
  Phys. Lett. B 694, 181–185 (2010-11); DOI 10.1016/j.physletb.2010.09.056. Erratum: PLB 701,
  672 (2011); DOI 10.1016/j.physletb.2011.05.047.
- **Entry 10 / "PRD":** Popławski, *Nonsingular, big-bounce cosmology from spinor-torsion
  coupling*, Phys. Rev. D 85, 107502 (2012-05-29); DOI 10.1103/PhysRevD.85.107502.
This audit therefore does not rest on the ungated ranking; the target selection is Duho's
verbatim order ("go ahead with target 1, the Popławski chain").

**Custody.** Full texts fetched 2026-08-19 16:00 KST (arXiv e-print TeX + ar5iv HTML):
- `sources/1007.0587.tar.gz` SHA-256 `95ba2de3…` → `sources/1007.0587/main.tex` ("P" line refs).
  **Version caution:** the TeX is stamped 2 Nov 2010 — it *predates* the Jun 2011 erratum.
- `sources/1111.4595.tar.gz` SHA-256 `9ac75297…` → `sources/1111.4595/cosmology_torsion.tex`
  ("D" refs).
- `sources/ar5iv_1007.0587.html` `b10c3be0…`; `sources/ar5iv_1111.4595.html` `25c275dd…`.

**Receipts** (all run tonight, outputs alongside):
`receipts/p2a1_plb_symbolic.py` (R1), `receipts/p2a1_plb_numerics.py` (R2),
`receipts/p2a1_prd_symbolic.py` (R3), `receipts/p2a1_prd_numerics.py` (R4). Constants: SI-exact
ħ, c, eV; G = 6.67430×10⁻¹¹ (CODATA 2018 — the same value used in the gate-passed Phase 1
receipts); everything else from the papers' own quoted inputs.

---

## 0. Headline findings

**H1 — The spine's two core papers are mutually incompatible, and the later one disavows the
earlier one's foundation.** PRD, in its own words (D 112–115): the spin-fluid particle
approximation "is not self-consistent" and "The spin-fluid description also violates the
cosmological principle" — the *exact* framework PLB's bounce is built on. The two papers'
torsion corrections are different fluids: spin-fluid gives ε̃ = +p̃ = −κs²/4 (stiff, w = +1,
repulsive at high density); the Dirac form gives ε̃ = −p̃ = −(9/16)κn² (w = −1) and a spin-spin
interaction that is **attractive** (PRD, D 249–254, citing Kerlick: it *enhances* the
energy condition for singularity formation). The bounces are different kinds: PLB's is a smooth
H = 0 turning point; PRD's is a **cusp with a velocity jump ȧ: −v → +v inserted by
prescription** (H2/D13). "The ECSK bounce" of this chain is not one derivation — it is two
conflicting ones, and the published record (these two papers) does not adjudicate between them.

**H2 — The averaging step, the known critique target, is never derived.** Both papers assert
⟨s²⟩ ∝ n² by citation (PLB: s² = (ħcn)²/8 citing Nurgaliev–Ponomariev; PRD: ⟨s²⟩ = (3/4)n² in
one line, D 100). Both then insert the **total** fermion density — all species summed — inside
the square. Cross-species spin coherence alone is worth a factor **6.00** in Ω_S for PLB's six
neutrino types (R2: coherent −8.8×10⁻⁷⁰ vs incoherent −1.5×10⁻⁷⁰); the deeper
n²-vs-n scaling question (whether randomly oriented spins in a fluid element square-average
coherently at all) is the published debate Goru's ingredient sweep is tasked with. The Ω_S
magnitude rests entirely on this undischarged assumption.

**H3 — The numbers: sign chain CHECK; three numerical defects found.** Every step of the
sign/magnitude chain to Ω_S reproduces (negative, ∝ a⁻⁶, R1/R2), and PLB's headline numbers
(â_m, a_m, Ω(√2â_m), t, v_a, N) all recompute exactly — **except ε_R(â_m): the paper prints
1.1×10¹¹⁶ J/m³, recomputation gives 7.65×10¹¹⁶ (×6.95)** (R2), the single candidate for the
unresolved erratum (H5). PRD's two headline worked values are internally inconsistent:
**v_ant = 8.9×10³⁴ reproduces only if a_r is taken as a₀ instead of the paper's own
a_eq = a₀/(1+z_eq)** (correct value per its own definitions: 2.8×10³¹, ×3200 smaller), and
**Ω(T_cr)−1 = 1.3×10⁻⁷⁰ equals 1/v_ant² with that same inflated v — the paper's own Eq.
(density) with its own inputs gives 1.3×10⁻⁶²** (8 orders off internally; R4). No conclusion
flips (the qualitative story needs only "enormous" and "tiny"), but a strict base model cannot
inherit these numbers as printed.

**H4 — Both bounces sit at or above the Planck scale.** PLB's bounce radiation density
recomputes to 7.65×10¹¹⁶ J/m³ ≈ **1,650× the Planck energy density** (R2; even the paper's own
printed value is ~240× above); PRD's bounce temperature is **T_cr = 0.785 m_P** (R4). The
classical ECSK field equations are being applied in a regime where no classical theory is
established. PLB acknowledges the super-Planckian density only as a particle-production
trigger (P 301–302); neither paper addresses validity. Every downstream claim inherits this.

**H5 — Erratum content unresolved this session.** Existence Crossref-verified (PLB 701, 672;
DOI pinned); the publisher page 403s for unauthenticated fetch, and the arXiv TeX predates the
erratum. Mitigation: every number in the paper was recomputed independently (R2), so anything
the erratum changed is either confirmed (all reproducing values) or flagged (the ×7 ε_R, P13).
The journal-record resolution is Goru's assigned ingredient item; Gate 1 should treat P13's
attribution (error vs erratum-subject) as open until then.

## 1. Claim-by-claim verdicts

### PLB 694, 181 (P-rows; line refs into `sources/1007.0587/main.tex`)

| # | Claim (P lines) | Verdict | Basis |
|---|---|---|---|
| P1 | ECSK field equations and combined Einstein–Cartan form (55–84) | CHECK (structure, cited) | Standard Hehl–von der Heyde–Kerlick forms; not re-derived from the action here — Friedmann-level consequences verified instead (R1) |
| P2 | Weyssenhoff spin-fluid σ_ij, s_ij^k forms (94–104) | SOURCED (cited to HHK) | carries H2 caveat |
| P3 | Effective perfect fluid (ε − κs²/4, p − κs²/4) (107–116) | CHECK | R1(a,b): Friedmann system + conservation law verified symbolically |
| P4 | Friedmann eqs (Fri1/Fri2) + conservation law (121–131) | CHECK | R1(a) |
| P5 | s² = (ħcn)²/8, unpolarized fermions (136–140) | **UNSUPPORTED-BY-DERIVATION** | asserted via citation; dimension CHECK (R1e); the critique target — H2; cross-species coherence factor 6 (R2) |
| P6 | ε ∝ a^{−3(1+w)}, ε_S ∝ a⁻⁶ for any w (142–155) | CHECK | R1(a): both verified from the conservation law |
| P7 | Bounce at â_m with subsequent expansion (219–232) | CHECK | R1(b): ä > 0 at ε_eff = 0 for w = 1/3; smooth H = 0 turning point |
| P8 | **Ω_S = −8.6×10⁻⁷⁰** (210–215) | CHECK-arithmetic / **UNSUPPORTED-convention** | R2: −8.82×10⁻⁷⁰ reproduces with all 6 neutrino species summed *inside* the square; incoherent species give −1.47×10⁻⁷⁰ (×6.00); sign CHECK |
| P9 | â_m = 3.1×10⁻³³; a_m = 9×10⁻⁶ m (222–225) | CHECK | R2 (3.126×10⁻³³; 9.2×10⁻⁶ m) |
| P10 | Ω(√2â_m) − 1 = 8.9×10⁻⁶⁴ (241) | CHECK | R2 (8.884×10⁻⁶⁴; also consistent with v_a: π²/v_a² check True) |
| P11 | t = 5.3×10⁻⁴⁶ s (247) | CHECK | R2 (5.261×10⁻⁴⁶; f(x) antiderivative verified R1d) |
| P12 | v_a = 1.1×10³² c; N ≈ 10⁹⁶ (262, 274) | CHECK | R2 (1.054×10³²; 1.17×10⁹⁶) |
| P13 | **ε_R(â_m) = 1.1×10¹¹⁶ J/m³** (301) | **ERROR (or erratum-subject)** | R2: 7.65×10¹¹⁶ — factor 6.95; all neighboring quantities reproduce; attribution open pending the erratum record (H5) |
| P14 | "greater than the Planck energy density by a few orders" (301–302) | CHECK (as stated) | R2: 3.2 orders (recomputed); ~2.4 orders even at the printed value |
| P15 | Classical ECSK at super-Planckian density | **UNSUPPORTED (regime)** | H4; the paper does not address validity |
| P16 | Flatness solved "without any fine tuning" (234–251, 294) | CHECK-with-note | mechanism gives Ω(min)−1 ∝ \|Ω_S\|(Ω−1)/Ω_R² — tiny for any O(1) present curvature; not circular; magnitude inherits P8's convention |
| P17 | Horizon argument, N causally disconnected volumes (255–276) | CHECK | R2; inherits P15 |
| P18 | Contraction/expansion asymmetry mechanisms (298–308) | UNSUPPORTED | qualitative; no calculation |
| P19 | Black-hole-parent narrative (310–331) | UNSUPPORTED | no matching calculation — exactly Track B's inheritance target |
| P20 | Axis/Kerr-radius prospect; GRS 1915+105 a < 26 km (333–339) | PROSPECT / no amplitude | consistent with the Phase 1 audit of the axis paper; the a-value is an imported observation |
| P21 | Erratum PLB 701, 672 | UNRESOLVED-CONTENT | H5; Crossref-pinned existence; publisher 403; deferred to Goru |

### PRD 85, 107502 (D-rows; line refs into `sources/1111.4595/cosmology_torsion.tex`)

| # | Claim (D lines) | Verdict | Basis |
|---|---|---|---|
| D1 | Cartan equations; U^ik quadratic correction (34–47) | CHECK (structure, cited) | standard forms |
| D2 | Dirac spin tensor totally antisymmetric; contortion (62–72) | CHECK | standard Kibble–Sciama result |
| D3 | U^ik = (κ/4)(2s^i s^k + s^l s_l g^ik) for Dirac (73–77) | CHECK (structure) | follows from D2 |
| D4 | Combined tensor matches Kerlick (90–96) | CHECK (cited agreement) | |
| D5 | **⟨s²⟩ = (3/4)n²** (100) | **UNSUPPORTED-BY-DERIVATION** | one line, no derivation; same n²-coherence class as P5; n is the all-species total (133–134) — H2 |
| D6 | ε̃ = −p̃ = −(9/16)κn² (101–105) | CHECK (algebra) | **note: w = −1 fluid — different physics from PLB's stiff w = +1 spin-fluid term** (H1) |
| D7 | Spin-fluid approximation "not self-consistent", "violates the cosmological principle" (112–115) | CHECK (as the paper's own statement) | **the cross-paper finding — H1: entry 10 disavows entry 9's foundation** |
| D8 | Dirac spin-spin interaction attractive; enhances energy condition (110, 249–254) | CHECK (cited, Kerlick/O'Connell) | makes the PRD bounce *not* repulsion-driven — H1 |
| D9 | a(T) = (a_rT_r/T)·exp(3αh_n²T²/4h_⋆) (144–148) | CHECK | R3(a): solves the conservation ODE |
| D10 | T_cr = (2h_⋆/3αh_n²)^½ (152–156); 0.78 m_P (267–271) | CHECK | R3(b); R4: 0.785 m_P with g_⋆ = 106.75, g_n = 67.5 |
| D11 | a_cr closed form (158–162); 5.9×10⁻⁴ m (276) | CHECK | R3(c); R4: 5.86×10⁻⁴ m (correctly uses a_eq) |
| D12 | Parametric β(t) dynamics (178–197) | CHECK | R3(d): antiderivative verified |
| D13 | **The cusp bounce: η jumps −η_cr → η_cr; ȧ jumps −v → +v** (185, 200–204, 259–264) | **UNSUPPORTED (as dynamics)** | the jump is a prescription, not evolution: the field equations are violated at the cusp instant (ä is a distribution); the increasing a(T) branch is excluded as "unphysical" by fiat; nonsingularity rests on this insertion |
| D14 | v = (32e/243)^½(h_⋆/h_n)a_rT_r (226–230) | CHECK | R3(e): closed form verified with α = 9κ/16 |
| D15 | **v_ant(T_cr) ≈ 8.9×10³⁴** (277) | **ERROR** | R4: reproduces only with a_r → a₀ (dropping the paper's own (1+z_eq)); per its own definitions: 2.8×10³¹; note a_cr (D11) *did* use a_eq — internally mixed |
| D16 | **Ω(T_cr) = 1 + 1.3×10⁻⁷⁰** (278–280) | **ERROR (double)** | R4: equals 1/v_ant² with the D15-inflated v; the paper's own Eq. (density), own inputs: 1 + 1.29×10⁻⁶² — 8 orders off internally |
| D17 | Ω_S order-of-magnitude bridge to PLB (284–291) | CHECK (as scaling argument) | order bookkeeping only |
| D18 | Bounce at T_cr = 0.785 m_P — classical validity | **UNSUPPORTED (regime)** | H4 |
| D19 | Flatness/horizon conclusions (291–297) | CHECK (as mechanism) | inherits D13, D16, D18 |

## 2. The three focus items the brief named

**(i) Spin-fluid averaging.** Never derived in either paper (P5, D5); both insert the summed
all-species density inside the square; the coherence choice is worth ×6 in Ω_S at minimum
(R2), and the full n²-vs-n question is the published-critique item awaiting Goru's sweep.
Verdict: the chain's quantitative anchor rests on an assumption both papers cite and neither
defends — and the later paper explicitly rejects the framework the earlier one used for it.

**(ii) Sign and magnitude chain to Ω_S.** Sign: CHECK at every step (torsion term negative,
∝ a⁻⁶, receipts R1). Magnitude: reproduces (−8.8 vs printed −8.6, constants rounding) under
the coherent-total convention only; ×6 smaller incoherently; and ×(unknown) under the
unresolved averaging debate. The number is convention-conditional, not derived-unique.

**(iii) The erratum's effect.** Unresolved this session (H5). What the receipts establish
independently of it: every printed number except ε_R(â_m) survives recomputation, so the
erratum either touched ε_R(â_m)-class values (then P13 is its subject) or something outside
the numbers (then P13 is a plain error). Either way Track B must not import ε_R(â_m) as
printed. Cross-referenced to Goru's journal-record item; flagged for Gate 1.

## 3. Consequences for Track B

1. **A fork must be declared, not smoothed:** the strict bounce re-derivation
   (`P2_DERIVATION_BOUNCE.md`) must either carry both treatments (spin-fluid w = +1 stiff
   repulsion; Dirac w = −1 with cusp prescription) or choose one with the incompatibility
   stated. The published chain gives no license to blend them.
2. **Ω_S must be re-derived as a bracket**, not a number: coherent vs incoherent species
   (×6), pending the averaging-critique ingredients; the sign and a⁻⁶ scaling are safe.
3. **The inheritance step (M, a★ → interior) has no published seed in these two papers**
   (P19: narrative only) — the Phase 1 ε-parameterization remains live unless the A2 papers
   supply mechanics; coordinate with Track A2.
4. **Numbers not to import as printed:** ε_R(â_m) (P13), v_ant and Ω(T_cr)−1 (D15, D16);
   recomputed values in R2/R4 replace them.
5. **Regime caveat travels with everything:** both bounces are Planck-scale events treated
   classically (H4); the strict model must carry this as a named validity limit.

**Confidence:** arithmetic rows: high (receipts, SI-exact constants). H1 (incompatibility):
high — the disavowal is verbatim in the PRD text. H2 (averaging): high on the absence of
derivation; the physics resolution awaits the published-critique ingredients. P13 attribution:
open (erratum unresolved).

— Lana, Track A1, 2026-08-19. Gate: `MIRU_P2_STAGE1_GATE.md` next per the brief;
`portal.nersc.gov` untouched (all fetches: arXiv, ar5iv, api.crossref.org, doi.org redirect,
one 403 from sciencedirect.com — no content consumed from it).
