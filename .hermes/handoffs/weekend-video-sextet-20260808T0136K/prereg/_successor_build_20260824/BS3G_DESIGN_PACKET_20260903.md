# BS-3g sensitivity-gradient control — design packet for Duho

**Choice, not recommendation.** BS-3g asks whether adding a plausible sky-position gradient to the synthetic instrument changes the flagship decision when everything else is held to the preregistered path. A **decision-changing cell** means that, for one allowed simulated draw and gradient, the production verdict differs from that draw's zero-gradient verdict; therefore the flagship cannot say its decision is invariant across the whole declared calibration range.

## What the result says

The headroom redesign did what it was meant to do: no cell stopped at the calibration floor. It nevertheless found one actual decision flip at the most negative endpoint.

- The receipt fields are `n_draws = 99` and `n_perturbations = 51`, hence 5,049 evaluated cells. Replay diagnostics recorded `inconclusive_count = 0` and exactly one decision-changing cell: zero-based draw 94 at `gamma = -0.10`, where the verdict is `REPRODUCED-LONGO` rather than that draw's `INCONCLUSIVE` baseline. The receipt field `baseline_verdict = INCONCLUSIVE` confirms the common baseline token.
- The failing point is exactly the declared edge: receipt field `gamma_bound = 0.1`. It is 0.10 from the zero-gradient baseline, or 25 grid intervals using receipt field `delta_gamma_max = 0.004`; it is not an interior near-zero instability.
- One of 5,049 cells flips: 1/5,049 = 0.0198% (about one in 5,049). Under the preregistered worst-case rule, frequency does not dilute the result: §11 says, **“A flip found anywhere is DECISIVE,”** and receipt field `invariance_outcome = FAILED` records that reduction.
- The sweep had calibration margin throughout: the replay diagnostic field `min_a_lb_b = 0.8639832635983262`, above the frozen 0.85 floor. Receipt fields `gamma_hat = -1.3752885039820904e-18` and `sigma_gamma = 0.04790176316993866` put the endpoint at about 2.09 standard errors from zero. Physically/statistically, the fitted average gradient is essentially zero, but one worst-case stochastic realization at the allowed negative edge crosses the production decision boundary. This is sensitivity of a thin categorical boundary, not evidence that the synthetic fixture has a nonzero fitted gradient.
- The earlier 0.88 receipt failed differently. Its fields are `gamma_bound = 0.25`, `n_draws = 99`, `n_perturbations = 51`, `baseline_verdict = INCONCLUSIVE`, and `invariance_outcome = FAILED`; its recorded diagnostics were 4,752/5,049 `INCONCLUSIVE-BY-CALIBRATION` cells and `min_a_lb_b = 0.694958`. Thus the 0.88 run primarily exposed inadequate floor headroom, whereas the 0.95 run has zero calibration-inconclusive cells and exposes one genuine verdict flip.

Both current producer runs were byte-identical (`run/classp_candidates/BS-3g.json` SHA-256 `19ffcbab…`), and the independent verifier reported 20/20 fields PASS. This authenticates the failure; it does not turn it into a hold.

## Options

### A — Accept the recorded failure

**Prereg change:** no criterion, range, statistic, or production rule changes. Record BS-3g as `DESIGN/UNFILLED`, preserve both FAILED receipts, and state that the decision is not invariant over the declared `[−0.10,+0.10]` calibration range; BS-6 remains blocked.

**Discipline:** this is the literal predeclared consequence, not post-hoc. §7 says, **“ONLY `invariance_outcome = HELD` CAN FILL THIS SLOT”** and **“a verifier-valid `FAILED` receipt is a TRUE RECORD THAT BLOCKS.”**

**Claim/cost:** the flagship cannot claim robustness over the declared range and cannot start its image half under this successor; the cost is delay or a later successor design. A hostile referee would say this is the only interpretation that preserves the advertised worst-case gate after its adverse result.

### B — Redesign the invariance criterion a priori

Examples are a predeclared tolerance for a limited number/location of edge flips, or a smaller declared Γ that excludes −0.10. **Prereg change:** amend §7/§11 acceptance language, its failure consequence, and—if Γ changes—the bound and derived grid spacing; rebuild and independently referee the receipt under the new rule.

