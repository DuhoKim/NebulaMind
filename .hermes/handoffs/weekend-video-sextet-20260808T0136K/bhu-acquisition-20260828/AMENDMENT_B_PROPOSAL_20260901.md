# PROPOSAL — the axis-substituted handedness test ("option B")

> # ⛔ REFUTED — DO NOT ACT ON THIS PROPOSAL
>
> **`AMENDMENT_B_REFUTED`, 2026-09-01, by adversarial review (`TOPIC_AMENDMENT_B_claude_VERDICT.md`),
> and I have VERIFIED every decisive point against the frozen text myself.** All four load-bearing
> claims fail. The proposal below is kept unedited as the record of what was proposed and why it was
> wrong; **its recommendation ("(a), develop to precondition 1") is WITHDRAWN.** Summary of the kill:
>
> 1. **Claim 1 (calibration-free detection) is FALSE OF THIS TEXT.** I quoted §3's estimand and
>    stopped one sentence short of the sentence that refutes me. **Line 423:** "Decision bands
>    evaluate at â / {â_b}; **the detection floor evaluates at a_LB / {a_LB_b}**" — the detection
>    floor is calibration-evaluated (§5 fixes it as `3.09 · σ_ours(a_LB)`). Worse, **line 477** is a
>    hard gate: "If any bin's `a_LB_b < 0.85`, it emits an immediate pre-unblinding
>    `INCONCLUSIVE-BY-CALIBRATION` and the run halts. **Only if all bins satisfy `a_LB_b >= 0.85`
>    may Stage C run.**" Without `â` the run halts **before any statistic is formed** — `β̂_obs`
>    (BS-7f) sits four gates downstream of BS-8f. The design already anticipated a missing
>    calibration and specified that it stops. There is no calibration-free path to rescue.
> 2. **Claim 2 (axis substitution is minimal) is FORECLOSED BY THE FROZEN TEXT.** **Line 132:**
>    "This tests that published amplitude at that published axis. It does not test A ≈ 0.02,
>    Shamir, **BHU**, or whether the sky is isotropic. **Fixed-axis.**" The signed text explicitly
>    disclaims — *by name* — the exact use I proposed for it. `AXIS` is a constant of a frozen
>    pinned reference and §0 makes code beat prose, so it is unexecutable as well as disclaimed.
> 3. **Claim 3 (it removes the stage-two blocker) is CIRCULAR.** Its own precondition (bound γ via
>    BS-3g) needs the run-time calibration artifacts stage two closed for; BS-3g blocks BS-6, which
>    blocks the first image byte. It does not even unblock the 148 GB now downloading.
> 4. **Claim 4 (power) was WRONG BY √3, AND MY "VALIDATION" WAS THE ERROR VALIDATING ITSELF.** I
>    used `σ_β = 1/√N_eq`, treating the gate threshold `N_eq = 3·N·Var(cos θ)` as an inverse
>    variance. Frozen §3 defines `Var(β̂) = Var_pop(s)/((N−1)·Var_pop(c))`, so
>    `σ_β = √3/√N_eq`. Corrected: **σ_A = 0.00743, not 0.00429** — I overstated precision by 73%.
>    The BATTERY-POS "model check" I offered as grounds to trust the table only passed *because* of
>    the error: corrected, it gives 5.71σ (8.16σ even at a perfect classifier) against the receipt's
>    ~9.5σ, so **no admissible `a` reproduces the control and the check FAILS.** Re-run
>    `axis_leverage_power.py` — it now prints the failure instead of hiding it.
> 5. **The conclusion inverts, and the frozen gate ends it anyway.** Corrected, the ψ=90° 3σ floor
>    is **5.48%**, *above* Longo's 4.08% — so "Longo-scale survives at any axis" is false. And the
>    frozen power floor (`N_eq ≥ 100,000`) admits **only ψ ≤ 20.1°**, while the candidate CMB axes
>    sit at ψ ≈ 48–61° (review's numbers, not independently verified here) → every one returns
>    **`INCONCLUSIVE-BY-POWER`** before any statistic. My table never applied the frozen gate at all.
> 6. **The systematic is measured, not hypothetical, and my proposal deleted its only defence.**
>    §2.7 measures `corr(psfsize_r, cos θ) = +0.4188` in the retained sample and says outright
>    "**Outcome-blind is not the same as systematics-neutral, and this cut is not neutral.**" The
>    amplitude band — which my "detection-class" reframing *removes* — was what forced a fake slope
>    to land near a pre-specified amplitude and sign. I proposed keeping the quantity the systematic
>    manufactures while dropping the constraint on it. My mirror-involution fallback is pre-refuted
>    by §1: that receipt "does not measure sky-position dependence."
> 7. **On integrity (A4), the review's answer is post-hoc pivot.** CMB-independence guards against
>    data-dependent choice of *test*, not outcome-dependent respecification of *claim* — and the
>    trigger here was learning the signed claim was unobtainable. Aggravated by my own precondition
>    4, which proposed re-deriving the power floor *after* the new axis misses it.
>
> **No repair set is offered, and I do not offer one:** repairs would produce a different study, not
> a modified amendment B. **Of the three options this file put to Duho, the answer is (c) — drop it.**

**Status: DRAFT FOR DUHO'S RULING — now REFUTED (see above). Nothing was amended. No frozen byte
was touched. No tier, no gate, no signature was changed by this file.** Written by Tori (BHU lane)
at Duho's instruction ("draft the amendment proposal for B"), 2026-09-01. The study it concerns
belongs to **Hwao's lane**, and Hwao's judgement on feasibility outranks mine on everything
operational.

---

## The proposal in one sentence

Run **the same frozen statistic on a different, independently-chosen axis** — an axis fixed from
published CMB data before any handedness byte is read — and report **whether a modulation exists**
(a detection), rather than **how big it is** (an amplitude), because the amplitude half is what
died yesterday and the detection half did not.

---

## Why this is worth your time: what died, and what did not

Stage two closed on your ruling because **`â` cannot be obtained**. `â` is how often a *human*
labels spiral handedness correctly on real objects from the accepted population — one checker
unavailable, a panel needing 38+ people, Galaxy Zoo unusable, floors not loosenable, and your own
capacity the binding constraint. That reasoning is sound and this proposal does not reopen it.

But look at exactly where `â` enters the frozen text (§3):

> "A sign-symmetric classifier of accuracy a gives `E[s_obs|c] = (2a−1)·A_L·c`.
> Scalar path: `Â_L = β̂/(2â−1)`."

**`â` is a divisor, and nothing else.** The quantity actually measured from the sky is `β̂`, the raw
centred slope — and `β̂` comes from the **machine committee** ("the agreement of two classifiers
about handedness"), not from humans. The humans (BS-8f) produce only `â, σ_a, a_LB, Cov_a`.

So the closure of stage two kills the *amplitude* `Â_L` — and with it both frozen verdicts,
`REPRODUCED-LONGO` and `REJECTED-AT-LONGO-AMPLITUDE`, since both compare `Â_L` to 0.0408. It does
**not** kill `β̂` or its permutation p-value. **"Is there a modulation?" survives. "Is it Longo's
amplitude?" does not.**

## Why the axis substitution is small, not a new instrument

This is the part I did not expect. The frozen estimand is `E[s|c] = (2a−1)·A_L·cos θ` where θ is
measured **from Longo's axis**. That is *already a dipole projected on a pre-chosen axis*. The
frozen test is not "a handedness test that happens to use an axis" — **it is an axis test.**

Which means substituting a CMB-fixed axis changes **`c` and nothing else**: same estimator
(`beta_slope()`), same instrument, same permutation null, same 49,211-object mask, same
antisymmetry identity (1000/1000 bit-exact mirror involutions). It is the smallest possible change
that asks a genuinely different question.

**Why a CMB axis is the right different question.** A rotating parent black hole imprints *one*
preferred axis. If that is real, the same axis must show up in the CMB (hemispherical power
asymmetry / low-ℓ alignment) **and** in galaxy handedness. Requiring the two independent probes to
agree on a direction fixed in advance is the content — it is what every earlier spin-dipole claim
(Longo, Shamir) lacked, because their axes were fitted after the fact and the look-elsewhere effect
ate the evidence.

## What it would cost in sensitivity — computed, not asserted

The footprint was *leverage-chosen for Longo's axis* (`Var(cos θ) = 0.7517` vs 0.4452 full-sky), so
moving the axis costs power. `N_eq = 3·N·Var(cos θ)` is pure axis-dependent leverage, so this is
computable in closed form. With `σ_A = 1/((2â−1)·√N_eq)`:

| angle from Longo's axis | Var(cos θ′) | N_eq | loss | 3σ detection floor |
|---|---|---|---|---|
| 0° (aligned) | 0.7517 | 110,976 | 1.00× | **1.29%** |
| 30° | 0.5948 | 87,814 | 1.26× | 1.45% |
| 45° | 0.4379 | 64,652 | 1.72× | 1.69% |
| 60° | 0.2810 | 41,490 | 2.67× | 2.10% |
| 90° (worst) | 0.1241 | 18,329 | 6.06× | **3.17%** |

*(Script: `axis_leverage_power.py`, run to completion, in this directory. It uses only public
numbers quoted from the frozen text — no sealed artifact, no object row, no χ sign, no label.)*

**Model validation:** at the frozen `N_eq` this predicts the positive control BATTERY-POS
(`Â_L = 0.04243`) lands at **9.9σ**; the frozen receipt records `p = 2.2e-21` (≈9.5σ). The model
reproduces the study's own control, which is why I trust the table.

**Reading it honestly:** Longo-scale signals (4.08%) stay detectable at *any* axis. Shamir-scale
signals (1–2%) survive only if the CMB axis lands within ~30–45° of Longo's. **So the amendment's
value depends on an angle nobody has measured yet** — and that measurement is cheap, geometry-only,
and touches no image.

## The three things that could kill it — stated before you decide, not after

1. **The systematic that fakes exactly this signal.** If machine-classifier accuracy varies across
   the sky, `a(c) = a₀ + γ·(c − c̄)`, it manufactures an axis-aligned dipole out of nothing. This is
   not a new worry I am inventing — it is **precisely the threat BS-3g exists to bound**, described
   in the frozen text as "a nonzero global offset multiplied by a sky gradient in sensitivity — the
   one route the antisymmetry identity does not close." The machinery is built (estimator +
   verifier CLEAR, Γ ratified ±0.25 in 50 steps, 5,049 evaluations, zero verdict flips) but **γ̂ is
   unmeasured, and BS-3g is an unfilled slot.** Without a bound on γ, a detection claim is not
   defensible. **This is the amendment's hardest precondition, and it may be fatal.**
2. **A machine-only committee has no measured accuracy at all.** Detection does not need the
   *value* of `a`, but it does need `a` to be *sign-symmetric and position-independent* — which is
   an assumption, not a measurement, once the humans are gone. Some of it is testable without
   humans (mirror-involution controls on real images are already byte-exact), but not all of it.
3. **The footprint may not reach the axis.** DR10-south is a partial, southern footprint. My
   leverage table assumes azimuthal symmetry about Longo's axis; a real CMB axis could fall near
   the footprint edge or outside it, where the table is optimistic. Real `Var(cos θ′)` must be
   measured on the actual mask before any of the above is believed.

## The integrity question, which I am raising against my own proposal

A signed preregistration exists to stop exactly one thing: **changing the claim after learning the
original claim is unobtainable.** That is what this proposal looks like from the outside, and you
should weigh it that way.

What I think distinguishes it from a post-hoc pivot — and you should judge whether it is enough:
the new axis comes from **independent data** (the CMB) that has nothing to do with galaxy
handedness; it is pre-registered **before any handedness byte is read** (the images are still
downloading and the authorization is acquisition-only); the number of axes is capped in advance;
and the original claim is **not quietly dropped but explicitly recorded as unobtainable**, with its
reason.

What would make it indefensible: choosing the axis after seeing any handedness result, trying more
than the pre-declared axes, or presenting the detection claim as if it were the amplitude claim
that was signed for.

## How it should be built, if you say yes

**Do not edit the signed text.** Stage one's bytes stay frozen under your ed25519 signature and
keep their standing as the banked deliverable. This should be a **successor preregistration that
inherits** stage one's frozen sample, instrument, and null — exactly the shape stage two's R-E
already anticipated ("its own manifest, P0′ signature and gate ladder"). Amending signed bytes is
the thing we should never do; writing a new frozen text that cites them is normal practice.

**Preconditions before it could be ratified** (each is a real gate, not a formality):

1. **Measure the leverage.** Compute `Var(cos θ′)` on the real 49,211-object mask for each
   candidate CMB axis. Geometry only, no images, no χ. *If the answer is near the 90° row, the
   proposal is not worth running and should be dropped here.*
2. **Bound γ, or stop.** BS-3g must be filled — a measured or bounded sky gradient in classifier
   sensitivity. Without it there is no defensible detection claim.
3. **Pre-register the axes**, capped at ≤3, from published CMB maps, committed and hashed before
   any handedness byte is read.
4. **Re-derive the power gate** at the new axis; the frozen `N_eq ≥ 100,000` floor was
   axis-specific and does not transfer.
5. **State the outcome space in advance**, including that a null is a publishable bound and is the
   likely result.
6. **Hwao's own feasibility judgement**, which I have not sought and which may override all of this.

## What I need from you

- **(a) Develop it** — hand this to Hwao, run precondition 1 (cheap, geometry-only) and let the
  answer decide whether preconditions 2–6 are worth it.
- **(b) Park it** — bank stage one as the deliverable, exactly as you ruled, and leave the image
  half closed. *Cost:* the 148 GB now downloading has no near-term scientific consumer.
- **(c) Drop it** — judge the axis substitution too close to a post-hoc pivot to be worth the
  reputational risk, whatever its arithmetic says. *This is a legitimate answer and I have tried to
  give you the case for it above.*

**My recommendation: (a), but only as far as precondition 1.** One cheap geometry computation
converts this from an argument into a number, and that number may kill the proposal by itself —
which is the fastest honest way to find out whether any of this is worth your time.

## Provenance, and what is NOT gated

Everything above rests on quotes from the frozen text (§3 estimand, §4 power gate, §5 decision
regions, §2.6 geometry, the BS-3g row) and the stage-two closure memo, all read this session, plus
one script run to completion in this lane.

**The load-bearing claims are UNGATED, and you should read them accordingly.** I dispatched two
independent adversarial seats to attack this before it reached you. **Both failed twice, in
different ways** — codex read the frozen text and exited without writing a verdict (the file's
lines run to thousands of characters); kimi returned only the echoed brief. Under this lane's
failure rule I stopped rather than trying a third time. A third seat on a different mechanism was
dispatched; its verdict is recorded below when it lands. **Until a gate says otherwise, treat
claims 1–4 as my reasoning, not as verified findings** — particularly the claim that detection is
calibration-free, which is the one everything else rests on.
