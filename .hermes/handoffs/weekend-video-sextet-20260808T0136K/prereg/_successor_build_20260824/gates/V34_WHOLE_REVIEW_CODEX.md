# V34 WHOLE-DOCUMENT REFEREE REVIEW — CODEX

## Verdict

**NOT CLEAR.** I verified the exact V34 subject, read all 885 lines, attacked the specified universal-negative surface clause by clause, independently checked the new BS-2a repair announcement against both cited round-6 reports, and checked the V30 preservation pins. Three live document-contract defects remain. Most importantly, §6.2 claims an unlogged archive read would break the access-log chain, but a read that bypasses the mediator is observational and need not alter the chain at all. Separately, the pinned production guard still accepts arbitrary caller-named bytes as “authorization,” and §1's universal statement that a biased or broken instrument “cannot create” a signal exceeds the antisymmetry identity and is contradicted by the document's own surviving-threat list. This verdict does not authorize a run, fetch, image byte, BS-2a fill, or change to any parked principal question.

## Identity and exact comparison

Subject: `../PREREG_SUCCESSOR_DRAFT_V34_20260828.md`.

- Brief-pinned SHA-256: `1c45d32d5f360ab48217ff8114478efa8818cd66f16fa38a8c83d6def31a2948`.
- Independently computed SHA-256: `1c45d32d5f360ab48217ff8114478efa8818cd66f16fa38a8c83d6def31a2948`.
- **Comparison: MATCH — exact 64-hex equality over the named V34 bytes.**
- Independently computed predecessor V33 SHA-256: `b247f40281df3c23282c5be8b8ca9970ba371c43ad74e4664a19a70c9ff2e6bb`, matching the brief's predecessor pin.
- V33→V34 unified diff: retitle; replacement of the BS-2a §7 row; addition of the V32→V33 §10 row. No other byte changes.
- The new quality component also matches its row pin: `ref/bs2a_quality_gate.py` independently hashes to `dfbd63d146b472f194f74d01b313874f23c9a4264f26903b22837ae32aa18508`.

## Numbered findings

### 1. HIGH / BLOCKING — §6.2 line 592 — an unlogged archive read does not necessarily break the log chain

The document says: “Any attempted read of the archive's contents will be blocked by the mediator and logged, **or if unlogged, break the access log's chain**.” The second branch is false as a construction claim. A raw or side-channel read that bypasses Row B can be purely observational: it need not append, delete, reorder, or modify any log record. The existing chain can remain cryptographically valid while containing no evidence of the read. This is exactly the assigned failure shape: the prohibited event can occur while every document-visible artifact remains unchanged.

Clause 4 at line 576 does contain the right prevention mechanism as future work: BS-2k must eliminate every raw-store read path and test the mediator boundary, and inability to enforce it makes BS-2k unfillable. That prevention requirement does not make the line-592 detection claim true. Prevention by construction and retrospective detection by chain break are different properties.

Smallest sufficient repair: delete the assertion that an unlogged read breaks the chain. State instead that an unlogged bypass may be invisible, which is why BS-2k must demonstrate exclusive mediation before freeze; if exclusive mediation cannot be established, BS-2k is unfillable and the archive cannot enter the run's custody claim.

### 2. HIGH / BLOCKING — §5 lines 511–514 — “the authorization does not exist” is not an operative absence guard

The prose says `require_authorization()` refuses real data without an authorization file pinned to a SHA-256, adds that “the authorization does not exist,” and treats that absence as a run guard. The pinned §0 code does not know a canonical authorization identity. `run_production_verdict()` accepts both `authorization_path` and `authorization_sha256` from the caller, and `require_authorization()` only hashes the caller's chosen path and compares it with the caller's chosen digest.

I executed the current pinned `successor_ref_v9.py` against `BRIEF_V34_REVIEW.md`, which is a referee brief and not a run authorization. Its independently computed hash was `117463c070c367d45ad3aca655b1639b0774ac68dcf5ff6ee7d32f79224a794c`; `require_authorization(brief_path, brief_hash)` returned that hash successfully. The same live probe showed `require_complete_sample(1, 1)` returns normally, though this finding is limited to the assigned authorization-absence claim.

Thus the document can say no authorization exists while the operative guard accepts arbitrary existing bytes as authorization, with no authorization schema, signer/authority, study identity, permitted operation, run identity, or independently frozen expected digest. The claimed absence could be false in the only sense the code can test without anything in the document noticing. Other unresolved guards and the BS-6 block still prevent treating this probe as permission to run; that does not repair this guard's contract.

