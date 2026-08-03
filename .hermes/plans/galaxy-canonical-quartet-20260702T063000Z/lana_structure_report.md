# Lana structure report — Galaxy Evolution canonical merge (V1 p57 × V2 p58)

Task: `GALAXY_CANONICAL_STRUCTURE_REVIEW_20260702`
Author: Lana (prose/structure lane, read-only design review)
Written: 2026-07-02, repo `/Users/duhokim/NebulaMind/NebulaMind`
Mode: **advisory only** — no mutation attempted or recommended inline; Hermes integrates & verifies.
Inputs read: `baseline_compare.md`, `baseline_compare.json`, `page_57_galaxy-evolution.md`, `page_58_galaxy-evolution-v2.md` (+ claim samples/counts from the JSON).

Page map under review:
- **V1 / p57** `galaxy-evolution` — v1708, 13,325 chars, **721 claim rows**, 8 citation links, 3 fact sources, 8 H2s, **22 inline claim chips**, evidence stances 98 supports / 82 neutral / 29 mismatch / 12 challenges / 2 refutes.
- **V2 / p58** `galaxy-evolution-v2` — v7, 10,265 chars, **8 claim rows**, **0 citation links, 0 fact sources**, 9 H2s, 8 inline chips; claims are high-evidence umbrella claims (2929=40 ev, 2934=25, 2931/2930=20).

---

## Top-line

Use **V1/p57 as the canonical base and refactor it in place**; use **V2/p58 as the structural + prose donor**. V1 has the more mature reader article *and* the entire provenance graph; V2 has the cleaner outline and three sections V1 lacks. This is an **additive refactor of V1**, not a republish of V2 over p57. Publishing V2's structure onto p57 without preserving V1's claim bindings is the one move that turns a working provenance page into a pretty but hollow one (see Q5).

---

## Q1 — Which page has the better article spine, and why?

**Split decision: V1 has the better *article*; V2 has the better *outline*.**

**V1 wins the spine that matters for a public page** — a causal throughline (regulated baryon cycle → halos → gas/feedback → quenching → environment → chemistry → high-z → open tensions). Every surfaced claim is embedded in explanatory prose with disciplined hedging ("best read conditionally rather than deterministically," "should remain caveated until its evidence is reconciled"). It reads like an article, not a claim list. It also already carries the 721-claim provenance and the surfaced-22 pattern, and it survived a deliberate 55k→13k distillation (v1707→v1708), so its density is earned.

**V2 wins the navigational outline**: conventional, reader-predictable section names (Physical Mechanisms / Dark Matter & Structure Formation / Star Formation & Quenching / AGN Feedback / Environmental Effects / Observational Evidence / Current Surveys & Missions / Synthesis). V2 adds three beats V1 is missing as standalone sections — **Observational Evidence, Current Surveys & Missions, and a Synthesis closer** — and its section naming is cleaner than V1's idiosyncratic "Gas Supply, Star Formation, And Feedback" + "Quenching And Maintenance Feedback."

**But V2's spine has a disqualifying flaw as prose**: it leaks editorial/meta self-talk into reader-facing text ("This page should avoid pretending…", "The section should not become a mission list," "The main editorial improvement is to stop presenting 'debates' as separate article furniture," "A reader-facing synthesis should therefore start with causal structure"). That is authoring instruction, not reader content — same defect class as the paper-packet PFR-001. V2's outline is a good editor's brief; its body is half-written and talks to itself.

Net: **keep V1's causal ordering and prose voice as the backbone; adopt V2's cleaner section taxonomy where they diverge and graft V2's three missing sections.**

---

## Q2 — Canonical H2s and order

Proposed canonical spine (9 H2s): V1 causal arc as the skeleton, V2's donor sections folded in, high-z massive-galaxy tension pulled forward into structure formation (per V2's argument) while reionization stays its own beat (it is a genuinely distinct topic — ionizing-photon budget, GC vs faint-galaxy sources).

