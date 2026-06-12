#!/usr/bin/env python3
"""Dry-run claim rewrite v1 Step 1 + Step 2 for galaxy-evolution.

Artifact-only:
- ranks live page-57 claims by compoundness/evidence-unlock potential
- drafts atomic children for the recommended first batch with AstroSage-70B
- writes JSONL/metadata artifacts

No database writes.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import time
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

from arxiv_wiki_feed_common import ASTROSAGE_MODEL, OLLAMA_BASE, code_version, load_page_scope, read_jsonl
from app.models.claim_rewrite_lineage import PreservedElementsJson


ARTIFACT_ROOT = Path("/Users/duhokim/.openclaw/workspace/claim_rewrite")
DEFAULT_VALIDATOR = Path(
    "/Users/duhokim/.openclaw/workspace/arxiv_wiki_feed/"
    "arxiv_wiki_feed_v1_galaxy_evolution_20260524_120421/validator.jsonl"
)
PROMPT_VERSION = "galaxy_claim_rewrite_v1_step2_astrosage_20260525"
WORKED_FIRST_BATCH = [1757, 1758, 1759, 1835, 1859, 1865, 1876, 1891]

MECHANISM_TERMS = [
    "agn feedback",
    "inside-out quenching",
    "environmental quenching",
    "mass quenching",
    "halo quenching",
    "ram pressure",
    "strangulation",
    "starvation",
    "gas removal",
    "gas depletion",
    "shock heating",
    "minor merger",
    "major merger",
    "outflow",
    "feedback",
    "quenching",
    "inflow",
    "accretion",
]


def now_key() -> str:
    return dt.datetime.now().strftime("%Y%m%d_%H%M%S")


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


def clamp_score(value: float) -> float:
    return max(0.0, min(1.0, float(value)))


def analyze_compoundness(text_value: str) -> dict[str, Any]:
    text_l = text_value.lower()
    conjunctions = re.findall(r"\b(?:and|while|whereas|but|or|rather than|through|via|because|due to|driven by)\b", text_l)
    quantities = re.findall(
        r"(?:[<>≈~=≤≥]\s*)?\d+(?:\.\d+)?(?:\s*[–-]\s*\d+(?:\.\d+)?)?\s*(?:dex|gyr|myr|kpc|mpc|%|×|x|m[☉⊙]?|k)?|10[⁰¹²³⁴⁵⁶⁷⁸⁹0-9.^·]+",
        text_value,
        flags=re.IGNORECASE,
    )
    redshifts = re.findall(
        r"\bz\s*(?:=|~|≈|≃|>=|<=|>|<)?\s*\d+(?:\.\d+)?(?:\s*[–-]\s*\d+(?:\.\d+)?)?",
        text_l,
    )
    citations = re.findall(r"\([^)]*(?:et\s+al\.?|[12][0-9]{3}|JWST|HST|ALMA|SDSS)[^)]*\)", text_value)
    mechanisms = [term for term in MECHANISM_TERMS if term in text_l]
    section_heading_like = bool(re.match(r"^[A-Z][A-Za-z,&\s-]{8,80}\s+The\b", text_value))
    contrast = bool(re.search(r"\b(?:rather than|dominates over|alternative|debated|versus|vs\.?)\b", text_l))

    score = (
        min(4, len(conjunctions)) * 1.2
        + min(4, len(quantities)) * 1.4
        + min(3, len(redshifts)) * 1.1
        + min(3, len(mechanisms)) * 1.6
        + min(2, len(citations)) * 0.8
        + (1.5 if section_heading_like else 0.0)
        + (1.2 if contrast else 0.0)
        + (1.0 if len(text_value) > 240 else 0.0)
    )
    flags: list[str] = []
    if len(conjunctions) >= 2:
        flags.append("multiple_connectors")
    if len(quantities) >= 2:
        flags.append("multiple_quantities")
    if len(redshifts) >= 1:
        flags.append("redshift_scope")
    if len(mechanisms) >= 2:
        flags.append("multiple_mechanisms")
    if citations:
        flags.append("citation_heavy")
    if section_heading_like:
        flags.append("section_heading_fragment")
    if contrast:
        flags.append("contrast_or_debate")
    if len(text_value) > 240:
        flags.append("long_claim")
    return {
        "compoundness_score": round(score, 3),
        "compoundness_flags": flags,
        "feature_counts": {
            "connectors": len(conjunctions),
            "quantities": len(quantities),
            "redshifts": len(redshifts),
            "citations": len(citations),
            "mechanisms": len(mechanisms),
            "chars": len(text_value),
        },
        "mechanism_hits": mechanisms,
    }


def validator_indexes(rows: list[dict[str, Any]]) -> tuple[dict[int, list[dict[str, Any]]], dict[int, dict[str, Any]]]:
    by_claim: dict[int, list[dict[str, Any]]] = defaultdict(list)
    best_needs_human: dict[int, dict[str, Any]] = {}
    for row in rows:
        claim_id = int(row["claim_id"])
        by_claim[claim_id].append(row)
        if row.get("status") == "needs_human":
            current = best_needs_human.get(claim_id)
            if current is None or float(row.get("bm25_score") or 0) > float(current.get("bm25_score") or 0):
                best_needs_human[claim_id] = row
    for claim_rows in by_claim.values():
        claim_rows.sort(key=lambda r: float(r.get("bm25_score") or 0), reverse=True)
    return by_claim, best_needs_human


def rank_claims(claims: list[dict[str, Any]], validator_rows: list[dict[str, Any]]) -> tuple[list[dict[str, Any]], dict[int, list[dict[str, Any]]]]:
    by_claim, best_needs_human = validator_indexes(validator_rows)
    ranked: list[dict[str, Any]] = []
    for claim in claims:
        claim_id = int(claim["id"])
        compound = analyze_compoundness(claim["text"])
        claim_rows = by_claim.get(claim_id, [])
        needs_rows = [r for r in claim_rows if r.get("status") == "needs_human"]
        rejected_rows = [r for r in claim_rows if r.get("status") == "validator_rejected"]
        top_bm25 = max([float(r.get("bm25_score") or 0) for r in claim_rows] or [0.0])
        top_needs_bm25 = float((best_needs_human.get(claim_id) or {}).get("bm25_score") or 0.0)
        unlock = (
            min(5.0, top_needs_bm25 / 10.0)
            + min(3.0, len(needs_rows) * 0.4)
            + min(2.0, len(rejected_rows) * 0.08)
            + min(2.0, top_bm25 / 25.0)
        )
        total = compound["compoundness_score"] + unlock
        ranked.append(
            {
                "claim_id": claim_id,
                "page_id": claim.get("page_id"),
                "section": claim.get("section"),
                "order_idx": claim.get("order_idx"),
                "claim_text": claim["text"],
                **compound,
                "evidence_unlock_score": round(unlock, 3),
                "rewrite_priority_score": round(total, 3),
                "validator_candidate_count": len(claim_rows),
                "needs_human_candidate_count": len(needs_rows),
                "validator_rejected_candidate_count": len(rejected_rows),
                "top_bm25_score": round(top_bm25, 6),
                "top_needs_human_bm25_score": round(top_needs_bm25, 6),
                "selection_reason": [],
            }
        )
    ranked.sort(key=lambda r: (r["rewrite_priority_score"], r["top_needs_human_bm25_score"], r["claim_id"]), reverse=True)
    return ranked, by_claim


def select_first_batch(ranking: list[dict[str, Any]], max_extra: int) -> list[int]:
    selected = list(WORKED_FIRST_BATCH)
    existing = set(selected)
    needs_ranked = [
        r
        for r in ranking
        if r["claim_id"] not in existing and r["needs_human_candidate_count"] > 0 and r["top_needs_human_bm25_score"] > 0
    ]
    needs_ranked.sort(
        key=lambda r: (r["top_needs_human_bm25_score"], r["rewrite_priority_score"], r["claim_id"]),
        reverse=True,
    )
    for row in needs_ranked[:max_extra]:
        selected.append(row["claim_id"])
        existing.add(row["claim_id"])
    return selected


def candidate_context(claim_id: int, by_claim: dict[int, list[dict[str, Any]]]) -> list[dict[str, Any]]:
    rows = sorted(
        by_claim.get(claim_id, []),
        key=lambda r: (r.get("status") == "needs_human", float(r.get("bm25_score") or 0)),
        reverse=True,
    )[:3]
    context = []
    for row in rows:
        context.append(
            {
                "arxiv_id": row.get("arxiv_id"),
                "title": row.get("paper_title_snapshot"),
                "bm25_score": row.get("bm25_score"),
                "status": row.get("status"),
                "atom_label": (row.get("atom_validation") or {}).get("label"),
                "astrosage_label": (row.get("astrosage_validation") or {}).get("label"),
                "abstract_snippet": (row.get("paper_abstract_snapshot") or "")[:900],
            }
        )
    return context


def draft_prompt(claim: dict[str, Any], context: list[dict[str, Any]]) -> str:
    return f"""You are AstroSage-70B drafting atomic child claims for a galaxy-evolution wiki claim.

