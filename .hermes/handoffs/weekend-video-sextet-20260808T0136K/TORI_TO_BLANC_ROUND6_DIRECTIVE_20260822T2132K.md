# Tori → Blanc: Duho's order — round six, using the gate's method

*Tori, 2026-08-22 21:32 KST*

Duho, verbatim: *"tell blanc to run round six with the gate's method."* Relaying with the method
spelled out so you do not have to mine the 252-line verdict for it.

## The method, from the gate's own §4

1. Tokenize **all** captions — the whole corpus, not the backfills. The gate's confirmed residuals
   include 08-19 whisper-1-era readings (`Blonk`, `Huao`), so the base.en population model is too
   narrow and round six's scope must be all 223.
2. Check tokens against a wordlist (it used `/usr/share/dict/words`) with only mechanical
   inflection/possessive/hyphen normalization — **no glossary of known bad forms**. That inversion
   is the whole point: hunt what is not a word, not what you already know went wrong.
3. Attack four families: OOV tokens near the crew/author/term list; malformed merges inside
   otherwise grammatical sentences; capitalized tokens whose nearby context names the intended
   referent; and the outputs between each backup stage and the next.
4. Reject ordinary acronyms, valid technical terms, and transparent compounds **by reading**, not
   by list — the gate turned 429 raw OOV types into a short confirmed set that way.

## Your head start

The verdict's §4 already lists every promoted candidate family **with context** — round six can
begin from that list rather than from zero. Confirmed and spot-verified by me: `GemIIni`
(inside my whisper-1 replacement of gemini-dr-verdict), `Blonk`/`Blunk`, `CUN`/`CUNS`, `Goryu`,
`Huao`. Borderline candidates the gate left under your floor caveat are listed separately — they
are findings to read, not repairs to apply.

## Discipline, unchanged

Evidence class on every repair, originals to `.pre-round6`, ledger events per change, and —
the gate's lesson — **no completeness claim at the end.** Say what the method covered; let the
next adversary find its edge. If you want a standing residual scan afterwards, this method is the
one that survived contact; the known-forms scan is the one that missed bare Coon 31 times.

## Still queued from the HOLD, separate from round six

The four drafted `caption_corrected` events for my whisper-1 replacements (in
`TORI_TO_BLANC_CGATE_HOLD_20260822T2129K.md`), and the stale base.en sidecars on those files.
Clearing F1 is those events; clearing F2 is round six. Both together reopen the gate.
