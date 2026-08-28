#!/usr/bin/env python3
"""Release the exact BHU V13 candidate unlisted, caption it, then retire exact V11.

The actual videos.insert call is delegated to upload_paper_video_unlisted.py.
There is no public-visibility path in this program.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import time
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

WORKSPACE = Path(__file__).resolve().parent
TOKEN = Path("/Users/duhokim/HermesOps/scripts/token_manage.json")
UPLOADER = Path("/Users/duhokim/HermesOps/scripts/upload_paper_video_unlisted.py")
VIDEO = Path("/Users/duhokim/HermesOps/cockpit/videos/bhu-closing-record-v13-local-20260813T0932Z.mp4")
SRT = Path("/Users/duhokim/HermesOps/cockpit/videos/bhu-closing-record-v13-captions-20260813T0932Z.srt")
VTT = Path("/Users/duhokim/HermesOps/cockpit/videos/bhu-closing-record-v13-captions-20260813T0932Z.vtt")
DESCRIPTION = Path("/Users/duhokim/HermesOps/scratchpad/bhu_description_v3.txt")
FREEZE = Path(
    "/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/"
    "weekend-video-sextet-20260808T0136K/bhu-closing-video-20260812T2322K/"
    "V13_FREEZE_FOR_UNLISTED_RELEASE.json"
)
ENCODED_QA = WORKSPACE / "encoded_qa" / "V13_ENCODED_QA.json"
VISUAL_PREFLIGHT = WORKSPACE / "V13_DECODED_FRAME_VISUAL_PREFLIGHT.json"
CHECKPOINT = WORKSPACE / "V13_YOUTUBE_UPLOAD_CHECKPOINT.json"
RECEIPT = WORKSPACE / "V13_UNLISTED_RELEASE_RECEIPT.json"
UPLOADER_STDOUT = WORKSPACE / "V13_UPLOADER_STDOUT.txt"
UPLOADER_STDERR = WORKSPACE / "V13_UPLOADER_STDERR.txt"

EXPECTED_CHANNEL_ID = "UCte32tv-Xre6rmkYI0HPc4Q"
EXPECTED_CHANNEL_TITLE = "Duho Kim"
TITLE = "Inside a black hole? What the sources predict—and why this route closed"
PRIVACY = "unlisted"
CAPTION_NAME = "English (manual V13)"
V11_ID = "e_eu-CoimOE"
RETIRED_V7_ID = "RbgW_4U7bi0"
KNOWN_SAME_TITLE_IDS = {V11_ID, RETIRED_V7_ID}
REQUIRED_SCOPES = {
    "https://www.googleapis.com/auth/youtube.force-ssl",
    "https://www.googleapis.com/auth/youtube.upload",
}
EXPECTED_HASHES = {
    VIDEO: "060764c04ba095637cb484237064d501e097b1c326d7bf8b389a22292f96d9c2",
    SRT: "8966f66a3d74c9b0e0c80c7d1aff9651bf6a5ee7267d72347f75f86d3ad7d8d5",
    VTT: "e893244f46e9bd377defc81d4afeb37a32a211adafee776103baa32790874f13",
    DESCRIPTION: "2a8da3d3cd158339c6b178b31442fb17b51dd328adbeb38738517b5ebf4bc762",
    FREEZE: "2bd295603b84ba07616116ba06f935804c818e110b67e04918a85ba517725d5e",
    ENCODED_QA: "051fb8c2643902a87d5e493fbd31eb13753f93b87bfb594cc5b4e5aef24c466f",
    VISUAL_PREFLIGHT: "93330e834836d8cd715219cb74cfc999f87eefcad8ab0d5b1b17d9ec97a8d1e2",
}
PYTHON = "/Users/duhokim/.hermes/hermes-agent/venv/bin/python"
FFPROBE = "/opt/homebrew/bin/ffprobe"


def now() -> str:
    return datetime.now(timezone.utc).isoformat()


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def atomic_json(path: Path, value: dict) -> None:
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(
        json.dumps(value, indent=2, sort_keys=True, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    os.replace(temporary, path)


def load_youtube():
    credentials = Credentials.from_authorized_user_file(str(TOKEN))
    granted = set(credentials.scopes or [])
    missing = REQUIRED_SCOPES - granted
    if missing:
        raise RuntimeError("YOUTUBE_CREDENTIAL_SCOPE_MISSING:" + json.dumps(sorted(missing)))
    if not credentials.valid:
        if not credentials.refresh_token:
            raise RuntimeError("YOUTUBE_CREDENTIAL_HAS_NO_REFRESH_TOKEN")
        credentials.refresh(Request())
        TOKEN.write_text(credentials.to_json(), encoding="utf-8")
        os.chmod(TOKEN, 0o600)
    return build("youtube", "v3", credentials=credentials, cache_discovery=False), sorted(granted)


def assert_owner(youtube) -> dict:
    items = youtube.channels().list(part="snippet,contentDetails", mine=True).execute().get("items", [])
    identity = [{"id": item["id"], "title": item["snippet"]["title"]} for item in items]
    if len(items) != 1:
        raise RuntimeError("YOUTUBE_CHANNEL_IDENTITY_AMBIGUOUS:" + json.dumps(identity))
    item = items[0]
    if item["id"] != EXPECTED_CHANNEL_ID or item["snippet"]["title"] != EXPECTED_CHANNEL_TITLE:
        raise RuntimeError("WRONG_YOUTUBE_CHANNEL:" + json.dumps(identity))
    return item


def inventory_uploads(youtube, uploads_playlist: str) -> list[dict]:
    rows: list[dict] = []
    page_token = None
    while True:
        response = youtube.playlistItems().list(
            part="snippet,contentDetails",
            playlistId=uploads_playlist,
            maxResults=50,
            pageToken=page_token,
        ).execute()
        for item in response.get("items", []):
            rows.append(
                {
                    "video_id": item["contentDetails"]["videoId"],
                    "title": item["snippet"]["title"],
                    "published_at": item["snippet"].get("publishedAt"),
                }
            )
        page_token = response.get("nextPageToken")
        if not page_token:
            return rows


def read_video(youtube, video_id: str) -> dict:
    items = youtube.videos().list(
        part="snippet,status,contentDetails,processingDetails",
        id=video_id,
    ).execute().get("items", [])
    if len(items) != 1:
        raise RuntimeError("VIDEO_ID_NOT_READABLE:" + video_id)
    return items[0]


def iso_duration_seconds(value: str) -> float:
    match = re.fullmatch(r"PT(?:(\d+)H)?(?:(\d+)M)?(?:(\d+(?:\.\d+)?)S)?", value)
    if not match:
        raise ValueError(value)
    hours = float(match.group(1) or 0)
    minutes = float(match.group(2) or 0)
    seconds = float(match.group(3) or 0)
    return hours * 3600 + minutes * 60 + seconds


def local_preflight() -> dict:
    for path in [TOKEN, UPLOADER, *EXPECTED_HASHES]:
        if not path.exists():
            raise FileNotFoundError(path)
    actual_hashes = {str(path): sha256(path) for path in EXPECTED_HASHES}
    for path, expected in EXPECTED_HASHES.items():
        if actual_hashes[str(path)] != expected:
            raise RuntimeError(f"FROZEN_HASH_MISMATCH:{path}:{expected}:{actual_hashes[str(path)]}")

    freeze = json.loads(FREEZE.read_text(encoding="utf-8"))
    if freeze.get("status") != "FROZEN_V13_READY_FOR_GATED_UNLISTED_RELEASE":
        raise RuntimeError("FREEZE_STATUS_NOT_RELEASE_READY")
    if freeze.get("candidate", {}).get("sha256") != EXPECTED_HASHES[VIDEO]:
        raise RuntimeError("FREEZE_CANDIDATE_HASH_MISMATCH")
    if freeze.get("pre_render_three_seat_gate", {}).get("status") != "PASS_V13_PRE_RENDER_THREE_SEAT_EXACT_HASH_GATE":
        raise RuntimeError("THREE_SEAT_GATE_NOT_PASS")
    if any(seat.get("verdict") != "PASS" for seat in freeze["pre_render_three_seat_gate"]["seats"].values()):
        raise RuntimeError("THREE_SEAT_GATE_HAS_NON_PASS")
    if freeze.get("local_qa", {}).get("checks") != "45/45":
        raise RuntimeError("ENCODED_QA_NOT_45_OF_45")
    if not freeze.get("caption_gate", {}).get("embedded_stream_present"):
        raise RuntimeError("EMBEDDED_SUBTITLE_STREAM_ABSENT")
    if not freeze.get("decoded_delivered_audio_wpm", {}).get("all_inside_135_150"):
        raise RuntimeError("DECODED_AUDIO_WPM_GATE_FAILED")

    probe = json.loads(
        subprocess.run(
            [
                FFPROBE,
                "-v",
                "error",
                "-show_entries",
                "format=duration,size:stream=index,codec_name,codec_type,width,height,r_frame_rate,channels,sample_rate:stream_tags=language",
                "-of",
                "json",
                str(VIDEO),
            ],
            check=True,
            text=True,
            capture_output=True,
        ).stdout
    )
    streams = probe.get("streams", [])
    if not any(stream.get("codec_type") == "subtitle" and stream.get("codec_name") == "mov_text" for stream in streams):
        raise RuntimeError("LOCAL_SUBTITLE_STREAM_PRESENCE_ASSERTION_FAILED")
    if abs(float(probe["format"]["duration"]) - 402.0) > 0.01:
        raise RuntimeError("LOCAL_DURATION_MISMATCH")
    if int(probe["format"]["size"]) != VIDEO.stat().st_size:
        raise RuntimeError("LOCAL_SIZE_MISMATCH")
    return {"hashes": actual_hashes, "probe": probe, "freeze": freeze}


def exact_title_rows(inventory: list[dict]) -> list[dict]:
    return [row for row in inventory if row["title"] == TITLE]


def wait_for_processing(youtube, video_id: str, timeout: int = 1200) -> dict:
    deadline = time.time() + timeout
    last = None
    while time.time() < deadline:
        last = read_video(youtube, video_id)
        upload_status = last["status"].get("uploadStatus")
        processing_status = last.get("processingDetails", {}).get("processingStatus")
        if upload_status == "processed" and processing_status == "succeeded":
            return last
        if upload_status in {"failed", "rejected"} or processing_status in {"failed", "terminated"}:
            raise RuntimeError(f"YOUTUBE_PROCESSING_FAILED:{upload_status}:{processing_status}")
        time.sleep(8)
    raise TimeoutError("YOUTUBE_PROCESSING_TIMEOUT:" + json.dumps(last or {}))


def run_mandated_uploader(youtube, pre_inventory: list[dict]) -> str:
    before_ids = {row["video_id"] for row in exact_title_rows(pre_inventory)}
    unexpected_before = before_ids - KNOWN_SAME_TITLE_IDS
    if unexpected_before:
        raise RuntimeError("UNEXPECTED_EXACT_TITLE_COLLISION_BEFORE_UPLOAD:" + json.dumps(sorted(unexpected_before)))

    command = [
        PYTHON,
        str(UPLOADER),
        "--file",
        str(VIDEO),
        "--title",
        TITLE,
        "--description-file",
        str(DESCRIPTION),
    ]
    result = subprocess.run(command, text=True, capture_output=True)
    UPLOADER_STDOUT.write_text(result.stdout, encoding="utf-8")
    UPLOADER_STDERR.write_text(result.stderr, encoding="utf-8")

    match = re.search(r"^video id: ([A-Za-z0-9_-]+)$", result.stdout, re.MULTILINE)
    video_id = match.group(1) if match else None
    if result.returncode != 0 or not video_id:
        channel = assert_owner(youtube)
        post_inventory = inventory_uploads(
            youtube, channel["contentDetails"]["relatedPlaylists"]["uploads"]
        )
        after_ids = {row["video_id"] for row in exact_title_rows(post_inventory)}
        added = sorted(after_ids - before_ids)
        if len(added) == 1:
            video_id = added[0]
        else:
            raise RuntimeError(
                "UPLOADER_FAILED_OR_AMBIGUOUS:"
                + json.dumps(
                    {
                        "returncode": result.returncode,
                        "video_id_in_stdout": video_id,
                        "new_exact_title_ids": added,
                    }
                )
            )
    if video_id in KNOWN_SAME_TITLE_IDS:
        raise RuntimeError("UPLOADER_RETURNED_PREDECESSOR_ID:" + video_id)
    return video_id


def verify_uploaded_video(video: dict, description: str) -> None:
    status = video["status"]
    snippet = video["snippet"]
    if snippet.get("channelId") != EXPECTED_CHANNEL_ID:
        raise RuntimeError("UPLOADED_VIDEO_WRONG_CHANNEL")
    if snippet.get("title") != TITLE:
        raise RuntimeError("YOUTUBE_TITLE_READBACK_MISMATCH")
    live_description = snippet.get("description", "")
    description_exact = live_description == description
    one_terminal_lf_stripped = (
        description.endswith("\n")
        and not description.endswith("\n\n")
        and live_description == description[:-1]
        and hashlib.sha256((live_description + "\n").encode("utf-8")).hexdigest()
        == EXPECTED_HASHES[DESCRIPTION]
    )
    if not description_exact and not one_terminal_lf_stripped:
        raise RuntimeError("YOUTUBE_DESCRIPTION_READBACK_MISMATCH")
    if status.get("privacyStatus") != PRIVACY:
        raise RuntimeError("YOUTUBE_PRIVACY_NOT_UNLISTED")
    if status.get("madeForKids") is True:
        raise RuntimeError("YOUTUBE_MADE_FOR_KIDS_UNEXPECTED")
    if status.get("uploadStatus") != "processed":
        raise RuntimeError("YOUTUBE_UPLOAD_NOT_PROCESSED")
    server_duration = iso_duration_seconds(video["contentDetails"]["duration"])
    if abs(server_duration - 402.0) > 1.2:
        raise RuntimeError(f"YOUTUBE_DURATION_MISMATCH:{server_duration}:402.0")


def insert_or_reuse_caption(youtube, video_id: str) -> dict:
    existing = youtube.captions().list(part="snippet", videoId=video_id).execute().get("items", [])
    for item in existing:
        snippet = item["snippet"]
        if snippet.get("language") == "en" and snippet.get("name") == CAPTION_NAME:
            return item
    return youtube.captions().insert(
        part="snippet",
        body={
            "snippet": {
                "videoId": video_id,
                "language": "en",
                "name": CAPTION_NAME,
                "isDraft": False,
            }
        },
        media_body=MediaFileUpload(str(SRT), mimetype="application/octet-stream", resumable=False),
    ).execute()


def wait_for_caption(youtube, video_id: str, caption_id: str, timeout: int = 300) -> dict:
    deadline = time.time() + timeout
    last = None
    while time.time() < deadline:
        items = youtube.captions().list(part="snippet", videoId=video_id).execute().get("items", [])
        last = next((item for item in items if item["id"] == caption_id), None)
        if last and last["snippet"].get("status") == "serving":
            return last
        if last and last["snippet"].get("status") == "failed":
            raise RuntimeError("CAPTION_PROCESSING_FAILED:" + json.dumps(last["snippet"]))
        time.sleep(6)
    raise TimeoutError("CAPTION_PROCESSING_TIMEOUT:" + json.dumps(last or {}))


def oembed(video_id: str) -> dict:
    url = "https://www.youtube.com/oembed?" + urllib.parse.urlencode(
        {"url": f"https://www.youtube.com/watch?v={video_id}", "format": "json"}
    )
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=30) as response:
        return json.loads(response.read())


def set_private_after_replacement_ready(youtube, video_id: str) -> tuple[dict, dict]:
    before = read_video(youtube, video_id)
    if before["snippet"].get("channelId") != EXPECTED_CHANNEL_ID:
        raise RuntimeError("PREDECESSOR_WRONG_CHANNEL")
    if before["snippet"].get("title") != TITLE:
        raise RuntimeError("PREDECESSOR_TITLE_MISMATCH")
    old_status = before["status"]
    if old_status.get("privacyStatus") not in {"unlisted", "private"}:
        raise RuntimeError("PREDECESSOR_UNEXPECTED_PRIVACY:" + str(old_status.get("privacyStatus")))
    if old_status.get("privacyStatus") != "private":
        allowed = [
            "license",
            "embeddable",
            "publicStatsViewable",
            "selfDeclaredMadeForKids",
            "containsSyntheticMedia",
        ]
        new_status = {key: old_status[key] for key in allowed if key in old_status}
        new_status["privacyStatus"] = "private"
        new_status["selfDeclaredMadeForKids"] = bool(old_status.get("selfDeclaredMadeForKids", False))
        youtube.videos().update(
            part="status",
            body={"id": video_id, "status": new_status},
        ).execute()

    consecutive = 0
    deadline = time.time() + 180
    after = None
    while time.time() < deadline:
        after = read_video(youtube, video_id)
        if after["status"].get("privacyStatus") == "private":
            consecutive += 1
            if consecutive >= 3:
                return before, after
        else:
            consecutive = 0
        time.sleep(5)
    raise TimeoutError("PREDECESSOR_PRIVATE_STATE_NOT_SETTLED:" + json.dumps(after or {}))


def compact_video(video: dict) -> dict:
    status = video["status"]
    return {
        "id": video["id"],
        "channel_id": video["snippet"].get("channelId"),
        "title": video["snippet"].get("title"),
        "privacy": status.get("privacyStatus"),
        "upload_status": status.get("uploadStatus"),
        "processing_status": video.get("processingDetails", {}).get("processingStatus"),
        "duration": video.get("contentDetails", {}).get("duration"),
        "embeddable": status.get("embeddable"),
        "made_for_kids": status.get("madeForKids", False),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--execute", action="store_true")
    args = parser.parse_args()

    local = local_preflight()
    youtube, granted_scopes = load_youtube()
    channel = assert_owner(youtube)
    inventory = inventory_uploads(
        youtube, channel["contentDetails"]["relatedPlaylists"]["uploads"]
    )
    title_rows = exact_title_rows(inventory)
    unexpected = sorted({row["video_id"] for row in title_rows} - KNOWN_SAME_TITLE_IDS)

    preflight = {
        "status": "PASS_V13_PERSONAL_CHANNEL_RELEASE_PREFLIGHT",
        "checked_at_utc": now(),
        "channel_id": channel["id"],
        "channel_title": channel["snippet"]["title"],
        "granted_scopes": granted_scopes,
        "privacy_constant": PRIVACY,
        "public_visibility_code_path": False,
        "title": TITLE,
        "exact_title_inventory": title_rows,
        "unexpected_exact_title_ids": unexpected,
        "candidate_sha256": EXPECTED_HASHES[VIDEO],
        "description_sha256": EXPECTED_HASHES[DESCRIPTION],
        "caption_sha256": EXPECTED_HASHES[SRT],
        "caption_stream_present_in_candidate": True,
        "predecessor_v11_id": V11_ID,
        "retired_v7_id": RETIRED_V7_ID,
    }
    if unexpected and not CHECKPOINT.exists():
        raise RuntimeError("UNEXPECTED_EXACT_TITLE_COLLISION:" + json.dumps(unexpected))
    if not args.execute:
        print(json.dumps(preflight, indent=2, ensure_ascii=False))
        return

    description = DESCRIPTION.read_text(encoding="utf-8")
    if CHECKPOINT.exists():
        checkpoint = json.loads(CHECKPOINT.read_text(encoding="utf-8"))
        required = {
            "source_sha256": EXPECTED_HASHES[VIDEO],
            "caption_sha256": EXPECTED_HASHES[SRT],
            "description_sha256": EXPECTED_HASHES[DESCRIPTION],
            "channel_id": EXPECTED_CHANNEL_ID,
            "title": TITLE,
            "privacy_intended": PRIVACY,
        }
        if any(checkpoint.get(key) != value for key, value in required.items()):
            raise RuntimeError("CHECKPOINT_BINDING_MISMATCH")
        video_id = checkpoint["video_id"]
    else:
        video_id = run_mandated_uploader(youtube, inventory)
        checkpoint = {
            "marker": "BHU_V13_PERSONAL_CHANNEL_UNLISTED_UPLOAD_CHECKPOINT",
            "state": "INSERT_RETURNED",
            "created_at_utc": now(),
            "video_id": video_id,
            "url": f"https://youtu.be/{video_id}",
            "channel_id": EXPECTED_CHANNEL_ID,
            "channel_title": EXPECTED_CHANNEL_TITLE,
            "title": TITLE,
            "privacy_intended": PRIVACY,
            "source": str(VIDEO),
            "source_sha256": EXPECTED_HASHES[VIDEO],
            "source_bytes": VIDEO.stat().st_size,
            "caption": str(SRT),
            "caption_sha256": EXPECTED_HASHES[SRT],
            "description": str(DESCRIPTION),
            "description_sha256": EXPECTED_HASHES[DESCRIPTION],
            "mandated_uploader": str(UPLOADER),
            "mandated_uploader_sha256": sha256(UPLOADER),
        }
        atomic_json(CHECKPOINT, checkpoint)

    channel = assert_owner(youtube)
    uploaded = wait_for_processing(youtube, video_id)
    verify_uploaded_video(uploaded, description)
    checkpoint.update(
        {
            "state": "PROCESSED_UNLISTED_VERIFIED",
            "processed_at_utc": now(),
            "owner_readback": compact_video(uploaded),
        }
    )
    atomic_json(CHECKPOINT, checkpoint)

    caption = insert_or_reuse_caption(youtube, video_id)
    checkpoint.update(
        {
            "state": "CAPTION_INSERTED_OR_REUSED",
            "caption_id": caption["id"],
        }
    )
    atomic_json(CHECKPOINT, checkpoint)
    caption = wait_for_caption(youtube, video_id, caption["id"])
    checkpoint.update(
        {
            "state": "UNLISTED_PROCESSED_CAPTION_SERVING",
            "caption_status": caption["snippet"].get("status"),
            "caption_serving_at_utc": now(),
        }
    )
    atomic_json(CHECKPOINT, checkpoint)

    uploaded = read_video(youtube, video_id)
    verify_uploaded_video(uploaded, description)
    external = oembed(video_id)
    if external.get("title") != TITLE or external.get("author_name") != EXPECTED_CHANNEL_TITLE:
        raise RuntimeError("OEMBED_TITLE_OR_CHANNEL_MISMATCH:" + json.dumps(external))

    v11_before, v11_after = set_private_after_replacement_ready(youtube, V11_ID)
    v7 = read_video(youtube, RETIRED_V7_ID)
    if v7["snippet"].get("channelId") != EXPECTED_CHANNEL_ID:
        raise RuntimeError("RETIRED_V7_WRONG_CHANNEL")
    if v7["status"].get("privacyStatus") != "private":
        raise RuntimeError("RETIRED_V7_NOT_PRIVATE")

    completed = now()
    receipt = {
        "marker": "BHU_V13_UNLISTED_PERSONAL_CHANNEL_RELEASE_COMPLETE",
        "completed_at_utc": completed,
        "authorization": {
            "user_direction": "use the personal channel, it's unlisted anyway.",
            "public_visibility_authorized": False,
            "upload_channel_id": EXPECTED_CHANNEL_ID,
            "upload_channel_title": EXPECTED_CHANNEL_TITLE,
            "identity_check_preserved": True,
            "identity_check_change": "expected channel changed from NebulaMind to the explicitly authorized personal channel",
            "earlier_bhu_channel_custody": "V11 and retired V7 were already uploaded to this same personal channel; this is now explicit authorization rather than an unrecorded assumption.",
        },
        "candidate": {
            "path": str(VIDEO),
            "sha256": EXPECTED_HASHES[VIDEO],
            "bytes": VIDEO.stat().st_size,
            "duration_seconds": 402.0,
            "resolution": "1920x1080",
            "streams": ["h264 video", "aac mono audio", "mov_text eng default subtitle"],
        },
        "metadata": {
            "title": TITLE,
            "description_path": str(DESCRIPTION),
            "description_sha256": EXPECTED_HASHES[DESCRIPTION],
            "description_bytes": DESCRIPTION.stat().st_size,
            "description_recovery": {
                "historical_expected_sha256": EXPECTED_HASHES[DESCRIPTION],
                "source_video_id": V11_ID,
                "source_video_channel_id": EXPECTED_CHANNEL_ID,
                "accepted_reversible_transform": "NFKD, LF, exactly one trailing LF, no BOM",
                "exact_digest_match": True,
            },
            "youtube_readback_boundary": {
                "live_description_equals_gated_file_without_one_terminal_lf": True,
                "terminal_lf_reappended_sha256": EXPECTED_HASHES[DESCRIPTION],
                "copy_changed": False,
            },
        },
        "local_gates": {
            "freeze": str(FREEZE),
            "freeze_sha256": EXPECTED_HASHES[FREEZE],
            "pre_render_three_seat_gate": "PASS exact V13 hashes",
            "encoded_qa": "45/45 PASS",
            "encoded_qa_path": str(ENCODED_QA),
            "encoded_qa_sha256": EXPECTED_HASHES[ENCODED_QA],
            "decoded_visual_preflight": str(VISUAL_PREFLIGHT),
            "decoded_visual_preflight_sha256": EXPECTED_HASHES[VISUAL_PREFLIGHT],
            "decoded_audio_wpm_range": [142.03730272596843, 142.4083769633508],
            "embedded_subtitle_stream_presence_asserted": True,
        },
        "youtube": {
            "video_id": video_id,
            "url": f"https://youtu.be/{video_id}",
            "channel_id": channel["id"],
            "channel_title": channel["snippet"]["title"],
            "privacy": uploaded["status"].get("privacyStatus"),
            "upload_status": uploaded["status"].get("uploadStatus"),
            "processing_status": uploaded.get("processingDetails", {}).get("processingStatus"),
            "duration": uploaded["contentDetails"].get("duration"),
            "embeddable": uploaded["status"].get("embeddable"),
            "made_for_kids": uploaded["status"].get("madeForKids", False),
            "oembed_title": external.get("title"),
            "oembed_author": external.get("author_name"),
        },
        "captions": {
            "source": str(SRT),
            "source_sha256": EXPECTED_HASHES[SRT],
            "source_vtt": str(VTT),
            "source_vtt_sha256": EXPECTED_HASHES[VTT],
            "caption_id": caption["id"],
            "language": caption["snippet"].get("language"),
            "name": caption["snippet"].get("name"),
            "status": caption["snippet"].get("status"),
        },
        "predecessor_v11": {
            "id": V11_ID,
            "channel_id": v11_after["snippet"].get("channelId"),
            "channel_title": EXPECTED_CHANNEL_TITLE,
            "privacy_before": v11_before["status"].get("privacyStatus"),
            "privacy_after": v11_after["status"].get("privacyStatus"),
            "retired_after_v13_caption_serving": True,
            "deleted": False,
        },
        "retired_v7": {
            "id": RETIRED_V7_ID,
            "channel_id": v7["snippet"].get("channelId"),
            "channel_title": EXPECTED_CHANNEL_TITLE,
            "privacy": v7["status"].get("privacyStatus"),
            "deleted": False,
        },
        "downstream": {
            "registry_update_pending": True,
            "cockpit_viewer_repoint_pending": True,
            "public_visibility_authorized": False,
            "git_mutation_performed": False,
        },
        "checkpoint": str(CHECKPOINT),
        "mandated_uploader": str(UPLOADER),
        "mandated_uploader_sha256": sha256(UPLOADER),
    }
    atomic_json(RECEIPT, receipt)
    checkpoint.update(
        {
            "state": "RELEASE_COMPLETE_V11_PRIVATE",
            "completed_at_utc": completed,
            "release_receipt": str(RECEIPT),
        }
    )
    atomic_json(CHECKPOINT, checkpoint)
    print(
        json.dumps(
            {
                "status": receipt["marker"],
                "video_id": video_id,
                "url": receipt["youtube"]["url"],
                "channel_id": receipt["youtube"]["channel_id"],
                "channel_title": receipt["youtube"]["channel_title"],
                "privacy": receipt["youtube"]["privacy"],
                "caption_status": receipt["captions"]["status"],
                "v11_privacy": receipt["predecessor_v11"]["privacy_after"],
                "receipt": str(RECEIPT),
            },
            ensure_ascii=False,
        )
    )


if __name__ == "__main__":
    main()
