# V53 whole-document review — GPT56

**Verdict: NOT CLEAR.** I verified the subject SHA-256 before reading it. V53 still promotes a demonstrably reachable `allocate_handcheck` guard to an unreachable status, does not supply the specific structural predecessors its own rule requires for the other four promotions, retains the BS-2v self-reference claim that its own checker refutes, and leaves mutually incompatible raise inventories in §5, §11, and the referenced ledger.

## Findings

### F1 — HIGH — the repaired `UNREACHABLE` example still fails its own promotion contract, and L1401 is reachable

**Draft §5 lines 497–506; pinned source lines 1378–1442; `ref/RAISE_SITE_CLASSIFICATION.md` lines 14–18 and 105–110.** Section 5 defines the third status as a guard that “cannot fire at all.” It allows promotion by a stated execution count, but its own absence-clause warning is decisive here: 60,000 non-firings do not establish that universal negative. The pinned callable accepts `budget` as an argument and its docstring explicitly says conditions above budget fail closed. With a contract-shaped 3×9 table of 100 objects per cell and `budget=200`, the exact pinned function raises at L1401:

`RuntimeError: inherited floors need 270 labels, budget 200 — FAIL`

The supplied argument has the documented type and shape; the draft does not state a calling contract that forbids this budget. Thus L1401 does not merely lack structural proof: at the raise-statement unit V53 and the current ledger use, it is reachable. If the intended claim is only that the production call site fixes `budget=HC_REAL_LABELS=500`, that is a call-site claim and requires the per-call-site artifact V53 openly says has not been built. Under the frozen 500 path a real proof is available (`total_need <= 9 × max(30, 3 × 10) = 270 < 500`), but V53 expressly declines that proof and calls the site measurement-only.

The four `(iii)` promotions also remain short of §5's literal evidence rule. Lines 498–501 require a structural promotion to state “the specific earlier condition” that provably subsumes each site. V53 names L1411/L1435/L1437/L1439, but gives all four only the generic docstring statement that feasibility is decided before allocation. It does not bind L1411 to `total_need <= budget`, L1435 to the availability/headroom invariant, L1437 to the loop's `left == 0` or raise partition, or L1439 to the per-cell headroom caps. Those proofs can be derived from the source, but the preregistration's own per-site contract requires them to be stated, not left for a referee to reconstruct.

The fallback sentence does safely route a wrongly marked numerical guard to `INCONCLUSIVE-BY-NUMERICAL-FAILURE`; the finding is the false/under-supported classification record, not an unterminated branch.

### F2 — MEDIUM — BS-2v is still declared unresolved for a self-reference obstacle its own checker disproves

**Preamble line 31; §7 line 733; `tools/void_registry.py` lines 6–19 and 37–39.** V53 still carries “BS-2v coverage still not independent of the converter,” and the BS-2v row still says the registry “cannot be pinned before the converter exists,” making that the reason the gate is UNRESOLVED. The referenced checker says the opposite in its governing comment and implements the construction: the canonical §7.1 rows are determined before the converter, the converter does not author them, and their digest can be stored outside the digested rows without a fixed point. The same V53 row already says the converter cannot alter the pinned contents, contradicting its impossibility sentence.

BS-2v remains honestly UNFILLED because the converter, authenticated schema, and fixtures do not exist. That implementation gap is not this finding. The defect is preserving a false impossibility as the reason for `UNRESOLVED` after CODEX-V52 F5 and the on-disk checker had already isolated and refuted it. Pin the canonical-row digest independently; describe converter/schema implementation as the remaining work.

### F3 — MEDIUM — the claimed raise-inventory repair still contains three incompatible current states

**Draft §5 line 507; §11 line 948; `ref/RAISE_SITE_CLASSIFICATION.md` lines 9–18; `ref/gen_raise_classification.py` lines 10–18 and 41–58.** The ledger table and generator currently count 17 rows literally labelled `NUMERICAL`, four `UNREACHABLE-BY-CONSTRUCTION`, and one `UNREACHABLE-MEASURED-ONLY`. V53 nevertheless gives the category roll-up as `NUMERICAL 22`, then two sentences later says “the numerical class is 17” (or 13 if the four soft rows move). The referenced ledger's own summary says 17, but its line 18 still says the soft reclassification would make the numerical class drop “from 22 to 18”; against the current table that arithmetic is 17 to 13.

