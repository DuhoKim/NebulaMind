# Sextet review briefs — spin presentation overhaul

Read `HWAO_OVERHAUL_ORDER.md` and `USER_DIRECTION_OVERHAUL_20260808T1258K.md` first.

**Before writing anything, look at what was rejected.** Not the brief — the artefact:

**PRIMARY — the exact file Duho was linked to and rejected** (provenance corrected 13:25 KST, see
`reviews/TORI_USER_WATCHED_ARTIFACT_CORRECTION.md`; SHA-256 `2b1db497…` re-verified against disk by
Hwao, 114.0 s, 1,943,640 B, video-only):

- `integrator/canaries/spin-method-canary-20260808T0204/spin-method-canary-20260808T0204.mp4`
- `integrator/canaries/spin-method-canary-20260808T0204/contact-sheet.jpg`

**SUPPLEMENTAL only — NOT the watched file:**

- `integrator/canaries/spin-method-canary-20260808T0648/` — a later iteration on the same 11-card
  skeleton (only card 05 was reworked). Useful as evidence that nine refinements never escaped the
  template; it must not be described as what Duho watched.

**If your packet was already written from 0648 alone, inspect 0204 and append a clearly labelled
amendment.** Do not silently restate — the diagnosis happens to survive, but the record must show
which artefact each judgement came from.

Duho watched that and said: *"still without audio, it looks almost same as before. i want you to
overhaul the video leveraging sextet making more scientific presentation."* Nine iterations polished
that grammar and none escaped it. If your review could equally have been written about v9, it has
not engaged with the rejection.

Write your own packet, independently. **Do not read another seat's packet before writing yours**, and
do not soften a disagreement to match. Independent packets are preserved before integration.

---

## LANA — scientific narrative and claim boundary → `reviews/LANA_OVERHAUL.md`

Own the argument, not the pixels. Is there a *scientific* through-line a conference audience would
follow — question, why it is hard, how the design answers it, why the answer is withheld — or is it
still a list of true statements in sequence?

Specifically: does the one-sentence question earn the next 100 seconds? Does the mirroring argument
land as the intellectual core (a signal in the sky must flip when images are mirrored; one in the
classifiers need not)? Is the withheld result framed as a *result of discipline* rather than an
apology?

Hard boundary you enforce: **no T3/T4 numbers or figures, no significance, no dipole/parity/cosmology,
no GRB/SN Ia/DE/quasar/H0, no black-hole-universe, no new DESI/Ganalyzer claims.** The equation is
symbolic with **no value**. Flag any sentence that implies a result direction.

## GORU — mechanical timeline and label integrity → `reviews/GORU_OVERHAUL.md`

Count things; do not interpret them. Deliver a table: each visual state, its start/end, duration,
and whether it is *materially* distinct from its neighbour (a zoom is not a new state).

Check against the order: **≥7 materially distinct states**; **no unchanged state >~8 s**; **≥75% of
runtime** carrying source-grounded plots/diagrams/animated graphics. Report the actual percentage
and how you measured it.

Also: every count traceable to a lane artifact; units and axis labels present and correct; and
**no internal filename used as an audience citation** — `T1_FUNNEL.json` is not a citation, the
survey and release are.

## KUN — reproducibility, rendering, A/V sync → `reviews/KUN_OVERHAUL.md`

Adversarial. Assume the candidate is worse than it looks and try to prove it.

Verify from the encoded artefact, not the build log: audio stream **exists**, is intelligible, no
clipping; measured wpm inside **105–125**; every substantive sentence has a visual action starting
within **±0.3 s** of it — sample specific sentences and report timings, do not assert compliance.

Then: can the candidate be rebuilt from its recorded inputs to the same hashes? Are progressive
builds real animation or crossfades between stills? Name the weakest thing you find even if
everything else passes.

## TORI — source status, frame verification, gates → `reviews/TORI_OVERHAUL.md`

Verify against `lanes/spin/SOURCE_FREEZE.json` and `STATUS.json` as they stand now, including the
**audio-contract change** (narration authorized for method-only claims; reportability unchanged,
`video_reportable_now` still `false`).

Decode **actual frames** and confirm no forbidden content appears anywhere — including inside a
figure, an axis label, or a legend, where a scan of the storyboard text would miss it. Confirm every
closed gate held: nothing uploaded, no shared/public MP4 touched, no Git write, no deletion of a
prior attempt.

Record a private playback verification: it plays, audio is audible, nothing is truncated.

## YUI — representation design and the build → `integrator/canaries/<new-versioned-dir>/`

You are the only candidate writer. Build the seven required elements in the order's §4 as a
**conference-science** grammar, not cards with voice added: animated funnel with counts attached to
labelled stages; progressive equation construction that withholds the value; a real mirroring
animation with the label inversion, marked `CONCEPTUAL — illustration, not data` if generated; a
bias-control matrix showing what failure mode each control tests, design only; a review-gate
timeline explaining precisely why the result is absent; a closing boundary slide.

Synthesize **sentence-aligned** Alloy audio first, then derive visual action boundaries from the
**actual** audio durations. Full receipts. Preserve every rejected attempt.
