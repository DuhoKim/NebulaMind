# Resource surge synthesis — Galaxy Evolution evidence/trust

Marker: `RESOURCE_SURGE_EVIDENCE_TRUST_20260708T022147Z`
Second-wave marker: `RESOURCE_SURGE_EVIDENCE_TRUST_20260708T022147Z_SECOND_WAVE`
Written by Tori after user direction to use idle resources, especially high-quota lanes.

## Status

Resource surge completed useful work across Goru/Gemini, Kun/Codex, Lana, and Hwao-m2 lanes. No live-root mirror, no restart, no product wiki publish, no DB/API/page_versions/git/deploy/browser/cloud/cron occurred.

The earlier final evidence/trust no-apply packet remains useful as a candidate inventory, but its original approval wording must be treated as **superseded** by the corrected wording below because resource-surge audits confirmed a restart/visibility caveat for brand-new static subdirectories.

## Resources used

High-quota / high-availability lanes used:
- Goru/Gemini: M1 link coverage, M2 trust/source audit, M3 docs trust audit, M1 label-fix audit/verification, M2 totals reconciliation, restart visibility audit.
- Kun/Codex: static-safety scan, link/checksum manifest, live-readiness dry-run, M1 additive label-fix candidate, M2 totals script check, corrected approval wording.
- Lana: M1 UX review, M2 approval wording review, cross-method no-overclaim review.
- Hwao-m2: read-only coordination/cross-check; no mirror/write gate opened.

Panes deliberately not used for mirror/apply: Hwao-director and Hwao-m3 still visually contain stale typed-looking mirror-apply text in their prompt lines. Tori did not press Enter there.

## Key findings

1. Evidence/trust candidates are static-safe overall: no executable scripts/fetch/API/page_versions/product DB routes. Method1 has intentional arXiv evidence links only.
2. M1 original candidate was honest but reader-confusing: 27 unbound chips were labeled `provenance`, which could read as stronger trust than the 3 actually evidence-bound chips.
3. Kun created an additive M1 P1 label-fix candidate, leaving the original untouched:
   `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/evidence-trust-rebuild/evidence-trust-preview-p1-label-fix-20260708T022147Z.html`
   Verification: 0 old `· provenance` labels, 27 `· no local evidence / unbound` labels, clarifier present, 43 evidence rows/arXiv links preserved.
4. M2 totals warning is resolved as a terminology/legend issue, not a data error: global totals include evidence `28060`, an `accepted_limited` caution with target `None`; per-claim arrays exclude it. The original totals `accepted_limited: 20` and `cited_positions: 22` are defensible if documented. A note should clarify that one accepted-limited caution is no-current-target and not assigned to a claim.
5. Restart/visibility caveat is confirmed: previously copied live-root `same-format-rebuild/` files exist on disk but still 404 through the running `next start`. Therefore new `evidence-trust-rebuild/` dirs may also remain 404 after mirror until a separately approved `:3000` restart.
6. The old approval wording saying “served immediately” / “no restart” is inaccurate and should not be used.

## Corrected approval gate wording to use if the user wants visibility

> Approve a live-root static mirror of the Galaxy Evolution evidence/trust candidate files from the working repo into `NebulaMind-origin-main-live/frontend/public/...`, creating three new `evidence-trust-rebuild/` directories for Method1, Method2, and Method3. This is a file-copy mirror into the live-served static root only. It does not publish to the product wiki, does not call `/api/pages`, does not write `page_versions`, does not touch the product DB/SQL, and does not run git/build/deploy.
>
> Important visibility caveat: because these are new static subdirectories under the running Next `public/` tree, the new URLs may continue to return 404 after the mirror until a separate `:3000` server restart is approved and performed. This approval covers only the static file mirror. Restart remains a separate deploy/restart hard gate unless explicitly approved in the same user instruction.
>
> Method limitations remain visible: Method2 has the strongest local source-first evidence binding. Method1 has real local evidence for only 3 of its 30 claim chips; the other 27 stay marked as unbound/local until the product claim/evidence database is opened under a separate gate. Use the P1 label-fix candidate for Method1 if mirroring, not the older confusing-label preview. Method3 is docs-only by design: it provides debate-map trust framing and local provenance navigation, not product claim/citation evidence binding. Method3 P3 product claim/citation binding remains a separate future gate.
>
> This mirror is reversible from backup. Product-wiki publication, `/api/pages`, `page_versions`, product DB/SQL, full Method1 binding, Method3 P3 binding, git, build/deploy, and any restart not explicitly approved remain closed.

