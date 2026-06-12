#!/usr/bin/env python3
"""Add 5 strong quantitative hero facts to galaxy-evolution (page_id=57).

Uses Nutty (gpt-oss:20b) with fallback to Mima (qwen3.6:35b-a3b-nvfp4).
Appends to existing hero_facts rather than replacing them.
"""
import sys, os, json, urllib.request, re, time
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.database import SessionLocal
from app.models.page import WikiPage
from app.services.hero_facts import validate_hero_fact, _enrich_facts_with_trust
from app.services.llm_utils import strip_think_blocks

OLLAMA_URL = "http://localhost:11434/v1/chat/completions"
PAGE_SLUG = "galaxy-evolution"
PAGE_ID = 57
TARGET_NEW = 5

MODELS = [
    ("Nutty", "gpt-oss:20b"),
    ("Mima", "qwen3.6:35b-a3b-nvfp4"),
]

SYSTEM = """You are a precision astrophysics data extractor specializing in galaxy evolution.
Generate exactly 5 hero facts about galaxy evolution. Each fact must:
- Have a specific numeric value (no vague words like "millions", "billions", "many", "several")
- Use real physical units
- Be sourced from well-known observational astronomy results (Madau & Dickinson 2014, Planck 2018, SDSS, etc.)

FORBIDDEN in value field: "millions", "billions", "trillions", "thousands", "hundreds", "many", "few", "several", "numerous"
REQUIRED: numeric values only (decimals, scientific notation like "10¹⁰", ranges like "1–3")

Good examples:
{"label":"Cosmic Noon Redshift","value":"~1.9","unit":"z","kind":"scalar"}
{"label":"SFRD at z=0","value":"0.015","unit":"M☉/yr/Mpc³","kind":"scalar"}
{"label":"Schechter Mass M*","value":"10¹⁰·⁶","unit":"M☉","kind":"scalar"}

Return ONLY a JSON array of exactly 5 objects. Each object must have: label, value, unit, kind.
No thinking tags, no explanation."""

FORBIDDEN_VALUES = {
    "millions", "billions", "trillions", "thousands", "hundreds",
    "many", "few", "several", "numerous", "various", "large",
}


def log(msg):
    print(msg, flush=True)


def call_ollama(model: str, user: str, temperature: float = 0.15) -> str:
    payload = json.dumps({
        "model": model,
        "messages": [
            {"role": "system", "content": SYSTEM},
            {"role": "user", "content": user},
        ],
        "stream": False,
        "temperature": temperature,
        "options": {"num_predict": 800},
    }).encode()
    req = urllib.request.Request(
        OLLAMA_URL, data=payload,
        headers={"Content-Type": "application/json"}
    )
    with urllib.request.urlopen(req, timeout=180) as r:
        resp = json.loads(r.read())
    content = resp["choices"][0]["message"]["content"]
    # Strip <think>...</think> from deepseek / qwen3 responses
    content = strip_think_blocks(content)
    return content


def parse_json(raw: str) -> list:
    cleaned = raw.strip()
    if cleaned.startswith("```"):
        cleaned = cleaned.split("\n", 1)[1].rsplit("```", 1)[0].strip()
    m = re.search(r'\[.*\]', cleaned, re.DOTALL)
    if m:
        return json.loads(m.group())
    return json.loads(cleaned)


def is_valid_fact(f: dict) -> tuple[bool, str]:
    """Check basic structure and forbidden words before validate_hero_fact."""
    if not isinstance(f, dict):
        return False, "not a dict"
    if not f.get("label") or not str(f.get("value", "")).strip():
        return False, "missing label or value"
    value_lower = str(f.get("value", "")).lower()
    for bad in FORBIDDEN_VALUES:
        if bad in value_lower.split():
            return False, f"forbidden word '{bad}' in value"
    # Delegate to service validator
    ok, reason = validate_hero_fact({**f, "kind": f.get("kind", "scalar")})
    return ok, reason


def generate_facts(model: str, page_content: str) -> list[dict] | None:
    user_prompt = (
        f"Page: Galaxy Evolution\n\n"
        f"Content excerpt:\n{page_content[:2000]}\n\n"
        f"Generate exactly 5 precise quantitative hero facts about galaxy evolution. "
        f"Focus on: star formation rate density history, galaxy mass scales, "
        f"structural evolution, quenching timescales, merger rates, or redshift epochs. "
        f"Every value must be a number or number range. /no_think"
    )

    for attempt in range(2):
        try:
            t0 = time.time()
            raw = call_ollama(model, user_prompt, temperature=0.1 if attempt else 0.15)
            dt = time.time() - t0
            log(f"    attempt {attempt + 1} ({dt:.1f}s): {raw[:400]}")
            facts = parse_json(raw)
            if not isinstance(facts, list):
                log(f"    attempt {attempt + 1}: not a list")
                continue
            # Validate each fact
            valid = []
            for f in facts:
                ok, reason = is_valid_fact(f)
                if ok:
                    f.setdefault("kind", "scalar")
                    f["source"] = {
                        "tier": "ai_estimate",
                        "generator": model,
                        "flagged": False,
                        "reason": "Generated by local LLM; needs peer review",
                        "attribution": f"NebulaMind AI estimate via {model}",
                    }
                    valid.append(f)
                else:
                    log(f"    rejected [{f.get('label', '?')}]: {reason}")
            if len(valid) >= 3:
                return valid
            log(f"    only {len(valid)} valid facts, retrying")
        except Exception as e:
            log(f"    attempt {attempt + 1} error: {e}")

    return None


