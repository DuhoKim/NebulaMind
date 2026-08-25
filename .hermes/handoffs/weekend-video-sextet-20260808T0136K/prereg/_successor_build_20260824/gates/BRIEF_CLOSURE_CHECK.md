# REFEREE BRIEF — the manifest-closure check, standalone

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

## What to review

- `../ref/successor_ref_v4.py` — `close_manifest()`, `frozen_plan_object()`,
  `frozen_planner_digest()`, `_frozen_planner()`, `parent_digest()`, and the retired
  `plan_object_bricks()`. sha256 must be
  `0b312c96db0b4551bcafd554b4bdd7124d3104cef4cc7f405eea3f849e08e21c`.
- `../../_objmanifest_20260820/build_object_manifest.py` — the FROZEN planner this binds to,
  with its pinned adapter.
- `../acquire/DOWNLOAD_QUEUE_PLAN_20260825.md` — what the download does when it fires.
- `../ref/FIXTURES_V4_20260825.out` (sha `6b14d8a69b606cbf5ddb6d0e82f856a08d6a5928227c3cba4956a1c02636e436`)
  — the `CLOSURE-*` lines are the relevant ones.

Do not read `/Users/duhokim/NebulaMindData/`.

## History you should know, because it is the failure pattern

This check has failed twice in one day, both times passing its own tests:

1. It used a REIMPLEMENTED planner. Against the real brick table that planner returned only the
   home brick for both historical objects — reproducing the exact defect it existed to prevent.
   Its fixtures passed because they ran on a synthetic brick grid the author had built.
2. The repair bound the FIXTURE to the frozen planner while `close_manifest()` itself still
   called the retired routine. The production path kept the defect; the test did not.

Both are now repaired. Neither repair has been independently reviewed.

## Questions to answer

1. Does `close_manifest()` itself derive the required bricks from the frozen planner, for every
   parent object, with no path by which a caller can supply the answer instead?
2. Run it end to end on the real geometry sidecar with the two historical objects. Does a
   complete manifest pass, and is a manifest missing either historical brick refused *by name*?
3. Can a manifest that is genuinely short still pass — via a shortened parent with a
   regenerated digest, a shortened or substituted brick universe, an altered planner
   configuration, duplicate entries, or any other route you find?
4. Is the frozen planner the right authority to bind to, and is `frozen_planner_digest()`
   actually a digest of what runs?
5. Is there any input on which the check raises an unexpected error rather than returning a
   clean pass/refuse — i.e. could it be unusable in production rather than wrong?

## Verdict

Write `CLOSURE_<YOURSEAT>.md` in this directory. Numbered findings with severity, the symbol or
quoted line at issue, why it fails, and the smallest sufficient repair. Final line exactly
`**CLEAR**` (the closure check is sound enough that a download built on it is safe) or
`**NOT CLEAR**` (with the blocking findings named). Unsupported statements under `Testimony`.
