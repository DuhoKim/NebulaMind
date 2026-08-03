FABLE_HARD_BURN_H2_REQ_CONTRACT_20260711T035354Z

# Gemini sidecar REQ prompt-contract packet — REQ_M3_RT_20260711T091128Z

Hard burn `fable-weekly-hard-burn-20260711T035354Z`, lane H2. Offline prep for rollup
follow-up item 2 (P3 follow-up queue item 2): give the future supervised Gemini Web sidecar
run — gated under `DUHO_GEMINI_WEB_WIKI_RESEARCH_ARTIFACT_SCOPE_20260711T004710Z` — a complete
prompt contract so it is cheap to launch and cheap to adjudicate.

**Binding disclaimers.** Nothing here is applied anywhere: the live REQ file is untouched, no
run is performed/requested/scheduled, no network was used. Section A is a *candidate* text for
Hwao to adopt under separate Duho approval. Everything below derives from four pinned inputs
(sha256 verified, see `H2_RECEIPT.md`):

| Abbrev | Input | sha256 |
|---|---|---|
| BL | `M3_ACCEPTANCE_BASELINE.md` (P3, prior burn) | `d028f3c716cc123be1840170d6111c42e24693451c9d3bf90284fdb19691d433` |
| DP | `RT_CARDS_DEEPENING.md` (P3, prior burn) | `21564dd6d78c72483087d436f4256e461913ec9ab013c4ab7053bfe14eed7e18` |
| P3R | `P3_RECEIPT.md` (P3, prior burn) | `70573e18df09cf45b73dcee5b75602541a6e33ea427dfa4b378c2f207eecd90b` |
| REQ r1 | `sources-snapshot/RT_GEMINI_WEB_REQUEST_M3_20260711T091128Z.md` (byte-identical to live REQ per P3R L27) | `b3488701775cf336da6b8ddbe1a66a91370f2b10afadfb8ed5b6e90098804040` |

`BL L<n>` / `DP L<n>` / `REQ L<n>` cite line numbers in those exact byte versions.
Live REQ path (for the future adopter; NOT modified by H2):
`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/gemini-web-deep-research/requests/RT_GEMINI_WEB_REQUEST_M3_20260711T091128Z.md`

Packet contents: **A** revised REQ candidate (verbatim, paste-ready) · **B** per-card
adjudication scorecard mapped line-by-line to BL · **C** supervised-run operator checklist ·
**D** precise diff r1→r2 with per-change justification · **E** (stretch) failure-mode playbook.

---

## A. Revised REQ candidate — r2, verbatim, paste-ready (NOT applied)

Copy everything between the fence lines into the live REQ path when (and only when) adoption
is approved. The block marked "OPERATOR-SIDE" stays in the file but is excluded from the text
pasted into Gemini (see C, step R2).

```markdown
# Gemini-Web Deep Research Request for Method 3 RT Quality

Marker: `RT_GEMINI_WEB_DEEP_RESEARCH_SIDECAR_PROTOCOL_V1`

**Request ID:** `REQ_M3_RT_20260711T091128Z`
**Revision:** r2 — contract-hardened candidate (drafted offline by hard-burn H2, 2026-07-11).
Adoption and the run itself are gated on separate Duho approval under
`DUHO_GEMINI_WEB_WIKI_RESEARCH_ARTIFACT_SCOPE_20260711T004710Z`.
**Method:** Method 3 (Debate-map-to-wiki rebuild)
**Current RT artifact paths:**
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.md`
- `/Users/duhokim/NebulaMind/NebulaMind/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html`
- Byte-identical snapshot copies exist under
  `.hermes/handoffs/galaxy-evolution/static-publish-20260709T124353Z/live-root-before/debate-map-to-wiki-rebuild/research-topics-from-wiki-20260708T090359Z/`
  (md sha256 `4f8e7fb0f272837b9b075f028cfb20ee89849e83383de104353fd529289abb56`).

**Exact topic/cards to improve:**
All 6 canonical research topic cards targeting Galaxy Evolution open questions. The artifact
at the paths above holds 3 consolidated proposals; the six canonical cards are the six-card
prospectus version (order marker
`AUTOPILOT_RESEARCH_TOPICS_JOURNAL_EVIDENCE_LINK_PASS_20260708T112408Z`). Answer
card-by-card against this mapping:

| Card | Canonical title | In current artifact |
|---|---|---|
| 1 | Isolating the causal contribution of AGN feedback to central-galaxy quenching | absorbed into P1/P3 (no standalone proposal) |
| 2 | A tracer-resolved, common-denominator census of AGN-driven outflows | Proposal P1 |
| 3 | Distinguishing reservoir removal from inefficient star formation | Proposal P2 |
| 4 | An observational determination of the maintenance-heating duty cycle | dropped in consolidation (still canonical) |
| 5 | Forward-modeled validation of simulation feedback predictions | Proposal P3 |
| 6 | Rebalancing the multi-channel evidence base: chemical, structural, high-redshift | downgraded to "Methodological note" |

