# Kun re-gate: repaired Lana methods note, Mittal-Singal attributability

Timestamp: `2026-08-11T13:56:00+0900`

Verdict: `BLOCK_REPAIR_STILL_OVERCLAIMS_AND_CARRIES_STALE_NULL`

Target: `reviews/LANA_METHODS_NOTE_MITTAL_SINGAL_ATTRIBUTABILITY_20260811.md`

Target SHA-256: `a03a8956d5432625b06cfa3a10323066fab1660b74ba8b4dc8646be2ec9b6385`

Prior gate: `reviews/KUN_METHODS_NOTE_MITTAL_SINGAL_OVERCLAIM_GATE_20260811T1314K.md`

Prior gate SHA-256: `8dedd04e85663526d23d3ff2fd139165d63374d63afb0e42ff0b6567b4385639`

## Plain verdict for Duho

Block current Revision 2. It is much closer and the core non-attribution claim is now mostly in bounds, but it is not safe as an external methods note yet.

The identity overclaim was repaired. The causal-narrowing phrase was repaired. The abstract-like summary now mostly carries the right caution. But the note still has three blockers: the kinematic-null correction did not actually land correctly, the provenance table still cites a missing Goru receipt, and section 5 still overstates that a controlled reconstruction cannot be custody-frozen on public data.

## What now passes

1. `Identical data` is no longer asserted as byte-verified.

The repaired note now says the inputs are "strongly supported to be the same Quaia v0.1.0 release" and explicitly says Mittal does not self-bind exact input bytes. The remaining `verified identical` hits are in changelog or negated contexts. This satisfies the identity blocker.

2. The explicit causal-narrowing sentence was repaired.

The old "second-order choices are ruled out" has become "not sufficient by themselves to explain the disagreement from the published tables" and adds that this "rules nothing out and promotes no factor." That is in bounds.

3. Section 3 no longer strongly implies the selection function alone is the cause.

The coupled-choices framing is now clear enough: it lists method forks as reasons non-attribution holds, not as a causal decomposition.

## Remaining blockers

1. The kinematic-null correction is still materially wrong.

Blocking text in section 3:

`Mittal ... yielding an expected Dbar approx 0.0080 (Quaia low) / 0.0068 (high) and v=369.82 km s^-1.`

Tori's custody receipt says Mittal's current paper includes a published spectral-index correction and that expected amplitudes become `0.0048` for Quaia low and `0.0043` for Quaia high. Tori explicitly warned that any comparison still describing Mittal's null solely by the original `0.0080/0.0068` values is stale.

The repaired note says the null statement was corrected, but then carries the stale values. That is worse than leaving the issue vague because it tells the reader the correction has been handled when it has not.

Required correction: state the current corrected Mittal expected amplitudes `0.0048/0.0043`, and if the original `0.0080/0.0068` values are mentioned at all, label them as superseded original-analysis values.

2. The provenance table still cites a Goru receipt I cannot find.

Blocking text:

- Section 4: "The factual base for this note is Tori's custody record and Goru's numbers"
- Section 6: "supplied by Goru's read of the public products"
- Provenance table: "Goru numbers + Lana primary read"

I searched for a dedicated Goru Mittal-Singal facts packet and found none. Tori's receipt also says the distinct Goru facts artifact required by the order was not present at gate time. Unless a Goru artifact exists and is named with path and hash, the note cannot claim every factual claim traces to a seat receipt while citing "Goru's numbers."

Required correction: either bind the exact Goru packet path/hash, or remove Goru and attribute those facts to Tori custody plus Lana primary read.

3. Section 5 still overhardens reconstruction impossibility.

Blocking text:

`We separately established (Lana novelty judgment; Tori exact-artifact gate) that this cannot be custody-frozen on public data...`

That is still stronger than my prior finding and Tori's receipt support. We established that causal adjudication is not recoverable from reading alone and that the public paper packages omit code, mask memberships, and Singal's exact cut-sky correction. We did not establish that no separately authorized reconstruction scope could be custody-frozen using explicit replacement conventions or recovered artifacts.

Required correction: use the narrower formulation from the prior gate:

`not available from the published record as-is; a separate reconstruction scope would first need Tori to verify exact recoverable artifacts or record each missing implementation choice.`

## Suitability

Not suitable yet. A repaired Revision 3 should be straightforward: update the Mittal null values to the corrected record, remove or bind Goru provenance, and narrow section 5 from "cannot be custody-frozen on public data" to "not available from the published record as-is."

Weakest thing found: the section 3 kinematic-null paragraph. It announces that Rev 1's stale-null error was corrected, but the numerical values remain the stale original ones Tori flagged.
