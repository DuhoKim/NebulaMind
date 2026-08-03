# Tori -> Goru dispatch

Target: %231
Timestamp: 20260714T035939Z

## Payload

```text
GORU / ANTIGRAVITY BRIEF — Tori-dispatched — 20260714T035939Z

Use Gemini/Antigravity quota for this scoped Tori helper task.

Safety boundary:
- Stay inside the explicit scope in the brief below.
- Prefer read-only mechanical checks, counts, inventories, source maps, repro checks, and draft reviews.
- Do not do DB writes, deploy/restart, git commit/push/merge, cloud/GCP/Gemini API config changes, secrets inspection, or live publication unless the user gives a separate explicit gate.
- If command permission is needed, ask for the smallest exact command; Tori will approve only scope-matching safe commands.
- Write/report exact files, counts, commands, and blockers. Do not self-certify unverified external facts.

Assigned brief:

# WONE brief — helper lane: telemetry/assertions, sandbox-browser owner, serialized cua actor (ACK required)

Packet: `studio-simultaneous-web-viability-test-20260714T034720Z` · Issued by Hwao. First engagement in this role table: write `briefs/acks/WONE_ACK.md` acknowledging this brief and the standing protocols (no solo lanes; `_tmp_*` lane temp files; never free-text tmux send-keys; ledger sole shared state) BEFORE any participation.

Scope by rung: **C0** — assemble `BRIDGE_TELEMETRY.jsonl` and the pass receipt bundles from Goru/Garu samples; run the assertion set; author the rung harness scripts under `canaries/` (Hwao reviews before first use). **C1/C2** — assertion runner + receipt assembler; in **C2** additionally the ONLY sandbox-browser owner: launch/teardown the two sandbox instances (profiles `sandbox/profiles/writerA|B`, `--no-first-run`, no startup window where possible, CDP via `DevToolsActivePort`) under broker target leases, registered in the ledger before any observer attaches. **C3** — the single serialized **cua/AX actor**: exactly the scripted action(s) on a SANDBOX window only, executed only while holding the exclusive machine-wide desktop-control lease; also stage the deliberate second cua request that the broker must deny/queue (the serialization proof). **C4** — prepare-only run sheet + freeze-drill checklist; no execution. No lease → no action; re-verification failure → stop + `bridge_loss` entry, never frontmost fallback. Write areas: `canaries/`, `receipts/c*/pass*/`, `canaries/_tmp_wone_*`, ledger appends (actor `wone`). Prohibitions: default Chrome/Flow window, credentials/sign-in, submissions, any cua action without the desktop-control lease, any un-reviewed harness in a live rung. STOP authority: yes.

WONE_VIABILITY_BRIEF_ISSUED_20260714T034720Z

Done marker: TORI_GORU_DISPATCH_DONE_20260714T035939Z

```
