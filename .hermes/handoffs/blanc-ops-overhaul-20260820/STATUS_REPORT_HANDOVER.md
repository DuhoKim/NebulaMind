# Morning handover — status-report format (Blanc, 2026-08-21)

**Open this first:**
https://duho-macstudio.taila27502.ts.net/reports/status-audio/report-20260821T004950-hwao-report.html

That is the exemplar you asked for: a status report in the new format, read it
with the sound off. Second one, from a completely different kind of work:
`report-20260820T235925-tori-report.html`. Live surface is now **status.html**
(listen.html redirects; your MacBook daemon is unaffected).

## What changed

The old thing was an **audio** report with slides bolted underneath — the audio
was the artifact and the page was a player. Now a status report is **one page**:
slides carry it, the voice narrates it, the caption records it. It has to read
silently, and it does.

| before | after |
|---|---|
| listen.html, a player | **status.html**, the live surface |
| a reading + a deck + a caption, separately | **one report page** per report, permalinked |
| "audio report", "readings" | "status report", "reports" everywhere |
| slides = bullets restating the caption | slides = the report; graphics carry real data |

## The two exemplars

**DESI (Hwao's spec).** He corrected my framing, and he was right: "first galaxy
measured" is the occasion; the finding is that **the study spent 2 days
deliberately not measuring** because two parameters were still choosable, and
choosing them a day later would have voided the run rather than delayed it.
Seven slides, every graphic kind exercised — real cutouts, frozen-choice badges,
a receipt card, the sky map, the pipeline chain. Slide 4 is the review that
caught the team's own amendment citing the wrong file; he insisted it stay
unsoftened, and he is right that it is the reason to trust the rest.

**BHU (Tori's spec).** She rejected the obvious headline — the null result — as
the *weaker* report, because a theory failing to be detectable confirms
everyone's prior. Her finding: the audit **passed 48 of 77 rows and failed all 7
that the conclusions rest on**. The verdict strip renders exactly that: the bulk
in small green cells, the load-bearing failures lifted out large and red.

## New graphics, all reading real files

`skymap`, `chain`, `failstrip`, `throughput`, `cutgrid`, `receipt` (DESI);
`verdictstrip`, `ladder` (BHU); plus `progress` and `badges`.

Each carries its own count and timestamp so a screenshot cannot age silently,
and each is captioned with what it *cannot* tell you. Three examples of the
constraint doing real work:
- the sky map labels the RA-ordered transfer front **on the image**, because an
  unlabelled leading edge reads as "a region is missing" when it means "not yet
  reached" — and states that the empty north is a frozen southern cap, not
  absent data;
- `verdictstrip` **refuses to render a pass percentage**, because 62% passing
  inverts Tori's finding — and refuses to render at all if the load-bearing
  flag is missing;
- `failstrip` draws the zeros and says "no digest mismatch **so far**", never
  "verified perfect".

## Bugs found by building it (all fixed)

1. **Sentence-final numbers failed their own slides.** My validator's regex took
   the trailing full stop, so `208,407.` never matched a slide quoting
   `208,407`. Correctly-written slides were being rejected.
2. **Light mode was unreadable where it mattered.** Measured on the real pages:
   amber numbers scored **1.57:1** against white, cyan kickers 1.65:1, chips
   3.11:1. The numbers *are* the content of a status report. All now ≥4.5:1.
   Phone width verified: nothing overflows 390px.
3. Time chips could not seek at all (the host answers Range requests with a
   plain 200), so clicks snapped back and dragged the slide with them.

## Held for you

- **Two reports were pulled**, on both coordinators' own recommendation: they
  went out minutes before your "no report tonight" correction, and neither
  wanted the format judged beside its own drafts. They are in `_drafts/`,
  nothing deleted.
- **A lane edited `nm_status_say.sh`** (my single-writer file) at 23:35 to add a
  stable per-reading URL, because `latest.mp3` races when three coordinators
  publish into one directory — one report overwrote another by 48 seconds and
  the wrong one played. The diagnosis was right, so I kept the work and pointed
  it at the report page. Worth a word about the boundary, not a reprimand.
- **Retention still unresolved**: status-audio is ~300 MB and grows ~30 MB/day.

## What I would do next

Give the report pages an index (a "reports" home), and let a report carry more
than one graphic per slide. Neither blocks anything today.
