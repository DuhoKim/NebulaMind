#!/usr/bin/env python3
"""Isolated NebulaMind arXiv frontier preview runner.

All writes are constrained to the approved run root. Canonical corpus, database,
frontend, public, scheduler, deployment, and Git state are read-only.
"""

from __future__ import annotations

import argparse
import datetime as dt
import hashlib
import html
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path
from urllib.error import HTTPError, URLError

import numpy as np

_VERSION_RE = re.compile(r"^(.*?)(v\d+)$", re.IGNORECASE)
ATOM = "{http://www.w3.org/2005/Atom}"
ARXIV = "{http://arxiv.org/schemas/atom}"


def canonical_arxiv_id(raw: str | None) -> tuple[str, str]:
    """Return ``(base_id, observed_version)`` for an arXiv identifier."""
    value = (raw or "").strip()
    value = re.sub(r"^https?://(?:export\.)?arxiv\.org/(?:abs|pdf)/", "", value, flags=re.I)
    value = re.sub(r"^oai:arXiv\.org:", "", value, flags=re.I)
    value = re.sub(r"^arXiv:", "", value, flags=re.I)
    value = value.removesuffix(".pdf").strip()
    match = _VERSION_RE.match(value)
    base = match.group(1) if match else value
    return base, value


def load_base_arxiv_ids(path: Path) -> set[str]:
    """Read normalized arXiv identities from the base ADS JSONL corpus."""
    identities: set[str] = set()
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            if not line.strip():
                continue
            row = json.loads(line)
            for identifier in row.get("identifier") or []:
                if re.match(r"^arXiv:", str(identifier), re.I):
                    base, _ = canonical_arxiv_id(str(identifier))
                    if base:
                        identities.add(base)
    return identities


def classify_candidate(
    paper: dict,
    base_ids: set[str],
    delta_versions: dict[str, str],
    seen_fetch: set[str],
    today: dt.date,
) -> str:
    """Return one closed-vocabulary disposition for a normalized paper."""
    base_id = str(paper.get("arxiv_id") or "").strip()
    observed = str(paper.get("observed_version") or base_id).strip()
    if not base_id or not observed:
        return "quarantine_bad_identity"

    title = " ".join(str(paper.get("title") or "").lower().split())
    abstract = " ".join(str(paper.get("abstract") or "").split())
    lowered = f"{title} {abstract.lower()}"
    if "withdrawn" in lowered:
        return "quarantine_withdrawn"
    if "retracted" in lowered or "retraction" in lowered:
        return "quarantine_retracted"

    try:
        published = dt.date.fromisoformat(str(paper.get("published") or "")[:10])
    except ValueError:
        return "quarantine_bad_date"
    if published > today:
        return "quarantine_bad_date"
    if not abstract:
        return "quarantine_missing_abstract"
    if len(abstract.split()) < 40:
        return "quarantine_short_abstract"
    if not set(paper.get("categories") or []).intersection({"astro-ph.GA", "astro-ph.CO"}):
        return "quarantine_out_of_scope"

    if base_id in seen_fetch:
        return "duplicate_fetch"
    if base_id in delta_versions:
        return (
            "duplicate_delta"
            if delta_versions[base_id] == observed
            else "version_update_only"
        )
    if base_id in base_ids:
        return "duplicate_base"
    return "accepted_new"


def _clean_text(value: str | None) -> str:
    value = html.unescape(value or "")
    value = re.sub(r"<[^>]+>", " ", value)
    return re.sub(r"\s+", " ", value).strip()


def parse_atom_page(payload: bytes) -> list[dict]:
    """Parse one arXiv Atom page into normalized provenance-rich rows."""
    root = ET.fromstring(payload)
    rows: list[dict] = []
    for entry in root.findall(f"{ATOM}entry"):
        identifier = entry.findtext(f"{ATOM}id") or ""
        base_id, observed = canonical_arxiv_id(identifier)
        primary = entry.find(f"{ARXIV}primary_category")
        categories = [
            str(element.get("term"))
            for element in entry.findall(f"{ATOM}category")
            if element.get("term")
        ]
        authors = [
            _clean_text(author.findtext(f"{ATOM}name"))
            for author in entry.findall(f"{ATOM}author")
            if _clean_text(author.findtext(f"{ATOM}name"))
        ]
        published = entry.findtext(f"{ATOM}published") or ""
        rows.append(
            {
                "arxiv_id": base_id,
                "observed_version": observed,
                "title": _clean_text(entry.findtext(f"{ATOM}title")),
                "abstract": _clean_text(entry.findtext(f"{ATOM}summary")),
                "authors": authors,
                "published": published[:10],
                "updated": (entry.findtext(f"{ATOM}updated") or "")[:10],
                "primary_category": primary.get("term") if primary is not None else "",
                "categories": categories,
                "url": f"https://arxiv.org/abs/{observed or base_id}",
            }
        )
    return rows


