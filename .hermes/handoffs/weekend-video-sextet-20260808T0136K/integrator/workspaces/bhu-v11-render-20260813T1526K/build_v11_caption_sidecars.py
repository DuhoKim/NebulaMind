#!/usr/bin/env python3
"""Build exact 64-sentence V11 SRT/VTT sidecars from frozen narration and measured timing."""
from __future__ import annotations

import hashlib
import json
import re
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path

SOURCE = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-closing-video-20260812T2322K/NARRATION_DRAFT_V11.md")
TIMELINE = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/integrator/workspaces/bhu-v11-render-20260813T1526K/audio/timeline.json")
VIDEO = Path("/Users/duhokim/HermesOps/cockpit/videos/bhu-closing-record-v11-local-20260813T1526K.mp4")
OUT_DIR = Path("/Users/duhokim/HermesOps/cockpit/videos")
STAMP = "20260813T1629K"
SRT = OUT_DIR / f"bhu-closing-record-v11-captions-{STAMP}.srt"
VTT = OUT_DIR / f"bhu-closing-record-v11-captions-{STAMP}.vtt"
REPORT = OUT_DIR / f"bhu-closing-record-v11-caption-sidecar-qa-{STAMP}.json"
EXPECTED = {
    "narration": "027a6e17fcb3c7d3708177b8fa30078735c11cc4157f6b44edfacceef7bb8535",
    "timeline": "0fdcc404e4b4e5886f82f776cc239e494d7c9f8d60a62773ab5628f003981048",
    "video": "8e6a4e564ddc25959ecb17c57fe19d898b9f92850b5c83da234ef3d2295f40fb",
}


@dataclass(frozen=True)
class Cue:
    card_id: str
    text: str
    start: float
    end: float
    source_fragment_ids: tuple[str, ...]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tokens(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower().replace("’", "'").replace("‘", "'"))


def split_sentences(text: str) -> list[str]:
    return re.split(r"(?<=[.!?])\s+(?=[A-Z“‘])", text)


def parse_frozen_narration() -> dict[str, str]:
    text = SOURCE.read_text()
    blocks = re.split(r"(?m)^## Card (\d\d) — assertion heading\s*$", text)
    if len(blocks) != 23:
        raise RuntimeError(f"frozen narration parse failed: {len(blocks)} blocks")
    cards: dict[str, str] = {}
    for index in range(1, len(blocks), 2):
        card_id = blocks[index]
        body = blocks[index + 1].strip()
        heading = re.search(r"^\*\*(.+?)\*\*\s*$", body, flags=re.MULTILINE)
        if not heading:
            raise RuntimeError(f"Card {card_id} heading missing")
        cards[card_id] = body[heading.end():].strip().split("\n\nSource:", 1)[0].strip()
    return cards


def merge_to_source_sentences(cards: dict[str, str], timeline: dict) -> list[Cue]:
    merged: list[Cue] = []
    timeline_cards = {card["card_id"]: card for card in timeline["cards"]}
    for card_id, narration in cards.items():
        card = timeline_cards[card_id]
        fragments = card["captions"]
        source_sentences = split_sentences(narration)
        cursor = 0
        for sentence in source_sentences:
            wanted = tokens(sentence)
            accumulated: list[str] = []
            first = cursor
            while cursor < len(fragments) and len(accumulated) < len(wanted):
                accumulated.extend(tokens(fragments[cursor]["text"]))
                cursor += 1
            if accumulated != wanted:
                raise RuntimeError(
                    f"Card {card_id} source/timeline sentence mapping failed: "
                    f"sentence={sentence!r} fragments={first}:{cursor} "
                    f"wanted={wanted} got={accumulated}"
                )
            selected = fragments[first:cursor]
            merged.append(Cue(
                card_id=card_id,
                text=sentence,
                start=float(selected[0]["master_start_seconds"]),
                end=float(selected[-1]["master_end_seconds"]),
                source_fragment_ids=tuple(item["id"] for item in selected),
            ))
        if cursor != len(fragments):
            raise RuntimeError(f"Card {card_id} left {len(fragments) - cursor} unmapped fragments")
        if " ".join(cue.text for cue in merged if cue.card_id == card_id) != narration:
            raise RuntimeError(f"Card {card_id} exact narration reconstruction failed")
    return merged


