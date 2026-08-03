# Hwao Coordinator Acceptance — Overnight Paper Board Portfolio (2026-07-27)

Coordinator: Hwao / Fable. Written at 2026-07-27T22:06 KST (2026-07-27T13:06:57Z), inside the approved execution window. Stop files checked at start of this task: `GLOBAL_STOP_OVERNIGHT_PB_20260727.md` — absent; `CONTENT_FREEZE_OVERNIGHT_PB_20260727.md` — absent. Work may proceed.

## 1. Decision

**ACCEPT**

The corrected portfolio board and the three packet briefs preserve every verified correction:

- Visible portfolio is 13 items = 1 flagship + 5 frontier + 7 real pipeline notes; the API holds 9 records of which `gated-e2e-demo` and `gated-halt-demo` are hidden fixtures. Confirmed against `input/PORTFOLIO_BOARD_SNAPSHOT.json` (counts block and a 13-item `items` array).
- MZR invariant preserved: TNG = 23,722; SDSS = 120,000 (present verbatim in the `c2v2e2e0726a` and `d8de519cb9c9` snapshot summaries). The earlier reversed counts from the superseded v2 coordinator draft are acknowledged as wrong and do not appear anywhere in these inputs.
- P0 leads because the highest-merit TNG-validation frontier (advisory 6.90) has a 404 review path — recorded in `input/BASELINE_RECEIPT.json` as the single non-200 (`p0_review`, status 404, overall `PASS_WITH_EXPECTED_P0_REVIEW_404`) — and contradictory MZR states across its served representation.
- Publication target is exactly one new public Paper Board audit report after integration preflight; no paper, PDF, card, Lab-run, cockpit, or wiki replacement.
- Hard stop 2026-07-28 10:00 KST per the execution board and brief; this supersedes the plan document's earlier 06:00 KST planning window.

## 2. Packet order and dependency adjustments

Order: **P0 → P1 → P2** in priority; P0 is first and last-to-drop.

Exact dependency adjustments:

1. All three primary lanes (Lana/P0, Kun/P1, Goru/P2) may start concurrently once their immutable `input/` snapshots exist; priority order governs quota and drop order under time pressure, not serialization.
2. Every packet pins artifact identity from the frozen baseline (`PORTFOLIO_BOARD_SNAPSHOT.json` + `BASELINE_RECEIPT.json`); no lane re-derives counts or fetches a "convenient copy" that differs from the pinned identity. Drift = `INPUT_OR_IDENTITY_DRIFT_BLOCKER`, stop that packet.
3. P0's 4-page served PDF (SHA-256 `086654…d62ef`) is the audit target; the divergent 3-page source copy is evidence of divergence, not a substitute target.
4. Cross-review of any packet starts only after that packet's primary done marker exists (`P0_LANA_PRIMARY_COMPLETE_20260727`, `P1_KUN_PRIMARY_COMPLETE_20260727`, `P2_GORU_PRIMARY_COMPLETE_20260727`); no barrier across packets — each swaps independently when ready.
5. Hwao dispositions depend on primary + cross-review receipts per packet (see §5). The single integration audit report depends on all three dispositions (or explicit `BLOCKED`/`DROPPED_BY_PRIORITY` states) plus Tori's custody verification, and passes integration preflight before the one approved publication.
6. If time degrades: drop P2 first, then P1; P0 is retained to the end. A dropped packet is recorded `DROPPED_BY_PRIORITY` with whatever intake ledger exists — never silently omitted.

## 3. Science stop conditions

Stop the affected packet immediately (preserve `BLOCKED`, do not draft around the gap) on any of:

- Input or public-artifact drift from the pinned baseline identity, or ambiguous artifact identity (two revisions claiming the same role).
- Unsupported or cross-wired source identity; a citation resolving only to topic proximity rather than the attached claim.
- Number, redshift, population, aperture, IMF, diagnostic, abundance-scale, or statistic mismatch that makes estimands incommensurable.
- An expected-value `CONTRADICTS` on a claim the packet depends on.
- Source-access failure that prevents line-level review, or the only remaining path requires login/CAPTCHA/payment/account/OAuth or any surface outside the approved network boundary.
- A fix that would require fresh data, a runner execution, mutation of any source/public/product file, or external submission.
- Two failed independent review attempts on the same candidate claim.
- Any write outside the lane's own directory under the overnight root.

Packet-specific: P0 — the missing/404 referee path is an artifact-integrity defect; no review verdict may be invented from the history JSON. P1 — no substituting Schechter parameters, UV luminosity functions, halo densities, or extreme-value ceilings for explicit `n(>M*)` evidence; populations stay separate. P2 — `fesc002` is never edited; entailment replays only on an isolated copy; coverage must rise above zero without fabricated support; no claim is strengthened to force a pass. Globally: no evidence-hunting to rescue an overbroad claim — narrow, block, or retire it. A compiled PDF or automated ACCEPT is not human validation.

## 4. Cross-review assignments (no self-review)

| Packet | Primary (excluded from reviewing it) | Cross-reviewers |
|---|---|---|
| P0 TNG validation | Lana | Kun — artifact/representation custody audit; Goru — mechanical claim-citation and numeric-invariant map |
| P1 massive abundance | Kun | Lana — scientific scope review; Goru — mechanical source/numeric map |
| P2 fesc lineage | Goru | Kun — citation-entailment audit; Lana — overclaim/status review |

Tori independently verifies the custody chain, manifests, and receipts for all packets and validates Hwao's roll-up; Tori authors no packet content. Hwao writes only disposition and coordination files and reviews no packet as author. No lane reviews its own primary output anywhere in this table.

## 5. No-conclusions-before-receipts confirmation

Confirmed: Hwao writes no packet conclusion, disposition, verdict, or synthesis for P0, P1, or P2 before that packet's lane receipts (primary done marker plus cross-review artifacts) exist on disk. This acceptance document contains no packet science conclusions — only ordering, boundaries, and stop conditions. Each `HWAO_DISPOSITION.md` will cite the specific receipts it relies on.

## 6. Final marker

HWAO_PB_COORDINATOR_ACCEPTED_20260727
