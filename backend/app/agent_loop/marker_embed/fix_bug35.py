import re
file_path = "pipeline.py"
with open(file_path, "r") as f:
    content = f.read()

# Apply the pipeline fix
old_clean = """    clean_content = strip_markers(content)
    sections = parse_sections(clean_content)
    
    all_sentences_with_sections = []
    for s in sections:
        for sent in split_sentences(s.body):
            all_sentences_with_sections.append((sent, s.title))"""

new_clean = """    if section_key:
        import re
        sections = parse_sections(content)
        target_section_block = None
        for s in sections:
            s_key = re.sub(r'[^a-z0-9\\s]', '', s.title.replace('##', '').lower()).replace(' ', '_').strip()
            if s_key == section_key:
                target_section_block = s.body
                break
                
        if target_section_block is None:
            stats.status = "rolled_back"
            stats.notes = f"Section {section_key} not found"
            return None, stats
            
        clean_section = strip_markers(target_section_block)
        all_sentences_with_sections = [(sent, section_key) for sent in split_sentences(clean_section)]
        clean_content = content.replace(target_section_block, clean_section)
    else:
        clean_content = strip_markers(content)
        sections = parse_sections(clean_content)
        all_sentences_with_sections = []
        for s in sections:
            for sent in split_sentences(s.body):
                all_sentences_with_sections.append((sent, s.title))"""
content = content.replace(old_clean, new_clean)

old_align = """        # If we have section_key (we are repairing a specific section), we only align against that section block
        if section_key and section_key != claim_section:
            # We are repairing a specific section, and this claim doesn't belong to it. 
            # But the caller already filtered claims by section_key if it was provided!
            pass
            
        target_sentences = split_sentences(section_block)
        page_sentences = [s[0] for s in all_sentences_with_sections]
            
        alignment = align_claim_multipass(
            claim_id=claim_id,
            claim_text=claim_text,
            trust_level=trust_level,
            section_title=claim_section,
            section_candidates=target_sentences,
            page_candidates=page_sentences
        )"""

new_align = """        if section_key:
            target_sentences = [s[0] for s in all_sentences_with_sections]
            page_sentences = target_sentences
            align_section_title = section_key
        else:
            target_sentences = split_sentences(section_block)
            page_sentences = [s[0] for s in all_sentences_with_sections]
            align_section_title = claim_section
            
        alignment = align_claim_multipass(
            claim_id=claim_id,
            claim_text=claim_text,
            trust_level=trust_level,
            section_title=align_section_title,
            section_candidates=target_sentences,
            page_candidates=page_sentences
        )"""
content = content.replace(old_align, new_align)

with open(file_path, "w") as f:
    f.write(content)
