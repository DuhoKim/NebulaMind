# Kun Input Custody Receipt — Gate A

Packet: `gemini-dr-c1r-validator-r3-implementation-20260713T034742Z`
Phase: A-P0 only.
Decision: GREEN.

Scope honored: packet-local receipt only. No network, browser, live model call, DB, dashboard, deploy, cron, account/billing, git, or write outside this packet.

## Coordination Inputs Read

- `../gemini-dr-c1r-r3-gates-ab-coordination-20260713T034742Z/HWAO_APPROVAL_RELAY.md`
- `../gemini-dr-c1r-r3-gates-ab-coordination-20260713T034742Z/HWAO_PARALLEL_PLAN.md`
- `../gemini-dr-c1r-r3-gates-ab-coordination-20260713T034742Z/ROLE_TABLE.md`
- `APPROVAL_AND_BOUNDARIES.md`
- `../gemini-dr-c1r-manual-source-verification-20260713T034742Z/APPROVAL_AND_BOUNDARIES.md`

## Prior Packet Completion Markers

| path | exists | bytes | sha256 |
|---|---:|---:|---|
| `../gemini-dr-revised-canary-20260712T045317Z/DR_C1R_FAILED_20260712T072206Z` | true | 0 | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| `../gemini-dr-c1r-chip-validator-repair-20260713T010203Z/markers/C1R_CHIP_VALIDATOR_REPAIR_DONE_20260713T010203Z` | true | 48 | `3d45a0f3b96ed2824034cbb722e6587c6f57137fa775556e0c785294ce3a0a20` |
| `../gemini-dr-c1r-contract-r3-manual-triage-20260713T024458Z/markers/C1R_CONTRACT_R3_TRIAGE_DONE_20260713T024458Z` | true | 45 | `c9a0599712fd44cd9730ded000873bfa4ef04297d27f702278fe790a1e3116c7` |

Result: all three prior packet terminal markers exist. No immutable input mismatch observed.

## Sealed Canary Inputs

| path | exists | bytes | sha256 |
|---|---:|---:|---|
| `../gemini-dr-revised-canary-20260712T045317Z/prompt/C1r.md` | true | 9965 | `fffac44fbf6e9abe3afb1f8f34f3a9e3e7688991f319c4927459fb29ac00e1ef` |
| `../gemini-dr-revised-canary-20260712T045317Z/runs/c1r/prompt_submitted.md` | true | 9965 | `fffac44fbf6e9abe3afb1f8f34f3a9e3e7688991f319c4927459fb29ac00e1ef` |
| `../gemini-dr-revised-canary-20260712T045317Z/runs/c1r/body.md` | true | 25963 | `8a130c5a6fc1b1f5d534888d3fb20806230b8b4c7737cb00f9bfb18ad0d6bc00` |
| `../gemini-dr-revised-canary-20260712T045317Z/runs/c1r/rendered_body.html` | true | 221150 | `78ed129c47daf9300d9ed319aa1ffe95bbb0d1810a223733afaf48c4372f2bbc` |
| `../gemini-dr-revised-canary-20260712T045317Z/validator/contract_spec.json` | true | 536 | `bd6bb54607c6e5c1d2cc0c52fbfedf6cf65f7afba0815fb7273e13a7b018a896` |

Prompt identity check: `prompt/C1r.md` and `runs/c1r/prompt_submitted.md` are byte-identical (`cmp -s` exit 0).

## Repair Packet Inputs

