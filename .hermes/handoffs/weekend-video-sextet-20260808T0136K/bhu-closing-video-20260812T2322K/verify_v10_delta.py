#!/usr/bin/env python3
"""Verify the exact BHU V9→V10 two-repair delta and full pacing audit.

Writes only deterministic V10 verification/audit JSON. It does not generate
speech, frames, video, uploads, publication state, or render authority.
"""
from __future__ import annotations

import hashlib
import json
import re
from pathlib import Path
from typing import Any

D = Path(__file__).resolve().parent
V9 = {
    "story": (D / "STORYBOARD_DRAFT_V9.json", "c9824b95453be7e67d6066f3810648dc8d588a8c3210546ec9caa5ee74710d7a"),
    "narration": (D / "NARRATION_DRAFT_V9.md", "85f111d366c5d11d912e4f7db5586f10b491b12b1c5091d3f94d822c388190b3"),
    "ledger": (D / "CLAIM_LINE_LEDGER_V9.md", "aa4b459a3b4112dc40feabb5e84a0853e205db400d0adfc9d58cab248f6cc9aa"),
    "graphics": (D / "DETERMINISTIC_DIAGRAM_SPEC_V9.md", "e296e2f29a00cf714cbc9f562bb224d224e185fb8d6a5ecb03e718cf5e1cc52e"),
}
V9_CONTROLS = {
    "V9_SHORTHAND_AUDIT.json": "2cd55bd9698ec11ccf002b3e1810ab51408bfdbe18f4bca3fa51314e46931624",
    "V9_FREEZE_RECEIPT.json": "3df2d6638aa13cd0db58b3926fb523a90506be28f3749f37b3897b2840150bcc",
    "LANA_CONFIRM_V9.md": "f553e690201c3eaccfeee5b8b12c34e9defe6924166fa7397ed0a3fb95a35b3c",
    "GORU_CONFIRM_V9.md": "d4ae02987ab1269d3c777b47031f56e81cbe5b1f9b106e808d11b970191c49bd",
    "KUN_CONFIRM_V9.md": "0ed5627ebef10460755151719a1313a3304dc0705d48c3fff8e20e7078f361f9",
}
V10 = {
    "story": D / "STORYBOARD_DRAFT_V10.json",
    "narration": D / "NARRATION_DRAFT_V10.md",
    "ledger": D / "CLAIM_LINE_LEDGER_V10.md",
    "graphics": D / "DETERMINISTIC_DIAGRAM_SPEC_V10.md",
}
EXPECTED_V10 = {
    "story": "dc853f90c3299c5e1c051c0c37a45b6612f5418eaa9bbaad63608fd10ec56ae9",
    "narration": "4324c9b73de038e760c67e80fee70b60656599cf22d95cb1d92167e818f5ef75",
    "ledger": "aa4b459a3b4112dc40feabb5e84a0853e205db400d0adfc9d58cab248f6cc9aa",
    "graphics": "e296e2f29a00cf714cbc9f562bb224d224e185fb8d6a5ecb03e718cf5e1cc52e",
}
OLD_HEADING = "One CNS chain puts a low ceiling on neutron-star mass"
NEW_HEADING = "One cosmological-natural-selection chain puts a low ceiling on neutron-star mass"
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


for path, expected in V9.values():
    require(path.exists() and sha(path) == expected, f"pinned V9 target drift: {path.name}")
for name, expected in V9_CONTROLS.items():
    path = D / name
    require(path.exists() and sha(path) == expected, f"pinned V9 authority/control drift: {name}")
for key, path in V10.items():
    require(path.exists() and sha(path) == EXPECTED_V10[key], f"V10 target drift: {path.name}")

