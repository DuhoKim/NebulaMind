import hashlib
import json
import re
from pathlib import Path

BASE = Path("/Users/duhokim/NebulaMind/NebulaMind/.hermes/handoffs/galaxy-evolution/mastermind/aas-autopilot/dr-revised-20260714")
ROUND1 = BASE / "round1"
ROUND2 = BASE / "round2"
RECEIPTS = ROUND2 / "receipts"
PAPERS = (1, 2, 9)


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def measured_numeric_lines(text: str) -> list[str]:
    start = text.index("\\section{Shared parent sample and selection function}")
    end = text.index("\\begin{figure", start)
    return [line for line in text[start:end].splitlines() if re.search(r"\d", line)]


def cited_keys(text: str) -> set[str]:
    keys: set[str] = set()
    for match in re.finditer(r"\\cite[a-zA-Z*]*(?:\[[^]]*\])*(?:\{([^}]+)\})", text):
        keys.update(key.strip() for key in match.group(1).split(",") if key.strip())
    return keys


def main() -> None:
    rows = []
    for number in PAPERS:
        paper_id = f"paper_{number:02d}"
        source_path = ROUND1 / f"{paper_id}_r1.tex"
        review_path = ROUND1 / "dr-review-packets" / f"{paper_id}_round1_review_dr_packet.md"
        output_path = ROUND2 / f"{paper_id}_r2.tex"
        receipt_path = RECEIPTS / f"{paper_id}_sources.json"
        note_path = RECEIPTS / f"{paper_id}_revision.md"
        source = source_path.read_text()
        output = output_path.read_text()
        receipt = json.loads(receipt_path.read_text())

        invariants = measured_numeric_lines(source)
        missing_invariant_lines = [line for line in invariants if output.splitlines().count(line) != source.splitlines().count(line)]
        cites = cited_keys(output)
        bib = re.findall(r"\\bibitem(?:\[[^]]*\])?\{([^}]+)\}", output)
        expected_flags = {
            "association_not_causal": True,
            "real_data_only": True,
            "drafts_only": True,
            "local_only": True,
            "browser_or_account_touched": False,
            "broker_touched": False,
            "publish_commit_git_performed": False,
            "analysis_measurements_recomputed": False,
        }
        receipt_flags_match = all(receipt.get(key) == value for key, value in expected_flags.items())
        source_hash_field = receipt.get("source_round1_tex_sha256", receipt.get("source_tex_sha256"))
        review_hash_field = receipt.get("source_round1_dr_review_sha256", receipt.get("review_packet_sha256"))

        special_checks = []
        if number == 1:
            special_checks = [
                "\\citep{duartepuertas2017,zibetti2026,belfiore2018}" in output,
                "\\citep{demellos2024}" in output,
                "\\citep{gatto2025}" in output,
                "not evidence that AGN activity caused host-wide quenching" in output,
            ]
        elif number == 2:
            special_checks = [
                "comparison between observable spectroscopic density quartiles" in output,
                "no lower-limit claim is made here" in output,
                "\\citep{goubert2024,goubert2024corr}" in output,
                "\\citep{okane2024}" in output,
                "\\citep{oxland2024,sampaio2024}" in output,
            ]
        else:
            special_checks = [
                "MNRAS, 518, 2605" not in output,
                "{imanga2023}" not in output,
                "{nanni2023imanga}" in output,
                "\\citep{hirschmann2023}" in output,
                "\\citep{vijayan2023}" in output,
                "this vector alone cannot identify a unique causal mechanism" in output,
            ]

        row = {
            "paper_id": paper_id,
            "artifacts_exist": all(path.exists() for path in (source_path, review_path, output_path, receipt_path, note_path)),
            "source_round1_sha_match": source_hash_field == sha(source_path),
            "review_packet_sha_match": review_hash_field == sha(review_path),
            "output_sha_match": receipt.get("output_tex_sha256") == sha(output_path),
            "measured_numeric_line_count": len(invariants),
            "measured_numeric_lines_preserved_exact": not missing_invariant_lines,
            "missing_or_changed_invariant_lines": missing_invariant_lines,
            "undefined_citations": sorted(cites - set(bib)),
            "duplicate_bibkeys": sorted({key for key in bib if bib.count(key) > 1}),
            "brace_delta": output.count("{") - output.count("}"),
            "begin_end_delta": len(re.findall(r"\\begin\{", output)) - len(re.findall(r"\\end\{", output)),
            "receipt_flags_match": receipt_flags_match,
            "special_review_fixes_present": all(special_checks),
            "output_sha256": sha(output_path),
        }
        row["pass"] = (
            row["artifacts_exist"]
            and row["source_round1_sha_match"]
            and row["review_packet_sha_match"]
            and row["output_sha_match"]
            and row["measured_numeric_lines_preserved_exact"]
            and not row["undefined_citations"]
            and not row["duplicate_bibkeys"]
            and row["brace_delta"] == 0
            and row["begin_end_delta"] == 0
            and row["receipt_flags_match"]
            and row["special_review_fixes_present"]
        )
        rows.append(row)

    result = {"status": "PASS" if all(row["pass"] for row in rows) else "FAIL", "papers": rows}
    RECEIPTS.mkdir(parents=True, exist_ok=True)
    (RECEIPTS / "ROUND2_VALIDATION.json").write_text(json.dumps(result, indent=2, sort_keys=True) + "\n")
    print(json.dumps(result, sort_keys=True))
    raise SystemExit(0 if result["status"] == "PASS" else 1)


if __name__ == "__main__":
    main()