| path | exists | bytes | sha256 |
|---|---:|---:|---|
| `../gemini-dr-c1r-chip-validator-repair-20260713T010203Z/readjudication/structured_capture_v2.json` | true | 157501 | `e26819dbc90a040ecc228639fbee3e2a68f8942fa9d26b9458aee71bbc65e3e9` |
| `../gemini-dr-c1r-chip-validator-repair-20260713T010203Z/readjudication/validator_result_v2.json` | true | 33925 | `ad4d035b291f6d64ad47f510811cc05826d822f449cf3d181974be2ce2473d52` |
| `../gemini-dr-c1r-chip-validator-repair-20260713T010203Z/readjudication/READJUDICATION_SUMMARY.json` | true | 862 | `600309c1a84721f71504577425a601501e1f739790a28621c2212540dca4c527` |
| `../gemini-dr-c1r-chip-validator-repair-20260713T010203Z/capture/structured_capture_v2.js` | true | 12570 | `11ed93ef89860009b2fc90cba0e358006b835a4cd30bf9197a5f509eeb7fc66a` |
| `../gemini-dr-c1r-chip-validator-repair-20260713T010203Z/capture/run_capture_v2.mjs` | true | 966 | `f5c259106a34f23684a7dbdcdc09c87e29946ea3589e2776e1303368996b4216` |
| `../gemini-dr-c1r-chip-validator-repair-20260713T010203Z/validator/validator_v2.py` | true | 17221 | `7f236772b1b370a7e4a233d850cd173fb18d164b5b13860c22610376a3a464b8` |
| `../gemini-dr-c1r-chip-validator-repair-20260713T010203Z/validator/run_validator_v2.py` | true | 1085 | `316fd8261a6c8edc3594ed4a978c0dcf6207dcb752a9a5da9559fc43f71a3d74` |
| `../gemini-dr-c1r-chip-validator-repair-20260713T010203Z/validator/contract_spec_v2.json` | true | 1190 | `1b10b4538162e1f786e3e36b639448cbe0d4252282d236c88495272398062338` |
| `../gemini-dr-c1r-chip-validator-repair-20260713T010203Z/receipts/TORI_PACKET_RECEIPT.md` | true | 4812 | `7546fab2e1ef46e39f9bc96eefbb0b259221a5bfca5a9a4059d202254d7dcdb5` |
| `../gemini-dr-c1r-chip-validator-repair-20260713T010203Z/receipts/KUN_GREEN_GATE.md` | true | 6050 | `d246539e055701e235be80e6278da6dd7ffb025bc7204b3d912ba1036828558c` |
| `../gemini-dr-c1r-chip-validator-repair-20260713T010203Z/receipts/KUN_WRITE_SCOPE_AUDIT.md` | true | 4426 | `9945c980b856b0370f1e6c796323ae67796defe35202b699e31fb85e2bac8e05` |
| `../gemini-dr-c1r-chip-validator-repair-20260713T010203Z/receipts/KUN_FIXTURE_COUNTERSIGN.md` | true | 3420 | `a07b7fb90f952d0452da50d9ea407a45a1471d35e74d3bf653c232b6e1e7bcdd` |

## Repair Tests

| path | exists | bytes | sha256 |
|---|---:|---:|---|
| `../gemini-dr-c1r-chip-validator-repair-20260713T010203Z/tests/test_capture_v2.mjs` | true | 5657 | `edfab84830efe5d576460427a16478859cd65925c94c7f69d9f7468b998bd8c4` |
| `../gemini-dr-c1r-chip-validator-repair-20260713T010203Z/tests/test_t0_custody.py` | true | 3754 | `19dae7df49c2b8feaeb61f0a996e224a7f648a9133c73c24ce0de03a521961b4` |
| `../gemini-dr-c1r-chip-validator-repair-20260713T010203Z/tests/test_validator_v2.py` | true | 11485 | `c976f0034eb11cfd934878de5376e5788355a57eda4d946d972b5dceaa2ad6ab` |
| `../gemini-dr-c1r-chip-validator-repair-20260713T010203Z/tests/test_integration_v2.py` | true | 5365 | `bd6794e627563bb051311da293982bcc96069310b0a4ca462366981eae00d71f` |
| `../gemini-dr-c1r-chip-validator-repair-20260713T010203Z/tests/dom_adapter.mjs` | true | 3878 | `e7ca497e9d43c32bcdd8f1dbc2274ca8ab01b3a8fa5f6ce85066f696325f9765` |
| `../gemini-dr-c1r-chip-validator-repair-20260713T010203Z/tests/run_all.sh` | true | 2023 | `b510f8d533882f4f3566611b7f2f75773147b9f53c7d75745e1d5e9ec385196b` |
| `../gemini-dr-c1r-chip-validator-repair-20260713T010203Z/tests/RED_RECEIPT_20260713T010203Z.txt` | true | 794 | `aff0f48e8a2157eb7cced59b890fd14b636b880b61828d36ae7a5170f40cb351` |
| `../gemini-dr-c1r-chip-validator-repair-20260713T010203Z/tests/GREEN_RECEIPT_20260713T010203Z.txt` | true | 957 | `9fbcd31b90c84542827ee74ad5318d4c2da88a7f61acf98f4749e75cbffee9c6` |

## Repair Fixtures

