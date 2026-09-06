ACCESS_SHA=f94b45e626ec95f1d2a60da783eb23c70f02394bbbe2be7389583013dd00cc49

Independent Seat B review of the complete, staged, unadopted V31 package. Nothing in this report adopts or approves the rule, its composed mode, a receipt origin, or a study seed.

Authorship disclosure: the package records earlier Codex authorship of builder field-validation code at 00:13–00:18 on September 6 and says that code no longer participates. I did not author or change the reviewed implementation. I reused earlier Seat B temporary-fixture scaffolding, redirected it to this sandbox's v11/v15 modules, and independently executed the results below. Historical authorship and execution chronology remain dependent on the filed records; the current counterexamples do not depend on accepting a prior verdict.

The V30 null-file FATAL is repaired. I found no new undisclosed composed acceptance bypass. Nevertheless, V31 is not ready to put to Duho: four MAJOR implementation/text contradictions remain. Passing the complete package tests does not establish the collector's advertised completeness.

For code references, D means [run_configurations_v15.py](/Users/duhokim/.claude/jobs/5b2f0371/tmp/selrule_v31_gate_bva0owfg/_stage2_image_analysis_20260901/_optionA_dev/fourier_chirality/run_configurations_v15.py:342); P means [provenance_designs_v11.py](/Users/duhokim/.claude/jobs/5b2f0371/tmp/selrule_v31_gate_bva0owfg/_stage2_image_analysis_20260901/_optionA_dev/track2/provenance_designs_v11.py:143); R means [the V31 rule](/Users/duhokim/.claude/jobs/5b2f0371/tmp/selrule_v31_gate_bva0owfg/_stage2_image_analysis_20260901/OPTION_A_INSTRUMENT_SELECTION_RULE_DRAFT_V31_20260907.md:38), especially its opening paragraph and §3c, lines 3 and 38; Q means [the unchanged questions file](/Users/duhokim/.claude/jobs/5b2f0371/tmp/selrule_v31_gate_bva0owfg/_stage2_image_analysis_20260901/QUESTIONS_FOR_DUHO_TRACK2_ORIGIN_AND_RECEIPTS_20260906.md). Line numbers below refer to the reviewed bytes. Execution sources, complete findings, request counts and logs are retained at `/var/folders/64/71dstw0j1gd_n58lsxnhl3p80000gn/T/codex_v31_seatb_jufevjzb`.

**V31-1 [MAJOR] — the staged wrapper still permits availability failures to suppress independent checks. UNREPAIRED CONTRADICTION with R §3c and the carried V29/V30 clauses.**

D:351–353 catches a stage's first exception, but D:373–375 only installs the conjunction's context if the entire S1 function returns. Any S1 refusal therefore prevents S2, S3, S4 and S5 from executing. This is not merely withholding acceptance until prerequisites succeed: it withholds checks whose inputs are already available.

Executed, on coherently sealed temporary identities using PRODUCTION's actual re-deriver:

- Genuine retained approval plus an available conflicting same-ID live event: `EVENT-FORGED`, one Events API request. Make only `git fetch origin` fail: `WITNESS-FETCH-FAILED`, zero Events API requests, S2–S5 NOT RUN. Both feed orders give the same suppression.
- A sealed identity with `schema_version='WRONG'`: `IDENTITY-SCHEMA`. Add the witness-fetch failure: `WITNESS-FETCH-FAILED`; the locally readable schema defect is never contributed.
- Published rewrite plus witness-fetch failure: `WITNESS-FETCH-FAILED`; the separately obtainable remote-history finding is never contributed. Seed findings are likewise absent in the S1/S4 pair.
- S0 itself launches `git rev-parse --show-toplevel` at D:360 before its approval precheck at D:361. A fixture launch OSError with a retained wrong repository returns `IO-UNAVAILABLE`, zero retrievals, and no `EVENT-INCONSISTENT`. The promised degraded local sweep is not independent of git availability.

There is also a literal exception outside the stage wrapper: D:350 calls `_P()` before classification exists. A targeted unavailable import of `provenance_designs_v11` raised raw `ImportError`, not `DataIntegrityFail` or a classified finding. This is an unavailable dependency, not class 0 by cause.

The five original V30 constructions now take their expected dispositions, but that narrower success does not implement the whole-path clause. Section H of the limits register must not close V30-2 unconditionally.

**V31-2 [MAJOR] — a failed later page erases already obtained contradictory evidence. UNREPAIRED CONTRADICTION with the snapshot/reconciliation clause.**

P:143–161 accumulates successful pages in a local `out` list, then raises `EventsUnavailable` on any subsequent HTTP/JSON failure. Neither the accumulated events nor their provenance accompanies the exception. D:379–382 consequently leaves the shared snapshot empty.

Executed: page one contained a valid same-ID canonical contradiction plus enough events to require page two. With a healthy second page the composed result was `EVENT-FORGED`. With page two returning HTTP 503, it was `RETRY-EVENTS-UNAVAILABLE: SERVER-ERROR`; with malformed JSON on page two, `RETRY-EVENTS-UNAVAILABLE: MALFORMED`. Both failure cases made two page requests and contributed no FORGED finding, despite having obtained the contradictory event.

