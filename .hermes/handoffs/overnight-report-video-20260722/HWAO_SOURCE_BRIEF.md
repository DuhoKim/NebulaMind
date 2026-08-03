# Hwao source brief — overnight report video

Marker: `OVERNIGHT_REPORT_VIDEO_SOURCE_BRIEF_20260722`

## User request

Make a video of the overnight report.

## Current source of truth

Direct live private status feed retrieved locally from:

`https://duho-macstudio.taila27502.ts.net/cockpit/ge-autopilot-status.json`

Live marker: `GE_AUTOPILOT_OVERNIGHT_20260719_CORPUS_GATES_DONE`

Live reported timestamp observed during source freeze: `2026-07-22T02:25:43Z`

Canonical constructor:

`/Users/duhokim/NebulaMind/NebulaMind/tools/render_ge_autopilot_dashboard_v2.py:1265-1304`

The current live feed supersedes the older July 2 public paper-distillation report and the stale C1r test fixture.

## Exact live claims

Headline:

> Overnight: built the full AI-Scientist corpus foundation + the three quality gates.

Stable report facts:

- 120,676 papers embedded.
- Scope: astro-ph.GA + astro-ph.CO, 2009–2026.
- qwen3-embedding-4b selected after a 10-model citation-retrieval evaluation.
- Semantic index size: 1.24 GB; about 10× the old 12k corpus.
- 57 topics derived from scratch with UMAP → HDBSCAN → c-TF-IDF.
- Topics ranked by recent citation inflow over an 8.9-million-edge graph.
- JWST high-redshift galaxy evolution is ranked first by a wide margin.
- Retrieval uses the local 120k corpus and deep-reads the working set HTML-first through ar5iv.
- Canonical deep layer: 4,864 top-cited papers, 96% clean HTML.
- Three quality gates are built, wired, and validated:
  - novelty: grounded, can abort already-completed work, and cites the prior paper;
  - expected value: numeric targeting plus physical-sanity checking to reject gross errors;
  - citation entailment: checks real citations and catches fabricated citations.
- Zero papers were auto-generated overnight. Work was deliberately held until the gates existed.
- Next action: end-to-end gated study runs.
- Approval phrase remains `NO ACTIVE EXECUTION PHRASE`.

## Exclusions

Do not include these changing dashboard cards in the durable video:

- Usage quota / live provider-card count.
- Flow/Veo credit count, which is explicitly stale and needs a new operator capture.

Do not imply:

- that a paper was generated;
- that the quality gates guarantee scientific truth;
- that an end-to-end gated study has already run;
- that any execution phrase is armed;
- that this local render authorizes upload, website embedding, deployment, DB writes, or git actions.

## Proposed video class

Status update / overnight report explainer.

Target contract:

- 73.5 seconds;
- six scenes;
- 1280×720, 24 fps;
- same established female astronomer and female narration as the accepted series;
- exact final narration drives facial animation, audible mix, and SRT;
- dark astronomical visual language, with a midnight-blue / dawn-gold progression;
- deterministic Pillow + ffmpeg charts and labels over reused atmospheric footage;
- local review master only.

## Proposed six-scene spine

1. Overnight outcome — foundation and gates completed, not a paper.
2. Corpus — 120,676 papers, scope, embedding, 1.24 GB / 10×.
3. Frontier map — 57 fresh topics, 8.9M edges, JWST high-z #1.
4. Retrieval and grounding — local semantic retrieval plus 4,864-paper full-text layer.
5. Three gates — novelty, expected value / physical sanity, citation entailment.
6. Honest handoff — zero auto-papers; next is end-to-end gated study runs; no active execution phrase.

## Hwao request

Return a concise evidence-bounded plan with:

- final six-scene narration;
- scene durations totaling exactly 73.5 seconds;
- visual hierarchy per scene;
- wording/caveat checks;
- whether this same-presenter decision is appropriate;
- local-only publication boundary.

Do not edit production code, cockpit, DB, site, git, or video assets. Write only:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/overnight-report-video-20260722/HWAO_VIDEO_PLAN.md`
