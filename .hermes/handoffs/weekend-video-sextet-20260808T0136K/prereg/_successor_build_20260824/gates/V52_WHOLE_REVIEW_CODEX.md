# V52 WHOLE-DOCUMENT REVIEW — CODEX

## Verdict

**NOT CLEAR.** The Row-L exemption repairs the two required signatures that previously self-voided, but the canonical antecedent remains incorrectly phase-scoped and the preamble still declares the repaired contradiction open. More seriously, the new `UNREACHABLE-BY-CONSTRUCTION` status fails its own per-site evidence rule: the alleged five-site live example names no five sites, and the supplied classification record marks all eight `allocate_handcheck` guards `NUMERICAL`, not unreachable. The document also carries mutually incompatible raise inventories and repeats a BS-2v self-reference claim that its own checker source refutes.

## Identity and machine checks

- Recomputed the subject SHA-256 before reading: `a825e5d2045721c44703558156f0532e9d09dc22ca0f9e08fa5031b6831dd2e4` — exact match.
- Recomputed §0 pins: `ref/successor_ref_v9.py` = `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`; `ref/closure_worker_v9.py` = `28f8e1f9a8c7bd3d4cf1aabf71a7dfae5f9a1da6b92a6f09fd9c65bfc7ea5959`.
- `prereg_counts.py`: 16 Class P / 8 Class E; prose matches.
- `prereg_trace.py --check ... --self-test`: real subject clean; all three scope controls fire.
- `void_registry.py --self-test`: 54 antecedents; six controls; zero failures. As the draft correctly discloses, this is name coverage, not semantic coverage.
- `prereg_lint.py`: exit 0, 0 blocking. It emitted **97**, not the brief's stated 96, legacy-citation advisories. They remain advisory under option D and are not numbered findings here.
- `ref/RAISE_SITE_CLASSIFICATION.md` contains 112 table rows and matches the 112 AST `Raise` nodes, but its generator classifies one source-line node at a time rather than failure paths/call sites.

## Findings

### F1 — HIGH / REPAIR-REQUIRED — §5 lines 497–504; `ref/RAISE_SITE_CLASSIFICATION.md` lines 5–16, 101–109

The new `UNREACHABLE-BY-CONSTRUCTION` status does not satisfy its own promotion contract. V52 requires evidence to be **named per site**, then calls five of `allocate_handcheck`'s eight guards a live example of evidence type (iii), but it never identifies which five guards are meant. The supplied classification record makes the contradiction concrete: all eight guards at reference lines 1397, 1401, 1403, 1411, 1435, 1437, 1439, and 1442 are marked `NUMERICAL`; none is marked `UNREACHABLE-BY-CONSTRUCTION`, and the record has no such class at all. Therefore there is no per-site promoted record to falsify and correct if one fires. A collective “five of eight” count is exactly the judgement-without-site-evidence that lines 498–501 prohibit.

This is not merely unfinished conversion code. The text affirmatively labels the example live and type (iii), while the named supporting record says something else. Either identify and mark the five sites with their specific harness/structural evidence, or retract the live promotion claim until that record exists.

### F2 — MEDIUM / REPAIR-REQUIRED — §5 line 504 and §11 line 944

V52's raise inventory describes three incompatible states. Section 5 says the frozen reference has 112 nodes but still reports the old `29 caller + 31 reachable + 48 unread = 108` partition. Section 11 then reverts to **111 raise sites**, says the remainder are `RuntimeError`/`ValueError`, and again says 48 are unread. The on-disk AST and classification artifact instead show 112 nodes, including 39 `ManifestClosureError`, and every node has a table row with current classes 20 caller / 61 integrity / 22 numerical / 3 numerical-planning / 3 typed / 3 wrapper.

The earlier 111 figure can be made true only by explicitly saying “111 exception-instantiating nodes plus one bare re-raise”; line 944 does not do that and falsely says the remainder are only `RuntimeError`/`ValueError`. The 48-unread claim is also stale once the document cites a complete 112-row classification. The class-rule implementation inventory must state one reconciled, current universe.

### F3 — HIGH / REPAIR-REQUIRED — §11 line 944 versus `ref/gen_raise_classification.py` lines 19–35 and `ref/successor_ref_v9.py` lines 1138–1153

The supporting classification is one row per syntactic `raise`, not the per-failure-path/per-call-site classification that V52 itself says is required. The generator walks `ast.Raise` nodes and assigns one class solely from exception type or source line. That cannot implement precedence for a helper used in different phases. For example, the same `perm_record()` non-finite raise at reference line 1153 is reachable from Stage P/Stage C before unblinding and from the production record after unblinding. V52 assigns post-unblinding permutation non-finiteness to `VOID`, while a pre-unblinding failure is not VOID and must follow the more specific/default inconclusive routing. A single source-line class `NUMERICAL` cannot encode both paths.

The same artifact adds `NUMERICAL-PLANNING` for `local_pass()` lines 963/973/986 even though that label is neither one of §5's caller/run/unreachable statuses nor a named lifecycle outcome. Thus the record is useful AST coverage, but it is not the call-site classification V52 says it is. It must enumerate path/phase/caller context and resulting named outcome, including implicit exceptions, before it can support the class rule.

### F4 — MEDIUM / REPAIR-REQUIRED — §6.1 Row L line 584 and §7.1 line 811