| # | Canonical H2 | Source | Note |
|---|---|---|---|
| 1 | **Overview: Galaxy Evolution as a Regulated Baryon Cycle** | V1 | Keep V1's thesis framing verbatim; it is the article's organizing idea. |
| 2 | **Dark Matter Halos & Structure Formation** | V1 + V2 | Merge V1 "…Baryon Conversion Efficiency" with V2 "Dark Matter & Structure Formation"; **fold the JWST high-z massive-galaxy tension in here** (V2's point: it's a test of formation efficiency, not a generic "frontier"). |
| 3 | **Gas Supply, Star Formation & Feedback** | V1 | V1 section is strong; keep. |
| 4 | **AGN Feedback & Quenching** | V1 + V2 | Promote AGN to its own H2 (V1 buries it inside "Quenching And Maintenance Feedback"; the DB carries 38 AGN/quenching-debate claims and V2 gives it a full section). Absorb V1's maintenance-feedback prose here. |
| 5 | **Environment, Morphology & Structural Growth** | V1 + V2 | Merge; V1's ram-pressure/S0/merger prose + V2's satellite/cosmic-web umbrella claims. |
| 6 | **Chemical Enrichment & Cosmic Timing** | V1 only | **Keep — V2 has no equivalent.** V1's FMR/metallicity-clock section is a real asset; do not lose it. |
| 7 | **The High-Redshift & Reionization Frontier** | V1 (slimmed) | Retain a lean reionization/ionizing-source section (GC vs faint-galaxy debate, claims 2925/2926); the *massive-galaxy* half moves to §2. |
| 8 | **Observational Evidence & Surveys** | V2 graft | Merge V2 "Observational Evidence" + "Current Surveys & Missions," framed by **"which physical ambiguity each observing mode adjudicates."** |
| 9 | **Synthesis & Open Tensions** | V2 + V1 | V2's causal "Synthesis" closer, fused with V1's honest "Open Tensions And Evidence Gaps" list. Replaces standalone debate furniture. |

Ordering rationale: sections 1→7 preserve V1's causal reading order (supply → conversion → shutdown → external processing → chemical record → earliest epochs); 8 tells the reader how we know; 9 recaps causally and states what's unresolved. A reader can stop after §1 or §9 and still have a correct mental model.

---

## Q3 — Graft from V2 vs. discard

**Graft into canonical (V1 base):**
- **Synthesis closer** (§9) — causal recap is a strong reader payoff V1 lacks.
- **Observational Evidence + Surveys sections** (§8), framed by uncertainty-reduction, not a facility catalogue.
- **"Evidence snapshot:" prose device** — one short narrative paragraph per major section that *characterizes* the evidence base ("radio-jet simulations…, molecular-gas studies of nearby AGN hosts…, high-z QSO ionized outflows…"). This is V2's single best anti-dump technique (see Q4).
- **Reader-note transparency line** — a concise, reader-facing version of V2's top blockquote (claim chips open provenance; trust badges/scores/evidence unchanged). Rewrite out of workbench jargon.
- **V2's consolidated umbrella claims** (2929/2930/2931/2934, high evidence_count) as the 1 anchor claim per section, complementing V1's atomic claims.
- **V2's cleaner conventional section names** where they beat V1's.

**Discard / do not carry:**
- **All meta-editorial self-talk** in V2 body ("This page should avoid pretending…," "should not become a mission list," "The main editorial improvement is…," "A reader-facing synthesis should therefore…"). Hard NO-GO for public prose. Strip every instance.
- **V2 marker format** `<!-- claim:NNNN-->` (leading space) — see Q5; normalize to V1's `<!--claim:NNNN-->`.
- **Title suffix** "(Intro-Synthesis V2 Pilot)" — obviously drop.
- **V2's provenance state** (0 citations / 0 fact sources) — do not let V2's empty bindings overwrite V1's 8 citation links / 3 fact sources.
- **V2's 55k→re-inflation risk** — don't reverse V1's distillation; canonical should land near V1's current density (~13–16k), not V2 verbosity or old V1 bloat.

---

## Q4 — Claim/evidence surfaces in prose without a database dump