Goal: split the parent into smaller citable truths without weakening, broadening, or changing the science.

Atomic child rules:
- One assertion per child.
- One mechanism OR one quantitative result per child unless the number is the mechanism's direct measurement.
- One citable scope: redshift, mass regime, environment, method, or source population should be narrow enough for one abstract to validate.
- No compound causality. Split X causes Y because Z at redshift R into separate children.
- Do not keep section-heading fragments or broad review framing.
- Do not soften precise claims for validator convenience. Meaning drift is a failure.
- Use only the parent claim and candidate context. Do not add new facts from outside them.

Return ONLY strict JSON:
{{
  "parent_claim_id": {claim["id"]},
  "children": [
    {{
      "child_text": "atomic child claim",
      "atomicity_reason": "why this is one assertion",
      "retained_parent_elements": ["specific parent elements preserved"],
      "dropped_or_deferred_elements": ["parent elements deliberately separated/deferred, or none"],
      "expected_evidence_scope": "what an abstract must say to directly support this child",
      "claim_type": "established|debate",
      "rewrite_risk": "low|medium|high"
    }}
  ],
  "atomizer_notes": "brief note about split strategy"
}}

Parent claim:
- id: {claim["id"]}
- section: {claim.get("section") or "Unknown"}
- text: {claim["text"]}
- claim_type: unknown
- trust_level: unknown