## Reports produced

First wave:
- `.hermes/handoffs/galaxy-evolution/mastermind/autopilot/RESOURCE_SURGE_DISPATCH_20260708T022147Z.md`
- `.hermes/handoffs/galaxy-evolution/method1/autopilot/RESOURCE_SURGE_GORU_M1_LINK_COVERAGE_20260708T022147Z.md`
- `.hermes/handoffs/galaxy-evolution/method2/autopilot/RESOURCE_SURGE_GORU_M2_SOURCE_TRUST_20260708T022147Z.md`
- `.hermes/handoffs/galaxy-evolution/method3/autopilot/RESOURCE_SURGE_GORU_M3_DOCS_TRUST_20260708T022147Z.md`
- `.hermes/handoffs/galaxy-evolution/mastermind/autopilot/RESOURCE_SURGE_KUN_STATIC_SAFETY_20260708T022147Z.md`
- `.hermes/handoffs/galaxy-evolution/mastermind/autopilot/RESOURCE_SURGE_KUN_LINK_CHECKSUMS_20260708T022147Z.md`
- `.hermes/handoffs/galaxy-evolution/mastermind/autopilot/RESOURCE_SURGE_KUN_LIVE_READINESS_DRY_RUN_20260708T022147Z.md`
- `.hermes/handoffs/galaxy-evolution/method1/autopilot/RESOURCE_SURGE_LANA_M1_UX_REVIEW_20260708T022147Z.md`
- `.hermes/handoffs/galaxy-evolution/mastermind/autopilot/RESOURCE_SURGE_LANA_M2_APPROVAL_WORDING_REVIEW_20260708T022147Z.md`
- `.hermes/handoffs/galaxy-evolution/mastermind/autopilot/RESOURCE_SURGE_LANA_CROSS_METHOD_REVIEW_20260708T022147Z.md`

Second wave:
- `.hermes/handoffs/galaxy-evolution/method1/autopilot/RESOURCE_SURGE2_GORU_M1_LABEL_FIX_AUDIT_20260708T022147Z.md`
- `.hermes/handoffs/galaxy-evolution/method1/autopilot/RESOURCE_SURGE2_KUN_M1_LABEL_FIX_CANDIDATE_20260708T022147Z.md`
- `.hermes/handoffs/galaxy-evolution/method1/autopilot/RESOURCE_SURGE2_GORU_M1_LABEL_FIX_VERIFICATION_20260708T022147Z.md`
- `.hermes/handoffs/galaxy-evolution/method2/autopilot/RESOURCE_SURGE2_GORU_M2_TOTALS_RECONCILE_20260708T022147Z.md`
- `.hermes/handoffs/galaxy-evolution/method2/autopilot/RESOURCE_SURGE2_KUN_M2_TOTALS_SCRIPT_CHECK_20260708T022147Z.md`
- `.hermes/handoffs/galaxy-evolution/mastermind/autopilot/RESOURCE_SURGE2_GORU_RESTART_VISIBILITY_AUDIT_20260708T022147Z.md`
- `.hermes/handoffs/galaxy-evolution/mastermind/autopilot/RESOURCE_SURGE2_KUN_CORRECTED_APPROVAL_WORDING_20260708T022147Z.md`

## Safety ledger

Zero live-root writes/copies, zero restart/deploy/service mutation, zero product DB/SQL, zero `/api/pages`, zero `page_versions`, zero product-wiki publish, zero git, zero browser automation, zero cloud/OAuth/secrets, zero cron. Writes were restricted to `.hermes` reports and one additive working-repo static Method1 preview candidate.
