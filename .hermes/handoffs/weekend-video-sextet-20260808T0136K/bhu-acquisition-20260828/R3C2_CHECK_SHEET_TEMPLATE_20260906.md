# R3C2 reproduction census — one-page human check sheet (TEMPLATE, written 2026-09-06 before any run; fill only from receipts)

Duho's rule (2026-09-03, "both"): a result is more than an annotation only with a one-page human check sheet AND a blind second route.
This sheet is filled after the census runs, from printed artefacts only; every box names the file it was read from. Blanks stay blank.

| # | Question a human can check in five minutes | Where to look | Answer |
|---|---|---|---|
| 1 | Which bytes ran? Master digest at freeze = digest Duho signed = digest in every seat's ACCESS_SHA line? | `R3C2_V23_SIGNABLE_20260906.md`; Duho's chat words; first line of each `SEAT_REPORT.md` | ☐ |
| 2 | Did both seats see only the packet? Packet digest in each report = pin file; path lists carry no OUT_OF_SCOPE row | `R3C2_SEAT_PACKET.sha256`; each report's path list | ☐ |
| 3 | Receipt P exists BEFORE limb A began (protocol hash + commit id, Blanc's timestamp) | Blanc's receipt P; run log line for limb A start | ☐ |
| 4 | Denominator: both seats' candidate counts agree; `census` PASS in both; exclusions all carry a kind | both `candidates.json` / `exclusions.json`; printed `census` runs | ☐ ___ / ___ claims |
| 5 | Inputs: `validate` PASS in both seats; every input carries a machine-matched quotation for its origin | printed `validate` runs (C3 artefact) | ☐ |
| 6 | Outcomes: final `census … final` PASS; no PENDING; every arithmetic outcome carries both numbers | printed final census runs | ☐ |
| 7 | Any seat disagreement? Denominator / input list / outcome / origin — which class filed, or none survived reconciliation | merge output; §4 filing | ☐ class: ______ |
| 8 | Controls: C5 harness live in both; C5b path lists classified; no control passed by assertion | seat reports | ☐ |
| 9 | Receipt T exists AFTER the tally commit and BEFORE the protocol opened; the receipt names every file in that commit | Blanc's receipt T; commit id | ☐ |
| 10 | C6 audit: seed supplied after receipt T; `C6_AUDIT.json` printed; MISMATCH count = 0 | `C6_AUDIT.json` | ☐ mismatches: ___ |
| 11 | The tally in one line: __ included claims; __ WITHIN_STATED_PRECISION; __ FAILED; __ non-arithmetic (by kind) | merged candidate file | ☐ |
| 12 | Study-level class filed, by name, and the sentence of §4 it satisfies | filing note | ☐ ______ |
| 13 | Interpretation: the protocol (V4) was opened only after receipt T; the mapping line quoted verbatim; Blanc re-hashed both artefacts | interpretation report | ☐ |
| 14 | Blind second route: the lane's sealed pre-run route exists and its digest predates limb A | run log; sealed file digest | ☐ |
| 15 | Negatives worded "unreproduced from the stated inputs" everywhere in the filing; no paper called wrong | filing text | ☐ |

**What this sheet cannot check:** whether an origin classification is semantically right (the human floor: two seats + the auditor),
and whether Tori had guessed the answer (the seal bounds the record, not the mind). Both are stated in the prereg.

**Signature line for the checker (plain words in chat, no ceremony):** "R3C2 check sheet: __ of 15 boxes ticked; rows ___ not ticked because ___."
