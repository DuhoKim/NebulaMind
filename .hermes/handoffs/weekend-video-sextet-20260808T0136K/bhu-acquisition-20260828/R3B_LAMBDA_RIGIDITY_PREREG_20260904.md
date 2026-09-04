# R3-B — FROZEN PRE-REGISTRATION: does the Λ-from-boundary construction forbid evolving dark energy?

**Tori, 2026-09-04 20:43 KST. Version 3. FROZEN pending the fresh referee gate. ORDERED by Duho ("run 1 and 2", relayed 19:52 KST; "go ahead" confirmed — second of two. R3A filed 20:12.)**
No derivation has been run and no data has been touched.**

## 0. Why this would exist

Entry 56 (Gaztañaga 2023) sets `Λ ≡ 3/r_S²` (**L28**) and reads cosmic acceleration as a measurement of the
gravitational radius. **We must test whether its equations hold the enclosed mass constant.** If `r_S` is constant, `Λ` is exactly
constant — equation of state `w = −1`, with no evolution available. **That premise is now known NOT to be free:**
the gate rejected an earlier version of this document as circular for asserting it, and the source is explicit
against the simple reading. Entry 56 at **L134–L138** says the mass inside `χ` is constant only "for matter-dominated fluid when `ρ ∼ a⁻³`", and that "in the early stages of the expansion, when the energy
density is dominated by radiation or a fluid with a different equation of state, **the mass inside `χ` is a
function of `τ`**"; at **L143–144**, "More generally, `M` could be a function of time." The paper then keeps
`M_T` constant by a stated mechanism — **letting the junction `χ*` be a function of time** (L138–140, Eq. (10)).
**Whether that mechanism leaves `w = −1` rigid is the question, not the premise.**

**This matters because it is the corpus's first candidate for a genuinely rigid quantitative commitment.** Unlike
ΛCDM, where Λ is a free parameter that can be replaced by a `w(z)` fluid, this construction **cannot absorb an
evolving-`w` result without abandoning the boundary that generates its acceleration**. Every K study so far found a
construction that fixes a shape and frees the magnitude; this is the place to look for the counterexample.

## 1. The question, exactly

**(a)** Does entry 56's construction, on its own stated equations, *force* `w = −1` exactly and forbid `w(z) ≠ −1`?
**(b)** If so, is that forbidden region the one current data prefer?

## 2. Objects to bind before any arithmetic

From entry 56 or marked ABSENT: the definition of `r_S` and what fixes it; every equation that holds the enclosed mass
constant; whether any admissible variant permits `r_S` to evolve (mass loss, accretion, a non-static exterior); and the
exact map from `Λ = 3/r_S²` to an equation of state.

**Any mechanism that would let `r_S` evolve must be sought in the source before the rigidity is asserted.** If one
exists, the answer to (a) is no and the study stops there — that outcome must be reachable.

## 3. Limb structure — cheap first

**Limb A (cheap, ~1 seat-day, no data):** establish (a) from the source alone. If the construction does **not** force
`w = −1`, file `RIGIDITY_ABSENT` and stop; no data is touched.

**Limb B (only if limb A holds):** compare against published constraints on `w0`–`wa`. **Public, already-published
constraints only** — no reanalysis, no likelihood, no new pipeline.

## 4. Outcome classes — declared now

1. **RIGIDITY_ABSENT** — the construction admits evolving `r_S`; no rigid prediction. Report the mechanism.
2. **RIGID_AND_TENSIONED** — `w = −1` is forced and current constraints disfavour it at a stated significance.
3. **RIGID_AND_CONSISTENT** — `w = −1` is forced and constraints are consistent with it.
4. **RIGID_BUT_SHARED** — `w = −1` is forced, but the constraint does not discriminate this construction from ΛCDM,
   because ΛCDM makes the same prediction. **This is the expected outcome and must not be dressed as a success.**
5. **INCONCLUSIVE_DATA** — constraints too weak to discriminate; state the precision that would be needed.
6. **R3B_NO_CLASS** — a control fails in both seats after two attempts.

**Class 4 takes precedence over 2 and 3 whenever the prediction is shared with ΛCDM.** The record must not report a
shared falsifier as a discriminating one.

## 5. Controls, each with an exact named code

- **C1 — source identity.** Reproduce `Λ = 3/r_S²` and the constant-mass statements from the pinned text. Exact
  assertion: `C1_SOURCE_IDENTITY=PASS`.
- **C2 — evolution search.** The seat must actively search the source for any admissible mechanism letting `r_S`
  evolve, and **print the exact search terms used and quote the resulting text.** A rigidity claim asserted without those quotes fails. Exact assertion:
  `C2_EVOLUTION_SEARCH=PASS`.
- **C3 — discrimination test.** State explicitly whether ΛCDM makes the same prediction. If it does, class 4 applies.
  Exact assertion: `C3_DISCRIMINATION_STATED=PASS`.
- **C4 — no reanalysis.** Only published constraints are quoted, with their source and assumptions; no likelihood is
  run. Exact assertion: `C4_PUBLISHED_ONLY=PASS`.

