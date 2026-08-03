# DR RESEARCH BATCH — 9 aas-autopilot papers, REFERENCE-ONLY

Duho authorized (2026-07-14): run the Deep Research research lane across all 9 aas-autopilot
manuscripts, producing sourced literature packets as REFERENCE artifacts.

## Prompts (submit each verbatim)
Directory: /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/dr-research-lane-9-20260714/prompts/
Files: paper_01_*.md ... paper_09_*.md (one DR prompt per paper).

## Task for Tori + Goru — sequential batch of 9 DR runs
For EACH paper prompt, in order 01..09:
1. Submit the prompt VERBATIM to Deep Research on the signed-in Pro Chrome (page-scoped preflight).
2. POLL to a terminal state (research complete, result text stable) before judging.
3. SAVE the full sourced packet as a REFERENCE artifact to:
   /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/dr-research-lane-9-20260714/packets/paper_NN_<shortname>_dr_packet.md
   and a metadata json alongside. Mark it advisory_only=true.
4. VERIFY the save, THEN delete ONLY that run's own Gemini conversation (history hygiene), log it.
5. Report that paper to Hwao, then proceed to the next.
After all 9: write a batch summary receipt (papers done, sources per packet, any that failed/STOPped).

## REFERENCE-ONLY — hard boundaries
- These packets are REFERENCE for the existing aas-autopilot workflow. Do NOT edit any .tex,
  do NOT touch the DB, do NOT modify or replace any autopilot lane, do NOT auto-apply anything.
- Rails unchanged: real page challenge = STOP+freeze; serialized submit via broker account lease;
  no credentials/secrets; fail closed on target drift; if you cannot positively identify a run's
  own conversation, do NOT delete.
- Serialized: one DR run at a time (account-submission lease). Flow may run concurrently on the
  Studio; the broker serializes the submit moments.
- If any single paper STOPs/fails, log it and CONTINUE to the next (don't abort the whole batch);
  report the failure in the batch summary.

DR_RESEARCH_BATCH_9_REFERENCE_20260714
