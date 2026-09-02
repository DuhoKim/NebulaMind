AUDIT_HOLDS_PROSPECT

# Entry 47 deep audit — claude-seat (BLIND; independent of codex/kimi) — 2026-09-02 21:02 KST

Source read: `../bhu-reading-20260823/sources/sato_kodama_sasaki_maeda_1982_plb108_103_clean.txt` (416 lines, OCR). Only this file. Line numbers below are receipts into it. Arithmetic is mine; where it disagrees with the paper's rounding I say so. Constants used: m_p = 1.22×10^19 GeV (paper uses ~10^19, L241), ħc = 1.97×10^-14 GeV cm, ħ = 6.58×10^-25 GeV s, 1 GeV = 1.78×10^-24 g.

## 1. The construction — is 10^77 derived from stated inputs?

**Chain, with what each step is (E = equation in the paper, A = assumption stated in the paper, I = numerical input chosen by the authors):**

| Step | Content | Receipt | Kind |
|---|---|---|---|
| 0 | Radiation negligible vs false-vacuum density ρ_v (constant); true-vacuum energy density exactly zero | L47–50 | A |
| 1 | de Sitter background: R(τ) = λ l exp[(τ−τ*)/l], l = (8πGρ_v/3)^-1/2 | L53–61, eqs 1–3 | E |
| 2 | Toy geometry: infinite number of bubbles nucleated *simultaneously on a sphere* X = X_0 at τ_0; walls at light speed; region B is Schwarzschild by Birkhoff | L66–69, L93–101, eq 4 | A (spherical toy) + E |
| 3 | Mass and gravitational radius of the trapped shell: M = (4π/3)ρ_v [R(τ_0)X_0]^3, r_g = 2GM = (aX_0)^3 l | L102–111, eqs 5–6 | E |
| 4 | Wall proper radii r_±(τ) = l{(aX_0 ± 1)exp[(τ−τ_0)/l] ∓ 1}; **dichotomy**: aX_0 < 1 → inner region collapses → black hole; aX_0 > 1 → inner region A inflates forever, joined to C by an Einstein–Rosen bridge (wormhole) | L113–134, eqs 7–8 | E |
| 5 | Generalisation to asymmetric domains: "expected to be still applicable … provided that the nucleation rate is sufficiently small"; "strongly indicates the general formation of wormhole-bridge structure, **though it is not exactly proved yet**" | L135–162 | A (explicitly unproved) |
| 6 | Nucleation rate per unit 4-volume constant in time = v l^-4 (quantum tunnelling only, no thermal nucleation); false-vacuum volume fraction u(τ) (Guth–Tye/Einhorn–Sato form); bubble number density n_B = v u/(3 l^3), "provided v ≪ 1" | L163–187, eqs 9–10 | A + E |
| 7 | Flat-space percolation: false-vacuum networks break up at u_c ≈ 0.3 [13]; critical time τ_c − τ* ≈ v^-1 l | L187–195, eq 11; footnote L218–226 | A (percolation import, defended in fn 1) + E |
| 8 | Mean bubble separation d = n_B^-1/3 ≈ (10/v)^1/3 l; **presumed** trapped-domain radius r_(τ_c) = 0.5(10/v)^1/3 l | L196–201, eq 12 | A ("we may presume") |
| 9 | Wormhole condition from eq 8 vs eq 12: (10/v)^1/3 > 1 ⇒ most trapped domains become wormholes | L202–205 | E (given 8) |
| 10 | **Homogeneity requires phase-transition duration > 60 l** (cited [1–3]) ⇒ v < 1/60 satisfies both that and step 9 | L206–214 | I (v = 1/60 is the *largest allowed* value) |
| 11 | Typical wormhole mass M_w ≈ (k/8)(10/v)(4πρ_v l^3/3), v/10 < k < 1; evaporation time t_ev ≈ 0.14 k^3 (10/v)^3 (m_p^4/ρ_v) l | L228–240, eqs 13–14 | E, with free factor k spanning 600× |
| 12 | GUT inputs: ρ_v = (10^15 GeV)^4, v = 1/60 ⇒ t_ev ≈ 3×10^-13 k^3 s | L241–246, eq 15 | I |
| 13 | Child's own transition completes at Schwarzschild time t_c = r_(τ_0) exp(v^-1) ≈ 10^26 l ≈ 10^-10 s; t_ev ≪ t_c ⇒ disconnection before the child's transition completes | L257–271, eqs 16–17; fn 3 L306–314 says this ordering "may be indispensable" for survival (ref [14], not shown here) | E + I |
| 14 | Child radius after its own transition: L ≲ (10/v)^1/3 exp(v^-1) l ≈ 10 cm | L283–287, eq 18 | E (upper bound) |
| 15 | Domain density at percolation n_f ≈ u_c/[4πr_(τ_c)^3/3] = v/(30 l^3); "**if all** the false vacuum domains become wormholes", children per universe p = n_f (4πL^3/3) ≈ exp(3/v)/3 | L326–336, eq 19 | E, under the "if all" assumption |
| 16 | v = 1/60 ⇒ p ≈ 10^77 | L337–338 | I |