v9 = json.loads(V9["story"][0].read_text())
v10 = json.loads(V10["story"].read_text())
changed = diffs(v9, v10)
expected_changed = [
    "cards[3].heading",
    "cards[3].planned_seconds",
    "estimated_duration_seconds",
]
require(changed == expected_changed, f"canonical V9→V10 delta is not exact: {changed}")
require(card_by_id(v9, "04")["heading"] == OLD_HEADING, "V9 Card 04 heading anchor drift")
require(card_by_id(v10, "04")["heading"] == NEW_HEADING, "V10 Card 04 preferred heading not verbatim")
require(card_by_id(v9, "04")["planned_seconds"] == 41, "V9 Card 04 timing anchor drift")
require(card_by_id(v10, "04")["planned_seconds"] == 48, "V10 Card 04 planned_seconds is not 48")
require(v9["estimated_duration_seconds"] == 392, "V9 aggregate duration anchor drift")
require(v10["estimated_duration_seconds"] == 399, "V10 aggregate duration is not 399")
require(v10["estimated_duration_seconds"] == sum(c["planned_seconds"] for c in v10["cards"]), "V10 aggregate duration is stale")

# Every field outside the authorized Card-04 changes and their derived total stays fixed.
for old, new in zip(v9["cards"], v10["cards"]):
    require(old["id"] == new["id"], "card order or ID changed")
    for key in old:
        if old["id"] == "04" and key in {"heading", "planned_seconds"}:
            continue
        require(old[key] == new[key], f"unauthorized Card {old['id']} field changed: {key}")

v9_narr = V9["narration"][0].read_text()
v10_narr = V10["narration"].read_text()
require(v9_narr.count(OLD_HEADING) == 1, "V9 standalone heading anchor count is not one")
require(v10_narr == v9_narr.replace(OLD_HEADING, NEW_HEADING), "standalone narration changed beyond heading replacement")
require(V10["ledger"].read_bytes() == V9["ledger"][0].read_bytes(), "claim ledger is not byte-identical")
require(V10["graphics"].read_bytes() == V9["graphics"][0].read_bytes(), "graphics spec is not byte-identical")

# Standalone headings and narration remain exact mirrors of canonical storyboard strings.
parts = re.split(r"## Card (\d+) — assertion heading\n", v10_narr)[1:]
seen: dict[str, tuple[str, str]] = {}
for index in range(0, len(parts), 2):
    card_id, block = parts[index], parts[index + 1]
    heading = block.split("**", 2)[1]
    narration = block.split("**", 2)[2].split("\n\nSource:", 1)[0].strip()
    seen[card_id] = (heading, narration)
require(len(seen) == 11, f"standalone narration parsed {len(seen)} cards, not 11")
for card in v10["cards"]:
    require(seen.get(card["id"]) == (card["heading"], card["narration"]), f"V10 narration divergence Card {card['id']}")

# Complete audience projection: every value rendered visibly or audibly by the local renderer.
audience: list[tuple[str, str]] = []
for card in v10["cards"]:
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

# CNS is eliminated from the audience projection; its full name is visible at Card 04 start.
require(not re.search(r"(?<![A-Za-z0-9])CNS(?![A-Za-z0-9])", projection), "viewer-facing CNS remains")
require(card_by_id(v10, "04")["heading"] == NEW_HEADING, "full Card 04 assertion heading missing")
require("cosmological natural selection" in card_by_id(v10, "04")["narration"].lower(), "Card 04 spoken full name missing")

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
    card = card_by_id(v10, item["spoken_expansion_card"])
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
    card = card_by_id(v10, item["first_viewer_card"])
    low = card["narration"].lower()
    require(all(witness.lower() in low for witness in item["spoken_plain_language"]), f"plain-language shorthand witness missing Card {card['id']}")
for token in ("BHU", "CW", "CCW", "M☉", "±", "68.3%", "95.4%", "≠"):
    require(token in projection, f"audited compact form absent from projection: {token}")

# Preserve the high-risk Card-05 representation constraints.
card05 = card_by_id(v10, "05")["diagram"].lower()
for primitive in (
    "endpoint", "arrow", "tick", "bracket", "marker", "whisker",
    "shaded boundary", "axis-aligned glyph", "position-bearing terminus", "no visible edge",
):
    require(primitive in card05, f"Card 05 no-terminus constraint lost: {primitive}")

