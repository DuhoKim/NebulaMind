# Lana cross-method review — evidence/trust consistency + no-overclaim (read-only)

Marker: RESOURCE_SURGE_EVIDENCE_TRUST_20260708T022147Z
Role: Lana — cross-method consistency / no-overclaim reviewer (no edits). Read-only/static verification + this one `.hermes` report.
Reviewed against final packet: `AUTOPILOT_EVIDENCE_TRUST_LINKING_20260708T014205Z` (STATUS READY_FOR_USER_APPROVAL).

## Verdict: **PASS with 4 WARNs** (0 FAIL)

The M1/M2/M3 evidence-trust candidates are honest and non-overclaiming: each method uses a trust vocabulary faithful to its actual basis and each explicitly discloses what its trust layer is, is not, and where binding is incomplete. No fabricated evidence/IDs/trust and no "settled/proven" overreach were found. WARNs are minor count/packet-consistency/legend items — none undermine the no-overclaim posture, and none are blockers.

## Exact paths inspected (read-only)
- Packets: `.hermes/…/mastermind/autopilot/RESOURCE_SURGE_DISPATCH_20260708T022147Z.md`; `.hermes/…/mastermind/autopilot/AUTOPILOT_EVIDENCE_TRUST_LINKING_20260708T014205Z_FINAL_NO_APPLY_PACKET.md`
- M1: `…/packet-gated-paper-to-wiki-reconciliation/evidence-trust-rebuild/{evidence-trust-bindings-20260708T014205Z.md.json, evidence-trust-preview-20260708T014205Z.html}`
- M2: `…/source-first-paper-adjudication/evidence-trust-rebuild/{evidence-trust-map-20260708T014205Z.json, page-content-20260708T014205Z.md, wiki-format-preview-20260708T014205Z.html}`
- M3: `…/debate-map-to-wiki-rebuild/evidence-trust-rebuild/{evidence-basis-20260708T014205Z.md, page-content-evidence-trust-20260708T014205Z.md, wiki-format-preview-evidence-trust-20260708T014205Z.html}`
- Verdict chain: `method1/HWAO_M1_EVIDENCE_TRUST_VERDICT_…`, `method2/HWAO_M2_EVIDENCE_TRUST_VERDICT_…`, `method2/EVIDENCE_TRUST_GORU_LEDGER_…`, `method3/HWAO_M3_EVIDENCE_TRUST_VERDICT_…` (all exist; verdict tokens PASS/READY).

## Per-method — trust vocabulary, unbound/unmatched honesty, overclaim

**M1 packet-gated — PASS.** Trust vocabulary = real product-derived `trust_level` (`unverified`/`debated`/`reported` with `trust_score`) for the **3 bound** claims (2929, 2931, 2946); **27 `unbound-local`**. Bindings JSON policy: "no invented evidence/cite/claim/source IDs, DOIs, or trust levels; product cite IDs not injected" (bound_count 3 + unbound_local_count 27 = 30 ✓). Preview reader-facing text is honest: "3 evidence-bound / 27 unbound-local (trust/evidence in product layer — **closed gate**) / 0 invented cites / IDs / links / Trust summary (from real local evidence only) / candidate · not published." No overclaim (2929 shown `unverified`, score −0.14). 0 claim/cite markers in the preview.

**M2 source-first — PASS (1 WARN).** Trust vocabulary self-labeled `"method-local source-first adjudication status (NOT product DB trust)"`: `ACCEPTED`(2, both "human +1") / `LIMITED`(=accepted-limited) / `excluded`(2, with F1/F3 reasons) / `rejected`(12, with reasons). Page-content markers = **6 claim, 0 cite, 7 cite-unmatched** — matches packet; cite-unmatched grammar is exemplary ("…evidence 28066 (arXiv:2512.05584)…; unresolved to product cite ID"). Preview surfaces "NOT product" trust explicitly. No overclaim (the lone "guarantee" hit is a negation: "…not as a guarantee that every active nucleus quenches its host"). WARN-1 below (totals off-by-one).