The Row-L exemption is narrow enough and wide enough for the three required objects: the P0 freeze signature and P7 opening authorization need exemptions, while the P6 BS-L signature is already over the canonical lock digest. That repair holds. But the canonical antecedent remains scoped only to **P7**: `VOID-6.1L-WRONG-SIGNATURE | ... | P7 | VOID`.

Row L's signing surface spans P0, P6, and P7, and its wrong-signature condition is not itself limited to P7. A non-exempt wrong signature at P0 or a signature over the wrong BS-L digest at P6 satisfies the row's forbidden condition but not the phase of its named antecedent. A generic protocol-deviation ID may overlap the event, but it does not make the Row-L stable ID's source/phase tuple true. Phase-index the antecedent (or split it by ceremony) so the registry represents every phase in which the row's condition can fire.

### F5 — MEDIUM / REPAIR-REQUIRED — preamble line 31; §7 line 730; `tools/void_registry.py` lines 6–19, 37–39

Two ruled/open-status statements remain stale. First, line 31 still lists “§6.1 Row L's signing path voids itself” as a carried-open item, directly contradicting V52's principal-ruling paragraph and repaired Row L. If retained as history, it must be explicitly version-scoped rather than presented as a current carried-open list.

Second, BS-2v still says the registry **cannot be pinned before the converter exists** and therefore the gate is unresolved. The named checker source states the opposite: §7.1's canonical rows can be digested and pinned before the converter because the converter does not author them; storing that digest outside the rows avoids self-reference. The checker already computes that digest. BS-2v may remain UNFILLED because the converter/schema do not exist, but it cannot honestly remain unresolved for an impossibility its own tool disproves. Pin the current canonical-row digest in the preregistration and describe the remaining work as converter/schema implementation.

## Failed attacks / repairs that held

1. **BS-3g receiptability is honest incompleteness, not a false fill.** Section 11 explicitly says the edge is not receiptable without a `SLOT_SCHEMA` entry, producer, and verifier; the slot remains DESIGN/UNFILLED and BS-6 remains blocked.
2. **The Row-L named-object exemption itself held.** Exactly the freeze signature and canonical opening authorization were previously caught; the BS-L detached signature is over the canonical lock digest and needs no exemption. The finding is the remaining antecedent phase, not exemption breadth.
3. **`UNREACHABLE-BY-CONSTRUCTION` fallback wording is routing-safe in isolation.** If a correctly marked site fires, lines 503–504 direct it to `INCONCLUSIVE-BY-NUMERICAL-FAILURE` and require record correction. The defect is that the claimed live sites are not named or marked.
4. **V42's citation correction held.** `gates/PREREG_TEXT_V11_KIMI.md` F7 is the Stage-P finding and explicitly says exact Stage P is not implemented in the §0-pinned file; KIMI F4 is the unrelated §6.1 access finding.
5. **Rerun deletion held.** No discretionary study-run retry, seed schedule, attempt log, cap, verifier, or extra slot was revived. Row P expressly forbids discretionary retry and post-unblinding removal does not rerun Stage C.
6. **VOID misconduct phases held.** Forbidden acts and protocol/digest deviation remain `Any` in §5 and §7.1; only numerical non-finite/degenerate conditions are post-unblinding.
7. **Class counts held.** The table parses to 16/8, current prose states 16/8, and the transition record identifies the historical 15/8 → 16/8 change at BS-3g.
8. **Pinned hashes, predecessor memo provenance, and Stage-P transfer claims checked in the assigned files without opening real χ data.** No subject/reference/checker bytes were modified.

## Evidence and limits

Read content: the governing V52 brief; all 948 lines of V52; the pinned reference around planning, masks, permutations, calibration, and production; `RAISE_SITE_CLASSIFICATION.md`; its generator; `PREREG_TEXT_V11_KIMI.md`; `FINDINGS_MAP.md`; `void_registry.py`; and the named freeze/trace artifacts needed for the attacks above. Ran SHA-256 checks, lint/count/trace/VOID checkers and self-tests, AST/table reconciliation, exact text searches, and read-only git status checks. I did not read real χ data, fetch external data, modify the draft/reference/checkers, or write outside this report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: CODEX
VERSION: V52
VERDICT: NOT CLEAR
COUNT: 5
F1 | HIGH | REPAIR-REQUIRED | §5 lines 497–504 | The claimed live UNREACHABLE example names no five sites, and the supporting ledger marks all eight guards NUMERICAL.
F2 | MEDIUM | REPAIR-REQUIRED | §5 line 504; §11 line 944 | V52 carries incompatible 108/111/112 raise inventories and a stale 48-unread status.
F3 | HIGH | REPAIR-REQUIRED | §11 line 944 | The supporting per-raise ledger cannot classify phase-sensitive failure paths or produce the required call-site outcomes.
F4 | MEDIUM | REPAIR-REQUIRED | §6.1 Row L line 584; §7.1 line 811 | The wrong-signature antecedent is P7-only although Row L's signing condition can fire at P0, P6, or P7.
F5 | MEDIUM | REPAIR-REQUIRED | preamble line 31; §7 line 730 | Stale Row-L-open and false BS-2v self-reference claims contradict V52's repair and its own checker.
<!-- END FINDINGS-BLOCK -->