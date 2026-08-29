# RAISE-SITE CLASSIFICATION — every `raise` in the frozen reference, classified per site

**Subject:** `ref/successor_ref_v9.py`, sha256 `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148` (FROZEN).

**Generated 2026-08-29 by AST enumeration; the CLASS column is a human reading, not a pattern match.** V50 §11 requires the classification be recorded per site — this is that record. It exists so a seat can check the reading line by line instead of accepting a count. **The counts below are a consequence of the table, not an input to it.**

**Boundary applied** (V50 §5): a raise is a CALLER error if it tests a property of an argument as supplied; a run outcome if it tests a value computed from admissible data. INTEGRITY covers failures already claimed by a VOID antecedent. NUMERICAL-PLANNING fires before the run exists. WRAPPER re-raises another site's failure.

- **CALLER** — 20
- **INTEGRITY** — 61
- **NUMERICAL** — 17
- **NUMERICAL-PLANNING** — 3
- **TYPED-OUTCOME** — 3
- **UNREACHABLE-BY-CONSTRUCTION** — 4
- **UNREACHABLE-MEASURED-ONLY** — 1
- **WRAPPER** — 3

**Total 112 raise nodes.** Sites marked *soft* are ones I am least sure of; if they read as CALLER instead, the numerical class drops from 22 to 18.

