# PER-CALL-SITE LEDGER — raise sites × reaching paths

**Subject:** `ref/successor_ref_v9.py`, sha256 `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148` — **read only, never written.**

**112 raise sites; 61 reachable by more than one path; 360 (site, path) rows.** The per-raise ledger collapses those 61 into one row each, which is why V50 §11 requires this unit.

**Limits:** production entry points outside this module are invisible to an in-module call graph, so a path rooting at `run_fixtures` is not evidence of fixture-only reachability; the graph is name-based, so paths are a **lower bound**; and any row whose context cannot be settled without running the study is marked `UNJUDGED`.

## The worked example — one raise, two contexts, two classifications

- **L168 `canon_f8` reached via `parent_digest` → INTEGRITY** — a non-finite reaching the digest of the PINNED parent catalogue is corrupted input, not a failed computation — the parent is a frozen artefact and §5 claims digest deviation
  - path: `parent_digest → canon_f8`
- **L168 `canon_f8` reached via `run_production_verdict` → NUMERICAL** — the same guard on the verdict path fires on a quantity the run just computed, which is a run-time numerical failure and terminates under the class rule
  - path: `run_fixtures → run_production_verdict → canon_f8`

**This is what the per-raise unit cannot express**: a single row for L168 must choose one of these, and either choice is wrong for the other path.

## Sites reachable by more than one path

| line | function | exception | paths | classification |
|---|---|---|---|---|
| 168 | `canon_f8` | `RuntimeError` | 2 | **context-dependent, resolved** |
| 395 | `frozen_planner_digest` | `ManifestClosureError` | 5 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 405 | `require_pinned_planner` | `ManifestClosureError` | 2 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 443 | `verified_bytes` | `ManifestClosureError` | 7 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 445 | `verified_bytes` | `ManifestClosureError` | 7 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 450 | `verified_bytes` | `ManifestClosureError` | 7 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 463 | `verified_bytes` | `ManifestClosureError` | 7 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 506 | `load_pinned_counts` | `ManifestClosureError` | 2 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 512 | `load_pinned_counts` | `ManifestClosureError` | 2 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 515 | `load_pinned_counts` | `ManifestClosureError` | 2 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 519 | `load_pinned_counts` | `ManifestClosureError` | 2 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 523 | `load_pinned_counts` | `ManifestClosureError` | 2 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 538 | `load_pinned_selection` | `ManifestClosureError` | 2 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 541 | `load_pinned_selection` | `ManifestClosureError` | 2 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 544 | `load_pinned_selection` | `ManifestClosureError` | 2 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 569 | `load_pinned_parent` | `ManifestClosureError` | 2 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 571 | `load_pinned_parent` | `ManifestClosureError` | 2 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 579 | `load_pinned_parent` | `ManifestClosureError` | 2 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 585 | `load_pinned_parent` | `ManifestClosureError` | 2 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 591 | `load_pinned_parent` | `ManifestClosureError` | 2 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 599 | `load_pinned_parent` | `ManifestClosureError` | 2 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 605 | `load_pinned_parent` | `ManifestClosureError` | 2 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 610 | `load_pinned_parent` | `ManifestClosureError` | 2 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 856 | `validate_count_table` | `RuntimeError` | 3 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 858 | `validate_count_table` | `RuntimeError` | 3 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 860 | `validate_count_table` | `RuntimeError` | 3 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 862 | `validate_count_table` | `RuntimeError` | 3 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 864 | `validate_count_table` | `RuntimeError` | 3 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 867 | `validate_count_table` | `RuntimeError` | 3 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 872 | `validate_count_table` | `RuntimeError` | 3 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 876 | `validate_count_table` | `RuntimeError` | 3 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 885 | `validate_count_table` | `RuntimeError` | 3 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 887 | `validate_count_table` | `RuntimeError` | 3 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 889 | `validate_count_table` | `RuntimeError` | 3 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 891 | `validate_count_table` | `RuntimeError` | 3 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 938 | `exact_min_subset` | `ValueError` | 3 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 963 | `local_pass` | `RuntimeError` | 3 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 973 | `local_pass` | `RuntimeError` | 3 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 986 | `local_pass` | `RuntimeError` | 3 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 1099 | `require_any_mask` | `RuntimeError` | 46 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 1102 | `require_any_mask` | `RuntimeError` | 46 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 1108 | `require_sealed` | `RuntimeError` | 14 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 1123 | `beta_slope` | `RuntimeError` | 15 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 1134 | `perm_sigma_exact` | `RuntimeError` | 10 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 1153 | `perm_record` | `RuntimeError` | 9 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 1206 | `inject_signs` | `RuntimeError` | 4 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 1209 | `inject_signs` | `RuntimeError` | 4 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 1331 | `_plan` | `InconclusiveByPower` | 2 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 1341 | `_plan` | `InconclusiveByPower` | 2 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 1369 | `calibration_bins` | `RuntimeError` | 3 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 1460 | `accuracy_from_handcheck` | `RuntimeError` | 2 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 1462 | `accuracy_from_handcheck` | `RuntimeError` | 2 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 1464 | `accuracy_from_handcheck` | `RuntimeError` | 2 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 1468 | `accuracy_from_handcheck` | `RuntimeError` | 2 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 1494 | `adjudicate_path` | `InconclusiveByCalibration` | 5 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 1503 | `_finite` | `RuntimeError` | 9 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 1513 | `w_profile` | `RuntimeError` | 3 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 1517 | `w_profile` | `RuntimeError` | 3 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 1537 | `sigma_ours_scalar` | `RuntimeError` | 3 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 1548 | `sigma_ours_profile` | `RuntimeError` | 3 | UNJUDGED — inherits the per-site class; context not settled without running the study |
| 1554 | `sigma_ours_profile` | `RuntimeError` | 3 | UNJUDGED — inherits the per-site class; context not settled without running the study |
