#!/usr/bin/env python3
"""Build exact-source V11 narration with free Edge TTS and a measured timeline."""
from __future__ import annotations

import asyncio
import hashlib
import json
import re
import subprocess
import time
import wave
from datetime import datetime, timezone
from pathlib import Path

import edge_tts

SOURCE = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-closing-video-20260812T2322K")
ROOT = Path(__file__).resolve().parent
STORY_PATH = SOURCE / "STORYBOARD_DRAFT_V11.json"
NARRATION_PATH = SOURCE / "NARRATION_DRAFT_V11.md"
EXPECTED = {
    "STORYBOARD_DRAFT_V11.json": "b0ec6a53061ccea4196df3036bd0ad59e34ef50814b92dd3ec16cf0e4794f7c4",
    "NARRATION_DRAFT_V11.md": "027a6e17fcb3c7d3708177b8fa30078735c11cc4157f6b44edfacceef7bb8535",
}
VOICE = "en-US-AndrewMultilingualNeural"
RATE = "+0%"
TARGET_WPM = 128.0
SAMPLE_RATE = 48_000
LEAD_SECONDS = 0.06
TAIL_SECONDS = 0.08
RAW_DIR = ROOT / "audio" / "raw"
CARD_DIR = ROOT / "audio" / "cards"
MASTER_PATH = ROOT / "audio" / "narration_master.wav"
TIMELINE_PATH = ROOT / "audio" / "timeline.json"
SRT_PATH = ROOT / "captions_v11.srt"


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, check=True, capture_output=True, text=True)


def probe_duration(path: Path) -> float:
    out = run(
        "ffprobe", "-v", "error", "-show_entries", "format=duration",
        "-of", "default=noprint_wrappers=1:nokey=1", str(path),
    ).stdout.strip()
    return float(out)


def normalized_tokens(text: str) -> list[str]:
    return re.findall(r"[a-z0-9]+", text.lower().replace("’", "'").replace("‘", "'"))


def spoken_count(text: str) -> int:
    return len(re.findall(
        r"[^\W_]+(?:[’'][^\W_]+)?",
        re.sub(r"[—–-]", " ", text),
        flags=re.UNICODE,
    ))


def parse_standalone_narration() -> dict[str, dict[str, str]]:
    text = NARRATION_PATH.read_text()
    blocks = re.split(r"(?m)^## Card (\d\d) — assertion heading\s*$", text)
    if len(blocks) != 23:
        raise RuntimeError(f"standalone narration parse failed: {len(blocks)} parts")
    result: dict[str, dict[str, str]] = {}
    for i in range(1, len(blocks), 2):
        card_id = blocks[i]
        body = blocks[i + 1].strip()
        heading_match = re.search(r"^\*\*(.+?)\*\*\s*$", body, flags=re.MULTILINE)
        if not heading_match:
            raise RuntimeError(f"Card {card_id} heading missing")
        after_heading = body[heading_match.end():].strip()
        narration = after_heading.split("\n\nSource:", 1)[0].strip()
        result[card_id] = {"heading": heading_match.group(1), "narration": narration}
    return result


def split_sentences(text: str) -> list[str]:
    return re.split(r"(?<=[.!?])\s+(?=[A-Z“‘])", text)


def cue_texts(card_id: str, narration: str) -> list[str]:
    sentences = split_sentences(narration)
    if card_id == "02":
        original = sentences[1]
        expected = "We found at least five different proposals under this label — black-hole universe, or BHU for short."
        if original != expected:
            raise RuntimeError("Card 02 earning sentence drift")
        sentences[1:2] = [
            "We found at least five different proposals under this label —",
            "black-hole universe, or",
            "BHU for short.",
        ]
    if card_id == "04":
        original = sentences[0]
        expected = "One proposal — called cosmological natural selection — says universes have children: every black hole buds off a new universe with slightly different physics."
        if original != expected:
            raise RuntimeError("Card 04 full-name earning sentence drift")
        sentences[0:1] = [
            "One proposal — called",
            "cosmological",
            "natural",
            "selection —",
            "says universes have children: every black hole buds off a new universe with slightly different physics.",
        ]
    if normalized_tokens(" ".join(sentences)) != normalized_tokens(narration):
        raise RuntimeError(f"caption cue token reconstruction failed Card {card_id}")
    return sentences


