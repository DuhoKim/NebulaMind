# REFEREE BRIEF — the manifest-closure check: does the independence invariant hold?

You are refereeing ONE mechanism, not the whole preregistration. A ~77 GB image download is
queued behind your verdict and will not start unless this clears. Scope is deliberately narrow;
please stay inside it.

## What the mechanism is for

A preregistered study selects a set of sky bricks whose galaxies it will analyse. The images it
must download are **not** that brick list: each galaxy's cutout can require neighbouring bricks
at the edges. The closure check computes the complete required image list from the galaxies
themselves and refuses any candidate manifest that differs from it.

This exists because the predecessor study got it wrong: its manifest held 60,308 bricks, the
analysis actually required 60,310, and nothing detected the shortfall until the pipeline stalled
two galaxies short at the very end. The two missing bricks were `3471m885` (needed by ls_id
10997315463551936, dec −88.59) and `2857m870` (needed by ls_id 10995116744378804, dec −87.13).

## The invariants you are asked to rule on

These are the properties the mechanism must have. Round 9 established the first one; it is the
substance of this round.

- **I1 — independence.** The check must not accept a manifest whose completeness rests on a
  digest computed by the same process that produced the list. Completeness must be established
  against the independent count oracle, whose total is pinned to the release. An artifact the
  check merely *reads at a path it was handed* is not independent of the caller, however the
  digest over it is computed.
- **I2 — derivation.** The required brick set must be derived inside the check, by the frozen
  planner, from the parent objects — with no path by which a caller supplies the answer.
- **I3 — naming.** A manifest omitting a required brick must be refused, and the refusal must
  name the brick.
- **I4 — fail-closed.** Malformed input must leave as one closure refusal carrying the numbers a
  receipt needs, never as an unrelated exception type.

## Evidence already on disk

`closure_probe_suite.py` (22 probes) exercises the production entry point
`close_manifest(parent_csv, selection_npz, oracle_npz, manifest_bricknames)` and records, per
probe, the input's declared expectation and the outcome. Its run is
`CLOSURE_PROBE_RECEIPT_20260825.json`.

Result as shipped: **18 of 22 conforming. Probes C01, C02, C03 and C04 are non-conforming** —
inputs the suite expected to be refused and the check accepted. I3 and I4 are satisfied by the
receipt's R- and E-probes. The four failures all sit against I1.

You are not asked to derive or construct any input. The probes exist; your task is to judge
whether they test what they claim, whether the invariants above are the right ones, and whether
I1 holds.

## What to review

- `closure_probe_suite.py` — read it as source, not just as output. Each probe declares what it
  varies, what outcome it expects, and the `basis` for that expectation.
- `CLOSURE_PROBE_RECEIPT_20260825.json` — `stable` must reproduce; `volatile` (timings, paths)
  must not.
- `../ref/successor_ref_v4.py` — the subject: `close_manifest()`, `load_pinned_geometry()`,
  `require_pinned_planner()`, `frozen_planner_digest()`, `sha256_file()`, `frozen_plan_object()`,
  and the retired `plan_object_bricks()`. sha256 must be
  `8191c42be1e8153e80480c0d110eb03c8f9c92f91895692e333af3fcbef50a21`.
- `../../_objmanifest_20260820/build_object_manifest.py` — the FROZEN planner it binds to.
- `../acquire/DOWNLOAD_QUEUE_PLAN_20260825.md` — what the download does when it fires.

Do not read `/Users/duhokim/NebulaMindData/`.

## Commands

From this directory:

    python3 closure_probe_suite.py --list                    # instant: the probe table
    python3 closure_probe_suite.py --fast-geometry           # ~50 s, reproducibility check
    python3 closure_probe_suite.py --json MY_RECEIPT.json    # ~17 min, the production path

The check re-reads and re-verifies the 366,912-brick geometry sidecar on every call (~47 s), so
a full run is slow; run it detached and read the file. `--fast-geometry` verifies the sidecar
once and reuses it — faster, but not the production path, and the receipt records which mode
produced it. Two `--fast-geometry` runs printed the same `stable_sha256`
(`3abf01ae66a6e7ed2a165099353c0762b1676e6eed4c8c138a607e81690d40c0`); the shipped default run's
hash is in the receipt. The two differ only because the mode is part of the hashed block.

The suite writes only inside `_tmp_closure_probe_run_<pid>/` in this directory. The run
directory is per-process, so the other seat running at the same time cannot disturb yours;
`--run-dir DIR` overrides it. `--only C01,C04` runs a subset; shared inputs are built in setup,
so a subset run gives the same inputs as a full one.

## Questions to answer

1. **Reproduction.** Does your run's `stable_sha256` match the receipt's for the same mode?
2. **Probe fidelity.** For each probe, does the code under its `@probe(...)` decorator exercise
   what its metadata claims? A probe that does something other than its label says would make a
   conforming line meaningless — twice in this lane a test has passed on inputs built to suit
   it. Name every probe whose metadata and code disagree.
3. **Are these the right invariants?** I1–I4 above are my statement of what the mechanism owes.
   Say where that statement is wrong, too weak, or incomplete.
4. **Does I1 hold?** Take the four non-conforming results as reported. For each: is it a real
   failure of I1, or an artefact of how the probe was set up? For each real one, give the
   smallest sufficient repair, naming the symbol or line it changes. C04 carries an explicit
   `dispute` note arguing it may fall outside this function's contract; rule on that one.
5. **Coverage.** The receipt's `not_covered` list is the suite author's own statement of what is
   untested. Treating it as incomplete, name conditions bearing on I1–I4 that neither the 22
   probes nor that list reach. A named gap becomes the next round's work.
6. **Production usability.** One closure call costs ~47 s of sidecar verification, and the real
   run is one call over 65,060 objects and 6,445 selected bricks. Is there any input on which the
   check raises an unexpected error rather than returning a clean pass/refuse, or any reason it
   would be unusable at that scale rather than wrong?

## Verdict

Write `CLOSURE_RECEIPT_<YOURSEAT>.md` in this directory. Numbered findings with severity, the
symbol or quoted line at issue, why it fails, and the smallest sufficient repair. Final line
exactly `**CLEAR**` (the closure check is sound enough that a download built on it is safe) or
`**NOT CLEAR**` (with the blocking findings named). Put anything you assert but did not verify
under a `Testimony` heading.
