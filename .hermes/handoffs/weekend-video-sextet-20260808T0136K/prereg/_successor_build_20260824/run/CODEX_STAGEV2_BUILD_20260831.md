# CODEX staging-v2 build receipt v4 — 2026-09-01

Go-live attempt 2's public-key divergence is repaired in
`bs2k_stage_v2.py`. All work and executions stayed under `run/`; `--go-live`
was not run.

## V4 repair

`provision_key` now treats each key's shares and hash-bearing metadata as the
single source of truth. On every staging run it recombines the private bytes,
refuses `REFUSED-CORRUPT-SHARE` unless their full SHA-256 and length match the
metadata, writes the recombined key to a temporary private file, derives the
public half with `ssh-keygen -y`, atomically replaces the escrow `.pub`, and
securely removes the temporary private file.

The public-key coherence fixture compares the complete derived string against
both the complete on-disk `.pub` string and the complete mediator-bound string
for both machine keys. The healing fixture writes junk to the enumerator
`.pub`, performs another staging run, and proves exact coherence is restored.
No prefix slices are used.

## Green runs

- `python3 bs2k_stage_v2.py`: 19/19 green.
- `python3 boundary_test.py`: 16/16 green.
- `python3 -m py_compile bs2k_stage_v2.py boundary_test.py`: green.
- Independent exact three-way audit for both public keys: green.
- Recombined temporary-file absence check: green.
- `git diff --check`: green.

## Final digests

- `bs2k_stage_v2.py`: `b45929a9424ac3539a3b694ee84bf405b6f4676ca1bdba26b445ff28335910d6`
- `STAGED_manifest.json`: `c6bbdf503555a468f699cb90f9268393aff5c82952486aa8a21bf76feb2d9681`
- `STAGED_seal_state.json`: `80122c976d20185c4121095b2a53b5e09219cf21ede6423a36a6beec91442200`
- `mediator/mediator.json`: `d81b9b62329e00605d2ca897b59d2e5e7df1ef6b244466088f0e29275ba45fd5`

SEAT: CODEX
VERSION: STAGEV2-V4
VERDICT: BUILT-GREEN
COUNT: 19
