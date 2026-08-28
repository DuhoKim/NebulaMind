#!/usr/bin/env python3
from pathlib import Path
import hashlib
import json

ROOT = Path("/Users/duhokim/NebulaMind/NebulaMind")
HERE = Path(__file__).resolve().parent
QA = HERE / "qa"

checks = {}
errors = []


def load(name):
    return json.loads((HERE / name).read_text())


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()

required = [
    "STATUS.json",
    "SOURCE_FREEZE.json",
    "NUMERIC_SOURCE_AUDIT.json",
    "FRAME_DIAGNOSIS.md",
    "PREORDER_CUSTODY.md",
    "STORYBOARD_CANDIDATE.json",
    "CANDIDATE_NOTES.md",
    "visual_proposal_v1.png",
    "visual_proposal_v2.png",
    "visual_proposal_v3.png",
    "visual_proposal_v4.png",
    "visual_proposal_v5.png",
    "visual_proposal_v6.png",
    "visual_proposal_v7.png",
    "visual_proposal_v8.png",
    "qa/visual_proposal_qa.json",
    "qa/proposal_validation.json",
    "qa/encoded_target_qa.json",
    "qa/deepening-pass2-encoded/AUDIT.json",
    "qa/deepening-pass2-encoded/ENCODED_FRAME_AUDIT.md",
    "qa/deepening-pass2-encoded/contact_sheet_20frames.jpg",
    "qa/deepening-pass3-encoded/AUDIT.json",
    "qa/deepening-pass3-encoded/ENCODED_FRAME_AUDIT.md",
    "qa/deepening-pass3-encoded/contact_sheet_32frames.jpg",
    "qa/deepening-pass3-encoded/FRAME_HASHES.json",
    "qa/PASS3_LOCAL_GATE.json",
    "qa/deepening-pass4-encoded/AUDIT.json",
    "qa/deepening-pass4-encoded/ENCODED_FRAME_AUDIT.md",
    "qa/deepening-pass4-encoded/contact_sheet_32frames_offset2.jpg",
    "qa/deepening-pass4-encoded/FRAME_HASHES.json",
    "qa/PASS4_LOCAL_GATE.json",
    "qa/PASS4_PACKET_SYNC.json",
    "qa/PASS4_PACKET_SYNC_V1_FAIL.json",
    "qa/PASS4_PACKET_SYNC_V1_PASS.json",
    "qa/PASS4_CITATION_GATE.json",
    "qa/PASS4_CITATION_GATE_V1_FAIL.json",
    "qa/PASS4_VALIDATOR_CUSTODY.json",
    "qa/deepening-pass5-encoded/AUDIT.json",
    "qa/deepening-pass5-encoded/ENCODED_FRAME_AUDIT.md",
    "qa/deepening-pass5-encoded/contact_sheet_32frames_offset1.jpg",
    "qa/deepening-pass5-encoded/FRAME_HASHES.json",
    "qa/PASS5_LOCAL_GATE.json",
    "qa/PASS5_PACKET_SYNC.json",
    "qa/PASS5_CITATION_GATE.json",
    "qa/PASS5_VALIDATOR_CUSTODY.json",
    "qa/deepening-pass6-encoded/AUDIT.json",
    "qa/deepening-pass6-encoded/ENCODED_FRAME_AUDIT.md",
    "qa/deepening-pass6-encoded/contact_sheet_32frames_offset3.jpg",
    "qa/deepening-pass6-encoded/FRAME_HASHES.json",
    "qa/deepening-pass6-encoded/SCENE_HOLDS.json",
    "qa/PASS6_LOCAL_GATE.json",
    "qa/PASS6_PACKET_SYNC.json",
    "qa/PASS6_CITATION_GATE.json",
    "qa/PASS6_VALIDATOR_CUSTODY.json",
    "qa/deepening-pass7-encoded/AUDIT.json",
    "qa/deepening-pass7-encoded/ENCODED_FRAME_AUDIT.md",
    "qa/deepening-pass7-encoded/FRAME_HASHES.json",
    "qa/deepening-pass7-encoded/BOUNDARY_CONTINUITY.json",
    "qa/deepening-pass7-encoded/OCR_DENSITY.json",
    "qa/PASS7_V2_CUSTODY_CHECKS.json",
    "qa/PASS7_V2_PACKET_PROJECTION_CHECKS.json",
    "qa/PASS7_V2_CITATION_CHECKS.json",
    "qa/PASS7_V2_CONTINUITY_CAUSALITY_CHECKS.json",
    "qa/PASS7_V2_VALIDATOR_CHECKS.json",
    "qa/PASS7_V2_LOCAL_CHECKS.json",
    "qa/PASS7_V3_CUSTODY_CHECKS.json",
    "qa/PASS7_V3_PACKET_PROJECTION_CHECKS.json",
    "qa/PASS7_V3_CITATION_CHECKS.json",
    "qa/PASS7_V3_CONTINUITY_CAUSALITY_CHECKS.json",
    "qa/PASS7_V3_VALIDATOR_CHECKS.json",
    "qa/PASS7_V3_LOCAL_CHECKS.json",
    "qa/PASS7_V4_CUSTODY_CHECKS.json",
    "qa/PASS7_V4_PACKET_PROJECTION_CHECKS.json",
    "qa/PASS7_V4_CITATION_CHECKS.json",
    "qa/PASS7_V4_CONTINUITY_CAUSALITY_CHECKS.json",
    "qa/PASS7_V4_VALIDATOR_CHECKS.json",
    "qa/PASS7_V4_LOCAL_CHECKS.json",
    "qa/PASS7_V5_CUSTODY_CHECKS.json",
    "qa/PASS7_V5_PACKET_PAYLOAD_CHECKS.json",
    "qa/PASS7_V5_CITATION_CHECKS.json",
    "qa/PASS7_V5_CONTINUITY_SEMANTIC_CHECKS.json",
    "qa/PASS7_V5_VALIDATOR_CHECKS.json",
    "qa/PASS7_V5_LOCAL_CHECKS.json",
    "qa/PASS7_V6_CUSTODY_CHECKS.json",
    "qa/PASS7_V6_PACKET_PAYLOAD_CHECKS.json",
    "qa/PASS7_V6_CITATION_CHECKS.json",
    "qa/PASS7_V6_CONTINUITY_SEMANTIC_CHECKS.json",
    "qa/PASS7_V6_VALIDATOR_CHECKS.json",
    "qa/PASS7_V6_LOCAL_CHECKS.json",
    "qa/PASS7_V7_CUSTODY_INVENTORY_CHECKS.json",
    "qa/PASS7_V8_LOCAL_CHECKS.json",
    "qa/PASS7_V11_LOCAL_CHECKS.json",
    "qa/PASS7_V12_LOCAL_CHECKS.json",
    "qa/PASS7_V13_LOCAL_CHECKS.json",
    "qa/PASS7_V14_LOCAL_CHECKS.json",
    "qa/PASS7_V15_LOCAL_CHECKS.json",
    "qa/PASS7_V16_LOCAL_CHECKS.json",
    "qa/PASS7_V17_LOCAL_CHECKS.json",
    "qa/PASS7_V18_LOCAL_CHECKS.json",
    "qa/PASS7_V19_LOCAL_CHECKS.json",
    "qa/PASS7_V20_LOCAL_CHECKS.json",
    "qa/PASS7_V21_LOCAL_CHECKS.json",
    "qa/PASS7_V22_LOCAL_CHECKS.json",
    "qa/PASS7_V23_LOCAL_CHECKS.json",
    "qa/PASS7_V24_LOCAL_CHECKS.json",
    "qa/PASS7_V25_LOCAL_CHECKS.json",
    "qa/PASS7_V26_LOCAL_CHECKS.json",
    "qa/PASS7_V27_LOCAL_CHECKS.json",
    "qa/PASS7_V28_LOCAL_CHECKS.json",
    "qa/HISTORICAL_LOCAL_RECEIPT_INDEX_V28.json",
    "qa/EXTERNAL_CANDIDATE_CUSTODY.json",
    "SNAPSHOT_SCOPE.md",
    "frozen_sources/pass7/MANIFEST.json",
    "qa/PASS7_VALIDATOR_MUTATION_TESTS.json",
    "qa/APPROVED_STORYBOARD_CONTRACT.json",
    "qa/PASS7_V2_ADDITIONAL_FALSE_PATHS.json",
    "qa/PAPER_NAIVE_RESULT_PASS7_V1.json",
    "qa/ADVERSARIAL_RESULT_PASS7_V1.json",
    "qa/PAPER_NAIVE_RESULT_PASS7_V2.json",
    "qa/ADVERSARIAL_RESULT_PASS7_V2.json",
    "qa/PAPER_NAIVE_RESULT_PASS7_V3.json",
    "qa/ADVERSARIAL_RESULT_PASS7_V3.json",
    "qa/PAPER_NAIVE_RESULT_PASS7_V4.json",
    "qa/ADVERSARIAL_RESULT_PASS7_V4.json",
    "qa/PAPER_NAIVE_RESULT_PASS7_V5.json",
    "qa/ADVERSARIAL_RESULT_PASS7_V5.json",
    "qa/PAPER_NAIVE_RESULT_PASS7_V6.json",
    "qa/ADVERSARIAL_RESULT_PASS7_V6.json",
    "qa/PAPER_NAIVE_RESULT_PASS7_V7.json",
    "qa/ADVERSARIAL_RESULT_PASS7_V7.json",
    "qa/PAPER_NAIVE_RESULT_PASS7_V8.json",
    "qa/ADVERSARIAL_RESULT_PASS7_V8.json",
    "qa/PAPER_NAIVE_RESULT_PASS7_V11.json",
    "qa/ADVERSARIAL_RESULT_PASS7_V11.json",
    "qa/PAPER_NAIVE_RESULT_PASS7_V12.json",
    "qa/ADVERSARIAL_RESULT_PASS7_V12.json",
    "qa/PAPER_NAIVE_RESULT_PASS7_V13.json",
    "qa/ADVERSARIAL_RESULT_PASS7_V13.json",
    "qa/PAPER_NAIVE_RESULT_PASS7_V14.json",
    "qa/ADVERSARIAL_RESULT_PASS7_V14.json",
    "qa/PAPER_NAIVE_RESULT_PASS7_V15.json",
    "qa/ADVERSARIAL_RESULT_PASS7_V15.json",
    "qa/PAPER_NAIVE_RESULT_PASS7_V16.json",
    "qa/ADVERSARIAL_RESULT_PASS7_V16.json",
    "qa/PAPER_NAIVE_RESULT_PASS7_V17.json",
    "qa/ADVERSARIAL_RESULT_PASS7_V17.json",
    "qa/PAPER_NAIVE_RESULT_PASS7_V18.json",
    "qa/ADVERSARIAL_RESULT_PASS7_V18.json",
    "qa/PAPER_NAIVE_RESULT_PASS7_V19.json",
    "qa/ADVERSARIAL_RESULT_PASS7_V19.json",
    "qa/PAPER_NAIVE_RESULT_PASS7_V20.json",
    "qa/ADVERSARIAL_RESULT_PASS7_V20.json",
    "qa/PAPER_NAIVE_RESULT_PASS7_V22.json",
    "qa/ADVERSARIAL_RESULT_PASS7_V22.json",
    "qa/PAPER_NAIVE_RESULT_PASS7_V26.json",
    "qa/PAPER_NAIVE_PACKET_PROJECTION.json",
    "qa/PAPER_NAIVE_RESULT.json",
    "qa/ADVERSARIAL_RESULT.json",
    "qa/PAPER_NAIVE_RESULT_PASS3.json",
    "qa/ADVERSARIAL_RESULT_PASS3.json",
    "qa/PAPER_NAIVE_RESULT_PASS4.json",
    "qa/ADVERSARIAL_RESULT_PASS4.json",
    "qa/PAPER_NAIVE_RESULT_PASS4_V1.json",
    "qa/ADVERSARIAL_RESULT_PASS4_V1.json",
    "qa/PAPER_NAIVE_RESULT_PASS5.json",
    "qa/ADVERSARIAL_RESULT_PASS5.json",
    "qa/PAPER_NAIVE_RESULT_PASS6.json",
    "qa/ADVERSARIAL_RESULT_PASS6.json",
    "qa/PAPER_NAIVE_RESULT_V2_V5.json",
    "qa/ADVERSARIAL_RESULT_V2_V5.json",
    "qa/REVIEW_INDEX.json",
    "ALLOY_NARRATION_MANIFEST_PROPOSAL.json",
    "DISPLAY_CITATIONS.md",
    "citation_ledger.json",
    "INTEGRATOR_REQUEST.md",
    "LANE_RECEIPT.md",
    "snapshots/pass2-v7/MANIFEST.json",
    "snapshots/pass3-audience-copy-v1/MANIFEST.json",
    "snapshots/pass4-retrieval-axis-provenance-v1/MANIFEST.json",
    "snapshots/pass4-retrieval-axis-provenance-v2/MANIFEST.json",
    "snapshots/pass5-all-axis-control-provenance-v1/MANIFEST.json",
    "snapshots/pass6-evidence-state-causality-v1/MANIFEST.json",
    "snapshots/pass7-state-continuity-v1/MANIFEST.json",
    "snapshots/pass7-validator-projection-causality-v2/MANIFEST.json",
    "snapshots/pass7-full-contract-closure-v3/MANIFEST.json",
    "snapshots/pass7-self-contained-contract-v4/MANIFEST.json",
    "snapshots/pass7-explicit-custody-inventory-v7/MANIFEST.json",
    "snapshots/pass7-adversarial-semantic-closure-v5/MANIFEST.json",
    "snapshots/pass7-manifest-authenticated-semantic-v6/MANIFEST.json",
    "snapshots/pass7-distinct-example-clock-v8/MANIFEST.json",
    "snapshots/pass7-complete-audience-static-v11/MANIFEST.json",
    "snapshots/pass7-current-artifact-traceability-v12/MANIFEST.json",
    "snapshots/pass7-live-receipt-identity-census-v28/MANIFEST.json",
]
missing = [name for name in required if not (HERE / name).exists()]
checks["required_artifacts_present"] = not missing
if missing:
    errors.append(f"missing artifacts: {missing}")

