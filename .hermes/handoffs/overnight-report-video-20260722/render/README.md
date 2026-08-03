# NebulaMind overnight-report video — local review production

Marker: `NEBULAMIND_OVERNIGHT_REPORT_V1_LOCAL_PRODUCTION`

## Source

This video represents the current private Galaxy Evolution overnight report frozen under marker:

`GE_AUTOPILOT_OVERNIGHT_20260719_CORPUS_GATES_DONE`

Canonical source:

`/Users/duhokim/NebulaMind/NebulaMind/tools/render_ge_autopilot_dashboard_v2.py:1265-1304`

Hwao plan:

`../HWAO_VIDEO_PLAN.md`

The transient usage-quota card and stale Flow/Veo-credit card are deliberately excluded.

## Contract

- Status-update explainer, not a generated-paper announcement.
- 73.5 seconds, six scenes, 1,764 frames.
- 1280×720 at 24 fps.
- Same established female astronomer and `en-US-EmmaNeural` voice.
- Exact final narration drives SadTalker facial animation, final mix, and SRT timing.
- Deterministic Pillow diagrams and text over reused atmospheric clips.
- Midnight-blue to dawn-gold accent progression.
- Scene 3 uses a uniform 57-item count grid. It does not invent UMAP coordinates or proportional citation-inflow values.

## Stable facts represented

- 120,676 embedded papers, astro-ph.GA + astro-ph.CO, 2009–2026.
- qwen3-embedding-4b selected after a ten-model citation-retrieval evaluation.
- 1.24 GB semantic index, roughly ten times the old 12k corpus.
- 57 topics derived from scratch.
- 8.9-million-edge citation graph.
- JWST high-redshift galaxy evolution ranked first by a wide margin.
- 4,864-paper canonical full-text layer, 96% clean HTML.
- Novelty, expected-value/physical-sanity, and citation-entailment gates built, wired, and validated.
- Zero auto-generated papers.
- Next step: end-to-end gated study runs.
- No execution phrase armed.

## Reproduce

```sh
python generate_narration.py
python run_talking_head.py
python build_video.py
python qa_video.py
```

## Provenance

- Narration: Edge TTS, `en-US-EmmaNeural`.
- Presenter: local SadTalker exact-audio animation of the previously accepted synthetic astronomer portrait.
- Graphics/compositing: Pillow + ffmpeg.
- Background footage: reused atmospheric NebulaMind clips; no new generative-video call.
- Hwao/Fable contributed the evidence-bounded plan; it did not render the media.

## Hard gate

Local review only. This production does not authorize YouTube upload, an unlisted review upload, public visibility, website embedding, deployment, DB writes, git actions, or any active execution phrase.
