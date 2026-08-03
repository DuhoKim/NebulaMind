# Hwao/Fable Doctrine Report — Step 9B claim/evidence continuity packet

Task: HWAO STEP 9B adversarial gate review · Status: COMPLETE — read-only except this report; no patch applied; no DB/API mutations; no git.
Verified directly: all six claim-decision rows (full fields), GO/NO-GO checklist (raw rows), validation JSON, source→product match summary, packet phrase scan (the only pattern hit is the packet's own "## No execute phrase" guard heading).

## Verdict: `PASS_WITH_PATCHES` — mark PACKET_ONLY_NOT_EXECUTED after three small patches; the dispositions are doctrinally sound and the insert-heavy block is correct.

## Q1/Q2 — The six claim decisions: mechanically complete and scientifically sane, including the counterintuitive one

Every row carries current text/trust/evidence IDs, a decision, a future claim action, the operator choice, target Step 9 sentences, and its own apply gate. On the substance:

- **2915, 2917 carry-forward: correct.** Both have faithful host sentences (P9S003/P9S013; P9S009), candidate rebind sentences that keep mechanism separate from prevalence, existing evidence stays attached, no inserts needed. The drift-check condition on both is right.
- **2913 do-not-carry: correct** — "rapid at z~2" has no supporting sentence in the new prose (the exact faithfulness gap I flagged at Step 9), and the packet properly offers retire-or-rewrite via claim workflow *or* a future rapid-quenching packet rather than hard-deleting a possibly-true but out-of-slice claim.
- **2921 move-not-retire: correct** — it is a central-structure claim, not an AGN-feedback claim; parking it for a central-structure section decision avoids both silent loss and section-scope stretch.
- **2924 replace-flat-claim: correct and important** — the flat "heats the gas reservoirs" chip at `consensus` cannot ride sentences capped at `in_model_only`; nuance-or-retire via claim workflow with its four evidence rows quarantined from reuse-without-audit is exactly right.
- **2929 supersede-with-split: the counterintuitive call, and it is right.** My first instinct at Step 9 was to carry the page's best-evidenced chip (40 rows) forward — the 9B rationale answers it: 2929 is a **compound claim** (jets + outflows + turbulence + heating + starvation + positive-feedback nuance in one chip), and its heating conjunct is model-bounded in this corpus. Carrying the compound chip would re-import the 2924 problem inside 2929. This is the ledger contract's atomicity rule correctly applied to a live production chip; the local-positive-feedback preservation option is properly noted.

## Q3 — Evidence mapping honesty: confirmed, and 1/26 MUST block apply

Only `2015Natur.521..192P` resolves to an existing product evidence ID (6651); 25/26 Step 9 sources are unresolved **against public endpoints**; the insert-heavy gate is TRIGGERED at 96.2% — far past the one-third rule, properly loud, correctly blocking. I confirm the block. Two sharpenings (patches below): the 25/26 denominator is a *public-surface* measurement — the honest next step named in the packet's own NO-GO note (a **read-only DB-level match** over the full evidence table) should run before the insert decision is put to the operator, since corpus papers may exist as evidence attached to other claims; and the match method for 6651 must be recorded and verified by exact ID (bibcode/arXiv roundtrip), per the standing no-title-match tripwire, before it counts as resolved.

## Q4 — No evidence-ID laundering: confirmed

No invented product IDs anywhere; every claim row's `evidence_id_decision` explicitly refuses reuse-without-audit where reuse is tempting (2924's four rows; 2929's forty); the one resolved ID is carried as a single honest match, not extrapolated.

## Q5 — No hidden apply phrasing; hard stops at zero: confirmed

The only phrase-pattern hit in the packet is its own "## No execute phrase" section. Validation: `api_mutations: 0`, `db_writes: 0`, `exact_diff_apply: 0`, apply gate LOCKED, product gate LOCKED. Five NO-GOs stand, including "Apply permission present: NO-GO — current direction explicitly says do not approve apply yet." No Step 10 creep found; the claim-workflow NO-GO correctly keeps even the *dispositions* pending operator approval, so there is no silent chip loss anywhere in this packet — the Step 9 gap is now fully decided-or-gated.

## Q6 — The three patches, then PACKET_ONLY_NOT_EXECUTED

1. **Link the maintenance-heating corpus gap card in the 2924 row.** Retire-or-nuance is right, but the queued observational-heating gap-fill card is the honest path *back* to a stronger heating claim later; referencing it prevents the retirement from orphaning that route (and keeps the `consensus`-label-vs-corpus tension attached to its remedy).
2. **Record and verify the 6651 match method; scope the denominator.** State how `2015Natur.521..192P → 6651` was matched and verify by exact ID; annotate the 25/26 figure as public-surface-only; name the read-only DB-level match as the required next resolution step **before** the insert-class decision goes to the operator.
3. **Add an evidence re-mapping audit to 2929's split plan.** Superseding a 40-row chip must include a plan for which split claim inherits which evidence subset (audited, not bulk-copied) — otherwise supersede-day orphans forty rows or silently bulk-attaches them, both failure modes this campaign exists to prevent.

With those three lines added, Step 9B is complete as `PACKET_ONLY_NOT_EXECUTED`. The apply gate remains NO-GO on: evidence IDs (insert-heavy), DB rollback backup, operator claim-workflow approval, and apply permission — all correctly held.

## Safety ledger

Patch applied 0 · product/wiki/DB/API mutations 0 · POST/PUT/PATCH/DELETE 0 · git 0 · deploy/restart 0 · generic NLI 0 · model downloads 0 · secrets 0 · files written 1 (this report).

HWAO_STEP9B_DOCTRINE_DONE_20260703T1329Z
