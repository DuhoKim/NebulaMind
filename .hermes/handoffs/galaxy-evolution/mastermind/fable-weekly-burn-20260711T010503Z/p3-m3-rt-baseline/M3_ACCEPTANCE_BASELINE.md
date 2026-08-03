FABLE_BURN_P3_ACCEPTANCE_BASELINE_20260711T010503Z

# M3 sidecar acceptance baseline — REQ_M3_RT_20260711T091128Z

Purpose: pre-agreed, fail-closed acceptance baseline for the **pending** supervised Gemini Web
sidecar run over the Method 3 research-topic cards. A future adjudicator scores the sidecar
answer card-by-card against this file without re-deriving anything. This packet **prepares** for
the run; it does not perform, request, or schedule it (run gated separately under
`DUHO_GEMINI_WEB_WIKI_RESEARCH_ARTIFACT_SCOPE_20260711T004710Z`).

Written by: Fable lane C, burn packet P3 (`HWAO_FABLE_BURN_P3_BRIEF_20260711T010503Z`), 2026-07-11.
All citations below are to local files only. Snapshots + sha256 of every source: see
`sources-snapshot/` and `P3_RECEIPT.md` in this directory.

Abbreviations used for citations (full paths + hashes in P3_RECEIPT.md):
- **REQ** — `RT_GEMINI_WEB_REQUEST_M3_20260711T091128Z.md` (the M3 sidecar request)
- **EB** — `evidence-basis-20260708T014205Z.md` (local evidence basis; anchors `#s1`–`#s9`)
- **SC** — six-card prospectus `research-topics-from-wiki-20260708T090359Z.md`, version
  `AUTOPILOT_RESEARCH_TOPICS_JOURNAL_EVIDENCE_LINK_PASS_20260708T112408Z` (snapshot
  `sources-snapshot/research-topics-from-wiki-20260708T090359Z.SIXCARD-prospectus.md`)
- **CUR** — current 3-proposal artifact at the paths named in REQ (snapshot
  `sources-snapshot/research-topics-from-wiki-20260708T090359Z.CURRENT-3proposal.md`)
- **CY7** — `JOURNAL_CYCLE7_GEMINI_WEB_20260710T232711Z_INTEGRATION.md` (cycle-7 rejection lesson)
- **VER** — `HWAO_GEMINI_WEB_VERDICT_20260711T000400Z.md` (Hwao wording/acceptance contract)

---

## 0. Card-set resolution (read first)

REQ names "All 6 extracted research topic cards" (REQ L11–12) but its "Current RT artifact
paths" (REQ L7–9) point to an artifact that now contains **3 consolidated proposals** (CUR L11:
"3 proposal-style research programmes"; consolidation stated at CUR L3). The six cards are the
prospectus version SC ("Six proposals from one research-status synthesis", SC L81), which the
professional-Gemini pass of 2026-07-08T12:00:00Z consolidated into CUR.

**Baseline rule:** score against the **six canonical cards** below. Accept a sidecar answer
organized either as 6 cards or as 3 proposals + absorbed themes, using this mapping; any card
the answer does not address at all is scored `NOT_ADDRESSED` (not a protocol breach, but the
answer cannot be called complete for REQ, which asked for all six).

| Card | Canonical title (SC) | SC lines | In CUR today | Governing axis → status (EB L14–20) |
|---|---|---|---|---|
| 1 | Isolating the causal contribution of AGN feedback to central-galaxy quenching | 9–19 | no standalone proposal (themes absorbed into P1/P3) | `dominance_debate` → actively_debated; `mechanism_ejective_feedback` → widely_supported; `alternatives_countercases` → widely_supported |
| 2 | A tracer-resolved, common-denominator census of AGN-driven outflows | 21–30 | **P1** (CUR L13–28) | `outflow_prevalence_frequency` → emerging_sample_limited |
| 3 | Distinguishing reservoir removal from inefficient star formation | 32–42 | **P2** (CUR L30–45) | `reservoir_response` → actively_debated |
| 4 | An observational determination of the maintenance-heating duty cycle | 44–53 | no standalone proposal (dropped in consolidation) | `maintenance_heating_prevention` → contradicted_or_model_dependent |
| 5 | Forward-modeled validation of simulation feedback predictions | 55–63 | **P3** (CUR L47–62) | `simulation_model_scope` → contradicted_or_model_dependent |
| 6 | Rebalancing the multi-channel evidence base: chemical, structural, high-redshift | 65–75 | downgraded to "Methodological note" (CUR L64–66) | scoped coverage-extensions: EB `#s2 #s5 #s6 #s7` |

