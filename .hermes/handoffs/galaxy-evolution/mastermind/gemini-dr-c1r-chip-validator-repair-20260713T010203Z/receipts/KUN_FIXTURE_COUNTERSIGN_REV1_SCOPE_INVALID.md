# Kun Fixture Countersign

Packet: `gemini-dr-c1r-chip-validator-repair-20260713T010203Z`
Role: independent custody/reproducibility gate.

Scope: local-only. No browser, network, live Gemini, DB, dashboard, deploy, public action, or git action.

## Commands and Exit Codes

- `node receipts/_kun_green_gen_run1/gen_expected_dom_facts.mjs` -> exit 0
- `node receipts/_kun_green_gen_run2/gen_expected_dom_facts.mjs` -> exit 0
- `shasum -a 256 receipts/_kun_green_gen_run1/EXPECTED_DOM_FACTS_V2.json receipts/_kun_green_gen_run1/rendered_body_corrupted_v2.html receipts/_kun_green_gen_run1/CORRUPTED_HTML_MANIFEST_V2.json receipts/_kun_green_gen_run2/EXPECTED_DOM_FACTS_V2.json receipts/_kun_green_gen_run2/rendered_body_corrupted_v2.html receipts/_kun_green_gen_run2/CORRUPTED_HTML_MANIFEST_V2.json fixtures/EXPECTED_DOM_FACTS_V2.json fixtures/rendered_body_corrupted_v2.html fixtures/CORRUPTED_HTML_MANIFEST_V2.json` -> exit 0
- `node -e <fixture fact verifier>` -> exit 0

## Hashes

Generated run 1:
- facts: `1b812817fe0f02b576106fcb701a98ea0de7ea3e3c681e9d6fdea90b047a21a1`
- corrupted HTML: `05833834be7b2e54cc3a1aeafd33890e974e40f9e1ae080c95d6f2ebb84665d0`
- corrupted manifest: `76d7fb5f38064a5627381a7f8f97ed13b65172f86b380d363dee0a0afe365b55`

Generated run 2:
- facts: `1b812817fe0f02b576106fcb701a98ea0de7ea3e3c681e9d6fdea90b047a21a1`
- corrupted HTML: `05833834be7b2e54cc3a1aeafd33890e974e40f9e1ae080c95d6f2ebb84665d0`
- corrupted manifest: `76d7fb5f38064a5627381a7f8f97ed13b65172f86b380d363dee0a0afe365b55`

Published fixture files:
- `fixtures/EXPECTED_DOM_FACTS_V2.json`: `1b812817fe0f02b576106fcb701a98ea0de7ea3e3c681e9d6fdea90b047a21a1`
- `fixtures/rendered_body_corrupted_v2.html`: `05833834be7b2e54cc3a1aeafd33890e974e40f9e1ae080c95d6f2ebb84665d0`
- `fixtures/CORRUPTED_HTML_MANIFEST_V2.json`: `76d7fb5f38064a5627381a7f8f97ed13b65172f86b380d363dee0a0afe365b55`

## Published Facts Verified

- Total chips: 108.
- Region chips: S1/S2/S3/S4/S5/ledger = 40/8/3/9/2/46.
- Ledger: 46 paired rows, 37 unique indices, 0 real mapping conflicts.
- Section-2 Citation-cell chips: 27,28,10,11,15,20,30,30.
- GAP units: chip30/token/chip36/token.
- Orphan indices: 2,5,8,9,13,16,18,23,24,29,31,33.
- Duplicate rows: 9.
- Blank short names: 46.
- Corrupted fixture: verification passed; index 10 maps to two URLs.

Kun countersigns the Tori fixture supersession as deterministic and matching the Hwao-published pins.

KUN_C1R_FIXTURE_COUNTERSIGN_GREEN_20260713T010203Z
