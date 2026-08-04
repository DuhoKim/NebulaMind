import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, "broker")
import ledger

EXPECTED = {
    "receipts/GORU_DR_RESULT.md": "84f3ebfee6ddc51fbfdbc918911fd1977f7943c7ddd5837e69c7784a12aed755",
    "receipts/GORU_DR_RESULT_METADATA.json": "17e137def32fb920662ed61de1d0f7f26bf88520ec3a33384cc4697082ccc13f",
    "receipts/GORU_DR_RUN_IDENTITY.json": "69bc9899ee044326ec97b5ef1f1bc2971557c6964e5f69dfa0dfeb3f42957fee",
    "receipts/GORU_DR_EXACT_OWN_DELETION.json": "759d150ff71074e8d6a09c5e14c4ce2516a00ec45e8b65fd6c08d9a184bdc43c",
}


def sha(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


hashes = {path: sha(path) for path in EXPECTED}
checks = {"hashes_match": hashes == EXPECTED}

ledger_path = Path("ledger/RUN_LEDGER.jsonl")
ledger_ok, ledger_msg = ledger.verify(ledger_path)
entries = ledger.read_entries(ledger_path)
by_epoch = {entry["epoch"]: entry for entry in entries}
checks.update({
    "ledger_verify": ledger_ok,
    "result_save_epoch_220": by_epoch.get(220, {}).get("type") == "dr_result_saved_verified" and by_epoch.get(220, {}).get("entry_sha256") == "3380829d0daf5f92c31086fce2870b18191841c0cdf1c7f214dea1139068c47d",
    "delete_epoch_239": by_epoch.get(239, {}).get("type") == "dr_exact_own_conversation_deleted",
    "title_correction_epoch_240": by_epoch.get(240, {}).get("type") == "dr_deletion_log_title_correction",
    "save_precedes_delete": 220 < 239 < 240,
})

identity = json.loads(Path("receipts/GORU_DR_RUN_IDENTITY.json").read_text())
metadata = json.loads(Path("receipts/GORU_DR_RESULT_METADATA.json").read_text())
deleted = json.loads(Path("receipts/GORU_DR_EXACT_OWN_DELETION.json").read_text())
checks.update({
    "id_matches": identity["conversation_id"] == metadata["identity"]["conversation_id"] == deleted["conversation_id"] == "8af765be7d623416",
    "submit_utc_matches": identity["submit_utc"] == metadata["identity"]["submit_utc"] == deleted["submit_utc"] == "2026-07-14T09:45:28.451996Z",
    "captured_title_matches": identity["conversation_title"] == deleted["captured_title"],
    "deletion_title_matches_prompt": identity["prompt"] == deleted["deletion_match_title"],
    "verified_receipt_hash_matches": deleted["verified_result_receipt_sha256"] == EXPECTED["receipts/GORU_DR_RESULT.md"],
    "verified_save_epoch_matches": deleted["verified_result_save_epoch"] == 220,
    "dialog_confirmation": deleted["confirmation_mode"] == "dialog" and "Delete chat?" in deleted["confirmation_dialog"],
    "post_path_is_new_chat": deleted["post_delete_path"] == "/app",
    "no_bulk_delete": deleted["bulk_delete_used"] is False,
    "no_unrelated_touch": deleted["unrelated_conversation_touched"] is False,
    "raw_result_quality_miss_recorded": "exceeded the requested no-more-than-eight-bullets format" in by_epoch[220]["payload"]["note"],
})

failed = sorted(name for name, passed in checks.items() if not passed)
print(json.dumps({
    "status": "PASS" if not failed else "FAIL",
    "failed": failed,
    "checks": checks,
    "ledger": ledger_msg,
    "ledger_entries": len(entries),
    "quality_note": "Raw result preserved but exceeded the requested eight-bullet format; no rerun authorized.",
}, sort_keys=True))
raise SystemExit(0 if not failed else 1)