**Arithmetic checks.**
- l: H = (8π/3)^1/2 ρ_v^1/2/m_p = 2.894 × 10^30 GeV^2 / 1.22×10^19 GeV = 2.37×10^11 GeV ⇒ l = 4.2×10^-12 GeV^-1 = 8.3×10^-26 cm = 2.8×10^-36 s (with m_p = 10^19: 6.8×10^-26 cm, 2.3×10^-36 s).
- exp(60) = 1.14×10^26 ✓ (L264 "≈10^26 l"); t_c = 1.14×10^26 × 2.3–2.8×10^-36 s = 2.6–3.2×10^-10 s ✓ (L264 "≈10^-10 s").
- (10/v)^1/3 = 600^1/3 = 8.43 > 1 ✓ (wormhole condition, step 9).
- M_w: (4π/3)ρ_v l^3 = 4.19 × 10^60 × 4.1×10^-35 GeV = 1.7×10^26 GeV ≈ 3×10^2 g; × (10/v)/8 = 75 ⇒ M_w ≈ 2×10^4 k g, i.e. 40 g – 20 kg over the stated k-range.
- t_ev: 0.14 × 600^3 × (10^76/10^60) × l = 3.0×10^23 l = 6.9×10^-13 k^3 s vs paper 3×10^-13 k^3 s — factor 2, fine. I also verified the coefficient: 10π·8^4/27 · M_w^3/m_p^4 reduces to 0.139 (m_p^4/ρ_v) l exactly as eq 14 states. (The prefactor 10π·8^4/27 ≈ 4.8×10^3 vs the standard 5120π ≈ 1.6×10^4 is a species-count choice; immaterial.)
- t_ev/t_c = 6.9×10^-13 k^3 / 3×10^-10 ≈ 2×10^-3 k^3 ≪ 1 for all k ≤ 1 ✓ — this inequality IS derived and holds across the free k range.
- L (eq 18): 8.43 × 1.14×10^26 × (6.8–8.3)×10^-26 cm = **65–80 cm**, or 33–40 cm if the 0.5 of eq 12 is kept. Paper says "about 10 cm" (L287). Factor 3–8 discrepancy in the paper's favour of a *smaller* L; immaterial for the count (see below) and immaterial for Q2 (makes the margin larger).
- n_f (eq 19 text): u_c/[4π(0.5·600^1/3 l)^3/3] = 0.3/(4.19 × 1.25 l^3/v) = v/(17.5 l^3), paper writes v/(30 l^3). Factor 1.7. Immaterial.
- p: with L^3 = (10/v) e^{3/v} l^3 and n_f = v/(30 l^3): p = (v/30)(4π/3)(10/v) e^{3/v} = 1.4 e^{3/v}; with the 0.5 kept, 0.17 e^{3/v}; paper 0.33 e^{3/v}. All O(1).
- **exp(3/v) at v = 1/60 = exp(180) = 10^(180/2.3026) = 10^78.17 = 1.5×10^78; /3 = 5×10^77.** Paper: "10^77!" (L338). So the record's "10^77" is the authors' rounding of ≈5×10^77 (my range 2.5×10^77–2×10^78).

