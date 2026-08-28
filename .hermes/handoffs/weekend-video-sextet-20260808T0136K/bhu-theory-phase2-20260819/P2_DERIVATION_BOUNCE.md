# P2 Track B step 1 — the ECSK bounce, re-derived (both treatments, our own algebra)

**Lana (science seat), 2026-08-19, under `PHASE2_BRIEF.md` Track B(1), Gate 1 = PASS_P2_STAGE1
with its five carried conditions honored (each cited where it bites).** Scope label: BHU is
Duho's personal side-interest, not a NebulaMind research programme. External-theorist review
required before any publication claim.

**Base and custody.** All equations are re-derived here from the pinned full texts under
`sources/` (PLB TeX `95ba2de3…`, PRD TeX `9ac75297…`); no new fetches were needed. Receipts
(fresh algebra, prefix p2b1, outputs alongside): `receipts/p2b1_spinfluid_derivation.py`
(B-R1) and `receipts/p2b1_dirac_derivation.py` (B-R2). Constants: SI-exact ħ, c, eV;
G = 6.67430×10⁻¹¹ (CODATA 2018, as in all prior gated receipts). Goru ingredients: per Gate 1
condition 1, sections 1/2/4 are excluded (no venues) — nothing below leans on them; the
erratum venue (section 3) is used at the metadata level only.

## 0. Result, up front

The published chain contains **two incompatible bounces**, and re-deriving both from their own
pinned equations confirms the incompatibility rather than resolving it (Gate 1 condition 3;
audit H1). Treatment I (spin-fluid) yields a smooth H = 0 bounce whose scale is set by
**Ω_S ∈ [−8.8×10⁻⁷⁰, −1.5×10⁻⁷⁰]** — a bracket, not a number, spanned by the underived
species-coherence choice (×6.00, derived below); the published −8.6×10⁻⁷⁰ sits at the
coherent edge. Treatment II (Dirac) yields not a smooth bounce but a **cusp**: we derive,
fresh, that H² > 0 at the minimum scale factor and that the temperature rate diverges there
(|β̇| → ∞, B-R2) — the bounce is a kinematic prescription with distributional ä, not
evolution. **Both treatments put the bounce at or above the Planck scale** (Treatment I:
1.6×10³–5.7×10⁴ × the Planck energy density across the bracket; Treatment II:
T_cr = 0.785–1.92 m_P across the same bracket) — the named validity limit V1 travels with
every quantity below. All three quarantined printed numbers are replaced by our own
recomputations (§2.4, §3.3).

## 1. The fork, declared (requirement 1)

