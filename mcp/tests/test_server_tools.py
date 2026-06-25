import importlib.util
from pathlib import Path
from types import SimpleNamespace
from unittest import TestCase, mock

SERVER_PATH = Path(__file__).resolve().parents[1] / "server.py"
SPEC = importlib.util.spec_from_file_location("nebulamind_mcp_server", SERVER_PATH)
assert SPEC is not None
server = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(server)


class GetClaimEvidenceToolTest(TestCase):
    def test_get_claim_evidence_labels_provisional_status(self):
        response = SimpleNamespace(
            status_code=200,
            json=lambda: {
                "claim_text": "A debated astronomy claim",
                "trust_level": "debated",
                "evidence": [
                    {
                        "title": "Fresh candidate paper",
                        "year": 2026,
                        "arxiv_id": "2601.01234",
                        "stance": "supports",
                        "summary": "Promising, but not reviewer-promoted yet.",
                        "status": "provisional",
                    },
                    {
                        "title": "Reviewed baseline paper",
                        "year": 2024,
                        "stance": "challenges",
                        "status": "active",
                    },
                ],
            },
        )

        with mock.patch.object(server.httpx, "get", return_value=response) as get:
            result = server.get_claim_evidence(claim_id=42)

        get.assert_called_once_with(f"{server.API_BASE}/api/claims/42/evidence", timeout=15)
        self.assertIn("Fresh candidate paper", result)
        self.assertIn("status: provisional", result)
        self.assertIn("not in trust until promoted", result)
        self.assertIn("Reviewed baseline paper", result)
        self.assertIn("status: active", result)


class PromoteEvidenceToolTest(TestCase):
    def test_promote_evidence_posts_authenticated_request_and_formats_result(self):
        response = SimpleNamespace(
            status_code=200,
            json=lambda: {
                "evidence_id": 123,
                "claim_id": 9,
                "promoted": True,
                "old_status": "provisional",
                "status": "active",
                "old_trust_level": "unverified",
                "trust_level": "accepted",
                "trust_score": 0.8123,
            },
        )

        with mock.patch.object(server.httpx, "post", return_value=response) as post:
            result = server.promote_evidence(api_key="test-key", evidence_id=123)

        post.assert_called_once_with(
            f"{server.API_BASE}/api/evidence/123/promote",
            headers={"X-API-Key": "test-key"},
            timeout=15,
        )
        self.assertIn("Evidence #123 promoted", result)
        self.assertIn("claim #9", result)
        self.assertIn("provisional → active", result)
        self.assertIn("unverified → accepted", result)
        self.assertIn("0.812", result)

    def test_promote_evidence_reports_unauthorized_without_leaking_key(self):
        response = SimpleNamespace(status_code=401, text="bad key", json=lambda: {})

        with mock.patch.object(server.httpx, "post", return_value=response):
            result = server.promote_evidence(api_key="secret-test-key", evidence_id=123)

        self.assertEqual(result, "Unauthorized — check your API key.")
        self.assertNotIn("secret-test-key", result)
