# K3 step 2 — what a critic gets

**Tori note, 2026-09-04 11:06 KST. NOTE ONLY — NO STUDY STARTED.** Same discipline as
`K3S1_WHAT_A_CRITIC_GETS_20260904.md`: written after the result, before any ruling, so the strongest objections to our
own finding are in the record rather than waiting to be discovered by someone else.

The result under attack: `K3S2_RESULT_20260904.md`, class `K3S2_EXCHANGE_N2_RESTORED`, exchange contribution
`−(3/8) n²/N_f` (non-relativistic) to `−(3/16) n²/N_f` (ultrarelativistic).

## 0. One thing in the source that strengthens the result, found while writing this

Entry 10 does not merely quote both closures — **it explicitly rejects the framework the `⅛` closure comes from**:

> L127–129: "The particle approximation for Dirac fields, however, is not self-consistent [4]. The spin-fluid
> description also violates the cosmological principle [14]. In this paper, we use the Dirac form of the spin tensor
> for fermionic matter, `s_ijk = s_[ijk]`."

So the `⅛ n²` at L121 is attributed to Hehl, von der Heyde and Kerlick (refs [8, 9]) inside a description this paper
says is not self-consistent and violates the cosmological principle. The paper's **own operative closure is the Dirac
`⟨s²⟩ = ¾ n²` at L113**, asserted with no citation attached.

K3 step 2 computed the Dirac form — the form the paper says it uses. The `−3/8 … −3/16` is therefore aimed at entry
10's own operative choice, not at a strawman. *(This is a reading of the source, not a ruling: what it does to the
warrant tokens on rows 9/10/11 is Duho's, and the packet does not currently propose it.)*

## 1. The strongest surviving objection: the free field is not the medium

The equation that defines the problem is the Hehl–Datta equation (entry 10 L87–88), whose four-fermion term
`−(3/8) κ (ψ̄γ^kγ⁵ψ) γ_kγ⁵ψ` **is an interaction**. K3 step 2 evaluated `⟨s_i s^i⟩` in the **free** Dirac gas.

At the densities the bounce chain invokes, that interaction is by construction not negligible — the whole claim is that
`κ⟨s²⟩` becomes comparable to the other terms in Eq. (9). A critic is entitled to say: at exactly the densities where
the answer matters, the state you evaluated in is not the state the theory has.

This does not touch the *negative* result about the printed coefficients — neither `⅛` nor `¾` is recovered from the
obvious free-field calculation, which is what "the closure is not derived" means — but it does bound the positive
claim. **The `−3/16` is a free-field number, not a prediction for a real bounce medium.**

**What would settle it:** a self-consistent evaluation with the Hehl–Datta term retained — Hartree–Fock in the
four-fermion channel, with the same medium normal ordering and the same two objects kept apart — reporting whether the
`n²` coefficient is stable, shifts, or changes sign under self-consistency. If the coefficient survives with its sign,
the finding hardens; if it flips, the finding narrows to "not derivable as printed" and the sign statement is withdrawn.

## 2. Flat-space quantum field theory at Planckian curvature

Every step used flat-space mode decomposition: plane-wave spinors, a momentum integral, and a vacuum subtraction
defined by the `T = μ = 0` flat vacuum. The regime under discussion is a cosmological bounce, where curvature is not a
small correction.

The medium part is the more robust half — `ρ_med` is built from occupation numbers and survives a change of background
more readily than the subtraction does — but the *subtraction* is exactly where a curved background bites, and the
result's own §8.3 already concedes the subtraction is a declared choice.

**What would settle it:** redo the coincident-point evaluation in the FLRW background the paper actually uses
(entry 10 L134–136, closed FLRW), with adiabatic regularisation instead of flat normal ordering, and report whether the
`n²` coefficient is unchanged.

## 3. The unpolarized assumption — fair, but it is doing work

The sign is negative **because the state is unpolarized**: the direct (Hartree) term vanishes and only the exchange
term survives. In a domain-polarized medium the direct term returns as `+n²/4` (control C2) and dominates, positive.

This is a fair assumption rather than a convenient one, because it is the papers' own: entry 10 L121–122 says the
behaviour is significant "even without spin polarization". A critic who wants the positive sign back has to argue for
polarized domains at bounce densities — and then owes an account of why the domains align, which the printed closures
do not supply either.

**What would settle it:** nothing in this step; it would be a different question about the state, not about the
average.

## 4. The object question, restated as an attack

Stated already in the result §3 and §8.1, repeated here because it is the objection a referee reaches for first: two
quantities in this literature are both written `⟨s²⟩`, and the answer differs between them. Our reading — that the local
field equations need the local coincident-point object — is a physics argument, and §0 above now adds that the paper
disowns the spin-fluid framework in which the other reading would live. **But the paper still does not say.**

The honest position is the one the result takes: **either reading refutes the printed closures**, by sign and magnitude
on the local object, or by the absence of any surviving `n²` on the other. A critic can move us between two refutations;
no available reading recovers `⅛` or `¾`.

## 5. What a critic cannot take away

- The direct term is zero for the unpolarized state — three scripts, two methods, and it reproduces K3 step 1.
- `½ s_ij s^ij = |s⃗|²` exactly, re-derived independently in three scripts and under both Levi-Civita sign conventions,
  so the two printed relations are two values of one quantity and cannot both be right.
- Neither printed numeral entered any computation (C8, asserted by recomputation with free symbols in all three scripts).
- The trace codex held constant is `2 + 4m²/E²` — Tori's own verification, not a relayed claim.

## 6. Status

**K4 was ordered 2026-09-04 13:15 KST and completed the same afternoon** — `K4_UNDETERMINED`, no Planck pixel touched (`K4_RESULT_20260904.md`). K5 and K6 remain **NOT ORDERED**. No study was started by this note. The annotation packet on rows 9/10/11 and the
inheritance rows is with Duho; option (b) in that packet — what the negative sign does to the bounce — would be a
downstream study and is **not** what §1 above proposes, which is instead a self-consistency check of this step's own
number. Neither is ordered. Paper HOLD; nothing outward.

K3S2_CRITIC_NOTE_COMPLETE
