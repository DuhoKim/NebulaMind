#!/usr/bin/env python3
"""Idempotently publish the checkpointed implementation-report YouTube ID."""
from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
import argparse
import hashlib
import json
import os
import time
import urllib.parse
import urllib.request

from google.oauth2.credentials import Credentials
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

BASE = Path(__file__).resolve().parent
SOURCE = BASE / "HWAO_TORI_KUN_IMPLEMENTATION_REPORT_V2.mp4"
CAPTION = BASE / "HWAO_TORI_KUN_IMPLEMENTATION_REPORT_V2.srt"
QA_RECEIPT = BASE / "qa_receipt.json"
UPLOAD_RECEIPT = BASE / "youtube_unlisted_upload_receipt.json"
UNLISTED_CHECKPOINT = BASE / "youtube_unlisted_checkpoint.json"
PUBLIC_METADATA = BASE / "youtube_public_metadata.json"
PUBLIC_CHECKPOINT = BASE / "youtube_publication_checkpoint.json"
PUBLIC_PREFLIGHT = BASE / "youtube_publication_preflight.json"
PUBLIC_RECEIPT = BASE / "youtube_publication_receipt.json"
TOKEN = Path("/Users/duhokim/HermesOps/scripts/token_manage.json")
CHANNEL_ID = "UCUHBNGk8ozEnisQRuchoS4Q"
CHANNEL_NAME = "NebulaMind"
VIDEO_ID = "jn1Bn3_CxfY"


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
    creds = Credentials.from_authorized_user_file(str(TOKEN))
    if not creds.valid:
        if creds.expired and creds.refresh_token:
            creds.refresh(Request())
            TOKEN.write_text(creds.to_json(), encoding="utf-8")
            os.chmod(TOKEN, 0o600)
        else:
            raise RuntimeError("YouTube manage credential is invalid and cannot refresh")
    scopes = set(creds.scopes or [])
    if not any(scope.endswith("/youtube.force-ssl") for scope in scopes):
        raise RuntimeError("manage token lacks youtube.force-ssl scope")
    return build("youtube", "v3", credentials=creds, cache_discovery=False)


def channel_identity(youtube) -> tuple[dict, str]:
    rows = youtube.channels().list(part="snippet,contentDetails", mine=True).execute().get("items", [])
    if len(rows) != 1:
        raise RuntimeError(f"expected one authenticated channel, found {len(rows)}")
    row = rows[0]
    if row["id"] != CHANNEL_ID or row["snippet"]["title"] != CHANNEL_NAME:
        raise RuntimeError("authenticated channel mismatch")
    return row, row["contentDetails"]["relatedPlaylists"]["uploads"]


def video_row(youtube) -> dict:
    rows = youtube.videos().list(
        part="snippet,status,processingDetails,contentDetails", id=VIDEO_ID
    ).execute().get("items", [])
    if len(rows) != 1:
        raise RuntimeError(f"video not found: {VIDEO_ID}")
    return rows[0]


def safe_state(row: dict) -> dict:
    status = row["status"]
    return {
        "id": row["id"],
        "title": row["snippet"]["title"],
        "description": row["snippet"].get("description", ""),
        "channel_id": row["snippet"].get("channelId"),
        "category_id": row["snippet"].get("categoryId"),
        "privacy": status.get("privacyStatus"),
        "upload_status": status.get("uploadStatus"),
        "processing": row.get("processingDetails", {}).get("processingStatus"),
        "embeddable": status.get("embeddable"),
        "made_for_kids": status.get("madeForKids"),
        "self_declared_made_for_kids": status.get("selfDeclaredMadeForKids"),
        "license": status.get("license"),
        "public_stats_viewable": status.get("publicStatsViewable"),
        "duration": row.get("contentDetails", {}).get("duration"),
    }


def manual_captions(youtube, metadata: dict) -> list[dict]:
    rows = youtube.captions().list(part="snippet", videoId=VIDEO_ID).execute().get("items", [])
    return [
        {
            "id": row["id"],
            "language": row["snippet"].get("language"),
            "name": row["snippet"].get("name"),
            "status": row["snippet"].get("status"),
            "track_kind": row["snippet"].get("trackKind"),
        }
        for row in rows
        if row["snippet"].get("language") == "en"
        and row["snippet"].get("name") == metadata["caption_name"]
    ]


