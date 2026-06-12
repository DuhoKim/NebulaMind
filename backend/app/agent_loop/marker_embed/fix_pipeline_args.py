file_path = "tasks.py"
with open(file_path, "r") as f:
    content = f.read()

# Pass section_key and expected_source_version to run_pipeline
old_call = """        new_content, stats = run_pipeline(
            page_id=page_id,
            content=content,
            claims=claims,
            source_version=source_version,
        )"""

new_call = """        if expected_source_version and source_version != expected_source_version:
            log.warning("[claim_marker] Version mismatch: expected %s, got %s. Aborting.", expected_source_version, source_version)
            return {"status": "aborted_version_mismatch"}
            
        new_content, stats = run_pipeline(
            page_id=page_id,
            content=content,
            claims=claims,
            source_version=source_version,
            section_key=section_key
        )"""

content = content.replace(old_call, new_call)
with open(file_path, "w") as f:
    f.write(content)
