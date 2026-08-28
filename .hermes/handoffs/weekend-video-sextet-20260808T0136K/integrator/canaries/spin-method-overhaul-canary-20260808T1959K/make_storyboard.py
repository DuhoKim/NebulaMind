#!/usr/bin/env python3
"""Build the audio-blocked v3 storyboard with provisional, non-render timing."""
from __future__ import annotations

import json
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent
SCRIPT = ROOT / "narration_script_v3.json"
OUTPUT = ROOT / "storyboard_v3.json"
SECTION_GAPS_AFTER = {"i04", "s02", "s05", "s10", "s11", "s13", "s16", "s18", "s21"}
FORBIDDEN = (
    "significance",
    "dipole",
    "parity",
    "cosmology",
    "grb",
    "sn ia",
    "dark energy",
    "quasar",
    "h0",
    "black-hole",
    "black hole",
    "desi",
    "ganalyzer",
)


def words(text: str) -> int:
    return len(re.findall(r"\b[\w'-]+\b", text))


def main() -> int:
    spec = json.loads(SCRIPT.read_text())
    sentences = spec["sentences"]
    ids = [item["id"] for item in sentences]
    if len(ids) != len(set(ids)):
        raise RuntimeError("duplicate sentence id")
    if ids[:4] != ["i01", "i02", "i03", "i04"]:
        raise RuntimeError("four-move introduction is not first")

    opening = " ".join(item["text"] for item in sentences[:4]).lower()
    for required in (
        "two handednesses",
        "sky",
        "fact about the universe",
        "humans sorted",
        "fact about the sorters",
        "how do we tell",
    ):
        if required not in opening:
            raise RuntimeError(f"missing required opening move: {required}")
    if not all(token in sentences[1]["text"].lower() for token in ("if", "were", "would")):
        raise RuntimeError("universe clause is not explicitly conditional")
    if "could" not in sentences[2]["text"].lower():
        raise RuntimeError("sorters clause is not explicitly conditional")
    if any(term in opening for term in ("not reportable", "withheld", "disclaimer", "result is")):
        raise RuntimeError("opening leads with a disclaimer")

    spoken = " ".join(item["text"] for item in sentences).lower()
    forbidden_hits = [term for term in FORBIDDEN if re.search(rf"(?<!\w){re.escape(term)}(?!\w)", spoken)]
    if forbidden_hits:
        raise RuntimeError(f"forbidden narration terms: {forbidden_hits}")

    section_words: dict[str, int] = defaultdict(int)
    for item in sentences:
        section_words[item["section"]] += words(item["text"])
    mirror_words = section_words["mirror-climax"]
    other_peak = max(value for key, value in section_words.items() if key != "mirror-climax")
    if mirror_words <= other_peak:
        raise RuntimeError(f"mirror is not the spoken peak: mirror={mirror_words}, other={other_peak}")

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
        "status": "BLOCKED_BEFORE_SYNTHESIS_OPENAI_AUDIO_GATEWAY_UNAVAILABLE",
        "timing_authority": "PROVISIONAL_FOR_STORYBOARD_PREVIEW_ONLY",
        "final_timing_requirement": "Rebuild from freshly decoded Alloy 1.18 PCM sample counts when the managed gateway returns.",
        "predecessor": spec["predecessor"],
        "sentence_count": len(records),
        "word_count": sum(item["word_count"] for item in records),
        "section_word_counts": dict(section_words),
        "mirror_is_spoken_peak_by_word_count": True,
        "opening_required_terms": {
            "sky": spoken.count("sky"),
            "universe": spoken.count("universe"),
            "fact_about": spoken.count("fact about"),
            "sorters": spoken.count("sorters"),
        },
        "claim_boundary": {
            "conditional_universe_clause": True,
            "conditional_sorters_clause": True,
            "forbidden_narration_hits": [],
            "video_reportable_now": False,
            "no_new_source_citation": True,
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
                    "opening_required_terms",
                    "provisional_preview_duration_seconds",
                )
            },
            indent=2,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
