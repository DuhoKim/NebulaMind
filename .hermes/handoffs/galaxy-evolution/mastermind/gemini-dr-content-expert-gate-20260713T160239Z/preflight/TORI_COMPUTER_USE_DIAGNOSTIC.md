# Tori computer-use bridge diagnostic

Packet: `gemini-dr-content-expert-gate-20260713T160239Z`
Decision: **NOT ARMED — process-local computer-use bridge loss**

Observed before any browser action:

- `computer_use list_apps`: zero apps.
- `computer_use capture app="Google Chrome" mode=som`: `0x0`, zero elements.
- `computer_use capture app="screen" mode=vision`: `0x0`, zero elements.
- `hermes computer-use doctor`: GREEN on cua-driver 0.7.1, macOS support, active MCP session, bundle identity, Accessibility, Screen Recording, AX reachability, ScreenCaptureKit, and one shareable display.

Classification: the driver and permissions are healthy, but this Hermes process has lost its computer-use bridge. The single-browser-owner contract requires a Hermes process relaunch followed by `--continue` and a fresh capture attempt before any authenticated-tab fallback or arming decision.

No managed/isolated browser, Apple Events fallback, alternate profile, API, browser action, prompt paste, tab creation, submission, Deep Research start, or quota consumption occurred. Root `NOT_ARMED` remains current.

TORI_CONTENT_DR_COMPUTER_USE_BRIDGE_BLOCKED_20260713T160239Z
