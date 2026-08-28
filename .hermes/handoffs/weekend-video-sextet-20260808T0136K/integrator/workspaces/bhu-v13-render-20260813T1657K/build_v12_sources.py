#!/usr/bin/env python3
"""Materialize V12's closed-world source and visual-text contract from Lana's redesign spec."""
from __future__ import annotations

import hashlib
import json
import re
from datetime import datetime, timezone
from pathlib import Path

HANDOFF = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-closing-video-20260812T2322K")
V11_STORY = HANDOFF / "STORYBOARD_DRAFT_V11.json"
V11_NARRATION = HANDOFF / "NARRATION_DRAFT_V11.md"
SPEC = HANDOFF / "LANA_VISUAL_REDESIGN_SPEC.md"
V12_STORY = HANDOFF / "STORYBOARD_DRAFT_V12.json"
V12_NARRATION = HANDOFF / "NARRATION_DRAFT_V12.md"
V12_TEXT_CONTRACT = HANDOFF / "V12_VISUAL_TEXT_CONTRACT.json"
V12_SOURCE_RECEIPT = HANDOFF / "V12_SOURCE_FREEZE_RECEIPT.json"
EXPECTED = {
    "STORYBOARD_DRAFT_V11.json": "b0ec6a53061ccea4196df3036bd0ad59e34ef50814b92dd3ec16cf0e4794f7c4",
    "NARRATION_DRAFT_V11.md": "027a6e17fcb3c7d3708177b8fa30078735c11cc4157f6b44edfacceef7bb8535",
    "LANA_VISUAL_REDESIGN_SPEC.md": "cf9cefe8a0c07f8cc960388004a20d4518a7cf7fbcea5ff688825ffdc47bfd22",
}
PLANNED = {"01": 36, "02": 38, "03": 42, "04": 47, "05": 44, "06": 29, "07": 32, "08": 34, "09": 30, "10": 33, "11": 37}
CREW_TERMS = ("duho", "lana", "goru", "kun", "hwao", "yui", "tori", "fable")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def text(role: str, value: str, reveal: str = "frame_zero", **extra) -> dict:
    return {"role": role, "text": value, "reveal": reveal, **extra}


