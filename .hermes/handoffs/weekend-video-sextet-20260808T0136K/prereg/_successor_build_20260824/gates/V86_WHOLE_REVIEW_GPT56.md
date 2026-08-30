# V86 whole-document adversarial review — GPT56

**VERDICT: NOT CLEAR.** The subject digest matches the brief, and several mechanical claims reproduce, but the seven-ruling application is not internally or mechanically complete. The added Row D2 breaks the canonical VOID registry; the arrival-event ruling is simultaneously asserted, contradicted, and left without a joinable authenticated schema; the rebuilt refusal principle coexists with—and is linted by—the superseded principle; the draw block still contains operative pre-ruling values; and the new terminal outcome has no producing route.

## Findings

### F1 — HIGH / REPAIR-REQUIRED — Row D2 has no canonical VOID antecedent

V86 adds Row D2 at §6.1 line 706 and gives it three void conditions: output outside the store, write after BS-2f, and any path into `calibration_bins()`. The canonical registry at §7.1 lines 955–1010 has no `VOID-6.1D2-*` antecedent at all: it moves directly from Row D's antecedent at line 976 to Row E's at line 977.

This is not merely semantic coverage beyond the checker's advertised reach. It fails the checker's own name-coverage contract. Running the referenced checker on the exact V86 bytes returned:

> `REFUSED: [V05] §6.1 row D2 is defined but no antecedent ID names it`

The advertised self-test is consequently contaminated too: `void_registry.py DRAFT --self-test` reported **5 failures**, because V05 appears in the clean case and alongside four positive controls. The brief's “6 controls, 0 failures” claim is false on the referenced current files. Until canonical antecedents name the new row's branches, BS-2v cannot compare against a complete registry and Clause 10 cannot convert every enumerated void antecedent.

### F2 — HIGH / REPAIR-REQUIRED — N2 was not actually retired from either normative lifecycle surface

The new rule is clear in the spec at lines 53–63 and in V86 lines 636 and 649: arrival is durable before processing, no real request can vanish, and N2 is retired. Both normative surfaces then reinstate the old model:

- `LIFECYCLE_GUARANTEE_SPEC.md` line 80 says W1 shows “nothing — N2,” with no binding and safe re-processing; line 176 says “N2 stands referred” and still “needs a second event class.”
- V86 line 640 says death before any commit has “no event” and “this is N2”; line 644 assigns validation death to N2; line 649, after saying arrival fixed the gap, retains the old “crash between decide-and-append is indistinguishable from a request that never arrived” residue; line 650 again says Row B death is an invisible N2 residue; line 652 says no second custody surface is created and nothing changes what the log records beyond refusal reason.

These are live semantic statements, not merely the historical N2 row. A request cannot both have a durable arrival event and have “no event/no binding” at W1. The derivation checker returns 0 only because it compares labelled G/N row quotations and the digest; its own documented blind spot (unlabelled normative lifecycle text) is exactly where this divergence lives. V86 therefore repeats the half-migration the brief says V85 resolved.

### F3 — HIGH / REPAIR-REQUIRED — the arrival events cannot be authenticated or paired to their terminal events per request

The write-ahead class is not integrated into the closed non-χ schema or the request identity model.

V86 lines 589–592 make the non-χ list exhaustive and define the access-log event schema as `(timestamp, actor, table row, operation, object identity, success/refusal, refusal reason, running chain digest)`. An ARRIVAL has no success/refusal verdict or refusal reason, and there is no event-class field. The generated `ref/STRING_FIELD_REGISTRY.md` lines 137–146 declares only one `nonslot.access_log_chain`; its field inventory at lines 167 and 192–203 is the same old touch/refusal schema. `ref/gen_string_field_registry.py` lines 170–180 and 210–218 likewise declare only that one event class. No authenticated arrival schema exists in §11.

Worse, V86 line 647 expressly keeps each request's internal identifier **out of the access log**. The arrival's identifying facts in the lifecycle spec (lines 55–57) are only row, operation, object identity and timestamp. Legal retries and repeated touches are explicitly expected, so those values are not a request key; the timestamp is only millisecond-resolution. Two same-object requests can therefore produce two arrivals and two terminals with no authenticated way to decide which terminal closes which arrival. A crash after one terminal can cause recovery either to pair the wrong request or to reprocess one already decided. The new event makes pre-verdict existence visible, but it does not make “every request ends exactly once” verifiable.

### F4 — HIGH / REPAIR-REQUIRED — the rebuilt storage-state principle coexists with the superseded “never describe the object” rule, and the checker enforces the wrong one

V86 line 593 correctly applies the new ruling: a refusal may describe the object's **storage state** but never content derived from its bytes. Line 617 later declares, as the live principle binding every code including the catch-all, that a reason “may never describe the object.” The four availability codes at lines 596—ABSENT, UNREADABLE, INCOMPLETE, INTEGRITY-MISMATCH—necessarily describe the object's storage state, so the two formulations cannot both govern.

The referenced checker confirms this is not harmless history. `tools/refusal_vocabulary_check.py` lines 23–28 still describes R03 as “never the object,” and lines 182–184 require a `never ... object` sentence to pass. It does not require the rebuilt storage/content distinction. Thus the exact stale sentence at V86 line 617 is what satisfies R03, while the ruled principle could be deleted and the checker would remain green. The actual run returned 0 problems and all self-controls passed, proving only that the checker mechanically accepts the contradiction. This leaves future codes judged by two incompatible tests and defeats the claimed ruling application.

### F5 — HIGH / REPAIR-REQUIRED — the BS-3g block still has mutually exclusive pre- and post-ruling parameter contracts

