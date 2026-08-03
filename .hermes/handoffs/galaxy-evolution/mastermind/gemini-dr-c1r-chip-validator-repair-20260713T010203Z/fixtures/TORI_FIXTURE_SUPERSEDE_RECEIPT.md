# Tori fixture supersession receipt

Authority: `HWAO_GORU_FIXTURE_ADJUDICATION.md`
Status: independently countersigned by Kun rev2

## Custody and parser pin

- Sealed HTML input sha256: `78ed129c47daf9300d9ed319aa1ffe95bbb0d1810a223733afaf48c4372f2bbc`.
- Generator: `gen_expected_dom_facts.mjs` sha256 `7e0cb71c2cfce81ddb4467873b978f9956a486070a8d2eeffc42a61d8d38ac11`.
- parse5 path: `/Users/duhokim/NebulaMind/NebulaMind/frontend/node_modules/parse5/dist/index.js`.
- parse5 version: `7.3.0`.
- parse5 module sha256: `b825162aced2e79be8d68d45efb1f89ec34ed4189467195a071a0d7b694a19d4`.
- parse5 package manifest sha256: `8196284780fe95c3245a40e3c17b45fc85ef709f1211775987d037e5e873fe95`.

## Deterministic outputs

- `EXPECTED_DOM_FACTS_V2.json`: `1b812817fe0f02b576106fcb701a98ea0de7ea3e3c681e9d6fdea90b047a21a1`.
- `rendered_body_corrupted_v2.html`: `05833834be7b2e54cc3a1aeafd33890e974e40f9e1ae080c95d6f2ebb84665d0`.
- `CORRUPTED_HTML_MANIFEST_V2.json`: `76d7fb5f38064a5627381a7f8f97ed13b65172f86b380d363dee0a0afe365b55`.
- Two consecutive generator executions produced byte-identical outputs.

## Fact-diff table

| Fact | Goru-invalid output | Regenerated v2 | Independently published pin |
|---|---|---|---|
| total chips | 108 | 108 | 108 |
| region chips | 40/8/3/9/2/46 | 40/8/3/9/2/46 | 40/8/3/9/2/46 |
| S2 Citation chips | all empty | 27,28,10,11,15,20,30,30 | 27,28,10,11,15,20,30,30 |
| GAP units | GAP1/GAP3/GAP5; incorrect attribution | four: chip/token/chip/token | four: chip30/token/chip36/token |
| ledger pairing | split chip and anchor pseudo-rows | 46 paired rows, 37 unique, 0 real conflicts | 46/37/0 |
| corrupted fixture | no detected conflict; verification false | index 10 has two URLs; verification true | must detect one injected conflict |
| orphan indices | not trustworthy | 2,5,8,9,13,16,18,23,24,29,31,33 | same 12 |

Preserved invalid evidence:
- `EXPECTED_DOM_FACTS_GORU_INVALID.json`: `1924a8d5dcbeb5bd8572296c8897cd0a9e65569d42a9fa3aa04977cd550030f9`.
- `CORRUPTED_HTML_MANIFEST_GORU_INVALID.json`: `ce388944ad852fff16d060b1c23d918c1b83c18aa6b0b36268e37c84a0b98fb3`.

The Goru done marker is preserved but superseded; it is not accepted as correctness evidence.

Kun countersign: GREEN. `receipts/KUN_FIXTURE_COUNTERSIGN.md` independently reran the generator twice, reproduced the three pinned hashes and all published facts, and ends with `KUN_C1R_FIXTURE_COUNTERSIGN_GREEN_20260713T010203Z`. `receipts/KUN_GREEN_GATE.md` and `receipts/KUN_WRITE_SCOPE_AUDIT.md` are rev2 receipts; they acknowledge and correct the rev1 temp-directory scope defect, preserve the rev1-invalid receipts byte-identically, rerun the full harness, and verify clean final scope.

TORI_C1R_FIXTURE_SUPERSEDE_RECEIPT_GREEN_20260713T010203Z
