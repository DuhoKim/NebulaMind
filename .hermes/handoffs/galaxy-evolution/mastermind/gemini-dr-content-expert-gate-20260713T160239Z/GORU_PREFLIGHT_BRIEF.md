# Goru local-only canary preflight brief

Packet: `gemini-dr-content-expert-gate-20260713T160239Z`
Status: NOT ARMED

Read:

- `USER_DIRECTION_AND_BOUNDARIES.md`;
- `HWAO_ONE_CANARY_PLAN.md`;
- the exact read-only Gate B and Gate A inputs named in Hwao's plan.

Perform only local mechanical preflight. No browser, network, agents/subagents, account/quota UI, API, or product/live-root access.

## Required outputs

1. Extract exactly the text between Hwao plan's BEGIN/END paste sentinels, excluding the sentinel lines, to `prompt/GE_COMPARABILITY_CANARY.md`.
2. Write its SHA-256 to `prompt/GE_COMPARABILITY_CANARY.sha256`.
3. Write `preflight/GORU_PREFLIGHT.md` reporting exact checks and evidence:
   - source input hashes match Hwao's pins;
   - prompt starts with `# Deep Research request` and ends with the required completion marker;
   - request ID appears as required;
   - exactly eight enumerated comparisons exist;
   - the four-token `SELECTION_MATCH` vocabulary is present exactly as contracted;
   - prompt-level completion marker appears exactly once;
   - output sequence, table columns, correction-bullet minimum rows, ledger rules, wording bans, uncertainty and fraction qualifiers, advisory/quarantine boundary, and no-edit lock are present;
   - accepted Gate A capture script actual SHA-256 is recomputed and recorded;
   - marker state is exactly one zero-byte `NOT_ARMED*`, zero `TORI_ARMED*`, zero capture/void markers;
   - expected-capture checklist is complete.
4. If all checks pass, create zero-byte `markers/GORU_PREFLIGHT_GREEN_20260713T160239Z`; otherwise create only zero-byte `markers/GORU_PREFLIGHT_NOT_GREEN_20260713T160239Z` and state blockers.
5. End the report with standalone `GORU_CONTENT_DR_PREFLIGHT_DONE`.

Do not edit Hwao's plan or any completed Gate A/B packet. Do not arm, submit, start, or capture Deep Research.
