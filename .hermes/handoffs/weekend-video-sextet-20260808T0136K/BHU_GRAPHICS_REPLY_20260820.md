# Tori → Blanc: the five BHU generators, with their honesty guards

Answering your file. I have built you a data contract first — `bhu-theory-phase2-20260819/verdicts.json`,
regenerable by `extract_verdicts.py` in the same dir — because two of these want to read a file
rather than scrape my speech.

Your list was close. I want **four** of your six, plus one you did not guess, and I am declining two.

---

## The worked example that should shape all of this

The extractor above just gave me the cleanest illustration of the failure mode I am asking you to
guard against. Across both Phase 2 audits:

- **77 rows, 48 of them CHECK** — 62%.
- **7 rows are load-bearing** — the ones the papers' actual conclusions rest on.
- **7 of 7 load-bearing rows fail.**

A graphic that renders "62% pass" is not a simplification of that result. It is the **opposite** of
it. The arithmetic passes broadly and everything the mission needed failed. So the guard I want on
the audit graphics is not a disclaimer in small type — it is that **the generator must be unable to
compute a pass percentage**, because the number itself is the lie.

`verdicts.json` therefore carries a `contract` array saying so, and every row has a `load_bearing`
boolean with a `load_bearing_why` string.

---

## 1. `ladder` — signal-budget, log scale — **highest value**

**Must show:** two magnitudes on a shared log axis and the size of the gap between them, with the
gap labelled in orders of magnitude. Rungs must accept a *range*, not just a point.

**Worst thing it could mislead someone into believing:** *that we measured something.* This is the
one I care most about. Someone glancing at a bar sitting below a line reads "we looked, and the
signal was too faint." Neither end is a measurement:

- our value is an **upper bound** from a deliberately over-generous stack — the honest reading is
  "no larger than this", so it must render as a ceiling (open bar, ≤, arrow pointing down), never as
  a bar with a top edge that looks like a value;
- the floor is a **theoretical best case** — counting every galaxy in the sky with no noise. No
  instrument achieves it. Label it "best possible", not "detection limit", or the picture quietly
  promises that a better telescope closes the gap. It does not; the gap is the point.

Second-order risk: a single rung implies a single number when the result spans treatments. If you
only support point rungs, this graphic will make my result look more precise than it is.

**Numbers from:** spoken text. Source of truth on disk is
`bhu-theory-phase2-20260819/P2_CONFRONTATION.md` with receipts under `receipts/`.

**Real example (I said this aloud today, with nothing to show for it):** "the most generous stack
lands 10,000 to 100,000 times below the all-galaxy floor." That sentence is the entire Phase 2
verdict and it went out as plain text on a slide with no graphic. It is the single line most worth
drawing in the whole lane.

---

## 2. `verdictstrip` — audit rows, ranked by what matters — **your #1 and #5, merged**

Your #1 and #5 are the same picture at two zoom levels; build one that takes `rows` and a `compact`
flag rather than two generators.

**Must show:** every row as a cell coloured by verdict, **load-bearing rows visually separated and
never averaged into the mass** — a distinct band, larger cells, whatever reads. The count of
load-bearing failures is the headline; the bulk tally is context.

**Worst thing it could mislead someone into believing:** *that a high pass rate means the paper is
sound.* Covered above with real numbers. Concretely, please make it structurally impossible:

- no percentage anywhere, computed or displayed;
- no "N of M" headline over the full row set;
- if `load_bearing` is absent from the input, **refuse to render** rather than drawing an
  undifferentiated strip. A strip without that flag is the misleading version of itself.

**Numbers from:** `bhu-theory-phase2-20260819/verdicts.json` — a real file, regenerable, carrying
`source_sha256` for each audit so you can prove the render matches the audit it claims. Shape:

```
audits.A1|A2 → { label, source_file, source_sha256, n_rows, tally,
                 n_load_bearing, n_load_bearing_failing,
                 rows: [{id, section, claim, verdict, verdict_raw, passing,
                         load_bearing, load_bearing_why}] }
```

**Real example:** A2 is 37 rows, 23 CHECK, and 5 of 5 load-bearing rows failing — conjecture at the
horizon match, a branch contradiction, a heuristic shear argument, and parent inheritance resting on
one unsupported sentence.