Smallest sufficient repair: define a typed, authenticated run-authorization record and canonical identity, bind the expected signer/study/operation/schema and digest independently of the caller, and make the production runner obtain those expectations from frozen configuration rather than accepting both sides of the equality from its caller. Keep the slot/run blocked until that implementation and its arbitrary-file negative fixture are gated.

### 3. HIGH / BLOCKING — §1 line 120 — “a biased or broken w … cannot create [a signal]” exceeds the identity

The antisymmetric definition guarantees `χ(mirror(x)) = −χ(x)` for a fixed input/mirror pair. It does not guarantee that a biased or broken `w` cannot generate a nonzero sky-correlated slope under a null sky. A classifier can respond to parity-odd raster artefacts, upstream non-equivariant processing, or sensitivity that varies with position; if the prevalence or response of that artefact covaries with `cos θ`, the resulting `χ` has a dipole-like slope without a real handedness signal.

The document notices this counterexample immediately after making the universal claim: it names “chirality introduced upstream,” “sample selection by a non-equivariant process,” and “a nonzero global offset multiplied by a sky gradient in sensitivity” as threats surviving the architecture, and says the explicit control remains DESIGN/UNFILLED. Those are precisely ways a biased/broken measurement chain can create an apparent signal. The mirror identity eliminates the parity-even component of a fixed response; it does not eliminate every position-coupled parity-odd failure.

Smallest sufficient repair: narrow the sentence to the property actually enforced, e.g. “a spatially uniform parity-even classification preference contributes no centred dipole slope under the exact mirror construction.” Do not retain “biased or broken w cannot create one” without the upstream/equivariance/position qualifications.

### 4. MEDIUM / REPAIR-REQUIRED — §7 line 698 — the BS-2a pin should state the gate evidence at its exact strength

The central citation is real and the verdict scope is accurately quoted: `BS2A_CODE_GATE_CODEX_R6.md` and `BS2A_CODE_GATE_GPT56_R6.md` both say **CLEAR for FREEZING the quality-predicate component; not a fill authorization**, and both end `**CLEAR**`. Both preserve the arbitrary-hostile-input limit, confirm 49,211/65,060, and leave BS-2a DESIGN/UNFILLED.

Two details need tighter custody wording:

1. V34 calls all 325 pairwise cases “deletion probes caught, strictly.” CODEX R6 lines 132–150 say the 325/325 pairwise result was filter-derived from real control outputs after an AST argument about control flow; only six pairs were literally source-mutated and re-executed. GPT56 R6 line 100 explicitly says it did not run all 325 pairwise deletions in round 6. The evidence can be credited, but the row must distinguish the derived 325-case sweep from the six literal pair mutants rather than making them read as 325 executed source deletions by both seats.
2. “A crash fails closed, never a PASS” is true only under process-exit semantics. Both reports found the post-verification `--emit` failure: an honestly earned `MATCH` can print before a destination-write crash, after which the process exits nonzero. The reports correctly classify this as no false verifier acceptance and require consumers to honor exit status. The row should carry that integration limit rather than relying on the ambiguous word “PASS.”

Smallest sufficient repair: say “CODEX derived 325/325 pairwise coverage from executed controls and literally mutated six representative pairs; GPT56 literally mutated all 26 singles in R6,” and say “observed crashes exit nonzero; consumers must gate on exit status because a post-verification emit failure can print MATCH before failing.” This finding does not convert the component freeze into a BS-2a fill.

## Universal-negative attack ledger

I searched the requested lexicon (`never`, `nowhere`, `cannot`, `must not`, `in no case`, `none`) case-insensitively. V34 has **74 token occurrences on 67 lines**; the brief's “~71 clauses” is therefore a fair approximation, with the difference caused by multiple tokens on several long lines. I inspected every occurrence in full context and asked (a) what must be true, (b) construction versus assertion, and (c) whether falsity can remain invisible. The line-by-line disposition follows. Counts in parentheses are token occurrences on that line.

