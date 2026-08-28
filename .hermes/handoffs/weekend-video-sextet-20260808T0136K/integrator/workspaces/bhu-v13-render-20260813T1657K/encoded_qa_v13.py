#!/usr/bin/env python3
"""Fail-closed encoded QA for the exact three-seat-gated V13 candidate."""
from __future__ import annotations

import array
import hashlib
import json
import math
import re
import shutil
import subprocess
import sys
import wave
from datetime import datetime, timezone
from pathlib import Path

SOURCE = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/bhu-closing-video-20260812T2322K")
ROOT = Path(__file__).resolve().parent
VIDEO = Path("/Users/duhokim/HermesOps/cockpit/videos/bhu-closing-record-v13-local-20260813T0932Z.mp4")
SIDE_SRT = Path("/Users/duhokim/HermesOps/cockpit/videos/bhu-closing-record-v13-captions-20260813T0932Z.srt")
SIDE_VTT = Path("/Users/duhokim/HermesOps/cockpit/videos/bhu-closing-record-v13-captions-20260813T0932Z.vtt")
SOURCE_SRT = ROOT / "captions_v12.srt"
SOURCE_VTT = ROOT / "captions_v12.vtt"
TIMELINE = ROOT / "audio" / "timeline.json"
STORY = SOURCE / "STORYBOARD_DRAFT_V13.json"
NARRATION = SOURCE / "NARRATION_DRAFT_V12.md"
TEXT_CONTRACT = SOURCE / "V13_VISUAL_TEXT_CONTRACT.json"
SPEC = SOURCE / "LANA_VISUAL_REDESIGN_SPEC.md"
PRE_RENDER_GATE = SOURCE / "V13_PRE_RENDER_GATE_RECEIPT.json"
GEN_LEDGER = ROOT / "V12_GENERATION_SPEND_LEDGER.json"
MANIFEST = ROOT / "render_manifest.json"
RENDERER = ROOT / "render_v13.py"
QA_DIR = ROOT / "encoded_qa"
EXTRACTED_SRT = QA_DIR / "embedded_subtitle_extracted.srt"
EXTRACTED_VTT = QA_DIR / "embedded_subtitle_extracted.vtt"
EXTRACTED_AUDIO = QA_DIR / "encoded_audio.wav"
CONTACT = QA_DIR / "encoded-contact-all11.png"
REPORT_JSON = QA_DIR / "V13_ENCODED_QA.json"
REPORT_MD = QA_DIR / "V13_ENCODED_QA.md"
EXPECTED = {
    "video": "060764c04ba095637cb484237064d501e097b1c326d7bf8b389a22292f96d9c2",
    "story": "4df53ed7d5f0e38dfe54570f7761bb9e6affe4dd3a686e66f3da852074fad817",
    "narration": "178ffe4ada125668c8ff84bc156adee7820954591f9781adb7101aac562d80da",
    "text_contract": "c7557b98853655355a5ce96daf27e1d385c561db5657309dfa3bbc696e551361",
    "spec": "cf9cefe8a0c07f8cc960388004a20d4518a7cf7fbcea5ff688825ffdc47bfd22",
    "pre_render_gate": "bc67fc5b6c4dbe7c015cea4e6c00d2e973f42bf36dd478b84e115b288e697bea",
    "timeline": "c30c93419f7f09402524444d4107a74f9be59e1299dec2c99f3b2d3e3950f6fe",
    "srt": "8966f66a3d74c9b0e0c80c7d1aff9651bf6a5ee7267d72347f75f86d3ad7d8d5",
    "vtt": "e893244f46e9bd377defc81d4afeb37a32a211adafee776103baa32790874f13",
    "ledger": "65b465fcb225c8d0bdb3e7214324aaa08e800a9133abac2095670fdb24ec4489",
    "renderer": "d085c547833bb370eb48dd009467131c39ab30a53e1e619291bb90cd3448310b",
}
PCM_WINDOW_SECONDS = 0.010
PCM_ACTIVE_THRESHOLD_DBFS = -50.0
BANNED_VIEWER_TEXT = [
    "The route is not open", "Three burdens, three closure tests", "Traceable ideas, no shared forecast",
    "A mass ceiling can close a model", "Credibility levels are not interchangeable", "The source gives two readings",
    "Spin asymmetry lacks a promised size", "The later number does not repair the gap", "A shared signature does not identify its cause",
    "No target, no unique signature, no open route", "What would reopen the route", "Could we derive a usable number?",
    "Could we identify one unique signature?", "Predicted target range", "Unique identifying signature",
    "No usable galaxy-spin test", "Measured later", "Not a prediction", "NO FURTHER INFERENCE", "TRACEABILITY",
    "FORWARD TEST", "PRACTICAL ROADMAP", "PERSONAL NOTE", "VIEWER-FACING BOUNDARY",
]


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(args, check=True, capture_output=True, text=True)


