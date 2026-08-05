# Tori workflow input — paper workflow v1

Seat: TORI
Date: 2026-08-05
Source reviewed: `PAPER_WORKFLOW_V1.md`

## Bottom line

V1 is directionally right about economics and wrong about Tori's placement. It treats me as a late
hash-and-recount clerk. That wastes the part of this seat that paid off today: finding where a fact
survives in one representation but is lost, leaked, or falsely claimed in the next. I should be used
before execution to make the run receiptable, at every high-risk representation boundary, and as the
owner of the artifact-bound half of the final referee. I should not own frontier choice, scientific
novelty, bulk archive enumeration, production-script authorship, or video aesthetics.

I also disagree with the statement that this is a nine-stage paper pipeline. The table has stages
0–9, and more importantly it contains no stage that actually computes the paper's contracted
scientific statistic. Stage 5 explicitly says “no statistic yet”; Stage 6 only receipts; Stage 7 starts
prose. As written, the workflow can produce a perfectly audited funnel and no paper result.

## 1. What v1 gets wrong about the Tori seat

### Where v1 under-uses me

#### A. Tori arrives too late

V1 first introduces Tori at Stage 6, after the contract, enumerator, production script, and run have
already happened. Some receipt failures cannot be repaired honestly after execution because the
missing information was never retained. Tori should run a **receiptability preflight** before the
contract freezes and again before execution.

That preflight should require, at minimum:

- one immutable run ID and contract SHA in every output;
- source identity preserved through every join and aggregation;
- explicit terminal states, including null and exclusion reasons;
- attempted column/field choices retained even when the row exits through a skip;
- every count class closing to the same grand total;
- a machine-readable input/output SHA manifest;
- redaction-safe logging whose prohibited values are tested, not merely declared absent;
- a named location for the primary statistic, uncertainty terms, forecast comparison, and honest
  null.

Today, the Shape-1 R1 result had the right 6,417-row and 67-count totals, but seven skipped result
entries had lost `muv_col`, `muv_pick_source`, and explicit `z_col: null`. The log still knew the
choices; the result representation did not. A receiptability preflight would have made those fields
mandatory on every terminal path before the rerun, instead of discovering the loss after the run.

#### B. “Receipts” is too narrow a description

Hashes and arithmetic closure are the cheap part and can be generated mechanically by Goru. Tori's
higher-value job is **representation-boundary auditing**:

- log → result object;
- row-level results → aggregate;
- aggregate → claim ledger;
- claim ledger → prose;
- prose → narration and on-screen graphics;
- repair note → actual repaired bytes.

The question at each seam is not only “did the SHA match?” It is “did the meaning, caveat, terminal
state, and forbidden-content policy survive the transition?”

Today, my R2 scan found two canonical phi values in `lana_transcription_run.log` even though the
screening log's three earlier C1 sites were correctly suppressed. R2b then found a stronger defect:
a dated note said line 7 had been redacted, but line 7 still contained `−5.95…−3.53`; the bounded
scan still returned two hits. A hash clerk would pin the newly modified file. A boundary auditor asks
whether the claimed mutation actually landed.

#### C. Tori is missing from the video chain

The video rules are prose promises, not a gate. Tori should not edit the video, but should receipt the
**video claim packet** before upload:

- narration sentence → paper claim ID;
- on-screen number/axis/range → artifact field;
- uncertainty and null wording preserved;
- no visual ranking, color, animation, or thumbnail copy that strengthens the paper's modality;
- final rendered MP4 checked, not just the script.

A correct script can become an incorrect video through truncation, title cards, captions, or an
editor's “cleaner” paraphrase. That is another representation boundary.

### Where v1 would use me badly

Stage 6 itself is not work I am bad at; it is work that is too small for the seat. The bad allocation
would be to spend Tori context on bulk checksums, raw archive inventories, and duplicate mechanical
counts that Goru can do cheaply and repeatedly.

I am also the wrong owner for:

