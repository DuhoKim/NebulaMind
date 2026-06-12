import re
file_path = "tasks.py"
with open(file_path, "r") as f:
    content = f.read()

old_call = """from app.models.claim import Claim as ClaimModel
                page_claims = db.query(ClaimModel).filter(ClaimModel.page_id == page_id).order_by(ClaimModel.created_at.desc()).limit(200).all()
                claims_text = "\\n".join(f"<!--claim:{c.id}--> [{c.trust_level}] {c.text[:200]}" for c in page_claims)
                proposal = propose_section_rewrite(page.content, section_header, program, claims_text)"""

new_call = """from sqlalchemy import text
                sec_key = re.sub(r'[^a-z0-9\\s]', '', section_header.replace('##', '').lower()).replace(' ', '_').strip()
                owned_res = db.execute(text(\"\"\"
                    SELECT c.id, c.trust_level, c.text 
                    FROM claim_section_assignments a
                    JOIN claims c ON c.id = a.claim_id
                    WHERE a.page_id = :pid AND a.owner_section_key = :sec_key AND a.assignment_status = 'active'
                \"\"\"), {"pid": page_id, "sec_key": sec_key}).fetchall()
                
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
                \"\"\"), {"pid": page_id, "sec_key": sec_key}).fetchall()
                context_claims_text = "\\n".join(f"<!--claim:{c.id}--> [{c.trust_level}] {c.text[:200]}" for c in context_res)

                proposal = propose_section_rewrite(page.content, section_header, program, owned_claims_text, context_claims_text)
                
                # Check gate
                raw_text = proposal.get("content", "")
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
                            logger.warning(f"[autowiki_tick] Missing must_keep claims unaccounted for in proposer: {unaccounted}")
                            proposal["reject_reason"] = "missing_must_keep_claims"
                    except Exception as e:
                        pass
                else:
                    proposal["reject_reason"] = "missing_marker_report"
                """

content = content.replace(old_call, new_call)

with open(file_path, "w") as f:
    f.write(content)
print("Updated autowiki_tick call")
