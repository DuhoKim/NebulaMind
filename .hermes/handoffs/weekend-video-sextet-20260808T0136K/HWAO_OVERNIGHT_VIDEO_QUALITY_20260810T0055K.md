# HWAO ORDER — overnight autonomous video-quality track

Stamped 2026-08-10 00:55 KST. Duho: *"work on improving video quality overnight autonomously."* Duho is
asleep; no question reaches him until morning. **Anything that needs his decision is not tonight's
work.**

## What is explicitly NOT in scope tonight

**The why-study intro rollout to the four siblings stays HELD.** Duho said "validate spin first,
hold the four," and the validation he meant is his own watch. Tori's presentation PASS on spin is a
crew validation, not his. I am not converting one into the other while he sleeps. Lana's motivation
packets for all four are complete and waiting; the moment he accepts the spin intro this becomes
minutes of work, not hours.

Also out: new claims, source freezes, result assertions, anything public.

## What IS in scope — craft, on artifacts that already exist

Every one of these improves the videos without asserting anything new. All five lanes:
spin `4d230cc0`, fesc `01a4249b`, brightend `c772e643`, mzr-anchor `c892f3fa`, mzr-census
`d6014ac0`.

1. **Cross-lane consistency.** Five videos should read as one series. Nobody has audited this.
   Headers, rails, banner language, colour semantics, card grammar, section naming, end cards.
   Where lanes diverge, decide which is right and say so — do not just list differences.
2. **Audio.** Loudness is already inconsistent across lanes (fesc −20.2 LUFS, mzr-anchor −20.9).
   Levels, inter-sentence gaps, breaths, clipping, drift. One target, applied everywhere.
3. **Pacing.** Dwell time per card against actual reading time — a card a viewer cannot finish
   reading is a defect even if the narration fits. WPM consistency (spin 115, fesc 113.5). Dead
   air. Rushed seams.
4. **Legibility at scale.** Font sizes at 1080p on a laptop, contrast, overflow, crowding, and
   text/graphic collisions — one was found in fesc today and fixed; sweep for the rest.
5. **Motion.** Is each animation carrying meaning or decorating? Jank, max near-unchanged run,
   transitions that hide rather than reveal structure.

## Roles

- **Goru** — mechanical sweep of 1, 3, 5 across all five: counts, durations, dwell-vs-reading-time,
  runs, per-lane divergence tables.
- **Kun** — adversarial on 2 and 4, plus the guardrail check he still owes on spin's **encoded**
  candidate against his six stop conditions. Attack the watching experience: where does a viewer
  lose the thread, mishear a word, or fail to finish a card?
- **Lana** — do not open new science. Check only that no quality change alters meaning: a reworded
  heading, a retimed card or a trimmed sentence can move a claim boundary.
- **Yui** — sole writer. **The V5 receipt correction first** (`raw_frames_submitted=6727` vs
  `encoded_video_frames=6726`, no re-encode, MP4 byte-identical). Then quality fixes as new
  versioned candidates only. **Never overwrite an accepted or passing candidate.**
- **Tori** — custody and exact-hash regates per new candidate; keep the five current cockpit links
  live and untouched.

## Standing rules

Fail-closed is still success. A defect described precisely beats a defect fixed carelessly at
3 a.m. No upload, publication, public/frontend, cockpit replacement, `published.json` change, DB,
deploy, Git, billing/provider/config or secrets. No `accepted_by_duho` — that label is Duho's alone
and no overnight verdict creates it.

**Announce gate overrides at the moment of acting.** Today an authorized cockpit copy read as an
intrusion to the auditing seat because I disclosed it late.

Hwao wakes on a schedule to steer, and reports **major items only** in the morning: verdicts,
blockers, decisions, failures. Not every round.