- `44(1)`: historical/current-revision limitation; the code/prose precedence gap cannot be repaired by the unchanged text alone. Held.
- `120(2)`: “none [meaningful ratio] is available” is bounded by the disclosed denominator/estimand mismatch and held; “cannot create one” fails — Finding 3.
- `124(1)`: communicative purpose (“stated so it cannot be inverted”), not a mechanism claim; the explicit signed constants and BS-4 anchor are the construction. Held as purpose, not proof of reader behavior.
- `129(1)`: exact fixture assertion (`BATTERY-SIGN`); code/fixture-gated. Held.
- `151(1)`: Branch-A non-transfer is a normative invalidation rule with mandatory re-pin/re-gate. Held.
- `181(1)`: counting path's no-payload property is tied to server-side aggregate query text, endpoint/byte ceiling, and count-oracle receipt. Held subject to its named gate.
- `218(1)`: “digest proves consistency, never custody” is a logical limitation, not an absence search. Held.
- `219(1)`: non-regenerable witness claim is tied to separately pinned universe and BS-2s receipt identities. Held subject to those external pins.
- `256(1)`: finite 832,393-row placement closure. Held as measured receipt testimony, not generalized absence.
- `269(1)`: finite historical statement about two direct reproductions not calling closure. Testimony; not needed for a future run authorization.
- `276(1), 284(1), 293(1), 324(1), 458(1)`: Stage-P/BS-5p non-fillability follows from the named missing exact rerun/implementation and remains explicitly blocked. Held.
- `332(1)`: historical description of a prior omission, not a current guarantee. Held.
- `342(1)`: pre-lock reason closure is a closed enum plus “new text required”; future enforcement is BS-2a-gated. Held as an unfilled design requirement.
- `346(1)`: sign-blindness is explicitly required by construction and the unfinished predicates keep BS-2a/BS-6 blocked. Held as an unfilled gate, not as a present implementation claim.
- `384(1)`: post-hoc tuning is prevented for the quality component by fixed thresholds/source digest/component pin; conditional handedness independence is expressly not claimed. Held.
- `395(1)`: code-defined statistic excludes the full-sky `3·D` constant. Held against the pinned symbol contract.
- `459(1)`: production/exploration paths are separated in the pinned code; production uses the full record. Held, without crediting the superseded Stage-P measurement.
- `466(1)`: no-χ-sign BS-2f schema is a frozen requirement whose producer remains blocked. Held as design, not executed fact.
- `474(1)`: “never analysed” is enforced by the accepted-mask contract and post-removal halt. Held for conforming runs.
- `478(1)`: verdict computation is assigned to the code path rather than table reading. Held subject to unresolved guards already disclosed.
- `497(2)`: per-attempt versus run-outcome cardinality and no P8 catalogue-quality removal are closed state-machine requirements; implementation is explicitly unresolved. Held as blocked design.
- `505(1), 506(1), 508(1)`: positive/negative fixture outcomes and N_eq derivation are executable checks. Held.
- `513(1)`: authorization absence is not enforced against arbitrary caller-chosen bytes — Finding 2.
- `522(3)`: the three “never” fields are exact permitted-surface schema exclusions. Held as freeze requirements; their schemas/producers are not represented as already executable.
- `525(1), 527(1), 530(1)`: closed non-χ-bearing schema claims are exact-field requirements, with BS-2a/BS-2k and relevant implementation blocked. Held as design. The no-export requirement depends on exclusive mediation, not on detecting absence after the fact.
- `542(1), 544(1), 545(1), 552(1)`: actor-row “never reads/exports” clauses are capabilities to be enforced by the unfilled mediator/hermetic-worker gates. Held as unfilled requirements, not current accomplishments.
- `553(2)`: key-holder “never licence” is normative; `none` is the explicit no-emission cell. Its enforceability depends on BS-2k exclusive mediation. Held as blocked design.
- `558(2)`: no Stage-C/calibration-fail branch and no P8 catalogue-quality removal are ordered-tree/schema requirements. Held as unresolved implementation requirements.
- `565(1), 567(1)`: universal ban and inability of C2/E to run are backed by the default-forbidden table plus the explicit BS-2a dependency. Held while the system remains blocked.
- `617(1)`: post-read amendment cannot cure a void is a normative temporal rule. Held.
- `620(1)`: “gate-state sentences never exceed the cited artifact's first line” is mostly honored, but the supporting-detail precision defect in the new row is Finding 4.
- `626(1)`: impossibility of clean-room byte reproduction from insufficient public specification is an information constraint, with divergence treated as a spec defect. Held.
- `631(1)`: never reconciling divergence by editing is a STOP policy. Held.
- `675(1)`: C2/E cannot run because BS-2a remains unfilled. Held.
- `698(1)`: crash-never-PASS wording needs exact exit-status/MATCH qualification — Finding 4.
- `700(2)`: BS-2v's author-independence/self-reference claims concern the parked VOID amendment and were not re-litigated; status remains UNRESOLVED.
- `707(1)`: predecessor receipts are barred as evidence for the new path by BS-9's replacement gate. Held as a future gate rule.
- `796(1), 803(1)`: historical failures; the first is documented provenance, the second follows exactly from plus-one p-value resolution at 999 permutations. Held.
- `833(1)–846(1)`: fourteen historical “none cited” cells are explicit transition records under the V1→V15 exemption and are machine-visible in the trace table. Held.
- `868(1)`: current-transition self-reference limitation follows from changing the bytes whose digest the row would name. Held.
- `876(1)`: low-bound BS-8f “cannot pass” is a required future negative fixture, not a claim that `verify_lock()` is already implemented. Held as unresolved work.

