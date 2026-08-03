# Tori -> Goru dispatch

Target: goru-agy-pilot-resume:0.0
Timestamp: 20260714T082256Z

## Payload

```text
GORU / ANTIGRAVITY BRIEF — Tori-dispatched — 20260714T082256Z

Use Gemini/Antigravity quota for this scoped Tori helper task.

Safety boundary:
- Stay inside the explicit scope in the brief below.
- Prefer read-only mechanical checks, counts, inventories, source maps, repro checks, and draft reviews.
- Do not do DB writes, deploy/restart, git commit/push/merge, cloud/GCP/Gemini API config changes, secrets inspection, or live publication unless the user gives a separate explicit gate.
- If command permission is needed, ask for the smallest exact command; Tori will approve only scope-matching safe commands.
- Write/report exact files, counts, commands, and blockers. Do not self-certify unverified external facts.

Assigned brief:

# GORU DR PREFLIGHT CORRECTION — inspect the Mac Pro, not the old Studio sandbox

The proposed blocker append was denied because it used the wrong host and target. `sandbox/profiles/writerA` is an old isolated viability profile on the Mac Studio; it is not the live DR target.

Canonical DR host:

- Mac Pro direct Thunderbolt SSH: `duhokim@169.254.100.1`
- Pin the known identity with `-o HostKeyAlias=100.122.78.110 -o StrictHostKeyChecking=yes -o BatchMode=yes`.

Perform only a read-only Mac Pro preflight now:

1. Confirm hostname.
2. Enumerate Chrome process command lines and listening local TCP ports sufficient to determine whether a CDP endpoint already exists. Do not read profile files, cookies, tokens, credentials, environment secrets, or browser databases.
3. If a CDP endpoint exists, query only `/json/version` and `/json/list` metadata needed to identify the exact Gemini/Deep Research page; do not navigate or mutate yet.
4. If no CDP endpoint exists, report that exact blocker to Tori before any launch. Do not launch Chrome with an existing/default profile, copy a profile, install software, or append a final ledger blocker yet.

The account-submission and target leases remain required before writes. The epoch-22 resume remains valid unless a real page-level challenge appears.

GORU_DR_PREFLIGHT_CORRECTION_MAC_PRO_20260714

Done marker: TORI_GORU_DISPATCH_DONE_20260714T082256Z

```
