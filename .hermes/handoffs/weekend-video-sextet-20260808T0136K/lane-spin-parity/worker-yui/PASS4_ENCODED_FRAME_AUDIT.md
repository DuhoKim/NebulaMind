# Spin worker-Yui — isolated deepening pass 4 temporal encoded-frame audit

Extraction completed: 2026-08-07T19:34:28.270561+00:00 (2026-08-08T04:34:28.270561+09:00)
Audit completed: 2026-08-08T04:42:35+09:00
Scope: exact held Hwao candidate, read-only; separate from sealed v8 static proposal.
Verdict: `FAIL_SCIENTIFIC_PRESENTATION_AND_HELD_SOURCE_GATE`

## Fresh temporal extraction

- Candidate: `/Users/duhokim/HermesOps/cockpit/videos/spin-parity-census-narrated-20260808T0149.mp4`
- SHA-256: `02fe11f0dd9bacc9a46ca2ec8b67764bd871ce2e2dab0f59990f36df11ee8431`; exact official-freeze match.
- Probe: 243.300 s; 28,637,729 bytes; H.264 1920×1080 at 30 fps; AAC mono 24 kHz.
- Fresh scene detection at threshold 0.04 again found 15 cuts and 16 scenes.
- Pass 4 expands the midpoint-only audit to 48 independent decodes: early, midpoint, and late samples for every scene. Early/late samples are one second inside each detected cut.
- Fresh contact sheets: `qa/pass4_encoded_audit/contact_sheet_early.png`, `contact_sheet_mid.png`, and `contact_sheet_late.png`.
- Exact receipt and per-frame hashes: `qa/pass4_encoded_audit/extraction_receipt.json`.
- No candidate byte, audio, shared tool, public asset, or storyboard-of-record was changed.

## Temporal scientific-presentation audit

The early, midpoint, and late sheets show the same complete card content. No headline, body, plot, axis, point, error bar, matrix value, caveat, provenance line, URL, or status boundary enters late, disappears early, or changes before the cut. The prior failure is therefore persistent across scene dwell time rather than an unlucky midpoint sample.

The encoded story remains exactly one opening, ten later text/hero-number cards, and five figures. Scene 5 is method-reusable. Scenes 7, 9, 10, and 11 remain dominant quarantined-result figures from one second after their cuts until one second before the next cuts.

- **Scene 1:** the substantive-measurement title and sky-versus-classifier premise remain dominant throughout; no held boundary appears later.
- **Scene 5:** sequential `rung` grammar, alternative-readout ambiguity, unprinted exact bar values, and internal source provenance persist throughout.
- **Scene 7:** the headline, eight result points, error bars, zero line, small negated caveat, and internal result provenance remain continuously visible. Full-resolution early/mid/late inspection shows no transition or claim change.
- **Scene 9:** the four large significance bars and threshold remain continuously dominant. The provenance still ends abruptly after `LANA_T3_REDERIV` because of the internal text-width limit established in pass 3.
- **Scene 10:** the paired-flip matrix and result prose remain continuously dominant while the storage frame and independent review gate stay absent.
- **Scene 11:** the numerical decomposition, uncertainty bars, and `the flip is real` prose remain continuously dominant; the small caveat never becomes a status gate.
- **Scene 16:** the URL/work-in-progress close remains unchanged and never gains `RESULT HELD`, `FRAME UNSTATED`, or a separate-authorization boundary.

## Encoded temporal stability finding

All 16 scenes are byte-nonstatic across early/mid/late samples because of low-level background/encode variation. Contact-sheet and full-resolution inspection finds no semantic animation or content transition. The dominant slide content is visually stable.

Deterministic Tesseract signatures at confidence 50 are exactly identical across all three samples for 8/16 scenes. Token-multiset similarity remains at least 0.976 for every scene except scene 7. Scene 7 falls to 0.888889 even though only 0.0364583% of pixels change by more than eight levels between midpoint and late samples and the full-resolution frames are visually content-identical. This is not a claim transition; it shows that the tiny caveat/provenance/plot-label layer is near machine-readability limits while the dominant result plot remains robust. Small disclaimer copy cannot carry the scientific gate.

The fresh temporal evidence strengthens, rather than changes, the presentation verdict: the result assertions persist throughout each result scene, while the source/status caveats remain visually subordinate and encode-fragile.

## Sealed-v8 disposition and temporal guard

Fresh pass-4 review found no evidence-backed defect in v8's sealed pixels. V8 already gives every frame a prominent `RESULT HELD` badge, keeps result plots and values absent, uses audience-readable provenance, and closes on a full-screen known/unresolved/not-claimed boundary. No v9 is warranted.

If Hwao integrates v8 into motion, the status boundary must persist from the first stable frame through the last stable frame of every scene. A fade, entrance, or exit must not temporarily remove `RESULT HELD`, reveal result content, or make a small caveat carry the gate. This is an integration guard, not a change to sealed v8 bytes and not authorization to render or narrate.

## Pass-4 exact blocker deepening

Pass 4 closes two remaining absence-proof blind spots without reading science into the result:

1. All six non-UTF-8 files are classified and hash-bound: four gzip data archives and two literature PDFs. Every one predates T4 by source filesystem metadata; there is no post-T4 binary file that could hide an unscanned review record.
2. Nine UTF-8 files postdate T4. Four identify T4. Zero post-T4 files contain both the exact T4 SHA-256 and exact frozen A3.8 SHA-256 required by the review contract, and zero files satisfy the conservative minimum marker combination of both hashes, a first-opened ledger, independent language, and review/verdict language.

The deterministic evidence is `qa/pass4_unblock_contract_scan.json`. This packet records only marker presence, file metadata, and hashes; it does not copy T4 measured values or adjudicate a branch.

## Integrator-safe next action

Preserve 0149 as failed evidence. If Hwao elects to integrate the method-only proposal, start from sealed v8 and apply the temporal guard above. Do not reuse held scenes 7, 9, 10, or 11, and do not transfer their values into new cards. Result integration, narration, candidate encoding, publication, and public wiring remain separate explicit gates.