**M3 debate-map — PASS.** Trust vocabulary = real debate-map axis statuses (`widely_supported` / `emerging_sample_limited` / `actively_debated` / `contradicted_or_model_dependent`) + "scoped coverage-extension", explicitly "**NOT a product trust score**", **0 product claim/cite markers by design** (page-content verified 0/0/0). Unbound honesty is the strongest of the three: evidence-basis flags its own **Unmatched (P3 repair)** items — `2915/2921/2913` (v1709-body-only), `2133→2605.22497` (missing source), `2374` (garbled claim_text) — and carries the `PENDING_RECHECK` baseline caveat. "All IDs are real … None are invented." No overclaim.

## Cross-method consistency findings
- **Consistent where it matters:** all three (a) match trust vocabulary to their true basis and (b) disclose binding limits reader-facing. None dresses up an unbound layer as product-bound. "model-dependent" is used consistently across all three previews.
- **No-invent — consistent PASS:** M1/M2 bind only to existing local inventories/ledgers; M3 fakes no product binding. No invented cite/claim/source IDs, DOIs, ADS links, or trust levels found in any candidate.
- **Packet ↔ candidate parity — PASS:** packet's per-method claims (M1 3-bound/27-unbound; M2 6 claims + 7 cite-unmatched + 0 numeric cites; M3 0 markers + the 3 named unmatched sets) all reconcile against the actual files.

## WARNs (minor, non-blocking; reconcile — I made no edits)
- **WARN-1 (M2 totals off-by-one).** `evidence-trust-map-20260708T014205Z.json` `totals.accepted_limited = 20` and `cited_positions = 22`, but the per-claim `evidence[]` arrays sum to **19** and **21** (accepted_full 2 ✓, excluded 2 ✓, rejected 12 ✓). A 1-count overstatement of cited positions. → M2/Goru reconcile the `totals` block to 19/21.
- **WARN-2 (packet self-contradiction: restart).** Packet body ("No build/deploy/restart needed"; approval wording "Static file copy served immediately") is contradicted by its own appended M2 correction (new `evidence-trust-rebuild/` subdirs 404 until `:3000` restart). Self-corrected in the appendix only → fold the restart caveat into the body/approval-gate wording so a body-only reader isn't over-promised.
- **WARN-3 (packet self-contradiction: M2 receipt gap).** Packet body §"Receipt-chain gap" says M2's Goru/Tori/Hwao chain is absent; the appendix + the actual files (`EVIDENCE_TRUST_GORU_LEDGER` PASS, `HWAO_M2_EVIDENCE_TRUST_VERDICT` PASS/READY) show it is **CLOSED**. Stale body claim → reconcile so the body matches the (correct) appendix.
- **WARN-4 (no shared trust legend across methods).** The three trust scales are legitimately different and non-comparable by design, but three different unbound terms — M1 `unbound-local`, M2 `cite-unmatched`, M3 `unmatched` — and a term collision (**M1 product `debated` vs M3 debate-map `actively_debated`/`debated` mean different things**) invite side-by-side misreading. → add a one-paragraph cross-method trust-vocabulary legend (or an explicit "scales are non-comparable" note) at the index/packet level. No candidate edit required.

## Hard-boundary compliance
Read-only/static inspection + this one `.hermes` report only. Zero edits to any candidate or live root; zero copy into `NebulaMind-origin-main-live`; zero `/api/pages`, `page_versions`, product DB/SQL, git, deploy/restart, browser, cloud/OAuth/secrets, cron, or live publication. No hard-gate prompt encountered → no BLOCKED. Local `python3`/`grep` read-only scans only.

## Next action (optional, non-blocking)
Reconcile WARN-1 (M2 totals) and WARN-2/3 (packet body vs appendix); optionally add the WARN-4 legend. None gate the packet's READY_FOR_USER_APPROVAL status; the separate live-root mirror / P3 binding gates remain closed.