Controls in a limb not reached are recorded `NOT RUN`, never as passes.

## 6. Seats and discipline

As R3-A §5: blind double, third seat via the wrapper on a split, independent second route, Kimi arithmetic with a
no-fallback control, one-page check sheet, Tori re-runs everything, critic note before any ruling, executable
discipline per `K4_BOUNDARY_TRANSFER_PREREG_20260904.md` §7.

## 7. Non-circularity and scope

The data enter **only** at limb B, after the rigidity question is settled from the source. No tier, warrant token,
standing or stamp moves. This does not re-run K4 or Program A, which concern perturbations and the CMB cutoff; this is
the background expansion history. Paper HOLD; nothing outward.

## 8. What would make it INCONCLUSIVE

Class 5, or C2 failing in both seats. **The honest expected outcome is class 4**, and the design says so in advance so
that a shared falsifier is not later reported as a discovery.

## 9. Cost

Limb A one seat-day; limb B two to four more. No lane data; published constraints only.



## 10. Harness custody — LIVE, per the lesson R3A's gate taught

Duho's BS-4 note required the harness to be pinned. **R3A's gate caught the lane implementing that as a printed block
a seat would simply echo, which proves nothing.** Corrected here from the start:

**Every seat must EXECUTE and print the real output of** `python3 -c "import sys;print(sys.version)"`,
`python3 -c "import sympy;print(sympy.__version__)"`, and `shasum -a 256 $(command -v python3)`. Transcribing expected
values without running them **fails** the control. Exact assertion: `C5_HARNESS_PINNED=PASS`.

For comparison only, R3A's live-verified environment was `python 3.9.6`, `sympy 1.14.0`, `python3` sha256
`b8763cf250e607a778bb4603cecb5b90338814d0a3dfcba0d57b1de242f610e9`. A seat printing different values is not wrong —
it is flagged in the reconciliation rather than silently merged.

## 11. Stall guard

R3A's gate warned that symbolic work through a paper's solver chain can hang without tripping any failure rule.
**Every symbolic operation runs under a hard 120-second wall-clock cap**; on timeout the seat prints
`SYMBOLIC_TIMEOUT` and falls back to an explicit algebraic or numerical argument. A silent hang is a failed run; a
reported timeout is not.

## 12. Data boundary — Hwao's lane is not ours to enter

Duho's 19:52 relay is explicit: **published DESI results only.** Anything requiring Hwao's data, her pipeline, or her
lane's files is **not authorised**. If limb B cannot be answered from published constraints alone, the seat **stops and
says so**, and the question goes to Duho. No seat may open a file under another lane's directory for this study.

The seat must explicitly list every local file path it opened during the study. If any path falls outside the
current lane, the control fails. Exact assertion: `C5b_NO_CROSS_LANE_ACCESS=PASS`, printed by every seat.

## 13. Gate record (draft → V1 frozen)

`R3_DRAFT_GATE_20260904_agy.md` returned `GATE_B=PREREG_SOUND_WITH_REPAIRS` with one repair, **applied verbatim**: C2
told the seat to "print what it searched for", which the gate called non-mechanical — a seat could satisfy it with a
sentence. It now requires **the exact search terms and the quoted resulting text**. The gate also judged that
declaring the expected outcome (class 4, a shared falsifier) in advance is good practice rather than pre-commitment,
"since objective controls govern the execution".

## 14. Why this is V2: the V1 gate REJECTED this document

`R3B_PREREG_GATE_20260904_agy.md` returned **`GATE=PREREG_UNSOUND`**, not a repair list. Its finding, quoted:

> "THE RIGIDITY PREMISE: The premise is assumed rather than shown. The cited lines explicitly allow M to evolve over
> time, meaning the lane is assuming its own answer to force a constant `r_S`. This makes the whole design circular."

**It was right, and Tori verified it against the source rather than taking it on trust.** The V1 document asserted the
rigidity it was supposed to test — the precise error this lane has spent the week finding in other people's work. Both
repairs are applied: the premise is now the question, and C2's failure condition is the gate's exact wording.

**The source is sharper than either the lane or the gate first said**, and §0 now records it: entry 56 supplies the
evolution mechanism itself, a time-dependent junction `χ*(τ)` (Eq. (10)), introduced expressly so `M_T` can stay
constant while the enclosed mass does not. **Limb A must now decide whether that mechanism preserves or breaks the
`w = −1` rigidity**, which is a real question with a real chance of `RIGIDITY_ABSENT`.

## 15. V2 gate

`R3B_PREREG_GATE_V2_20260904_agy.md` returned `PREREG_SOUND_WITH_REPAIRS`, **both applied**: a drafting typo had
dropped the word "No" from "No derivation has been run", inverting a statement the pre-registration depends on; and
`C5b` was an assertion a seat could print while having opened another lane's files, so it now requires the seat to
**list every path it opened**, failing if any lies outside this lane.

The V2 gate also re-examined the rigidity premise and found it now **established by the cited lines rather than
assumed**, and confirmed the design reaches a guaranteed verdict without stalling.

R3B_PREREG_V3_FROZEN