| path | exists | bytes | sha256 |
|---|---:|---:|---|
| `../gemini-dr-c1r-chip-validator-repair-20260713T010203Z/fixtures/rendered_body.html` | true | 221150 | `78ed129c47daf9300d9ed319aa1ffe95bbb0d1810a223733afaf48c4372f2bbc` |
| `../gemini-dr-c1r-chip-validator-repair-20260713T010203Z/fixtures/body.md` | true | 25963 | `8a130c5a6fc1b1f5d534888d3fb20806230b8b4c7737cb00f9bfb18ad0d6bc00` |
| `../gemini-dr-c1r-chip-validator-repair-20260713T010203Z/fixtures/prompt_submitted.md` | true | 9965 | `fffac44fbf6e9abe3afb1f8f34f3a9e3e7688991f319c4927459fb29ac00e1ef` |
| `../gemini-dr-c1r-chip-validator-repair-20260713T010203Z/fixtures/structured_capture.json` | true | 96222 | `2d10e34a46c609b713d980ded746c8bf4f1214ea7213603535cd3c7e271ec468` |
| `../gemini-dr-c1r-chip-validator-repair-20260713T010203Z/fixtures/validator_result.json` | true | 21556 | `34f525a58b1c71d237b1723fc42bfab5acfaf631e9b25175a703462e108c91f4` |
| `../gemini-dr-c1r-chip-validator-repair-20260713T010203Z/fixtures/contract_spec.json` | true | 536 | `bd6bb54607c6e5c1d2cc0c52fbfedf6cf65f7afba0815fb7273e13a7b018a896` |
| `../gemini-dr-c1r-chip-validator-repair-20260713T010203Z/fixtures/EXPECTED_DOM_FACTS_V2.json` | true | 15114 | `1b812817fe0f02b576106fcb701a98ea0de7ea3e3c681e9d6fdea90b047a21a1` |
| `../gemini-dr-c1r-chip-validator-repair-20260713T010203Z/fixtures/rendered_body_corrupted_v2.html` | true | 221150 | `05833834be7b2e54cc3a1aeafd33890e974e40f9e1ae080c95d6f2ebb84665d0` |
| `../gemini-dr-c1r-chip-validator-repair-20260713T010203Z/fixtures/CORRUPTED_HTML_MANIFEST_V2.json` | true | 572 | `76d7fb5f38064a5627381a7f8f97ed13b65172f86b380d363dee0a0afe365b55` |
| `../gemini-dr-c1r-chip-validator-repair-20260713T010203Z/fixtures/gen_expected_dom_facts.mjs` | true | 11760 | `7e0cb71c2cfce81ddb4467873b978f9956a486070a8d2eeffc42a61d8d38ac11` |
| `../gemini-dr-c1r-chip-validator-repair-20260713T010203Z/fixtures/TORI_FIXTURE_SUPERSEDE_RECEIPT.md` | true | 2759 | `44c4f3c9417a4e5d2b596c5e84c47181d905cb8c06fa0cab89b13ebc7306f93b` |

Fixture ledger summary from `EXPECTED_DOM_FACTS_V2.json`: 108 chips; 46 ledger pairs; 37 unique indices; 0 ledger mapping conflicts; 12 orphan indices; 9 duplicate rows; 46 blank short names.

## R3/Triage Inputs

| path | exists | bytes | sha256 |
|---|---:|---:|---|
| `../gemini-dr-c1r-contract-r3-manual-triage-20260713T024458Z/design/CONTRACT_R3_DRAFT.md` | true | 37457 | `0ac73b70b5590211f0352cd1ebaf3752171a384cc2489bcf91f91ca1d1b03bd9` |
| `../gemini-dr-c1r-contract-r3-manual-triage-20260713T024458Z/HWAO_R3_REVIEW.md` | true | 6626 | `00aa4000856e5c4454dc11b7c2b53db791cd00370da82188767808e60a381887` |
| `../gemini-dr-c1r-contract-r3-manual-triage-20260713T024458Z/HWAO_FINAL_RECOMMENDATION.md` | true | 7573 | `a1afa0623dea5b60966926f1f435a361cadc1efa9a207de33c2704f31357cfe9` |
| `../gemini-dr-c1r-contract-r3-manual-triage-20260713T024458Z/receipts/KUN_INPUT_CUSTODY_RECEIPT.md` | true | 4987 | `9675db17dc27bee20bc6ad9fac2d209982d5bc8102b80da1435d22a331681ae0` |
| `../gemini-dr-c1r-contract-r3-manual-triage-20260713T024458Z/receipts/KUN_TRIAGE_ARITHMETIC_RECEIPT.md` | true | 6522 | `f50234b04c6ab52ee349887b6318f6e5f311d67ee9bf55151e5e51fed63352ea` |

## Decision

Gate A P0 input custody: GREEN.

No immutable input mismatch found. Gate A may proceed within its approved boundaries after this receipt.
