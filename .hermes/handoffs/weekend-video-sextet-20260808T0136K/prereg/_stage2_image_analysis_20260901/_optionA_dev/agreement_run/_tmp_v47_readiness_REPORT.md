# V47 readiness repair — author report

Authoring repair completed; INPUT readiness is **FALSE** because `RUNTIME_REPRESENTATION` remains unresolved. This report makes no review verdict or runtime-representation completion claim.

Governing sources: `AGY_A1_REVIEW3_20260907.md`, FATALs 3 and 4, and the owner's `A1_REVIEW3_OUTCOME_20260907.md`. OBLIGATION means current preparation work due before INPUT freeze. COMPLETE means every declared member is present, regardless of resolution.

The changes are confined to `_optionA_dev/agreement_run/`: `run_path.py`, the CORE manifest, runtime pins documentation, manifest scope note, the existing run-path synthetic fixture, new `test_readiness.py`, and V47 evidence artifacts. The governing files, A1 prose and retained inventories are unchanged. No real pixels or labels were accessed; no real study stage or network action was performed. The existing synthetic suites retain their stage/selection fixtures. No excluded framework, draft, git operation or review sandbox was used.

## Declared set and predicate

`run_path.OBLIGATION_REGISTRY` declares ids and meanings independently of the manifest's rows or counts:

| Id | Current preparation meaning | Manifest resolved |
|---|---|---|
| CORE_CONSUMER_RECONCILIATION | Bind the run-path consumer to CORE and bounded runtime pins while preserving gates. | true |
| MEDIUM_CURRENT_PREPARATION | Implement and bind the scientific MEDIUM perturbation producer. | true |
| RUNTIME_REPRESENTATION | Resolve A1's import-artifact and OS shared-cache representation, including reproducible byte bindings. Compact pins do not waive this work. | false |

`input_readiness` retains the existing file, alias, required-code/input, configuration, cache and placeholder checks. It additionally checks that every declared id appears exactly once, that no undeclared id appears, that every present obligation is resolved, and that A1's mapped declarations/statuses agree. Missing entries report `MISSING-OBLIGATION: <id>`; duplicates and undeclared ids also fail by name. `_core` requires both the computed predicate and the stored TRUE flag, retaining the exact recorded-check comparison. Flags and counts do not determine the computed predicate.

The current list is complete and agrees with A1. Rehashing all 29 current CORE files succeeds. The five later-stage groups keep their existing timing. The added physical file is A1 itself, now read solely for the obligation cross-check. The resulting checks are:

| Predicate | Result |
|---|---|
| all_real_entries_rehashed_and_matched | true |
| input_due_placeholders_resolved | true |
| declared_obligation_set_complete | true |
| current_preparation_obligations_resolved | false |
| a1_manifest_obligations_agree | true |
| ready_for_input_freeze (AND of checks) | **false** |

The manifest's flag/checks were assigned from `input_readiness(c)`, not hand-set. Its unresolved count is 1. The recorded runtime obligation is the sole false readiness operand.

## A1 cross-check and its boundary

The gate reads the actual `AGREEMENT_RUN_AMENDMENT_A1_20260907.md`, pinned in CORE and independently bound in code to the reviewed source SHA-256 `c0459ad1b16cfdec2333eabae4d78284f09f4c396e1781e489cbbf8cca6c7d12`. Its mapped prose reports the CORE consumer and MEDIUM producer implemented, and runtime representation unfinished. The code compares each id/status against the manifest. Marking runtime resolved produces `A1-OBLIGATION-MISMATCH: RUNTIME_REPRESENTATION; A1 resolved=False, manifest resolved=True`.

This is a bounded interpretation of the reviewed source, not a general natural-language completeness parser. ANY unfamiliar A1 revision fails `A1-OBLIGATION-SOURCE-CHANGED`, including a newly added obligation elsewhere or a removed declaration, even if its CORE digest is repinned. A revised A1 requires an explicit reviewed mapping/source-digest update. This prevents the excerpts themselves becoming an unchecked partial list. A1 was outside the write scope; its historical TRUE statement and old CORE/runtime digest statements remain stale and are identified as such in the updated scope note. They are not current readiness operands. The cross-check covers current preparation obligations, not historical bindings or later-stage groups.

## TOCTOU

`run_path.py`, `RUNTIME_PINS_A1_CORE.json` and `MANIFEST_SCOPE_NOTE_20260907.md` now plainly state that extension modules are hashed and later imported with **no lock between**. Pins evidence what was on disk at check time, not what the loader used or what was already loaded. Both named NumPy extension digests are reverified immediately before the imports that can open them. A synthetic mutation after initial hashing now fails at this recheck. The interval is narrowed, not eliminated; the runtime-representation obligation remains unresolved.

## Tests and evidence

The specified interpreter, exact lane BLS PYTHONPATH and `PYTHONDONTWRITEBYTECODE=1` were used throughout.

