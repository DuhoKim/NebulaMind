# HWAO_ONE_CANARY_PLAN — one supervised Deep Research canary: the Section-2 comparability cluster

Packet: `gemini-dr-content-expert-gate-20260713T160239Z` · Status: PLAN — **NOT ARMED**. Hwao is plan/contract author only; Tori is sole browser owner; no browser/network action occurs in this pass. All hard boundaries of `USER_DIRECTION_AND_BOUNDARIES.md` bind verbatim.

## 1. Content target and why it is the highest-value first canary

**Target: the eight-entry comparability cluster M066–M073** — the eight Section-2 validation rows whose `MATCHED_SELECTIONS` tokens are all uncorroborated (`AMBIGUOUS_NEEDS_EXPERT`, 8/8), **plus** the row-level citation-quality corrections that Gate B surfaced inside the same eight rows (row 1 cites an aggregator page; row 4 cites a project blog page; rows 7–8 share one citation, a probable mis-attribution).

Why this beats the alternatives: (a) it is **load-bearing for r3 C6** — the semantic comparability layer is the one device the whole mechanical program deliberately cannot judge, and a future r3 run exercises exactly it; (b) it is **content truth, not validator mechanics** — the question is whether each simulation-observation comparison actually used commensurable selections, answerable only from primary literature; (c) it is **bounded**: exactly 8 rows, 7 unique current sources, a closed output schema; (d) it is **DR-shaped**: selection functions are stated in methods sections across pairs of papers — precisely what Deep Research retrieves well; (e) it **cannot contaminate** settled work: no overlap with contaminated indices 1/3/4, no nine-H2 structure content, advisory-only. Rejected alternatives: M018 (one unresolved citation — low leverage), M023 sizes clause (single clause, local expert task), the 25 source-fidelity ambiguities (heterogeneous, full-text-reading work, poorly bounded), M064/M065 (document-level, unbounded).

## 2. Exact input records (completed Gate B packet `../gemini-dr-c1r-manual-source-verification-20260713T034742Z`, read-only)

- `verification/VERDICTS.jsonl` (sha256 `a4821a54806088c977289d1e7ce103d4deb67b32eee7a573754d68874ba17b3f`) — records M066–M073 incl. both `semantic_comparability_assessment` notes.
- `sources/ROUTE_MAP.json` (`1fb3165d7e884f535f42b2271273f34f98ecea1f76d5028576ba8e43987d4442`) and `sources/SOURCE_INDEX_MAP.json` (`5b56a549bdcfb36fe7a748105e31d2671f0b49d70bb85ec389b80090228958cf`) — row→source-index routing: rows 1–8 cite indices 27, 28, 10, 11, 15, 20, 30, 30.
- `sources/EVIDENCE_CATALOG.json` (`71de81290f4c21298eda170fdf12f6cdb9529344a9d1590144849028facbfc6b`) + `sources/text/idx{10,11,15,20,27,28,30}_*` — already-fetched local texts for cross-checking the answer offline.
- Sealed S2 row claims: `…/gemini-dr-revised-canary-20260712T045317Z/runs/c1r/body.md` (`8a130c5a…bc00`) lines 190–204.
- Suspect flags of record: `HWAO_ROOT_CAUSE.md` §3.5 (idx-27 aggregator; rows 7–8 shared chip 30) and Gate B `receipts/HWAO_SAMPLE_REVIEW.md` (M072).

## 3. Paste-ready prompt and structured answer contract

Goru freezes the block below as `prompt/GE_COMPARABILITY_CANARY.md`, records sha256, and verifies paste-equality at preflight. Tori pastes EXACTLY this text between the sentinels (sentinels excluded), nothing else, no follow-up steering (one neutral logged "continue" permitted on visible truncation).

-----BEGIN PASTE GE_COMPARABILITY_CANARY_20260713T160239Z-----
# Deep Research request — Selection commensurability of eight simulation-observation comparisons (Galaxy Evolution)

