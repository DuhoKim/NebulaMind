# R3-B limb A — blind seat brief (theory only; NO DATA)

**Authority:** Duho "run 1 and 2" (19:52) + "go ahead". **Governing document:**
`R3B_LAMBDA_RIGIDITY_PREREG_20260904.md` (frozen **V3**) — read it in full first, including §14, which records that
an earlier version of this document was **rejected as circular** for assuming the answer. Do not repeat that error.

**BLIND.** Do not open any file whose name contains `R3B_limbA`, `R3B_LIMBA`, `R3B_RESULT`, `R3B_CHECK` or
`R3B_RECONCIL`. You MAY read the prereg and `../bhu-reading-20260823/sources/gaztanaga_mass_mnras_clean.txt`
(entry 56).

**NO DATA. NO NETWORK.** Limb A is theory only. **Do not open any path outside this lane** — `C5b` requires you to
**list every file path you opened**, and fails if any lies outside `bhu-acquisition-20260828/` or
`../bhu-reading-20260823/sources/`.

## The question — limb A only

**Does entry 56's construction FORCE `w = −1` and forbid evolving dark energy — or does it admit an evolving `r_S`?**

The chain is: `Λ ≡ 3/r_S²` (**L28**) with `r_S = 2GM_T`. So `Λ` is constant **iff** `M_T` is constant.

**The question is therefore whether `M_T` is constant as a CONSEQUENCE of the construction, or as an ASSUMPTION
imposed on it.** Read these and quote what is decisive:

- **L134–L135:** the mass inside `χ` is constant "for matter-dominated fluid when `ρ ∼ a⁻³`";
- **L136–L137:** "in the early stages of the expansion, when the energy density is dominated by radiation or a fluid
  with a different equation of state, **the mass inside `χ` is a function of `τ`**";
- **L138–L140 and Eq. (10):** "**If we want `M_T` … to be constant** throughout the evolution, we need the junction
  `χ*` … to be a function of time `τ`";
- **L143–L144:** "More generally, `M` could be a function of time."

Note the conditional in L138. **Decide whether it makes constancy a choice or a consequence, and say which.** Consider
also the physical argument the paper relies on — an isolated black hole's mass is conserved — and say whether the
construction *derives* that or *assumes* it.

## Mandatory mechanics

1. **C5 — harness, LIVE.** Execute and print real output of `python3 -c "import sys;print(sys.version)"`,
   `python3 -c "import sympy;print(sympy.__version__)"`, `shasum -a 256 $(command -v python3)`. Transcribing fails.
2. **C5b — path list.** Print **every** file path you opened. Any path outside this lane fails the control.
3. **C2 — evolution search, with quotes.** Print the **exact search terms** you used to look for a mechanism letting
   `r_S` evolve, and **quote the resulting text**. A rigidity claim without those quotes fails.
4. **C1 — source identity.** Reproduce `Λ = 3/r_S²` and the L138 conditional from the pinned text; the text is
   PDF-extracted, so print `repr()` and match after normalisation.
5. **C3 — discrimination.** State explicitly whether ΛCDM makes the same `w = −1` prediction. If it does, the
   prereg's class 4 precedence applies.
6. **120-second cap** on every symbolic operation; on timeout print `SYMBOLIC_TIMEOUT` and argue algebraically.

## Deliverables — exactly two files

1. `R3B_limbA_<seat>.py` — self-contained, runs under `python3`, prints everything it claims. **Run it.**
2. `R3B_LIMBA_<seat>_RESULT.md` — first line exactly one token:
   `RIGIDITY_ABSENT` · `RIGIDITY_HOLDS` · `RIGIDITY_UNDETERMINED`

`RIGIDITY_HOLDS` means limb B would follow. `RIGIDITY_ABSENT` ends the study at limb A. Print every control code by
name. You have no authority over any tier, token, standing or stamp.

R3B_LIMBA_SEAT_BRIEF_COMPLETE
