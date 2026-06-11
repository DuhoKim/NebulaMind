"""
Proposal generators for the autowiki tick loop (§2.1, §4.2 step 5-6).

Four proposal types (ranked by blast radius):
  1. evidence_link   — add 1-3 Evidence rows to an existing Claim
  2. claim_insert    — insert 1 Claim (+ evidence), debate or subtopic
  3. hero_upgrade    — replace 1 hero_facts entry
  4. section_rewrite — rewrite one ## section in page.content

Each proposer returns a ProposalResult; the tick runner applies it
in a pending state, scores, then commits or rolls back.

Atom-7B alignment gate: every new (claim_text, evidence_abstract) pair
must score ≥ 0.55 — hard REJECT before the judge runs if any pair fails.
"""
import json
import logging
import re
from dataclasses import dataclass, field
from typing import Literal

import httpx

from app.config import settings

log = logging.getLogger(__name__)


# ---------------------------------------------------------------------------
# Robust JSON extraction
# ---------------------------------------------------------------------------

_decoder = json.JSONDecoder()


def _extract_json(raw: str, expect: str = "object") -> dict | list | None:
    """
    Extract a JSON object or array from a model response that may contain
    markdown code fences, prose, or other noise.

    Strategy:
      1. Strip ``` / ```json fences.
      2. Try direct parse.
      3. Use raw_decode from each { or [ to find the first valid block.

    expect: 'object' → prefer {, 'array' → prefer [
    """
    # Strip markdown code fences
    text = re.sub(r"```(?:json)?\s*", "", raw, flags=re.IGNORECASE).strip()

    # Try direct parse first
    try:
        return json.loads(text)
    except (json.JSONDecodeError, ValueError):
        pass

    # Try raw_decode from each opener position, prefer the expected type
    openers = "{[" if expect == "object" else "[{"
    for opener in openers:
        for i, ch in enumerate(text):
            if ch != opener:
                continue
            try:
                obj, _ = _decoder.raw_decode(text, i)
                return obj
            except json.JSONDecodeError:
                continue

    log.warning("[proposers] JSON extract failed (first 300 chars): %s", raw[:300])
    return None

ProposalType = Literal[
    "evidence_link", "claim_insert", "hero_upgrade", "section_rewrite"
]

_ASTROSAGE = "astrosage-70b"
_ATOM = "vanta-research/atom-astronomy-7b"


# ---------------------------------------------------------------------------
# Result types
# ---------------------------------------------------------------------------

@dataclass
class EvidenceLinkProposal:
    claim_id: int
    papers: list[dict]  # [{arxiv_id, title, abstract, year, stance, quality}]


@dataclass
class ClaimInsertProposal:
    section: str
    claim_text: str
    claim_type: str           # "debate" | "established"
    debate_topic: str | None
    papers: list[dict]        # same structure as above


@dataclass
class HeroUpgradeProposal:
    new_hero_fact: dict       # single hero_facts entry dict
    replace_index: int | None # None = append


@dataclass
class SectionRewriteProposal:
    section_header: str
    new_content: str          # full new markdown for that ## section


@dataclass
class ProposalResult:
    proposal_type: ProposalType
    payload: EvidenceLinkProposal | ClaimInsertProposal | HeroUpgradeProposal | SectionRewriteProposal
    gate_passed: bool = True
    gate_reason: str = ""
    model_proposer: str = _ASTROSAGE


# ---------------------------------------------------------------------------
# Model helpers
# ---------------------------------------------------------------------------

def _base_url() -> str:
    """Return base URL normalised to include exactly one /v1 suffix."""
    url = settings.OLLAMA_BASE_URL.rstrip("/")
    if not url.endswith("/v1"):
        url += "/v1"
    return url


def _call_astrosage(prompt: str, system: str, timeout: int = 90) -> str:
    try:
        resp = httpx.post(
            f"{_base_url()}/chat/completions",
            json={
                "model": settings.ASTRO_SYNTH_MODEL or _ASTROSAGE,
                "messages": [
                    {"role": "system", "content": system},
                    {"role": "user", "content": prompt},
                ],
                "temperature": 0.7,
                "options": {"num_ctx": 8192},
                # 2026-05-12 fix: AstroSage-70B was unloading between 15-min
                # ticks (default keep_alive 5 min), so every tick paid the
                # 70B cold-start. After Tori's prompt hardening raised the
                # required output to 400+ words, the cold-start + inference
                # consistently exceeded 120s and every section_rewrite
                # gate_rejected with "too short or failed". Keep_alive=1h
                # holds the model in RAM between ticks.
                "keep_alive": "1h",
            },
            timeout=timeout,
        )
        resp.raise_for_status()
    except Exception as exc:
        log.warning("[proposers] AstroSage HTTP error: %s", exc)
        raise
    return resp.json()["choices"][0]["message"]["content"].strip()


