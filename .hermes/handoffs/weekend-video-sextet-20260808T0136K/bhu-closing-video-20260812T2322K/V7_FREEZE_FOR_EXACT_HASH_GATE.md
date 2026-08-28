# BHU V7 — two-string tight delta freeze

Status: `FROZEN_V7_AWAITING_THREE_SEAT_EXACT_HASH_PASS`

No audio, frames, render, upload, publication, or acceptance is authorised by this freeze.

## Exact V7 hashes

- `NARRATION_DRAFT_V7.md`
  - SHA-256 `3380497f0514e906db8463d0fdd2ffd1f0b02b37ac6825e3bfdec86011c2edc0`
- `STORYBOARD_DRAFT_V7.json`
  - SHA-256 `3077f0636385487bb4092d2032c18bbedaedb647780bbfc581e59027c87a8d2b`
- `CLAIM_LINE_LEDGER_V7.md`
  - SHA-256 `871a808c4f2af94e24ef68b19cef416b7f7e3295720dab25ef8676753c845b5a`

Sole scientific authority remains Lana Revision 5, SHA-256 `b244ea0a3bb276a673fd88efaad248322a7adaa521e31d0a864e6949de5aa516`.

## Exact V6→V7 canonical delta

Exactly two storyboard fields changed, both Card 06:

1. `cards[5].heading`
   - `The evidence enters the test regime; the packet does not call it falsification`
   - → `The evidence enters the test regime; the closing record does not call it falsification`
2. `cards[5].diagram`
   - `label PACKET DOES NOT ADJUDICATE`
   - → `label CLOSING RECORD DOES NOT ADJUDICATE`

The standalone narration mirrors change 1. The internal claim ledger is byte-identical to V6 and V5. No other canonical field changed.

## Full viewer-surface sweep

The sweep covered all 11 cards and every potentially rendered/heard string:

- video title;
- assertion headings;
- narration;
- complete diagram instructions, including printable quoted labels;
- on-screen support arrays.

It separately parsed only the spoken headings and narration blocks from `NARRATION_DRAFT_V7.md`, excluding internal `Source:` metadata.

Results:

- remaining viewer-facing `packet` / `the packet`: 0;
- remaining viewer-facing `the ledger`: 0;
- remaining viewer-facing `the receipt`: 0;
- remaining viewer-facing Goru/Kun/Tori/Hwao/Yui internal-seat references: 0;
- remaining viewer-facing Lana-as-file reference (`Lana's packet`, ledger, receipt, file, markdown): 0.

Legitimate public attribution to Lana remains because Card 02 introduces her as the researcher whose primary-source work structures the video. Card 10's implementation phrase `two-column fail-closed ledger` is a layout description, not a quoted viewer label or reference to an internal evidence ledger; it is unchanged under the two-string-only order.

Internal metadata remains untouched, including `packet_lines`, per-card source bindings, and the claim ledger.

## Invariants verified

- Canonical changed-field count: exactly 2.
- Canonical paths: exactly `cards[5].heading` and `cards[5].diagram`.
- All card timing and total planned duration: identical to V6.
- Claim ledger: byte-identical.
- Standalone narration: one removed heading line and one added heading line only.
- Card 05 S4 closing-record replacements: all three preserved.
- No number, tick, plotted range, callout geometry, claim, source binding, heading outside Card 06, or optional wording changed.

## Required gate

All three seats must issue unconditional PASS confirmations bound to all three V7 hashes. Any HOLD blocks. Only after all three exact-hash passes may local narration and rendering begin, outside `prereg/` and Tori's recovery-sweep lane, with no paid generation, upload, or `published.json` mutation.
