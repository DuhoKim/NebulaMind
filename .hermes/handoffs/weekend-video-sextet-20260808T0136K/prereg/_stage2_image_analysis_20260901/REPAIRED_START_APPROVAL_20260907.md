# DUHO APPROVED ONE REPAIRED PROSPECTIVE START (2026-09-07 21:08:35 KST)
**"Approve one repaired start"** — provider UTC **2026-09-07T12:06:06.582636Z** (21:06:06 KST), create_time `1788782766.582636`, message `msg_01a07bc2-e9f6-7de0-b19f-95f2abf5e8bf`, turn `01a07bb7-9006-77a0-87f2-ec34630f7942`, response_item 3893, question id `["request_user_input_async","call_ttP2rdA06mPS9Pvgvh41mV65",0]`.
**Approves exactly one** prospective start on the repaired candidate, digests re-verified by me against the approval before use:
| file | approved digest | verified |
|---|---|---|
| `_repair_candidate/RUNTIME_PINS_A1_CORE.json` | `d1cd15d2ced15a65145fb05283447ab1d3a51e1cda074885d707f9343e00fad6` | equal |
| `_repair_candidate/INPUT_MANIFEST_A1_CORE.json` | `f4f782be7e872f9ebacdb63db501096916422c419f729fa614dc288e624e3878` | equal |
| `_repair_candidate/INPUT_FREEZE_C_20260907.json` | `58f72730b1b9f21277e0e2c2e6676fe574502f93bb15465c3fe22def1df1a658` | equal |
A1, run_path and the scientific rules are unchanged. **The originals stay frozen** (CORE `e9222abf…`, C `bbc08cd6…`, A1 `6b9ecc79…`) and **both failed journals are preserved**. Execution goes to a **distinct new journal, `OUT_A1_REPAIRED/`**. **Exposed rounds 6440756 and 6444980 will not be reused.** No extra validation and no automatic further restart is authorized.
**This commit is the new INPUT anchor publication**; the designation command is ready and runs immediately against its server-side timestamp.
