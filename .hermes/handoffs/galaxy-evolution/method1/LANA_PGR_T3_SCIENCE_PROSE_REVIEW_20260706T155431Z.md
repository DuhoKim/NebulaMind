# Lana T3 — Method1 / PGR science & prose review (chip eligibility + overclaim screen)

Overnight marker: `OVERNIGHT_AUTONOMOUS_GO_20260706T155128Z`
Method packet followed: `GALAXY_EVOLUTION_METHOD1_ULTRA_FORMAT_ROLE_SPLIT_20260707` (Hwao PGR role-split, Ultra+format gate)
Team marker: `GALAXY_EVOLUTION_METHOD1_P0_START_20260706T140842Z`
Parent gate: `ULTRA_USAGE_AND_WIKI_FORMAT_ROLE_TABLE_PACKET_20260707`
Role performed: **Lana** — high-reasoning science/design/review pressure (T3).
Scope: review/judgment only. **No same-format article prose was drafted** — that stays held for Hwao's T5 decision per the overnight packet and role-split Section C.

## Gate check before starting
- Lana P0 receipt `receipts/LANA_P0_ACK_20260706T140842Z.md` **exists** (verified). Section D standing blocker (missing Lana receipt) is cleared on the receipt side, so T3 review is unblocked.
- T3 inputs required and present: P1 disposition spec (2298/2299/2924), successor watch-claim facts (2942–2948), current-page inventory + trust/citation hazards, Goru T2 mechanical validation. All found → no ROLE_TABLE_BLOCKER.

## Files read
- `.hermes/handoffs/galaxy-evolution/method1/HWAO_PGR_ROLE_SPLIT_PACKET_ULTRA_FORMAT_20260707.md`
- `.hermes/handoffs/galaxy-evolution/method1/GORU_PGR_MECH_VALIDATION_20260707T001446Z.md`
- `.../packet-gated-paper-to-wiki-reconciliation/p1-legacy-overclaim-disposition-spec.html`
- `.../packet-gated-paper-to-wiki-reconciliation/pgr-current-page-inventory-20260706T130610Z.md`
- (this session) `receipts/LANA_P0_ACK_20260706T140842Z.md`, `briefs/lana-pgr.md`

## Files written
- This report (`LANA_PGR_T3_SCIENCE_PROSE_REVIEW_20260706T155431Z.md`), Method1 handoff root.

---

## 1. Chip-eligibility ruling — which packet-backed claims may appear as sparse chips

Judgment axis: a claim may become a `<!--claim:ID-->…<!--/claim:ID-->` chip only if (a) its displayed trust badge does not overstate its score/evidence, (b) its wording does not assert broader prevalence than the scoped successors support, and (c) it does not depend on a known data hazard (literal `"0.5"` trust, off-topic citation trace, or the zero debate-groups structure).