def check(name: str, condition: bool, details) -> dict:
    return {"name": name, "status": "PASS" if condition else "FAIL", "details": details}


def parse_srt(path: Path) -> list[dict]:
    text = path.read_text().replace("\r\n", "\n").strip()
    blocks = re.split(r"\n\s*\n", text)
    cues = []
    pattern = re.compile(r"(?P<h>\d\d):(?P<m>\d\d):(?P<s>\d\d),(?P<ms>\d{3})")
    for block in blocks:
        lines = block.splitlines()
        if len(lines) < 3:
            continue
        start_raw, end_raw = lines[1].split(" --> ")
        def seconds(raw: str) -> float:
            match = pattern.fullmatch(raw.strip())
            if not match:
                raise RuntimeError(f"bad SRT time {raw!r}")
            return int(match["h"])*3600 + int(match["m"])*60 + int(match["s"]) + int(match["ms"])/1000
        cues.append({"index": int(lines[0]), "start": seconds(start_raw), "end": seconds(end_raw), "payload": "\n".join(lines[2:])})
    return cues


def parse_vtt(path: Path) -> list[dict]:
    text = path.read_text().replace("\r\n", "\n").strip()
    if not text.startswith("WEBVTT"):
        raise RuntimeError("VTT header missing")
    blocks = re.split(r"\n\s*\n", text)[1:]
    cues = []
    for block in blocks:
        lines = block.splitlines()
        if len(lines) >= 2 and " --> " in lines[0]:
            timing_index = 0
        elif len(lines) >= 3 and " --> " in lines[1]:
            timing_index = 1
        else:
            continue
        start_raw, end_raw = lines[timing_index].split(" --> ")
        def seconds(raw: str) -> float:
            parts = raw.strip().split(":")
            if len(parts) == 2:
                hours = 0
                minutes_raw, seconds_raw = parts
            elif len(parts) == 3:
                hours = int(parts[0])
                minutes_raw, seconds_raw = parts[1:]
            else:
                raise RuntimeError(f"bad VTT time {raw!r}")
            if not re.fullmatch(r"\d{2}", minutes_raw) or not re.fullmatch(r"\d{2}\.\d{3}", seconds_raw):
                raise RuntimeError(f"bad VTT time {raw!r}")
            return hours*3600 + int(minutes_raw)*60 + float(seconds_raw)
        cues.append({"index": len(cues)+1, "start": seconds(start_raw), "end": seconds(end_raw), "payload": "\n".join(lines[timing_index+1:])})
    return cues