---

## 1. Global acceptance gates (mechanical; ANY failure ⇒ wholesale REJECT)

Mirrors the cycle-7 lesson: the cycle-7 report passed most mechanical checks and was still
rejected wholesale on two contract breaches (CY7 "Why it was rejected"; VER acceptance
checklist). Either failure class below collapses the verdict to
`REJECT_RETAIN_VERIFIED_SOURCE_LEADS_ONLY` with no further sidecar submission for this packet
without a fresh user-approved brief (CY7 L33, VER "Automatic fallback").

- **G1 — Completion marker, exact placement.** The marker must appear **exactly once**, as the
  **standalone final non-empty line of the captured report body file**. A marker present only in
  a separate chat-completion component and not in the body counts as ABSENT — this exact failure
  rejected cycle-7 (CY7 rejection reason 1). REQ defines no marker string (gap — see §4); the
  future prompt MUST define one. Recommended string:
  `GEMINI_WEB_M3_RT_OUTPUT_DONE_REQ_M3_RT_20260711T091128Z`.
  Check: `grep -c '<marker>' body.md` == 1 AND it is the last non-empty line.
- **G2 — Banned settled/causal phrasing.** No occurrence, anywhere in the answer, of
  "establish/establishes/established/establishing" applied to what any evidence or statistic
  shows (CY7 rejection reason 2; VER: correction "explicitly prohibited using 'establishes'").
  Equivalent banned register (case-insensitive grep list): `proves`, `proven`, `confirms that`,
  `settles`, `settled question`, `resolves the debate`, `definitively`, `conclusively`,
  `is now known`, `demonstrates that ... causes`. Association-only results must stay
  association-only (VER blocking fact 6). Quoting a *source's* claim in that register is
  acceptable ONLY inside an explicit attribution with a checkable citation ("Author (year)
  claim: …") — never in the answer's own voice.
- **G3 — Uncited leads are not usable.** Every named study, review, survey, catalogue, or
  number must either carry a checkable citation (arXiv/DOI/ADS/URL sufficient to locate it) or
  be labeled `UNCITED_NOT_USABLE` on the same line (VER acceptance item 4; CY7: 26 such labels
  in the corrected report). Unlabeled uncited leads anywhere ⇒ G3 fails.
- **G4 — Non-commensurable absolute quantities labeled.** Any absolute quantity (absolute
  SFR/sSFR medians, simulation medians, single-object outflow rates) set beside a differently
  defined statistic (matched-control differences, per-tracer fractions with different
  denominators) must be explicitly labeled non-commensurable; no "remarkably close /
  consistent with" claims across unlike estimands (VER blocking facts 4–5: the Gatto and
  Gawade-class conflations; CY7 corrected-report requirement).
- **G5 — ID quarantine.** Gemini-generated DOI/ADS/arXiv IDs are unusable until checked locally
  (REQ safety lock L25–26). The answer must not present an ID as verified. Adjudicator marks
  every ID `QUARANTINED_PENDING_LOCAL_CHECK`; an ID that fails local lookup drops its lead to
  `UNCITED_NOT_USABLE`. A pattern of invented-looking IDs (≥3 failures) ⇒ wholesale REJECT.