async def synthesize(text: str, output: Path, events_path: Path) -> list[dict]:
    communicator = edge_tts.Communicate(text=text, voice=VOICE, rate=RATE, boundary="WordBoundary")
    audio = bytearray()
    events: list[dict] = []
    async for chunk in communicator.stream():
        if chunk["type"] == "audio":
            audio.extend(chunk.get("data", b""))
        elif chunk["type"] == "WordBoundary":
            events.append({
                "offset_seconds": int(chunk.get("offset", 0)) / 10_000_000,
                "duration_seconds": int(chunk.get("duration", 0)) / 10_000_000,
                "text": str(chunk.get("text", "")),
            })
    if not audio or not events:
        raise RuntimeError(f"Edge TTS returned incomplete output for {output.name}")
    output.write_bytes(bytes(audio))
    events_path.write_text(json.dumps(events, indent=2, ensure_ascii=False) + "\n")
    return events


def load_or_synthesize(card_id: str, text: str) -> tuple[Path, list[dict], int]:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    text_hash = hashlib.sha256(text.encode("utf-8")).hexdigest()
    output = RAW_DIR / f"card-{card_id}-{text_hash[:12]}.mp3"
    events_path = RAW_DIR / f"card-{card_id}-{text_hash[:12]}-boundaries.json"
    attempts = 0
    events: list[dict]
    if output.exists() and events_path.exists():
        events = json.loads(events_path.read_text())
    else:
        last_error: Exception | None = None
        for attempt in (1, 2):
            attempts = attempt
            try:
                events = asyncio.run(synthesize(text, output, events_path))
                probe_duration(output)
                last_error = None
                break
            except Exception as exc:
                last_error = exc
                output.unlink(missing_ok=True)
                events_path.unlink(missing_ok=True)
                if attempt == 1:
                    time.sleep(2)
        if last_error is not None:
            raise RuntimeError(f"Card {card_id} exact-input synthesis failed: {last_error}")
    return output, events, attempts


def flatten_boundaries(text: str, events: list[dict]) -> list[dict]:
    expected = normalized_tokens(text)
    flattened: list[dict] = []
    for event in events:
        tokens = normalized_tokens(event["text"])
        if not tokens:
            continue
        start = float(event["offset_seconds"])
        duration = float(event["duration_seconds"])
        for index, token in enumerate(tokens):
            flattened.append({
                "token": token,
                "raw_start_seconds": start + duration * index / len(tokens),
                "raw_end_seconds": start + duration * (index + 1) / len(tokens),
            })
    actual = [item["token"] for item in flattened]
    if actual != expected:
        mismatch = next((i for i, pair in enumerate(zip(expected, actual)) if pair[0] != pair[1]), None)
        raise RuntimeError(
            f"Edge boundary/source token mismatch at {mismatch}: "
            f"expected={expected[mismatch:mismatch+8] if mismatch is not None else expected[-8:]} "
            f"actual={actual[mismatch:mismatch+8] if mismatch is not None else actual[-8:]}"
        )
    return flattened


def locate_sequence(tokens: list[dict], phrase: str, start_index: int = 0) -> tuple[int, int]:
    needle = normalized_tokens(phrase)
    haystack = [item["token"] for item in tokens]
    for index in range(start_index, len(haystack) - len(needle) + 1):
        if haystack[index:index + len(needle)] == needle:
            return index, index + len(needle) - 1
    raise RuntimeError(f"phrase not found in boundary stream: {phrase}")


def timestamp(seconds: float) -> str:
    milliseconds = round(seconds * 1000)
    hours, milliseconds = divmod(milliseconds, 3_600_000)
    minutes, milliseconds = divmod(milliseconds, 60_000)
    secs, milliseconds = divmod(milliseconds, 1000)
    return f"{hours:02d}:{minutes:02d}:{secs:02d},{milliseconds:03d}"