**Verdict on derivation.** The count IS derived from stated inputs, and the derivation is short once you see its structure: p = u_c × (child's volume at its own percolation)/(one trapped domain's volume at percolation) = u_c × [exp(N)]^3 with **N = 1/v the number of e-folds of the phase-transition era**. Every geometric factor cancels (n_f ∝ v/l^3 and L^3 ∝ l^3/v) and the entire 10^77 comes from one number: N = 60 e-folds, which is not derived but *imported* as the minimum needed for homogeneity (L206–214). Three consequences the record should carry:
(a) v = 1/60 is the **upper limit** allowed by homogeneity (L212). The model requires v ≪ 1 (L187), and p ∝ e^{3/v} grows without bound as v → 0: v = 1/61 gives e^3 ≈ 20× more; v = 1/100 gives ≈10^130. So 10^77 is a **floor**, "≳ 10^77", not a number the model pins.
(b) The step that turns "10^77 trapped domains" into "10^77 child universes" is the unproved generalisation (L155 "not exactly proved yet") plus the "if all the false vacuum domains become wormholes" assumption (L331–332). Under the paper's own toy model only domains with aX_0 > 1 become wormholes; the rest are black holes (L124–129). No fraction is computed; "most" (L203–204) is asserted from (10/v)^1/3 > 1.
(c) Inputs assumed, not derived here: the GUT scale ρ_v = (10^15 GeV)^4 (L241–243 "a plausible model"); v itself is never computed from a potential (Coleman [10] is cited, no action evaluated); wall speed = c (L93–94), thin walls implicit; u_c = 0.3 from flat-space percolation (defended fn 1 L218–226 but note "the essential scenario … does not depend on the actual value of u_c" — true for the exponent, false for the O(1) prefactor).

## 2. "Present child radius > H_0^-1" — derived consistency or assertion? Identification or allowance?

Receipt L283–295: L ≲ (10/v)^1/3 exp(v^-1) l ≈ 10 cm; universe expands 10^28× after the transition (T_GUT/T_0 = 10^15 GeV / 10^-4 eV); "the present radius of a child universe is larger than H_0^-1 ≈ 10^28 cm … Thus there are no observational conflicts."

**Arithmetic.** 10^15 GeV = 10^24 eV; /10^-4 eV = 10^28 ✓ (with T_0 = 2.35×10^-4 eV it is 4×10^27). H_0^-1 = c/H_0 = 4.3 Gpc = 1.3×10^28 cm for H_0 = 70 ✓ (0.9–1.9×10^28 for the 1982 range 50–100). Present radius: 10 cm × 10^28 = 10^29 cm (paper) or 65–80 cm × 10^28 ≈ 10^30 cm (my eq-18 evaluation). Margin over H_0^-1: **10× (paper) to 60× (mine).**

**Status.** It is a *derived consistency statement* with inputs stated (ρ_v, v, T_GUT, T_0, H_0), not a bare assertion — but two soft spots:
- Eq 18 is an **upper bound** ("≲", L285). The conclusion "larger than H_0^-1" needs L within a factor ~10 of its bound. The paper does not say what sets the lower end (the trapped-domain radius spread, k in eq 13, spans 600× in mass ⇒ ~8× in radius).
- The 10^28 factor assumes adiabatic expansion from reheating at T_GUT. The paper's own problem #1 (L342–347: bubble-wall kinetic energy may not thermalise quickly) would lower the effective reheat temperature and shrink the factor; its problem #2 (evaporation entropy, L347–353) would *raise* it. Neither is folded in.
- **Identification vs allowance:** allowance only. "This length is large enough to regard our universe as such a child universe" (L288–289); "it might have been born as one of the child universes in this sequence" (L322–325, "might"). The mother and every child undergo the identical 60-e-fold transition, so nothing in the paper distinguishes the two cases observationally. "Thus there are no observational conflicts" (L294–295) is a non-conflict claim — the language of consistency, not of a prediction.

