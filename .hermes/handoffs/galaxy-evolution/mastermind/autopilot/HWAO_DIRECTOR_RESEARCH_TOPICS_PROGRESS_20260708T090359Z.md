# Hwao-director progress — research-topics-from-wiki supervision

Marker: AUTOPILOT_RESEARCH_TOPICS_FROM_WIKI_20260708T090359Z
Role: Hwao-director — supervisor + final rollup owner (method teams author the research-topic candidates; NOT director solo-author). Snapshot 2026-07-08T09:06Z (18:06 KST).
Runs concurrently with the low-usage continuation (`…LOW_USAGE_CONTINUATION_20260708T083100Z`, time-gated 10:31Z).

## Goal
Three additive, method-matched **research-topic** HTML candidates (wiki-style) derived ONLY from each method's resulted local wiki candidate — 6–12 topic cards each (title · plain-English question · why it emerged from the wiki · method-specific evidence/trust basis · scope/limits · docs-only next action), + md + topic-map JSON + manifest. **No invented evidence/IDs/DOI/ADS/product bindings.** Static-safe (no JS/fetch/XHR/handlers/external assets). Expected product claim/cite comment count: **0**. Visible caveat that topics are hypotheses/questions, not accepted claims.

## Source candidates confirmed present
- M1: `…/packet-gated-…/prose-evidence-trust-deepening-20260708T043427Z/wiki-prose-evidence-trust-deepening-hwao-20260708T043427Z.html` (richer Hwao variant; fallback = canonical) ✅
- M2: `…/source-first-…/…/wiki-prose-evidence-trust-deepening-20260708T043427Z.html` (+ v2 comparison) ✅
- M3: `…/debate-map-…/…/wiki-prose-evidence-trust-deepening-20260708T043427Z.html` (repaired evidence/trust-visible) + `evidence-trust-rebuild/evidence-basis-20260708T014205Z.md` ✅

## Output dirs (additive; do not overwrite prior candidate dirs)
`…/<method-dir>/research-topics-from-wiki-20260708T090359Z/` with `research-topics-from-wiki-…html`, `…md`, `research-topic-map-…json`, `manifest-…json`.

## Plan (method teams author; low-usage lanes verify; director rolls up)
- Hwao-m1/m2/m3 each derive their method's 6–12 topics from their wiki candidate (M1 = evidence-bound-vs-unbound + AGN caution + row-count ambiguity + source gaps; M2 = accepted/limited/rejected/excluded + 28060-no-target + 22-vs-21 totals + cite-unmatched gaps; M3 = debate-map axes + PENDING_RECHECK + unmatched).
- Goru/Gemini: exact topic count, evidence/trust-basis count, source-section map, static-safety scan → one artifact each.
- Kun/Codex: HTML/JSON validation, relative-link target scan, checksum manifest.
- Lana: no-overclaim review if available.
- Director: independent verification + final rollup (per-method table: paths, bytes, sha256(16), topic count, rel-link count, static-safety, product claim/cite count, source wiki path) after candidates + checks land. Rollup must include the marker + the word `wiki`.

## Boundaries / hard gates (CLOSED)
Additive working-repo static/docs under the 3 method research-topics dirs + `.hermes` only. NO live-root/mirror, `:3000` restart/deploy, product DB/SQL, `/api/pages`, page-version, publish, git, cockpit/global/shared-parent, cloud/OAuth/secrets, browser, cron, Method3 P3. No director keystrokes; no solo authoring.

## Safety ledger (this note)
Read-only inspection + this one note. Zero gated actions; zero keystrokes; zero solo authoring. Hard gates closed.

AUTOPILOT_RESEARCH_TOPICS_FROM_WIKI_20260708T090359Z
