#!/usr/bin/env python3
"""Fetch public Crossref records for all non-none item-06 DOI values."""

from __future__ import annotations

import argparse
import importlib.util
import json
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def load_membership_module(path: Path) -> Any:
    spec = importlib.util.spec_from_file_location("item06_membership", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to import {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def fetch_doi(doi: str, max_attempts: int = 5) -> dict[str, Any]:
    url = "https://api.crossref.org/works/" + urllib.parse.quote(doi, safe="")
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "NebulaMind/1.0 (local bibliography reconciliation)"},
    )
    for attempt in range(1, max_attempts + 1):
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                return {
                    "url": url,
                    "http_status": response.status,
                    "response": json.loads(response.read().decode("utf-8")),
                }
        except urllib.error.HTTPError as error:
            if error.code not in {429, 500, 502, 503, 504} or attempt == max_attempts:
                return {
                    "url": url,
                    "http_status": error.code,
                    "error": str(error),
                }
            retry_after = error.headers.get("Retry-After")
            delay = int(retry_after) if retry_after and retry_after.isdigit() else 3 * attempt
            time.sleep(delay)
        except urllib.error.URLError as error:
            if attempt == max_attempts:
                return {"url": url, "http_status": None, "error": str(error)}
            time.sleep(3 * attempt)
    raise RuntimeError("unreachable")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--membership-script", type=Path, required=True)
    parser.add_argument("--raw", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    membership_module = load_membership_module(args.membership_script)
    rows = membership_module.parse_raw_rows(args.raw.read_text(encoding="utf-8"))
    keys = [key for key in sorted(rows) if rows[key]["doi"].lower() != "none"]
    results: dict[str, Any] = {}
    for index, key in enumerate(keys):
        if index:
            time.sleep(0.5)
        results[key] = {
            "requested_doi": rows[key]["doi"],
            **fetch_doi(rows[key]["doi"]),
        }

    artifact = {
        "schema_version": 1,
        "status": "PUBLIC_CROSSREF_DOI_RECORDS_CAPTURED",
        "captured_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "retrieval": "unauthenticated public Crossref API; no browser or account action",
        "record_count": len(results),
        "results": results,
    }
    args.output.write_text(
        json.dumps(artifact, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
