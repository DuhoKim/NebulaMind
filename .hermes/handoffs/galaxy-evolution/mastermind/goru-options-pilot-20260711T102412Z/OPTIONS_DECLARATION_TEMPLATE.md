# OPTIONS_DECLARATION_TEMPLATE — fill exactly; one block per option; no field omitted
Output file: `goru/OPTIONS_DECLARATION.md` · Author must be Goru · Referenced code files listed with path + sha256.
A field with nothing to declare says `NONE`. Vague entries ("various", "improved", "etc.") are non-conforming.

**Options are already named (DIRECTION §1): OPTION-1 gemini-webapi/bard-api RPC wrapper; OPTION-2
stealth Playwright/Puppeteer + copied profile; OPTION-3 virtual display + System Events GUI
automation. Their LIVE transports are pre-classified (1,2 = INADMISSIBLE-LIVE; 3 = SEPARATELY-GATED)
and are NOT what you declare here. Declare the SURROGATE mechanics only — the transport-free /
localhost-mock / benign-local shim that Phase 1 will actually run. If an option cannot be tested
without its banned live transport, declare it `PAPER_ONLY_NOW` in the Local testability statement.**

---

## OPTION-<1|2|3> — <precise short name>

**One-sentence mechanism.** <what it does, concretely>

**Full mechanism.** <step-by-step: how a prompt would be composed, how the target conversation is
addressed, how state is read, how start/stop is decided, how capture happens>

**Tooling inventory.** <every binary/library/framework/language it uses, with versions if known;
one per line>

**Network surface.** <every host it would contact in LIVE use; and the exact subset (must be NONE)
contacted during LOCAL fixture tests>

**Credential/profile surface.** <what auth state it relies on in live use (e.g. existing signed-in
profile); must include: "no cookie export, no profile cloning, no credential handling" or the
option is INADMISSIBLE>

**Reads/writes.** <files/dirs it reads; files/dirs it writes; must be confined to a stated lane
root in live use and to `tests/results/<option>/` in local tests>

**Single-launch & fail-closed behavior.** <how it guarantees one launch per prompt; what it does on
verification/billing/login walls (must be: stop, zero actions, marker); what it does on uncertainty>

**Five macro failure modes — fix mapping.**
1. Pro + Deep Research never selected → <how this option guarantees/verifies selection>
2. Start research never clicked → <how it verifies active server state after exactly one start>
3. Wrong-tab capture → <how it binds every action/read to the exact conversation identity>
4. No quota/marker/verification gates → <which gates it implements and where>
5. 93 identical-hash captures → <how capture is target-bound and content-verified (marker count,
   final line, per-run hash)>

**Local testability statement.** <which parts run browserless over HTML/JSON fixtures via the
harness contract in TEST_DESIGN.md; entrypoint command; or an honest "inseparable from live
browser" ⇒ PAPER_ONLY_NOW>

**Banned-tech self-certification (each line kept verbatim, answered YES):**
- Uses no cookies / `__Secure-1PSID` / session-token handling: YES/NO
- Uses no cloned or secondary browser profiles: YES/NO
- Uses no headless/stealth browser or fingerprint evasion: YES/NO
- Handles no CAPTCHA/verification surface, ever: YES/NO
- Uses no undocumented/private Google APIs: YES/NO
- Requires no billing/API enablement or account changes: YES/NO
- Never executes `ruthless_weekend_burn.py` or derivatives: YES/NO
Any NO ⇒ the option is INADMISSIBLE as declared; revise or withdraw it.

**Known risks/limitations (honest).** <list>

---

## Attestation (bottom of the filled file)
- `Declared by Goru at <UTC>. These are the three options exactly as I intend them; no other
  mechanism is bundled or implied.`
- `Referenced code files and sha256: <list or NONE>`