All six cards MUST be addressed. A card with nothing to add still gets its full section
skeleton (contract C2) with `NONE_FOUND` fields (contract C3). Cards 1 and 4 being absorbed/
dropped in the current artifact is an editorial consolidation, not a scientific resolution;
answer them as first-class cards.

**Existing source-basis links/claim IDs that must not be contradicted:**
Local evidence anchors from `evidence-basis-20260708T014205Z.md#s2` to `#s8`. A cited external
study that disagrees may be reported as that study's claim — linked and flagged for local
verification — but the answer must not assert the contradiction as settled fact in its own
voice.

**The question Gemini should answer:**
What major recent (2020+) literature reviews or high-impact studies are missing from these
cards? Are the proposed decision criteria realistic given current JWST and ALMA survey
capabilities?
Note on question 2: cards 1 and 4 are primarily optical/X-ray/radio territory. For those
cards, "JWST/ALMA marginal here — the relevant capability is <instrument family>" is a
first-class, complete realism answer when justified. Do not force-fit JWST/ALMA relevance.

**Expected output shape — BINDING OUTPUT CONTRACT (new in r2):**

- C1 (meta header). The answer is ONE self-contained markdown report body. Its first lines
  are a meta block:

      # M3 RT sidecar answer — REQ_M3_RT_20260711T091128Z
      Run date (UTC): <YYYY-MM-DDTHH:MM:SSZ, operator-verified>
      Model: <model/product self-identification>
      Cards addressed: <N> of 6

- C2 (per-card section contract). For EACH card 1–6, in ascending order, exactly these seven
  headings, echoing the canonical titles verbatim:

      ## Card <N> — <canonical title from the mapping table>
      ### <N>.1 Prior-study findings (with source links)
      ### <N>.2 What remains unknown
      ### <N>.3 Recommended data/survey families
      ### <N>.4 Test/decision-criteria realism (JWST/ALMA or stated alternative)
      ### <N>.5 Overclaim risks
      ### <N>.6 Key papers to verify

- C3 (empty-field device). A field with genuinely nothing to report contains exactly
  `NONE_FOUND` — never silently omitted, never padded with filler.

- C4 (citation labeling). Every named study, review, survey, catalogue, or number carries a
  checkable citation (arXiv ID, DOI, ADS bibcode, or URL) on the same line, or the same-line
  label `UNCITED_NOT_USABLE`.

- C5 (wording contract). In the answer's own voice, settled/causal register about what
  evidence or statistics show is banned (case-insensitive): establish / establishes /
  established / establishing, proves, proven, confirms that, settles, settled question,
  resolves the debate, definitively, conclusively, is now known, "demonstrates that … causes".
  Association-only results stay association-only. A source's own claim in that register may be
  quoted only as explicit attribution with a checkable citation ("Author (year) claim: …").

- C6 (estimand labels). Any absolute quantity (absolute SFR/sSFR medians, simulation medians,
  single-object outflow rates) set beside a differently defined statistic (matched-control
  differences, per-tracer fractions with different denominators) must be explicitly labeled
  non-commensurable; no "remarkably close" / "consistent with" claims across unlike estimands.
  Every incidence/prevalence number carries all four qualifiers: tracer + selection +
  denominator + redshift range.

- C7 (links ledger). After Card 6, a section `## Links ledger` lists every cited item, one per
  line: `<short name> | <citation or UNCITED_NOT_USABLE> | QUARANTINED_PENDING_LOCAL_CHECK`.

- C8 (completion marker). The exact string

      GEMINI_WEB_M3_RT_OUTPUT_DONE_REQ_M3_RT_20260711T091128Z

  must appear exactly once in the report body, as the standalone final non-empty line of the
  body file. A marker present only in a chat-UI completion element and not in the body counts
  as ABSENT and the run is rejected.

**Adjudication reference — OPERATOR-SIDE, not part of the pasted prompt:**
Answers are scored fail-closed against `M3_ACCEPTANCE_BASELINE.md`
(sha256 `d028f3c716cc123be1840170d6111c42e24693451c9d3bf90284fdb19691d433`, in prior burn dir
`fable-weekly-burn-20260711T010503Z/p3-m3-rt-baseline/`): global gates G1–G8 in order, floor
F1–F5, per-card CHKs; per-card verdicts PASS_ADVISORY / PASS_WITH_QUARANTINE / FAIL /
NOT_ADDRESSED. Any global-gate failure, OR ≥3 card FAILs, OR ≥3 fabricated-ID events ⇒
wholesale `REJECT_RETAIN_VERIFIED_SOURCE_LEADS_ONLY`. Even a full pass is advisory leads only.

