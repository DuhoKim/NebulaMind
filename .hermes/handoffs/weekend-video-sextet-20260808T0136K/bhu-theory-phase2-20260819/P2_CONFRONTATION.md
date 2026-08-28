# P2 Track B step 3 — confrontation: does any finite-amplitude signature survive?

**claude-seat (science seat), 2026-08-19, under `PHASE2_BRIEF.md` Track B(3).** Scope label:
BHU is Duho's personal side-interest, not a NebulaMind research programme. External-theorist
review required before any publication claim. All three gates honored (Stage 1 conditions 1–5;
bounce flags 1–4; inherit nits N1–N3 — the gate-corrected sliver values are used, not the
doc-rounded ones). Receipts (prefix p2b3, outputs alongside): `p2b3_bbn_confront.py` (B3-R1),
`p2b3_stack.py` (B3-R2). Fetches this step: ar5iv.org and api.crossref.org only (one new
pinned source, §2); portal.nersc.gov untouched.

## 0. The honest headline (first, plain, unsoftened)

**No finite-amplitude signature of the Popławski chain survives at observable magnitude.
Nothing in this confrontation comes within four orders of magnitude of any floor any
instrument could ever reach, and the best-motivated reading puts the one candidate signal
seventy orders below it.** Specifically: (i) the chain's only calibrated relic, the torsion
density Ω_S, sits **44–46 orders of magnitude below** the one named published bound on
a⁻⁶ components (BBN stiff-fluid, §2) — consistent, and unobservably so; (ii) the
rotating-parent handedness signal, carried through the derived Phase 2 ceiling under the most
generous defensible stacking, is **A ≤ 6×10⁻¹² (Treatment I) / 5×10⁻¹¹ (Treatment II)** —
10⁻⁵–10⁻⁴ of the 1σ counting floor of a perfect all-galaxy survey; under the
angular-momentum-conservation stacking it is **A ≤ 10⁻⁷⁶** (§4); (iii) every other derived
quantity is either untestable in principle (bounce states behind the parent horizon) or
consistency-only (the M→size channel). The conditions this verdict rests on are themselves
part of the finding: every quantity carries the V1 Planck-regime caveat (the chain's bounces
are classical calculations in a quantum-gravity regime), the torsion normalization carries
the V2 undischarged averaging assumption, and the axis-memory question remains UNDETERMINED
because the chain's isotropization rests on an underived heuristic (§5). **If the published
Popławski chain is taken exactly as published and pushed as generously as its own mechanics
allow, it predicts nothing that any survey, present or physically possible, could detect.**

## 1. Confrontation table (requirement 1; treatment named per row; V-markers per row)

| # | Derived quantity (source) | Value | Best published bound | Verdict |
|---|---|---|---|---|
| 1 | Ω_S bracket (B1; Treatment I bookkeeping) [V1,V2] | −8.8×10⁻⁷⁰ … −1.5×10⁻⁷⁰ | BBN stiff-fluid: ρ_S10/ρ_R10 < 30 at 10 MeV (§2 pin) | **CONSISTENT** — \|ε_S/ε_R\|(10 MeV) = 1.8×10⁻⁴⁴ … 3.0×10⁻⁴⁵; margin 10⁴⁵–10⁴⁶ (B3-R1) |
| 2 | Treatment I bounce state (T_max = 1.152×10³² K, ε_b = 7.1×10¹¹⁴ J/m³; A2-certified/B1) [V1,V2] | — | none exists: interior to the parent horizon, pre-BBN | **UNTESTABLE** (the chain itself says the interior is invisible from outside — A2 §5) |
| 3 | Treatment II bounce state (T_cr = 0.785 m_P) [V1,V2,V3] | — | none exists | **UNTESTABLE** (+ cusp prescription V3) |
| 4 | Spin-inheritance ceiling ε_max = ξc²R_b/(a★GM), ∝ M^(−2/3) (B2) [V1; both treatments] | 1.5×10⁻²⁷ (I) / 1.4×10⁻²⁶ (II) at 10 M☉, a★ = 0.7; 10⁻³³–10⁻³² supermassive | not an observable — a derived bound on a parameter | **NOT-AN-OBSERVABLE** — feeds the stack (§4); its testable consequence is the absence it enforces |
| 5 | Polarization sliver (gate-corrected: 5.1×10⁻¹³ (I), 2.9×10⁻¹³ (II) matched-input per nit N2; B3-R2 recomputed) [V1] | ≤ 10⁻¹² | no published bound on interior spin polarization exists | **UNTESTABLE** (and negligible by ~12 orders against even order-unity effects) |
| 6 | Frozen-ratio shear theorem (B2) [V2-independent, exponent statement] | a condition, not an amplitude | — | **CONDITION** — see §5; not convertible to a number |
| 7 | M→size channel: a₀T₀ ∝ χ^(3/4)M^(1/2); a₀, R₀, T₀ exact (B2) [V1] | — | flatness/size data cannot identify parentage (Phase 0 Route C; A2 §5 table) | **CONSISTENCY-ONLY** |
| 8 | Stacked handedness amplitude (§4) [V1,V2; both treatments; both stack forms] | A ≤ 6×10⁻¹² / 5×10⁻¹¹ (Stack A); ≤ 10⁻⁷⁶ (Stack B) | all-sky sample-complete 1σ floor σ_A = 7.07×10⁻⁷ (Phase 0/1 pins, reused: `../bhu-theory-phase1-20260819/CONFRONTATION_AND_INVERSION.md`) | **RULED-OUT-AS-OBSERVABLE** — the signal *budget* is 10⁻⁵–10⁻⁴ of the noise floor at best (this rules out detection, not the scenario) |