def _call_atom_alignment(claim_text: str, evidence_abstract: str, timeout: int = 20) -> float:
    """Atom-7B alignment gate. Returns score 0-1. Threshold: 0.55."""
    prompt = (
        f"Claim: {claim_text[:300]}\n\n"
        f"Evidence abstract: {evidence_abstract[:500]}\n\n"
        "Does this evidence directly support the claim with specific findings? "
        "Reply with a decimal number 0.00-1.00 only (e.g. 0.82)."
    )
    try:
        resp = httpx.post(
            f"{_base_url()}/chat/completions",
            json={
                "model": settings.ASTRO_SCORER_MODEL or _ATOM,
                "messages": [{"role": "user", "content": prompt}],
                "temperature": 0.0,
                "options": {"num_ctx": 8192},
            },
            timeout=timeout,
        )
        resp.raise_for_status()
        text = resp.json()["choices"][0]["message"]["content"].strip()
        m = re.search(r"([01]\.\d+|\d+)", text)
        if m:
            return min(1.0, float(m.group(1)))
    except Exception:
        pass
    return 0.0


def _gate_pairs(claim_text: str, papers: list[dict]) -> tuple[bool, str]:
    """Return (passed, reason). Fails if any pair scores < 0.55."""
    for p in papers:
        abstract = p.get("abstract") or p.get("summary") or p.get("title", "")
        score = _call_atom_alignment(claim_text, abstract)
        if score < 0.55:
            return False, f"Atom alignment {score:.2f} < 0.55 for arxiv:{p.get('arxiv_id','?')}"
    return True, ""


# ---------------------------------------------------------------------------
# Proposal type implementations
# ---------------------------------------------------------------------------

def propose_evidence_link(page_content: str, claims: list, program: str) -> ProposalResult:
    """
    EvidenceLink: pick an existing claim with weak evidence, find 2024-2025 papers.
    Returns papers to add as Evidence rows.
    """
    if not claims:
        return ProposalResult(
            proposal_type="evidence_link",
            payload=EvidenceLinkProposal(claim_id=0, papers=[]),
            gate_passed=False,
            gate_reason="no claims available",
        )

    # Pick a claim that needs evidence (prefer low-evidence ones)
    target_claim = claims[0]  # sorted by task.py (fewest evidence first)

    system = (
        "You are an astronomy research assistant. Find 2024-2025 published papers "
        "that directly support the given astronomy claim. Return JSON array only."
    )
    prompt = (
        f"Program context:\n{program[:500]}\n\n"
        f"Claim to support: {target_claim.text}\n\n"
        "Return a JSON array of up to 3 papers. Each: "
        '{"arxiv_id": "YYMM.NNNNN", "title": "...", "abstract": "...", '
        '"year": 2024, "stance": "supports"}. '
        "Only real papers from 2024-2025 with valid arXiv IDs."
    )

    try:
        raw = _call_astrosage(prompt, system)
        parsed = _extract_json(raw, expect="array")
        if isinstance(parsed, dict):
            # model returned an object wrapping a list
            parsed = parsed.get("papers", [])
        papers = [p for p in (parsed or []) if isinstance(p, dict) and p.get("arxiv_id")][:3]
    except Exception:
        papers = []

    if not papers:
        return ProposalResult(
            proposal_type="evidence_link",
            payload=EvidenceLinkProposal(claim_id=target_claim.id, papers=[]),
            gate_passed=False,
            gate_reason="proposer returned no valid papers",
        )

    passed, reason = _gate_pairs(target_claim.text, papers)
    return ProposalResult(
        proposal_type="evidence_link",
        payload=EvidenceLinkProposal(claim_id=target_claim.id, papers=papers),
        gate_passed=passed,
        gate_reason=reason,
    )