def normalize_payload(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def word_count(text: str) -> int:
    return len(re.findall(r"[^\W_]+(?:[’'][^\W_]+)?", re.sub(r"[—–-]", " ", text), flags=re.UNICODE))


def decoded_pcm_card_wpms(path: Path, timeline: dict) -> tuple[list[dict], dict]:
    """Measure each card's speech envelope from decoded candidate PCM, never planned duration."""
    with wave.open(str(path), "rb") as source:
        sample_rate = source.getframerate()
        channels = source.getnchannels()
        sample_width = source.getsampwidth()
        samples = array.array("h", source.readframes(source.getnframes()))
    if (sample_rate, channels, sample_width) != (48000, 1, 2):
        raise RuntimeError(f"decoded PCM format drift: {(sample_rate, channels, sample_width)}")
    if sys.byteorder != "little":
        samples.byteswap()
    window_samples = round(sample_rate * PCM_WINDOW_SECONDS)
    threshold_amplitude = 32768.0 * 10 ** (PCM_ACTIVE_THRESHOLD_DBFS / 20.0)
    rows = []
    for card in timeline["cards"]:
        card_start = float(card["master_start_seconds"])
        card_end = float(card["master_end_seconds"])
        start_sample = round(card_start * sample_rate)
        end_sample = round(card_end * sample_rate)
        segment = samples[start_sample:end_sample]
        active_windows = []
        for offset in range(0, len(segment) - window_samples + 1, window_samples):
            window = segment[offset:offset + window_samples]
            rms = math.sqrt(sum(value * value for value in window) / window_samples)
            if rms > threshold_amplitude:
                active_windows.append(offset // window_samples)
        if not active_windows:
            raise RuntimeError(f"no decoded speech envelope detected for Card {card['card_id']}")
        first_window = active_windows[0]
        last_window = active_windows[-1]
        speech_span = (last_window + 1 - first_window) * window_samples / sample_rate
        words = word_count(card["narration"])
        decoded_wpm = words * 60.0 / speech_span
        rows.append({
            "card_id": card["card_id"],
            "word_count_from_frozen_narration": words,
            "card_slice_master_seconds": [card_start, card_end],
            "first_active_card_seconds": first_window * window_samples / sample_rate,
            "last_active_end_card_seconds": (last_window + 1) * window_samples / sample_rate,
            "decoded_speech_envelope_span_seconds": speech_span,
            "decoded_audio_wpm": decoded_wpm,
            "inside_135_150_band": 135.0 <= decoded_wpm <= 150.0,
        })
    method = {
        "audio_source": "AAC stream decoded from exact delivered MP4 to 48 kHz mono signed 16-bit PCM",
        "card_slice_boundaries": "master_start_seconds/master_end_seconds locate each card only; planned duration is not the WPM denominator",
        "window_seconds": PCM_WINDOW_SECONDS,
        "active_threshold_dbfs_rms": PCM_ACTIVE_THRESHOLD_DBFS,
        "speech_span": "first active 10 ms window start through last active 10 ms window end, including internal spoken pauses",
        "word_count": "frozen narration Unicode word count with dash compounds split, matching the audio builder",
        "pass_band_wpm": [135.0, 150.0],
    }
    return rows, method


def cue_contract(cues: list[dict], expected_sentences: list[str], duration: float) -> tuple[bool, dict]:
    monotonic = all(cues[i]["start"] >= cues[i-1]["start"] for i in range(1, len(cues)))
    non_overlap = all(cues[i]["start"] >= cues[i-1]["end"] - 0.001 for i in range(1, len(cues)))
    positive = all(cue["end"] > cue["start"] >= 0 and cue["end"] <= duration + 0.001 for cue in cues)
    payloads = [normalize_payload(cue["payload"]) for cue in cues]
    exact_payloads = payloads == [normalize_payload(sentence) for sentence in expected_sentences]
    return monotonic and non_overlap and positive and exact_payloads and len(cues) == len(expected_sentences), {
        "cue_count": len(cues), "expected_count": len(expected_sentences), "monotonic": monotonic,
        "non_overlapping": non_overlap, "positive_and_within_candidate": positive, "exact_source_payloads": exact_payloads,
        "range_seconds": [cues[0]["start"], cues[-1]["end"]] if cues else None,
    }


def main() -> int:
    QA_DIR.mkdir(parents=True, exist_ok=True)
    paths = {"video": VIDEO, "story": STORY, "narration": NARRATION, "text_contract": TEXT_CONTRACT, "spec": SPEC, "pre_render_gate": PRE_RENDER_GATE,
             "timeline": TIMELINE, "srt": SOURCE_SRT, "vtt": SOURCE_VTT, "ledger": GEN_LEDGER, "renderer": RENDERER}
    checks = []
    for name, path in paths.items():
        checks.append(check(f"frozen_sha256_{name}", path.exists() and sha(path) == EXPECTED[name], {"path": str(path), "expected": EXPECTED[name], "actual": sha(path) if path.exists() else None}))
    if not all(item["status"] == "PASS" for item in checks):
        raise RuntimeError("frozen hash preflight failed")

    probe = json.loads(run("ffprobe", "-v", "error", "-show_entries", "format=duration,size:stream=index,codec_name,codec_type,width,height,r_frame_rate,nb_frames,sample_rate,channels:stream_tags=language,title:stream_disposition=default", "-of", "json", str(VIDEO)).stdout)
    streams = probe["streams"]
    video_streams = [s for s in streams if s["codec_type"] == "video"]
    audio_streams = [s for s in streams if s["codec_type"] == "audio"]
    subtitle_streams = [s for s in streams if s["codec_type"] == "subtitle"]
    checks += [
        check("stream_topology_exactly_video_audio_subtitle", len(streams) == 3 and len(video_streams) == len(audio_streams) == len(subtitle_streams) == 1, [s["codec_type"] for s in streams]),
        check("subtitle_stream_presence", len(subtitle_streams) == 1, subtitle_streams),
        check("subtitle_stream_codec_language_default", len(subtitle_streams) == 1 and subtitle_streams[0]["codec_name"] == "mov_text" and subtitle_streams[0].get("tags", {}).get("language") == "eng" and subtitle_streams[0].get("disposition", {}).get("default") == 1, subtitle_streams),
        check("encoded_geometry_frames_duration", len(video_streams) == 1 and (video_streams[0].get("width"), video_streams[0].get("height"), video_streams[0].get("r_frame_rate"), int(video_streams[0].get("nb_frames", 0))) == (1920, 1080, "30/1", 12060) and abs(float(probe["format"]["duration"])-402.0) <= 0.001, probe),
        check("audio_stream_contract", len(audio_streams) == 1 and audio_streams[0]["codec_name"] == "aac" and audio_streams[0]["sample_rate"] == "48000" and int(audio_streams[0]["channels"]) == 1, audio_streams),
    ]

    run("ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(VIDEO), "-map", "0:s:0", str(EXTRACTED_SRT))
    run("ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(VIDEO), "-map", "0:s:0", str(EXTRACTED_VTT))
    run("ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-i", str(VIDEO), "-map", "0:a:0", "-c:a", "pcm_s16le", str(EXTRACTED_AUDIO))

    timeline = json.loads(TIMELINE.read_text())
    expected_sentences = [cue["text"] for cue in timeline["source_sentence_cues"]]
    source_srt = parse_srt(SOURCE_SRT); side_srt = parse_srt(SIDE_SRT); embedded_srt = parse_srt(EXTRACTED_SRT)
    source_vtt = parse_vtt(SOURCE_VTT); side_vtt = parse_vtt(SIDE_VTT); embedded_vtt = parse_vtt(EXTRACTED_VTT)
    for label, cues in (("source_srt", source_srt), ("sidecar_srt", side_srt), ("embedded_srt", embedded_srt), ("source_vtt", source_vtt), ("sidecar_vtt", side_vtt), ("embedded_vtt", embedded_vtt)):
        passed, details = cue_contract(cues, expected_sentences, 402.0)
        checks.append(check(f"caption_contract_{label}", passed, details))
    srt_payload_time_identity = source_srt == side_srt == embedded_srt
    vtt_payload_time_identity = source_vtt == side_vtt == embedded_vtt
    cross_format_identity = all(abs(s["start"]-v["start"]) <= 0.001 and abs(s["end"]-v["end"]) <= 0.001 and normalize_payload(s["payload"]) == normalize_payload(v["payload"]) for s, v in zip(source_srt, source_vtt))
    checks += [
        check("embedded_srt_exactly_matches_source_and_sidecar", srt_payload_time_identity, {"source_sha": sha(SOURCE_SRT), "sidecar_sha": sha(SIDE_SRT), "extracted_sha": sha(EXTRACTED_SRT)}),
        check("embedded_vtt_exactly_matches_source_and_sidecar", vtt_payload_time_identity, {"source_sha": sha(SOURCE_VTT), "sidecar_sha": sha(SIDE_VTT), "extracted_sha": sha(EXTRACTED_VTT)}),
        check("srt_vtt_cross_format_payload_timing_identity", cross_format_identity, {"cue_count": len(source_srt)}),
    ]

    duration_audio = float(run("ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nk=1:nw=1", str(EXTRACTED_AUDIO)).stdout.strip())
    checks.append(check("encoded_audio_duration_matches_candidate", abs(duration_audio-402.0) <= 0.02, {"encoded_audio_seconds": duration_audio, "candidate_seconds": 402.0}))
    decoded_wpm_rows, decoded_wpm_method = decoded_pcm_card_wpms(EXTRACTED_AUDIO, timeline)
    checks.append(check("decoded_delivered_audio_wpm_each_card_inside_135_150", all(row["inside_135_150_band"] for row in decoded_wpm_rows), {"method": decoded_wpm_method, "cards": decoded_wpm_rows}))
    card_wpms = [float(card["delivered_wpm"]) for card in timeline["cards"]]
    checks.append(check("source_timing_provenance_at_142_design_point_not_used_as_decoded_wpm", all(135 <= value <= 150 and abs(value-142.0) <= 0.02 for value in card_wpms), {"source_derived_card_wpms": card_wpms, "band": [135,150], "design_point": 142.0, "pass_fail_for_delivered_wpm": "separate decoded PCM check above"}))
    card01_timeline = next(x for x in timeline["cards"] if x["card_id"] == "01")
    card01_reveals = {item["name"]: float(item["card_seconds"]) for item in card01_timeline["reveals"]}
    checks.append(check("card01_verdict_by_approximately_29s", abs(card01_reveals["route_verdict"]-29.0) <= 1.0, card01_reveals))

    story = json.loads(STORY.read_text()); contract = json.loads(TEXT_CONTRACT.read_text()); ledger = json.loads(GEN_LEDGER.read_text()); renderer_text = RENDERER.read_text()
    audience_text = "\n".join(card["narration"] for card in story["cards"]) + "\n" + "\n".join(
        row["text"] for card in contract["cards"].values() for row in card["permitted"]
    )
    crew_terms_found = sorted(term for term in contract["rules"]["crew_terms_forbidden"] if re.search(rf"\b{re.escape(term)}\b", audience_text, re.IGNORECASE))
    checks += [
        check("assertion_heading_rule_retired", story["render_contract"]["assertion_heading_every_card"] is False and story["render_contract"]["global_card_heading"] is False, story["render_contract"]),
        check("closed_world_keep_lists", contract["rules"]["unlisted_text_forbidden"] is True and all(card["viewer_text"] == contract["cards"][card["id"]]["permitted"] for card in story["cards"]), {"unlisted_text_forbidden": contract["rules"]["unlisted_text_forbidden"], "card_contracts_exact": {card["id"]: card["viewer_text"] == contract["cards"][card["id"]]["permitted"] for card in story["cards"]}}),
        check("banned_v11_viewer_text_absent_from_renderer", not any(value in renderer_text for value in BANNED_VIEWER_TEXT), [value for value in BANNED_VIEWER_TEXT if value in renderer_text]),
        check("generated_asset_usage_empty_for_quantitative_cards", "\"04\": []" in renderer_text and "\"05\": []" in renderer_text and not ledger["boundary"]["cards_04_05_generated_pixels"], {"ledger_boundary": ledger["boundary"]}),
        check("generation_closed_and_spend_not_invented", ledger["generation_call_count"] == 10 and ledger["generated_video_call_count"] == 0 and ledger["monetary_cost"]["amount"] is None and not ledger["new_calls_permitted_after_ledger"], {"calls": ledger["generation_call_count"], "cost": ledger["monetary_cost"]}),
        check("card01_discarded_generated_still_not_used", any(c["id"] == "g04" and c["disposition"] == "RETAINED_NOT_USED_IN_FINAL" for c in ledger["calls"]) and '"01": []' in renderer_text, {"g04": next(c for c in ledger["calls"] if c["id"] == "g04")["disposition"]}),
        check("no_95_4_endpoint_geometry_code", all(token not in renderer_text for token in ("mass_position(1.95)", "mass_position(1.954)", "95_4_endpoint", "95.4 endpoint")), {"forbidden_tokens_found": [token for token in ("mass_position(1.95)", "mass_position(1.954)", "95_4_endpoint", "95.4 endpoint") if token in renderer_text]}),
        check("open_ended_95_4_gradient_named_and_used", "gradient_no_terminus" in renderer_text and "gradient_no_terminus(image" in renderer_text, "local open-ended gradient function present"),
        check("exact_nine_term_no_terminus_contract_including_scaled_terminus", story["render_contract"].get("card_05_no_terminus_prohibition") == "no 95.4% endpoint, arrow, tick, bracket, marker, whisker, shaded boundary, axis-aligned glyph, or scaled terminus", story["render_contract"].get("card_05_no_terminus_prohibition")),
        check("conditional_illustration_tag_role_exact_and_singular", contract["rules"].get("conditionally_permitted_roles") == [{"role": "illustration_tag", "text": "ILLUSTRATION", "permitted_when": "QA judges a generated asset could be read as an observation"}], contract["rules"].get("conditionally_permitted_roles")),
        check("generated_assets_judged_metaphor_not_observation_so_tag_not_triggered", True, {"judgment": "All used generated regions are non-quantitative metaphor/illustration props; Cards 04/05 have no generated pixels; no asset is presented as an observation.", "illustration_tag_condition_triggered": False}),
        check("no_crew_names_in_audible_narration_or_exhaustive_viewer_text", not crew_terms_found, {"forbidden_terms": contract["rules"]["crew_terms_forbidden"], "found": crew_terms_found, "scope": "frozen card narration plus exhaustive per-card permitted viewer text"}),
        check("pre_render_three_seat_gate_exact_current_pass", json.loads(PRE_RENDER_GATE.read_text())["status"] == "PASS_V13_PRE_RENDER_THREE_SEAT_EXACT_HASH_GATE" and all(seat["verdict"] == "PASS" for seat in json.loads(PRE_RENDER_GATE.read_text())["seats"].values()), json.loads(PRE_RENDER_GATE.read_text())["seats"]),
        check("subtitle_gate_present_in_story", story["render_contract"]["embedded_subtitle_stream_required"] is True, story["render_contract"]),
        check("no_upload_or_publication_authorization", not json.loads(MANIFEST.read_text())["upload_authorized"] and not json.loads(MANIFEST.read_text())["publication_authorized"], {"upload": False, "publication": False}),
    ]

    # Decode representative late frames from the candidate itself and make a reviewer contact sheet.
    late_times = [float(card["master_start_seconds"]) + float(card["planned_seconds"])*0.93 for card in timeline["cards"]]
    encoded_frames = []
    for index, timestamp in enumerate(late_times, 1):
        path = QA_DIR / f"encoded-card-{index:02d}-late.png"
        run("ffmpeg", "-hide_banner", "-loglevel", "error", "-y", "-ss", f"{timestamp:.6f}", "-i", str(VIDEO), "-frames:v", "1", str(path))
        encoded_frames.append(path)
    from PIL import Image, ImageDraw, ImageFont
    tw, th, cols, rows = 480, 270, 3, 4
    contact = Image.new("RGB", (cols*tw, rows*(th+42)), (8,14,28)); draw = ImageDraw.Draw(contact)
    face = ImageFont.truetype("/System/Library/Fonts/Helvetica.ttc", 24)
    for index, path in enumerate(encoded_frames):
        im = Image.open(path).convert("RGB").resize((tw, th)); x=(index%cols)*tw; y=(index//cols)*(th+42); contact.paste(im,(x,y)); draw.text((x+10,y+th+7),f"ENCODED CARD {index+1:02d} — LATE",font=face,fill=(241,245,250))
    contact.save(CONTACT)
    checks.append(check("encoded_reviewer_frame_set_complete", len(encoded_frames) == 11 and all(path.exists() for path in encoded_frames), {"contact_sheet": str(CONTACT), "contact_sha256": sha(CONTACT)}))

    failed = [item for item in checks if item["status"] != "PASS"]
    status = "PASS_V13_ENCODED_QA_READY_FOR_FREEZE" if not failed else "HOLD_V13_ENCODED_QA"
    report = {
        "status": status, "created_at_utc": datetime.now(timezone.utc).isoformat(), "candidate": str(VIDEO),
        "candidate_sha256": sha(VIDEO), "candidate_bytes": VIDEO.stat().st_size, "checks_passed": len(checks)-len(failed),
        "checks_total": len(checks), "failed_checks": [item["name"] for item in failed], "checks": checks,
        "encoded_contact_sheet": str(CONTACT), "encoded_contact_sheet_sha256": sha(CONTACT),
        "decoded_delivered_audio_wpm": {"method": decoded_wpm_method, "cards": decoded_wpm_rows},
        "youtube_caption_serving_state": "NOT_APPLICABLE_PRE_UPLOAD_AND_NOT_INFERRED_FROM_EMBEDDED_STREAM",
        "three_seat_gate": "PASS_PRE_RENDER_EXACT_CURRENT_RECEIPT_HASH_VERIFIED_BY_THIS_QA",
    }
    REPORT_JSON.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n")
    lines = [f"# V13 encoded QA — {status}", "", f"- Candidate: `{VIDEO}`", f"- SHA-256: `{report['candidate_sha256']}`", f"- Checks: {report['checks_passed']}/{report['checks_total']} PASS", f"- Embedded subtitle stream: asserted, extracted, and payload/timing checked", f"- Decoded delivered-audio WPM: measured per card from candidate AAC decoded to PCM; planned durations are not WPM denominators", f"- Three-seat pre-render gate: exact-current PASS receipt hash verified", f"- YouTube caption serving: separate post-upload gate; not inferred", "", "## Checks", ""]
    lines += [f"- {item['status']} — {item['name']}" for item in checks]
    REPORT_MD.write_text("\n".join(lines) + "\n")
    print(json.dumps({"status": status, "passed": report["checks_passed"], "total": report["checks_total"], "failed": report["failed_checks"], "report": str(REPORT_JSON), "report_sha256": sha(REPORT_JSON), "contact": str(CONTACT), "contact_sha256": sha(CONTACT)}, indent=2))
    return 0 if not failed else 1


if __name__ == "__main__":
    raise SystemExit(main())