V31 does use a single logical retrieval on paths reaching S2. It does not preserve all evidence obtained during that retrieval. A partial snapshot cannot justify acceptance or an absence/expiry inference, but an affirmative contradiction already obtained must survive the later failure under the stated policy. Replacing three retrievals with one does not by itself satisfy that policy.

**V31-3 [MAJOR] — helpers still stop before independently derivable higher findings. UNREPAIRED CONTRADICTION with R §3c's collector and predicate promises.**

Three executed examples:

1. P:351–364 stops the per-entry loop at its first missing publication. I supplied an authentic approval and open event, omitted entry 1's publication without evidence of batching, and supplied a later push proving entry 2 was delivered in a multi-commit batch through before..head ancestry. The complete load returned `RETRY-HISTORY-CONTINUATION: EVIDENCE-INCOMPLETE` for entry 1. The entire history finding list contained only that retry. Independently calling the production delivery predicate on the later batch and entry 2 returned `DELIVERED`. `HISTORY-PUBLICATION-BATCH`, class 4, was derivable but absent. The extension loop also breaks at P:341–344, and publication ordering is evaluated only if the entire publication loop completes.
2. P:207–208 returns EXPIRED/UNAVAILABLE for undetermined retained delivery before reaching the absent-only same-commit predicate at P:212–213. I retained an event with an unknown `before`, a real later head and no commits shortcut; the feed carried a distinct-ID genuine event demonstrably delivering the approval commit. The retained event was absent and canonical bytes differed. The standalone result was `UNAVAILABLE`, and the complete result `RETRY-EVENTS-UNAVAILABLE`, even though the code's own live-delivery predicate returned `DELIVERED`. Under the package's expressly defined same-commit contradiction predicate, FORGED was independently derivable. The repaired same-ID arm does not exhaust the promised predicate.
3. The standalone `validate_continuation_v11` retrieves, then P:319–321 returns on unavailable remote head/fetch before checking the open event locally. Wrong open repository plus remote-head failure returned `RETRY-REMOTE-UNAVAILABLE`. The complete composed path normally catches this through S0 and returns `OPEN-EVENT-INCONSISTENT-INPUT`; the standalone path does not. The two paths must be distinguished, not jointly certified as enforcing clause (1).

The requested three-defect example DOES work: rewrite + wrong open repository + empty feed returned `HISTORY-CONTINUATION: OPEN-EVENT-INCONSISTENT-INPUT`. Captured contributions included the S0 local finding, approval-feed unavailability, the S5 open-input finding, `HISTORY-NOT-AN-EXTENSION`, and per-entry-feed unavailability. Class 0 correctly won. This establishes that specific repair, not that every history finding is collected.

A malformed open payload also prevents independent history verification: a published rewrite plus a PushEvent object with scalar `payload` produced `MALFORMED-RETAINED-INPUT` and `HISTORY-OPEN-EVENT-INVALID`, with no rewrite finding. It refused safely, but contradicts the stronger “every derivable finding”/“nothing downstream is skipped” claim.

**V31-4 [MAJOR] — classification is not total over actual named checks, and exception types do not establish evidence provenance. UNREPAIRED CONTRADICTION with the named class boundaries and receipt policy.**

- Actual raises `SPLIT-INPUTS` at D:453 and `SPLIT-NOT-REPRODUCED` at D:461 are missing from P:290–306. Both return `unclassified=True`. I exercised enabled split verification against a real mismatching temporary catalogue file: the complete path produced a flagged class-0 `SPLIT-INPUTS`. The advertised inventory test does not include these real raises. Conversely, a new `EVENT-NEW-UNKNOWN` code receives class 0 with `unclassified=False` through the broad prefix. The literal claim that every unknown code is flagged is stronger than this family-prefix classifier.
- An events runner returning malformed JSON correctly produces class-5 `RETRY-EVENTS-UNAVAILABLE: MALFORMED`. But a JSON list containing a PushEvent with scalar `payload` passes retrieval's shallow shape check, raises AttributeError during authentication/history processing, and becomes class-0 `MALFORMED-RETAINED-INPUT` at P:310. I executed that result on a valid retained identity. The malformed object came from the remote feed, not retained input. Exception type alone cannot justify a local-integrity conclusion.
- An expired approval with a receipt whose schema, events and digest were valid but whose `origin` was a nonempty list raised AttributeError at P:552. D:397 does not normalize this as a receipt refusal; the S3 wrapper emitted class-0 `MALFORMED-RETAINED-INPUT`. R explicitly assigns receipt-path refusal class 3 regardless of cause. That policy only holds when `verify_events_receipt` returns `(False, reason)`; it does not hold for exceptions escaping it.

The explicitly named choices are otherwise intelligible: seed verification/mismatch in class 4, `REDERIVE-RETRY` in class 5; publication findings in class 4; PENDING-PUSH/HISTORY-DIVERGED terminal for this invocation with publication/reconciliation as the remedy; receipt refusal in class 3 by policy; EXPIRED above derived terminal and temporary unavailability above incompleteness. These are policies, not consequences of a universal “local versus remote” theorem. The counterexamples concern their implementation and completeness.

