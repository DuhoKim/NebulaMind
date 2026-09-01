# ADVERSARIAL CHECK — proposed amendment (B) to a FROZEN, SIGNED preregistration

You are checking a proposal BEFORE it reaches the principal. **Your job is to REFUTE it.**
Default to REFUTED if uncertain. A plausible-but-wrong amendment to a signed prereg is worse
than no amendment. Do not be agreeable.

## Background (all verifiable in the repo)

A spin-parity ("galaxy handedness") study, `_successor_build_20260824`, is **frozen and signed**
(P0, ed25519, 2026-08-31 19:33 KST, manifest `d1be4a3b…`). Its text is
`PREREG_SUCCESSOR_DRAFT_V134_20260831.md`. Key frozen facts, quoted:

- **§3 Estimand:** "A sign-symmetric classifier of accuracy a gives `E[s_obs|c] = (2a−1)·A_L·c`.
  Scalar path: `Â_L = β̂/(2â−1)`." `beta_slope()` is the raw centred slope β̂;
  `Var(β̂) = Var_pop(s)/((N−1)·Var_pop(c))`.
- `c` is **cos θ measured from Longo's axis**; the footprint was *leverage-chosen* to maximise
  `Var(cos θ)` about that axis (polar |cos θ| selection).
- **§4:** N = 49,211 (locked BS-2f mask), Var(cos θ) = 0.7517, **N_eq = 110,983 = 3·N·Var(cos θ)**,
  floor 100,000 → PASS. Calibration floor `a_LB < 0.85` → `INCONCLUSIVE-BY-CALIBRATION`, halt.
- **§5 verdicts:** `REPRODUCED-LONGO` needs p<0.001 AND Longo's sign AND |Â_L − 0.0408| ≤ 3σ_comb
  AND Â_L ≥ floor. `REJECTED-AT-LONGO-AMPLITUDE` needs p>0.05 AND (|Â_L| + 3σ) < 0.0408.
- **Positive control:** BATTERY-POS measured Â_L = 0.04243, p = 2.2e-21.
- Instrument antisymmetry: 1000/1000 bit-exact identity, 1000/1000 byte-exact mirror involutions.
- **BS-3g** (unfilled slot) exists for exactly one threat: "a nonzero global offset multiplied by a
  sky gradient in sensitivity — the one route the antisymmetry identity does not close." Its ruled
  mapping is **position-dependent accuracy `a(c) = a₀ + γ·(c − c̄)`**, Γ ratified ±0.25 in 50 steps,
  estimator + verifier built and CLEAR, 5,049 evaluations, zero verdict flips. **γ̂ is unmeasured.**

