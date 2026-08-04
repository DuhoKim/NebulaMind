import hashlib
import json
import re
from pathlib import Path

ROOT = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot")
ROUND = ROOT / "dr-revised-20260714/round1"
INPUTS = json.loads((ROUND / "ROUND1_INPUTS.json").read_text())
CANDIDATES = json.loads((ROUND / "ROUND1_PACKET_SOURCE_CANDIDATES.json").read_text())
CANDIDATE_COUNTS = {row["paper_id"]: len(row["sources"]) for row in CANDIDATES["papers"]}


def digest(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def is_subsequence(original, revised):
    cursor = 0
    for line in revised:
        if cursor < len(original) and line == original[cursor]:
            cursor += 1
    return cursor == len(original)


def main():
    rows = []
    for paper in range(1, 10):
        item = INPUTS["inputs"][paper - 1]
        paper_id = f"paper_{paper:02d}"
        src_path = Path(item["source_tex"])
        packet_path = Path(item["source_packet"])
        out_path = Path(item["round1_output"])
        receipt_path = ROUND / "receipts" / f"{paper_id}_sources.json"
        note_path = ROUND / "receipts" / f"{paper_id}_revision.md"
        out = out_path.read_text()
        src = src_path.read_text()
        receipt = json.loads(receipt_path.read_text())
        citep = set()
        for match in re.finditer(r"\\citep(?:\[[^]]*\])?(?:\[[^]]*\])?\{([^}]*)\}", out):
            citep.update(key.strip() for key in match.group(1).split(","))
        bib = re.findall(r"\\bibitem(?:\[[^]]*\])?\{([^}]*)\}", out)
        added = receipt.get("added_sources", [])
        added_keys = [str(row["citation_key"]) for row in added if isinstance(row, dict) and row.get("citation_key")]
        selected_numbers = [int(row["source_number"]) for row in added if isinstance(row, dict) and isinstance(row.get("source_number"), int)]
        skipped_numbers = [int(row["source_number"]) for row in receipt.get("skipped_sources", []) if isinstance(row, dict) and isinstance(row.get("source_number"), int)]
        row = {
            "paper_id": paper_id,
            "artifacts_exist": out_path.exists() and receipt_path.exists() and note_path.exists(),
            "source_tex_sha_match": digest(src_path) == item["source_tex_sha256"] == receipt["source_tex_sha256"],
            "source_packet_sha_match": digest(packet_path) == item["source_packet_sha256"] == receipt["source_packet_sha256"],
            "output_sha_match": digest(out_path) == receipt["output_tex_sha256"],
            "original_lines_preserved": is_subsequence(src.splitlines(keepends=True), out.splitlines(keepends=True)),
            "undefined_cites": sorted(citep - set(bib)),
            "duplicate_bibkeys": sorted({key for key in bib if bib.count(key) > 1}),
            "added_keys_not_cited_with_citep": sorted(set(added_keys) - citep),
            "brace_delta": out.count("{") - out.count("}"),
            "begin_end_delta": len(re.findall(r"\\begin\{", out)) - len(re.findall(r"\\end\{", out)),
            "source_accounting_complete": sorted(selected_numbers + skipped_numbers) == list(range(1, CANDIDATE_COUNTS[paper_id] + 1)),
            "source_accounting_unique": len(selected_numbers + skipped_numbers) == len(set(selected_numbers + skipped_numbers)),
            "flags": {key: receipt.get(key) for key in ("original_lines_preserved_in_order", "association_not_causal", "real_data_only", "drafts_only")},
            "added_source_count": len(added),
            "skipped_source_count": len(skipped_numbers),
            "output_sha256": digest(out_path),
        }
        row["pass"] = (
            row["artifacts_exist"]
            and row["source_tex_sha_match"]
            and row["source_packet_sha_match"]
            and row["output_sha_match"]
            and row["original_lines_preserved"]
            and not row["undefined_cites"]
            and not row["duplicate_bibkeys"]
            and not row["added_keys_not_cited_with_citep"]
            and row["brace_delta"] == 0
            and row["begin_end_delta"] == 0
            and row["source_accounting_complete"]
            and row["source_accounting_unique"]
            and all(value is True for value in row["flags"].values())
        )
        rows.append(row)
    result = {"status": "PASS" if all(row["pass"] for row in rows) else "FAIL", "rows": rows}
    (ROUND / "receipts" / "ROUND1_VALIDATION.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True))
    raise SystemExit(0 if result["status"] == "PASS" else 1)


if __name__ == "__main__":
    main()
