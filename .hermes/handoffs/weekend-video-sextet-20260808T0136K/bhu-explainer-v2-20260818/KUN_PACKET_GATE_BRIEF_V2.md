# KUN — v2 packet gate brief

Read `SEXTET_BRIEF_V2.md` first. Gate the v2 explainer packet in THIS directory: `SCRIPT.md`,
`STORYBOARD.json`, `CLAIM_LEDGER.md` (+ `DEFINITIONAL_SOURCES.md` if present), `VISUALS.md`.
Reference precedent: your v1 gate `../bhu-neutron-star-explainer-20260817/KUN_PACKET_GATE_20260818.md`.

Deliverable: `KUN_PACKET_GATE_V2.md` in this directory. First line exactly
`PASS_EXPLAINER_PACKET` on pass; otherwise a HOLD token plus the complete, numbered repair list
(the whole list — a partially-relayed repair list has already cost this crew once).

## What to verify, minimum

1. **Ledger completeness**: every factual sentence in SCRIPT.md has a row; no FLAG survives;
   framing rows genuinely assert nothing.
2. **Source truth**: spot-check MAPPED rows against A/P/L/D at the cited lines — especially the
   new CNS-mechanism sentences against P 259–278 (direction: CNS's stated consequence is the low
   ceiling), the five-programmes claim, the 1972 claim, and every number (1.5, 2.00, 2.08 ± 0.07,
   68.3/95.4, 1.599/1.290 ± 0.008, 19.3 ± 0.7, 4%, 2020, 2026).
3. **Hash pins**: P equals `b244ea0a…`; D-row local copies match their recorded SHA-256.
4. **Must-not-say sweep**: no "BHU is falsified", no "Smolin refuted", no "we measured/
   discovered", no 2.35-M⊙ star, no invented mechanism for the 4% rule.
5. **Script/storyboard identity**: narration byte-identical between SCRIPT.md and
   STORYBOARD.json; headings match; word counts and `narration_sha256` correct; panel 01 ≤ 72
   words; total ≤ 730; planned_total_seconds ≤ 355; authorization block all false.
6. **Structure contract**: verdict complete in panel 01; assertion headings everywhere; ends on
   the verdict; no divider cards.
7. **Comprehension check (new for v2, Duho's direction)**: state plainly whether a viewer with
   no physics background could answer, from the script alone: what is the BHU idea; what does
   CNS claim; why do neutron stars test it; what happened. If not, that is a HOLD.

Findings-only: you never edit lane artifacts. Every finding carries quote + file + line. Write
only your verdict file into this lane directory. No fetches; `portal.nersc.gov` untouched.