**V31-5 [MINOR] — stage bookkeeping and evidence wording overstate what was established.**

D:353 adds a stage to `ran` even when its body raises. With a null open file, S5 explicitly says its inputs prevent history execution at D:411, yet `_stages_run` includes `S5-history` and `not_run` is empty. The accompanying finding prevents acceptance, so this is not the repaired FATAL recurring. It does contradict “a stage whose inputs failed is NOT RUN.” Distinguish attempted, completed, blocked and successful stages. `_findings` at D:419 retains class/code/stage/flag but omits reasons; several distinct history refusals collapse to the same generic `HISTORY-CONTINUATION` code there. The full reasons were obtainable in my resolver instrumentation, not from that stripped list alone.

The track-11 receipt correctly exhibits the first null load, but its run-1 test stops at that failed assertion. The displayed run-1 output does not separately show the later rewrite+null subcase executing. I independently reproduced both acceptances on retained v14 and both refusals on v15; the repair is real. Attribute the historical rewrite reproduction to evidence that actually ran it, rather than to the unexecuted remainder of that test. Similarly, run 2b was 10 passes and one wording failure; run 2c reran the affected test successfully. “All 11 passed after the disclosed restoration” is accurate as that combined evidence, not as a single all-green run-2b log.

**Acceptance guard, exceptions and the composed raise inventory.**

The requested malformed/missing-input probes did not skip into acceptance:

| Complete-path input | Executed refusal | Event-page requests |
|---|---|---:|
| JSON identity null, list, scalar or string | `IDENTITY-SCHEMA` | 0 |
| Open file null, list, scalar, string, object without `type`, or wrong type | `HISTORY-OPEN-EVENT-INVALID` | 1 |
| Missing open file, also with NOT-EARLIEST + bad seed bodies + unavailable remote | `HISTORY-OPEN-EVENT-MISSING` | 1 |
| Coherently sealed identity missing `approval_witness` | `EVENT-INCONSISTENT`, plus S1 `IDENTITY-WITNESS-MISSING` | 0 |
| Malformed first-page JSON | `RETRY-EVENTS-UNAVAILABLE: MALFORMED` | 1 |
| Beacon record read denied at its Path read | `BEACON-RECORD-UNREADABLE` | 0 |
| Required seed context absent with no earlier finding, using a labelled `require_beacon=False` test protocol | `STAGE-NOT-RUN` | 0 |

The last row exercises D:418 directly: S2–S5 were not run and the guard refused. It is a negative fixture configuration, not PRODUCTION's setting. Missing/unreadable/invalid retained open events are class 0 in these tests. No evidence here supports claiming that a required stage can currently be skipped into ACCEPT.

I read the actual raise sites rather than relying on track 11's inventory. `raise_inventory.json` records 81 explicit raise nodes across the selected loader-related functions, including offline comparison arms. On the composed path:

| Location | Actual refusal sites and class assessment |
|---|---|
| D:332, 350; `_P` D:63–65 | Dispatch has no named pre-conjunction refusal. The helper import remains outside `stage`; unavailable import escapes, class 5 by cause. Access to malformed Protocol objects would also escape, but is not an identity-input acceptance path. |
| Adoption D:76–77 | `ADOPTION-MISSING`, `ADOPTION-MALFORMED`: class 0, called inside S1. |
| Verifier/re-deriver D:124, 132, 134 | `VERIFIER-UNAVAILABLE`: class 5; `BEACON-RECORD-UNREADABLE`: named class 0; dynamic `REDERIVE-RETRY`: class 5, other `REDERIVE-*`: class 4. Called inside S1/S4. |
| Witness D:181, 183, 185, 188, 190, 193, 196, 198 | Missing/malformed commit, not-a-repository, lacks-journal, lacks-record and remote-URL mismatch: class 0. `WITNESS-FETCH-FAILED`: class 5. `WITNESS-NOT-PUSHED`: class 4. These are caught at S1, but terminate its collection and suppress later stages. |
| Conjunction D:214–231 | Missing/unsealed/non-witnessed identity; schema/required-field/pool/exclusion/adoption/rule/beacon-mode checks; missing re-deriver: class 0. |
| Conjunction D:238–259 | Outcome/source/witness fields/commit; approval record existence/digest/blob/history; first-approval and approval schema lines: class 0, except fetched-evidence `APPROVAL-COMMIT-NOT-PUSHED` at 253, class 4. |
| Conjunction D:262–291 | T_sign/T_pulse/round/exclusions, retained type/ref/time/lateness/digest/delivery/provenance, nonce and adoption binding: class 0. D:278's named undetermined-delivery refusal is offline-only; composed defers that condition. |
| Conjunction D:294–318 | Collection-log digest/blob/chain/genesis/count/first accept/lock/CLOSED/conflict; beacon record digest/blob/read/binding/statement/relay-shape checks: named class 0. Their implicit I/O/type/JSON exceptions reach the outer stage classifier, with the provenance problems above. |
| Lists D:325, 327 | Three dynamic `IDENTITY-<list>-SIZE-OR-TYPE` raises and `IDENTITY-OVERLAP`: class 0, now S0b before remote work. |
| Local/seed/history bodies D:356, 358, 406, 411 | Missing identity/schema: class 0; seed mismatch: class 4; absent valid open-event input: class 0. Caught by their stage wrappers. Other local/event/history outcomes are contributed directly rather than raised. |
| Enabled split D:453, 461 | `SPLIT-INPUTS`, `SPLIT-NOT-REPRODUCED`: class 0 by cause, but flagged as unknown. Catalogue I/O and classifier exceptions also need contextual classification. |
| Final D:420 | The intended resolver decision, after constructing the available finding list. It cannot recover findings suppressed inside earlier bodies. |