def propose_claim_insert(
    page_content: str,
    page_id: int,
    program: str,
    claim_type: str = "debate",
    missing_subtopics: list[str] | None = None,
    topic_hint: str | None = None,
) -> ProposalResult:
    """
    ClaimInsert: draft a new claim + supporting evidence.
    claim_type='debate' for contested findings, 'established' for subtopic coverage.
    topic_hint: orphan research idea question text (§16.4 rule 2) — guides AstroSage.
    """
    section_hint = ""
    debate_topic = None
    if claim_type == "established" and missing_subtopics:
        topic = missing_subtopics[0].replace("_", " ")
        section_hint = f"for the missing subtopic: {topic}"
    elif claim_type == "debate":
        if topic_hint:
            section_hint = f'on this research question: "{topic_hint[:200]}"'
        else:
            section_hint = "for an actively debated/contested finding in this field"

    system = (
        "You are an astronomy knowledge engineer. Draft a new wiki claim backed by evidence. "
        "Return JSON only. "
        "REQUIREMENT: the claim_text MUST contain a specific measurement, observation, or "
        "quantitative finding (e.g. a redshift value, stellar mass, percentage, timescale, "
        "or named survey/instrument result). Vague or qualitative-only claims are REJECTED."
    )
    prompt = (
        f"Program:\n{program[:600]}\n\n"
        f"Page excerpt:\n{page_content[:2000]}\n\n"
        f"Task: Draft ONE new {claim_type} claim {section_hint}. "
        "The claim_text must include a specific measurement or quantitative finding — "
        "not a vague statement. Cite the actual result (value, units, instrument, or survey). "
        "Include a debate_topic if contested.\n"
        "Return JSON:\n"
        '{"section": "Overview", "claim_text": "...", '
        '"debate_topic": "...|null", '
        '"papers": [{"arxiv_id": "...", "title": "...", "abstract": "...", "year": 2024, "stance": "supports"}]}'
    )

    try:
        raw = _call_astrosage(prompt, system)
    except Exception as exc:
        return ProposalResult(
            proposal_type="claim_insert",
            payload=ClaimInsertProposal(
                section="Overview", claim_text="", claim_type=claim_type,
                debate_topic=None, papers=[],
            ),
            gate_passed=False,
            gate_reason=f"proposer HTTP error: {type(exc).__name__}",
        )

    obj = _extract_json(raw, expect="object")
    if not isinstance(obj, dict):
        return ProposalResult(
            proposal_type="claim_insert",
            payload=ClaimInsertProposal(
                section="Overview", claim_text="", claim_type=claim_type,
                debate_topic=None, papers=[],
            ),
            gate_passed=False,
            gate_reason="proposer JSON parse failed",
        )
    claim_text = obj.get("claim_text", "").strip()
    debate_topic = obj.get("debate_topic") or None
    section = obj.get("section", "Overview")
    papers = [p for p in obj.get("papers", []) if isinstance(p, dict) and p.get("arxiv_id")][:3]

    if not claim_text or not papers:
        return ProposalResult(
            proposal_type="claim_insert",
            payload=ClaimInsertProposal(
                section=section, claim_text=claim_text, claim_type=claim_type,
                debate_topic=debate_topic, papers=papers,
            ),
            gate_passed=False,
            gate_reason="proposer: empty claim or no papers",
        )

    passed, reason = _gate_pairs(claim_text, papers)
    return ProposalResult(
        proposal_type="claim_insert",
        payload=ClaimInsertProposal(
            section=section,
            claim_text=claim_text,
            claim_type=claim_type,
            debate_topic=debate_topic,
            papers=papers,
        ),
        gate_passed=passed,
        gate_reason=reason,
    )


def propose_hero_upgrade(page_content: str, hero_facts_json: str | None, program: str) -> ProposalResult:
    """HeroFactUpgrade: replace/add one hero_facts entry with a quantitative finding."""
    existing = []
    try:
        existing = json.loads(hero_facts_json) if hero_facts_json else []
    except Exception:
        pass

    system = "You are an astronomy knowledge engineer. Draft a hero fact. Return JSON only."
    prompt = (
        f"Program:\n{program[:400]}\n\n"
        f"Current hero facts: {json.dumps(existing[:3])}\n\n"
        "Draft ONE new hero fact with a specific quantitative finding, range, or milestone. "
        "Return JSON: "
        '{"label": "...", "value": "...", "unit": "...", "kind": "range", '
        '"source": {"tier": "authoritative", "arxiv_id": "...", "year": 2024}}'
    )

    try:
        raw = _call_astrosage(prompt, system)
        new_fact = _extract_json(raw, expect="object")
        if not isinstance(new_fact, dict) or not new_fact.get("label") or not new_fact.get("value"):
            raise ValueError("missing label/value")
    except Exception:
        return ProposalResult(
            proposal_type="hero_upgrade",
            payload=HeroUpgradeProposal(new_hero_fact={}, replace_index=None),
            gate_passed=False,
            gate_reason="proposer: invalid hero fact JSON",
        )

    # Find weakest existing fact to replace (if len >= 3)
    replace_index = None
    if len(existing) >= 3:
        replace_index = 0  # replace first (usually most generic)

    return ProposalResult(
        proposal_type="hero_upgrade",
        payload=HeroUpgradeProposal(new_hero_fact=new_fact, replace_index=replace_index),
        gate_passed=True,
    )


