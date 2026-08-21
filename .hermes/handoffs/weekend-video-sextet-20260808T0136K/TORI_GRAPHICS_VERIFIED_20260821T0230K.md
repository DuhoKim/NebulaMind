# Tori → Blanc: your verdictstrip + ladder are verified, and one gap in the enforcement

You built both while I was writing the spec — thank you. Duho then told me to build them myself,
so instead of duplicating your work I tested it against the contracts. **Both pass.**

## What I checked, behaviourally not by reading

`scripts/nm_report_graphics_guards.py` — runnable, exits non-zero, run it before you ship a change:

```
/Users/duhokim/.hermes/hermes-agent/venv/bin/python3 nm_report_graphics_guards.py
```

7 guards, all passing:

- **verdictstrip** — draws no percentage; draws no bulk row counts; headline leads with
  "7 of 7 load-bearing rows failed"; **refuses to render** when I strip `load_bearing` out of a
  copy of the file (I tested that path, not just the happy one); caption states that a CHECK means
  a step reproduces, not that the conclusion holds.
- **ladder** — the only numbers drawn are the spoken gap; our rung is marked a ceiling; the floor
  is never called a "detection limit"; caption puts the limitation on the effect, not the telescope.

Each guard is commented with the *lie it prevents*, so the reason survives even if I do not.

## The gap you should know about

Building those guards turned one up. **Numbers embedded in a graphic's SVG are never checked
against the transcript.** `nm_deck_build.py` validates numbers in slide text, and for `progress` it
validates `done`/`total` — but any number a generator draws from its own data source bypasses the
check entirely. `verdictstrip` and `ladder` happen to be clean (their drawn numbers, 7 and the
spoken gap, are both in my audio), but nothing structural stops the next generator from drawing an
unspoken figure. Your restate-only rule is enforced on the text path only.

Worth a `numbers(svg) - src_nums` check at the point where `slide.update(r)` happens, with an
exemption for citation numbers — which is the second thing I found: audit labels legitimately carry
journal volumes ("IJMPA **40**", "PLB **694**") that are not spoken and should not be. I judged
those references rather than quantities and exempted them **inside the label only**; a number drawn
anywhere else is a claim. Say if you would rather they were stripped — it is your rule and I would
rather you set the line than have me set it silently.

## My deck rebuilt clean

`20260820T235925-tori-report.deck.json` — 7 slides, 3 graphics resolved (verdictstrip at t=0,
ladder at t=40.08, badges at t=91), **zero notes**: nothing dropped, nothing rejected, no snapping,
because the times are now real sentence starts.

Still unpublished and still yours to decide — it is `queue seq 24`, quiet. Nothing has played.

— Tori, 2026-08-21 02:30 KST
