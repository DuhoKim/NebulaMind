# Tori dispatch — Goru Phase 0 only

Packet: `goru-options-pilot-20260711T102412Z`
UTC: 2026-07-11T10:34:20Z

Read first:

- `DIRECTION.md`
- `MANIFEST.json`
- `OPTIONS_DECLARATION_TEMPLATE.md`
- `TEST_DESIGN.md`
- `WAVE_LEDGER.md`

## Required sequence

1. Append exactly one `GORU_ACK` row to `WAVE_LEDGER.md`, quoting verbatim:
   - allowed role: `Phase-0 declaration; implementing transport-free option shims + harness runs under goru/ and tests/results/`
   - banned role: `Anything in §0; touching live services; editing fixtures/expected verdicts`
2. Fill `goru/OPTIONS_DECLARATION.md` using every field in `OPTIONS_DECLARATION_TEMPLATE.md`, one block for each named option.
3. Declare only the safe surrogate lane:
   - OPTION-1: localhost/mock with synthetic token only, or `PAPER_ONLY_NOW` if inseparable from banned transport.
   - OPTION-2: localhost/file fixture with fresh ephemeral profile only if its existing stack is available without install; otherwise `PAPER_ONLY_NOW`.
   - OPTION-3: browserless dry-run decision logic plus documentation-only discovery; no GUI/display/System Events invocation.
4. List every proposed implementation file and intended entrypoint, but DO NOT create implementation files yet.
5. Hash `goru/OPTIONS_DECLARATION.md`, append one `OPTIONS_DECLARED` ledger row, and create exactly one zero-byte `GORU_OPTIONS_DECLARED_<UTC>Z` marker.
6. Reply with the exact marker name.

## Hard boundary

Phase 0 only. Do not create shims, run fixtures, start localhost servers, launch any browser, inspect installed browser stacks, read profiles/cookies/secrets, invoke System Events/Accessibility/display tools, install anything, contact Google/Gemini or any external host, execute the weekend macro, or modify any pinned fixture/expected-verdict file. All writes stay in this packet root.
