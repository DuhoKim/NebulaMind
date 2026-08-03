# Hwao standing brief — RT Gemini-web Deep Research sidecar

Marker: RT_GEMINI_WEB_DEEP_RESEARCH_STANDING_BOARD_BRIEF_20260708T115334Z

User direction: “can you use deep research of Gemini-web? if so, please let RT autopilots leverage that to enhance quality.”

## Decision

Yes, but only as a supervised, advisory sidecar. RT autopilots should leverage Gemini-web / Deep Research for high-leverage research-topic quality improvements, especially literature/status-map breadth, missing prior-study axes, survey/data-plan feasibility, and skeptical overclaim review.

## Standing protocol

Use:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/gemini-web-deep-research/RT_GEMINI_WEB_DEEP_RESEARCH_PROTOCOL.md`

Prompt template:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/gemini-web-deep-research/templates/GEMINI_WEB_RT_PROMPT_TEMPLATE.md`

Request template:
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/gemini-web-deep-research/templates/RT_GEMINI_WEB_REQUEST_TEMPLATE.md`

## How method autopilots should use it

When an RT order/page remains too generic, under-sourced, or not journal-quality:
1. Method Hwao/director writes a request packet under `gemini-web-deep-research/requests/`.
2. Stop there for Gemini-web. Do not open Gemini, use browser automation, configure API/GCP/billing/OAuth, or handle secrets.
3. Tori/Hwao runs one supervised Gemini-web/Deep Research packet or asks the user to run/paste it manually.
4. Tori verifies/captures output and writes an integration packet under `outputs/` + `integrations/`.
5. Method lanes may consume only verified integration artifacts, and only as advisory source-discovery/status-map input.
6. Any scientific claim, source link, numeric result, DOI/ADS/arXiv ID, or prior-study statement must still be verified locally/publicly before entering RT pages.

## Controller update already done

`tools/galaxy_evolution_autopilot.py` dispatch prompts now mention this sidecar protocol for method Hwao, director, and idle-continuation prompts. `python3 -m py_compile` and `self-test` passed; dry-run dispatch rendered all four target lanes.

## Hard gates remain closed

No product DB/SQL, `/api/pages`, page_versions/live wiki publish, trust recompute, deploy/restart, git, cloud/GCP/API/billing/OAuth/token/secrets, browser automation by autopilot panes, cron, or Method3 P3 binding.

Action for Hwao-director: treat this as a standing RT quality protocol. No Gemini run is requested right now unless a new RT quality order asks for it; just acknowledge or incorporate it into the next RT order planning.

RT_GEMINI_WEB_DEEP_RESEARCH_STANDING_BOARD_BRIEF_20260708T115334Z
