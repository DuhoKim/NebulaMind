# LIVE_DIRECTION — Goru Option-3 Live Pilot Authorization

Packet: `goru-live-pilot-20260711T210500Z`
Author: Duho

## 1. Safety Clearance
I, Duho, officially declare that the overarching `Google unusual-traffic verification` hard stop is CLEARED. 
The joint canary packet `gemini-web-joint-burn-recovery-20260711T100139Z` is officially ARMED.
This packet authorizes a highly bounded live test of Option 3.

## 2. Environment Provisioning
This test is authorized to run ONLY within the provisioned isolated environment.
- **Environment:** Dedicated 'goru-test' Local User Account on the host Mac.
- **Permissions:** Accessibility and System Events have been explicitly granted to the terminal process executing this packet in the isolated environment.
- **Profile:** A clean, isolated instance of Google Chrome with a dedicated, low-privilege test account is active. No host profile data is exposed.

## 3. Strict Bounds
Goru is authorized to execute the provided AppleScript mechanics to drive the Chrome UI.
- **Maximum Execution Time:** 300 seconds.
- **Maximum Actions:** Exactly ONE prompt submission.
- **Target Query:** "What are the latest advancements in solid-state batteries as of 2026?"
- **Fail-Closed:** If the UI state is UNKNOWN or does not match the expected flow, the AppleScript must immediately abort. No evasion plugins or stealth binaries are allowed.

## 4. Execution Protocol
Goru will invoke `applescript_scaffold.applescript` using `osascript`. 
Upon completion or abort, Goru will capture the result and append it to this packet's ledger.
