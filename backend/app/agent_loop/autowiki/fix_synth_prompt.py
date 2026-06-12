import re
file_path = "../tasks.py"
with open(file_path, "r") as f:
    content = f.read()

# Update synthesize_renovation system prompt
old_sys = """SYNTH_SYSTEM = (
    "You are an expert astronomy wiki editor. Your task is to write a highly specific, graduate-level "
    "astronomy wiki section based heavily on the provided evidence and existing claims.\n\n"
    "Requirements:\n"
    "- High scientific density: include specific redshifts, masses, temperatures, timescales, or physical limits.\n"
    "- Citations MUST be given inline strictly as (Author et al. YYYY).\n"
    "- No narrative fluff: DO NOT use 'fascinating', 'plays a crucial role', 'in summary', or 'recent studies show'.\n"
    "- Every sentence should impart a fact, constraint, or physical model.\n"
    "- Preserve any existing accepted/consensus claims in the section.\n"
    "- You MUST PRESERVE any existing HTML claim markers (e.g. <!--claim:123-->) from the current section.\n"
    "- You MUST weave HTML claim markers inline immediately after asserting any of the provided key claims (e.g. <!--claim:xxx-->).\n"
    "- Do NOT invent papers or unsourced claims.\n"
    "- Output ONLY the rewritten section starting with ## {section_to_rewrite}\n"
    "- 6-10 distinct claim sentences with citations.\n"
)"""

new_sys = """SYNTH_SYSTEM = (
    "You are an expert astronomy wiki editor. Your task is to write a highly specific, graduate-level "
    "astronomy wiki section based heavily on the provided evidence and existing claims.\n\n"
    "Requirements:\n"
    "- High scientific density: include specific redshifts, masses, temperatures, timescales, or physical limits.\n"
    "- Citations MUST be given inline strictly as (Author et al. YYYY).\n"
    "- No narrative fluff: DO NOT use 'fascinating', 'plays a crucial role', 'in summary', or 'recent studies show'.\n"
    "- Every sentence should impart a fact, constraint, or physical model.\n"
    "- You MUST PRESERVE all trust/consensus HTML comments (e.g. <!--accepted-->, <!--consensus-->).\n"
    "- You MUST weave HTML claim markers inline immediately after asserting any of the provided 'owned' claims (e.g. <!--claim:123-->).\n"
    "- Do NOT invent papers or unsourced claims.\n"
    "- Output ONLY the rewritten section starting with ## {section_to_rewrite}\n"
    "- 6-10 distinct claim sentences with citations.\n"
    "- MUST output a valid JSON report at the end wrapped in <!--marker-report ... -->.\n"
)"""
content = content.replace(old_sys, new_sys)

# Update the user query in synthesize_renovation
old_query = """        from app.models.claim import Claim as ClaimModel
        page_claims = db.query(ClaimModel).filter(ClaimModel.page_id == page.id).order_by(ClaimModel.created_at.desc()).limit(200).all()
        claims_text = "\\n".join(f"<!--claim:{c.id}--> [{c.trust_level}] {c.text[:200]}" for c in page_claims)

        user_msg = f\"\"\"Available evidence (arXiv, last 3 years):
{evidence_text}

Key claims on this page:
{claims_text}

Missing subtopics to address (if applicable):
{missing_text}

Rewrite the section '## {section_to_rewrite}'.\"\"\""""

new_query = """        from sqlalchemy import text
        sec_key = re.sub(r'[^a-z0-9\\s]', '', section_to_rewrite.lower()).replace(' ', '_').strip()
        owned_res = db.execute(text(\"\"\"
            SELECT c.id, c.trust_level, c.text 
            FROM claim_section_assignments a
            JOIN claims c ON c.id = a.claim_id
            WHERE a.page_id = :pid AND a.owner_section_key = :sec_key AND a.assignment_status = 'active'
        \"\"\"), {"pid": page.id, "sec_key": sec_key}).fetchall()
        
        must_keep = [r for r in owned_res if r.trust_level in ('accepted', 'consensus')]
        optional = [r for r in owned_res if r.trust_level not in ('accepted', 'consensus')]
        
        owned_claims_text = "Must-Keep Owned Claims:\\n" + "\\n".join(f"<!--claim:{c.id}--> [{c.trust_level}] {c.text[:200]}" for c in must_keep) + "\\n\\n"
        owned_claims_text += "Optional Owned Claims:\\n" + "\\n".join(f"<!--claim:{c.id}--> [{c.trust_level}] {c.text[:200]}" for c in optional)
        
        context_res = db.execute(text(\"\"\"
            SELECT c.id, c.trust_level, c.text 
            FROM claim_section_assignments a
            JOIN claims c ON c.id = a.claim_id
            WHERE a.page_id = :pid AND a.owner_section_key != :sec_key AND a.assignment_status = 'active'
            LIMIT 10
        \"\"\"), {"pid": page.id, "sec_key": sec_key}).fetchall()
        context_claims_text = "\\n".join(f"<!--claim:{c.id}--> [{c.trust_level}] {c.text[:200]}" for c in context_res)

        user_msg = f\"\"\"Available evidence (arXiv, last 3 years):
{evidence_text}

Owned claims for this section:
{owned_claims_text}

Context claims (DO NOT force into this section):
{context_claims_text}

Missing subtopics to address (if applicable):
{missing_text}

Rewrite the section '## {section_to_rewrite}'.
At the end of your response, you MUST include a marker report in exactly this format:
<!--marker-report
{{
  "section": "Section Name",
  "asserted_claim_ids": [123, 124],
  "omitted_owned_claim_ids": [{{"id": 126, "reason": "not asserted"}}]
}}
-->\"\"\""""

content = content.replace(old_query, new_query)

# Update the parsing logic
old_accept = """        new_section_text = response.content[0].text.strip()
        
        plan.status = "verifying"
        plan.proposed_content = new_section_text"""

new_accept = """        raw_text = response.content[0].text.strip()
        
        report_match = re.search(r"<!--marker-report\\s*({.*?})\\s*-->", raw_text, re.DOTALL)
        if report_match:
            try:
                import json
                report = json.loads(report_match.group(1))
                asserted = set(report.get("asserted_claim_ids", []))
                must_keep_ids = {r.id for r in must_keep}
                missing_must_keep = must_keep_ids - asserted
                omitted = report.get("omitted_owned_claim_ids", [])
                omitted_with_reason = {o["id"] for o in omitted if "id" in o and o.get("reason")}
                unaccounted = missing_must_keep - omitted_with_reason
                if unaccounted:
                    logger.warning(f"[synthesize_renovation] Missing must_keep claims unaccounted for: {unaccounted}")
                    # Could reject, but synth creates a proposal plan, so we'll just log and strip.
            except Exception as e:
                pass
                
        new_section_text = re.sub(r"<!--marker-report.*?-->", "", raw_text, flags=re.DOTALL).strip()
        
        plan.status = "verifying"
        plan.proposed_content = new_section_text"""

content = content.replace(old_accept, new_accept)

with open(file_path, "w") as f:
    f.write(content)
print("Updated synthesize_renovation prompt")
