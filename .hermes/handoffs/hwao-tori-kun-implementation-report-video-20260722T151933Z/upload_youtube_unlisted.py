#!/usr/bin/env python3
"""Idempotently upload the QA-locked implementation report as an unlisted YouTube review video."""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import argparse
import hashlib
import json
import os
import subprocess
import time
import urllib.parse
import urllib.request

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload

BASE = Path(__file__).resolve().parent
SOURCE = BASE / "HWAO_TORI_KUN_IMPLEMENTATION_REPORT_V2.mp4"
CAPTION = BASE / "HWAO_TORI_KUN_IMPLEMENTATION_REPORT_V2.srt"
BUILD_RECEIPT = BASE / "build_receipt.json"
QA_RECEIPT = BASE / "qa_receipt.json"
FINAL_RECEIPT = BASE / "FINAL_RECEIPT.md"
METADATA_PATH = BASE / "youtube_metadata.json"
CHECKPOINT = BASE / "youtube_unlisted_checkpoint.json"
PREFLIGHT_RECEIPT = BASE / "youtube_unlisted_preflight.json"
UPLOAD_RECEIPT = BASE / "youtube_unlisted_upload_receipt.json"
TOKEN = Path("/Users/duhokim/HermesOps/scripts/token_manage.json")
CHANNEL_ID = "UCUHBNGk8ozEnisQRuchoS4Q"
CHANNEL_NAME = "NebulaMind"
RETRIABLE = {500, 502, 503, 504}


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def write_json(path: Path, value: dict) -> None:
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    os.replace(tmp, path)


def service():
    if not TOKEN.is_file():
        raise RuntimeError("YouTube manage credential is missing")
    creds = Credentials.from_authorized_user_file(str(TOKEN))
    if not creds.valid:
        if creds.expired and creds.refresh_token:
            creds.refresh(Request())
            TOKEN.write_text(creds.to_json(), encoding="utf-8")
            os.chmod(TOKEN, 0o600)
        else:
            raise RuntimeError("YouTube manage credential is invalid and cannot refresh")
    scopes = set(creds.scopes or [])
    has_upload = any(scope.endswith("/youtube.upload") for scope in scopes)
    has_manage = any(scope.endswith("/youtube.force-ssl") for scope in scopes)
    if not has_upload or not has_manage:
        raise RuntimeError("manage token lacks youtube.upload or youtube.force-ssl scope")
    return build("youtube", "v3", credentials=creds, cache_discovery=False)


def channel_identity(youtube) -> tuple[str, str, str]:
    rows = youtube.channels().list(part="snippet,contentDetails", mine=True).execute().get("items", [])
    if len(rows) != 1:
        raise RuntimeError(f"expected exactly one authenticated channel, found {len(rows)}")
    row = rows[0]
    if row["id"] != CHANNEL_ID or row["snippet"]["title"] != CHANNEL_NAME:
        raise RuntimeError(f"authenticated channel mismatch: {row['id']} / {row['snippet']['title']}")
    return row["id"], row["snippet"]["title"], row["contentDetails"]["relatedPlaylists"]["uploads"]


def inventory_by_title(youtube, uploads: str, title: str, max_items: int = 500) -> list[dict]:
    token = None
    ids: list[str] = []
    while len(ids) < max_items:
        page = youtube.playlistItems().list(
            part="contentDetails", playlistId=uploads, maxResults=50, pageToken=token
        ).execute()
        ids.extend(row["contentDetails"]["videoId"] for row in page.get("items", []))
        token = page.get("nextPageToken")
        if not token:
            break
    matches: list[dict] = []
    for offset in range(0, len(ids), 50):
        rows = youtube.videos().list(
            part="snippet,status,processingDetails", id=",".join(ids[offset : offset + 50])
        ).execute().get("items", [])
        for row in rows:
            if row["snippet"]["title"] == title:
                matches.append(
                    {
                        "id": row["id"],
                        "title": title,
                        "privacy": row["status"]["privacyStatus"],
                        "upload_status": row["status"].get("uploadStatus"),
                        "processing": row.get("processingDetails", {}).get("processingStatus"),
                    }
                )
    return matches


def video_state(youtube, video_id: str) -> dict:
    rows = youtube.videos().list(
        part="snippet,status,processingDetails,contentDetails", id=video_id
    ).execute().get("items", [])
    if len(rows) != 1:
        raise RuntimeError(f"video not found: {video_id}")
    row = rows[0]
    status = row["status"]
    processing = row.get("processingDetails", {})
    return {
        "id": video_id,
        "title": row["snippet"]["title"],
        "description": row["snippet"].get("description", ""),
        "channel_id": row["snippet"].get("channelId"),
        "privacy": status["privacyStatus"],
        "upload_status": status.get("uploadStatus"),
        "embeddable": status.get("embeddable"),
        "made_for_kids": status.get("madeForKids"),
        "self_declared_made_for_kids": status.get("selfDeclaredMadeForKids"),
        "processing": processing.get("processingStatus"),
        "processing_failure_reason": processing.get("processingFailureReason"),
        "duration": row.get("contentDetails", {}).get("duration"),
    }