## 3. The n_B/s flag — route or number?

Exact text, L347–355: "Another is on the baryon-entropy ratio. When black holes and wormholes evaporate, a large amount of entropy is generated, which consequently reduces the baryon number to entropy ratio considerably. Thus, even if the ratio is initially of order unity, the evaporation may dilute the baryon excess too much to agree with observations. In order to avoid this difficulty, some new baryon-number generation mechanism might be necessary [15]. To judge the validity of the present result, more precise investigations … will be required." (L355–358.)

The earlier passages the sweep cited (L124–162, L283–358) contain the black-hole/wormhole formation and the child-radius argument; the only baryon-to-entropy sentence in the paper is the one above. I also grepped for every observation-facing term; nothing else.

**What it contains:** a named observable (n_B/s), a sign of the *effect* (evaporation entropy lowers it: "reduces … considerably", "dilute"), and the words "may … too much". **What it does not contain:** any factor, any inequality of the form n_B/s < X or S_after/S_before > Y, any reference to the observed value (10^-10 appears nowhere), and no statement of the initial ratio other than the hypothetical "even if … of order unity".

**Adversarial check — could the paper's own inputs fix a magnitude?** Partly, which is why it is a route. Lane-owned illustration (NOT in the paper): wormholes hold ~u_c ≈ 0.3 of the energy at percolation (L190) and evaporate at t_ev = 7×10^-13 k^3 s (eq 15); radiation reheated at ~t_c − τ* ≈ 60 l ≈ 10^-34 s redshifts while the wormhole population does not, so the population dominates from ~10^-33 s until evaporation; entropy injection ratio ≈ (ρ_wh/ρ_rad)^{3/4} at t_ev ≈ [(t_ev/10^-33 s)^{2/3}]^{3/4} = (t_ev/10^-33 s)^{1/2} ≈ **10^10 for k = 1, ≈10^6 for k = 1/600**. So the dilution factor lies somewhere in 10^6–10^10 across the paper's own free factor k, on lane assumptions (f, reheat time, k) the paper never makes. This is a **missing number** in the scheme's sense — the paper asserts no amplitude, and the lane may own a missing threshold but never a missing number — so it cannot lift the tier. Note too the arithmetic direction: 10^10 dilution of an O(1) initial ratio lands right at the observed 10^-10, so the authors' "may dilute … too much" is honest hedging, not a hidden inequality.

**Is there a derived sign on an observable?** The sign is derived relative to a *theory baseline* (the same GUT baryogenesis without evaporation), not relative to an observation: the paper does not say whether the observed n_B/s is high or low for this model, and it explicitly offers post-evaporation baryogenesis [15] as the fix (L353–355), which would erase any prediction. A directional claim that its authors immediately un-commit from is not QUALITATIVE-DIRECTIONAL; it is a named observable with no amplitude — the definition Duho's 47a ruling placed at PROSPECT. Also note the flag is a *liability* of the model, not a prediction of the multi-production content: the 10^77 children are by construction spatially disconnected (fn 2, L272–276) and unobservable.

## 4. Anything else observation-facing?