- `_tmp_v47_failfirst.txt`: captured BEFORE production edits, against current `run_path.py` SHA-256 `0b47f76bb35bc619ed49b1705506912637b2295c2c8f844a6376e0795766cc07` and manifest SHA-256 `cdac63a5c32f35e43c897a9fd256363a648e4254d0ac879e909a75afe8d50bc0`. All 12 FAIL-FIRST methods failed as assertions, including deletion of each declared id, empty/duplicate/extra lists, A1 divergence and the pre-import mutation. Both positive controls passed. Exit 1 was the required reproduction.
- `_tmp_v47_baseline.txt`: the corrected complete pre-change run passed all 122 existing tests (32 CORE consumer, 42 run path, 32 MEDIUM, 16 selector). Initial discovery/local-import invocation errors are retained transparently before the successful corrected run; they were not product failures.
- `_tmp_v47_after.txt`: all **136 tests passed**, comprising those same 122 tests and 14 readiness tests. Code compared baseline and after method identities/statuses; every previous passing outcome is preserved. Actual metadata-only gate probes additionally show that deleting each current obligation fails by its id, including deletion of the unresolved runtime row. The actual current gate refuses runtime preparation; falsely resolving it is rejected as A1 divergence.
- `_tmp_v47_kit.txt`: PASS for the 14 new methods (12 FAIL-FIRST, 2 POSITIVE-REGRESSION), each with exactly one outcome assertion and the proper observed predecessor status. PASS also for the 42 migrated-fixture run-path methods against the V47 baseline, 32 unchanged consumer methods against their applicable V46 predecessor log, and 32 unchanged MEDIUM methods against the V47 baseline. The 16 selector methods and their historical labels remain unchanged; their executable outcomes pass. No new selector kit claim is made.
- `_tmp_v47_validation_summary.json`: mechanically verified 122-to-136 preservation and the exact five-file existing-change set. A1, governing sources and retained inventory digests are unchanged.

The existing synthetic ready fixture now includes all three obligations and a separately bound synthetic A1 with resolved runtime work so existing tests reach their intended checks. No existing outcome assertion was changed. The new test methods retain their fail-first bodies; after that capture, their setup path comparison was canonicalized to account for macOS `/var` versus `/private/var` when the shared fixture acquired its A1 row. `_tmp_v47_initial_after.txt` retains that intermediate fixture failure; `_tmp_v47_focused_after.txt` records the subsequent 14/14 pass.

Acceptance: deleting any of the three declared obligation entries fails by name; current readiness computes FALSE solely from unresolved runtime preparation; A1/manifest divergence is detected by code; all 122 previously passing tests still pass. The requested repair is complete. Resolving runtime representation remains future authoring work under its recorded obligation.

## After-digests (SHA-256)

This report was written last, after all verification and the digest ledger. The report cannot contain its own full-file digest; all repaired source/document/test files and V47 evidence artifacts, including the digest ledger, are bound below.

| File in `_optionA_dev/agreement_run/` | Bytes | SHA-256 |
|---|---:|---|
| `INPUT_MANIFEST_A1_CORE.json` | 35797 | `fe7ca8581186fa6bad0ae22643e9537154538b0df990cf02fe208c7c8c1ceb1e` |
| `MANIFEST_SCOPE_NOTE_20260907.md` | 6821 | `bdd30f69fea52163c44fde52dcfabf776486d18daabd71f44a7a547db1fb17cf` |
| `RUNTIME_PINS_A1_CORE.json` | 7665 | `95ea06f8a2f21261d0aec0f68f7593ae307782720c0ea0a3035f5b00e953919f` |
| `_tmp_v47_after.txt` | 24225 | `fd814eb0337a033e044520a66e5697bcd24ab560f865a35e8368abef301d8e3e` |
| `_tmp_v47_after_digests.json` | 1907 | `1ff4d7ec8a160c363d3c4fab8e4e64387355de1babdad33aef9d4d8c9513345f` |
| `_tmp_v47_baseline.txt` | 41292 | `26493f09855d8cf9bce3908a6da170b966738ec5951a3aa9dbe601f7901c81c5` |
| `_tmp_v47_before_digests.json` | 4239 | `e4206b5f3ec848a2b1d3df0e2dcb072621fea196690f4400316dde96dcc9200c` |
| `_tmp_v47_failfirst.txt` | 11809 | `f65beb18ef1d99eb504448e0003a77ba08c3a264d2de6eaf85fc87970657205d` |
| `_tmp_v47_focused_after.txt` | 2549 | `acb11399fe8c277d35a8d86f79f44e5f19c880bffd3159da3a460d67cd690c1e` |
| `_tmp_v47_initial_after.txt` | 17234 | `ac64f8c13e7c03c5751363ddab08e5f1c6b554bea4e728570838f144742b9b6b` |
| `_tmp_v47_kit.txt` | 2162 | `412b4ef14ad0ecc7b9ca98948b7274f5e950621a4f53b516476b51f2f9c89384` |
| `_tmp_v47_validation_summary.json` | 759 | `1bf9017836485714a47698f8796c348f6d28523c8f164792b4bf7d6802351301` |
| `run_path.py` | 47123 | `53f8bef5cf24bdcf80f0658b0238639ab274ccb96f4aee3e95ab03fe2d39a906` |
| `test_readiness.py` | 8444 | `50531a79d94305a00a706e97da114a3bb66512b2745fcf4f16e868de950d2ca1` |
| `test_run_path.py` | 25859 | `0345ec6a1dc5e2c74ffcf440cc5005cfebc79db2118ebfe5eaf44b34ef43a66e` |

Written at 2026-09-07T08:31:37.384935+00:00.

READINESS-REPAIR-COMPLETE