def request_bytes_with_retries(
    url: str,
    *,
    opener=urllib.request.urlopen,
    sleeper=time.sleep,
    timeout: int = 60,
    attempts: int = 3,
) -> tuple[bytes, list[dict]]:
    """Fetch bytes with bounded rate-limit/transient retries and a receipt ledger."""
    ledger: list[dict] = []
    backoff = (10.0, 30.0, 90.0)
    request = urllib.request.Request(url, headers={"User-Agent": "NebulaMind-preview/1"})
    for index in range(attempts):
        started = time.monotonic()
        try:
            response = opener(request, timeout=timeout)
            body = response.read()
            ledger.append(
                {
                    "attempt": index + 1,
                    "status": int(getattr(response, "status", 200) or 200),
                    "elapsed_seconds": round(time.monotonic() - started, 3),
                    "bytes": len(body),
                }
            )
            return body, ledger
        except HTTPError as exc:
            ledger.append(
                {
                    "attempt": index + 1,
                    "status": exc.code,
                    "elapsed_seconds": round(time.monotonic() - started, 3),
                }
            )
            retryable = exc.code == 429 or 500 <= exc.code < 600
            if not retryable or index + 1 >= attempts:
                raise
            retry_after = exc.headers.get("Retry-After") if exc.headers else None
            delay = float(retry_after) if retry_after else backoff[index]
            sleeper(delay)
        except (TimeoutError, URLError) as exc:
            ledger.append(
                {
                    "attempt": index + 1,
                    "status": "timeout_or_url_error",
                    "error": type(exc).__name__,
                    "elapsed_seconds": round(time.monotonic() - started, 3),
                }
            )
            if index + 1 >= attempts:
                raise
            sleeper(backoff[index])
    raise RuntimeError("unreachable retry state")


def reached_date_boundary(papers: list[dict], boundary: dt.date) -> bool:
    """True when a descending page reaches or crosses the overlap date."""
    dates = []
    for paper in papers:
        try:
            dates.append(dt.date.fromisoformat(str(paper.get("published") or "")[:10]))
        except ValueError:
            continue
    return bool(dates) and min(dates) <= boundary


