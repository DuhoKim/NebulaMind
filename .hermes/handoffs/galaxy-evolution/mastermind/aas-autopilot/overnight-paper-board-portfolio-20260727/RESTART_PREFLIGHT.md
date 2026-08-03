# Controlled Next Restart Preflight — Staged Paper Board Audit Report

Prepared independently by Tori after the user directed Tori not to wait on busy Hwao.

Status: `EXECUTED__PASS`

## Why a restart is required

The canonical report source already exists as one new additive file in the rich live frontend public root and matches the preflighted candidate byte-for-byte:

- Report marker: `PAPER_BOARD_AUDIT_REPORT_20260728_V1`
- Bytes: 12,221
- SHA-256: `ea96ec76d95e9530eede0c5f2eaad5bdb8db667c7f6b1f400c791cfd956b3c7a`
- Intended clean URL: `https://nebulamind.net/agent-reports/paper-board-audits/overnight-paper-board-portfolio-20260728.html`

The clean URL is currently HTTP 404 because the running Next 14.2.35 process started before the public file existed. No build is needed; Next only needs to reload its public-file manifest.

## Live service identity

- launchd label: `com.nebulamind.frontend`
- launchd state: enabled, KeepAlive, PID 82773 at preflight
- child: Next server PID 82777, port 3000
- working directory: rich live frontend
- stdout/stderr: existing frontend log files
- process is launchd-managed, not a tmux or ad-hoc server

## Pre-restart health baseline

Observed before any restart:

| Probe | State |
|---|---:|
| `/` | HTTP 200, 20,977 bytes |
| `/lab` | HTTP 200, 68,111 bytes |
| `/api/lab/runs` | HTTP 200 JSON, 5,721 bytes |
| staged clean report URL | HTTP 404, 22,072-byte Next error page |

## Single authorized action

After explicit approval only:

`launchctl kickstart -k gui/$(id -u)/com.nebulamind.frontend`

This restarts the existing launchd-managed service without changing code, build output, config, environment, or routing.

## Verification ladder

1. Confirm old PID changes and launchd reports a live replacement.
2. Poll local `127.0.0.1:3000/` until HTTP 200 or a bounded timeout.
3. Verify local `/lab` and `/api/lab/runs` preserve HTTP 200 and expected content types.
4. Verify public `/`, `/lab`, and `/api/lab/runs` remain healthy.
5. Fetch the clean report URL with cache-busting through direct HTTP, web extraction, and browser rendering.
6. Require HTTP 200, HTML content type, exact report marker, `NO ACTIVE EXECUTION PHRASE`, all three packet status strings, no private path leakage, and no script/form/action surface.
7. Record served bytes/hash and visual representation in `PUBLICATION_RECEIPT.json`.

## Fail-closed conditions

- If launchd does not produce a live process, local root does not return 200, or existing public routes regress, stop and report the failure. Do not build, change config, alter Cloudflare/Tailscale routing, or touch another service.
- If the app is healthy but the report remains 404, stop. Do not perform a second restart or build without a new gate.
- No paper/PDF/card/Lab/cockpit/wiki/DB/Git change is part of this restart.

## Required approval

`APPROVE ONE CONTROLLED NEXT RESTART FOR THE STAGED PAPER-BOARD AUDIT REPORT; VERIFY APP HEALTH + CLEAN URL; NO OTHER DEPLOYMENT.`

## Execution result

- Explicit approval received.
- One launchd kickstart executed at 2026-07-28 00:00:51 KST.
- Frontend PID changed from 82773 to 29257; local root returned 200 within two polls by 00:00:53 KST.
- Local `/`, `/lab`, `/api/lab/runs`, and the report returned 200.
- Public `/`, `/lab`, `/api/lab/runs`, and the clean report URL returned 200.
- Origin report bytes: 12,257; SHA-256 `0d1ec2e6db585f53c6bc21aa5e430abce9537b34ce2a9b13fdc6245d20b9ce10`.
- Web extraction and browser rendering showed the complete report without clipping, overlap, missing glyphs, or broken layout.
- No build, config, routing, paper, Lab, cockpit, wiki/DB, project-source, or Git action occurred.
