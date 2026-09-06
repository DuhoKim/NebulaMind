# DISCLOSED LIMITS vs REPAIRED CONTRADICTIONS — the two categories, kept apart (Blanc's order 02:06 KST, 2026-09-07)

A rule that documents what it cannot prove is honest. A rule that documents a contradiction between its text and its code as if it were a limit is not. This file is the register of which is which for the option (A) sampling amendment; every candidate text from V28 on carries the same split in §3c, and nothing that reaches Duho may merge the two columns.

## A. DISCLOSED LIMITS (a precommitment may legitimately carry these; reviewers confirm their disclosure)
| limit | where disclosed | what it means for the ACTUAL RUN |
|---|---|---|
| L-OFF: the OFFLINE candidate (PRODUCTION default) accepts a coherently forged approval event, a history rebuilt before the freeze, and codex's attack A | §3c; every inspection since V22 | if Duho adopts the offline baseline as the rule to run under, the driver does not detect those three fabrications; only the composed mode does |
| L-COV: THE COVENANT — the validator authenticates the published append-only history and ordered publications, not when operations occurred nor the completeness of unpublished observations/decisions (before genesis publication or between publications); an unpublished absence-based CLOSED can be erased; the seed is unchanged; a late approval event stays disqualifying | code, design doc, §3c, questions file | hidden attempts cannot change the fixed-round seed; an erased absence-based CLOSED cannot be detected by any validator; a stronger guarantee needs independently retained decision evidence, NOT implemented |
| L-RCPT: the fabricated-first-receipt step (Option A′ only) | design doc, §3c, questions file | irrelevant under Option C (recommended: no receipt path) |
| L-INH: the INHERITED V15 driver trusts the object lists / pool and exclusion digests (verify_split UNADOPTED, off) | §3c; inspection row 6 | a coherently sealed swapped list loads unless verify_split is adopted |
| L-AVAIL: GitHub's feed availability (300 events / 30 days; 30 s–6 h latency) governs Option C; retry dispositions are stateless — an inconsistent identity can stay pending indefinitely without ever loading | questions file, §3c | loss before tune or between tune and holdout closes the approval under the rule; the loader refuses, it does not persist the closure |

## B. CONTRADICTIONS (text says one thing, code does another) — REPAIRED in the next candidate, never disclosed as limits
| finding | the contradiction | repair (track 8, successors) |
|---|---|---|
| V27-1 precedence | the text promises "positive inconsistencies are terminal; retries are unavailable evidence"; the code declared a retry before examining a same-id contradiction, skipped the contradiction when a verbatim copy was present, and turned a locally decidable wrong-repository mismatch into a retry when the feed retrieval failed | `provenance_designs_v8`: local input checks BEFORE retrieval; same-id contradictions BEFORE the undetermined-delivery and verbatim-presence shortcuts; the same-commit arm scoped to the pinned protected ref |
| V27-2 tri-state propagation | the text promises tri-state delivery on the complete path; the driver's witness-commit precheck and the open-event stage still used the Boolean helper, and a git launch exception raised instead of reporting undetermined | driver v12 precheck and `validate_continuation_v8` open-event stage use `delivery()`; OSError → UNDETERMINED |
| V27-3 names/count | the driver lineage table, comments, an inspection header and a suite count said things the bytes do not | swept with per-item assertions |

Earlier contradictions of the same kind (V20 fatal … V26-1/2) were repaired in tracks 1–7; they are listed in the outcomes, not here, because they are closed. Any proportionality argument put to Duho later must carry: (1) the exact rule text to sign; (2) the enumerated remaining failure modes; (3) what each means for the actual run; (4) which are limits (column A) and which would be unrepaired contradictions (column B — none may remain).

## C. UNREPAIRED CONTRADICTIONS as of the V28 review (2026-09-07 02:44 KST) — column two, open
| finding | the contradiction | status |
|---|---|---|
| V28-1 (codex) | the text promises same-id contradictions and locally decidable mismatches are decided before any retry; driver v12's witness-commit precheck returns RETRY-EVENTS-UNAVAILABLE on UNDETERMINED delivery before composed provenance can run local_precheck, retrieval and the same-id check | OPEN — track 9 |
| V28-2 (codex) | the same on the history-open stage: validate_continuation_v8 reclassifies v3's Boolean refusal as EVIDENCE-UNAVAILABLE without consulting the feed | OPEN — track 9 |
Column A qualifications accepted from codex: L-INH is a default-mode implementation limit (verify_split staged, unadopted), not irreducible; L-AVAIL combines an external availability limit with stateless closure enforcement. Both restated with their mode qualifications in the next candidate. Column A never absorbs a column-C entry.

## D. Section C resolved in the V29 candidate (2026-09-07 02:57 KST)
| finding | repair (track 9, successors) | status |
|---|---|---|
| V28-1 | driver v13's witness precheck defers an undetermined delivery, in composed mode, to composed provenance (local_precheck → retrieval → same-id contradictions → only then the retry); codex's clause (1) in force | REPAIRED in V29 — moves to column B; the V29 reviewers test it on the complete path |
| V28-2 | validate_continuation_v9 consults the feed before returning EVIDENCE-UNAVAILABLE / EVIDENCE-INCOMPLETE | REPAIRED in V29 — moves to column B |
Column A re-qualified (codex V28): L-INH = a default-mode implementation limit (verify_split staged, unadopted), not irreducible; L-AVAIL = external availability + stateless closure enforcement, never covering a decidable mismatch. UNREPAIRED as of V29 staging: none known.

