# The v9 repair — one finding, and the record I twice failed to write

2026-08-26, Hwao. Against `CLOSURE_V9_KIMI.md` (**CLEAR**, five minor findings).

## Why this file exists at all

KIMI's v8 F1 and v9 F1 are the same finding, made twice: **the brief named a change record that
did not exist.** I wrote "`CLOSURE_REPAIR_V8_20260826.md` is the change record" into the v8
brief and never created the file, then repeated it verbatim for v9. A referee asked to check a
claim against a document was twice sent to a path with nothing at it.

That is not a mechanism defect and it is worse than most of the mechanism defects found today,
because it is the same failure the whole lane is built against: a document asserting something
about an artifact that isn't there. This file is the repair, written late.

## What v9 changed — one thing

**KIMI-V8 F3.** Two written claims said every receipt records the worker's `sys.path`. After
v8's early-refusal fix, no receipt did: the worker refused before provenance was built, and
`closure_receipt()` dropped provenance for PASS and REFUSE alike.

Fixed by making the claim true, which was that seat's preferred route over narrowing it:

- interpreter state (flags, full `sys.path`, the pinned add-back) is captured **before** the
  isolation gate, since none of it needs a file read;
- the isolation refusal carries it;
- `closure_receipt()` returns `worker_provenance` beside the result for PASS and REFUSE alike;
- **W03** asserts it on a real closure, **B04** asserts it on a refusal.

Measured, not asserted: W03 reports 4 `sys.path` entries with `isolated=True` and the add-back
named; B04 reports 7 entries in an un-isolated refusal. 34/34 conforming, 13 hooks declared and
13 run, `stable_sha256 687a4543…`.

Also corrected where the mechanism lives rather than only in a freeze record: the worker's
docstring said "numpy lives in that user site directory". So do **astropy — which parses the
sidecar** — plus erfa, scipy and yaml, and the CommandLineTools site-packages still precedes the
add-back.

## What v9 did NOT fix, and one it introduced

- **KIMI-V9 F3, the same sentence shape, half-true.** "even a refusal carries it" holds for the
  isolation refusal and every closure refusal — but **five other early `fail()` sites carry no
  interpreter state**: subject missing, subject digest mismatch, stdin not JSON, stdin lacking
  `manifest`, and a non-list manifest. Read strictly, the sentence covers those and it does not.
  The repair is one argument each. A round whose purpose was making two sentences true left the
  same sentence shape half-true on the same file, which is that seat's phrasing and it is right.
- **F2** — the brief's question block is v8's verbatim and still cites probe B03, removed in v7.
- **F4** — the suite's own text names v6/v7/v8 in places where it means v9.
- **F5's carried list** — the six `varies` strings, B06's vacuous hook, F05's basis, the worker
  timeout, ignored stdin keys, the WORKER-ERROR channel, R06's thin payload, the unused
  `require_environment()`, the three fingerprint blind spots, and the selection's missing
  producer receipt.

## The pattern this round completes

Five rounds. Every one closed the previous round's findings and introduced a smaller defect of
the same kind — and for the last four, the *only* defects in the artifacts were mine, made while
repairing: a hardcoded filename, a hardcoded phrase, a claim left standing after the mechanism
moved beneath it, a brief carrying the previous version's hashes, and now a sentence that is
true in the place it was false and untrue in five smaller places.

The mechanism findings have been minor-only for three rounds. The defect rate I introduce while
repairing now exceeds the defect rate the repairs remove. That is the argument for stopping, and
it is an argument about me rather than about the mechanism.
