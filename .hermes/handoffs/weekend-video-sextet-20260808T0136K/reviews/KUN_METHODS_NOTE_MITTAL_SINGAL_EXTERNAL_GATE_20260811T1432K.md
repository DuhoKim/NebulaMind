# Kun gate: Mittal-Singal methods note external edition

Timestamp: `2026-08-11T14:40:00+0900`

Verdict: `PASS_EXTERNAL_METHODS_NOTE_NO_OVERCLAIM`

Target: `reviews/LANA_METHODS_NOTE_MITTAL_SINGAL_ATTRIBUTABILITY_20260811_EXTERNAL.md`

Target SHA-256: `a79f748e42cf92d1831e6115b7ce55912afe4b0555fb9bc185b6d9428edc292b`

Prior passed internal Rev 3: `reviews/LANA_METHODS_NOTE_MITTAL_SINGAL_ATTRIBUTABILITY_20260811.md`

Prior passed internal Rev 3 SHA-256: `36e4efe8984c8d5f7f6f1996f2d6efb38a1be2ceade49b4622f0131917fb99aa`

## Plain verdict for Duho

The external edition is safe to treat as an external methods note on overclaim grounds.

It is now safe to claim:

`From the published record, the factor-of-three disagreement between two analyses of what is strongly supported to be the same Quaia v0.1.0 release, with Mittal not byte-self-binding exact inputs, cannot be attributed to any single isolated analysis choice, because the choices are coupled, an order-unity correction is unstated, and the two estimate different quantities.`

It is not safe to claim that the analyses are byte-verified identical on Mittal's side, that the selection-function fork is the demonstrated cause, that either paper is correct, or that the universe is anisotropic/isotropic.

## Gate checks

1. Identity strength after citation conversion: `PASS`

The external edition did not upgrade the identity claim. It says "strongly supported to be the same Quaia v0.1.0 release," states that Mittal does not self-bind exact input bytes, and explicitly says the product checksum check verifies the public products and Singal's binding, not Mittal's exact bytes. The DOI/checksum language does not silently become "verified identical."

2. Own-method claims versus external citations: `PASS`

Facts established by the note's own work are labeled as "this note's own product check" or "this note's own reading," not dressed as external authority. That is the right external conversion: readers can see which claims are published-source facts and which are the note's analysis.

3. Section 3 reasoning attribution: `PASS`

The non-attribution reasoning is presented as the note's own reading of the papers. It does not invent a source for the coupled-choices conclusion, and it still frames the selection-function fork as the leading stated difference, not the demonstrated explanation.

4. Provenance table: `PASS`

The provenance table was converted, not deleted. It traces each claim to published sources or the note's stated checks. It does not retain Goru, seat names, or Hwao's non-authoritative assessment as factual support.

5. Protected boundaries: `PASS`

The external edition preserves the required boundaries:

- "We did not re-run either analysis."
- The permitted claim remains qualified by strongly-supported same release and Mittal not byte-self-binding.
- Corrected Mittal expected amplitudes are `0.0048/0.0043`.
- Superseded original `0.0080/0.0068` values are labeled superseded.
- The note draws no inference from numerical relations between expected amplitudes.
- Controlled re-derivation is "not available from the published record as-is," not impossible in principle.
- The selection-function fork remains the obvious candidate but not the demonstrated cause.

## Weakest remaining thing

The weakest remaining thing is that the external edition says "for this note, the v0.1.0 catalogues and selection maps were downloaded and checked" without embedding a hash receipt path in the note itself. That is not an overclaim blocker because the statement is explicitly this note's own check and does not upgrade Mittal's input identity. Tori still binds sources separately.