def exact_title_matches(youtube, uploads: str, title: str) -> list[str]:
    token = None
    ids: list[str] = []
    while True:
        page = youtube.playlistItems().list(
            part="contentDetails", playlistId=uploads, maxResults=50, pageToken=token
        ).execute()
        ids.extend(row["contentDetails"]["videoId"] for row in page.get("items", []))
        token = page.get("nextPageToken")
        if not token:
            break
    matches: list[str] = []
    for offset in range(0, len(ids), 50):
        rows = youtube.videos().list(
            part="snippet", id=",".join(ids[offset : offset + 50])
        ).execute().get("items", [])
        matches.extend(row["id"] for row in rows if row["snippet"]["title"] == title)
    return matches


def verify_local_and_remote_preconditions(youtube, uploads: str, metadata: dict) -> tuple[dict, dict, list[dict]]:
    qa = json.loads(QA_RECEIPT.read_text(encoding="utf-8"))
    uploaded = json.loads(UPLOAD_RECEIPT.read_text(encoding="utf-8"))
    unlisted = json.loads(UNLISTED_CHECKPOINT.read_text(encoding="utf-8"))
    if qa.get("marker") != "HWAO_TORI_KUN_IMPLEMENTATION_REPORT_VIDEO_QA_PASS_V2" or qa.get("status") != "PASS":
        raise RuntimeError("local QA is not PASS")
    if uploaded.get("marker") != "HWAO_TORI_KUN_IMPLEMENTATION_REPORT_YOUTUBE_UNLISTED_UPLOAD_COMPLETE_V1":
        raise RuntimeError("unlisted upload receipt marker mismatch")
    if uploaded.get("video_id") != VIDEO_ID or unlisted.get("video_id") != VIDEO_ID:
        raise RuntimeError("checkpointed video ID mismatch")
    source_hash = sha256(SOURCE)
    caption_hash = sha256(CAPTION)
    if source_hash != qa["media"]["sha256"] or source_hash != uploaded["source_sha256"]:
        raise RuntimeError("source hash drift")
    if caption_hash != qa["captions"]["sha256"] or caption_hash != uploaded["caption_sha256"]:
        raise RuntimeError("caption hash drift")
    if metadata["privacy"] != "public" or metadata["made_for_kids"] is not False or metadata["embeddable"] is not True:
        raise RuntimeError("unsafe public metadata contract")
    if len(metadata["title"]) > 100 or len(metadata["description"]) > 5000:
        raise RuntimeError("YouTube metadata exceeds limits")
    stale_phrases = ("unlisted review", "will not appear on the channel", "unless separately made public")
    if any(phrase in metadata["description"].lower() for phrase in stale_phrases):
        raise RuntimeError("public description contains stale unlisted wording")
    row = video_row(youtube)
    state = safe_state(row)
    if state["id"] != VIDEO_ID or state["channel_id"] != CHANNEL_ID:
        raise RuntimeError("owner-state video identity mismatch")
    if state["privacy"] not in {"unlisted", "public"}:
        raise RuntimeError(f"unsafe current privacy: {state['privacy']}")
    if state["processing"] != "succeeded" or state["upload_status"] != "processed" or state["embeddable"] is not True:
        raise RuntimeError(f"video not publication-ready: {state}")
    captions = manual_captions(youtube, metadata)
    if len(captions) != 1 or captions[0]["status"] != "serving":
        raise RuntimeError(f"manual caption gate failed: {captions}")
    matches = exact_title_matches(youtube, uploads, metadata["title"])
    if matches != [VIDEO_ID]:
        raise RuntimeError(f"exact-title inventory mismatch: {matches}")
    local = {
        "source_sha256": source_hash,
        "source_bytes": SOURCE.stat().st_size,
        "caption_sha256": caption_hash,
        "metadata_sha256": sha256(PUBLIC_METADATA),
    }
    return local, state, captions


