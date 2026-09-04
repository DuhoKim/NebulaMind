# K3 step 2 — FROZEN PRE-REGISTRATION: does an exchange correlation restore an n² spin-density term?

**Tori, 2026-09-04 10:07 KST. Version 1. Status: FROZEN pending the fresh referee gate; ORDERED by Duho ("k3s2", relayed by Blanc 2026-09-04 09:57 KST).**

Predecessor: `K3S2_EXCHANGE_PREREG_DRAFT_20260903.md` (DRAFT — NOT ORDERED), gated `PREREG_SOUND_WITH_REPAIRS` on 2026-09-03 20:20 KST
(`K3S2_DRAFT_GATE_agy.md`, agy via `nm_referee_dispatch.sh`, ACCESS PROVEN). Its three repairs are applied and were re-verified
clause by clause on 2026-09-04 09:58 KST. This version is the draft plus the five binding requirements of Duho's order; no
requirement of the draft is weakened, and the four draft outcome classes survive with two added.

No derivation has been run. Nothing below may be revised once the gate returns; a defect found later is an amendment with its own
record, not an edit.

---

## 0. What this is for, and what it cannot do

K3 step 1 (`K3S1_RESULT_20260903.md`, 3 seats / 2 methods, unanimous) filed **CLOSURE_SCALING_FAILS**: for N uncorrelated, randomly
oriented spin-½ particles the ensemble average of the squared macroscopic spin density is linear in n, so neither printed closure —
`⅛ n²` (entry 10 L121) nor `¾ n²` (entry 10 L113) — follows from the unpolarized average.

`K3S1_WHAT_A_CRITIC_GETS_20260904.md` states the one surviving objection: that result answers the **uncorrelated product ensemble**
it preregistered, which may not be the quantum operator and state Einstein–Cartan theory needs. For identical fermions an
unpolarized one-body state does not by itself make the coincident two-body expectation factorize.

**This step therefore tests the objection, not the conclusion.** It can strengthen `CLOSURE_SCALING_FAILS`, narrow it, overturn it,
or find it undecidable without a prescription the sources do not fix. It cannot move a tier, a warrant token, a standing or a stamp;
those are Duho's, and this preregistration proposes annotations only after he rules.

---

## 1. Objects, every symbol bound, with sign, projection and normalisation

All operators are those of entry 10 (`1111.4595v2_poplawski_prd85_clean.txt`); units `ℏ = c = k_B = 1` as the source declares
(L70–71), restored in C5. Metric signature and the Levi-Civita convention are pinned at step 1 from the source's own equations and
recorded in the pin sheet before any evaluation; the seats state them in their scripts.

**O1 — the Dirac spin pseudovector.** `s^i = ½ ψ̄ γ^i γ⁵ ψ` — entry 10 Eq. (4), L73–78. The factor ½ is the source's, not ours; it
 renders on L74 and L76 because the source PDF splits the fraction across the equation line L75.

**O2 — the completely antisymmetric Dirac spin tensor.** `s_ijk = −e_ijkl s^l` — the same equation, L75. The minus sign is the
source's and is load-bearing for O4; a seat that drops it fails C6.

**O3 — the four-fermion axial self-interaction actually in the field equations.** The Hehl–Datta equation of entry 10 L87–88,
`iγ^k ψ_{:k} = mψ − (3/8) κ (ψ̄ γ^k γ⁵ ψ) γ_k γ⁵ ψ`, the contortion it comes with, `C_ijk = S_ijk = ½ κ e_ijkl s^l`
(Eq. (5), L80–82), and the spin contribution `¼ κ (2 s^i s^k + s_l s^l g^ik)` to `U^ik` (Eq. (6), L84–86), whose trace part the
source carries into Eq. (9) (L104–106) as `(3/4) κ s_l s^l g_ik`. Every numeral in
this paragraph is the source's, at the lines given. **The quantity under test is the one that enters here** — this is requirement 1
of the order, and no seat may substitute a convenient proxy for it.

**O4 — the two audited scalars, and the exact map between them.**
- spin-fluid scalar `s²_fluid = ½ s_ij s^ij` with the source's projection `s_ijk = s_ij u_k`, `s_ij u^j = 0` (entry 10 L119–120),
  the scalar itself printed at L121;
- Dirac scalar `s²_Dirac = |s⃗|²`, the spatial pseudovector square that Eq. (9) contracts (entry 10 L110–112, where `s^i u_i = 0`
  gives `s^0 = 0` in the comoving frame and the second term of Eq. (9) becomes `−(3/4) κ s² g_ik`).

