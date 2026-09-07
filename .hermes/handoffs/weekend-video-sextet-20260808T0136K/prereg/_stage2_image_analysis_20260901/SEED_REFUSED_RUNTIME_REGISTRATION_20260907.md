# SEED REFUSED — the runtime registration set was captured without a network call (2026-09-07 20:28 KST)
**Actual outcome, not readiness: `SEED REFUSED`.** `UNREGISTERED-RUNTIME-MODULE: encodings.idna`. The draw did not run. No protected data touched.

## WHAT SUCCEEDED, AND IS RETAINED
The beacon itself was fine. Round **6444980** was collected in two passes and **all three pinned hosts returned identical randomness**:
`6497c5eb0ec4e6886349dffe42decb747a6fdd7c8636e0ff71191ea83f9c675f` — api.drand.sh, api2.drand.sh, api3.drand.sh, 8 responses retained in `OUT_A1_FRESH/seed.collection*.json` and `seed.refetch*.json`. `accept_seed` reached its runtime check only after the hosts agreed.

## THE EXACT CAUSE, AND THE COMPLETE MISSING SET
`runtime_binding` requires every live module to be registered. The first HTTPS fetch lazily imports IDNA hostname handling. I enumerated the whole set rather than fixing one and rediscovering the next: **`encodings.idna`, `stringprep`, `unicodedata`** — exactly three, and nothing else.
**Root cause: the runtime capture that built the pins never made a network call**, so it could not contain the modules the seed stage actually loads. Same class as this evening's bytecode cache — a registration set captured under conditions that differ from the run it governs. **The gate refused rather than proceeding with an unregistered module, which is correct behaviour and the reason this was caught at the seed rather than inside the science.**

## WHY I HAVE STOPPED INSTEAD OF FIXING IT
Registering those three modules changes CORE's digest. CORE's digest is quoted inside C; the anchor bound `published_sha256` to the old CORE; `_start` requires `prev["C"] == self.C`. **So any legitimate fix invalidates the accepted designation for 6444980 and requires a new anchor and a new future round — a SECOND restart.**
Duho authorized **exactly one** fresh start, and it has been consumed: a designation was accepted (`OUT_A1_FRESH/designation.json`, PASS) and then failed at seed acceptance. A1 line 125: *"No automatic restart or extra validation attempt is authorized."* **I will not weaken the runtime check, will not hand-register the modules to rescue this designation, and will not treat the retained 6444980 randomness as usable.** Its value is now known to us, so like 6440756 it can never seed this study.

## THE CONCRETE PROPOSAL, READY FOR CODEX TO PUT TO DUHO
1. Rebuild the runtime registration from a capture that **exercises the network path**, adding exactly `encodings.idna`, `stringprep`, `unicodedata` — no exemption, no weakened check, correspondence rules unchanged.
2. Re-issue C against the new CORE; publish a fresh anchor binding the new CORE digest; designate the next future round by the adopted formula under the pinned invocation; collect and draw into a third journal.
3. Everything else unchanged: exclusions, exact 400/200/2,000, stage gates, winner/holdout rules, the single further validation limit — still unspent, since no draw, scoring or validation has occurred.
**This is a second restart and it needs Duho's word. I am not asking him myself and I have not performed any part of it.**
