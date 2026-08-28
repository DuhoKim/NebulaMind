# DISPATCH — Goru, Kun, Tori: catch up on lanes 1 and 2

Filed 2026-08-09 02:40 KST by the **Claude-macbook** seat (Directors board, pane %30), on Duho's
direct instruction in that pane: *"have goru, kun and tori catch up on both lanes."*

**Hwao retains coordination and the accept/hold decision.** This dispatch conveys Duho's instruction
and assembles the facts; it does not issue verdicts or reorder anyone's charge.

Lana has filed on both lanes already. Goru, Kun and Tori have filed on **neither**. Builds are two
lanes ahead of review, and lane 3 (`brightend`) is rendering now.

## The two candidates — bind these exact hashes

### Lane 1 — mzr-census
`integrator/canaries/mzr-census-method-overhaul-canary-20260809T0214K/mzr-census-method-overhaul-canary-20260809T0214K.mp4`
- SHA-256 `0496435a9488bd946f7453989e7b9c5f4a528a691e698acab6b1e0d56e064536`
- 9,421,699 B · 224.233 s · h264 + aac · `encoded_qa.json` **PASS 27/27**

**Review this hash only.** An earlier encode `d940a7e8…` HELD at 25/27 and was **superseded by a
re-render** at 02:26:40. The failing QA is preserved as `encoded_qa.HOLD1.json`, and prior attempts
sit in `rejected-attempts/`. Do not review `d940a7e8…` as the candidate.

### Lane 2 — fesc
`integrator/canaries/fesc-method-overhaul-canary-20260809T0227K/fesc-method-overhaul-canary-20260809T0227K.mp4`
- SHA-256 `b900383142c0ddeadc32247282f511798d8c4a449cbf5c7b7aef0a56aff4c168`
- 9,736,958 B · 236.739 s · h264 + aac · `encoded_qa.json` **PASS 27/27 on the first encode**

## Standing boundary — applies to both

Neither lane has a `SOURCE_FREEZE.json`. Per Tori's own baseline packet, **an absent freeze is not
authorization**: any rendered result, selected direction or sign, significance, claimed outcome, or
result-bearing figure/legend is HOLD. `video_reportable_now` is `false` for both.

Both specs declare lane-specific `forbidden_terms` beyond the standard four —
mzr-census: *(the standard four)*; fesc adds `closure crossing`, `shortfall survives`, `deficit rises`.

## What each seat owes, per its existing charge

### GORU — mechanical timeline, state uniqueness, units/labels/citations, graphics share
Both lanes. Specific to these candidates:
1. **Lane 1's static-hold history.** `no_eight_second_freeze` failed at **13.5 s** on the superseded
   encode and reads **0.0 s** after the re-render. Confirm that independently on `0496435a…` — it is
   the one defect that forced a rebuild tonight.
2. **Lane 2 carries Lana's soft watch-point**: the `CONCEPTUAL SWEEP` envelopes are drawn with a
   definite crossing *shape*. She judged it disarmed by on-frame `VALUES WITHHELD` / `NO ORDER OR
   CROSSING IS REPORTED`, not a breach. Geometry-versus-label is a visual-state question, so a second
   pair of eyes on it is yours.
3. Lane 2 renders **no numeric tokens at all** (`numeric_guard` evidence is empty, correctly — the
   spec contains no numbers). Whether a count-free funnel still satisfies the graphics grammar is
   worth your explicit call rather than silence.

### KUN — reproducibility, rendering implementation, audio/action sync, encoded-artifact checks
Both lanes. Specific to these candidates:
1. **Re-measure wpm from each encode.** Reported: lane 1 `115.0000` over 424 words / 224.2 s;
   lane 2 `115.0000` over 448 words / 236.7 s. Both are longer than spin's 187.7 s.
2. **The loudness threshold on lane 1 moved mid-run.** `loudness_in_target_band` flipped False→True at
   02:24:08 on an *unchanged* video hash with a byte-identical measurement (`input_i: -21.51`). The
   value is inside the band the accepted spin script defines (`-22 … -14`, `qa_encoded.py:317`), so
   the substance appears defensible — but it was not stamped. Detail in
   `FREEZE_INTEGRITY_CHECK_REQUEST_TORI.md` (amendment). Lane 2 measures `-21.48`.
3. **Reproducibility.** Neither candidate directory contains any `.py`; no script in the handoff tree
   references either candidate. If a deterministic rebuild is not possible, say so plainly rather
   than leaving the row untested — that gap went unrecorded on the spin lane.
4. Name the weakest thing found even if everything else passes.

### TORI — source/status receipt, actual-frame verification, gate enforcement, private playback
Both lanes. Specific to these candidates:
1. **Decode actual frames.** Only a pixel sweep can catch a result inside an axis, legend or
   annotation. Lane 1 is a mass-metallicity lane and lane 2 an f_esc lane — both have contested
   quantities a figure could leak.
2. Verify each lane's STATUS and freeze state **as they stand at review time** (both freezes absent).
3. Closed gates and prior-attempt preservation, including lane 1's `encoded_qa.HOLD1.json` and
   `rejected-attempts/`.
4. **Private playback — note the route changed.** Port **8766 was retired at 02:07 KST** on Duho's
   instruction (`TAILNET_8766_RETIRED_20260809T0207K.md`); do not assume it is up. Port 8765 currently
   serves the **spin** candidate only. Neither sibling has a live route, so a playback row needs one
   opened first.
5. Separately outstanding and **non-blocking**: `FREEZE_INTEGRITY_CHECK_REQUEST_TORI.md`, on whether
   a hand-authored freeze and a per-candidate QA threshold can detect drift at all.

## Seat state at dispatch, recorded honestly

| Seat | Pane | State at 02:40 KST |
|---|---|---|
| Goru | `%3` (`goru-agy`, Gemini 3.1 Pro) | shows an active task — may pick this up later than the others |
| Kun | `%25` (`kun-codex-overhaul`, gpt-5.5) | idle at prompt |
| Tori | `%23` (`tori-overhaul`, gpt-5.6-sol) | idle at prompt |

Dispatched by file. **Nothing was pasted into any pane.**

## Rules unchanged

Independent packets, append-only, preserve disagreements, do not read each other's before writing.
A machine-QA PASS is **not** semantic authorization — 27/27 is a starting point for review, not a
substitute for it. No gate reopens; `video_reportable_now` stays `false`; single-writer preserved.
