# Phase 5b — closing summary

Tori, 2026-08-27 19:52 KST. Lane opened 2026-08-25 17:27
(`PHASE5_BRIEF.md`). Fifteen gate verdicts, eight of them holds.

**One-line result: the phase set out to find whether a shock-wave black-hole cosmology can be
tested by light, and finished by establishing that it cannot be — not because the test is hard,
but because the published papers do not contain enough physics to say what the test would show.**

The phase's positive finding did not survive. That is the honest headline and it is stated
first deliberately.

---

## 1. What Phase 5b claims now

Three claims, all gated.

**Claim 1 — nothing reaches us from beyond the boundary.** Two separable parts:

- **(i) Causal, unconditional.** A true event horizon transmits nothing from its forbidden side,
  for any source whatsoever. Not a redshift argument.
- **(ii) Redshift suppression, conditional, threshold sharp.** The transmitted bolometric weight
  vanishes iff `γ² (N−1) → 0`, i.e. `γ = o((N−1)^(−1/2))`, γ being the emitter's Lorentz factor
  relative to comoving. Every bounded boost satisfies it.

  Receipt `P11_CLAIM1_SCOPE_RECEIPT.md`, `p11_claim1_boost.py` (8/8, exit 0). The comoving
  scaling is *measured* here, not assumed: fitting the lane's own column gives
  `Z ~ (N−1)^0.500033`. Defeating the suppression at our horizon offset needs `γ ≈ 8.97×10⁴`,
  and that requirement **diverges** as the horizon is approached — 316× over five decades — so
  no fixed γ ever suffices.

  **Not claimed:** singular emissivity. Named by the gate, still uncovered.

**Claim 2 — the invariant optical-depth element**, with the photon trajectory cancelling because
`r̄` is timelike. PASS in its stated comoving-fluid scope; holds for non-radial rays provided
`r̄` is monotone on the segment and the absorber is the pinned comoving fluid. Blind-doubled.

**Claim 3 — `β_rel = −1/√N`.** Carried PASS, unchanged since first gated, unattacked since.

**Not a claim — a receipt sentence only:** *"the two tested closures each contain a cancellation,
at different locations."* True, low-value, and explicitly **never to be promoted** to a model
finding. Both REGATE5 seats agreed on this disposition after disagreeing on whether it was
vacuous (agy: vacuous, drop it; codex: not vacuous but low-value, keep as a receipt sentence).
I adopted the narrower reading.

---

## 2. What was withdrawn

Every item below was *claimed* at some point in this phase and is now gone. This list is the
phase's real output as much as section 1 is.

| withdrawn | when / by |
|---|---|
| "the exterior is optically thin across the authorised range" | P1c, self-withdrawn against P1's own headline |
| My claim that finding A2's bracket was refuted | p1c re-run; the refutation was my error, not the gate's |
| P5's transmitted-background term and its saturation floor | P6 |
| Every numeric exclusion strength ever quoted (1 in 181, 245–2286, 1107/2832, 120/904) | successive gates; the last found stale **today**, a factor ~9 |
| The null's **location**, mine and the blind seat's | epoch ruling, both engines |
| My source law's epoch variation | epoch ruling — assumed a composition the closure excludes |
| **The null's EXISTENCE as a model property** | REGATE4 — the phase's only positive finding |
| **The flatness-gap closure** | REGATE4 — diagnosed a shape with a percent change of a ratio near 1 |
| The Hawking "degeneracy" argument | REGATE5 — a factor of two is not a degeneracy |
| The blanket form of the expansion-anisotropy kill | GATE_TRACKA narrowed it to wholly-interior signals |

---

## 3. Gate trail

| verdict | when | token |
|---|---|---|
| `GATE_S0S2` | 08-25 18:24 | HOLD_S0_OPTICAL_DEPTH_AND_S2_EXCLUSION_UNDERIVED |
| `KGATE_S0S2` | 08-25 20:05 | HOLD_S2_DIPOLE_BOUND_MISNORMALIZED… |
| `REGATE_S0S2` | 08-25 21:05 | HOLD_OPTICS_INFERENCE_STILL_UNLABELLED |
| `REGATE2_S0S2` | 08-25 21:11 | PASS_S0S2_FIXED |
| `KREGATE_S0S2` | 08-25 21:26 | PASS_S0S2_FIXED |
| `GATE_PHASE5B` | 08-26 00:04 | HOLD_A3_A5_A6_RANGES_AND_P2_TRANSFER_NOT_CARRIED |
| `REGATE_PHASE5B` | 08-26 14:22 | HOLD_A6_AND_P1B_SWEEPS_NOT_EXHAUSTIVE… |
| `REGATE2_PHASE5B` | 08-26 20:07 | HOLD_P5_REMAINS_A_SINGLE_SCREEN_MODEL… |
| `REGATE3_PHASE5B` | 08-26 22:30 | HOLD_CONTINUOUS_CANCELLATION_NULL |
| `GATE_EPOCH` | 08-27 13:52 | NEITHER IS DETERMINED BY THE PINNED MODEL |
| `KGATE_EPOCH` | 08-27 14:05 | RULE_A_LOCAL_ANCHORING__B_ADIABATIC_CARRY_GEOMETRICALLY_FORBIDDEN |
| `REGATE4_PHASE5B` | 08-27 14:55 | HOLD_NULL_EXISTENCE_AND_FLATNESS_UNSUPPORTED |
| `AGATE_REGATE5` | 08-27 18:10 | **PASS_PHASE5B** |
| `CGATE_REGATE5_PHASE5B` | 08-27 18:10 | HOLD_HAWKING_DEGENERACY_OVERCLAIM |
| `CGATE_REGATE5_CONFIRM` | 08-27 19:21 | **CLEARED_HAWKING_DEMOTION** |