Line 1201 says the draw discipline is unfrozen and fixes `n_draws = 99`, COMMON RANDOM variates, master seed 20260830, `numpy-1.26.4-PCG64-default_rng`, and `Δγ = 0.01` by the committed artifact. The referenced `ref/DRAW_MECHANICS_COMMIT_20260830.md` lines 10–17 confirms those exact values and says only the ±0.25 endpoint remains pending.

The same normative schema block then says the opposite:

- lines 1202–1208 say those parameters are awaiting the principal, the sitting has not landed, and the draw discipline is excluded from review;
- line 1258 calls Δγ CURRENTLY UNSET and also calls `n_draws`, seed and generator blockers;
- lines 1313–1316 call COMMON RANDOM an UNSET choice and leave the master seed to be frozen;
- lines 1437–1448 call `n_draws` and seed CURRENTLY UNSET and the generator closed set CURRENTLY EMPTY;
- lines 1270–1273 retain the superseded measurement-derived origin (“the measurement itself plus a frozen constant”) after line 1264 makes the bound a priori;
- lines 1293–1298 still claim the bound places the true gradient inside the interval with stated confidence, which was the sampling-bound claim, not the new a-priori sweep claim.

The generated registry reproduces the stale side: `ref/STRING_FIELD_REGISTRY.md` lines 178–190 says generator EMPTY, seed UNSET, `gamma_bound` recomputed as `|gamma_hat|+k*sigma`, and `n_draws` UNSET. A verifier cannot both refuse values unequal to the committed 99/20260830/PCG64/0.01 and treat those domains as unset/empty. This is more than the known pending γ endpoints: every other mechanics value was ruled, yet the operative field definitions still deny that ruling.

### F6 — HIGH / REPAIR-REQUIRED — `TERMINATED-UNNAMEABLE-REFUSAL-CLASS` is named but has no producer or conversion route

V86 lines 538 and 619 are the only two occurrences of the new run ending. They say it is “produced” when a catch-all class recurs after the first real χ. The mechanism they point to does something else: lines 603–614 make recurrence stop explanation from discharging the class, keep the enumeration incomplete, and make the next verifier **refuse/block its gate**. The §11 enumeration-verifier item at lines 1521–1533 likewise recomputes entries and refuses a second `EXPLAINED`; it specifies no terminal-outcome emission.

There is no terminal receipt schema, producer, converter, or implementation item for this third ending. Section 5 line 543 states what `run_production_verdict()` can return and omits it; the exception-to-outcome conversion in §11 is for raised failures in the pinned numerical reference, not access-log recurrence. Therefore the actual path for a post-χ recurrence is a gate held shut, not exactly one run-level `TERMINATED-UNNAMEABLE-REFUSAL-CLASS` outcome. This repeats the document's own rule that a named outcome nothing can produce is not a route.

## Attacks that held / mechanical evidence

- Subject SHA-256 independently recomputed as `25cfb64cd69d0d86915ad1b9635bcdc55ea288c3e4144589669842412829457e` before reading.
- Lifecycle-spec SHA-256 recomputed as `b6951ae0f09133167c531d369e0943e25628906640fbddf255e0d190f8a33fa0`, matching V86 line 627; the labelled derivation checker and its nine controls pass. F2 is in the checker's expressly unlabelled blind spot.
- `tools/refusal_vocabulary_check.py` SHA-256 recomputed as `d65933546d0fbfe42f32d72699a53c47d18d8d70b808cf87fad65d6f92f785c3`, matching V86 line 622. The checker reports 0 problems and its 34 controls pass; F4 attacks what R03 defines, not its execution.
- `tools/prereg_counts.py` reproduces 17 class P / 8 class E. This count held.
- Full `prereg_lint.py` exits 0 with 97 advisory and 0 blocking findings, as the brief states. The legacy citation advisories were not re-reported.
- `ref/RAISE_SITE_CLASSIFICATION.md` contains 112 enumerated raise rows with displayed totals summing to 112. I did not re-derive the parked per-raise-versus-per-call-site defect.
- I did not re-derive the parked `require_authorization`, availability-code identity leak, BS-3g lifecycle cycle, Row-L phase, BS-2v self-reference, gain sign mapping, or the already-referred general VOID/numerical overlap.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V86
VERDICT: NOT CLEAR
COUNT: 6
F1 | HIGH | REPAIR-REQUIRED | §6.1 line 706; §7.1 lines 955–1010 | Row D2 has void branches but no canonical VOID antecedent, and the real registry/self-test fail V05.
F2 | HIGH | REPAIR-REQUIRED | §6.1 lines 636–652; lifecycle spec lines 53–70, 80, 176 | N2 is declared retired but both normative lifecycle surfaces still make pre-commit requests invisible and referred.
F3 | HIGH | REPAIR-REQUIRED | §6.1 lines 589–592, 647–650; lifecycle spec lines 53–63 | Arrival events lack an authenticated class/schema and an on-chain request key joining each arrival to exactly one terminal event.
F4 | HIGH | REPAIR-REQUIRED | §6.1 lines 593, 617; tools/refusal_vocabulary_check.py lines 23–28, 182–184 | The rebuilt storage-state principle conflicts with a live never-describe-the-object rule that R03 still requires.
F5 | HIGH | REPAIR-REQUIRED | §11 lines 1201–1208, 1258, 1264–1298, 1313–1316, 1437–1448 | The draw block fixes ruled mechanics and simultaneously leaves the same values unset/empty under the superseded bound model.
F6 | HIGH | REPAIR-REQUIRED | §5 lines 538, 543; §6.1 lines 603–619; §11 lines 1521–1533 | The new terminated-class ending has no producer or conversion; recurrence only makes verifiers refuse and gates remain shut.
<!-- END FINDINGS-BLOCK -->
