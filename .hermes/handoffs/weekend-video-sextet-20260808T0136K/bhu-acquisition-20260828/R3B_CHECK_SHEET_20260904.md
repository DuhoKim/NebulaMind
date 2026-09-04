# R3-B — one-page check sheet

**Tori, 2026-09-04 20:53 KST.**

## The question
Entry 56 reads cosmic acceleration as a boundary effect: `Λ = 3/r_S²`. Since `r_S = 2GM_T`, a constant total mass
would force `w = −1` exactly, with no room for evolving dark energy. **Does the construction actually force that?**

## The answer in one line
**No — the rigidity is assumed, not derived**, and the paper says so in a conditional sentence.

## The four lines that settle it
| line | text | effect |
|---|---|---|
| L134–135 | mass inside χ is constant "for matter-dominated fluid when ρ ∼ a⁻³" | constancy is **conditional** |
| L136–137 | with radiation or another equation of state "**the mass inside χ is a function of τ**" | not general |
| L138–140 | "**If we want** M_T … to be constant … we need the junction χ\* … to be a function of time τ" (Eq. 10) | constancy is **adopted**, and engineered |
| L143–144 | "More generally, M could be a function of time" | evolution is explicitly permitted |

**Eq. (10) is the device that satisfies the assumption, not a proof of it.**

## What follows
- A variant with `M_T(τ)` is admissible on the printed text → time-dependent `Λ` → `w ≠ −1`.
- So an evolving-`w` measurement would **not refute** this model; it would select a branch the paper already allows.
- And `w = −1` never discriminated anyway: **ΛCDM predicts it too** (C3). The prereg declared that expectation in
  advance, before anything was computed.

## The hoped-for counterexample did not appear
R3B was ranked second because it was the only candidate that might show a BHU construction fixing a magnitude rigidly
enough for data to hit. It doesn't. **The shape/magnitude pattern survives this test intact** — and the reason is more
interesting than a counterexample: what looked like a rigid prediction is a modelling choice.

## What was NOT done
- **No DESI data. No published constraints. No pixel. No network. Nothing from Hwao's lane.** `C5b` made each seat list
  every path it opened; both lists are clean.
- `C4_PUBLISHED_ONLY` is **NOT RUN** — limb B was never reached.
- **No tier, warrant token, standing or stamp moved.**

## A dispatch failure of mine, ruled on by Duho
The first codex run returned `UNDETERMINED` with three controls NOT RUN — **because my dispatch forbade opening any
path outside the lane and so blocked the seat from the paper it was auditing.** The seat obeyed; my instruction was
wrong. Duho ruled "fix the dispatch and re-run" and added a requirement I had not: the seat must **prove** it read the
source with a full `ACCESS_SHA`, quarantined if absent. My own corrected re-run still lacked that proof, so it too is
set aside. **Three filings are preserved, none deleted**; only the access-proven one counts.

## Receipts
```
R3B_LAMBDA_RIGIDITY_PREREG_20260904.md  fd75e8b0…6cebc17
R3B_limbA_claude.py / .out              e38ef81b…6d91f / 4eb7b12b…45b3e
R3B_limbA_codex.py / .out               e45884d9…954a1a / 581bc1cb…611cab
entry 56 source (ACCESS_SHA)            17dec02b20e65e57d8f5a9d1a6ea8644ad8ee6f58ac73051e7f1f1458735c2a4
```
Gates: `R3B_PREREG_GATE_20260904_agy.md` (V1 **UNSOUND**), `R3B_PREREG_GATE_V2_20260904_agy.md`.

R3B_CHECK_SHEET_COMPLETE
