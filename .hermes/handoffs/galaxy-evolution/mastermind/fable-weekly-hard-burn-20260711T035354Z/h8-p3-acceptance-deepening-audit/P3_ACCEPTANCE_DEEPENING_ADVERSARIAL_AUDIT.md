FABLE_HARD_BURN_H8_P3_AUDIT_20260711T035354Z

# Adversarial audit — P3 M3 acceptance baseline + RT-card deepening packet

Auditor: Fable lane H8, hard burn `fable-weekly-hard-burn-20260711T035354Z`. Audit window
2026-07-11T04:13:19Z → 04:4xZ. Method: documents-only, zero network, zero writes outside
`h8-p3-acceptance-deepening-audit/`. Every input verified against its pinned sha256 before
use (all matched — see `H8_RECEIPT.md`). All line numbers below refer to the pinned files;
source line refs (REQ/EB/SC/CUR/CY7/VER) refer to the byte-identical `sources-snapshot/`
copies (identity recomputed and confirmed).

**Packet verdict: PASS-WITH-FIXES.**
Custody is perfect (every hash and byte count re-verified, 0 mismatches). Every substantive
scientific/status claim I checked traces correctly to the snapshotted sources — axis
statuses, the 17%/46% anchors, all trust-level counts, claim/ledger IDs, arXiv IDs, the
consolidation lineage, and the cycle-7 lesson. The defects found are: one MAJOR
adjudication gap (no packet-level verdict rule for partial coverage / 1–2 card FAILs), ten
MINOR correctable citation/decidability defects, and eight NOTEs. Nothing rises to BLOCKER;
none of the defects poisons the baseline's floors or checks, but the MAJOR item should be
fixed before the gated sidecar run is adjudicated against this packet.

Files audited (pinned):
- `M3_ACCEPTANCE_BASELINE.md` (BASE) — 26082 B, `d028f3c7…91d433` ✓
- `RT_CARDS_DEEPENING.md` (DEEP) — 19686 B, `21564dd6…eed7e18` ✓
- `P3_RECEIPT.md` (RCPT) — 10475 B, `70573e18…ecd90b` ✓

---

## 1. Findings table (severity-ordered)