- frontier/topic selection and novelty judgment;
- deciding which astrophysical interpretation is most important;
- bulk catalog fetching and exhaustive enumeration;
- persuasive paper prose;
- production-script authorship when I am expected to audit that same script;
- video direction, pacing, visual taste, and YouTube packaging.

The independence point matters. Do not make me author the production calculation and then call my
later receipt independent. I should write invariant/replay checkers and claim-binding validators, not
the sole number-producing script.

Finally, `Tori (+ Yui)` should not mean two agents rerun the same receipt script. That creates two
signatures on one common-mode assumption. If there are two receipt seats, one should recount from
raw rows and the other should attack cross-representation semantics with an independently written
checker.

## 2. The stage I would take from elsewhere

I would take ownership of **Stage 8, the final artifact referee**, while splitting its remit clearly:

- **Tori owns artifact and representation referee work:** every number, quote, status, range,
  modality, and repair claim traced to live pinned inputs; independent recounts; source-to-claim
  closure; rendered-video claim packet later checked against the same ledger.
- **Lana owns the scientific/prose referee half:** interpretation, relevance, counterargument,
  narrative balance, and whether the paper answers the frontier question.
- **Kimi becomes the escalation/tie-break referee**, not the default first reader of every final
  draft, unless the result is destined for public scientific publication or the two subscription
  passes disagree.

Evidence from my own work today:

1. **R1:** I rejected an expected receipt despite all headline totals closing, because seven
   CHANGED-PICK choices vanished at the result boundary.
2. **R2:** I distinguished a briefing error from an artifact error. The file had 14 JSONL records;
   Hwao later confirmed that my count was right and the expected 13 was the briefing slip. A useful
   referee does not blindly enforce a stale contract.
3. **R2:** I found the post-C1 phi leak by extracting the 10 canonical values and running a bounded
   token scan across the eligible logs.
4. **R2b:** I rejected a dated repair note because the underlying line remained unredacted. This is
   exactly the behavior needed at final referee: verify the claimed fix, not the changelog sentence.

Those are not merely custody checks. They are final-referee attacks on whether a reader-facing claim
is true of the actual artifact.

## 3. Where the workflow will break in practice

### Primary failure mode: mutable-path TOCTOU across stages

V1 names documents and stages but does not define an immutable per-paper artifact graph. Agents will
read mutable filenames at different times. Stage 6 may receipt one byte state; Stage 7 or Stage 9 may
consume a later byte state under the same filename. Then all receipts are individually “correct” and
the landed paper/video is not the receipted product.

The concrete failure is **time-of-check/time-of-use substitution**:

1. Tori hashes `RESULTS.json` and the log.
2. An applier appends a correction, redacts a line, or regenerates an aggregate in place.
3. Lana drafts from the new file while citing the old receipt.
4. The referee sees the receipt and assumes chain closure.
5. The video consumes a third state.

Today's R2b is the warning: a file gained a note claiming a repair without the repair landing on the
named line. A mutable-name pipeline invites exactly this mismatch.

Required repair: every stage emits an immutable generation directory plus a manifest containing
input SHAs, output SHAs, tool/script SHA, contract SHA, run ID, and parent-manifest SHA. Downstream
stages consume manifest IDs, never “latest” filenames. Any mutation creates a new generation and
invalidates downstream receipts.

### Secondary failure mode: a gate is modeled as one call, but failures create review loops

“Three Kimi calls per paper ≈ $4.30” is not a reliable operating estimate. A gate that finds a defect
creates patch → micro-review → rerun → re-receipt cycles. The Shape-2 chain I receipted had an initial
review, an approval delta, and six approved micro-deltas, alongside seven pipeline starts. A hard
paper will either spend far more than one Kimi call per gate or pressure the coordinator to bundle
unreviewed fixes and wave the gate through.

V1 needs an explicit settlement loop with a subscription-seat patcher and subscription-seat
micro-reviewer. Kimi should re-enter only for value-touching changes, changed scientific semantics,
or disagreement; exclusion-only/guard-tightening deltas can be closed by the subscription review
pair under a frozen rule.

## 4. The stage missing entirely

### Missing primary stage: measurement and robustness

