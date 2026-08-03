# Tori -> Goru dispatch

Target: goru-agy-pilot-resume:0.0
Timestamp: 20260714T093826Z

## Payload

```text
GORU / ANTIGRAVITY BRIEF — Tori-dispatched — 20260714T093826Z

Use Gemini/Antigravity quota for this scoped Tori helper task.

Safety boundary:
- Stay inside the explicit scope in the brief below.
- Prefer read-only mechanical checks, counts, inventories, source maps, repro checks, and draft reviews.
- Do not do DB writes, deploy/restart, git commit/push/merge, cloud/GCP/Gemini API config changes, secrets inspection, or live publication unless the user gives a separate explicit gate.
- If command permission is needed, ask for the smallest exact command; Tori will approve only scope-matching safe commands.
- Write/report exact files, counts, commands, and blockers. Do not self-certify unverified external facts.

Assigned brief:

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

Done marker: TORI_GORU_DISPATCH_DONE_20260714T093826Z

```