## E. Column C reopened at the V29 review (2026-09-07 03:17 KST) — UNREPAIRED CONTRADICTIONS, open
| finding | the contradiction | status |
|---|---|---|
| V29-1 (codex) | clause (1) promises local mismatches and obtainable same-id authentication before ANY retry; the seed re-deriver's REDERIVE-RETRY (D:303) precedes composed provenance, so an undetermined + wrong-repo / same-id-contradicted approval event is kept pending with zero retrievals | OPEN — track 10 |
| V29-2 (codex) | the history stage's RETRY-REMOTE-UNAVAILABLE and the approval stage's RETRY-EVENTS-UNAVAILABLE precede the local check of the retained open event (type / repository / ref) and its same-id authentication | OPEN — track 10 |
Section D's "none known" is superseded by this section. Column A unchanged (codex: qualifications necessary and now substantially honest).

## F. Section E resolved in the V30 candidate — by ONE resolver, not a point fix (2026-09-07 03:39 KST; Blanc 03:20)
| finding | repair (track 10) | status |
|---|---|---|
| V29-1, V29-2 (and the whole pattern V27-1 / V27-2 / V28-1 / V28-2) | the precedence order stated once (`PRECEDENCE`), enforced in one resolver (`resolve`) to which every composed stage contributes (driver v14 `composed_resolver`), exhibited pairwise (`V30_PRECEDENCE_EXHIBIT_20260907.md`) | REPAIRED in V30 — moves to column B; the V30 reviewers test it |
UNREPAIRED as of V30 staging: none known.

## G. Column C reopened at the V30 review (2026-09-07 04:13 KST) — UNREPAIRED CONTRADICTIONS, open; section F's "none known" superseded
| finding | the contradiction | status |
|---|---|---|
| V30-1 (codex, FATAL) | a JSON `null` open-event file is treated as "nothing to check" by the track-10 resolver and the composed load ACCEPTS, even over a published history rewrite — §3c and Q1 Option C promise every required event authenticated | OPEN — track 11; the lane's own regression, to be reproduced in executed output first |
| V30-2 (codex) | verify_witness's fetch failure and the verifier import raise retries BEFORE the local sweep; list shape / disjointness / split checks run AFTER the resolver; unnormalized exceptions bypass it | OPEN — track 11 |
| V30-3 (codex) | the history helper suppresses a higher finding (rewrite) behind a lower one (open retrieval empty); authenticate_event returns UNAVAILABLE before evaluating EXPIRED; three retrievals, evidence not shared, so retrieval order can hide an obtained contradiction | OPEN — track 11 |
Column A unchanged (codex: the mode qualifications make them honest; none licenses V30-1/2/3 into this column).

## H. Section G resolved in the V31 candidate (2026-09-07 04:30 KST)
| finding | repair (track 11) | status |
|---|---|---|
| V30-1 (FATAL, the lane's own) | reproduced in executed output first; the open-event file must hold a PushEvent object; ACCEPT only when every required stage ran and contributed nothing | REPAIRED in V31 — moves to column B; the V31 reviewers test it |
| V30-2 | the whole composed path as a staged finding collector; list checks before anything remote; witness fetch / verifier import as contributed retries after the local sweep; exceptions classified; an explicit code→class table with unknown codes flagged | REPAIRED in V31 — column B |
| V30-3 | the history stage as a collector; one evidence snapshot; expiry before unavailability | REPAIRED in V31 — column B |
UNREPAIRED as of V31 staging: none known.

## I. Column C reopened at the V31 review (2026-09-07 05:00 KST) — section H's "none known" superseded
| finding | the contradiction | status |
|---|---|---|
| V31-1 (codex) | the text promises independent stages; a failed S1 (witness fetch) leaves S2–S5 not run, so obtainable contradictions and local defects are never contributed; S0's git launch precedes its local precheck; the helper import is outside the wrapper | OPEN — track 12 |
| V31-2 (codex) | the snapshot clause promises every obtained event evaluated; a later page's failure discards page one's obtained contradiction | OPEN — track 12 |
| V31-3 (codex) | the collector clause promises every derivable finding; the per-entry / extension loops break at the first defect; the same-commit arm is not evaluated for an undetermined retained delivery; the standalone path returns on remote failure before the local open-event check | OPEN — track 12 |
| V31-4 (codex) | the class table is not total (SPLIT-*), a family prefix silently classes unknown codes, malformed REMOTE evidence is classed as retained input, receipt exceptions escape the receipt policy | OPEN — track 12 |
Column A unchanged. The FATAL (V30-1) stays REPAIRED (codex confirmed).

## J. Section I resolved in the V32 candidate — under ONE property, NSD (2026-09-07 05:35 KST; Blanc 05:02)
| finding | repair (track 12) | status |
|---|---|---|
| V31-1, V31-2, V31-3, V31-4 | the contribution half of NSD: independent stages on the locally readable context, page-keeping snapshot, no-stop loops and both arms before availability, allowlist classification by provenance; controls derived from the INDEPENDENCE table (66 pairs) | REPAIRED in V32 — column B; the V32 reviewers test it |
UNREPAIRED as of V32 staging: none known.