The separate CLI/environment checks precede identity loading: argparse rejects invalid invocation, and D:159/162 rejects environment hash/value mismatches, class 0 by cause. Raw module/import/file-access failures are not all class 0. Manifest, scoring and tuning-receipt checks are outside this identity conjunction and should not be described as covered by its resolver. There is no remaining ordinary named S1 `DataIntegrityFail` escaping directly around `stage`; the defect is that catching one still decides what may be examined next.

**Pairwise execution and retrieval counts.**

I ran all 21 pairs among S0, S0b, S1, S2, S3, S4 and S5: 84 complete-path invocations, with both feed orders and production versus reversed independent S3/S4/S5 body order in an explicitly labelled in-memory experiment. Inputs were: S0 wrong open repository; S0b a coherently resealed short tuning list; S1 witness-fetch failure; S2 HTTP failure, with partial-page contradictory evidence in the S2/S3 pair; S3 an obtained conflicting approval copy; S4 coherently rebound invalid seed-signature bodies, with PRODUCTION's callback unchanged; S5 a published rewrite and restoration. Actual findings were captured at the resolver, and also passed to the unchanged resolver in both list orders.

| Pair | Production winner | Requests |
|---|---|---:|
| S0/S0b | Open-event input inconsistency, class 0 | 1 |
| S0/S1 | Open-event input inconsistency, class 0 | 0 |
| S0/S2 | Open-event input inconsistency, class 0 | 1 |
| S0/S3 | Open-event input inconsistency, class 0 | 1 |
| S0/S4 | Open-event input inconsistency, class 0 | 1 |
| S0/S5 | Open-event input inconsistency, class 0 | 1 |
| S0b/S1 | List-size/type inconsistency, class 0 | 0 |
| S0b/S2 | List-size/type inconsistency, class 0 | 1 |
| S0b/S3 | List-size/type inconsistency, class 0 | 1 |
| S0b/S4 | List-size/type inconsistency, class 0 | 1 |
| S0b/S5 | List-size/type inconsistency, class 0 | 1 |
| S1/S2 | `WITNESS-FETCH-FAILED`, class 5; S2–S5 absent | 0 |
| S1/S3 | `WITNESS-FETCH-FAILED`, class 5; FORGED absent | 0 |
| S1/S4 | `WITNESS-FETCH-FAILED`, class 5; seed finding absent | 0 |
| S1/S5 | `WITNESS-FETCH-FAILED`, class 5; rewrite finding absent | 0 |
| S2/S3 | `RETRY-EVENTS-UNAVAILABLE`, class 5; obtained FORGED absent | 2 |
| S2/S4 | `RETRY-EVENTS-UNAVAILABLE`, class 5 | 1 |
| S2/S5 | `HISTORY-NOT-AN-EXTENSION`, class 4 | 1 |
| S3/S4 | `EVENT-FORGED`, class 1 | 1 |
| S3/S5 | `EVENT-FORGED`, class 1 | 1 |
| S4/S5 | `HISTORY-NOT-AN-EXTENSION`, class 4 | 1 |

Winner classes were invariant across the four variants of every pair. That includes invariant wrong winners where findings were suppressed. All S1-failure pairs left S2–S5 NOT RUN. S2/S3's two requests were pages of one logical retrieval, not two snapshots.

I additionally ran all six A/B/C/D pairs in 24 complete-path invocations, with both feed orders and actual ABCD versus DCBA body execution in memory: A=S0 local event sweep, B=S3 snapshot authentication, C=S4 seed re-derivation, D=S5 history. The DCBA experiment preloaded the already-readable identity/open JSON solely to supply the bodies' input dependencies; it changed no reviewed file or production re-deriver. AB/AC/AD selected class 0; BC/BD selected FORGED; CD selected the class-4 rewrite. Those collected findings survived reversal. The 21-class-pair filed exhibit also passed.

These are controlled order experiments, not a claim that every dependency can literally be reversed in production. S1 produces the context currently required by S2–S5, and S2 supplies their feed; the fact that an unavailable S1 blocks otherwise independent evidence is itself the failed derivability test. Exhaustive code-path or arbitrary-input coverage is not established by a finite pair matrix.

