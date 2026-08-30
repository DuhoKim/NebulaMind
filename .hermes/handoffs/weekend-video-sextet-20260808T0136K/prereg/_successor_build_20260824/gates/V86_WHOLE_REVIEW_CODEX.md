# V86 whole-document adversarial review — CODEX

## Verdict

**NOT CLEAR.** The assigned bytes match the brief, but V86 did not apply the seven rulings coherently. The new Row D2 is absent from the canonical VOID registry; BS-SI is assigned to the pre-freeze class while its receipt cannot exist until P2–P3; the arrival-event ruling contradicts both its companion spec and the draft's surviving N2 lifecycle; BS-L issuance still creates an event at the temporal partition's supposedly empty seam; and the BS-3g block simultaneously says its mechanics are committed and unset. The green lints do not reach these failures.

## Subject and independent checks

- Subject SHA-256: `25cfb64cd69d0d86915ad1b9635bcdc55ea288c3e4144589669842412829457e` — exact match before reading.
- Referenced frozen bytes independently matched: `successor_ref_v9.py` = `6a9abbbd…`, `closure_worker_v9.py` = `28f8e1f9…`, `LIFECYCLE_GUARANTEE_SPEC.md` = `b6951ae0…`, `tools/refusal_vocabulary_check.py` = `d6593354…`.
- `prereg_lint.py`: exit 0, 97 advisory / 0 blocking; counts 17 P / 8 E.
- `prereg_trace.py --check`: 85 transitions, 0 problems.
- `refusal_vocabulary_check.py`: 0 problems; self-test 34 controls, 0 failures.
- `lifecycle_derivation_check.py`: 0 problems; self-test 9 controls, 0 failures.
- Contrary to the brief's checker claim, `void_registry.py` refused V86 and its self-test failed 5/6 controls after Row D2 entered the table.

## Findings

### F1 — HIGH — REPAIR-REQUIRED — Row D2 has no canonical VOID antecedent

§6.1 Row D2 (line 706) creates three live VOID branches: output outside the store, a write after BS-2f, and any path into `calibration_bins()`. Section 7.1 claims every §6.1 row is name-covered (lines 941–943), but its table jumps from Row D at line 976 to Row E at 977; there is no `VOID-6.1D2-*` row. Executing the referenced checker on the assigned bytes returns:

`REFUSED: [V05] §6.1 row D2 is defined but no antecedent ID names it`

Its advertised six-control self-test now reports five failures because the unhandled D2 defect contaminates the clean fixture and four mutation expectations. This is not semantic-coverage subtlety: the checker proves the new row is not even name-covered, so BS-2v cannot handle every enumerated antecedent and the V85 ruling application is incomplete.

### F2 — HIGH — REPAIR-REQUIRED — BS-SI cannot be the Class-P receipt V86 defines

The draft says it becomes a preregistration only when every Class-P slot holds a receipt before freeze (lines 53–59), and §7 labels Class P as “freeze prerequisites” (line 898). Yet BS-SI is Class P while its content is the *real per-object χ-derived stratum-index artifact's receipt* (line 919), produced by Row D2 only at P2–P3 after Row D and before BS-2f (line 706). Those bytes cannot exist at P0 without reading the real χ that the freeze precedes. A pre-freeze design/schema receipt and the later realised BS-SI value receipt are different artifacts, but V86 gives one slot one identity. Either freeze waits for post-image χ (violating the phase model) or it cannot satisfy its own all-Class-P receipt condition. The ruling's count move was applied to the wrong lifecycle class/object.

### F3 — HIGH — REPAIR-REQUIRED — the arrival ruling did not replace N2; the “derived” lifecycle is internally contradictory

The companion authorizes a write-ahead arrival event and says no request can vanish (spec lines 53–63), and marks N2 retired (line 70). The same spec still says W1 is invisible N2 and safe to reprocess (line 80) and closes by saying “N2 stands referred” and still needs a second event class (line 176). V86 repeats the contradiction: it calls death before commit N2 (line 640), calls a validation death N2 (line 644), calls Row-B death the N2 residue (line 650), and says nothing changed what the log records (line 652), despite line 649 and Row B line 702 saying the opposite. Line 649 even retains “crash between decide-and-append is indistinguishable from a request that never arrived,” which the preceding durable arrival event is specifically supposed to distinguish.

The derivation checker exits 0 because, as its own source lines 17–23 state, it checks only labelled G/N quote rows and cannot see unlabelled normative lifecycle text. V86 line 626's claim that this class of divergence is “impossible” is therefore false on the assigned bytes. The operative crash table and terminal treatment still implement the retired lifecycle.

