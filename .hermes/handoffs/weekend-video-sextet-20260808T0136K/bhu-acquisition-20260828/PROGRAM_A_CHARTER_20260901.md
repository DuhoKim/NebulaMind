# PROGRAM (A) — calibrate or kill the 60° causal cutoff. Charter + step 1.

**Authority:** Duho, in chat 2026-09-01, verbatim: **"start (A)"** — the topic the three-seat team
converged on. **Status: OPEN, step 1 complete.** No tier is changed by this program; entries
23–27 remain QUALITATIVE-DIRECTIONAL unless a gated result says otherwise, which would be a
MUST-STOP decision for Duho, not mine.

## The question, in plain words

The Gaztañaga causal-horizon cutoff is the one genuinely a-priori prediction in the whole BHU
corpus: it says the CMB should lose correlation beyond about 60°. We already established (twice,
adversarially) that it fixes **where** the cutoff sits but not **how much** power is missing — the
amplitude is free, so it cannot be tested as a number. This program's job is to stop saying "it's
free" as an opinion and **prove it as a theorem — or discover it isn't free after all.**

## What is already established, and re-verified this session from the primary source

`2003.11544_clean.txt` (entry 23, MNRAS 494), read **past the definition to its disposition**
(register §1ak, which exists because I got this wrong once):

- **Eq. 16 is a flux, not a field:** `Φ = −∫_M √−g d⁴x R⁰₀` — a 4-volume integral of R⁰₀.
- The causal condition `Φ(χ>χ_§)=0` is imposed "**so that there is no flux (i.e. no effects of
  gravity) beyond the causal scale**", and the source says this **"implies"** Eq. 17
  (`Λ/8πG = ⟨ρ+3p⟩_§/2`) — i.e. it fixes **Λ / the scale**.
- On the perturbation side the source gives only: "**an infrared cutoff in the spectrum of
  inhomogeneities for χ>χ_§**", plus "solutions in different regions **could be matched** as in
  Sanghai & Clifton 2015" — a gesture, **no matching law, no covariance, no initial-condition
  model**. An observer at the edge "could measure different cosmological parameters, because she
  sees a different patch of the initial conditions."

**So the freedom is real and is located precisely:** the theory constrains the *support* of the
primordial spectrum, and says nothing about its *shape* inside that support.

## The move that makes this decidable

Previous rounds argued about which completion is "principled" and got a spread (≈6,230–22,327 μK⁴)
that persuaded nobody, because any spread can be answered with "you picked the wrong completions."
**Replace the argument with an optimization over the whole class.**

**Admissible completions** — the class, stated in advance:

| | constraint | why |
|---|---|---|
| (i) | `P(k) = 0` for `k < k_§` | the causal condition, in the source's own words (IR cutoff) |
| (ii) | `P(k) ≥ 0` | it is a power spectrum |
| (iii) | `P(k) = P_ΛCDM(k)` for `k > k_norm` | high-ℓ is measured; the low-ℓ data is **held out** |

**The key structural fact:** `C_ℓ` is **linear** in `P`, and `S₁/₂` is a positive-semidefinite
**quadratic form** in `C_ℓ`. Therefore `S₁/₂` is a **convex** functional of `P` over a **convex**
admissible set — so its minimum is a convex program with a unique global optimum, and reduces
exactly to **non-negative least squares** (`M = LᵀL`, then `min ‖L·C_fixed + L·A·p‖²` s.t. `p ≥ 0`).
**Certifiable, not argued.** No new data, no telescope time, no calibration.

## The decision rule — pre-registered, so it cannot be chosen afterwards

Let `S_min` = the minimum of `S₁/₂` over the admissible class, `S_Planck ≈ 1,150 μK⁴` observed.

- **`S_min > S_Planck`** → **the model cannot produce the observed deficit at all.** The published
  claim that the causal cutoff explains the low-ℓ anomaly is **refuted** — a real falsification of
  a real claim, from theory plus public data.
- **`S_min ≤ S_Planck`** → the model can **accommodate** the deficit but not **predict** it. Report
  the full interval `[S_min, S_max]` as the exact, quantified measure of the freedom: a **no-go on
  calibration with a number attached**, which is strictly stronger than the current "it's free."

**Both branches are publishable and neither is the outcome I am hoping for.** That is the point of
writing the rule down before running it.

## Step 1 — DONE, and receipted

`cutoffA_s12_machinery.py` (run to completion; output in the commit):

1. **The S₁/₂ operator is exact, not approximate.** `S₁/₂ = CᵀMC` with
   `M_{ℓℓ'} = [(2ℓ+1)(2ℓ'+1)/16π²]·∫_{-1}^{1/2}P_ℓP_ℓ' dx`, built by Gauss–Legendre with more
   nodes than the integrand degree, so it is exact by construction. Checked against an independent
   dense-Simpson evaluation at ℓ=2,5,17: **relative difference ~1e-14**.
2. **Converged in ℓ_max:** 34,932 (ℓ_max 80) → 34,919 (ℓ_max 120), a 0.04% change.
3. **Validated against an INDEPENDENT reference:** this pipeline gives ΛCDM
   `S₁/₂ = 34,926 μK⁴`; the reference (~34,900) comes from the prior blind seats' *separate* CAMB
   runs and the published literature — **not from this pipeline**. Agreement **0.1%**.
   The check therefore does not share its suspect quantity with the thing under test, which is the
   trap recorded as register §1al (a validation that passed *because* of the error it existed to
   catch). Stated explicitly there and here.

**What step 1 does NOT establish, said plainly:** that the admissible class above is the *correct*
formalization of the causal condition. That is a physics judgement, and it is exactly the thing to
put to adversarial seats before any number is believed — because if the class is wrong, every
number downstream is wrong in the same direction.

## Steps remaining

2. **Gate the admissible class** — two independent seats attack the formalization itself: is (i)
   the right reading of "infrared cutoff in the spectrum of inhomogeneities"? Should the cut be on
   `P(k)` or on the *correlation support* `ξ(r>χ_§)=0` (these are NOT equivalent)? Is (iii)
   non-circular? **Per lane rules, if the seats disagree on substance I stop and bring it to Duho.**
   Hand seats the quotes inline — do not let them read a huge file whole (register §1am).
3. **Fix `k_§` from the source, not by hand** — `χ_§` follows from Eq. 17 and the measured Λ; it is
   the one number the theory genuinely predicts, and it must be derived, receipted, and not tuned.
4. **Run the convex program** → `S_min` (and `S_max` over the extreme points).
5. **Apply the pre-registered rule** above and write the result — either branch.
6. **Held-out checks, if a completion survives:** the shape of `C(θ)` beyond 60°, octupole
   planarity, and the low-ℓ E-mode spectrum the same completion implies.

## Standing constraints on this program

- **The low-ℓ data is held out.** The normalization is fixed at high ℓ only. Choosing any parameter
  to match `S₁/₂` would be exactly the circularity this program exists to avoid, and would void it.
- **No tier moves without Duho.** A result here bears on entries 23–27; the tier decision is his.
- **Publishable-bar honesty:** if the answer is "underdetermined," that is the result and it gets
  written as such — not dressed up as a prediction.
