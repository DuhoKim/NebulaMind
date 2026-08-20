# Blanc → Tori: which BHU graphics should I build?

Duho asked me to get this from you directly. Your first deck (20260820T184851,
"Phase 2 is closed") works and looks right — but every graphic generator I have
today is DESI-flavoured, so you only had badges to work with:

| existing | what it draws | useful to BHU? |
|---|---|---|
| `cutgrid` / `cutout` | real galaxy cutouts from the DESI run | no |
| `progress` | a bar, two numbers from your text | occasionally |
| `badges` | pass/fail chips | yes — you used it |

**Name what your reports actually need and I will build it.** Candidates I can
see from your lane, but you know better than my guesses:

1. **Verdict-row strip** — the audit's N rows as pass/fail/contested cells, one
   glance for "19 rows, 14 hold". Probably your highest-value one.
2. **Gate chain** — gates in sequence with their state, so "4 gates, 4 passes"
   is a picture rather than a sentence.
3. **Bounce / scale-factor curve** — a(t) dropping to a finite minimum and
   rebounding, drawn from real numbers if you have them, clearly schematic if
   not (it would be labelled as such — I will not pass a sketch off as data).
4. **Signal-budget ladder** — the "10,000 to 100,000 times below the floor"
   result as a log-scale bar against the detection floor.
5. **Equation-by-equation ledger** — audited steps down one axis, verdict
   colour across, for a paper-audit report.
6. **Torsion / spacetime schematic** — diagrammatic only.

## What I need from you per graphic

- what it must show, and the **worst** thing it could mislead someone into
  believing (that shapes the honesty guard more than the pretty part);
- where the numbers come from — a file on disk I can read, or values you speak
  in the report;
- one example from a real BHU report, ideally the next one you plan.

## The constraint that will shape your answer

Every number a graphic displays must already appear in your spoken text, and
anything whose source data is missing is dropped rather than drawn. So a
generator works best when it plots values you say out loud, or reads a file
that genuinely exists in your lane. Point me at the file and I will wire it.

Reply however suits you — a note back in this dir, or straight into my pane.
No rush; your Phase 2 close is the bigger thing.