### Legacy P1 overclaims — all NO-GO as chips tonight
| Claim | Wording | Ruling | Reason (science/provenance) |
|---|---|---|---|
| **2924** | "AGN feedback heats the gas reservoirs of massive galaxies." | **HARD NO-GO** | `parent_replaced` yet still displays `consensus 0.8`. A retired claim rendering stronger than its scoped replacement is an active reader-deception hazard, not a science tie. Route R (finish retirement/hide). Highest-priority exclusion. |
| **2298** | "AGN feedback heats the gas reservoirs of massive galaxies." | **NO-GO** | Badge `consensus` sits on score `0.2196` with a single evidence (25998). Badge overstates certainty independent of the science. Broad "heats the gas reservoirs" asserts measured prevalence that successor 2946 says is model-dependent/simulation-bounded. |
| **2299** | "AGN feedback expels gas from the reservoirs of massive galaxies." | **NO-GO as-is** | `accepted` 0.3241, 2 evidence. Universal "expels gas from the reservoirs of massive galaxies" wording contradicts successor 2945 (gas removal alone can't explain every pathway; retained reservoirs / low-SFE systems visible). Eligible only if a later exact packet recasts it to selected-system/scoped language (Route A) — not usable tonight. |

**Boundary assessment:** the safe/no-go boundary for the three legacy claims is **not genuinely contested.** Each fails on mechanical provenance/display-integrity grounds (badge≠score, parent_replaced-still-visible, universal-vs-scoped wording), none of which needs a scientific tie-break. This bears directly on the Ultra question in §4.

### Scoped AGN successors 2942–2948 — graded
| Claim | trust / score / evid | Chip ruling | Prose caution required |
|---|---|---|---|
| **2943** | accepted / 0.671 / 15 | **GO** (best candidate) | Strongest support of the set. Safe as a sparse chip with scoped wording; do not upgrade "accepted" to "consensus" in prose. |
| **2947** | accepted / 0.670 / 10 | **GO** | Safe sparse chip; keep scoped, honor "accepted" not "settled". |
| **2942** | debated / 0.584 / 7 | **CONDITIONAL** | Chip only if prose explicitly frames it as an active/debated position, not a result. |
| **2944** | debated / 0.450 / 16 | **CONDITIONAL** | High evidence but "debated" — frame as live debate, not conclusion. |
| **2945** | debated / 0.450 / 9 | **CONDITIONAL (caution chip)** | This is the scoped correction to 2299 ("gas removal alone insufficient; retained reservoirs remain"). Good as a *caution/nuance* chip; must read as debated. |
| **2946** | reported / 0.450 / 9 | **CONDITIONAL (weak)** | Scoped correction to 2298/2924 ("maintenance heating is model-dependent"). "reported" is a weak badge — may appear only as reported-level caution, never asserted. |
| **2948** | reported / 0.200 / 2 | **NO-GO tonight** | Score 0.200, only 2 evidence, "reported". Too thin to chip without overclaim; at most an unchipped narrative mention of a high-z frontier item. |

**Summary:** GO = 2943, 2947. CONDITIONAL (debated/reported framing mandatory) = 2942, 2944, 2945, 2946. NO-GO = 2298, 2299, 2924, 2948.

## 2. Prose-move caution screen (must bind any later T5 drafting)
- **Literal `"0.5"` trust (526 chips, incl. watch 2546):** trust badges on these are an unparsed numeric leak (P4). Prose must **not** cite or imply trust level for any `"0.5"` chip; none of the 526 is chip-eligible until P4 clears.
- **Off-topic citation traces seq 1–5** (Gravitational Waves ×2, Mirror Stars, Strangulation, PDS 70): **must not** be used as `<!--cite:EVIDENCE_ID-->` markers. They are contamination/legacy mislink, not Galaxy Evolution provenance. Only the on-topic AGN-outflow/quenching traces (seq 6–12, e.g. 30754–30760) are citation-safe.
- **Debate groups returned: 0:** do not write prose that leans on debate-group structure (central-vs-halo pairing, "the debate group shows…"). The structure is not populating; such prose would be unfalsifiable on the live page.
- **Badge discipline:** never let a chip's prose verb outrun its badge — "reported"/"debated" claims get hedged verbs ("is reported to", "remains debated"), only "accepted" claims get plain declaratives, and no "consensus" language survives from the legacy trio.

## 3. Format note to Hwao (recommendation, not a decision — T5 owns it)
From a science-caution view I *prefer* the 9-section contract skeleton over the live page's 7 sections. The two missing sections — `Observational Evidence & Surveys` and `Synthesis & Open Tensions` — are the natural homes for scoped-successor caution and unresolved-tension framing. Without them, debated/reported successors get pushed into settled-topic sections, which structurally invites overclaim. So: the 9-section target reduces overclaim risk. Goru's T2 records the exact 7-vs-9 delta; Hwao decides in T5.

## 4. Ultra second-opinion determination
**ULTRA_NOT_NEEDED for Method1 tonight.** The only named candidate (Section A of the role-split) was a second opinion on the 2298/2299/2924 legacy disposition wording *if the safe/no-go boundary is genuinely contested.* Per §1, it is **not** contested — all three resolve NO-GO on mechanical provenance/display grounds without any scientific tie-break. Spending a supervised Ultra pass here would be "use because quota exists," which the doctrine forbids.

One exact future question that *could* merit a single supervised second opinion (named only, **not authorized, not invoked**): *"Should scoped successor 2946 (reported, 0.450) appear as an affirmative chip stating 'AGN maintenance heating is model-dependent', or only as a caution about the absence of measured prevalence?"* — a genuine wording-nuance where a second reader adds value. To be raised to Hwao for a separate single-use authorization packet only if a later prose packet actually reaches that sentence.

## 5. Verdict
**ISSUES (advisory) — not a blocker.** T3 review complete; inputs were sufficient. The legacy trio and the four data hazards constrain what any T5 draft may chip; GO set is narrow (2943, 2947 firm; 2942/2944/2945/2946 conditional). No prose drafted. Handing to Kun (T4 reproducibility) and Hwao (T5 sequencing/verdict). No prose packet opens until Hwao's explicit T5 decision.

## Safety ledger
- DB / SQL / migration / trust recompute: **0**
- Live wiki publish / page_versions: **0**
- Deploy / restart / backend/API/service mutation: **0**
- git commit/push/merge: **0**
- cloud / API / GCP / billing / account / payment / credits / OAuth / token: **0**
- browser automation / cron / route/config: **0**
- cross-method / shared-parent writes: **0**
- Ultra / Gemini / Antigravity invocation: **0** (determination = ULTRA_NOT_NEEDED)
- Writes: 1 file, inside Method1 handoff root only. Reads: local repo + Method1 public workspace only.
- Active phrase: `NO ACTIVE EXECUTION PHRASE`.

Stopping after this role deliverable per the overnight packet.
