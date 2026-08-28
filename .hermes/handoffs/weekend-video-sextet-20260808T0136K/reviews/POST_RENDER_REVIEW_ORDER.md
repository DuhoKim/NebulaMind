# Post-render review order — Tori and Kun re-run their packets

Duho, 2026-08-08: *"have tori and kun redo their packets once it lands."*

Standing and binding. Recorded on disk so it survives session loss: if this coordinator drops, whoever
picks up must still enforce it.

## Trigger

A **stable** MP4 in `integrator/canaries/spin-method-overhaul-canary-*/` — byte size unchanged across
a ≥20 s re-check, so nobody reviews a file still being written. Hwao dispatches on that signal, after
checking each seat is idle. **No automated paste into a live agent pane**; a timed paste into a busy
composer is the hazard already fixed once in the sustainer.

## Why a re-run rather than an amendment

Both current packets were written against the **rejected baseline**, because that was all that
existed:

- `KUN_OVERHAUL.md` states plainly: *"No new spin overhaul canary is present for KUN acceptance yet."*
- `TORI_OVERHAUL.md` records encoded-frame, audio and private-playback rows as
  `PENDING_NEW_CANDIDATE`.

Both are honest, and neither is a verdict on the new candidate. **Preserve both**; append the new
pass as a clearly labelled second section. Do not overwrite a packet that correctly described a
different artefact.

## KUN — re-run, adversarially, from the encoded artefact

Everything in the KUN section of `REVIEW_BRIEFS.md` still applies. Specifically, on the new MP4:

1. **Audio exists and is real** — stream present, intelligible, no clipping. The previous script was
   discarded in the narrative correction, so the audio is newly synthesized: **re-measure delivered
   wpm from the actual encode** (target 105–125). Do not carry forward the 110.2 measured on the
   superseded master — that number belongs to a rejected attempt.
2. **A/V sync** — sample specific sentences and report real timings against the ±0.3 s requirement.
   Report measurements, not compliance claims.
3. **Progressive builds are genuine animation**, not crossfades between stills — the whole point of
   the overhaul.
4. **Reproducibility** — can the candidate be rebuilt from its recorded inputs to the same hashes?
5. Name the weakest thing found even if everything else passes.

## TORI — re-run source/gate verification against the encode

Everything in the TORI section still applies. Specifically:

1. **Decode actual frames.** Confirm no forbidden content anywhere — including inside a figure, axis
   label, or legend, where a storyboard text scan cannot see it. This is the check nothing else
   substitutes for.
2. Verify against `lanes/spin/SOURCE_FREEZE.json` and `STATUS.json` **as they stand at review time**,
   including the audio-contract change (narration authorized for method-only; `video_reportable_now`
   still `false`).
3. Confirm every closed gate held: nothing uploaded, no shared/public MP4 touched, no Git write, no
   prior attempt deleted.
4. **Private playback verification** — it plays, audio is audible, nothing truncated.
5. Re-verify the served bytes by hash if the file is exposed for Duho's watch, as was done for 0204.

## Both

Judge against the **corrected** requirements, not the original brief — `HWAO_NARRATIVE_CORRECTION.md`
added three: the mirror must be the **peak**, not merely early; the gates section must read as
discipline rather than a ticketing system; and the close must re-pose the opening question instead of
ending on workflow.

Independent packets. Do not read each other's before writing. Preserve disagreements.

A numeric-guard or machine-QA PASS is **not** semantic authorization — that error was made once
already tonight and corrected.