Happy-path retrieval count was one. Reaching S2 with first-page HTTP/JSON failure made one request; successful page one followed by failing page two made two. Invalid open files still permitted one retrieval; malformed identity, missing approval witness, unreadable beacon and S1 failures made zero. No tested path made the old three separate logical event retrievals. P's history collector itself made no Events API retrieval. Remote git operations and the optional receipt verifier remain separate operations; “one snapshot” here concerns the event feed.

**The three states, exercised.**

1. OFFLINE PRODUCTION default: genuine identity ACCEPTED; coherent wrong-repository retained approval ACCEPTED; inspection counter-cases 1, 2 and A still ACCEPTED. The offline conjunction does not authenticate the live feed or published history. Undetermined approval delivery returned `IDENTITY-WITNESS-COMMIT-UNDETERMINED`; positive non-delivery returned `IDENTITY-WITNESS-COMMIT`; coherently rebound unverifiable seed bodies returned `REDERIVE-RETRY`; witness-fetch failure retains `WITNESS-FETCH-FAILED`. `_list_checks` runs after the conjunction, re-derivation and optional split verification, as D:334–338 describes. V30-4's corrected offline wording agrees with execution.
2. STANDALONE v11: genuine retained event AUTHENTIC and genuine published continuation accepted; wrong repository/positive non-delivery INCONSISTENT-INPUT; same-ID contradiction FORGED; plain covered absence INCOMPLETE; unresolved ancestry without contradiction UNAVAILABLE; expiry EXPIRED; strictly earlier qualifying event NOT-EARLIEST. History detects rewrites/genesis/batch defects in the established cases. Its remote-failure local-precheck gap and the shared authentication same-commit gap remain as V31-3 above.
3. COMPOSED v15: genuine identity ACCEPTED; the filed fabricated-event and published-history cases refused; null/open-shape bypass repaired; genuine seed re-derivation is executed. It still returns lower retries or incorrect class-0 findings in the newly executed cases. This mode is staged and unadopted, not the default CLI rule.

The retained V30 driver independently accepted null both on normal history and over a published rewrite/restoration, while its genuine open-event control refused `HISTORY-NOT-AN-EXTENSION`. V31 refused both null cases as `HISTORY-OPEN-EVENT-INVALID`; both fixtures used their respective PRODUCTION re-deriver by identity, with no replacement callback.

The additional V26–V29 controls also ran: before-only/head-only changes → FORGED; conflicting same-ID copy beside verbatim genuine → FORGED; missing descendant with only the retained event → UNAVAILABLE; missing descendant with genuine conflicting same ID → FORGED; unlaunchable git in `delivery` → UNDETERMINED. On the complete path, unknown `before` + real later head + genuine same-ID conflict → `EVENT-FORGED`; wrong repository with healthy feed or HTTP 503 → `EVENT-INCONSISTENT`; retained undetermined event alone → `RETRY-EVENTS-UNAVAILABLE`. The history-open analogues returned `OPEN-EVENT-FORGED`, `OPEN-EVENT-INCONSISTENT-INPUT`, and `RETRY-HISTORY-CONTINUATION: EVIDENCE-UNAVAILABLE`. Positive open non-delivery was terminal.

Unverifiable seed bodies plus wrong repository selected `EVENT-INCONSISTENT`; plus same-ID contradiction selected `EVENT-FORGED`; genuine approval selected `REDERIVE-RETRY`. Open wrong repository beat unavailable remote and approval HTTP 503 on the composed path; the aliased older tests also exercised open same-ID contradiction plus unavailable remote. NOT-EARLIEST beat seed retry in both feed orders. EXPIRED beat remote retry, including undetermined approval plus a newer-only feed. Missing open file beat NOT-EARLIEST, seed retry and remote unavailability together.

Equal server timestamps did not establish an earlier event in either order. A verbatim earliest event plus a later distinct qualifying event remained AUTHENTIC. A synthetic absent-retained/same-commit redelivery fixture reached FORGED by the expressly defined absent-only arm; that alone does not prove an honest protected-branch execution can produce that history. In actual temporary git pushes, an honest fast-forward advance and a delivery to another ref did not become FORGED; verbatim presence plus those pushes stayed AUTHENTIC. The branch-protection/no-deletion assumptions matter.

GitHub documents event IDs as unique and PushEvent delivery fields as `ref`, `head` and `before`; a commits list is not required by that documented payload. Distinct genuine events should not share one ID under that contract. Uniqueness alone is not a guarantee that every metadata field is eternally byte-immutable. The fixed FORGED identifiers are defensible as the package's retained/live contradiction disposition, not attribution of wrongdoing to a particular producer. [GitHub event types](https://docs.github.com/en/rest/using-the-rest-api/github-event-types).

**Disposition of the carried findings and Blanc's requirements.**

“REPAIRED” below refers to the original concrete defect and its executed regression cases; it does not erase the broader current contradictions above.

