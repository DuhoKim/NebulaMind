# Teach autopilots to use Gemini web/app safely

Marker: GEMINI_WEB_AUTOPILOT_TEACHING_PACKET_20260707T134324Z
Author: Tori-director
Time: 2026-07-07T13:43:24Z / 2026-07-07 22:43:24 KST

## Rule 0 — what Gemini web/app is for

Gemini web/app is an advisory outside-review lane for high-leverage cognitive work. It is not a general executor.

Use it for:
- one-packet critique of Galaxy Evolution method status;
- dashboard/operator UX review;
- red-team review of a readiness packet;
- boundary matrix / caveat list / missing-risk analysis;
- human-readable prose or report clarity review.

Do not use it for:
- mechanical counts, marker checks, file inventories, or static audits that Goru/scripts can do;
- source-of-truth verification without local reconciliation;
- DB/API/pages/live publish/deploy/git/cron/cloud/account/billing/OAuth/secrets;
- unattended multi-packet loops.

## Routing rule

1. If task is mechanical/read-only local inspection -> use Goru/Antigravity panes.
2. If task is repo truth, implementation, reproducibility, or tests -> use local tools/Kun/Lana as appropriate.
3. If task is outside judgment on a compact packet -> prepare Gemini web/app packet.
4. If no fresh supervised browser approval -> manual paste/capture only.
5. If fresh supervised one-packet approval exists -> one prompt only, capture output, verify marker, stop.

## Manual Gemini web/app loop

Autopilot may prepare artifacts without opening a browser:

1. Create a run dir under `/Users/duhokim/HermesOps/reports/YYYY-MM-DD/<topic>/web-gemini-loop-<timestamp>/`.
2. Write `WEB_GEMINI_PROMPT_001.md` from the template.
3. Include a unique standalone marker.
4. Copy prompt to clipboard/tmux buffer if helpful.
5. Wait for user/supervisor to paste into Gemini web/app and copy the answer.
6. Capture clipboard to `WEB_GEMINI_OUTPUT_001.md` with metadata: bytes, lines, sha256, marker_present.
7. Write `WEB_GEMINI_INTEGRATION_001.md` that distinguishes useful suggestions from local corrections.
8. Feed only the integration note back into autopilot/Hwao decisions.

## Supervised one-packet pilot loop

Only after explicit approval phrase in `NEXT_APPROVAL.md`:

- Use a fresh child Hermes session with only `computer_use` exposed.
- Do not use terminal/file/web/cron/cloud/API tools inside the child.
- Do not inspect browser profiles, cookies, tokens, keychain, credentials, or passwords.
- Capture Gemini app/page, paste one prompt, wait, capture generated answer, stop.
- Parent process writes all artifacts and verifies output.

## Output acceptance rules

A run is accepted only when all are true:
- Generated answer contains the required marker.
- Marker appears in Gemini's answer, not only in the prompt text.
- Captured output is not prompt-only.
- Output metadata has bytes, lines, sha256, capture time, marker_present=true.
- Integration note reconciles claims against local repo/artifacts.
- Safety ledger says no API/GCP/billing/OAuth/secrets/account/browser drift, DB, deploy, git, cron, or publication.

## Stop rules

Stop immediately on login, 2FA, CAPTCHA, payment, API key, GCP/project/billing, OAuth code, token, cookie, password, account-change prompt, URL drift, UI uncertainty, prompt-only capture, missing marker, or any computer_use action error/denial.

## Current reusable prompt packet

The already prepared prompt from the previous step lives at:
`/Users/duhokim/HermesOps/reports/2026-07-07/galaxy-evolution-web-gemini-loop-20260707T124934Z/WEB_GEMINI_PROMPT_001.md`

If clipboard is needed:
`pbcopy < /Users/duhokim/HermesOps/reports/2026-07-07/galaxy-evolution-web-gemini-loop-20260707T124934Z/WEB_GEMINI_PROMPT_001.md`

## For Hwao/autopilot

Treat this packet as a standing teaching artifact. It authorizes preparing Gemini web/app packets and asking for the next gate. It does not authorize autonomous browser execution by itself.

GEMINI_WEB_AUTOPILOT_TEACHING_PACKET_20260707T134324Z
