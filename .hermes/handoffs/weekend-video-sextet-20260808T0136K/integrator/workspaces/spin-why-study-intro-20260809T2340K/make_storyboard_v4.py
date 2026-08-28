#!/usr/bin/env python3
"""Build the v4 why-study storyboard with provisional, non-render timing."""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SCRIPT = ROOT / "narration_script_v4.json"
OUTPUT = ROOT / "storyboard_v4.json"
SECTION_GAPS_AFTER = {"i02", "i03", "i04", "i05", "i06", "s02", "s05", "s10", "s11", "s13", "s16", "s18", "s21"}
LONGO = (
    "A preference for spiral galaxies in one sector of the sky to be left-handed or right-handed spirals "
    "would indicate a parity violating asymmetry in the overall universe and a preferred axis."
)
FORBIDDEN_ASSERTIONS = (
    "we find an asymmetry",
    "we found an asymmetry",
    "this study finds an asymmetry",
    "there is a preferred direction",
    "the universe is anisotropic",
    "parity is violated",
    "observed asymmetry",
    "statistically significant",
    "black-hole",
    "black hole",
)


def words(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", text))


def main() -> int:
    spec = json.loads(SCRIPT.read_text())
    sentences = spec["sentences"]
    ids = [item["id"] for item in sentences]
    if len(ids) != len(set(ids)):
        raise RuntimeError("duplicate sentence id")
    if ids[:6] != ["i01", "i02", "i03", "i04", "i05", "i06"]:
        raise RuntimeError("five-beat why-study introduction is not first")

    opening = " ".join(item["text"] for item in sentences[:6]).lower()
    for required in (
        "same in every direction",
        "no built-in preference",
        "angular momentum",
        "balance is the prediction",
        "would indicate",
        "preferred axis",
        "left unsettled",
        "sorting bias",
        "mirror control",
    ):
        if required not in opening:
            raise RuntimeError(f"missing required opening move: {required}")
    if sentences[3]["text"] != LONGO:
        raise RuntimeError("Longo directional sentence is not verbatim")
    if "would indicate" not in sentences[3]["text"].lower():
        raise RuntimeError("Longo stakes sentence is not conditional")
    if [item.get("beat") for item in sentences[:6]] != [
        "expectation",
        "expectation",
        "tidal-torque",
        "conditional-stakes",
        "open-question",
        "catch-and-handoff",
    ]:
        raise RuntimeError("why-study beats are merged or out of order")
    if any(term in opening for term in ("not reportable", "withheld", "disclaimer", "result is")):
        raise RuntimeError("opening leads with a disclaimer")

    spoken = " ".join(item["text"] for item in sentences).lower()
    forbidden_hits = [term for term in FORBIDDEN_ASSERTIONS if term in spoken]
    if forbidden_hits:
        raise RuntimeError(f"forbidden result assertions: {forbidden_hits}")

    section_words: dict[str, int] = defaultdict(int)
    for item in sentences:
        section_words[item["section"]] += words(item["text"])

    cursor = 0.6
    records = []
    for item in sentences:
        word_count = words(item["text"])
        # Preview timing only. Final timing must come from decoded Alloy PCM sample counts.
        provisional_speech = max(2.6, word_count / 150.0 * 60.0)
        start = cursor
        end = start + provisional_speech
        records.append(
            {
                **item,
                "word_count": word_count,
                "audio_start_seconds": start,
                "audio_end_seconds": end,
                "visual_action_start_seconds": start,
                "timing_status": "PROVISIONAL_NO_AUDIO_DO_NOT_ENCODE",
            }
        )
        cursor = end + 0.75 + (1.5 if item["id"] in SECTION_GAPS_AFTER else 0.0)

    storyboard = {
        "candidate": ROOT.name,
        "revision": spec["revision"],
        "status": "PRE_SYNTHESIS_STORYBOARD_READY",
        "timing_authority": "PROVISIONAL_FOR_STORYBOARD_PREVIEW_ONLY",
        "final_timing_requirement": "Rebuild from freshly decoded Alloy 1.18 PCM sample counts when the managed gateway returns.",
        "predecessor": spec["predecessor"],
        "sentence_count": len(records),
        "word_count": sum(item["word_count"] for item in records),
        "section_word_counts": dict(section_words),
        "mirror_is_progressive_method_peak": True,
        "opening_contract": {
            "broad_reason_before_method": True,
            "first_ids": ids[:6],
            "five_beats_distinct": True,
            "long_source_quote_verbatim": True,
            "non_specialist_question_repeatable": True,
        },
        "claim_boundary": {
            "conditional_stakes_clause": True,
            "open_question_adopts_no_answer": True,
            "forbidden_assertion_hits": [],
            "video_reportable_now": False,
            "primary_source_anchors_frozen": [
                "sources/LONGO_2011_ABSTRACT_EXACT.md",
                "sources/LAND_2008_ABSTRACT_EXACT.md",
                "sources/WHITE_1984_ABSTRACT_EXACT.md"
            ],
            "black_hole_universe_omitted": True,
        },
        "provisional_preview_duration_seconds": cursor + 1.65,
        "records": records,
    }
    OUTPUT.write_text(json.dumps(storyboard, indent=2) + "\n")
    print(
        json.dumps(
            {
                key: storyboard[key]
                for key in (
                    "status",
                    "sentence_count",
                    "word_count",
                    "section_word_counts",
                    "opening_contract",
                    "provisional_preview_duration_seconds",
                )
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
