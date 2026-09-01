# Stage-P rerun build — STAGEP-V1

Built `run/stagep_rerun.py` as a read-only-v9 exact Stage-P driver. It quotes the
governing §0 and exact-per-trial clauses, sha-verifies every required input at
load, uses v9's masks, geometry, traversal, retention, reduction, injection,
permutation, encoders and `receipt()`, provides `--plan` and resumable `--full`
modes, and writes full-run candidates only to `run/classp_candidates/`.

No `--full` run was started and no candidate receipt was emitted in this build
round.

## Authenticated inputs

- `acquire/positions_selected_cut.csv`: 49,211 rows, sha256
  `a20682c114508dbdd18ede6a56c61509ea9c16784aaca7eee61f76bf97cdd372`.
- `acquire/selected_brickids_cut.txt`: 6,104 unique IDs, sha256
  `939b4ef2d2e00fb974892e835e51e512a5511bbe04a74780be15e38eb3879fd5`.
- release count table: sha256
  `4e4ec45d83f156e8daa738d81cd71a1e140d4ccbadd5343dc0bb8ed9f2479aa0`.
- universe sidecar: sha256
  `863e5ded7a4aae7abcb5df76f322f35cf89945483715ff6d1874c88f5a072d9a`.
- frozen v9: sha256
  `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`.

The full machine-readable plan result is `run/stagep_plan_20260901.json`.

## Plan and smoke result

The requested exact smoke ran end-to-end on the authenticated 49,211-object
mask. Every trial used its own v9 `perm_record()` call with 20,000 permutations;
no shared reference null was computed or consulted.

- workers: 20
- trials: 10
- successes: 10/10
- wall time: 11.9158 s
- measured wall time per trial: 1.1916 s
- extrapolated 1,000-trial battery: 1,191.6 s = 19.86 min = 0.331 h

The full route costs at least two such batteries (one planning-prefix battery
and the mandatory final-set re-pass), and more if successive prefixes must be
tested before the first pass. The estimate is a linear extrapolation of this
ten-trial concurrency sample, not a promise about contention during an
hours-long run.

## STOP-AND-BLOCKED

The authenticated 49,211-row file is already the realised post-exclusion mask.
Treating its 6,104 per-brick counts as v9 `build_plan()` raw counts makes v9
apply `retained_counts()` a second time. Under the exact frozen traversal the
maximum resulting `N_eq` is only `88,757.0269`, so no prefix reaches v9's
`NEQ_MIN = 100,000`; the dry run failed closed with `no traversal prefix reaches
N_eq minimum` before attempting a power battery.

The exact missing artifact is: **an authenticated raw pre-retention planning
table whose frozen v9 `local_pass()` output is
`acquire/selected_brickids_cut.txt`** (or an authenticated frozen-chain receipt
that binds that relationship). The release count table exists, but its frozen
selection is the pre-exclusion geometry; it does not establish that its
`local_pass()` output is the later 6,104-brick, 49,211-row realised mask.
Substituting either table would change the chain. Consequently `L_min_plan`,
`L_plan`, the BS-2o traversal receipt, BS-5p, BS-2s, and the downstream
successful `count_oracle_harness.production_build_plan()` call cannot yet be
produced honestly.

## BS-3 weights hunt

Found. A sha256 scan of 258 candidate model/weights files under the complete
NebulaMind repo, `/Users/duhokim/HermesOps`, and the weekend-video-sextet
predecessor/handoff tree matched:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/weights_frozen.pt`

Full sha256:
`83008c1cbdae511af5d30020540e1e281c62c2bd95d3cb05527fc0687bf49e6d`.

SEAT: CODEX
VERSION: STAGEP-V1
VERDICT: BLOCKED
COUNT: 10