K3 step 1's corollary derived `½ s_ij s^ij = |s⃗|²` **exactly, for every orientation**, so the two printed relations are two values
of one quantity. **Each seat re-derives this map independently from O1–O2 rather than importing it**, and reports sign, projection
and normalisation explicitly at each step. If a seat's own re-derivation contradicts the step-1 corollary, that contradiction is the
result and is filed under K3S2_MAP_CONTRADICTED (§4); it is not reconciled away.

**O5 — the coarse-graining scale.** The macroscopic average is over a comoving cell of proper volume `V = ℓ³` containing `N = nV`
fermions. `ℓ` is a declared parameter, not a fitted one, and every reported quantity states its `ℓ` and `V` dependence explicitly.
Step 1's leading term was `(¾)·n/V` operator-ordered (`K3S1_RESULT_20260903.md` §2) — a term that vanishes in the thermodynamic
limit at fixed `n`, which is precisely why the density power, not just the coefficient, is the object of this test.

---

## 2. The many-fermion state, specified before computing

This is requirement 2 of the order. The state is declared here and may not be adjusted after seeing a result.

- **Field:** free Dirac field of mass `m`, no interactions other than the four-fermion term of O3, which is treated to the order
  stated in §3 and not resummed.
- **Statistical state:** grand-canonical ideal Fermi gas, occupation
  `n(p,σ,r) = [ exp((E_p − r μ)/T) + 1 ]^{-1}`, `E_p = √(p² + m²)`, with `σ` the spin label and `r = +1` for particles and `r = −1`
  for antiparticles. Both `r` sectors are carried explicitly; a seat that silently drops the antiparticle sector fails C7.
- **Polarisation:** unpolarized — equal occupation of both `σ` at every `p`. The fully polarized state is control C2, not the test
  state.
- **Species:** `N_f` degenerate species, carried symbolically. The printed closures are stated by the source for "fermions"
  without fixing `N_f`; whether the answer depends on `N_f` is part of the result and is reported, not chosen.
- **Thermodynamic parameters:** `T` and `μ` are the independent variables; `n` is derived from them by the seat, with the degenerate
  limit `T → 0` (Fermi sea, `n(p) = θ(p_F − |p|)`) and the classical limit `T → ∞` at fixed `n` both evaluated. The relation between
  `p_F` and `n` is a textbook constant and is **pinned at step 1 by a receipted derivation inside each seat's own script**, never
  quoted from memory.
- **Regimes:** the non-relativistic (`p_F ≪ m`) and ultrarelativistic (`p_F ≫ m`) limits are both reported. The bounce literature's
  own densities are pinned at step 1 from entries 9–11 and used only to say which regime the printed closures live in.

---

## 3. The evaluation, with the two contractions kept apart

This is requirement 3 of the order.

The object is the coincident-point expectation `⟨ O(x) ⟩` of the quadratic operator built from O1, in the state of §2, with the
macroscopic average of O5.

- **Wick decomposition, reported separately.** The seat reports the **direct (Hartree)** contraction and the **exchange (Fock)**
  contraction as separate, separately-labelled quantities, each with its own density power and coefficient, before any sum is taken.
  Step 1's finding is that the direct piece vanishes for the unpolarized state; the seat must reproduce that as C1 rather than
  assume it.
- **Ordering / renormalisation prescription, declared.** The coincident-point product of two bilinears carries a state-independent
  vacuum piece. The seat uses normal ordering with respect to the **medium** (subtracting the `T = μ = 0` vacuum value) and states
  that choice in its script header before running. Any additional subtraction, cut-off or dimensional continuation the evaluation
  needs is declared **as it is introduced**, with the dependence of the answer on it reported.
- **What is delivered.** A symbolic or numerically converged evaluation (with convergence tolerance explicitly deferred to a
  receipted pin), with the spinor traces shown, of both contractions in both the degenerate and classical limits and in both mass
  regimes.
- **Contact terms.** If the exchange contraction requires a contact-term or regulator choice that the sources do not fix, that fact
  is the result: class `EXCHANGE_PRESCRIPTION_DEPENDENT`, with the residual freedom stated **exactly** — which object, which
  parameter, and the range of coefficients admissible completions produce. A coefficient is never manufactured to fill it.

---

## 4. Outcome classes — declared now, before any computation

Exhaustive and mutually exclusive; one is filed.

