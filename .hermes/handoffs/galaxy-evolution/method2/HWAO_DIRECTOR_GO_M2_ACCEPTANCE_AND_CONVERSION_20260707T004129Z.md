# Director GO — Method2 filename-mismatch resolution + same-format conversion packet

Marker: USER_CONFIRM_9H2_CONTINUE_METHODS_20260707T003920Z
GO marker: HWAO_DIRECTOR_GO_M2_ACCEPTANCE_AND_CONVERSION_20260707T004129Z
From: Hwao-director → Hwao-m2 (SFA).

## Step A — resolve the S3/S4 deliverable-path mismatch (mechanical; director-resolved per user policy correction, no user hold)

Tori's S5 Pass-2 receipt correctly blocked on path mismatch, not content: Goru wrote `goru/GORU_SFA_FORMAT_COUNTS_PASS2_20260707.md` (assigned: `..._PASS2_20260706T161345Z.md`) and Kun updated `kun/KUN_SFA_REBUILD_CHECK_20260707.md` (assigned: `..._PASS2_20260706T161345Z.md`), both content-complete with the Pass-2 marker.

Resolution = ACCEPTANCE-BY-RECORD: Hwao-m2 writes one acceptance note mapping observed↔assigned paths and declaring the observed files the official Pass-2 S3/S4 refresh artifacts. Nobody renames, copies, or re-emits anything; Tori does not touch worker files. Then Tori reruns S5 receipts-last against the acceptance note — expected outcome `PASS_WITH_ISSUES` (the ISSUES being the recorded staleness/erratum notes, not new work). Re-emit by the original authors ONLY if your acceptance review finds actual content gaps — not for the filenames.

## Step B — bounded same-format conversion packet (after Step A closes)

Hwao-m2 may then issue the conversion role-split packet. Target deliverable set (method-local, docs/static only):
1. Same-format Markdown article draft in the Method2 public workspace — title `# Galaxy Evolution`, opening provenance blockquote, exact 9-H2 contract list in order — converted from the RATIFIED S2 source-position ledger (`lana/LANA_SFA_SOURCE_ADJUDICATION_20260707.md`, RATIFIED WITH NOTES) under the method rule: only accepted / accepted-limited source positions may support sentences.
2. Carry-forward obligations: row-28133 erratum noted in Kun S4 must be carried visibly; adjudication NOTES respected; no sentence rests on a rejected source position.
3. Format-conformance receipt (all parent-packet fields) + lane receipts: Lana overclaim review of converted prose; Goru mechanical conformance counts; Kun rebuild check; Tori receipts-last.
4. Chips/citations: sparse ≤30 bound; claim grammar `<!--claim:ID-->…<!--/claim:ID-->`; cite grammar numeric-only `<!--cite:ID-->`; renderer rules per `docs/wiki_content_contract_v1.md`; `hero_facts` untouched. Static reference snapshot: the common v1709 body named in the mastermind sequencing record.

## Hard rails

Method2 handoff root + Method2 public workspace writes only. No live wiki/page_versions, DB/SQL, trust recompute, deploy/restart, git, cloud/API/billing/credits/OAuth, browser, cron, route/config, cross-method/shared-parent, or Ultra/Gemini/Antigravity action. Publication remains a separate future user gate. Stop on blockers with `ROLE_TABLE_BLOCKER`.

Receipts: every file carries this GO marker plus your method packet markers, with exact paths listed.
