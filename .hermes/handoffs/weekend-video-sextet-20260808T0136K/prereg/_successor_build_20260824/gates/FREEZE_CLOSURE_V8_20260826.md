# FREEZE — the manifest-closure mechanism, at v8

2026-08-26, Hwao. Duho: *"freeze at v8 if kimi clears."* KIMI cleared v8 at 21:24:58 KST. This
records what is frozen, what backs it, and — at least as importantly — what freezing it does not
mean.

## What is frozen

Held read-only (`-r--r--r--`) as of this record:

| artifact | sha256 |
|---|---|
| `ref/successor_ref_v8.py` | `1bec5c2831464e023f2fee472a30480761b9a9f40cc034ba092cbfc28ad7758a` |
| `ref/closure_worker_v8.py` | `245057259830c60e65b179bc01053d531964a7005b560e264bdefa0745c0092d` |
| `ref/FIXTURES_V8_20260826.out` | `fab32ba24cedcedf7fe601c3a8d9dbde13f57b1c9bf2e0b88963bcfebc33a8b5` (46 checks, all pass) |
| `gates/closure_probe_suite_v8.py` | `382a078ff108cf0aea1f7c89f448dc650d8f86a0a7fdb6e988a711cf12309926` (33 probes) |
| `gates/CLOSURE_PROBE_V8_RECEIPT_20260826.json` | `stable_sha256 509071e1138c867567e8059fccaa6abea82446fa7b09d699e044ecede4b94939` |
| `gates/CLOSURE_V8_KIMI.md` | `47d24f3219776e7da72f3ef5fd9835777a6c5ffddc5f6111544ec5441fdb8b96` |

The suite run: 33/33 conforming, no error-typed probe, 12 verify hooks declared and 12 run.
The closure it derives: **65,060 objects → 6,445 selected bricks → 12,117 required bricks**,
`plan_digest aaeaa9f37aabf1da6000a6ad07890cfe010677e301583530ba1a108833e3b3f1`.

## What backs it, and the limitation that comes with it

**One referee seat.** KIMI reproduced the receipt's `stable_sha256` exactly with
dictionary-equal stable objects, re-derived 12,117 independently without calling the mechanism,
and tested both v8 repairs dynamically — the subject-byte execution and the early isolation
refusal, including its own poisoned-numpy run.

**The panel was designed for more than one seat and returned one.** The codex and gpt56 seats
were refused mid-analysis by their provider's safety filter on 2026-08-26, twice each, on
material that includes their own prior reports. Duho ruled that a single verdict may stand
rather than stall the lane; that ruling was made about a *gate*, and this record extends it to a
*freeze* on his instruction. **A one-seat review is a narrower review, not a stronger one.**
Anything downstream that cites this freeze should cite that sentence with it.

Four rounds of referee history sit beside it and remain legible: `CLOSURE_RECEIPT_GPT56.md` and
`CLOSURE_RECEIPT_CODEX.md` (v4, both NOT CLEAR), `CLOSURE_V5_CODEX.md` (NOT CLEAR),
`CLOSURE_V6_KIMI.md` and `CLOSURE_V7_KIMI.md` (CLEAR with conditions). v4 through v7 are
unmodified on disk so each report still checks against the digests it pins.

## Known-open at freeze time — carried, not closed

Freezing does not convert these into resolved. Every one was named by a referee and is
reproduced here so a later reader cannot mistake silence for absence.

