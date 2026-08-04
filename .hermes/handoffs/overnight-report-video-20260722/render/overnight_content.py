#!/usr/bin/env python3
"""Evidence-bounded content contract for the private overnight-report explainer."""

DURATION = 73.5
FPS = 24
SCENE_BOUNDARIES = [0.0, 10.5, 23.5, 36.0, 48.0, 62.5, 73.5]
SCENE_FRAMES = [0, 252, 564, 864, 1152, 1500, 1764]

NARRATION = [
    "Overnight, the autopilot built the full AI-Scientist corpus foundation — and all three quality gates. Not a paper. The foundation first, by design.",
    "The foundation: over one hundred twenty thousand papers embedded — galaxies and cosmology, 2009 through 2026. The embedding model won a ten-model retrieval evaluation, and the new index is about ten times the old corpus.",
    "Fifty-seven research topics were derived from scratch, then ranked by recent citation inflow over eight point nine million citation edges. JWST high-redshift galaxy evolution is first — by a wide margin.",
    "Retrieval runs on the local corpus and deep-reads each working set in full text. The canonical layer: nearly five thousand top-cited papers, ninety-six percent in clean HTML.",
    "Between an idea and a paper now stand three gates. Novelty can abort work that's already been done — and cite the prior paper. Expected value checks physical sanity, rejecting gross errors. And citation entailment catches fabricated citations.",
    "The honest scoreboard: zero papers auto-generated — work was held until the gates existed. Next: end-to-end gated study runs. No execution phrase is armed; the system waits.",
]

CAPTION_CUES = [
    [
        "Overnight, the autopilot built the full AI-Scientist corpus foundation",
        "— and all three quality gates.",
        "Not a paper. The foundation first, by design.",
    ],
    [
        "The foundation: over one hundred twenty thousand papers embedded",
        "— galaxies and cosmology, 2009 through 2026.",
        "The embedding model won a ten-model retrieval evaluation,",
        "and the new index is about ten times the old corpus.",
    ],
    [
        "Fifty-seven research topics were derived from scratch,",
        "then ranked by recent citation inflow over eight point nine million citation edges.",
        "JWST high-redshift galaxy evolution is first — by a wide margin.",
    ],
    [
        "Retrieval runs on the local corpus and deep-reads each working set in full text.",
        "The canonical layer: nearly five thousand top-cited papers,",
        "ninety-six percent in clean HTML.",
    ],
    [
        "Between an idea and a paper now stand three gates.",
        "Novelty can abort work that's already been done — and cite the prior paper.",
        "Expected value checks physical sanity, rejecting gross errors.",
        "And citation entailment catches fabricated citations.",
    ],
    [
        "The honest scoreboard: zero papers auto-generated",
        "— work was held until the gates existed.",
        "Next: end-to-end gated study runs.",
        "No execution phrase is armed; the system waits.",
    ],
]

TITLES = [
    ("Foundation first — by design", "The overnight result is infrastructure and gates, not a paper."),
    ("120,676 papers embedded", "A ten-times-larger semantic foundation for galaxies and cosmology."),
    ("57 topics, derived from scratch", "Recent citation inflow ranks a fresh frontier map without inherited topics."),
    ("Retrieval reads beyond abstracts", "Local semantic search hands a working set to HTML-first full-text grounding."),
    ("Three gates stand before a paper", "Grounded checks filter prior work, physical errors, and unsupported citations."),
    ("The honest overnight scoreboard", "No auto-paper; the next step is an end-to-end gated study run."),
]

GUIDE = [
    "Foundation + gates.",
    "Build the corpus.",
    "Derive the frontier.",
    "Ground every study.",
    "Filter before drafting.",
    "Hold the boundary.",
]

SOURCE_CONTRACT = {
    "live_status_url": "https://duho-macstudio.taila27502.ts.net/cockpit/ge-autopilot-status.json",
    "live_marker": "GE_AUTOPILOT_OVERNIGHT_20260719_CORPUS_GATES_DONE",
    "live_headline": "Overnight: built the full AI-Scientist corpus foundation + the three quality gates.",
    "canonical_constructor": "/Users/duhokim/NebulaMind/NebulaMind/tools/render_ge_autopilot_dashboard_v2.py:1265-1304",
    "source_brief": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/overnight-report-video-20260722/HWAO_SOURCE_BRIEF.md",
    "hwao_plan": "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/overnight-report-video-20260722/HWAO_VIDEO_PLAN.md",
    "character_strategy": "same established female astronomer and Emma voice; data graphics lead scenes 2-5",
    "publication_gate": "local review only; no upload, site/embed, deploy, DB, git, or execution phrase",
    "excluded_dynamic_cards": ["Usage quota", "Flow / Veo credits"],
}

assert SCENE_FRAMES[-1] == int(DURATION * FPS)
assert all(abs(SCENE_BOUNDARIES[i] * FPS - SCENE_FRAMES[i]) < 1e-9 for i in range(7))
assert len(NARRATION) == len(CAPTION_CUES) == len(TITLES) == len(GUIDE) == 6
