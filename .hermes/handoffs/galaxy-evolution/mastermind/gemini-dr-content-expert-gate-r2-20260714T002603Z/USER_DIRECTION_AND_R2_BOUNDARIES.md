# User direction and R2 boundaries — Deep Research content canary

Packet: `gemini-dr-content-expert-gate-r2-20260714T002603Z`
Relationship: **supersedes, does not resume** `gemini-dr-content-expert-gate-20260713T160239Z`
Status: approved for one fresh canary preparation; NOT ARMED

The user explicitly directed: **“for the content use Deep Research.”** The first packet stopped before any browser mutation because the authenticated Gemini composer was initially on Flash-Lite and Deep Research was not selected. Using Deep Research necessarily requires a reversible pre-submit UI mode/model selection.

For this R2 packet, Tori may perform exactly one bounded pre-submit configuration sequence in the authenticated Gemini UI:

1. select Deep Research mode;
2. select the highest available Gemini model tier compatible with Deep Research;
3. select maximum thinking/effort if the UI exposes it;
4. then verify and record mode/model/quota/tab state before arming.

If the required controls are unavailable, ambiguous, lead to login/verification/billing/upsell, or create operator doubt: stop NOT_ARMED. This is not permission to change account settings, purchase quota, use alternate profiles, handle verification/CAPTCHA, or use an API.

The original prompt content is carried forward byte-for-byte with SHA-256 `4d57fd71b49e74760cc1be1acc6fb50ce1e777b4c43907612830b346b471f42a`. One new conversation/tab is permitted only if the Gemini UI requires it for Deep Research; Tori must pin the exact identity after mode selection and before paste. One submission, one start, no retry.

All original hard boundaries remain: no DB/wiki/product/trust mutation, publication, dashboard edit, git write, deploy/restart, cron, billing/OAuth/account action, quarantine release, or automatic prose application.

USER_CONTENT_DR_R2_MODE_SELECTION_APPROVED_20260714T002603Z
