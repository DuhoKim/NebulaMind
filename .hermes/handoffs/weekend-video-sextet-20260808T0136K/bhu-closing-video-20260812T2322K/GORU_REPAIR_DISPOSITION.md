# DISPOSITION — Goru source-bound repair invalidates frozen draft V2/V1 hashes

Goru's exact-hash number audit returned `PASS WITH REPAIRS` on:

- narration V2 SHA `640d43e1ff299d7e4f28a1d6ef2f3f2e6d21c7d1ea91a60fdf68c330a251d937`
- storyboard V1 SHA `8f99c03d7af951d71dd11c1028c0510d02c244b766b056c93f7dbb3e390930bc`
- ledger V1 SHA `89ac87be41a62c33135be72106781069b434514df663a649c03dc216be95cfb2`

Defect: the exact 95.4% lower-bound value `1.95` is not stated in the sole-authority Lana Revision-5 packet. Its presence in a different landed custody receipt does not permit it here because Duho required every video claim to come from Lana's packet.

The frozen predecessors remain byte-preserved. They are not renderable and no pass on those hashes authorises audio or rendering.

Repaired exact artifacts:

- `NARRATION_DRAFT_V3.md` — SHA-256 `ffed91f6d5625726170d149b5c78987f7b1371104ad469a3651f01156feacd6d`
- `STORYBOARD_DRAFT_V2.json` — SHA-256 `ac1c18fb9b5da1a2dc68330477ae42c0265bbf8e9620fe599929c612cd72ee91`
- `CLAIM_LINE_LEDGER_V2.md` — SHA-256 `f0fce1fdc9404d8d799064bbe5a44ac564e38b2b4bb11f45ac9ff42ce38eb89e`

Repair is deliberately minimal:

- Narration now says the result does not clear 2.00 at 95.4% credibility, exactly as Lana's packet permits.
- Storyboard no longer plots or prints a 95.4% lower-bound value; it marks only that the result does not clear 2.00.
- Ledger now explicitly forbids inventing that unstated bound.

Verification:

- unsupported exact-value sweep: PASS absent from all three repaired artifacts;
- 11/11 assertion headings; 0 divider cards;
- opening card remains 34 planned seconds;
- narration/storyboard text match 11/11;
- no paid-generation notes;
- no audio or render started.

All three seats must re-gate these new exact hashes. Any prior PASS/HOLD on predecessor hashes is historical only.
