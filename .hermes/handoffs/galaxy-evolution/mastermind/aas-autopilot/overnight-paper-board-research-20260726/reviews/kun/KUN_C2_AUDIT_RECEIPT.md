# Kun C2 Audit Receipt

Dispatch marker: OVERNIGHT_PAPER_BOARD_PACKET_C2_KUN_AUDIT_BRIEF_V1

## File Produced

| file | sha256 |
|---|---|
| packets/C-candidate-build/kun-c2-audit/C2_CONTRACT_AUDIT.md | e7452b728e555eae73b5f80af66c8b536b5377ac4993341e5317d7139df66252 |

Receipt file SHA-256 is not self-listed because the receipt content would change its own hash.

## PASS/FAIL Summary

| audit item | result |
|---|---|
| Source diff | PASS |
| Hash / figure identity | PASS |
| PDF-text extraction | PASS |
| Claim surface | PASS |
| Reference integrity | PASS |
| Receipt-contract concordance | PASS |

## Discrepancies

None. No FAIL discrepancies found.

## Key Evidence

- Source drift check passed for `gated-e2e-demo/draft.tex`, `gated-e2e-demo.json`, and `gated-e2e-demo/result.png`.
- Unified source-to-candidate diff has exactly 3 hunks: non-rendered header comments, Introduction connective split, and append-only Caveats additions.
- Recomputed hashes match expected values: `candidate.tex` = `c615b2f39502bf4e15f54e8fba3818ca480c9fd162360044c804893a11bc00d9`; `candidate.pdf` = `eed8992dbcfd2a23abc5e459dddbd2660a9add3607e9f34035df9115ac26b98e`; C2 `result.png` = source `result.png` = `ed83a8250b4a7a2ba969751f3519253f7a2e386080de239bd06e66baa9f82639`.
- `pdftotext` output shows the O/H-scale caveat, TENSION caveat, provenance caveat, and rendered `AI_DRAFT_NOT_HUMAN_GOLD` token.
- Reference-block diff is empty; all five entries including `LaraLopez2013` are preserved.
- Compile evidence supports rc=0 and PDF creation; only underfull-box warnings were found.

## Attestation

No candidate edits made. No source edits made. No recompile performed. No runner/data pull, public/static-root write, DB/SQL/API/wiki/page-version write, deploy/restart, git action, cron/browser/account/billing/cloud action, or PAYG/Nous route occurred.

## STOP Notes

None triggered.

## Completion State

DONE

OVERNIGHT_PAPER_BOARD_PACKET_C2_KUN_AUDIT_COMPLETE_V1
