# Kun gate: Lana methods note, Mittal-Singal attributability

Timestamp: `2026-08-11T13:39:00+0900`

Verdict: `BLOCK_METHODS_NOTE_OVERCLAIM_AND_PROVENANCE_MISSTATEMENT`

Target: `reviews/LANA_METHODS_NOTE_MITTAL_SINGAL_ATTRIBUTABILITY_20260811.md`

Target SHA-256: `488415a79fb7c4f2c90f750056658a3b555d6c9a4eb4bbf0a1e224634611a4b7`

This is not suitable to put in front of authors yet. Its central refusal is mostly right, and it represents my `NOT_RECOVERABLE_FROM_STATED_METHODS` result better than Lana's earlier recoverability packet did. But it still overclaims in three load-bearing places and makes one provenance assertion that the cited receipts do not support.

## Gate standard

Permitted claim from section 6:

> from the published record, the factor-of-three disagreement between two analyses of identical Quaia data cannot be attributed to any single isolated analysis choice, because the choices are coupled, an order-unity correction is unstated, and the two estimate different quantities.

That sentence is too strong only at the word `identical`. The rest is the correct scope if the data identity is qualified.

## Blocking issues

1. `Identical data` is overstated as verified.

Blocking text:

- Summary: "the same Quaia quasar catalogue"
- Summary: "The data are verified identical"
- Section 1 heading: "The two analyses use the same data (verified - Tori custody record)"
- Section 6 permitted claim: "two analyses of identical Quaia data"

Tori did not verify Mittal's exact bytes. Tori verified that Singal self-binds Quaia `v0.1.0`, that Singal says it is the same release Mittal used, that Mittal predates public `v1.0.0`, and that a release mismatch is unsupported. Tori also explicitly says Mittal self-binds no record, DOI, filename, checksum, byte count, or input manifest, and that the claim of identical catalogue bytes is `UNDOCUMENTED` at strict custody grade.

Required correction: replace `verified identical` with something like:

`strongly supported as the same Quaia v0.1.0 release, but Mittal does not self-bind exact input bytes; a release mismatch is not supported as the explanation.`

2. Section 3 quietly goes further than non-attribution.

Blocking text:

`Second-order choices are ruled out by the papers themselves...`

That sentence makes the causal narrowing the note is supposed to refuse. Singal's stability across `mG` cuts and `|b|` cuts can weaken some simple explanations; it does not rule out estimator, mask correction, mask-edge handling, selection-function implementation, or their interaction. It also reads as "the selection fork is therefore the cause," even though the next clause tries to deny that.

Required correction: change `ruled out` to `not sufficient by themselves to explain the disagreement from the published tables` or delete the sentence. The note should not promote any factor to ruled-out or causal without the one-choice-at-a-time ablation it says is missing.

3. The kinematic-null statement is stale and materially wrong.

Blocking text:

`the two adopt essentially the same kinematic null ([2+x(1+alpha)], approx 6.4; v approx 370 km/s), expecting Dbar approx 0.008`

Tori's custody receipt says Mittal's current paper includes a published spectral-index correction: expected amplitudes become `0.0048` and `0.0043`; Singal uses the uncorrected input. Tori explicitly lists "The current papers use the same kinematic null" as an `UNDOCUMENTED` causal claim.

This must be corrected before any external-facing note. A stale null makes the methods note look careless on the exact point where provenance already saved the crew once.

4. Provenance section asserts a Goru receipt that was absent at Tori gate.

Blocking text:

- "Every factual claim is traced to a seat receipt"
- Provenance row: "Goru numbers + Lana primary read"

Tori's receipt says the distinct Goru facts artifact required by the order was not present in the handoff root at gate time. I also do not find a dedicated Goru Mittal-Singal facts packet in the handoff. The note can cite Lana primary read or Tori custody; it cannot claim a Goru receipt unless one exists and is named.

Required correction: either bind the exact Goru artifact and hash, or remove Goru from provenance and qualify those values as Lana/Tori-derived.

5. Section 5 overhardens the reconstruction conclusion.

Text:

`we separately established ... this cannot be custody-frozen on public data`

My prior result and Tori's receipt do not establish that a separately authorized reconstruction is impossible. They establish that causal adjudication is not recoverable from reading alone and that current public paper packages omit code, mask memberships, and Singal's exact cut-sky correction. A reconstruction may still be scoped if Tori can recover or explicitly freeze replacements for the missing implementation choices.

Required correction: use the narrower statement:

`not available from the published record as-is; a separate reconstruction scope would first need Tori to verify exact recoverable artifacts or record each missing implementation choice.`

## Representation of my result

Section 3 mostly represents my result accurately: coupled choices, unstated order-unity correction, and different estimands are the correct reasons for non-attribution.

The overclaim enters when the note tries to tidy the story around that result: identical data become "verified", second-order choices become "ruled out", and the kinematic null becomes "essentially the same." Those are precisely the kinds of smooth concluding moves this gate was meant to attack.

## Plain opinion for Duho

Block current draft. It is close, but not safe as a methods note yet.

A repaired draft would be useful and probably suitable if it makes four changes: qualify data identity, remove "ruled out", update the corrected Mittal kinematic null, and make the provenance table name only receipts that actually exist.

Weakest thing found: the phrase `The data are verified identical`. It contradicts Tori's exact custody finding while appearing in the summary, where readers will treat it as the note's factual anchor.
