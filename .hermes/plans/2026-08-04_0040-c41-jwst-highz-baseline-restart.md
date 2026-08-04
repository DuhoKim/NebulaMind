# C41 restart plan — the Baseline primitive aimed at the #1 frontier

> **Status: RED-TEAMED, STEP 0 GATED 2026-08-03 21:53 KST** ("APPROVE C41 STEP 0 — freeze the
> question"). Drafted by Hwao on Duho's word ("draft the C41 restart plan overnight");
> adversarially reviewed by Kun (kimi-k3), 12 findings (`KUN_PLAN_REVIEW_C41_20260804.md`), all
> folded or answered — see **§Red-team disposition** at the end.
> **Dating correction:** this file's name and the review's header say 2026-08-04 — that was
> Hwao's clock-drift error; drafting and review actually ran 2026-08-03 ~20:30–21:50 KST. Real
> timestamps from Step 0 onward.

**Crew map (inline, per Kun F2 — the authoritative correction text lives in the RETIRED banner of
`.hermes/agents/kun-codex-lane-protocol.md`):** Hwao (Claude/Fable) coordinates. Tori = Hermes
gpt-5.6-sol seat. Yui = Hermes seat on the Mac Studio (pane %25 — same host as the repo, so
host-local tools and `backend/.env` tokens are reachable from her lane). Goru = Antigravity/agy
Gemini. Kun = Kimi K3 via Nous (`hermes chat --provider nous -m moonshotai/kimi-k3`). Lana =
Claude Code no-overclaim lane. Codex engine: retired/unassigned 2026-08-03 — no Codex lanes.
All subscription-only; no API-key/PAYG.

## Why this, why now

- All 9 autopilot papers were rejected for the same reason: z~0 low-hanging fruit, circular
  results, no wiki/lit-grounded motivation. Duho's bar: **frontier studies** — sim-vs-physics,
  JWST high-z — with DR in the loop as reference ([[feedback_autopilot_publishable_bar]],
  [[feedback_frontier_not_lowhanging]]).
- **C41 — "JWST high-redshift galaxy evolution and emission" — is #1 under both rankings on the
  box** (Kun F4, verified): #1 by the citation-activity score shown on the Lab (`score` 0.957) AND
  #1 by the controversy×tractability composite (`scoreV1` 0.374; next core cluster is C40 at
  0.143), before and after the 2026-08-03 rerank, and also top within the hand-reviewed core scope
  (`frontierScope.ts`). Stats: 1,317 papers (+21 July deltas), median year 2021, recentFrac 0.426,
  citeMedian 46. `nDebates` 146 = `round(strict_tension × size)` — a title/abstract disagreement-
  lexicon hit count (Kun F5), NOT a count of real controversies; condensing it into real debate
  axes is precisely Step 6's job.
- The Baseline pipeline (papers → claim/status ledger → status/debate map → prose) has been stalled
  at "status/debate map next" since 2026-07-03 (Kun audit R7). The claim-ledger contract v1 exists
  and was validated on the 26-paper AGN pilot. **This plan advances the real stage on a real
  frontier** — R7 closes as a by-product of doing the mission, not as paperwork.
- C41's newest members (July 2026 deltas) define the live battleground: feedback-free efficiency
  ("A Massive Galaxy at the Edge of Feedback-Free Efficiency"), non-thermal/bursty SF models
  (Azahar), variable-IMF simulations, blue/red "monsters" and the bright-end UV LF, JWST/NIRSpec
  ionizing budgets for reionization, Little Red Dots, gas-phase metallicities down to
  M*≈10^5.7 M⊙. The sim-vs-observation tension Duho named is the cluster's center of mass.

## Two tracks, deliberately ordered

**Track A — Knowledge (the Baseline primitive on C41).** Run roadmap Steps 0–6 on a C41 working
corpus to produce the **status/debate map for cosmic-dawn galaxy formation**. This is the flagship
pipeline's "next" stage executed on a frontier that matters.

