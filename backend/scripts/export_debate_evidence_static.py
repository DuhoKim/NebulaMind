#!/usr/bin/env python3
"""Export static debate_evidence.v1 envelopes without writing to the database."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
if str(ROOT) not in sys.path:
    sys.path.insert(0, str(ROOT))

from app.database import SessionLocal
from app.models.claim import Claim
from app.routers.claims import serialize_claim_evidence


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Export static debate_evidence.v1 JSON keyed by claim id.")
    parser.add_argument("--output", required=True, help="Output evidence.json path.")
    parser.add_argument("--claim-id", type=int, action="append", default=[], help="Claim id to export; repeatable.")
    parser.add_argument("--page-id", type=int, help="Export all claims for a page id.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if not args.claim_id and args.page_id is None:
        raise SystemExit("Provide at least one --claim-id or --page-id.")

    output = Path(args.output)
    db = SessionLocal()
    try:
        claim_ids = list(dict.fromkeys(args.claim_id))
        if args.page_id is not None:
            page_claim_ids = [
                row[0]
                for row in db.query(Claim.id)
                .filter(Claim.page_id == args.page_id)
                .order_by(Claim.order_idx, Claim.id)
                .all()
            ]
            claim_ids.extend(page_claim_ids)
            claim_ids = list(dict.fromkeys(claim_ids))

        payload = {str(claim_id): serialize_claim_evidence(claim_id, db) for claim_id in claim_ids}
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n")
        db.rollback()
    finally:
        db.close()

    print(json.dumps({"output": str(output), "claims": len(payload), "schema_version": "debate_evidence.v1"}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
