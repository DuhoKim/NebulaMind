# Stage-P build and round-2 closure report — STAGEP-V2

## Build and authenticated inputs

Round 1 built `run/stagep_rerun.py`: a read-only-v9 driver for the exact
per-trial Stage-P route, with 20,000 permutations independently recomputed for
each trial, resumable 50-result checkpoints, and candidate emission restricted
to a successful full route. The runner authenticates frozen v9
(`6a9abbbd900d...`), the 49,211-row final mask (`a20682c11450...`), the
6,104-ID closure fixture (`939b4ef2d2e0...`), the universe sidecar
(`863e5ded7a4a...`), and the full raw count table.

Round 2 corrected the planning-input seam. The runner now parses
`combined_per_brick_counts.csv` only after matching sha256
`4e4ec45d83f156e8daa738d81cd71a1e140d4ccbadd5343dc0bb8ed9f2479aa0`.
It requires exactly 270,577 unique positive-count rows and the frozen sum
832,393. Planning geometry comes from the authenticated universe brick
centres; it does not reuse the 6,104-brick post-cut mask.

Frozen `greedy_ledger()` is a literal quadratic Python loop at 270,577 rows.
The production-scale traversal therefore uses the existing vectorized
equivalent in `real/greedy_fast.py`, after 40 random-case order-agreement
fixtures against the frozen implementation. Reduction uses
`real/reduce_fast.py` after 30 random-case `local_pass()` agreement fixtures.
These are execution accelerators, not alternate selection rules.

The machine-readable result is `run/stagep_plan_20260901.json`.

## Smoke measurements

Round 1, this seat: 10/10 successes on the authenticated 49,211-object final
mask in 11.9158 s wall, or 1.1916 s/trial and 1,191.6 s (19.86 min) per
1,000-trial battery by linear extrapolation.

The coordinator's independent round-1 invocation reported 10/10 in 1.213
s/trial, approximately 20.2 min per battery.

Round 2 `--plan`: 10/10 in 12.1503 s wall, or 1.2150 s/trial and 1,215.0 s
(20.25 min) per battery by linear extrapolation. Every smoke trial used its own
v9 `perm_record()` 20,000-permutation null.

## Full-table plan and closure gate

The first retained traversal prefix satisfying `N_eq >= 100,000` occurs at
prefix 5,024. Its values are:

- `L_min_plan = 33336.25526173975`
- `L_plan = 1.2 * L_min_plan = 40003.5063140877`
- reduced `local_pass` leverage `L_ret = 40005.550078633496`
- one committed reduction move

The mandatory closure fixture **FAILED**. Canonical sorted newline-delimited
`local_pass` output has 6,446 IDs and sha256
`9f8f3cddd2e24f81ed475e51ed40da34afeee1efae3ae21d4ec0554e6a57b23c`.
The required fixture has 6,104 IDs and sha256
`939b4ef2d2e00fb974892e835e51e512a5511bbe04a74780be15e38eb3879fd5`.
All 6,104 expected IDs are present, but the route contains 342 extras; there
are zero missing IDs. The first ten extras are 5231, 6586, 6899, 7783, 8417,
8418, 8744, 9417, 9418, and 9419.

This is the stipulated STOP-AND-BLOCKED condition. No 50-trial `--full` slice
was started, no full battery was started, and no Stage-P candidate was emitted.
`--full` now recomputes and enforces the closure before starting trials.

## Candidate repairs

`run/classp_candidates/BS-4.json` now stores the experimental clauses after
the runner prefix, verbatim:

`A=-0.0408 -> INCONCLUSIVE (A_L=-0.04272)`

`A=+0.0408 at powered N -> REPRODUCED-LONGO (A_L=0.04243, p=2.23e-21, floor=0.01431)`

Its sign field now quotes the frozen sentence exactly: `The published sign is
NEGATIVE in Longo's (R-L)/(R+L) convention; our East-of-North winding maps it
to +0.0408.` A fresh v9 fixture run produced 46 PASS lines and `ALL FIXTURES
PASS`, with output sha256 `fab32ba24ced...`, reproducing both battery lines.

The deterministic candidate encoding rule for BS-4 and BS-7p is: every stored
field value is a JSON string; after JSON parsing, encode that Unicode string as
strict UTF-8, with no Unicode normalization and no terminator, then pass the
resulting byte map to `v9.receipt()`. Both candidates have exactly their v9
schema fields and round-trip deterministically under this rule. Fresh receipt
hashes are:

- BS-4: body `7c24a26d5f6c...`, envelope `edf6bc654d2c...`
- BS-7p: body `3bfabc557aa8...`, envelope `15bf924ec2aa...`

## Round-1 BS-3 weights hunt

The round-1 log contains eight mentions of the requested prefix during the
hunt. A sha256 scan of 258 candidate model/weights files across the complete
NebulaMind repository, `/Users/duhokim/HermesOps`, and the predecessor/handoff
tree found the authenticated file:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/prereg/weights_frozen.pt`

Its full sha256 is
`83008c1cbdae511af5d30020540e1e281c62c2bd95d3cb05527fc0687bf49e6d`.

SEAT: CODEX
VERSION: STAGEP-V2
VERDICT: BLOCKED
COUNT: 46
