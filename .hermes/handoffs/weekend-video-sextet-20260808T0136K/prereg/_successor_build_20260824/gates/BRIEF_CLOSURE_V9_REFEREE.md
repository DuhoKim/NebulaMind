# REFEREE BRIEF — the manifest-closure check behind a process boundary (v9)

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

You refereed v8 and returned CLEAR with five minor findings. **This round exists for one of
them.** Duho read your F3 — two written claims false against the artifact — and directed a v9 to
fix it rather than carry it into the freeze as a known-stale line.

- **F3 is fixed by making the claim true, not by narrowing it.** You offered both routes; this
  takes the one you preferred. Interpreter state (flags, full `sys.path`, the pinned add-back)
  needs no file reads, so the worker now captures it **before** the isolation gate — a refusal
  carries it too, which v8's correct early-refusal had removed. `closure_receipt()` returns that
  provenance beside the result for PASS and REFUSE alike; in v8 it dropped it in both paths,
  which is why `sys_path` occurred zero times while two sentences said every receipt had it.
  Probe **W03** asserts the provenance is present and isolated; **B04** now additionally
  requires a refusal to carry it. The two sentences are rewritten to describe what the code
  does, and both say the probes establish it rather than the prose.
- **Your F3 residual measurement is folded into the worker's own docstring.** It said "numpy
  lives in that user site directory". So do astropy — which parses the sidecar — plus erfa,
  scipy and yaml, and the CommandLineTools site-packages still precedes the add-back. The
  sidecar's bytes are pinned; its parser is not. That now sits where the mechanism is.

**NOT fixed, and named because you have twice found a finding that went unlisted:**

- **F1 and F2 from your v8 report** — the change record the brief named did not exist, and the
  brief carried v7 hashes and cited a removed probe. Both were bookkeeping in artifacts that are
  now superseded; this brief is regenerated, and `CLOSURE_REPAIR_V9_20260826.md` exists.
- **F4** — the frozen planner's three files are verified and consumed by distinct reads. Named
  in `not_covered`, not closed.
- **F5's list in full** — six `varies` strings, B06's vacuous hook, F05's basis, the worker
  timeout, ignored stdin keys, the WORKER-ERROR channel, R06's thin payload, the unused
  `require_environment()`, the three fingerprint blind spots, and the selection's missing
  producer receipt.

**Freeze status while you read this.** The mechanism is frozen at **v8** under
`FREEZE_CLOSURE_V8_20260826.md`, with your v8 verdict attached and the false claim recorded as
false. If v9 clears, the freeze moves and that record supersedes rather than rewrites; v8 stays
read-only and legible against your v8 report either way.

`CLOSURE_REPAIR_V9_20260826.md` is the change record. Read it as a claim to be checked.

## Evidence on disk

- `../ref/successor_ref_v9.py` — the subject. sha256 `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`.
- `../ref/closure_worker_v9.py` — the boundary. sha256 `28f8e1f9a8c7bd3d4cf1aabf71a7dfae5f9a1da6b92a6f09fd9c65bfc7ea5959`.
- `../ref/FIXTURES_V9_20260826.out` — fixtures, all pass. sha256 `fab32ba24cedcedf7fe601c3a8d9dbde13f57b1c9bf2e0b88963bcfebc33a8b5`.
- `closure_probe_suite_v9.py` — 34 probes. sha256 `b218aa998ac8ef97a0c4c933d73068d18ff45ce3553cb7bc80f1fe59be8c91d7`.
- `CLOSURE_PROBE_V9_RECEIPT_20260826.json` — its production-path run. **Take every hash from
  this file rather than from this brief.**
- `../acquire/DOWNLOAD_QUEUE_PLAN_20260825.md` — what the download does, and the raised ceiling.
- The earlier rounds, which you are **required to read**: `CLOSURE_RECEIPT_GPT56.md` and
  `CLOSURE_RECEIPT_CODEX.md` (the v4 round), `CLOSURE_V5_CODEX.md` (v5), and `CLOSURE_V6_KIMI.md` and
  `CLOSURE_V7_KIMI.md` and `CLOSURE_V8_KIMI.md` (v6, v7 and v8 — your own, if you are the
  KIMI seat). The
  restatements above are mine and may be self-serving; the reports are what you actually found.
  `../ref/successor_ref_v4.py` and `../ref/successor_ref_v5.py` are unchanged on disk so those
  reports stay readable against the digests they pin.

Do not read `/Users/duhokim/NebulaMindData/`.

## Commands

    python3 closure_probe_suite_v9.py --list                      # instant
    python3 closure_probe_suite_v9.py --json MY_RECEIPT.json      # ~45 min, production path
    python3 closure_probe_suite_v9.py --only B01,R08 --run-dir DIR

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
   bearing on I1–I5 that neither the 34 probes nor that list reach.
8. **The 12,117 figure.** The download's approved byte ceiling is tied to it. You confirmed it
   independently last round; confirm it again against v6, since the planner digest changed.

## Verdict

Write `CLOSURE_V9_<YOURSEAT>.md` in this directory. Numbered findings with severity, the symbol
or quoted line at issue, why it fails, and the smallest sufficient repair. Final line exactly
`**CLEAR**` (the closure check is sound enough that a download built on it is safe) or
`**NOT CLEAR**` (with the blocking findings named). Anything you assert but did not verify goes
under a `Testimony` heading.