Request ID: REQ_GE_COMPARABILITY_20260713T160239Z

Role: You are a literature analyst for a galaxy-evolution research journal. Report only published work; you have no access to the journal's internal results.

Question: For each numbered comparison below, determine from the PRIMARY published literature: (a) the sample-selection function used on the simulation side of the claimed comparison; (b) the observational comparator actually used and its selection function; (c) whether the two selections are commensurable ("matched") as published; and (d) the correct PRIMARY peer-reviewed reference(s) for the comparison where the listed current source is an aggregator page, a project/blog page, or appears mis-attributed.

The eight comparisons (simulation | observable | claimed result | currently listed source):
1. IllustrisTNG | galaxy color bimodality distribution | agreement (sharp blue-to-red transition near M*≈10^10.5 M_sun) | https://oamonitor.ireland.openaire.eu/national/search/publication?pid=10.1093%2Fmnras%2Fstx3040 (aggregator — identify the primary paper)
2. EAGLE | specific star-formation rate vs stellar mass at intermediate redshift | tension (simulated relation steeper; observed normalisation higher at z≈1–2) | https://www.cambridge.org/core/journals/publications-of-the-astronomical-society-of-australia/article/relation-between-starformation-rate-and-stellar-mass-of-galaxies-at-z-14/2AAB84B2524F5870838E5BCC736A18DC
3. SIMBA | molecular gas mass distributions | tension (overproduces H2 mass fractions while matching the stellar mass function) | https://academic.oup.com/mnras/article/497/1/146/5866845
4. FIRE/FIRE-2 | visual morphologies and central mass concentrations in massive galaxies | agreement (convergence with resolution; central concentrations sensitive to wind recycling) | https://fire.northwestern.edu/2017/03/21/fire-2-simulations-physics-versus-numerics-in-galaxy-formation/ (project page — identify the primary paper)
5. ROMULUS | dual active-galactic-nucleus frequency | agreement (dual-AGN demographics vs larger contexts) | https://arxiv.org/abs/1607.02151
6. ASTRID | supermassive black hole mass and luminosity functions | agreement (broadly consistent constraints, notably before z=3) | https://arxiv.org/abs/2110.14154
7. FLAMINGO | kinetic Sunyaev-Zel'dovich effect of SDSS BOSS galaxies | tension (Planck/ACT stacking prefers stronger feedback than fiducial calibration) | https://arxiv.org/abs/2410.19905
8. BAHAMAS | cosmic shear and matter power spectrum clustering | tension (S8-resolving feedback strengths disagree with X-ray cluster gas fractions) | https://arxiv.org/abs/2410.19905 (same source as item 7 — verify whether this reference actually covers BAHAMAS, and if not identify the correct primary reference)

OUTPUT DISCIPLINE (binding): the report body is STRUCTURED ONLY, in this exact sequence: (a) the 4-line meta header; (b) Section 1 table; (c) Section 2 bullets; (d) the Links ledger; (e) the final completion-marker line, alone. Nothing else — no abstract, introduction, summary, or free narrative outside table cells, bullets, ledger lines, and the marker line.

Meta header (first 4 lines, exactly):
    # GE comparability canary — REQ_GE_COMPARABILITY_20260713T160239Z
    Run date (UTC): <YYYY-MM-DDTHH:MM:SSZ>
    Model: Gemini Pro (selected UI mode; backend version not exposed)
    Rows covered: <N> of 8
Emit the Model line verbatim; do not substitute a version number.

## 1. Selection commensurability ledger — Markdown table, one row per comparison, exactly these columns:
| Row | Simulation | Simulation-side selection (as stated, same-cell citation) | Observational comparator + selection (as stated, same-cell citation) | SELECTION_MATCH | Basis (≤2 sentences, same-cell citation) |
The SELECTION_MATCH cell contains exactly one token: MATCHED_SELECTIONS_CONFIRMED, PARTIALLY_MATCHED, UNMATCHED_SELECTIONS, or INDETERMINATE_FROM_PUBLISHED_SOURCES. Every claim-bearing cell carries its OWN checkable citation (arXiv ID, DOI, ADS bibcode, or URL) or UNCITED_NOT_USABLE; a citation in one cell does not cover another. An empty field is exactly NONE_FOUND.