1. **K3S2_EXCHANGE_N2_RESTORED** — a term scaling as `n²` at fixed `V` survives the thermodynamic limit with a coefficient derived
   from O1–O3 alone. Report the coefficient and state whether it equals `⅛` (entry 10 L121), `¾` (entry 10 L113), or neither.
2. **K3S2_EXCHANGE_OTHER_POWER** — the exchange contraction survives but scales as a different power of `n` (for example a power set
   by `p_F` rather than by `n²`). Report the power and coefficient.
3. **K3S2_EXCHANGE_NEGLIGIBLE** — the exchange contraction vanishes in the thermodynamic limit, scaling at the same order as or
   sub-leading to step 1's `n/V` term throughout the density range the bounce papers use (pinned at step 1 from entries 9–11).
4. **K3S2_EXCHANGE_PRESCRIPTION_DEPENDENT** — the leading density power or its coefficient depends on the ordering, regulator,
   coarse-graining scale, species content or state in a way the sources do not fix. **INCONCLUSIVE**; the residual freedom is stated
   exactly, per §3.
5. **K3S2_MAP_CONTRADICTED** — a seat's independent re-derivation of the O4 map contradicts K3 step 1's corollary. The contradiction
   is filed and the step-1 corollary is re-opened by amendment; no other class is filed in the same run.
6. **K3S2_NO_CLASS** — a control in §6 fails in both seats after two attempts. Nothing is filed but the failure.

---

## 5. Mapping back to both printed relations

This is requirement 5 of the order and is a **required deliverable of every class except 5 and 6**.

Whatever the leading behaviour turns out to be, the seat maps it back onto **both** printed relations — the spin-fluid `s² = ⅛ n²`
(entry 10 L121, and Gasperini 1986 `σ² = ℏ²⟨n²⟩/8`, `GASPERINI_K3_RESULT_20260904.md`) and the Dirac `⟨s²⟩ = ¾ n²` (entry 10 L113) —
using the O4 map, and states for each whether the calculation derives it, contradicts it, or leaves it free.

**Neither printed coefficient may be used as an input anywhere in the derivation.** Each seat's script asserts this positively: a
declared deletion probe in which both printed numerals are replaced by symbols must leave every computed quantity unchanged, and the
seat states this before running. This is C8.

---

## 6. Controls — each with its exact failure set

A control "passes" only if the seat's script prints the exact assertion named. Failure of any control halts that seat; failure in
both seats after two attempts is class 6.

- **C1 — direct term.** The unpolarized direct (Hartree) contraction must evaluate to zero. Exact assertion: `C1_DIRECT_ZERO=PASS`.
- **C2 — polarized limit.** The fully polarized state must return the polarized closure `n²/4` at leading order — coefficient pinned
  at step 1 by the same receipted derivation as K3 step 1's C2, not quoted from the printed sources. Exact assertion:
  `C2_POLARIZED_N2_QUARTER=PASS`.
- **C3 — classical limit.** The `T → ∞` limit at fixed `n` must reproduce K3 step 1's linear-in-`n` result, `(¾)·n/V`
  operator-ordered (`K3S1_RESULT_20260903.md` §2). Exact assertion: `C3_CLASSICAL_LINEAR_IN_N=PASS`.
- **C4 — antisymmetrisation deletion probe.** With antisymmetrisation deleted, the exchange contraction must vanish **identically**,
  and the seat states this prediction in its script header before running. Exact assertion: `C4_EXCHANGE_DELETED=PASS`.
- **C5 — units.** Restoring `ℏ` and `c` must return the `(ℏ c n)²` form the printed closures carry (entries 9, 11; entry 10 L121).
  Exact assertion: `C5_UNITS_RESTORED=PASS`.
- **C6 — sign and projection.** The seat's own re-derivation of O4 must return `s_ij u^j = 0` and its own value for
  `½ s_ij s^ij / |s⃗|²`, printed with its sign. Exact assertion: `C6_MAP_DERIVED=PASS` (the printed ratio is reported, not asserted
  to be 1; a value other than 1 routes to class 5).
- **C7 — antiparticle sector.** The antiparticle occupation must appear in the evaluated expression; deleting it must change a
  printed quantity. Exact assertion: `C7_ANTIPARTICLE_SECTOR_LIVE=PASS`.
- **C8 — no printed coefficient as input.** Per §5. Exact assertion: `C8_NO_PRINTED_COEFF_INPUT=PASS`.

