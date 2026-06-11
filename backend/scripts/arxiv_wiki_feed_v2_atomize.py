#!/usr/bin/env python3
"""Phase 1 offline atomization for arXiv -> Wiki Feed v2.

Artifact-only: reads current page claims and writes element JSONL/report files.
No database writes.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import random
import re
import time
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from arxiv_wiki_feed_common import ASTROSAGE_MODEL, OLLAMA_BASE, code_version, load_page_scope


ARTIFACT_ROOT = Path("/Users/duhokim/.openclaw/workspace/arxiv_wiki_feed_v2")
PROMPT_VERSION = "arxiv_wiki_feed_v2_atomizer_p1_20260525"
ELEMENT_TYPES = {
    "subject",
    "mechanism",
    "quantity_or_threshold",
    "redshift_or_environment",
    "citation_or_method",
    "relationship",
    "scope_modifier",
}

MECHANISM_TERMS = [
    "AGN feedback",
    "inside-out quenching",
    "environmental quenching",
    "mass quenching",
    "halo quenching",
    "ram pressure stripping",
    "ram-pressure stripping",
    "starvation",
    "strangulation",
    "gas removal",
    "halo gas depletion",
    "shock heating",
    "virial shock heating",
    "tidal stripping",
    "minor mergers",
    "major mergers",
    "supernova feedback",
    "stellar feedback",
    "outflows",
    "reionization",
    "morphological quenching",
    "disk instabilities",
    "cold accretion",
]


def utc_stamp() -> str:
    return dt.datetime.now(dt.UTC).strftime("%Y%m%dT%H%M%SZ")


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True), encoding="utf-8")


def write_jsonl(path: Path, rows: list[dict[str, Any]]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False, sort_keys=True) + "\n")


def extract_json_object(text_value: str) -> dict[str, Any]:
    stripped = (text_value or "").strip()
    if stripped.startswith("```"):
        stripped = re.sub(r"^```(?:json)?\s*", "", stripped)
        stripped = re.sub(r"\s*```$", "", stripped)
    try:
        parsed = json.loads(stripped)
        if isinstance(parsed, dict):
            return parsed
    except Exception:
        pass
    match = re.search(r"\{.*\}", stripped, re.DOTALL)
    if not match:
        raise ValueError("no JSON object found")
    parsed = json.loads(match.group(0))
    if not isinstance(parsed, dict):
        raise ValueError("top-level JSON is not an object")
    return parsed


def clamp_score(value: Any, default: float = 0.7) -> float:
    try:
        score = float(value)
    except Exception:
        score = default
    return max(0.0, min(1.0, score))


def deterministic_preparse(claim: dict[str, Any]) -> dict[str, Any]:
    text_value = claim["text"]
    hints: dict[str, list[dict[str, Any]]] = {
        "redshift_or_environment": [],
        "quantity_or_threshold": [],
        "citation_or_method": [],
        "mechanism": [],
        "subject": [],
    }

    def add(kind: str, value: str, span: str, normalized: str | None = None) -> None:
        value = re.sub(r"\s+", " ", value).strip(" .,;")
        span = re.sub(r"\s+", " ", span).strip()
        if not value:
            return
        item = {"text": value, "source_span": span}
        if normalized:
            item["normalized"] = normalized
        if item not in hints[kind]:
            hints[kind].append(item)

    for pattern in [
        r"\bz\s*(?:=|~|≈|≃|>=|≤|<=|>|<)?\s*\d+(?:\.\d+)?(?:\s*[–-]\s*\d+(?:\.\d+)?)?",
        r"\bredshift[s]?\s*(?:of|range)?\s*[~≈≃=<>]?\s*\d+(?:\.\d+)?(?:\s*[–-]\s*\d+(?:\.\d+)?)?",
        r"\b(?:groups?|clusters?|protoclusters?|field|satellite galaxies|central galaxies|dense environments?|overdense environments?|circumgalactic media|CGM)\b",
    ]:
        for match in re.finditer(pattern, text_value, re.IGNORECASE):
            add("redshift_or_environment", match.group(0), match.group(0), match.group(0).lower())

    for pattern in [
        r"M[★_*]?\s*(?:>|<|>=|<=|≈|~|=)\s*10[0-9¹²³⁴⁵⁶⁷⁸⁹\^·.]+(?:\s*M[☉⊙]?)?",
        r"Σ[★_*]?[,\w\s]*\s*(?:>|<|>=|<=|≈|~|=)\s*[0-9.]+\s*[×x]\s*10[0-9⁰¹²³⁴⁵⁶⁷⁸⁹]+(?:\s*M[☉⊙]?\s*kpc[⁻-]?[²2])?",
        r"\b\d+(?:\.\d+)?\s*(?:dex|Gyr|Myr|kpc|Mpc|M[☉⊙]|%|×|x)\b",
        r"\b10[0-9¹²³⁴⁵⁶⁷⁸⁹\^·.]+\s*(?:M[☉⊙]|M_sun|K|yr)?\b",
    ]:
        for match in re.finditer(pattern, text_value):
            add("quantity_or_threshold", match.group(0), match.group(0), match.group(0))

    for pattern in [
        r"\(([^)]*(?:et\s+al\.?|[12][0-9]{3}|JWST|HST|ALMA|SDSS|TNG|Illustris|COLIBRE|EAGLE|MaNGA)[^)]*)\)",
        r"\b[A-Z][A-Za-z-]+ et\s+al\.?\s*(?:\(?[12][0-9]{3}\)?)?",
    ]:
        for match in re.finditer(pattern, text_value):
            add("citation_or_method", match.group(0).strip("()"), match.group(0))

    for term in MECHANISM_TERMS:
        match = re.search(re.escape(term), text_value, re.IGNORECASE)
        if match:
            add("mechanism", match.group(0), match.group(0), term.lower())

    subject_match = re.match(
        r"^(.{12,150}?)(?:\s+(?:is|are|can|may|has|have|shows|reveals|suggests|indicates|constrains|drives|operates|dominates|links?|involves)\b)",
        text_value,
        re.IGNORECASE,
    )
    if subject_match:
        add("subject", subject_match.group(1), subject_match.group(1), subject_match.group(1).lower())
    else:
        add("subject", text_value[:120], text_value[:120], text_value[:120].lower())

    return hints


def atomizer_prompt(claim: dict[str, Any], parser_hints: dict[str, list[dict[str, Any]]]) -> str:
    return f"""You are AstroSage-70B atomizing one astronomy wiki claim into evidence-checkable elements.

