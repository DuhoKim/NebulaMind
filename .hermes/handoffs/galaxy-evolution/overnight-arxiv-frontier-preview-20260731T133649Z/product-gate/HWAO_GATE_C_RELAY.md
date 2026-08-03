# HWAO RELAY — Gate C approved by user

The user explicitly approved the gate described immediately beforehand: apply the verified frontier-ranking preview to the canonical ranking artifact and frontend/live public ranking view.

Run ID: `overnight-arxiv-frontier-preview-20260731T133649Z`
Preview map SHA-256: `ab9c37fb26a0a6112a9281ebdfee16b50ec8f9edace559472b1b90ae5e82e9ac`
Preview TypeScript SHA-256: `08ec69b7b059dc9c0ed1bc1311f9253d092c8ec314e684c149a1e13f3882dc36`
Promotion receipt SHA-256: `65a5117e54c0e46eb11189e1559ef195a922d3c88a4a77b7feff79eaa5a460fe`

Tori is preflighting the exact target set, source authority, rollback snapshots, tests/build, and whether public verification can settle without restart.

Approved bounded scope:
- canonical `frontier_map_v3_reranked.json`;
- canonical `frontiersData.v3.staging.ts`;
- tracked frontend ranking data source;
- richest active live frontend ranking data source/public view;
- run-root Gate C receipts/backups.

Still excluded unless separately approved:
- DB/SQL/API mutations;
- curated `RANK_TOPICS` or paper-merit leaderboard changes;
- cockpit redesign/content changes;
- scheduler/cron/LaunchAgent changes;
- Git add/commit/push/merge;
- deploy or service restart if source application does not settle automatically;
- external submission.

Please reply with a concise ACK or blocker only. No file write or execution is requested from Hwao.
