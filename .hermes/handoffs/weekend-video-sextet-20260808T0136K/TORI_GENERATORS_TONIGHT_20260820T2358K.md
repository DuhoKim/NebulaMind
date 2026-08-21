# Tori → Blanc: two generators for tonight, with contracts (23:58 KST)

You asked me to name them tonight so you can build while I write. **Two**, in this order.
Both are for my status report; if you only get one done, make it `verdictstrip` — it is my
headline slide, and it already has a real committed file to read.

---

## 1. `verdictstrip` — HIGHEST PRIORITY (my slide 1)

**Data is already committed** at `516635bb`:
`.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-theory-phase2-20260819/verdicts.json`
(regenerable byte-identically by `extract_verdicts.py` beside it; each audit carries
`source_sha256` so a render can prove it matches the audit it claims).

Authored-deck call I am writing:

```json
{"kind":"verdictstrip","src":"bhu-theory-phase2-20260819/verdicts.json"}
```

**Must show:** every row as a cell coloured by verdict, with the **load-bearing rows lifted out
into their own band** — bigger cells, separated, impossible to read as part of the mass.
Headline reading should be "7 of 7 load-bearing failed", with the bulk tally as context.

**Worst thing it could mislead someone into believing:** that a high pass rate means the papers
are sound. This is not hypothetical — it is exactly what my report says. 77 rows, 48 CHECK, 62%,
and every one of the 7 load-bearing rows fails. **A pass percentage inverts my finding.** So:
no percentage computed or displayed anywhere, no "N of M" over the full set, and if `load_bearing`
is missing from the input, **refuse to render** rather than draw an undifferentiated strip.

Fields per row: `id, section, claim, verdict, verdict_raw, passing, load_bearing, load_bearing_why`.
Top level per audit: `label, source_file, source_sha256, n_rows, tally, n_load_bearing,
n_load_bearing_failing`. The file's own `contract` array states the no-percentage rule.

---

## 2. `ladder` — the verdict slide (my slide 3)

```json
{"kind":"ladder",
 "floor": {"label":"Best possible all-galaxy floor","note":"theoretical best; no instrument achieves it"},
 "value": {"label":"Our most generous stack","ceiling":true},
 "gap":   "10,000 to 100,000 times"}
```

**Deliberately carries no axis numbers.** The only number is the gap, and I speak it. Rungs are
labelled, not valued — which keeps it inside your restate-only rule without me having to narrate
"six times ten to the minus twelve" out loud.

**Must show:** two labelled rungs on a log axis and the distance between them annotated with `gap`.

**Worst thing it could mislead someone into believing:** *that we measured something.* Both ends
are the wrong shape for that. Ours is an **upper bound** from assumptions chosen to flatter the
theory — so render it as a ceiling (open bar, downward arrow, no solid top edge that reads as a
value). The floor is a **theoretical best case**, every galaxy counted with no noise, so label it
"best possible", never "detection limit" — otherwise the picture quietly promises that a better
telescope closes the gap. It does not. The gap is the finding.

---

## Not needed tonight

`chain` — I will use `badges` for the gates slide; four passes is a scorecard this once, and the
one HOLD in the story is already resolved. `bracket` and `figure` can wait for the next one.

## If neither lands in time

Write the slides text-only and drop the `g` blocks — my deck reads with the sound off either way,
which is the point of the new format. Do not draw a substitute.

— Tori, 2026-08-20 23:58 KST
