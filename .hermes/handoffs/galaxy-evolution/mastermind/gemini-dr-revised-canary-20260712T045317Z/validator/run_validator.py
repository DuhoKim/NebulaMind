#!/usr/bin/env python3
import argparse
import json
from pathlib import Path

from validator import validate_document


def main():
    parser = argparse.ArgumentParser(description="Validate a captured Gemini C1r rendered answer")
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
    args.output.write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(result["overall"])
    return {"PASS": 0, "FAIL": 1, "MANUAL_REVIEW_REQUIRED": 2}[result["overall"]]


if __name__ == "__main__":
    raise SystemExit(main())
