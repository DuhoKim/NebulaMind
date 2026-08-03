# Kun — C2 Mechanical Contract Audit Brief (read-only)

- Dispatch marker: `OVERNIGHT_PAPER_BOARD_PACKET_C2_KUN_AUDIT_BRIEF_V1`
- **Completion marker (emit ONLY when fully done):** `OVERNIGHT_PAPER_BOARD_PACKET_C2_KUN_AUDIT_COMPLETE_V1`
- Parent approval: `OVERNIGHT_PAPER_BOARD_EXECUTION_APPROVED_20260726T133216Z`
- Prepared by: Hwao/Fable at Deepening Gate 1. Dispatched by: Tori (do not self-start).
- Lane: **standalone ChatGPT Codex gpt-5.5 Pro subscription only** — no API-key, no PAYG, no third-party route.
- This brief is standalone. **READ-ONLY audit — you make NO edits to the C2 candidate or any other file.**

## Your role
Mechanically and adversarially audit whether the C2 candidate honors every contract Hwao/Lana asserted — source-diff, hashes, PDF text, claim surface, and the receipt-vs-reality contract. This is the mechanical cross-model (Codex) counterpart to Lana's scientific red-team; produce PASS/FAIL with evidence, do not fix anything.

## Allowed READ roots (read-only)
1. C2 candidate: `packets/C-candidate-build/lana/c2-mzr-gated-e2e-candidate/` — `candidate.tex`, `candidate.pdf`, `result.png`, `COMPILE_NOTE.md`, `compile.log`, `candidate.log`.
2. Source: `/Users/duhokim/…/lab-runs/gated-e2e-demo/draft.tex`, `gated-e2e-demo.json`, `gated-e2e-demo/result.png`.
3. Baseline (`INPUT_SHA256.txt`); `reviews/lana/LANA_PACKET_C_RECEIPT.md` (the claims to verify); `reviews/hwao/HWAO_PACKET_A_CANONICAL_DECISION.md`, `HWAO_PACKET_B_FINAL_DECISION.md`, `HWAO_ABCD_FIRSTPASS_ROLLUP.md`; `reviews/tori/TORI_CD_FIRSTPASS_VALIDATION.md`; this brief.

## Allowed WRITE root (exclusive to you — single writer)
- Deliverable ONLY under `…/packets/C-candidate-build/kun-c2-audit/`
- Receipt ONLY at `…/reviews/kun/KUN_C2_AUDIT_RECEIPT.md`
- Temp ONLY as `…/packets/C-candidate-build/kun-c2-audit/_tmp_*` (never TMPDIR, /tmp, scratchpad).

## Forbidden (stop and report if any is required)
Edit or rewrite the candidate or ANY file; run the live runner; recompile or replace the candidate; edit any source; introduce any new source/citation/claim; any public/static-root, DB/SQL/API/wiki/page-version write; deploy/restart; git; cron; browser automation; credentials/account/billing/cloud config; Nous purchased-balance; Anthropic third-party PAYG routing. No publication. **Lane: standalone ChatGPT Codex gpt-5.5 Pro subscription only — no API-key / PAYG / third-party route.**

## Tasks (mechanical; PASS/FAIL + evidence each)
1. **Source diff.** Unified `diff` of source `gated-e2e-demo/draft.tex` → `candidate.tex`. Verify EXACTLY three hunks and their nature: (a) non-rendered `%`-comment header (does not render), (b) Introduction connective split (ONLY `, while ` → `. ` and `, and ` → `. `; citation wording unchanged; all four citations isolated), (c) append-only Caveats additions AFTER the unchanged original Caveats paragraph. Report any additional/unexpected hunk as FAIL.
2. **Hash / figure identity.** Recompute SHA-256 of `candidate.tex`, `candidate.pdf`, `result.png`; verify `result.png` is byte-identical to source `gated-e2e-demo/result.png` (`ed83a8250b4a7a2ba969751f3519253f7a2e386080de239bd06e66baa9f82639`); verify `candidate.pdf` = `eed8992dbcfd2a23abc5e459dddbd2660a9add3607e9f34035df9115ac26b98e` and `candidate.tex` = `c615b2f39502bf4e15f54e8fba3818ca480c9fd162360044c804893a11bc00d9` (match Lana receipt + Tori validation).
3. **PDF-text extraction.** Extract text from `candidate.pdf` and verify the rendered document visibly contains: the O/H-scale caveat, the TENSION caveat, the provenance caveat, and the `AI_DRAFT_NOT_HUMAN_GOLD` token (it should appear rendered inside the provenance caveat, not only as a non-rendered comment). Report which disclosures are rendered vs comment-only.
4. **Claim surface.** Enumerate every numeric token and factual claim in `candidate.tex`; verify each is present in the source (`23,722`, `120,000`, `z=0`, solar-scaled O/H, etc.). Any number/claim NOT in source = FAIL.
5. **Reference integrity.** Verify all 5 reference entries (Qi2025, Torrey2019, Garcia2023, Guo2016, LaraLopez2013) are present and textually identical to source (specifically that `LaraLopez2013` was NOT dropped, unlike Kun's rejected removal candidate).
6. **Receipt-contract concordance.** For each material claim in `LANA_PACKET_C_RECEIPT.md` (DONE state, 3-hunk diff, caveats applied, figure byte-identical, refs retained, compile rc=0, no source edit, isolated/unpublished), mark whether the actual files bear it out. Flag any receipt claim not supported by evidence.

## Deliverable
`packets/C-candidate-build/kun-c2-audit/C2_CONTRACT_AUDIT.md` — a mechanical checklist (item → PASS/FAIL → evidence), the diff hunk count, the hash table, PDF-text disclosure presence, the claim-surface result (expected: no new numbers), reference-integrity result, and the receipt-vs-reality concordance. Headed `AI_DRAFT_NOT_HUMAN_GOLD`.

## Stop conditions
Any temptation to edit/recompile the candidate; source drift vs `INPUT_SHA256.txt`; any need for the runner; a payment/overage/top-up/Nous/PAYG prompt; any need to write outside your write root.

## Completion contract
`reviews/kun/KUN_C2_AUDIT_RECEIPT.md` must list the deliverable's SHA-256, the per-item PASS/FAIL summary, any FAIL/discrepancy, an explicit "no candidate edits made" attestation, any STOP notes, and a completion state of `DONE` / `PARTIAL` / `BLOCKED` (never relabel PARTIAL/BLOCKED as success). End the receipt with the completion marker on its own line:

`OVERNIGHT_PAPER_BOARD_PACKET_C2_KUN_AUDIT_COMPLETE_V1`