The check sheet records the **exact set** `{C1_DIRECT_ZERO, C2_POLARIZED_N2_QUARTER, C3_CLASSICAL_LINEAR_IN_N, C4_EXCHANGE_DELETED,
C5_UNITS_RESTORED, C6_MAP_DERIVED, C7_ANTIPARTICLE_SECTOR_LIVE, C8_NO_PRINTED_COEFF_INPUT}` and asserts that all eight codes are
present in each seat's output. A run in which some refusal fired, or in which a control merely "passed", does not satisfy this: the
eight codes are checked by name, and a deletion probe confirms that removing a check removes its code.

---

## 7. Seats, blind double, second route, check sheet — Duho's "both" standard

- **Route 1, blind double:** two seats (codex and the Claude seat) evaluate independently, each from O1–O3 and §2 only, neither
  seeing the other's script or output, both writing executable scripts that print their control codes and their class.
- **Split rule:** if the two disagree on the class, a third seat is dispatched **only** through
  `/Users/duhokim/HermesOps/scripts/nm_referee_dispatch.sh` (ACCESS_SHA proof or no verdict) and the split is reported in the
  reconciliation, never averaged away.
- **Route 2, independent method:** a second route by a different method (momentum-space Wick contraction versus one-body
  density-matrix / Slater-determinant construction — whichever route 1 did not take), dispatched through the same wrapper, blind to
  route 1's result files.
- **Arithmetic re-check:** Kimi via the Moonshot route (`--provider moonshot -m kimi-k3`; a control confirms no fallback line) on
  the check sheet's arithmetic.
- **Check sheet:** one page, human-readable, every claim carrying a source line or an executed-output line receipt, per
  `feedback_seat_results_need_check_sheet_and_second_route`.
- **Tori's own re-run:** every route-1 script is re-executed by Tori and the printed controls compared, as in K3 step 1.

---

## 8. What makes this INCONCLUSIVE, stated in advance

Class 4; or C1/C2/C3 failing in both seats after two attempts (class 6); or route 1 and route 2 disagreeing on the density power
after a third seat. In every such case the residual freedom is stated exactly and **no coefficient is manufactured**.

---

## 9. Non-circularity and scope

No cosmological input. The printed coefficients are under test, never inputs (C8). The scope is this document: K4, K5 and K6 remain
**NOT ORDERED**; K1 stage 2 remains stopped; the Tuesday neutron-star mass watch stays armed. No tier, warrant token, standing or
stamp moves on Tori's authority — the result proposes annotations and Duho rules. Paper HOLD; nothing outward.

## 10. Cost and stopping rule

Two to five seat-days, no data acquisition. Stop and file whatever class is reached if the evaluation has not converged after the
second route plus one third seat.

---

## 11. Gate record (V1 -> V2)

`K3S2_PREREG_GATE_20260904_agy.md` (fresh seat, `nm_referee_dispatch.sh`, ACCESS PROVEN,
`ACCESS_SHA=79a025231548887c2f7f94ac3c958a622ec5d07c5014c85e1124f8b4f6ca4d0e`) returned `GATE=PREREG_SOUND_WITH_REPAIRS` with four
repairs.

- **Repairs 2, 3 and 4 applied verbatim.** Repair 4 is the substantive one: it closed a real gap in the outcome classes -- an
  exchange term at *exactly* the same order as step 1's `n/V` term would have fallen into no class. Repairs 3 and 4 also removed the
  phrase "`CLOSURE_SCALING_FAILS` stands and is strengthened" from two outcome classes, which was a standing declaration this
  document has no authority to make.
- **Repair 1 declined, with the receipt.** The referee asked to widen the Eq. (5) citation from L80-82 to L80-83 on the ground that
  "line 83 ... actually contains the denominator '2'". It does not. In
  `../bhu-reading-20260823/sources/1111.4595v2_poplawski_prd85_clean.txt`, with runs of spaces squeezed:
  `L80: [ 1]`, `L81: [ Cijk = Sijk = kappa e_ijkl s^l . (5)]`, `L82: [ 2]`, `L83: [Substituting (4) into (2) gives]`, `L84: [ 1]`.
  The denominator is at **L82**, already inside the cited range; L83 is prose opening the next sentence, and L84 is the numerator of
  Eq. (6)'s 1/4, which is cited separately as L84-86. Applying the repair would have made the citation less exact, not more. The
  decline and this receipt went to a second fresh referee for adjudication
  (`K3S2_PREREG_GATE_ADJUDICATION_20260904_agy.md`); the outcome is recorded there and in this section.

K3S2_PREREG_V2_FROZEN