def _atomic_bytes(path: Path, payload: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    temporary.write_bytes(payload)
    os.replace(temporary, path)


def build_shadow_delta(
    source_delta: Path,
    shadow_delta: Path,
    new_records: list[dict],
    new_vectors: np.ndarray,
    *,
    dim: int,
) -> dict:
    """Copy and transactionally extend a delta store without touching its source."""
    vectors = np.asarray(new_vectors, dtype=np.float32)
    if vectors.shape != (len(new_records), dim):
        raise ValueError(
            f"embedding shape {vectors.shape} != ({len(new_records)}, {dim})"
        )
    if vectors.size and (not np.isfinite(vectors).all() or np.any(np.linalg.norm(vectors, axis=1) == 0)):
        raise ValueError("embeddings must be finite and nonzero")

    source_papers = source_delta / "new_papers.jsonl"
    source_labels = source_delta / "new_labels.json"
    source_embeddings = source_delta / "new_emb.f32"
    historical_lines = [
        line
        for line in source_papers.read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    historical = [json.loads(line) for line in historical_lines]
    before = len(historical)
    expected_before_bytes = before * dim * 4
    if source_embeddings.stat().st_size != expected_before_bytes:
        raise ValueError("source embedding byte count is not aligned")
    labels = json.loads(source_labels.read_text(encoding="utf-8"))
    historical_ids = [str(row.get("arxiv_id") or "") for row in historical]
    if len(historical_ids) != len(set(historical_ids)) or set(labels) != set(historical_ids):
        raise ValueError("source paper and label IDs are not uniquely aligned")
    new_ids = [str(row.get("arxiv_id") or "") for row in new_records]
    if any(not value for value in new_ids) or len(new_ids) != len(set(new_ids)):
        raise ValueError("new paper IDs must be present and unique")
    if set(new_ids).intersection(historical_ids):
        raise ValueError("new paper IDs overlap the historical delta")

    shadow_delta.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(source_papers, shadow_delta / "new_papers.jsonl")
    shutil.copyfile(source_labels, shadow_delta / "new_labels.json")
    shutil.copyfile(source_embeddings, shadow_delta / "new_emb.f32")
    with (shadow_delta / "new_papers.jsonl").open("a", encoding="utf-8") as handle:
        for record in new_records:
            handle.write(json.dumps(record, sort_keys=True) + "\n")
    with (shadow_delta / "new_emb.f32").open("ab") as handle:
        handle.write(np.ascontiguousarray(vectors, dtype=np.float32).tobytes())
    for record in new_records:
        labels[str(record["arxiv_id"])] = int(record.get("cluster", -1))
    _atomic_bytes(
        shadow_delta / "new_labels.json",
        (json.dumps(labels, sort_keys=True) + "\n").encode("utf-8"),
    )

    after_lines = [
        line
        for line in (shadow_delta / "new_papers.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    after_ids = [str(json.loads(line)["arxiv_id"]) for line in after_lines]
    final_labels = json.loads((shadow_delta / "new_labels.json").read_text(encoding="utf-8"))
    embedding_bytes = (shadow_delta / "new_emb.f32").stat().st_size
    if set(after_ids) != set(final_labels) or embedding_bytes != len(after_ids) * dim * 4:
        raise ValueError("shadow paper, label, and embedding stores are misaligned")
    return {
        "before": before,
        "added": len(new_records),
        "after": len(after_ids),
        "embedding_bytes": embedding_bytes,
    }


def ensure_within_run(run_root: Path, candidate: Path) -> Path:
    """Resolve a write target and reject anything outside the approved run root."""
    root = run_root.resolve()
    resolved = candidate.resolve()
    if resolved != root and root not in resolved.parents:
        raise ValueError(f"output is outside approved run root: {resolved}")
    return resolved


def _tractable_ranks(document: dict) -> dict[int, int]:
    rows = sorted(
        (row for row in document.get("clusters", []) if int(row.get("tractable", 0)) == 1),
        key=lambda row: (-float(row.get("score_v1", 0.0)), int(row["cluster"])),
    )
    return {int(row["cluster"]): index + 1 for index, row in enumerate(rows)}


def validate_and_explain_rerank(
    previous: dict,
    current: dict,
    new_records: list[dict],
) -> dict:
    """Validate frozen ranking semantics and explain every current tractable row."""
    if current.get("constants_frozen") is not True:
        raise ValueError("rerank did not declare frozen constants")
    if current.get("v1_constants") != previous.get("v1_constants"):
        raise ValueError("frozen v1 constants changed")
    previous_rows = {int(row["cluster"]): row for row in previous.get("clusters", [])}
    current_rows = {int(row["cluster"]): row for row in current.get("clusters", [])}
    previous_ranks = _tractable_ranks(previous)
    current_ranks = _tractable_ranks(current)
    if len(current_ranks.values()) != len(set(current_ranks.values())):
        raise ValueError("current ranks are not unique")
    new_by_cluster: dict[int, list[str]] = {}
    for record in new_records:
        cluster = int(record.get("cluster", -1))
        if cluster != -1:
            new_by_cluster.setdefault(cluster, []).append(str(record["arxiv_id"]))
    metric_names = (
        "size",
        "strict_tension",
        "recent_frac",
        "ga_frac",
        "co_frac",
        "sat_activity",
        "tension_norm",
        "growth_norm",
        "tractable",
        "score_v1",
    )
    explanations = []
    review_holds = []
    for cluster, current_rank in sorted(current_ranks.items(), key=lambda item: item[1]):
        current_row = current_rows[cluster]
        previous_row = previous_rows.get(cluster, {})
        previous_rank = previous_ranks.get(cluster, current_rank)
        rank_delta = previous_rank - current_rank
        row = {
            "cluster": cluster,
            "previous_rank": previous_rank,
            "current_rank": current_rank,
            "rank_delta": rank_delta,
            "new_paper_ids": sorted(new_by_cluster.get(cluster, [])),
            "metrics": {
                name: {
                    "before": previous_row.get(name),
                    "after": current_row.get(name),
                }
                for name in metric_names
            },
        }
        explanations.append(row)
        if abs(rank_delta) >= 3:
            review_holds.append({"type": "rank_move_ge_3", "cluster": cluster, "delta": rank_delta})
        if previous_row and previous_row.get("tractable") != current_row.get("tractable"):
            review_holds.append({"type": "tractability_flip", "cluster": cluster})
    return {"explanations": explanations, "review_holds": review_holds}


def assign_records(
    papers: list[dict],
    vectors: np.ndarray,
    centroids: np.ndarray,
    centroid_metadata: dict,
) -> tuple[list[dict], dict]:
    """Assign normalized vectors to frozen centroids without forcing novel rows."""
    vectors = np.asarray(vectors, dtype=np.float32)
    centroids = np.asarray(centroids, dtype=np.float32)
    if vectors.ndim != 2 or centroids.ndim != 2 or vectors.shape[0] != len(papers):
        raise ValueError("paper/vector/centroid shapes are inconsistent")
    if vectors.shape[1] != centroids.shape[1]:
        raise ValueError("vector and centroid dimensions differ")
    normalized = vectors / (np.linalg.norm(vectors, axis=1, keepdims=True) + 1e-9)
    similarities = normalized @ centroids.T
    best_indices = similarities.argmax(axis=1)
    best_values = similarities.max(axis=1)
    order = list(centroid_metadata["order"])
    tau_assign = float(centroid_metadata["tau_assign"])
    tau_drift = float(centroid_metadata["tau_drift"])
    records = []
    review_queue = []
    assigned = 0
    drift_count = 0
    for index, paper in enumerate(papers):
        similarity = float(best_values[index])
        cluster = int(order[int(best_indices[index])]) if similarity >= tau_assign else -1
        drift_far = similarity < tau_drift
        if cluster != -1:
            assigned += 1
        if drift_far:
            drift_count += 1
        record = {
            "arxiv_id": str(paper["arxiv_id"]),
            "version": str(paper.get("observed_version") or paper["arxiv_id"]),
            "title": str(paper.get("title") or ""),
            "abstract": str(paper.get("abstract") or ""),
            "authors": list(paper.get("authors") or []),
            "primary_category": str(paper.get("primary_category") or ""),
            "categories": list(paper.get("categories") or []),
            "submitted": str(paper.get("published") or "")[:10],
            "updated": str(paper.get("updated") or "")[:10],
            "year": int(str(paper.get("published") or "")[:4]),
            "url": str(paper.get("url") or ""),
            "source": "arxiv_new",
            "source_tier": "preprint",
            "cluster": cluster,
            "assign_cos": round(similarity, 6),
            "drift_far": drift_far,
            "keyword": [str(paper.get("primary_category") or "")],
            "bibcode": None,
        }
        records.append(record)
        reasons = []
        if abs(similarity - tau_assign) <= 0.02:
            reasons.append("near_assign_threshold")
        if record["primary_category"] not in {"astro-ph.GA", "astro-ph.CO"}:
            reasons.append("cross_list_primary_outside_ga_co")
        if drift_far:
            reasons.append("drift_far")
        if reasons:
            review_queue.append(
                {
                    "arxiv_id": record["arxiv_id"],
                    "cluster": cluster,
                    "assign_cos": record["assign_cos"],
                    "reasons": reasons,
                }
            )
    report = {
        "papers": len(records),
        "assigned": assigned,
        "novel_or_noise": len(records) - assigned,
        "drift_far": drift_count,
        "tau_assign": tau_assign,
        "tau_drift": tau_drift,
        "review_queue": review_queue,
    }
    return records, report


def verify_protected_hashes(input_lock: dict) -> list[dict]:
    """Return every missing, resized, or rehashed protected file."""
    mismatches = []
    for raw_path, expected in input_lock.get("protected_files", {}).items():
        path = Path(raw_path)
        actual = {
            "exists": path.is_file(),
            "bytes": path.stat().st_size if path.is_file() else None,
            "sha256": hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None,
        }
        if not actual["exists"] or actual["bytes"] != expected.get("bytes") or actual["sha256"] != expected.get("sha256"):
            mismatches.append({"path": raw_path, "expected": expected, "actual": actual})
    return mismatches


def _utc_now() -> dt.datetime:
    return dt.datetime.now(dt.timezone.utc)


def _sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _write_json(run_root: Path, path: Path, payload) -> None:
    target = ensure_within_run(run_root, path)
    _atomic_bytes(target, (json.dumps(payload, indent=2, sort_keys=True, default=str) + "\n").encode("utf-8"))


def _write_jsonl(run_root: Path, path: Path, rows: list[dict]) -> None:
    target = ensure_within_run(run_root, path)
    data = "".join(json.dumps(row, sort_keys=True, default=str) + "\n" for row in rows)
    _atomic_bytes(target, data.encode("utf-8"))


def _update_state(run_root: Path, phase: str, *, status: str = "running", details: dict | None = None) -> None:
    path = ensure_within_run(run_root, run_root / "STATE.json")
    state = json.loads(path.read_text(encoding="utf-8"))
    completed = list(state.get("completed_phases") or [])
    if phase not in completed:
        completed.append(phase)
    state.update(
        {
            "phase": phase,
            "status": status,
            "updated_at_utc": _utc_now().isoformat(),
            "completed_phases": completed,
        }
    )
    if details is not None:
        state.setdefault("details", {})[phase] = details
    _write_json(run_root, path, state)


def _check_deadline(deadline: dt.datetime) -> None:
    if _utc_now() >= deadline:
        raise RuntimeError(f"hard stop reached: {deadline.isoformat()}")


def acquire_arxiv_window(
    run_root: Path,
    *,
    boundary: dt.date,
    page_size: int,
    max_results: int,
    min_interval: float,
    deadline: dt.datetime,
) -> dict:
    """Fetch and immutably cache newest-first GA/CO pages through the boundary."""
    raw_dir = ensure_within_run(run_root, run_root / "raw/arxiv")
    raw_dir.mkdir(parents=True, exist_ok=True)
    request_ledger: list[dict] = []
    in_window: list[dict] = []
    raw_entry_count = 0
    reached = False
    last_request_finished: float | None = None
    page_count = (max_results + page_size - 1) // page_size
    for page_index in range(page_count):
        _check_deadline(deadline)
        start = page_index * page_size
        limit = min(page_size, max_results - start)
        params = urllib.parse.urlencode(
            {
                "search_query": "cat:astro-ph.GA OR cat:astro-ph.CO",
                "start": start,
                "max_results": limit,
                "sortBy": "submittedDate",
                "sortOrder": "descending",
            }
        )
        url = f"https://export.arxiv.org/api/query?{params}"
        raw_path = ensure_within_run(run_root, raw_dir / f"page_{page_index:03d}.xml")
        if raw_path.exists():
            body = raw_path.read_bytes()
            attempts = [{"attempt": 0, "status": "cached", "bytes": len(body)}]
        else:
            if last_request_finished is not None:
                wait = min_interval - (time.monotonic() - last_request_finished)
                if wait > 0:
                    time.sleep(wait)
            body, attempts = request_bytes_with_retries(url)
            _atomic_bytes(raw_path, body)
            last_request_finished = time.monotonic()
        response_sha = hashlib.sha256(body).hexdigest()
        fetched_at = _utc_now().isoformat()
        for attempt in attempts:
            request_ledger.append(
                {
                    **attempt,
                    "page": page_index,
                    "start": start,
                    "max_results": limit,
                    "url": url,
                    "fetched_at_utc": fetched_at,
                    "response_sha256": response_sha if attempt.get("status") in {200, "cached"} else None,
                }
            )
        rows = parse_atom_page(body)
        if not rows:
            raise RuntimeError(f"arXiv page {page_index} was empty before reaching boundary")
        raw_entry_count += len(rows)
        for row in rows:
            try:
                published = dt.date.fromisoformat(row["published"])
            except ValueError:
                in_window.append(row)
                continue
            if published >= boundary:
                in_window.append(row)
        if reached_date_boundary(rows, boundary):
            reached = True
            break
    _write_jsonl(run_root, run_root / "raw/arxiv/request_ledger.jsonl", request_ledger)
    _write_jsonl(run_root, run_root / "staged/candidates_raw.jsonl", in_window)
    summary = {
        "status": "finished" if reached else "NEEDS_WIDER_CATCHUP",
        "boundary": boundary.isoformat(),
        "raw_entry_count": raw_entry_count,
        "in_window_count": len(in_window),
        "pages": len({row["page"] for row in request_ledger}),
        "reached_boundary": reached,
        "max_results": max_results,
    }
    _write_json(run_root, run_root / "raw/arxiv/acquisition_summary.json", summary)
    return {"papers": in_window, "summary": summary}


def gate_candidates(run_root: Path, engine: Path, papers: list[dict], boundary: dt.date) -> dict:
    """Apply identity, version, scientific-row, and duplicate gates."""
    base_ids = load_base_arxiv_ids(engine / "corpus_ga_co_2009_2026.jsonl")
    delta_rows = [
        json.loads(line)
        for line in (engine / "delta/new_papers.jsonl").read_text(encoding="utf-8").splitlines()
        if line.strip()
    ]
    delta_versions = {
        str(row["arxiv_id"]): str(row.get("version") or row["arxiv_id"])
        for row in delta_rows
    }
    today = (_utc_now() + dt.timedelta(hours=9)).date()
    seen_fetch: set[str] = set()
    accepted: list[dict] = []
    quarantined: list[dict] = []
    versions: list[dict] = []
    duplicates: list[dict] = []
    counts: Counter = Counter()
    for paper in papers:
        reason = classify_candidate(paper, base_ids, delta_versions, seen_fetch, today)
        counts[reason] += 1
        routed = {**paper, "disposition": reason}
        if reason == "accepted_new":
            accepted.append(paper)
        elif reason.startswith("quarantine_"):
            quarantined.append(routed)
        elif reason == "version_update_only":
            versions.append(routed)
        else:
            duplicates.append(routed)
        if paper.get("arxiv_id"):
            seen_fetch.add(str(paper["arxiv_id"]))
    if sum(counts.values()) != len(papers):
        raise RuntimeError("candidate disposition accounting mismatch")
    accepted_ids = [row["arxiv_id"] for row in accepted]
    if len(accepted_ids) != len(set(accepted_ids)) or set(accepted_ids).intersection(base_ids) or set(accepted_ids).intersection(delta_versions):
        raise RuntimeError("accepted candidates are not uniquely absent from the corpus")
    _write_jsonl(run_root, run_root / "staged/candidates_dedup.jsonl", accepted)
    _write_jsonl(run_root, run_root / "staged/quarantine.jsonl", quarantined)
    _write_jsonl(run_root, run_root / "staged/version_updates.jsonl", versions)
    _write_jsonl(run_root, run_root / "staged/duplicates.jsonl", duplicates)
    report = {
        "fetched_in_window": len(papers),
        "accepted": len(accepted),
        "duplicates": len(duplicates),
        "version_updates": len(versions),
        "quarantined": len(quarantined),
        "dispositions": dict(sorted(counts.items())),
        "boundary": boundary.isoformat(),
        "accepted_submission_from": min((row["published"] for row in accepted), default=None),
        "accepted_submission_to": max((row["published"] for row in accepted), default=None),
        "primary_categories": dict(sorted(Counter(row.get("primary_category") for row in accepted).items())),
        "accepted_ids": accepted_ids,
        "accounting_balanced": len(papers) == len(accepted) + len(duplicates) + len(versions) + len(quarantined),
    }
    _write_json(run_root, run_root / "staged/dedup_report.json", report)
    _write_json(run_root, run_root / "staged/gate_report.json", {**report, "gate": "PASS"})
    return {"accepted": accepted, "report": report}


def embed_candidates(
    run_root: Path,
    papers: list[dict],
    *,
    model: str,
    dim: int,
    deadline: dt.datetime,
) -> np.ndarray:
    """Embed accepted rows locally and atomically persist only the complete matrix."""
    vectors = []
    for index, paper in enumerate(papers):
        _check_deadline(deadline)
        body = json.dumps(
            {"model": model, "input": [f"{paper['title']}. {paper['abstract']}"[:4000]]}
        ).encode("utf-8")
        request = urllib.request.Request(
            "http://localhost:11434/api/embed",
            data=body,
            headers={"Content-Type": "application/json"},
        )
        last_error = None
        for attempt in range(3):
            try:
                with urllib.request.urlopen(request, timeout=120) as response:
                    vector = np.asarray(json.load(response)["embeddings"][0], dtype=np.float32)
                if vector.shape != (dim,) or not np.isfinite(vector).all() or float(np.linalg.norm(vector)) == 0:
                    raise ValueError(f"invalid embedding at row {index}: {vector.shape}")
                vectors.append(vector)
                last_error = None
                break
            except Exception as exc:
                last_error = exc
                if attempt < 2:
                    time.sleep(2 ** attempt)
        if last_error is not None:
            raise RuntimeError(f"embedding failed for {paper['arxiv_id']}: {last_error}") from last_error
    matrix = np.vstack(vectors).astype(np.float32) if vectors else np.empty((0, dim), dtype=np.float32)
    _atomic_bytes(run_root / "staged/new_emb.f32", matrix.tobytes())
    _write_json(
        run_root,
        run_root / "staged/embedding_report.json",
        {"papers": len(papers), "model": model, "dim": dim, "bytes": matrix.nbytes},
    )
    return matrix


def prepare_and_rerank_shadow(
    run_root: Path,
    engine: Path,
    records: list[dict],
    vectors: np.ndarray,
) -> dict:
    """Build the shadow engine and run existing frozen-constant ranking scripts there."""
    shadow = ensure_within_run(run_root, run_root / "shadow_engine")
    shadow.mkdir(parents=True, exist_ok=True)
    for name in (
        "frontier_map_v3.json",
        "frontier_map_v3_reranked.json",
        "rerank_incremental.py",
        "gen_frontiers_data.py",
    ):
        shutil.copyfile(engine / name, shadow / name)
    if (engine / "cluster_names.json").is_file():
        shutil.copyfile(engine / "cluster_names.json", shadow / "cluster_names.json")
    previous = json.loads((engine / "frontier_map_v3_reranked.json").read_text(encoding="utf-8"))
    delta_summary = build_shadow_delta(engine / "delta", shadow / "delta", records, vectors, dim=2560)
    rerank = subprocess.run(
        [sys.executable, str(shadow / "rerank_incremental.py")],
        cwd=shadow,
        text=True,
        capture_output=True,
        timeout=300,
        check=False,
    )
    _atomic_bytes(run_root / "validation/rerank.stdout.log", rerank.stdout.encode("utf-8"))
    _atomic_bytes(run_root / "validation/rerank.stderr.log", rerank.stderr.encode("utf-8"))
    if rerank.returncode != 0:
        raise RuntimeError(f"shadow rerank failed: {(rerank.stderr or rerank.stdout)[-2000:]}")
    current_path = shadow / "frontier_map_v3_reranked.json"
    current = json.loads(current_path.read_text(encoding="utf-8"))
    explanation = validate_and_explain_rerank(previous, current, records)
    preview_map = shadow / "frontier_map_v3_reranked.preview.json"
    shutil.copyfile(current_path, preview_map)
    generator = subprocess.run(
        [sys.executable, str(shadow / "gen_frontiers_data.py")],
        cwd=shadow,
        text=True,
        capture_output=True,
        timeout=300,
        check=False,
    )
    _atomic_bytes(run_root / "validation/generator.stdout.log", generator.stdout.encode("utf-8"))
    _atomic_bytes(run_root / "validation/generator.stderr.log", generator.stderr.encode("utf-8"))
    if generator.returncode != 0:
        raise RuntimeError(f"shadow generator failed: {(generator.stderr or generator.stdout)[-2000:]}")
    staging = shadow / "frontiersData.v3.staging.ts"
    preview_ts = shadow / "frontiersData.v3.preview.ts"
    shutil.copyfile(staging, preview_ts)
    markers = ("FRONTIER_RANKING_UPDATE", "FRONTIER_RANK_MOVEMENT", "FRONTIERS")
    source = preview_ts.read_text(encoding="utf-8")
    if not all(marker in source for marker in markers):
        raise RuntimeError("preview TypeScript is missing ranking exports")
    _write_json(run_root, run_root / "ranking/rank_movements.json", current.get("rank_movements") or {})
    _write_json(run_root, run_root / "ranking/rank_explanations.json", explanation)
    recommendations = {
        "advisory_only": True,
        "automatic_curated_topic_change": False,
        "review_holds": explanation["review_holds"],
        "top_movers": sorted(
            explanation["explanations"], key=lambda row: abs(row["rank_delta"]), reverse=True
        )[:12],
    }
    _write_json(run_root, run_root / "ranking/curated_topic_recommendations.json", recommendations)
    return {
        "delta": delta_summary,
        "comparison": current.get("rank_comparison") or {},
        "rank_explanations": explanation,
        "preview_map": str(preview_map),
        "preview_map_sha256": _sha256(preview_map),
        "preview_ts": str(preview_ts),
        "preview_ts_sha256": _sha256(preview_ts),
        "rerank_stdout_tail": rerank.stdout[-2000:],
        "generator_stdout_tail": generator.stdout[-2000:],
    }


def finalize_run(
    run_root: Path,
    input_lock: dict,
    *,
    acquisition: dict,
    gate: dict,
    assignment: dict,
    ranking: dict,
    verdict: str,
) -> dict:
    """Validate isolation, create checksums/manifest, and write the morning handoff."""
    protected_mismatches = verify_protected_hashes(input_lock)
    repo = Path(input_lock["repo_root"])
    git_status = subprocess.run(
        ["git", "status", "--porcelain=v1"], cwd=repo, text=True, capture_output=True, check=True
    ).stdout.splitlines()
    git_unchanged = git_status == input_lock.get("git_status_lines")
    review_holds = list(ranking.get("rank_explanations", {}).get("review_holds", []))
    accepted = int(gate.get("accepted", 0))
    if accepted:
        assigned_fraction = assignment["assigned"] / accepted
        novel_fraction = assignment["novel_or_noise"] / accepted
        drift_fraction = assignment["drift_far"] / accepted
        if assigned_fraction < 0.70:
            review_holds.append({"type": "assigned_fraction_below_70pct", "value": assigned_fraction})
        if novel_fraction > 0.25:
            review_holds.append({"type": "novel_fraction_above_25pct", "value": novel_fraction})
        if drift_fraction > 0.10:
            review_holds.append({"type": "drift_fraction_above_10pct", "value": drift_fraction})
        if accepted > 300:
            review_holds.append({"type": "accepted_cohort_above_300", "value": accepted})
    preview_ts = Path(ranking["preview_ts"])
    preview_markers_ok = all(
        marker in preview_ts.read_text(encoding="utf-8")
        for marker in ("FRONTIER_RANKING_UPDATE", "FRONTIER_RANK_MOVEMENT", "FRONTIERS")
    )
    safety_ledger = {
        "db_sql_writes": 0,
        "canonical_local_delta_writes": 0,
        "live_staging_frontend_writes": 0,
        "wiki_evidence_trust_writes": 0,
        "public_cockpit_writes": 0,
        "deploy_restart_actions": 0,
        "scheduler_cron_launchagent_writes": 0,
        "git_writes": 0,
        "external_submissions": 0,
    }
    validation = {
        "verdict": verdict,
        "protected_mismatches": protected_mismatches,
        "protected_files_unchanged": not protected_mismatches,
        "git_status_unchanged": git_unchanged,
        "preview_markers_ok": preview_markers_ok,
        "review_holds": review_holds,
        "safety_ledger": safety_ledger,
        "all_hard_checks_pass": not protected_mismatches and git_unchanged and preview_markers_ok,
    }
    if not validation["all_hard_checks_pass"]:
        raise RuntimeError(f"final isolation validation failed: {validation}")
    _write_json(run_root, run_root / "validation/validation_report.json", validation)
    _update_state(run_root, "complete", status="finished", details={"verdict": verdict})

    excluded = {"MANIFEST.json", "MORNING_HANDOFF.md", "validation/SHA256SUMS.txt"}
    artifact_rows = []
    for path in sorted(p for p in run_root.rglob("*") if p.is_file()):
        relative = str(path.relative_to(run_root))
        if relative in excluded:
            continue
        artifact_rows.append({"path": relative, "bytes": path.stat().st_size, "sha256": _sha256(path)})
    sums = "".join(f"{row['sha256']}  {row['path']}\n" for row in artifact_rows)
    _atomic_bytes(run_root / "validation/SHA256SUMS.txt", sums.encode("utf-8"))
    manifest = {
        "schema_version": 1,
        "run_id": run_root.name,
        "verdict": verdict,
        "created_at_utc": _utc_now().isoformat(),
        "input_lock_sha256": _sha256(run_root / "INPUT_LOCK.json"),
        "validation_sums_sha256": _sha256(run_root / "validation/SHA256SUMS.txt"),
        "artifacts": artifact_rows,
        "acquisition": acquisition,
        "gate": gate,
        "assignment": assignment,
        "ranking": {
            key: value
            for key, value in ranking.items()
            if key not in {"rank_explanations", "rerank_stdout_tail", "generator_stdout_tail"}
        },
        "review_holds": review_holds,
        "safety_ledger": safety_ledger,
        "promotion": {"attempted": False, "authorized": False},
    }
    _write_json(run_root, run_root / "MANIFEST.json", manifest)
    manifest_sha = _sha256(run_root / "MANIFEST.json")
    movers = sorted(
        ranking["rank_explanations"]["explanations"],
        key=lambda row: abs(row["rank_delta"]),
        reverse=True,
    )[:8]
    mover_lines = "\n".join(
        f"- C{row['cluster']}: rank {row['previous_rank']} → {row['current_rank']} "
        f"(Δ {row['rank_delta']:+d}); {len(row['new_paper_ids'])} newly assigned"
        for row in movers
    ) or "- No rank movement."
    disposition_lines = "\n".join(
        f"- {name}: {count}" for name, count in sorted(gate.get("dispositions", {}).items())
    )
    handoff = f"""# NebulaMind overnight arXiv frontier preview — morning handoff

**Verdict:** `{verdict}`  
**Run ID:** `{run_root.name}`  
**Manifest SHA-256:** `{manifest_sha}`  
**Canonical promotion:** NOT ATTEMPTED / NOT AUTHORIZED

## Acquisition

- Boundary overlap: {acquisition.get('boundary')}
- Cached/fetched pages: {acquisition.get('pages')}
- Raw Atom entries: {acquisition.get('raw_entry_count')}
- In-window candidates: {acquisition.get('in_window_count')}

## Corpus gate

- Accepted new: {gate.get('accepted')}
- Duplicates: {gate.get('duplicates')}
- Version updates held: {gate.get('version_updates')}
- Quarantined: {gate.get('quarantined')}

{disposition_lines}

## Assignment

- Assigned: {assignment.get('assigned')}
- Novel/noise: {assignment.get('novel_or_noise')}
- Drift-far: {assignment.get('drift_far')}
- Review queue: {len(assignment.get('review_queue') or [])}

## Topic-rank preview

{mover_lines}

- Preview map: `{ranking.get('preview_map')}`
- Preview map SHA-256: `{ranking.get('preview_map_sha256')}`
- Preview TypeScript: `{ranking.get('preview_ts')}`
- Preview TypeScript SHA-256: `{ranking.get('preview_ts_sha256')}`
- Curated `RANK_TOPICS`: unchanged; recommendations are advisory only.
- DR + Quartet paper-merit leaderboard: unchanged.

## Review holds

```json
{json.dumps(review_holds, indent=2, sort_keys=True)}
```

## Safety ledger

```json
{json.dumps(safety_ledger, indent=2, sort_keys=True)}
```

## Next gate

To promote the local shadow delta only after review:

`PROMOTE LOCAL FRONTIER DELTA {run_root.name} {manifest_sha}`

This does not authorize DB, frontend, public, deploy, scheduler, or Git changes.
"""
    _atomic_bytes(run_root / "MORNING_HANDOFF.md", handoff.encode("utf-8"))
    return {
        "verdict": verdict,
        "run_id": run_root.name,
        "run_root": str(run_root),
        "manifest": str(run_root / "MANIFEST.json"),
        "manifest_sha256": manifest_sha,
        "handoff": str(run_root / "MORNING_HANDOFF.md"),
        "handoff_sha256": _sha256(run_root / "MORNING_HANDOFF.md"),
        "review_holds": review_holds,
        "safety_ledger": safety_ledger,
    }


def run_preview(args: argparse.Namespace) -> dict:
    run_root = Path(args.run_root).resolve()
    engine = Path(args.engine).resolve()
    ensure_within_run(run_root, run_root)
    if not args.execute_preview:
        raise RuntimeError("preview execution requires --execute-preview")
    input_lock = json.loads((run_root / "INPUT_LOCK.json").read_text(encoding="utf-8"))
    if input_lock.get("approval_phrase") != "GO OVERNIGHT ARXIV PREVIEW":
        raise RuntimeError("input lock does not contain the approved Gate A phrase")
    if Path(input_lock["engine_root"]).resolve() != engine:
        raise RuntimeError("engine path differs from input lock")
    mismatches = verify_protected_hashes(input_lock)
    if mismatches:
        raise RuntimeError(f"protected inputs drifted before start: {mismatches}")
    deadline = dt.datetime.fromisoformat(args.deadline.replace("Z", "+00:00"))
    boundary = dt.date.fromisoformat(args.boundary)
    _update_state(run_root, "driver_tests_passed")
    acquired = acquire_arxiv_window(
        run_root,
        boundary=boundary,
        page_size=args.page_size,
        max_results=args.max_results,
        min_interval=args.min_interval,
        deadline=deadline,
    )
    _update_state(run_root, "acquisition_complete", details=acquired["summary"])
    if not acquired["summary"]["reached_boundary"]:
        raise RuntimeError("NEEDS_WIDER_CATCHUP: boundary not reached within max results")
    gated = gate_candidates(run_root, engine, acquired["papers"], boundary)
    _update_state(run_root, "corpus_gate_complete", details=gated["report"])
    if not gated["accepted"]:
        raise RuntimeError("NO_NEW_PAPERS path is not expected for this stale catch-up run")
    vectors = embed_candidates(
        run_root,
        gated["accepted"],
        model=args.model,
        dim=args.dim,
        deadline=deadline,
    )
    centroids = np.load(engine / "centroids_v2.npy")
    centroid_metadata = json.loads((engine / "centroids_meta.json").read_text(encoding="utf-8"))
    records, assignment = assign_records(gated["accepted"], vectors, centroids, centroid_metadata)
    _write_jsonl(run_root, run_root / "staged/assigned_new_papers.jsonl", records)
    _write_json(run_root, run_root / "staged/assignment_report.json", assignment)
    _write_jsonl(run_root, run_root / "staged/assignment_review_queue.jsonl", assignment["review_queue"])
    _update_state(run_root, "embedding_assignment_complete", details=assignment)
    ranking = prepare_and_rerank_shadow(run_root, engine, records, vectors)
    _update_state(run_root, "shadow_rerank_complete", details=ranking["comparison"])
    verdict = "PREVIEW_READY_FOR_REVIEW"
    return finalize_run(
        run_root,
        input_lock,
        acquisition=acquired["summary"],
        gate=gated["report"],
        assignment=assignment,
        ranking=ranking,
        verdict=verdict,
    )


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Run an isolated NebulaMind arXiv frontier preview")
    parser.add_argument("--run-root", required=True)
    parser.add_argument("--engine", required=True)
    parser.add_argument("--boundary", default="2026-07-24")
    parser.add_argument("--page-size", type=int, default=100)
    parser.add_argument("--max-results", type=int, default=500)
    parser.add_argument("--min-interval", type=float, default=3.2)
    parser.add_argument("--model", default="qwen3-embedding:4b")
    parser.add_argument("--dim", type=int, default=2560)
    parser.add_argument("--deadline", default="2026-07-31T22:30:00Z")
    parser.add_argument("--execute-preview", action="store_true")
    args = parser.parse_args(argv)
    run_root = Path(args.run_root).resolve()
    try:
        result = run_preview(args)
    except Exception as exc:
        if (run_root / "STATE.json").is_file():
            _update_state(
                run_root,
                "blocked",
                status="blocked",
                details={"error_type": type(exc).__name__, "error": str(exc)[:4000]},
            )
            _write_json(
                run_root,
                run_root / "validation/failure.json",
                {"status": "BLOCKED", "error_type": type(exc).__name__, "error": str(exc), "at_utc": _utc_now().isoformat()},
            )
        raise
    print(json.dumps(result, indent=2, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
