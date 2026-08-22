# Audio disclosure ledger — what the published reports actually SAY

> **CORRECTED 2026-08-21 22:1x KST — the values below were wrong.** This file
> first recorded the disclosed values as *"zero point 27, zero point 20, minus
> zero point 20"*, taken from the caption. The audio says **0.834336, 0.384410,
> and −0.640352** — six-decimal precision, verified by my own `faster_whisper`
> run agreeing with the two models in Hwao's `CHI_DISCLOSURE_ASR_FINDING`.
>
> The caption was wrong because **my caption normaliser summed a digit sequence**
> (8+3+4+3+3+6 = 27). Root cause, fix and the regeneration of the affected
> captions: [CAPTION_CORRUPTION_20260821.md](CAPTION_CORRUPTION_20260821.md).
>
> **The method below is also unsound where it clears anything.** It read
> captions, and a caption is not a faithful record of its audio. The 17
> exclusions and the statement that none of Tori's 21 transcripts carry
> χ-shaped values rest on text, not on what was spoken. Treat every "excluded"
> or "clean" line here as unverified until re-run against ASR. The one
> DISCLOSING entry is confirmed — by audio, not by caption.
>
> Corrections are recorded as appended ledger events
> (`disclosure_audit_CORRECTION`, `caption_corrected` ×2), never by rewriting
> history.

Built 2026-08-21 on Duho's instruction, after `GATE_CHI_CUSTODY_R6_20260821.md`
refuted the Chi Custody Receipt for omitting the rendered MP3 as a disclosure
surface. Three independent local ASR runs of the 23:12 audio agreed it speaks
real χ values aloud, and the receipt's disclosure ledger — which enumerates
documents — had never counted it.

The gate is right, and the gap is mine. Tonight's publication ledger
(`queue_ledger.jsonl`, see [PUBLICATION_LEDGER.md](PUBLICATION_LEDGER.md))
records **that** a report was published. Nothing recorded **what it contains**.
A ledger that stores a filename and not the fact that the file says three real
measurements out loud will pass its own audit while missing the thing an auditor
came for.

Reproduce with `HermesOps/scripts/nm_disclosure_audit.py`; machine-readable copy
in `disclosure_audit_20260821.json`; recorded as a `disclosure_audit` event in
the append-only ledger (event 45).

## Method, and the discriminator

> **These counts are products of the unsound method and are superseded.**
> `GATE_CHI_CUSTODY_EVIDENCE_20260822` Finding 5 is right that this file kept
> asserting counts in its body while its header said the method was unverified —
> a document contradicting itself on the same page. Current position, from the
> audio-based sweep v2 (all numbers, both directions, 219 reports, 0 ASR errors)
> plus a re-run of the caption audit over 222 transcripts: **1 report discloses
> real measured values** (unchanged, and the one finding that never depended on
> the broken method), **17 carry other decimals and are excluded**. Thirteen
> captions were corrupted and are repaired; see
> [CAPTION_CORRUPTION_20260821.md](CAPTION_CORRUPTION_20260821.md). The
> historical text below is retained rather than edited, because the numbers it
> got wrong are part of what the record has to show.

All **220** transcripts on disk were scanned — live and `_drafts/` — for spoken
(`"zero point 27"`, `"minus zero point 20"`) and numeric (`0.27`) values.
**18** carry decimals. Only **1** carries a real measurement.

The discriminator is a date, not a judgement. The campaign's first real
measurement was **2026-08-20**. Nothing spoken before that can be a real χ: it
is published literature (Longo's dipole amplitude, ~0.04), a preregistered
threshold, or a rehearsal artifact. Every exclusion below is on that basis and
is checkable without taking my word for it.

## The disclosure

**`20260820T231235-hwao-report`** — published seq 20, recorded 23:12:35 KST,
published 23:12:51 KST, 16 seconds later. Never republished, never withdrawn.

> "The first 3 real values: 0.834336, 0.384410, and -0.640352."

The caption now says what the audio always said. The line this file originally
quoted — *"zero point 27, zero point 20, and minus zero point 20"* — was the
corrupted caption, and those three numbers were never measured.

Eleven sentences later the same report says *"nobody is allowed to look yet. No
tertile, no average, no summary of chi until the last galaxy is cut."* Both
sentences are in the same 182-word caption.

**Six surfaces carry it**, not one. Counting only the MP3 is how it was missed:

| surface | path | sha256 (16) |
|---|---|---|
| audio | `20260820T231235-hwao-report.mp3` | `2a38a887bd897147` |
| caption | `20260820T231235-hwao-report.txt` | `2c85b2028209273a` (was `7c8a8668a00cd9b8`) |
| slides | `20260820T231235-hwao-report.deck.json` | `1da50dc6878db905` |
| alignment | `20260820T231235-hwao-report.times.json` | `a9cfedc4ab127794` |
| served page | `report-20260820T231235-hwao-report.html` | `050a3f6245fc74f1` (was `c5d5d5b81f5ae997`) |
| served page | `archive.html` | `c104ea59992472cc` (was `36a0499615eb74ca`) |

Three digests moved when the corrupted caption was repaired; the old values are
kept beside the new so a receipt pinning either can tell which it holds. The
**audio digest never moved** — the mp3 was not touched at any point, which is
what makes it the authority the text surfaces are checked against. `archive.html`
changes on every index rebuild, so it is the weakest pin here and should not be
cited as evidence of anything but the page's current state.

The alignment file matters and is easy to overlook: it carries per-sentence
timings, so it locates the values in the audio to the second.

## Checked and excluded — 17

Recorded because an auditor needs what was rejected, not only what was found.
All predate 2026-08-20:

- **2026-08-11 `spin-recap`** — 0.095 ± 0.024 parity symmetry, from external
  catalogue cells, nine days before the run's first measurement.
- **2026-08-12 (6 reports)** — Longo's published 0.04, a mirror-artifact range
  0.058–0.944 quoted *as a fraction of the χ scale*, power targets at 0.02.
  Systematics rehearsal, explicitly about what a resampling mirror can fake.
- **2026-08-14 (9 reports)** — preregistered thresholds and estimator sigmas
  (0.12 vs a 0.8 limit, 0.13 vs 0.6, a 0.85 pass floor). Design values arguing
  about what the threshold should be, before any data.

## What this does NOT rule on

**Whether the disclosure was authorised.** The report says the no-unblinding
clause was *"deliberately spent"*, which may make it sanctioned rather than a
leak. That is the investigator's call and Duho's signature, not mine. This file
establishes only what was published, on which surfaces, and when.

Nothing was altered, withdrawn, or unpublished in producing it. Editing a
published report in the middle of an audit of that report is precisely the
mutation that broke the custody record earlier tonight.
