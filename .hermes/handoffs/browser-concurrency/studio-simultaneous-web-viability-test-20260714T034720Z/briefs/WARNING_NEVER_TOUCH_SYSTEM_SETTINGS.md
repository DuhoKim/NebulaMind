# ⛔ HARD BOUNDARY — agents must NEVER touch macOS System Settings (Duho, 2026-07-15)

An automation lane on the Studio strayed out of the browser into **System Settings** and toggled Screen Sharing **"anyone may request remote control" ON**, then left Settings frozen. This widened a real remote-control exposure (Screen Sharing listens on `*:5900`, all interfaces) and coincided with Universal Control dropping.

**Every agent / CUA / browser-concurrency lane, effective immediately:**
- **NEVER** open, navigate, or change **macOS System Settings / System Preferences** — especially **Sharing, Screen Sharing, Remote Management, Remote Login, Privacy & Security, Accessibility, Continuity/Handoff, Bluetooth, Wi-Fi, Users & Groups**.
- Keep all screen/keyboard/mouse automation **strictly inside the target app window** (the Flow/browser). Do not click anything in the macOS menu bar, Settings, or Finder that changes system state.
- If a task appears to require an OS-level permission, **STOP and hand off to Duho** — only a human grants OS permissions.
- Treat any System Settings / security / account dialog like an account challenge: **do not interact; hold for the human.**

Violating this is a stop-the-lane event. If you have code/skill steps that open Settings or change sharing/permissions, remove them and report.
