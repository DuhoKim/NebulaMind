# REFEREE BRIEF — the manifest-closure check behind a process boundary (v7)

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

You refereed v6 and returned CLEAR with conditions. This round fixes five of your findings; the
ones it does NOT fix are listed after, because a repair round that quietly drops a finding is
worse than one that leaves it open.

- **F3 — the interpreter can no longer be nominated.** `closure_receipt` took a
  `python_executable` argument; you forged it with a three-line fake interpreter that ignored
  `-I` and the worker and printed a PASS, and the forged result was handed back. The parameter
  is gone. Probe B06 now calls with that keyword and requires the call itself to fail.
- **F1 — the verify hooks run.** They were registered and never invoked, so the suite's
  conformance was exactly as narrow as v5's while the brief claimed otherwise. Hooks now run on
  the live result and their verdict is folded into conformance. The receipt also carries
  `verify_hooks_declared`, `verify_hooks_ran` and `verify_hooks_all_ran`, so the next reader does
  not have to take my word that they fire.
- **F2 — `stable_sha256` reproduces across processes.** Refusal payloads carrying the
  per-process run directory are normalised now, not just messages. Two runs of the same subset
  in separate processes printed the same hash before this went out.
- **F5 — the symlink refusal is on the open.** `O_NOFOLLOW`, and the lstat that preceded it is
  gone along with the docstring claim it contradicted. Probe F05 covers it.
- **F6 — the worker validates the manifest's type.** A JSON object is refused rather than
  iterated as its keys. Probe B07 covers it.

**Not fixed, and stated rather than buried:** your F4 blind spots are real and remain. A global
resolving to a module is still folded as `<module>` (your `math.radians` demonstration), a
pure-Python helper reachable only through a class method is still not recursed into (your
`tangent_plane_offsets` demonstration), and C callables still contribute a type name only. The
suite's `not_covered` list now names all three, in your words rather than mine, and records that
the digest's cross-process stability and its blindness share a root cause. Your F8 items — the
unfrozen phase-aware refusal schema and the unused `require_environment()` — are likewise open.
The selection still has no producer receipt.

`CLOSURE_REPAIR_V7_20260826.md` is the change record. Read it as a claim to be checked.

## Evidence on disk

- `../ref/successor_ref_v7.py` — the subject. sha256 `6be341bd443d45c42eecd6b47e806f652882c971827300d51ff6fcb568069f33`.
- `../ref/closure_worker_v7.py` — the boundary. sha256 `3468b90d981c07459cc1fc040b2a9e2828d76d1d1c128bea70cdf963cd4255b5`.
- `../ref/FIXTURES_V7_20260826.out` — fixtures, all pass. sha256 `fab32ba24cedcedf7fe601c3a8d9dbde13f57b1c9bf2e0b88963bcfebc33a8b5`.
- `closure_probe_suite_v7.py` — 31 probes. sha256 `a0e8fcf5c167bfa490cf1f5e42e91b9c2b3f144d76ef9b839eca0f377cbdb718`.
- `CLOSURE_PROBE_V7_RECEIPT_20260826.json` — its production-path run. **Take every hash from
  this file rather than from this brief.**
- `../acquire/DOWNLOAD_QUEUE_PLAN_20260825.md` — what the download does, and the raised ceiling.
- The earlier rounds, which you are **required to read**: `CLOSURE_RECEIPT_GPT56.md` and
  `CLOSURE_RECEIPT_CODEX.md` (the v4 round), `CLOSURE_V5_CODEX.md` (v5), and `CLOSURE_V6_KIMI.md`
  (v6 — your own, if you are the KIMI seat). The
  restatements above are mine and may be self-serving; the reports are what you actually found.
  `../ref/successor_ref_v4.py` and `../ref/successor_ref_v5.py` are unchanged on disk so those
  reports stay readable against the digests they pin.

Do not read `/Users/duhokim/NebulaMindData/`.

## Commands

    python3 closure_probe_suite_v7.py --list                      # instant
    python3 closure_probe_suite_v7.py --json MY_RECEIPT.json      # ~45 min, production path
    python3 closure_probe_suite_v7.py --only B01,R08 --run-dir DIR

One closure that reaches planning costs ~200 s through the worker. Most probes reach planning,
so budget 45 minutes and **run it detached** — an executor that kills background jobs at 180 s
cannot complete a single closure. The run directory is per-process.

## Questions to answer

1. **Reproduction.** Does your `stable_sha256` match the receipt's for the same mode? In v6 it
   could not, by construction, and you diagnosed why. If it still does not, the diagnosis is
   wrong or incomplete and I would rather know that than have the number agree by luck.
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
6. **Do the five fixes hold, and did any of them break something?** B06, B07 and F05 are new
   probes for F3, F6 and F5; the hook counts in the receipt summary are the meta-check you asked
   for. A repair round is the easiest place to introduce a regression, so treat v7 as a fresh
   subject rather than a diff.
7. **Probe fidelity.** Several probes now carry a `verify` hook that asserts on the structured
   result, because you found probes whose `basis` claimed more than conformance checked. Do the
   hooks assert what the `basis` claims? Does any probe's metadata still under-declare what it
   changes?
8. **Coverage.** Treating the receipt's `not_covered` list as incomplete, name conditions
   bearing on I1–I5 that neither the 31 probes nor that list reach.
8. **The 12,117 figure.** The download's approved byte ceiling is tied to it. You confirmed it
   independently last round; confirm it again against v6, since the planner digest changed.

## Verdict

Write `CLOSURE_V7_<YOURSEAT>.md` in this directory. Numbered findings with severity, the symbol
or quoted line at issue, why it fails, and the smallest sufficient repair. Final line exactly
`**CLEAR**` (the closure check is sound enough that a download built on it is safe) or
`**NOT CLEAR**` (with the blocking findings named). Anything you assert but did not verify goes
under a `Testimony` heading.
