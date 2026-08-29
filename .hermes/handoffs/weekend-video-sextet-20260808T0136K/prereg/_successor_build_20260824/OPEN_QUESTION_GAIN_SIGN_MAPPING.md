# OPEN QUESTION — what counterfactual sign vector does a gain gradient produce?

**Raised 2026-08-29 11:2x KST by Hwao, at exactly the point the standing orders said to stop. The
principal ruled the gain control a "real gate" (option (b)), and the orders attached a condition:
"when you reach the counterfactual sign-vector mapping for a given γ, stop and raise it as its own
question. Do not choose that mapping quietly." This is that stop.**

## The path around it is built and passes

`ref/gain_counterfactual_path.py` — 9 refusal codes, self-test 0 failures. It carries a counterfactual
sign vector through the **real** production machinery: `perm_record` on `mask.with_signs(s')` returns
β′, the null, p′ and σ_β′ **together from the same s'**, and `_decide_from` produces the verdict. `A`
and `p` therefore move jointly, which is the whole point of option (b) — my refuted reduction let them
drift apart by inserting an assumed scalar `p_of_A`, and GPT56's counterexample killed it.

**The module ships no mapping and refuses to run without one.** No default, no fallback, no
"reasonable" identity — `evaluate_at` raises `MappingNotFrozen`. The self-test supplies
`_TEST_ONLY_flip_fraction_mapping`, named so it cannot be mistaken for a model; it encodes no claim
about the instrument and must never be promoted.

## What the mapping has to decide

Given a gradient γ, produce the accepted-sign vector the instrument **would have** produced. Two
things ride on it, and the second is easy to miss:

1. **the signs** `s'` — which objects flip, and how that depends on position; and
2. **the calibration** `cal'` — if sensitivity varies with sky position, the measured per-bin
   accuracy `a_b` varies too. The interface already accepts a `cal'`; leaving it unchanged is itself
   a modelling choice, not a neutral default.

## The candidates, and what each costs

**A. Position-dependent accuracy, redrawn.** The physical reading: a gradient makes the classifier's
accuracy vary along cos θ, `a(c) = a₀ + γ·(c − c̄)`, and signs are redrawn under it — the same shape
production already uses in `inject_signs`, where `s = −lat` with probability `1 − a_b`.
*Cost:* it is **stochastic**. The counterfactual becomes a distribution over sign vectors, not a
vector, so the gate needs a further preregistered policy — worst case over draws, a quantile, or a
fixed seed — and a seed policy is exactly the kind of thing that looks innocuous and decides outcomes.

**B. Deterministic adversarial flip.** Flip the k signs most favourable to the observed slope, k set
by γ's bound. *Cost:* it is **not a model of the instrument**; it answers *"could any allowed gradient
flip the verdict"* rather than *"does the gradient we bound actually flip it"*. That may be the right
question for a gate — a bound, not a prediction — but it risks being so conservative the control can
never pass, which would make the gate useless in a different way.

**C. Analytic propagation, no redraw.** Propagate γ's effect on the slope and the null in closed
form. *Cost:* **this is option (a) wearing a new hat.** It reintroduces an assumed relationship
between the perturbation and `p`, which is the move both seats refuted and the principal rejected. I
list it only so it is visibly rejected rather than silently available.

## My reading, not my decision

**B for the gate, and A as a reported diagnostic beside it.** A gate should answer whether *any*
allowed gradient can move the verdict, which is B's question; A's distributional answer is the more
informative number but needs a quantile policy that is itself a preregistered choice. Running A
alongside without letting it gate would give the reader the magnitude without letting a seed decide
the outcome.

**What I am least sure of:** whether B can pass at all. If the bound on γ is loose, an adversarial
flip may always cross a verdict boundary, and a gate that structurally cannot pass is not a gate — it
is a guaranteed failure that will later be argued away. **That should be checked before B is frozen**,
and it is checkable now that the path exists: run B's construction against the current bound and see
whether the verdict survives.

I did not run it, because doing so would produce a number that starts to look like an answer.

## Status

- `ref/gain_counterfactual_path.py` built, self-test 0 failures, **v9 untouched** (`6a9abbbd…`).
- **The gain control cannot be frozen until this mapping is preregistered.** BS-3g stays
  DESIGN/UNFILLED, and BS-6 and the first image byte remain blocked.
