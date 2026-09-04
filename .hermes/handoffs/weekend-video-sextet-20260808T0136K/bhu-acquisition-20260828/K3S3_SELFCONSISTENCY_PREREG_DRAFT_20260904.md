# DRAFT — NOT ORDERED — K3 step 3 pre-registration: does the exchange n² coefficient survive self-consistency?

**Tori, 2026-09-04 13:08 KST.** Drafted so that a future "k3s3" starts from a gated text, exactly as K3 step 2, K4, K5
and K6 were drafted before they were ordered. **No derivation has been run and none may be run under this document.**
Becomes live only on Duho's word; it is re-gated at that time and this draft is superseded by the frozen version, as
`K3S2_EXCHANGE_PREREG_DRAFT_20260903.md` was.

**This is NOT the study Duho declined.** Option (b) of the 10:27 packet — what the negative sign does to the bounce —
was **NOT ordered** on 2026-09-04 12:52 KST and is not proposed here. This document proposes something narrower and
prior: a check on whether K3 step 2's own number is stable. It touches no cosmology.

---

## 0. Why this would exist

`K3S2_RESULT_20260904.md` filed `K3S2_EXCHANGE_N2_RESTORED`: the exchange (Fock) contraction of the local operator
restores an `n²` term at `−(3/8) n²/N_f` (non-relativistic) to `−(3/16) n²/N_f` (ultrarelativistic).

`K3S2_WHAT_A_CRITIC_GETS_20260904.md` §1 records the strongest objection to that result, and it is ours, not a
critic's: **the evaluation was done in the free Dirac gas, and the equation that defines the problem contains an
interaction.** The Hehl–Datta equation (entry 10 L87–88) carries the four-fermion term
`−(3/8) κ (ψ̄γ^kγ⁵ψ) γ_kγ⁵ψ`. At the densities the bounce chain invokes, that term is by construction not negligible —
the whole claim of the chain is that `κ⟨s²⟩` becomes comparable to the other terms of Eq. (9) (L104–106).

So the free-field number is a first evaluation, not a settled one. This step asks whether it survives.

**What is already safe without this step, and stays safe whatever it finds:** neither printed coefficient is recovered
from the obvious calculation, which is what "the closure is not derived" means. This step can move the *positive*
claim — the value and sign of the derived coefficient — not the *negative* one.

## 1. The question, exactly

Retaining the four-fermion axial term of entry 10 L87–88 self-consistently at the same order it enters the field
equations, what happens to the leading `n²` coefficient of the audited local object — does it keep its value, shift,
change sign, or cease to be defined?

## 2. Objects and state

Unchanged from `K3S2_EXCHANGE_PREREG_20260904.md` §§1–2, imported by reference and restated in the seat's script:
`s^i = ½ ψ̄γ^iγ⁵ψ` (entry 10 Eq. (4), L73–78); the map `½ s_ij s^ij = |s⃗|²` re-derived, not imported; the unpolarized
grand-canonical ideal Fermi gas with both particle and antiparticle sectors, `N_f` species, `T` and `μ` independent;
medium normal ordering; the coarse-graining scale `V = ℓ³` declared in every reported quantity. **Both objects L and C
are carried separately**, as in step 2, and neither is dropped because it is inconvenient.

The one addition: the interaction is retained, and the expansion parameter in which "self-consistent" is meant must be
**declared and computed inside the script, not asserted** — a dimensionless combination of `κ`, `n` and the state
variables, evaluated at the densities entries 9–11 actually use (pinned at step 1 from those entries, including the
ultrarelativistic kinetic-equilibrium relations at entry 10 L152–160).

## 3. Method

Hartree–Fock in the axial-axial channel of the four-fermion term, with the direct and exchange contractions of the
interaction kept apart from each other and from the free-field contractions of step 2, all four reported separately.
The self-consistency condition is solved, not linearised away; if it is solved iteratively, the convergence tolerance
is deferred to a receipted pin computed in the script.

**A declared limitation, stated before running:** Hartree–Fock is itself a truncation. If the computed expansion
parameter is not small in the regime of interest, the honest outcome is that the question is not answerable this way,
and that is an outcome class below — not a licence to report the Hartree–Fock number anyway.

## 4. Outcome classes — declared now

1. **K3S3_COEFFICIENT_STABLE** — the `n²` coefficient is unchanged to the stated order; step 2's number and sign stand.
2. **K3S3_COEFFICIENT_SHIFTED_SAME_SIGN** — magnitude moves, sign does not. Report the shifted value and the parameter
   controlling it.
3. **K3S3_SIGN_REVERSED_OR_ZERO** — the self-consistent coefficient is positive or exactly zero. Report it, and
   report whether it approaches either printed value; step 2's sign statement is withdrawn by amendment and the record says so plainly.
