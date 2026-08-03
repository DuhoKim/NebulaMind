# Hwao/Fable Doctrine Report — B1-prime adversarial review

Task: HWAO B1-PRIME adversarial doctrine review · Status: COMPLETE — read-only except this report; no generic NLI run; no models downloaded; no DB/git/deploy; no Step 8 prose.
Verified directly: master brief, gold draft JSONL (all 15 rows with labels, legacy stances, audit classes, rationales), verifier script (prompt construction inspected line-level), packet metrics.

## Verdict: `PASS_WITH_PATCHES`

The direction is right and the hygiene is mostly excellent. The verifier is genuinely *not* generic NLI (a scope/attribution prompt harness with the doctrine's rules encoded — "if the evidence supports a narrower claim, use qualifies, not supports"), the prompt receives **only** `claim_text` + `evidence_snippet` (no gold label, no legacy stance, no audit class — I checked the format call), the gold is class-balanced (majority baseline 0.333, unlike B1's 0.711 skew), and every artifact says `step8_unlocked: false`. What blocks "gold" status is the labels themselves — four of fifteen have specific problems, and at n=15 each one is 6.7 accuracy points.

## Attack findings

**1. Gold circularity / poisoned provenance — the quarantined rows are in the gold (serious).**
Rows 26084 and 26088 (`legacy_stance: refutes`) are the **quarantined-fabricated** evidence rows from the 2557/2572 saga, now gold-labeled `supports`. Two distinct problems: (a) *provenance* — a gold benchmark must not inherit snippets from rows whose provenance is `quarantined_fabricated`; even if the text happens to match the real paper (the 2557 reconcile confirmed the paper's abstract does affirm the correlation), the gold row's evidence must be re-sourced from the actual paper (2512.16290v1) with location, or the rows dropped. A measurement instrument with fabricated-batch inputs cannot certify anything. (b) *label substance* — for 26084 vs claim 2557 ("influenced by…"), our own reconcile packet concluded the paper is a **valid challenge to dominance that does not refute the influence wording** — that maps to `qualifies`, not `supports`. (For 26088 vs claim 2572's "correlates" wording, `supports` is textually defensible since the paper explicitly affirms the correlation before arguing halo causality.)

**2. Two labels look swapped relative to the audit lineage.**
- **26687** gold `refutes` — but the stance audit deliberately classified it `partial_or_ambiguous` ("a genuine qualification, not keyword noise"; mixed source: supportive threshold physics + limiting conclusion). Under B1-prime's own definitions, `qualifies` fits; forcing `refutes` takes one half of a mixed paper.
- **26691** gold `qualifies` — but the audit preserved it as a **true challenge** ("correlates weakly… a direct material narrowing. Challenge stance is CORRECT"), and B1-prime's `refutes` definition explicitly includes "materially weakens." These two rows appear to have traded labels relative to the adjudicated record. Lana's lane owns the final call; the audit quotes above are the evidence.

**3. Gold-vs-production divergence is real and must be documented, not discovered later.**
Row 25999 gold `qualifies` while our *executed* production stance is `supports`. The divergence is actually principled — the gold judges snippet-vs-claim-text under B1-prime's strict scope rules against a claim we already know is overbroad (the 2299 lesson), while production encoded a claim-level cleanup decision — but if it ships undocumented, the next audit finds gold contradicting the DB with no note saying which is authoritative for what. Add a reconciliation table to the gold summary: per divergent row, both labels and the one-line reason.

**4. False confidence in the headline number.**
0.533 vs 0.333 baseline is +0.2 at n=15 — roughly 8/15 vs 5/15, about one sigma. Directionally promising; statistically inconclusive. No threshold, ranking, or adoption decision may cite this run as evidence of reliability, and the packet should say so in one sentence.

**5. Shared-worldview circularity (name it, accept it).**
The label drafter, the prompt author, and the interpreter are the same lane, and the verifier's rules encode the same doctrine used to draft the labels — agreement is partly the doctrine agreeing with itself. Mitigated by: labels pending Quintet review, prompt seeing no labels, and Lana's independent adjudication. Acceptable for an internal safety-net instrument; not claimable as external validity.

**6. Step-8 unlock creep lives in the question wording.**
"Does the verifier clear a Step-8 safety-net threshold?" invites a future rule where a verifier score *clears a gate*. Doctrine: the verifier may **add** checks (a Step-9 audit assistant, a disagreement flagger); it may never **clear** anything. Gates are satisfied by artifacts and human review, tools only ever raise flags.

## Tripwires (block use of verifier or gold set)

1. Gold cited as "Quintet-reviewed" before Lana's label adjudication completes → BLOCK.
2. Any gold row carrying quarantined/fabricated-provenance snippets without re-sourced, located, verified text → BLOCK.
3. Verifier output entering any production `stance`/ledger/status/certainty field → BLOCK.
4. Any rule of the form "verifier ≥ X% → unlock/skip/clear a step" → BLOCK (Step 8 remains operator + Steps 0–7 artifacts).
5. Verifier labels *reducing* human review attention anywhere → BLOCK (attention-additive only).
6. Aggregated verifier scores rendered as consensus/quality/percentage claims → BLOCK.
7. Prompt/rule/model changes without re-running the full gold and re-recording metrics (pin script sha + model tag in every result) → BLOCK.

## Safe adoption language (paste-ready)

> **Gold set:** the 15-row Page57 contradiction-rich set is a valid **draft** built from project-owned sources with balanced classes (5/5/3/2). It becomes "Quintet-reviewed gold v1 (page57-scoped)" only after: Lana adjudicates the four contested labels (26084, 26687, 26691, and confirmation of 26088), the two quarantine-lineage snippets are re-sourced from the actual paper with location, and a gold-vs-production divergence table is attached. Until then its status is TORI_DRAFT.
> **Verifier:** the local scope/attribution verifier (qwen3.6 local, prompt-rule harness, not generic NLI) is **adopted as an experimental, attention-additive instrument only**: it may flag rows for extra review and may run inside Step-9 adversarial audits as a defect-suggester. Measured 0.533 vs 0.333 baseline at n=15 — directionally promising, statistically inconclusive. It has no stance authority, no gate authority, never writes to ledger or production fields, and does not affect Step 8, which remains locked behind Steps 0–7 gates and explicit operator approval.

## Master-brief gate answers (this lane)

1. Valid contradiction-rich held-out gold **draft** from owned sources — **yes**, with the quarantine-provenance exception (patch required). 2. Labels to patch — **26084 (→qualifies), 26687 (→qualifies or drop), 26691 (→refutes candidate), 26088 (re-source, confirm)**; document 25999 divergence. 3. Better direction than generic NLI — **yes, clearly**: task-shaped, rule-encoded, local, leakage-clean prompt. 4. Step-8 threshold cleared — **no**, and no such threshold should exist; the verifier adds checks, never clears gates. 5. Safe adoption language — above, verbatim.

## Safety ledger

Generic NLI runs 0 · model downloads 0 · DB 0 · SQL 0 · migrations 0 · deploy/restart 0 · git 0 · Step 8 prose 0 · secrets 0 · files written 1 (this report).

HWAO_B1_PRIME_DOCTRINE_DONE_20260703
