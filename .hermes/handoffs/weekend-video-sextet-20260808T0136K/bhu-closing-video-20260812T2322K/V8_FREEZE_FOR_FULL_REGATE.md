# BHU V8 — full three-seat exact-hash freeze

Status: `FROZEN_V8_AWAITING_FULL_THREE_SEAT_EXACT_HASH_PASS`

No audio, frames, render, upload, publication, acceptance, or carry-forward gate is authorised by this freeze. This is not a tight delta. Any HOLD blocks.

## Exact V8 review targets

- `NARRATION_DRAFT_V8.md`
  - SHA-256 `6dc0ca1984e9fa262a28c39cc23b6559dac0cc1c4ebb6026693fb7b5b004f35c`
- `STORYBOARD_DRAFT_V8.json`
  - SHA-256 `56bcf195a871ae4f60f822b3e8cc3c5bd90f262a1a8325ca7b18a42b0917ddcb`
- `CLAIM_LINE_LEDGER_V8.md`
  - SHA-256 `aa4b459a3b4112dc40feabb5e84a0853e205db400d0adfc9d58cab248f6cc9aa`
- `DETERMINISTIC_DIAGRAM_SPEC_V8.md`
  - SHA-256 `e296e2f29a00cf714cbc9f562bb224d224e185fb8d6a5ecb03e718cf5e1cc52e`

All four hashes are mandatory in each full-seat verdict. The graphics specification is a review target because graphics carry scientific/comprehension meaning in this version.

## Build and verification records

- `V8_BUILD_MATRIX.json`
  - SHA-256 `1afc44f665285788e421b2b1ca3698a3e9c1b0fdf4710e3f72d439b21ea5b2ae`
  - Audits 27 copy replacement units and eight graphics: G1–G8.
- `V8_BUILD_VERIFICATION.json`
  - SHA-256 `90c37c16352b494b878f3fd08206093df41d2f14e810025061366a5b6a27adbf`
  - Result: `PASS_BUILD_SEMANTICS_AWAITING_FULL_THREE_SEAT_GATE`.
- `V8_EXPECTED_HASHES.json`
  - Fail-closed expected-hash control for `preflight_gate_v8.py`.

## Pinned inputs

- Lana simplify/de-name spec: `53e2c694334cdb9913e8d14e91032dbfb552e5c2eee5d1aea75360403f4b3274` (12,472 bytes).
- V7 narration: `3380497f0514e906db8463d0fdd2ffd1f0b02b37ac6825e3bfdec86011c2edc0`.
- V7 storyboard: `3077f0636385487bb4092d2032c18bbedaedb647780bbfc581e59027c87a8d2b`.
- V7 claim ledger: `871a808c4f2af94e24ef68b19cef416b7f7e3295720dab25ef8676753c845b5a`.
- Sole scientific authority: Lana Revision 5, `b244ea0a3bb276a673fd88efaad248322a7adaa521e31d0a864e6949de5aa516`.

The authority and old-text references above are internal custody records and are not audience copy.

## Full-build results

- Lana's specification was read in full before edits.
- Exactly 27 audited copy replacement units landed.
- Exactly eight graphics are contracted: four revisions/new builds (G1/G2/G3/G5), three existing graphics retained (G4/G6/G7), and the G8 opening-map/boundary revision.
- All 11 assertion headings are unchanged and nonempty.
- All source-claim IDs and packet-line mappings are unchanged.
- The claim ledger differs from V7 only in its H1 version label.
- Standalone narration is generated from the canonical storyboard and matches all 11 cards.
- Cards 03 and 09 retain their V7 diagrams byte-for-byte. Card 10 retains its V7 construction and labels except that the non-printing internal layout word `ledger` becomes `comparison`.
- B-10 is included exactly as proposed and remains contingent on Kun's exact-hash sign-off.

## Whole audience-projection sweep

The sweep covers title, slug, every assertion heading, all narration, complete diagram instructions and quoted/printable labels, every on-screen support string, and string-valued render/visual metadata.

Results:

- viewer-facing Duho/Lana/Goru/Kun/Tori/Yui/Hwao occurrences: 0;
- viewer-facing crew-internal `packet`/`ledger`/`receipt`/`lane`/`seat`/`freeze`: 0;
- viewer-facing filenames, hashes, or stale V7/V5 filing labels: 0;
- banned claim-strength strings: 0;
- published-author attributions Brown, Lee, Rho, Demorest, and Fonseca: present.

An underscore-safe raw sweep also classified every local-name occurrence outside the audience projection: one storyboard authority-path token, one narration source-scaffolding token, five claim-ledger custody/claim-row tokens, zero graphics-spec tokens, nine allowed build-matrix old-text/sign-off audit tokens, and zero unclassified occurrences.

Internal source scaffolding and the internal claim ledger retain historical names as Lana's specification explicitly requires; they are excluded from the audience projection and must never be rendered.

## A1 and A2 load-bearing checks

A1:

- Exact narration sentence is present.
- Exact all-caps boundary badge is present in both printable support and the canonical diagram instruction.
- Canonical instruction requires the badge from frame one through the full Card 01.
- At 120 WPM, `side-interest` completes at 9.0 seconds and the `not part…` marker starts at 9.5 seconds.

A2:

- Card 02 introduces `the closing record` as the document this video reports from.
- Later attribution occurs only after that introduction.
- Cards 03, 05, and 06 use the required found/says/does-not-decide forms; Card 04 uses `our record surveyed` exactly as specified.

## Required timing adjudication — no silent repair

Card 01 contains 89 narration words. Under the storyboard's target cadence:

- 120 WPM: 44.50 seconds;
- 128 WPM: 41.72 seconds;
- 135 WPM: 39.56 seconds;
- planned Card-01 duration: 35 seconds.

The exact visual badge satisfies the opening boundary from frame one. However, the full spoken phrase `not part of the lab's research programme` completes at 12.5 seconds at 120 WPM, and the full narration does not fit 35 seconds anywhere in the 120–135 WPM target range. No unreviewed deletion, wording change, speed-up, or timing extension was made. Lana and Kun must explicitly adjudicate this during the full gate.

## Card 05 visual boundary

- Demorest and Fonseca exact values are spoken once and printed exactly.
- The finite 68.3% interval remains above 2.00.
- The 95.4% state uses only an open-ended gradient fading through 2.00.
- Its mode label is non-scaled and outside the mass plot.
- Absolute prohibition remains: no 95.4% endpoint, arrow, tick, bracket, marker, whisker, shaded boundary, axis-aligned glyph, visible lower edge, or other position-bearing terminus at any scaled mass value.

## Fail-closed gate state

`python3 preflight_gate_v8.py` currently returns exit 2:

`HOLD: no full exact-hash LANA V8 verdict`

The gate requires unconditional, exact-current PASS verdicts from Lana, Goru, and Kun, each binding all four review-target hashes. No prior V7 verdict carries forward. Only after the script returns `PASS_V8_FULL_THREE_SEAT_EXACT_HASH_GATE_RENDER_AUTHORIZED` may audio or frames be produced.
