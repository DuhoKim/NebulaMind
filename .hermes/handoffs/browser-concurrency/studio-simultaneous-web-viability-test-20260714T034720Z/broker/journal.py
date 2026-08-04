"""Small journal helper (Tori: use a helper, not complex shell pipelines).

Appends ONE ledger entry whose payload includes sha256 of the listed files.
Usage: journal.py <ledger_path> <actor> <type> <note> <file1> [file2 ...]
"""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import ledger as ledger_mod


def sha256(p: Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def main(argv):
    ledger_path, actor, etype, note = Path(argv[1]), argv[2], argv[3], argv[4]
    files = {str(f): sha256(f) for f in argv[5:]}
    entry = ledger_mod.append(ledger_path, actor, etype, {"note": note, "files": files})
    print(json.dumps({"epoch": entry["epoch"], "entry_sha256": entry["entry_sha256"],
                      "n_files": len(files)}))
    ok, msg = ledger_mod.verify(ledger_path)
    print(("VERIFY_OK " if ok else "VERIFY_FAIL ") + msg)
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))