Section 11 then retains the superseded sentence that “48 sites are currently unread and the class is reported as a range until they are,” even though §5 says the corpus has been read in full, none is unassigned, and the old 29/31/48 and range are withdrawn. This is not the parked per-call-site-unit finding: even at the acknowledged per-raise unit, V53 and its named artifact do not state one reconciled current inventory. Replace all three stale/current mixtures with the literal table classes, and keep any broader “numerical family” subtotal explicitly named as a roll-up rather than using the `NUMERICAL` class label for both 22 and 17.

## Attacks that held

- Subject custody held: SHA-256 `cc4e289578b129e403c07c78749bc6064a23385e0ec261c0dacd2a35cd010eba` matched before the first subject read. The §0 source pins also matched: `successor_ref_v9.py` = `6a9abbbd900db882b804149edd6d2b8d1780b7114b191e1a58457d7e5875c148`; `closure_worker_v9.py` = `28f8e1f9a8c7bd3d4cf1aabf71a7dfae5f9a1da6b92a6f09fd9c65bfc7ea5959`.
- BS-3g is now on the closed non-χ receipt list and has a `blocks BS-6` edge. Section 11 accurately says the edge is not yet receiptable because no schema, producer, or independent verifier exists; the slot remains DESIGN/UNFILLED. I did not convert disclosed incompleteness into a finding.
- Row L's named-object exemption is narrow and wide enough for its own mandated objects: freeze signature and canonical opening authorization are exempt; the BS-L detached signature is already over the canonical lock digest. The P7-only antecedent phase remains the expressly parked CODEX-V52 F4 issue and is not re-numbered here.
- The class rule is stated as a general condition covering unenumerated computations, gives specific outcomes and every VOID antecedent precedence, and sends a falsified unreachable classification to a named default outcome. The conversion remains openly unimplemented and BS-6 remains blocked.
- The V43 discretionary rerun allowance remains deleted. Searches found historical reruns, required pre-run Stage-P execution, Branch-A refixturing, BS-2a retry semantics, and explicit no-rerun clauses, but no retry after a terminal study-run outcome.
- `KIMI-V11 F7` is the Stage-P finding: it says exact Stage P is not implemented in the §0-pinned file. The V42 correction is accurate.
- The misconduct conditions remain `Any` in both prose and registry: `VOID-5-FORBIDDEN-ACT`, `VOID-5-PROTOCOL-DEVIATION`, and `VOID-5-DIGEST-DEVIATION`. Numerical non-finite/degenerate conditions remain post-unblinding.
- Class counts held at 16 class P / 8 class E; the historical 15/8 → 16/8 transition is explicitly recorded at V36→V37.

## Machine checks and evidence

- `tools/prereg_counts.py`: 16 class P, 8 class E; prose matches.
- `tools/prereg_trace.py --check ... --self-test`: real subject clean; 52-transition trace context; three scope controls, zero failures.
- `tools/void_registry.py --self-test`: 54 antecedents; six controls, zero failures. As V53 discloses, this is name coverage, not semantic coverage.
- `tools/prereg_lint.py --gates ...`: exit 0, zero blocking, 97 legacy-citation advisories. I did not report those advisories as unresolved under option D. The brief's “96” is a dispatch-count mismatch, not a draft defect.
- Independent AST/table inspection confirmed 112 `Raise` nodes and the literal table classes above. The per-call-site unit remains parked as instructed; F3 is the contradiction before reaching that deeper unit problem.
- Direct execution of the pinned `allocate_handcheck` produced the L1401 failure quoted in F1.

I read all 952 subject lines, the V52 reports from both seats, `PREREG_TEXT_V11_KIMI.md`, the pinned reference around the relevant raises and verdict path, `RAISE_SITE_CLASSIFICATION.md`, its generator, the numerical-route and V52-residue notes, and the named checkers. I did not modify the draft, reference code, checkers, or any file outside this report.

<!-- FINDINGS-BLOCK v1 -->
SEAT: GPT56
VERSION: V53
VERDICT: NOT CLEAR
COUNT: 3
F1 | HIGH | REPAIR-REQUIRED | §5 lines 497–506; ref lines 1378–1442 | L1401 is directly reachable under the callable's documented argument surface, and the other four promotions still omit the specific per-site predecessor conditions §5 requires.
F2 | MEDIUM | REPAIR-REQUIRED | preamble line 31; §7 line 733 | BS-2v remains UNRESOLVED for a claimed registry/converter self-reference that tools/void_registry.py explicitly disproves.
F3 | MEDIUM | REPAIR-REQUIRED | §5 line 507; §11 line 948; raise ledger lines 9–18 | V53 and its ledger still conflict among NUMERICAL 22, NUMERICAL 17/13, 48 unread/range, and none unassigned.
<!-- END FINDINGS-BLOCK -->