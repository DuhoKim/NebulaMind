# Autonomous same-format repair order

Marker: `AUTONOMOUS_SAME_FORMAT_REPAIR_ORDER_20260707T074231Z`
Parent packet: `HWAO_SAME_FORMAT_REBUILD_PACKET_20260707T064500Z`
User directive: run the Method1/2/3 teams autonomously with maximum permissions inside the current docs/static no-apply scope; director team resolves stalls, including permission prompts.

## Permission model

Maximum permission is granted only inside this bounded scope:

Allowed without waiting for new user approval:
- Read/write docs/static artifacts under:
  - `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/*/same-format-rebuild/`
  - `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/`
- Run local read/write validation scripts in the repo or handoff roots for this same-format repair.
- Patch the current same-format preview shell files and receipts/ledgers/verdicts for this repair.
- Use method-local helper panes autonomously: Hwao may dispatch Kun/Goru/Lana/Tori-local prompts for this repair if needed.
- Tori/director may approve one-time or conversation-scoped permission prompts for commands matching the above docs/static roots.

Hard stops still require a separate explicit user gate:
- DB/SQL/trust recompute, `/api/pages`, `page_versions`, live wiki publish, deploy/restart/service mutation.
- Git commit/push/merge/rebase/history rewrite.
- Cockpit/public root/global/shared route mutation outside these static method preview paths.
- Cloud/GCP/Gemini API config, billing/account/payment/credits, OAuth/token/credential reads, `.env`, `.claude/settings*`, secrets.
- Browser automation, cron, external network/API calls.

## Current verified state

Existing rebuilt artifacts are additive under `same-format-rebuild/`; old `wiki-page.html` files remain preserved.

Confirmed by Tori direct HTML check:
- M1 preview has Reader/Evidence controls and disabled History/Sources. M1 has exactly 9 article `<h2>` headings and no TOC `<h2>` problem.
- M2 preview has Reader/Evidence controls and preview-only History/Sources, but uses `<h2>Contents</h2>` in the TOC rail. This creates a 10th raw `<h2>` outside the article.
- M3 preview has Reader/Evidence controls and disabled History/Sources, but uses `<h2>Contents</h2>` in the TOC rail. This creates a 10th raw `<h2>` outside the article.
- Standalone Goru crosscheck falsely reported missing M1/M2 Reader/Evidence controls because its detector looked for `Reader/Evidence` as one string or `Reduce highlights`; actual controls are present as separate Reader and Evidence controls.

## Autonomous repair tasks

1. Method2 Kun: patch only M2 preview shell TOC rail label from `<h2>Contents</h2>` to `<h3>Contents</h3>`; verify article `<h2>` count is 9 and controls remain present.
2. Method3 Kun: patch only M3 preview shell TOC rail label from `<h2>Contents</h2>` to `<h3>Contents</h3>`; verify article `<h2>` count is 9 and controls remain present.
3. Method2 Goru: rerun conformance ledger after M2 shell patch.
4. Method3 Goru: rerun conformance ledger after M3 shell patch.
5. Tori receipts-last: rerun M2/M3 receipts after their ledgers land; preserve M1 receipt unless crosscheck demands a correction note.
6. Hwao M2/M3: rerun same-format verdicts after repaired receipts.
7. Standalone Goru: rerun cross-method crosscheck with corrected control detection: controls pass if HTML contains `Reader` and `Evidence` as separate static controls; `Reduce highlights` is optional preview chrome, not mandatory.
8. Hwao director: final director roll-up after M2/M3 verdicts and standalone crosscheck land.

## Output targets

Use fresh timestamp `20260707T074231Z` for repair addenda and rerun reports. Do not overwrite original 064500Z verdicts/ledgers unless patching the specific preview shell files; record addenda under handoff paths.

Expected repair artifacts:
- M2 patched preview: existing `source-first-paper-adjudication/same-format-rebuild/wiki-format-preview-20260707T064500Z.html`
- M3 patched preview: existing `debate-map-to-wiki-rebuild/same-format-rebuild/wiki-format-preview-20260707T064500Z.html`
- M2 Goru rerun: `.hermes/handoffs/galaxy-evolution/method2/SAME_FORMAT_CONFORMANCE_LEDGER_RERUN_20260707T074231Z.md`
- M3 Goru rerun: `.hermes/handoffs/galaxy-evolution/method3/SAME_FORMAT_CONFORMANCE_LEDGER_RERUN_20260707T074231Z.md`
- M2 Tori receipt rerun: `.hermes/handoffs/galaxy-evolution/method2/receipts/TORI_SAME_FORMAT_REPAIR_RECEIPT_20260707T074231Z.md`
- M3 Tori receipt rerun: `.hermes/handoffs/galaxy-evolution/method3/receipts/TORI_SAME_FORMAT_REPAIR_RECEIPT_20260707T074231Z.md`
- M2 Hwao verdict rerun: `.hermes/handoffs/galaxy-evolution/method2/HWAO_SAME_FORMAT_REPAIR_VERDICT_20260707T074231Z.md`
- M3 Hwao verdict rerun: `.hermes/handoffs/galaxy-evolution/method3/HWAO_SAME_FORMAT_REPAIR_VERDICT_20260707T074231Z.md`
- Standalone Goru rerun: `.hermes/handoffs/galaxy-evolution/mastermind/GORU_SAME_FORMAT_CONFORMANCE_CROSSCHECK_RERUN_20260707T074231Z.md`
- Director final roll-up: `.hermes/handoffs/galaxy-evolution/mastermind/HWAO_AUTONOMOUS_SAME_FORMAT_REPAIR_FINAL_20260707T074231Z.md`

## Stop condition

Stop when final director roll-up exists and reports PASS or PASS_WITH_NOTES with safety ledger clean. If any hard-stop action is needed, stop and ask the user.