# Recompute every card under two disclosed text proxies. The whitespace rule
# exactly reproduces Lana's Card-04 count of 99; the spoken-compound proxy splits
# dash/hyphen compounds, addressing her warning that the true spoken count is
# slightly higher. Encoded per-card speech duration remains the final pace gate.
wpm_rows: list[dict[str, Any]] = []
for card in v10["cards"]:
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
    wpm_rows.append({
        "card": card["id"],
        "planned_seconds": seconds,
        "whitespace_proxy": {
            "token_count": whitespace_count,
            "computed_wpm": round(whitespace_wpm, 2),
            "band_status": whitespace_status,
        },
        "spoken_compound_proxy": {
            "token_count": spoken_count,
            "computed_wpm": round(spoken_wpm, 2),
            "band_status": spoken_status,
        },
    })
require(card_by_id(v10, "04")["planned_seconds"] == 48, "Card 04 timing repair lost before WPM audit")
card04_row = next(row for row in wpm_rows if row["card"] == "04")
require(card04_row["whitespace_proxy"]["token_count"] == 99, "Card 04 audit no longer reproduces Lana's 99-token count")
require(card04_row["spoken_compound_proxy"]["token_count"] == 101, "Card 04 spoken-compound proxy drift")
expected_whitespace_outliers = {
    "01": "HIGH", "02": "HIGH", "05": "LOW", "07": "HIGH",
    "10": "LOW", "11": "LOW",
}
expected_spoken_outliers = {
    "01": "HIGH", "02": "HIGH", "03": "HIGH", "05": "LOW",
    "07": "HIGH", "09": "HIGH", "10": "LOW",
}
whitespace_outliers = {
    row["card"]: row["whitespace_proxy"]["band_status"]
    for row in wpm_rows if row["whitespace_proxy"]["band_status"] != "IN_BAND"
}
spoken_outliers = {
    row["card"]: row["spoken_compound_proxy"]["band_status"]
    for row in wpm_rows if row["spoken_compound_proxy"]["band_status"] != "IN_BAND"
}
require(whitespace_outliers == expected_whitespace_outliers, f"whitespace WPM outlier set drifted: {whitespace_outliers}")
require(spoken_outliers == expected_spoken_outliers, f"spoken-compound WPM outlier set drifted: {spoken_outliers}")
robust_outliers = {
    card: whitespace_outliers[card]
    for card in sorted(whitespace_outliers.keys() & spoken_outliers.keys())
    if whitespace_outliers[card] == spoken_outliers[card]
}
method_sensitive_cards = sorted(whitespace_outliers.keys() ^ spoken_outliers.keys())
require(robust_outliers == {"01": "HIGH", "02": "HIGH", "05": "LOW", "07": "HIGH", "10": "LOW"}, f"robust WPM outlier set drifted: {robust_outliers}")
require(method_sensitive_cards == ["03", "09", "11"], f"method-sensitive WPM card set drifted: {method_sensitive_cards}")
total_whitespace_count = sum(row["whitespace_proxy"]["token_count"] for row in wpm_rows)
total_spoken_count = sum(row["spoken_compound_proxy"]["token_count"] for row in wpm_rows)
total_seconds = sum(row["planned_seconds"] for row in wpm_rows)
require(total_whitespace_count == 832 and total_spoken_count == 841 and total_seconds == 399, "V10 total count or duration drift")
wpm_audit = {
    "status": "REPORT_ALL_OUTLIERS_AND_TOKENIZATION_SENSITIVITY_NO_SILENT_RETIMING",
    "contract_band_wpm": [120, 135],
    "counting_rules": {
        "whitespace_proxy": "len(card narration .split()); exactly reproduces Lana's disclosed V9 Card-04 count of 99",
        "spoken_compound_proxy": "Unicode word tokens after splitting em dash, en dash, and hyphen compounds; responds to Lana's warning that joined compounds undercount spoken words",
    },
    "counting_caveat": "Both are transparent text proxies, not measured speech. Encoded per-card speech duration is the final pace authority.",
    "authority_repair": {
        "card": "04",
        "planned_seconds_old": 41,
        "planned_seconds_new": 48,
        "authority_floor_seconds": 46,
        "selected_seconds": 48,
    },
    "cards": wpm_rows,
    "whitespace_proxy_outliers_after_card04_repair": whitespace_outliers,
    "spoken_compound_proxy_outliers_after_card04_repair": spoken_outliers,
    "robust_outliers_under_both_proxies": robust_outliers,
    "method_sensitive_cards": method_sensitive_cards,
    "disposition": "Reported for three-seat/user adjudication; V10 changes no timing outside Card 04.",
    "total_whitespace_proxy_tokens": total_whitespace_count,
    "total_spoken_compound_proxy_tokens": total_spoken_count,
    "total_planned_seconds": total_seconds,
    "aggregate_whitespace_proxy_wpm": round(total_whitespace_count * 60 / total_seconds, 2),
    "aggregate_spoken_compound_proxy_wpm": round(total_spoken_count * 60 / total_seconds, 2),
}

