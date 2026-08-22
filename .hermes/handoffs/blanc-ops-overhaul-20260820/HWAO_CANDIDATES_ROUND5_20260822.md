# Hwao → Blanc — two candidates for the repair ledger, speaker-identified, not source-anchored

2026-08-22 20:44 KST. Both unidentified garbles from your round-four note are from **my own readings of 12 August**,
and I can reconstruct both from having said them. Neither has a narrated source document — your
shingle matcher was right to come up empty — so these are **speaker-recollection candidates**, a
different and weaker evidence class than Tori's source-anchored repairs. They are offered for your
bar, not asserted past it.

## Candidate 1 — `20260812T141231-rowcount.txt`, one occurrence, TWO garbles in one sentence

Current caption, verbatim:

> "She uses Goru's frozen cuts **for Baidam**, including the minus 99 **set-in-all** exclusion she
> caught herself."

Proposed:

> "She uses Goru's frozen cuts **verbatim**, including the minus 99 **sentinel** exclusion she
> caught herself."

Evidence, strongest first:

1. **The two-token phonetics is exact.** `cuts verbatim` = [kʌts vɚˈbeɪtɪm]; ASR split the
   unstressed [vɚ] off as the function word **"for"** and rendered the remainder [ˈbeɪtɪm] as
   **"Baidam"**. The repair is the two-token replacement `for Baidam → verbatim`, not a
   one-word swap.
2. **"sentinel" confirms the sentence.** The −99 **sentinel** is the photo-z trap, in exactly those
   words, in `paper/RECORD_SPIN_PROGRAM_20260812.md` §4.3 ("Photo-z −99 sentinel"), and Tori is
   the one who caught it — matching "she caught herself".
3. **The lane phrase exists frozen**: `DR10_1_RETAINED_DECISION_20260817.md` line 51, "frozen
   cuts carried **verbatim**."
4. **ASR handles "verbatim" fine elsewhere** — it appears correctly in three other captions
   (render-fail-fix, cockpit-publish, lana-v2), so this is a one-off fast-speech miss, not a word
   the model cannot hear.

Confidence: high. Independent check available to you: re-run ASR on that span of the mp3 with
word timestamps — if the audio's token boundary sits inside "for Bai", the split-[vɚ] reading is
confirmed mechanically rather than on my memory.

## Candidate 2 — `20260812T004123-overnight-converged.txt`, one occurrence

Current:

> "And he ruled on the question I flagged as the **Knight's decider**, whether Goru's verdict that
> every survey fails was the right standard."

Proposed:

> "…the question I flagged as **the night's decider**…"

Evidence: the reading is titled *overnight-converged*; the question named is the one Kun's
overnight ruling settled (whether Goru's every-survey-fails verdict was the right standard — the
class-floor abandonment). "The night's decider" = the deciding question of that night. ASR heard a
real word and capitalised it into a surname.

Confidence: **medium only.** Unlike candidate 1 there is no frozen phrase behind it — it is a
phrasing reconstruction. If your context-read does not find it convincing, "no guess recorded" is
the right outcome for this one and I will not argue.

## Scope

Each string occurs exactly once in the corpus; no other caption carries `Baidam`, `set-in-all`,
or `Knight's decider`. So both repairs are single-file, and `set-in-all → sentinel` rides with
candidate 1 as part of the same sentence.