def load_or_initialize_checkpoint(local: dict, metadata: dict, state: dict, captions: list[dict]) -> dict:
    expected = {
        "marker": "HWAO_TORI_KUN_IMPLEMENTATION_REPORT_YOUTUBE_PUBLICATION_CHECKPOINT_V1",
        "video_id": VIDEO_ID,
        "url": f"https://youtu.be/{VIDEO_ID}",
        "title": metadata["title"],
        "source_sha256": local["source_sha256"],
        "source_bytes": local["source_bytes"],
        "caption_sha256": local["caption_sha256"],
        "caption_id": captions[0]["id"],
        "metadata_sha256": local["metadata_sha256"],
        "privacy": state["privacy"],
        "status": "PUBLICATION_PREFLIGHT_READY" if state["privacy"] == "unlisted" else "PUBLIC_RECONCILE_READY",
        "created_at": now(),
    }
    if not PUBLIC_CHECKPOINT.exists():
        write_json(PUBLIC_CHECKPOINT, expected)
        return expected
    checkpoint = json.loads(PUBLIC_CHECKPOINT.read_text(encoding="utf-8"))
    for key in ("marker", "video_id", "title", "source_sha256", "source_bytes", "caption_sha256", "caption_id", "metadata_sha256"):
        if checkpoint.get(key) != expected[key]:
            raise RuntimeError(f"publication checkpoint identity mismatch: {key}")
    return checkpoint


def publish_once(youtube, row: dict, metadata: dict, checkpoint: dict) -> bool:
    state = safe_state(row)
    snippet_matches = state["title"] == metadata["title"] and state["description"] == metadata["description"]
    if state["privacy"] == "public" and snippet_matches:
        return False
    if state["privacy"] not in {"unlisted", "public"}:
        raise RuntimeError(f"refusing publication from privacy {state['privacy']}")
    status = row["status"]
    body = {
        "id": VIDEO_ID,
        "snippet": {
            "title": metadata["title"],
            "description": metadata["description"],
            "categoryId": metadata["category_id"],
            "defaultLanguage": metadata["default_language"],
            "defaultAudioLanguage": metadata["default_audio_language"],
            "tags": metadata["tags"],
        },
        "status": {
            "privacyStatus": "public",
            "license": status.get("license", "youtube"),
            "embeddable": bool(status.get("embeddable", True)),
            "publicStatsViewable": bool(status.get("publicStatsViewable", True)),
            "selfDeclaredMadeForKids": bool(status.get("selfDeclaredMadeForKids", False)),
        },
    }
    youtube.videos().update(part="snippet,status", body=body).execute()
    checkpoint.update(
        {
            "mutation_accepted_at": now(),
            "mutation": "exact-ID snippet/status update to public",
            "status": "PUBLICATION_MUTATION_ACCEPTED_AWAITING_SETTLEMENT",
        }
    )
    write_json(PUBLIC_CHECKPOINT, checkpoint)
    return True


def settle_public(youtube, metadata: dict, timeout: int = 180) -> tuple[dict, list[dict]]:
    deadline = time.time() + timeout
    consecutive = 0
    observations: list[dict] = []
    while time.time() < deadline:
        state = safe_state(video_row(youtube))
        expected = (
            state["privacy"] == "public"
            and state["title"] == metadata["title"]
            and state["description"] == metadata["description"]
            and state["processing"] == "succeeded"
            and state["upload_status"] == "processed"
            and state["embeddable"] is True
            and state["self_declared_made_for_kids"] is False
        )
        observations.append(
            {
                "observed_at": now(),
                "privacy": state["privacy"],
                "metadata_match": state["title"] == metadata["title"] and state["description"] == metadata["description"],
                "processing": state["processing"],
                "upload_status": state["upload_status"],
                "expected": expected,
            }
        )
        consecutive = consecutive + 1 if expected else 0
        if consecutive >= 6:
            return state, observations
        time.sleep(6)
    raise TimeoutError(f"public settlement did not converge: {observations[-10:]}")


