#!/usr/bin/env python3
"""Backfill authors column from arXiv API for evidence rows where authors IS NULL."""

import json
import re
import time
import xml.etree.ElementTree as ET

import psycopg2
import urllib.request
import urllib.error

DB_URL = "postgresql://nebula:nebula@localhost:5432/nebulamind"
ARXIV_API = "http://export.arxiv.org/api/query"
BATCH_SIZE = 100
RATE_LIMIT_DELAY = 0.34  # ~3 req/sec

NS = {"atom": "http://www.w3.org/2005/Atom"}


def normalize_arxiv_id(raw_id: str) -> str | None:
    """Normalize various arXiv ID formats to canonical YYMM.NNNNN or area/YYMMNNN."""
    # Already standard: 1711.03285 or 2207.07013 (4+4 or 4+5 digits)
    if re.match(r"^\d{4}\.\d{4,5}$", raw_id):
        return raw_id
    # Old-style: hep-th/0101234
    if re.match(r"^[a-z][\w-]+/\d{7}$", raw_id):
        return raw_id
    # ADS bibcode: 2014arXiv1403.7377W or 2023arXiv230500999P
    m = re.match(r"^\d{4}arXiv(.+?)([A-Z]?)$", raw_id)
    if m:
        inner = m.group(1)  # e.g. "1403.7377" or "230500999"
        if "." in inner:
            return inner  # already has period
        # Insert period after 4-digit YYMM prefix
        if len(inner) >= 8:
            return inner[:4] + "." + inner[4:]
        return None
    # DOI format: 10.48550/arXiv.2410.07841
    m = re.match(r"^10\.\d+/arXiv\.(.+)$", raw_id)
    if m:
        candidate = m.group(1)
        if re.match(r"^\d{4}\.\d{4,5}$", candidate):
            return candidate
    return None


def fetch_authors_batch(arxiv_ids: list[str]) -> dict[str, list[str]]:
    """Fetch authors for a batch of canonical arXiv IDs. Returns {canonical_id: [authors]}."""
    id_list = ",".join(arxiv_ids)
    url = f"{ARXIV_API}?id_list={id_list}&max_results={len(arxiv_ids)}"

    try:
        req = urllib.request.Request(url, headers={"User-Agent": "NebulaMind/1.0 (backfill)"})
        with urllib.request.urlopen(req, timeout=30) as resp:
            data = resp.read()
    except urllib.error.URLError as e:
        print(f"  HTTP error: {e}")
        return {}

    root = ET.fromstring(data)
    result = {}

    for entry in root.findall("atom:entry", NS):
        id_elem = entry.find("atom:id", NS)
        if id_elem is None:
            continue
        # e.g. http://arxiv.org/abs/1234.56789v1
        raw_id = id_elem.text.strip().split("/abs/")[-1]
        # Strip version suffix
        canonical = re.sub(r"v\d+$", "", raw_id)

        authors = []
        for author_elem in entry.findall("atom:author", NS):
            name_elem = author_elem.find("atom:name", NS)
            if name_elem is not None and name_elem.text:
                authors.append(name_elem.text.strip())

        if authors:
            result[canonical] = authors
            result[raw_id] = authors  # also store versioned form

    return result


def main():
    conn = psycopg2.connect(DB_URL)
    conn.autocommit = False
    cur = conn.cursor()

    cur.execute(
        "SELECT DISTINCT arxiv_id FROM evidence WHERE authors IS NULL AND arxiv_id IS NOT NULL"
    )
    raw_ids = [row[0] for row in cur.fetchall()]
    print(f"Unique raw arxiv IDs: {len(raw_ids)}")

    # Build mapping: raw_id -> canonical_id
    id_map: dict[str, str] = {}
    skipped_ids = []
    for raw in raw_ids:
        canonical = normalize_arxiv_id(raw)
        if canonical:
            id_map[raw] = canonical
        else:
            skipped_ids.append(raw)

    canonical_ids = list(set(id_map.values()))
    print(f"Normalizable: {len(canonical_ids)} unique canonical IDs")
    print(f"Skipped (unrecognized format): {len(skipped_ids)}: {skipped_ids[:5]}")

    # Fetch in batches
    authors_cache: dict[str, list[str]] = {}
    fetch_errors = 0

    for i in range(0, len(canonical_ids), BATCH_SIZE):
        batch = canonical_ids[i : i + BATCH_SIZE]
        batch_num = i // BATCH_SIZE + 1
        total_batches = (len(canonical_ids) + BATCH_SIZE - 1) // BATCH_SIZE
        print(f"Fetching batch {batch_num}/{total_batches} ({len(batch)} IDs)...")

        result = fetch_authors_batch(batch)
        authors_cache.update(result)

        found = sum(1 for id_ in batch if id_ in result)
        missing_in_batch = len(batch) - found
        if missing_in_batch:
            fetch_errors += missing_in_batch
            missing = [id_ for id_ in batch if id_ not in result]
            print(f"  {missing_in_batch} not found: {missing[:3]}")
        else:
            print(f"  OK: {found}/{len(batch)} found")

        time.sleep(RATE_LIMIT_DELAY)

    print(f"\nAuthors found for {len(set(authors_cache.keys()))} canonical IDs")

    # Update rows
    cur.execute(
        "SELECT id, arxiv_id FROM evidence WHERE authors IS NULL AND arxiv_id IS NOT NULL"
    )
    rows = cur.fetchall()

    rows_updated = 0
    rows_skipped = 0

    for row_id, raw_arxiv_id in rows:
        canonical = id_map.get(raw_arxiv_id)
        authors = None
        if canonical:
            authors = authors_cache.get(canonical)
            if authors is None:
                # Try without version
                stripped = re.sub(r"v\d+$", "", canonical)
                authors = authors_cache.get(stripped)

        if authors:
            cur.execute(
                "UPDATE evidence SET authors = %s WHERE id = %s",
                (json.dumps(authors), row_id),
            )
            rows_updated += 1
        else:
            rows_skipped += 1

    conn.commit()
    cur.close()
    conn.close()

    print(f"\n=== Done ===")
    print(f"Rows updated : {rows_updated}")
    print(f"Rows skipped : {rows_skipped} (no authors found or unrecognized ID)")
    print(f"Fetch errors : {fetch_errors}")


if __name__ == "__main__":
    main()