| | Treatment I — spin-fluid (PLB 694) | Treatment II — Dirac (PRD 85) |
|---|---|---|
| Torsion correction | ε̃ = p̃-partner: ε_eff = ε − κs²/4, p_eff = p − κs²/4 (stiff, w = +1) | ε̃ = −p̃ = −(9/16)κn² (w = −1) |
| Spin-spin character | repulsive at high density | **attractive** (enhances the energy condition; PRD's own text) |
| Bounce type | smooth H = 0 turning point, ä > 0 | **cusp**: ȧ jumps −v → +v by prescription |
| Mutual standing | — | PRD calls the spin-fluid particle approximation "not self-consistent" and says it "violates the cosmological principle" (audit D7) |

They cannot be blended; both are carried through in parallel. Any downstream Phase 2 document
citing "the ECSK bounce" must name which treatment it means.

## 2. Treatment I — spin-fluid bounce, our derivation

### 2.1 Dynamics (every step receipted)

Base (source-pinned, PLB main.tex 119–131): closed FLRW, effective fluid
ε_eff = ε − κs²/4, p_eff = p − κs²/4; Friedmann pair F1: ȧ² + 1 = (κ/3)ε_eff a²,
F2: ȧ² + 2aä + 1 = −κ p_eff a² (dots w.r.t. ct).

- **Conservation law derived, not assumed** (B-R1 step 1): differentiating F1 and eliminating
  ä (via F2) and ȧ² (via F1) leaves exactly (−κ/3a) × [d(ε_eff a³) + p_eff d(a³)] — the
  factor is pure, so the law is forced for ȧ ≠ 0.
- **Scalings derived** (B-R1 steps 2–3): with p = wε and dn/n = dε/(ε+p), n ∝ a⁻³ for any w;
  hence with s² ∝ n² (the V2 assumption, §5), ε_S ≡ −κs²/4 ∝ a⁻⁶ for any w, and ε ∝ a^{−3(1+w)}
  solves the law.
- **Bounce** (B-R1 steps 5–6): H = 0 at â_m² = |Ω_S|/Ω_R with the exact closed-universe root
  differing only by a relative curvature correction |Ω_S|(Ω−1)/Ω_R² ≈ 2×10⁻⁶⁴ (derived
  symbolically, evaluated numerically — the neglect is justified, not assumed); and
  −(ε_eff + 3p_eff) = +κs²/2 > 0 at the bounce — genuine re-expansion, not a stall.

### 2.2 Ω_S as a bracket (requirement 2)

The averaging chain: s² = C_avg(ħc)²n². The **n²-form itself is ASSUMED-WITH-CITATION**
(PLB 136–140, citing Nurgaliev–Ponomariev; underived in the chain — audit H2; the published
critique literature is not usable here per Gate 1 condition 1, so this derivation makes no
claim about the n²-vs-n question and conditions everything on the n² form). What **can** be
derived is the species structure (B-R1 step 4): for six neutrino species with independent,
zero-mean spin fields, E[(Σᵢsᵢ)²] = ΣᵢE[sᵢ²] — cross terms vanish — while the published
computation inserts the **summed density inside the square** (coherent). With six equal
species the ratio is exactly **6.00**. Hence, under the paper's own inputs
(H₀⁻¹ = 4.4×10¹⁷ s, Ω = 1.002, Ω_R = 8.8×10⁻⁵, n = 5.6×10⁷ m⁻³ × 6 types):

  **Ω_S = −8.82×10⁻⁷⁰ (coherent edge) … −1.47×10⁻⁷⁰ (incoherent edge)**  (B-R1 step 7)

The published **−8.6×10⁻⁷⁰ sits at the coherent edge** (2.6% inside it — constants rounding).
Physical note: independence across distinct species is the standard expectation; the coherent
edge therefore requires cross-species spin correlations the chain never argues for. The
incoherent edge is the better-motivated one *given* the n² form; both are carried.

**Erratum handling, exactly as Gate 1 resolved it (its Check 2):** the erratum's existence and
venue are Crossref-confirmed at the metadata level (PLB 701, 672; DOI
10.1016/j.physletb.2011.05.047); its **content is UNVERIFIED-AT-GATE** and nothing here
attributes any specific correction to it. The bracket above is derived from the pinned
pre-erratum TeX; if the erratum's content, once obtained, changes an input, the bracket
recomputes mechanically (every number is scripted).

### 2.3 Downstream bounce quantities — bracket table (B-R1 step 7)

| quantity | coherent edge | incoherent edge |
|---|---|---|
| Ω_S | −8.82×10⁻⁷⁰ | −1.47×10⁻⁷⁰ |
| â_m | 3.17×10⁻³³ | 1.29×10⁻³³ |
| a_m | 9.3×10⁻⁶ m | 3.8×10⁻⁶ m |
| Ω(√2â_m) − 1 | 9.1×10⁻⁶⁴ | 1.5×10⁻⁶⁴ |
| t(√2â_m) | 5.4×10⁻⁴⁶ s | 9.0×10⁻⁴⁷ s |
| v_a/c | 1.04×10³² | 2.55×10³² |
| ε_R(â_m) | 7.3×10¹¹⁶ J/m³ | 2.6×10¹¹⁸ J/m³ |
| **ε_R(â_m)/ε_Planck** | **1.6×10³** | **5.7×10⁴** |

Note vs the audit's R2 rows: R2 tested the paper's *internal consistency* using the printed
Ω_S = −8.6×10⁻⁷⁰; this table uses **our derived** coherent value −8.82×10⁻⁷⁰, so entries
differ from R2 by (8.82/8.6)^p factors (e.g. ε_R: 7.27 vs 7.65 ×10¹¹⁶, ratio (8.82/8.6)² —
stated per requirement 3, discrepancy explained, not hidden).

### 2.4 Quarantined number P13 (requirement 3)

**ε_R(â_m): the printed 1.1×10¹¹⁶ is not used anywhere.** Our recomputation: 7.27×10¹¹⁶
(with our Ω_S) / 7.65×10¹¹⁶ (with the printed Ω_S — reproducing audit R2 exactly). The ×7
misprint-or-erratum-subject attribution stays open per Gate 1 condition 2.

## 3. Treatment II — Dirac bounce, our derivation

### 3.1 Dynamics (B-R2, fresh)

Base (source-pinned, PRD cosmology_torsion.tex 127–134): conservation law with
ε̃ = −p̃ = −αn², α = (9/16)κ; thermal forms ε = h⋆T⁴, p = ε/3, n = h_nT³.
- **a(T) solved fresh by ODE** (B-R2 step 1): a ∝ (1/T)exp(c₁T²/2), c₁ = 3αh_n²/(2h⋆) —
  matches the pinned Eq. (int).
- **T_cr and a_cr fresh** (step 2): T_cr = 1/√c₁ = √(2h⋆/(3αh_n²)); a_cr = a_rT_r√e/T_cr.

### 3.2 The cusp, quantified (new, receipted)

At T_cr the effective energy density is **strictly positive**:
(κ/3)ε_eff(T_cr) = 4h⋆³κ/(81α²h_n⁴) > 0 (B-R2 step 3) — so H ≠ 0 at the minimum scale
factor: this is **not** a turning point. And the temperature rate **diverges** there:
lim(β→β_cr⁺)|β̇| = ∞ (B-R2 step 3). The "bounce" is therefore a cusp with distributional ä
and divergent Ṫ, entered by the prescription ȧ: −v → +v (audit D13). Our derivation confirms
the audit's verdict at the equation level: Treatment II's nonsingularity is
curvature-finiteness only; the evolution through the minimum is inserted, not derived.

### 3.3 Numbers, with quarantined D15/D16 replaced (requirement 3)

With the paper's own inputs (g_b = 28, g_f = 90 ⇒ g⋆ = 106.75, g_n = 67.5; T_r = 0.75 eV;
a_r = a₀/(1+z_eq), a₀ = 2.9×10²⁷ m, z_eq = 3200):
- T_cr = **0.785 m_P** (m_P reduced = 2.435×10¹⁸ GeV) — agrees with audit R4.
- a_cr = **5.86×10⁻⁴ m**.
- **v_ant(T_cr) = 2.77×10³¹** — our own computation; agrees with audit R4; the printed
  8.9×10³⁴ (D15) is not used.
