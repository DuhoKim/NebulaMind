# Gemini web/app autopilot teaching packet

Marker: GEMINI_WEB_AUTOPILOT_TEACHING_PACKET_20260707T134324Z
Author: Tori-director
Time: 2026-07-07T13:43:24Z / 2026-07-07 22:43:24 KST
Scope: teach autopilots how to use Gemini web/app safely. This packet does not execute browser automation.

## What this is

A docs-only control-plane packet for Hwao/Tori/autopilot lanes. It explains when Gemini web/app is useful, how to prepare one-packet prompt artifacts, how to capture and integrate output, and when to stop.

## Files

- `GEMINI_WEB_AUTOPILOT_TEACHING_PACKET.md` — human-readable policy/playbook.
- `rules/operator_state_machine.json` — machine-readable state machine.
- `rules/stop_conditions.json` — hard stop list.
- `templates/WEB_GEMINI_PACKET_TEMPLATE.md` — prompt template for one Gemini web/app packet.
- `templates/WEB_GEMINI_INTEGRATION_NOTE_TEMPLATE.md` — local reconciliation template.
- `CHILD_HERMES_COMPUTER_USE_OPERATOR_BRIEF_TEMPLATE.md` — only for a future supervised pilot.
- `scripts/disabled_gemini_web_operator.py` — disabled skeleton; exits without browser action.
- `NEXT_APPROVAL.md` — exact approval gate for the one-packet supervised pilot.
- `VERIFY_PREFLIGHT.json` — preflight manifest stating no browser execution happened.

## Current posture

Manual packet loop is allowed by the user's latest direction. Browser automation remains disabled until the one-packet supervised pilot phrase in `NEXT_APPROVAL.md` is explicitly approved.

GEMINI_WEB_AUTOPILOT_TEACHING_PACKET_20260707T134324Z
