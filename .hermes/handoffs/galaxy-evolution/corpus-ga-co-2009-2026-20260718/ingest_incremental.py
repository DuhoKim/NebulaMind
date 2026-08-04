#!/usr/bin/env python3
"""Increment-1 daily ingest for recent arXiv astro-ph.GA/CO papers.

Fetch from the tokenless public API, deduplicate, embed with
qwen3-embedding:4b, assign to the nearest frozen cluster centroid, and append
to the delta store. The frozen full-corpus snapshot is never modified.
"""

import argparse
from contextlib import contextmanager
import fcntl
import html
import json
import os
import re
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

import numpy as np

ENG = os.path.dirname(os.path.abspath(__file__))
DELTA = f"{ENG}/delta"
os.makedirs(DELTA, exist_ok=True)
MODEL = "qwen3-embedding:4b"
DIM = 2560
TEXTCHARS = 4000
ATOM = "{http://www.w3.org/2005/Atom}"
ARX = "{http://arxiv.org/schemas/atom}"


def clean(value):
    """Mirror embed_corpus text cleanup."""
    value = html.unescape(value or "")
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def element_text(entry, tag):
    element = entry.find(tag)
    return element.text if element is not None and element.text else ""


FETCH_ATTEMPTS = 4
FETCH_BACKOFF_SECONDS = (30, 120, 300)
FETCH_RETRY_STATUSES = (429, 500, 502, 503, 504)


def fetch_bytes(request, timeout=40):
    """arXiv throttles hard near the 00:00 UTC announcement; back off, honor Retry-After."""
    for attempt in range(FETCH_ATTEMPTS):
        try:
            return urllib.request.urlopen(request, timeout=timeout).read()
        except urllib.error.HTTPError as error:
            if error.code not in FETCH_RETRY_STATUSES or attempt == FETCH_ATTEMPTS - 1:
                raise
            delay = FETCH_BACKOFF_SECONDS[attempt]
            retry_after = (error.headers.get("Retry-After") or "").strip()
            if retry_after.isdigit():
                delay = min(max(int(retry_after), delay), 300)
            print(
                f"arxiv fetch HTTP {error.code}; retry {attempt + 1} in {delay}s",
                flush=True,
            )
            time.sleep(delay)
        except OSError as error:
            if attempt == FETCH_ATTEMPTS - 1:
                raise
            delay = FETCH_BACKOFF_SECONDS[attempt]
            print(f"arxiv fetch failed ({error}); retry {attempt + 1} in {delay}s", flush=True)
            time.sleep(delay)


def fetch(n=30):
    query = (
        "https://export.arxiv.org/api/query?"
        "search_query=cat:astro-ph.GA+OR+cat:astro-ph.CO"
        f"&start=0&max_results={n}&sortBy=submittedDate&sortOrder=descending"
    )
    request = urllib.request.Request(
        query,
        headers={"User-Agent": "NebulaMind-ingest/1"},
    )
    xml = fetch_bytes(request)
    root = ET.fromstring(xml)
    papers = []
    for entry in root.findall(f"{ATOM}entry"):
        arxiv_id = element_text(entry, f"{ATOM}id").split("/abs/")[-1]
        if not arxiv_id:
            continue
        base_id = arxiv_id.split("v")[0]
        primary = entry.find(f"{ARX}primary_category")
        category = primary.get("term") if primary is not None else ""
        published = element_text(entry, f"{ATOM}published")
        year = published[:4]
        papers.append(
            {
                "arxiv_id": base_id,
                "version": arxiv_id,
                "title": clean(element_text(entry, f"{ATOM}title")),
                "abstract": clean(element_text(entry, f"{ATOM}summary")),
                "primary_category": category,
                "submitted": published[:10] or None,
                "year": int(year) if year.isdigit() else None,
            }
        )
    return papers


def embed(texts):
    vectors = []
    for text in texts:
        body = json.dumps({"model": MODEL, "input": [text[:TEXTCHARS]]}).encode()
        request = urllib.request.Request(
            "http://localhost:11434/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
        )
        response = urllib.request.urlopen(request, timeout=120)
        vectors.append(np.asarray(json.load(response)["embeddings"][0], np.float32))
    return np.vstack(vectors)


def atomic_json(path, payload):
    temporary = f"{path}.{os.getpid()}.tmp"
    with open(temporary, "w", encoding="utf-8") as handle:
        json.dump(payload, handle)
        handle.flush()
        os.fsync(handle.fileno())
    os.replace(temporary, path)


def truncate_to(path, size):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "ab"):
        pass
    with open(path, "r+b") as handle:
        handle.truncate(size)


def recover_incomplete_transaction():
    transaction = f"{DELTA}/.ingest_transaction.json"
    if not os.path.exists(transaction):
        return False
    with open(transaction, encoding="utf-8") as handle:
        state = json.load(handle)
    truncate_to(f"{DELTA}/new_emb.f32", state["embedding_bytes"])
    truncate_to(f"{DELTA}/new_papers.jsonl", state["paper_bytes"])
    atomic_json(f"{DELTA}/new_labels.json", state["labels"])
    os.unlink(transaction)
    print("recovered an incomplete prior delta append")
    return True