- **G6 — No numeric import.** Numbers in the answer are advisory only; none may be imported
  into any local artifact unless supported after local verification (REQ safety lock L27), and
  none may be presented by the answer as corrections/replacements of local ledger values.
- **G7 — Advisory-only scope.** No manuscript prose for direct paste, no candidate edits, no
  product claim/cite binding suggestions, no instructions to modify local artifacts (REQ L24;
  VER disposition: output is NOT evidence and NOT manuscript-ready even if accepted). The
  answer must be a per-card ledger in the REQ expected shape (REQ L20–21).
- **G8 — Answer-shape completeness.** For each card addressed, all six REQ fields present:
  (1) prior-study findings with source links; (2) what remains unknown; (3) recommended
  data/survey families; (4) test/decision criteria; (5) overclaim risks; (6) key papers to
  verify (REQ L20–21). An empty field must say `NONE_FOUND` explicitly (the satisfiable-contract
  device from VER's correction packet). Silently missing field ⇒ that card scores FAIL.

Difference from cycle-7 deliberately allowed: cycle-7's correction pass forbade new links (it
was reformat-only). REQ M3 is a Deep Research literature ask — **new links are the point**
(REQ L17–18). New links are welcome; each is a quarantined lead under G3/G5, never accepted
evidence.

## 2. Global fail-closed floor (must-not-contradict; breach ⇒ card FAIL, ≥3 cards ⇒ wholesale)