**Track B — Study (one non-circular measurement).** A tractable sim-vs-data confrontation **chosen
FROM the Track-A debate map, not before it** — the map picks the study, so study selection cannot
be motivated reasoning. Candidate shapes are pre-scoped below so the morning review can veto any,
but the final pick waits for the map + Duho's gate.

## Track A — stages, lanes, gates

Stage vocabulary and invariants are the canonical roadmap's
(`.hermes/plans/2026-07-01_205807-paper-prose-distillation-roadmap.md`); the claim-ledger contract
v1 artifacts are reused as-is. Proportionality rule applies throughout.

| Step | What | Lane (engine) | Output artifact |
|---|---|---|---|
| 0 | Freeze the question: "What do we currently know, dispute, and not know about early (z≳6) galaxy formation efficiency, chemical enrichment, and ionizing output?" Scope: C41 subset. | Hwao drafts; **Duho freezes** | frozen-question doc |
| 1 | Corpus protocol BEFORE collecting: selection rules for a working set from C41's 1,317+21 (recency-weighted, review-aware, contested-measurement-first via the dispersion lexicon). Anti-cherry-picking is MECHANICAL (Kun F7): (a) the selection rule is an executable filter over the C41 member list, run before anyone reads titles; (b) the EXCLUDED list is published with reasons-per-class, not just the included list; (c) Kun runs a decoy test — injected papers designed to tempt motivated exclusion must survive or be excluded by a named rule. Ceiling 180 papers; the shrink ladder (below) governs reality. | Tori (Hermes) authors; Kun refutes vs (a)–(c) | corpus protocol + frozen selection+exclusion lists w/ shas |
| 2 | Full text + source-strength labels (`nm_fulltext_layer`, ADS/arXiv; cache under the engine dir, not git). **Preconditions (Kun F1/F10): commit `tools/nm_fulltext_layer.py` via the proven PR path first** (it is untracked and hardcodes host-local `_ROOT` + reads `backend/.env` for the ADS token — which is fine because Yui's Hermes seat runs on this same Studio host; if her seat is unavailable, Tori executes on-host as fallback). | Yui (Hermes, on-host); fallback Tori | fulltext manifest + strength labels |
| 3 | Candidate span extraction w/ location + rhetorical zone | Goru (**Antigravity/Gemini**) mechanical; Tori spot-verifies 10% blind | span table |
| 4 | Claim/status ledger build (contract v1 schema, machine-validated) | Goru builds; Lana (Claude) no-overclaim pass | C41 ledger JSONL + validation receipt |
| 5 | Claim-source stance verification — adversarial, verifier≠extractor | **Kun (Kimi K3 via Nous)** | stance matrix + refutation log |
| 6 | **Status/debate map**: cluster the ledger into named debates, each with sides, best evidence, measurement dispersions, and "what would settle it". Deliverable MUST include a **condensation report** (Kun F5): 146 lexicon hits → K merged axes, with the merge rule receipted — K is an output, not a target. | Hwao + Lana synthesize; Kun red-teams; Tori receipts | **C41 status/debate map v1 + condensation report** ← the stage the board has awaited since Jul 3 |

DR usage (Track A): at most 2 Deep Research runs, spaced, as **filed reference dossiers** feeding
Step 6 context only — never writing any artifact directly
([[feedback_dr_as_reference_not_lane_replacement]], [[reference_dr_account_throttle_gentle_pace]]).

Gate phrases (Duho, verbatim, one per stage): `APPROVE C41 STEP <n> — <one-line scope>`. Steps 0–1
may be approved together in the morning; 2–6 run gated but can be batched per day. Track-B gates
are defined NOW so no gate is invented mid-flight (Kun F8a): `APPROVE C41 TRACK-B SHAPE <n> —
<name>` (the pick, after the Step-6 map review) and `APPROVE C41 TRACK-B MEASUREMENT START`
(execution). All findings-only until Step 6 output exists. Writes carve-out, precisely (Kun F8b):
**no product/DB/wiki/live/git-surface writes inside the stages**; lane-dir artifacts
(`.hermes/handoffs/c41-baseline-restart-<ts>/`) and engine-dir caches (fulltext_cache) are the
expected working writes; git capture only via the proven PR path at stage boundaries Duho approves.

## Track B — candidate study shapes (pre-scoped; final pick gated on the Step-6 map)

1. **Bright-end UV luminosity function at z≈8–14 vs. model predictions** *(recommended primary)* —
   Assemble number densities from public JWST photometric catalogs (JADES / CEERS / COSMOS-Web;
   exact VizieR table IDs verified at Step 1 — none are invented here) via `nm_external_data`
   (VizieR TAP with retry/cache; built precisely to escape the z~0 envelope). Confront the
   ledger'd, stance-verified predictions of FFB, non-thermal (Azahar), and variable-IMF models —
   predictions enter as **ledger claims with citations**, not re-simulated numbers, so the
   comparison is between published predictions and independent photometric data.
   *Non-circularity, two layers* (second per Kun F6): (i) data side never touches the models;
   model side never fits our data. (ii) **Shared-pipeline circularity**: the public catalogs are
   the same ones model papers calibrate/validate on — so the Step-1 protocol must declare, per
   catalog, which reduction / photo-z (EAZY/BEAGLE-class) / completeness chain it inherits, prefer
   model predictions NOT calibrated on those same chains, and record any residual overlap as an
   explicit scope limit in the ledger rather than silently absorbing it.
   *Tractability:* catalog-level; no imaging reprocessing.
2. **High-z mass–metallicity relation vs. enrichment models** — extends the newest C41 work down
   to M*≈10^5.7 M⊙. **Known trap** ([[reference_metallicity_calibration_scale]]): O/H calibration
   scales do not cancel across samples (Te vs strong-line offsets ≈0.24 dex); contract: single
   Te-anchored scale or explicit per-sample conversion, declared in the corpus protocol before any
   number is compared.
3. **Ionizing-budget tension (f_esc, ξ_ion) for reionization** — ties into the v2 dispersion
   machinery that already promotes f_esc as contested; measurement = dispersion-aware synthesis of
   NIRSpec-based budgets vs. "driven by the few" claims.

Each shape ends at the same bar: wiki/lit-grounded motivation (from the Step-6 map), a
**non-circular result**, a defensible conclusion, merit-scored by the 5-member panel before any
draft is called a paper. Human directions during drafting are logged verbatim via
`tools/nm_paper_history.py` ([[feedback_auto_record_human_paper_history]]).

## Explicit non-goals

- No wiki-page deliverables (wiki is deprecated; the Lab is the surface — any Lab-page rendering of
  the debate map is a SEPARATE, gated, post-Step-6 proposal).
- No z~0 SDSS relations as standalone results (anchors only, if needed for calibration context).
- No video/explainer work inside this plan. No Codex lanes (engine retired/unassigned). No new
  cron/launchd. No /credits. Subscription-only engines per the corrected crew map.

## Schedule sketch (KST; assumes morning gates land ~10:00)

- **Day 1 (Aug 4):** Step 0 freeze + Step 1 protocol authored and refuted; selection list frozen
  with shas. (Independent: 14:00 frontier-daily unattended run — its receipt closes audit R4;
  Tori verifies.)
- **Day 2:** Steps 2–3 (fulltext, spans). — **Schedule honesty (Kun F3): the 180-paper ceiling is
  a 5–7× scale-up over the only completed pilot (26 AGN papers, 16 ledger entries, 45 spans,
  human-driven over ~2.5 weeks). Goru's mechanical span throughput has NO prior data point.**
- **Day 3:** Steps 4–5 (ledger, stances). **Pre-committed shrink ladder (not discovered
  mid-flight): if fewer than 60 papers are fully ledgered by end of Day 3, cut scope to the top-60
  by contested-measurement rank and proceed; if fewer than 30, cut to top-30. The map ships on
  whatever cleared honestly; the shortfall and cut are receipted. Scope shrinks before quality
  does — by rule, not by improvisation.**
- **Day 4:** Step 6 map synthesis + condensation report + Kun red-team → **debate-map review with
  Duho; Track-B pick via its gate phrase.**
- **Week 2:** Track-B measurement (behind `APPROVE C41 TRACK-B MEASUREMENT START`), DR dossier #2
  if needed, merit-panel scoring, paper decision.

## Note on `[[...]]` references (Kun F11)

The double-bracket names in this plan are **Hwao's persistent memory-note titles, not repo files**
— Kun correctly found they resolve nowhere in the repo. Their substance, inlined: *autopilot
publishable bar* = all 9 prior autopilot papers rejected; publishable needs grounded motivation, a
non-circular result, a defensible conclusion. *Frontier not low-hanging* = attack top-ranked
frontiers; z~0 relations are anchors, not papers. *DR as reference* = Deep Research output is a
filed dossier feeding context; it never writes artifacts. *DR throttle* = few runs, spaced; back
off on first soft throttle. *Metallicity calibration scale* = O/H scales don't cancel across
samples (Te vs strong-line ≈0.24 dex); declare one scale before comparing. *Auto-record human
paper history* = Duho's verbatim words go to `tools/nm_paper_history.py` when they change a draft.

## Risks and honesty notes

- **Catalog availability** is asserted generically (JADES/CEERS/COSMOS-Web have public releases);
  the exact tables, columns, and completeness limits are a Step-1 verification task — if the
  bright-end LF cannot be built from public catalogs at honest completeness, shape #1 falls back
  to #3, and that fallback decision is itself receipted.
- **146 nDebates** provenance and the Step-6 condensation-report requirement are covered above.
- **Throughput** risk is governed by the pre-committed shrink ladder in the schedule (Kun F3).

## Red-team disposition (Kun review `KUN_PLAN_REVIEW_C41_20260804.md`, 12 findings)

| # | Sev | Disposition |
|---|---|---|
| F1 | HIGH | **Folded** — Step 2 now states Yui's Hermes seat runs on the Studio host (repo + `.env` local), with Tori as on-host fallback. Kun's roster source (`memory/platoon-roster.md` v3, Jun 11) predates Yui's seat; his own uncertainty note anticipated this. |
| F2 | HIGH | **Folded** — crew map inlined in the header; authoritative correction text cited (`kun-codex-lane-protocol.md` RETIRED banner). |
| F3 | HIGH | **Folded** — 180 relabeled as ceiling; pilot-scale honesty stated; numeric shrink ladder (60/30) pre-committed in the schedule. |
| F4 | MED | **Folded** — ranking sentence replaced with Kun's both-metrics formulation (verified: #1 by score 0.957 AND scoreV1 0.374). |
| F5 | MED | **Folded** — nDebates formula stated; Step 6 requires a condensation report with receipted merge rule; the "8–15" prediction removed. |
| F6 | MED | **Folded** — shape #1 gains the shared-pipeline circularity layer (per-catalog chain declaration, prediction-source preference, ledger'd scope limits). |
| F7 | MED | **Folded** — anti-cherry-picking is now three mechanical checks incl. Kun's decoy test, refutation criteria named. |
| F8 | L-M | **Folded** — Track-B gate phrases defined now; writes carve-out made precise. |
| F9 | LOW | Verified-true inventory — no change needed; morning review may rely on it. |
| F10 | LOW | **Folded** — committing `nm_fulltext_layer.py` is a Step-2 precondition (rides the morning docs PR with the protocol-banner edit). |
| F11 | LOW | **Folded** — `[[...]]` names disclosed as Hwao memory-note titles; substance inlined in its own section. |
| F12 | LOW | Verified-true (fesc in dispersion machinery) — no change needed. |

Answered-not-folded: none. Every HIGH/MED finding produced a text change above.