- **Black holes** (aX_0 < 1 branch, L124–129, L142–148): mass M < (4π/3)ρ_v l^3 ≈ 3×10^2 g, evaporation time ∝ M^3 ⇒ < 10^-17 s. Wormhole masses 40 g – 2×10^4 g (eq 13 with v/10 < k < 1) evaporate in ≤ 7×10^-13 s (eq 15). **No relic population** today (relic PBHs need M ≳ 10^15 g); the paper never claims one. **No mass function** — only a "typical" mass with a 600× uncertainty factor k; the k-range is a spread, not a distribution.
- **Gravitational-wave background:** absent. "gravitational" and "wave" do not occur in the text.
- **Galaxy seeds, monopole suppression, matter–antimatter domains** (L19–24): introduction citations of [1], [5–7], [1,9] — context, not developed here.
- The only observation-facing statement is the non-conflict of Q2 (L294–295).

## 5. Tier consequence, argued

- **CALIBRATED-FALSIFIER:** no. No number on any observable; 10^77 is a floor on an unobservable (disconnected) population and is set by the imported N = 60.
- **QUALITATIVE-DIRECTIONAL:** no. The only sign (evaporation lowers n_B/s) is relative to a theory baseline, has no stated amplitude, and is disowned in the next sentence via [15]. A derived sign that the authors decline to commit to cannot be the lane's directional falsifier.
- **CONSISTENCY-ONLY (the case for a downgrade, recorded for the packet):** the sole observation-facing claim is "no observational conflicts" (Q2); the n_B/s remark is a self-flagged liability with an escape hatch, not a test of the multi-production content, which is unobservable by construction (fn 2). A reader could say the paper's contact with observation is entirely consistency.
- **PROSPECT holds (my verdict):** the n_B/s remark is more than a consistency statement because its magnitude is *computable from the paper's own inputs* (ρ_v, v, u_c, k, t_ev, t_c are all stated) — my lane-owned illustration shows the paper's inputs bracket the dilution to 10^6–10^10 — the paper just never did it. That is exactly a route with a named observable and no amplitude, which is the PROSPECT definition under ruling 47a. The scheme's "never a missing number" rule blocks promotion; the existence of a calculable route blocks the downgrade. **Tier unchanged; no tier-adjacent packet needed.**

**Record corrections (not tier changes), for Tori:** (i) annotate "~10^77" as "≳ 10^77 (= e^{3N}/3 with N = 1/v = 60 e-folds imported from the homogeneity condition, L206–214; v = 1/60 is the maximum allowed, so the count is a floor)"; (ii) the "present child radius > H_0^-1" line rests on an upper bound (eq 18 "≲") with a 10–60× margin, and identifies our universe as a child only permissively ("might", L322–325); (iii) the n_B/s flag is the paper's *problem #2*, stated with a sign but no amplitude and with [15] as the authors' own escape (L347–355).

## Plain language

This 1982 paper says: if the early universe went through a violent "boiling" change of its vacuum, pockets of old vacuum get trapped, pinch off, and become separate baby universes — and it counts about 10^77 of them per parent. I checked the count. It really does follow from the paper's equations, but almost everything cancels and the whole number is just "e to the 180, divided by 3", where 180 = 3 × 60, and 60 is the number of doublings the authors *borrowed* from the requirement that our universe look smooth. If that borrowed number were 61 instead of 60 the count is twenty times bigger; the model itself only says "at least this many". The baby universes are cut off from us, so they cannot be seen. The paper then says our universe could be one of the babies — the numbers allow it (a baby would be at least ten times bigger than what we can see today), but nothing in the paper says it *is*. The one place the paper touches something we can measure is a worry it raises against itself: the tiny black holes left over would evaporate and flood the universe with heat, which would wash out the matter-over-antimatter excess "too much" — but it gives no number for how much, says maybe some other process fixes it, and calls for more study. I can rough out from its own inputs that the wash-out would be a factor of a million to ten billion, which is why the worry is real, but the paper does not do that sum, and the lane's rules say we cannot do it for them to raise the tier. So the entry stays where Duho put it: a real lead with a named measurable quantity and no number attached.
