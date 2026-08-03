# PROMPT SCHEMA CHECK

- PASS: SHA-256 matches MANIFEST.json.
- PASS: BEGIN/END sentinels present and match REQ ID.
- PASS: C1-C8 contract labels present.
- PASS: Request ID and completion marker match manifest.
- PASS: Marker instruction specifies exactly once and final non-empty line.
- PASS: Canary is the only manifest run and run-count cap is 1.

Verdict: PASS