def propose_section_rewrite(
    page_content: str,
    section_header: str,
    program: str,
    owned_claims_text: str = "",
    context_claims_text: str = "",
    page_id: int | None = None,
) -> ProposalResult:
    """SectionRewrite: rewrite one ## section with improved depth and citations."""
    # Extract current section content
    lines = page_content.split("\n")
    in_section = False
    section_lines: list[str] = []
    for line in lines:
        if line.startswith("## ") and section_header in line:
            in_section = True
        elif line.startswith("## ") and in_section:
            break
        if in_section:
            section_lines.append(line)
    current_section = "\n".join(section_lines[:50])

    evidence_map = ""
    if page_id is not None:
        try:
            from app.agent_loop.autowiki.citation_context import build_evidence_map
            from app.database import SessionLocal

            with SessionLocal() as db:
                evidence_map = build_evidence_map(db, page_id, max_rows=40, section=section_header)
        except Exception:
            evidence_map = ""

    system = (
        "You are an astronomy wiki editor writing at graduate-textbook depth. "
        "Rewrite the given section with maximum scientific specificity. "
        "Return markdown followed by a JSON marker report. "
        "HARD REQUIREMENTS — violating any disqualifies the response:\n"
        "  1. Minimum 400 words below the ## header.\n"
        "  2. At least 3 quantitative facts: redshifts, masses, luminosities, "
        "percentages, timescales, temperatures, or distances with units.\n"
        "  3. Do not write author-year parenthetical citations. Use only <!--cite:EVIDENCE_ID--> markers from the EVIDENCE MAP.\n"
        "  4. BANNED phrases: 'plays a crucial role', 'complex and dynamic', "
        "'plays an important role', 'is a fascinating', 'remains to be seen', "
        "'future work will', 'this page covers', 'in conclusion'.\n"
        "  5. You MUST weave HTML claim markers (e.g. <!--claim:123-->) inline immediately after asserting any of the provided 'owned' claims.\n"
        "  6. You MUST PRESERVE all trust/consensus HTML comments (e.g. <!--accepted-->, <!--consensus-->).\n"
        "  7. MUST output a valid JSON report at the end wrapped in <!--marker-report ... -->.\n"
    )
    prompt = (
        f"Program:\n{program[:400]}\n\n"
        f"{evidence_map}\n\n"
        f"Current section:\n{current_section}\n\n"
        f"Owned claims for this section:\n{owned_claims_text[:2000]}\n\n"
        f"Context claims (DO NOT force into this section):\n{context_claims_text[:2000]}\n\n"
        "Rewrite this section. Requirements:\n"
        "- Minimum 400 words below the ## header\n"
        "- At least 3 quantitative facts (numbers with units: redshifts, masses, percentages, etc.)\n"
        "- DO NOT write inline citations in (Author et al. Year) format\n"
        "- Cite only with <!--cite:EVIDENCE_ID--> markers from the EVIDENCE MAP; omit citations when no evidence ID is available\n"
        "- No filler phrases: 'plays a crucial role', 'complex and dynamic field', etc.\n"
        "- Surface active debates as explicit contested findings with named positions\n"
        "- Keep ## header unchanged, improve everything below it\n\n"
        "At the end of your response, you MUST include a marker report in exactly this format:\n"
        "<!--marker-report\n{\n  \"section\": \"Section Name\",\n  \"asserted_claim_ids\": [123, 124],\n  \"omitted_owned_claim_ids\": [{\"id\": 126, \"reason\": \"not asserted\"}]\n}\n-->"
    )

    try:
        # 2026-06-06: timeout raised 240→600s. AstroSage-70B on Apple Silicon
        # can take longer to load and generate 400+ words under concurrent GPU load.
        new_content = _call_astrosage(prompt, system, timeout=600)
        if len(new_content) < 100:
            raise ValueError("too short")
    except Exception:
        return ProposalResult(
            proposal_type="section_rewrite",
            payload=SectionRewriteProposal(section_header=section_header, new_content=""),
            gate_passed=False,
            gate_reason="proposer: section rewrite too short or failed",
        )

    return ProposalResult(
        proposal_type="section_rewrite",
        payload=SectionRewriteProposal(section_header=section_header, new_content=new_content),
        gate_passed=True,
    )
