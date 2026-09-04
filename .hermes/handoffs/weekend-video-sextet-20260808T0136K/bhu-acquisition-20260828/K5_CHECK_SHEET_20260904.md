# K5 — one-page check sheet

**Tori, 2026-09-04 16:27 KST.** For a human checking this without redoing it.

## The question
Entry 21 puts de Sitter-core ringdown frequencies in a space-detector band. **Could LISA actually see one, and tell it
from an ordinary black hole?**

## The answer in one line
**Unanswerable from the model as it stands** — it fixes the ringdown's frequencies but not its loudness, and loudness
is what a detector measures.

## Why, in one step
Write the driven perturbation problem with a source `S` and solve it with the retarded Green's function. The ringing
signal is a sum over poles with coefficients

`C_n = (dW/dω|ω_n)⁻¹ × ∫ φ₁ Ŝ dr*`

- the first factor comes from the **potential** — fixed by the model's `(M, α)`;
- the integral comes from the **source** — the binary merger.

Entry 21's model is a **static equilibrium**. It contains no merger. So `C_n` is free, and with it the strain.
**The pole structure is fixed up to scale; the scale is not fixed at all.**

Receipt: `K5_route2_agy.out` and `K5_ROUTE2_20260904_agy.md` (Green's-function construction);
`K5_limbA_codex.out` (homogeneity: if `φ` solves it, so does `λφ`); `K5_limbA_claude.out` (`DERIVATION_HALTS_AT=epsilon_0`).

## The trap this study was designed to avoid
Entry 21 says at **L400** the excitation factors "have to be calculated… an involved task, that this work urges the
community to perform." **It would be a fallacy to conclude from that sentence that the model cannot fix the
amplitude** — that is an argument from ignorance about what the authors did.

All three seats rest on the structure instead, and Kimi's independent logic check confirms it: the paper's omission
"appears nowhere in the derivation… deleting it leaves conclusion 3 intact."

## One inference the logic check REJECTED
Kimi ruled invalid the claim that "the excitation *factor* is determined by the model": that holds only under the
narrow Wronskian-only definition, where it is trivial — and entry 21's own usage at L400 probably means something
wider, since a Wronskian residue "is directly calculable" and would not be called "an involved task".

**This makes the finding stronger.** If the paper's "excitation factors" include the source overlap, then what L400
defers to the community is not a hard calculation but **a quantity the construction does not contain**.

## The escape, and why it was refused
Calibrating the radiated-energy fraction from ordinary numerical-relativity mergers would give a number. It would be an
**added assumption**, not a derivation: no such calibration exists for this model, and importing the ordinary value
assumes the merger dynamics and surface structure are unchanged — which is what the model alters. Kimi: any amplitude
so obtained "inherits the status 'assumed, not derived.'"

## What was NOT done
- **No LISA sensitivity product was fetched. No network was used.** `LISA_PRODUCT_FETCHED=no`, `NETWORK_USED=no`.
- **Limb B (acquisition) and limb C (the ~15 seat-day pipeline) never ran.** About one seat-day was spent.
- **Four of the five controls are NOT RUN**, by name: `C1_TABLE1_REPRODUCED`, `C2_SCHWARZSCHILD_LIMIT`,
  `C3_DETECTOR_CONTROL`, `C4_DISTINGUISHABILITY_DELETION`. Only `C5_AMPLITUDE_PROVENANCE=PASS` is claimed.
- **Entry 16 was never reached**, so its `W_ROUTE_NAMED_ONLY` stands untouched.
- **No tier, warrant token, standing or stamp moved.**

## The pattern worth noticing
The freedom map found the causal-horizon cutoff's **amplitude free** while its scale was derivable. K5 finds entry 21's
**amplitude free** while its frequencies are derivable. Twice, in unrelated corners of this corpus: the construction
gives you a scale or a frequency, and never the size of the effect — which is the only part a measurement tests.

## Receipts (sha256)
```
K5_LISA_FORECAST_PREREG_20260904.md  fc013ec4…b57f41
K5_limbA_claude.py / .out            43a85d33…450da / 4234137c…c1fc14
K5_limbA_codex.py / .out             73743d81…155a3c / b1a845d3…673d3b
K5_route2_agy.py / .out              e14b439c…b9a6c9 / c835e7d8…781c15
```
Full hashes in `K5_RESULT_20260904.md` §9. Gate: `K5_PREREG_GATE_20260904_agy.md`. Logic check:
`K5_KIMI_LOGIC_20260904.md` (Moonshot route, no-fallback control).

K5_CHECK_SHEET_COMPLETE