shorthand_audit = {
    "status": "PASS_STRING_INVENTORY_NO_CNS_EXCEPTION_WITH_RENDER_REVEAL_CONSTRAINTS",
    "scope": "title plus all card headings, narration, diagram/printable-label instructions, and on-screen support",
    "lexical_initialisms": initialisms,
    "retired_initialism": {
        "form": "CNS",
        "viewer_occurrences": 0,
        "replacement_heading": NEW_HEADING,
        "spoken_full_name_card": "04",
        "renderer_exception_required": False,
    },
    "scientific_shorthand": shorthand,
    "unearned_string_defects_after_v10_repair": 0,
    "render_reveal_constraints": [item["render_timing"] for item in initialisms + shorthand],
    "nonviewer_classifications": {
        "bhu-closing-record slug": "routing metadata; current local renderer does not consume it; no upload/publication authorized",
        "G1..G8": "implementation IDs, not printable labels",
        "fps/px/WPM": "render-contract metadata, not spoken or printed",
        "arrows, list dots, question marks": "structural diagram grammar, not lexical initialisms",
    },
    "render_gate": "Encoded-frame/audio QA must prove each remaining first-use compact label is revealed no earlier than its listed spoken witness.",
}

v10_media = [
    str(path.relative_to(D))
    for path in D.rglob("*")
    if path.is_file() and "v10" in path.name.lower() and path.suffix.lower() in MEDIA_SUFFIXES
]
require(not v10_media, f"premature V10 media exists: {v10_media}")
require(v10.get("slug") == "bhu-closing-record", "routing slug changed")

result = {
    "status": "PASS_V10_TWO_REPAIR_DELTA_AWAITING_TIGHT_THREE_SEAT_EXACT_HASH_CONFIRMATION",
    "render_authority": False,
    "review_targets": {path.name: sha(path) for path in V10.values()},
    "authored_canonical_changed_paths": ["cards[3].heading", "cards[3].planned_seconds"],
    "derived_canonical_changed_paths": ["estimated_duration_seconds"],
    "all_structured_changed_paths": changed,
    "standalone_narration_change": "Card 04 assertion heading only; all spoken narration byte-equivalent to V9",
    "unchanged_byte_copies": [V10["ledger"].name, V10["graphics"].name],
    "viewer_local_name_hits": 0,
    "viewer_internal_vocabulary_hits": 0,
    "viewer_cns_hits": 0,
    "remaining_initialism_inventory": [item["form"] for item in initialisms],
    "unearned_string_defects_after_repair": 0,
    "render_reveal_constraints_required": True,
    "planned_runtime_seconds": 399,
    "wpm_robust_outliers_reported_not_repaired": robust_outliers,
    "wpm_method_sensitive_cards_reported_not_repaired": method_sensitive_cards,
    "premature_v10_media_files": 0,
}

(D / "V10_WPM_AUDIT.json").write_text(json.dumps(wpm_audit, indent=2, ensure_ascii=False) + "\n")
(D / "V10_SHORTHAND_AUDIT.json").write_text(json.dumps(shorthand_audit, indent=2, ensure_ascii=False) + "\n")
(D / "V10_BUILD_VERIFICATION.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
print(json.dumps({
    "verification": result,
    "wpm_audit": wpm_audit,
    "shorthand_audit": shorthand_audit,
}, indent=2, ensure_ascii=False))
