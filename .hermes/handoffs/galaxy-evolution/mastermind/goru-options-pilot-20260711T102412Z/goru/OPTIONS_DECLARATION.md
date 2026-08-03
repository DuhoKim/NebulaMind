# OPTIONS_DECLARATION

## OPTION-1 — Localhost Mock with Synthetic Token

**One-sentence mechanism.** Option-1 bypasses live Google APIs by using a localhost `http.server` mock returning canned JSON.

**Full mechanism.** A prompt is composed and directed at `http://127.0.0.1:<port>` rather than Google. Target conversation is addressed via the mock server's synthetic URLs. State is read from canned JSON responses matching the test fixtures. Start/stop is decided based on the parsed mock JSON. Capture happens by extracting the simulated body text from the mock response.

**Tooling inventory.**
python3
http.server
requests

**Network surface.** NONE

**Credential/profile surface.** no cookie export, no profile cloning, no credential handling. (Uses synthetic `DUMMY_1PSID_DO_NOT_USE` token only).

**Reads/writes.**
Reads: `tests/fixtures/`
Writes: `tests/results/OPTION-1/`

**Single-launch & fail-closed behavior.** Guarantees one launch by tracking state and asserting `planned_actions == ["HARD_STOP"]` with no execution upon encountering verification/billing/login walls, or uncertainty.

**Five macro failure modes — fix mapping.**
1. Pro + Deep Research never selected → Mock verifies payload parameters for selection.
2. Start research never clicked → Mock tracks state transitions and refuses second starts.
3. Wrong-tab capture → Target conversation id strictly bound to local HTTP session tracking.
4. No quota/marker/verification gates → Harness halts on encountering wall states in canned JSON.
5. 93 identical-hash captures → Harness verifies target bounds and output markers before writing.

**Local testability statement.** Runs browserless over JSON/HTML fixtures via the harness contract. Entrypoint: `python3 goru/option1_shim.py`.

**Banned-tech self-certification (each line kept verbatim, answered YES):**
- Uses no cookies / `__Secure-1PSID` / session-token handling: YES
- Uses no cloned or secondary browser profiles: YES
- Uses no headless/stealth browser or fingerprint evasion: YES
- Handles no CAPTCHA/verification surface, ever: YES
- Uses no undocumented/private Google APIs: YES
- Requires no billing/API enablement or account changes: YES
- Never executes `ruthless_weekend_burn.py` or derivatives: YES

**Known risks/limitations (honest).** The mock server cannot replicate live Gemini anti-bot protections or DOM changes.

---

## OPTION-2 — Localhost Ephemeral Profile

**One-sentence mechanism.** Option-2 automates a local fixture page using Playwright/Puppeteer with a completely fresh, ephemeral profile.

**Full mechanism.** A prompt is composed to interact with a `file://` or `http://127.0.0.1` served static fixture. Target conversation is addressed via standard DOM selectors on the fixture. State is read by polling the local DOM. Start/stop is decided based on DOM state markers. Capture happens by extracting text content from the matched target container.

**Tooling inventory.**
python3
playwright

**Network surface.** NONE

**Credential/profile surface.** no cookie export, no profile cloning, no credential handling. (Uses a fresh ephemeral profile under `tests/results/OPTION-2/profile/` which is deleted after).

**Reads/writes.**
Reads: `tests/fixtures/`
Writes: `tests/results/OPTION-2/`

**Single-launch & fail-closed behavior.** DOM polling ensures start is clicked exactly once. On encountering verification/billing/login walls (detected via DOM elements), it issues a `HARD_STOP` with zero other actions.

**Five macro failure modes — fix mapping.**
1. Pro + Deep Research never selected → Explicit DOM assertions for selection state.
2. Start research never clicked → Validates DOM transitions after click.
3. Wrong-tab capture → Extracts only from containers matching the target ID.
4. No quota/marker/verification gates → Halts immediately if wall selectors are present.
5. 93 identical-hash captures → Verifies unique final-line markers and target IDs before saving.

**Local testability statement.** Since Playwright is assumed installed, runs over HTML fixtures via the harness contract. Entrypoint: `python3 goru/option2_shim.py`.

**Banned-tech self-certification (each line kept verbatim, answered YES):**
- Uses no cookies / `__Secure-1PSID` / session-token handling: YES
- Uses no cloned or secondary browser profiles: YES
- Uses no headless/stealth browser or fingerprint evasion: YES
- Handles no CAPTCHA/verification surface, ever: YES
- Uses no undocumented/private Google APIs: YES
- Requires no billing/API enablement or account changes: YES
- Never executes `ruthless_weekend_burn.py` or derivatives: YES

**Known risks/limitations (honest).** DOM layout of synthetic fixtures may diverge from live Google pages. Does not test evasion of anti-bot measures since it runs locally.

---

## OPTION-3 — Browserless Dry-Run Decision Logic

**One-sentence mechanism.** Option-3 runs purely browserless decision logic to parse synthetic HTML fixtures, with GUI automation mechanics separately documented but never invoked.

**Full mechanism.** A prompt is simulated by providing inputs to a parser. Target conversation is addressed by matching IDs within the HTML strings. State is read by parsing the HTML fixture file. Start/stop is decided based on parsed state mapping. Capture happens by extracting text from the parsed DOM tree.

**Tooling inventory.**
python3
beautifulsoup4

**Network surface.** NONE

**Credential/profile surface.** no cookie export, no profile cloning, no credential handling.

**Reads/writes.**
Reads: `tests/fixtures/`
Writes: `tests/results/OPTION-3/`

**Single-launch & fail-closed behavior.** State machine parses HTML and returns `HARD_STOP` with zero actions if wall conditions are met. Will not issue duplicate start commands if state indicates already started.

**Five macro failure modes — fix mapping.**
1. Pro + Deep Research never selected → Logic verifies selection criteria in parsed HTML.
2. Start research never clicked → Logic transitions state only upon confirming click readiness.
3. Wrong-tab capture → Parser strictly filters output by the provided target ID.
4. No quota/marker/verification gates → Parser identifies wall elements and forces `HARD_STOP`.
5. 93 identical-hash captures → Parser checks for expected markers and hashes before final output.

**Local testability statement.** Runs browserless over HTML fixtures via the harness contract. Entrypoint: `python3 goru/option3_shim.py`.

**Banned-tech self-certification (each line kept verbatim, answered YES):**
- Uses no cookies / `__Secure-1PSID` / session-token handling: YES
- Uses no cloned or secondary browser profiles: YES
- Uses no headless/stealth browser or fingerprint evasion: YES
- Handles no CAPTCHA/verification surface, ever: YES
- Uses no undocumented/private Google APIs: YES
- Requires no billing/API enablement or account changes: YES
- Never executes `ruthless_weekend_burn.py` or derivatives: YES

**Known risks/limitations (honest).** AppleScript/GUI automation is not tested, leaving actual interaction reliability unverified.

---

## Attestation
- Declared by Goru at 2026-07-11T10:36:49Z. These are the three options exactly as I intend them; no other mechanism is bundled or implied.
- Referenced code files and sha256: `goru/option1_shim.py` (NONE), `goru/option2_shim.py` (NONE), `goru/option3_shim.py` (NONE), `goru/OPTION-3_DISCOVERY.md` (NONE)
