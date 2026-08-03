# Goru fixture review — BLOCKED / invalid evidence

The Goru lane printed its done marker, but independent file review rejects the second-pass `EXPECTED_DOM_FACTS.json` and `CORRUPTED_HTML_MANIFEST.json` as invalid test evidence.

Observed contradictions with the sealed HTML and Hwao/Lana pins:

- S2 lists eight rows with every `citation_chips` array empty; the sealed HTML has `[27,28,10,11,15,20,30,30]` in the eight dedicated Citation cells.
- S5 lists only three units named `GAP1`, `GAP3`, and `GAP5`; the sealed report has four logical GAP lines, with chips on GAP1/GAP3 and absence tokens on GAP2/GAP4.
- Ledger output splits chip and anchor into separate pseudo-rows rather than pairing each chip with the following anchor; it therefore cannot establish the 46 pairs / 37 unique / 0 conflict map.
- The corrupted fixture manifest says `verification_passed: false` and reports no inconsistent mappings, contradicting the requested positive corruption fixture.
- The done marker therefore proves only that the lane stopped, not that the artifacts are correct.

Custody copies preserved byte-identically:

- `EXPECTED_DOM_FACTS_GORU_INVALID.json` sha256 `1924a8d5dcbeb5bd8572296c8897cd0a9e65569d42a9fa3aa04977cd550030f9`
- `CORRUPTED_HTML_MANIFEST_GORU_INVALID.json` sha256 `ce388944ad852fff16d060b1c23d918c1b83c18aa6b0b36268e37c84a0b98fb3`

These invalid outputs must not be used as GREEN expectations. Tori has escalated to Hwao and will build/verify corrected facts from the real sealed HTML before authoring RED tests.

GORU_C1R_FIXTURE_REVIEW_BLOCKED_20260713T010203Z
