**STATUS: RULED — option (b), "real gate", 2026-08-29.** Option (a) is dead. The remaining open input is the γ → sign-vector mapping; see `OPEN_QUESTION_GAIN_SIGN_MAPPING.md`.

# OPEN QUESTION — the p-gated freeze blocker is a fork, and both directions cost something

**Raised 2026-08-29 02:05 KST by Hwao under self-continuation. Hard stop: "a fork where both
directions cost something." Both seats agree on the diagnosis; the remedy is a choice.**

## What is settled

**My reduction is dead.** I argued production `p` is a monotone function of `|A|` against a null the
gain gradient cannot move, so the `p` gates could be folded into `A`-breakpoints and `T` made
complete in `A` alone. Both seats refuted it, and GPT56 supplied a constructed counterexample rather
than an argument — geometry `c = [-1,-0.5,0,0.5,1]`, two accepted-sign vectors with the **same** raw
slope `β = −0.8` and therefore the same `A` at fixed `w`:

    s = [1,-1,-1,-1,-1]   mean sign -0.6   exact one-sided p = 1.0   perm_sigma = 0.5656854249
    s = [1,-1, 1,-1,-1]   mean sign -0.2   exact one-sided p = 0.9   perm_sigma = 0.6928203230

**`p(A)` is not single-valued at fixed geometry and fixed calibration.** Both premises were wrong:
production permutes the accepted-sign vector (v9:1138–1155) and `perm_sigma_exact()` uses the
variance of `s` (v9:1127–1135), so the null depends on the sign multiset — which a gain gradient
moves. CODEX reached the same conclusion independently.

**A second defect, mine, and worth naming:** `verdict_breakpoints.py`'s "transcription" test compares
`verdict_at()` against **another local restatement of the same `if/elif`**, not against production. I
called that check the trust root. It was vacuous — the same could-not-fail shape this lane has been
removing all night. The production branch *is* reachable as `_decide_from()` at v9:1561, so this is
fixable; I have not fixed it because whether the module survives depends on the choice below.

## The fork — GPT56's words, and what each costs

> "Freeze one explicit sensitivity semantics. Either (a) hold the observed production `p` fixed and
> derive completeness with `p` gates treated as fixed booleans, or (b) freeze an executable joint
> counterfactual path that maps each allowed gain perturbation through accepted signs/calibration and
> the production permutation record. Do not insert an assumed scalar `p_of_A` between production and
> the verdict."

**(a) Hold observed `p` fixed; `p` gates become fixed booleans.**
*Cheap and nearly done* — the amplitude-side breakpoints already work and are derived from the
production branch. `T` becomes complete over `A` with the `p` gates evaluated once at the observed
value.
*What it costs:* it asserts the systematic **does not meaningfully move `p`**. That is a claim about
the science, not a specification detail — and it is a claim GPT56's counterexample makes
uncomfortable, since a gain gradient acting on the sign vector is exactly what moves the permutation
null. **If it is wrong, the invariance test passes while the real verdict could still flip.**

**(b) Freeze an executable joint counterfactual path.**
*Honest and complete* — each allowed perturbation is mapped through accepted signs, calibration and
the production permutation record, so both `A` and `p` move together as they actually would.
*What it costs:* it is a substantial build — a counterfactual model of the sign vector under a gain
gradient, plus its own freeze and its own gate. It also needs a decision I cannot make: **what
counterfactual sign vector does a given `γ` produce?** That mapping is itself a modelling assumption
that would need preregistering.

**(c) Withdraw the invariance rule and state the systematic as an unbounded limitation.**
*Cost:* the sensitivity-gradient control stops being a gate and becomes a caveat. Cheapest, and the
most honest if neither (a) nor (b) can be done well — but it gives up the thing the control was for.

## My reading, not my decision

**(a) is tempting and I do not trust it.** It is nearly free because the amplitude machinery already
works, and that is exactly why I would be inclined toward it — which is the reason to have a human
look. It converts an open question into an assumption, and the assumption is precisely the one
GPT56's counterexample undermines.

**(b) is correct and expensive**, and its modelling assumption is a claim about the study, so it
needs preregistering rather than choosing.

If forced to recommend: **(b) if the mirror/gain control is meant to be a gate, (c) if it is not.**
I would not pick (a) without someone deciding, in the open, that the systematic's effect on `p` is
negligible — because that is a scientific judgement wearing an engineering costume.

## State

- `ref/verdict_breakpoints.py` — refutation recorded at the top of the module; the amplitude-side
  derivation and the (vacuous) transcription check are the only parts still standing.
- Gain design §4 marked **REFUTED and OPEN**; §4a keeps the amplitude-side rule.
- Reports: `gates/GAIN_V5_REVIEW_{GPT56,CODEX}.md`, both NOT CLEAR, converged.
- **This blocks FREEZING the gain control. It does not block anything else, and `γ̂` remains
  unmeasured regardless. BS-6 and the first image byte remain blocked.**

---

## VERIFIED CURRENT AGAINST V36 — 2026-08-29 07:25 KST

This question is about code, not draft text, so the V34→V36 move does not touch it. What I re-ran:
`ref/gain_gradient_estimator.py --self-test` (9 codes G01–G09, none exempt), `gates/verify_mu_gamma.py`
(10 in-domain cases, 5 domain controls) and `ref/verdict_breakpoints.py --self-test` — **0 failures
each**. Digests: estimator `e2270297`, verifier `e33d9275`, breakpoints `bd248c93`.

The fork is unchanged and remains open. **The estimator itself is finished and cleared ×2 at gain v6;
what is blocked is the choice below, not any remaining code.**
