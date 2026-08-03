# Goru brief — C1r sealed-HTML fixtures and deterministic counts

Read first:
- `HWAO_IMPLEMENTATION_DIRECTION.md`
- `ROLE_TABLE.md`
- immutable sealed inputs under `../gemini-dr-revised-canary-20260712T045317Z/`

Role: mechanical fixture/count lane only. No contract judgment and no implementation code.

Allowed writes only under this packet's `fixtures/` directory.
First write `fixtures/GORU_ACK` containing exactly:
`GORU_C1R_REPAIR_ACK_20260713T010203Z`

Required outputs:
1. byte-copy the minimum sealed inputs required for offline tests: rendered HTML, body text, contract spec, submitted prompt/contract, and original structured capture/result;
2. `GORU_FIXTURE_MANIFEST.json` with source path, source sha256, copied path, copied sha256, byte-identical boolean;
3. `EXPECTED_DOM_FACTS.json` mechanically derived from the sealed HTML, pinning all facts listed in Hwao direction §2 and identifying exact S1/S2/S3/S4/S5/ledger units;
4. one deliberately corrupted HTML fixture where a repeated source index is paired with two distinct ledger URLs, plus a manifest recording the deterministic minimal edit;
5. `GORU_FIXTURES_DONE` containing exactly `GORU_C1R_REPAIR_FIXTURES_DONE_20260713T010203Z`.

Use only local file reads and local scripts. Do not rely on external sources. Stop and write a `BLOCKED.md` if real-HTML counts disagree with Hwao's pins; do not silently adjust expectations.

Hard scope: packet-only writes; sealed inputs immutable; no browser/network/live Gemini/DB/wiki/product/deploy/restart/git/cron/dashboard/public-cockpit action. Stop before 40% of the current Antigravity five-hour window.