# Parse every JSON file except the output being written.
json_files = [p for p in HERE.rglob("*.json") if p.name != "final_worker_checks.json"]
json_errors = []
for path in json_files:
    try:
        json.loads(path.read_text())
    except Exception as exc:
        json_errors.append(f"{path.relative_to(HERE)}: {exc}")
checks["all_json_parse"] = not json_errors
if json_errors:
    errors.extend(json_errors)

expected_hashes = {
    HERE / "visual_proposal_v1.png": "d468dd6e3366ce57dfc33a5bb6c8153b8fa5793505a082c452c53b3fdcdef1e9",
    HERE / "visual_proposal_v2.png": "b24f573de61c68a9f2d75c014900b7a9fcc602809d2db150ad17da7645887601",
    HERE / "visual_proposal_v3.png": "74592fabe143b6efbd88b74c7e8e7eab28cb98e658741807bd7706017732e7b2",
    HERE / "visual_proposal_v4.png": "0b0fdb065a37050479b0b3f110e1898ef689384b3ca009ba75445f79c7f92be3",
    HERE / "visual_proposal_v5.png": "f07a3ccbbfadda9a409c074e06578777c6ce221b42685cd0876fcda9363a1fe0",
    HERE / "visual_proposal_v6.png": "535e72112db05a1b06352813cd2778a7b9a1c86d3339aad8870588b418b45463",
    HERE / "visual_proposal_v7.png": "ed1f9c7c2aa192b423b23655388d10c941c84069a394032de868bd51fe902883",
    HERE / "visual_proposal_v8.png": "5c36f6e1d4b63d215a0bb68545457376d961b168bff1f18686ad45e1d4d19df9",
    HERE / "visual_proposal_v9.png": "c07eb10a3652e088f8dfca9085b1e1cc35d6af4f84ccf58d4ab767efca78eebe",
    HERE / "qa/deepening-pass2-encoded/contact_sheet_20frames.jpg": "5ac85b0f20ac582edb9ff9b52633170675a7f2b69ff9f0530e9fcadcc52ff563",
    HERE / "qa/deepening-pass3-encoded/contact_sheet_32frames.jpg": "a54f9c5d7fc1cd3e7b0f186bdec4d6c5f44147b154bdc9ae7487f0bc797826df",
    HERE / "qa/deepening-pass4-encoded/contact_sheet_32frames_offset2.jpg": "f2f1ab19f1b38f6a5a8c813077d57a3e61e4f22290289f2a50b415c0f39d8c4c",
    HERE / "qa/deepening-pass5-encoded/contact_sheet_32frames_offset1.jpg": "278a6c6f76c0e7c8977cff0aa91bd7c044f4f4c2c64c92bdad1abc3babc8459a",
    HERE / "qa/deepening-pass6-encoded/contact_sheet_32frames_offset3.jpg": "08539f7b3e535cde8811352f62ec6968dfe7db7982a4c5f6b781c451932f0bd4",
    Path("/Users/duhokim/HermesOps/cockpit/videos/mzr-archive-census-narrated-20260808T0155.mp4"): "0bdfd12dcc87098e1034196bc973df4ace79044cadc4261f3f827b65d7cd162d",
    ROOT / "frontend/public/videos/mzr-archive-census.mp4": "dc2f32a24e5418cb2cf1781401e877e70682dfcf17e4514407cc6cc48d08fcc0",
    ROOT / "tools/nm_paper_video.py": "919af6b18057309bfa5ecc2dd0fa44536dabaa4ba02aba960cabd3d791099f5c",
    ROOT / "tools/nm_paper_plot.py": "6acc8ba13e0393b60950ab78b1dbdf053c48459b0449581211ecc0eff021c43d",
}
hash_checks = {str(path): sha256(path) == expected for path, expected in expected_hashes.items()}
checks["custody_hashes"] = hash_checks
if not all(hash_checks.values()):
    errors.append(f"custody hash mismatch: {[k for k, v in hash_checks.items() if not v]}")

