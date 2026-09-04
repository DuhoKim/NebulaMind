# R3-A — one-page check sheet

**Tori, 2026-09-04 20:12 KST.** For a human checking this without redoing it.

## The question
Entry 59 derives inflationary observables from a particle-production law `K = β(κε̃)²`. **Is β derived, or put in by
hand?**

## The answer in one line
**Put in by hand — and the paper says so.** `β` is chosen; only `β_cr`, the critical value it must sit below, is derived.

## The four lines that settle it (entry 59)
| line | text | what it establishes |
|---|---|---|
| L122–124 | "For a rigorous treatment, it should be derived from quantum field theory… **Following [32], we assume that**" | the form is assumed, and the paper says the derivation is owed |
| L128 | "where β is a dimensionless particle production coefficient" | no value, no derivation |
| L197–199 | "For standard-model particles, `β_cr = 1/929.0915`" | **β_cr IS derived** |
| L228–229 | "We need a value of β which is slightly smaller than β_cr. **Thus, we choose β = 1/929.25**" | **β is chosen** |

And **L373–374**: the reported `n_s`, `r`, `α_s` are "only sensitive to β" — so the observables ride on the chosen number.

## The citation was opened, not waved through
The prereg forbade counting a citation as a derivation unopened. `[32]` is Popławski arXiv:1410.3881, **in the lane**:
- **L297** "Ultimately, K should be derived from quantum field theory…"
- **L298** "The **simplest form** of K which vanishes at a bounce… is"
- **L301** "where **β > 0 is a nondimensional constant**."

**The chain terminates.** Neither paper derives β; neither claims to.

## Why FREE and not FITTED — the split, and how it was settled
codex read the conclusion (L459–463: agreement with Planck "for a particular range of the particle production
coefficient") as a fit, and filed `BETA_FITTED`. A third seat set that aside on the prereg's definitions:

> a fitted parameter would have been tuned to remove the tension. The paper instead **reports its own ~6σ tension**
> with Planck 2015 at standard e-fold counts (L368–369) and recovers agreement only at `N ≈ 20–25`. Reporting which
> subset of a parameter range matches data "is standard reporting for a free parameter, not evidence of it being fixed
> to a target."

## One seat error, recorded
**codex marked `CITATION_[32]=BLOCKED` without opening a file that was in the lane.** The third seat ruled that
`INCORRECT`. It did not change codex's conclusion — [32] doesn't derive β either — but the control existed precisely to
stop citations being waved through, and the miss is in the record rather than absorbed.

## What was NOT claimed
- **Not an error claim.** Both papers openly flag that a QFT derivation is owed. The record says *unreproduced from the
  stated inputs*.
- The stall guard never fired (`DEPENDENCE_SYMBOLIC_TIMEOUT=no` in both seats).
- **No tier, warrant token, standing or stamp moved**; entry 59 keeps `W_MIXED`.

## Harness, live in both seats
`python 3.9.6`, `sympy 1.14.0`, `python3` sha256 `b8763cf2…f610e9` — **executed, not transcribed**, per the control the
gate forced after it caught the first version being a printed block. Tori re-ran both scripts.

## Receipts
```
R3A_BETA_PRODUCTION_PREREG_20260904.md  c5f5d80b…1607e8
R3A_beta_claude.py / .out               a5ea195d…1aa4dd / 8a1f25d3…ea1e442
R3A_beta_codex.py / .out                22e9287f…0a352d3 / e3812d49…271b1b5e
```
Gate `R3A_PREREG_GATE_20260904_agy.md`; third seat `R3A_THIRD_SEAT_20260904_agy.md`.

R3A_CHECK_SHEET_COMPLETE
