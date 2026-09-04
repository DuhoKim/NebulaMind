# K3 step 3 — FROZEN PRE-REGISTRATION: does the negative exchange n² coefficient survive self-consistency?

**Tori, 2026-09-04 14:58 KST. Version 1. FROZEN pending the fresh referee gate. ORDERED by Duho ("K3 step 3, K5, K6 in
order", relayed by Blanc 2026-09-04 14:56 KST — first of three, sequential.)**

Predecessor: `K3S3_SELFCONSISTENCY_PREREG_DRAFT_20260904.md`, gated `PREREG_SOUND_WITH_REPAIRS`
(`K3S3_DRAFT_GATE_20260904_agy.md`); its one repair — outcome class 3 widened to
`K3S3_SIGN_REVERSED_OR_ZERO`, closing a gap where an exactly-zero coefficient fell into no class — is applied and
carried here.

**Standing objection, recorded and overruled by the principal.** The draft's §9 carried the gate's judgement that this
step is not worth ordering (the printed closures are already falsified without it), and Tori's own agreement with that.
**Duho ordered it anyway on 2026-09-04 14:56 KST.** That is his call; it is recorded here so the record shows the
objection was made before the work, not invented after it, and the study now proceeds in full.

**No derivation has been run under this document.**

---

## 0. What this is for

`K3S2_RESULT_20260904.md` filed `K3S2_EXCHANGE_N2_RESTORED`: the Fock contraction of the coincident-point operator
gives `−(3/8) n²/N_f` (non-relativistic) to `−(3/16) n²/N_f` (ultrarelativistic) — negative, where both printed closures
are positive.

**That was computed in the FREE Dirac gas.** The equation defining the problem is not free: entry 10's Hehl–Datta
equation (L87–88) carries the four-fermion axial term `−(3/8) κ (ψ̄γ^kγ⁵ψ) γ_kγ⁵ψ`. This step asks whether the
coefficient survives when that term is retained self-consistently.

**What is already safe and stays safe whatever this finds:** neither printed coefficient is recovered from the obvious
calculation. This step can move the *positive* claim — the value and sign of the derived coefficient — not the negative
one.

## 1. THE CHEAP LIMB, RUN FIRST — per Duho's order that a disqualifying check precede the expensive half

**Limb A (cheap, ~1 seat-day, run before any Hartree–Fock machinery is written):** compute the dimensionless
four-fermion coupling strength of the state, at the densities the bounce chain itself invokes.

The relevant comparison is the spin contribution against the ordinary energy density in entry 10's own Eq. (10),
`ε̃ = −p̃ = −α n²` with `α = (9/16) κ` (entry 10 **L116–118**), set against `ε` in the same equations; the bounce of
Eq. (16)–(17) (**L179–L193**) is by construction the point where those balance. The seat computes the ratio at the
pinned bounce condition and prints it.

- **If that ratio's magnitude is ≥ 0.1 at the bounce** — which is what "the spin term causes the bounce" means —
  then perturbation theory in the four-fermion term fails exactly where the answer matters. **File
  `K3S3_NOT_PERTURBATIVE` and stop.** No Hartree–Fock machinery is written, no expensive half is run.
- **If it is small**, proceed to limb B.

**Limb B (expensive):** the Hartree–Fock evaluation of §3.

The ratio must be **computed and printed by the seat's script**, never asserted, and the pinned densities traced to
entries 9–11.

## 2. Objects and state

Unchanged from `K3S2_EXCHANGE_PREREG_20260904.md` §§1–2, imported by reference and restated in each seat's script:
`s^i = ½ ψ̄γ^iγ⁵ψ` (entry 10 Eq. (4), **L73–78**); the map `½ s_ij s^ij = |s⃗|²` **re-derived, not imported**; the
unpolarized grand-canonical ideal Fermi gas with both particle and antiparticle sectors, `N_f` species, `T` and `μ`
independent; medium normal ordering; the coarse-graining scale `V = ℓ³` stated in every reported quantity. **Both
objects L (local, coincident point) and C (cell-averaged) are carried separately**, as in step 2.

The addition: the four-fermion term of entry 10 **L87–88** is retained, with the contortion `C_ijk = S_ijk = ½ κ
e_ijkl s^l` (Eq. (5), **L80–82**) and `U^ik = ¼ κ (2 s^i s^k + s_l s^l g^ik)` (Eq. (6), **L84–86**) as the source's own
statement of how it enters.

## 3. Method (limb B only)

Hartree–Fock in the axial-axial channel, with **four** contractions kept apart and separately labelled: free-direct,
free-exchange, interaction-direct, interaction-exchange. The self-consistency condition is solved, not linearised away;
if solved iteratively, the convergence tolerance is deferred to a receipted pin computed in the script.

**Declared limitation, before running:** Hartree–Fock is itself a truncation. If limb A's parameter is not small, the
question is not answerable this way and class 4 is filed — not a licence to report the Hartree–Fock number anyway.

## 4. Outcome classes — declared now

1. **K3S3_COEFFICIENT_STABLE** — the `n²` coefficient is unchanged to the stated order; step 2's number and sign stand.
2. **K3S3_COEFFICIENT_SHIFTED_SAME_SIGN** — magnitude moves, sign does not. Report the shifted value and the parameter
   controlling it.
3. **K3S3_SIGN_REVERSED_OR_ZERO** — the self-consistent coefficient is positive, exactly zero, or changes sign
   depending on the regime. Report it, and report whether it approaches either printed value; step 2's sign statement is then withdrawn **by amendment**, and the
   record says so plainly.
4. **K3S3_NOT_PERTURBATIVE** — the computed expansion parameter is not small where the chain operates, so no
   self-consistent coefficient is derivable this way. **INCONCLUSIVE**; state the parameter's value and what method
   would be needed. **This is limb A's exit and requires no expensive half.**
5. **K3S3_PRESCRIPTION_DEPENDENT** — the answer depends on the truncation, ordering or coarse-graining in a way the
   sources do not fix. **INCONCLUSIVE**; state the residual freedom exactly. This class takes precedence over classes
   1, 2 and 3.
6. **K3S3_NO_CLASS** — a control fails in both seats after two attempts.

## 5. Controls, each with an exact named code

- **C1 — free-field limit.** Switching the interaction off must reproduce K3 step 2 exactly: `−(3/8) n²/N_f` and
  `−(3/16) n²/N_f`. Exact assertion: `C1_FREE_LIMIT_MATCHES_K3S2=PASS`.
- **C2 — interaction deletion probe.** Deleting the four-fermion term must delete the entire correction identically;
  the seat states this prediction in its script header **before** running. Exact assertion: `C2_INTERACTION_DELETED=PASS`.
- **C3 — the four contractions are separate.** All four printed as separately labelled quantities before any sum.
  Exact assertion: `C3_FOUR_TERMS_SEPARATE=PASS`.
- **C4 — expansion parameter computed.** Computed and printed, not asserted, at the pinned densities. Exact assertion:
  `C4_EXPANSION_PARAMETER_COMPUTED=PASS`. **This is the control limb A turns on.**
- **C5 — map re-derived.** `½ s_ij s^ij / |s⃗|²` derived in-script with its sign. Exact assertion: `C5_MAP_DERIVED=PASS`.
- **C6 — both objects carried.** L and C both reported. Exact assertion: `C6_BOTH_OBJECTS_REPORTED=PASS`.
- **C7 — no printed coefficient as input.** Recomputation with `⅛` and `¾` replaced by free symbols is unchanged.
  Exact assertion: `C7_NO_PRINTED_COEFF_INPUT=PASS`.

**If limb A exits, C1/C2/C3/C5/C6/C7 belong to the half never reached and are recorded `NOT RUN`, never as passes** — the
discipline K4 established. The check sheet asserts the exact set `{C1_FREE_LIMIT_MATCHES_K3S2, C2_INTERACTION_DELETED,
C3_FOUR_TERMS_SEPARATE, C4_EXPANSION_PARAMETER_COMPUTED, C5_MAP_DERIVED, C6_BOTH_OBJECTS_REPORTED,
C7_NO_PRINTED_COEFF_INPUT}` by name and states the status of each.

## 6. Executable discipline

As `K4_BOUNDARY_TRANSFER_PREREG_20260904.md` §7, which this document adopts unchanged: every cited script exists, runs
under `python3`, is **re-executed by Tori** and not only by its author, has its output preserved as a file and hashed in
the check sheet, and no sentence calls a script executable support unless all of that holds. This lane has now found
three instances of the defect (`K2_route2_agy.py` a stub, `cutoff_phase1_camb.py` absent, K4's seat outputs unpreserved
by their authors).

## 7. Seats — Duho's "both" standard

Blind double (codex and the Claude seat); third seat through `nm_referee_dispatch.sh` (ACCESS_SHA proof or no verdict)
on any split; an independent second route by a different method, blind to route 1; Kimi via the Moonshot route on the
check-sheet arithmetic with a no-fallback control; a one-page human check sheet; Tori re-runs every script. A
"what a critic gets" note is filed after the result and before any ruling.

## 8. What makes this INCONCLUSIVE

Class 4 (limb A's exit) or class 5; or C1/C4 failing in both seats after two attempts (class 6); or route 1 and route 2
disagreeing after a third seat. In every case the residual freedom is stated exactly and **no coefficient is
manufactured**.

## 9. Non-circularity and scope

No cosmological input; no statement about the bounce; the printed coefficients are under test, never inputs (C7). This
document cannot move a tier, warrant token, standing or stamp. **NOT ordered and untouched by this document:** the
downstream bounce study from K3 step 2, and the K4 follow-up under a declared assumption. K5 and K6 are ordered but
follow *after* this study is filed, one at a time. Row 23 of the K4 annotation stays as applied. Paper HOLD; nothing
outward.

## 10. Cost and stopping rule

Limb A: about one seat-day. Limb B, only if limb A passes: three to six seat-days. Stop and file at limb A's exit if it
fires; otherwise stop and file whatever class is reached after the second route plus one third seat.

---

## 11. Gate record (V1 → V2), and the referee's warning that this study can only come back INCONCLUSIVE

`K3S3_PREREG_GATE_20260904_agy.md` (fresh seat via `nm_referee_dispatch.sh`, ACCESS PROVEN,
`ACCESS_SHA=26aaca948236038f1ffd70da442432e58151ccc70538f88f657960c8a7a51aff`) returned
`GATE=PREREG_SOUND_WITH_REPAIRS` with four repairs, **all applied verbatim**:

1. **Limb A's exit was left to taste.** "Not small" is now the declared threshold **|ratio| ≥ 0.1**. Declared in
   advance, which is what makes it a falsifier rather than a judgement call; it is a threshold, not a derived number.
2. **Class 3 had a gap:** a coefficient whose sign changes with regime fell between classes 2 and 3. Class 3 now names
   it.
3. **Classes 2 and 5 could both fire** on a prescription-dependent result that stayed negative. Class 5 now takes
   precedence over 1, 2 and 3.
4. **The NOT RUN list was short:** C5 and C7 also belong to the expensive half and could have been falsely claimed.
   Now all six are named.

The referee also confirmed, on the two questions the brief pressed hardest, that **C1 is not circular** — using the
predecessor's free-field number as the non-interacting limit of new code is a software control, not a physical input —
and that the recorded objection in this document's header is honest and correctly placed.

### The warning, recorded in full because it changes what this study can deliver

Asked whether the design can ever return anything but an inconclusive class, the referee answered **effectively no**:

> "the bounce is defined *by construction* as the point where these two quantities balance (i.e. the ratio is exactly
> 1). Therefore, the dimensionless parameter will always evaluate to order 1 at the bounce, limb A will always fail the
> 'small' test, and the study is mathematically guaranteed to exit with the inconclusive `K3S3_NOT_PERTURBATIVE` class."

**Tori's assessment: the referee is right about the bounce, and this is still worth the one seat-day.** Entry 10's
bounce is where `α n²` cancels the ordinary energy density (Eq. (10) at L116–118, the bounce at L179–L193), so the
ratio is 1 there by construction and limb A will fire. But there is a difference between an argument that it must and
a **printed, re-runnable receipt that it does**, and this lane has spent the week on exactly that distinction.

There is also a second thing limb A can deliver that the referee's framing misses: the same computation, evaluated
**away** from the bounce, says whether the free-field coefficient of K3 step 2 is safe in the regime where the theory
*is* perturbative. So the expected filing is class 4 **with** a statement of where step 2's number does and does not
hold — which is more than "inconclusive".

**Limb B is expected never to run.** If limb A fires as predicted, the expensive half is not written, and the cost of
this study is limb A alone.

K3S3_PREREG_V2_FROZEN
