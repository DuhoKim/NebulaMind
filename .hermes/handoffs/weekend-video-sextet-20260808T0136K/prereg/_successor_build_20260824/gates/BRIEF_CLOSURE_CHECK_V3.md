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

- `../ref/successor_ref_v4.py` — `close_manifest()`, `load_pinned_geometry()`,
  `require_pinned_planner()`, `frozen_planner_digest()`, `sha256_file()`,
  `frozen_plan_object()`, and the retired `plan_object_bricks()`. sha256 must be
  `8191c42be1e8153e80480c0d110eb03c8f9c92f91895692e333af3fcbef50a21`.
- `../../_objmanifest_20260820/build_object_manifest.py` — the FROZEN planner this binds to,
  with its pinned adapter.
- `../acquire/DOWNLOAD_QUEUE_PLAN_20260825.md` — what the download does when it fires.
- `../ref/FIXTURES_V4_20260825.out` (sha `c9a3af3787ad57fa0349821d5f382b4da2bb787b714ed3d2ce8d4ac19c3fa052`)
  — the `CLOSURE-*` lines are the relevant ones.

Do not read `/Users/duhokim/NebulaMindData/`.

## History you should know, because it is the failure pattern

This check has now failed THREE times in one day, each time passing its own tests:

1. It used a REIMPLEMENTED planner. Against the real brick table that planner returned only the
   home brick for both historical objects — reproducing the exact defect it existed to prevent.
   Its fixtures passed because they ran on a synthetic brick grid the author had built.
2. The repair bound the FIXTURE to the frozen planner while `close_manifest()` itself still
   called the retired routine. The production path kept the defect; the test did not.

3. Your last round found that every "external witness" was still supplied BY THE CALLER — the
   parent digest, a receipt-shaped dict, and the geometry object — so a incomplete input list with a matching self-computed digest passed, and the planner digest did not cover all executing code.

The response to (3) changed the signature: `close_manifest(parent_csv, selection_npz,
oracle_npz, manifest_bricknames)` takes PATHS only. It loads geometry from a pinned path and
verifies the file digest; enforces a pinned full-transitive planner digest; reads selection and
parent from their own files; and proves the parent's COMPLETENESS against the count oracle
(per-brick row counts must equal the oracle's eligible counts for the selected bricks, and the
oracle total must equal the pinned release total 832,393). The intent is that a shortened
parent fails on a proof it cannot also reproduce.

Your job is to decide whether that intent is achieved. None of this has been independently
reviewed.

## Questions to answer

1. Does `close_manifest()` itself derive the required bricks from the frozen planner, for every
   parent object, with no path by which a caller can supply the answer instead?
2. Run it end to end on the real geometry sidecar with the two historical objects. Does a
   complete manifest pass, and is a manifest missing either historical brick refused *by name*?
3. Can a manifest that is genuinely short still pass? Retry your successful round-9 routes
   (incomplete input list with self-computed digest, substituted universe/geometry, altered planner
   configuration) against the new signature, and look for new ones: a doctored oracle file, a
   selection file that disagrees with the parent, symlinked or swapped paths, a parent whose
   per-brick counts match the oracle while its rows are wrong, or anything the completeness
   proof does not actually constrain.
4. Is the frozen planner the right authority to bind to, and is `frozen_planner_digest()`
   actually a digest of what runs?
5. Is there any input on which the check raises an unexpected error rather than returning a
   clean pass/refuse — i.e. could it be unusable in production rather than wrong?

## Verdict

Write `CLOSURE_<YOURSEAT>.md` in this directory. Numbered findings with severity, the symbol or
quoted line at issue, why it fails, and the smallest sufficient repair. Final line exactly
`**CLEAR**` (the closure check is sound enough that a download built on it is safe) or
`**NOT CLEAR**` (with the blocking findings named). Unsupported statements under `Testimony`.