## 2. Primary-source corrections — bullets only; one bullet per row whose listed current source is not the primary peer-reviewed source of the claimed comparison (at minimum evaluate rows 1, 4, 7, 8): "Row <N>: correct primary reference(s) = <citation(s)>; the listed source is <aggregator page | project page | mis-attributed — actually covers <what>>." Same-bullet citations mandatory.

## Links ledger — one line per unique cited source: <short name, non-empty> | <citation> | QUARANTINED_PENDING_LOCAL_CHECK. Bidirectional and unique: every inline citation appears exactly once here; every ledger row is cited inline at least once; no duplicates; no blank short names.

Wording contract: in your own voice the settled/causal register is BANNED (case-insensitive): establish/establishes/established/establishing, proves, proven, confirms that, settles, settled question, resolves the debate, definitively, conclusively, is now known, "demonstrates that … causes". A source's claim in that register appears only as an attributed quote with a checkable citation. Every quoted scientific number carries the source's uncertainty in the same cell OR the label UNCERTAINTY_NOT_QUOTED_BY_SOURCE (citation identifiers, section numbers, and the header row count are exempt). Any quoted numeric fraction or incidence carries, in the same cell: TRACER=<...>; SELECTION=<...>; DENOMINATOR=<...>; REDSHIFT=<...> (use NOT_APPLICABLE per qualifier as needed).

Safety locks: output is advisory only — not accepted evidence, not product-claim binding; do not present generated DOI/ADS/arXiv IDs as verified (all are quarantined pending local check); do not propose edits to any local artifact.

The last non-empty line of the report must be exactly the completion marker below, with nothing after it:
GEMINI_WEB_GE_COMPARABILITY_CANARY_DONE_20260713T160239Z
-----END PASTE GE_COMPARABILITY_CANARY_20260713T160239Z-----

## 4. Completion marker and validation clauses

Marker: `GEMINI_WEB_GE_COMPARABILITY_CANARY_DONE_20260713T160239Z` — exactly once, standalone final non-empty body line (chat-UI-only marker = ABSENT ⇒ reject). Validation clauses, fail-closed, executed offline on the capture: **V1** marker once/final; **V2** meta header exact incl. verbatim Model line; **V3** Section-1 table has all 8 rows, each SELECTION_MATCH cell exactly one vocabulary token; **V4** every claim-bearing cell cited (literal ID/URL, or resolved citation chip captured per V9) or `UNCITED_NOT_USABLE`; **V5** ledger bidirectional, unique, non-empty short names; **V6** zero own-voice banned-register hits; **V7** quoted numbers carry uncertainty token; quoted numeric fractions carry the four-qualifier syntax; **V8** no content outside allowed units; **V9** capture via the accepted Gate A chip-aware `structured_capture_v3.js` (sha256 `dd2a96707bc47456bbfc9383b384a164e1d86c7e8933b707a4ad22fa4d3fa924`), chip→URL map recovered fail-closed. Any V-clause failure ⇒ run rejected as evidence (leads still quarantine-harvested); no retry.

## 5. Custody: single tab, single browser owner

Tori is the SOLE browser owner: one browser, one profile, one tab, one conversation; exact tab identity (conversation URL) recorded in `runs/canary/meta.md` before submission and re-verified before capture; no concurrent drivers, duplicate tabs, second submissions, or retries. Hwao/Goru/Lana/Kun perform zero browser actions. Prompt custody: Goru's frozen file sha256 must equal the composer-normalized paste hash Tori records pre-submit.

## 6. Deep Research mode and best-model / max-thinking checks

