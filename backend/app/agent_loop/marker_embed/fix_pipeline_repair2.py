import re
file_path = "pipeline.py"
with open(file_path, "r") as f:
    content = f.read()

# Make it section-scoped
old_section_block = """        section_block = resolve_section(claim_section, sections)
        if section_block is None:
            log.info("pipeline: claim_id=%d section=%r -> rejected_no_section", claim_id, claim_section)
            stats.rejected_no_section += 1
            continue"""

new_section_block = """        section_block = None
        # In Phase 3, claim_section is actually the owner_section_key.
        # We need to find the matching section block.
        for s in sections:
            sec_key = re.sub(r'[^a-z0-9\s]', '', s.title.replace('##', '').lower()).replace(' ', '_').strip()
            if sec_key == claim_section:
                section_block = s.body
                break
                
        if section_block is None:
            log.info("pipeline: claim_id=%d section=%r -> rejected_no_section", claim_id, claim_section)
            stats.rejected_no_section += 1
            continue"""

content = content.replace(old_section_block, new_section_block)

# Fix the alignment target
old_align = """        alignment = align_claim_multipass(claim_text, section_block, all_sentences_with_sections)"""
new_align = """        # If we have section_key (we are repairing a specific section), we only align against that section block
        target_sentences = []
        if section_key:
            target_sentences = [(sent, claim_section) for sent in split_sentences(section_block)]
        else:
            target_sentences = all_sentences_with_sections
            
        alignment = align_claim_multipass(claim_text, section_block, target_sentences)"""

content = content.replace(old_align, new_align)

with open(file_path, "w") as f:
    f.write(content)
print("Patched pipeline.py for section-scope")
