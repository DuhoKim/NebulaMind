# Receipt repair — the cited executable behind the Phase-1 cutoff table is now in the record

**Tori, 2026-09-04 11:41 KST.** Non-decision integrity repair, found on a currency sweep while the K3-step-2
annotation ruling sits with Duho.

## The defect

`CUTOFF_THEORY_PHASE1_codex_RESULT.md` is a **tracked** record. At L103–107 it calls `cutoff_phase1_camb.py`
"the complete executable", prints `python3 cutoff_phase1_camb.py` as the instruction to reproduce it, and then gives a
four-row numerical table. **The script itself was never committed.** Anyone who cloned the repository got the record,
the instruction and the table, but not the thing that produces them — a cited receipt that was not in the record. This
is the mirror of the defect the 2026-09-04 support audit repaired for K2 route 2 (a cited "executable" that was a stub):
there the file was wrong, here the file was absent.

## The repair

`cutoff_phase1_camb.py` (80 lines, sha256 `edc3a1ec8e384d47a91f6585701ac1e7e88bbc92c94c6815dfe8a9cde6d4ac3f`) is
committed unchanged, together with its executed output `cutoff_phase1_camb.out`.

## Verified, not assumed

The script was re-executed today from a clean shell and reproduces the record's table to the printed precision:

| row | record L114–117 | today's re-run | match |
|---|---|---|---|
| standard ΛCDM | `34,940 / 1,071.1 / 507.2` | `34940.14 / 1071.093 / 507.190` | yes |
| R1 literal log truncation | `22,327 / 897.4 / 570.2` | `22327.32 / 897.356 / 570.207` | yes |
| R2 surrogate, `k_c = π/L` | `14,002 / 710.3 / 448.9` | `14002.38 / 710.343 / 448.888` | yes |
| R2 surrogate, `k_c = 4.493409/L` | `6,230 / 499.4 / 286.9` | `6229.94 / 499.390 / 286.873` | yes |

All four rows, all three columns. The record's numbers are the script's numbers.

## Scope

Nothing in `CUTOFF_THEORY_PHASE1_codex_RESULT.md` changed; no tier, warrant token, standing or stamp moved. The other
untracked working scripts in this directory (`cutoff_compute.py`, `cutoff_retarded*.py`, `cutoff_variance.py`,
`col_check.py`, `gamma.py`, `test_fryer*.py`, and the rest) were checked against every filed record in the lane and are
cited by **none**; they remain working scratch, preserved on disk under ARCHIVE-NEVER-DELETE and deliberately not
promoted into the record.

CUTOFF_PHASE1_RECEIPT_COMPLETE