### F4 — HIGH — REPAIR-REQUIRED — arrival events cannot be joined to terminal events or deadlines by request

The companion's arrival schema carries only row, operation, object identity, and timestamp (spec lines 55–57). V86 separately says the actual internal request identifier is *not written to the access log* (line 647). Repeated legal requests for the same `(row, operation, object)` are expected (line 647), so neither recovery nor an auditor can bijectively pair two arrival records with two later terminal records, identify which request is still pending, enforce one decision per request, or close the correct deadline. Timestamp is not declared unique and object identity deliberately denotes the touched object, not the request.

The boundary is also undefined for a truncated or malformed frame: logging only after full decode permits a half-arrived request to vanish; logging on first bytes cannot yet carry the required row/operation/object facts. “On receipt” is not a state transition that resolves this. The new event class needs a canonical request identity and an explicit framing/acceptance boundary, with that identity joined into its terminal binding.

### F5 — HIGH — REPAIR-REQUIRED — BS-L issuance's own access-log event is orphaned by the temporal partition

Line 611 says every pre-BS-L event must be inside the sealed checkpoint, every continuation event must be appended *after* BS-L issuance, and no event can be appended during the atomic issuance step. But Row N writes the BS-L artifact (line 716), and Row B is the only path for sealed-store writes and must append both a write-ahead arrival and exactly one terminal touch/refusal event (line 702; lifecycle G1–G4). The terminal event for the BS-L write commits with issuance itself: it does not exist early enough to be in the already-canonicalized checkpoint, is not after the committed issuance, and cannot be omitted without violating G1/G3. Atomicity removes partial state; it does not remove the transaction's own event. The partition needs an explicit rule for issuance's arrival and terminal event (or a proof that BS-L is outside the mediated store-effect domain, which the current universal Row-B wording denies).

### F6 — MEDIUM — REPAIR-REQUIRED — the rebuilt refusal principle is contradicted by the stale principle that makes the checker green

The ruled principle at line 593 permits reasons to describe an object's storage state and forbids only content-derived information. Line 617 then declares, as the principle binding *every code*, that a reason “may never describe the object”; line 665 applies the same old rule to explanations. That condemns the four ruled availability reasons again. `refusal_vocabulary_check.py` passes because R03 (source lines 182–191) looks for the stale “never … object” phrase; its contradiction regex does not reject “may describe the object's STORAGE STATE.” Thus the green result is evidence of the contradictory old sentence's presence, not of the rebuilt principle's consistency. Replace every operative old formulation, and make the checker require the storage-state/content-derived split rather than accept its superseded predecessor.

### F7 — MEDIUM — REPAIR-REQUIRED — `REFUSED-INTEGRITY-MISMATCH` is both unresolved and resolved

The live eleven-code inventory labels `REFUSED-INTEGRITY-MISMATCH` “flagged and UNRESOLVED” (line 596). Twenty-two lines later the normative ruling application says “IS RESOLVED: THE REFUSAL OWNS IT,” logs it, continues the run, and scopes VOID (line 618). Those are incompatible states for a code whose consequence determines continuation versus halt/VOID. This is not the parked availability-code observation; it is stale status inside V86 after the principal explicitly ruled the item.

### F8 — HIGH — REPAIR-REQUIRED — the BS-3g verifier has two incompatible frozen parameter states and two incompatible bound semantics

Line 1201 and `ref/DRAW_MECHANICS_COMMIT_20260830.md` lines 10–14 fix `n_draws=99`, seed `20260830`, generator `numpy-1.26.4-PCG64-default_rng`, Δγ `0.01`, and COMMON RANDOM variates. The same live BS-3g specification says Δγ is currently unset (line 1258), common-random semantics are Class-P unset (lines 1312–1314), `n_draws` and seed are currently unset (lines 1434–1439), and the generator's closed set is empty (lines 1443–1448). §7 line 920 still says the draw set is missing. A verifier cannot know whether those fields must equal committed literals or must be refused as inadmissible.

The bound text also retains the superseded measurement-derived formula: lines 1274–1300 use `|γ̂| + kγ·σγ`, claim it places the true gradient inside the swept interval, and discuss choosing between measurement-derived and a-priori shapes, even though lines 1201 and 1264–1269 rule `kγ` moot and the endpoint a-priori. Historical banners do not make these field definitions historical; they remain in the operative schema/verifier description. Re-derive the whole BS-3g block from the ruling instead of prepending a one-line override.

### F9 — HIGH — REPAIR-REQUIRED — Δγ does not precommit the perturbation grid, so the producer can still choose it after seeing flips

