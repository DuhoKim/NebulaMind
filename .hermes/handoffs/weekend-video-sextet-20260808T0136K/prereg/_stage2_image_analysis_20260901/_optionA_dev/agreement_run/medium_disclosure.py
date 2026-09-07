"""Retain source evidence about approval medium; never grant or infer approval.

API: disclose(source_pin, version_pin, message_id, output_path=None).
The source is a retained provider export, schema A1-PROVIDER-MESSAGES-1:
  provider, medium, reference, messages[]
Each message has id, role="user", author, provider_utc, text,
presented_version_sha256. These fields must already be in the pinned export.
An optional relay_utc is copied separately. No approval text, approval time,
digest, or author may be supplied as a replacement/default.

Pins protect bytes, not provenance. The operator must obtain the source pin
from retained provider evidence and independently establish that this was
Duho's approving message. A fabricated local export cannot be authenticated
by this module. Output ALWAYS says authorizes_execution=false and contains
no PASS/verdict/adopted/approved status. It is unusable as a run_path gate.
No real export or approval is produced by importing this module.
"""
import hashlib
import json
from pathlib import Path
import re
from datetime import datetime, timezone

class EvidenceError(ValueError):
    pass

def _require(ok, reason):
    if not ok:
        raise EvidenceError(reason)

def _read(pin):
    _require(isinstance(pin, dict) and set(pin) == {"path", "sha256"}, "Exact path/digest pin required")
    _require(isinstance(pin["path"], str) and bool(pin["path"]), "Missing evidence path")
    _require(isinstance(pin["sha256"], str) and
             re.fullmatch(r"[0-9a-f]{64}", pin["sha256"]), "Missing digest")
    try:
        raw = Path(pin["path"]).read_bytes()
    except OSError as exc:
        raise EvidenceError("Evidence file unavailable") from exc
    _require(hashlib.sha256(raw).hexdigest() == pin["sha256"], "Evidence digest mismatch")
    return raw

def _time(value):
    _require(isinstance(value, str), "Provider timestamp required")
    try:
        result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as exc:
        raise EvidenceError("Malformed timestamp") from exc
    _require(result.tzinfo is not None and result.utcoffset().total_seconds() == 0, "UTC timestamp required")
    _require(result <= datetime.now(timezone.utc), "Future timestamp refused")
    return result

def disclose(source_pin, version_pin, message_id, output_path=None):
    source_raw, version_raw = _read(source_pin), _read(version_pin)
    def unique_pairs(pairs):
        result = {}
        for key, value in pairs:
            _require(key not in result, "Duplicate JSON key")
            result[key] = value
        return result
    try:
        source = json.loads(source_raw, object_pairs_hook=unique_pairs)
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise EvidenceError("Malformed provider export") from exc
    _require(isinstance(source, dict) and source.get("schema") == "A1-PROVIDER-MESSAGES-1", "Provider export schema")
    for key in ("provider", "medium", "reference"):
        _require(isinstance(source.get(key), str) and bool(source[key].strip()), "Missing source " + key)
    messages = source.get("messages")
    _require(isinstance(messages, list) and all(isinstance(m, dict) for m in messages), "Messages required")
    _require(isinstance(message_id, str) and bool(message_id), "Message ID required")
    matches = [m for m in messages if m.get("id") == message_id]
    _require(len(matches) == 1, "Message missing or duplicated")
    message = matches[0]
    _require(message.get("role") == "user", "User evidence required")
    for key in ("author", "text"):
        _require(isinstance(message.get(key), str) and bool(message[key].strip()), "Missing message " + key)
    at = _time(message.get("provider_utc"))
    _require(message.get("presented_version_sha256") == version_pin["sha256"], "Presented-version mismatch")
    record = {
        "schema": "A1-MEDIUM-DISCLOSURE-1",
        "record_kind": "retained-provider-message-evidence",
        "authorizes_execution": False,
        "approval_determination": "outside-this-recorder",
        "provider_authenticity": "not-established-by-file-hash",
        "source": dict(source_pin),
        "version": dict(version_pin),
        "provider": source["provider"], "medium": source["medium"],
        "provider_reference": source["reference"],
        "message_id": message_id, "author": message["author"],
        "provider_utc": message["provider_utc"],
        "verbatim_message": message["text"],
        "message_utf8_sha256": hashlib.sha256(message["text"].encode("utf-8")).hexdigest(),
    }
    if "relay_utc" in source:
        _require(_time(source["relay_utc"]) >= at, "Relay precedes provider message")
        record["relay_utc"] = source["relay_utc"]
    raw = (json.dumps(record, sort_keys=True, separators=(",", ":"), allow_nan=False) + "\n").encode("utf-8")
    if output_path is not None:
        with Path(output_path).open("xb") as stream:
            stream.write(raw)
    return raw
