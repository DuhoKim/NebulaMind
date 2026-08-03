# Kun C2 V2 Audit Receipt

Dispatch marker: OVERNIGHT_PAPER_BOARD_PACKET_C2_KUN_V2_AUDIT_BRIEF_V1

## File Produced

| file | sha256 |
|---|---|
| packets/C-candidate-build/kun-c2-v2-audit/C2_V2_CONTRACT_AUDIT.md | 857fcce56722c1471cd5f051a3a4e16b3c043865af639831e7b47eab25dbdd44 |

Receipt file SHA-256 is not self-listed because the receipt content would change its own hash.

## PASS/FAIL Summary

| audit item | result |
|---|---|
| Hashes -- source/V1/V2 | PASS |
| V1-to-V2 diff limited to F1-F4 + header | PASS |
| Rendered PDF strings | PASS |
| Reference integrity | PASS |
| Citation split | PASS |
| Caveats | PASS |
| Figure byte-identity | PASS |
| Compile evidence | PASS |
| V2 receipt concordance | PASS |

## Discrepancies

None. No FAIL discrepancies found.

## Key Evidence

- Source baseline checks passed for `gated-e2e-demo/draft.tex`, `gated-e2e-demo.json`, and `gated-e2e-demo/result.png`.
- Frozen V1 hashes match: `candidate.tex c615b2f3...`, `candidate.pdf eed8992d...`, `result.png ed83a825...`.
- V2 hashes match Lana/Hwao values: `candidate.tex bb77d38d...`, `candidate.pdf ac59ac60...`, `result.png ed83a825...`, `COMPILE_NOTE 07456dc5...`, `V1_TO_V2_DIFF 7950cbf0...`.
- V1-to-V2 diff has one grouped hunk containing only the non-rendered header update plus rendered F1-F4 edits.
- `pdftotext` output shows F4 tag, F3 abstract flag, F3 caption note, F1 softened Result sentence, O/H-scale caveat, TENSION caveat, Provenance caveat, and rendered `AI_DRAFT_NOT_HUMAN_GOLD`.
- Rendered PDF text omits the old overclaim phrase `provides insights into the relationship` and omits `reproducible`.
- Reference-block diff is empty; all five references including `LaraLopez2013` are preserved.
- Compile note/logs support `rc=0` and PDF output with only underfull-box warnings.

## Attestation

No candidate, V1, V2, source, Lab artifact, PDF, public target, DB/wiki, git, cron, browser, account, deploy, runner, recompile, or PAYG edit/action was made.

## STOP Notes

None triggered.

## Completion State

DONE

OVERNIGHT_PAPER_BOARD_PACKET_C2_KUN_V2_AUDIT_COMPLETE_V1
