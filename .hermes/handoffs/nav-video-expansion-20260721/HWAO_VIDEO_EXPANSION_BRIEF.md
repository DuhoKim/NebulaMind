# Hwao brief — remaining NebulaMind Lab navigation videos

Task: `nav-video-expansion-20260721`
Lane: Hwao/Fable coordinator
Status: READY_FOR_PLAN

## User direction

The user said: “generate videos for remained parts also. should we change the character for each Nav?”

Interpret this as a request to extend the current narrated Lab explainer series beyond Topic, while deciding the presenter-character continuity before rendering.

## Source of truth

Use the currently served production root, not the stale working checkout:

- `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/src/app/lab/labTabStore.ts`
- `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/src/app/lab/stageData.ts`
- `/Users/duhokim/NebulaMind/NebulaMind-origin-main-live/frontend/src/app/lab/LabStages.tsx`
- live page: `https://nebulamind.net/lab`

Existing media implementation and verified V8 style:

- `/Users/duhokim/HermesOps/scripts/clips/subnav_flow_female_voice_v8/`
- saved presenter master: `/Users/duhokim/HermesOps/scripts/clips/character/master_portrait.png`
- current voice: `en-US-EmmaNeural`, clearly female
- current format: 1280×720, about 73.5 seconds, six scene-aligned narration paragraphs, exact-audio talking presenter, manual SRT, light ambient music

## Current coverage

Topic is already covered by:

- Corpus overview (`oMA-H1m5yZQ`)
- Embedding V8 (`1vjXzWa9JAY`)
- Clustering V8 (`RbjFCiX2i3k`)
- Activity Overlay V8 (`cp8-I5XRP9s`)
- Ranking V8 (`1tG5cuTcPXI`)

Production’s `subnavVideos.ts` is stale and is not authority for current YouTube state. Updating it or any delivery manifest is outside this brief.

## Remaining production navigation

Top-level stages:

1. Data — four subitems: SDSS, JWST, COSMOS2020, IllustrisTNG.
2. Methods — five subitems: star-forming main sequence, mass–metallicity relation, stellar mass function, SF efficiency/baryon budget, simulation vs observation.
3. Paper — five subitems: draft board, flagship studies, frontier drafts, pipeline runs, how papers are made.

## Decision requested from Hwao

Write a coordination plan that decides:

1. Scope: three 60–75 second stage-overview videos (recommended) versus fourteen per-subitem videos. Explain why the chosen scope matches the actual top navigation and avoids repetitive channel uploads.
2. Character system: whether to keep one established female astronomer identity across all stages or introduce different identities. Recommended direction: same face and female voice as the recognizable series anchor; change wardrobe/accent palette/framing/background and specialty cues per stage, not the person.
3. Exact creative variants if continuity is chosen:
   - Data: observational astronomer; cool teal/blue; telescope/archive/catalog cues.
   - Methods: computational astrophysicist; violet/indigo; equations, plots, simulation cues.
   - Paper: research editor/referee; warm gold; manuscript, citation, review-loop cues.
4. One acceptance matrix per planned video: purpose, current source claims, six scene beats, narration boundaries, presenter treatment, voice, captions, duration, local QA, and separate publication gate.
5. Explicitly identify claims that require more live-source inspection before narration is final.

## Safety and ownership

This is a planning-only Hwao task.

Allowed:

- read the production Lab source files listed above;
- read existing V8 scripts/receipts;
- write only the requested plan file.

Not allowed:

- no rendering;
- no image/video generation calls;
- no YouTube upload or visibility change;
- no website/source/manifest edits;
- no DB/API writes;
- no deploy/restart;
- no git writes;
- no cockpit edits;
- no secrets.

## Deliverable

Write:

`/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/nav-video-expansion-20260721/HWAO_VIDEO_EXPANSION_PLAN.md`

Required standalone marker:

`HWAO_NAV_VIDEO_EXPANSION_PLAN_COMPLETE_20260721`

The plan must be concise but executable by Tori as bounded local rendering work. Stop after writing it.