- **Ω(T_cr) − 1 = 1.29×10⁻⁶²** — our own; agrees with R4; the printed 1.3×10⁻⁷⁰ (D16) is
  not used.

### 3.4 The coherence bracket reaches Treatment II too

⟨**s**²⟩ = (3/4)n² (PRD line 100) uses the all-species total density squared — the same
V2-class assumption. Reducing the effective ⟨s²⟩ by an incoherence factor f multiplies T_cr
by √f: for the equal-species illustration f = 6, **T_cr → 1.92 m_P** and a_cr → 2.4×10⁻⁴ m
(B-R2 step 5) — the incoherent edge pushes the Dirac bounce *super*-Planckian. (An exact f
for the standard-model species mix would need the per-species g_i decomposition; the
direction and scale of the effect are what matter here.)

## 4. Cross-treatment comparison (the fork in numbers)

| | Treatment I (coherent…incoherent) | Treatment II (coherent…f=6) |
|---|---|---|
| bounce scale factor | 3.8–9.3 ×10⁻⁶ m | 2.4–5.9 ×10⁻⁴ m |
| bounce thermodynamic state | ε_R = 10³·⁲–10⁴·⁸ × ε_Planck | T_cr = 0.79–1.92 m_P |
| H at minimum | 0 (smooth) | ≠ 0 (cusp) |
| mechanism | repulsive stiff torsion term | prescription (velocity jump) |

The chain's own two treatments disagree on the bounce scale by **two orders of magnitude**
and on the mechanism qualitatively. "The ECSK bounce" is treatment-dependent even at the
order-of-magnitude level — a fact any inheritance derivation (Track B step 2) must carry.

## 5. Named validity limits (requirements 4–5; all travel with every quantity above)

- **V1 — Planck regime (Gate 1 condition 5):** every bounce state above sits at or above the
  Planck scale under classical field equations — Treatment I: ≥1.6×10³ × ε_Planck (worse on
  the better-motivated incoherent edge: 5.7×10⁴×); Treatment II: T_cr ≥ 0.785 m_P (worse
  incoherent: 1.92 m_P). Per Gate 1 Check 4(c) this caveat also covers the A2-certified
  T_max = 1.15×10³² K ≈ 0.81 T_P and τ = 4.75×10⁻⁴⁵ s used downstream. No quantity derived
  here is validity-clean.
- **V2 — the n² averaging (requirement 5):** ASSUMED-WITH-CITATION wherever used (Treatment I
  §2.2; Treatment II §3.4); the species-coherence bracket (×6.00, derived) is propagated —
  never collapsed to one edge. The deeper n²-vs-n question stays open pending named, pinned
  critique publications (Gate 1 condition 1).
- **V3 — the cusp prescription (Treatment II only):** ȧ jump inserted by hand; ε_eff > 0 and
  |β̇| → ∞ at the minimum are receipted facts (§3.2).
- **V4 — curvature neglect at the bounce:** justified, not assumed — relative correction
  ~2×10⁻⁶⁴ (B-R1 step 5).
- **V5 — erratum content unresolved (Gate 1 condition 2):** metadata-level only; all inputs
  scripted so any future content lands mechanically.

## 6. Handoff to Track B step 2 (inheritance)

Confirmed inputs for `P2_DERIVATION_INHERITANCE.md`: the bounce state is
treatment-dependent — Treatment I hands over (a_m, ε(a_m)) per bracket edge; Treatment II
hands over (a_cr, T_cr, ±v). Per Gate 1 conditions 3–4 and both audits' agreement: **no
published equation connects parent (M, a★) to any of these interior states' rotational
content** — the A2-certified M→(a₀, T₀, R₀) map carries mass only. The Phase 1 ε/f_b
parameterization therefore remains the named vehicle for spin inheritance unless step 2 can
derive a piece of it from the pinned interior solutions; where it cannot, the parameter stays
and is named (brief Track B(2) rule).

— Lana, Track B step 1, 2026-08-19. Receipts p2b1_* all run clean this session. Gate:
`MIRU_P2_BOUNCE_GATE.md` expected next. portal.nersc.gov untouched; zero new fetches.