1. **Keep V1's inline model, not lists.** Claims appear as `<!--claim:ID-->load-bearing sentence<!--/claim:ID-->` inside explanatory prose. Never render claims as bullet dumps or expose the raw `claim.section` taxonomy/counts ("Retrieval-Complete Evidence Claims: 22") in reader text.
2. **Surface only load-bearing claims.** V1 surfaces 22 of 721 — that ratio is correct; do not inline all 721. Rule of thumb: a claim earns an inline chip only if its sentence would be in the article anyway. The remaining ~699 stay in the provenance/debate layer reached *through* chips.
3. **One umbrella anchor + a few specifics per section.** Lead a section with a V2-style consolidated claim (high evidence_count, e.g. 2929 for AGN), then 2–4 V1 atomic claims for concrete numbers (e.g. 2910 FMR 0.1 dex, 2923 major-merger size doubling). Avoid stacking near-duplicate atomic claims in one paragraph.
4. **Use "Evidence snapshot:" paragraphs** to summarize the evidence base narratively (V2's device) instead of exposing rows — the anti-dump move.
5. **Debates in-context, not as furniture.** Present both sides in the same paragraph (V1: "remains contested"; V2: "mode-, phase-, scale-dependent"); reserve the consolidated open-tensions beat for §9. This adopts V2's "absorb debates into topical sections" thesis without importing its meta-commentary.
6. **Trust stays a chip attribute, not prose.** Let trust badges/scores ride on the chip; don't narrate "trust_level: debated" in the sentence.

---

## Q5 — Top risk if combined poorly

**#1 (blocking): provenance / claim-binding regression.** V1/p57 is the asset — 721 claims, 8 citation links, 3 fact sources, a full evidence-stance graph — surfaced through inline chips 2905–2926. V2/p58 has 8 claims and zero citation/fact-source wiring, with a disjoint ID set (2929–2936). If "combine" is executed as *replace p57 content with V2-style prose*, every V1 claim ID not re-embedded loses its inline surface: chips orphan, the claim↔evidence contract breaks, and the citations/evidence view points at claims no longer in the prose. The result is a prettier page that has silently dropped the product's entire differentiator. **Mitigation: refactor p57 in place; re-map all currently-surfaced V1 claim IDs into the new §1–§9 layout before any apply; treat "no surfaced V1 claim ID orphaned" as a gate.**

**Secondary risks:**
- **Marker-format break (concrete, verified).** V1 uses `<!--claim:2905-->`; V2 uses `<!-- claim:2931-->` **with a leading space — and V2's *closing* tags `<!--/claim:2931-->` have no space, so V2 is internally inconsistent.** A strict chip parser keyed on `<!--claim:` will fail to render V2-format chips. Normalize every marker to `<!--claim:ID-->` / `<!--/claim:ID-->` and have Goru grep for any residual `<!-- claim:` before/after merge.
- **Meta-leak into public prose** — importing V2's authoring self-talk damages credibility; must be stripped (Q3).
- **Section-taxonomy mismatch is unresolved and large.** The DB `claim.section` buckets (10 of them) match neither page's H2 spine: "Open Questions & Frontier Debates" alone holds **377 of 721 claims**, and there are near-duplicate buckets ("Open Questions & Frontier Debates" vs "Open Questions and Active Debates": 4) plus a process-artifact bucket ("Retrieval-Complete Evidence Claims": 22). Whatever canonical H2 set is chosen, **Goru must produce a claim.section → canonical-H2 routing map**, with special attention to decomposing the 377-bucket; otherwise most content stays invisible or lands in the wrong section.
- **Re-inflation / caveat loss** — a careless merge can undo V1's 55k→13k distillation or drop hard-won hedges. Preserve caveat density.
- **Data-quality signals to carry forward, not bury:** 29 "mismatch" + 2 "refutes" evidence rows on p57 and stale `trust_level:"0.5"` string values (e.g. claims 2132/2135/2136/2138) are pre-existing defects; the merge shouldn't paper over them.

---

## Suggested pre-merge gate checklist (for Hermes/Goru; advisory)

1. **Base = p57**, refactor in place; p58 is donor only. Confirm canonical slug/title = `galaxy-evolution` / "Galaxy Evolution".
2. **Claim-ID preservation map**: every surfaced V1 chip (2905–2926) reassigned to a §1–§9 home; zero orphans. Decide per V2 umbrella claim (2929–2936) whether to import (and wire evidence) or drop.
3. **Marker normalization**: all chips `<!--claim:ID-->`; grep asserts no `<!-- claim:` remains.
4. **Meta-strip**: no authoring/editorial self-talk in body (reuse the V2 no-meta check).
5. **claim.section → H2 routing map** produced, 377-bucket decomposed, duplicate/artifact buckets reconciled.
6. **Provenance preserved**: citation links (8) and fact sources (3) retained or improved, never regressed to V2's zero.
7. **Density target** ~13–16k chars; caveats preserved.
8. Whole-page before/after diff + backup + hash-pin on p57 before any apply (this review authorizes none).

**Bottom line:** V1 is the canonical base and the thing to protect; V2 is a strong outline and a few good prose devices trapped in a half-written, self-talking pilot. Merge additively onto p57, graft V2's Observational/Surveys/Synthesis sections and its "evidence snapshot" device, strip V2's meta and fix its markers, and guard the 721-claim provenance graph as the non-negotiable. Combined carelessly, the top risk is shipping a better-looking Galaxy page that has quietly severed its evidence bindings.

LANA_GALAXY_CANONICAL_STRUCTURE_DONE_20260702
