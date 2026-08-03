# Lana T3 — prose-safety / overclaim review — Method1 / PGR

Overnight marker: OVERNIGHT_AUTONOMOUS_GO_20260706T155128Z
Method packet marker followed: GALAXY_EVOLUTION_METHOD1_ULTRA_FORMAT_ROLE_SPLIT_20260707 (T3)
Team marker: GALAXY_EVOLUTION_METHOD1_P0_START_20260706T140842Z
Role performed: Lana — science/prose reviewer (pane Method1 Hwao/Lana; Lana receipt LANA_P0_ACK_20260706T140842Z.md confirmed present before starting)
Safety: NO ACTIVE EXECUTION PHRASE. Docs-only review; no DB/SQL, live wiki/page_versions, deploy/restart, git, cloud/API/billing/credits/OAuth, browser automation, or Ultra/Gemini/Antigravity execution.

## Files read (exact)
- .hermes/handoffs/galaxy-evolution/mastermind/OVERNIGHT_AUTONOMOUS_GO_20260706T155128Z.md
- .hermes/handoffs/galaxy-evolution/method1/HWAO_PGR_ROLE_SPLIT_PACKET_ULTRA_FORMAT_20260707.md
- .hermes/handoffs/galaxy-evolution/method1/receipts/LANA_P0_ACK_20260706T140842Z.md
- .hermes/handoffs/galaxy-evolution/method1/GORU_PGR_MECH_VALIDATION_20260707T001446Z.md
- frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/p1-legacy-overclaim-disposition-spec.html
- frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/pgr-current-page-inventory-20260706T130610Z.md (claim-chip/trust/watch-claim tables)

## File written (exact)
- .hermes/handoffs/galaxy-evolution/method1/LANA_PGR_PROSE_SAFETY_REVIEW_20260706T155406Z.md (this file)

## 1. P1 target dispositions (route recommendations to Hwao)

Method rule applied: preserve only prose moves that are ALREADY safe for a reader-facing wiki page. All three legacy targets fail "already safe" as currently badged.

### Claim 2298 — "AGN feedback heats the gas reservoirs of massive galaxies."
Packet facts: trust `consensus`, score 0.2196, single evidence row 25998; contradicted by scoped successor 2946 (reported, 0.450, 9 supports: heating/maintenance support is model-dependent / simulation-bounded, not measured prevalence).
- Overclaim findings: (a) universal present-tense mechanism claim vs model-bounded successor; (b) `consensus` badge sitting on a 0.22 score overstates certainty to readers; (c) one evidence row cannot carry a page-level settled statement.
- **Recommendation: Route R** — retire/hide from reader-facing chip surfaces now. Route A (scoped recast, e.g. "in massive halos, AGN heating is a candidate maintenance mechanism with model-dependent support") stays available only via a later exact packet with source-position verification. Not safe-now in any settled voice.

### Claim 2299 — "AGN feedback expels gas from the reservoirs of massive galaxies."
Packet facts: trust `accepted`, score 0.3241, evidence 25999 + 30631; contradicted by scoped successor 2945 (debated, 0.450, 9 supports: gas removal alone cannot explain every quenching pathway; retained reservoirs and low star-formation efficiency remain observed).
- Overclaim findings: unqualified expulsion-as-mechanism wording asserts universality the successor explicitly denies; the two evidence rows support outflows in selected systems, not reservoir-wide expulsion as a general rule.
- **Recommendation: Route R** for the broad claim as a visible chip. Any expulsion sentence in future prose must be scoped ("in selected massive systems, AGN-driven outflows remove molecular gas…") and chip-linked to successors — that is Route A wording requiring a later exact packet. Until then, the topic may appear only as explicitly debated prose without a settled chip.

### Claim 2924 — "AGN feedback heats the gas reservoirs of massive galaxies." (retrieval-complete duplicate)
Packet facts: status `parent_replaced` yet still displaying `consensus 0.800`, evidence 26704–26707.
- Overclaim findings: a retired parent rendering with the strongest certainty badge on the page is the single worst display-integrity hazard in this method: it makes superseded broad wording look stronger than its scoped replacements (2946 et al.).
- **Recommendation: Route R, highest priority** — finish retirement/display removal; under no condition may it render as visible consensus. No recast; content is already covered by successors.

Common ruling: none of 2298/2299/2924 is a safe-now prose move. Safe-now moves that DO exist: presenting AGN heating vs expulsion as an open, scoped debate anchored on successor claims (below).

## 2. Successor chip-safety classes for the same-format article (sparse-chip discipline)

Conditional on exact claim-text verification at draft time (texts for 2942–2944/2947/2948 are not in the packets read; classes below are from packet trust/score/stance facts plus the spec's semantic summaries for 2945/2946):

- **Safe-now chip candidates:** 2943 (accepted, 0.671, 15 supports), 2947 (accepted, 0.670, 10 supports). Strongest provenance on the page; suitable as the AGN section's sparse chips.
- **Debate-framed only:** 2942 (debated, 0.584, 7 supports), 2944 (debated, 0.450, 16 supports), 2945 (debated, 0.450 — carries the tension against legacy 2299), 2946 (reported, 0.450 — carries the tension against 2298/2924). These may appear as chips only inside prose that explicitly frames the point as debated/under test; never in settled voice.
- **Not chip-worthy now:** 2948 (reported, 0.200, 2 evidence) — too weak; prose caution sentence at most, no chip.
- Sparse-chip rule for the future draft: at most ~2 chips per AGN paragraph, only where provenance changes what a reader should believe; do not flood (format contract requirement).

## 3. Overclaim screen — constraints that bind the future same-format draft

1. No settled-voice sentence may assert universal AGN heating or expulsion of massive-galaxy reservoirs; both mechanisms render only as scoped/debated.
2. Badge-score mismatches must not anchor prose certainty: `consensus` on 0.2196 (2298) and `consensus` on −0.272 (2187) are P4-guard territory; prose must follow score+stance reality, not the badge, until the P4 guard applies.
3. Citation traces seq 1–5 (gravitational-wave, mirror-star, PDS 70, off-scope strangulation entries) are Goru NO-GO rows: they must not be cited by any prose move; carried unchanged.
4. The literal `"0.5"` trust bucket (526 chips incl. 2546) is NO-GO for chip rendering; no future chip may rely on that bucket before the P4 route fix.
5. Debate-group API returns 0 groups: the article's open-debates section must be authored from packet facts, not from the debate-group surface, until that route is fixed (Goru NO-GO carried).

## 4. Ultra second-opinion determination

**ULTRA_NOT_NEEDED.** The P1 dispositions follow deterministically from packet facts: a `parent_replaced` row must not display as consensus (2924), badge-over-score inflation cannot be published (2298), and broad wording contradicted by its own scoped successors cannot render as settled (2298/2299). There is no genuinely contested boundary here that an external second opinion would move. No Ultra/Gemini/Antigravity was invoked, and none is requested.

## 5. Status

**PASS** — T3 deliverable complete. Carried conditions (not blockers): successor claim texts 2942/2943/2944/2947/2948 must be text-verified before chip insertion in any future draft packet (assigned naturally to Goru counts + Kun reproduction at draft time).

Safety ledger: DB/SQL 0 · live wiki/page_versions 0 · trust recompute 0 · deploy/restart 0 · git 0 · cloud/API/GCP/billing/account/payment/credits/OAuth 0 · browser automation 0 · cron/route/config 0 · cross-method/shared-parent writes 0 · Ultra/Gemini/Antigravity 0.

Stopping after this deliverable per overnight packet.