**Explicit safety locks copied from protocol:**
- Output is advisory only. Not accepted evidence, not product claim binding.
- Do not use Gemini-generated DOI/ADS/arXiv IDs until checked locally.
- Do not import numeric results unless supported.
```

---

## B. Per-card adjudication scorecard (line-by-line to BL)

How to use: adjudicate only hashed captured text (BL L351–352). Run B.1 gates in order — stop
at first failure ⇒ wholesale `REJECT_RETAIN_VERIFIED_SOURCE_LEADS_ONLY`, leads still quarantined
to the Tori verification queue (BL L353–354). Then B.2 floors and B.3 per card: fields → floors
→ CHKs (BL L355–357). Wholesale rule: any gate failure OR ≥3 card FAILs OR ≥3 fabricated-ID
events (BL L358–359). Ceiling: even full pass = advisory leads only (BL L360–362). Fill ☐ with
PASS / FAIL / N.A. plus a one-line evidence note (grep output or quote + line ref).

### B.1 Global gates (ANY failure ⇒ wholesale REJECT; BL L52–106)

| ID | Reject-if | BL ref | Mechanical check | ☐ |
|---|---|---|---|---|
| G1 | Completion marker `GEMINI_WEB_M3_RT_OUTPUT_DONE_REQ_M3_RT_20260711T091128Z` not exactly once as standalone final non-empty body line; marker only in chat-completion element = ABSENT (cycle-7 rejection 1) | BL L60–66 | `grep -c '<marker>' body.md` == 1 AND `awk 'NF{last=$0} END{print last}' body.md` == marker | ☐ |
| G2 | Banned settled/causal register in own voice: establish(es/ed/ing), proves, proven, confirms that, settles, settled question, resolves the debate, definitively, conclusively, is now known, demonstrates that … causes; attribution-quoted hits acceptable only with checkable citation | BL L67–75 | `grep -inE 'establish(es|ed|ing)?\b|proves|proven|confirms that|settles|settled question|resolves the debate|definitively|conclusively|is now known' body.md` then manual attribution triage of each hit | ☐ |
| G3 | Any named study/review/survey/catalogue/number without checkable citation AND without same-line `UNCITED_NOT_USABLE` | BL L76–79 | manual sweep per card + links-ledger cross-check | ☐ |
| G4 | Absolute quantities set beside differently defined statistics without non-commensurable label; "remarkably close/consistent with" across unlike estimands (Gatto/Gawade-class conflations) | BL L80–85 | manual; flag every cross-estimand comparison | ☐ |
| G5 | Any Gemini-generated DOI/ADS/arXiv ID presented as verified; ≥3 failed-lookup IDs ⇒ wholesale | BL L86–89 | inventory all IDs → mark `QUARANTINED_PENDING_LOCAL_CHECK`; local lookups happen in the gated Tori pass | ☐ |
| G6 | Numbers presented as corrections/replacements of local ledger values, or importable without local verification | BL L90–92 | manual | ☐ |
| G7 | Manuscript prose for paste, candidate edits, claim/cite binding suggestions, instructions to modify local artifacts; answer not in the per-card ledger shape | BL L93–96 | manual | ☐ |
| G8 | For any addressed card, one of the six REQ fields silently missing (empty field must say `NONE_FOUND`) ⇒ that card FAIL | BL L97–101 | heading grep per card: `grep -c '^### <N>\.' body.md` == 6 | ☐ |

Deliberately allowed (do NOT penalize): new links are the point of this Deep Research ask —
each is a quarantined lead under G3/G5, never accepted evidence (BL L103–106).

### B.2 Global fail-closed floor (own-voice contradiction of EB `#s2`–`#s8`; breach ⇒ card FAIL, ≥3 cards ⇒ wholesale; BL L108–136)

| ID | Breach-if (own voice) | BL ref | ☐ |
|---|---|---|---|
| F1 | Asserts as settled: dominant quenching cause / population-wide outflow prevalence / resolved reservoir response / observationally established maintenance heating / simulation-derived prevalence | BL L116–122 | ☐ |
| F2 | Inflates mechanism support (widely_supported in selected systems) into prevalence support, or erases the multi-channel account | BL L123–126 | ☐ |
| F3 | Describes local claim/cite chips as bound (M3 page has 0 product claim markers and 0 cite markers by design) or proposes treating them as bound | BL L127–129 | ☐ |
| F4 | States/implies resolution of open repair items: `PENDING_RECHECK` baseline caveat; unmatched claims `2915, 2921, 2913`; `2133`→missing `2605.22497`; garbled claim `2374` (EoR SMBH-seeding clause locally unsupported) | BL L130–134 | ☐ |
| F5 | Attributes to a local EB anchor a statement that does not appear there | BL L135–136 | ☐ |

### B.3 Per-card scorecards

Verdict vocabulary per card: `PASS_ADVISORY` / `PASS_WITH_QUARANTINE` (only quarantined-lead
issues) / `FAIL` / `NOT_ADDRESSED` (BL L356–357). Fields row = contract C2/G8. "Advisory
credit" = what earns ACCEPT beyond safety (BL legend L140–144); cross-check each card's
tightened criterion in DP §(b) — an answer engaging it scores in minutes (DP L302–310).

#### Card 1 — Isolating the causal contribution of AGN feedback to central-galaxy quenching (BL L146–172; DP L17–61)

