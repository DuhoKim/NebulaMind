# REFEREE BRIEF — the manifest-closure check, reviewed from a receipt

You are refereeing ONE mechanism, not the whole preregistration. A ~77 GB image download is
queued behind your verdict and will not start unless this clears. Scope is deliberately narrow;
please stay inside it.

## What the mechanism is for

A preregistered study selects a set of sky bricks whose galaxies it will analyse. The images it
must download are **not** that brick list: each galaxy's cutout can require neighbouring bricks
at the edges. The closure check computes the complete required image list from the galaxies
themselves, and refuses any candidate manifest that differs from it.

This exists because the predecessor study got it wrong: its manifest held 60,308 bricks, the
analysis actually required 60,310, and nothing detected the shortfall until the pipeline stalled
two galaxies short at the very end. The two missing bricks were `3471m885` (needed by ls_id
10997315463551936, dec −88.59) and `2857m870` (needed by ls_id 10995116744378804, dec −87.13).

## What is different about this round

Earlier rounds asked you to construct the check's input files yourself. That is no longer your
job. A test suite in this directory — `closure_probe_suite.py`, 22 probes — constructs each
input, runs it through the production entry point, and records what happened. Its run is in
`CLOSURE_PROBE_RECEIPT_20260825.json`.

**Your job is to check the probes and rule on the results, not to invent inputs.** Concretely:
whether each probe builds what its label says, whether its declared expectation is the right
one, what the suite does not cover, and what the failures mean.

The run as shipped: **18 of 22 probes conforming; C01, C02, C03 and C04 non-conforming** —
each of those four is an input the suite expected to be refused and which the check accepted.
Those four are the substance of this round. The receipt states this itself; it is not hidden.

## What to review

- `closure_probe_suite.py` — the suite. Read it as source, not just as output.
- `CLOSURE_PROBE_RECEIPT_20260825.json` — its run. `stable` is the part that must reproduce;
  `volatile` holds timings and absolute paths and must not.
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
the full run is slow; run it detached and read the file. `--fast-geometry` verifies the sidecar
once and reuses it — faster, but not the production path, and the receipt records which mode
produced it. Two `--fast-geometry` runs on this machine printed the same `stable_sha256`
(`3abf01ae66a6e7ed2a165099353c0762b1676e6eed4c8c138a607e81690d40c0`); the shipped default run
printed `f1cd1004de806c6bb6f1261e4177680bc7fdc9f28de056ca5ca1dc5a26281961` in 16 min 29 s. The
two differ only because the mode is part of the hashed block; the probe outcomes are identical
under both.

The suite writes only inside `_tmp_closure_probe_run_<pid>/` in this directory and modifies
nothing else. The run directory is per-process, so the other seat running the suite at the same
time cannot disturb yours; `--run-dir DIR` overrides it. `--only C01,C04` runs a subset; shared
inputs are built in setup, so a subset run gives the same inputs as a full one.

## Questions to answer

1. **Reproduction.** Run the suite. Does your `stable_sha256` match the receipt's for the same
   mode? If not, what differs?
2. **Probe fidelity.** For each probe, does the code under its `@probe(...)` decorator actually
   construct the input the label and `varies` field describe? A probe that quietly builds
   something else would make a conforming line meaningless — this is the failure mode that has
   already occurred twice in this lane, where a test passed on inputs the author had built to
   suit it. Name every probe whose label and code disagree.
3. **Expectation audit.** Each probe declares a `basis` — where its expected outcome comes from.
   Say which expectations you think are wrong and why. C04 carries an explicit `dispute` note
   arguing it may be outside `close_manifest`'s contract; rule on that one specifically.
4. **The four non-conforming results.** For C01, C02, C03 and C04: is each a real defect of
   `close_manifest`, or an artefact of how the probe was set up? For each real one, give the
   smallest sufficient repair, naming the symbol or line it changes.
5. **Coverage.** The receipt's `not_covered` list is the suite author's own statement of what
   is untested. Treating that list as incomplete, name conditions in `close_manifest`'s contract
   — its four stated bindings, its refusal paths, its inputs' types and ranges — that neither
   the 22 probes nor that list reach. A named gap here becomes the next round's work.
6. **Production usability.** One closure call costs ~47 s of sidecar verification, and the real
   run is one call over 65,060 objects and 6,445 selected bricks. Is there any input on which
   the check raises an unexpected error rather than returning a clean pass/refuse, or any reason
   it would be unusable at that scale rather than wrong?

## Verdict

Write `CLOSURE_RECEIPT_<YOURSEAT>.md` in this directory. Numbered findings with severity, the
symbol or quoted line at issue, why it fails, and the smallest sufficient repair. Final line
exactly `**CLEAR**` (the closure check is sound enough that a download built on it is safe) or
`**NOT CLEAR**` (with the blocking findings named). Put anything you assert but did not verify
under a `Testimony` heading.