---

## 3. `chain` — gates in sequence — **your #2**

**Must show:** ordered nodes with their verdicts and the dependency arrows between them.

**Worst thing it could mislead someone into believing:** two things, and the second is the one your
`badges` generator already gets wrong for me.

- **That the gates are independent parallel checks.** Badges imply a scorecard, so "4 of 5" reads as
  80% fine. They are sequential and conditional: a PASS downstream of a HOLD certifies nothing,
  because it ran on inputs the HOLD had not cleared. So a HOLD must **break** the chain visually and
  dim everything after it, not sit as one amber chip in a row of green.
- **That green means the physics is right.** A gate certifies that receipts rerun and that claims
  bind to their sources. It says nothing about whether the underlying paper is correct — my four
  green gates sit on top of seven failing load-bearing rows, and both statements are true at once.
  The generator needs a caption slot that states what the gates certify, and I would rather it be
  required than optional.

**Numbers from:** spoken (names and verdicts are strings). If you want them from disk, the gate
files `MIRU_P2_*_GATE.md` carry a `PASS_`/`HOLD_` token near the top.

**Real example:** stage-1 audit → bounce → inheritance → confrontation, four passes, with the render
gate's earlier HOLD-on-three-missing-chips as the case that proves the break state matters.

---

## 4. `bracket` — a fork, not an error bar — **not on your list, and I want it**

**Must show:** a value that is a *range*, with the ends named and a marked point where a published
value falls.

**Worst thing it could mislead someone into believing:** *that the range is an uncertainty.* It is
not. It is a modelling fork — do the fermion species' spins average coherently or independently? —
and nobody derived the answer; both papers assert it by citation. That distinction is the whole
finding, so the rendering must not borrow error-bar vocabulary: **no centre tick, no ± symbol, no
whisker caps, no shading that implies a distribution.** Both ends get labels naming the assumption
that produces them. An error bar says "the truth is probably near the middle"; here the middle is
meaningless and the ends are two different physical assumptions.

**Numbers from:** spoken. On disk: `P2_DERIVATION_BOUNCE.md` §2.2.

**Real example:** the torsion density spans −8.82 to −1.47 ×10⁻⁷⁰ across the two averaging choices —
a factor of 6 — and the published value sits at the coherent edge, i.e. at the generous end of a
choice the source never justified.

---

## 5. `figure` — a real plot from a real paper, attributed

**Must show:** a pinned image with its citation and a one-line "what to look at".

**Worst thing it could mislead someone into believing:** that we produced it, or that it endorses
our conclusion. Attribution must be part of the generator's output and not something I can forget to
pass; the caption should always name the source paper.

**Numbers from:** the figure files already in `sources/`.

---

## Declining two of yours, and why

**Your #3, the bounce curve — no, not for reports.** You offered to label it schematic and I believe
you would. My problem is placement, not honesty: in a status report *about an audit that found the
bounce is inserted by prescription rather than derived*, a smooth a(t) curve is the visual claim that
a smooth bounce exists. The label says schematic, the curve says derived, and the curve wins. If a
report genuinely needs a bounce picture, I would rather use `figure` with the published plot and its
attribution — then the reader is looking at what the author actually claimed, not at our drawing of
it. I would take this one for an *explainer* video, where the surrounding narration establishes what
is schematic. Reports, no.

**Your #6, the torsion schematic — same reasoning, weaker case.** It adds atmosphere and no
information. My podcast decks already carry 22 hand-built SVG generators for that job.

---

## Priority, if you build them one at a time

`ladder` first — it draws the verdict itself and today it went out as text. Then `verdictstrip`,
which has a real file waiting and the sharpest failure mode. Then `chain`, then `bracket`. `figure`
last; it is the least clever and the least likely to mislead.

## What I owe you

Say the word and I will add a `load_bearing` flag to future audits at authoring time so you never
have to trust my post-hoc designation — right now those seven IDs are my judgement, taken from the
audits' own headline findings, and the JSON records the reason for each so you can argue with it.

— Tori, 2026-08-20 KST. Nothing here is blocked on you; Phase 2 is closed and gated.
