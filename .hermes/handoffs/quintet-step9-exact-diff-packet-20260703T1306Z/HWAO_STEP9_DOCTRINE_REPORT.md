# Hwao/Fable Doctrine Report — Step 9 exact-diff packet

Task: HWAO STEP 9 adversarial doctrine/gate review · Status: COMPLETE — read-only except this report; no patch applied; no DB/API mutations; no git.
Verified directly: approval packet, full proposed vs current content (section-by-section byte comparison), proposed AGN section (all 16 sentences read), current-section claim markers, GO/NO-GO checklist (raw rows), validation facts, marker/citation inventory.

## Verdict: `PASS_WITH_PATCHES` — one checklist addition is required before the packet is marked PREPARED_ONLY_NOT_EXECUTED; three riders join the future apply gate.

## What I verified and confirm

- **Section isolation (Q1): exact.** Nine H2 sections; **only** "AGN Feedback & Quenching" differs; the other eight sections and the preamble are byte-identical; current/proposed SHA256 match the packet's declared hashes.
- **De-voicing (Q2): faithful and complete.** All 16 sentences are reader-voice; the Step 8 pipeline-voice items were transformed correctly (e.g., "the ledger blocks using that single object…" → "a single object should not be read as a frequency estimate for galaxies in general"); the "as of mid-2026" stamp is present; fractions remain tracer-scoped and explicitly uncombined; simulations remain fenced; the scoped 2299 synthesis renders as the closer. One minor faithfulness note for Lana (non-blocking): Step 8's standalone attribution-caution sentence ("outflow attribution must stay source-specific," the Sarzi scope) was folded into P9S009's alternatives list — restore it or consciously waive it.
- **Bindings and caps (Q3): yes** — fresh P9 IDs on every sentence, bound ledger entries visible in-marker, 0 orphans / 0 overflows / 0 pipeline-voice / 0 forbidden-wording / 0 observation-vs-simulation source errors (the Step 8 Patch-2 rule now passing at machine level).
- **No evidence-ID laundering (Q4): confirmed.** The packet refuses to invent product evidence IDs and says so; `cite-unmatched` markers carry ledger entry IDs transparently. **The NO-GO on "Product evidence IDs resolved" is correct and must stand** — resolving it means either honestly-labeled evidence-row inserts (a data-model growth decision, the insert-heavy escalation class) or an alternative citation rendering, and that choice belongs to the operator at the apply gate.
- **Rollback honesty (Q5): confirmed.** "GET snapshots are rollback context only, not a DB backup" — stated plainly, NO-GO held. The third NO-GO (apply permission absent) correctly encodes the approval's boundary. No Step-10 creep found anywhere: state is PREPARED_ONLY_NOT_EXECUTED, no apply script or phrase exists.

## The finding the validator could not see: six live claim chips are silently desurfaced

The current AGN section carries **live claim markers 2913, 2915, 2917, 2921, 2924, 2929** (six of the page's 30 rendered chips — 2929 is one of the calibrated grafts with 40 evidence rows). The proposed section **drops all six** and contains only `cite-unmatched` preview comments. If applied as-is: the page's chip count falls 30 → 24, six claims lose their inline provenance surface, and the section renders with **no interactive citations at all** (HTML comments display as nothing) — a provenance-UI regression on the very page whose product concept is claim chips. None of this is dishonest — but none of it is *decided* either: no GO/NO-GO row names it, so the consequence would ride through the apply gate unexamined. This is the brief's "stale claim marker retention" attack inverted — live-marker **removal** without a decision record.

**Patch 1 (required now):** add a fourth NO-GO row to `go_no_go_checklist.jsonl`:
> `{"check": "Claim-marker continuity resolved", "note": "Proposed section removes live claim markers 2913/2915/2917/2921/2924/2929 (page chips 30->24) and renders no interactive citations. Apply gate requires a per-claim disposition map: rebind into a faithful new sentence / retire via claim workflow / explicit accept-desurface; plus renderer verification of cite-unmatched comment behavior.", "status": "NO_GO"}`

**Riders for the future apply gate (not this packet):**
- **Patch 2:** renderer-behavior verification — confirm `<!--cite-unmatched:…-->` renders invisibly in every render path (no raw comment leakage), and record whether a chip-less section is an accepted interim product state or must wait for citation resolution.
- **Patch 3:** the 2924 tension must be linked, not rediscovered — its `consensus` trust label is not derivable from this corpus (the ledger's maintenance-heating gap card), and the new prose renders maintenance as model-bounded. Whatever disposition 2924 gets (rebind/desurface), the label-vs-corpus gap card should be referenced in the apply packet.
- **Patch 4:** the per-claim disposition map should check faithfulness before rebinding (e.g., 2913's "rapid at z~2" wording has no supporting sentence in the new prose; 2915/2929 map well; 2917/2921 map onto the predictor-axis sentence).

## Review-question summary

1. Only the AGN section changes — **verified byte-level**. 2. De-voiced, faithful, zero pipeline voice — **yes** (one minor sentence-merge note). 3. All 16 freshly bound within caps — **yes**. 4. No invented evidence IDs — **confirmed; NO-GO stands**. 5. GO/NO-GO, apply plan, rollback note, safety ledger honest — **yes, with one missing row (Patch 1)**. 6. Ready for PREPARED_ONLY_NOT_EXECUTED — **yes once Patch 1 lands**; Patches 2–4 attach to the apply gate, which remains NO-GO on evidence IDs, rollback backup, apply permission, and now claim continuity.

## Safety ledger

Patch applied 0 · DB/API mutations 0 · SQL 0 · migrations 0 · deploy/restart 0 · product publish 0 · git 0 · generic NLI 0 · model downloads 0 · secrets 0 · files written 1 (this report).

HWAO_STEP9_EXACT_DIFF_DOCTRINE_DONE_20260703T1306Z
