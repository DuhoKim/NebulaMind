# Adoptions from hellices/harness-workshop (reviewed 2026-08-25)

Duho pointed at https://github.com/hellices/harness-workshop — a Korean
harness-engineering workshop for agent-assisted astronomy. Much of it converges
on lessons we paid 21 gates for ("do not complete without new evidence",
"humans decide next action"), which is validation, not adoption. Three things
we do NOT already have:

## 1. Academic gates for external-data results → the successor prereg
A fixed checklist wherever results come from archives/MCP/literature:
- preserve bibcodes, DOIs, publication status of every cited result
- record coordinate system, equinox, search radius for every catalog query
- log data release and observation dates
- archive the exact ADQL/TAP queries incl. row limits
- pin notebook versions, random seeds, input checksums
- reconstruct any MCP/natural-language tool output as a reproducible script;
  "natural-language MCP responses are never paper evidence"
Our byte custody (digests, receipts, append-only ledgers) is stronger than his;
our literature/citation side has no equivalent standard. Owner: successor
prereg (Hwao), citation binding (Tori).

## 2. One-change-per-iteration, as explicit gate-loop discipline
"Change one element per iteration; if multiple must change together, document
the hypothesis and combination rationale." The v8 refutation (parser
withdrawal inserted without deleting superseded prose — every claim defined
twice) was this rule being violated. Adopt verbatim for any gated revision.

## 3. Close the loop on instruction changes
His outer loop ends: re-run a comparable range, then adopt / supplement /
revert. We write memory files and handoff rules but never verify they changed
behavior. Adoption: when a memory/instruction is added after a failure, name
the observable that should differ, and check it on the next comparable run.

Not adopted: his skill pairings and MCP scaffolding (we have our own), and
nothing in his material covers adversarial gating or append-only custody —
ours is ahead there.