CONTRACT = {
    "01": {
        "anchor": "ROUTE CLOSED",
        "viewer_text": [
            text("safety_badge", "A PERSONAL SIDE-QUESTION · NOT PART OF THE LAB'S RESEARCH PROGRAMME", "frame_zero", persistent_full_card=True),
            text("anchor", "ROUTE CLOSED", "route_verdict"),
        ],
        "picture": "An open book forks into a checkable-star road and a galaxy-fog road; a gate closes across only the fog road and remains intact.",
        "blur_claim": "Two source-reading roads differ; the fog route closes without demolition.",
        "generated": ["open book", "roads", "fog", "checkable star", "gate prop"],
        "deterministic": ["fork chronology", "gate-closing motion", "badge and anchor"],
        "named_dwell": "route gate closes",
    },
    "02": {
        "anchor": "FIVE IDEAS — NO SHARED PREDICTION",
        "viewer_text": [
            text("root_label", "BLACK-HOLE UNIVERSE (BHU)", "bhu"),
            text("tile_caption", "CLOSED UNIVERSE", "proposal_1"),
            text("tile_caption", "COLLAPSE BOUNCE", "proposal_2"),
            text("tile_caption", "INHERITED SPIN", "proposal_3"),
            text("tile_caption", "REPRODUCING UNIVERSES", "proposal_4"),
            text("tile_caption", "DISTINCT FINGERPRINTS", "proposal_5"),
            text("anchor", "FIVE IDEAS — NO SHARED PREDICTION", "no_shared_forecast"),
        ],
        "picture": "Five icon tiles light in spoken order and send arrows to five visibly different endpoints.",
        "blur_claim": "One root fans into five unlike mechanisms whose outputs do not reconverge.",
        "generated": ["nested universes", "bounce", "handed-down spinning top", "universe family tree", "unlike fingerprints"],
        "deterministic": ["tile reveal timing", "five diverging arrow endpoints", "all text"],
        "named_dwell": "fifth tile lights; five arrows end apart",
    },
    "03": {
        "anchor": None,
        "viewer_text": [],
        "picture": "A glowing orb throws a dart at a board and can miss; the board disappears and the next dart sails into empty space; two differently colored orbs then land darts on one board.",
        "blur_claim": "A test requires something missable, and a shared hit cannot identify the thrower.",
        "generated": ["dartboard", "darts", "two glowing orbs"],
        "deterministic": ["three-beat motion logic", "board removal", "dart trajectories"],
        "named_dwell": "two-archers beat",
    },
    "04": {
        "anchor": None,
        "viewer_text": [text("quotation", "“SERIOUS DOUBT OR SIMPLY FALSIFY” — BROWN, LEE & RHO", "source_quote")],
        "picture": "A star inflates and rises through a deterministic column of sun units until it meets a hard lid at one-and-a-half suns; two suns sit above the lid beside the source quote.",
        "blur_claim": "A proposed star-mass ceiling lies below the source-named two-sun consequence regime.",
        "generated": ["inflating star prop", "painterly backdrop"],
        "deterministic": ["entire mass gauge", "sun-unit positions", "lid", "two-sun zone", "motion", "quotation"],
        "named_dwell": "rising star meets the lid",
        "quantitative_card": True,
    },
    "05": {
        "anchor": "AT 95.4% CREDIBILITY, THE CLOSING RECORD STATES ONLY THAT THE RESULT DOES NOT CLEAR 2.00",
        "viewer_text": [
            text("chart_data", "1.97 ± 0.04 M☉", "demorest_uncertainty"),
            text("chart_data", "2.08 ± 0.07 M☉", "fonseca_uncertainty"),
            text("chart_data", "68.3%", "percent_68_3"),
            text("anchor", "AT 95.4% CREDIBILITY, THE CLOSING RECORD STATES ONLY THAT THE RESULT DOES NOT CLEAR 2.00", "percent_95_4"),
        ],
        "picture": "A deterministic mass chart uses sun-icon units, two measured bars, and an open-ended uncertainty gradient that widens and fades continuously through two suns.",
        "blur_claim": "Two uncertainty bars approach/cross two suns; the stricter treatment becomes an unresolved open fade rather than a fabricated endpoint.",
        "generated": ["non-observational painterly atmosphere only"],
        "deterministic": ["entire chart", "axis", "sun units", "bars", "centres", "values", "68.3% state", "95.4% fade", "anchor"],
        "named_dwell": "widening band and its fade",
        "quantitative_card": True,
    },
    "06": {
        "anchor": None,
        "viewer_text": [
            text("quotation", "SERIOUS DOUBT", "source_disjunction"),
            text("quotation_join", "OR", "source_disjunction"),
            text("quotation", "SIMPLY FALSIFY", "source_disjunction"),
        ],
        "picture": "The road forks beneath a two-armed signpost; the returning measurement marker reaches the fork and stops without choosing.",
        "blur_claim": "Two source-named readings remain unresolved because the traveller stops at the fork.",
        "generated": ["fork road", "signpost", "walking/measurement figure"],
        "deterministic": ["arrival and stop timing", "quotation text"],
        "named_dwell": "stopping at the fork",
    },
    "07": {
        "anchor": None,
        "viewer_text": [text("missing_value", "?", "no_amplitude")],
        "picture": "Two stacks of stylized spiral galaxies rotate in opposite senses; one stack is visibly taller, while only a question mark occupies the gap.",
        "blur_claim": "The source says the counts differ but supplies no magnitude for the gap.",
        "generated": ["stylized spiral-galaxy icon"],
        "deterministic": ["stack heights", "rotation arrows", "question-mark gap"],
        "named_dwell": "unequal stacks; question-mark gap",
    },
    "08": {
        "anchor": None,
        "viewer_text": [
            text("chart_data", "2025", "timeline"),
            text("missing_value", "?", "forecast_blanks", repeat=4),
        ],
        "picture": "Survey-photo icons land on a timeline before a later paper speech-bubble; then four empty props appear: blank ruler, blank map, needleless compass, needleless pass/fail meter.",
        "blur_claim": "The claim comes after the cited material and leaves four prediction slots empty.",
        "generated": ["stylized survey-photo icon", "paper and speech bubble", "four empty props"],
        "deterministic": ["timeline ordering", "2025 tag", "empty-slot reveal chronology"],
        "named_dwell": "four empty slots revealed",
    },
    "09": {
        "anchor": "MEASUREMENT ≠ IDENTIFICATION",
        "viewer_text": [text("anchor", "MEASUREMENT ≠ IDENTIFICATION", "measurement_not_identification")],
        "picture": "One footprint lies between three different unlabeled animal silhouettes; a pointer from the print splits toward all three.",
        "blur_claim": "One trace can have several possible makers, so the trace cannot identify one cause.",
        "generated": ["footprint", "three unlabeled animal silhouettes"],
        "deterministic": ["three-way pointer split", "anchor"],
        "named_dwell": "three animals appear over one footprint",
    },
    "10": {
        "anchor": None,
        "viewer_text": [],
        "picture": "The card-01 gate returns; a blank-ruler lock and footprint lock close onto it in sequence.",
        "blur_claim": "The route is locked by the two failures already learned: no calibrated size and no unique cause.",
        "generated": ["reused gate and lock props"],
        "deterministic": ["reused blank-ruler and footprint lock faces", "two lock clicks"],
        "named_dwell": "two locks close the gate",
    },
    "11": {
        "anchor": "REOPENS ONLY WITH A NUMBER — OR A FINGERPRINT",
        "viewer_text": [text("anchor", "REOPENS ONLY WITH A NUMBER — OR A FINGERPRINT", "reopen")],
        "picture": "The locked gate has two keyholes; a ruler-range key and fingerprint key fit them, while the unequal-stack token fits neither.",
        "blur_claim": "The current token cannot reopen the route; either of two missing keys could.",
        "generated": ["ruler-blade key", "fingerprint key"],
        "deterministic": ["keyholes", "fit/refusal motion", "reused unequal-stack token", "anchor"],
        "named_dwell": "keys tried; final hold on gate",
    },
}