| Item | Judgment |
|---|---|
| V30-1 FATAL | REPAIRED; independently reproduced on v14 and refused on v15. |
| V30-2 | NOT REPAIRED as the whole-path promise. Original wrong-repository/fetch and list/503 examples repaired; V31-1 and V31-4 remain. |
| V30-3 | NOT REPAIRED as collector/snapshot completeness. Original empty-feed rewrite and expiry-before-undetermined cases repaired; V31-2/V31-3 remain. |
| V30-4 | REPAIRED; offline has multiple availability dispositions, as now stated. |
| Blanc: order stated once | REPAIRED as the explicit eight-class order; classification coverage/policies still require V31-4. |
| Blanc: one enforcing place across the whole path | NOT REPAIRED; a minimum over only surviving findings is insufficient. |
| Blanc: pairwise exhibit | REPAIRED as a resolver exhibit; NOT a proof of derivability. Executed stage-pair failures are above. |
| Blanc: tests kept and added | REPAIRED; 147/26 plus 11 aliased precedence tests passed. |
| V29-1, V29-2 | Original seed/remote/approval-feed precedence cases REPAIRED; their universal clause still NOT REPAIRED under V31-1/V31-2. |
| V29-3, V29-4 | REPAIRED: pin backreferences/names corrected; strictly-earlier ordering, including ties, executed. |
| V28-1, V28-2 | Original undetermined-delivery same-ID cases REPAIRED; universal both-path/every-stage assurance remains NOT REPAIRED. |
| V28-3 | REPAIRED: later delivery versus earlier ordering, historical filename/digest associations and text qualification. |
| V27-1 | Original local/same-ID/absent-only precedence cases REPAIRED; current complete-pattern exceptions remain above. |
| V27-2 | REPAIRED for tri-state propagation and git-launch handling within `delivery`; the distinct S0 root-discovery launch is V31-1. |
| V27-3 | REPAIRED as the historical lineage/count corrections; new stage-bookkeeping wording needs V31-5. |
| V26-1, V26-2 | Original before/head contradiction and stale-object false-forgery cases REPAIRED. The full same-commit predicate is still incomplete under V31-3. |
| V26-3 | REPAIRED as the cited historical text corrections. |
| P1 | Ancestry-aware batch predicate REPAIRED; collection of a later proven batch remains NOT REPAIRED under V31-3. |
| P2 | Plain absence/empty-feed false-forgery defect REPAIRED; broader precedence qualifications above apply. |
| P3, P4 | REPAIRED: cost/availability wording and covenant in Q. |
| N1 | COVENANT, not a repaired operation-completeness mechanism. |
| N2 | Original empty/missing-versus-proven-batch distinctions REPAIRED; all-findings claim still has V31-3. |
| N3 | REPAIRED: unrelated unpublished commits refused before publication; current CLI names present. |
| N4 | REPAIRED by the correction note; read per test, not by counting unittest ERROR labels. |
| N5 | Historical current-label/pin-list dispatch issues REPAIRED; new current overclaims identified above. |
| M1 | Distinct ordered publication requirement built; operation-time/completeness remainder is COVENANT. New collection gap is V31-3. |
| M2 | REPAIRED: pending commit reused/reconciled; outer producer failure entries published. |
| M3 | COVENANT, correctly widened to unpublished decisions before and between publications. |
| M4 | REPAIRED as A′'s missing history/per-entry receipt disclosure; C's “works today as described” needs the current contradictions closed. |
| M5 | REPAIRED by archived original bytes and immutability rule; historical-list qualification below. |
| M6 | Historical text sweep REPAIRED; do not promote historical helper descriptions into current guarantees. |
| A | Authenticated genesis-only opening built; original late-first-publication refusal REPAIRED; unpublished-operation remainder is COVENANT. |
| B | Producer boundary built and original defects REPAIRED; full history-collector completeness still NOT REPAIRED. |
| C | Shared delivery semantics/tri-state controls REPAIRED in the named cases. |
| D | REPAIRED: builder control failure logged before False. |
| E | REPAIRED: render-end must be the last relevant record. |
| F | Original empty-feed/HTTP/availability defects REPAIRED; partial retrieval evidence loss is V31-2. |

Section H's unconditional resolution of column C/G is therefore not supported: V30-1 can move to repaired; V30-2/3 cannot be closed as universal guarantees.

Not every disclosed limit is irreducible. L-OFF is a limitation of the selected offline mode, L-INH expressly describes an unadopted implementation choice, and L-AVAIL combines an external retention limit with changeable stateless closure enforcement. L-COV is structural without independent decision evidence; L-RCPT is structural under the single-account/label-only trust design. Those mode qualifications make the disclosures substantially honest. None licenses the new contradictions into the limits column. Already-decidable mismatches being kept pending are specifically outside L-AVAIL's current qualification.

**Covenant, receipt trust, questions and cost.**

The complete covenant is stated in P's header, the design document, R §3c and Q: published append-only history and distinct ordered publications are authenticated; underlying operation times and completeness of unpublished observations/decisions are not; an unpublished absence-based CLOSED may disappear before genesis publication or between publications; the fixed-round seed does not change; an authentic late approval remains disqualifying; stronger completeness requires independently retained decision evidence, not implemented. I appended and erased an unpublished CLOSED in both intervals in temporary fixtures: offline and composed both ACCEPTED. That is COVENANT behavior, not a new bypass of the promised published-history boundary.