The lexical sweep also exposed why a keyword-only search is insufficient: Finding 1's false universal is phrased as “Any attempted read … will be blocked … or … break,” without one of the six seed tokens. I therefore read the surrounding document rather than treating the 74-token census as complete proof.

## BS-2a pin adjudication

- Component identity: live `ref/bs2a_quality_gate.py` SHA-256 matches V34's full digest exactly.
- Citation self-check: both named R6 reports exist, both independently report the same digest comparison, both state CLEAR only for freezing the quality-predicate component, both deny fill authorization, and both end `**CLEAR**`. I did not use the quarantined lint citation result as evidence.
- Recorded limit: arbitrary-hostile-input hardening remains expressly not established; builder-reachable census is bounded to the authenticated 65,060-row output; crashes are nonzero-exit failures, with the MATCH-before-emit-failure caveat noted in Finding 4.
- Slot status: V34 still labels BS-2a `DESIGN, CLASS P — UNFILLED` and names the missing `verify_cutout_integrity`, confidence threshold, retry/failure semantics, ledger schema, and transformed-cutout producer fixtures.
- Counts: `tools/prereg_counts.py` independently returns 15 class P, 8 class E, with only BS-2m claimed filled, for both V33 and V34. Counts did not move.
- Blocking: Rows C2 and E remain unable to run; BS-6 and the first image byte remain blocked.

## V30 preservation pins

I compared raw line bytes, not rendered text.

- §1 scope block: V30 lines 131–133 and V34 lines 131–133 are byte-identical and occupy the same line positions.
- §2.7 conditional-independence sentence: V30 line 384 and V34 line 384 are byte-identical (533 bytes including newline) and occupy the same line position.
- Earlier long-line repairs changed absolute byte offsets, so “position-identical” is satisfied as the brief and prior reviews use it: same line-number position plus byte-identical line/block, not identical file byte offset.

## Machine checks and disclosure handling

- `tools/prereg_counts.py` on V34: 15 class P, 8 class E; prose matches table; only BS-2m claimed filled.
- `tools/prereg_trace.py .. --check V34`: 33 computed transitions, 0 problems.
- `tools/prereg_lint.py V34 --gates .`: exit 0, 23 §7 data rows, 15 class P, 8 class E, no reported inconsistencies.
- **Citation quarantine honored:** I assign no evidentiary weight to lint's citation behavior or its green aggregate result for citations. The new repair-announcement citation was checked manually against the two R6 reports as described above.

## Failed attacks / standing that held

1. The V34 digest, V33 predecessor digest, and BS-2a component digest all match their pins.
2. The V33→V34 delta is limited to the retitle, new BS-2a row, and one trace row.
3. The BS-2a component is not laundered into a filled slot; all named missing pieces remain visible.
4. Class counts and filled-slot count did not move.
5. V30's protected §1 scope and §2.7 line 384 survived byte-for-byte at the same line positions.
6. The conditional-independence limitation survives: it remains unestablished, while the measured coupling raises consequence rather than likelihood.
7. Stage P remains superseded/non-applicable to the 49,211 mask; BS-5p remains unfillable pending rerun.
8. BS-2v remains unresolved; Rows C2/E cannot run; BS-6 and the first image byte remain blocked.
9. I did not re-litigate the parked VOID-registry amendment, gain-control T-completeness fork, or quarantined citation checker.

## Testimony and constraints

- I did not read `/Users/duhokim/NebulaMindData/`.
- I did not fetch or inspect an image byte, fill a slot, run Stage P/C, execute inference, unblind, alter the subject, or mutate git.
- Historical measurement/reproduction statements not independently rerun in this pass are identified in the ledger as finite testimony rather than promoted to universal proof.
- The only intended durable write is this report.

## Evidence ledger

Content read: `BRIEF_V34_REVIEW.md`; all 885 lines of V34; V33→V34 diff; relevant V30 bytes and `V30_WHOLE_REVIEW_CODEX.md`; `BRIEF_V33_REVIEW.md`; `BS2A_CODE_GATE_CODEX_R6.md`; `BS2A_CODE_GATE_GPT56_R6.md`; `BS2A_QUALITY_CUT_RECEIPT_20260828.md`; relevant current `successor_ref_v9.py` authorization code.

Independent executions: V34/V33/V30/component SHA-256; universal-token census and full-context extraction; V33→V34 unified diff; V30 raw-byte and line-position comparisons; current `require_authorization()` arbitrary-brief probe; current `require_complete_sample(1,1)` probe; V33/V34 class-count parser; V34 trace check; V34 lint (citation output quarantined, not credited).

**NOT CLEAR**