1. **Two claims in the frozen bytes are now false** (KIMI-V8 F3), **and the fact they promised
   is supplied below instead.** The worker docstring and the suite's `not_covered` both say the
   receipt records the worker's full `sys.path`. It no longer does: the v8 fix correctly refuses
   before provenance is built, and `closure_receipt()` returns only the result. The direction is
   fail-safe — less information, never more trust — but the sentences overstate the mechanism.

   **Why they are frozen as written rather than corrected first.** Blanc, relaying, asked that
   this be resolved before the freeze rather than carried into it, on the grounds that my own
   condition was that the text must not claim what it lacks. That condition stands and this is
   an instance of it. But correcting the sentences changes the bytes, and the CLEAR attaches to
   the bytes KIMI actually ran — a corrected artifact would be an unrefereed one, and freezing
   prose no referee has seen is the precise failure this lane keeps finding in its own work.
   Editing to look right is what "self-describing" means here, and it is the thing that has
   fallen every time.

   So the claim is recorded as false, and **the transparency it promised is delivered here**,
   measured from the frozen worker rather than asserted. Note also that the referee that found
   this rated it MINOR and returned CLEAR knowing it.

   Under `python3 -I` plus the single pinned add-back, the frozen worker's `sys.path` is:

       1. …/CommandLineTools/…/Versions/3.9/lib/python39.zip
       2. …/CommandLineTools/…/Versions/3.9/lib/python3.9
       3. …/CommandLineTools/…/Versions/3.9/lib/python3.9/lib-dynload
       4. …/CommandLineTools/…/Versions/3.9/lib/python3.9/site-packages
       5. /Users/duhokim/Library/Python/3.9/lib/python/site-packages   ← the pinned add-back

   Both `numpy` and `astropy` resolve from entry 5, the unpinned user directory. Entry 4, the
   system site-packages, precedes the add-back. This is the residual in item 4 below, stated
   with its actual contents rather than by reference.
2. **The frozen planner's three files are verified and consumed by distinct reads** (F4). Unlike
   the four pinned artifacts and the subject, they are not closed by construction. Exploiting it
   needs write access to the pinned lane tree — the conceded machine-ownership class.
3. **The fingerprint's three blind spots** (KIMI-V6 F4, re-verified twice since): a global
   resolving to a module folds as `<module>`; a helper reachable only through a class method is
   not recursed into; a C callable contributes a type name. Demonstrated, not argued.
4. **The site-packages residual, wider than first stated.** Under `-I` plus the single pinned
   add-back, numpy, astropy, erfa, astropy_iers_data, packaging, yaml, scipy and dateutil all
   resolve from the unpinned user directory. The sidecar's bytes are pinned; **its parser is
   not.**
5. **Six probe `varies` strings** still omit the `PINNED_*_REL` reassignment (KIMI-V6 F7, named
   three times, never fixed). **B06's verify hook asserts nothing.** **F05's basis** claims a
   property no static-symlink probe can evidence.
6. **No timeout on the worker subprocess**; extra stdin keys ignored; the manifest-type refusal
   uses the WORKER-ERROR channel rather than REFUSE.
7. **R06's structured payload is thin**; no frozen phase-aware refusal schema;
   `require_environment()` is never called on the closure path.
8. **The selection has no producer receipt** (CODEX-V5 F6). Upstream of this mechanism, and the
   one item on this list that gates acquisition rather than merely being recorded.

## What this freeze is not

- **It is not authorization to fetch.** No image byte has been fetched. The ~148 GB ceiling Duho
  approved on 2026-08-26 is a planning decision; BS-6 still gates the first image byte, and item
  8 above is unresolved.
- **It is not a frozen preregistration.** It fills **BS-2m** — one of twelve class-P slots. The
  other eleven are unfilled, and `PREREG_SUCCESSOR_DRAFT_V10_20260825.md` has never passed a gate
  round in any of its ten drafts.
- **It does not settle the power claim.** Stage P was restored to *measured* on 2026-08-26
  (995/1000, exact per-trial nulls) but the exact implementation lives in a measurement harness,
  not in the frozen code. **BS-5p remains unfillable.**

## Why it stops here

Four repair rounds. v5 fixed caller-supplied artifacts and left mutable pins; v6 fixed the pins
and shipped a nomination parameter and hooks that never ran; v7 fixed those and left two
verify-then-consume gaps; v8 fixed those. The last two rounds produced only minor findings, and
in each of the last three the only defects in the suite were ones I introduced while repairing —
a hardcoded filename, a hardcoded phrase, a claim left standing after the mechanism moved
beneath it. The marginal defect found per round is now smaller than the defect rate repairing
introduces. That is the argument for stopping, and it is an argument about my error rate rather
than about the mechanism being finished.
