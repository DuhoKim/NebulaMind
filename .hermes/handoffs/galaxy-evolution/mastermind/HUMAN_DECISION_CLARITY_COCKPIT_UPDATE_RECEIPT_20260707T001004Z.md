# Human-decision clarity cockpit update receipt

Marker: HUMAN_DECISION_CLARITY_COCKPIT_UPDATE_RECEIPT_20260707T001004Z
Cockpit marker: HUMAN_DECISION_CLARITY_COCKPIT_20260707T001004Z
Updated UTC: 2026-07-07T00:10:04Z

## User request

Make the human-decision parts in all cockpits more precise and easy to understand.

## Result

Done. The main stable cockpit, mobile view, public status JSON, Galaxy method index, and all three method cockpits/manifests now use a clear A/B/C menu.

## New wording pattern

Decision needed now: choose which Galaxy Evolution snapshot/H2 section list all methods should use next.

- Pick A: use the 9-section local snapshot. Method3 Goru+Kun corroborated 9 H2 sections and 30 visible claim chips.
- Pick B: use the 7-section live/API snapshot. Method1 inventory on v1710 reported 7 H2 sections.
- Pick C: ask Hwao to reconcile once more, read-only, with no drafting/conversion/P1.5/P2.

## What the cockpits now make explicit

- Until A/B/C is explicit, Method1 draft assembly stays frozen.
- Until A/B/C is explicit, Method2 same-format conversion stays frozen.
- Until A/B/C is explicit, Method3 P1.5/P2 stays frozen.
- Later decisions can wait: non-canonical sweep files, Method3 B3 coverage, Ultra doctrine, timestamp cleanup, skill self-patch review, and Method3 Lana addendum.

## Files updated

Stable cockpit source/rendered files:

- frontend/public/agent-reports/stable-cockpit-canonical.json
- frontend/public/agent-reports/live-steering-cockpit.html
- frontend/public/agent-reports/live-steering-status.json
- frontend/public/agent-reports/mobile.html
- frontend/public/agent-reports/baseline-roadmap.html
- frontend/public/agent-reports/baseline-galaxy-current.html

Method cockpit source files:

- frontend/public/agent-reports/wiki-method-results/galaxy-evolution/index.html
- frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/index.html
- frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/manifest.json
- frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/index.html
- frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/manifest.json
- frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/index.html
- frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/manifest.json

Backup:

- /Users/duhokim/NebulaMind/NebulaMind/docs/galaxy_human_decision_clarity_backup_20260707T001006Z

## Verification

- stable_cockpit_renderer.py render-all-public-roots succeeded for repo and live roots.
- stable_cockpit_guard.py lock/check passed with marker HUMAN_DECISION_CLARITY_COCKPIT_20260707T001004Z.
- Public probes passed for main cockpit, public status JSON, mobile page, Galaxy method index, Method1 page, Method2 page, Method3 page, and all three method manifests.
- Each public page/manifest contains marker, clear A/B/C decision wording, snapshot/H2 text, NO ACTIVE EXECUTION PHRASE, and no APPROVE EXECUTE string.

## Safety

Static cockpit/status wording update only. No live wiki/page_versions publish, DB/SQL/migration/trust recompute, deploy/restart, git commit/push/merge, cloud/API/GCP/billing/account/payment/credits/OAuth, browser automation, cron, or extra Ultra/Gemini/Antigravity action.
