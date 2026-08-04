#!/usr/bin/env python3
"""Fetch public Semantic Scholar title-search candidates for selected item-06 rows."""

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


FIELDS = "title,year,authors,venue,journal,externalIds,url"


def load_membership_module(path: Path) -> Any:
    spec = importlib.util.spec_from_file_location("item06_membership", path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"Unable to import {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def fetch_title(title: str, max_attempts: int = 6) -> dict[str, Any]:
    query = urllib.parse.urlencode(
        {"query": title, "limit": 5, "fields": FIELDS}
    )
    url = "https://api.semanticscholar.org/graph/v1/paper/search?" + query
    request = urllib.request.Request(
        url,
        headers={"User-Agent": "NebulaMind/1.0 local bibliography reconciliation"},
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
            if error.code != 429 or attempt == max_attempts:
                raise
            retry_after = error.headers.get("Retry-After")
            delay = int(retry_after) if retry_after and retry_after.isdigit() else 4 * attempt
            time.sleep(delay)
        except urllib.error.URLError:
            if attempt == max_attempts:
                raise
            time.sleep(3 * attempt)
    raise RuntimeError("unreachable")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--membership-script", type=Path, required=True)
    parser.add_argument("--raw", type=Path, required=True)
    parser.add_argument("--keys", nargs="+", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()

    membership_module = load_membership_module(args.membership_script)
    rows = membership_module.parse_raw_rows(args.raw.read_text(encoding="utf-8"))
    unknown = sorted(set(args.keys) - set(rows))
    if unknown:
        raise ValueError(f"Unknown keys: {unknown}")

    results: dict[str, Any] = {}
    for index, key in enumerate(args.keys):
        if index:
            time.sleep(3)
        results[key] = {
            "raw_title_query": rows[key]["title"],
            **fetch_title(rows[key]["title"]),
        }

    artifact = {
        "schema_version": 1,
        "status": "PUBLIC_TITLE_SEARCH_CANDIDATES_CAPTURED",
        "captured_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "retrieval": "unauthenticated public Semantic Scholar API; no browser or account action",
        "results": results,
    }
    args.output.write_text(
        json.dumps(artifact, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
