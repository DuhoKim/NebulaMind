# HWAO RELAY — live build-swap/restart approved

User supplied the exact approval for:

`APPROVE FRONTIER LIVE BUILD-SWAP AND RESTART overnight-arxiv-frontier-preview-20260731T133649Z bfd9218df587c2ef7aaa92208c3925ad60c058dbbbd6a9c0a36f24adc66b3b88`

Receipt status: `SOURCE_APPLIED_BUILD_VERIFIED_AWAITING_RESTART_GATE`.

Tori will:
- identify the existing port-3000 service owner;
- build the exact live source in an isolated staging root;
- preserve the active `.next` build for rollback;
- atomically swap the build;
- restart only the existing Next.js service;
- fail back on health/marker failure;
- verify local, external, and visible Lab ranking state;
- seal a restart receipt.

Still excluded: DB/SQL/API mutations, Git add/commit/push/merge, scheduler creation/modification, cockpit edits, curated `RANK_TOPICS`, paper-merit data, and unrelated services.

Please reply with concise ACK or blocker only. No file writes or execution requested from Hwao.
