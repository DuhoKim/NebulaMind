# ADOPTION PACKET — assembled deterministically, 2026-09-07 17:32 KST
Assembled by `scripts/assemble_adoption_packet.py`. It states what exists; it adopts nothing and asserts no review result it cannot read.

## The bytes
| item | path | sha256 |
|---|---|---|
| candidate | `AGREEMENT_RUN_AMENDMENT_A1_20260907.md` | `c0459ad1b16cfdec2333eabae4d78284f09f4c396e1781e489cbbf8cca6c7d12` |
| decision sheet | `AGREEMENT_RUN_DECISION_SHEET_FOR_DUHO_20260907.md` | `e869ad92c97e6586ed26ccf8761cf843819d009ae3acb87f091d86440b43cd57` |
| implementation delta | `A1_IMPLEMENTATION_DELTA_20260907.md` | `aedfef21a4a34529ebed3dc952249584eb1fdc8fdc40b072e9f2c570ff03f33d` |
| input manifest (CORE) | `_optionA_dev/agreement_run/INPUT_MANIFEST_A1_CORE.json` | `fe7ca8581186fa6bad0ae22643e9537154538b0df990cf02fe208c7c8c1ceb1e` |
| runtime pins (CORE) | `_optionA_dev/agreement_run/RUNTIME_PINS_A1_CORE.json` | `95ea06f8a2f21261d0aec0f68f7593ae307782720c0ea0a3035f5b00e953919f` |
| selection code | `_optionA_dev/agreement_run/select_sample.py` | `8e517aab2715e6ec814a37f0dfb517b186f2f0ed7b64f045ae6a2a34120144b5` |
| run path | `_optionA_dev/agreement_run/run_path.py` | `53f8bef5cf24bdcf80f0658b0238639ab274ccb96f4aee3e95ab03fe2d39a906` |
| MEDIUM producer | `_optionA_dev/agreement_run/medium_perturbation.py` | `ea46478e1947c58ebf641803eab317f20d230f7244569d07604785a8216b831f` |
| eligible ids | `_optionA_dev/agreement_run/inputs/eligible_ids_20260907.txt` | `15f34e4ef21b47a5393786a404ecc45aa07f347d548c4811fcc92932a258611d` |
| failed-set ids | `_optionA_dev/agreement_run/inputs/failed_set_ids_20260907.txt` | `f459d2fd996047ac8470ba2309062f98d9ce21c5adf5d28d609f14126bad3f5d` |

## The independent review chain
| pass | file | verdict |
|---|---|---|
| review 1 (REFUSED) | `AGY_A1_REVIEW_20260907.md` | VERDICT: NOT-SOUND |
| review 2 (changed bytes) | `AGY_A1_REVIEW2_20260907.md` | VERDICT: REVIEWABLE-AND-SOUND |
| review 3 (final delta) | `AGY_A1_REVIEW3_20260907.md` | VERDICT: DELTA-NOT-SOUND |

## Status, stated narrowly
- `ready_for_input_freeze` = **False** — this means ONLY that the input-stage files are ready to freeze. It is not adoption, not permission to start a run, and not the existence of later-stage evidence.
- Nothing is adopted. Duho has made no decision. No seed, round, anchor, selection, draw or holdout has occurred.
- Approval medium: plain-language approval in Duho's dialogue with Codex, bound to the exact presented version (his recorded decision, `CODEX_DUHO_CONVERSATION_APPROVAL_RECORD_20260906.md`). He recites no digest.

## Is this presentable to Duho?
**NO — input readiness is not TRUE.**