| line | function | exception | class | | message |
|---|---|---|---|---|---|
| 64 | `require_environment` | `RuntimeError` | **INTEGRITY** |  | FROZEN ENVIRONMENT MISMATCH: {}={} want {} |
| 168 | `canon_f8` | `RuntimeError` | **WRAPPER** |  | non-finite in digest payload — FAIL |
| 215 | `receipt` | `RuntimeError` | **CALLER** |  | receipt {}: empty payload for {} — FAIL |
| 217 | `receipt` | `RuntimeError` | **CALLER** |  | receipt {}: field set mismatch; missing {}, extra {} |
| 262 | `plan_object_bricks` | `RuntimeError` | **CALLER** |  | plan_object_bricks is RETIRED — it reproduced the defect it was writte |
| 395 | `frozen_planner_digest` | `ManifestClosureError` | **INTEGRITY** |  | LIVE PLANNER CALLABLE {} is not a plain function ({}); its executing c |
| 405 | `require_pinned_planner` | `ManifestClosureError` | **INTEGRITY** |  | PLANNER DIGEST MISMATCH: {} != pinned {} — the code or configuration d |
| 443 | `verified_bytes` | `ManifestClosureError` | **INTEGRITY** |  | {} is a symlink: {} |
| 445 | `verified_bytes` | `ManifestClosureError` | **INTEGRITY** |  | {} cannot be opened: {} ({}) |
| 450 | `verified_bytes` | `ManifestClosureError` | **INTEGRITY** |  | {} is not a regular file: {} |
| 463 | `verified_bytes` | `ManifestClosureError` | **INTEGRITY** |  | {} DIGEST MISMATCH: {} != pinned {} |
| 488 | `load_pinned_geometry` | `ManifestClosureError` | **INTEGRITY** |  | SIDECAR CARDINALITY {} != pinned {} |
| 506 | `load_pinned_counts` | `ManifestClosureError` | **INTEGRITY** |  | count table columns {} != pinned {} |
| 512 | `load_pinned_counts` | `ManifestClosureError` | **INTEGRITY** |  | count table has duplicate brickid {} |
| 515 | `load_pinned_counts` | `ManifestClosureError` | **INTEGRITY** |  | count table has negative count {} for brick {} |
| 519 | `load_pinned_counts` | `ManifestClosureError` | **INTEGRITY** |  | count table has {} rows != pinned {} |
| 523 | `load_pinned_counts` | `ManifestClosureError` | **INTEGRITY** |  | count table totals {} != pinned release total {} |
| 538 | `load_pinned_selection` | `ManifestClosureError` | **INTEGRITY** |  | pinned selection is not 1-D: shape {} |
| 541 | `load_pinned_selection` | `ManifestClosureError` | **INTEGRITY** |  | pinned selection is empty or has duplicate bricks |
| 544 | `load_pinned_selection` | `ManifestClosureError` | **INTEGRITY** |  | pinned selection holds {} bricks != pinned {} |
| 569 | `load_pinned_parent` | `ManifestClosureError` | **INTEGRITY** |  | parent receipt lacks '{}' |
| 571 | `load_pinned_parent` | `ManifestClosureError` | **INTEGRITY** |  | PARENT NOT THE FETCHED ARTIFACT: producer receipt records {}, file is  |
| 579 | `load_pinned_parent` | `ManifestClosureError` | **INTEGRITY** |  | parent receipt chunk sequence is not 1..{} without repeats |
| 585 | `load_pinned_parent` | `ManifestClosureError` | **INTEGRITY** |  | parent receipt chunk {} lacks '{}' |
| 591 | `load_pinned_parent` | `ManifestClosureError` | **INTEGRITY** |  | parent receipt is internally inconsistent: totals ({} rows, {} bricks) |
| 599 | `load_pinned_parent` | `ManifestClosureError` | **INTEGRITY** |  | parent columns {} lack {} |
| 605 | `load_pinned_parent` | `ManifestClosureError` | **INTEGRITY** |  | parent row {} has out-of-range coordinates ({}, {}) |
| 610 | `load_pinned_parent` | `ManifestClosureError` | **INTEGRITY** |  | parent holds {} rows; pinned {}, receipts {} |
| 664 | `close_manifest` | `ManifestClosureError` | **INTEGRITY** |  | selection has {} brickid(s) absent from the pinned geometry universe,  |
| 671 | `close_manifest` | `ManifestClosureError` | **INTEGRITY** |  | the pinned count table has no row for {} selected brick(s), first {} |
| 694 | `close_manifest` | `ManifestClosureError` | **INTEGRITY** |  | PARENT ROWS OUTSIDE SELECTION: {} row(s) sit in bricks that are not se |
| 699 | `close_manifest` | `ManifestClosureError` | **INTEGRITY** |  | PARENT ROWS INCOHERENT: {} row(s) carry coordinates outside the brick  |
| 705 | `close_manifest` | `ManifestClosureError` | **INTEGRITY** |  | parent table is empty |
| 711 | `close_manifest` | `ManifestClosureError` | **INTEGRITY** |  | PARENT INCOMPLETE: {} of {} selected bricks have a row count differing |
| 721 | `close_manifest` | `ManifestClosureError` | **INTEGRITY** |  | parent has duplicate ls_id |
| 727 | `close_manifest` | `ManifestClosureError` | **INTEGRITY** |  | object {} plans zero bricks |
| 739 | `close_manifest` | `ManifestClosureError` | **INTEGRITY** |  | PLANNER CHANGED DURING THE PLAN: {} -> {} |
| 770 | `close_manifest` | `ManifestClosureError` | **INTEGRITY** |  | MANIFEST NOT CLOSED: {} distinct entries vs required {}; duplicated {} |
| 776 | `close_manifest` | `bare` | **WRAPPER** |  |  |
| 778 | `close_manifest` | `ManifestClosureError` | **INTEGRITY** |  | closure refused: {}: {} |
| 797 | `closure_receipt` | `ManifestClosureError` | **INTEGRITY** |  | closure worker missing: {} |
| 811 | `closure_receipt` | `ManifestClosureError` | **INTEGRITY** |  | closure worker produced no receipt (exit {}): {} |
| 818 | `closure_receipt` | `ManifestClosureError` | **INTEGRITY** |  |  |
| 820 | `closure_receipt` | `ManifestClosureError` | **INTEGRITY** |  | closure worker failed (exit {}): {} |
| 830 | `closure_receipt` | `ManifestClosureError` | **INTEGRITY** |  |  |
| 856 | `validate_count_table` | `RuntimeError` | **INTEGRITY** |  | count table: field lengths disagree or table empty — FAIL |
| 858 | `validate_count_table` | `RuntimeError` | **INTEGRITY** |  | count table: brickid must be integral — FAIL |
| 860 | `validate_count_table` | `RuntimeError` | **INTEGRITY** |  | count table: counts must be integral, not float — FAIL |
| 862 | `validate_count_table` | `RuntimeError` | **INTEGRITY** |  | count table: duplicate brickid — FAIL |
| 864 | `validate_count_table` | `RuntimeError` | **INTEGRITY** |  | count table: negative count — FAIL |
| 867 | `validate_count_table` | `RuntimeError` | **INTEGRITY** |  | count table: c outside [-1, 1] or non-finite — FAIL |
| 872 | `validate_count_table` | `RuntimeError` | **INTEGRITY** |  | universe manifest: duplicate brickid — FAIL |
| 876 | `validate_count_table` | `RuntimeError` | **INTEGRITY** |  | count table vs universe: {} missing, {} extra — FAIL |
| 885 | `validate_count_table` | `RuntimeError` | **INTEGRITY** |  | count table does not sum to the grouped total — FAIL |
| 887 | `validate_count_table` | `RuntimeError` | **INTEGRITY** |  | ungrouped total absent — the completeness proof is not optional |
| 889 | `validate_count_table` | `RuntimeError` | **INTEGRITY** |  | grouped total != ungrouped total — FAIL |
| 891 | `validate_count_table` | `RuntimeError` | **INTEGRITY** |  | ungrouped total {} != pinned release total {} — FAIL |
| 938 | `exact_min_subset` | `ValueError` | **CALLER** |  | exact mode only for <= N_EXACT candidates |
| 963 | `local_pass` | `RuntimeError` | **NUMERICAL-PLANNING** |  | no subset reaches l_plan on retained counts |
| 973 | `local_pass` | `RuntimeError` | **NUMERICAL-PLANNING** |  | greedy order never reaches l_plan on retained counts |
| 986 | `local_pass` | `RuntimeError` | **NUMERICAL-PLANNING** |  | MOVE_CAP reached — FAIL |
| 1018 | `__init__` | `RuntimeError` | **CALLER** |  | mask field lengths disagree or mask is empty |
| 1020 | `__init__` | `RuntimeError` | **INTEGRITY** |  | mask carries non-finite or /c/ > 1 |
| 1022 | `__init__` | `RuntimeError` | **CALLER** |  | mask has duplicate (brickid, objid) |
| 1027 | `__init__` | `RuntimeError` | **CALLER** |  | supplied bin labels disagree with the sealed boundaries — FAIL |
| 1032 | `__init__` | `RuntimeError` | **CALLER** |  | bin labels malformed |
| 1038 | `__init__` | `RuntimeError` | **CALLER** |  | acceptance flags malformed |
| 1040 | `__init__` | `RuntimeError` | **CALLER** |  | mask contains non-accepted rows — FAIL |
| 1050 | `__init__` | `RuntimeError` | **CALLER** |  | sign vector length {} != mask length {} — FAIL |
| 1053 | `__init__` | `RuntimeError` | **CALLER** |  | sign labels must be exactly +1 or -1 |
| 1077 | `__init__` | `RuntimeError` | **CALLER** |  | a sealed mask requires sealed calibration boundaries |
| 1099 | `require_any_mask` | `RuntimeError` | **CALLER** |  | inadmissible input: not a mask type (bare vectors, parent positions an |
| 1102 | `require_any_mask` | `RuntimeError` | **CALLER** |  | this operation requires sign labels |
| 1108 | `require_sealed` | `RuntimeError` | **CALLER** |  | PRODUCTION PATH requires a SealedMask, got {} — FAIL |
| 1123 | `beta_slope` | `RuntimeError` | **NUMERICAL** |  | zero or non-finite denominator — FAIL |
| 1134 | `perm_sigma_exact` | `RuntimeError` | **NUMERICAL** |  | degenerate c or s — FAIL |
| 1153 | `perm_record` | `RuntimeError` | **NUMERICAL** |  | non-finite permutation value — FAIL |
| 1206 | `inject_signs` | `RuntimeError` | **CALLER** |  | per-bin accuracy must have shape ({},) |
| 1209 | `inject_signs` | `RuntimeError` | **NUMERICAL** | soft | accuracy outside (0.5, 1] — FAIL |
| 1331 | `_plan` | `InconclusiveByPower` | **TYPED-OUTCOME** |  | no ledger prefix passes Stage P at planning |
| 1341 | `_plan` | `InconclusiveByPower` | **TYPED-OUTCOME** |  | final selected set fails the Stage-P re-pass ({}/{} < {}) |
| 1369 | `calibration_bins` | `RuntimeError` | **NUMERICAL** |  | degenerate calibration bins {} — FAIL |
| 1397 | `allocate_handcheck` | `RuntimeError` | **NUMERICAL** |  | stratum {} needs {} labels but only {} objects exist — FAIL |
| 1401 | `allocate_handcheck` | `RuntimeError` | **UNREACHABLE-MEASURED-ONLY** |  | inherited floors need {} labels, budget {} — FAIL |
| 1403 | `allocate_handcheck` | `RuntimeError` | **NUMERICAL** |  | budget {} exceeds available objects {} — FAIL |
| 1411 | `allocate_handcheck` | `RuntimeError` | **UNREACHABLE-BY-CONSTRUCTION** |  | floors exceed budget after the stratum lift — FAIL |
| 1435 | `allocate_handcheck` | `RuntimeError` | **UNREACHABLE-BY-CONSTRUCTION** |  | no headroom remains to place the budget — FAIL |
| 1437 | `allocate_handcheck` | `RuntimeError` | **UNREACHABLE-BY-CONSTRUCTION** |  | allocation {} != budget {} — FAIL |
| 1439 | `allocate_handcheck` | `RuntimeError` | **UNREACHABLE-BY-CONSTRUCTION** |  | allocation exceeds available objects in a cell — FAIL |
| 1442 | `allocate_handcheck` | `RuntimeError` | **NUMERICAL** |  | stratum {} below floor after apportionment — FAIL |
| 1460 | `accuracy_from_handcheck` | `RuntimeError` | **CALLER** |  | calibration inputs malformed — FAIL |
| 1462 | `accuracy_from_handcheck` | `RuntimeError` | **NUMERICAL** | soft | empty calibration bin — FAIL |
| 1464 | `accuracy_from_handcheck` | `RuntimeError` | **NUMERICAL** | soft | agreement count outside [0, n] — FAIL |
| 1468 | `accuracy_from_handcheck` | `RuntimeError` | **NUMERICAL** | soft | epsilon outside [0, 0.5) — FAIL |
| 1494 | `adjudicate_path` | `InconclusiveByCalibration` | **TYPED-OUTCOME** |  | a_lb_b min {} < {} |
| 1503 | `_finite` | `RuntimeError` | **NUMERICAL** |  | non-finite decision quantity — FAIL |
| 1513 | `w_profile` | `RuntimeError` | **NUMERICAL** |  | degenerate c — FAIL |
| 1517 | `w_profile` | `RuntimeError` | **NUMERICAL** |  | profile factor ~ 0 — FAIL |
| 1537 | `sigma_ours_scalar` | `RuntimeError` | **NUMERICAL** |  | 2a-1 <= 0 — FAIL |
| 1548 | `sigma_ours_profile` | `RuntimeError` | **NUMERICAL** |  | non-finite gradient/covariance — FAIL |
| 1554 | `sigma_ours_profile` | `RuntimeError` | **NUMERICAL** |  | negative quadratic form — FAIL |
| 1601 | `run_production_verdict` | `RuntimeError` | **INTEGRITY** |  | a BS-5f Stage-C receipt is required — FAIL |
| 1603 | `run_production_verdict` | `RuntimeError` | **CALLER** |  | BS-5f must be a canonical receipt() envelope, not a bare dict — FAIL |
| 1605 | `run_production_verdict` | `RuntimeError` | **INTEGRITY** |  | Stage-C receipt does not bind THIS mask — FAIL |
| 1620 | `run_production_verdict` | `RuntimeError` | **WRAPPER** |  | production permutation record failed: {} |
| 1641 | `require_authorization` | `RuntimeError` | **INTEGRITY** |  | authorization unreadable: {} |
| 1643 | `require_authorization` | `RuntimeError` | **INTEGRITY** |  | authorization digest mismatch: {} |
| 1649 | `require_complete_sample` | `RuntimeError` | **INTEGRITY** |  | INCOMPLETE SAMPLE: {} of {} — refusing |
| 1675 | `resolve_branch` | `RuntimeError` | **CALLER** |  | resolution_date must be YYYY-MM-DD, got {} |
| 1677 | `resolve_branch` | `RuntimeError` | **INTEGRITY** |  | the choice-point cannot close for Branch B before {}: DR11 photo-z may |
| 1681 | `resolve_branch` | `RuntimeError` | **INTEGRITY** |  | after {} the choice-point is closed on Branch B; selecting A requires  |
| 1687 | `resolve_branch` | `RuntimeError` | **INTEGRITY** |  | branch config field set differs between branches — FAIL |