| ID | Sev | Where (file:line, quote) | Why wrong | Proposed disposition |
|---|---|---|---|---|
| H8-F01 | MAJOR | BASE:36–39 "any card the answer does not address at all is scored `NOT_ADDRESSED` (not a protocol breach…)"; BASE:349–362 (§5) | The packet-level outcome space is incomplete: wholesale REJECT triggers are defined (any gate failure, ≥3 card FAILs, ≥3 fabricated IDs) and per-card verdicts are defined, but no ACCEPT condition is ever stated. An answer addressing only 1–2 cards, or with 1–2 card FAILs, trips no wholesale trigger and has no defined packet verdict; "cannot be called complete for REQ" carries no verdict consequence. Adjudicator discretion at verdict time is exactly what this baseline exists to remove. | Add an explicit packet rule, e.g.: `ACCEPT_ADVISORY` iff all gates pass AND 0 card FAIL AND ≥5 of 6 cards addressed; `PARTIAL_ADVISORY_LEADS_ONLY` iff all gates pass but coverage/FAIL below that; else wholesale REJECT per §5.4. |
| H8-F02 | MINOR | BASE:63–66 "REQ defines no marker string (gap — see §4); the future prompt MUST define one." | G1 is undecidable if the future prompt author ignores §4: with no marker defined, "must appear exactly once" has no operand, and the gate can neither pass nor fail. No fail-closed default is stated. | Add to G1: "If the run prompt defines no marker string, the run is invalid — do not submit; if submitted anyway, G1 = FAIL by definition." |
| H8-F03 | MINOR | BASE:92 "(REQ safety lock L27)"; BASE:87 "(REQ safety lock L25–26)" | Off-by-one citations. REQ (snapshot, 26 lines + trailing newline — recount confirmed) has the numeric-import lock at L26 ("Do not import numeric results unless supported."); **REQ L27 does not exist**. The ID-quarantine lock is L25 alone; "L25–26" over-spans into the numeric lock. | G5 → cite REQ L25; G6 → cite REQ L26. |
| H8-F04 | MINOR | BASE:84–85 "(VER blocking facts 4–5: the Gatto and Gawade-class conflations…)" | Mislabelled evidence. VER blocking fact 4 is the Gatto estimand conflation ✓, but VER blocking fact 5 is the **Ellison −0.06 vs −0.12 dex misquote**, not a Gawade-class conflation. The Gawade absolute-estimand lesson lives in CY7 retained-leads (CY7:55 "a different absolute estimand") and VER fact 7 context. BASE's own CHK-3.3 (BASE:232–234) cites it correctly. | G4 → cite "VER blocking fact 4 + CY7 retained-leads Gawade note". |
| H8-F05 | MINOR | BASE:86–89 (G5) "an ID that fails local lookup… ≥3 failures ⇒ wholesale REJECT" vs BASE:353–354 (§5.2) "stop at first failure" | Temporal undecidability: at gate-pass time every ID is `QUARANTINED_PENDING_LOCAL_CHECK` and the local-lookup pass is itself gated (RCPT follow-up item 4). The ≥3-failure wholesale trigger therefore cannot fire during the mechanical gate pass — a gate-clean ACCEPT can be flipped retroactively, and the protocol never says the verdict is provisional. | State in §5: "Verdict is PROVISIONAL until the gated ID-verification pass completes; ≥3 lookup failures then retroactively collapse it to wholesale REJECT." |
| H8-F06 | MINOR | BASE:90–92 (G6) "none may be imported into any local artifact unless supported after local verification" | Unfalsifiable against the object under test: import behaviour is a constraint on local actors, not a property of the answer text, so this clause can never be scored FAIL on the answer. Only the second clause ("presented by the answer as corrections/replacements of local ledger values") is answer-scoreable. | Reword G6 to the answer-scoreable clause; move the import ban to §5.5 (ceiling), where it already effectively lives. |
| H8-F07 | MINOR | BASE:67–75 (G2) vs BASE:123–124 (F2 "non-AGN channels are established (EB L15)"), BASE:154 (card-1 floor-3 "are established required context") | Register collision: the floor's own wording uses the banned verb (inherited from EB:15 "non-AGN channels are established" and SC:14). An answer that echoes the floor/EB wording verbatim — i.e. *agrees* with the local basis — trips G2 unless the attribution exception is stretched beyond its "Author (year)" wording. | Add a G2 carve-out: restating a local axis status is legal only in status vocabulary (`widely_supported`) or with explicit EB attribution; floor echo ≠ violation. |
| H8-F08 | MINOR | BASE:134–136 (F5 "must actually appear at the cited EB anchor (`#s2`–`#s8`)") vs BASE:154–155 (card-1 floor-3 cites "EB `#s1` claim `2931`") | Anchor-range gap: F5's attribution-integrity check is scoped to #s2–#s8 (REQ's range), but the baseline's own card-1 floor rests on **#s1**. A sidecar misattribution to #s1 escapes F5 as written. | Extend F5 to "#s1–#s9 (any anchor this baseline cites)". |
| H8-F09 | MINOR | DEEP:115 "claims `2905–2911, 2930`" vs BASE:215–216 and EB:46 "claims `2905, 2906, 2909, 2911, 2907, 2930`" | Range notation over-claims: "2905–2911" includes **2908** — which is an EB §5 *environment* claim (EB:55), not a §3 reservoir claim — and **2910**, which appears nowhere in EB. The baseline's enumeration is correct; the deepening's compression silently changes the claim set an adjudicator would anchor-check. | Replace the range with the exact enumeration from EB:46. |
| H8-F10 | MINOR | DEEP:268–274 (card-6 (b)) "verified fraction = (accepted + challenged + debated) / total rows… reaches a pre-set ratio" | Criterion not yet decidable: (i) the "pre-set ratio" is never set — no default value exists, so the pass line is undefined; (ii) the formula's labels don't map onto EB §5's vocabulary ("consensus 1 / debated 4", EB:54) — "consensus" ∉ {accepted, challenged, debated} without a stated mapping. | Fix a default ratio (e.g. ≥0.5× the AGN-axes fraction) and add the label mapping (consensus→accepted). |
| H8-F11 | MINOR | BASE:196–198 (CHK-2.4), BASE:205–206 ("at the card's redshift grid"); DEEP:105 ("at the card's z grid") | Dangling reference: no concrete redshift grid is enumerated anywhere in the packet or its sources — SC:28 names "One selection + redshift grid" without values; CUR P1 gives none. The JWST/ALMA realism checks therefore have an undefined input and devolve to adjudicator judgment. (Same class, lesser: card-1 (e) "public at the needed depth" — "needed depth" undefined, DEEP:59–61.) | Have the future prompt fix the grid (e.g. z bins of the parent-sample candidates); until then mark CHK-2.4 realism scoring as judgment-based. |
| H8-F12 | NOTE | BASE:57–58, 354 `REJECT_RETAIN_VERIFIED_SOURCE_LEADS_ONLY` vs CY7:13 `REJECTED_RETAIN_VERIFIED_SOURCE_LEADS_ONLY` | Verdict-token drift from the historical cycle-7 token (REJECT_ vs REJECTED_). Legal as a new token, but a grep across the program's verdicts will split into two families. | Adopt the historical token or footnote the deliberate variant. |
| H8-F13 | NOTE | BASE:111–112 quotes REQ as "Existing source-basis links/claim IDs that must not be contradicted: … `#s2`–`#s8`" | Splice presented as quotation: REQ:14 is the header, REQ:15 actually reads "Local evidence anchors from `evidence-basis-20260708T014205Z.md#s2` to `#s8`." Meaning preserved; wording is a paraphrase inside quote marks. | Mark as paraphrase or quote L15 verbatim. |
| H8-F14 | NOTE | DEEP:4–5 "same source abbreviations: REQ / EB / SC / CUR" | Abbreviation list incomplete: the deepening body also uses CY7 (DEEP:147–148, 306–309) and VER (DEEP:148, 236, 309), declared only in BASE. | Extend the list to REQ/EB/SC/CUR/CY7/VER. |
| H8-F15 | NOTE | DEEP:8–9 "no numbers not already present in local files" vs DEEP:36 "in ≥2 independent mass bins" | Self-rule literally violated: devised design thresholds ("≥2 mass bins"; card-6's ratio placeholder) are numbers not present in local files. Intent ("logical tightening") is evident but the rule as worded fails its own audit. | Reword: "no new *empirical* values; design thresholds are logical tightening." |
| H8-F16 | NOTE | DEEP:264 "the verified-row mass sits in the AGN axes" | Not computable from the counts quoted in-packet: with EB's own §4 atlas counts (accepted 2 / debated 3 / reported 2 / unverified 1, EB:50), the AGN *section* has 5 verified-class rows vs Physical Mechanisms' 7 (EB:42). Reading "AGN axes" as the whole 7-axis debate map makes the sentence plausible but unquantified either way. | Quote the §4 counts and define "mass", or soften to a qualitative claim. |
| H8-F17 | NOTE | BASE:66 "Check: `grep -c '<marker>' body.md` == 1 AND it is the last non-empty line." | `grep -c` counts matching *lines*, not occurrences: a line containing the marker twice counts once, so "exactly once" can be over-approved in a pathological case; the standalone-final-line clause only partially compensates. | Use `grep -o '<marker>' body.md | wc -l`. |
| H8-F18 | NOTE | RCPT:43–45 (AAS PDFs "59116 B / 182955 B / 59768 B — existence verified") | Two divergent PDF copy-sets exist on disk: the receipt's byte counts match the live-root-before copies exactly ✓, but the frontend/public copies of the same three filenames differ (91577 / 222437 / 98223 B). RCPT claimed byte-identity only for md/html (true — re-verified), so this is not a P3 error, but a future adjudicator following CUR's relative links from the *other* copy would stat different files. | Pin the live-root-before PDFs as primary (matching RCPT ambiguity-2's md/html precedent). |
| H8-F19 | NOTE | BASE:45 (§0 canonical "Distinguishing reservoir removal from inefficient star formation") vs BASE:208 / DEEP:110 heading "Reservoir removal vs inefficient star formation (CUR P2)" | Title drift between the §0 canonical SC titles and the §3/DEEP headings (card 3 reworded; cards 2/4 drop the leading article "A"/"An"). Card numbers and content keep the bijection unambiguous; exact-title matching would stumble. | Repeat the canonical SC title verbatim in §3/DEEP headings. |

No BLOCKER findings. No claimed-pass-without-evidence (check-4 MAJOR class) found anywhere in the packet.

---

## 2. Criterion-by-criterion testability table

Legend: **DECIDABLE** = measurable threshold + defined input + defined pass/fail;
**PARTIAL** = decidable only with judgment or an undefined input; findings in ().

| Criterion | Testability | Basis / defect |
|---|---|---|
| G1 marker exactly-once, final line | PARTIAL (H8-F02, H8-F17) | Mechanical once a marker string exists; no fail-closed default if the future prompt omits it; `grep -c` counts lines. |
| G2 banned settled/causal register | DECIDABLE w/ caveat (H8-F07) | Grep list is mechanical; "applied to what evidence shows" needs light judgment; floor-echo collision unresolved. |
| G3 uncited leads labeled | DECIDABLE | Link-or-label on same line; mechanical. Verified consistent with VER item 4 + CY7's 26-label precedent. |
| G4 non-commensurables labeled | DECIDABLE (H8-F04 is citation-only) | Requires identifying unlike estimands — bounded judgment; examples given (Gatto/Gawade class). |
| G5 ID quarantine | PARTIAL (H8-F05) | Marking QUARANTINED is mechanical; the ≥3-failure wholesale trigger is undecidable until the gated lookup pass. |
| G6 no numeric import | PARTIAL (H8-F06) | First clause unfalsifiable on the answer; "presented as corrections/replacements" clause decidable. |
| G7 advisory-only shape | DECIDABLE | "Per-card ledger in REQ expected shape (REQ L20–21)" verified as a real, checkable contract; manuscript-prose call needs light judgment. |
| G8 six fields or NONE_FOUND | DECIDABLE | Field list matches REQ L21 exactly (re-verified, six fields); NONE_FOUND device makes it satisfiable. |
| F1 axis statuses stand | DECIDABLE | All five named statuses re-verified verbatim against EB:14–20. Own-voice vs cited-study distinction is explicit. |
| F2 mechanism vs prevalence | DECIDABLE | EB:14–15 verified ("in selected systems"; non-AGN channels). |
| F3 0 claim / 0 cite markers | DECIDABLE | EB:8 and EB:79 verified verbatim. |
| F4 open repair items stay open | DECIDABLE | All five cited loci verified: EB:22 (PENDING_RECHECK), EB:51 (2915/2921/2913), EB:56 (2133→2605.22497), EB:65 (2374 garbled; 2235 supported), EB:80 (P3 gate). |
| F5 anchor integrity | DECIDABLE w/ gap (H8-F08) | Comparison against EB anchors is mechanical; range excludes #s1 which card-1 floor uses. |
| CHK-1.1–1.4 | DECIDABLE | 1.3's "high-impact" inherits REQ:18's own vagueness (judgment); 1.4 has NONE_FOUND escape. Floors verified at SC:12–18, EB:37–38/41/50. |
| CHK-2.1–2.5 | DECIDABLE (H8-F11 on 2.4) | Four-qualifier rule, non-commensurability, merged-rate ban all mechanical; SC:24–29, CUR:15/18–19/24/26/28 all verified; 2.4's z-grid input undefined. |
| CHK-3.1–3.4 | DECIDABLE | Decomposition criterion + 3 named systematics verified at CUR:43/45; Gawade-class citation correct here; SC:35–38/40–41 verified. |
| CHK-4.1–4.4 | DECIDABLE | Scope-inflation test well-formed; SC:47–52 verified; 4.3's "may note the drop, must not claim resolved" decidable; instrument claims link-or-label. |
| CHK-5.1–5.4 | DECIDABLE | Global-ranking ban verified at CUR:62; joint-distribution + selection-function requirements verified at CUR:56/58/60; 5.4 has NONE_FOUND escape. |
| CHK-6.1–6.5 | DECIDABLE | z≈2.3 scope verified at SC:68/EB:59–60; 2374 seeding ban verified at EB:65; ranking ban verified at SC:71; 6.5's re-promotion allowance decidable. |
| §5 protocol order + wholesale rule | PARTIAL (H8-F01, H8-F05) | Gate order and per-card sequence defined; packet-level ACCEPT undefined; G5 trigger deferred. |
| DEEP (b) tightened criteria, cards 1–5 | DECIDABLE | Estimand-first: statistic, denominator, systematic budget, failure clause each present (e.g. card 1's "insufficient denominator" clause; card 2's fail-on-merged-rate; card 3's classifier with systematics inside; card 4's verdict bands; card 5's joint-distribution rule). |
| DEEP (b) card 6 | PARTIAL (H8-F10) | Metric defined but ratio unset and label vocabulary unmapped. |

Vacuous/self-satisfying criteria hunted for explicitly: none found — every gate/floor/CHK names a
falsifying observation except the G6 first clause (H8-F06), which is untestable rather than vacuous.

---

## 3. Full check log (all six families; clean checks included)

### Check 1 — Criterion testability → **DEFECT** (H8-F01, F02, F05, F06, F07, F08, F10, F11, F17)
Walked every gate (G1–G8), every floor (F1–F5), all 22 CHKs, the §5 protocol, and all six DEEP
(b) criteria — table above. 1 MAJOR (packet verdict undefined for partial coverage), rest MINOR/NOTE.
Clean highlights: G3/G8 fully mechanical; every DEEP card 1–5 criterion carries an explicit
failure clause; NOT_ADDRESSED / NONE_FOUND devices prevent self-satisfying scoring.

### Check 2 — Card ↔ baseline bijection → **CLEAN** (NOTE H8-F19)
Set-difference both ways = ∅: BASE §0/§3 cards {1..6} ↔ DEEP cards {1..6}, same numbering,
same CUR mapping per card (1 absorbed; 2→P1; 3→P2; 4 dropped; 5→P3; 6→methodological note).
Statuses agree in every pair (e.g. card 4: BASE "dropped in consolidation" ↔ DEEP (d) "editorial
consolidation (CUR L3), nothing more" — and CUR:3/64–66 verified). Mapping evidence verified in CUR:
P1=L13–28 (census), P2=L30–45 (depletion vs efficiency), P3=L47–62 (forward-modeled validation),
methodological note=L64–66 (corpus rebalancing); card-1 absorption is defensible (P1 carries
matched inactive controls, CUR:24; P3 carries the TNG/Horizon-AGN counterfactual leg, CUR:58).
RCPT card-coverage table (6/6 COMPLETE/COMPLETE) re-verified by direct read of both docs. Only
defect: heading drift (H8-F19).

### Check 3 — Numeric consistency → **DEFECT** (H8-F09; all else clean)
Values appearing in both docs, all recomputed/compared:
- 17% ionized (cosmic-noon AGN) / 46% neutral Na I D (massive-galaxy): BASE:178–180 ↔ DEEP:69–71 ↔ SC:24 ↔ EB:50 ledger names (`…17pct_ionized…`, `…46pct_neutral_naid…`) — MATCH.
- FMR ~0.1 dex to z≈2.3: BASE:306 ↔ DEEP:249–250 ↔ SC:68 ↔ EB:59 — MATCH.
- Claim IDs card 1 (2917, 2924; 2931; clc_agn_007; clc_agn2299_003/009/010): BASE ↔ DEEP ↔ EB:38/41/50 — MATCH.
- Claim IDs card 3: BASE:215–216 ↔ EB:46 — MATCH; DEEP:115 range notation — **MISMATCH** (H8-F09: sweeps 2908 = EB:55 environment claim, and 2910 ∉ EB).
- Repair items 2915/2921/2913, 2133→2605.22497, 2374 garbled + 2235 supported: BASE F4 & card 6 ↔ DEEP card 6 ↔ EB:51/56/65 — MATCH.
- Atlas counts: PM 4/3/7/16 (EB:42), Env 1/4 (EB:54), Frontier 3/2/1/4/59 (EB:63) ↔ DEEP:259–263 — MATCH.
- Derived, recomputed: "unverified-heavy by an order of magnitude" — frontier unverified 59 vs verified-class (3+2+1)=6 → 59/6 ≈ 9.8 ≈ 10× under DEEP's own verified-fraction ingredients — SUPPORTED (alternative reading 59/10 = 5.9× would not be; the doc's own metric definition licenses the 59:6 reading). Frontier total 69 rows; PM total 30.
- arXiv IDs (1706.08987, 2009.11175, 2401.12953, 2008.00005, 1606.03086, 1301.3092): BASE ↔ CUR:18/19/36/37/52/53/54 — MATCH (local presence only; external resolution is network-gated by design).
- Marker strings: `FABLE_BURN_P3_ACCEPTANCE_BASELINE_…` top+bottom of BASE ✓; `FABLE_BURN_P3_RT_DEEPENING_…` DEEP:3+312 ✓; recommended sidecar marker string identical at BASE:65 and BASE:339 ✓; REQ id `REQ_M3_RT_20260711T091128Z` consistent everywhere ✓.
- RCPT arithmetic: t_ack 01:47:52 → t_end 02:04 = 16.1 min ≈ "≈16 min" ✓; "target T0+55" matches P3 brief §6 ✓.

### Check 4 — Evidence for claimed status → **CLEAN**
No criterion or card in BASE/DEEP is marked met/passed/accepted — the packet is consistently
pre-adjudication (the §5 scoring table is an empty template; DEEP card-5 explicitly "none
adjudicated yet"). The only met/complete claims live in RCPT and all carry in-packet evidence,
which I independently re-verified: card coverage 6/6 (direct read ✓); "snapshots byte-identical
to originals" (all 6 hash-pairs recomputed, identical ✓); "referenced-but-missing paths: NONE"
(all 14 source paths + both copy-pairs + 3 PDFs + deepening HTML exist ✓); md/html byte-identity
across live-root-before vs frontend/public (`4f8e7fb0…` ×2, `e0342efb…` ×2 recomputed ✓);
deepening-HTML anchors #agn #gas #halos #chemical #high-redshift #environment #observational
each present exactly once (grep ✓); AAS PDF byte sizes match the primary copies ✓ (H8-F18 NOTE
on the divergent secondary copies); poll log 4 entries spaced ≤6.3 min, within the brief's
~15-min contract ✓; receipt final line is the exact required string ✓; done marker 0 B ✓.
Axis statuses asserted in BASE §0/F1 re-verified verbatim against EB:14–20 ✓. Baseline's
"REQ defines no completion marker" claim re-verified: REQ:3's `…SIDECAR_PROTOCOL_V1` is the
request's own protocol tag, not an answer-body completion marker — the gap claim is accurate ✓.
Unverifiable here: P3 pane id %186 (tmux session gone) — immaterial, no decision rests on it.

### Check 5 — Per-card network items → **CLEAN** (vagueness noted under H8-F11)
All six DEEP (e) sections carry the exact label `GATED — needs sidecar/network pass (separate
Duho approval)` verbatim (6/6 string-identical); every item names what to fetch (studies/
catalogs/sensitivity docs per card); none is silently assumed done — cross-checked (a)–(d) of
every card: no external fact is presented as fetched, and DEEP's header rule routes every
network need to (e). Confirmation criteria are explicit where it matters (card 2 "published
selection functions"; card 3 "existence, sample sizes"; card 4 "population statistics 2020+";
card 5 "which public data releases expose the fields"; card 6 "whether any proposes a
cross-channel weighting methodology") with two soft spots folded into H8-F11 (card 1 "needed
depth"; card 2 "card's z grid" undefined). RCPT follow-up queue: all 4 items GATED-labeled per
the P3 brief §8 requirement ✓, and item 2 correctly routes the §4 marker-contract fix to the
future prompt author ✓.

### Check 6 — Receipt custody recheck → **CLEAN** (0 mismatches)
Recomputed sha256 + bytes for **every** file RCPT lists (full pinned-vs-recomputed table in
`H8_RECEIPT.md`): 3 audited inputs ✓; `P3_ACK.md` 436 B ✓; done marker 0 B ✓; all 6
`sources-snapshot/` files ✓ and each byte-identical to its original ✓; all 14 source-table
paths ✓ including both md and both html copies (byte-identical pairs confirmed) ✓; P3 brief ✓;
CY7 ✓; VER ✓; director rollup ✓; M3 status ✓; Goru audit ✓; deepening HTML ✓. `P3_RECEIPT.md`
itself carries no self-hash by design ("post-hoc by auditor") — its pinned hash in the H8 brief
recomputed ✓. Result: 24/24 hash comparisons MATCH, 0 mismatches, 0 missing files.

---

## 4. Verdict

**PASS-WITH-FIXES.** The packet does what it claims: a fail-closed, card-by-card scorable
baseline whose every load-bearing citation survived adversarial re-derivation against pinned
snapshots. Required fixes before sidecar adjudication: H8-F01 (define the packet-level verdict
rule) plus the MINOR citation/decidability repairs (F02–F11), none of which disturb the floors.

FABLE_HARD_BURN_H8_P3_AUDIT_20260711T035354Z