worker_media = [str(p.relative_to(HERE)) for p in HERE.rglob("*") if p.is_file() and p.suffix.lower() in {".mp4", ".mp3", ".wav", ".m4a", ".aac", ".mov"}]
checks["no_worker_audio_or_video"] = not worker_media
if worker_media:
    errors.append(f"unexpected worker media: {worker_media}")

if not missing:
    proposal = load("qa/proposal_validation.json")
    visual = load("qa/visual_proposal_qa.json")
    naive = load("qa/PAPER_NAIVE_RESULT.json")
    adversarial = load("qa/ADVERSARIAL_RESULT.json")
    naive_pass3 = load("qa/PAPER_NAIVE_RESULT_PASS3.json")
    adversarial_pass3 = load("qa/ADVERSARIAL_RESULT_PASS3.json")
    naive_pass4 = load("qa/PAPER_NAIVE_RESULT_PASS4.json")
    adversarial_pass4 = load("qa/ADVERSARIAL_RESULT_PASS4.json")
    naive_pass4_v1 = load("qa/PAPER_NAIVE_RESULT_PASS4_V1.json")
    adversarial_pass4_v1 = load("qa/ADVERSARIAL_RESULT_PASS4_V1.json")
    naive_pass5 = load("qa/PAPER_NAIVE_RESULT_PASS5.json")
    adversarial_pass5 = load("qa/ADVERSARIAL_RESULT_PASS5.json")
    naive_pass6 = load("qa/PAPER_NAIVE_RESULT_PASS6.json")
    adversarial_pass6 = load("qa/ADVERSARIAL_RESULT_PASS6.json")
    pass2_audit = load("qa/deepening-pass2-encoded/AUDIT.json")
    pass3_audit = load("qa/deepening-pass3-encoded/AUDIT.json")
    pass3_local = load("qa/PASS3_LOCAL_GATE.json")
    pass3_frame_manifest = load("qa/deepening-pass3-encoded/FRAME_HASHES.json")
    pass3_frame_dir = HERE / "qa/deepening-pass3-encoded"
    pass3_frame_hashes = {
        name: (pass3_frame_dir / name).exists() and sha256(pass3_frame_dir / name) == expected
        for name, expected in pass3_frame_manifest["frames"].items()
    }
    pass4_audit = load("qa/deepening-pass4-encoded/AUDIT.json")
    pass4_local = load("qa/PASS4_LOCAL_GATE.json")
    pass4_packet_sync = load("qa/PASS4_PACKET_SYNC.json")
    pass4_citation = load("qa/PASS4_CITATION_GATE.json")
    pass4_validator = load("qa/PASS4_VALIDATOR_CUSTODY.json")
    pass4_frame_manifest = load("qa/deepening-pass4-encoded/FRAME_HASHES.json")
    pass4_frame_dir = HERE / "qa/deepening-pass4-encoded"
    pass4_frame_hashes = {
        name: (pass4_frame_dir / name).exists() and sha256(pass4_frame_dir / name) == expected
        for name, expected in pass4_frame_manifest["frames"].items()
    }
    pass5_audit = load("qa/deepening-pass5-encoded/AUDIT.json")
    pass5_local = load("qa/PASS5_LOCAL_GATE.json")
    pass5_packet_sync = load("qa/PASS5_PACKET_SYNC.json")
    pass5_citation = load("qa/PASS5_CITATION_GATE.json")
    pass5_validator = load("qa/PASS5_VALIDATOR_CUSTODY.json")
    pass5_frame_manifest = load("qa/deepening-pass5-encoded/FRAME_HASHES.json")
    pass5_frame_dir = HERE / "qa/deepening-pass5-encoded"
    pass5_frame_hashes = {
        name: (pass5_frame_dir / name).exists() and sha256(pass5_frame_dir / name) == expected
        for name, expected in pass5_frame_manifest["frames"].items()
    }
    pass6_audit = load("qa/deepening-pass6-encoded/AUDIT.json")
    pass6_scene_holds = load("qa/deepening-pass6-encoded/SCENE_HOLDS.json")
    pass6_local = load("qa/PASS6_LOCAL_GATE.json")
    pass6_packet_sync = load("qa/PASS6_PACKET_SYNC.json")
    pass6_citation = load("qa/PASS6_CITATION_GATE.json")
    pass6_validator = load("qa/PASS6_VALIDATOR_CUSTODY.json")
    pass6_frame_manifest = load("qa/deepening-pass6-encoded/FRAME_HASHES.json")
    pass6_frame_dir = HERE / "qa/deepening-pass6-encoded"
    pass6_frame_hashes = {
        name: (pass6_frame_dir / name).exists() and sha256(pass6_frame_dir / name) == expected
        for name, expected in pass6_frame_manifest["frames"].items()
    }
    pass7_audit = load("qa/deepening-pass7-encoded/AUDIT.json")
    pass7_frames = load("qa/deepening-pass7-encoded/FRAME_HASHES.json")
    pass7_boundary = load("qa/deepening-pass7-encoded/BOUNDARY_CONTINUITY.json")
    pass7_ocr = load("qa/deepening-pass7-encoded/OCR_DENSITY.json")
    pass7_custody = load("qa/PASS7_V6_CUSTODY_CHECKS.json")
    pass7_packet = load("qa/PASS7_V6_PACKET_PAYLOAD_CHECKS.json")
    pass7_citation = load("qa/PASS7_V6_CITATION_CHECKS.json")
    pass7_continuity = load("qa/PASS7_V6_CONTINUITY_SEMANTIC_CHECKS.json")
    pass7_validator = load("qa/PASS7_V6_VALIDATOR_CHECKS.json")
    pass7_local = load("qa/PASS7_V28_LOCAL_CHECKS.json")
    pass7_v7_custody = load("qa/PASS7_V7_CUSTODY_INVENTORY_CHECKS.json")
    pass7_mutations = load("qa/PASS7_VALIDATOR_MUTATION_TESTS.json")
    pass7_approved_contract = load("qa/APPROVED_STORYBOARD_CONTRACT.json")
    pass7_v2_false_paths = load("qa/PASS7_V2_ADDITIONAL_FALSE_PATHS.json")
    pass7_v1_paper = load("qa/PAPER_NAIVE_RESULT_PASS7_V1.json")
    pass7_v1_adversarial = load("qa/ADVERSARIAL_RESULT_PASS7_V1.json")
    pass7_v2_paper = load("qa/PAPER_NAIVE_RESULT_PASS7_V2.json")
    pass7_v2_adversarial = load("qa/ADVERSARIAL_RESULT_PASS7_V2.json")
    pass7_v3_paper = load("qa/PAPER_NAIVE_RESULT_PASS7_V3.json")
    pass7_v3_adversarial = load("qa/ADVERSARIAL_RESULT_PASS7_V3.json")
    pass7_v4_paper = load("qa/PAPER_NAIVE_RESULT_PASS7_V4.json")
    pass7_v4_adversarial = load("qa/ADVERSARIAL_RESULT_PASS7_V4.json")
    pass7_v5_paper = load("qa/PAPER_NAIVE_RESULT_PASS7_V5.json")
    pass7_v5_adversarial = load("qa/ADVERSARIAL_RESULT_PASS7_V5.json")
    pass7_v6_paper = load("qa/PAPER_NAIVE_RESULT_PASS7_V6.json")
    pass7_v6_adversarial = load("qa/ADVERSARIAL_RESULT_PASS7_V6.json")
    pass7_v7_paper = load("qa/PAPER_NAIVE_RESULT_PASS7_V7.json")
    pass7_v7_adversarial = load("qa/ADVERSARIAL_RESULT_PASS7_V7.json")
    pass7_v8_paper = load("qa/PAPER_NAIVE_RESULT_PASS7_V8.json")
    pass7_v8_adversarial = load("qa/ADVERSARIAL_RESULT_PASS7_V8.json")
    pass7_v11_paper = load("qa/PAPER_NAIVE_RESULT_PASS7_V11.json")
    pass7_v11_adversarial = load("qa/ADVERSARIAL_RESULT_PASS7_V11.json")
    pass7_v12_paper = load("qa/PAPER_NAIVE_RESULT_PASS7_V12.json")
    pass7_v12_adversarial = load("qa/ADVERSARIAL_RESULT_PASS7_V12.json")
    pass7_v13_paper = load("qa/PAPER_NAIVE_RESULT_PASS7_V13.json")
    pass7_v13_adversarial = load("qa/ADVERSARIAL_RESULT_PASS7_V13.json")
    pass7_v14_paper = load("qa/PAPER_NAIVE_RESULT_PASS7_V14.json")
    pass7_v14_adversarial = load("qa/ADVERSARIAL_RESULT_PASS7_V14.json")
    pass7_v15_paper = load("qa/PAPER_NAIVE_RESULT_PASS7_V15.json")
    pass7_v15_adversarial = load("qa/ADVERSARIAL_RESULT_PASS7_V15.json")
    pass7_v16_paper = load("qa/PAPER_NAIVE_RESULT_PASS7_V16.json")
    pass7_v16_adversarial = load("qa/ADVERSARIAL_RESULT_PASS7_V16.json")
    pass7_v17_paper = load("qa/PAPER_NAIVE_RESULT_PASS7_V17.json")
    pass7_v17_adversarial = load("qa/ADVERSARIAL_RESULT_PASS7_V17.json")
    pass7_v18_paper = load("qa/PAPER_NAIVE_RESULT_PASS7_V18.json")
    pass7_v18_adversarial = load("qa/ADVERSARIAL_RESULT_PASS7_V18.json")
    pass7_v19_paper = load("qa/PAPER_NAIVE_RESULT_PASS7_V19.json")
    pass7_v19_adversarial = load("qa/ADVERSARIAL_RESULT_PASS7_V19.json")
    pass7_v20_paper = load("qa/PAPER_NAIVE_RESULT_PASS7_V20.json")
    pass7_v20_adversarial = load("qa/ADVERSARIAL_RESULT_PASS7_V20.json")
    pass7_v22_paper = load("qa/PAPER_NAIVE_RESULT_PASS7_V22.json")
    pass7_v22_adversarial = load("qa/ADVERSARIAL_RESULT_PASS7_V22.json")
    pass7_v26_paper = load("qa/PAPER_NAIVE_RESULT_PASS7_V26.json")
    pass7_source_manifest = load("frozen_sources/pass7/MANIFEST.json")
    pass7_projection = load("qa/PAPER_NAIVE_PACKET_PROJECTION.json")
    narration = load("ALLOY_NARRATION_MANIFEST_PROPOSAL.json")
    freeze = load("SOURCE_FREEZE.json")
    storyboard = load("STORYBOARD_CANDIDATE.json")
    citation_ledger = load("citation_ledger.json")
    display_citations = (HERE / "DISPLAY_CITATIONS.md").read_text()
    snapshot_manifest = load("snapshots/pass3-audience-copy-v1/MANIFEST.json")
    snapshot_dir = HERE / "snapshots/pass3-audience-copy-v1"
    snapshot_hashes = {
        name: (snapshot_dir / name).exists() and sha256(snapshot_dir / name) == expected
        for name, expected in snapshot_manifest["files"].items()
    }
    pass4_snapshot_manifest = load("snapshots/pass4-retrieval-axis-provenance-v2/MANIFEST.json")
    pass4_snapshot_dir = HERE / "snapshots/pass4-retrieval-axis-provenance-v2"
    pass4_snapshot_hashes = {
        name: (pass4_snapshot_dir / name).exists() and sha256(pass4_snapshot_dir / name) == expected
        for name, expected in pass4_snapshot_manifest["files"].items()
    }
    pass5_snapshot_manifest = load("snapshots/pass5-all-axis-control-provenance-v1/MANIFEST.json")
    pass5_snapshot_dir = HERE / "snapshots/pass5-all-axis-control-provenance-v1"
    pass5_snapshot_hashes = {
        name: (pass5_snapshot_dir / name).exists() and sha256(pass5_snapshot_dir / name) == expected
        for name, expected in pass5_snapshot_manifest["files"].items()
    }
    pass6_snapshot_manifest = load("snapshots/pass6-evidence-state-causality-v1/MANIFEST.json")
    pass6_snapshot_dir = HERE / "snapshots/pass6-evidence-state-causality-v1"
    pass6_snapshot_hashes = {
        name: (pass6_snapshot_dir / name).exists() and sha256(pass6_snapshot_dir / name) == expected
        for name, expected in pass6_snapshot_manifest["files"].items()
    }
    pass7_snapshot_manifest = load("snapshots/pass7-live-receipt-identity-census-v28/MANIFEST.json")
    pass7_snapshot_dir = HERE / "snapshots/pass7-live-receipt-identity-census-v28"
    pass7_snapshot_hashes = {
        entry["path"]: (pass7_snapshot_dir / entry["path"]).exists()
        and sha256(pass7_snapshot_dir / entry["path"]) == entry["sha256"]
        for entry in pass7_snapshot_manifest["files"]
    }
    pass7_snapshot_file_modes = {
        str(path.relative_to(pass7_snapshot_dir)): path.stat().st_mode & 0o777
        for path in pass7_snapshot_dir.rglob("*") if path.is_file()
    }
    pass7_snapshot_dir_modes = {
        str(path.relative_to(pass7_snapshot_dir)) or ".": path.stat().st_mode & 0o777
        for path in [pass7_snapshot_dir, *[candidate for candidate in pass7_snapshot_dir.rglob("*") if candidate.is_dir()]]
    }
    frozen_input_hashes = {}
    for entry in freeze["inputs"]:
        path = Path(entry["path"])
        if not path.is_absolute():
            path = ROOT / path
        frozen_input_hashes[entry["role"]] = path.exists() and sha256(path) == entry["sha256"]
    checks.update({
        "proposal_validation_pass": proposal["verdict"] == "PASS",
        "visual_proposal_pass": visual["verdict"].startswith("PASS_FOR_STATIC_VISUAL_PROPOSAL_ONLY"),
        "visual_is_v9": visual["accepted_artifact"] == "visual_proposal_v9.png" and visual["accepted_sha256"] == "c07eb10a3652e088f8dfca9085b1e1cc35d6af4f84ccf58d4ab767efca78eebe" and visual["deterministic_rerender"]["match"],
        "paper_naive_pass": naive["verdict"] == "PASS" and naive["mandatory_questions_passed"],
        "adversarial_pass": adversarial["verdict"] == "PASS",
        "pass2_encoded_audit_preserved": pass2_audit["verdict"] == "FAIL_FOR_SCIENTIFIC_REPRESENTATION_GRAPHICS_GRAMMAR_AND_CONTAMINATION_TAXONOMY" and not pass2_audit["candidate_modified"],
        "pass3_encoded_audit_preserved": pass3_audit["verdict"] == "FAIL_FOR_SCIENTIFIC_REPRESENTATION_GRAPHICS_GRAMMAR_TAXONOMY_AND_CLOSURE_BOUNDARY" and not pass3_audit["candidate"]["candidate_modified"],
        "pass3_local_gate_pass": pass3_local["verdict"].startswith("PASS") and pass3_local["checks"]["worker_media_count"] == 0 and not pass3_local["checks"]["tts_invoked"],
        "pass3_frame_hashes": pass3_frame_hashes,
        "pass3_frame_custody_stable": len(pass3_frame_hashes) == 32 and all(pass3_frame_hashes.values()),
        "pass3_paper_naive_pass": naive_pass3["verdict"] == "PASS" and naive_pass3["mandatory_questions_passed"],
        "pass3_adversarial_pass": adversarial_pass3["verdict"] == "PASS" and not adversarial_pass3["material_defects"],
        "pass3_snapshot_hashes": snapshot_hashes,
        "pass3_snapshot_stable": all(snapshot_hashes.values()),
        "pass4_encoded_audit_preserved": pass4_audit["verdict"] == "FAIL_FOR_SCIENTIFIC_REPRESENTATION_TARGET_VS_AXIS_EVIDENCE_CLASS_CONTROL_STAGE_AND_PRIOR_BOUNDARIES" and not pass4_audit["candidate"]["candidate_modified"],
        "pass4_local_gate_pass": pass4_local["verdict"].startswith("PASS") and pass4_local["checks"]["worker_media_count"] == 0 and not pass4_local["checks"]["tts_invoked"],
        "pass4_packet_sync_pass": pass4_packet_sync["verdict"] == "PASS" and pass4_packet_sync["all_narration_present"] and pass4_packet_sync["all_on_screen_copy_present"],
        "pass4_citation_gate_pass": pass4_citation["verdict"] == "PASS" and pass4_citation["renderer_footer_ledger_driven"] and not pass4_citation["hard_coded_scholarly_citation_strings_in_python"],
        "pass4_validator_custody_pass": pass4_validator["verdict"].startswith("PASS") and pass4_validator["proposal_validation_root_matches_review_snapshot"] and pass4_validator["taxonomy_predicate_uses_audience_projection"],
        "pass4_frame_hashes": pass4_frame_hashes,
        "pass4_frame_custody_stable": len(pass4_frame_hashes) == 32 and all(pass4_frame_hashes.values()),
        "pass4_paper_naive_pass": naive_pass4["verdict"] == "PASS" and naive_pass4["mandatory_questions_passed"],
        "pass4_adversarial_pass": adversarial_pass4["verdict"] == "PASS" and not adversarial_pass4["material_defects"],
        "pass4_v1_failed_review_preserved": naive_pass4_v1["verdict"] == "PASS" and adversarial_pass4_v1["verdict"] == "FAIL" and bool(adversarial_pass4_v1["material_defects"]),
        "pass4_snapshot_hashes": pass4_snapshot_hashes,
        "pass4_snapshot_stable": all(pass4_snapshot_hashes.values()),
        "pass5_encoded_audit_preserved": pass5_audit["verdict"] == "FAIL_FOR_SCIENTIFIC_REPRESENTATION_ALL_AXIS_SEARCH_SCOPE_ASYMMETRIC_T2_CONTROL_PROVENANCE_AND_PRIOR_BOUNDARIES" and not pass5_audit["candidate_modified"],
        "pass5_local_gate_pass": pass5_local["verdict"].startswith("PASS") and pass5_local["checks"]["worker_media_count"] == 0 and not pass5_local["checks"]["tts_invoked"],
        "pass5_packet_sync_pass": pass5_packet_sync["verdict"] == "PASS" and pass5_packet_sync["all_narration_present"] and pass5_packet_sync["all_on_screen_copy_present"],
        "pass5_citation_gate_pass": pass5_citation["verdict"] == "PASS" and pass5_citation["renderer_footer_ledger_driven"] and not pass5_citation["hard_coded_scholarly_citation_strings_in_python"],
        "pass5_validator_custody_pass": pass5_validator["verdict"].startswith("PASS") and pass5_validator["root_matches_snapshot"] and pass5_validator["all_axis_predicate_uses_audience_projection"] and pass5_validator["balanced_T2_control_predicate_uses_audience_projection"],
        "pass5_frame_hashes": pass5_frame_hashes,
        "pass5_frame_custody_stable": len(pass5_frame_hashes) == 32 and all(pass5_frame_hashes.values()),
        "pass5_paper_naive_pass": naive_pass5["verdict"] == "PASS" and naive_pass5["mandatory_questions_passed"],
        "pass5_adversarial_pass": adversarial_pass5["verdict"] == "PASS" and not adversarial_pass5["material_defects"],
        "pass5_snapshot_hashes": pass5_snapshot_hashes,
        "pass5_snapshot_stable": len(pass5_snapshot_hashes) == 14 and all(pass5_snapshot_hashes.values()),
        "pass6_encoded_audit_preserved": pass6_audit["verdict"] == "FAIL_FOR_SCIENTIFIC_REPRESENTATION_STATIC_EVIDENCE_STATE_CAUSALITY_AND_PRIOR_BOUNDARIES" and not pass6_audit["candidate"]["candidate_modified"],
        "pass6_scene_metrics": pass6_scene_holds["detected_cut_count"] == 14 and pass6_scene_holds["hold_count"] == 15 and pass6_scene_holds["holds_over_6_seconds"] == 10 and pass6_scene_holds["max_hold_seconds"] == 16.133,
        "pass6_local_gate_pass": pass6_local["verdict"].startswith("PASS") and pass6_local["checks"]["worker_media_count"] == 0 and not pass6_local["checks"]["tts_invoked"],
        "pass6_packet_sync_pass": pass6_packet_sync["verdict"] == "PASS" and pass6_packet_sync["all_narration_present"] and pass6_packet_sync["all_on_screen_copy_present"] and pass6_packet_sync["manifest_segments_and_timed_reveals_match_storyboard"],
        "pass6_citation_gate_pass": pass6_citation["verdict"] == "PASS" and pass6_citation["renderer_footer_ledger_driven"] and not pass6_citation["hard_coded_scholarly_citation_strings_in_python"],
        "pass6_validator_custody_pass": pass6_validator["verdict"].startswith("PASS") and pass6_validator["root_matches_snapshot"] and pass6_validator["motion_predicate_uses_timed_reveal_states"] and pass6_validator["motion_contract_pass"],
        "pass6_frame_hashes": pass6_frame_hashes,
        "pass6_frame_custody_stable": len(pass6_frame_hashes) == 32 and all(pass6_frame_hashes.values()),
        "pass6_paper_naive_pass": naive_pass6["verdict"] == "PASS" and naive_pass6["mandatory_questions_passed"],
        "pass6_exact_failure_preserved": adversarial_pass6["verdict"] == "FAIL" and bool(adversarial_pass6["material_defects"]) and adversarial_pass6["integration_gate"] == "CLOSED" and adversarial_pass6["publication_gate"] == "CLOSED",
        "pass6_snapshot_hashes": pass6_snapshot_hashes,
        "pass6_snapshot_stable": len(pass6_snapshot_hashes) == 16 and all(pass6_snapshot_hashes.values()),
        "pass6_failure_receipt_marker": "YUI_MZR_CENSUS_WEEKEND_PASS6_EXACT_FAIL" in (HERE / "LANE_RECEIPT.md").read_text(),
        "pass7_encoded_audit_preserved": pass7_audit["verdict"].startswith("FAIL_") and not pass7_audit["candidate"]["candidate_modified"],
        "pass7_frame_custody_stable": pass7_custody["verdict"] == "PASS" and pass7_custody["audited_frame_pngs"] == 43 and pass7_custody["audited_frame_hashes_match"],
        "pass7_boundary_findings_preserved": len(pass7_boundary["cuts"]) == 14 and sum(cut["preserved_anchor_count"] == 0 for cut in pass7_boundary["cuts"]) == 11 and sum(hold["ocr_word_count"] > 25 for hold in pass7_ocr["holds"]) == 6,
        "pass7_packet_projection_pass": pass7_packet["verdict"] == "PASS" and not pass7_packet["answer_key_present"] and pass7_projection["contract"] == "EXACT_AUDIENCE_PAYLOAD_PLUS_DECLARED_REVIEW_SCAFFOLDING" and pass7_projection["audience_projection_fields"] == ["narration", "on_screen_copy", "display_citation"] and pass7_projection["narration_count"] == 10 and pass7_projection["on_screen_leaf_string_count"] == 62 and pass7_projection["display_citation_count"] == 10,
        "pass7_citation_pass": pass7_citation["verdict"] == "PASS" and pass7_citation["all_display_citations_exactly_ledger_bound"] and not pass7_citation["internal_paths_visible"],
        "pass7_continuity_causality_pass": pass7_local["checks"]["distinct_state_contract"].startswith("45/45 exact approved states") and proposal["motion_contract"]["global_checks"]["maximum_semantic_gap_seconds"] == 3.0,
        "pass7_validator_pass": proposal["verdict"] == "PASS" and all(proposal["approved_storyboard_contract_checks"].values()) and all(proposal["source_render_bindings"].values()) and all(proposal["numeric_source_audit_checks"].values()) and all(proposal["paper_naive_question_contract_checks"].values()) and pass7_mutations["verdict"] == "PASS" and len(pass7_mutations["cases"]) == 37,
        "pass7_approved_contract_pass": pass7_approved_contract["contract_version"] == "pass7-distinct-state-custody-v23" and pass7_approved_contract["publication_gate"] == "CLOSED" and pass7_approved_contract["source_freeze_manifest_sha256"] == sha256(HERE / "frozen_sources/pass7/MANIFEST.json") and pass7_approved_contract["packet_contract"] == "EXACT_AUDIENCE_PAYLOAD_PLUS_DECLARED_REVIEW_SCAFFOLDING" and pass7_approved_contract["trust_anchor"] == "EXTERNALLY_SUPPLIED_IMMUTABLE_SNAPSHOT_MANIFEST_SHA256" and pass7_approved_contract["co_located_hashes_independent_trust_anchor"] is False and pass7_approved_contract["snapshot_manifest_authentication_required"],
        "pass7_source_freeze_stable": len(pass7_source_manifest["files"]) == 8 and all((HERE / "frozen_sources/pass7" / entry["file"]).exists() and sha256(HERE / "frozen_sources/pass7" / entry["file"]) == entry["sha256"] for entry in pass7_source_manifest["files"]),
        "pass7_v2_false_paths_preserved": pass7_v2_false_paths["false_pass_count"] == 4 and pass7_v2_false_paths["snapshot_modified"] is False,
        "pass7_v1_exact_fail_preserved": pass7_v1_paper["verdict"] == "PASS" and pass7_v1_paper["score"] == 8 and pass7_v1_adversarial["verdict"] == "FAIL" and len(pass7_v1_adversarial["material_defects"]) == 2 and pass7_v1_adversarial["candidate_disposition"] == "FAIL preserved",
        "pass7_v2_exact_fail_preserved": pass7_v2_paper["verdict"] == "PASS" and pass7_v2_paper["score"] == 8 and pass7_v2_adversarial["verdict"] == "FAIL" and len(pass7_v2_adversarial["material_defects"]) == 4 and pass7_v2_adversarial["candidate_disposition"] == "FAIL preserved",
        "pass7_v3_exact_fail_preserved": pass7_v3_paper["verdict"] == "PASS" and pass7_v3_paper["score"] == 8 and pass7_v3_paper["mandatory_questions_passed"] and pass7_v3_adversarial["verdict"] == "FAIL" and len(pass7_v3_adversarial["material_defects"]) == 3 and pass7_v3_adversarial["candidate_disposition"] == "FAIL preserved" and "YUI_MZR_CENSUS_WEEKEND_PASS7_V3_EXACT_FAIL" in (HERE / "LANE_RECEIPT.md").read_text(),
        "pass7_v4_exact_fail_preserved": pass7_v4_paper["verdict"] == "PASS" and pass7_v4_paper["score"] == 8 and pass7_v4_paper["mandatory_questions_passed"] and pass7_v4_paper["manifest_entries"] == 89 and pass7_v4_adversarial["verdict"] == "FAIL" and len(pass7_v4_adversarial["material_defects"]) == 4 and pass7_v4_adversarial["candidate_disposition"] == "FAIL preserved" and "YUI_MZR_CENSUS_WEEKEND_PASS7_V4_EXACT_FAIL" in (HERE / "LANE_RECEIPT.md").read_text(),
        "pass7_v5_exact_fail_preserved": pass7_v5_paper["verdict"] == "PASS" and pass7_v5_paper["score"] == 8 and pass7_v5_paper["mandatory_questions_passed"] and pass7_v5_paper["manifest_entries"] == 95 and pass7_v5_adversarial["verdict"] == "FAIL" and len(pass7_v5_adversarial["material_defects"]) == 3 and pass7_v5_adversarial["candidate_disposition"] == "FAIL preserved" and "YUI_MZR_CENSUS_WEEKEND_PASS7_V5_EXACT_FAIL" in (HERE / "LANE_RECEIPT.md").read_text(),
        "pass7_v6_exact_fail_preserved": pass7_v6_paper["verdict"] == "PASS" and pass7_v6_paper["score"] == 8 and pass7_v6_paper["mandatory_questions_passed"] and pass7_v6_adversarial["verdict"] == "FAIL" and len(pass7_v6_adversarial["material_defects"]) == 4 and pass7_v6_adversarial["candidate_disposition"] == "FAIL preserved" and "YUI_MZR_CENSUS_WEEKEND_PASS7_V6_EXACT_FAIL" in (HERE / "LANE_RECEIPT.md").read_text(),
        "pass7_v7_exact_fail_preserved": pass7_v7_paper["verdict"] == "PASS" and pass7_v7_paper["score"] == 8 and pass7_v7_paper["mandatory_questions_passed"] and pass7_v7_adversarial["verdict"] == "FAIL" and len(pass7_v7_adversarial["material_defects"]) == 4 and pass7_v7_adversarial["candidate_disposition"] == "FAIL preserved" and "YUI_MZR_CENSUS_WEEKEND_PASS7_V7_EXACT_FAIL" in (HERE / "LANE_RECEIPT.md").read_text(),
        "pass7_v8_exact_fail_preserved": pass7_v8_paper["verdict"] == "PASS" and pass7_v8_paper["score"] == 8 and pass7_v8_paper["mandatory_questions"]["Q4"] == "PASS" and pass7_v8_paper["mandatory_questions"]["Q8"] == "PASS" and pass7_v8_adversarial["verdict"] == "FAIL" and len(pass7_v8_adversarial["material_defects"]) == 4 and pass7_v8_adversarial["external_candidate_disposition"] == "FAIL_PRESERVED" and "YUI_MZR_CENSUS_WEEKEND_PASS7_V8_EXACT_FAIL" in (HERE / "LANE_RECEIPT.md").read_text(),
        "pass7_v11_exact_fail_preserved": pass7_v11_paper["verdict"] == "PASS" and pass7_v11_paper["score"] == 8 and pass7_v11_paper["mandatory_questions"]["Q4"] == "PASS" and pass7_v11_paper["mandatory_questions"]["Q8"] == "PASS" and pass7_v11_adversarial["verdict"] == "FAIL" and len(pass7_v11_adversarial["material_defects"]) == 4 and pass7_v11_adversarial["external_candidate_disposition"] == "FAIL_PRESERVED" and "YUI_MZR_CENSUS_WEEKEND_PASS7_V11_EXACT_FAIL" in (HERE / "LANE_RECEIPT.md").read_text(),
        "pass7_v12_exact_fail_preserved": pass7_v12_paper["verdict"] == "PASS" and pass7_v12_paper["score"] == 8 and pass7_v12_paper["mandatory_questions"]["Q4"] == "PASS" and pass7_v12_paper["mandatory_questions"]["Q8"] == "PASS" and pass7_v12_adversarial["verdict"] == "FAIL" and len(pass7_v12_adversarial["material_defects"]) == 3 and pass7_v12_adversarial["external_candidate_disposition"] == "FAIL_PRESERVED" and "YUI_MZR_CENSUS_WEEKEND_PASS7_V12_EXACT_FAIL" in (HERE / "LANE_RECEIPT.md").read_text(),
        "pass7_v13_exact_fail_preserved": pass7_v13_paper["verdict"] == "PASS" and pass7_v13_paper["score"] == 8 and pass7_v13_paper["mandatory_questions"]["Q4"] == "PASS" and pass7_v13_paper["mandatory_questions"]["Q8"] == "PASS" and pass7_v13_adversarial["verdict"] == "FAIL" and len(pass7_v13_adversarial["material_defects"]) == 4 and pass7_v13_adversarial["external_candidate_disposition"] == "FAIL_PRESERVED" and "YUI_MZR_CENSUS_WEEKEND_PASS7_V13_EXACT_FAIL" in (HERE / "LANE_RECEIPT.md").read_text(),
        "pass7_v14_exact_fail_preserved": pass7_v14_paper["verdict"] == "PASS" and pass7_v14_paper["score"] == 8 and pass7_v14_paper["mandatory_questions"]["Q4"] == "PASS" and pass7_v14_paper["mandatory_questions"]["Q8"] == "PASS" and pass7_v14_adversarial["verdict"] == "FAIL" and len(pass7_v14_adversarial["material_defects"]) == 4 and pass7_v14_adversarial["external_candidate_disposition"] == "FAIL_PRESERVED" and "YUI_MZR_CENSUS_WEEKEND_PASS7_V14_EXACT_FAIL" in (HERE / "LANE_RECEIPT.md").read_text(),
        "pass7_v15_exact_fail_preserved": pass7_v15_paper["result"] == "PASS" and pass7_v15_paper["score"] == "8/8" and pass7_v15_paper["mandatory"]["q4"] == "PASS" and pass7_v15_paper["mandatory"]["q8"] == "PASS" and pass7_v15_adversarial["result"] == "FAIL" and len(pass7_v15_adversarial["material_defects"]) == 5 and pass7_v15_adversarial["external_candidate_policy_read_only"] == "FAIL" and "YUI_MZR_CENSUS_WEEKEND_PASS7_V15_EXACT_FAIL" in (HERE / "LANE_RECEIPT.md").read_text(),
        "pass7_v16_exact_fail_preserved": pass7_v16_paper["result"] == "PASS" and pass7_v16_paper["score"] == "8/8" and pass7_v16_paper["mandatory"]["q4"] == "PASS" and pass7_v16_paper["mandatory"]["q8"] == "PASS" and pass7_v16_adversarial["result"] == "FAIL" and len(pass7_v16_adversarial["material_defects"]) == 2 and pass7_v16_adversarial["external_candidate_policy_read_only"] == "FAIL" and "YUI_MZR_CENSUS_WEEKEND_PASS7_V16_EXACT_FAIL" in (HERE / "LANE_RECEIPT.md").read_text(),
        "pass7_v17_exact_fail_preserved": pass7_v17_paper["result"] == "PASS" and pass7_v17_paper["score"] == "8/8" and pass7_v17_paper["mandatory"]["q4"] == "PASS" and pass7_v17_paper["mandatory"]["q8"] == "PASS" and pass7_v17_adversarial["result"] == "FAIL" and len(pass7_v17_adversarial["material_defects"]) == 6 and pass7_v17_adversarial["external_candidate_policy_read_only"] == "FAIL" and "YUI_MZR_CENSUS_WEEKEND_PASS7_V17_EXACT_FAIL" in (HERE / "LANE_RECEIPT.md").read_text(),
        "pass7_v18_exact_fail_preserved": pass7_v18_paper["result"] == "PASS" and pass7_v18_paper["score"] == "8/8" and pass7_v18_paper["mandatory"]["q4"] == "PASS" and pass7_v18_paper["mandatory"]["q8"] == "PASS" and pass7_v18_adversarial["result"] == "FAIL" and len(pass7_v18_adversarial["material_defects"]) == 2 and pass7_v18_adversarial["external_candidate_policy_read_only"] == "FAIL" and "YUI_MZR_CENSUS_WEEKEND_PASS7_V18_EXACT_FAIL" in (HERE / "LANE_RECEIPT.md").read_text(),
        "pass7_v19_exact_fail_preserved": pass7_v19_paper["verdict"] == "PAPER_NAIVE_PASS_ONLY" and pass7_v19_paper["score"] == "8/8" and pass7_v19_paper["mandatory_questions"]["q4"].startswith("PASS") and pass7_v19_paper["mandatory_questions"]["q8"].startswith("PASS") and pass7_v19_adversarial["verdict"] == "FAIL" and len(pass7_v19_adversarial["material_defects"]) == 9 and pass7_v19_adversarial["candidate_or_packet_clearance"] == "NOT_GRANTED" and "YUI_MZR_CENSUS_WEEKEND_PASS7_V19_EXACT_FAIL" in (HERE / "LANE_RECEIPT.md").read_text(),
        "pass7_v20_exact_fail_preserved": pass7_v20_paper["verdict"] == "PAPER_NAIVE_PASS_ONLY" and pass7_v20_paper["score"] == "8/8" and pass7_v20_paper["mandatory_questions"]["q4"].startswith("PASS") and pass7_v20_paper["mandatory_questions"]["q8"].startswith("PASS") and pass7_v20_adversarial["verdict"] == "FAIL" and len(pass7_v20_adversarial["material_defects"]) == 5 and pass7_v20_adversarial["candidate_or_packet_clearance"] == "NOT_GRANTED" and "YUI_MZR_CENSUS_WEEKEND_PASS7_V20_EXACT_FAIL" in (HERE / "LANE_RECEIPT.md").read_text(),
        "pass7_v22_exact_fail_preserved": pass7_v22_paper["verdict"] == "PAPER_NAIVE_PASS_ONLY" and pass7_v22_paper["score"] == "8/8" and pass7_v22_paper["mandatory_questions"]["q4"].startswith("PASS") and pass7_v22_paper["mandatory_questions"]["q8"].startswith("PASS") and pass7_v22_adversarial["verdict"] == "FAIL" and len(pass7_v22_adversarial["material_defects"]) == 7 and pass7_v22_adversarial["candidate_or_packet_clearance"] == "NOT_GRANTED" and "YUI_MZR_CENSUS_WEEKEND_PASS7_V22_EXACT_FAIL" in (HERE / "LANE_RECEIPT.md").read_text(),
        "pass7_v26_exact_fail_preserved": pass7_v26_paper["verdict"] == "PAPER_NAIVE_PASS_CONTROL_PLANE_FAIL" and pass7_v26_paper["score"] == "8/8" and pass7_v26_paper["mandatory_questions"]["q4"] == "PASS" and pass7_v26_paper["mandatory_questions"]["q8"] == "PASS" and "index-only v1/v7" in pass7_v26_paper["material_defect"] and pass7_v26_paper["candidate_or_packet_clearance"] == "NOT_GRANTED" and "YUI_MZR_CENSUS_WEEKEND_PASS7_V26_EXACT_FAIL" in (HERE / "LANE_RECEIPT.md").read_text(),
        "pass7_local_gate_pass": pass7_local["verdict"] == "PASS" and pass7_local["packet_version"] == "pass7-live-receipt-identity-census-v28" and pass7_local["storyboard_version"] == "pass7-distinct-state-custody-v23" and pass7_local["checks"]["validator"].startswith("PASS") and pass7_local["checks"]["paper_naive_preparer"] == "PASS_NO_WRITE" and pass7_local["checks"]["narration_preparer"] == "PASS_NO_WRITE" and pass7_local["checks"]["deterministic_renderer"].startswith("PASS_NO_WRITE") and pass7_local["checks"]["mutation_suite"].startswith("PASS; 37 cases") and "no index-only or live-only paths" in pass7_local["checks"]["live_receipt_identity_census"] and pass7_local["checks"]["literal_handoff"].startswith("packet v28 named") and pass7_local["candidate_clearance"] == "NOT_GRANTED" and pass7_local["integration_gate"] == "CLOSED" and pass7_local["publication_gate"] == "CLOSED",
        "pass7_v7_custody_inventory_pass": pass7_v7_custody["verdict"] == "PASS" and pass7_v7_custody["external_candidate"]["filesystem_mode"] == "0644" and pass7_v7_custody["external_candidate"]["filesystem_read_only_enforced"] is False and pass7_v7_custody["external_candidate"]["handling_authorization"] == "READ_ONLY_BY_WORKER_POLICY" and pass7_v7_custody["packet_inventory"]["manifest_is_complete_authority"] and pass7_v7_custody["packet_inventory"]["numeric_source_audit_included"] and not pass7_v7_custody["packet_inventory"]["prior_paper_naive_or_adversarial_results_included"],
        "pass7_storyboard_version": storyboard["storyboard_version"] == "pass7-distinct-state-custody-v23",
        "pass7_storyboard_hash_current": sha256(HERE / "STORYBOARD_CANDIDATE.json") == freeze["worker_proposal_current"]["storyboard_sha256"] == narration["source_storyboard_sha256"],
        "pass7_audience_projection_current": proposal["audience_copy_contract"]["projection_sha256"] == freeze["worker_proposal_current"]["audience_copy_projection_sha256"] == pass7_projection["audience_projection_sha256"],
        "pass7_motion_contract_current": proposal["motion_contract"]["verdict"] == "PASS" and sum(len(beat["timed_reveal_states"]) for beat in storyboard["beats"]) == 45 and sum(len(beat["narration_clauses"]) for beat in storyboard["beats"]) == 21 and proposal["motion_contract"]["global_checks"]["maximum_semantic_gap_seconds"] == 3.0,
        "pass7_snapshot_hashes": pass7_snapshot_hashes,
        "pass7_snapshot_stable": len(pass7_snapshot_hashes) == 93 and all(pass7_snapshot_hashes.values()) and not any("PAPER_NAIVE_RESULT" in name or "ADVERSARIAL_RESULT" in name for name in pass7_snapshot_hashes) and sha256(pass7_snapshot_dir / "MANIFEST.json") == "3fd33d66cc93385caddf11cb991e5d60ae5f4a4ba69f97fc8bd3f39c554966bd" and [name for name in pass7_snapshot_hashes if "PASS7_" in name and "_LOCAL_CHECKS.json" in name] == ["qa/PASS7_V28_LOCAL_CHECKS.json"] and "qa/HISTORICAL_LOCAL_RECEIPT_INDEX_V28.json" in pass7_snapshot_hashes,
        "pass7_snapshot_read_only": set(pass7_snapshot_file_modes.values()) == {0o444} and set(pass7_snapshot_dir_modes.values()) == {0o555},
        "pass7_receipt_marker": "YUI_MZR_CENSUS_WEEKEND_PASS7_V28_LOCAL_PENDING_EXACT" in (HERE / "LANE_RECEIPT.md").read_text(),
        "citation_ledger_grounded": all(source["url"] in display_citations and source["title"] in display_citations for source in citation_ledger["sources"]),
        "tts_not_executed": narration["status"] == "PROPOSAL_ONLY_NOT_EXECUTED" and not narration["tts_invoked"] and narration["audio_artifacts"] == [],
        "qualified_reportability": freeze["video_reportable_now"]["decision"] == "YES_WITH_STRICT_SCOPE",
        "publication_gate_closed": narration["publication_gate"] == "CLOSED",
        "frozen_inputs_unchanged": all(frozen_input_hashes.values()),
        "frozen_input_hashes": frozen_input_hashes,
        "lane_receipt_marker": "YUI_MZR_CENSUS_WEEKEND_PASS6" in (HERE / "LANE_RECEIPT.md").read_text(),
    })
    for key in ["proposal_validation_pass", "visual_proposal_pass", "visual_is_v9", "paper_naive_pass", "adversarial_pass", "pass2_encoded_audit_preserved", "pass3_encoded_audit_preserved", "pass3_local_gate_pass", "pass3_frame_custody_stable", "pass3_paper_naive_pass", "pass3_adversarial_pass", "pass3_snapshot_stable", "pass4_encoded_audit_preserved", "pass4_local_gate_pass", "pass4_packet_sync_pass", "pass4_citation_gate_pass", "pass4_validator_custody_pass", "pass4_frame_custody_stable", "pass4_paper_naive_pass", "pass4_adversarial_pass", "pass4_v1_failed_review_preserved", "pass4_snapshot_stable", "pass5_encoded_audit_preserved", "pass5_local_gate_pass", "pass5_packet_sync_pass", "pass5_citation_gate_pass", "pass5_validator_custody_pass", "pass5_frame_custody_stable", "pass5_paper_naive_pass", "pass5_adversarial_pass", "pass5_snapshot_stable", "pass6_encoded_audit_preserved", "pass6_scene_metrics", "pass6_local_gate_pass", "pass6_packet_sync_pass", "pass6_citation_gate_pass", "pass6_validator_custody_pass", "pass6_frame_custody_stable", "pass6_paper_naive_pass", "pass6_exact_failure_preserved", "pass6_snapshot_stable", "pass6_failure_receipt_marker", "pass7_encoded_audit_preserved", "pass7_frame_custody_stable", "pass7_boundary_findings_preserved", "pass7_packet_projection_pass", "pass7_citation_pass", "pass7_continuity_causality_pass", "pass7_validator_pass", "pass7_approved_contract_pass", "pass7_source_freeze_stable", "pass7_v2_false_paths_preserved", "pass7_v1_exact_fail_preserved", "pass7_v2_exact_fail_preserved", "pass7_v3_exact_fail_preserved", "pass7_v4_exact_fail_preserved", "pass7_v5_exact_fail_preserved", "pass7_v6_exact_fail_preserved", "pass7_v7_exact_fail_preserved", "pass7_v8_exact_fail_preserved", "pass7_v11_exact_fail_preserved", "pass7_v12_exact_fail_preserved", "pass7_v13_exact_fail_preserved", "pass7_v14_exact_fail_preserved", "pass7_v15_exact_fail_preserved", "pass7_v16_exact_fail_preserved", "pass7_v17_exact_fail_preserved", "pass7_v18_exact_fail_preserved", "pass7_v19_exact_fail_preserved", "pass7_v20_exact_fail_preserved", "pass7_v22_exact_fail_preserved", "pass7_v26_exact_fail_preserved", "pass7_local_gate_pass", "pass7_v7_custody_inventory_pass", "pass7_storyboard_version", "pass7_storyboard_hash_current", "pass7_audience_projection_current", "pass7_motion_contract_current", "pass7_snapshot_stable", "pass7_snapshot_read_only", "pass7_receipt_marker", "citation_ledger_grounded", "tts_not_executed", "qualified_reportability", "publication_gate_closed", "frozen_inputs_unchanged", "lane_receipt_marker"]:
        if not checks[key]:
            errors.append(f"failed check: {key}")

result = {
    "verdict": "PASS" if not errors else "FAIL",
    "checks": checks,
    "errors": errors,
    "scope": "worker-yui evidence/proposal/QA/request lane only",
}
QA.mkdir(parents=True, exist_ok=True)
(QA / "final_worker_checks.json").write_text(json.dumps(result, indent=2) + "\n")
print(json.dumps(result, indent=2))
raise SystemExit(0 if not errors else 1)