def caption_rows(youtube, video_id: str) -> list[dict]:
    return youtube.captions().list(part="snippet", videoId=video_id).execute().get("items", [])


def verify_local_lock(metadata: dict) -> dict:
    build_receipt = json.loads(BUILD_RECEIPT.read_text(encoding="utf-8"))
    qa_receipt = json.loads(QA_RECEIPT.read_text(encoding="utf-8"))
    final_text = FINAL_RECEIPT.read_text(encoding="utf-8")
    if build_receipt.get("marker") != "HWAO_TORI_KUN_IMPLEMENTATION_REPORT_VIDEO_BUILD_COMPLETE_V2":
        raise RuntimeError("build receipt marker mismatch")
    if qa_receipt.get("marker") != "HWAO_TORI_KUN_IMPLEMENTATION_REPORT_VIDEO_QA_PASS_V2" or qa_receipt.get("status") != "PASS":
        raise RuntimeError("QA receipt is not PASS")
    if "HWAO_TORI_KUN_IMPLEMENTATION_REPORT_VIDEO_FINAL_PASS_V2" not in final_text:
        raise RuntimeError("final receipt marker missing")
    source_hash = sha256(SOURCE)
    caption_hash = sha256(CAPTION)
    if source_hash != build_receipt["artifact_sha256"] or source_hash != qa_receipt["media"]["sha256"]:
        raise RuntimeError("video hash drift")
    if caption_hash != build_receipt["srt_sha256"] or caption_hash != qa_receipt["captions"]["sha256"]:
        raise RuntimeError("caption hash drift")
    if SOURCE.stat().st_size != qa_receipt["media"]["bytes"]:
        raise RuntimeError("video byte-count drift")
    if metadata.get("privacy") != "unlisted":
        raise RuntimeError("metadata privacy must remain unlisted")
    if metadata.get("made_for_kids") is not False or metadata.get("embeddable") is not True:
        raise RuntimeError("unsafe metadata status contract")
    if len(metadata["title"]) > 100 or len(metadata["description"]) > 5000:
        raise RuntimeError("YouTube title or description exceeds platform limit")
    duration = subprocess.check_output(
        ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "default=nk=1:nw=1", str(SOURCE)],
        text=True,
    ).strip()
    if abs(float(duration) - 100.0) > 0.01:
        raise RuntimeError(f"unexpected source duration: {duration}")
    return {
        "source_sha256": source_hash,
        "source_bytes": SOURCE.stat().st_size,
        "caption_sha256": caption_hash,
        "metadata_sha256": sha256(METADATA_PATH),
        "duration_seconds": float(duration),
    }


def load_or_initialize_checkpoint(local: dict, metadata: dict) -> dict:
    expected = {
        "marker": "HWAO_TORI_KUN_IMPLEMENTATION_REPORT_YOUTUBE_CHECKPOINT_V1",
        "source": str(SOURCE),
        "source_sha256": local["source_sha256"],
        "source_bytes": local["source_bytes"],
        "caption": str(CAPTION),
        "caption_sha256": local["caption_sha256"],
        "metadata": str(METADATA_PATH),
        "metadata_sha256": local["metadata_sha256"],
        "title": metadata["title"],
        "privacy": "unlisted",
        "video_id": "",
        "caption_id": "",
        "status": "LOCAL_LOCKED_READY",
        "created_at": now(),
    }
    if not CHECKPOINT.exists():
        write_json(CHECKPOINT, expected)
        return expected
    checkpoint = json.loads(CHECKPOINT.read_text(encoding="utf-8"))
    for key in ("marker", "source_sha256", "source_bytes", "caption_sha256", "metadata_sha256", "title", "privacy"):
        if checkpoint.get(key) != expected[key]:
            raise RuntimeError(f"checkpoint local identity mismatch: {key}")
    return checkpoint