The commitment fixes only the *maximum spacing* Δγ and says this means 51 points (commit line 13). V86 requires endpoints, zero, at least three values, and adjacent gaps no larger than Δγ (lines 1242–1254), but it never freezes the actual manifest or an origin/lattice/count. `perturbation_manifest_sha256` is merely reported in the eventual receipt (lines 1237–1241), so it proves which grid was reported, not when that grid was chosen.

Many nonuniform grids satisfy the same endpoints and max gap while omitting different interior points; adding a nearby point permits an otherwise regular lattice point to be shifted away without exceeding 0.01. A producer can therefore probe, then report a conforming grid that misses a narrow flip, while every frozen field remains unchanged. Freeze the exact ordered manifest (or a deterministic generation rule including origin, count, and endpoint arithmetic) and require equality to it; a receipt digest cannot attest to its own priority.

### F10 — MEDIUM — REPAIR-REQUIRED — the committed SeedSequence indexing is off by one against the matrix contract

V86 defines draw indices as `i ∈ [1, n_draws]` (line 1452). The committed generator rule is `SeedSequence(master_seed).spawn(n_draws)[i]` (commit line 12). For `n_draws=99`, `spawn(99)` has Python indices 0–98: draw 99 raises `IndexError`, while child 0 is unused. I executed this under the frozen NumPy 1.26.4 environment. The rule must either define zero-based draw indices or index `[i-1]`; as written, the promised 99-draw matrix cannot be generated.

## Failed attacks / verified survivals

- The assigned draft, lifecycle companion, refusal checker, and frozen v9/worker digests match their cited values.
- Counts independently reproduce 17 P / 8 E; the count itself is not the defect.
- The citation-lint result matches the brief: 97 legacy advisories and no blockers; I did not re-report them.
- The trace checker reproduces all 85 transitions.
- The refusal checker and lifecycle quote checker pass their own stated, narrow predicates; the findings above exploit their declared blind spots rather than alleging different exit results.
- I did not re-derive the parked logged-object leak, per-call-site classification unit, freeze-signature residue, `require_authorization`, or the open γ→sign mapping.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V86
VERDICT: NOT CLEAR
COUNT: 10
F1 | HIGH | REPAIR-REQUIRED | §6.1 line 706; §7.1 lines 941-978 | Row D2 has live VOID branches but no canonical VOID antecedent, and void_registry.py refuses V86.
F2 | HIGH | REPAIR-REQUIRED | §0 lines 53-59; §7 lines 898-919 | BS-SI is a pre-freeze Class-P receipt for a real χ-derived artifact that cannot exist until P2-P3.
F3 | HIGH | REPAIR-REQUIRED | §6.1 lines 625-652; lifecycle spec lines 53-80, 174-176 | The arrival ruling did not replace N2; the spec and draft retain the retired invisible-request lifecycle while the quote checker stays green.
F4 | HIGH | REPAIR-REQUIRED | §6.1 lines 647-650; lifecycle spec lines 53-63 | Arrival records omit request identity, so repeated requests cannot be paired with terminal events or deadlines.
F5 | HIGH | REPAIR-REQUIRED | §6.1 lines 611, 702, 716 | BS-L issuance's own mediated write event is neither pre-issuance checkpoint material nor post-issuance continuation.
F6 | MEDIUM | REPAIR-REQUIRED | §6.1 lines 593, 617, 665; refusal_vocabulary_check.py lines 182-191 | The stale never-describe-object principle contradicts the ruled storage-state principle and is what makes R03 pass.
F7 | MEDIUM | REPAIR-REQUIRED | §6.1 lines 596, 618 | REFUSED-INTEGRITY-MISMATCH is simultaneously labelled unresolved and resolved with continue semantics.
F8 | HIGH | REPAIR-REQUIRED | §11 lines 1201, 1258, 1274-1314, 1434-1448 | BS-3g's operative block simultaneously commits and unsets its draw mechanics and retains the superseded measurement-derived bound.
F9 | HIGH | REPAIR-REQUIRED | §11 lines 1237-1254; DRAW_MECHANICS_COMMIT lines 13-18 | A maximum gap does not freeze the perturbation grid; a receipt-chosen conforming manifest can still avoid interior flips.
F10 | MEDIUM | REPAIR-REQUIRED | §11 line 1452; DRAW_MECHANICS_COMMIT line 12 | One-based draw indices address spawn(n_draws)[n_draws], which is out of range and leaves child zero unused.
<!-- END FINDINGS-BLOCK -->