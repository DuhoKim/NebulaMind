# Method1 autopilot — research-topics proposal-style dispatch

Order marker: AUTOPILOT_RESEARCH_TOPICS_PROPOSAL_STYLE_20260708T093140Z
Continuation marker: GE_AUTOPILOT_IDLE_CONTINUATION_V1
Controller: Method1 Hwao. Class: BOUNDED DOCS/STATIC.

## Task (M1)
Rewrite the M1 research-topics page into **academic research-proposal style** (user: current pages too jargonic). Overwrite the existing `research-topics-from-wiki-20260708T090359Z/` files (explicitly allowed). Merge the 8 prior topics → 6 polished proposal cards across M1 focus areas: separating internal AGN feedback from environment/halo effects; observational tests for maintenance heating vs simulation-only; evidence-prioritization for under-supported areas; data-quality as a methods appendix (framed academically).

## Editorial rules
- Title: "Galaxy Evolution — Research proposal agenda (Method 1)".
- 5–8 proposal cards; each with: proposal title · research aim/central question · background & significance · **`Survey/data plan`** (named surveys/instruments/archives/simulations as *proposed* data, with what each contributes) · study design/analysis · expected contribution · feasibility & caveats · small provenance note (claim/source IDs ONLY here).
- No internal jargon in headings/body (no claim IDs, unbound-local, cite-unmatched, P3, packet, lane, audit) — demote to the provenance line.
- Proposed data ≠ existing evidence; don't imply a survey already supports a claim.
- Static-safe: no script/fetch/XHR/WebSocket/handlers/forms/external assets/hosts. Product claim/cite comments 0/0. Plain-language "proposed studies, not accepted claims" note.

## Output (overwrite existing set)
`…/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/` → `.html` + `.md` + `research-topic-map-…json` + `manifest-…json`.

## Lane chain
Lana/Hwao author proposals → Kun generate → Goru mechanical (proposal count, Survey/data-plan presence, static-safety, product-binding=0, jargon scan) → Kun validity → Tori receipt → Hwao verdict (`method1/autopilot/RESEARCH_TOPICS_PROPOSAL_STYLE_M1_…`). Director rollup is mastermind (not this lane).

## Gates closed
live-root write · :3000 restart · DB/SQL · /api/pages · page_versions/publish · deploy · git · cockpit/global/shared-parent · cloud/OAuth/secrets · browser · cron · M3 P3.

Status: **DISPATCHED** — building M1 proposal-style page.
