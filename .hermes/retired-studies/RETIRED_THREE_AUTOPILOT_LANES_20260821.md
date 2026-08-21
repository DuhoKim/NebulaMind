# Retired: three lanes that had been asking for a decision for two weeks

Retired by Duho, 2026-08-21, verbatim: **"retire all three and add age to NEEDS YOU"**.

| lane | stage | last touched | video |
|---|---|---|---|
| `spin-parity-census-20260805T1922K` | 6/17 | 2026-08-07 | narrated cut, published unlisted |
| `mzr-archive-census-20260805T1857K` | 5/17 | 2026-08-06 | narrated cut, unpublished |
| `c41-trackb-shape2-mzr-20260804T1452K` | — | 2026-08-06 | narrated cut, unpublished |

## Why they were retired

All three sat at **"GATE: PASS — gates clear, freeze decision pending"** and had done so on
every cockpit render for a fortnight (335, 355 and 355 hours untouched at retirement). Their
machine gates passed; nothing after that ever happened.

They belong to the cohort covered by the standing bar in
`HUMAN_REJECTION_RECORD.md`: *a flagship study must contain something that exists nowhere else
— a measurement, a census, or a negative result established under a pre-registered contract.
Assembly of published values plus a systematics commentary does not qualify.* Two of the three
are MZR papers, the same family as the z≈9–10 metallicity-deficit paper Duho pulled on
2026-08-05 for exactly that reason.

Retiring them is not a judgement that the work was worthless — it is a refusal to keep asking a
human to decide something that has not moved in two weeks, in wording ("gates clear") that
sounds more affirmative than the situation deserved.

## Disposition

- Nothing deleted. Each lane directory keeps every artifact and gains a `RETIRED.md` naming the
  date, the instruction, and this record.
- The cockpit's paper collector skips lanes carrying that marker, so they no longer appear as
  "NEEDS YOU". They remain on disk and in git history.
- The published unlisted video for `spin-parity-census` stays as it is; retirement of the lane
  is not a retraction of anything already shown.

## The board defect this exposed

"NEEDS YOU" carried **no age**, so a two-week-old prompt looked identical to a fresh one and
three dead lanes read as live decisions every time Duho opened the page. Fixed in the same
change: every awaiting-human row now shows how long it has been untouched, amber past 48 hours
and red past a week.