| Item | Reject-if / requirement | BL ref | ☐ |
|---|---|---|---|
| Fields 1–6 | all present or `NONE_FOUND` | BL L97–101 | ☐ |
| Floor 1.1 | contradicts: BH/bulge/σ correlate as coupled predictors, not isolated causal channels | BL L150–151 | ☐ |
| Floor 1.2 | contradicts: AGN dominance has no settled ordering | BL L152–153 | ☐ |
| Floor 1.3 | contradicts: alternative channels are established required context | BL L154–155 | ☐ |
| Floor 1.4 | contradicts: halo-mass vs central-property predictor debate is OPEN | BL L156 | ☐ |
| CHK-1.1 | claims a study "settles/establishes" the causal partition ⇒ G2/F1 fail | BL L158 | ☐ |
| CHK-1.2 | causal designs must keep simulation counterfactuals labeled model-dependent | BL L159–160 | ☐ |
| CHK-1.3 | literature must be 2020+ with links AND state which co-varying host property each study controls | BL L161–163 | ☐ |
| CHK-1.4 | realism verdict names survey/instrument family per role (matched denominators, resolved SFH/structure, AGN power) or `NONE_FOUND` | BL L164–166 | ☐ |
| Advisory credit | matched-control/causal-inference 2020+ literature; X-ray/radio AGN-power proxies at survey scale; selection-coupling mitigation; JWST/ALMA only where justified (force-fit = padding) | BL L168–172 | ☐ |
| **Verdict** | | | ☐ |

#### Card 2 — Tracer-resolved, common-denominator census of AGN-driven outflows / CUR P1 (BL L174–206; DP L65–107)

| Item | Reject-if / requirement | BL ref | ☐ |
|---|---|---|---|
| Fields 1–6 | all present or `NONE_FOUND` | BL L97–101 | ☐ |
| Floor 2.1 | combines the ~17% ionized and ~46% neutral tracer-specific fractions | BL L178–180 | ☐ |
| Floor 2.2 | contradicts: prevalence is emerging and sample-limited, heterogeneous selections | BL L181–182 | ☐ |
| Floor 2.3 | contradicts: no common denominator links the fractions; incidence by phase/z unconstrained | BL L183–184 | ☐ |
| Floor 2.4 | treats single cases as prevalence anchors | BL L185 | ☐ |
| Floor 2.5 | treats card-cited priors (arXiv:1706.08987, arXiv:2009.11175) as census results | BL L186–188 | ☐ |
| CHK-2.1 | merged "X% of galaxies" without tracer+selection+denominator+z ⇒ F1 fail | BL L190–191 | ☐ |
| CHK-2.2 | every prevalence number: all four qualifiers AND link; unlike denominators labeled non-commensurable | BL L192–194 | ☐ |
| CHK-2.3 | cross-phase outflow-rate/kinetic-power combination without conversion-uncertainty language ⇒ fail | BL L195–196 | ☐ |
| CHK-2.4 | NIRSpec-IFU / ALMA-CO realism claims cite instrument/survey documentation or `UNCITED_NOT_USABLE` | BL L197–198 | ☐ |
| CHK-2.5 | proposals reintroducing heterogeneous denominators fail the card's decision criterion | BL L199–201 | ☐ |
| Advisory credit | 2020+ multiphase censuses/reviews; concrete parent-sample candidates with selection functions; per-tracer sensitivity at matched depth; NIRSpec/ALMA feasibility at the card's z grid | BL L203–206 | ☐ |
| **Verdict** | | | ☐ |

#### Card 3 — Reservoir removal vs inefficient star formation / CUR P2 (BL L208–239; DP L110–153)

| Item | Reject-if / requirement | BL ref | ☐ |
|---|---|---|---|
| Fields 1–6 | all present or `NONE_FOUND` | BL L97–101 | ☐ |
| Floor 3.1 | contradicts: central-kpc depletion reported in SOME quenched systems | BL L212–213 | ☐ |
| Floor 3.2 | contradicts: others retain gas at low SFE — suppressed SF ≠ depleted reservoir | BL L214–216 | ☐ |
| Floor 3.3 | contradicts: central expulsion does not imply galaxy-wide loss | BL L217 | ☐ |
| Floor 3.4 | contradicts: removed-vs-retained fraction unmeasured; AGN association untested | BL L218–220 | ☐ |
| Floor 3.5 | treats card-cited priors (arXiv:1706.08987, arXiv:2401.12953) as settling depletion-vs-efficiency | BL L221–223 | ☐ |
| CHK-3.1 | settled split in own voice ⇒ F1; fraction numbers need link + sample definition + non-commensurability vs local unmeasured state | BL L225–227 | ☐ |
| CHK-3.2 | realism must engage the f_gas/t_dep decomposition incl. CO-to-H2, aperture, SFR-timescale systematics — else G8 field-4 incomplete | BL L228–231 | ☐ |
| CHK-3.3 | TNG/EAGLE-class medians labeled different absolute estimands, non-commensurable with matched-control offsets (Gawade-class) | BL L232–234 | ☐ |
| CHK-3.4 | central vs galaxy-wide depletion distinct in every proposed test | BL L235 | ☐ |
| Advisory credit | 2020+ CO/dust surveys of quenched/transition galaxies; ALMA resolved-CO feasibility at card's mass/z; dust-continuum cross-checks; matched-control design refs | BL L237–239 | ☐ |
| **Verdict** | | | ☐ |

