# USER ARCHITECTURE DECISION — DR on Mac Pro, Flow on Mac Studio

Packet: `studio-simultaneous-web-viability-test-20260714T034720Z`
Recorded UTC: 2026-07-14T07:22:54Z

User direction:

> Keep Deep Research work on the Mac Pro. The user will work separately on Flow on the Mac Studio with Yui.

## Operational assignment

- **Mac Pro:** Deep Research lane, coordinated by Hwao; Tori remains the DR correspondent/receipt verifier.
- **Mac Studio:** User-operated Flow lane with Yui as the Flow correspondent.
- **Primary inter-host path:** direct Thunderbolt Bridge (`169.254.100.1` Pro ↔ `169.254.100.2` Studio).
- **Tailscale:** recovery/out-of-band access only; no silent transport fallback inside an active canary or brokered browser action.
- **Broker authority:** one fail-closed authority on the Studio for any agent-controlled shared resources.

## Boundaries retained

- Separate browser processes/profiles/targets per writer.
- Exact target identity and lease required before every agent-controlled DOM/CDP write.
- Zero shared desktop-control assumption: any future CUA/AX/pointer/keyboard action is serialized per host.
- The account plane remains shared even though the machines are separate: quota, concurrent submissions, and challenge scope are not isolated by Thunderbolt or by separate profiles.
- Agent-controlled live submissions, quota spending, prompt/challenge handling, and Phase-IV same-account overlap remain separate explicit gates.
- The user's own Flow work on Studio is not to be inspected or manipulated unless the user explicitly asks.

## Execution state

This receipt records the routing decision only. It does not launch a Deep Research job, touch Flow, submit anything, or spend quota. XM-1 passes 2–3 remain held unless separately requested; the one successful XM-1 pass already established the mechanical split needed for this operational choice.

USER_DECISION_DR_PRO_FLOW_STUDIO_20260714T072254Z
