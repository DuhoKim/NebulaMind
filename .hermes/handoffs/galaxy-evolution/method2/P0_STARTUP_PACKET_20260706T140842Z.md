# Method2 P0 startup packet — Source-first adjudication

Marker: GALAXY_EVOLUTION_METHOD2_P0_START_20260706T140842Z

Method: Method2 / SFA / source-first paper adjudication
Mesh: mesh-ge-m2-source:Mesh-m2

Assigned handoff root:
/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/method2

Assigned public workspace:
/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication

Existing method briefs:
- Hwao: /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/briefs/hwao-sfa.md
- Lana: /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/briefs/lana-sfa.md
- Goru: /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/briefs/goru-sfa.md
- Kun: /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/briefs/kun-sfa.md
- Tori: /Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/source-first-paper-adjudication/briefs/tori-sfa.md

Method rule:
Begin from the papers themselves, adjudicate source positions first, then allow claims and prose only after source roles are accepted or accepted-limited.

P0 only — required visible-pane receipt:
Each visible lane should read this packet plus its role brief, then write one receipt file under this method handoff root:

- Hwao receipt: receipts/HWAO_P0_ACK_20260706T140842Z.md
- Lana receipt: receipts/LANA_P0_ACK_20260706T140842Z.md
- Goru receipt: receipts/GORU_P0_ACK_20260706T140842Z.md
- Kun receipt: receipts/KUN_P0_ACK_20260706T140842Z.md
- Tori receipt: receipts/TORI_P0_ACK_20260706T140842Z.md

Receipt must include:
- The marker above.
- Role/lane name.
- Acknowledgement of assigned handoff root and public workspace.
- Confirmation that no cross-method/shared-parent/product/wiki/DB/runtime/git/cloud writes are authorized.
- Intended first local artifact or blocker.

Hard stops:
- No commit/push/merge.
- No deploy/publish/live wiki/page_versions update.
- No DB write, SQL apply/rollback, migration, trust recompute, backend/API restart, service restart, production data write, or cloud/API mutation.
- No writes outside Method2 handoff root or Method2 public workspace unless Hwao/user gives explicit later approval.
- Do not edit the shared parent/alias files in the galaxy-evolution public method root unless explicitly coordinated.

Stop condition for P0:
P0 is complete when the Method2 visible lanes have receipt files or explicit visible blockers recorded in this method root.
