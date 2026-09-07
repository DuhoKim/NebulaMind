# ADOPTION PACKET — assembled deterministically, 2026-09-07 18:44 KST
Assembled by `scripts/assemble_adoption_packet.py`. It states what exists; it adopts nothing and asserts no review result it cannot read.

## The bytes
| item | path | sha256 |
|---|---|---|
| candidate | `AGREEMENT_RUN_AMENDMENT_A1_20260907.md` | `d2049709c6b6d9bec1f7120c8329e27cd4757b5d75951cba7ec2be8e3ccdcdf5` |
| decision sheet | `AGREEMENT_RUN_DECISION_SHEET_FOR_DUHO_20260907.md` | `9d6ed807d44462e649c3dce3f245e75d5bae45a94dd0a53f698f2350492a3e60` |
| implementation delta | `A1_IMPLEMENTATION_DELTA_20260907.md` | `aedfef21a4a34529ebed3dc952249584eb1fdc8fdc40b072e9f2c570ff03f33d` |
| input manifest (CORE) | `_optionA_dev/agreement_run/INPUT_MANIFEST_A1_CORE.json` | `ec2e51586d5664cded303112a02b7f1bc55fa114d3ede753fb390d70cfc67fbe` |
| runtime pins (CORE) | `_optionA_dev/agreement_run/RUNTIME_PINS_A1_CORE.json` | `0fc7024c9a4e6337ec8a3a6c0ccd76b16e5926ae19619f5f40556c844a02251c` |
| selection code | `_optionA_dev/agreement_run/select_sample.py` | `8e517aab2715e6ec814a37f0dfb517b186f2f0ed7b64f045ae6a2a34120144b5` |
| run path | `_optionA_dev/agreement_run/run_path.py` | `f5100a046ba63c9e043e7ff67ef6e01e7621fe12eaa1097ac68a0fd96b5ffeec` |
| MEDIUM producer | `_optionA_dev/agreement_run/medium_perturbation.py` | `ea46478e1947c58ebf641803eab317f20d230f7244569d07604785a8216b831f` |
| eligible ids | `_optionA_dev/agreement_run/inputs/eligible_ids_20260907.txt` | `15f34e4ef21b47a5393786a404ecc45aa07f347d548c4811fcc92932a258611d` |
| failed-set ids | `_optionA_dev/agreement_run/inputs/failed_set_ids_20260907.txt` | `f459d2fd996047ac8470ba2309062f98d9ce21c5adf5d28d609f14126bad3f5d` |

## The independent review chain
| pass | file | verdict |
|---|---|---|
| review 9 (A1 bytes) | `AGY_A1_REVIEW9_20260907.md` | VERDICT: CANDIDATE-SOUND |
| review 8 (decision sheet) | `AGY_A1_REVIEW8_20260907.md` | VERDICT: SHEET-SOUND |
| review 7 | `AGY_A1_REVIEW7_20260907.md` | VERDICT: CANDIDATE-NOT-SOUND |
| review 6 (final) | `AGY_A1_REVIEW6_20260907.md` | VERDICT: FINAL-SOUND |
| review 5 | `AGY_A1_REVIEW5_20260907.md` | VERDICT: FINAL-NOT-SOUND |
| review 4 (repair) | `AGY_A1_REVIEW4_20260907.md` | VERDICT: REPAIR-SOUND |
| review 1 (REFUSED) | `AGY_A1_REVIEW_20260907.md` | VERDICT: NOT-SOUND |
| review 2 (changed bytes) | `AGY_A1_REVIEW2_20260907.md` | VERDICT: REVIEWABLE-AND-SOUND |
| review 3 (final delta) | `AGY_A1_REVIEW3_20260907.md` | VERDICT: DELTA-NOT-SOUND |

## Status, stated narrowly
- `ready_for_input_freeze` = **True** — this means ONLY that the input-stage files are ready to freeze. It is not adoption, not permission to start a run, and not the existence of later-stage evidence.
- Nothing is adopted. Duho has made no decision. No seed, round, anchor, selection, draw or holdout has occurred.
- Approval medium: plain-language approval in Duho's dialogue with Codex, bound to the exact presented version (his recorded decision, `CODEX_DUHO_CONVERSATION_APPROVAL_RECORD_20260906.md`). He recites no digest.

## Does a review actually cover the CURRENT bytes?
- current A1 digest: `d2049709c6b6d9bec1f7120c8329e27cd4757b5d75951cba7ec2be8e3ccdcdf5`
- reviews and the digest each one actually read:
  - `AGY_A1_REVIEW9_20260907.md` — read `2c8f31828fa13de790e891bcf2da3091d55b2567cb4436beb74f519d81ebeac9` — VERDICT: CANDIDATE-SOUND  (older bytes)
  - `AGY_A1_REVIEW8_20260907.md` — read `c37ff259a19bdaecf3b02f3355aeb76bfaa09a6dcd591306fe71b376ce17494f` — VERDICT: SHEET-SOUND  (older bytes)
  - `AGY_A1_REVIEW7_20260907.md` — read `2c8f31828fa13de790e891bcf2da3091d55b2567cb4436beb74f519d81ebeac9` — VERDICT: CANDIDATE-NOT-SOUND  (older bytes)
  - `AGY_A1_REVIEW6_20260907.md` — read `f5100a046ba63c9e043e7ff67ef6e01e7621fe12eaa1097ac68a0fd96b5ffeec` — VERDICT: FINAL-SOUND  (older bytes)
  - `AGY_A1_REVIEW5_20260907.md` — read `2465294f44d0afcd8201117e4f45964b36c3e83070755629f9482863512d1546` — VERDICT: FINAL-NOT-SOUND  (older bytes)
  - `AGY_A1_REVIEW4_20260907.md` — read `53f8bef5cf24bdcf80f0658b0238639ab274ccb96f4aee3e95ab03fe2d39a906` — VERDICT: REPAIR-SOUND  (older bytes)
  - `AGY_A1_REVIEW_20260907.md` — read `a2c396be1f5e4924bbf8f49f02558a2739151a97c44e2d9034e281e34a037139` — VERDICT: NOT-SOUND  (older bytes)
  - `AGY_A1_REVIEW2_20260907.md` — read `61e253cef941de58b6be805faacc12822d0a31900ae8309f160ad976618ac069` — VERDICT: REVIEWABLE-AND-SOUND  (older bytes)
  - `AGY_A1_REVIEW3_20260907.md` — read `c0459ad1b16cfdec2333eabae4d78284f09f4c396e1781e489cbbf8cca6c7d12` — VERDICT: DELTA-NOT-SOUND  (older bytes)
- coverage per governing artefact:
  - A1 `d2049709c6b6d9bec1f7120c8329e27cd4757b5d75951cba7ec2be8e3ccdcdf5` — **no access-proved review of these bytes**
  - run path `f5100a046ba63c9e043e7ff67ef6e01e7621fe12eaa1097ac68a0fd96b5ffeec` — positively reviewed by AGY_A1_REVIEW6_20260907.md
  - decision sheet `9d6ed807d44462e649c3dce3f245e75d5bae45a94dd0a53f698f2350492a3e60` — **no access-proved review of these bytes**

## Is this presentable to Duho?
**NO — A1 has no access-proved POSITIVE review of its current bytes; decision sheet has no access-proved POSITIVE review of its current bytes.**