No new observables were invented at this step (requirement 6); rows 1–8 exhaust the derived
quantities of steps 1–2 plus the mandated stack.

## 2. The pinned a⁻⁶ bound (Gate 1 condition 1 — CLOSED for this row)

**Named publication, acquired and pinned this step:** S. Dutta & R. J. Scherrer, *"Big bang
nucleosynthesis with a stiff fluid,"* **Phys. Rev. D 82, 083501 (2010)**, DOI
10.1103/PhysRevD.82.083501 — Crossref-verified this session
(`sources/crossref_prd82_stiff.json`); full text `sources/ar5iv_1006.4166.html`, SHA-256
`f99cd41924258887be309706fe2dc4fd58de34f666b983fafe83a885f781fe22`. Verbatim, from the pinned
text: *"Models that lead to a cosmological stiff fluid component, with a density ρ_S that
scales as a⁻⁶ … have been proposed recently in a variety of contexts."* and *"we obtain the
bound ρ_S10/ρ_R10 < 30"* (their Eq. 9; ρ_S10, ρ_R10 the stiff and relativistic densities at
T = 10 MeV, from the primordial ⁴He abundance with the WMAP7 η).

**Sign caveat, stated:** the bound is derived for a *positive* stiff component; the torsion
term is *negative* with the same a⁻⁶ scaling (it slows rather than speeds the expansion). At
44+ orders below the bound's magnitude, the distinction is academic — a component of this
absolute size is invisible to BBN either way — but the row's CONSISTENT verdict is a
magnitude statement, not a sign-exact one. The excluded Goru quotes remain excluded; this row
rests solely on the pin above. No other CMB/BBN claim is made anywhere in this document, so no
other row required a new bound; rows 2–3 and 5 are UNTESTABLE for structural reasons
(interior quantities), not for lack of a bound — no UNCONFRONTED-NO-PINNED-BOUND rows remain.

## 3. Reused pins (paths, per requirement)

From `../bhu-theory-phase1-20260819/CONFRONTATION_AND_INVERSION.md` (gate-passed, post-repair
hash `2d662a5f…`): the S2 rotation bound ω_max,0 = 1.66×10⁻²⁷ s⁻¹; Ω_H(10 M☉, 0.7) =
4.144×10³ s⁻¹; the derived transfer coefficient C = 7.19 [1.36, 12.78] and the z_ta = 3
mapping factor 3.50; the floors σ_A = 3.16×10⁻³ (design; 3σ 9.5×10⁻³) and 7.07×10⁻⁷
(all-sky). From this lane: ε_max, R_b, bounce states (B1/B2 receipts, gate-passed).

## 4. The stack, quantified (requirement 3; receipts B3-R2)

**Stack A — spec-chain form (maximally generous).** ω₀ ≤ (εf_b)_max·Ω_H/D with
(εf_b) ≤ ε_max (the B2 ceiling applies to the product — B2 A5 row, inherit-gate note),
D ≥ Z_mat² = (1+3400)² alone (Z_rad, Z_inf ≥ 1 dropped in the signal's favor; z_eq flagged
standard). Result: ω₀ ≤ 5.4×10⁻³¹ s⁻¹ (I) / 4.9×10⁻³⁰ (II); through the Phase 1 gated
transfer A = C·(ω/H)(z_ta):

  **A ≤ 6.0×10⁻¹² (I) / 5.4×10⁻¹¹ (II)** (C-bracket tops: 1.1×10⁻¹¹ / 9.6×10⁻¹¹)
  → **8.5×10⁻⁶ / 7.6×10⁻⁵ of the all-sky 1σ floor**; 6×10⁻¹⁰ / 6×10⁻⁹ of the design 3σ floor.