def main():
    db = SessionLocal()
    try:
        page = db.query(WikiPage).filter(WikiPage.slug == PAGE_SLUG).first()
        if not page:
            log(f"ERROR: page '{PAGE_SLUG}' not found")
            return

        # Load existing hero_facts
        existing = []
        if page.hero_facts:
            raw = page.hero_facts
            if isinstance(raw, str):
                existing = json.loads(raw)
            elif isinstance(raw, list):
                existing = raw
        log(f"Existing hero_facts: {len(existing)} items")
        for i, f in enumerate(existing):
            log(f"  [{i}] {f.get('label')}: {f.get('value')} {f.get('unit', '')}")

        # Try each model
        new_facts = None
        for agent_name, model in MODELS:
            log(f"\n--- Trying {agent_name} ({model}) ---")
            new_facts = generate_facts(model, page.content or "")
            if new_facts:
                log(f"  {agent_name} produced {len(new_facts)} valid facts")
                break
            log(f"  {agent_name} failed, trying next model")

        if not new_facts:
            log("All models failed. Falling back to hand-curated facts.")
            new_facts = _FALLBACK_FACTS

        # Deduplicate by label
        existing_labels = {f.get("label", "").lower() for f in existing}
        to_add = [f for f in new_facts if f.get("label", "").lower() not in existing_labels]
        to_add = to_add[:TARGET_NEW]

        log(f"\nAdding {len(to_add)} new facts:")
        for f in to_add:
            log(f"  {f.get('label')}: {f.get('value')} {f.get('unit', '')} [{f.get('kind')}]")

        merged = existing + to_add
        # Enrich with trust levels from claims
        merged = _enrich_facts_with_trust(page, db, merged)
        page.hero_facts = json.dumps(merged, ensure_ascii=False)
        db.commit()
        log(f"\nSaved. hero_facts now has {len(merged)} items.")

    except Exception as e:
        db.rollback()
        log(f"Fatal error: {e}")
        import traceback; traceback.print_exc()
        raise
    finally:
        db.close()


# Authoritative fallback if all LLM models fail
_FALLBACK_FACTS = [
    {
        "label": "Cosmic Noon Redshift",
        "value": "~1.9", "unit": "z", "kind": "scalar",
        "source": {
            "tier": "authoritative",
            "authority": "Madau & Dickinson 2014",
            "reference_url": "https://doi.org/10.1146/annurev-astro-081811-125615",
            "reference_title": "Madau & Dickinson (2014): Cosmic Star-Formation History",
            "retrieval_year": 2014,
            "attribution": "Madau & Dickinson (2014) ARA&A 52",
        },
    },
    {
        "label": "SFRD at z=0",
        "value": 0.015, "unit": "M☉/yr/Mpc³", "kind": "scalar",
        "source": {
            "tier": "authoritative",
            "authority": "Madau & Dickinson 2014",
            "reference_url": "https://doi.org/10.1146/annurev-astro-081811-125615",
            "reference_title": "Madau & Dickinson (2014): Cosmic Star-Formation History",
            "retrieval_year": 2014,
            "attribution": "Madau & Dickinson (2014) ARA&A 52",
        },
    },
    {
        "label": "Schechter Mass M*",
        "value": "10¹⁰·⁶", "unit": "M☉", "kind": "scalar",
        "source": {
            "tier": "authoritative",
            "authority": "Baldry et al. 2012",
            "reference_url": "https://doi.org/10.1111/j.1365-2966.2012.20340.x",
            "reference_title": "Baldry et al. (2012): GAMA galaxy stellar mass function at z<0.06",
            "retrieval_year": 2012,
            "attribution": "Baldry et al. (2012) MNRAS 421",
        },
    },
    {
        "label": "Galaxy Size at z=2",
        "value_min": 0.5, "value_max": 2.0, "unit": "kpc", "kind": "range", "scale": "linear",
        "value": "0.5–2.0",
        "qualifier": "effective radius of quiescent galaxies",
        "source": {
            "tier": "authoritative",
            "authority": "van Dokkum et al. 2008",
            "reference_url": "https://doi.org/10.1086/587033",
            "reference_title": "van Dokkum et al. (2008): Confirmation of the remarkable compactness of massive quiescent galaxies at z~2.3",
            "retrieval_year": 2008,
            "attribution": "van Dokkum et al. (2008) ApJ 677",
        },
    },
    {
        "label": "Quenching Timescale",
        "value_min": 1.0, "value_max": 3.0, "unit": "Gyr", "kind": "range", "scale": "linear",
        "value": "1–3",
        "qualifier": "rapid quenching of star formation in massive galaxies",
        "source": {
            "tier": "authoritative",
            "authority": "Belli et al. 2019",
            "reference_url": "https://doi.org/10.3847/1538-4357/ab14ee",
            "reference_title": "Belli et al. (2019): MOSDEF survey — quenching timescales at z~2",
            "retrieval_year": 2019,
            "attribution": "Belli et al. (2019) ApJ 874",
        },
    },
]


if __name__ == "__main__":
    main()
