# GORU HOLD — revised live driver requires Tori review before execution

Your first driver failed closed before any browser write because its broker requests used `action` instead of required `op` and expected the wrong response shape. Finish saving the revised source, but do not execute it yet.

Tori must review the exact revised file for:

- broker request/response correctness and denial handling;
- page-only challenge detection and broker freeze path;
- exact target rediscovery before every write;
- target and account-submission lease heartbeat/release in every failure path;
- unique Deep Research mode selection and submit button identity;
- completion detection that does not save a partial response;
- exact conversation ID/title/submit-UTC custody;
- verified result-save and ledger `VERIFY_OK` before any deletion.

Do not launch the revised driver until Tori sends a new review-pass dispatch. No live action or lease request meanwhile.

GORU_DR_DRIVER_REVIEW_HOLD_20260714