#### Card 4 — Observational determination of the maintenance-heating duty cycle (BL L241–267; DP L157–197)

| Item | Reject-if / requirement | BL ref | ☐ |
|---|---|---|---|
| Fields 1–6 | all present or `NONE_FOUND` | BL L97–101 | ☐ |
| Floor 4.1 | contradicts: maintenance heating is model-dependent, not established observed galaxy-scale prevalence | BL L245–246 | ☐ |
| Floor 4.2 | contradicts: simulation statements are model-scope, distinct from ejective feedback | BL L247–248 | ☐ |
| Floor 4.3 | contradicts: observed heating-to-cooling balance and halo-mass dependence not established here | BL L249–250 | ☐ |
| CHK-4.1 | "radio-mode heating observationally confirmed to balance cooling" in own voice ⇒ F1; cluster cavities quoted as settling galaxy-scale prevalence ⇒ scope inflation | BL L252–254 | ☐ |
| CHK-4.2 | balance/deficit numbers need sample definition + halo-mass range + duty-cycle treatment + link; cavity-power systematics acknowledged | BL L255–257 | ☐ |
| CHK-4.3 | must not claim the card was dropped because resolved (consolidation was editorial) | BL L258–259 | ☐ |
| CHK-4.4 | eROSITA/LOFAR/MeerKAT/X-ray-cavity realism claims each cited or `UNCITED_NOT_USABLE` | BL L260–262 | ☐ |
| Advisory credit | 2020+ cavity/duty-cycle population studies; eROSITA-era group-scale cooling; honest low-halo-mass feasibility; explicit "JWST/ALMA limited here" is the correct realism answer | BL L264–267 | ☐ |
| **Verdict** | | | ☐ |

#### Card 5 — Forward-modeled validation of simulation feedback predictions / CUR P3 (BL L269–298; DP L200–242)

| Item | Reject-if / requirement | BL ref | ☐ |
|---|---|---|---|
| Fields 1–6 | all present or `NONE_FOUND` | BL L97–101 | ☐ |
| Floor 5.1 | contradicts: simulation-only statements are model-dependent demonstrations, not observed prevalence | BL L273–275 | ☐ |
| Floor 5.2 | contradicts: which predictions survive survey selection is untested | BL L276–277 | ☐ |
| Floor 5.3 | treats card-cited priors (arXiv:2008.00005, arXiv:1606.03086, arXiv:1301.3092) as validation results | BL L278–280 | ☐ |
| Floor 5.4 | ranks simulations globally instead of reporting which observables discriminate | BL L281–282 | ☐ |
| CHK-5.1 | "Simulation X validated/ruled out" globally ⇒ fail; allowed: per-observable constraint with residuals vs stated uncertainties | BL L284–286 | ☐ |
| CHK-5.2 | claimed forward-modeled comparisons linked; unlinked "TNG reproduces …" ⇒ `UNCITED_NOT_USABLE` | BL L287–288 | ☐ |
| CHK-5.3 | simulation absolute medians vs observed distributions: selection-function language + non-commensurable labels | BL L289–290 | ☐ |
| CHK-5.4 | realism addresses mock-pipeline cost/fidelity and names ≥1 concrete selection function per compared survey, or `NONE_FOUND` | BL L291–293 | ☐ |
| Advisory credit | 2020+ mock-observable pipelines/reviews; which public sim data products expose needed fields; ALMA mock-CO + JWST deep-field selection matching; per-observable discrimination power | BL L295–298 | ☐ |
| **Verdict** | | | ☐ |

#### Card 6 — Rebalancing the multi-channel evidence base (BL L300–331; DP L246–298)

| Item | Reject-if / requirement | BL ref | ☐ |
|---|---|---|---|
| Fields 1–6 | all present or `NONE_FOUND` | BL L97–101 | ☐ |
| Floor 6.1 | contradicts scoping: MZR modest scatter at cosmic noon; FMR ~stable to ~0.1 dex to z≈2.3, scoped z~0–2.3, no product binding | BL L305–308 | ☐ |
| Floor 6.2 | contradicts: reionization frontier framed as open debate (photon budget; z>10 mass tension) | BL L309–310 | ☐ |
| Floor 6.3 | uses our page to support SMBH seeding (claim `2374` garbled; cold-gas part `2235` stands) | BL L311–312 | ☐ |
| Floor 6.4 | contradicts: halo/structure channels are scoped coverage-extensions on lightly verified rows; predictor debate OPEN | BL L313–314 | ☐ |
| Floor 6.5 | asserts channels can (or cannot) be ranked against AGN — unresolved | BL L315 | ☐ |
| CHK-6.1 | FMR/MZR beyond z≈2.3 in own voice without linked 2020+ source ⇒ fail; with link ⇒ quarantined lead marked beyond local scope | BL L317–319 | ☐ |
| CHK-6.2 | settled resolution of z>10 tension or photon budget ⇒ F1-class fail; new JWST results as linked leads only | BL L320–321 | ☐ |
| CHK-6.3 | any SMBH-seeding support from our page ⇒ F4 fail | BL L322 | ☐ |
| CHK-6.4 | channel ranking in own voice ⇒ fail; ranking METHODOLOGIES with citations are the desired content | BL L323–324 | ☐ |
| CHK-6.5 | may argue re-promotion from methodology note with sources; must not assert the downgrade was scientifically settled | BL L325–327 | ☐ |
| Advisory credit | 2020+ JADES/AURORA-class compilations; size–mass/morphology evolution (HST+JWST); halo-regulation (lensing/clustering, DESI-era); reionization-budget reviews; a cited cross-channel weighting proposal | BL L328–331 | ☐ |
| **Verdict** | | | ☐ |

