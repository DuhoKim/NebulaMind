# DECISION MEMO — the frozen gate is preserved intact, and the investigator declines to proceed

Hwao, 2026-08-21 18:56 KST. **Draft for gating and for Duho's signature. Not effective until both.**
Supersedes two refuted attempts, each retained byte-for-byte:
`DECLARATION_INCONCLUSIVE_BY_POWER_20260821_REFUTED.md` and
`DECLARATION_VOID_ON_DESIGN_DEFECT_20260821_REFUTED.md`.

## What this memo is

**It is not a preregistered outcome and does not claim one.** It does not declare
INCONCLUSIVE-BY-POWER, INCONCLUSIVE, REPRODUCED-LONGO, REJECTED-AT-LONGO-AMPLITUDE, or void. It
invents no category, reinterprets no frozen text, and asks nothing of section 5 or F-6.

It records a decision that lies **outside** the preregistration: the investigator chooses not to
carry the study further. A principal investigator declining to run is not a preregistration event.
Nothing in the frozen document compels anyone to proceed, and nothing in it is amended by stopping.

This path was identified by the gate that refuted the previous attempt, which ruled it superior to
what I had drafted. It is adopted because that ruling is right.

## The frozen gate is left exactly as it stands

HC-6 is preserved unexecuted and unreinterpreted. For the record of what it is:

- Its freeze-time firing is already on record — BS-8: power ~= 1.0000 at N = 130,076,
  a = 0.999711, A_eff = 0.04077642.
- Its **second, pre-unblinding firing has not occurred and cannot occur yet**, because it is
  evaluated at the noise-corrected lower-bound hand-checked `a`, and `a` is measured by the
  150-label hand-check, which requires strata, which require a complete sample.

**No PASS is asserted here, and none is fabricated.** What is asserted is narrower and is
established by inspection of the frozen text: HC-6 is evaluated at exactly two inputs,
`A_eff = (2a-1)*0.0408` and bound `N`. **Neither is a footprint quantity.** The analytical logic
it evaluates is `spike/sim_power.py`'s, which draws `costheta` uniformly on `[-1,1]` and assumes
`mean(cos^2) = 1/3`. Whatever it returns, it returns without inspecting where on the sky the
sample lies.

## The reason for declining

`HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821.md` (Revision 3), twice gated and never refuted:

- the measured parent has `Var(cos theta) = 0.057985` about Longo's frozen axis, against a
  full-sky `1/3`;
- `SSE(S) <= SSE(P)` bounds **every** accepted subset at 36,253 full-sphere-equivalent galaxies;
- at the most favourable attenuation `a = 1`, geometric noncentrality is bounded at `4.4888`
  where `4.7351` is needed for 0.95 power.

So the sample cannot deliver the sensitivity the study was designed around, and the frozen gate
cannot notice.

**The concrete cost of proceeding** is the clearest way to put it: continuing means asking Duho to
hand-label 150 blinded galaxies in order to measure an `a` whose only use is to feed a
calculation that cannot see the footprint, and thereby to obtain a certification we already know
is uninformative. That is the expenditure being declined.

## What this memo does NOT claim

- **Nothing about Longo.** Declining to run is not rejection. An instrument that could not reach
  the designed sensitivity cannot reject the amplitude it could not detect.
- **Nothing about the sky.** The canonical boundary sentence stands.
- **Nothing about black-hole-universe cosmology**, in either direction. Duho's 2026-08-21
  confirmation places this lane inside the BHU programme as scope and motivation; it licenses no
  inference from any outcome here, and there is no outcome here.
- **No fault in the instrument's mechanics** — weights, tau, the bit-exact antisymmetry receipts,
  the committee and the hand-check harness are untouched by this evidence. **The statistical
  estimator and power protocol are impeached**: F-1's `3 * D_hat` does not transfer to this
  footprint, F-4 and F-7 inherit the same `1/3`, and `sim_power.py` is two-sided where F-3 is
  one-sided.

## Resulting status of the study

**Halted by investigator decision. No preregistered outcome reported.** That is an unusual status
and is stated plainly rather than dressed as a result: this study does not report INCONCLUSIVE,
and it does not report a null. It reports nothing, and the record explains why.

## Disclosed alongside

`CHI_CUSTODY_RECEIPT_20260821.md` (Revision 2) records that a **summary over chi signs** was
published in `report-20260820T231324-hwao-report.html` 43 minutes after K-8 — "one leaning each
way among the pair the committee was confident about" — in breach of the letter of
`K8_CROSSING_AUTHORIZATION_20260820.md` condition 1, with no discernible scientific consequence.
It is disclosed here rather than filed separately, because a memo that halts a study on integrity
grounds must carry that study's own integrity failures on its face.

## What continues

Acquisition runs to completion, preserving a complete verified sample for the successor without
re-fetching. The verdict estimator is still built and hash-frozen per
`VERDICT_ESTIMATOR_BUILD_SPEC_20260821.md` and is **not** run on real chi.
Successor design: `SUCCESSOR_SCOPE_20260821.md`.

## What this requires

Duho's decision. This memo requests it; no seat may take it alone.
