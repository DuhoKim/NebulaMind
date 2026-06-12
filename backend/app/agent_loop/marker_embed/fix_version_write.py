import re
file_path = "tasks.py"
with open(file_path, "r") as f:
    content = f.read()

# I will encode the section_key into the notes column so it logs section-level counts without a schema migration.
old_run_log = """                ) VALUES (
                    :page_id, :page_version, :source_version,
                    :total_claims, :matched_claims,
                    :rej_conf, :rej_sec, :rej_ambig, :rej_val,
                    :mean_conf, :judge_pct, :cov_pct,
                    :status, :started_at, :finished_at, :notes,
                    :asserted_count, :topical_anchor_count, :tier_breakdown
                )"""

new_run_log = """                ) VALUES (
                    :page_id, :page_version, :source_version,
                    :total_claims, :matched_claims,
                    :rej_conf, :rej_sec, :rej_ambig, :rej_val,
                    :mean_conf, :judge_pct, :cov_pct,
                    :status, :started_at, :finished_at, :notes,
                    :asserted_count, :topical_anchor_count, :tier_breakdown
                )"""

old_notes_bind = """:notes": stats.notes,"""
new_notes_bind = """:notes": stats.notes if not section_key else f"Section repair: {section_key}. " + stats.notes,"""
content = content.replace(old_notes_bind, new_notes_bind)

with open(file_path, "w") as f:
    f.write(content)
