# Hwao — Deepening Gate 2 Dispatch Receipt

- Marker: `OVERNIGHT_PAPER_BOARD_HWAO_DEEPENING_GATE2_DISPATCH_RECEIPT_V1`
- Parent approval: `OVERNIGHT_PAPER_BOARD_EXECUTION_APPROVED_20260726T133216Z`
- Authored by Hwao/Fable at Deepening Gate 2 (machine-authored coordination artifact; not human gold). No memory/config written this gate. No source / current-Lab / PDF-replacement / public / DB / wiki / git / cron / browser / account / deploy / PAYG byte changed.

## Inputs read this gate (read-only)
- Lana C2 red-team: `packets/C-candidate-build/lana-c2-redteam/SCIENCE_REDTEAM_REVIEW.md` + `reviews/lana/LANA_C2_REDTEAM_RECEIPT.md` — **PASS** (BLOCKER 0 / MAJOR 0 / MINOR 4 / OK 7); candidate byte-unchanged.
- Kun C2 audit: `packets/C-candidate-build/kun-c2-audit/C2_CONTRACT_AUDIT.md` + `reviews/kun/KUN_C2_AUDIT_RECEIPT.md` — **PASS** on all six items; no FAIL; no candidate edits.
- Goru public mapping: `publication/goru-target-mapping/PUBLIC_TARGET_MAP.md` + `publication/GORU_PUBLIC_TARGET_MAPPING_RECEIPT.md` — served target **dynamic from `lab-runs/`**; read-only.

## Adjudication issued (`HWAO_C2_REDTEAM_ADJUDICATION.md`)
- V1 is **mechanically PASS and representation-PASS** as an isolated, unpublished AI research-note draft, but **NOT READY FOR PUBLIC PROMOTION** until **F1 + F3** are fixed. **F2 + F4 also to be fixed** in V2 (cheap honesty/representation hardening).
- **Dynamic current-Lab replacement = HIGH-RISK, NOT authorized this gate.** A C2 promotion would replace `lab-runs/gated-e2e-demo/draft.pdf` (`0d863bff…`) + `draft.tex` (`f1aeadd8…`) and edit `gated-e2e-demo.json` — i.e. mutate an immutable baseline INPUT run. Requires the later exact publish packet (backup, before/after + hashes, rollback, label-survival, SHA+HTTP smoke test, exact `APPROVE PUBLISH <packet_id>`). Open question flagged to that packet: prefer a **new run id / distinct served target** over overwriting a baseline input — Hwao provisional recommendation is NOT to overwrite the immutable input.

## Lane dispatched this gate (Tori will dispatch; Hwao does not self-start lanes)
1. **C2 V2 repair — `packets/C-candidate-build/LANA_C2_V2_REPAIR_BRIEF.md`** (Lana, **direct Claude subscription**).
   - Build a NEW versioned `c2-mzr-gated-e2e-candidate-v2/` applying F1 (soften Result → descriptive + see Caveats), F2 (qualify/remove "reproducible"), F3 (surface scale-limited/TENSION/anchor at Abstract + figure-caption), F4 (visible "AI-assembled draft — not submitted, not peer-reviewed" near title/abstract).
   - Retain all source numbers/refs, the citation split, and the O/H/TENSION/provenance caveats; copy figure byte-identically; compile root-local with saved tectonic rc. **No V1 / source / current-Lab / public edits.**
   - Receipt `reviews/lana/LANA_C2_V2_RECEIPT.md`; marker `OVERNIGHT_PAPER_BOARD_PACKET_C2_LANA_V2_COMPLETE_V1`.

Active helper lanes: one (Lana C2 V2). The Kun audit and Goru mapping lanes are complete.

## Preservation & public status
All writes this gate are NEW files under the approved output root (the adjudication, the V2 repair brief, this receipt). All prior files preserved — V1 candidate frozen (`candidate.tex c615b2f3…`, `candidate.pdf eed8992d…`); no overwrite/delete. **Public status: `AWAITING_EXPLICIT_PUBLISH_APPROVAL`** — no candidate crossed a public-write gate; no `lab-runs` artifact was touched. Promotion still requires a separate candidate-specific packet + exact `APPROVE PUBLISH <packet_id>` phrase.

## Status
This gate: **DONE** — C2 adjudication + V2 repair brief + this dispatch receipt written under the approved output root; markers/roots verified; V1 and all prior files preserved. Handing to Tori for visible dispatch of the Lana C2 V2 repair.

`OVERNIGHT_PAPER_BOARD_HWAO_DEEPENING_GATE2_DISPATCH_RECEIPT_V1`