def main() -> int:
    for name, expected in EXPECTED.items():
        path = HANDOFF / name
        actual = sha(path)
        if actual != expected:
            raise RuntimeError(f"authority drift {name}: {actual}")
    story11 = json.loads(V11_STORY.read_text())
    if {card["id"] for card in story11["cards"]} != set(CONTRACT):
        raise RuntimeError("card set mismatch")
    if sum(PLANNED.values()) != 402:
        raise RuntimeError("V12 plan must total 402 seconds")

    story12 = {
        "title": story11["title"],
        "slug": story11["slug"],
        "version": "V12",
        "status": "V12_BUILT_FROM_LANA_VISUAL_REDESIGN_SPEC_AWAITING_FULL_THREE_SEAT_GATE",
        "authority": {
            "redesign_spec": str(SPEC),
            "redesign_spec_sha256": EXPECTED[SPEC.name],
            "base_storyboard": str(V11_STORY),
            "base_storyboard_sha256": EXPECTED[V11_STORY.name],
            "base_narration": str(V11_NARRATION),
            "base_narration_sha256": EXPECTED[V11_NARRATION.name],
        },
        "render_contract": {
            "resolution": "1920x1080",
            "fps": 30,
            "assertion_heading_every_card": False,
            "global_card_heading": False,
            "global_card_counter": False,
            "burned_caption_box": False,
            "target_narration_wpm": 142,
            "allowed_wpm_band": [135, 150],
            "embedded_subtitle_stream_required": True,
            "embedded_subtitle_codec": "mov_text",
            "exact_srt_sidecar_required": True,
            "exact_vtt_sidecar_required": True,
            "generated_stills_allowed_for_non_claim_bearing_illustration": True,
            "generated_video_preferred": False,
            "generated_text_allowed": False,
            "generated_quantitative_pixels_allowed": False,
            "viewer_text_policy": "closed-world per-card lists; any unlisted string is forbidden",
            "blur_test_required_all_cards": True,
            "upload_authorized": False,
            "publication_authorized": False,
        },
        "metaphor_kit": {
            "mass": "sun icons",
            "route": "road and gate",
            "testability": "dartboard",
            "underdetermination": "footprint",
            "closure_reopening": "locks and keys",
        },
        "cards": [],
        "estimated_duration_seconds": 402,
    }
    text_contract = {
        "status": "V12_CLOSED_WORLD_VIEWER_TEXT_CONTRACT",
        "authority_sha256": EXPECTED[SPEC.name],
        "rules": {
            "unlisted_text_forbidden": True,
            "captions_are_subtitle_stream_and_sidecars_not_burned_frame_text": True,
            "generated_text_forbidden": True,
            "crew_terms_forbidden": list(CREW_TERMS),
        },
        "cards": {},
    }
    for card11 in story11["cards"]:
        card_id = card11["id"]
        contract = CONTRACT[card_id]
        permitted = [item["text"] for item in contract["viewer_text"]]
        if any(len(item["text"].split()) > 2 for item in contract["viewer_text"] if item["role"] == "tile_caption"):
            raise RuntimeError(f"Card {card_id} tile caption over two words")
        old_strings = [card11["heading"], *card11.get("on_screen_support", [])]
        deleted = [value for value in old_strings if value not in permitted]
        card12 = {
            "id": card_id,
            "planned_seconds": PLANNED[card_id],
            "source_claims": card11["source_claims"],
            "packet_lines": card11["packet_lines"],
            "narration": card11["narration"],
            "narration_sha256": hashlib.sha256(card11["narration"].encode()).hexdigest(),
            "legacy_heading_metadata_only": card11["heading"],
            "assertion_heading_viewer_facing": False,
            "viewer_text": contract["viewer_text"],
            "deleted_v11_viewer_text": deleted,
            "picture": contract["picture"],
            "blur_test_expected_claim": contract["blur_claim"],
            "generated_layer": contract["generated"],
            "deterministic_layer": contract["deterministic"],
            "named_dwell_event": contract["named_dwell"],
            "quantitative_card": contract.get("quantitative_card", False),
        }
        story12["cards"].append(card12)
        text_contract["cards"][card_id] = {
            "permitted": contract["viewer_text"],
            "forbidden_legacy_strings": deleted,
        }

    public_blob = " ".join(
        item["text"] for card in story12["cards"] for item in card["viewer_text"]
    ).lower()
    crew_hits = [name for name in CREW_TERMS if re.search(rf"\b{re.escape(name)}\b", public_blob)]
    if crew_hits:
        raise RuntimeError(f"crew terms in viewer contract: {crew_hits}")
    if "cns" in public_blob:
        raise RuntimeError("unearned CNS in viewer contract")

    V12_STORY.write_text(json.dumps(story12, indent=2, ensure_ascii=False) + "\n")
    V12_TEXT_CONTRACT.write_text(json.dumps(text_contract, indent=2, ensure_ascii=False) + "\n")

    lines = [
        "# BHU closure video — narration V12",
        "",
        "Status: V12 source frozen for build and full three-seat exact-hash gate.",
        "",
        f"Visual-redesign authority: `LANA_VISUAL_REDESIGN_SPEC.md`, SHA-256 `{EXPECTED[SPEC.name]}`.",
        f"Narration authority: V11 SHA-256 `{EXPECTED[V11_NARRATION.name]}`; all 11 card payloads remain word-for-word identical.",
        "",
    ]
    for card11 in story11["cards"]:
        lines.extend([
            f"## Card {card11['id']}",
            "",
            card11["narration"],
            "",
            f"Source: {', '.join(card11['source_claims'])}; packet lines {', '.join(card11['packet_lines'])}.",
            "",
        ])
    lines.extend([
        "## Generation boundary",
        "",
        "Generated stills may carry metaphor or atmosphere only. All numbers, quantitative geometry, labels, quotations, anchors, captions, and semantic motion are local deterministic composites. Generated text and generated quantitative pixels are forbidden.",
        "",
    ])
    V12_NARRATION.write_text("\n".join(lines))

    # Re-read exact bytes and prove the 11 spoken payloads are unchanged.
    story12_live = json.loads(V12_STORY.read_text())
    narration_match = all(a["narration"] == b["narration"] for a, b in zip(story11["cards"], story12_live["cards"]))
    if not narration_match:
        raise RuntimeError("V12 narration payload drift")
    receipt = {
        "status": "PASS_V12_SOURCE_FREEZE_EXACT_V11_NARRATION_NEW_CLOSED_WORLD_VISUAL_CONTRACT",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "authority": {name: {"path": str(HANDOFF / name), "sha256": digest} for name, digest in EXPECTED.items()},
        "outputs": {
            V12_STORY.name: {"path": str(V12_STORY), "sha256": sha(V12_STORY), "bytes": V12_STORY.stat().st_size},
            V12_NARRATION.name: {"path": str(V12_NARRATION), "sha256": sha(V12_NARRATION), "bytes": V12_NARRATION.stat().st_size},
            V12_TEXT_CONTRACT.name: {"path": str(V12_TEXT_CONTRACT), "sha256": sha(V12_TEXT_CONTRACT), "bytes": V12_TEXT_CONTRACT.stat().st_size},
        },
        "checks": {
            "all_11_narration_payloads_word_for_word_equal_v11": narration_match,
            "planned_duration_seconds": sum(card["planned_seconds"] for card in story12_live["cards"]),
            "assertion_heading_every_card_retired": not story12_live["render_contract"]["assertion_heading_every_card"],
            "closed_world_text_contract": story12_live["render_contract"]["viewer_text_policy"],
            "subtitle_stream_presence_gate_required": story12_live["render_contract"]["embedded_subtitle_stream_required"],
            "generated_quantitative_pixels_forbidden": not story12_live["render_contract"]["generated_quantitative_pixels_allowed"],
            "crew_term_hits": crew_hits,
        },
    }
    V12_SOURCE_RECEIPT.write_text(json.dumps(receipt, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps(receipt, indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