def millis(seconds: float) -> int:
    return round(seconds * 1000)


def timestamp(value_ms: int, decimal: str) -> str:
    hours, value_ms = divmod(value_ms, 3_600_000)
    minutes, value_ms = divmod(value_ms, 60_000)
    seconds, value_ms = divmod(value_ms, 1000)
    return f"{hours:02d}:{minutes:02d}:{seconds:02d}{decimal}{value_ms:03d}"


def render(cues: list[Cue], vtt: bool) -> str:
    lines = ["WEBVTT", ""] if vtt else []
    decimal = "." if vtt else ","
    for index, cue in enumerate(cues, 1):
        start_ms = millis(cue.start)
        end_ms = millis(cue.end)
        if end_ms <= start_ms:
            raise RuntimeError(f"non-positive cue {index}")
        lines.extend([
            str(index),
            f"{timestamp(start_ms, decimal)} --> {timestamp(end_ms, decimal)}",
            cue.text,
            "",
        ])
    return "\n".join(lines)


def parse_sidecar(path: Path, vtt: bool) -> list[tuple[int, int, str]]:
    text = path.read_text()
    if vtt:
        if not text.startswith("WEBVTT\n\n"):
            raise RuntimeError("VTT header missing")
        text = text[len("WEBVTT\n\n"):]
    blocks = [block for block in text.strip().split("\n\n") if block.strip()]
    parsed: list[tuple[int, int, str]] = []
    pattern = re.compile(
        r"^(\d+):(\d+):(\d+)[,.](\d{3}) --> "
        r"(\d+):(\d+):(\d+)[,.](\d{3})$"
    )
    for expected_index, block in enumerate(blocks, 1):
        lines = block.splitlines()
        if len(lines) < 3 or int(lines[0]) != expected_index:
            raise RuntimeError(f"invalid cue block {expected_index} in {path.name}")
        match = pattern.match(lines[1])
        if not match:
            raise RuntimeError(f"invalid timestamp {lines[1]!r}")
        values = [int(value) for value in match.groups()]
        start = ((values[0] * 60 + values[1]) * 60 + values[2]) * 1000 + values[3]
        end = ((values[4] * 60 + values[5]) * 60 + values[6]) * 1000 + values[7]
        parsed.append((start, end, "\n".join(lines[2:])))
    return parsed


