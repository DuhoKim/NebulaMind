#!/usr/bin/env python3
"""Pin exact arXiv abstract metadata for item-06 composite corrections."""

from __future__ import annotations

import argparse
import hashlib
import json
import time
import urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path
from typing import Any


CORRECTIONS = {
    "REV06-P004": {
        "arxiv": "1002.2149",
        "doi": "10.1038/nature08773",
    },
    "REV06-P015": {
        "arxiv": "1003.3889",
        "doi": "10.1088/2041-8205/714/1/l118",
    },
    "REV06-P016": {
        "arxiv": "1103.1642",
        "doi": "10.1111/j.1365-2966.2011.18677.x",
    },
    "REV06-P017": {
        "arxiv": "astro-ph/9712213",
        "doi": "10.1086/305588",
    },
    "REV06-P024": {
        "arxiv": "astro-ph/0608003",
        "doi": "10.1086/511055",
    },
}


class MetaParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.meta: dict[str, list[str]] = {}

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        if tag.lower() != "meta":
            return
        values = dict(attrs)
        name = values.get("name") or values.get("property")
        content = values.get("content")
        if name and content:
            self.meta.setdefault(name, []).append(content)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--directory", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    args.directory.mkdir(parents=True, exist_ok=True)

    results: dict[str, dict[str, Any]] = {}
    for index, (key, correction) in enumerate(CORRECTIONS.items()):
        if index:
            time.sleep(3)
        arxiv_id = correction["arxiv"]
        url = "https://arxiv.org/abs/" + arxiv_id
        request = urllib.request.Request(
            url,
            headers={"User-Agent": "NebulaMind/1.0 local bibliography reconciliation"},
        )
        with urllib.request.urlopen(request, timeout=60) as response:
            body = response.read()
            status = response.status
        safe_id = arxiv_id.replace("/", "_")
        page_path = args.directory / f"arxiv_{safe_id}_abstract.html"
        page_path.write_bytes(body)
        meta_parser = MetaParser()
        meta_parser.feed(body.decode("utf-8", errors="replace"))
        meta = meta_parser.meta
        related_dois = [
            value
            for name, values in meta.items()
            if "doi" in name.lower()
            for value in values
        ]
        results[key] = {
            "url": url,
            "http_status": status,
            "arxiv_id": arxiv_id,
            "expected_related_doi": correction["doi"],
            "citation_title": (meta.get("citation_title") or [None])[0],
            "citation_authors": meta.get("citation_author") or [],
            "citation_date": (meta.get("citation_date") or [None])[0],
            "citation_arxiv_id": (meta.get("citation_arxiv_id") or [None])[0],
            "citation_doi_values": related_dois,
            "saved_html": str(page_path),
            "saved_html_sha256": hashlib.sha256(body).hexdigest(),
            "saved_html_bytes": len(body),
        }

    artifact = {
        "schema_version": 1,
        "status": "ARXIV_COMPOSITE_CORRECTIONS_PINNED",
        "captured_at_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "retrieval": "unauthenticated arXiv abstract pages; no browser or account action",
        "results": results,
    }
    args.output.write_text(
        json.dumps(artifact, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
