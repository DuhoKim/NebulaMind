# DECISION SUMMARY — the comparison, in one page (2026-09-07 19:26 KST)
Final snapshot **passes**: A1 `6b9ecc79…`, run path `1c4f96fb…`, decision sheet `768598ef…`, each with an access-proved **SNAPSHOT-SOUND** from agy/Gemini, which authored none of it. **No remaining result-invalidating defect.** Nothing is adopted.

**The question.** How often does the machine's chirality call agree with the human GZ1 call on images the machine has never seen — reported with an uncertainty interval against a pre-stated bar.

**Population and exclusions.** The pinned guarded pool, restricted to renderable identities with r-band coverage: **11,837 eligible**. Removed: the **2,644** already-seen dry-run identities and the **2,000** failed set (disjoint; 90 of them legitimately fall outside the eligible population and are recorded, not hidden). **Post-exclusion population 7,283.**

**Sampling and splits (unchanged).** One reproducible selection from a seed: order by `SHA256(seed ‖ "||" ‖ objid)`, ties by objid; draw **exactly 400 tuning / 200 holdout / 2,000 validation**, disjoint by construction. A draw that cannot be filled STOPS the run rather than shrinking. Scored-count floors **380 / 190 / 1,900** are applied later, after the estimator runs — they are not permission for a smaller draw.

**How separation is protected.** Tuning, holdout and validation are disjoint at selection. The estimator and its configuration are frozen by digest at the **winner freeze**, which happens after tuning and before the holdout opens — a winner cannot exist at the earlier input freeze. **The holdout opens once.** Every draw, abort, re-draw and holdout opening is anchored by publication, so an abandoned attempt leaves a visible gap; **one further validation attempt** is permitted, and there is no secondary.

**The statistic.** Orientation-agnostic agreement, `max(k, m−k)`, allowing one overall sign reversal. Tuning over a fixed 400 and holdout over a fixed 200 with unscored counting as **misses**; validation over **m**, the scored count, with refusals excluded and reported separately as `r` — that asymmetry is inherited from the signed rule and its pinned gate, not introduced here. Holdout passes iff the **Wilson 95% lower bound > 0.70** after the floor check; validation likewise, n = 2,000, m ≥ 1,900. A failure closes the option; it is not retried into a pass.

**The seed.** A **future** drand round, named only after the inputs are fixed and published to a third party, at least ten minutes after that anchor, BLS-verified against the pinned chain with ≥2 hosts agreeing as an additional check. The V15 round 6440756 is already observed and **cannot** seed this run.

**What Duho's ordinary approval would authorize.** Adoption of this amended procedure — and nothing else. It would NOT start a run, name a round, draw a sample, open the holdout or touch protected data; those follow adoption as separate, gated steps.

**Material remaining limitations, stated plainly.** (1) The runtime byte binding covers the **on-disk** copy; a custom loader or a post-load in-memory change could evade it. (2) The first receipt produced under the OPS label is caught only by OPS's own retained copy. (3) The offline baseline still loads counter-cases 1, 2 and A — a disclosed limit of that mode, unchanged since V27. (4) Five later-stage inventories cannot exist until their stages run.
Supporting records (version history, cache inventories, test counts, the eleven review passes) stay in the lane files; this page is the decision.
