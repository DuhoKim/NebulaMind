# PACKET ASSEMBLED — handed to Codex for presentation (2026-09-07 18:35 KST). **NOT ADOPTED.**
The deterministic assembler (`scripts/assemble_adoption_packet.py`) exits 0 for the first time today. Every governing artefact now has an ACCESS-PROVED POSITIVE review of its CURRENT bytes:
| artefact | digest | verdict |
|---|---|---|
| candidate A1 | `2c8f31828fa13de790e891bcf2da3091d55b2567cb4436beb74f519d81ebeac9` | CANDIDATE-SOUND — `AGY_A1_REVIEW9_20260907.md` |
| run path | `f5100a046ba63c9e043e7ff67ef6e01e7621fe12eaa1097ac68a0fd96b5ffeec` | FINAL-SOUND — `AGY_A1_REVIEW6_20260907.md` |
| decision sheet | `c37ff259a19bdaecf3b02f3355aeb76bfaa09a6dcd591306fe71b376ce17494f` | SHEET-SOUND — `AGY_A1_REVIEW8_20260907.md` |
Reviewer throughout: **agy / Gemini** — a different engine from the Codex authors, which wrote none of this. Nine passes: v1 REFUSED · v2 delta SOUND · v3 delta NOT-SOUND (2 FATALs) · v4 repair SOUND · v5 FINAL-NOT-SOUND (2 FATALs) · v6 FINAL-SOUND · v7 CANDIDATE-NOT-SOUND (the sheet) · v8 SHEET-SOUND · v9 CANDIDATE-SOUND. Every negative verdict is retained; none was re-run to obtain a better one.

## WHAT IS TRUE, AND WHAT IS NOT
**Prepared and independently reviewed.** Readiness is TRUE and evidence-driven — it cannot be flipped by editing prose. All three preparation obligations are resolved. The disclosed limit stands in the sheet in plain words: the byte binding covers the on-disk cache copy, not the bytes the process holds in memory, so a custom loader or a post-load change could evade it.
**NOT adopted, not approved, not started.** Duho has decided nothing. No seed, round, anchor, selection, draw or holdout has occurred; the unseen evaluation data remain UNOPENED; drand-only stands and round 6440756 cannot seed this run. Assembly is not adoption, and this handoff is not a request for a ceremony: the approval medium is his ordinary conversational decision with Codex, bound to the exact presented version, with the agents recording the words, time, provider reference and digest.
**Presentation is Codex's step, not mine.** I am recording the packet and relaying it.

## WHAT THIS COST, WORTH KNOWING BEFORE THE NEXT ONE
Six of the day's defects were checks that never asked whether their own input set was complete — an aggregate gate reading part of a log; controls asserting "some refusal fired"; a table verification blind to codes it never enumerated; a readiness gate blind to a deleted obligation; a manifest too large to check; and my own assembler counting reviews without asking what they covered. Two more were mine at the level of design: a readiness predicate that parsed prose instead of evidence, and a record that said work was dispatched before it was. The pattern is one sentence long — **a check over a set must first establish what the set contains** — and it cost most of a day because it wears a different costume each time.
