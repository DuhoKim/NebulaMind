# Goru M3 Gemini usage boost packet — debate-map static audit

Marker: `GORU_M3_DEBATE_STATIC_AUDIT_BRIEF_20260707T104025Z`
Target: Goru M3 / Antigravity Gemini lane
Purpose: Increase Gemini/Goru usage safely by doing a useful read-only debate-map-to-wiki static artifact audit.

## Safety boundary

Allowed:
- Read local static files under `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/`.
- Read related local handoff ledgers under `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method3/`.
- Run read-only shell/Python checks if permission is requested.
- Write exactly one report under `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/gemini-usage-boost/`.

Forbidden:
- No editing static/public files.
- No DB/SQL, no live wiki publish, no deploy/restart, no git actions.
- No cloud/GCP/Gemini API/billing/account/credits/OAuth/secrets.
- No browser automation, no cron, no credential/token/cookie file reads.

## Files to inspect if present

- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/index.html`
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/wiki-page.html`
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/same-format-rebuild/wiki-format-preview-20260707T064500Z.html`
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/quintet.html`
- `/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method3/SAME_FORMAT_CONFORMANCE_LEDGER_RERUN_20260707T074231Z.md`

## Task

Perform a deep mechanical audit:

1. Inventory Method 3 static pages and identify the debate-map-to-wiki rebuild flow.
2. Count headings and static controls in the same-format preview.
3. Count visible claim IDs, status labels, cite/cite-unmatched markers, and disabled/live links.
4. Check whether the page distinguishes debate-map/status work from final reader-facing live wiki completion.
5. Check that no invented source/evidence application is implied by the static artifact.
6. Compare against the rerun conformance ledger and list any mismatch.
7. Produce a PASS/WARN/FAIL report with exact counts and file paths.

## Output

Write exactly:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/gemini-usage-boost/GORU_M3_DEBATE_STATIC_AUDIT_20260707T104025Z.md`

End with:
`GORU_M3_DEBATE_STATIC_AUDIT_DONE_20260707T104025Z`