**What happened on 2026-09-01:** the image-analysis half (stage two) was **CLOSED** by the
principal ("bank stage one and leave the image half") because **`â` cannot be obtained**: it is how
often a *human* labels handedness correctly on real objects from the accepted population; one
checker is unavailable, a distributed panel needs **38+ people**, Galaxy-Zoo external labels are
**not usable** (modern releases publish winding *tightness* not direction; GZ1 lacks DR10.1-south
coverage, has no known-answer controls, and no publishable sign anchor to our convention; the
8.67M-row DESI catalogue is model predictions, forbidden inside `a`), and loosening the floors
deletes population coverage. The principal's own capacity is the binding constraint. Note the
labels themselves come from a **machine committee** ("the agreement of two classifiers about
handedness"); the humans (BS-8f) produce only â, σ_a, a_LB, Cov_a.

Meanwhile the principal authorised and is now running the **bulk image acquisition** (~148 GB,
12,117 bricks, SHA-verified) — **acquisition only**: no cutouts, no instrument inference, no χ
measurement, no handedness label.

## THE PROPOSAL YOU MUST ATTACK

Proposed amendment (B): evaluate the **same frozen statistic on a DIFFERENT, pre-registered axis**
— a CMB-fixed axis (hemispherical power-asymmetry / low-ℓ alignment axis), chosen from published
CMB data *before* any handedness data is touched — and report a **detection-class** result
(is the handedness field modulated along that axis?) rather than an amplitude-class result.

Its four load-bearing claims:

1. **CALIBRATION-FREE DETECTION.** β̂ and its permutation p-value are computable **without â**;
   `â` enters only as the divisor turning β̂ into Â_L. So the *existence* of a modulation is
   testable even though stage two closed. Only the *amplitude* claim died.
2. **AXIS SUBSTITUTION IS MINIMAL.** Because the frozen estimand is already
   `E[s|c] = (2a−1)·A_L·cos θ`, the frozen test **is already an axis-projected dipole**. Using a
   CMB axis changes `c`, not the estimator, the instrument, the null, or the sample.
3. **IT REMOVES THE EXACT BLOCKER THAT CLOSED STAGE TWO** — the 38-person human panel — because a
   machine committee alone can produce β̂.
4. **POWER (my arithmetic, attack it).** With σ_β = 1/√N_eq and dilution (2a−1):
   σ_A = 1/((2a−1)·√N_eq). Validation: at N_eq=110,983, a=0.85 → σ_A=0.00429, so BATTERY-POS's
   Â_L=0.04243 is 9.9σ, vs the receipt's p=2.2e-21 (≈9.5σ) — model reproduces the receipt.
   Leverage at angle ψ from the selection axis, assuming azimuthal symmetry about Longo's axis and
   ±cos θ symmetry: `Var(cos θ') = cos²ψ·Var(cosθ) + sin²ψ·(1−Var(cosθ))/2`, giving
   ψ=0°: N_eq 110,976, 3σ floor 1.29% · ψ=45°: 64,652, 1.69% · ψ=90°: 18,329, **3.17%** (6.06× loss).
   Conclusion drawn: even at the worst axis, Longo-scale (4.08%) stays detectable; Shamir-scale
   (1–2%) is lost off-axis.

## ATTACK THESE SPECIFICALLY

- **A1.** Is claim 1 actually true of THIS text, or does something in the frozen text make the
  p-value or the decision path depend on â after all? (Note the branch predicate checks the
  calibration floor `a_LB_b < 0.85` and halts **pre-unblinding** — does that kill a
  calibration-free path outright? Is `INCONCLUSIVE-BY-CALIBRATION` reachable without â?)
- **A2.** Does a **machine-only** committee break the estimand's stated premise of a
  **sign-symmetric classifier of accuracy a**? If machine accuracy is unknown *and possibly
  position-dependent*, does the detection claim survive — or is BS-3g's `a(c) = a₀ + γ(c−c̄)`
  precisely the systematic that manufactures a fake axis-aligned dipole? Can a detection claim be
  made at all while **γ̂ is unmeasured**?
- **A3.** Is my power arithmetic right? Check σ_A, the N_eq = 3·N·Var(cos θ) convention, the
  leverage formula, and whether the azimuthal-symmetry assumption is safe for a real DR10-south
  footprint (it is a *southern* footprint; a CMB axis may fall near its edge or outside it).
- **A4.** **The integrity question.** Is this a legitimate amendment, or is it **rescuing a dead
  study by swapping in a weaker claim after learning the original one is unobtainable**? A signed
  prereg's whole purpose is to stop exactly that. Does it matter that the new axis is chosen from
  *independent* data (CMB) and pre-registered before any handedness byte is read? Would a referee
  see a legitimate second question or a post-hoc pivot? **Say REFUTED if this is the latter.**
- **A5.** Anything else that kills it.

## OUTPUT

Verdict token first: `AMENDMENT_B_SOUND` / `AMENDMENT_B_SOUND_WITH_REPAIRS` / `AMENDMENT_B_REFUTED`.
Then per-claim (1,2,3,4) HOLDS/FAILS with the reason, then A1–A5, then — only if not refuted — the
**minimum set of things that must be true or measured before the principal could ratify it**.
Be specific and quote the frozen text where it decides a point. Review only: change no file.
