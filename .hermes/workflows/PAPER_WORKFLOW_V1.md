# NebulaMind paper workflow v1 — subscription-first, Kimi-as-auditor, YouTube-reported

Designed 2026-08-05 on Duho's brief: *"leveraging subscription models in max and use Kimi model
oversee from time to time. and report the results in Youtube video."* Grounded in measured facts
from the 2026-08-05 session, not in guesses about what each seat can do.

## The economics that set the shape

| seat | engine | billing | measured load today | role this implies |
|------|--------|---------|---------------------|-------------------|
| Hwao | Claude (Fable) | subscription | 4% of 5h, 21% weekly | coordinator, script author, executor |
| Lana | Claude CLI | subscription | same pool | author: prose, plans, prediction entries |
| Tori | Hermes gpt-5.6-sol | subscription | context-gauge only | receipts, custody, consolidated verification |
| Yui | Hermes (Studio host) | subscription | idle | second receipts / video lane |
| Goru | Antigravity, Gemini 3.1 Pro | subscription | **0.9% weekly, 6.2% 5h** | the most under-used seat: bulk audits, inventories |
| Codex | ChatGPT/Codex | subscription | 14% weekly | unassigned seat; available for bulk work |
| **Kun / Miru** | **Kimi K3 (Moonshot key)** | **$3/M in, $15/M out** | **$14.25 tonight over 10 reviews ≈ $1.42 each; $80.41 left ≈ 56 reviews** | **scarce auditor — spend only where being wrong is expensive** |

The subscriptions are flat: using them harder costs nothing. Kimi is the only metered seat, and
tonight proved it is worth its price *at the right moments* — so the design maximises subscription
work per Kimi call rather than minimising Kimi calls outright.

## Where Kimi actually earned its cost today (the evidence this design encodes)
- caught a **fail-open status path** that would have reported dropped cells as clean;
- caught `phys.abund` admitting **stellar iron** — StarHorse's ~10⁸ rows would have swamped an
  MZR census aggregate;
- caught the mirror-bias clause that was **a licence to publish a known systematic under a
  disclaimer**;
- caught a **tie-drop** that silently discarded 29,053 objects;
- curated a **recall set our own enumerator can fail**, correcting his own earlier record;
- caught an **unpinned appendix reference** that would have let the recall set drift.

Every one of those is a *pre-execution or pre-publication* defect. None would have been caught by
running the pipeline harder. That is the rule below.

## The pipeline — one paper, nine stages

| # | stage | seat | Kimi? |
|---|-------|------|-------|
| 0 | **Data survey** — what the archive holds for this question (`tools/nm_data_survey.py`) | Hwao | no |
| 1 | **Frontier/topic framing** — why this question, what is contested | Lana | no |
| 2 | **Contract freeze** — frame, cuts, gates, statistic, honest outcomes; sha + chmod 444 | Hwao drafts | **KIMI GATE 1** |
| 3 | **Enumeration + eligibility** — two-channel (UCD + case-complete name), per-table verdicts with source receipts | Goru (bulk) + Hwao | no |
| 4 | **Reviewed script** — the only thing allowed to produce numbers | Hwao writes | **KIMI GATE 2** (pre-execution) |
| 5 | **Execute + funnel** — counts, terminal states, no statistic yet | Hwao | no |
| 6 | **Receipts** — totals re-added from raw artifacts, custody, hashes | Tori (+ Yui) | no |
| 7 | **Draft** — prose from receipted artifacts only, provenance block | Lana | no |
| 8 | **Referee** — overclaim hunt, claim↔artifact binding, established/overstated/understated | — | **KIMI GATE 3** |
| 9 | **Video + landing** — see below | Yui/Goru + Hwao | no |

**Three Kimi calls per paper** (contract, script, referee) ≈ **$4.30 per paper** at tonight's rate,
so the current balance funds roughly **18 papers**. Escalation beyond three is allowed but must be
named: a reviewer conflict, a fabrication suspicion, or a result that would be published.

**Everything else runs on flat-rate seats**, and the biggest lever is Goru at 0.9% weekly — bulk
inventories, eligibility sweeps, and quote-checkable audits belong there, verified mechanically
(`_tmp_microdelta/verify_quotes.py` pattern: every claim carries a verbatim quote, a script checks
each against the file, and the verification rate is reported unedited).

## The video stage (stage 9)
Existing tooling, not new: `HermesOps/scripts/{assemble_video,generate_long_video,upload_to_youtube}.py`,
`PAPER_VIDEOS` on the Lab board, Flow/Veo for footage, Nano Banana Pro for legible on-screen text.

Rules carried from what Duho has already corrected:
1. **Informative, not cosmic** — the video must convey the goal and the method with on-screen text
   and figures; footage is a dim backdrop, never the content.
2. **The paper's honesty survives into the video.** If the paper reports a bound, the video says
   bound. If a null, the video says null. A video may never claim more than its paper.
3. **Unlisted by default.** Public only on Duho's explicit per-video word.
4. **Script from the paper, not from memory** — the narration is generated from the receipted
   artifacts and the referee log, so what is said traces to what was measured.
5. A video is only made for a study that **landed** (or for an honest null that landed) — never
   for a draft.

## Gates that stay human
Lab landing, publication, going public on YouTube, opening a new fetch channel, and any new engine
seat. Those are Duho's, as they are now.

## What this replaces
The current ad-hoc pattern where a lane invents its own review order and Kimi gets called whenever
something feels risky. Under v1 the three Kimi moments are fixed and everything else is scheduled
onto seats that cost nothing to run harder.
