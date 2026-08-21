# DECISION MEMO (Revision 3) — the frozen gate is preserved intact, and the investigator declines to proceed

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

`HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821.md`. Its gate history is **generated**, not
recalled — three hand-written versions of this sentence were wrong. Emitted by
`_custody_20260821/build_custody_tables.py` (sha256 `0d4053fb0365b1e2a78efd820781030e405a79fb7e0ede223dafd12385d0f0cc`),
which resolves each gate against the SHA-256 of the revision it recorded reading:

```
A. GATE HISTORY (resolved by SHA-256, not by recollection)
  GATE_FOOTPRINT_GEOMETRY_20260821.md
      verdict : HOLD_FOOTPRINT_GEOMETRY_FINDING
      reviewed: UNRESOLVED — gate recorded no hash
  GATE_FOOTPRINT_GEOMETRY_REGATE_20260821.md
      verdict : HOLD_FOOTPRINT_GEOMETRY_REV2
      reviewed: Revision 1, Revision 2
  revisions on disk: Revision 1, Revision 2, Revision 3 (current)
  NEVER GATED      : Revision 3 (current)
  gate count per revision: each revision above appears at most once — 'gated twice' is false for every revision.
```

Gate 1 recording no hash is itself a finding: a gate that does not record what it read cannot
be audited afterwards, and future briefs will require it.

The findings:

- the measured parent has `Var(cos theta) = 0.057985` about Longo's frozen axis, against a
  full-sky `1/3`;
- `SSE(S) <= SSE(P)` bounds **every** accepted subset at 36,253 full-sphere-equivalent galaxies;
- at the most favourable attenuation `a = 1`, geometric noncentrality is bounded at `4.4888`
  where `4.7351` is needed for 0.95 power.

So the sample cannot deliver the sensitivity the study was designed around, and the frozen gate
cannot notice.

**The concrete cost of proceeding.** Continuing means running the hand-check to measure `a` — the
optional 150-label pilot first, whose only outcomes are PASS-TO-FULL-HC1H or INCONCLUSIVE, and
then the full 850-label HC-1H that yields the `a` HC-6 re-evaluates at. `a` is not used only by
the power gate: it also enters `A_eff`, `sigma_ours` and the F-6 band evaluation. But every one of
those uses sits downstream of a test whose sensitivity the footprint has already bounded, so the
labelling would be spent to obtain a certification we know in advance cannot see the footprint.
That is the expenditure being declined.

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

`CHI_CUSTODY_RECEIPT_20260821.md` (**Revision 4**) carries the ledger, and it too is generated
rather than composed. Three hand audits were wrong three different ways; the fourth stops
asserting and pastes tool output.

What the generator establishes, counting **publications** rather than files:

- **2026-08-20 23:12**, seq 20 — *"The first 3 real values: zero point 27, zero point 20, and minus
  zero point 20."* and *"One leaning each way among the confident pair."* — **52 minutes** after
  the authorization.
- **2026-08-20 23:13 and 23:24**, seq 21 **and seq 22** — the sign statement, republished.
- **2026-08-21 00:50, 10:37 and 11:02**, seq 26, 28 **and seq 30** — the exemplar carrying the exact
  value `χ = 0.013161621987819672`, three publications. **Seq 30 is mine, made this morning**,
  while re-enqueueing that report to obtain a playback receipt. I republished a chi disclosure
  during an audit of chi disclosures.

`GATE_DECISION_MEMO_R2_20260821.md` ruled the question the receipt had left open: publishing all
three then-existing values **was** an aggregation and a summary over χ, because it transmitted the
complete empirical distribution in existence at that moment. The breached clause is **condition
2**; condition 1, the partial-tertile prohibition, was not breached.

These sit here rather than in a footnote because a memo halting a study on integrity grounds
cannot understate that study's own integrity failures — and this one understated them twice before.

## What continues

Acquisition runs to completion, preserving a complete verified sample for the successor without
re-fetching. The verdict estimator is still built and hash-frozen per
`VERDICT_ESTIMATOR_BUILD_SPEC_20260821.md` and is **not** run on real chi.
Successor design: `SUCCESSOR_SCOPE_20260821.md`.

## What this requires

Duho's decision. This memo requests it; no seat may take it alone.