Use ONLY the claim text. Do not add background facts. An element is the smallest factual unit that a paper abstract can support, miss, or contradict.

Return ONLY one strict JSON object:
{{
  "parseable": true,
  "failure_mode": null,
  "elements": [
    {{
      "element_type": "subject|mechanism|quantity_or_threshold|redshift_or_environment|citation_or_method|relationship|scope_modifier",
      "required": true,
      "text": "directly checkable element text",
      "source_span": "exact words from the claim",
      "normalized_subject": null,
      "normalized_mechanism": null,
      "quantity_or_range": null,
      "redshift_or_environment": null,
      "citation_hint": null,
      "atomizer_confidence": 0.0,
      "notes": null
    }}
  ]
}}

Rules:
- Required elements are claim-breaking: if missing, a paper cannot strictly support the claim.
- Optional elements are context or citation hints.
- Split compound claims into multiple elements; do not weaken or broaden the claim.
- Redshift, mass, environment, mechanism, and quantity constraints are required when they affect the claim meaning.
- Citation names/methods are usually optional unless the claim is specifically about that method or source.
- Use element_type only from the allowed enum.
- source_span must be copied from the claim text.

Claim:
- id: {claim["id"]}
- section: {claim.get("section") or "Unknown"}
- text: {claim["text"]}