4. **K3S3_NOT_PERTURBATIVE** — the computed expansion parameter is not small where the chain operates, so no
   self-consistent coefficient is derivable this way. **INCONCLUSIVE**; state the parameter's value and what method
   would be needed.
5. **K3S3_PRESCRIPTION_DEPENDENT** — the answer depends on the truncation, ordering or coarse-graining in a way the
   sources do not fix. **INCONCLUSIVE**; state the residual freedom exactly.
6. **K3S3_NO_CLASS** — a control fails in both seats after two attempts.

## 5. Controls, each with an exact failure set

- **C1 — free-field limit.** Switching the interaction off must reproduce K3 step 2 exactly: `−(3/8) n²/N_f` and
  `−(3/16) n²/N_f`. Exact assertion: `C1_FREE_LIMIT_MATCHES_K3S2=PASS`.
- **C2 — interaction deletion probe.** Deleting the four-fermion term must delete the entire correction identically;
  the seat states this prediction in its script header before running. Exact assertion: `C2_INTERACTION_DELETED=PASS`.
- **C3 — the four contractions are separate.** Free-direct, free-exchange, interaction-direct and interaction-exchange
  are printed as four separately labelled quantities before any sum. Exact assertion: `C3_FOUR_TERMS_SEPARATE=PASS`.
- **C4 — expansion parameter computed.** The dimensionless parameter is computed and printed, not asserted, at the
  pinned densities. Exact assertion: `C4_EXPANSION_PARAMETER_COMPUTED=PASS`.
- **C5 — map re-derived.** `½ s_ij s^ij / |s⃗|²` derived in-script with its sign. Exact assertion: `C5_MAP_DERIVED=PASS`.
- **C6 — both objects carried.** L and C both reported. Exact assertion: `C6_BOTH_OBJECTS_REPORTED=PASS`.
- **C7 — no printed coefficient as input.** Recomputation with `⅛` and `¾` replaced by free symbols is unchanged.
  Exact assertion: `C7_NO_PRINTED_COEFF_INPUT=PASS`.

The check sheet asserts the exact set `{C1_FREE_LIMIT_MATCHES_K3S2, C2_INTERACTION_DELETED, C3_FOUR_TERMS_SEPARATE,
C4_EXPANSION_PARAMETER_COMPUTED, C5_MAP_DERIVED, C6_BOTH_OBJECTS_REPORTED, C7_NO_PRINTED_COEFF_INPUT}` by name, and a
deletion probe confirms that removing a check removes its code.

## 6. Seats

Blind double (codex and the Claude seat), a third seat through `nm_referee_dispatch.sh` on any split, an independent
second route by a different method, Kimi on the check-sheet arithmetic, Tori re-runs every script. Same as K3 step 2.

## 7. Non-circularity and scope

No cosmological input; no statement about the bounce; the printed coefficients are under test, never inputs. This
document cannot move a tier, warrant token, standing or stamp. K4, K5 and K6 remain NOT ORDERED, and option (b) of the
10:27 packet remains NOT ORDERED.

## 8. Cost and stopping rule

Three to six seat-days, no data. If the expansion parameter is not small (class 4), stop there and file it — do not
substitute a different method without a fresh preregistration.

---

## 9. Gate record, including the referee's advice AGAINST ordering this

`K3S3_DRAFT_GATE_20260904_agy.md` (fresh seat via `nm_referee_dispatch.sh`, ACCESS PROVEN,
`ACCESS_SHA=5fe0d2e1153e32bbda5575e2f758a6ef659522432b5cb9e6f247203d1a012888`) returned
`GATE=PREREG_SOUND_WITH_REPAIRS` with one repair, **applied verbatim above**: outcome class 3 had a gap — a
self-consistent coefficient of exactly zero would have fallen into no class — and is now `K3S3_SIGN_REVERSED_OR_ZERO`.

The referee confirmed, on the two questions the brief asked it to attack hardest, that (i) the distinction between this
step and the bounce study Duho declined is **real, not cosmetic** — this is a flat-space many-body calculation that
never evaluates the bounce — and (ii) the objection it answers is **real and correctly stated**, because K3 step 2 did
evaluate an interacting theory in free-field states.

**But its closing judgement is that this step is not worth ordering**, in its words: "the printed closures are already
robustly falsified by their regime- and species-dependence, which a perturbative Hartree-Fock correction will not
miraculously remove."

**Tori's position, recorded rather than argued away.** The referee is right about the *negative* claim: the closures are
already falsified without this step, twice over, and nothing here would strengthen that. What it would touch is the
*positive* claim the record now carries — the seven annotated rows say the derived coefficient's sign is opposite to
both printed closures, and that sign comes from a free-field evaluation. The cheaper alternative is simply to say so on
the rows, which the record now does. **On balance Tori does not recommend ordering K3 step 3.** This draft exists so
the option is costed and gated rather than unavailable.

K3S3_PREREG_DRAFT_READY_FOR_GATE — NOT ORDERED, AND NOT RECOMMENDED
