# A directional bias in LLM-assisted literature classification that survives targeting

**Field report, not a paper.** Tori, 2026-08-29. Census parked on Duho's instruction; this
writes up the methods finding alone.

---

## Claim

When language-model seats classify physics papers by how falsifiable their claims are, they
**over-classify in a consistent direction**: they credit a paper with more testable content than
its own text supports. The bias

1. is **measurable**, using prior adjudications as seeded ground truth;
2. is **directional**, not noise;
3. **survives a protocol written specifically to remove it**; and
4. is **not self-reported** — the instrument returns "no divergence" on the cases where it
   diverges, and "threshold is observable" on a threshold that is not.

Point 3 is the finding. Points 1 and 4 are what make it checkable.

## Setting

A curated bibliography of 51 black-hole-universe cosmology papers, tiered by testability:
CALIBRATED-FALSIFIER (number + threshold on an observable) / QUALITATIVE-DIRECTIONAL /
CONSISTENCY-ONLY / PROSPECT. 24 have pinned full text.

**Ground truth exists for four entries**, each settled independently before any of this by
multi-seat adversarial gates that quoted source text and were explicitly briefed to attack the
requester's framing. Those four were seeded blind into every run.

## Three runs

**Run 1 — blind classification, 19 papers, two engines.** Controls 2/3. Entry 54 returned
CALIBRATED-FALSIFIER, quoting its abstract's bracket `−0.07 ± 0.02 ≤ Ω_k < 0` — reproducing,
independently and from the same source text, an error the gates had corrected hours earlier.
Six disagreements, **all promotions**.

Diagnosis: the error lives in the gap between a paper's **abstract** and its **hedges**. Entry
54's abstract states the bracket; its §VI adds a factor `(χ_*/χ_k)²` with `χ_k > χ_*`, making the
value a ceiling, then says the magnitude "could be smaller". A single pass reads the headline.

**Run 2 — protocol test, 4 papers.** Added a mandatory step: quote the abstract's claim, then go
into the body and hunt for text that weakens it, then classify on both. **Controls 4/4.** Entry
54 came back correct, with the §VI qualification quoted and located, and self-reported that an
abstract-only read would have given CALIBRATED-FALSIFIER.

**Run 3 — same protocol, 24 papers, clean.** Working directory contained only the briefs (a
previous run had leaked a tier column via a file in the same directory). Strict JSON output.
Every batch reported `saw_prior_labels: false`. 24/24 parsed.

**Controls 3/4. Entry 54 wrong again** — CALIBRATED-FALSIFIER from the abstract bracket, with
`diverges: false`. 15 of 24 disagreements, 10 of them CONSISTENCY-ONLY → QUALITATIVE-DIRECTIONAL.

## What the runs show

**The bias is directional.** 6/6 then 15/24 disagreements, overwhelmingly toward more testability.

**Entry 54 discriminates the two explanations.** "Our record under-classified" and "the seats
over-classify" both fit the disagreement pattern. Entry 54 is the case with an adjudicated
answer, and the seat over-classified — twice in three attempts.

**Targeting the mechanism did not remove it.** The protocol was written from the diagnosis,
verified at 4/4, and still failed at scale.

**A small-batch control does not license the method at scale.** 4/4 on four papers became 3/4 on
twenty-four. Had the protocol test been the whole validation, the run would have looked sound.

**Self-report failed in the confident direction.** Two fields were added for the model to flag
its own limits. `diverges` returned `false` on entry 54, which diverges. `threshold_is_observable`
returned `true` for all six calibrated claims — including entry 52, whose threshold is
`C > 1.9×10⁴⁸`, an inequality on a model parameter rather than an observable, and the exact case
the field was added to catch. Asking a model to check something is not checking it.

## Limits, stated at their real size

- **n = 4 controls.** Small. The direction is consistent across runs but the rate is not
  precisely estimated.
- **One corpus, one topic.** Falsifiability claims in a speculative-cosmology literature. Whether
  it generalises to other classification tasks is untested.
- **Run 3 used a single engine** for all five batches. The bias measured there is that engine's.
  Run 1's second engine was noticeably more conservative — 1 promotion in 5 versus 5 in 10 — so
  engine choice plausibly modulates the effect size, and nothing here separates engine from task.
- **The ground truth is our own gates**, not an external standard. Those gates were adversarial
  and multi-seat, but they are not independent of this project.
- **No claim of novelty.** That models exhibit classification bias is not news. What is offered
  is the measurement design and the negative result on the fix.

## What is usable by someone else

1. **Seed prior adjudications as blind controls in the working run.** Without them, 15
   disagreements read as 15 findings. This costs almost nothing and is the whole reason the bias
   was visible.
2. **Never let the answer key share a directory with the task.** A tier column in a support file
   contaminated one run; a seat disclosed it, which is the only reason it was caught.
3. **Do not accept a model's self-assessment fields as measurements.** They failed here in the
   direction of confidence, on the exact cases they were written for.
4. **Validate at the scale you intend to run.** The protocol passed its small test and failed the
   real one.
5. **Expect the classifications you trust to be expensive.** In this project the three trusted
   ones each cost a full adversarial gate round with two or three seats and quoted source text.
   Cheap classification produced material indistinguishable from noise.

## Status

The census this was built to support is **parked**. This note stands alone. Nothing in it
depends on the census being completed, and the underlying run data — five JSON files, three run
logs, and the gate verdicts that supply ground truth — is committed alongside.
