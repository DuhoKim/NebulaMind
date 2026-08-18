# D-C — confrontation with survey floors, and the CMB→parent inversion (Track B step 5)

**Lana (science seat), 2026-08-19, under frozen `MODEL_SPEC.md`, using D-ω and D-T.** Scope
label: black-hole-universe cosmology is Duho's personal side-interest, not a NebulaMind
research programme. Receipts: `receipts/bound_mapping_receipt.py` (R9),
`receipts/inversion_receipt.py` (R10). Novelty basis for §3: Goru item 4 (NOT-FOUND — no
published mapping of CMB rotation limits onto parent-hole parameters).

## 1. Confrontation: A at the bound-allowed vorticity, with the DERIVED coefficient

A(z_ta) = C·(ω/H)(z_ta), C = 7.2 [1.4, 12.8] (D-T), (ω/H)(z_ta) from D-ω §3. At the generous
S2 bound (Planck Bianchi VII_h; S1 is 16× tighter throughout):

| z_ta | A headline | A bracket |
|---|---|---|
| 1 | 1.2×10⁻⁸ | [2.3×10⁻⁹, 2.2×10⁻⁸] |
| **3 (fiducial)** | **1.9×10⁻⁸** | **[3.6×10⁻⁹, 3.4×10⁻⁸]** |
| 10 | 3.2×10⁻⁸ | [6.1×10⁻⁹, 5.7×10⁻⁸] |

(R9.) Against the Phase 0 certified floors:

- **Design floor** (N = 10⁵, Kun-certified): 3σ needs A ≥ 9.5×10⁻³ → the strict A falls short
  by **5×10⁵ (5.7 orders)** at fiducial; 5.2–6.7 orders across the full (z_ta, C) sweep.
- **Sample-complete comparison** (all 2.0×10¹² observable galaxies, Phase 0 pin S7):
  σ_A = 7.1×10⁻⁷ → the strict signal is **0.027σ** (bracket 0.0025–0.08σ across the full
  (z_ta, C) sweep). A 3σ detection would
  need 2.5×10¹⁶ galaxies ≈ **12,000 observable universes** (R9).

**Verdict vs Phase 0:** the strict result **strengthens the closure**. Phase 0's generous
Li-normalized branch allowed A up to 5.2×10⁻⁷; the derived transfer function puts the
bound-allowed signal at 0.04× that edge (R9: strict/generous = 0.037), comfortably inside
Phase 0's declared bracket [10⁻¹², 5×10⁻⁷] — the order-of-magnitude device bracketed the truth,
and the derivation lands it 1.4 orders below the generous edge. Nothing is overturned; the
sample-complete kill deepens from "18 universes short" to "~12,000 universes short."

## 2. Why no lever escapes

Each factor is now derived or bracketed: the epoch lever is √(1+z_ta) (mild, D-ω); the
coefficient lever is C ≤ 12.8 (derived bracket, D-T); the bound lever is S2-vs-S1 (using the
looser already). Multiplying every lever to its favorable edge (z_ta = 10, C = 12.8, S2) gives
A = 5.7×10⁻⁸ — still 5.2 orders under the design floor and 0.08σ all-sky. The closure of the
galaxy-handedness route is not an artifact of Phase 0's shortcuts; it survives the strict
model, with margin to spare.

## 3. The inversion: what the CMB already says about the parent black hole

Chain (MODEL_SPEC §2 + D-ω exponents): ω₀ = ε·Ω_H(M_p, a★)·f_b / D, with dilution
**D = Z_inf^{n_inf} · Z_rad · Z_mat²** (n_rad = 1, n_mat = 2 derived in D-ω; n_inf ∈ [1, 2]
parameterized). The S2 bound ω₀ < 1.66×10⁻²⁷ s⁻¹ (R10) inverts two ways:

**(a) Minimum-dilution form — "the CMB already constrains the parent to…":** the parent
(M_p, a★, ε) is allowed **only if** the total post-bounce spin dilution exceeds

  **D_min = ε Ω_H f_b / ω_max,0** ,  Ω_H = a★c³ / (2GM_p(1+√(1−a★²))) [standard Kerr horizon
  angular velocity; flagged for source-pinning at Kun's gate — the only imported formula in
  this document].

Worked values (R10, ε = f_b = 1): a stellar parent (10 M☉, a★ = 0.7) requires
**D > 2.5×10³⁰ (ln D > 70)**; a 10⁹ M☉ parent requires D > 2.5×10²². Splitting off the known
late history (Z_mat² = (1+z_eq)² ≈ 1.2×10⁷; z_eq = 3400 flagged as a standard value, not
load-bearing at these magnitudes), the early factor must satisfy Z_inf^{n_inf}·Z_rad >
2.2×10²³ (stellar) / 2.2×10¹⁵ (supermassive) — with n_inf = 2 and all of it from inflation,
**N_inf > 27 e-folds (stellar) / 18 e-folds (supermassive)** (R10).

**(b) Exclusion form:** at fixed D, **ε·a★_eff < ω_max,0·D/(c³/2GM_p)** — binding (below 1)
for D ≲ 6×10³⁰ (stellar) / 10²³ (supermassive) (R10 table).

**Honest reading, stated plainly:** ECSK torsion-bounce inflation is generically quoted at
tens of e-folds, above these minima — so for plausible bounce histories the CMB rotation bound
does **not** meaningfully constrain (a★, ε); the constraint is real but easily satisfied. The
genuinely new statement (Goru item 4: first formulation) is the quantitative form itself:
*a rotating-parent origin is CMB-compatible only because — and only if — the bounce-to-today
expansion dilutes the inherited spin by ≥ 10²²–10³⁰; any future model that pins its dilution
below D_min for its parent class is already excluded by Planck.* That is a falsifiable
statement about model space, and it is the first arm of C15 done properly: the derivation
exists, and its pass-or-fail range lands (for now) in the pass region for every plausible
history.

## 4. Error budget

| Link | Uncertainty | Effect on A / D_min |
|---|---|---|
| S2 vs S1 bound choice | ×16 | linear in A; linear in D_min |
| C (ξ, κ_c, μ_λ, σ_λ brackets) | ×[0.19, 1.8] around headline | bounded, derived (D-T) |
| z_ta ∈ [0.5, 10] | ×[0.49, 1.7] around fiducial | mild (D-ω) |
| bound back-evolution consistency (D-ω §3 flag) | factor few | cannot bridge 5+ orders |
| n_inf ∈ [1, 2], Z_rad, Z_inf unpinned | orders of magnitude | inversion only — named parameters (spec A6), displayed in D_min form, not hidden |
| f_b (bounce mapping) | absorbed in ε (spec A5) | one knob, displayed |
| post-turnaround decoherence, classifier noise | reduces A only | strengthens closure |

**Gate-recorded caveats (UNVERIFIED-AT-GATE, per `KUN_P1_CONFRONT_GATE.md` Check 6 — carried
here openly, not held on):**
- **U1:** the Kerr Ω_H formula, a★c³/(2GM_p(1+√(1−a★²))), carries no fetched primary-source pin
  (the gate ran local-files-only and could not fetch). It is exercised numerically in R10, was
  independently recomputed at the gate (its Check 2c), and is dimensionally correct — but it
  remains the one imported-without-pin formula in this document; pin before any external use.
- **U2:** "ECSK torsion-bounce inflation is generically quoted at tens of e-folds" is a
  literature characterization with no fetched pin in this lane; it is hedged, qualitative, and
  not load-bearing (the D_min values stand alone) — pin or drop before any external use.

Confidence: confrontation (§1–2) high — every factor derived or bracketed with receipts;
inversion (§3) medium-high on the formula, low on the numeric bite because D is honestly
unpinned — which is itself the finding.

— Lana, D-C, 2026-08-19. Gate: `KUN_P1_CONFRONT_GATE.md` expected. External-theorist review
required before any of this is called publishable.
