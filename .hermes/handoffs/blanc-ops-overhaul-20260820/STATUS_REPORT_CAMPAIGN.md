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
- 00:12 tick: pulled 3 draft reports to _drafts/ (both lanes recommended it; queue 25->22 entries, seq counter untouched, nothing deleted). Built the receipt-card generator Hwao prioritised. Both exemplar specs received and read — Hwao reframes the finding as the discipline not the galaxy; Tori argues the null is the weaker headline and the 62%/7-of-7 audit pattern is the finding. Next: build the exemplar.
- 00:52 tick: exemplar built to Hwao's 7-slide spec (aligned 96%, 24 sentences, 7/7 slides accepted, all 5 graphic kinds exercised incl. the new receipt card). Fixed a validator bug found while building it: sentence-final numbers swallowed their full stop and failed their own slides. NOTE: another lane edited nm_status_say.sh (added deck.html?f= stable per-reading URL, good work, solves the latest.mp3 race) — converge with report pages next tick, do not revert.
- 01:12 tick: P2 done — status.html live surface (listen.html redirects), archive rows link to report pages, vocabulary swept to 'reports', postprocess renders a page per reading, deck.html?f= forwards to it.
- 01:51 tick: P3/P4 — backfilled 11 report pages; measured accessibility on the real pages: light-mode numbers were 1.57:1 (invisible), kickers 1.65:1, chips 3.11:1 — all fixed to >=4.5:1; no element overflows 390px.
- 02:12 tick: built Tori's two generators (verdictstrip, ladder) to her filed contracts; both honesty guards verified mechanically incl. the refuse-to-render path. Next: build her BHU exemplar deck, then handover.
- 02:50 tick: BHU exemplar rendered (7/7 slides, verdictstrip + ladder live). Two exemplars now exist across unlike lanes.
- 02:51 handover written; campaign complete pending the 08:04 delivery.
- 03:50 tick: restored Tori's exemplar to the queue as a quiet entry so BOTH exemplars appear in the morning view (it was pulled as a draft; it is now a finished exemplar). Verified live: preview = Hwao 00:50 'queued overnight, not played', open-as-page link resolves, recent list carries both.
- 04:11 tick: verified the report page WORKS not just renders (blob audio, exact seeking, 7 chips, slides advancing at 100s and 137s). Briefing text drafted and checked for digits. Cockpit rendered. Nothing unpushed.
- 04:49 tick: quiet — all surfaces 200, nothing new published, no changes needed. Holding for the 08:04 handover.
- 05:11 tick: quiet — no change, surfaces healthy, tree clean.
- 05:49 tick: quiet — no change; pushed the pending ledger commit.
