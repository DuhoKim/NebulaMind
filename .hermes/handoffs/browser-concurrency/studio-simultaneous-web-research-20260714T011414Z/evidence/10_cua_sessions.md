# cua-driver multi-session evidence
URL: https://github.com/trycua/cua/issues/1777
Accessed: 2026-07-14
Product/version: official cua-driver issue/merged-work record opened 2026-05-31

> #1776 landed the foundation — proxy-minted `session_id` in the request envelope, session-owned recording, per-session config (macOS), and `session_end`/disconnect cleanup.

> The macOS agent-cursor overlay was effectively one shared cursor ... Concurrent MCP sessions clobbered each other on it last-writer-wins.

> Each `cua-driver mcp` proxy now opens ONE long-lived control connection to the daemon at startup.

Status: PARTIAL. The official project records multi-session engineering and fixes, but does not guarantee that two agents may safely write to the same browser target. Current installed behavior still needs canary verification.