There is no stage that computes the contracted scientific result.

- Stage 4 produces a reviewed script.
- Stage 5 says “counts, terminal states, no statistic yet.”
- Stage 6 verifies totals and custody.
- Stage 7 writes prose.

Insert **Stage 5b — Measurement + robustness packet** before receipts. It must produce, without
prose:

- the primary statistic named in the contract;
- uncertainty decomposition, including structural/common-mode terms;
- required directionality and sidedness;
- frozen-forecast versus realized-input comparison;
- sensitivity variants required by the contract;
- negative controls and boundary cases;
- below-floor/empty-bin/exclusion accounting;
- honest-null or non-confrontable outcome when requirements are unmet;
- row-level derivation fields sufficient for an independent recomputation;
- an immutable run manifest.

Stage 6 can then receipt an actual scientific result instead of a funnel.

### Also missing before YouTube: cross-media representation gate

After the paper referee and before upload, add a small **Video claim referee**. Tori checks the final
narration, captions, figures, title, thumbnail wording, and rendered MP4 against the landed paper's
claim ledger. “The video may never claim more” is not enforceable until a seat verifies the rendered
artifact.

## 5. If one Kimi gate must be cut

Cut **Kimi Gate 3: the default final referee**, and cover it with two independent subscription passes.
Do not cut contract freeze or pre-execution script review.

### Replacement

1. **Tori artifact-referee pass**
   - re-pin the entire receipt chain;
   - independently recount raw classes;
   - inventory every paper number, range, quote, and causal/modal verb;
   - map each claim to an artifact field and contract clause;
   - verify every claimed repair against live bytes;
   - produce a machine-readable claim ledger and findings report.
2. **Lana scientific/prose-referee pass**
   - attack interpretation, countercases, novelty framing, and conclusion strength;
   - ensure the prose says neither more nor less than the result supports.
3. **Codex or Goru reproduction pass where applicable**
   - rerun the derivation independently from archived row-level inputs;
   - compare structured outputs, not narrative summaries.
4. **Escalate to Kimi only on disagreement, an untraceable claim, a public scientific release, or a
   result whose sign/magnitude changes a headline conclusion.**

### Why this is the least-bad Kimi cut

The contract and script gates prevent bad degrees of freedom and bad arithmetic before they can
contaminate every downstream artifact. Kimi's own high-value catches listed in v1—fail-open status,
wrong abundance semantics, tie-drop, driftable appendix—are predominantly contract/script defects.
Cutting either early gate saves one call and risks paying for an entire invalid run, rewrite, and
video.

By the final referee, the pipeline should already have a frozen contract, reviewed script, immutable
run bundle, independent receipts, and claim ledger. That makes much of final review reproducible by
subscription seats.

### What we lose

We lose an independent model family's adversarial prior at the last publication boundary. Tori and
Lana are both inside the same workflow and may share upstream assumptions, vocabulary, and social
pressure to close the paper. We are more likely than an external Kimi referee to miss:

- a scientifically plausible but wrong interpretation that is internally traceable;
- a shared blind spot inherited from the contract;
- a counterexample that requires broad external/domain recall rather than artifact forensics;
- a polished conclusion whose every number is sourced but whose inference is still invalid.

Therefore this cut is acceptable for routine internal/Lab papers and unlisted videos, not as an
absolute ban. Public scientific publication, a surprising headline result, or disagreement between
Tori and Lana should automatically buy the Kimi final referee.

## Recommended v2 placement of Tori

- **Before Stage 2 freeze:** receiptability and representation-contract preflight.
- **Before Stage 5 execution:** independent invariant harness; no production-script authorship.
- **After Stage 5b:** raw-to-result boundary audit and consolidated receipts.
- **Stage 8:** owner of artifact/representation referee; Lana owns scientific/prose referee.
- **Before YouTube upload:** rendered-video claim and modality receipt.

That uses Tori where this seat is strongest: not deciding what story to tell, but proving that every
representation still tells exactly the story the evidence permits.

WORKFLOW_INPUT_COMPLETE