**Status, stated precisely.** The reduced claim set was passed outright by one seat (agy) and
its hold discharged on the other (codex, after the p9 demotion). **No seat has issued a
`PASS_PHASE5B` token *after* the demotion** — agy's pass predates it and did not raise the
Hawking objection at all; the confirm seat wrote "Phase 5b may pass in the limited reduced sense
described by the prior verdict." That is a discharged hold plus a prior pass, not a fresh
unanimous pass. Anyone who needs the stronger statement should re-gate.

---

## 4. Artifacts and run records

All from this directory, python 3.9.6 / numpy 1.26.4 / scipy 1.13.1.

| script | exit | checks | note |
|---|---|---|---|
| `p1c_rigorous_sweep.py` | 0 | 10/10 | high-w row repaired today |
| `p6_path_transfer.py` | 0 | 6/6 | `nan` repaired today; closure-conditional banner |
| `p7_signed_sweep.py` | 0 | 4/4 | closure-conditional banner + runtime block |
| `p8_thick_limit.py` | **1** | 2/3 | genuine negative result, not a defect |
| `p9_hawking.py` | 0 | 16/16 | section B demoted today |
| `p10_flatness_redo.py` | **1** | 2/4 | genuine anchor mismatch, correctly not tuned |
| `p11_claim1_boost.py` | 0 | 8/8 | claim 1 scope, derived |

Both non-zero exits are correct negative findings and were confirmed as such by two seats.

---

## 5. Routes

`BHU_CLOSED_ROUTES.md` is the register. Summary:

- **C1 — expansion-rate anisotropy: CLOSED**, in the gate's scope — null for *wholly interior*
  signals (comoving sources whose complete light paths stay in exact FRW), not identically null.
  The qualifier is the gate's and governs; my stakes document's blanket "dead, permanently" does
  not.
- **C2 — Hawking radiation: CLOSED AS A SOURCE-PINNED ROUTE.** These artifacts do not define a
  Hawking observable. **Not** a proof that no added horizon-thermodynamics model could ever
  produce one.
- **H1 — boundary glow / optical transfer: HELD**, blocked on the same missing exterior
  thermodynamics as C2.

---

## 6. What would move this forward

Exactly one thing: **someone must supply the missing exterior physics — what the material beyond
the boundary is, how hot it is, how its heat is distributed — as a stated physical model
defended in its own right.** Then the optical route reopens, the Hawking route falls outside C2's
scope, and the null question becomes answerable. Until then every computed signature is a
property of an invented description, and the answer changes with each invention.

The remaining REGATE4 repair item, unaddressed: replacing claim 4 with a theorem bounding an
admissible class of closures. I did not attempt it because the record already supplies a no-root
counterexample inside any natural class. That is a reason, not an excuse — someone else may see
a bound I could not.

---

## 7. What I got wrong, and the shape of it

Recorded because the pattern is more useful than any single correction.

**A check that agrees with itself finds nothing.** p6's `dipole_and_bound()` took `abs()` and
sampled six values, so "min(c1)>0" proved only that six absolute samples were positive — it
could not have seen the sign change. REGATE3 found it. Then, repairing claim 1 today, I built a
threshold test that asked "is the weight below 1e-3 at one point?" — which cannot see a limit,
and reported FAIL on a case the theory gets right. **Same defect, eight hours apart, by me,
after having written the lesson down.**

**Two wrong closures agreeing is not evidence about the thing they approximate.** I built the
phase headline on a cancellation reproduced under two incompatible source maps and read the
agreement as robustness. The gate's counterexample took one line.

**Elegant over robust, twice in one day.** The null was the striking finding; the Hawking factor
of two was the striking argument. Both were promoted above duller, stronger material — and in
the Hawking case the duller argument (the papers never define the quantity) was already written
in my own receipt, ranked fourth.

**Receipts drift from the scripts that produced them.** Two receipts tabulated numbers their
scripts could not produce (p1c's 0.037, p6's 0.930 — both vindicated on repair, but neither
reproducible as delivered). P6's result table was stale by a factor of nine and nobody caught it
for a day. I found it only by re-running the script against its own receipt, which should be
routine and was not.

**Custody details are not cosmetic.** A seat wrote its verdict under another seat's filename
prefix, putting a Gemini PASS next to a Codex HOLD under near-identical names; a `CGATE*` glob
would have merged two engines' opposing verdicts. And the `kun` launcher attaches to a
persistent session rather than starting a fresh one, so a second gate on any topic is not
fresh-context unless launched deliberately otherwise.

**What went right, and it is the only reason any of the above surfaced:** every one of these was
caught by an adversarial reader — a gate, a blind double, or a seat — and not by my own
checking. The phase's method worked. Its findings mostly did not survive it, which is what a
working method looks like.

---

## 8. The public statement

`../WHAT_IS_AT_STAKE_BHU_20260827.md` carries the plain-language version, revised twice and with
the central claim withdrawn in its second revision. Five audio readings are on the record
(queue seq 78, 80, 81, 82, 83); the last three are corrections. The line that survives:

> **This cosmology cannot currently be tested by light, and the reason is not that the test is
> hard — it is that the theory as published does not contain enough physics to say what the test
> would show.**
