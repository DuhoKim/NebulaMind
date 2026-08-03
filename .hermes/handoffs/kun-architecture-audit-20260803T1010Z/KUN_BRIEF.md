# KUN BRIEF — Fresh NebulaMind overall-architecture audit (Kimi K3 route)

Task ID: `kun-architecture-audit-20260803T1010Z`
Coordinator: Hwao/Fable. Requested by Duho: a fresh Kun oversight pass on the Kimi K3 route.
Date: 2026-08-03 (~19:10 KST / 10:10 UTC)

## Role

You are Kun on Hermes via Nous Portal route `moonshotai/kimi-k3` — the same seat and route that produced the 2026-07-21 whole-system oversight pass:
`.hermes/handoffs/kun-kimi-k3-oversight-20260721T110854Z/KUN_NEBULAMIND_OVERSIGHT_REPORT.md`
Read that report first. Your job now: a fresh, independent, adversarial audit of NebulaMind's overall architecture as it stands TODAY — and an explicit delta assessment against your prior report.

## Hard constraints (violations void the audit)

- FINDINGS ONLY. Read-only everywhere, with exactly two write exceptions:
  1. your report file (see Deliverable), and
  2. temp/intermediate files, which must stay INSIDE this lane dir (`.hermes/handoffs/kun-architecture-audit-20260803T1010Z/`), named `_tmp_*`.
- WRITE YOUR REPORT AS A FILE. Do not deliver it only to stdout.
- Never open the contents of any `.env*`, token, key, or credential file. Listing names is allowed.
- No git writes of any kind (no add/commit/stash/checkout/reset/clean). Read-only git (status/log/diff/show/branch) is allowed and encouraged.
- No process or system actions: no launchctl, no kill/restart, no installs, no cron, no network mutations. Plain HTTP GET probes of localhost:3000 / https://nebulamind.net are allowed.
- Running focused test suites is allowed (pytest single-file scope, node smoke scripts); full-suite runs only if time permits. Note any test-DB litter they create; do not delete anything.
- No subagents, no browsing beyond the probes above.

## Ground map (verify, don't trust)

- Dev checkout: `/Users/duhokim/NebulaMind/NebulaMind` — now on a DETACHED HEAD; heavily dirty; recent main-line commits #123–#127 (merit 5-panel, external-data capability).
- Live serving checkout: `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live` — production `next build` served by launchd `com.nebulamind.frontend` (next start :3000, Cloudflare tunnel → nebulamind.net; `lab.` 308s to canonical `/lab`). At your 07-21 pass this checkout was clean; it is now DIRTY (hand-patched files, uncommitted promotions).
- Frontier-ranking loop (today's ops, all receipts real): retry/backoff patch in `.hermes/handoffs/galaxy-evolution/corpus-ga-co-2009-2026-20260718/ingest_incremental.py`; launchd `com.nebulamind.frontier-daily` moved 10:45→14:00 KST, `--limit 300`; catch-up receipt `receipts/daily_frontier_ingest_20260803T093855Z.json` (+41 → 994 papers, coverage 2026-07-31); weekly rerank receipt same day; staging `frontiersData.v3.staging.ts` (sha b3b0f6d5…) promoted UNCOMMITTED into both checkouts' `frontend/src/app/lab/frontiersData.ts`; pre-promotion backup `frontiersData.live.backup-20260803T1850K.ts` in the engine dir.
- Research doctrine: `.hermes/plans/2026-07-01_205807-paper-prose-distillation-roadmap.md`, board `.hermes/board/paper-prose-distillation-board.md` (P0 apply gate HELD). Pending plan awaiting user gate: `docs/plans/2026-07-31_223011-nebulamind-overnight-arxiv-corpus-ranking-preview.md` (Yui).
- Context: the whole crew spent ~late-July on the DESI paper (submitted 2026-08-03); NebulaMind work resumed today.

## Deliverable

Write: `.hermes/handoffs/kun-architecture-audit-20260803T1010Z/KUN_NEBULAMIND_ARCHITECTURE_AUDIT_20260803.md`

Required sections:
1. Executive verdict (one line, e.g. HEALTHY_WITH_RISKS) + 3-sentence justification.
2. Delta vs 2026-07-21: status of EACH of your prior 7 prioritized actions (done / partial / untouched / worsened, with evidence).
3. Architecture map as-built today (product runtime, serving/deploy topology incl. the two-checkout + launchd + tunnel reality, research pipelines, trust stack, automation jobs).
4. Ranked risks/blockers with severity and concrete failure scenarios — be adversarial; attack the promotion-without-commit pattern, the detached HEAD, the receipt-less state transitions you find, anything that smells.
5. Evidence/trust assessment (doctrine vs enforcement; what is machine-checked vs aspirational).
6. Engineering/reproducibility (what you ran, exact commands + results; can current behavior be reconstructed from git alone?).
7. Prioritized next actions (owner / action / expected evidence / gate).
8. Evidence ledger: every command run, every file read (content vs names-only).
9. Uncertainties + what you deliberately did not inspect. Separate fact from inference throughout.

End the report file with the marker line:
`KUN_KIMI_K3_ARCHITECTURE_AUDIT_COMPLETE_20260803T1010Z`
