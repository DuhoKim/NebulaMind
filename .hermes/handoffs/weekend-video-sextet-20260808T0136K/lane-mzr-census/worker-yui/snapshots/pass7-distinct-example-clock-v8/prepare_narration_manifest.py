#!/usr/bin/env python3
"""Prepare, but never execute, the Alloy narration manifest proposal."""
from pathlib import Path
import hashlib
import json
import re
import sys

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
        "narration_clauses": beat["narration_clauses"],
        "state_handoff": beat["state_handoff"],
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
        "No substantive scientific evidence state may remain unchanged for more than three seconds on the global timeline; every declared narration clause must map to at least one structured reveal or transform state.",
        "Do not create standalone section-divider holds; persist section identity with the evidence surface.",
        "Reveal REPORTABLE NOW, then PENDING, then the no-count gate, then transform into the combined qualified summary.",
        "After mux, re-run hard-cut/evidence-state timing and sentence/action alignment on the exact candidate.",
        "Do not use full-frame scientific resets between beats; each exit_state_id must match the next entry_state_id.",
        "Keep the 178-to-minus-21-to-157-to-T2 main spine visible after it is constructed through the final qualified close.",
        "Whenever 62 is visible, preserve its 157 parent, side-check boundary, and the all-157-to-T2 main path.",
        "Persist T1/T2 stage identity across handoffs and re-run exact cut-boundary continuity after mux.",
        "Use the final spoken script corresponding to the final Hwao storyboard, then run waveform and mux checks in the integrator lane.",
        "Listening approval is a separate gate after synthesis and mux.",
    ],
    "publication_gate": "CLOSED",
}
assert total_words == 208
assert cursor == 105.0
assert 105 <= manifest["planned_delivered_wpm"] <= 125
assert all(len(segment["timed_reveal_states"]) >= 2 for segment in segments)
assert all(
    max(
        [b - a for a, b in zip([s["at_seconds"] for s in segment["timed_reveal_states"]], [s["at_seconds"] for s in segment["timed_reveal_states"]][1:])]
        + [segment["visual_floor_seconds"] - segment["timed_reveal_states"][-1]["at_seconds"]]
    ) <= 3.0
    for segment in segments
)
assert all(
    segments[index]["state_handoff"]["exit_state_id"] == segments[index + 1]["state_handoff"]["entry_state_id"]
    for index in range(len(segments) - 1)
)
assert all("not-an-MZR" in " ".join(segment["state_handoff"]["persistent_layers"]) for segment in segments)
assert segments[5]["timed_reveal_states"][0]["evidence_delta"] == "new direct 157-to-T2 eligibility-gate path"
assert all("178→−21→157→T2 main spine" in segments[index]["state_handoff"]["persistent_layers"] for index in range(6, 10))
assert all(
    {clause["clause_id"] for clause in segment["narration_clauses"]}
    == {clause_id for state in segment["timed_reveal_states"] for clause_id in state["clause_ids"]}
    for segment in segments
)
assert all(
    state["operation"] in {"reveal", "transform"}
    and state["evidence_delta"]
    and not re.search(r"\b(hold|retain|standalone section divider)\b", state["visible_change"] + " " + state["evidence_delta"], re.IGNORECASE)
    for segment in segments
    for state in segment["timed_reveal_states"]
)
global_times = [
    segment["proposed_start_seconds"] + state["at_seconds"]
    for segment in segments
    for state in segment["timed_reveal_states"]
]
global_gaps = [b - a for a, b in zip(global_times, global_times[1:])] + [cursor - global_times[-1]]
assert global_times == sorted(set(global_times))
assert max(global_gaps) <= 3.0

out = HERE / "ALLOY_NARRATION_MANIFEST_PROPOSAL.json"
payload = json.dumps(manifest, indent=2) + "\n"
if "--check" in sys.argv:
    assert out.exists() and out.read_text() == payload
    print(f"PASS {out}")
else:
    out.write_text(payload)
    print(out)
