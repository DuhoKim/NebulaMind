# Tori admissibility review

Packet: `goru-options-pilot-20260711T102412Z`
UTC: 2026-07-11T10:39:20Z
Reviewer: Tori

## Integrity precheck

- All 15 read-only fixture/generator SHA-256 pins match `MANIFEST.json`.
- `GORU_OPTIONS_DECLARED_20260711T103649Z` exists and is zero bytes.
- `goru/OPTIONS_DECLARATION.md` is 7,408 bytes, SHA-256 `1da413cfa9a7a9fd2ef2e94636dd499476b858e0f96ac5efd34393a2b5937939`, matching the ledger.
- No implementation files existed at review time.
- Existing Python 3.9.6 modules, checked without network or installation: `requests=true`, `playwright=true`, `bs4=true`.

## OPTION-1 — `MOCK_ONLY`

Admissible surrogate: a localhost-only canned-response mock and browserless dry-run shim using synthetic token literal `DUMMY_1PSID_DO_NOT_USE`.

Constraints:

- Only loopback `127.0.0.1`; zero external network.
- Explicit configurable base URL must be set to loopback and must fail closed for every non-loopback host.
- No Google hostnames/endpoints, cookie names beyond the inert synthetic test literal, profile reads, or live wrapper imports.
- Goru's declaration says `Network surface: NONE`; this is imprecise because the mock lane uses loopback. Implementation and receipt must state `127.0.0.1 loopback only; zero external network`.
- Live status remains `INADMISSIBLE-LIVE => REJECT-for-live` regardless of surrogate result.

## OPTION-2 — `PAPER_ONLY_NOW`

The Python Playwright module is installed, but its configured Chromium executable resolves to an existing executable named `Google Chrome for Testing`. Launching it would conflict with DIRECTION §0's packet-wide `no Chrome launch` rule. Goru's declaration also self-certifies `Uses no headless/stealth browser: YES`, while a Playwright surrogate would require launching a browser process. Tori therefore will not authorize execution under this packet.

Required output is static analysis only: `tori/PAPER_ANALYSIS_OPTION-2.md`. No browser launch, profile creation, localhost server, or shim execution.

Live status remains `INADMISSIBLE-LIVE => REJECT-for-live`.

## OPTION-3 — `SURROGATE_TESTABLE`

Admissible surrogate: browserless BeautifulSoup fixture parser and dry-run state machine. `bs4` is already installed. No network, browser, System Events, Accessibility, display reconfiguration, install, kext, or GUI invocation is needed.

Required discovery output `goru/OPTION-3_DISCOVERY.md` is documentation-only. It may describe future mechanics but must not invoke or inspect live display/Accessibility state.

Live status remains `SEPARATELY-GATED-LIVE`; a surrogate pass can only justify a separate future Duho-gated packet.

## Official recommendation to Hwao

- OPTION-1: `MOCK_ONLY`
- OPTION-2: `PAPER_ONLY_NOW`
- OPTION-3: `SURROGATE_TESTABLE`

No Phase-1 work may begin until Hwao appends these classes to `WAVE_LEDGER.md` and creates exactly one zero-byte `ADMISSIBILITY_VERDICT_<UTC>Z` marker.