### B.4 Summary table (template verbatim from BL L364–373)

| Card | Fields 1–6 present | Floor breaches | Banned-verb hits | Uncited-lead labeling | Non-commensurable labeling | Verdict |
|---|---|---|---|---|---|---|
| 1 | | | | | | |
| 2 | | | | | | |
| 3 | | | | | | |
| 4 | | | | | | |
| 5 | | | | | | |
| 6 | | | | | | |

Wholesale verdict: ______ (REJECT if any G-gate failed, ≥3 card FAILs, or ≥3 fabricated-ID
events; otherwise ACCEPT-as-advisory with per-card verdicts; leads → Tori queue either way.)

---

## C. Supervised-run checklist (operator steps, custody, evidence capture)

**Authorization gate (read first).** The run happens only under
`DUHO_GEMINI_WEB_WIKI_RESEARCH_ARTIFACT_SCOPE_20260711T004710Z` with fresh, explicit Duho
approval naming this REQ. This packet authorizes nothing: it is offline prep (P3R follow-up
queue items 1–2 are `GATED — needs separate Duho approval`). Adopting the r2 candidate into
the live REQ path is itself a gated write for Hwao, outside H2's scope.

Pre-run:
- P1 ☐ Record UTC start, operator name, approval reference (message/file that granted the run).
- P2 ☐ Confirm the live REQ file equals the adopted r2 candidate; record its sha256
  (`shasum -a 256 <live REQ path>`). If it still equals r1 (`b3488701…8804040`), STOP — the
  contract gap that sank cycle 7 (missing marker/section contract) is still open.
- P3 ☐ Record baseline custody: BL sha256 must equal `d028f3c7…9691d433`; mismatch ⇒ STOP,
  re-pin before any adjudication.
- P4 ☐ Create capture dir `gemini-web-deep-research/answers/REQ_M3_RT_20260711T091128Z-r2-<UTC>/`.
- P5 ☐ Poll coordination files for the active burn/session (STOP/HOLD) before starting.

Run (supervised, single conversation):
- R1 ☐ Human watches the full generation; no unattended runs.
- R2 ☐ Paste exactly the r2 REQ text MINUS the "OPERATOR-SIDE" adjudication-reference block.
  No other instructions, no follow-up steering, no extensions/tools/account changes.
- R3 ☐ If generation visibly truncates, at most one neutral "continue" is permitted and must
  be logged in `meta.md` (H2-proposed operator rule — content-steering follow-ups are not
  permitted). If Gemini asks to browse/act beyond producing text, decline and note it.
- R4 ☐ No mid-run edits to any local file; the run produces text to capture, nothing else.

