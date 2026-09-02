AUDIT_HOLDS_CONSISTENCY_ONLY

# Entry 19 — Dymnikova (2019) *Universe* 5, 111 — claude-seat DEEP RESULT (blind double)

**Seat:** claude-seat (Fable 5.1). **Written:** 2026-09-02 20:45 KST. **Brief:** `ENTRY19_AUDIT_BRIEF_20260902.md` (Tori, STEP 3, queue draw #21).
**Source read in full:** `../bhu-reading-20260823/sources/dymnikova_2019_universe_clean.txt` (1,333 lines; lines cited as L#).
**Blind discipline:** no `ENTRY19_*RESULT*` file, no codex/kimi file opened. For axis 5 only, the statement of Easson's
Proposition 2 was taken from this seat's own prior gate (`CGATE_B24_VERDICT.md` L40–44) and the lane brief
`RQ_D_MAPPING_BRIEF_20260831.md` L18–19 (neither is an entry-19 result). No other file was read.
**Method:** every equation in Section 3 was re-derived by hand from (4), (7) and (11); discrepancies are reported below.

---

## 1. The construction — what is built here, what is imported

**Parent (regular ΛBH), all imported.** Metric (2) `ds² = (1 − R_g(r)/r)dt² − dr²/(1 − R_g(r)/r) − r²dΩ²`, `R_g = 2GM(r)` (L198–218);
mass function (3) (L222–228); asymptotics (4): `M < ∞`, `R_g(r→∞) = r_g`, `R_g(r→0) = r³/r0²`, `r0² = 3c²/(8πGρ0)` (L236–250);
the explicit profile `ρ(r) = ρ0 exp(−r³/r0²r_g)` (L252–254) is the 1992 solution, ref. [14] = entry 18 (L1224–1225).
The source algebra `T^r_r = T^t_t` (1) (L166–168), pressures (5) `p_r = −ρ, p_⊥ = −ρ − (r/2)dρ/dr` (L263–271), WEC/Type I
(L255–258), two horizons `r±` for `M > M_crit` (L277–280) — all cited to [14,24,26]. **Nothing in Section 2 is new.**
The Penrose diagram (Fig. 2) with "an infinite sequence of black and white holes" and regular cores RC (L541–545) and the
"traveling to other universes" remark (L585–588, ref. [29]) are also imported.

**Daughter (Section 3) — a de Sitter-space minisuperspace tunnelling calculation transplanted into RC.**
- Friedmann equation in conformal time (6): `(da/dη)² = 8πGρa⁴/3c² − ka²` (L812–823).
- WDW reduced to Schrödinger form (7): `(ħ²/2m_Pl) d²ψ/da² − U(a)ψ = 0`, `U(a) = (m_Pl c²/2l_Pl²)(ka² − 8πGρa⁴/3c²)` (L840–855).
- Closed-from-"nothing" potential (8): `U = (m_Pl c²/2l_Pl²)(a² − a⁴/r0²)` (L861–869); penetration factor (9)
  `D1 = exp[−(2/3)(r0/l_Pl)²] = exp[−(2/3)×10¹⁶]` at the GUT scale (L877–892). **Checked:** `r0/l_Pl ~ (M_Pl/E_GUT)² = 10⁸` → 10¹⁶ ✓.
- Extended matter content (10)–(11): `ρ = ρ0[1 + B_s r0²/a² + B_γ r0⁴/a⁴]` — radiation `p = ρ/3` and strings `p = −ρ/3` (L898–922), ref. [48].
- Potential and energy (13): `U = (m_Pl c²/2l_Pl²)[(k − B_s)a² − a⁴/r0²]`, `E = (B_γ/2)(r0/l_Pl)² E_Pl` (L930–952).
  **Re-derived:** insert (11) into (7) and use `8πGρ0/3c² = 1/r0²` from (4); the `B_γ` term is a constant
  `−(m_Pl c²/2)(r0/l_Pl)²B_γ` which moves to the right-hand side as `E` ✓. Equation (13) is exactly right.
- Levels (14): `E_n ≃ E_Pl √(k − B_s)(n + ½)` (L1036–1048). **Re-derived:** the well bottom is harmonic with
  `ħω = ħc√(k−B_s)/l_Pl = E_Pl√(k−B_s)` ✓.
- WKB penetration (15) (L1050–1066), and (16): `D2 = exp[−(2/3)(r0/l_Pl)²(k − B_s)^{3/2} + (2n+1) + I]`, `I < 10⁻²(2n+1)` (L1073–1097).
  **Re-derived** the leading term: `(2/ħ)∫₀^{a₂} √(2m_Pl U) da` with `a₂ = r0√(k−B_s)` gives exactly `(2/3)(r0/l_Pl)²(k−B_s)^{3/2}` ✓
  (reduces to (9) for `k = 1, B_s = 0` ✓). The `+(2n+1)` correction is order-of-magnitude plausible (log-divergent
  under-barrier time at `a→0`); its coefficient is not derivable from this text (ref. [48]).
- Level-count constraint (17): `n + ½ < (k−B_s)^{3/2}(r0/l_Pl)²/(π√2)` (L1097–1116). **Re-derived** from `E_n ≤ U_max`
  via the paper's own Bohr–Sommerfeld normalisation (14) with `U_max − U = (m_Pl c²/2l_Pl² r0²)(a² − a_max²)²`: I get the
  constant `2/(3π√2) ≈ 0.150`, the paper prints `1/(π√2) ≈ 0.225` — a factor 3/2 in a counting constant, immaterial to
  any conclusion.
- Final number (18): `D3 = exp[−(2/3)×10⁷]` "for all values of k" (L1131–1143). **Re-derived:** with `(k−B_s) = 3×10⁻⁶`
  (L1120) the leading term is `(2/3)×10¹⁶×5.2×10⁻⁹ = (2/3)×5.2×10⁷`; the printed `(2/3)×10⁷` corresponds to `(k−B_s) = 10⁻⁶`
  (L1120 "around 10⁻⁶"). Internally consistent at order of magnitude; the `n`-dependence is silently dropped
  (n up to ~10⁷ is allowed by (17), and `(2n+1)` is then comparable to the leading term).

**Free inputs, stated explicitly.**
(i) `k ∈ {0, ±1}` — a chosen label, never derived (L1121–1130). (ii) `Λ_core`, i.e. `r0` (equivalently `ρ0`) — fixed
by *assuming* the GUT scale, `r0/l_Pl = 10⁸` (L892). (iii) `B_s` — free; only the combination `(k − B_s)` is
constrained, and that from an *imported* observational bound `ΔT/T ≤ 10⁻⁵ "as in our Universe"` cited to [48]
(L1118–1120); the link ΔT/T ↔ (k−B_s) is not derived in this paper. (iv) `B_γ` (equivalently `E`, `n`) — free
within (17); the value of `n` used in (18) is unstated. (v) The matter content of the fluctuation itself
(radiation + strings with `p = −ρ/3`) is a modelling premise (L900–903).

**Where the black hole actually enters.** Equations (6)–(18) contain no trace of the parent metric (2): they are a
homogeneous FRW minisuperspace with vacuum density `ρ0`. The ΛBH enters only (a) by supplying `ρ0`/`r0` through (4),
and (b) by the global-structure claim that there are infinitely many RC arenas (L596–600, L616–619, L1146–1147).
The daughter's scale factor `a` is never related to the parent's `r`; no junction, matching, or embedding is written.
The RC region is only *asymptotically* de Sitter as `r→0` (L543–544) — the homogeneous-vacuum minisuperspace
idealises away the profile `ρ(r)`. Not mentioned anywhere: the Cauchy-horizon (`r−`) instability on which the
"infinite sequence" of Fig. 2 rests.

## 2. Derived vs premised; the "favours a FLAT birth" claim — CONFIRMED as the paper's conclusion, REFUTED as a probability preference

- **Premised:** the de Sitter interior (Section 2, all imported), the string/radiation content, the GUT scale, the ΔT/T value.
- **Derived (within the WKB minisuperspace):** a *nonzero* tunnelling probability, (16) → (18), `D3 = exp[−(2/3)×10⁷]`,
  given the inputs above. So "birth of a universe" is a derived number in the sense the brief asks — but it is a
  WKB estimate in a model whose parameters are all set by hand or imported.
- **The flat preference, with equation and line.** The record's paraphrase is correct as to what the paper *says*:
  L1128–1130 "(3) A flat universe, k = 0; B_s ≃ −3×10⁻⁶ ... This case is favored by the fact that the strings content is
  very small"; L1144–1145 "The most plausible case is the birth of a flat (Ω = 1) universe distinguished by the fact
  that, in this case, the very small admixture of strings is sufficient"; L1175–1177 (Conclusions) restates it; abstract L20–23.
- **But the mechanism is parsimony, not probability.** Equation (16) depends on `k` *only* through `(k − B_s)`, and
  `(k − B_s)` is fixed at ~10⁻⁶ by the ΔT/T constraint *before* `k` is chosen (L1118–1120). Hence the tunnelling
  probability (18) is **identical for k = 0, ±1** — the paper says so itself: "for all values of k" (L1142).
  The three cases (L1123–1130) differ only in how much string matter is required: `|B_s| ≈ 1` for k = ±1
  ("comparable with ρ0", L1124–1125, L1127) versus `|B_s| ≈ 3×10⁻⁶` for k = 0 ("ρ_s ≪ ρ0", L1129).
  So the model does **not** compute that flat births are more probable; it *prefers* flat because flat needs the
  least exotic ingredient. There is no likelihood ratio, no measure over `B_s`, and no prior stated.
- **Adversarial note on the word "flat".** In all three cases the effective curvature term in (6)/(13) is
  `−(k − B_s)a²` with `(k − B_s) > 0`: dynamically every daughter is born slightly *closed-mimicking* (the strings
  "mimic the positive curvature behavior", L955–956); "Ω = 1" (L1144) refers to the geometric label `k = 0` only.
  Nothing in the paper turns this into a present-day `Ω_k` for any daughter.

**Verdict on axis 2:** "the model favours a FLAT birth" is a faithful quotation of the paper's stated conclusion
(L1128–1130, L1144, L1175), but it is a naturalness ranking, not a derived preference of the dynamics; the
computed probability is `k`-independent by construction (L1142).

## 3. The claim-level exclusion (flat/open need sufficiently negative B_s) — DERIVED at the level of (13), inequality stated

From (13), `U(a) = A[(k − B_s)a² − a⁴/r0²]`, `A = m_Pl c²/2l_Pl² > 0`. `U` has a maximum at `a_max² = (k − B_s)r0²/2`,
`U_max = A(k − B_s)²r0²/4`, **iff `(k − B_s) > 0`**. That is the whole inequality:
- `k = 0`: barrier iff `B_s < 0`;
- `k = −1`: barrier iff `B_s < −1`;
- `k = 1`: barrier for any `B_s < 1` (including `B_s = 0`, which is (8)–(9)).
The paper states this in words (L953–958: a negative `B_s` "mimics the positive curvature behavior and provides
the appearance in (7) of a barrier, in the cases k = 0 and k = −1") and implements it numerically in the three
cases (L1123–1130: `B_s ≃ −(1 + 3×10⁻⁶)` for open, `B_s ≃ −3×10⁻⁶` for flat). It does not print the inequality,
but it is a one-line consequence of (13), which I have verified from (7) + (11) + (4). A second, weaker
condition is also needed for tunnelling to be meaningful — a level below the barrier top, `E_n < U_max`, which
is (17). So: **derived, given the premise that the only curvature-mimicking component is a `p = −ρ/3` fluid.**
"Sufficiently negative" means `B_s < −k` exactly, plus (17); the *magnitude* 10⁻⁶ is imported from ΔT/T, not derived.

## 4. Observation-facing content for OUR universe — possibility statement only; the one observational number is an INPUT

- The only observational quantity in the paper, `ΔT/T ≤ 10⁻⁵`, is used as an **input** to fix `(k − B_s)`
  (L1118–1120: "The observational constraint on the model parameter (k − B_s) is needed to estimate the probability
  (16), for example by ΔT/T ≤ 10⁻⁵, as in our Universe"; repeated L1169–1171). It is not a prediction.
- Identification: L1178–1181 "The probability of the quantum birth of baby universes inside a Λ black hole is not
  negligible, due to the existence of an infinite number of the appropriate RC regions inside a particular ΛBH.
  All this makes it possible to speculate (at least not exclude) that our Universe could be located inside some
  regular black hole with the de Sitter interior." — explicitly a speculation / non-exclusion. "Not negligible"
  is `∞ × exp[−(2/3)×10⁷]` (L1146–1147, L1178–1179): no rate per RC region, no measure, no number — asserted.
- Curvature sign: none predicted; k is free, all three allowed with equal (18); flat merely "most plausible" by parsimony (§2).
- Λ: only the *inflationary* vacuum `r0` (GUT scale, assumed, L892); nothing on a daughter's late-time Λ.
- Relic / threshold: none. The string admixture `|B_s| ~ 3×10⁻⁶` redshifts as `a⁻²`, i.e. exactly like curvature
  (L953–956), so it is degenerate with `k` in the expansion history and is not offered as an observable.
**Nothing in the paper can be falsified by any measurement of our universe; there is no threshold the lane could own.**

## 5. Easson map (entry 22, Proposition 2) — INAPPLICABLE; neither restricting nor sparing on the merits

Proposition 2 (per this seat's B24 gate and the mapping brief) bounds **nondegenerate, comoving, no-shell,
closed-FRW daughters** of **static, asymptotically flat, finite-ADM** parents: with `F(R)→1`, the comoving boundary
obeys `Ṙ_b² = E − F(R_b) ≥ 0` with `E = cos²ψ_b < 1`, which fails at large `R_b`; independent of the regular-core
details, and surviving a static redshift function.

Applied to entry 19 on its own hypotheses:
- **Parent-side hypotheses are all met.** Metric (2) is static; `R_g(r→∞) = r_g` and `M < ∞` (L236–250) give
  asymptotic flatness and finite ADM mass; the de Sitter core is precisely the regular-core detail Prop. 2 is
  independent of. So the *regular core buys no escape*.
- **Daughter-side hypotheses are not instantiated — that is the whole reason it is inapplicable.** The paper's
  daughters (both the closed one of Fig. 3-left, L596–600, L1158–1160, and the open/flat ones of Fig. 3-right,
  L604–619) are minisuperspace WDW wave functions tunnelling in a homogeneous de Sitter vacuum (7)–(18). No comoving
  2-sphere boundary in the parent, no matching of `a` to `r`, no no-shell junction is ever written; the nucleating
  bubble carries a quantised energy `E_n ≠ 0` (L1131–1141) and is a quantum object with no classical FRW embedding
  in the parent's coordinates. Prop. 2's antecedent (a classical comoving closed-FRW region of the static parent)
  simply does not occur in the paper.
- **Contrapositive reading.** Prop. 2 says a classical no-shell closed-FRW daughter of such a parent cannot grow
  unboundedly. Entry 19 never attempts that route; it uses quantum tunnelling (the nucleation of a bubble, the very
  mechanism of Farhi–Guth–Guven [5], L133–136, which is a *shell*/wall construction — an author-named Easson escape
  route). So entry 19 is consistent with Prop. 2 in the trivial sense that it lives outside its domain; but Prop. 2
  does not "spare" it either, because the paper makes no statement at all about how a born daughter is embedded in,
  or exits, the parent geometry — the one thing Prop. 2 is about.
- The flat/open daughters are outside Prop. 2's closed-only scope in any case (they would fall to Theorem 1's limb
  with its extra ANEC/regularity assumptions), and again are not comoving no-shell FRW regions of the parent.
**Answer: INAPPLICABLE.** If anyone later tries to give the Fig. 3-left "closed world closing the BH sequence"
(L1158–1160) a classical no-shell comoving realisation inside the ΛBH, Prop. 2 bounds it; the paper does not do so.

## 6. Tier consequence, argued

- **CALIBRATED-FALSIFIER:** no — no observable, no threshold, no identification beyond "speculate (at least not exclude)" (L1180).
- **PROSPECT:** no — nothing is proposed as a future test; the one observational number (ΔT/T) is consumed as an input.
- **QUALITATIVE-DIRECTIONAL:** no — the only candidate direction, "flat" (L1144, L1175), is a parsimony ranking whose
  computed probability is explicitly `k`-independent (L1142); the model's only curvature-related number,
  `(k − B_s) ≈ 10⁻⁶`, is the same in all three cases. The lane could own a missing *threshold* but not a missing
  *number*, and here there is no number that separates the directions.
- **THEORETICAL-OBSTRUCTION:** no — it is an existence/possibility argument, not an impossibility over a stated domain.
- **CONSISTENCY-ONLY:** yes — the paper shows that a WKB minisuperspace tunnelling with an assumed string admixture
  yields a nonzero (though `exp[−10⁷]`-small) birth probability, in a spacetime whose regular interior is premised
  from entry 18, and concludes with a non-exclusion of our universe being such a daughter.
**Tier held: CONSISTENCY-ONLY. A(a): no tier change requested; no packet to Duho.**
Minor findings for the record (no tier weight): factor-3/2 constant in (17); (18) corresponds to `(k − B_s) = 10⁻⁶`
rather than the `3×10⁻⁶` chosen at L1120; the `n`-dependence of (16) is dropped in (18); the Cauchy-horizon
instability of the Fig. 2 "infinite sequence" is unaddressed.

---

**Plain language.** This paper takes Dymnikova's own 1992 black hole, whose centre is a smooth de Sitter vacuum instead of
a singularity, and asks whether a new universe could pop out of that centre by quantum tunnelling. It answers "yes, with
a tiny probability", but every knob is set by hand: the interior is assumed, the energy scale is assumed, and the one
number taken from observation (the smoothness of the microwave sky in *our* universe) is used to tune the model, not to
test it. The headline that a *flat* baby universe is "most plausible" is real, but it does not come from the
probability formula — which gives the same answer for flat, open and closed — it comes from flat needing the least
exotic ingredient (a whisper of "strings" with negative tension instead of a full dose). The paper ends by saying one
"cannot exclude" that we live inside such a black hole, which is a possibility, not a prediction. Easson's no-go does not
bite because the paper never actually joins the baby universe to the parent black hole — the one step that no-go is
about. The tier stays where it was: a consistency argument, nothing observable to check.
