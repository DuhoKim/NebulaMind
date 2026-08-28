# Kun re-gate: Lana methods note Revision 3

Timestamp: `2026-08-11T14:00:00+0900`

Verdict: `PASS_METHODS_NOTE_NO_OVERCLAIM`

Target: `reviews/LANA_METHODS_NOTE_MITTAL_SINGAL_ATTRIBUTABILITY_20260811.md`

Target SHA-256: `36e4efe8984c8d5f7f6f1996f2d6efb38a1be2ceade49b4622f0131917fb99aa`

Prior blocked Revision 2 SHA-256: `a03a8956d5432625b06cfa3a10323066fab1660b74ba8b4dc8646be2ec9b6385`

Prior gate: `reviews/KUN_METHODS_NOTE_MITTAL_SINGAL_REPAIR_REGATE_20260811T1331K.md`

Prior gate SHA-256: `5515e927c4f9990055501ef9a9ff132d8dfd7aff0c626830344fe818d615f1ed`

## Plain verdict for Duho

Revision 3 is suitable as an external methods note on overclaim grounds.

It is now safe to claim:

`From the published record, the factor-of-three disagreement between two analyses of what is strongly supported to be the same Quaia v0.1.0 release, with Mittal not byte-self-binding exact inputs, cannot be attributed to any single isolated analysis choice, because the choices are coupled, an order-unity correction is unstated, and the two estimate different quantities.`

It is not safe to claim that either paper is correct, that the selection function alone caused the gap, that the data bytes are verified identical on Mittal's side, or that a future reconstruction is impossible.

## Blocker closure

1. Stale kinematic null: `PASS`

Revision 3 replaces Mittal's superseded `0.0080/0.0068` expected amplitudes with the corrected `0.0048/0.0043` values and labels the old pair as superseded. The note also removes the Rev 2 "numerically comparable" inference. This resolves the stale-null blocker.

2. Goru provenance: `PASS`

Revision 3 removes Goru from section 4, section 6, and the provenance table. I found no invented Goru path or hash. The remaining provenance traces the cuts/numbers to Tori custody plus Lana primary read, which is consistent with the available receipts.

3. Reconstruction overhardening: `PASS`

Revision 3 narrows the claim to "not available from the published record as-is" and states that a separate reconstruction scope would first need Tori to verify exact recoverable artifacts or record missing implementation choices. This resolves the prior overstatement that reconstruction cannot be custody-frozen on public data.

4. Hwao non-authoritative artifact: `PASS`

The note cites `HWAO_LOOSENED_BAR_MITTAL_SINGAL_ASSESSMENT_20260811T1110K.md` only to exclude it and identify its errors. I do not see a factual claim resting on that artifact.

## Scope check

The summary now carries the same qualification as the body. Section 3 still lists the coupled differences, but it frames them as reasons attribution cannot be isolated, not as a causal decomposition. The remaining hits for "verified identical" and the superseded amplitudes occur in changelog/supersession or explicit negation contexts.

Weakest remaining thing: the note still has a lot of changelog text at the top, which makes it heavier than a clean external note. That is not a blocking overclaim problem; it is an editorial decision.
