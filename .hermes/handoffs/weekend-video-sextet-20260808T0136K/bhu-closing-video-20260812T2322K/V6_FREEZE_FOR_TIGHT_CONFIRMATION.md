# BHU V6 — S4-only tight delta freeze

Status: `FROZEN_V6_AWAITING_TIGHT_THREE_SEAT_CONFIRMATION`

No audio, frames, render, upload, publication, or acceptance is authorised by this freeze.

## Exact V6 hashes

- `NARRATION_DRAFT_V6.md`
  - SHA-256 `6bdc2ca6676a3e83a72b5cc7d0cf6ab0d3e12b44a5090fca9efb0b1e5b2fb4f0`
- `STORYBOARD_DRAFT_V6.json`
  - SHA-256 `26b6c2b8049d1f7196a7f75570a66e9f732d5b9a9457c07c40e096caff7a64b6`
- `CLAIM_LINE_LEDGER_V6.md`
  - SHA-256 `871a808c4f2af94e24ef68b19cef416b7f7e3295720dab25ef8676753c845b5a`

Sole scientific authority remains Lana Revision 5, SHA-256 `b244ea0a3bb276a673fd88efaad248322a7adaa521e31d0a864e6949de5aa516`.

## Tight delta contract

The canonical storyboard differs from frozen V5 in exactly three fields, all on Card 05:

1. `cards[4].narration`
   - `the packet says it does not`
   - → `the closing record says it does not`
2. `cards[4].diagram` callout text
   - `the packet states only that the result does not clear 2.00`
   - → `the closing record states only that the result does not clear 2.00`
3. `cards[4].on_screen_support[3]`
   - `THE PACKET STATES ONLY THAT THE RESULT DOES NOT CLEAR 2.00`
   - → `THE CLOSING RECORD STATES ONLY THAT THE RESULT DOES NOT CLEAR 2.00`

The standalone narration mirrors change 1. The claim ledger is byte-identical to V5 because Lana explicitly allowed internal ledger vocabulary to retain `packet`.

No other canonical storyboard field changed. In particular:

- all 11 headings are unchanged;
- all other narration, diagram, and on-screen strings are unchanged;
- all card timings and total planned duration are unchanged;
- every number, tick instruction, plot range, and 95.4% non-scaled-callout prohibition is unchanged;
- the existing Card 06 heading is unchanged;
- S4b was skipped, so the adjacent 68.3%/95.4% repetition remains exactly as passed;
- no version/status/header string inside the copied artifacts was changed. V6 identity is established by filenames and hashes, avoiding an unrelated administrative-text delta.

## Mechanical verification

- Canonical changed-field count: exactly 3.
- Canonical changed paths: exactly the three listed above.
- V5/V6 timings: byte-equivalent after JSON parse; total planned duration unchanged.
- V5/V6 ledger: byte-identical.
- V6 Card 05 `the packet`: zero occurrences.
- V6 Card 05 `the closing record`: exactly three canonical occurrences.
- Standalone narration: one removed line and one added line, differing only in the S4 referent.

## Required tight confirmation

The same Lana, Goru, and Kun seats need check only:

1. that the three S4 substitutions preserve attribution and claim strength;
2. that the canonical V5→V6 diff contains exactly those three fields;
3. that every other canonical field, timing, number, and ledger byte is unchanged.

Any HOLD blocks. Rendering begins only after all three issue unconditional PASS confirmations bound to all three V6 hashes.
