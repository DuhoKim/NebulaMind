#!/usr/bin/env python3
"""Gate-B GET-only source acquisition with custody logging.

Reads immutable local ledgers, writes only inside this Gate-B packet. No verdicts.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import time
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path
from urllib.parse import parse_qs, quote, unquote, urlparse

import requests
from bs4 import BeautifulSoup

try:
    import fitz
except Exception:  # pragma: no cover
    fitz = None

USER_AGENT = "NebulaMindSourceVerifier/1.0 (read-only research verification; contact: local operator)"
ARXIV_RE = re.compile(r"arxiv\.org/(?:abs|html|pdf)/(\d{4}\.\d{4,5})(?:v\d+)?", re.I)
DOI_RE = re.compile(r"\b10\.\d{4,9}/[-._;()/:A-Za-z0-9]+\b", re.I)


def utc_now() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def safe_piece(value: str, limit: int = 80) -> str:
    value = re.sub(r"[^A-Za-z0-9._-]+", "_", value).strip("._")
    return (value or "artifact")[:limit]


def json_dump(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, ensure_ascii=False) + "\n")


def unit_chips(block: dict, refs: list) -> list[int]:
    if len(refs) == 2 and isinstance(refs[1], int) and block.get("cells"):
        return [int(x) for x in block["cells"][refs[1]].get("chips", [])]
    return [int(x) for x in block.get("chips", [])]


def build_maps(master: Path, packet: Path) -> tuple[dict, dict]:
    triage = json.loads((master / "gemini-dr-c1r-contract-r3-manual-triage-20260713T024458Z/triage/TRIAGE_LEDGER.json").read_text())
    capture = json.loads((master / "gemini-dr-c1r-chip-validator-repair-20260713T010203Z/readjudication/structured_capture_v2.json").read_text())
    blocks = {b["id"]: b for b in capture["blocks"]}
    index_urls: dict[int, str] = {}
    index_rows: dict[int, list[int]] = defaultdict(list)
    for row in capture.get("ledger_entries", []):
        idx = int(row["index"])
        url = str(row.get("url", "")).strip()
        if idx in index_urls and index_urls[idx] != url:
            raise RuntimeError(f"index/url conflict {idx}: {index_urls[idx]} != {url}")
        index_urls[idx] = url
        index_rows[idx].append(int(row.get("row") or 0))

    source_index_map = {
        "schema": "NM_GATE_B_SOURCE_INDEX_MAP_V1",
        "created_utc": utc_now(),
        "source_capture_sha256": sha256((master / "gemini-dr-c1r-chip-validator-repair-20260713T010203Z/readjudication/structured_capture_v2.json").read_bytes()),
        "unique_indices": len(index_urls),
        "indices": [
            {"index": i, "url": index_urls[i], "ledger_rows": index_rows[i]}
            for i in sorted(index_urls)
        ],
    }

    routes = []
    all_indices = sorted(index_urls)
    for entry in triage["entries"]:
        refs = entry["source_refs"]
        indices: list[int] = []
        method = "direct_logical_unit"
        if refs and refs[0] in blocks:
            block = blocks[refs[0]]
            indices = unit_chips(block, refs)
            if not indices and block.get("section") == "2. Out-of-sample validation ledger":
                citation_cells = [c for c in block.get("cells", []) if c.get("role") == "citation"]
                indices = [int(x) for c in citation_cells for x in c.get("chips", [])]
                method = "section2_authoritative_citation_cell"
        if entry["manual_id"] in {"M064", "M065"}:
            indices = all_indices
            method = "document_level_all_37_source_indices"
        if not indices:
            method = "no_citation_bound_in_captured_unit"
        routes.append(
            {
                "manual_id": entry["manual_id"],
                "lane": entry["lane"],
                "clause": entry["clause"],
                "code": entry["code"],
                "finding_ordinal": entry["finding_ordinal"],
                "source_refs": refs,
                "evidence_snippet": entry["evidence_snippet"],
                "source_indices": sorted(set(indices)),
                "source_urls": [index_urls[i] for i in sorted(set(indices)) if i in index_urls],
                "routing_method": method,
            }
        )
    route_map = {
        "schema": "NM_GATE_B_MANUAL_SOURCE_ROUTE_MAP_V1",
        "created_utc": utc_now(),
        "triage_sha256": sha256((master / "gemini-dr-c1r-contract-r3-manual-triage-20260713T024458Z/triage/TRIAGE_LEDGER.json").read_bytes()),
        "total": len(routes),
        "routes": routes,
    }
    json_dump(packet / "sources/SOURCE_INDEX_MAP.json", source_index_map)
    json_dump(packet / "sources/ROUTE_MAP.json", route_map)
    return source_index_map, route_map


class Fetcher:
    def __init__(self, packet: Path, max_fetches: int = 200, min_host_interval: float = 2.0):
        self.packet = packet
        self.raw_dir = packet / "sources/raw"
        self.text_dir = packet / "sources/text"
        self.meta_dir = packet / "sources/metadata"
        for p in (self.raw_dir, self.text_dir, self.meta_dir):
            p.mkdir(parents=True, exist_ok=True)
        self.log_path = packet / "sources/FETCH_LOG.jsonl"
        self.max_fetches = max_fetches
        self.min_host_interval = min_host_interval
        self.host_last: dict[str, float] = {}
        self.host_failures: dict[str, int] = defaultdict(int)
        self.fetch_count = 0
        self.cache: dict[str, dict] = {}
        self.ads_token = os.getenv("ADS_API_KEY") or os.getenv("ADS_API_TOKEN") or os.getenv("ADS_DEV_KEY")

    def _append_log(self, record: dict) -> None:
        with self.log_path.open("a") as fh:
            fh.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")

    def fetch(self, url: str, label: str, index: int, purpose: str, ads_auth: bool = False) -> dict:
        if url in self.cache:
            cached = dict(self.cache[url])
            cached["cache_reuse"] = True
            return cached
        if self.fetch_count >= self.max_fetches:
            raise RuntimeError("fetch budget exhausted")
        parsed = urlparse(url)
        if parsed.scheme not in {"http", "https"}:
            raise RuntimeError(f"non-http scheme blocked: {url}")
        host = parsed.netloc.lower()
        if self.host_failures[host] >= 3:
            result = {"requested_url": url, "status": 0, "error": "host_stopped_after_3_failures", "bytes": 0, "sha256": sha256(b"")}
            self._append_log({"utc": utc_now(), "method": "GET", "host": host, "index": index, "label": label, "purpose": purpose, **result})
            return result
        elapsed = time.monotonic() - self.host_last.get(host, 0.0)
        if elapsed < self.min_host_interval:
            time.sleep(self.min_host_interval - elapsed)
        headers = {"User-Agent": USER_AGENT, "Accept": "text/html,application/pdf,application/json;q=0.9,*/*;q=0.5"}
        if ads_auth:
            if not self.ads_token:
                result = {"requested_url": url, "status": 0, "error": "ads_token_not_configured", "bytes": 0, "sha256": sha256(b"")}
                self._append_log({"utc": utc_now(), "method": "GET", "host": host, "index": index, "label": label, "purpose": purpose, "auth": "ADS_NOT_CONFIGURED", **result})
                return result
            headers["Authorization"] = "Bearer " + self.ads_token
        started = utc_now()
        self.fetch_count += 1
        try:
            response = requests.get(url, headers=headers, timeout=60, allow_redirects=True)
            self.host_last[host] = time.monotonic()
            data = response.content
            status = int(response.status_code)
            if status >= 400:
                self.host_failures[host] += 1
            ctype = response.headers.get("content-type", "").split(";", 1)[0].strip().lower()
            ext = ".pdf" if "pdf" in ctype or response.url.lower().split("?", 1)[0].endswith(".pdf") else ".json" if "json" in ctype else ".html" if "html" in ctype else ".bin"
            digest = sha256(data)
            raw_name = f"idx{index:02d}_{safe_piece(label)}_{digest[:12]}{ext}"
            raw_path = self.raw_dir / raw_name
            raw_path.write_bytes(data)
            record = {
                "utc": started,
                "method": "GET",
                "host": host,
                "index": index,
                "label": label,
                "purpose": purpose,
                "requested_url": url,
                "final_url": response.url,
                "status": status,
                "bytes": len(data),
                "sha256": digest,
                "content_type": ctype,
                "raw_path": raw_path.relative_to(self.packet).as_posix(),
                "auth": "ADS_CONFIGURED_BOOLEAN_ONLY" if ads_auth else "NONE",
                "cache_reuse": False,
            }
            self._append_log(record)
            self.cache[url] = record
            return record
        except Exception as exc:
            self.host_last[host] = time.monotonic()
            self.host_failures[host] += 1
            record = {
                "utc": started,
                "method": "GET",
                "host": host,
                "index": index,
                "label": label,
                "purpose": purpose,
                "requested_url": url,
                "final_url": "",
                "status": 0,
                "bytes": 0,
                "sha256": sha256(b""),
                "content_type": "",
                "raw_path": "",
                "auth": "ADS_CONFIGURED_BOOLEAN_ONLY" if ads_auth else "NONE",
                "cache_reuse": False,
                "error": f"{type(exc).__name__}: {str(exc)[:240]}",
            }
            self._append_log(record)
            return record

    def read_raw(self, record: dict) -> bytes:
        p = record.get("raw_path")
        return (self.packet / p).read_bytes() if p else b""

    def extract(self, record: dict, index: int, label: str) -> dict:
        data = self.read_raw(record)
        ctype = record.get("content_type", "")
        result = {"title": "", "doi": "", "arxiv_id": "", "pdf_url": "", "text_path": "", "text_sha256": "", "text_chars": 0}
        if not data:
            return result
        text = ""
        if "pdf" in ctype or str(record.get("raw_path", "")).endswith(".pdf"):
            if fitz is not None:
                try:
                    doc = fitz.open(stream=data, filetype="pdf")
                    text = "\n\n".join(str(page.get_text("text")) for page in doc)
                    result["pdf_pages"] = doc.page_count
                except Exception as exc:
                    result["extract_error"] = f"{type(exc).__name__}: {str(exc)[:200]}"
        elif "html" in ctype or str(record.get("raw_path", "")).endswith(".html"):
            soup = BeautifulSoup(data, "html.parser")
            def meta(*names: str) -> str:
                for name in names:
                    node = soup.find("meta", attrs={"name": name}) or soup.find("meta", attrs={"property": name})
                    if node and node.get("content"):
                        return str(node.get("content")).strip()
                return ""
            result["title"] = meta("citation_title", "dc.title", "og:title") or (soup.title.get_text(" ", strip=True) if soup.title else "")
            result["doi"] = meta("citation_doi", "dc.identifier")
            if result["doi"]:
                m = DOI_RE.search(result["doi"])
                result["doi"] = m.group(0).rstrip(".,;)") if m else ""
            result["arxiv_id"] = meta("citation_arxiv_id")
            result["pdf_url"] = meta("citation_pdf_url")
            text = soup.get_text("\n", strip=True)
        elif "json" in ctype:
            try:
                obj = json.loads(data)
                text = json.dumps(obj, indent=2, ensure_ascii=False)
            except Exception:
                text = data.decode("utf-8", "replace")
        else:
            text = data.decode("utf-8", "replace")
        if text:
            digest = sha256(text.encode())
            text_path = self.text_dir / f"idx{index:02d}_{safe_piece(label)}_{digest[:12]}.txt"
            text_path.write_text(text)
            result.update({"text_path": text_path.relative_to(self.packet).as_posix(), "text_sha256": digest, "text_chars": len(text)})
        if not result["doi"]:
            candidate = unquote(record.get("requested_url", "")) + " " + unquote(record.get("final_url", ""))
            m = DOI_RE.search(candidate)
            if m:
                result["doi"] = m.group(0).rstrip(".,;)")
        m = ARXIV_RE.search(record.get("final_url", "") or record.get("requested_url", ""))
        if m and not result["arxiv_id"]:
            result["arxiv_id"] = m.group(1)
        return result


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--master", required=True)
    ap.add_argument("--packet", required=True)
    args = ap.parse_args()
    master = Path(args.master).resolve()
    packet = Path(args.packet).resolve()
    source_index_map, route_map = build_maps(master, packet)
    fetcher = Fetcher(packet)
    results = []
    title_ads_cache: dict[str, dict] = {}
    for item in source_index_map["indices"]:
        idx = int(item["index"]); url = item["url"]
        initial = fetcher.fetch(url, "initial", idx, "captured_citation_url")
        meta = fetcher.extract(initial, idx, "initial")
        records = [initial]
        extracts = [{"label": "initial", **meta}]

        # arXiv full text is the preferred T2 evidence route.
        arxiv_id = meta.get("arxiv_id")
        m = ARXIV_RE.search(url)
        if not arxiv_id and m:
            arxiv_id = m.group(1)
        if arxiv_id:
            pdf = fetcher.fetch(f"https://arxiv.org/pdf/{arxiv_id}", "arxiv_pdf", idx, "primary_full_text")
            records.append(pdf); extracts.append({"label": "arxiv_pdf", **fetcher.extract(pdf, idx, "arxiv_pdf")})

        # Resolve DOI, including DOI embedded in aggregator query strings.
        doi = meta.get("doi", "")
        if not doi:
            decoded = unquote(url)
            dm = DOI_RE.search(decoded)
            doi = dm.group(0).rstrip(".,;)") if dm else ""
        if doi:
            doi_rec = fetcher.fetch(f"https://doi.org/{doi}", "doi", idx, "doi_primary_resolution")
            doi_meta = fetcher.extract(doi_rec, idx, "doi")
            records.append(doi_rec); extracts.append({"label": "doi", **doi_meta})
            pdf_url = doi_meta.get("pdf_url")
            if pdf_url:
                pdf_rec = fetcher.fetch(pdf_url, "publisher_pdf", idx, "primary_full_text")
                records.append(pdf_rec); extracts.append({"label": "publisher_pdf", **fetcher.extract(pdf_rec, idx, "publisher_pdf")})
        elif meta.get("pdf_url"):
            pdf_rec = fetcher.fetch(meta["pdf_url"], "publisher_pdf", idx, "primary_full_text")
            records.append(pdf_rec); extracts.append({"label": "publisher_pdf", **fetcher.extract(pdf_rec, idx, "publisher_pdf")})

        # Read-only ADS metadata query. Token presence is logged only as a boolean.
        query = ""
        if arxiv_id:
            query = f'identifier:"arXiv:{arxiv_id}"'
        elif doi:
            query = f'doi:"{doi}"'
        elif meta.get("title"):
            query = f'title:"{meta["title"][:220]}"'
        ads_record = None
        if query and fetcher.ads_token:
            cache_key = query.lower()
            if cache_key in title_ads_cache:
                ads_record = dict(title_ads_cache[cache_key]); ads_record["cache_reuse"] = True
            else:
                fields = "bibcode,title,abstract,doi,identifier,author,year,pub,property"
                ads_url = "https://api.adsabs.harvard.edu/v1/search/query?q=" + quote(query) + "&fl=" + quote(fields) + "&rows=5"
                ads_record = fetcher.fetch(ads_url, "ads", idx, "read_only_metadata", ads_auth=True)
                title_ads_cache[cache_key] = ads_record
            if ads_record:
                records.append(ads_record)
                if not ads_record.get("cache_reuse"):
                    extracts.append({"label": "ads", **fetcher.extract(ads_record, idx, "ads")})

        result = {
            "index": idx,
            "captured_url": url,
            "ledger_rows": item["ledger_rows"],
            "records": records,
            "extracts": extracts,
        }
        json_dump(fetcher.meta_dir / f"index_{idx:02d}.json", result)
        results.append(result)

    summary = {
        "schema": "NM_GATE_B_SOURCE_ACQUISITION_SUMMARY_V1",
        "completed_utc": utc_now(),
        "method": "GET-only; local-first routes; no verdicts",
        "ads_token_present_boolean": bool(fetcher.ads_token),
        "fetch_budget": fetcher.max_fetches,
        "fetches_made": fetcher.fetch_count,
        "unique_source_indices": len(source_index_map["indices"]),
        "manual_routes": route_map["total"],
        "status_counts": {},
        "host_failures": dict(fetcher.host_failures),
        "results": results,
    }
    counts: dict[str, int] = defaultdict(int)
    for row in fetcher.log_path.read_text().splitlines():
        rec = json.loads(row); counts[str(rec.get("status", 0))] += 1
    summary["status_counts"] = dict(sorted(counts.items()))
    json_dump(packet / "sources/ACQUISITION_SUMMARY.json", summary)
    print(json.dumps({"status": "DONE", "fetches": fetcher.fetch_count, "sources": len(results), "status_counts": summary["status_counts"], "ads_token_present": bool(fetcher.ads_token), "host_failures": summary["host_failures"]}, indent=2))


if __name__ == "__main__":
    main()