**Stack B — angular-momentum form (no D, fewer assumptions).** With L conserved after the
bounce (spec A2/A7, named) and J_b ≤ ξMcR_b: today ω₀ = J_b/I_today with
I_today = ξM_univ a₀² (closed 3-sphere at critical density, a₀ = 2.95×10²⁷ m; a
Hubble-volume-only inertia would only *raise* ω₀ — the choice is conservative):

  **A ≤ 6.3×10⁻⁷⁷ (I) / 5.7×10⁻⁷⁶ (II)** for a 10 M☉ parent; supermassive parents give
  ω₀ ≤ 10⁻⁸⁵ despite J_b ∝ M^(4/3).

The two stacks differ by 65 orders because Stack A lets the spec's parameterized dilution
absorb the bounce-to-today mismatch while Stack B integrates it away; **the signal budget is
bounded by whichever stacking one defends, and both are unobservable** — the *most favorable
defensible* reading is 10⁻⁵ of a perfect survey's noise. For comparison: Phase 1's
generous-bound signal (no ceiling) was A ≈ 1.9×10⁻⁸; the Phase 2 ceiling cuts that budget by
a further **≥3.5 orders** (Stack A) — the strict treatment moves the verdict monotonically
away from observability, again. The sliver channel (row 5) is 5.1×10⁻¹³/2.9×10⁻¹³ at the
bounce patch itself, before any dilution — nothing there either.

**"Observable by what":** nothing. The smallest relevant floor any instrument could ever
reach is the sample-complete all-sky counting floor σ_A = 7.07×10⁻⁷ (there are no more
galaxies than all of them); the best-case stacked signal is 10⁻⁵ of it. No named instrument
bound (BBN §2 included, margin 10⁴⁵) comes within tens of orders of any derived quantity.

## 5. The frozen-ratio condition and axis memory (requirement 4 — condition, not amplitude)

The B2 theorem (shear and torsion terms both ∝ a⁻⁶; ratio frozen; bounce exists only if
shear is already subdominant) does exactly two things to the axis-memory story, and no more:
(i) it removes the chain's "the bounce isotropizes" language — the bounce mechanism performs
**zero** isotropization, so any parent-axis anisotropy that enters the bounce exits it at the
same fractional level; (ii) it therefore hangs the entire question — does axis memory survive
to observability, or is it erased? — on the particle-production step, which the published
chain treats heuristically (A2 row B-13) and which no gated document derives. **Axis memory:
UNDETERMINED, in both directions.** This is a condition on any future claim, not a number: it
neither adds an amplitude to row 8 nor rescues one, and this document does not convert it.

## 6. Validity markers (requirement 5, summarized; per-row markers in §1)

**V1** on every bounce-anchored quantity (rows 1–5, 8): all descend from classical states at
or above the Planck scale — the strict model's own regime caveat, carried since B1;
Gate-flag 2 honored (incoherent edges shown, never dropped). **V2** on rows 1–3, 8 through
the torsion normalization (×6 coherence bracket carried in row 1's spread; the frozen-ratio
theorem itself is exponent-only and bracket-independent). **V3** on row 3 and row 8's
Treatment II branch. **V5** (erratum metadata-only) unchanged — no row descends from a
quarantined printed number.

## 7. What this closes and what it does not

This confrontation completes the Phase 2 mission statement: the published Popławski chain,
audited equation-by-equation, re-derived strictly, and pushed through its own mechanics with
every lever set generously, **yields no finite-amplitude signature that any physically
possible observation could detect** — the honest answer to "does ANY survive" is **no**, with
the two structural escapes named: a derived particle-production isotropization calculation
(would settle §5's UNDETERMINED either way) and a quantum-gravity completion of the bounce
(would discharge V1, in either direction). It does **not** falsify BHU (family boundary,
standing since V11/C02), does not test the wider family, and does not touch the spin-parity
measurement, which continues on its own merits.

— claude-seat, Track B step 3, 2026-08-19. Receipts p2b3_* run clean this session; one new
pinned source (§2); fetches from ar5iv.org and api.crossref.org only. Gate:
`MIRU_P2_CONFRONT_GATE.md` expected next, then `PHASE2_SUMMARY.md`.
