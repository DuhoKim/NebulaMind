# V34 REPAIR — STATUS AND WHAT EACH REPAIR DOES NOT CLAIM (2026-09-07 09:58 KST)
STAGED, UNADOPTED. Successors only (run_configurations_v18 / provenance_designs_v14 / precedence_core_v2); V33 stays byte-frozen. Nothing approved, signed, frozen, adopted or run.

| seat B finding | state | evidence |
|---|---|---|
| B-1a..1d (FATAL, NSD at actual-input boundaries) | REPAIRED, reproduced first | track 14 v4: 10 fail-first methods observed FAILING on V33 and passing on V34; kit-enforced one assertion per method |
| B-2 (table verification blind to `m[o]`-selected codes) | REPAIRED | the mutation control now BITES: removing EVENT-FORGED from the table fails the v18 verification, where all four v17 tests passed |
| B-3 (verified receipt refused) | REPAIRED | the whole call completes; three separate subcases |
| **B-4 (the control oracle)** | **NOT CLOSED — see below** | dispatched to a bounded Codex author |
| B-5 (pins, `{NCTRL}`, the "run 2 = 16 OK" sentence, obsolete hashes) | OPEN | pins are regenerated only AFTER the code freezes |
| staged sandbox missing catalogue inputs (3 suites, 365 not 369) | OPEN | V34's dispatch stages them or the text names exactly which suites a sandbox cannot run |

## B-4: WHAT FREEZING THE BASELINE DOES AND DOES NOT ESTABLISH (Blanc 09:58)
The defect was real: the controls took their baseline from the implementation AT RUN TIME, so an incomplete implementation became its own oracle, and `by_check` reduced findings to CODE STRINGS — which is why a false PENDING-PUSH and a genuine HISTORY-NOT-AN-EXTENSION were indistinguishable to it. Freezing that baseline into `BASELINE_DECLARATIONS_V18.py` and comparing (class, code, stage) tuples fixes **REGRESSION DETECTION**: from now on, drift fails.
**IT DOES NOT ESTABLISH CORRECTNESS. A snapshot of the implementation's own output agrees with itself by construction.** Every declared class / stage / code / reason / multiplicity must be **VALIDATED BY THE INDEPENDENT REVIEW AGAINST THE SPECIFIED RULES**, including the reviewer's own counterexamples. **B-4 is closed only when that validation happens** — not on the strength of the freeze. Where a declared value cannot be derived from the rule text, that is a FINDING, not a baseline.
ROLES: the Codex worker preparing this is an AUTHOR and is told so in its brief; it does not review or sign off its own changes. Under Codex-first routing this separation is enforced, not assumed: the V34 package still goes to two independent seats under the different-engine requirement, and if routing ever forced one engine instance to both author and review, the round stops and Blanc is told.

## THE PATH IS SETTLED (Blanc 10:00, correcting 09:58)
The DRAND-ONLY SUCCESSOR is the authorised path — Duho chose it on 2026-09-06 ~19:02 KST and it is not to be re-asked. V34's preparation continues under that authorisation. The successor draws its OWN prospectively fixed FUTURE round when ready, so the V15 seed (round 6440756) does not carry into it and the exhibit-round overlap is not a live collision. Executing under signed V15 instead would be the deviation and would need fresh explicit authorisation from Duho. The no-draw boundary holds until the successor is genuinely ready.
