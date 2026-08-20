# Status-report overhaul — overnight campaign, 2026-08-20 23:55 KST

Duho, verbatim: **"okay let's overhaul audio report to just status report and
combine slides+audio+caption format like tori's recent report, spend a night for
that so that i can check tomorrow morning"**

## What this means (my reading, stated so it can be corrected)

Today's thing is an **audio** report with slides bolted underneath. The audio is
the artifact; the deck and caption are accessories, and the page is a *player*.
Duho wants the opposite: a **status report** whose primary form is the slides,
which happens to be narrated and captioned. Tori's podcast page is the shape —
a card per report: title, meta line, audio, slides that follow it, transcript.

So: **one report = one thing**, containing slides + audio + caption, and the
word "audio" stops being the headline anywhere in the system.

## Design decisions (mine to make tonight; reversible, all in git)

1. **The report page is the artifact.** Every reading gets a self-contained
   permalink page `report-<stamp>-<speaker>.html`: headline slide large at the
   top, audio bar beneath it, slides advancing with the voice, full caption
   under that, provenance footer (speaker, voice, time, counts, timestamps).
   Shareable, screenshot-able, readable with the sound off.
2. **Slides lead, audio supports.** Reading with the sound off must work: the
   deck carries the report. The player is a strip, not the centrepiece.
3. **`listen.html` becomes `status.html`** — the live view, embedding the same
   report component for the newest report, plus the recent list. Old URL keeps
   working (redirect), because the MacBook daemon and Duho's tab use it.
4. **`archive.html` stays paginated**, but rows link to report pages.
5. **Vocabulary**: "status report" everywhere in UI text. No "audio report".
6. **Nothing regresses**: quiet hours, queue delivery, restate-only enforcement,
   auto-transcribed badges, deterministic decks, honest staleness — all keep
   working exactly as they do now.

## Hard rules tonight (same as the last overnight)

- **No audio playback before 08:00 KST.** The pipeline enforces quiet hours,
  and I will not force-live anything. Morning briefing at ~08:0x is the first
  sound.
- Boundaries: no `prereg/`, no `bhu-*` work products, no other lanes' files.
  **Commit with explicit paths only** — never a directory (the 5,943-file
  mistake was mine and will not repeat).
- Every change committed in scope and pushed; the live copies mirror to
  `tools/audio-reports/`.
- Fable weekly cap is exhausted until Sat 13:59 KST; this session is Opus.
  Non-Claude seats stay available but this is single-surface work, so I do it.

## CORRECTION 00:0x — quality, not volume

Duho, verbatim: **"no report tonight, i said spend a night to make it a good
quality new format report with slides."**

I had briefed Hwao and Tori to each publish a report overnight. That was my
misreading and it is retracted. The night's deliverable is **the format at a
quality bar, demonstrated by ONE genuinely good report**, not a stream of
routine ones. Publishing nothing further tonight is a fine outcome; the
coordinators contribute judgment (which moment deserves the exemplar, what the
slides should say, which generator they need), and I do the craft.

Quality bar for the exemplar — it has to survive being read by a person who
was not here:
- the headline states the finding, not the occasion;
- every slide earns its place; no slide restates the previous one;
- graphics carry data, not decoration, and each is captioned with what it
  cannot tell you;
- the caveat sits beside the claim it qualifies, not exiled to the end;
- it reads with the sound off, and rewards listening rather than requiring it.

## Phases

- P1 build the report-page renderer + component (slides-first)
- P2 status.html (live view) + archive rows linking to report pages
- P3 ONE exemplar report built to the bar above (content from the lane that
  owns the moment); vocabulary sweep; backfill pages for existing readings
- P4 verify in a real browser (dark AND light, phone width), commit, push
- P5 morning handover + 08:0x audio briefing

## Ledger

- 23:55 campaign opened; reference read (Tori's podcast card format).
- 00:0x P1 done: nm_report_page.py renders a real report page (verified in browser, dark). Hwao+Tori briefed to write real status reports overnight per Duho.
- 00:0x CORRECTION: Duho — no reports tonight; the night is for FORMAT QUALITY plus one exemplar. Retracted my publish-a-report brief to both coordinators.