def main() -> int:
    live = {"narration": sha(SOURCE), "timeline": sha(TIMELINE), "video": sha(VIDEO)}
    if live != EXPECTED:
        raise RuntimeError(f"custody drift: {live}")
    timeline = json.loads(TIMELINE.read_text())
    if timeline["source_hashes"]["NARRATION_DRAFT_V11.md"] != EXPECTED["narration"]:
        raise RuntimeError("timeline does not bind frozen narration")
    if float(timeline["master_duration_seconds"]) != 415.0:
        raise RuntimeError("timeline duration drift")
    cards = parse_frozen_narration()
    cues = merge_to_source_sentences(cards, timeline)
    if len(cues) != 64:
        raise RuntimeError(f"expected 64 source sentences, got {len(cues)}")
    if any(millis(cues[i].end) > millis(cues[i + 1].start) for i in range(len(cues) - 1)):
        raise RuntimeError("caption cues overlap")

    SRT.write_text(render(cues, vtt=False))
    VTT.write_text(render(cues, vtt=True))

    srt_parsed = parse_sidecar(SRT, vtt=False)
    vtt_parsed = parse_sidecar(VTT, vtt=True)
    expected_payloads = [cue.text for cue in cues]
    if [row[2] for row in srt_parsed] != expected_payloads:
        raise RuntimeError("SRT exact payload mismatch")
    if [row[2] for row in vtt_parsed] != expected_payloads:
        raise RuntimeError("VTT exact payload mismatch")
    if [(row[0], row[1]) for row in srt_parsed] != [(row[0], row[1]) for row in vtt_parsed]:
        raise RuntimeError("SRT/VTT timing mismatch")
    if any("\n" in row[2] for row in srt_parsed):
        raise RuntimeError("unexpected payload wrapping")

    per_card = []
    for card_id, narration in cards.items():
        payloads = [cue.text for cue in cues if cue.card_id == card_id]
        per_card.append({
            "card_id": card_id,
            "cue_count": len(payloads),
            "exact_join_matches_frozen_card_narration": " ".join(payloads) == narration,
        })

    report = {
        "status": "PASS_V11_64_OF_64_EXACT_SOURCE_SENTENCE_SIDECARS",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "scope": {
            "sidecar_generation_only": True,
            "video_modified": False,
            "video_reencoded": False,
            "youtube_caption_uploaded": False,
        },
        "custody": {
            "video": str(VIDEO),
            "video_sha256": live["video"],
            "narration": str(SOURCE),
            "narration_sha256": live["narration"],
            "measured_timeline": str(TIMELINE),
            "measured_timeline_sha256": live["timeline"],
        },
        "caption_count": len(cues),
        "exact_payload_matches": {
            "srt": sum(row[2] == expected_payloads[index] for index, row in enumerate(srt_parsed)),
            "vtt": sum(row[2] == expected_payloads[index] for index, row in enumerate(vtt_parsed)),
            "expected": len(cues),
        },
        "exact_card_narration_reconstruction_all_11": all(row["exact_join_matches_frozen_card_narration"] for row in per_card),
        "timestamps_monotonic_non_overlapping": True,
        "first_cue_start_seconds": srt_parsed[0][0] / 1000,
        "last_cue_end_seconds": srt_parsed[-1][1] / 1000,
        "source_timeline_fragment_count": sum(len(card["captions"]) for card in timeline["cards"]),
        "merge_note": "The 70 measured display fragments were merged to 64 frozen source sentences; only exact consecutive fragments from Card 02 and Card 04 earning splits were recombined.",
        "outputs": {
            "srt": {"path": str(SRT), "sha256": sha(SRT), "bytes": SRT.stat().st_size},
            "vtt": {"path": str(VTT), "sha256": sha(VTT), "bytes": VTT.stat().st_size},
        },
        "per_card": per_card,
        "cues": [
            {
                "index": index,
                "card_id": cue.card_id,
                "start_seconds": millis(cue.start) / 1000,
                "end_seconds": millis(cue.end) / 1000,
                "text": cue.text,
                "source_timeline_fragment_ids": list(cue.source_fragment_ids),
            }
            for index, cue in enumerate(cues, 1)
        ],
        "qa_gap": {
            "confirmed_mp4_streams_before_fix_forward": ["h264", "aac"],
            "subtitle_stream_present": False,
            "external_v11_sidecars_present_before_fix_forward": False,
            "root_cause": "encoded QA verified caption payload content and timing artifacts but did not assert an actual subtitle stream or required external sidecar existence",
            "recurrence_prevention": "future encoded QA must independently assert the intended delivery contract: subtitle stream presence when embedding is required and/or exact SRT/VTT sidecar existence, count, source equality, candidate-hash binding, and serving/upload state when YouTube captions are required",
        },
    }
    REPORT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    print(json.dumps({
        "status": report["status"],
        "caption_count": report["caption_count"],
        "exact_payload_matches": report["exact_payload_matches"],
        "exact_card_narration_reconstruction_all_11": report["exact_card_narration_reconstruction_all_11"],
        "first_cue_start_seconds": report["first_cue_start_seconds"],
        "last_cue_end_seconds": report["last_cue_end_seconds"],
        "outputs": report["outputs"],
        "report": str(REPORT),
    }, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
