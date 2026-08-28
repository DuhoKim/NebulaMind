#!/usr/bin/env python3
"""Prepare, but never execute, the Alloy narration manifest proposal."""
from pathlib import Path
import hashlib
import json
import re

HERE = Path(__file__).resolve().parent
storyboard = json.loads((HERE / "STORYBOARD_CANDIDATE.json").read_text())
storyboard_sha256 = hashlib.sha256((HERE / "STORYBOARD_CANDIDATE.json").read_bytes()).hexdigest()
visual_qa = json.loads((HERE / "qa/visual_proposal_qa.json").read_text())
assert visual_qa["verdict"].startswith("PASS_FOR_STATIC_VISUAL_PROPOSAL_ONLY")
assert visual_qa["accepted_artifact"] == "visual_proposal_v8.png"

segments = []
cursor = 0.0
for beat in storyboard["beats"]:
    words = len(re.findall(r"\b[\w–-]+\b", beat["narration"]))
    duration = float(beat["proposed_seconds"])
    segments.append({
        "segment_id": beat["id"],
        "text": beat["narration"],
        "word_count": words,
        "visual_floor_seconds": duration,
        "timed_reveal_states": beat["timed_reveal_states"],
        "proposed_start_seconds": cursor,
        "proposed_end_seconds": cursor + duration,
        "output_basename_proposal": f"{beat['id']}-alloy.wav",
        "synthesis_state": "NOT_EXECUTED",
    })
    cursor += duration

total_words = sum(s["word_count"] for s in segments)
manifest = {
    "status": "PROPOSAL_ONLY_NOT_EXECUTED",
    "writer": "Hwao only",
    "provider_route": "Nous-managed OpenAI text-to-speech route",
    "voice": "Alloy",
    "speed": 1.18,
    "speed_source": "authoritative HWAO_WEEKEND_ORDER.md; do not re-derive per segment",
    "source_storyboard": "STORYBOARD_CANDIDATE.json",
    "source_storyboard_version": storyboard["storyboard_version"],
    "source_storyboard_sha256": storyboard_sha256,
    "audience_copy_status": storyboard["audience_copy_contract"]["status"],
    "visual_qa_gate": {
        "artifact": visual_qa["accepted_artifact"],
        "sha256": visual_qa["accepted_sha256"],
        "verdict": visual_qa["verdict"],
    },
    "planned_total_words": total_words,
    "planned_visual_floor_seconds": cursor,
    "planned_delivered_wpm": round(total_words / cursor * 60, 1),
    "pronunciation_guidance": {
        "VizieR": "VEE-zee-air",
        "UCD": "U-C-D",
        "MZR": "M-Z-R",
        "T2": "T two",
        "src.redshift": "source dot redshift",
        "symbol Z": "symbol zee",
    },
    "segments": segments,
    "audio_artifacts": [],
    "tts_invoked": False,
    "integration_constraints": [
        "Visual card durations are floors; narration duration may expand a card but must not compress below the visual floor.",
        "No worker-lane audio synthesis is authorized.",
        "No narration may call 62 eligible or describe the census as an MZR measurement.",
        "No narration may call abundance-search-, mass-search-, or redshift-search-axis metadata reach an adjudicated physical measurement.",
        "T1 retrieval controls and T2 contract-design controls are distinct workflow stages and must remain labeled separately.",
        "If T2 control counts are spoken or shown, include all 12 decoys plus 3 anchors and call them contract-design controls, not eligibility results.",
        "Public release requires an audience-reachable methods and count ledger for internally derived denominators.",
        "No substantive scientific evidence state may remain unchanged for more than four seconds; every substantive narration clause must trigger a visible reveal.",
        "Do not create standalone section-divider holds; persist section identity with the evidence surface.",
        "Reveal REPORTABLE NOW, then PENDING, then hold the combined qualified summary.",
        "After mux, re-run hard-cut/evidence-state timing and sentence/action alignment on the exact candidate.",
        "Use the final spoken script corresponding to the final Hwao storyboard, then run waveform and mux checks in the integrator lane.",
        "Listening approval is a separate gate after synthesis and mux.",
    ],
    "publication_gate": "CLOSED",
}
assert total_words == 207
assert cursor == 105.0
assert 105 <= manifest["planned_delivered_wpm"] <= 125
assert all(len(segment["timed_reveal_states"]) >= 2 for segment in segments)
assert all(
    max(
        [b - a for a, b in zip([s["at_seconds"] for s in segment["timed_reveal_states"]], [s["at_seconds"] for s in segment["timed_reveal_states"]][1:])]
        + [segment["visual_floor_seconds"] - segment["timed_reveal_states"][-1]["at_seconds"]]
    ) <= 4.0
    for segment in segments
)

out = HERE / "ALLOY_NARRATION_MANIFEST_PROPOSAL.json"
out.write_text(json.dumps(manifest, indent=2) + "\n")
print(out)
