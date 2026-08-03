# Final no-apply rollup — research topics rewritten as academic proposal agendas

Marker: AUTOPILOT_RESEARCH_TOPICS_PROPOSAL_STYLE_20260708T093140Z
Author: Hwao-director (pane %107). Written 2026-07-08T09:42Z (18:42 KST).
Basis: three method-team proposal-style rewrites (in place, over the `research-topics-from-wiki-20260708T090359Z` sets) + method receipts + this director's independent read-only verification.

## Status: COMPLETE

The three method research-topic pages were rewritten into **academic research-proposal style** — plain-language mini-proposals for an astronomy reader, each with a mandatory `Survey/data plan`, no internal jargon in headings, static-safe, no product bindings. This is a **wiki**-derived docs/static rewrite; working-repo only (no live-root mirror by the autopilots).

## Per-method proposal counts + verification

Rewritten in place at `…/galaxy-evolution/<method>/research-topics-from-wiki-20260708T090359Z/` (HTML + MD + `research-topic-map` JSON + manifest).

| Method | proposals | `Survey/data plan` per card | static-safe | product claim/cite | jargon-in-page | HTML bytes / sha256(12) |
|---|---|---|---|---|---|---|
| **M1** packet-gated | 6 | ✅ (6/6) | ✅ (0 script/fetch/onclick/form/ext) | 0 / 0 | 1 (demoted to provenance) | 15,050 / `ca4599f77053` |
| **M2** source-first | 6 | ✅ (6/6 cards; 7 literal mentions including intro) | ✅ | 0 / 0 | 0 | 16,389 / `d379aabe9640` |
| **M3** debate-map | 6 | ✅ (6/6) | ✅ | 0 / 0 | 0 | 19,226 / `77d2dd9f329e` |

Sidecars (sha256(12)/bytes): M1 map `3f4d1292290d`/5,142 · md `8d2d3f8cce9d`/10,476 · manifest `d9c9f17ce03d`/663. M2 map `27efa641969d`/6,636 · md `acb045f36802`/11,360 · manifest `479ae046f446`/832. M3 map `92050034214f`/4,101 · md `ba0a25512a72`/8,442 · manifest `f13ee3361da0`/2,117.

## Public-readability summary
Each page now reads as `Galaxy Evolution — Research proposal agenda (Method X)` with 6–8 polished proposal cards instead of a jargonic gap list. Internal terms (claim IDs, cite-unmatched, P3, bound/unbound-local, packet, lane, audit) were demoted out of headings to near-zero (M1=1 residual in a provenance line; M2/M3=0). Every card names concrete **proposed** data (surveys/instruments/archives/simulations — e.g. DESI, JWST, ALMA, SDSS/MaNGA, Chandra/XMM/eROSITA, VLA/LOFAR, IllustrisTNG-style) labeled as data the study *would* use, not as evidence already in the wiki. Each method keeps its own POV and honesty caveat in plain words.

## Static validation
All three HTML: 0 `<script>` / `fetch(` / `onclick` / `<form>` / external hosts; product claim/cite comment counts **0 / 0**. Hard-excluded surfaces touched: **0**. No invented evidence/IDs/DOI/ADS.

## Receipts
- M2: `method2/autopilot/RESEARCH_TOPICS_PROPOSAL_STYLE_M2_20260708T093140Z.md`
- M3: `method3/autopilot/RESEARCH_TOPICS_PROPOSAL_STYLE_M3_20260708T093140Z.md`
- M1: `method1/autopilot/GORU_M1_PROPOSAL_STYLE_CHECK_20260708T093140Z.md` + director verification above (M1 page independently verified: 6 proposals, Survey/data plan 6/6, static-safe, 0/0 markers).

## Live-root / public mirror
Autopilot mirror: **0** — method autopilots did not touch the live root.

Tori post-rollup static mirror, in response to the user's request about the public Method1 topic page: **Method1 only**. Copied the four revised Method1 static files to the live public root:
`/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/public/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/`

Live backup before copy:
`…/research-topics-from-wiki-20260708T090359Z.backup-before-proposal-style-20260708T094443Z/`

Public verification: `https://nebulamind.net/agent-reports/wiki-method-results/galaxy-evolution/packet-gated-paper-to-wiki-reconciliation/research-topics-from-wiki-20260708T090359Z/research-topics-from-wiki-20260708T090359Z.html` returned HTTP 200 with `Galaxy Evolution — Research proposal agenda (Method 1)`, marker `AUTOPILOT_RESEARCH_TOPICS_PROPOSAL_STYLE_20260708T093140Z`, and 6 `Survey/data plan` sections. Existing Method1 index still links to this page. No frontend restart was needed.

M2/M3 were **not** mirrored to the live root; same static-copy pattern can be applied later if requested.

## Safety ledger
Read-only inspection + method-team in-place rewrites under the 3 `research-topics-from-wiki-20260708T090359Z/` dirs + `.hermes` receipts + this rollup. Tori then performed one narrow static live-root copy for Method1 only (4 files) and verified the public URL. **Zero** `:3000` restart/deploy, product DB/SQL, `/api/pages`, page_versions, live-wiki publish, trust recompute, git, cockpit/global/shared-parent, cloud/OAuth/secrets, browser, cron; zero Method3 P3 binding; zero invented data; zero director keystrokes into panes. All non-static hard gates remain closed.

AUTOPILOT_RESEARCH_TOPICS_PROPOSAL_STYLE_20260708T093140Z
