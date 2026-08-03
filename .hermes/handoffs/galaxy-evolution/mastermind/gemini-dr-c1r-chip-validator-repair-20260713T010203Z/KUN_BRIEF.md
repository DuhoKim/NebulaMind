# Kun brief — C1r repair custody and reproducibility preflight

Read first:
- `HWAO_IMPLEMENTATION_DIRECTION.md`
- `ROLE_TABLE.md`
- sealed `../gemini-dr-revised-canary-20260712T045317Z/runs/c1r/RUN_RECEIPT.json`
- sealed input artifacts and validator tests

Role: reproducibility/custody verifier. Do not implement capture or validator behavior.

Allowed writes only:
- `receipts/KUN_ACK`
- `receipts/KUN_IMMUTABLE_INPUT_RECEIPT.md`
- `receipts/KUN_PREFLIGHT.json`
- `tests/run_all.sh`

First write ACK containing exactly:
`KUN_C1R_REPAIR_ACK_20260713T010203Z`

Tasks:
1. hash every sealed artifact used by the repair and reconcile available hashes with RUN_RECEIPT/custody receipts;
2. record a write-scope baseline for the sealed packet and root-cause packet;
3. create a packet-local deterministic `tests/run_all.sh` harness that runs Node capture tests and Python validator/integration tests when present, never writes outside this packet, and returns nonzero on any failure;
4. document the two-run byte-determinism gate and postflight immutability gate without weakening expected findings;
5. write preflight marker exactly `KUN_C1R_REPAIR_PREFLIGHT_DONE_20260713T010203Z` as final line of `KUN_IMMUTABLE_INPUT_RECEIPT.md`.

Hard scope: packet-only writes; sealed inputs immutable; no browser/network/live Gemini/DB/wiki/product/deploy/restart/git/cron/dashboard/public-cockpit action. Do not commit.