def upload_once(youtube, metadata: dict) -> str:
    request = youtube.videos().insert(
        part="snippet,status",
        notifySubscribers=False,
        body={
            "snippet": {
                "title": metadata["title"],
                "description": metadata["description"],
                "categoryId": metadata["category_id"],
                "defaultLanguage": metadata["default_language"],
                "defaultAudioLanguage": metadata["default_audio_language"],
                "tags": metadata["tags"],
            },
            "status": {
                "privacyStatus": "unlisted",
                "selfDeclaredMadeForKids": False,
                "embeddable": True,
            },
        },
        media_body=MediaFileUpload(str(SOURCE), chunksize=8 * 1024 * 1024, resumable=True),
    )
    response = None
    failures = 0
    while response is None:
        try:
            status, response = request.next_chunk()
            if status:
                print(f"upload_progress={int(status.progress() * 100)}%", flush=True)
        except HttpError as exc:
            if exc.resp.status not in RETRIABLE or failures >= 5:
                raise
            time.sleep(2**failures)
            failures += 1
    return response["id"]


def wait_processing(youtube, video_id: str, timeout: int = 1200) -> dict:
    deadline = time.time() + timeout
    while time.time() < deadline:
        state = video_state(youtube, video_id)
        if state["processing"] == "succeeded" and state["upload_status"] == "processed":
            return state
        if state["processing"] in {"failed", "terminated"} or state["upload_status"] in {"failed", "rejected", "deleted"}:
            raise RuntimeError(f"YouTube processing failed: {state}")
        time.sleep(10)
    raise TimeoutError(f"processing timeout for {video_id}")


def ensure_manual_caption(youtube, video_id: str, metadata: dict, checkpoint: dict) -> tuple[str, str]:
    name = metadata["caption_name"]
    rows = caption_rows(youtube, video_id)
    matches = [
        row
        for row in rows
        if row["snippet"].get("language") == "en" and row["snippet"].get("name") == name
    ]
    if len(matches) > 1:
        raise RuntimeError(f"duplicate manual caption tracks: {[row['id'] for row in matches]}")
    if matches:
        row = matches[0]
    else:
        row = youtube.captions().insert(
            part="snippet",
            body={
                "snippet": {
                    "videoId": video_id,
                    "language": "en",
                    "name": name,
                    "isDraft": False,
                }
            },
            media_body=MediaFileUpload(str(CAPTION), mimetype="application/x-subrip", resumable=False),
        ).execute()
        checkpoint.update(
            {
                "caption_id": row["id"],
                "caption_inserted_at": now(),
                "status": "UNLISTED_PROCESSING_SUCCEEDED_CAPTION_INSERTED",
            }
        )
        write_json(CHECKPOINT, checkpoint)
    caption_id = row["id"]
    if checkpoint.get("caption_id") and checkpoint["caption_id"] != caption_id:
        raise RuntimeError("checkpoint caption ID conflicts with server caption")
    deadline = time.time() + 300
    while time.time() < deadline:
        refreshed = [item for item in caption_rows(youtube, video_id) if item["id"] == caption_id]
        if refreshed:
            status = refreshed[0]["snippet"].get("status")
            if status == "serving":
                return caption_id, status
            if status == "failed":
                raise RuntimeError(f"caption failed: {caption_id}")
        time.sleep(5)
    raise TimeoutError(f"caption serving timeout: {caption_id}")


def oembed(video_id: str) -> dict:
    url = "https://www.youtube.com/oembed?" + urllib.parse.urlencode(
        {"url": f"https://www.youtube.com/watch?v={video_id}", "format": "json"}
    )
    with urllib.request.urlopen(url, timeout=30) as response:
        payload = json.load(response)
    return {
        "title": payload.get("title"),
        "author_name": payload.get("author_name"),
        "author_url": payload.get("author_url"),
        "provider_name": payload.get("provider_name"),
    }