def main() -> int:
    for name, expected in EXPECTED.items():
        actual = sha(SOURCE / name)
        if actual != expected:
            raise RuntimeError(f"frozen source hash mismatch {name}: {actual}")
    story = json.loads(STORY_PATH.read_text())
    if story["estimated_duration_seconds"] != 415:
        raise RuntimeError("V11 planned runtime is not 415 seconds")
    if story["render_contract"] != {
        **story["render_contract"],
        "local_only": True,
        "paid_generation": False,
    }:
        raise RuntimeError("local/free render contract drift")
    standalone = parse_standalone_narration()
    if set(standalone) != {card["id"] for card in story["cards"]}:
        raise RuntimeError("standalone/storyboard card set mismatch")
    for card in story["cards"]:
        if standalone[card["id"]]["heading"] != card["heading"]:
            raise RuntimeError(f"heading drift Card {card['id']}")
        if standalone[card["id"]]["narration"] != card["narration"]:
            raise RuntimeError(f"narration drift Card {card['id']}")

    CARD_DIR.mkdir(parents=True, exist_ok=True)
    timeline_cards = []
    all_cues = []
    master_start = 0.0
    for card in story["cards"]:
        card_id = card["id"]
        text = card["narration"]
        raw, raw_events, attempts = load_or_synthesize(card_id, text)
        tokens = flatten_boundaries(text, raw_events)
        raw_speech_start = tokens[0]["raw_start_seconds"]
        raw_speech_end = tokens[-1]["raw_end_seconds"]
        raw_speech_span = raw_speech_end - raw_speech_start
        count = spoken_count(text)
        target_speech_span = count * 60 / TARGET_WPM
        atempo = raw_speech_span / target_speech_span
        if not 0.5 <= atempo <= 2.0:
            raise RuntimeError(f"Card {card_id} atempo outside safe range: {atempo}")
        crop_start = max(0.0, raw_speech_start - LEAD_SECONDS)
        crop_end = raw_speech_end + TAIL_SECONDS
        planned = float(card["planned_seconds"])
        delivered = CARD_DIR / f"card-{card_id}.wav"
        filter_chain = (
            f"atrim=start={crop_start:.9f}:end={crop_end:.9f},asetpts=PTS-STARTPTS,"
            f"atempo={atempo:.9f},aresample={SAMPLE_RATE},"
            f"aformat=sample_fmts=s16:channel_layouts=mono,"
            f"apad=whole_dur={planned:.9f},atrim=duration={planned:.9f}"
        )
        run(
            "ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(raw),
            "-af", filter_chain, "-ar", str(SAMPLE_RATE), "-ac", "1", "-c:a", "pcm_s16le", str(delivered),
        )
        duration = probe_duration(delivered)
        if abs(duration - planned) > 0.002:
            raise RuntimeError(f"Card {card_id} delivered duration drift: {duration} vs {planned}")
        transformed_tokens = []
        for index, item in enumerate(tokens):
            transformed_tokens.append({
                "index": index,
                "token": item["token"],
                "card_start_seconds": max(0.0, (item["raw_start_seconds"] - crop_start) / atempo),
                "card_end_seconds": max(0.0, (item["raw_end_seconds"] - crop_start) / atempo),
            })
        speech_start = transformed_tokens[0]["card_start_seconds"]
        speech_end = transformed_tokens[-1]["card_end_seconds"]
        speech_span = speech_end - speech_start
        delivered_wpm = count * 60 / speech_span
        if not 120 <= delivered_wpm <= 135:
            raise RuntimeError(f"Card {card_id} delivered WPM out of band: {delivered_wpm}")
        if speech_end > planned + 0.001:
            raise RuntimeError(f"Card {card_id} speech overruns planned card")

        cues = []
        token_cursor = 0
        for cue_index, cue_text in enumerate(cue_texts(card_id, text), 1):
            first, last = locate_sequence(transformed_tokens, cue_text, token_cursor)
            token_cursor = last + 1
            cue = {
                "id": f"c{card_id}-{cue_index:02d}",
                "card_id": card_id,
                "text": cue_text,
                "card_start_seconds": transformed_tokens[first]["card_start_seconds"],
                "card_end_seconds": transformed_tokens[last]["card_end_seconds"],
                "master_start_seconds": master_start + transformed_tokens[first]["card_start_seconds"],
                "master_end_seconds": master_start + transformed_tokens[last]["card_end_seconds"],
                "first_token_index": first,
                "last_token_index": last,
            }
            cues.append(cue)
            all_cues.append(cue)
        if token_cursor != len(transformed_tokens):
            raise RuntimeError(f"Card {card_id} captions did not consume every spoken token")
        if normalized_tokens(" ".join(cue["text"] for cue in cues)) != normalized_tokens(text):
            raise RuntimeError(f"Card {card_id} caption/source mismatch")

        def witness(name: str, phrase: str, edge: str = "end") -> dict:
            first, last = locate_sequence(transformed_tokens, phrase)
            at = transformed_tokens[first]["card_start_seconds"] if edge == "start" else transformed_tokens[last]["card_end_seconds"]
            return {
                "name": name,
                "phrase": phrase,
                "edge": edge,
                "card_seconds": at,
                "master_seconds": master_start + at,
            }

        reveals: list[dict] = []
        sentence_cues = cues
        if card_id == "01":
            reveals += [
                witness("primary_sources", "We read the original papers", "start"),
                witness("number_we_can_check", "One idea gives us a number", "start"),
                witness("galaxy_spin_limits", "For galaxy spin", "start"),
                witness("route_verdict", "So this route closes", "start"),
                witness("true_false_boundary", "The idea is not declared true or false", "start"),
            ]
        elif card_id == "02":
            reveals += [
                witness("bhu", "black-hole universe, or BHU for short", "end"),
                witness("proposal_1", "A closed universe inside a black hole", "start"),
                witness("proposal_2", "A collapse that bounces", "start"),
                witness("proposal_3", "A universe that inherits its parent's spin", "start"),
                witness("proposal_4", "Universes that reproduce", "start"),
                witness("proposal_5", "And baby universes", "start"),
                witness("no_shared_forecast", "Five ideas", "start"),
                witness("closing_record", "We wrote what we found into a closing record", "start"),
            ]
        elif card_id == "03":
            reveals += [
                witness("target", "It needs a number", "start"),
                witness("identify", "And if you find it", "start"),
                witness("neutron_stars", "It uses neutron stars", "start"),
                witness("pulsars", "The ones we can time as they spin", "start"),
            ]
        elif card_id == "04":
            reveals += [
                witness("family_tree", "One proposal", "start"),
                witness("mass_1_5", "one point five solar masses", "end"),
                witness("mass_2", "approximately two solar masses or above", "end"),
                witness("source_quote", "serious doubt or simply falsify", "end"),
            ]
        elif card_id == "05":
            reveals += [
                witness("demorest_uncertainty", "give or take point zero four", "end"),
                witness("fonseca_uncertainty", "give or take point zero seven", "end"),
                witness("percent_68_3", "sixty-eight point three percent", "end"),
                witness("percent_95_4", "ninety-five point four percent", "end"),
            ]
        elif card_id == "06":
            reveals += [
                witness("source_disjunction", "serious doubt, or simply falsify", "end"),
                witness("not_adjudicated", "does not decide which side applies", "end"),
                witness("named_regime", "entered the regime named by the source", "end"),
            ]
        elif card_id == "07":
            reveals += [
                witness("inherited_axis", "inherits its axis", "end"),
                witness("cw_ccw", "clockwise- and counterclockwise-spinning galaxy counts should be different", "end"),
                witness("no_amplitude", "What's missing is any number", "start"),
            ]
        elif card_id == "08":
            reveals += [
                witness("timeline", "after the galaxy studies", "end"),
                witness("post_data", "not a prediction made before the data", "end"),
                witness("forecast_blanks", "not a numerical forecast", "end"),
            ]
        elif card_id == "09":
            reveals += [
                witness("observed_difference", "spin-handedness difference", "end"),
                witness("not_identify", "would not identify BHU by itself", "end"),
                witness("other_causes", "several different causes", "end"),
                witness("measurement_not_identification", "not automatically a successful test", "end"),
            ]
        elif card_id == "10":
            reveals += [
                witness("no_range", "no pass-or-fail range", "end"),
                witness("no_signature", "without a unique signature", "end"),
                witness("trustworthy_measurement", "trustworthy measurement", "end"),
                witness("closing_line", "The hunt had a source", "start"),
            ]
        elif card_id == "11":
            reveals += [
                witness("target_gate", "a published calculation", "start"),
                witness("signature_gate", "a fingerprint only a black-hole birth would leave", "start"),
                witness("asymmetry_alone", "A confirmed spin asymmetry alone", "start"),
                witness("reopen", "This route reopens only", "start"),
            ]

        timeline_cards.append({
            "card_id": card_id,
            "heading": card["heading"],
            "narration": text,
            "text_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
            "planned_seconds": planned,
            "master_start_seconds": master_start,
            "master_end_seconds": master_start + planned,
            "raw_audio": str(raw.relative_to(ROOT)),
            "raw_audio_sha256": sha(raw),
            "delivered_audio": str(delivered.relative_to(ROOT)),
            "delivered_audio_sha256": sha(delivered),
            "synthesis_attempts_this_run": attempts,
            "spoken_compound_count": count,
            "target_wpm": TARGET_WPM,
            "atempo_factor": atempo,
            "speech_start_seconds": speech_start,
            "speech_end_seconds": speech_end,
            "speech_span_seconds": speech_span,
            "delivered_wpm": delivered_wpm,
            "dwell_after_speech_seconds": planned - speech_end,
            "tokens": transformed_tokens,
            "captions": cues,
            "reveals": reveals,
        })
        master_start += planned
        print(f"Card {card_id}: {count} words / {speech_span:.3f}s = {delivered_wpm:.2f} WPM; dwell {planned - speech_end:.3f}s")

    if abs(master_start - 415) > 0.001:
        raise RuntimeError(f"master timeline drift: {master_start}")
    with wave.open(str(MASTER_PATH), "wb") as output:
        output.setnchannels(1)
        output.setsampwidth(2)
        output.setframerate(SAMPLE_RATE)
        for card in timeline_cards:
            with wave.open(str(ROOT / card["delivered_audio"]), "rb") as source:
                if (source.getnchannels(), source.getsampwidth(), source.getframerate()) != (1, 2, SAMPLE_RATE):
                    raise RuntimeError(f"Card {card['card_id']} WAV format drift")
                output.writeframes(source.readframes(source.getnframes()))
    master_duration = probe_duration(MASTER_PATH)
    if abs(master_duration - 415) > 0.002:
        raise RuntimeError(f"master WAV duration drift: {master_duration}")

    srt_lines = []
    for index, cue in enumerate(all_cues, 1):
        srt_lines += [
            str(index),
            f"{timestamp(cue['master_start_seconds'])} --> {timestamp(cue['master_end_seconds'])}",
            cue["text"],
            "",
        ]
    SRT_PATH.write_text("\n".join(srt_lines), encoding="utf-8")
    timeline = {
        "status": "PASS_EXACT_V11_AUDIO_BUILT_REAL_WPM_IN_BAND",
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_hashes": EXPECTED,
        "provider": "Microsoft Edge TTS free endpoint via edge-tts",
        "paid_generation": False,
        "voice": VOICE,
        "edge_tts_version": edge_tts.__version__,
        "input_unit": "one exact frozen card narration per request",
        "target_wpm": TARGET_WPM,
        "sample_rate": SAMPLE_RATE,
        "music": False,
        "master_audio": str(MASTER_PATH.relative_to(ROOT)),
        "master_audio_sha256": sha(MASTER_PATH),
        "master_duration_seconds": master_duration,
        "captions": str(SRT_PATH.relative_to(ROOT)),
        "captions_sha256": sha(SRT_PATH),
        "caption_token_match_all_cards": True,
        "cards": timeline_cards,
    }
    TIMELINE_PATH.write_text(json.dumps(timeline, indent=2, ensure_ascii=False) + "\n")
    print(TIMELINE_PATH)
    print(MASTER_PATH)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
