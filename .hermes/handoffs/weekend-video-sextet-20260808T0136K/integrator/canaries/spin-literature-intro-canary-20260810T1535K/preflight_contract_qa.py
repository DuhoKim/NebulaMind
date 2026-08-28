#!/usr/bin/env python3
"""Fail-closed contract QA for the Spin v5 literature-only revision."""
from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent
HANDOFF = ROOT.parents[2]
SCRIPT = ROOT / "narration_script_v5.json"
MANIFEST = ROOT / "source_manifest_v5.json"
REPORT = ROOT / "PRE_SYNTHESIS_CONTRACT_QA.json"
PREDECESSOR_WORKSPACE = ROOT.parent / "spin-why-study-intro-20260809T2340K"
PREDECESSOR_CANARY = ROOT.parents[1] / "canaries/spin-method-overhaul-canary-20260809T2340K"

OPENING_IDS = ["i01", "i02", "i03", "i04", "i05l", "i05s", "i05d", "i05u", "i06"]
LONGO_CONDITIONAL = (
    "A preference for spiral galaxies in one sector of the sky to be left-handed or right-handed spirals "
    "would indicate a parity violating asymmetry in the overall universe and a preferred axis."
)
QUOTES = {
    "i05l": (
        "Longo reported: ",
        "An unbinned analysis for a dipole component that made no prior assumptions for the dipole axis gives a dipole asymmetry of −0.0408±0.011 with a probability of occurring by chance of 7.9×10⁻⁴.",
    ),
    "i05s": (
        "Shamir reported: ",
        "The results show that the local universe (z<0.3) is not isotropic in terms of galaxy spin, with probability P<5.8×10⁻⁶ of such asymmetry to occur by chance.",
    ),
    "i05d": (
        "Land and colleagues reported: ",
        "After establishing and correcting for a certain level of bias in our handedness results we find the winding sense of the galaxies to be consistent with statistical isotropy.",
    ),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> int:
    script = json.loads(SCRIPT.read_text())
    manifest = json.loads(MANIFEST.read_text())
    predecessor_script = json.loads((PREDECESSOR_WORKSPACE / "narration_script_v4.json").read_text())
    by_id = {item["id"]: item for item in script["sentences"]}
    narration = " ".join(item["text"] for item in script["sentences"]).lower()
    current_method = [item for item in script["sentences"] if item["id"].startswith("s")]
    predecessor_method = [item for item in predecessor_script["sentences"] if item["id"].startswith("s")]
    renderer = (ROOT / "build.py").read_text()

    manifest_input_hashes_match = all(
        Path(item["path"]).is_file() and sha256(Path(item["path"])) == item["sha256"]
        for item in manifest["candidate_inputs"]
    )
    non_literature_text = " ".join(
        item["text"].lower()
        for item in script["sentences"]
        if item["id"] not in {"i04", "i05l", "i05s", "i05d"}
    )
    unqualified_result_terms = (
        "we find an asymmetry",
        "we found an asymmetry",
        "this study finds an asymmetry",
        "there is a preferred direction",
        "parity is violated",
        "statistically significant",
    )
    checks = {
        "opening_ids_exact": [item["id"] for item in script["sentences"][: len(OPENING_IDS)]] == OPENING_IDS,
        "five_beat_arc_exact": [item.get("beat") for item in script["sentences"][: len(OPENING_IDS)]]
        == ["expectation", "expectation", "tidal-torque", "conditional-stakes", "open-question", "open-question", "open-question", "open-question", "catch-and-handoff"],
        "conditional_longo_sentence_unchanged": by_id["i04"]["text"] == LONGO_CONDITIONAL,
        "three_primary_sentences_verbatim_and_attributed": all(
            by_id[quote_id]["text"] == prefix + quote for quote_id, (prefix, quote) in QUOTES.items()
        ),
        "land_null_not_settled": "remains disputed" in by_id["i05u"]["text"].lower()
        and "adopts none" in by_id["i05u"]["text"].lower(),
        "no_superseded_topic_in_narration": not any(
            term in narration for term in ("black hole", "black-hole", "black_hole", "bhu")
        ),
        "no_unqualified_result_claim_outside_attributed_quotes": not any(
            term in non_literature_text for term in unqualified_result_terms
        ),
        "method_spine_script_unchanged": current_method == predecessor_method,
        "alloy_1_18_exact": script["voice"] == "alloy" and script["speed"] == 1.18,
        "forbidden_icon_primitives_hardening_carried": script["forbidden_icon_primitives"] == ["curve"]
        and "elif kind == \"curve\"" not in renderer
        and "elif kind == 'curve'" not in renderer,
        "why_it_matters_rail_fix_carried": all(
            token in renderer
            for token in ("WHY IT MATTERS", "focus_left", "focus_right", "glow =", "9 + int(round(math.sin(math.pi * t)))")
        ),
        "no_answer_selected_header_carried": "WHY-STUDY QUESTION · NO ANSWER SELECTED" in renderer,
        "method_spine_renderer_functions_carried": all(
            token in renderer
            for token in ("def draw_question", "def draw_two_worlds", "def draw_mirror", "def draw_discipline_freeze", "def draw_funnel", "def draw_equation", "def draw_controls", "def draw_boundary", "def draw_payoff")
        ),
        "superseded_draft_not_copied_into_workspace": not (ROOT / "sources/LANA_SPIN_BHU_BEAT_DRAFT_20260810.md").exists(),
        "manifest_input_hashes_match": manifest_input_hashes_match,
        "predecessor_video_preserved": sha256(PREDECESSOR_CANARY / "spin-method-overhaul-canary-20260809T2340K.mp4")
        == "4d230cc0efca0eb68a8d027d614b6b7e500590cff06154f1514d4402a84d7078",
        "predecessor_script_preserved": sha256(PREDECESSOR_CANARY / "narration_script_v4.json")
        == "5df1d0a20e1feede746a82cd784ecd43c5cd1f21ebcc74d5418cbb87d69e90f1",
        "closed_human_acceptance_gate": script["video_reportable_now"] is False
        and manifest["closed_gates"]["human_watch_acceptance_conferred"] is False,
    }
    report = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "status": "PASS_PRE_SYNTHESIS_CONTRACT" if all(checks.values()) else "HOLD_PRE_SYNTHESIS_CONTRACT",
        "script_sha256": sha256(SCRIPT),
        "source_manifest_sha256": sha256(MANIFEST),
        "checks": checks,
    }
    REPORT.write_text(json.dumps(report, indent=2) + "\n")
    print(json.dumps(report, indent=2))
    return 0 if all(checks.values()) else 1


if __name__ == "__main__":
    raise SystemExit(main())