I also created a FIRST receipt under the lane-proposed `{actor: ops-witness, session: OPS}`, committed and pushed it in a protected local fixture, and created no OPS-retained copy. The receipt verifier accepted it. With approval evidence expired and required history evidence live, the configured approval-receipt composed path ACCEPTED; the same identity under Option C returned `EVENT-EXPIRED-NO-RECEIPT-PATH`. This reproduces the precisely disclosed trusted step. The label is unadopted lane metadata, not a Duho decision. Delegation requires no per-receipt human confirmation. A second token on the same GitHub account does not supply an independent identity.

Q1 Option C remains the sound recommendation after the implementation contradictions are repaired: ALL approval/open/per-entry events must authenticate at tune and holdout; loss closes that approval under the rule; temporary unavailable/incomplete evidence retries the same commitment; no replacement approval, round, seed, split or attempt follows. The loader does not persist study-level closure. “No residual trusted step” in C concerns the receipt-origin step, not GitHub, drand or branch-protection assumptions. Its present “only option that works today as described” wording cannot be certified while the priority/collection contradictions remain.

A′ accurately says approval-only receipt support exists and that history-open/per-entry support is NOT BUILT. Its proposed receipts cover ALL required events and substitute only for EXPIRED; unavailable/incomplete evidence and proven inconsistency retain their dispositions. B accurately says NOT IMPLEMENTED: a second GitHub identity or inaccessible custodian signing key needs Duho once, and a durable signature avoids relying forever on another expiring PushEvent. Q2 correctly asks nothing. Q should remain held; these implementation repairs require no additional Duho chores or design permission.