Deterministic parser hints:
{json.dumps(parser_hints, ensure_ascii=False, indent=2)}
"""


def ollama_atomize(prompt: str, timeout: int, retries: int) -> tuple[dict[str, Any] | None, dict[str, Any]]:
    payload = {
        "model": ASTROSAGE_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
        "options": {"temperature": 0.0, "num_ctx": 8192, "num_predict": 1600},
    }
    data = json.dumps(payload).encode("utf-8")
    delay = 8
    errors: list[str] = []
    for attempt in range(1, retries + 1):
        started = time.time()
        try:
            request = urllib.request.Request(
                f"{OLLAMA_BASE}/api/chat",
                data=data,
                headers={"Content-Type": "application/json"},
                method="POST",
            )
            with urllib.request.urlopen(request, timeout=timeout) as response:
                raw = response.read().decode("utf-8", errors="replace")
            response_json = json.loads(raw)
            content = ((response_json.get("message") or {}).get("content") or "").strip()
            parsed = extract_json_object(content)
            meta = {
                "attempts": attempt,
                "duration_seconds": round(time.time() - started, 3),
                "raw_response": content[:4000],
                "errors": errors,
            }
            return parsed, meta
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")[:500]
            error = f"attempt {attempt}: HTTP {exc.code}: {body}"
        except Exception as exc:
            error = f"attempt {attempt}: {type(exc).__name__}: {exc}"
        errors.append(error)
        if attempt < retries:
            print(f"[warn] AstroSage atomizer failed: {error}; retrying in {delay}s", flush=True)
            time.sleep(delay)
            delay *= 2
    return None, {"attempts": retries, "duration_seconds": None, "raw_response": None, "errors": errors}


def normalize_elements(claim: dict[str, Any], parsed: dict[str, Any] | None, meta: dict[str, Any]) -> tuple[bool, list[dict[str, Any]], str | None]:
    if parsed is None:
        return False, [], "atomizer_failed_after_retries"
    if not bool(parsed.get("parseable", True)):
        return False, [], str(parsed.get("failure_mode") or "model_marked_unparseable")
    output: list[dict[str, Any]] = []
    seen: set[tuple[str, str]] = set()
    for raw in parsed.get("elements") or []:
        if not isinstance(raw, dict):
            continue
        element_type = str(raw.get("element_type") or "relationship").strip()
        if element_type not in ELEMENT_TYPES:
            element_type = "relationship"
        text_value = re.sub(r"\s+", " ", str(raw.get("text") or raw.get("element_text") or "")).strip()
        if not text_value:
            continue
        key = (element_type, text_value.lower())
        if key in seen:
            continue
        seen.add(key)
        output.append(
            {
                "claim_id": int(claim["id"]),
                "element_index": len(output) + 1,
                "element_type": element_type,
                "required": bool(raw.get("required", True)),
                "text": text_value[:500],
                "parent_claim_text": claim["text"],
                "source_span": re.sub(r"\s+", " ", str(raw.get("source_span") or text_value)).strip()[:500],
                "normalized_subject": raw.get("normalized_subject"),
                "normalized_mechanism": raw.get("normalized_mechanism"),
                "quantity_or_range": raw.get("quantity_or_range"),
                "redshift_or_environment": raw.get("redshift_or_environment"),
                "citation_hint": raw.get("citation_hint"),
                "atomizer_model": ASTROSAGE_MODEL,
                "atomizer_prompt_version": PROMPT_VERSION,
                "atomizer_confidence": clamp_score(raw.get("atomizer_confidence"), default=0.7),
                "notes": raw.get("notes"),
                "section": claim.get("section"),
                "order_idx": claim.get("order_idx"),
                "atomizer_attempts": meta.get("attempts"),
                "atomizer_duration_seconds": meta.get("duration_seconds"),
            }
        )
    if not output:
        return False, [], "empty_elements"
    return True, output, None


def choose_examples(claim_rows: list[dict[str, Any]], by_claim: dict[int, list[dict[str, Any]]]) -> dict[str, dict[str, Any] | None]:
    examples: dict[str, dict[str, Any] | None] = {"clean": None, "compound": None, "citation_heavy": None, "ambiguous": None}
    for claim in claim_rows:
        cid = int(claim["id"])
        elements = by_claim.get(cid, [])
        text_value = claim["text"]
        if examples["clean"] is None and 2 <= len(elements) <= 3 and not re.search(r"\bet al\.?|[12][0-9]{3}", text_value):
            examples["clean"] = {"claim": claim, "elements": elements}
        if examples["compound"] is None and len(elements) >= 6:
            examples["compound"] = {"claim": claim, "elements": elements}
        if examples["citation_heavy"] is None and re.search(r"\bet al\.?|[12][0-9]{3}", text_value):
            examples["citation_heavy"] = {"claim": claim, "elements": elements}
        if examples["ambiguous"] is None and any(el["element_type"] == "scope_modifier" for el in elements):
            examples["ambiguous"] = {"claim": claim, "elements": elements}
    for key, value in list(examples.items()):
        if value is None and claim_rows:
            claim = claim_rows[0]
            examples[key] = {"claim": claim, "elements": by_claim.get(int(claim["id"]), [])}
    return examples


def markdown_table(elements: list[dict[str, Any]]) -> list[str]:
    lines = ["| idx | type | req/opt | text | source span |", "|---:|---|---|---|---|"]
    for el in elements:
        req = "required" if el.get("required") else "optional"
        text_value = str(el.get("text") or "").replace("|", "\\|")
        span = str(el.get("source_span") or "").replace("|", "\\|")
        lines.append(f"| {el['element_index']} | {el['element_type']} | {req} | {text_value} | {span} |")
    return lines


def write_report(out_dir: Path, meta: dict[str, Any], claim_rows: list[dict[str, Any]], elements: list[dict[str, Any]]) -> None:
    by_claim: dict[int, list[dict[str, Any]]] = defaultdict(list)
    for element in elements:
        by_claim[int(element["claim_id"])].append(element)
    examples = choose_examples(claim_rows, by_claim)
    lines = [
        "# arXiv Wiki Feed v2 Phase 1 Atomization — galaxy-evolution",
        "",
        f"Run key: `{meta['run_key']}`",
        f"Artifact dir: `{out_dir}`",
        "",
        "## Summary",
        "",
        f"- Claim count attempted: {meta['claim_count']}",
        f"- Parseable claims: {meta['parseable_claims']} ({meta['parseable_pct']:.2%})",
        f"- Total elements: {meta['element_count']}",
        f"- Element type distribution: {meta['element_type_counts']}",
        f"- Required vs optional: {meta['required_optional_counts']}",
        f"- Parser hit stats: {meta['parser_hit_stats']}",
        f"- Failure modes: {meta['failure_mode_counts']}",
        f"- Acceptance bar >=95% parseable: {'PASS' if meta['parseable_pct'] >= 0.95 else 'FAIL'}",
        "",
        "## Worked Examples",
        "",
    ]
    for label, payload in examples.items():
        if not payload:
            continue
        claim = payload["claim"]
        lines += [
            f"### {label.replace('_', ' ').title()} — Claim {claim['id']}",
            "",
            f"Section: {claim.get('section') or 'Unknown'}",
            "",
            f"> {claim['text']}",
            "",
            *markdown_table(payload["elements"]),
            "",
        ]
    lines += [
        "## Stop",
        "",
        "Phase 1 artifacts only. No DB writes, migrations, validator runs, production evidence writes, or v1 manifest changes were performed.",
        "",
    ]
    (out_dir / "atomize_report.md").write_text("\n".join(lines), encoding="utf-8")


def run(args: argparse.Namespace) -> tuple[Path, dict[str, Any]]:
    run_key = args.run_key or f"atomize_galaxy_evolution_{utc_stamp()}"
    out_dir = ARTIFACT_ROOT / run_key
    out_dir.mkdir(parents=True, exist_ok=True)

    scope = load_page_scope(args.page_slug, min_abstract_chars=0)
    claim_rows = scope["claims"]
    elements: list[dict[str, Any]] = []
    claim_meta: list[dict[str, Any]] = []
    parser_hit_totals = Counter()
    failure_modes = Counter()

    for index, claim in enumerate(claim_rows, start=1):
        print(f"[atomize {index}/{len(claim_rows)}] claim={claim['id']}", flush=True)
        hints = deterministic_preparse(claim)
        for kind, hits in hints.items():
            parser_hit_totals[kind] += len(hits)
        parsed, atomizer_meta = ollama_atomize(
            atomizer_prompt(claim, hints),
            timeout=args.timeout,
            retries=args.retries,
        )
        parseable, claim_elements, failure_mode = normalize_elements(claim, parsed, atomizer_meta)
        if failure_mode:
            failure_modes[failure_mode] += 1
        elements.extend(claim_elements)
        claim_meta.append(
            {
                "claim_id": int(claim["id"]),
                "parseable": parseable,
                "element_count": len(claim_elements),
                "failure_mode": failure_mode,
                "parser_hits": {key: len(value) for key, value in hints.items()},
                "atomizer_attempts": atomizer_meta.get("attempts"),
                "atomizer_duration_seconds": atomizer_meta.get("duration_seconds"),
                "atomizer_errors": atomizer_meta.get("errors") or [],
            }
        )

    type_counts = Counter(element["element_type"] for element in elements)
    required_counts = Counter("required" if element.get("required") else "optional" for element in elements)
    parseable_claims = sum(1 for row in claim_meta if row["parseable"])
    meta = {
        "run_key": run_key,
        "artifact_dir": str(out_dir),
        "page_slug": args.page_slug,
        "page": scope["page"],
        "code_version": code_version(),
        "model": ASTROSAGE_MODEL,
        "ollama_base": OLLAMA_BASE,
        "atomizer_prompt_version": PROMPT_VERSION,
        "claim_count": len(claim_rows),
        "parseable_claims": parseable_claims,
        "parseable_pct": round(parseable_claims / max(1, len(claim_rows)), 6),
        "element_count": len(elements),
        "element_type_counts": dict(type_counts),
        "required_optional_counts": dict(required_counts),
        "parser_hit_stats": dict(parser_hit_totals),
        "failure_mode_counts": dict(failure_modes),
        "claims": claim_meta,
        "params": {"timeout": args.timeout, "retries": args.retries},
        "outputs": {
            "elements_jsonl": str(out_dir / "elements.jsonl"),
            "atomize_meta_json": str(out_dir / "atomize_meta.json"),
            "atomize_report_md": str(out_dir / "atomize_report.md"),
        },
    }

    write_jsonl(out_dir / "elements.jsonl", elements)
    write_json(out_dir / "atomize_meta.json", meta)
    write_report(out_dir, meta, claim_rows, elements)
    return out_dir, meta


def main() -> None:
    parser = argparse.ArgumentParser(description="Offline v2 atomization for arXiv -> Wiki Feed.")
    parser.add_argument("--page-slug", default="galaxy-evolution")
    parser.add_argument("--run-key")
    parser.add_argument("--timeout", type=int, default=360)
    parser.add_argument("--retries", type=int, default=3)
    args = parser.parse_args()
    out_dir, meta = run(args)
    print(
        json.dumps(
            {
                "artifact_dir": str(out_dir),
                "run_key": meta["run_key"],
                "claim_count": meta["claim_count"],
                "parseable_claims": meta["parseable_claims"],
                "element_count": meta["element_count"],
            },
            indent=2,
        )
    )


if __name__ == "__main__":
    main()
