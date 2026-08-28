#!/usr/bin/env python3
"""Verify the exact BHU V10→V11 Lana retiming delta and full pacing audit.

Writes only deterministic V11 verification/audit JSON. It does not generate
speech, frames, video, uploads, publication state, or render authority.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

D = Path(__file__).resolve().parent
V10 = {
    "story": (D / "STORYBOARD_DRAFT_V10.json", "dc853f90c3299c5e1c051c0c37a45b6612f5418eaa9bbaad63608fd10ec56ae9"),
    "narration": (D / "NARRATION_DRAFT_V10.md", "4324c9b73de038e760c67e80fee70b60656599cf22d95cb1d92167e818f5ef75"),
    "ledger": (D / "CLAIM_LINE_LEDGER_V10.md", "aa4b459a3b4112dc40feabb5e84a0853e205db400d0adfc9d58cab248f6cc9aa"),
    "graphics": (D / "DETERMINISTIC_DIAGRAM_SPEC_V10.md", "e296e2f29a00cf714cbc9f562bb224d224e185fb8d6a5ecb03e718cf5e1cc52e"),
}
V10_CONTROLS = {
    "V10_WPM_AUDIT.json": "5ca591ca336e991381662d865a9cb8a3434829d097af73427d0c3c32b6457678",
    "V10_SHORTHAND_AUDIT.json": "ec8a8d2095785b0db936fbdd009da0872a086d9a5acb82c3b02b9bfb2095224c",
    "V10_FREEZE_RECEIPT.json": "2bc19869459219c9909691b33c174bf32e17ebfe8f6f9e13f42c7d14da66da13",
    "LANA_CONFIRM_V10.md": "436e5596f8ef874d7bb5ec0945327e0bef7106c82badce4ceef93926c30008c4",
    "GORU_CONFIRM_V10.md": "4c65cebcf6a99e268ed59218a64f064f6641526599c14fa441717a4f10efcff3",
    "KUN_CONFIRM_V10.md": "48a53432753041ca7acfc0b5a46424c8ee7adacb8edd7d7e6d364524039d9fff",
}
V11 = {
    "story": D / "STORYBOARD_DRAFT_V11.json",
    "narration": D / "NARRATION_DRAFT_V11.md",
    "ledger": D / "CLAIM_LINE_LEDGER_V11.md",
    "graphics": D / "DETERMINISTIC_DIAGRAM_SPEC_V11.md",
}
EXPECTED_V11 = {
    "story": "b0ec6a53061ccea4196df3036bd0ad59e34ef50814b92dd3ec16cf0e4794f7c4",
    "narration": "027a6e17fcb3c7d3708177b8fa30078735c11cc4157f6b44edfacceef7bb8535",
    "ledger": "aa4b459a3b4112dc40feabb5e84a0853e205db400d0adfc9d58cab248f6cc9aa",
    "graphics": "e296e2f29a00cf714cbc9f562bb224d224e185fb8d6a5ecb03e718cf5e1cc52e",
}
OLD_CARD01 = (
    "Could our universe be inside a black hole? It's a question we were personally curious about — "
    "a side-interest, not part of the lab's research programme. We read the original scientific "
    "papers to see what they actually predict. One of these ideas gives us a number we can check "
    "against real stars. For galaxy spin, the sources give no expected size for the effect, and even "
    "a perfect measurement couldn't tell us a black hole was the cause. So this route closes. The "
    "idea is not declared true or false."
)
NEW_CARD01 = (
    "Could our universe be inside a black hole? It's a personal side-interest — not part of the lab's "
    "research programme. We read the original papers to see what they actually predict. One idea "
    "gives us a number to check against real stars. For galaxy spin, the sources give no expected "
    "size for the effect — and even a perfect measurement couldn't tell us a black hole was the "
    "cause. So this route closes. The idea is not declared true or false."
)
EXPECTED_TIMINGS = {
    "01": 38, "02": 40, "03": 42, "04": 48, "05": 51, "06": 29,
    "07": 33, "08": 35, "09": 29, "10": 36, "11": 34,
}
LOCAL_NAMES = re.compile(r"(?i)(?<![A-Za-z0-9])(?:duho|lana|goru|kun|tori|yui|hwao)(?![A-Za-z0-9])")
MEDIA_SUFFIXES = {
    ".wav", ".mp3", ".m4a", ".aac", ".mp4", ".mov", ".mkv",
    ".png", ".jpg", ".jpeg", ".webp", ".srt", ".vtt",
}


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SystemExit("HOLD: " + message)


def diffs(a: Any, b: Any, path: str = "") -> list[str]:
    if type(a) is not type(b):
        return [path]
    if isinstance(a, dict):
        if list(a) != list(b):
            return [path + ".<keys>"]
        out: list[str] = []
        for key in a:
            child = f"{path}.{key}" if path else key
            out.extend(diffs(a[key], b[key], child))
        return out
    if isinstance(a, list):
        if len(a) != len(b):
            return [path + ".<length>"]
        out = []
        for index, (left, right) in enumerate(zip(a, b)):
            out.extend(diffs(left, right, f"{path}[{index}]"))
        return out
    return [] if a == b else [path]


def card_by_id(story: dict[str, Any], card_id: str) -> dict[str, Any]:
    return next(card for card in story["cards"] if card["id"] == card_id)


for path, expected in V10.values():
    require(path.exists() and sha(path) == expected, f"pinned V10 target drift: {path.name}")
for name, expected in V10_CONTROLS.items():
    path = D / name
    require(path.exists() and sha(path) == expected, f"pinned V10 authority/control drift: {name}")
for key, path in V11.items():
    require(path.exists() and sha(path) == EXPECTED_V11[key], f"V11 target drift: {path.name}")

v10 = json.loads(V10["story"][0].read_text())
v11 = json.loads(V11["story"].read_text())
changed = diffs(v10, v11)
expected_changed = [
    "cards[0].planned_seconds",
    "cards[0].narration",
    "cards[1].planned_seconds",
    "cards[2].planned_seconds",
    "cards[6].planned_seconds",
    "cards[8].planned_seconds",
    "estimated_duration_seconds",
]
require(changed == expected_changed, f"canonical V10→V11 delta is not exact: {changed}")
require(card_by_id(v10, "01")["narration"] == OLD_CARD01, "V10 Card 01 narration anchor drift")
require(card_by_id(v11, "01")["narration"] == NEW_CARD01, "V11 Card 01 narration is not Lana's verbatim text")
require({card["id"]: card["planned_seconds"] for card in v11["cards"]} == EXPECTED_TIMINGS, "V11 planned_seconds table drift")
require(v10["estimated_duration_seconds"] == 399, "V10 aggregate duration anchor drift")
require(v11["estimated_duration_seconds"] == 415, "V11 aggregate duration is not 415")
require(v11["estimated_duration_seconds"] == sum(c["planned_seconds"] for c in v11["cards"]), "V11 aggregate duration is stale")

# Every canonical field outside Lana's exact authorized delta remains unchanged.
allowed_by_card = {
    "01": {"narration", "planned_seconds"},
    "02": {"planned_seconds"},
    "03": {"planned_seconds"},
    "07": {"planned_seconds"},
    "09": {"planned_seconds"},
}
for old, new in zip(v10["cards"], v11["cards"]):
    require(old["id"] == new["id"], "card order or ID changed")
    for key in old:
        if key in allowed_by_card.get(old["id"], set()):
            continue
        require(old[key] == new[key], f"unauthorized Card {old['id']} field changed: {key}")

v10_narr = V10["narration"][0].read_text()
v11_narr = V11["narration"].read_text()
require(v10_narr.count(OLD_CARD01) == 1, "V10 standalone Card 01 anchor count is not one")
require(v11_narr == v10_narr.replace(OLD_CARD01, NEW_CARD01), "standalone narration changed beyond Card 01 replacement")
require(V11["ledger"].read_bytes() == V10["ledger"][0].read_bytes(), "claim ledger is not byte-identical")
require(V11["graphics"].read_bytes() == V10["graphics"][0].read_bytes(), "graphics spec is not byte-identical")

# Standalone headings and spoken narration remain exact mirrors of the storyboard.
parts = re.split(r"## Card (\d+) — assertion heading\n", v11_narr)[1:]
seen: dict[str, tuple[str, str]] = {}
for index in range(0, len(parts), 2):
    card_id, block = parts[index], parts[index + 1]
    heading = block.split("**", 2)[1]
    narration = block.split("**", 2)[2].split("\n\nSource:", 1)[0].strip()
    seen[card_id] = (heading, narration)
require(len(seen) == 11, f"standalone narration parsed {len(seen)} cards, not 11")
for card in v11["cards"]:
    require(seen.get(card["id"]) == (card["heading"], card["narration"]), f"V11 narration divergence Card {card['id']}")

# Complete audience projection for names, internal vocabulary, citations, and shorthand.
audience: list[tuple[str, str]] = []
for card in v11["cards"]:
    for key in ("heading", "narration", "diagram"):
        audience.append((f"cards[{card['id']}].{key}", card[key]))
    for index, value in enumerate(card["on_screen_support"]):
        audience.append((f"cards[{card['id']}].on_screen_support[{index}]", value))
projection = "\n".join(value for _, value in audience)
require(not [(path, hit.group(0)) for path, value in audience for hit in LOCAL_NAMES.finditer(value)], "viewer-facing local name returned")
for term in ("packet", "ledger", "receipt", "lane", "seat", "freeze"):
    require(not [(path, term) for path, value in audience if re.search(rf"(?i)\b{term}\b", value)], f"viewer internal term returned: {term}")
for author in ("Brown", "Lee", "Rho", "Demorest", "Fonseca"):
    require(author.lower() in projection.lower(), f"published-author citation lost: {author}")

# Lana/Kun opening invariants: both spoken markers and the unchanged frame-one badge.
card01_v10 = card_by_id(v10, "01")
card01_v11 = card_by_id(v11, "01")
require("personal side-interest" in card01_v11["narration"].lower(), "Card 01 personal-side-interest marker lost")
require("not part of the lab's research programme" in card01_v11["narration"].lower(), "Card 01 lab-programme boundary lost")
require(card01_v11["on_screen_support"] == card01_v10["on_screen_support"], "Card 01 on-screen boundary badge/support changed")
require(card01_v11["on_screen_support"][0] == "A PERSONAL SIDE-QUESTION · NOT PART OF THE LAB'S RESEARCH PROGRAMME", "Card 01 boundary badge text drift")
require(card01_v11["diagram"] == card01_v10["diagram"], "Card 01 diagram/reveal instruction changed")
require("visible from frame one for the full card" in card01_v11["diagram"].lower(), "Card 01 frame-one full-card badge instruction lost")
require("So this route closes. The idea is not declared true or false." in card01_v11["narration"], "Card 01 route verdict boundary lost")
require(not re.search(r"(?<![A-Za-z0-9])(?:BHU|CNS|CW|CCW)(?![A-Za-z0-9])", card01_v11["narration"]), "Card 01 introduced an initialism")

# Current shorthand inventory has no CNS exception and is unchanged in meaning.
require(not re.search(r"(?<![A-Za-z0-9])CNS(?![A-Za-z0-9])", projection), "viewer-facing CNS returned")
initialisms = [
    {
        "form": "BHU",
        "meaning": "black-hole universe",
        "first_viewer_card": "02",
        "spoken_expansion_card": "02",
        "spoken_witness": "black-hole universe, or BHU for short",
        "status": "EARNED_IN_BREATH_REVEAL_MUST_BE_SYNCHRONIZED",
        "render_timing": "Reveal BLACK-HOLE UNIVERSE (BHU) no earlier than the witness phrase.",
    },
    {
        "form": "CW/CCW",
        "meaning": "clockwise/counterclockwise",
        "first_viewer_card": "07",
        "spoken_expansion_card": "07",
        "spoken_witness": "clockwise- and counterclockwise-spinning galaxy counts",
        "status": "EARNED_SAME_CARD_REVEAL_MUST_BE_SYNCHRONIZED",
        "render_timing": "Reveal CW COUNTS, CCW COUNTS, and the unequal sign no earlier than the witness sentence; later Cards 09–10 are already earned.",
    },
]
for item in initialisms:
    card = card_by_id(v11, item["spoken_expansion_card"])
    require(item["spoken_witness"].lower() in card["narration"].lower(), f"spoken expansion missing: {item['form']}")
    tokens = ("CW", "CCW") if item["form"] == "CW/CCW" else (item["form"],)
    earned = int(item["spoken_expansion_card"])
    for path, value in audience:
        match = re.match(r"cards\[(\d+)\]", path)
        if match and int(match.group(1)) < earned:
            for token in tokens:
                require(re.search(rf"(?<![A-Za-z0-9]){re.escape(token)}(?![A-Za-z0-9])", value) is None, f"{token} appears before earning at {path}")

shorthand = [
    {
        "forms": ["~", "M☉", "M ≳ 2 M☉"],
        "first_viewer_card": "04",
        "spoken_plain_language": [
            "about one and a half times the mass of our Sun",
            "one point five solar masses",
            "approximately two solar masses or above",
        ],
        "render_timing": "Reveal each mass label with or after the corresponding Card-04 spoken phrase.",
    },
    {
        "forms": ["±"],
        "first_viewer_card": "05",
        "spoken_plain_language": ["give or take point zero four", "give or take point zero seven"],
        "render_timing": "Reveal each uncertainty row with or after its spoken measurement.",
    },
    {
        "forms": ["68.3%", "95.4%"],
        "first_viewer_card": "05",
        "spoken_plain_language": ["sixty-eight point three percent", "ninety-five point four percent"],
        "render_timing": "Reveal each percentage label with or after its spoken level; retain every no-terminus constraint.",
    },
    {
        "forms": ["≠"],
        "first_viewer_card": "07",
        "spoken_plain_language": ["clockwise- and counterclockwise-spinning galaxy counts should be different"],
        "render_timing": "Reveal the unequal sign with or after the Card-07 witness sentence.",
    },
]
for item in shorthand:
    card = card_by_id(v11, item["first_viewer_card"])
    low = card["narration"].lower()
    require(all(witness.lower() in low for witness in item["spoken_plain_language"]), f"plain-language shorthand witness missing Card {card['id']}")
for token in ("BHU", "CW", "CCW", "M☉", "±", "68.3%", "95.4%", "≠"):
    require(token in projection, f"audited compact form absent from projection: {token}")

# High-risk Card-05 visual constraints remain exact despite deliberate dwell.
card05 = card_by_id(v11, "05")["diagram"].lower()
for primitive in (
    "endpoint", "arrow", "tick", "bracket", "marker", "whisker",
    "shaded boundary", "axis-aligned glyph", "position-bearing terminus", "no visible edge",
):
    require(primitive in card05, f"Card 05 no-terminus constraint lost: {primitive}")

# Full-card occupancy audit under both transparent text proxies.
wpm_rows: list[dict[str, Any]] = []
for card in v11["cards"]:
    whitespace_count = len(card["narration"].split())
    spoken_count = len(re.findall(
        r"[^\W_]+(?:[’'][^\W_]+)?",
        re.sub(r"[—–-]", " ", card["narration"]),
        flags=re.UNICODE,
    ))
    seconds = card["planned_seconds"]
    whitespace_wpm = whitespace_count * 60 / seconds
    spoken_wpm = spoken_count * 60 / seconds
    whitespace_status = "IN_BAND" if 120 <= whitespace_wpm <= 135 else ("HIGH" if whitespace_wpm > 135 else "LOW")
    spoken_status = "IN_BAND" if 120 <= spoken_wpm <= 135 else ("HIGH" if spoken_wpm > 135 else "LOW")
    authority_disposition = None
    if card["id"] == "05":
        authority_disposition = "DELIBERATE_LOW_HARDEST_IDEA_AND_G3_WIDENING_BAND_WATCHING_TIME"
    elif card["id"] == "10":
        authority_disposition = "DELIBERATE_LOW_LEDGER_BLANK_RULER_DWELL_AND_CLOSING_LINE_AIR"
    wpm_rows.append({
        "card": card["id"],
        "planned_seconds": seconds,
        "whitespace_proxy": {
            "token_count": whitespace_count,
            "occupancy_wpm": round(whitespace_wpm, 2),
            "band_status": whitespace_status,
        },
        "spoken_compound_proxy": {
            "token_count": spoken_count,
            "occupancy_wpm": round(spoken_wpm, 2),
            "band_status": spoken_status,
        },
        "authority_disposition": authority_disposition,
    })

whitespace_high = [row["card"] for row in wpm_rows if row["whitespace_proxy"]["band_status"] == "HIGH"]
spoken_high = [row["card"] for row in wpm_rows if row["spoken_compound_proxy"]["band_status"] == "HIGH"]
whitespace_low = [row["card"] for row in wpm_rows if row["whitespace_proxy"]["band_status"] == "LOW"]
spoken_low = [row["card"] for row in wpm_rows if row["spoken_compound_proxy"]["band_status"] == "LOW"]
method_sensitive = [
    row["card"] for row in wpm_rows
    if row["whitespace_proxy"]["band_status"] != row["spoken_compound_proxy"]["band_status"]
]
require(whitespace_high == [] and spoken_high == [], f"V11 still has HIGH cards: whitespace={whitespace_high}, spoken={spoken_high}")
require(whitespace_low == ["05", "10", "11"], f"V11 whitespace LOW set drifted: {whitespace_low}")
require(spoken_low == ["05", "10"], f"V11 spoken-proxy LOW set drifted: {spoken_low}")
require(method_sensitive == ["11"], f"V11 method-sensitive set drifted: {method_sensitive}")
require(all(next(row for row in wpm_rows if row["card"] == card_id)["authority_disposition"] for card_id in ("05", "10")), "deliberate LOW disposition missing")
card01_row = next(row for row in wpm_rows if row["card"] == "01")
require(card01_row["whitespace_proxy"]["token_count"] == 81, "Card 01 whitespace count drift")
require(card01_row["spoken_compound_proxy"]["token_count"] == 80, "Card 01 spoken count drift")
max_whitespace = max((row["whitespace_proxy"]["occupancy_wpm"], row["card"]) for row in wpm_rows)
max_spoken = max((row["spoken_compound_proxy"]["occupancy_wpm"], row["card"]) for row in wpm_rows)
require(max_whitespace == (127.89, "01"), f"V11 max whitespace occupancy drift: {max_whitespace}")
require(max_spoken == (126.32, "01"), f"V11 max spoken occupancy drift: {max_spoken}")
total_whitespace = sum(row["whitespace_proxy"]["token_count"] for row in wpm_rows)
total_spoken = sum(row["spoken_compound_proxy"]["token_count"] for row in wpm_rows)
total_seconds = sum(row["planned_seconds"] for row in wpm_rows)
require((total_whitespace, total_spoken, total_seconds) == (823, 831, 415), "V11 aggregate count/duration drift")

wpm_audit = {
    "status": "PASS_NO_HIGH_CARDS_TWO_AUTHORIZED_DELIBERATE_LOW_CARDS",
    "metric": "full-card occupancy proxy; not encoded narration rate",
    "contract_band_wpm": [120, 135],
    "counting_rules": {
        "whitespace_proxy": "len(card narration .split()); preserves continuity with the V10 audit",
        "spoken_compound_proxy": "Unicode word tokens after splitting em dash, en dash, and hyphen compounds; Lana's ruling uses this proxy for pacing decisions",
    },
    "counting_caveat": "LOW means available visual/silent dwell, not automatically slow speech. Encoded per-card speech spans remain the final pace authority.",
    "cards": wpm_rows,
    "high_cards": {"whitespace_proxy": whitespace_high, "spoken_compound_proxy": spoken_high},
    "deliberate_low_cards": {
        "05": "Hardest idea; G3 widening-band animation needs watching time; nuance lands after the closing sentence.",
        "10": "Ledger and blank-ruler dwell; the closing line benefits from air.",
    },
    "method_sensitive_cards": {
        "11": "LOW at 116.47 by whitespace proxy; IN_BAND at 121.76 by spoken-compound proxy; Lana rules keep for wanted final reopen-gate hold."
    },
    "maximum_occupancy_wpm": {
        "whitespace_proxy": {"card": max_whitespace[1], "wpm": max_whitespace[0]},
        "spoken_compound_proxy": {"card": max_spoken[1], "wpm": max_spoken[0]},
    },
    "card01_spine_authority": {
        "planned_seconds": 38,
        "spoken_compound_proxy_wpm": 126.32,
        "authority_estimated_verdict_arrival_seconds": "32-33",
        "encoded_qa_required": "Verify the route verdict lands by approximately 35 seconds and all speech remains inside Card 01 without rushing.",
    },
    "total_whitespace_proxy_tokens": total_whitespace,
    "total_spoken_compound_proxy_tokens": total_spoken,
    "total_planned_seconds": total_seconds,
    "aggregate_whitespace_proxy_wpm": round(total_whitespace * 60 / total_seconds, 2),
    "aggregate_spoken_compound_proxy_wpm": round(total_spoken * 60 / total_seconds, 2),
    "silent_retiming_outside_authorized_cards": False,
}

shorthand_audit = {
    "status": "PASS_V11_NO_NEW_SHORTHAND_NO_CNS_EXCEPTION_WITH_RENDER_REVEAL_CONSTRAINTS",
    "scope": "title plus all card headings, narration, diagram/printable-label instructions, and on-screen support",
    "card01_new_initialisms": [],
    "lexical_initialisms": initialisms,
    "retired_initialism": {
        "form": "CNS",
        "viewer_occurrences": 0,
        "replacement_heading": card_by_id(v11, "04")["heading"],
        "spoken_full_name_card": "04",
        "renderer_exception_required": False,
    },
    "scientific_shorthand": shorthand,
    "unearned_string_defects_after_v11_retiming": 0,
    "render_reveal_constraints": [item["render_timing"] for item in initialisms + shorthand],
    "render_gate": "Encoded-frame/audio QA must prove each remaining first-use compact label is revealed no earlier than its listed spoken witness.",
}

v11_media = sorted(
    str(path.relative_to(D))
    for path in D.rglob("*")
    if path.is_file() and "v11" in path.name.lower() and path.suffix.lower() in MEDIA_SUFFIXES
)
require(not v11_media, f"premature V11 media exists: {v11_media}")
require(v11.get("slug") == "bhu-closing-record", "routing slug changed")

result = {
    "status": "PASS_V11_LANA_RETIMING_AWAITING_TIGHT_THREE_SEAT_EXACT_HASH_CONFIRMATION",
    "render_authority": False,
    "review_targets": {path.name: sha(path) for path in V11.values()},
    "authored_canonical_changed_paths": expected_changed[:-1],
    "derived_canonical_changed_paths": ["estimated_duration_seconds"],
    "all_structured_changed_paths": changed,
    "standalone_narration_change": "Exact Card 01 spoken replacement only",
    "unchanged_byte_copies": [V11["ledger"].name, V11["graphics"].name],
    "card01_boundary_markers": ["personal side-interest", "not part of the lab's research programme"],
    "card01_badge_unchanged": True,
    "viewer_local_name_hits": 0,
    "viewer_internal_vocabulary_hits": 0,
    "viewer_cns_hits": 0,
    "remaining_initialism_inventory": [item["form"] for item in initialisms],
    "render_reveal_constraints_required": True,
    "planned_runtime_seconds": 415,
    "high_wpm_cards": [],
    "deliberate_low_cards": ["05", "10"],
    "method_sensitive_cards": ["11"],
    "premature_v11_media_files": 0,
}

(D / "V11_WPM_AUDIT.json").write_text(json.dumps(wpm_audit, indent=2, ensure_ascii=False) + "\n")
(D / "V11_SHORTHAND_AUDIT.json").write_text(json.dumps(shorthand_audit, indent=2, ensure_ascii=False) + "\n")
(D / "V11_BUILD_VERIFICATION.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({
    "verification": result,
    "wpm_audit": wpm_audit,
    "shorthand_audit": shorthand_audit,
}, indent=2, ensure_ascii=False))
