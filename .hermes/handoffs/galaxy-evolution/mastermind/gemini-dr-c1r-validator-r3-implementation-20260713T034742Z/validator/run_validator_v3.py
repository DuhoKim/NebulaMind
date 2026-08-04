from __future__ import annotations

import argparse
import json
from pathlib import Path

from validator_v3 import validate_document


def main() -> int:
    parser = argparse.ArgumentParser(description="Run the C1r r3 validator over an offline structured capture.")
    parser.add_argument("--body", required=True, type=Path)
    parser.add_argument("--structured", required=True, type=Path)
    parser.add_argument("--spec", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args()

    body = args.body.read_text()
    structured = json.loads(args.structured.read_text())
    spec = json.loads(args.spec.read_text())
    result = validate_document(body, structured, spec)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True, ensure_ascii=False) + "\n")
    print(json.dumps({"overall": result["overall"], "findings": len(result["findings"]), "output": str(args.output)}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
