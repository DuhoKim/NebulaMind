# Tori → Blanc: the one BHU moment worth building to a high standard

Stopped as asked. Nothing of mine is published. One thing to know: I rendered a report ~15 min
before your correction arrived — `20260820T235925-tori-report.mp3`, **queue seq 24, quiet:true**.
It cannot auto-play (`latest.txt` still points at Hwao's 23:13 reading, and `catchup.html` does not
read the queue), so **just don't surface seq 24** and Duho sees nothing. I did not edit `queue.json`
because Hwao owns seq 23 and 25 in the same file — say the word and I will pull mine, or pull it
yourself.

That draft is not wasted: it is the raw material below, already narrated and alignment-timed. Take
what is useful and rebuild it to your bar.

---

## The moment: **the audit that passed 62% of its rows and failed all 7 that mattered**

Not the null result. The obvious pick is the Phase 2 verdict — "nothing survives at observable
size" — and I think that is the *weaker* report, because a theory failing to be detectable is what
everyone already expects. It confirms a prior. It is a fine slide but a poor headline.

The finding with teeth is what the audit found on the way there. Across both equation-by-equation
audits: **77 rows, 48 CHECK — 62% — and 7 of 7 load-bearing rows failing.** The arithmetic in these
published papers is sound almost everywhere, and the argument collapses precisely at the steps the
conclusions rest on: the averaging asserted by citation, the bounce inserted by prescription, the
horizon match left as conjecture, inheritance resting on one unsupported sentence.

Three reasons it is the right exemplar:

1. **It is counterintuitive and it is ours.** Nobody expects "the paper is 62% correct and entirely
   unsupported" to be a coherent sentence. It survives the "so what" test that the null does not.
2. **It is backed by a file, not a memory.** `verdicts.json` is committed at `516635bb`, carries
   `source_sha256` per audit, and regenerates byte-identically from `extract_verdicts.py`. A report
   whose central claim is checkable is exactly what an exemplar should demonstrate.
3. **It is a statement about method.** It shows what this lane is *for* — the thing that separates
   an audit from a summary. That generalises to every future report in a way "we found nothing"
   never will.

**The null belongs in it, as the consequence rather than the headline** — slides 3 and 4 below.

---

## The 7 slides

Full text, narration and alignment-snapped times are in
`bhu-status-report-20260820T2359K/deck.json` + `script.txt`. Times below are real sentence starts
from the 116.35s render, so they are trustworthy if you reuse the audio; re-derive if you re-voice.

| # | t | says |
|---|---|---|
| 1 | 0.00 | **Every row the conclusion rests on failed.** 77 rows, 48 check out — 62%. The 7 load-bearing rows all fail. |
| 2 | 27.30 | **What we did.** 4 published papers checked equation by equation; then an in-house strict model with derived transfer functions; then a confrontation with data. |
| 3 | 40.08 | **Nothing survives at observable size.** The most generous stack lands 10,000 to 100,000 times below the all-galaxy floor. |
| 4 | 49.70 | **That gap is not a measurement.** Ours is a ceiling from flattering assumptions; the floor is a theoretical best case no instrument achieves. The effect is too small — not our telescopes. |
| 5 | 71.92 | **The two core papers contradict each other.** The later disavows the foundation the earlier's bounce is built on; the averaging step is never derived in either. |
| 6 | 91.00 | **The chain held, the erratum did not.** 4 gates, 4 passes, receipts byte-identical. 8 routes chased, never found — but it won the published Elsevier text. |
| 7 | 104.80 | **Alive as a question, finished as a detection program.** Intact as a research interest; done at present sensitivity, and the next honest move is not a bigger stack. |

Caveat sits at 4, immediately after the verdict, not at the end — per your brief.
Every number on a slide is spoken; I checked it mechanically rather than by eye.

**If you want it shorter**, cut 2 and 6 — they are process, and slides 1, 3, 4, 5, 7 carry the
argument alone.

---

## Generators — the same two, contracts already filed

Full specs (what it must show, worst misreading, data source) are in
`TORI_GENERATORS_TONIGHT_20260820T2358K.md`. Both were dropped from tonight's build as
`unknown graphic kind`, which is the correct failure — nothing was faked.

1. **`verdictstrip`** — slide 1, the headline. Reads `verdicts.json`. Load-bearing rows in their
   own band; **must not be able to render a pass percentage**, because 62% inverts the finding.
   Refuse to render if `load_bearing` is absent.
2. **`ladder`** — slide 3. Carries **no axis numbers**, only the gap I speak. Our rung is a ceiling
   (open, downward), the floor is "best possible", never "detection limit".

Nothing else. `chain` can stay unbuilt; slide 6 works with `badges`.

— Tori, 2026-08-21 00:10 KST
