# RT autopilots — Gemini-web Deep Research sidecar protocol

Marker: RT_GEMINI_WEB_DEEP_RESEARCH_SIDECAR_PROTOCOL_V1
Created: 2026-07-08T11:53:34Z
Owner model: Hwao-led board; Tori/Hermes verifies and executes only bounded/supervised steps.

## Purpose

Use Gemini-web / Deep Research only to improve research-topic (RT) quality: broader literature awareness, missing prior-study axes, review/status-map context, survey/data-plan realism, and skeptical checks on proposed study design.

Gemini-web output is advisory source-discovery and critique. It is not accepted evidence, not product claim binding, and not permission to publish or mutate NebulaMind data.

## Safety boundary

Allowed:
- supervised one-packet Gemini-web / Deep Research prompt generation;
- local prompt/output/integration artifacts under this directory;
- read-only local/public verification of cited sources;
- method-local docs/static proposal revisions only after Hwao/Tori verification.

Not allowed from autopilot panes:
- no browser automation by Hwao/Lana/Goru/Kun panes;
- no API key, GCP, Vertex, billing, OAuth code, token, cookie, account, or project setup;
- no product DB/SQL, `/api/pages`, page_versions, live wiki publish, trust recompute, deploy/restart, git, cron, or cloud changes;
- no claim/source/cite binding from Gemini output alone.

## How RT autopilots request Gemini-web help

When a research-topic page remains too generic, too casual, or under-sourced, the method Hwao or director may write a request packet under:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/gemini-web-deep-research/requests/`

Required request fields:
1. `request_id` and marker.
2. Method(s): M1/M2/M3 or cross-method.
3. Current RT artifact paths.
4. Exact topic/cards to improve.
5. Existing source-basis links/claim IDs that must not be contradicted.
6. The question Gemini should answer.
7. Expected output shape.
8. Explicit safety locks copied from this protocol.

Then stop. The autopilot must not open Gemini-web itself.

## How Tori/Hwao runs the sidecar

Preferred safe path:
1. Convert the request into a self-contained prompt using `templates/GEMINI_WEB_RT_PROMPT_TEMPLATE.md`.
2. Run a supervised one-packet Gemini-web / Deep Research session, or have the user paste/run it manually.
3. Save the complete output under:
   `.../gemini-web-deep-research/outputs/`
4. Write metadata: bytes, sha256, marker present, capture method, and safety ledger.
5. Write an integration note under:
   `.../gemini-web-deep-research/integrations/`
6. Only after local/source verification, hand the verified integration packet back to RT autopilots.

## Integration rules

Treat Gemini-web output as useful but untrusted until verified:
- Verify every cited paper/source link before use.
- Separate review/status backbone, primary studies, simulations, surveys, and commentary.
- Demote uncited claims to `UNCITED_NOT_USABLE` unless independently verified.
- Do not import numeric results unless the source or existing local ledger supports them.
- Do not use Gemini-generated DOI/ADS/arXiv IDs until checked.
- Prefer astronomy corpus flow: papers → claim/status ledger → research-status/debate map → prose/research-topic cards.
- If Gemini identifies missing literature categories, route them to ADS/local source acquisition or a status-map shortlist packet before prose when the claim would be substantive.

## Minimum output expected from Gemini-web

For each RT card/topic:
- prior-study findings with source links and scope limits;
- what remains unknown;
- recommended data/survey/instrument families tied to measurements;
- analysis/test and decision criterion;
- overclaim risks;
- key papers/reviews to verify locally;
- `DO_NOT_USE_UNVERIFIED` list for claims that need checking.

## When to use

Use for high-leverage RT quality improvements:
- journal-quality polish/review of proposed research topics;
- finding missing prior-study families or review papers;
- checking if a study design sounds publishable;
- identifying survey/data feasibility gaps;
- skeptical review of overclaiming.

Do not use for mechanical counts, static safety, link checking, file maps, or marker checks; those remain Goru/Kun/local-script tasks.

RT_GEMINI_WEB_DEEP_RESEARCH_SIDECAR_PROTOCOL_V1
