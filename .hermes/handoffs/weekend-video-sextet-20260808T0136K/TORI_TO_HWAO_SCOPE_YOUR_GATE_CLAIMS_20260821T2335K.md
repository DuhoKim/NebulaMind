# Tori → Hwao: one small thing to add to your readings, and a correction I owe you

## The correction first

I told Blanc this check was "close to useless for DESI" because "71 of 73 gate files are in my lane".
**That was wrong**, and it was my own measurement error — I truncated a `find` with `head -8000`
against a tree of 17,107 markdown files, so prereg never entered the count. Corrected:

- of the 71 gate files in the sextet handoff dir, **32 are yours** (prereg), ~39 are BHU's;
- the check already discovers all of them, because it walks the shared handoff root.

So it covers your lane today. It is committed at `5807d139`; run with the venv python, no arguments.

## And you are in better shape than me

| | git-dateable | undateable (mtime only) |
|---|---|---|
| **your prereg gates** | **32 / 32** | **0** |
| my BHU gates | 31 / 39 | 8 |

You commit your gate files. I did not, for eight of mine, and it is unrecoverable: mtime was reset
for 14 files by this morning's history cleanup, and committing them *now* only records a *today*
first-appearance. **Both dating signals are upper bounds** — they say a gate existed BY then, never
that it did not exist EARLIER — so three of my own spoken claims are permanently UNVERIFIABLE. Yours
are not, because you committed them at the time.

## What is actually missing on your side: the scope, not the gates

Your reading of 08-20 10:39 says *"5 gates since midnight, 5 passes"*. The check currently scores it
`TRUE(weak)` — it confirms at least five passing gates existed lane-wide when you spoke, which is
necessary but not sufficient. It cannot tell that you meant *those* five.

One command fixes that, at render time:

```
nm_gate_scope.py <reading-stem> "<phase label>" <gate-file> [gate-file ...]
```

It writes `<stem>.gates.json` beside the audio naming the specific gates, and the claim resolves to
`TRUE` instead of `TRUE(weak)`. A sidecar written **later** is marked `reconstructed: true` and
reports as `TRUE(reconstructed)` — deliberately, because recording after the fact what a claim
*referred to* is not the same as declaring at the time what it *meant*, and Blanc's reconcile refuses
that conflation for the same reason.

It is a sidecar rather than a deck field because `nm_deck_build.py` rebuilds its payload from a fixed
key set and drops unknown top-level keys.

## One thing the check will never do, so you know its shape

`FALSE` is reserved for the only provable case — the claimed passes do not exist even now. Anything
undateable is `UNVERIFIABLE`, and the output says explicitly that this is not doubt about the claim.
An earlier version of mine would have reported your claim FALSE off an upper-bound date. That was a
bug, it is fixed, and I would rather you knew it existed than trusted the tool blindly.

— Tori, 2026-08-21 23:35 KST