**Discipline:** doing this now is squarely post-hoc because the failing cell and its location are known. The prereg's own clauses say **“The resolution is preregistered, not chosen afterwards,”** **“The grid's fineness is where the strength of the `HELD` claim is set,”** and, most directly, **“if the worst case over draws also crosses a verdict boundary at a γ within the bound, that is EVIDENCE ABOUT THE DESIGN … It is not a cue to look for a fourth mapping.”** A defensible later design would need an independent scientific basis fixed without tuning to draw 94—for example, an external calibration bound supporting a smaller Γ, or a domain-based loss/coverage argument specifying an edge-cell tolerance—plus new blind fixtures or data not used to choose that tolerance.

**Claim/cost:** afterwards the flagship could claim only the newly defined result (for example, no flips inside the smaller range, or compliance with the stated tolerance), never invariance under the original worst-case `[−0.10,+0.10]` rule. Cost: an openly post-result successor amendment, new tooling/schema/verifier work, new independent review, and a permanently visible sensitivity of the conclusion to the revised rule. A hostile referee would say the threshold was drawn around the observed counterexample unless the independent justification genuinely predates or is insulated from it.

### C — Change the statistic or production decision rule

**Prereg change:** alter the statistic, its uncertainty/threshold, or the production decision helper so this boundary cell cannot change category, then rerun every dependent validation and re-freeze the affected analysis path. Merely special-casing draw 94 or `gamma = -0.10` would not be a scientific rule.

**Discipline/P0:** this is post-hoc if motivated by the observed flip, and it is not allowed under the present V137-H amendment signature. The preamble says the amendment **“does not replace or alter P0's ssh-signed V134 manifest,”** while §7 requires the control's **“statistic … acceptance rule, and failure consequence”** to be bound before BS-6. The verdict comes through the P0-signed `ref/gain_counterfactual_path.py` (`counterfactual_path_sha256 = 92cbbdf…` in both receipts). A real change would therefore take an expressly authorized new P0 freeze/signature, dependency audit, regenerated pins and receipts, and fresh hostile review—not a BS-3g-only amendment.

**Claim/cost:** the flagship could claim robustness only under the new statistic/rule, with the old FAILED receipt and original-rule non-invariance disclosed. Cost is the largest redesign and loss of continuity with the frozen test. A hostile referee would say the endpoint was moved after the result to erase an inconvenient classification unless the replacement rule has strong external justification and independent prospective validation.

### D — Keep the failure, add a separate prospective diagnostic/control

**Prereg change:** leave BS-3g and its block untouched, but predeclare a distinct successor study—for example, denser endpoint mapping or independent draws/fixtures—to measure how often and how locally the boundary crossing occurs. It must have a new identity and cannot retroactively fill BS-3g.

**Discipline:** allowed as follow-up evidence if clearly labelled prospective and non-curative. It respects §11's limit that `HELD` means only no flip on the evaluated grid and that a found flip is decisive for this gate.

**Claim/cost:** it could support a narrower descriptive claim about localization, prevalence, or mechanism and inform a future design; it cannot restore the original invariance claim or open BS-6 by itself. Cost: another preregistration, computation, receipts, and review, with no immediate discharge. A hostile referee would accept it as diagnosis but reject any attempt to relabel it as a rerun or use a favorable result to overwrite this failure.

## What the seats recommended before this run

The headroom memo recommended option (ii): **“V137-H: fixture accuracy 0.95, Γ = 0.10: a real-size tilt test. Recommended.”** It anticipated elimination of the floor failure, saying **“With a_hat = 0.95 and Γ = 0.10 … BS-3g tests whether the frozen decision is invariant”** and that the 0.88 FAILED receipt would remain as the real-floor record. It did **not** anticipate this outcome: the range record states, **“The memo correctly forecast floor headroom but did not forecast the worst-case decision result.”** In other words, the recommendation successfully made the intended question answerable, and the answer was adverse at one edge cell.

Decision belongs to the principal; a blind committee poll (codex, kimi, agy) can be run on the options before he decides.