def commit_batch(vectors, records, labels):
    embeddings_path = f"{DELTA}/new_emb.f32"
    papers_path = f"{DELTA}/new_papers.jsonl"
    labels_path = f"{DELTA}/new_labels.json"
    transaction = f"{DELTA}/.ingest_transaction.json"
    previous_labels = {}
    if os.path.exists(labels_path):
        with open(labels_path, encoding="utf-8") as handle:
            previous_labels = json.load(handle)
    state = {
        "embedding_bytes": (
            os.path.getsize(embeddings_path) if os.path.exists(embeddings_path) else 0
        ),
        "paper_bytes": os.path.getsize(papers_path) if os.path.exists(papers_path) else 0,
        "labels": previous_labels,
    }
    atomic_json(transaction, state)
    try:
        with open(embeddings_path, "ab") as handle:
            handle.write(np.ascontiguousarray(vectors, np.float32).tobytes())
            handle.flush()
            os.fsync(handle.fileno())
        with open(papers_path, "a", encoding="utf-8") as handle:
            for record in records:
                handle.write(json.dumps(record) + "\n")
            handle.flush()
            os.fsync(handle.fileno())
        atomic_json(labels_path, labels)
    except BaseException:
        recover_incomplete_transaction()
        raise
    os.unlink(transaction)


@contextmanager
def pipeline_lock():
    if os.getenv("NEBULAMIND_FRONTIER_LOCK_HELD") == "1":
        yield
        return
    lock_path = f"{ENG}/.frontier_pipeline.lock"
    with open(lock_path, "a+", encoding="utf-8") as handle:
        try:
            fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError as exc:
            raise RuntimeError(f"frontier pipeline already running: {lock_path}") from exc
        try:
            yield
        finally:
            fcntl.flock(handle.fileno(), fcntl.LOCK_UN)


def run(n, dry_run=False):
    recover_incomplete_transaction()
    papers_path = f"{DELTA}/new_papers.jsonl"
    seen = set()
    if os.path.exists(papers_path):
        with open(papers_path, encoding="utf-8") as handle:
            seen = {json.loads(line)["arxiv_id"] for line in handle if line.strip()}
    fetched = fetch(n)
    window_saturated = len(fetched) >= n and all(
        paper["arxiv_id"] not in seen for paper in fetched
    )
    papers = [
        paper
        for paper in fetched
        if paper["arxiv_id"] not in seen and len(paper["abstract"].split()) >= 40
    ]
    if dry_run:
        result = {
            "status": "dry_run",
            "fetched": len(fetched),
            "new_papers": len(papers),
            "window_saturated": window_saturated,
            "arxiv_ids": [paper["arxiv_id"] for paper in papers],
        }
        print(json.dumps(result, sort_keys=True))
        return result
    if window_saturated and n < 500:
        raise RuntimeError(
            f"all {n} fetched papers are unseen; run an audited catch-up with limit 500"
        )
    if not papers:
        result = {
            "status": "finished",
            "ingested": 0,
            "assigned": 0,
            "novel_or_noise": 0,
        }
        print("no new papers")
        print(json.dumps(result, sort_keys=True))
        return result

    centroids = np.load(f"{ENG}/centroids_v2.npy")
    with open(f"{ENG}/centroids_meta.json", encoding="utf-8") as handle:
        centroid_metadata = json.load(handle)
    order = centroid_metadata["order"]
    tau_assign = centroid_metadata["tau_assign"]
    tau_drift = centroid_metadata["tau_drift"]
    with open(f"{ENG}/frontier_map_v3.json", encoding="utf-8") as handle:
        frontier_map = json.load(handle)
    keywords = {
        cluster["cluster"]: ", ".join(cluster["keywords"][:5])
        for cluster in frontier_map["clusters"]
    }

    vectors = embed([f'{paper["title"]}. {paper["abstract"]}' for paper in papers])
    if vectors.ndim != 2 or vectors.shape[1] != DIM:
        raise RuntimeError(
            f"embedding dimension mismatch: got {vectors.shape}, expected (*, {DIM})"
        )
    normalized = vectors / (np.linalg.norm(vectors, axis=1, keepdims=True) + 1e-9)
    similarities = normalized @ centroids.T
    best = similarities.argmax(1)
    best_similarity = similarities.max(1)

    labels_path = f"{DELTA}/new_labels.json"
    labels = {}
    if os.path.exists(labels_path):
        with open(labels_path, encoding="utf-8") as handle:
            labels = json.load(handle)
    drift_far = 0
    records = []
    assignments = []
    for index, paper in enumerate(papers):
        similarity = float(best_similarity[index])
        cluster = order[int(best[index])] if similarity >= tau_assign else -1
        if similarity < tau_drift:
            drift_far += 1
        record = {
            **paper,
            "source": "arxiv_new",
            "source_tier": "preprint",
            "cluster": cluster,
            "assign_cos": round(similarity, 3),
            "keyword": [paper["primary_category"]],
            "bibcode": None,
        }
        records.append(record)
        labels[paper["arxiv_id"]] = cluster
        assignments.append(cluster)
    commit_batch(vectors, records, labels)

    assigned_count = sum(cluster != -1 for cluster in assignments)
    print(
        f"ingested {len(papers)} new papers | assigned {assigned_count} | "
        f"noise/novel {len(papers) - assigned_count} | drift-far {drift_far}"
    )
    print("sample assignments (paper -> cluster [keywords] cos):")
    for index, paper in enumerate(papers[:6]):
        cluster = assignments[index]
        print(
            f"  {paper['arxiv_id']} {paper['primary_category']:12s} -> C{cluster} "
            f"[{keywords.get(cluster, 'novel/noise')[:46]}]  "
            f"cos={best_similarity[index]:.3f}"
        )
        print(f"     '{paper['title'][:80]}'")
    result = {
        "status": "finished",
        "ingested": len(papers),
        "assigned": assigned_count,
        "novel_or_noise": len(papers) - assigned_count,
        "drift_far": drift_far,
    }
    print(json.dumps(result, sort_keys=True))
    return result


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("n", type=int, nargs="?", default=30)
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()
    if not 1 <= args.n <= 500:
        parser.error("n must be between 1 and 500")
    with pipeline_lock():
        run(args.n, dry_run=args.dry_run)


if __name__ == "__main__":
    main()
