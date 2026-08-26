# REFEREE BRIEF — the repaired manifest-closure check (v5)

You are refereeing ONE mechanism, not the whole preregistration. An image download of order
148 GB is queued behind your verdict and will not start unless this clears. Scope is
deliberately narrow; please stay inside it.

You refereed the previous version of this mechanism and returned NOT CLEAR. This round is the
repair. If you are the GPT56 seat, your F4 is one of the things repaired; if you are the CODEX
seat, your F1 note about the CSV-versus-NPZ digest is the reason the count table is read the way
it is. Both reports are on disk and you may read your own and the other seat's.

## What the mechanism is for

A preregistered study selects a set of sky bricks whose galaxies it will analyse. The images it
must download are **not** that brick list: each galaxy's cutout can require neighbouring bricks
at the edges. The closure check computes the complete required image list from the galaxies
themselves and refuses any candidate manifest that differs from it.

The predecessor study got this wrong: its manifest held 60,308 bricks, the analysis required
60,310, and nothing detected the shortfall until the pipeline stalled two galaxies short at the
end.

## The invariants

I1–I4 are as before, with I1 strengthened and I5 added because your reports said the earlier set
was necessary but incomplete.

- **I1 — independence.** No artifact that judges the manifest may be nominated by whoever
  presents the manifest. Custody must be verified for the whole count table, the selection and
  the parent's row identities and coordinates — not merely for a grand total, and not by a
  digest computed by the same process.
- **I2 — derivation.** The required brick set must be derived inside the check, by the frozen
  planner, from the parent objects, with no path by which a caller supplies the answer.
- **I3 — naming.** A manifest omitting a required brick must be refused, and the refusal must
  identify the bricks — in the structured result, not only in a truncated message.
- **I4 — fail-closed.** Malformed input must leave as one closure refusal carrying the numbers a
  receipt needs.
- **I5 — custody and atomicity** (GPT56's addition, accepted). Every answer-determining artifact
  and live callable must be fixed before the candidate is presented, and the verified bytes and
  code must be the bytes and code actually consumed.

## What changed, so you can aim at it

`close_manifest` takes ONE argument: the candidate manifest. Geometry, planner, count table,
selection and parent are each loaded from a pinned path with a pinned digest. Four further
changes trace to your numbered findings: the count table is read as the CSV its pinned digest
actually covers; the parent must satisfy both the code constant and the `output_sha256` its
fetch receipts recorded; the planner digest now includes a recursive fingerprint of the live
callables, not only source bytes; and two validators were added — selected bricks must resolve
in the pinned geometry universe, and each parent row's coordinates must lie in the brick that
row declares.

`CLOSURE_REPAIR_20260826.md` is the change record and states what is still open. Read it as a
claim to be checked, not as evidence.

## Evidence on disk

- `../ref/successor_ref_v5.py` — the subject. sha256
  `02237163b27be3a531676275e10dfd08c2ae6198bf383b2ffd0f63e9437c1171`.
- `../ref/FIXTURES_V5_20260826.out` — 42 checks, all pass. sha256
  `dfa8d92784ea98a4c72bba18bf160cdcd94e7fc0f20d215b9def539a7d6cc3af`.
- `closure_probe_suite_v5.py` — 23 probes. sha256
  `856ec71c319d0dd9dbbe784229a5ed9412a9d1aa2cf4a40c183d4eb99b9470dc`.
- `CLOSURE_PROBE_V5_RECEIPT_20260826.json` — its production-path run. **Take every hash from
  this file, not from this brief.** The previous brief quoted a stale hash and both of you
  caught it; quoting fewer numbers here is the fix.
- `CLOSURE_RECEIPT_GPT56.md`, `CLOSURE_RECEIPT_CODEX.md` — the v4 round.
- `../ref/successor_ref_v4.py` — unchanged, so your earlier reports stay readable against it.
- `../acquire/DOWNLOAD_QUEUE_PLAN_20260825.md` — what the download does, and the raised ceiling.

Do not read `/Users/duhokim/NebulaMindData/`.

## Commands

    python3 closure_probe_suite_v5.py --list                      # instant
    python3 closure_probe_suite_v5.py --json MY_RECEIPT.json      # ~25 min, production path
    python3 closure_probe_suite_v5.py --fast-geometry --only D01,N01

A closure call verifies the 366,912-brick sidecar (~47 s), parses the 270,577-row count table
and the 65,060-row parent, and plans 65,060 objects (~77 s). Probes that refuse before planning
cost ~50 s; the ones that plan cost ~185 s. **Run it detached and read the file** — the GPT56
seat's executor killed background jobs at 180 s last round, which is shorter than one closure.
The run directory is per-process, so the other seat cannot disturb yours.

## Questions to answer

1. **Reproduction.** Run the suite. Does your `stable_sha256` match the receipt's for the same
   mode? Report both numbers.
2. **Does I1 hold now?** The claim is that no artifact judging the manifest can be nominated by
   the caller. Check the claim against the code, not against the probe outcomes.
3. **Is the planner binding sufficient for I5?** The digest now fingerprints live callables'
   bytecode, names, constants and defaults. Is that the code that actually runs, for the whole
   duration of the plan? Note that the naive implementation of this was non-deterministic across
   processes and had to be rewritten; check that the version on disk is stable and that its
   stability does not come from ignoring something it should cover.
4. **The two-witness parent.** It must satisfy both a code constant and its fetch receipt. Is
   that genuinely two witnesses, or one witness counted twice?
5. **The selection is bound by a code pin only** — no producer receipt, unlike the parent. Is
   that sufficient? If not, name what would be.
6. **Probe fidelity.** For each probe, does the code under its `@probe(...)` decorator exercise
   what its metadata claims — including the redirection probes that also override a pinned
   digest constant in order to reach a validator behind it? Your F5/F6 last round were about
   metadata that failed to enumerate everything a probe changed.
7. **Coverage.** Treating the receipt's `not_covered` list as incomplete, name conditions
   bearing on I1–I5 that neither the 23 probes nor that list reach.
8. **Production usability, now measurable.** The first end-to-end closure ran: 65,060 objects,
   6,445 selected bricks, 12,117 required bricks, 185 s. Is 12,117 consistent with the
   mechanism as you read it? An independent check of that number is worth more than my assertion
   of it — the download's approved byte ceiling is tied to it.

## Verdict

Write `CLOSURE_V5_<YOURSEAT>.md` in this directory. Numbered findings with severity, the symbol
or quoted line at issue, why it fails, and the smallest sufficient repair. Final line exactly
`**CLEAR**` (the closure check is sound enough that a download built on it is safe) or
`**NOT CLEAR**` (with the blocking findings named). Anything you assert but did not verify goes
under a `Testimony` heading.
