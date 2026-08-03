# Gemini-web GUI sidecar status — current RT professionalization

Marker: GEMINI_WEB_GUI_BLOCKED_CURRENT_RT_20260708T120000Z

Attempted path: supervised Gemini-web browser packet for `RT_GEMINI_WEB_DEEP_RESEARCH_CURRENT_TOPICS_20260708T120000Z`.

Result: BLOCKED for GUI capture, not for account/billing/API.

Evidence:
- `hermes computer-use doctor` returned OK for cua-driver 0.7.0, Accessibility, Screen Recording, AX, and ScreenCaptureKit.
- `computer_use capture app=screen` returned 0x0 and 0 interactable elements.
- `computer_use capture app='Google Chrome'`, `app='Chrome'`, `app='Safari'`, and `app='com.google.Chrome'` returned 0x0 or no on-screen window.
- `open -g -a 'Google Chrome' https://gemini.google.com/app` completed, but `computer_use` still returned 0x0 for Chrome.

No login, payment, API/GCP/billing/OAuth/token/cookie/profile screen was clicked or handled. No prompt was submitted to Gemini-web.

Fallback for this run: use the authenticated Gemini/Antigravity (`agy`) lane with the same prompt as an advisory Gemini research sidecar, then verify sources locally/publicly before revising RT pages. This is not a substitute for a real Gemini-web Deep Research transcript; it will be labeled as `GEMINI_AGY_FALLBACK_ADVISORY` unless Gemini-web is later available.

GEMINI_WEB_GUI_BLOCKED_CURRENT_RT_20260708T120000Z