The current documented window is up to 300 events created within the past 30 days, with repository-event latency of 30 seconds to six hours. It is not a guaranteed number of days in which both protected invocations can run. [GitHub Events API](https://docs.github.com/en/rest/activity/events).

Cost is one acknowledged push per HISTORY ENTRY, including genesis and failure entries; one collector/builder invocation can emit several entries. PENDING-PUSH means reconcile/retry the same pending publication, DIVERGED/HISTORY-DIVERGED refuses incompatible local history, and unavailable remote evidence produces the appropriate remote/witness availability refusal. These are not the only possible diagnostic codes. No current affirmative “one push per freeze” claim was found in R/Q/P/design text. The design document's line 34 does contain “NOT one push per freeze” outside quotation, as an explicit correction; its line 3 and P:124 quote the earlier error. Fixture remotes were local bare repositories with non-fast-forward receives denied and fixture-supplied gh runners. No live publishing occurred.

**Execution, counts, preservation and immutable pins.**

All 147 requested tests in 26 suites passed with the requested interpreter split, `PYTHONDONTWRITEBYTECODE=1`, warning settings and separate environment variables. Counts: driver v15/V15 23/17; history 4; witness 3; builder v31/V15 8/4; beacon v31 7; verifier 4; track 1 10; track 2 8/2; tracks 3–5 10/7/6; track 6 5+1; track 7 4+1; track 8 7+1; track 9 3+1; track 10 4+1; track 11 5+1. Pinned older label tests ran against their specified V25–V30 texts; track 9's version-agnostic case ran against V30 as explicitly requested. This is not a claim that passing predecessor label tests validates V31's prose.

The 11 track-8/9/10 precedence tests additionally passed with imports aliased to v11/v15. The 10-test family fixture also passed. Exactly one inherited RuntimeWarning occurred in the requested suite logs, at `fourier_chirality.py:87`; no ResourceWarning occurred.

Both beacon exhibit outputs were byte-identical and printed `2160fa754ce3db25613389d58bacd3098763ea8536744558e9dae96c5b4f0ae1`. The drand-only exhibit printed `45d6149a2ccf30cb167dc4331455f3403a733516a82399292b1e7ad2c029e531`. All 35 executed inspection verdicts matched BOTH filed V30 and V31 tables after normalizing temporary commit hashes. The resolver's 21 class-pair exhibit passed.

Signature preimages reproduced exactly:

- V31: `f94b45e626ec95f1d2a60da783eb23c70f02394bbbe2be7389583013dd00cc49`
- V30: `98881c7ecba0ac3bb718983f8534aaa55d325efeb4314d72b31b64b95af2abb9`
- V29: `4458b821e3a1249c0646ce2790491f4d04e7224d0ef60721144354e216450599`
- V28: `c9e65f1bfc2bdac10716760670c85866d20c1ec0ca1d9aebdfa5b83842804fc2`

V31 contains 102 distinct full digest values: 99 resolve to retained file bytes, and the other three are the two reproduced exhibit-output digests and the reproduced sentinel digest. V23–V30 contain respectively 80/81/83/85/89/90/91/99 values, with those same three generated-value exceptions. I hashed their retained file bytes and inspected filename associations. No new pinned-byte drift was found. Historical wrong filename/digest associations in V27/V28 cannot literally match the mistakenly named path; their intended bytes remain retained, and the corrected V29–V31 associations resolve. This historical documentation defect is not missing historical bytes.

All four archived V22 originals matched their pinned digests. The V22 and V24 copied-digest lists contain all four old values; the V23 list contains successors and does NOT contain those four old values. The pin-drift record's specific reliance on the V22 list is supported. The stronger requested assertion that all three lists carry the old digests would be false. Q's unchanged digest is `4e6dc490485cf956a6471ccad6be73fb86bfe0dc0d60712343b18f3a162e8a52`.

Fail-first evidence was read per test. Track 11 run 1 supplies three behavioral first-failure observations, one missing-classifier interface error, and one text failure; it does not execute every later subcase after the first failing assertion. Runs 2/2c and the present executions establish current repaired cases. The correction note remains controlling: track 1 all behavioral; track 2 eight missing-interface errors with old behavior separately demonstrated; track 3 five missing-interface/five behavioral; track 4 three missing-interface/four behavioral; track 5 three/three. Existing-function exceptions are not automatically missing interfaces. Historical timestamps and unretained intermediate edits cannot be authenticated by current passing tests.

Individually preserved and rechecked:

- Sample sizes 400/200/2,000 and floors 380/190/1,900; strict Wilson lower-bound >0.70, fixed denominator and the one-candidate/one-attempt rule.
- Failed-set exclusion; all 2,644 dry-run identity lines are distinct; rounds 6440756/6441904/6441924 remain excluded in production. Fixture exclusion overrides stayed inside fixture processes.
- E5(d) custody's separate-account, point-in-time evidence and interval covenant; blindness and freeze-before-fresh-pixel rules. This review does not certify actual custody installation or access isolation.
- An ACTUAL FUTURE drand round: at host UTC `2026-09-06T19:39:13.667826+00:00`, prospective T_sign `19:40:13Z` gave T_pulse `19:51:00Z`, round 6443108. Collection returned `BEACON-NOT-YET` with zero fetch calls. No exhibit or probe round was adopted as a study seed.
- ONE holdout remains the rule; `holdout_once` is PREPARED NOT ADOPTED and defaults False. The executable marker's stricter behavior remains an adoption choice.
- E1's test-count correction is a FACTUAL ERRATUM: the retained V15 driver suite executed 17 tests, not the historical “10.”
- `verify_split` remains UNADOPTED, default off; the stronger path exists but its classifier coverage needs V31-4.
- Guarded-pool reconstruction from the absent GZ1 source table is UNVERIFIABLE HERE. Hashing the supplied guarded_pool.csv does not substitute for that reconstruction.

The current suite totals, exhibit digests, inspection names and corrected pin associations are verified. The current universal collector/classifier guarantees and stage-status claims are not true; listing tests or marking older prose historical does not repair them. All V31 file-pin paths were rehashed unchanged after execution. Only the requested report was written in the reviewed directory; probe sources, fixtures and logs are outside it.

**Required clauses before Duho is asked to adopt exact reviewed behavior.**

Repair versioned successors and reproduce the failures above before changing their behavior. Retain the existing V30 clauses and add precise implementation-backed text along these lines:

“Each independently readable input and independently obtainable evidence source contributes findings even when another prerequisite fails. A failed freeze-witness fetch or verifier import does not prevent local integrity checks, obtainable approval/open-event contradiction checks, seed verification whose retained inputs are available, or independently obtainable history checks. The collector records which individual checks are blocked and why; a blocked check never permits acceptance. Local retained-event type/repository/ref checks do not depend on launching git.”

“One logical event retrieval accumulates every successfully obtained page with provenance. A later page's transport, HTTP, schema or JSON failure contributes unavailability without discarding earlier events. Every obtained event is evaluated for applicable affirmative contradictions and ordering predicates. Partial retrieval never establishes complete presence requirements, absence, expiry or acceptance merely because an unrequested or failed page may contain missing evidence.”

“History validation evaluates every independently checkable commit/publication and ordering relation despite an earlier missing or invalid entry, preserving all findings already derived if another check fails. Authentication evaluates both defined contradiction arms before a lower-priority availability disposition whenever their inputs are available. The standalone and composed paths share these obligations; unavailable remote state does not excuse locally decidable open-event mismatches.”

“Classification is explicit for every actual enabled refusal, including split verification. Malformed remote evidence is classified by its remote provenance, not as malformed retained input. All receipt-verification failures, including malformed nested values and exceptions, follow the stated receipt-loss policy. Unknown-code handling is defined precisely, including how code families are validated. Diagnostics distinguish attempted, completed and blocked checks and retain each finding's specific code and reason.”

Keep the complete covenant, mode qualifications, ALL-events Option C consequences, OPS first-receipt trusted step and unbuilt A′/B labels. Update the limits register and Q's readiness claim only after the reviewed successor implements these clauses. These are ordinary package repairs, not decisions to delegate back to Duho.

VERDICT: NOT-SIGNABLE