Capture (mirror the cycle-7 custody set — body, meta, links ledger; BL L351–352):
- E1 ☐ Save the answer body EXACTLY as produced to `body.md` (the answer text only — do not
  include the pasted prompt echo; C8's exactly-once marker check applies to `body.md`).
- E2 ☐ Write `meta.md`: model/product label as displayed, conversation URL (if any), UTC
  start/end, operator, approval reference, any "continue" events (R3), anomalies.
- E3 ☐ Verify the links ledger section exists in `body.md` (contract C7); if Gemini omitted
  it, that is a G8/C7 contract failure — do not reconstruct it yourself inside `body.md`;
  adjudicator notes may live in a separate file.
- E4 ☐ Custody receipt `CAPTURE_RECEIPT.md`: `wc -c` bytes + `shasum -a 256` for `body.md`,
  `meta.md`, and every other captured file. No adjudication on un-hashed text.
- E5 ☐ Captured files are immutable from this point; all scoring happens in a separate
  adjudication file that cites `body.md` line numbers.

Post-run adjudication (fail-closed order; BL §5):
- A1 ☐ Mechanical G1: `grep -c 'GEMINI_WEB_M3_RT_OUTPUT_DONE_REQ_M3_RT_20260711T091128Z' body.md`
  == 1 AND `awk 'NF{last=$0} END{print last}' body.md` prints the marker.
- A2 ☐ Mechanical G2 seed: `grep -inE 'establish(es|ed|ing)?\b|proves|proven|confirms that|settles|settled question|resolves the debate|definitively|conclusively|is now known' body.md`;
  triage each hit (own voice ⇒ fail; attributed quote with citation ⇒ acceptable).
- A3 ☐ Mechanical G8/C2: per card `grep -c '^### <N>\.' body.md` == 6 and `grep -c '^## Card ' body.md` == 6.
- A4 ☐ ID inventory (G5): list every DOI/arXiv/ADS ID → all marked
  `QUARANTINED_PENDING_LOCAL_CHECK`. Local lookups are a separate gated pass (P3R follow-up 4).
- A5 ☐ Fill scorecard B.1→B.2→B.3, stop-at-first-gate-failure; record B.4 summary + wholesale verdict.
- A6 ☐ Disposition regardless of verdict: leads (with citations) → Tori local-verification
  queue; NOTHING imported into wiki/product artifacts; no claim/cite binding; answer text is
  never evidence (BL L360–362; REQ safety locks).
- A7 ☐ File the adjudication + capture dir path + hashes back to the mastermind handoff area;
  reference this packet and BL by sha256.

---

## D. Precise diff summary — REQ r1 (b3488701…) → r2 candidate

r1 is 27 lines; every r1 line is accounted for below as kept-verbatim, modified, or replaced.
No deletion of any safety-relevant content; all three protocol safety locks kept verbatim.

| # | r1 location | Change in r2 | Justification (P3 findings) |
|---|---|---|---|
| D1 | L1 title, L3 protocol marker, L5 Request ID, L6 Method | Kept verbatim | Baseline citations (BL "REQ L…" refs) and the marker string embed this REQ ID; changing them would orphan BL/DP cross-references. |
| D2 | (new) after L5 | Added `**Revision:** r2 …` line naming drafting lane, adoption gate, and scope string | Custody discipline: adjudicator must be able to tell r1 from r2 by content, and P2 of checklist C pins the run to r2 by sha256; P3R records the r1 hash (`b3488701…`) as the cycle-7-era contract-gap version. |
| D3 | L7–9 artifact paths with `...` elision | Replaced elided prefix with both full absolute live paths + snapshot location + md sha256 `4f8e7fb0…` | P3R "Ambiguity 2": elided prefix forced P3 to resolve two candidate copies (found byte-identical). r2 removes the ambiguity and pins content by hash. |
| D4 | L11–12 "All 6 extracted research topic cards" | Kept the six-card ask; added the §0 mapping table (6 canonical cards ↔ CUR P1/P2/P3/absorbed/dropped/downgraded), the all-six-mandatory rule, and the editorial-not-scientific consolidation note | P3R "Ambiguity 1" + BL §0 (L28–48): REQ said six cards while pointing at a 3-proposal artifact — the prompt must carry the mapping so Gemini answers card-by-card (BL §4 bullet 2, L342–344). CHK-4.3/CHK-6.5 (BL L258–259, L325–327) motivate the editorial note. |
| D5 | L14–15 must-not-contradict | Kept anchors verbatim; added own-voice vs cited-disagreement clarification | BL §2 intro (L110–114) draws exactly this line; putting it in the prompt prevents Gemini from either contradicting the floor or suppressing genuinely disagreeing literature (which the ask wants as quarantined leads, BL L103–106). |
| D6 | L17–18 the two questions | Kept verbatim; appended the JWST/ALMA marginality note for cards 1 and 4 | BL §4 bullet 3 (L345–347): cards 1/4 are optical/X-ray/radio territory; "marginal here" must be a first-class answer to prevent padded relevance claims (BL L168–172, L264–267; DP L193–197). |
| D7 | L20–21 expected output shape (one sentence) | Expanded into binding output contract C1–C8; the six fields of the r1 sentence became the six per-card sections of C2 in the same order | The core P3 finding: "REQ defines no completion-marker string, no capture/meta contract, and no per-card section ordering — exactly the failure surface that rejected cycle-7" (P3R L48–51; BL §4 L337–341; CY7 rejection reasons per BL L54–58). C1 meta ← capture/meta gap; C2 ordering ← G8 (BL L97–101); C3 `NONE_FOUND` ← VER satisfiable-contract device (BL L100–101); C4 ← G3 (BL L76–79); C5 ← G2 (BL L67–75); C6 ← G4 + four-qualifier rule (BL L80–85, L192–194); C7 ← cycle-7 capture set "body, meta, links ledger" (BL L351–352); C8 ← G1 with BL's recommended marker string verbatim (BL L60–66). |
| D8 | (new) | Added OPERATOR-SIDE adjudication-reference block (baseline path+sha256, gate/floor/verdict vocabulary, wholesale rule, advisory ceiling) | Makes the run cheap to adjudicate (rollup follow-up item 2; P3R follow-up 1–2). Marked operator-side so the pasted prompt stays clean; scoring rules come from BL §5 (L349–363). |
| D9 | L23–27 safety locks | Kept verbatim, unchanged, still labeled "copied from protocol" | G5/G6/G7 (BL L86–96) adjudicate directly against these lock sentences; altering them would decouple prompt from baseline. |

Net effect: every cycle-7 structural killer named in the P3 cross-card note — estimand
conflation, settled-verb register, marker placement, unlabeled uncited leads (DP L302–310) —
is now pre-empted in the prompt itself (C6, C5, C8, C4 respectively), not only in the
adjudicator's checklist.

---

## E. Stretch — failure-mode playbook (reject-if trigger → operator response)

Standing rules inherited from BL: a global-gate failure means NO further sidecar submission
for this packet without a fresh user-approved brief (BL L54–58); leads with citations are
retained as quarantined input to the Tori queue in every outcome (BL L353–354); "re-prompt"
below therefore always means "a NEW gated run under a fresh Duho-approved brief", never an
in-conversation retry (sole exception: the single logged neutral "continue" of C/R3).

| Trigger | Detection | Operator response |
|---|---|---|
| G1 marker absent / duplicated / not final body line | A1 grep/awk | Wholesale REJECT. Complete custody (E1–E4) anyway; harvest cited leads → quarantine queue; escalate to Duho with the capture receipt. If the marker sits in the chat UI but not the body, record that explicitly — it is the cycle-7 signature failure and proves the contract text was ignored, so the fresh brief should tighten nothing except delivery emphasis. |
| G2 banned register in own voice | A2 grep + triage | Wholesale REJECT (contract breach class). Keep the triage table (hit line, own-voice vs attributed) in the adjudication file so the fresh brief can quote the exact violations. |
| G2 hit inside an attributed quote with citation | A2 triage | Not a failure. Mark hit `ATTRIBUTED_OK` with the citation; no action. |
| G3 unlabeled uncited lead(s) | per-card sweep + C7 ledger cross-check | Gate failure ⇒ wholesale REJECT. Before escalation, count them: if the ledger exists and only isolated in-text lines lack labels, note "labeling drift" vs "systemic" in the escalation — it changes how the fresh brief weights C4. Leads WITH citations still go to quarantine. |
| G4 non-commensurable comparison unlabeled | manual | Gate failure ⇒ wholesale REJECT; quote each conflation with line refs (Gatto/Gawade-class evidence for the escalation). |
| G5 ID presented as verified | A4 inventory | Relabel to `QUARANTINED_PENDING_LOCAL_CHECK` in the adjudication file (never edit `body.md`); if the answer's own text insists IDs are verified ⇒ G5 gate failure ⇒ wholesale REJECT. |
| G5 ≥3 IDs fail local lookup (later Tori pass) | gated verification pass | Retroactive wholesale REJECT of the answer as a source of anything but already-verified leads; record fabricated-ID count; escalate — pattern of invention voids the run. |
| G6 numeric import pressure ("replace local value X") | manual | Gate failure ⇒ wholesale REJECT of that guidance; under no verdict do numbers enter local artifacts without the separate verification pass. |
| G7 manuscript prose / edit instructions / binding suggestions | manual | Gate failure ⇒ wholesale REJECT; explicitly do NOT paste any of it anywhere, including "just the harmless parts". |
| G8/C2 card missing a field silently | A3 grep | That card ⇒ FAIL (not wholesale by itself). <3 such cards: score the rest normally; ≥3: wholesale. Record which fields — if the same field dies across cards (e.g., realism), the fresh brief should strengthen that field's instruction, not the whole contract. |
| C3 padding instead of `NONE_FOUND` | per-card read | Not an automatic gate hit; score the padded field's content on its merits (padding usually trips CHK realism/citation items — e.g., forced JWST/ALMA relevance on cards 1/4, BL L168–172, L264–267). Note padding in the card verdict. |
| Floor F1–F5 breach in a card | B.2/B.3 rows | That card ⇒ FAIL; harvest its cited leads; ≥3 card FAILs ⇒ wholesale (BL L108). F4 breaches: additionally re-check that the open repair items (claims `2915/2921/2913`, `2133`, `2374`) are still open before scoring — if a repair landed since, the floor item is stale and the breach is void (record either way). |
| Card `NOT_ADDRESSED` | B.3 | Score it `NOT_ADDRESSED`; the answer cannot be called complete for REQ (BL L38–39). 1–2 missing: accept the rest as advisory, queue a follow-up ask covering the gap cards in the next fresh brief; all-or-most missing: treat as contract failure of C2 ⇒ escalate. |
| Truncated generation | operator observation | One neutral logged "continue" (C/R3). Still truncated ⇒ capture what exists, mark PARTIAL in `meta.md`; G1 will fail mechanically ⇒ wholesale path with truncation noted as cause (distinct from contract defiance in the escalation). |
| Gemini requests actions/browsing beyond text | operator observation | Decline, log in `meta.md`, continue watching. If it refuses to complete without it, stop, capture, PARTIAL, escalate. |
| Live REQ ≠ adopted r2 at P2, or BL hash mismatch at P3 | pre-run hashes | Do not launch. Escalate to Hwao/Duho; a run against r1 re-creates the cycle-7 failure surface by construction. |

---

Produced by hard-burn lane H2, 2026-07-11. Inputs, hashes, poll log, and safety attestation:
`H2_RECEIPT.md` alongside this file.

FABLE_HARD_BURN_H2_REQ_CONTRACT_20260711T035354Z