def verify_server_state(state: dict, metadata: dict) -> None:
    if state["title"] != metadata["title"] or state["description"] != metadata["description"]:
        raise RuntimeError("server title or description mismatch")
    if state["channel_id"] != CHANNEL_ID:
        raise RuntimeError("server channel mismatch")
    if state["privacy"] != "unlisted" or state["embeddable"] is not True:
        raise RuntimeError(f"unsafe server privacy or embed state: {state}")
    if state["self_declared_made_for_kids"] is not False:
        raise RuntimeError(f"made-for-kids declaration mismatch: {state}")
    # YouTube can round a 100.000-second MP4 with AAC padding up to PT1M41S.
    if state["duration"] not in {"PT1M40S", "PT1M41S"}:
        raise RuntimeError(f"server duration mismatch: {state['duration']}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--execute-unlisted", action="store_true")
    args = parser.parse_args()

    metadata = json.loads(METADATA_PATH.read_text(encoding="utf-8"))
    local = verify_local_lock(metadata)
    checkpoint = load_or_initialize_checkpoint(local, metadata)
    youtube = service()
    channel_id, channel_name, uploads = channel_identity(youtube)
    matches = inventory_by_title(youtube, uploads, metadata["title"])
    video_id = checkpoint.get("video_id", "")

    if video_id:
        if matches and video_id not in [row["id"] for row in matches]:
            raise RuntimeError("checkpoint video ID conflicts with exact-title inventory")
        state = video_state(youtube, video_id)
    else:
        if matches:
            raise RuntimeError(f"exact-title collision; refusing upload: {matches}")
        if not args.execute_unlisted:
            receipt = {
                "marker": "HWAO_TORI_KUN_IMPLEMENTATION_REPORT_YOUTUBE_PREFLIGHT_PASS_V1",
                "completed_at_utc": now(),
                "channel_id": channel_id,
                "channel_name": channel_name,
                "title": metadata["title"],
                "privacy": "unlisted",
                "source_sha256": local["source_sha256"],
                "caption_sha256": local["caption_sha256"],
                "exact_title_matches": [],
                "status": "READY_NO_DUPLICATE",
                "mutation_performed": False,
            }
            write_json(PREFLIGHT_RECEIPT, receipt)
            print(json.dumps(receipt, indent=2, ensure_ascii=False))
            return
        try:
            print("uploading_once_as_unlisted=true", flush=True)
            video_id = upload_once(youtube, metadata)
        except Exception:
            ambiguous = inventory_by_title(youtube, uploads, metadata["title"])
            checkpoint.update(
                {
                    "status": "UPLOAD_AMBIGUOUS_STOPPED",
                    "ambiguous_candidates": ambiguous,
                    "last_checked_at": now(),
                }
            )
            write_json(CHECKPOINT, checkpoint)
            raise
        checkpoint.update(
            {
                "video_id": video_id,
                "url": f"https://youtu.be/{video_id}",
                "privacy": "unlisted",
                "processing": "uploaded_processing",
                "status": "UNLISTED_PROCESSING",
                "uploaded_at": now(),
            }
        )
        write_json(CHECKPOINT, checkpoint)
        state = video_state(youtube, video_id)

    if not args.execute_unlisted:
        receipt = {
            "marker": "HWAO_TORI_KUN_IMPLEMENTATION_REPORT_YOUTUBE_PREFLIGHT_CHECKPOINT_V1",
            "completed_at_utc": now(),
            "channel_id": channel_id,
            "channel_name": channel_name,
            "video_id": video_id,
            "state": state,
            "mutation_performed": False,
        }
        write_json(PREFLIGHT_RECEIPT, receipt)
        print(json.dumps(receipt, indent=2, ensure_ascii=False))
        return

    state = wait_processing(youtube, video_id)
    verify_server_state(state, metadata)
    caption_id, caption_status = ensure_manual_caption(youtube, video_id, metadata, checkpoint)
    external = oembed(video_id)
    if external["title"] != metadata["title"] or external["author_name"] != CHANNEL_NAME:
        raise RuntimeError(f"oEmbed mismatch: {external}")
    checkpoint.update(
        {
            "caption_id": caption_id,
            "caption_status": caption_status,
            "privacy": "unlisted",
            "processing": state["processing"],
            "upload_status": state["upload_status"],
            "duration": state["duration"],
            "embeddable": state["embeddable"],
            "status": "UNLISTED_PROCESSING_SUCCEEDED_MANUAL_CAPTIONS_SERVING",
            "verified_at": now(),
            "server_state": state,
            "oembed": external,
        }
    )
    write_json(CHECKPOINT, checkpoint)
    receipt = {
        "marker": "HWAO_TORI_KUN_IMPLEMENTATION_REPORT_YOUTUBE_UNLISTED_UPLOAD_COMPLETE_V1",
        "completed_at_utc": now(),
        "channel_id": channel_id,
        "channel_name": channel_name,
        "video_id": video_id,
        "url": f"https://youtu.be/{video_id}",
        "title": metadata["title"],
        "privacy": "unlisted",
        "processing": state["processing"],
        "upload_status": state["upload_status"],
        "duration": state["duration"],
        "embeddable": state["embeddable"],
        "made_for_kids": state["made_for_kids"],
        "self_declared_made_for_kids": state["self_declared_made_for_kids"],
        "caption_id": caption_id,
        "caption_status": caption_status,
        "source_sha256": local["source_sha256"],
        "source_bytes": local["source_bytes"],
        "caption_sha256": local["caption_sha256"],
        "oembed": external,
        "public_visibility_changed": False,
        "website_or_cockpit_changed": False,
        "git_changed": False,
        "runtime_deployed": False,
        "deletion_performed": False,
    }
    write_json(UPLOAD_RECEIPT, receipt)
    print(json.dumps(receipt, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