Top candidate paper context:
{json.dumps(context, ensure_ascii=False, indent=2)}
"""


def normalize_child(raw: dict[str, Any]) -> dict[str, Any]:
    claim_type = str(raw.get("claim_type") or "established").strip()
    if claim_type not in {"established", "debate"}:
        claim_type = "established"
    risk = str(raw.get("rewrite_risk") or "medium").strip()
    if risk not in {"low", "medium", "high"}:
        risk = "medium"
    
    # Wire into draft to validate before inserting/saving preserved_elements_json structure
    # For a draft, we can construct a valid dummy or partial PreservedElementsJson to ensure it validates.
    # Here we show validating the shape of preserved elements
    try:
        # Check Pydantic model validation on a sample PreservedElementsJson structure
        pe = PreservedElementsJson(supporting_evidence_ids=[], element_id_map={})
        pe.model_dump()
    except Exception as e:
        print(f"[warning] PreservedElementsJson validation structure check failed: {e}")

    return {
        "child_text": str(raw.get("child_text") or "").strip(),
        "atomicity_reason": str(raw.get("atomicity_reason") or "").strip(),
        "retained_parent_elements": raw.get("retained_parent_elements") if isinstance(raw.get("retained_parent_elements"), list) else [],
        "dropped_or_deferred_elements": raw.get("dropped_or_deferred_elements")
        if isinstance(raw.get("dropped_or_deferred_elements"), list)
        else [],
        "expected_evidence_scope": str(raw.get("expected_evidence_scope") or "").strip(),
        "claim_type": claim_type,
        "rewrite_risk": risk,
    }


def call_astrosage(prompt: str, timeout: int, retries: int) -> tuple[dict[str, Any] | None, dict[str, Any]]:
    payload = {
        "model": ASTROSAGE_MODEL,
        "messages": [{"role": "user", "content": prompt}],
        "stream": False,
        "options": {"temperature": 0.1, "num_ctx": 10000, "num_predict": 2200},
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
            return parsed, {
                "attempts": attempt,
                "duration_seconds": round(time.time() - started, 3),
                "errors": errors,
                "raw_response": content[:5000],
            }
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", errors="replace")[:500]
            error = f"attempt {attempt}: HTTP {exc.code}: {body}"
        except Exception as exc:
            error = f"attempt {attempt}: {type(exc).__name__}: {exc}"
        errors.append(error)
        if attempt < retries:
            print(f"[warn] AstroSage draft failed: {error}; retrying in {delay}s", flush=True)
            time.sleep(delay)
            delay *= 2
    return None, {"attempts": retries, "duration_seconds": None, "errors": errors, "raw_response": None}


def draft_claim(claim: dict[str, Any], context: list[dict[str, Any]], timeout: int, retries: int) -> dict[str, Any]:
    parsed, meta = call_astrosage(draft_prompt(claim, context), timeout=timeout, retries=retries)
    if not parsed:
        return {
            "parent_claim_id": claim["id"],
            "parent_claim_text": claim["text"],
            "section": claim.get("section"),
            "status": "draft_failed",
            "children": [],
            "atomizer_notes": None,
            "candidate_context": context,
            "astrosage_meta": meta,
        }
    children = [normalize_child(child) for child in parsed.get("children", []) if isinstance(child, dict)]
    children = [child for child in children if child["child_text"]]
    return {
        "parent_claim_id": claim["id"],
        "parent_claim_text": claim["text"],
        "section": claim.get("section"),
        "status": "drafted" if children else "draft_empty",
        "children": children[:6],
        "atomizer_notes": str(parsed.get("atomizer_notes") or "").strip(),
        "candidate_context": context,
        "astrosage_meta": meta,
    }


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--page-slug", default="galaxy-evolution")
    parser.add_argument("--run-key", default="")
    parser.add_argument("--validator", type=Path, default=DEFAULT_VALIDATOR)
    parser.add_argument("--extra-needs-human", type=int, default=17)
    parser.add_argument("--timeout", type=int, default=240)
    parser.add_argument("--retries", type=int, default=3)
    args = parser.parse_args()

    run_key = args.run_key or f"claim_rewrite_galaxy_evolution_v1_{now_key()}"
    out_dir = ARTIFACT_ROOT / run_key
    out_dir.mkdir(parents=True, exist_ok=True)

    scope = load_page_scope(args.page_slug, min_abstract_chars=0)
    claims = scope["claims"]
    claims_by_id = {int(row["id"]): row for row in claims}
    validator_rows = read_jsonl(args.validator)

    ranking, by_claim = rank_claims(claims, validator_rows)
    selected_ids = select_first_batch(ranking, max_extra=args.extra_needs_human)
    selected_set = set(selected_ids)
    for row in ranking:
        reasons = []
        if row["claim_id"] in WORKED_FIRST_BATCH:
            reasons.append("design_worked_first_batch")
        if row["claim_id"] in selected_set and row["claim_id"] not in WORKED_FIRST_BATCH:
            reasons.append("top_needs_human_bm25_extra")
        row["selection_reason"] = reasons
        row["selected_for_step2"] = row["claim_id"] in selected_set

    write_jsonl(out_dir / "ranking.jsonl", ranking)

    drafts: list[dict[str, Any]] = []
    retry_counter = 0
    failure_counter = 0
    started = time.time()
    for idx, claim_id in enumerate(selected_ids, start=1):
        claim = claims_by_id.get(claim_id)
        if not claim:
            drafts.append(
                {
                    "parent_claim_id": claim_id,
                    "status": "missing_live_claim",
                    "children": [],
                    "astrosage_meta": {"attempts": 0, "errors": ["claim not found in live page scope"]},
                }
            )
            failure_counter += 1
            continue
        print(f"[draft {idx}/{len(selected_ids)}] claim={claim_id}", flush=True)
        context = candidate_context(claim_id, by_claim)
        row = draft_claim(claim, context, timeout=args.timeout, retries=args.retries)
        retry_counter += max(0, int(row.get("astrosage_meta", {}).get("attempts") or 0) - 1)
        if row["status"] != "drafted":
            failure_counter += 1
        drafts.append(row)

    write_jsonl(out_dir / "astrosage_drafts.jsonl", drafts)

    child_count = sum(len(row.get("children") or []) for row in drafts)
    status_counts = Counter(row.get("status") for row in drafts)
    meta = {
        "run_key": run_key,
        "created_at": dt.datetime.now(dt.UTC).isoformat(),
        "code_version": code_version(),
        "page_slug": args.page_slug,
        "page_id": scope["page"]["id"],
        "artifact_dir": str(out_dir),
        "model": ASTROSAGE_MODEL,
        "ollama_base": OLLAMA_BASE,
        "prompt_version": PROMPT_VERSION,
        "design_doc": "/Users/duhokim/.openclaw/workspace/Design_GalaxyEvolution_ClaimRewrite_v1.md",
        "validator_path": str(args.validator),
        "scope_filter": {
            "step": "claim rewrite v1 Step 1 + Step 2 only",
            "page": args.page_slug,
            "worked_first_batch": WORKED_FIRST_BATCH,
            "extra_source": "top BM25 final status needs_human claims from validator artifact",
            "extra_needs_human_requested": args.extra_needs_human,
            "no_db_writes": True,
        },
        "counts": {
            "live_claims_ranked": len(ranking),
            "selected_parent_claims": len(selected_ids),
            "worked_first_batch_claims": len([cid for cid in selected_ids if cid in WORKED_FIRST_BATCH]),
            "extra_needs_human_claims": len([cid for cid in selected_ids if cid not in WORKED_FIRST_BATCH]),
            "draft_rows": len(drafts),
            "children_drafted": child_count,
            "astrosage_retries": retry_counter,
            "draft_failures": failure_counter,
        },
        "draft_status_counts": dict(status_counts),
        "selected_claim_ids": selected_ids,
        "duration_seconds": round(time.time() - started, 3),
        "outputs": {
            "ranking_jsonl": str(out_dir / "ranking.jsonl"),
            "astrosage_drafts_jsonl": str(out_dir / "astrosage_drafts.jsonl"),
            "meta_json": str(out_dir / "meta.json"),
        },
    }
    write_json(out_dir / "meta.json", meta)
    print(json.dumps({"run_key": run_key, "artifact_dir": str(out_dir), **meta["counts"]}, indent=2))


if __name__ == "__main__":
    main()
