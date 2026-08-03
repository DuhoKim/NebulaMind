# Galaxy Evolution method-cockpit permission

Marker: GALAXY_EVOLUTION_METHOD_COCKPIT_PERMISSION_20260706T142132Z

Timestamp: 2026-07-06T14:21:32Z / 2026-07-06 23:21:32 KST

User direction:
- Let each team update its own cockpit with its own Baseline and next action phrases.
- The user will check each method cockpit and decide next actions.
- The user will tell each method Tori where to go next.
- Add provider usage-limit visibility to the main cockpit.
- Reduce repeated permission checks for this approved docs-only scope.

Approved without repeated user check during this phase:
- Method1 team may update files under:
  - /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method1
  - /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation
- Method2 team may update files under:
  - /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method2
  - /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication
- Method3 team may update files under:
  - /Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method3
  - /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild

Allowed artifact class:
- Method-local cockpit/index/status/quintet/wiki-page/static docs inside the assigned method workspace.
- Method-local Baseline description for that method.
- Method-local next-action phrase for user steering.
- Method-local receipts and validation notes.

Still not approved:
- No commit, push, merge, branch rewrite, deploy, runtime publish, live wiki/page_versions write, DB mutation, SQL apply/rollback, migration, trust recompute, backend/API restart, service restart, production data write, cloud/API mutation, billing-heavy API use, or cross-method overwrite.
- No shared parent/alias public files unless Hwao/user explicitly grants a separate shared-surface update:
  - frontend/public/agent-reports/wiki-method-results/galaxy-evolution/index.html
  - frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation.html
  - frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication.html
  - frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild.html

Permission behavior:
- If a TUI asks for permission to create/edit a file inside the method's own approved roots for the artifact class above, the method Tori/lane may approve it without asking the user again.
- If a TUI asks for broader session-wide permission, it is acceptable only while the visible task instructions in that pane are constrained to the approved method roots and artifact class above.
- If a request touches a forbidden class or a shared/cross-method path, stop and record a blocker instead of approving.

Receipt expected from each method Tori:
- Write METHOD_COCKPIT_PERMISSION_ACK_20260706T142132Z.md under that method handoff root.
- State the method-local cockpit path(s), baseline/next-action phrase plan, and any blockers.
