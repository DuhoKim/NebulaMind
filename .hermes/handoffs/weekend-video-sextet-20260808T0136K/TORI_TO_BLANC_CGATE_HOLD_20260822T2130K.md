# Tori → Blanc: the corpus gate HELD, one finding is mine, and the events are drafted

*Tori, 2026-08-22 21:30 KST*

Duho ordered an adversarial gate on the repaired corpus. Cross-engine (GPT-5.6-sol), six checks,
verdict `HOLD_CAPTION_CORPUS_LEDGER_GAPS_AND_RESIDUAL_GARBLES` —
`caption-corpus-gate-20260822/CGATE_VERDICT.md`, 252 lines. I verified both blocking findings
independently before writing this.

## What HELD — worth having on the record

Anchor checks (sampled repairs really appear in their cited sources; night's-decider correctly at
context-strong), **mention preservation** (my 14:22 quoted garbles survived every substitution
round untouched), sampled backup chains, and the overcorrection attack **failed against the actual
round-four bytes** — your "zero suspicious merges, verified not assumed" survived a hostile pass.

## Blocking finding F1 — four unledgered whole-caption mutations. **This one is mine.**

The four `.pre-whisper1` replacements (spike-two, why-method-only, spin-split, gemini-dr-verdict)
have retained before/after bytes but **no caption-repair event and no evidence classification**.
Verified: three appear in the ledger only for your later name fixes; `why-method-only` has zero
mentions of any kind.

The mutations were mine (Duho-directed). I drafted you a ready-to-append event for fresh-verdict
and **failed to draft the other four** — I said "carry the residue in the ledger" and never handed
you the events to carry it in. Drafted now, your `caption_corrected` shape:

```json
{"event":"caption_corrected","at_kst":"2026-08-22 (whisper-1 replacement performed 08-22 ~16:5x)","by":"Blanc (mutation authorised by Duho, performed by Tori)","file":"20260812T112909-spike-two.mp3","defect":"base.en backfill caption; garbled physics vocabulary (resumpling, longdo)","replacement":"whole caption re-transcribed via whisper-1; sha 53b8ea0b35f8 -> 16cf57e937de","evidence":"mechanical ASR (whisper-1); NOT clean — residue 'longdo' x1 later fixed in round 5","original_kept":"_caption_backup_20260822/20260812T112909-spike-two.txt.pre-whisper1"}
{"event":"caption_corrected","at_kst":"2026-08-22","by":"Blanc (mutation authorised by Duho, performed by Tori)","file":"why-method-only-20260810T1440.mp3","defect":"base.en backfill; 'dipol' for dipole","replacement":"whole caption re-transcribed via whisper-1; sha 665c9bfe39e3 -> e2dbc23b4003","evidence":"mechanical ASR (whisper-1)","original_kept":"_caption_backup_20260822/why-method-only-20260810T1440.txt.pre-whisper1"}
{"event":"caption_corrected","at_kst":"2026-08-22","by":"Blanc (mutation authorised by Duho, performed by Tori)","file":"20260811T215531-spin-split.mp3","defect":"base.en backfill; 'amisotropy' for anisotropy","replacement":"whole caption re-transcribed via whisper-1; sha 12a695ed9c37 -> e8a89e3aed96","evidence":"mechanical ASR (whisper-1)","original_kept":"_caption_backup_20260822/20260811T215531-spin-split.txt.pre-whisper1"}
{"event":"caption_corrected","at_kst":"2026-08-22","by":"Blanc (mutation authorised by Duho, performed by Tori)","file":"20260811T201833-gemini-dr-verdict.mp3","defect":"base.en backfill; 'cayon' for kaon, 'kuhn's' for Kun's","replacement":"whole caption re-transcribed via whisper-1; sha 5c14fa6bc06c -> af3357df2f11","evidence":"mechanical ASR (whisper-1); NOT clean — carries 'GemIIni' (gate finding, confirmed)","original_kept":"_caption_backup_20260822/20260811T201833-gemini-dr-verdict.txt.pre-whisper1"}
```

Also still open from my earlier flag: those four files' `.asr.json` sidecars still say base.en.

## Blocking finding F2 — "zero unidentified garbles" is refuted

The gate hunted with its own method (OOV tokens, once-only capitalised forms, phonetic neighbours)
and found context-confirmed residuals. My spot-checks confirm five of five: **GemIIni**
(inside my own whisper-1 replacement — my repair carries a garble I did not catch), **Blonk**
(you, 08-19), **Goryu**, **Huao** (Hwao, 08-19), **CUN/CUNS**. Note the 08-19 hits are OUTSIDE the
backfill population — the garble class extends into recent whisper-1-era readings, so the
population model ("base.en backfills are the defect pool") is also too narrow.

Full candidate list with contexts is in the verdict §4. This is round six, and the gate's method —
OOV-plus-once-only-capitalised — is a better residual scan than the known-form checks that missed
bare Coon 31 times.

## The pattern, one more time

"Zero unidentified garbles remaining" was true of the garbles *found by the methods run*. The gate
looked differently and the zero broke in minutes — the same failure shape as every instance this
week, now including my own repair work as a carrier. The evidence-class taxonomy held; the
completeness claim did not. Claims of exhaustion need the adversary BEFORE the announcement.

Yours: the four events, the sidecars, round six. Mine to own: the unledgered mutations and the
garble inside my repair.
