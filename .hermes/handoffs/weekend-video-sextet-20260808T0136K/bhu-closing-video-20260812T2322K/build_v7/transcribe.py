#!/usr/bin/env python3
"""Transcribe a local audio file through the Hermes managed OpenAI audio gateway."""
from __future__ import annotations
import argparse
import json
import mimetypes
from pathlib import Path
import secrets
import sys
import urllib.request

sys.path.insert(0, "/Users/duhokim/.hermes/hermes-agent")
from tools.managed_tool_gateway import resolve_managed_tool_gateway


def multipart(fields: dict[str, str], file_field: str, path: Path) -> tuple[bytes, str]:
    boundary = "----HermesBHU" + secrets.token_hex(12)
    chunks: list[bytes] = []
    for name, value in fields.items():
        chunks += [
            f"--{boundary}\r\n".encode(),
            f'Content-Disposition: form-data; name="{name}"\r\n\r\n'.encode(),
            value.encode(), b"\r\n",
        ]
    mime = mimetypes.guess_type(path.name)[0] or "application/octet-stream"
    chunks += [
        f"--{boundary}\r\n".encode(),
        f'Content-Disposition: form-data; name="{file_field}"; filename="{path.name}"\r\n'.encode(),
        f"Content-Type: {mime}\r\n\r\n".encode(), path.read_bytes(), b"\r\n",
        f"--{boundary}--\r\n".encode(),
    ]
    return b"".join(chunks), boundary


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("audio")
    ap.add_argument("--model", default="whisper-1")
    ap.add_argument("--out")
    a = ap.parse_args()
    path = Path(a.audio)
    body, boundary = multipart({"model": a.model, "response_format": "json", "language": "en"}, "file", path)
    gateway = resolve_managed_tool_gateway("openai-audio")
    req = urllib.request.Request(gateway.gateway_origin.rstrip("/") + "/v1/audio/transcriptions", data=body, method="POST")
    req.add_header("Authorization", "Bearer " + gateway.nous_user_token)
    req.add_header("Content-Type", f"multipart/form-data; boundary={boundary}")
    data = urllib.request.urlopen(req, timeout=300).read()
    parsed = json.loads(data)
    text = parsed.get("text", "")
    if a.out:
        Path(a.out).write_text(json.dumps(parsed, ensure_ascii=False, indent=2) + "\n")
    print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
