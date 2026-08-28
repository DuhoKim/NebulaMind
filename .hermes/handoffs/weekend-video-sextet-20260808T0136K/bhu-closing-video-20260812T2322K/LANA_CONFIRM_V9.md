# Lana — V9 tight confirmation: repair landed; audit ruled sound; one timing repair before render

**Lana (science / claim-boundary seat), 2026-08-13.** Bound to exactly:

- `NARRATION_DRAFT_V9.md` — `85f111d366c5d11d912e4f7db5586f10b491b12b1c5091d3f94d822c388190b3`
- `STORYBOARD_DRAFT_V9.json` — `c9824b95453be7e67d6066f3810648dc8d588a8c3210546ec9caa5ee74710d7a`
- `CLAIM_LINE_LEDGER_V9.md` — `aa4b459a3b4112dc…` (byte-identical to V8 — verified, correct)

## VERDICT: **PASS WITH ONE TIMING REPAIR** — a single numeric field (card 04 `planned_seconds`).
Not a HOLD; a one-field delta. Everything else is confirmed for render.

## 1. My repair — confirmed landed, with intent

My own V8→V9 diff shows exactly one changed field in each channel: card 04's narration gains
"— called cosmological natural selection —" in sentence 1. The full name is spoken exactly once
(verified count), as the opening phrase of the card whose heading carries "CNS" — the in-breath
earning pattern V7 established and V8 accidentally broke. Nothing else moved: no other field, no
timing, no ledger byte. **The heading is re-earned as intended.**

## 2. The pacing check — and here my V8 certification was wrong, so V9 inherits a repair

Recomputing card 04: **99 narration tokens in 41 s = ~145 WPM needed**, against the render
contract's 120–135 band — and the true spoken count is slightly higher still, because em-dash
joins ("Sun—one") count as one token but two spoken words. **Disclosure: this violation did not
start with my five words.** V8's card 04 already required ~138 WPM; my V8 gate claimed "headroom on
every card" while I had only recomputed the total, not the per-card table — that was my error, and
my five words merely widened a breach I should have caught then. Left alone, this forces either
rushed TTS (damaging exactly the comprehension this rebuild bought) or a silent contract breach at
encode.

**Repair: card 04 `planned_seconds` 41 → 48** (≈103 spoken words at the 128 WPM design point;
46 is the floor at the 135 ceiling — do not go below it). Total runtime becomes ~399 s. One
storyboard numeric field; narration, claims, and every other card untouched. I also recommend the
encoded-audio QA (already contemplated by the render contract's "design at 128, then gate the
encoded audio") add an automated per-card WPM check, so this class of error is machine-caught
rather than seat-caught.

## 3. Ruling on the shorthand audit: **SOUND, and complete for this artifact**

`V9_SHORTHAND_AUDIT.json` is a genuine advance, and the reveal-timing constraint closes a hole none
of us had named — an initialism can be script-earned yet appear on screen before the words that
earn it. My checks:

- **Coverage — complete.** The three lexical initialisms (BHU, CNS, CW/CCW) are the full set; my
  independent sweeps across nine gates surface no fourth. The scientific-shorthand inventory
  (~, M☉, ≳, ±, the two percentages, ≠) matches every symbol that reaches a viewer, each mapped to
  its exact spoken witness. The nonviewer classifications (slug, G-IDs, contract metadata, diagram
  grammar) are correctly excluded. The video title carries no shorthand. Nothing is missing.
- **The constraint is the right rule, stated testably.** "Reveal no earlier than the witness
  phrase" plus the closing render-gate line ("Encoded-frame/audio QA must prove each first-use
  label is revealed no earlier than its listed spoken witness") turns earning from a script
  property into a **frame-verifiable render property**. That is the same move as the card-05
  no-terminus rule, applied to vocabulary, and it should be kept as a standing pattern for future
  videos.
- **The one nuance, affirmed rather than flagged:** the CNS entry allows the heading to remain
  visible from card start while the witness is the card's opening spoken phrase. That is a gap of
  at most ~3 seconds and matches the in-breath standard this chain has applied since V7 (and the
  identical treatment card 04's on-screen M☉ labels received). Consistent, not a defect.
- **Card-05 constraints retained** inside the audit's percentage entry ("retain every no-terminus
  constraint") — the two hard rules compose rather than compete.

## 4. Scope of the release

With the §2 field set to 46–48 s (48 recommended), my seat releases render on the resulting bytes
after a single-field delta check (hashes to me, same-day; the check verifies one number and that
nothing else moved). All V8 certifications carry: boundary strength, referent chain, comprehension
gains, zero seat names, zero banned strings, no-terminus rules, reveal-timing constraints now
added. No audio, no render, no upload before that delta and the other two seats' passes; Duho
decides on the finished artifact.

— Lana, 2026-08-13.
