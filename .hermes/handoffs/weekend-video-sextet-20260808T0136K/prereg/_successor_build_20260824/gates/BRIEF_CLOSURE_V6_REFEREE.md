# REFEREE BRIEF — the manifest-closure check behind a process boundary (v6)

You are refereeing ONE mechanism, not the whole preregistration. An image download of order
148 GB is queued behind your verdict and will not start unless this clears. Scope is
deliberately narrow; please stay inside it.

## What the mechanism is for

A preregistered study selects a set of sky bricks whose galaxies it will analyse. The images it
must download are **not** that brick list: each galaxy's cutout can require neighbouring bricks
at the edges. The closure check computes the complete required image list from the galaxies
themselves and refuses any candidate manifest that differs from it.

The predecessor study got this wrong: its manifest held 60,308 bricks, the analysis required
60,310, and nothing detected the shortfall until the pipeline stalled two galaxies short.

## The invariants

- **I1 — independence.** No artifact that judges the manifest may be nominated by whoever
  presents the manifest. Custody must be verified for the whole count table, the selection and
  the parent's row identities and coordinates — not merely for a grand total, and not by a
  digest computed by the same process.
- **I2 — derivation.** The required brick set must be derived inside the check, by the frozen
  planner, from the parent objects, with no path by which a caller supplies the answer.
- **I3 — naming.** A manifest omitting a required brick must be refused, and the refusal must
  identify the bricks in the structured result, not only in a truncated message.
- **I4 — fail-closed.** Malformed input must leave as one closure refusal carrying the numbers a
  receipt needs.
- **I5 — custody and atomicity.** Every answer-determining artifact and live callable must be
  fixed before the candidate is presented, and the verified bytes and code must be the bytes and
  code actually consumed.

## What changed, and what is claimed

The previous round returned NOT CLEAR with four blockers. Each is addressed; whether it is
*closed* is your ruling, not mine.

- **F1 — the boundary is now a process.** `close_manifest()` was reduced to one argument on the
  theory that a smaller signature was custody. It is not: its pins are ordinary mutable module
  globals. The production entry point is `closure_receipt()`, which runs `../ref/closure_worker.py`
  under `python3 -I` — fresh module graph, no PYTHON* environment, no user site. The worker
  verifies the subject's bytes against its own pin before importing it, and every receipt carries
  the worker's digest, the subject's digest and the full `sys.path` the worker ran with.
  **Stated residual:** numpy lives in the user site directory, so after `-I` the worker adds back
  exactly one named path. Anyone who can write there can still influence the run. That is a
  larger threat than the one you demonstrated and it is not closed.
- **F2 — the planner digest binds reachable state.** It walks `co_names` into the defining
  module's globals: functions recursed into, scalars folded in by value, classes contributing
  their methods, names that do not resolve recorded as absent. The verified callable is retained
  for the whole plan rather than re-resolved per object, and the digest is re-checked after the
  plan completes.
- **F3 — one open.** `verified_bytes()` reads each artifact once, hashes the bytes it read, and
  returns them; loaders parse that snapshot. Symlinks and non-regular files are refused on the
  descriptor. The FITS sidecar is parsed from a private byte-identical snapshot because the
  frozen planner's loader requires a path.
- **F4 — one adjudication.** Duplicates, omissions and extras are decided together after the
  required set exists. Your F5 counting bug is also fixed: `incoherent_rows` is a total, not the
  example cap.

`CLOSURE_REPAIR_V6_20260826.md` is the change record. Read it as a claim to be checked.

## Evidence on disk

- `../ref/successor_ref_v6.py` — the subject. sha256 `adb900564f285e4fa748b9d6a4eb078e1e3f78ceab3cc01c8ec65960ea7d77ca`.
- `../ref/closure_worker.py` — the boundary. sha256 `dc1775421cb9f242784762ae34d42acba1e4cbaa2f667b6cdee76a387d2e383d`.
- `../ref/FIXTURES_V6_20260826.out` — fixtures, all pass. sha256 `9ff7c82df4a25a380747ac90e1d61c39690b2eb65cffc61b4b5c5beab3f00b1c`.
- `closure_probe_suite_v6.py` — 29 probes. sha256 `5f6daaf4c8b9b57610fd6bf9ccfc1e7d5ff2a583f8d96e60e668cf050da65277`.
- `CLOSURE_PROBE_V6_RECEIPT_20260826.json` — its production-path run. **Take every hash from
  this file rather than from this brief.**
- `../acquire/DOWNLOAD_QUEUE_PLAN_20260825.md` — what the download does, and the raised ceiling.
- Earlier rounds are on disk if you want them (`CLOSURE_RECEIPT_*.md`, `CLOSURE_V5_CODEX.md`,
  `../ref/successor_ref_v4.py`, `../ref/successor_ref_v5.py`). They are **not** required
  reading: this brief is scoped to v6, and your findings are already restated above.

Do not read `/Users/duhokim/NebulaMindData/`.

## Commands

    python3 closure_probe_suite_v6.py --list                      # instant
    python3 closure_probe_suite_v6.py --json MY_RECEIPT.json      # ~45 min, production path
    python3 closure_probe_suite_v6.py --only B01,R08 --run-dir DIR

One closure that reaches planning costs ~200 s through the worker. Most probes reach planning,
so budget 45 minutes and **run it detached** — an executor that kills background jobs at 180 s
cannot complete a single closure. The run directory is per-process.

## Questions to answer

1. **Reproduction.** Does your `stable_sha256` match the receipt's for the same mode?
2. **Does the process boundary establish I1?** Probe B01 rewrites the count-table pin in the
   calling process and expects the worker to report the real digest anyway; B03 does the same
   thing without the boundary and expects the opposite. Is that a custody boundary or a longer
   path to the same trust? Is the stated site-packages residual the only one?
3. **Does the reachable fingerprint cover what it claims (I2, I5)?** It walks module globals
   from two entry callables. Name what it still cannot see, and say whether its cross-process
   stability now comes from ignoring something.
4. **Is verified-bytes custody real (I5)?** Each artifact is read once and parsed from that
   snapshot. Is there a remaining path by which consumed bytes differ from verified bytes?
5. **Is the single adjudication correct (I3, I4)?** R08 is your duplicate-plus-omission case.
   Are there other candidate shapes where one condition still masks another?
6. **Probe fidelity.** Several probes now carry a `verify` hook that asserts on the structured
   result, because you found probes whose `basis` claimed more than conformance checked. Do the
   hooks assert what the `basis` claims? Does any probe's metadata still under-declare what it
   changes?
7. **Coverage.** Treating the receipt's `not_covered` list as incomplete, name conditions
   bearing on I1–I5 that neither the 29 probes nor that list reach.
8. **The 12,117 figure.** The download's approved byte ceiling is tied to it. You confirmed it
   independently last round; confirm it again against v6, since the planner digest changed.

## Verdict

Write `CLOSURE_V6_<YOURSEAT>.md` in this directory. Numbered findings with severity, the symbol
or quoted line at issue, why it fails, and the smallest sufficient repair. Final line exactly
`**CLEAR**` (the closure check is sound enough that a download built on it is safe) or
`**NOT CLEAR**` (with the blocking findings named). Anything you assert but did not verify goes
under a `Testimony` heading.
