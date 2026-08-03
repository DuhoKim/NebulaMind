# Hwao/Fable Doctrine Report — Real-NLI B1 adversarial review

Task: HWAO/FABLE REAL-NLI B1 adversarial doctrine review · Status: COMPLETE — read-only except this report; no DB/migrations/deploy/git; no Step 8 prose.
Inputs: master brief, comparison packet + JSON, gold stance matrix (distribution computed directly), ledger context.

## Verdict: `PASS_WITH_PATCHES`

The **benchmark work passes** — 45/45 rows on real models, per-model validation artifacts, `auto_stance_authority_threshold_met: false` and `step8_unlocked: false` everywhere, honest weak numbers reported rather than buried. This is exactly the "measured gold delta" evaluation my Step 7a review demanded. What needs patching is the **interpretation language**: "NLI tool adopted only as assistive warning/triage" still overclaims, because of a decisive number the packet omits.

## The attack: the packet's conclusion, versus the missing baseline

**The gold distribution is supports 32 / qualifies 10 / contradicts 3 (n=45). The majority-class constant classifier ("always say supports") therefore scores 0.711 accuracy. The best NLI model scores 0.378 — barely half the trivial baseline. All three models are substantially worse than doing nothing intelligent at all.**

Consequences the interpretation must absorb:

1. **"Triage" is not a safe word for a sub-baseline classifier.** Triage means sorting review effort; anything sorted *down* by a model this weak receives less attention for no valid reason. The headline metrics flatter the models: ynie's `qualifier_recall 1.0` is an artifact of flooding rows into the neutral→qualifies bucket (that is *why* accuracy is 0.378), and `support_precision 0.875` clears the 0.711 base rate by only ~16 points.
2. **Contradiction performance is not weak — it is unmeasured.** There are 3 contradiction rows in gold. Two models scored 0/3, one scored 1/3. No recall estimate from n=3 means anything; what we can say is the two better models showed **total contradiction blindness on the only rows that exist**, and contradiction is the single most safety-critical class in this system (the entire false-challenges campaign was about it).
3. **The 3→5 class mapping is doing silent work.** NLI `neutral` is ignorance; ledger `qualifies` is *active narrowing*. Conflating them manufactures the 0.9–1.0 qualifier recalls. Also, gold contains only 3 of the 5 ledger classes, so this was really a 3-class task scored against a 5-class vocabulary.

## How NLI models can falsely imply consensus, dominance, universality, or source-level proof

- **False consensus by aggregation:** averaging entailment scores across spans/papers into "N% supported" — the Consensus-meter failure, automated. Especially toxic over a supports-heavy corpus (71% base rate guarantees impressive-looking percentages).
- **False consensus by contradiction blindness:** a status map fed by models with measured 0/3 contradiction recall would structurally contain *no counterevidence* — consensus manufactured by omission, the exact defect class the stance audit spent a day repairing.
- **False universality by scope-blindness:** NLI happily "entails" a universal sentence from a 46%-subset span; it has no quantifier or modality discipline. This is claim 2299's original sin with a model attached.
- **False source-level proof by zone-blindness:** entailment is sentence-level textual inference. A background/related-work span entails a claim just as strongly as a findings span — NLI would launder quote-mined zones into "the paper supports this." Sentence entailment ≠ paper finding.
- **False dominance:** absence of model-detected contradiction read as "unchallenged" → dominance language.

## Tripwires that must block Step 8 (or any artifact) if lanes overinterpret

1. **Field contamination:** any NLI score/label appearing in `stance`, `certainty_dimensions`, `certainty_level`, status-map computation, or wording-contract inputs → BLOCK.
2. **Attention subtraction:** any workflow where NLI output *reduces* human review on any row → BLOCK. Model outputs may only ADD attention (flags), never remove it. A sub-baseline classifier has no sorting authority.
3. **Aggregation language:** any artifact containing NLI-derived percentages, "models agree," or model-consensus phrasing → false-consensus tripwire → BLOCK.
4. **Contradiction delegation:** any process relying on NLI to find/screen contradictions or counterevidence → BLOCK (measured blindness; n=3 unmeasurable). Contradiction discovery stays human + citation-stance reading.
5. **Authority flip:** changing `auto_stance_authority_threshold_met` to true — or any equivalent policy — without a NEW held-out, contradiction-rich gold set and full Quintet re-review → BLOCK.
6. **Step 8 leakage:** any artifact stating or implying B1 unlocks Step 8 → BLOCK. B1 satisfies the *B1 execution gate only*; Step 8 remains locked behind Steps 0–7 gates plus explicit operator approval, exactly as the master brief expects (Q4 answer: **no, not automatically — correct**).

## Exact safe adoption language (paste-ready)

> **Real-NLI B1 outcome:** The B1 benchmark harness (script + 45-row human gold + per-model validation) is **adopted as NebulaMind's standing tool-evaluation instrument** for stance tools. **None of the three tested models is adopted for pipeline use** — best accuracy 0.378 versus a 0.711 majority-class baseline, with contradiction recall unmeasurable (n=3; 0/3 for the two stronger models). One narrow experimental use is permitted: **attention-additive disagreement flagging** — where a model label disagrees with a human stance, the row may be *flagged for extra review*; flags never reduce review, never enter ledger/status/certainty fields, never aggregate into percentages, and always carry in-band tool provenance. `auto_stance_authority` remains false; revisiting requires a new contradiction-rich held-out gold and Quintet re-review. B1 does not unlock Step 8.

## Patches (small, exact)

1. **Add the majority-baseline line to the comparison packet** ("gold: 32/10/3; constant-supports baseline accuracy 0.711") — the single number that makes every other number interpretable. Its absence is how false confidence would start.
2. **Replace "adopted only as assistive warning/triage"** in the Tori interpretation with the safe adoption language above (harness adopted; models not adopted; additive-only disagreement flagging).
3. **Add the n=3 caveat** wherever contradict_recall is reported ("unmeasurable at n=3").
4. **Note the mapping defect** (NLI neutral ≠ ledger qualifies) as a known artifact inflating qualifier recall.
5. **Build the contradiction-rich gold next** — NebulaMind already owns the raw material: the page-57 stance-audit corpus (confirmed false challenges, true challenges, quarantined refutes) can seed a held-out gold with ≥20 real contradiction rows. That, not more models, is the highest-value follow-up to B1.

## Master-brief gate answers (this lane's view)

1. Executed reproducibly on all 45 rows — yes per artifacts (Goru/Kun own the deep check). 2. Script/mapping sane as an *evaluation artifact* — yes, with the mapping defect documented (patch 4). 3. Results justify — **less than assistive triage**: harness adoption + additive-only experimental flagging; no model authority of any kind. 4. Step 8 unlock — **no, not automatically**; operator approval and Steps 0–7 gates stand.

## Safety ledger

Read-only review · report file only · DB 0 · SQL 0 · migrations 0 · deploy/restart 0 · git 0 · Step 8 prose 0 · secrets 0.

HWAO_REAL_NLI_B1_DOCTRINE_DONE_20260703
