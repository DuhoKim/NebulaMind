# DECISION MEMO (Revision 6) — the frozen gate is preserved intact, and the investigator declines to proceed

Hwao, Revision 6, 2026-08-21.

> **THIS IS A DRAFT. NOTHING IN IT IS IN FORCE.**
> It requires an adversarial gate AND Duho's signature. It has neither. **The study has not been
> declined.** Every statement below is what this memo *would* record if signed — read the
> conditional mood as binding, and where a sentence slips into the indicative, that is a drafting
> error and not a fact.

**Correction to the retention claim.** Revision 5 said Revisions 1-4 were "retained byte-for-byte".
For Revision 4 that was false. After `GATE_DECISION_MEMO_FINAL_20260821.md` hashed and reviewed it,
I ran a `sed` over the live memo to update a pointer, and only afterwards copied it to
`_REV4_SUPERSEDED.md`. The retained file is therefore the **post-gate-mutation** version,
`d69be7af81613c3f6a103e5ff833778d…`, not the bytes that were gated. This is the same mutation-during-audit that Blanc
declined to commit on a published report an hour earlier, and I committed it on my own document
without noticing. It is why `_custody_20260821/gate_snapshot.sh` now exists: deliverables are
snapshotted immutably **at dispatch**, not from memory afterwards.

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

`HWAO_FOOTPRINT_GEOMETRY_FINDING_20260821.md`. Its gate history is generated. **The generator
now pins its own digest inside its output**, so an embedded table can no longer cite a hash that
has drifted from the tool that produced it — Revision 5 pinned a stale one:

```
GENERATOR: build_custody_tables.py sha256 94e941093c716b5a1a276a30a270a477b4aec7893d758b5f6edb336ea86a2ba3


  GATE_CHI_CUSTODY_R6_20260821.md
      verdict         : REFUTED_CHI_CUSTODY_R6
      hashes cited    : Rev3(current)
  GATE_DECISION_MEMO_20260821.md
      verdict         : REFUTED_DECISION_MEMO
      hashes cited    : Rev2, Rev3(current)
  GATE_DECISION_MEMO_FINAL_20260821.md
      verdict         : REFUTED_DECISION_MEMO_FINAL
      hashes cited    : Rev1, Rev2, Rev3(current)
  GATE_DECISION_MEMO_R2_20260821.md
      verdict         : REFUTED_DECISION_MEMO_R2
      hashes cited    : Rev2, Rev3(current)
  GATE_DECISION_MEMO_R3_20260821.md
      verdict         : REFUTED_DECISION_MEMO_R3
      hashes cited    : Rev1, Rev2, Rev3(current)
  GATE_DECISION_MEMO_R5_CODEX_20260821.md
      verdict         : REFUTED_DECISION_MEMO_R5
      hashes cited    : Rev1, Rev2, Rev3(current)
  GATE_DECLARATION_INCONCLUSIVE_BY_POWER_20260821.md
      verdict         : REFUTED_DECLARATION_INCONCLUSIVE_BY_POWER
      hashes cited    : Rev3(current)
  GATE_FOOTPRINT_GEOMETRY_20260821.md
      verdict         : HOLD_FOOTPRINT_GEOMETRY_FINDING
      hashes cited    : (none)
  GATE_FOOTPRINT_GEOMETRY_REGATE_20260821.md
      verdict         : HOLD_FOOTPRINT_GEOMETRY_REV2
      hashes cited    : Rev1, Rev2
  GATE_VOID_ON_DESIGN_DEFECT_20260821.md
      verdict         : REFUTED_VOID_ON_DESIGN_DEFECT
      hashes cited    : Rev2, Rev3(current)

  CITATION IS NOT REVIEW. No gate declares its subject by hash, so which revision each
  gate actually reviewed is NOT DETERMINABLE from these files. This tool makes no claim
  about how many times any revision was gated.
  Revisions whose hash is cited by NO gate: (none)
```

That gates do not record the hash of what they read remains a finding; future briefs require it.

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

