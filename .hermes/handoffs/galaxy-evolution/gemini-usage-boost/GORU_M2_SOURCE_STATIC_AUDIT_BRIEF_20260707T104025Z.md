# Goru M2 Gemini usage boost packet — source-first static audit

Marker: `GORU_M2_SOURCE_STATIC_AUDIT_BRIEF_20260707T104025Z`
Target: Goru M2 / Antigravity Gemini lane
Purpose: Increase Gemini/Goru usage safely by doing a useful read-only source-first static artifact audit.

## Safety boundary

Allowed:
- Read local static files under `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/`.
- Read related local handoff ledgers under `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method2/`.
- Run read-only shell/Python checks if permission is requested.
- Write exactly one report under `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/gemini-usage-boost/`.

Forbidden:
- No editing static/public files.
- No DB/SQL, no live wiki publish, no deploy/restart, no git actions.
- No cloud/GCP/Gemini API/billing/account/credits/OAuth/secrets.
- No browser automation, no cron, no credential/token/cookie file reads.

## Files to inspect if present

- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/index.html`
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/wiki-page.html`
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/same-format-rebuild/wiki-format-preview-20260707T064500Z.html`
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p1-source-position-ledger.html`
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p2-claim-status-ledger.html`
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/p3-wiki-prose-packet.html`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method2/SAME_FORMAT_CONFORMANCE_LEDGER_RERUN_20260707T074231Z.md`

## Task

Perform a deep mechanical audit:

1. Inventory Method 2 packet pages and identify the source-first flow: source-position ledger → claim-status ledger → prose packet.
2. Count headings and static controls in the same-format preview.
3. Count visible claim IDs 2942–2947 and cite/cite-unmatched markers.
4. Inspect whether source-position language stays docs/static and does not imply a live wiki apply.
5. Verify disabled/no-live links for history/sources/edit/publish surfaces.
6. Compare against the rerun conformance ledger and list any mismatch.
7. Produce a PASS/WARN/FAIL report with exact counts and file paths.

## Output

Write exactly:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/gemini-usage-boost/GORU_M2_SOURCE_STATIC_AUDIT_20260707T104025Z.md`

End with:
`GORU_M2_SOURCE_STATIC_AUDIT_DONE_20260707T104025Z`
