# Kun — C2 V2 Mechanical Contract Audit Brief (read-only)

- Dispatch marker: `OVERNIGHT_PAPER_BOARD_PACKET_C2_KUN_V2_AUDIT_BRIEF_V1`
- **Completion marker (emit ONLY when fully done):** `OVERNIGHT_PAPER_BOARD_PACKET_C2_KUN_V2_AUDIT_COMPLETE_V1`
- Parent approval: `OVERNIGHT_PAPER_BOARD_EXECUTION_APPROVED_20260726T133216Z`
- Prepared by: Hwao/Fable at Deepening Gate 3. Dispatched by: Tori (do not self-start).
- Lane: **Codex gpt-5.5 using ChatGPT Pro subscription only** — no API-key, no PAYG, no third-party route.
- This brief is standalone. **READ-ONLY audit — you make NO edits to V1, V2, source, or any file.** Public status stays `AWAITING_EXPLICIT_PUBLISH_APPROVAL`.

## Your role
Independently, mechanically verify that the V2 candidate applies exactly the F1–F4 fixes and preserves everything else — the cross-model (Codex) check on the V2 build. Produce PASS/FAIL with evidence; fix nothing.

## Allowed READ roots (read-only)
1. V2 candidate: `packets/C-candidate-build/lana/c2-mzr-gated-e2e-candidate-v2/` — `candidate.tex`, `candidate.pdf`, `result.png`, `COMPILE_NOTE.md`, `compile.log`, `candidate.log`, `V1_TO_V2_DIFF.md`.
2. V1 candidate (frozen, for the V1→V2 diff + preservation): `…/c2-mzr-gated-e2e-candidate/candidate.tex`, `candidate.pdf`, `result.png`.
3. Source: `/Users/duhokim/…/lab-runs/gated-e2e-demo/draft.tex`, `gated-e2e-demo.json`, `gated-e2e-demo/result.png`.
4. Baseline (`INPUT_SHA256.txt`); `reviews/lana/LANA_C2_V2_RECEIPT.md`; `reviews/hwao/HWAO_C2_REDTEAM_ADJUDICATION.md`, `HWAO_C2_V2_BUILD_ACCEPTANCE.md`; this brief.

## Allowed WRITE root (exclusive to you — single writer)
- Deliverable ONLY under `…/packets/C-candidate-build/kun-c2-v2-audit/`
- Receipt ONLY at `…/reviews/kun/KUN_C2_V2_AUDIT_RECEIPT.md`
- Temp ONLY as `…/packets/C-candidate-build/kun-c2-v2-audit/_tmp_*` (never TMPDIR, /tmp, scratchpad).

## Forbidden (stop and report if any is required)
Edit/rewrite/recompile V1, V2, source, or ANY file; run the live runner; edit any `lab-runs` artifact; introduce any new source/citation/claim; any public/static-root, DB/SQL/API/wiki/page-version write; deploy/restart; git; cron; browser automation; credentials/account/billing/cloud config; Nous purchased-balance; Anthropic third-party PAYG routing. No publication. **Lane: Codex gpt-5.5 (ChatGPT Pro) only — no API-key / PAYG / third-party route.**

## Tasks (mechanical; PASS/FAIL + evidence each)
1. **Hashes — source/V1/V2.** Recompute and verify: source unchanged (`draft.tex f1aeadd8…`, `gated-e2e-demo.json 46ddd75d…`, `result.png ed83a825…`); **V1 FROZEN/unchanged** (`candidate.tex c615b2f3…`, `candidate.pdf eed8992d…`, `result.png ed83a825…`); V2 matches receipt (`candidate.tex bb77d38d…`, `candidate.pdf ac59ac60…`, `result.png ed83a825…`, `COMPILE_NOTE 07456dc5…`, `V1_TO_V2_DIFF 7950cbf0…`).
2. **V1→V2 diff limited to F1–F4 + header.** Unified `diff -u` of V1 `candidate.tex` → V2 `candidate.tex`. Verify the ONLY rendered changes are: F1 (Result softening), F2 ("reproducible" removed), F3 (Abstract scale-limited/TENSION flag + figure-**caption** note), F4 (not-submitted tag), plus the non-rendered `%` header-comment update. Any other rendered change = FAIL.
3. **Rendered PDF strings.** `pdftotext` the V2 `candidate.pdf`. Verify PRESENT (rendered): the F4 tag, the F3 abstract flag, the F3 caption note, the F1 softened Result sentence, the O/H-scale caveat, the TENSION caveat, the provenance caveat, and a rendered `AI_DRAFT_NOT_HUMAN_GOLD`. Verify ABSENT: the old overclaim "provides insights into the relationship" and the word "reproducible".
4. **Reference integrity.** All five references (Qi2025, Torrey2019, Garcia2023, Guo2016, **LaraLopez2013**) present and textually identical to source; reference block unchanged vs source/V1.
5. **Citation split.** The Introduction is four single-citation sentences (Qi2025 / Torrey2019 / Garcia2023 / Guo2016), preserved from V1.
6. **Caveats.** O/H-scale (bounded wording), TENSION (carried, not upgraded), and Provenance caveats all present; the original source Caveats paragraph intact; none weakened.
7. **Figure byte-identity.** V2 `result.png` SHA-256 = source `gated-e2e-demo/result.png` (`ed83a825…`).
8. **Compile evidence.** `COMPILE_NOTE.md` records `rc=0`; `compile.log`/`candidate.log` show `candidate.pdf` produced with only underfull-box warnings; no errors/overfull/missing-package.
9. **V2 receipt concordance.** For each material claim in `LANA_C2_V2_RECEIPT.md` (DONE; V1/source frozen; F1–F4 applied; retention; figure identity; rc=0; isolated/unpublished), mark whether the actual files bear it out. Flag any claim not supported.

## Deliverable
`packets/C-candidate-build/kun-c2-v2-audit/C2_V2_CONTRACT_AUDIT.md` — a mechanical checklist (item → PASS/FAIL → evidence), the V1→V2 diff hunk inventory, the hash table (source/V1/V2), PDF-string present/absent results, reference/split/caveat/figure/compile results, and the receipt-vs-reality concordance. Headed `AI_DRAFT_NOT_HUMAN_GOLD`.

## Stop conditions
Any temptation to edit/recompile; source drift vs `INPUT_SHA256.txt`; a V1 hash that differs from the frozen value; any need for the runner; a payment/overage/top-up/Nous/PAYG prompt; any need to write outside your write root.

## Completion contract
`reviews/kun/KUN_C2_V2_AUDIT_RECEIPT.md` must list the deliverable's SHA-256, the per-item PASS/FAIL summary, any FAIL/discrepancy, an explicit "no candidate/V1/source edits made" attestation, any STOP notes, and a completion state of `DONE` / `PARTIAL` / `BLOCKED` (never relabel PARTIAL/BLOCKED as success). End the receipt with the completion marker on its own line:

`OVERNIGHT_PAPER_BOARD_PACKET_C2_KUN_V2_AUDIT_COMPLETE_V1`
