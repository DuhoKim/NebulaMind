import argparse
import hashlib
import json
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path

LEDGER = Path("ledger/RUN_LEDGER.jsonl")
EXPECTED_FILE_SHA256 = "61b4a2c5c777d375aaf5c2815c9a573515cb739c19ebcd3b53b418123cb9b239"
EXPECTED_ENTRY_COUNT = 1573
EXPECTED_FIRST_CONFLICT_INDEX = 1564
EXPECTED_BROKER_BRANCH_SHA256 = "5e26d295587d0725b8cf870acdfeed3c8c081362e270ebd6e9eaf83e28f48a36"
EXPECTED_HWAO_BRANCH_SHA256 = "ec5cdd0b8292c8f1dd0f2a7c8d10b971d9eea94a142204859d3b9f559c1d41fb"


def canon(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode()


def entry_hash(entry):
    return hashlib.sha256(canon({k: v for k, v in entry.items() if k != "entry_sha256"})).hexdigest()


def file_sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def verify(entries):
    previous = "0" * 64
    for index, entry in enumerate(entries):
        if entry["epoch"] != index:
            return False, f"epoch break at index {index}: {entry['epoch']}"
        if entry["prev_sha256"] != previous:
            return False, f"chain break at epoch {index}"
        if entry_hash(entry) != entry["entry_sha256"]:
            return False, f"hash mismatch at epoch {index}"
        previous = entry["entry_sha256"]
    return True, f"OK ({len(entries)} entries)"


def rebuild(original, backup_path, backup_sha):
    rebuilt = []
    previous = "0" * 64
    for index, old in enumerate(original):
        entry = {
            "epoch": index,
            "utc": old["utc"],
            "actor": old["actor"],
            "type": old["type"],
            "payload": old["payload"],
            "prev_sha256": previous,
        }
        entry["entry_sha256"] = entry_hash(entry)
        rebuilt.append(entry)
        previous = entry["entry_sha256"]
    repair = {
        "epoch": len(rebuilt),
        "utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "actor": "tori",
        "type": "ledger_epoch_fork_repaired",
        "payload": {
            "reason": "Concurrent direct Hwao journal append raced the live broker at epoch 1563 during paper_09 submit.",
            "method": "Preserved every original entry in original file order; reindexed and rehashed from the first duplicate; appended this repair receipt.",
            "original_entry_count": len(original),
            "first_conflict_index": EXPECTED_FIRST_CONFLICT_INDEX,
            "duplicate_epoch": 1563,
            "original_broker_branch_entry_sha256": EXPECTED_BROKER_BRANCH_SHA256,
            "original_hwao_branch_entry_sha256": EXPECTED_HWAO_BRANCH_SHA256,
            "invalid_ledger_backup": str(backup_path.resolve()),
            "invalid_ledger_backup_sha256": backup_sha,
            "broker_emergency_stop_preserved": True,
            "broker_remains_frozen_pending_user-gated_reset": True,
            "all_original_events_preserved": True,
            "hwao_acknowledged_no_more_direct_ledger_appends": True,
        },
        "prev_sha256": previous,
    }
    repair["entry_sha256"] = entry_hash(repair)
    rebuilt.append(repair)
    return rebuilt


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    raw = LEDGER.read_bytes()
    current_sha = hashlib.sha256(raw).hexdigest()
    if current_sha != EXPECTED_FILE_SHA256:
        raise SystemExit(f"FAIL_CLOSED ledger drift: {current_sha}")
    original = [json.loads(line) for line in raw.decode().splitlines() if line.strip()]
    if len(original) != EXPECTED_ENTRY_COUNT:
        raise SystemExit(f"FAIL_CLOSED entry count drift: {len(original)}")
    if original[EXPECTED_FIRST_CONFLICT_INDEX]["entry_sha256"] != EXPECTED_HWAO_BRANCH_SHA256:
        raise SystemExit("FAIL_CLOSED Hwao conflict entry drift")
    if original[EXPECTED_FIRST_CONFLICT_INDEX - 1]["entry_sha256"] != EXPECTED_BROKER_BRANCH_SHA256:
        raise SystemExit("FAIL_CLOSED broker conflict entry drift")
    backup = LEDGER.with_name("RUN_LEDGER.invalid-epoch1563-20260714T133556Z.jsonl")
    rebuilt = rebuild(original, backup, current_sha)
    ok, message = verify(rebuilt)
    if not ok:
        raise SystemExit(f"REBUILD_VERIFY_FAIL {message}")
    encoded = ("\n".join(json.dumps(entry, sort_keys=True) for entry in rebuilt) + "\n").encode()
    report = {
        "mode": "apply" if args.apply else "dry-run",
        "original_sha256": current_sha,
        "backup": str(backup),
        "rebuilt_entry_count": len(rebuilt),
        "rebuilt_file_sha256": hashlib.sha256(encoded).hexdigest(),
        "last_epoch": rebuilt[-1]["epoch"],
        "last_entry_sha256": rebuilt[-1]["entry_sha256"],
        "verify": message,
    }
    if not args.apply:
        print(json.dumps(report, sort_keys=True))
        return
    if backup.exists():
        raise SystemExit(f"FAIL_CLOSED backup already exists: {backup}")
    with backup.open("xb") as handle:
        handle.write(raw)
        handle.flush()
        os.fsync(handle.fileno())
    if file_sha(backup) != current_sha:
        raise SystemExit("FAIL_CLOSED backup hash mismatch")
    descriptor, temporary = tempfile.mkstemp(prefix=LEDGER.name + ".repair-", dir=str(LEDGER.parent))
    try:
        with os.fdopen(descriptor, "wb") as handle:
            handle.write(encoded)
            handle.flush()
            os.fsync(handle.fileno())
        if file_sha(Path(temporary)) != report["rebuilt_file_sha256"]:
            raise SystemExit("FAIL_CLOSED temporary repaired hash mismatch")
        if file_sha(LEDGER) != EXPECTED_FILE_SHA256:
            raise SystemExit("FAIL_CLOSED ledger changed during repair")
        os.replace(temporary, LEDGER)
        temporary = None
    finally:
        if temporary:
            Path(temporary).unlink(missing_ok=True)
    repaired = [json.loads(line) for line in LEDGER.read_text().splitlines() if line.strip()]
    ok, message = verify(repaired)
    if not ok:
        raise SystemExit(f"POST_APPLY_VERIFY_FAIL {message}")
    report["post_apply_sha256"] = file_sha(LEDGER)
    report["post_apply_verify"] = message
    report["backup_sha256"] = file_sha(backup)
    print(json.dumps(report, sort_keys=True))


if __name__ == "__main__":
    main()
