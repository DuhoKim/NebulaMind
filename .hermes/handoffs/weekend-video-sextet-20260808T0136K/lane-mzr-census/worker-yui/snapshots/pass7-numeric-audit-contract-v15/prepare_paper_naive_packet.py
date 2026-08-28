#!/usr/bin/env python3
"""Render exact audience payload plus explicitly declared closed-book review scaffolding."""
from pathlib import Path
import hashlib
import json
import sys

HERE = Path(__file__).resolve().parent
STORY_PATH = HERE / "STORYBOARD_CANDIDATE.json"
PACKET_PATH = HERE / "PAPER_NAIVE_PACKET.md"
RECEIPT_PATH = HERE / "qa/PAPER_NAIVE_PACKET_PROJECTION.json"
story = json.loads(STORY_PATH.read_text())


def visible_strings(value):
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [text for item in value for text in visible_strings(item)]
    if isinstance(value, dict):
        return [text for item in value.values() for text in visible_strings(item)]
    return []


questions = [
    "What is this work counting? State its scope and non-scope.",
    "What two retrieval channels were used?",
    "Reconstruct the main count sequence and explain where the 62-term check sits relative to the T2 eligibility application.",
    "What does `62` mean, and what does it not mean?",
    "Contrast the recorded T1 evidence with the T2 contract-design evidence and status.",
    "What did the recorded checks establish, and what did they leave unresolved?",
    "How are the recorded examples grouped? Name each grouping and its members.",
    "What is reportable now, and what remains pending?",
]
approved_questions_sha256 = "dc90d53b99c063842071b7d51c84469489f92ec592587827e9aa29935ac0144f"
questions_sha256 = hashlib.sha256(
    json.dumps(questions, ensure_ascii=False, separators=(",", ":")).encode()
).hexdigest()
assert questions_sha256 == approved_questions_sha256
answer_premise_fragments = [
    "not themselves adjudicated physical measurements",
    "not eligibility results",
    "failure mode did those checks not certify",
    "precision-failure categories are shown",
]
question_answer_premise_hits = {
    fragment: [question for question in questions if fragment.lower() in question.lower()]
    for fragment in answer_premise_fragments
}
assert all(not hits for hits in question_answer_premise_hits.values())
lines = [
    f"# Paper-naive closed-book packet — MZR archive census {story['storyboard_version']} proposal",
    "",
    "Read this packet once. Then answer the eight questions from memory without reopening it, browsing, or reading any other file.",
    "",
    "## Deterministic projection boundary",
    "",
    "Each beat below contains the exact `narration`, every leaf string under `on_screen_copy`, and the exact `display_citation`, in storyboard order. The packet is not projection-only: its title, directions, headings, bullets, and eight questions are declared review scaffolding outside the audience projection. The scaffolding asks questions but supplies no answers or new declarative scientific claims. No visual action, timed state, handoff, clause map, verification source, prior verdict, or answer key is included.",
    "",
]
projected_records = []
for beat in story["beats"]:
    screen = visible_strings(beat["on_screen_copy"])
    record = {
        "beat_id": beat["id"],
        "narration": beat["narration"],
        "on_screen_copy_leaf_strings": screen,
        "display_citation": beat["display_citation"],
    }
    projected_records.append(record)
    lines.extend([
        f"## Beat {beat['id']}",
        "",
        f"Narration: {beat['narration']}",
        "",
        "On-screen copy:",
    ])
    lines.extend(f"- `{text}`" for text in screen)
    lines.extend(["", f"Display citation: `{beat['display_citation']}`", ""])
lines.extend(["## Questions", ""])
lines.extend(f"{index}. {question}" for index, question in enumerate(questions, 1))
packet = "\n".join(lines) + "\n"
audience_projection = "\n".join(
    text
    for beat in story["beats"]
    for text in visible_strings({"narration": beat["narration"], "on_screen_copy": beat["on_screen_copy"], "display_citation": beat["display_citation"]})
)
receipt = {
    "verdict": "PASS",
    "contract": "EXACT_AUDIENCE_PAYLOAD_PLUS_DECLARED_REVIEW_SCAFFOLDING",
    "storyboard_version": story["storyboard_version"],
    "storyboard_sha256": hashlib.sha256(STORY_PATH.read_bytes()).hexdigest(),
    "packet_sha256": hashlib.sha256(packet.encode()).hexdigest(),
    "audience_projection_sha256": hashlib.sha256(audience_projection.encode()).hexdigest(),
    "audience_projection_fields": ["narration", "on_screen_copy", "display_citation"],
    "beat_count": len(projected_records),
    "narration_count": len(projected_records),
    "display_citation_count": len(projected_records),
    "on_screen_leaf_string_count": sum(len(record["on_screen_copy_leaf_strings"]) for record in projected_records),
    "question_count": len(questions),
    "review_scaffolding": {
        "outside_audience_projection": True,
        "elements": ["title", "procedural directions", "beat headings", "labels and bullets", "eight questions"],
        "questions_supply_answers": False,
        "new_declarative_scientific_claims": False,
        "approved_neutral_questions_sha256": approved_questions_sha256,
        "questions_sha256": questions_sha256,
        "exact_reviewed_questions_match": questions_sha256 == approved_questions_sha256,
        "answer_premise_guard": "PASS",
        "answer_premise_hits": question_answer_premise_hits,
    },
    "excluded_fields": ["visual_action", "timed_reveal_states", "state_handoff", "narration_clauses", "verification_sources", "visual_rejections"],
    "records": projected_records,
}
receipt_payload = json.dumps(receipt, indent=2, ensure_ascii=False) + "\n"
if "--check" in sys.argv:
    assert PACKET_PATH.exists() and PACKET_PATH.read_text() == packet
    assert RECEIPT_PATH.exists() and RECEIPT_PATH.read_text() == receipt_payload
    print(f"PASS {PACKET_PATH} {RECEIPT_PATH}")
else:
    PACKET_PATH.write_text(packet)
    RECEIPT_PATH.parent.mkdir(parents=True, exist_ok=True)
    RECEIPT_PATH.write_text(receipt_payload)
    print(PACKET_PATH)
    print(RECEIPT_PATH)
