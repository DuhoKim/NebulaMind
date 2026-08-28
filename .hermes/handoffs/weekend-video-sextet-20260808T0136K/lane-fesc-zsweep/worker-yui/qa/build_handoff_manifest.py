#!/usr/bin/env python3
"""Build a custody manifest for the official worker-Yui review directory."""

from __future__ import annotations

import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/weekend-video-sextet-20260808T0136K/lane-fesc-zsweep/worker-yui")
OUTPUT = ROOT / "HANDOFF_MANIFEST.json"
ALLOWED_SUFFIXES = {"", ".json", ".md", ".py", ".png", ".jpg", ".log"}
FORBIDDEN_MEDIA_SUFFIXES = {".mp4", ".mov", ".mkv", ".wav", ".mp3", ".m4a", ".aac"}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as handle:
        for block in iter(lambda: handle.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def main() -> None:
    files = []
    forbidden = []
    unexpected = []
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file() or path == OUTPUT:
            continue
        relative = path.relative_to(ROOT).as_posix()
        suffix = path.suffix.lower()
        if suffix in FORBIDDEN_MEDIA_SUFFIXES:
            forbidden.append(relative)
        if suffix not in ALLOWED_SUFFIXES:
            unexpected.append(relative)
        files.append({
            "path": relative,
            "sha256": sha256(path),
            "bytes": path.stat().st_size,
        })
    manifest = {
        "packet_type": "WORKER_YUI_REVIEW_HANDOFF__NO_OFFICIAL_CANDIDATE",
        "generated_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "root": str(ROOT),
        "file_count_excluding_manifest": len(files),
        "total_bytes_excluding_manifest": sum(item["bytes"] for item in files),
        "forbidden_media_files": forbidden,
        "unexpected_suffix_files": unexpected,
        "files": files,
    }
    OUTPUT.write_text(json.dumps(manifest, indent=2) + "\n")
    print(json.dumps({
        "manifest": str(OUTPUT),
        "file_count": len(files),
        "total_bytes": manifest["total_bytes_excluding_manifest"],
        "forbidden_media_files": forbidden,
        "unexpected_suffix_files": unexpected,
    }, indent=2))
    if forbidden or unexpected:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