def oembed() -> dict:
    url = "https://www.youtube.com/oembed?" + urllib.parse.urlencode(
        {"url": f"https://www.youtube.com/watch?v={VIDEO_ID}", "format": "json"}
    )
    with urllib.request.urlopen(url, timeout=30) as response:
        payload = json.load(response)
    return {
        "title": payload.get("title"),
        "author_name": payload.get("author_name"),
        "author_url": payload.get("author_url"),
        "provider_name": payload.get("provider_name"),
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--execute-public", action="store_true")
    args = parser.parse_args()

    metadata = json.loads(PUBLIC_METADATA.read_text(encoding="utf-8"))
    youtube = service()
    channel, uploads = channel_identity(youtube)
    local, initial_state, captions = verify_local_and_remote_preconditions(youtube, uploads, metadata)
    checkpoint = load_or_initialize_checkpoint(local, metadata, initial_state, captions)

    if not args.execute_public:
        receipt = {
            "marker": "HWAO_TORI_KUN_IMPLEMENTATION_REPORT_YOUTUBE_PUBLICATION_PREFLIGHT_PASS_V1",
            "completed_at_utc": now(),
            "channel_id": channel["id"],
            "channel_name": channel["snippet"]["title"],
            "video_id": VIDEO_ID,
            "current_privacy": initial_state["privacy"],
            "processing": initial_state["processing"],
            "upload_status": initial_state["upload_status"],
            "embeddable": initial_state["embeddable"],
            "manual_caption": captions[0],
            "source_sha256": local["source_sha256"],
            "caption_sha256": local["caption_sha256"],
            "public_metadata_sha256": local["metadata_sha256"],
            "status": "READY_FOR_EXACT_ID_PUBLICATION",
            "mutation_performed": False,
        }
        write_json(PUBLIC_PREFLIGHT, receipt)
        print(json.dumps(receipt, indent=2, ensure_ascii=False))
        return

    row = video_row(youtube)
    mutation_performed = publish_once(youtube, row, metadata, checkpoint)
    final_state, observations = settle_public(youtube, metadata)
    final_captions = manual_captions(youtube, metadata)
    if len(final_captions) != 1 or final_captions[0]["status"] != "serving":
        raise RuntimeError(f"caption gate failed after publication: {final_captions}")
    external = oembed()
    if external["title"] != metadata["title"] or external["author_name"] != CHANNEL_NAME:
        raise RuntimeError(f"oEmbed mismatch after publication: {external}")
    checkpoint.update(
        {
            "privacy": "public",
            "processing": final_state["processing"],
            "upload_status": final_state["upload_status"],
            "embeddable": final_state["embeddable"],
            "caption_status": final_captions[0]["status"],
            "status": "PUBLIC_PROCESSING_SUCCEEDED_MANUAL_CAPTIONS_SERVING",
            "published_at": now(),
            "settlement_observations": observations,
            "oembed": external,
        }
    )
    write_json(PUBLIC_CHECKPOINT, checkpoint)
    receipt = {
        "marker": "HWAO_TORI_KUN_IMPLEMENTATION_REPORT_YOUTUBE_PUBLICATION_COMPLETE_V1",
        "completed_at_utc": now(),
        "channel_id": channel["id"],
        "channel_name": channel["snippet"]["title"],
        "video_id": VIDEO_ID,
        "url": f"https://youtu.be/{VIDEO_ID}",
        "title": metadata["title"],
        "privacy": "public",
        "processing": final_state["processing"],
        "upload_status": final_state["upload_status"],
        "duration": final_state["duration"],
        "embeddable": final_state["embeddable"],
        "made_for_kids": final_state["made_for_kids"],
        "self_declared_made_for_kids": final_state["self_declared_made_for_kids"],
        "caption_id": final_captions[0]["id"],
        "caption_status": final_captions[0]["status"],
        "source_sha256": local["source_sha256"],
        "source_bytes": local["source_bytes"],
        "caption_sha256": local["caption_sha256"],
        "public_metadata_sha256": local["metadata_sha256"],
        "mutation_performed": mutation_performed,
        "settlement_expected_reads": sum(1 for row in observations if row["expected"]),
        "settlement_observations": observations,
        "oembed": external,
        "older_videos_changed": False,
        "website_or_cockpit_changed": False,
        "git_changed": False,
        "runtime_deployed": False,
        "deletion_performed": False,
    }
    write_json(PUBLIC_RECEIPT, receipt)
    print(json.dumps(receipt, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