Before submit, Tori verifies and screenshots: Deep Research mode selected; the highest available model tier for the account (precedent: "Gemini Pro"); any extended-thinking/effort control at maximum if the UI surfaces one; records the exact UI labels in `meta.md`. Wrong mode or model ⇒ NOT_ARMED stop (no adjustment-and-proceed).

## 7. Quota evidence and hard-stop thresholds

Pre-flight and post-run screenshots of the account usage surface into `runs/canary/screenshots/` with values recorded in `meta.md` (last observed baseline: 3% used, reset Jul 14). Hard stops — abort NOT_ARMED (pre-submit) or capture-partial + VOID (mid-run): usage ≥80%; any billing/upsell interstitial; account-verification or unusual-traffic challenge; CAPTCHA; login wall; model/mode mismatch; tab-identity doubt; operator doubt of any kind. No quota purchase, no account/OAuth action, ever.

## 8. Plan-ready / start ownership

Plan-ready = Hwao (this file + its end marker). Preflight = Goru, local-only: freeze prompt file + sha256, schema/token-vocabulary lint, marker-string uniqueness check against all packet files, expected-capture checklist → `GORU_PREFLIGHT_GREEN_20260713T160239Z` or NOT_GREEN. Arming decision = per §11. Start = **Tori alone**, only after (a) Goru GREEN, (b) arming condition met, (c) Tori's own custody checks GREEN; Tori writes `TORI_ARMED_20260713T160239Z` immediately before submission. Lana and Kun are explicitly included: Lana reviews the ANSWER's content/method quality post-capture (advisory, no browser); Kun reruns V1–V9 reproducibly and audits custody (no browser).

## 9. Capture and validator artifacts (all under this packet, `runs/canary/`)

`body.md` (exact innerText, no prompt echo) · `rendered_body.html` (DOM) · `structured_capture_v3.json` (V9 capture) · `validation_result.json` + `VALIDATION_CHECKLIST.md` (V1–V8 outcomes with evidence refs) · `meta.md` (conversation URL, UTC start/end, operator, mode/model labels, quota pre/post, continue events, anomalies) · `screenshots/` · `CAPTURE_RECEIPT.md` (bytes + sha256 of every captured file; capture immutable thereafter) · `RUN_RECEIPT.json` (terminal state) · exactly one of `CANARY_CAPTURED_20260713T160239Z` / `CANARY_VOID_20260713T160239Z`. Post-run order: Kun validation rerun → Lana content review (`LANA_CONTENT_REVIEW.md`: per-row assessment of the 8 verdicts against the local Gate B evidence texts; expert-queue disposition recommendations) → Hwao synthesis. Answer content is ADVISORY ONLY: it feeds the expert queue; it never auto-updates verdicts, prose, wiki, trust, or the 73-entry ledger — any application is a separate future gate.

## 10. Fail-closed stops and no-retry

One canary, one conversation, ever, under this packet. Any §7 trigger, prompt-hash mismatch, paste anomaly, mid-run local-file edit, second-tab temptation, or capture-set incompleteness ⇒ stop, capture what exists, write `CANARY_VOID_…` with reason, report to Duho. A VOID or rejected run is NOT retried under this packet; any fresh attempt needs a new packet and fresh user gate. No API fallback, no alternate profile, no parallel research.

## 11. Arming recommendation

**The user's direction is sufficient to arm after a clean preflight — no additional approval round-trip is needed**, on these grounds: the direction ("for the content use Deep Research") explicitly approves one supervised content canary and this packet's boundaries anticipate arming "after clean preflight, absent account verification or operator doubt"; precedent (the C1r run) armed on equivalent specificity. Binding conditions: arming occurs ONLY if Goru preflight is GREEN, Tori's custody/mode/model/quota checks are all GREEN, and zero §7 triggers are present — **any** exception, including bare operator doubt, means NOT_ARMED and a report back to Duho instead. This recommendation arms nothing by itself; Tori owns the start per §8, and this pass performs no browser or network action.

HWAO_CONTENT_DR_ONE_CANARY_PLAN_DONE