Blanc's `blanc-ops-overhaul-20260820/DISCLOSURE_LEDGER_AUDIO_20260821.md` (commit `d53fd6c1`,
machine-readable twin `disclosure_audit_20260821.json`) is now the authoritative ledger and
supersedes mine. It establishes **six sha-pinned surfaces for one publication event** — mp3,
caption, deck, alignment `times.json`, report page and `archive.html` — and sweeps all 220
transcripts, of which 18 carry decimals and exactly **one** carries real measured values, the
discriminator being the 2026-08-20 first-measurement date rather than anyone's judgement.
**And the audio speaks full-precision values — `0.834336`, `0.384410`, `-0.640352` — which every
text surface fabricates as `0.27`/`0.20`/`-0.20`, because `nm_caption_norm` sums digit-words after
"point".** `CHI_CUSTODY_RECEIPT_20260821.md` (Revision 6) is stale on this point and is being
rebuilt. My earlier ledger, and it too is generated
rather than composed. Three hand audits were wrong three different ways; the fourth stops
asserting and pastes tool output.

What the generator establishes, counting **publications** rather than files:

- **2026-08-20 23:12**, seq 20 — *"The first 3 real values: zero point 27, zero point 20, and minus
  zero point 20."* and *"One leaning each way among the confident pair."* — **52 minutes** after
  the authorization.
- **2026-08-20 23:13 and 23:24**, seq 21 **and seq 22** — the sign statement, republished. The archive pages carry copies too, and — correcting Revision 5 —
  they **are** attributable: each reading is bound to its report by `data-src` and an
  `href="report-<stamp>-…"`. `20260820T231235` appears in `archive.html` and **not** in
  `archive-2.html`, so the `archive-2` detector hit belongs to a different, pre-crossing reading.
- **2026-08-21 00:50, 10:37 and 11:02**, seq 26, 28 **and seq 30** — the exemplar carrying the exact
  value `χ = 0.013161621987819672`, three publications. **Seq 30 is mine, made this morning**,
  while re-enqueueing that report to obtain a playback receipt. I republished a chi disclosure
  during an audit of chi disclosures.

`GATE_DECISION_MEMO_R2_20260821.md` ruled the question the receipt had left open: publishing all
three then-existing values **was** an aggregation and a summary over χ, because it transmitted the
complete empirical distribution in existence at that moment. The breached clause is **condition
2**; condition 1, the partial-tertile prohibition, was not breached.

Two further facts arrived after Revision 4 and are folded in here:

- **A fourth republication exists in the window.** The ledger records
  `20260820T231324-hwao-report.mp3` published at seq 21 **and seq 22 (23:24:55)** — a second
  publication of the sign-summary report. Blanc's relayed list of three republications omitted it;
  I verified it directly against `queue_ledger.jsonl`.
- **One unenumerated identity is not an unenumerated report.**
  `20260820T232407-20260820T230754-tori-report.mp3` was absent from the queue but is
  **byte-identical** to the enumerated `20260820T230754-tori-report.mp3` — both
  `27e70b61f97b4bf6…`, verified here. A duplicate filename escaped the record; no report did.

These sit here rather than in a footnote because a memo halting a study on integrity grounds
cannot understate that study's own integrity failures — and this one understated them twice before.

## What continues

Acquisition runs to completion, preserving a complete verified sample so a successor need not
re-fetch it. Successor design: `SUCCESSOR_SCOPE_20260821.md`.

**Correction — the verdict estimator does not exist.** Revisions 1 to 3 of this memo said it "is
still built and hash-frozen". That was false and was carried across three revisions unchecked:
`_verdict_20260821/` does not exist, there is no `verdict_runner.py` anywhere in the handoff or
repository, and there is no freeze or gate record for one. What exists is a build spec,
`VERDICT_ESTIMATOR_BUILD_SPEC_20260821.md`, and an open task. Nothing has been built, gated or
frozen, and this memo makes no forward claim that anything will be.

This memo therefore rests on no unbuilt artifact. Its grounds are the footprint geometry and the
frozen text alone.
