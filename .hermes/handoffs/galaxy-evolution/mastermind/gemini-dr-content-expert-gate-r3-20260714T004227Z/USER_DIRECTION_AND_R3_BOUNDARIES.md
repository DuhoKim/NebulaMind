# User direction and R3 boundaries — fresh-process Deep Research canary

Packet: `gemini-dr-content-expert-gate-r3-20260714T004227Z`
Relationship: **supersedes, does not resume** R2 `gemini-dr-content-expert-gate-r2-20260714T002603Z`
Status: NOT ARMED

The user asked Tori to resume without closing the user's current window and previously directed that the content use Deep Research. R2 completed all local preflight, but its detached Tori browser process lost its process-local computer-use bridge before any UI mutation. The one permitted UI configuration sequence was not started or consumed; no prompt was pasted or submitted and no quota was consumed.

R3 changes only browser-process custody:

- the failed detached R2 Tori process must be exited and its tmux session removed before R3 starts;
- one newly launched detached Hermes/Tori process becomes the sole browser owner;
- it must read the complete R3/R2 custody chain and execute the Deep Research + highest-compatible-model + maximum-thinking configuration, verification, arming, one submission, one start, capture, and validation in its first bounded task turn;
- no other browser process or fallback adapter may act concurrently.

The user-facing Terminal window must not be closed or replaced. A detached tmux worker is the approved recovery mechanism.

The frozen prompt remains byte-identical and pinned to SHA-256 `4d57fd71b49e74760cc1be1acc6fb50ce1e777b4c43907612830b346b471f42a`. All R2 hard stops and prohibited actions carry unchanged. No DB/wiki/product/trust mutation, publication, dashboard edit, git write, deploy/restart, cron, billing/OAuth/account action, alternate profile, API fallback, quarantine release, or automatic prose application.

USER_CONTENT_DR_R3_FRESH_PROCESS_APPROVED_20260714T004227Z