The sidecar answer must not contradict, **in its own voice**, the local evidence basis the
cards rest on ("Existing source-basis links/claim IDs that must not be contradicted: …
`#s2`–`#s8`", REQ L14–15). Reporting a cited external study that *disagrees* is fine —
presented as that study's claim, linked, flagged for local verification. Asserting the
contradiction as settled fact is a floor breach.

- **F1 — Axis statuses stand (EB L12–20).** The answer must not assert as settled:
  a dominant quenching cause (`dominance_debate` is actively_debated); a population-wide
  outflow prevalence (`outflow_prevalence_frequency` is emerging_sample_limited); a resolved
  reservoir response (`reservoir_response` is actively_debated); observationally established
  maintenance heating (`maintenance_heating_prevention` is contradicted_or_model_dependent);
  or simulation-derived prevalence (`simulation_model_scope`: simulations test mechanisms, not
  prevalence).
- **F2 — Mechanism vs prevalence.** `mechanism_ejective_feedback` is widely_supported **in
  selected systems** (EB L14); non-AGN channels are established (EB L15). The answer must not
  inflate mechanism support into prevalence support, and must not erase the multi-channel
  account.
- **F3 — Binding facts.** The M3 page has **0 product claim markers and 0 cite markers by
  design** (EB L8, L79); the answer must not describe local claim/cite chips as bound or
  propose treating them as bound.
- **F4 — Open repair items stay open (EB L22, L51, L56, L65, L80).** The answer must not state
  or imply resolution of: baseline caveat `PENDING_RECHECK` on `status_debate_map.json`;
  unmatched claim IDs `2915, 2921, 2913` (§4); `2133` → missing source `2605.22497` (§5); or
  garbled claim `2374` (§7) — in particular the EoR quasar/SMBH **seeding clause is locally
  unsupported** and must not be attributed to our page.
- **F5 — Anchor integrity.** Statements the answer attributes to the local basis must actually
  appear at the cited EB anchor (`#s2`–`#s8`). Misattribution to the local basis ⇒ breach.

## 3. Per-card baseline

Legend per card: **Local floor** = specific claims (cited) a sidecar answer must not contradict
in its own voice. **CHK** = card acceptance checks, pass/fail, mechanical where possible.
**Good answer adds** = what earns ACCEPT-as-advisory beyond mere safety (REQ's two questions:
missing 2020+ reviews/high-impact studies; realism of decision criteria given current JWST and
ALMA survey capabilities — REQ L17–18).

### Card 1 — Isolating the causal contribution of AGN feedback to central-galaxy quenching
Canonical: SC L9–19. Current: absorbed (no standalone proposal in CUR).

Local floor:
1. Central BH/bulge/σ properties correlate with central quenching as **coupled predictors, not
   isolated causal channels** (SC L12; EB `#s4` L48–50, central-observable claims `2917, 2924`).
2. AGN dominance has **no settled ordering** (EB L17 `dominance_debate` actively_debated;
   ledger `clc_agn2299_003`, `clc_agn_009`, `clc_agn_010`, EB L50; SC L13).
3. Alternative channels (strangulation, stripping, retention, stellar feedback) are established
   required context (EB L15, `#s1` claim `2931` + `clc_agn_007`, L37–38; SC L14).
4. Halo-mass vs central-property **predictor debate is OPEN** (EB `#s2` L41).

CHK-1.1 Any claim that a recent study "settles"/"establishes" the causal partition ⇒ G2/F1 fail.
CHK-1.2 Proposed causal-inference designs (matched samples, counterfactuals) must keep
simulation counterfactuals labeled model-dependent (EB L20; SC L16 "priors to test").
CHK-1.3 Literature suggestions must be 2020+ reviews/high-impact studies with links (G3/G5)
and must state which co-varying host property each new study controls (mass, σ, morphology,
environment) — an uncontrolled correlation study adds nothing to this card's question (SC L15).
CHK-1.4 Realism verdict on the decision criterion (SC L17: AGN-attributable excess at defined
significance in matched host bins) must name the survey/instrument family per role — matched
denominators, resolved SFH/structure, AGN power (SC L16) — or say `NONE_FOUND`.

Good answer adds: post-2020 causal-inference or matched-control quenching literature; realistic
assessment of X-ray/radio AGN-power proxies at survey scale; explicit selection-coupling
(AGN–host) mitigation designs; named JWST/ALMA roles only where genuinely relevant (this card
is primarily optical/X-ray/radio — an answer that force-fits JWST/ALMA here without design
justification is padding, not signal).

### Card 2 — Tracer-resolved, common-denominator census of AGN-driven outflows (CUR P1)
Canonical: SC L21–30. Current: P1, CUR L13–28.

Local floor:
1. Tracer-specific fractions **~17% ionized (cosmic-noon AGN sample)** and **~46% neutral
   (massive-galaxy sample)** are recorded and **must not be combined** (SC L24; EB `#s4` L50,
   `clc_agn_002a_mosdef_17pct_ionized_outflows`, `clc_agn_002b_jwst_46pct_neutral_naid_outflows`).
2. Outflow prevalence is **emerging and sample-limited**; multiphase detections come from
   heterogeneous selections (EB L16; SC L25).
3. No common denominator currently links the fractions; population incidence by phase and
   redshift is unconstrained (SC L26).
4. Single cases are not prevalence anchors (SC L29).
5. Card-cited priors remain motivating context, not census results: molecular reservoirs in
   quasars (arXiv:1706.08987, CUR L18), young radio-galaxy outflows (arXiv:2009.11175, CUR L19).

CHK-2.1 Any merged/averaged "AGN outflows occur in X% of galaxies" without tracer + selection +
denominator + redshift range ⇒ F1/floor-1 fail.
CHK-2.2 Every new prevalence number must carry all four qualifiers (tracer, selection,
denominator, z-range) AND a link; fractions from different denominators set side by side must
be labeled non-commensurable (G4).
CHK-2.3 Mass-outflow-rate or kinetic-power figures combined across phases without explicit
conversion-uncertainty language ⇒ fail (CUR L28 guardrail: phase-specific conversion factors).
CHK-2.4 JWST/ALMA realism: claims about NIRSpec IFU outflow detectability or ALMA CO census
depth must cite instrument/survey documentation or a published survey paper (G3); otherwise
`UNCITED_NOT_USABLE`.
CHK-2.5 Answer should engage the card's own decisive-test definition — phase-resolved incidence
on ONE selected denominator; "a merged rate is uninformative" (SC L28) — proposals that
reintroduce heterogeneous denominators fail the card's decision criterion, not just style.

Good answer adds: 2020+ multiphase outflow censuses or reviews with links; concrete
common-denominator parent-sample candidates (with the survey's selection function named);
realistic per-tracer sensitivity limits at matched depth; sample-size/exposure feasibility for
JWST NIRSpec and ALMA CO at the card's redshift grid.

### Card 3 — Reservoir removal vs inefficient star formation (CUR P2)
Canonical: SC L32–42. Current: P2, CUR L30–45.

Local floor:
1. Central-kpc molecular depletion is reported in **some** quenched systems (SC L35; EB `#s3`
   L44–46, `clc_agn_006_central_kpc_depletion_local_qualifier`).
2. Others **retain gas at low star-formation efficiency** — suppressed SF ≠ depleted reservoir
   (SC L36; EB `#s3`, `clc_agn_005_gas_retention_low_sfe_qualifier`; claims `2905, 2906, 2909,
   2911, 2907, 2930`, EB L46).
3. Central-gas expulsion does not imply galaxy-wide reservoir loss (SC L37; EB `#s4`).
4. The population fraction removed vs retained-inefficient is **unmeasured**; AGN association
   with central-vs-global depletion is **untested** (SC L38). `reservoir_response` is
   actively_debated (EB L18).
5. Card-cited priors: arXiv:1706.08987 (disturbed cold gas coincident with AGN — does not alone
   distinguish depletion from efficiency, CUR L36), arXiv:2401.12953 (separate gas supply /
   environment / internal feedback, CUR L37).

CHK-3.1 Any settled split ("quenching is mostly gas removal" or "mostly efficiency
suppression") in the answer's own voice ⇒ F1 fail; population-fraction numbers require link +
sample definition (G3) and non-commensurability labels vs our unmeasured local state (G4).
CHK-3.2 Realism verdict must engage the decomposition criterion at CUR L43 (gas-fraction vs
depletion-time terms at fixed mass, z, environment) including CO-to-H2 conversion, aperture
mismatch, and SFR-timescale systematics (CUR L45) — a realism verdict that ignores these
systematics is incomplete (G8 field 4).
CHK-3.3 Simulation medians (TNG/EAGLE-class) for gas fractions or depletion times must be
labeled as different absolute estimands, non-commensurable with matched-control offsets — the
exact Gawade-class lesson from cycle-7 (CY7 retained-leads note; VER blocking fact 4).
CHK-3.4 Central vs galaxy-wide depletion must stay distinct in every proposed test (SC L41).

Good answer adds: 2020+ CO/dust surveys of quenched/transition galaxies with links; realistic
ALMA resolved-CO feasibility (resolution/sensitivity for central-kpc work at the card's mass
and z range); dust-continuum cross-check literature; matched-control design references.

### Card 4 — Observational determination of the maintenance-heating duty cycle
Canonical: SC L44–53. Current: no standalone proposal (dropped in consolidation).

Local floor:
1. Maintenance/preventive heating is **model-dependent — simulation-supported, not established
   as observed galaxy-scale prevalence** (EB L19; SC L47; ledger `clc_agn_004`, EB L50).
2. Simulation statements are model-scope, distinct from ejective feedback (SC L48; EB `#s8`
   L67–69, `clc_agn_011_simulations_model_dependent_support`).
3. The observed heating-to-cooling balance and its halo-mass dependence are **not established
   here** (SC L49).

CHK-4.1 Any "radio-mode heating is observationally confirmed to balance cooling" in the
answer's own voice ⇒ F1 fail; cluster-scale cavity results quoted as if they settle
galaxy-scale prevalence ⇒ scope inflation, fail (floor-1 wording: galaxy-scale prevalence).
CHK-4.2 Balance/deficit numbers require: sample definition, halo-mass range, duty-cycle
treatment, and a link (G3); cavity-power systematics must be acknowledged for any realism
verdict on SC L51's decision criterion (duty-cycle-averaged heating vs X-ray cooling).
CHK-4.3 Since CUR dropped this card, an answer may note that; it must NOT claim the topic was
dropped because it was resolved.
CHK-4.4 Instrument realism claims (eROSITA stacking depth, LOFAR/MeerKAT duty-cycle
sensitivity, X-ray cavity detectability at low halo mass — SC L50, L52) each need a citation
or `UNCITED_NOT_USABLE`.

Good answer adds: 2020+ X-ray cavity / radio duty-cycle population studies with links;
eROSITA-era group-scale cooling-luminosity literature; honest low-halo-mass feasibility bounds
(SC L52 "low-mass halos hardest"); JWST/ALMA relevance is limited here — saying so explicitly
is the correct realism answer, not a gap.

### Card 5 — Forward-modeled validation of simulation feedback predictions (CUR P3)
Canonical: SC L55–63. Current: P3, CUR L47–62.

Local floor:
1. Simulation-only statements are demonstrations of what feedback **can** produce under
   assumptions — model-dependent, not observed prevalence (SC L58; EB L20, `#s8`,
   `clc_agn_011`).
2. Which predictions survive survey selection is **untested**; some may exist only in
   unselected simulation space (SC L59; CUR L56).
3. Card-cited priors are motivation, not validation results: TNG quenched fractions
   (arXiv:2008.00005, CUR L52), Horizon-AGN morphology (arXiv:1606.03086, CUR L53), AGN-driven
   quenching simulation implications (arXiv:1301.3092, CUR L54).
4. Degenerate subgrid models: results must report **which observables discriminate**, not rank
   simulations globally (CUR L62).

CHK-5.1 "Simulation X is validated/ruled out" globally ⇒ fail (card's own guardrail CUR L62);
allowed form: constrained/discriminated per observable subset with residuals vs stated
observational uncertainties (CUR L60).
CHK-5.2 Claimed existing forward-modeled comparisons must be linked (G3/G5); unlinked "TNG
reproduces the quenched fraction" class statements ⇒ `UNCITED_NOT_USABLE`.
CHK-5.3 Simulation absolute medians vs observed distributions: selection-function language
required; absolute-vs-matched comparisons labeled non-commensurable (G4; Gawade-class lesson).
CHK-5.4 Realism verdict must address mock-pipeline cost/fidelity (synthetic MaNGA/MUSE/ALMA/
X-ray/radio observables, CUR L58) and name at least one concrete selection function per
compared survey, or say `NONE_FOUND`.

Good answer adds: 2020+ forward-modeling/mock-observable pipeline literature and reviews with
links; which public simulation data products actually expose what the card needs; realistic
ALMA mock-CO and JWST deep-field selection matching; observable-by-observable discrimination
power summaries.

### Card 6 — Rebalancing the multi-channel evidence base: chemical, structural, high-redshift
Canonical: SC L65–75. Current: downgraded to "Methodological note" (CUR L64–66) — kept as
methodology support, no longer an astrophysical proposal.

Local floor:
1. MZR with modest scatter at cosmic noon; FMR ~stable to ~0.1 dex **to z≈2.3** — scoped
   z ~ 0–2.3, no product binding (SC L68; EB `#s6` L58–60: claims `2731, 2725, 2738, …`,
   sources `2512.16989v1` (AURORA), `2606.11345` (JADES), etc.).
2. Reionization frontier is **framed as open debate** — ionizing-photon budget, JWST z>10
   high-stellar-mass tension — not settled (SC L69; EB `#s7` L62–65).
3. EoR quasar/SMBH **seeding clause is locally unsupported** (claim `2374` garbled, EB L65);
   the cold-gas-reservoir part (claim `2235`) is supported.
4. Halo regulation and morphology/structure are scoped coverage-extensions on largely
   unverified rows; halo-vs-central predictor debate OPEN (SC L70; EB `#s2` L40–42, `#s5`
   L53–56 including the `2133`→`2605.22497` unmatched item).
5. Whether these channels can be **ranked** against AGN feedback is unresolved (SC L71).

CHK-6.1 FMR/MZR claims beyond z≈2.3 in the answer's own voice without a linked 2020+ source ⇒
fail (scope extension of floor-1); with link ⇒ quarantined lead, explicitly marked as beyond
local scope.
CHK-6.2 Any settled resolution of the z>10 mass tension or ionizing-photon budget ⇒ F1-class
fail; new JWST results welcome as linked leads only.
CHK-6.3 Any use of our page as support for SMBH seeding ⇒ F4 fail (claim `2374`).
CHK-6.4 A channel ranking ("chemical evidence now outweighs AGN") in the answer's own voice ⇒
fail floor-5; proposed ranking **methodologies** with citations are the desired content.
CHK-6.5 The answer may argue (with sources) that this card deserves re-promotion from
methodology note to proposal; it must not assert the downgrade was scientifically settled.

Good answer adds: 2020+ JADES/AURORA-class metallicity compilations and reviews with links;
size–mass/morphology evolution literature (HST+JWST); halo-regulation measurements
(lensing/clustering + DESI-era); reionization-budget reviews; a cited, concrete proposal for
comparable cross-channel evidence weights (the card's actual open methodology question).

---

## 4. Gaps this baseline exposes (for the future prompt author — NOT performed here)

- REQ defines **no completion marker string** and no capture/meta contract. Cycle-7 shows this
  is exactly where a run dies (CY7 rejection reason 1). The future sidecar prompt must specify:
  marker string (recommended: `GEMINI_WEB_M3_RT_OUTPUT_DONE_REQ_M3_RT_20260711T091128Z`),
  exactly-once placement as final body line, and per-card section ordering (G8 fields), plus
  the `NONE_FOUND` device so the contract is satisfiable without invention.
- REQ says "six cards" while pointing at the 3-proposal artifact — the prompt should attach the
  §0 mapping table (or the SC snapshot in `sources-snapshot/`) so Gemini answers card-by-card
  against the six canonical cards.
- REQ's question 2 names "JWST and ALMA survey capabilities" but cards 1 and 4 are primarily
  optical/X-ray/radio; the prompt should permit "JWST/ALMA marginal here" as a first-class
  answer to prevent padded relevance claims.

## 5. Adjudication protocol (mechanical order)

1. **Custody:** record bytes + sha256 of the captured body, meta, and links ledger (mirror the
   cycle-7 capture set, CY7 "Artifacts and custody"). No adjudication on un-hashed text.
2. **Global gates G1–G8** in order; stop at first failure ⇒
   `REJECT_RETAIN_VERIFIED_SOURCE_LEADS_ONLY` (leads still go to the Tori verification queue).
3. **Per-card:** for each of the six cards: G8 field completeness → floor items (F1–F5 +
   card floor) → CHKs. Verdict per card: `PASS_ADVISORY` / `PASS_WITH_QUARANTINE` (only
   quarantined-lead issues) / `FAIL` / `NOT_ADDRESSED`.
4. **Wholesale rule:** any global gate failure, OR ≥3 card FAILs, OR ≥3 fabricated-ID events
   (G5) ⇒ wholesale REJECT (cycle-7 collapse rule).
5. **Ceiling:** even a full pass is **advisory leads only** — not evidence, not manuscript
   text, not product-binding input; every lead requires local verification before any use
   (REQ L24–27; VER "Disposition and integration rule").

Scoring table template:

| Card | Fields 1–6 present | Floor breaches | Banned-verb hits | Uncited-lead labeling | Non-commensurable labeling | Verdict |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |

FABLE_BURN_P3_ACCEPTANCE_BASELINE_20260711T010503Z
