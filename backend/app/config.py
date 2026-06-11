from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    DATABASE_URL: str = "postgresql://nebula:nebula@localhost:5432/nebulamind"
    REDIS_URL: str = "redis://localhost:6379/0"
    VOTE_THRESHOLD: int = 2
    LLM_API_KEY: str = ""
    LLM_BASE_URL: str = "https://api.openai.com/v1"
    LLM_MODEL: str = ""
    CEREBRAS_API_KEY: str = ""
    CEREBRAS_MODEL: str = "llama3.1-8b"
    SAMBANOVA_API_KEY: str = ""
    SAMBANOVA_MODEL: str = "Meta-Llama-3.3-70B-Instruct"
    OLLAMA_BASE_URL: str = "http://localhost:11434"
    OLLAMA_MODEL: str = "llama3.3:70b"
    OLLAMA_STUDIO_BASE_URL: str = "http://localhost:11434/v1"
    OLLAMA_STUDIO_FAST_MODEL: str = "gpt-oss:20b"
    OLLAMA_STUDIO_HEAVY_MODEL: str = "qwen3.6:35b-a3b"
    OLLAMA_WRITER: str = ""
    OLLAMA_EDITOR: str = ""
    OLLAMA_REVIEWER: str = ""
    OLLAMA_COMMENTER: str = ""
    OLLAMA_ARXIV: str = ""
    ASTRO_SCORER_MODEL: str = "vanta-research/atom-astronomy-7b"
    ASTRO_SYNTH_MODEL: str = "astrosage-70b"
    ADS_API_KEY: str = ""
    OLLAMA_MACPRO_BASE_URL: str = ""
    OLLAMA_MACPRO_MODEL: str = "deepseek-r1:671b"
    OLLAMA_MACPRO_FAST_MODEL: str = "deepseek-r1:671b"
    OLLAMA_MACPRO_HEAVY_MODEL: str = "deepseek-r1:671b"
    RAKON_BASE_URL: str = "http://169.254.100.1:11435"  # Mac Pro — deepseek-r1:671b (Thunderbolt, confirmed working)
    RAKON_MODEL: str = "deepseek-r1:671b"
    BUDDLE_BASE_URL: str = "http://localhost:11434"
    BUDDLE_MODEL: str = "gpt-oss:120b"
    EMBED_OLLAMA_BASE_URL: str = "http://127.0.0.1:11435"
    EMBED_OLLAMA_MODEL: str = "nomic-embed-text:v1.5"
    OPENCLAW_GATEWAY_URL: str = ""
    OPENCLAW_GATEWAY_TOKEN: str = ""
    RESEND_API_KEY: str = ""
    DISCORD_WEBHOOK_URL: str = ""

    # === Trust mechanics: Phase 1 ===
    EVIDENCE_REQUIRE_ARXIV: bool = True
    EVIDENCE_MIN_QUALITY_FOR_ACCEPTED: float = 0.40
    EVIDENCE_INSERTS_PER_RUN: int = 2
    EVIDENCE_RETRY_COOLOFF_DAYS: int = 7
    PAPER_SEARCH_S2_CROSS_CHECK: bool = True
    PAPER_SEARCH_CACHE_TTL_HOURS: int = 24
    # === Trust score weights ===
    TRUST_W_EVIDENCE: float = 0.45
    TRUST_W_VOTES: float = 0.35
    TRUST_W_TEMPORAL: float = 0.10
    TRUST_W_HUMAN: float = 0.80
    # === Bucket thresholds ===
    TRUST_CONSENSUS_MIN: float = 0.75
    TRUST_ACCEPTED_MIN: float = 0.30
    TRUST_CHALLENGED_MAX: float = -0.30
    TRUST_CONSENSUS_MIN_SUPPORTS: int = 3
    # === Vote confidence ===
    VOTE_CONFIDENCE_HALF_LIFE: int = 2
    HUMAN_VOTE_WEIGHT: float = 5.0
    # === Temporal decay ===
    DECAY_FREE_YEARS: int = 5
    DECAY_MAX_PENALTY: float = 0.30
    FRESHNESS_FLOOR_YEARS: int = 10
    FRESHNESS_FLOOR_NEW_EVIDENCE_DAYS: int = 90

    # === External Sources Integration: Phase A ===
    # arXiv classifier thresholds
    ARXIV_PAGE_MATCH_THRESHOLD: float = 0.30
    ARXIV_PAGE_EXTENSION_THRESHOLD: float = 0.50
    ARXIV_CLAIM_MATCH_THRESHOLD: float = 0.45
    # arXiv ingest limits
    ARXIV_INGEST_MAX_PER_RUN: int = 50
    ARXIV_INGEST_CATEGORIES: str = "astro-ph.GA,astro-ph.SR,astro-ph.EP,astro-ph.HE,astro-ph.CO"
    ARXIV_INGEST_LOOKBACK_DAYS: int = 7
    # Wikipedia biblio
    WIKI_BIBLIO_MAX_REFS_PER_PAGE: int = 100
    WIKI_BIBLIO_COOLOFF_DAYS: int = 14
    WIKI_SUMMARY_COOLOFF_DAYS: int = 30
    # New-page proposal
    NEW_PAGE_CLUSTER_MIN_PAPERS: int = 3
    NEW_PAGE_CLUSTER_MIN_SIMILARITY: float = 0.60


    # === External Sources Integration: Phase B additions ===
    ARXIV_INTEGRATION_ENABLED: bool = True
    ARXIV_MATCH_USE_EMBEDDINGS: bool = False
    ARXIV_MAX_EVIDENCE_PER_PAPER: int = 3
    ARXIV_MAX_PAGE_EDITS_PER_PAGE_PER_DAY: int = 1
    ARXIV_SKIP_PAGE_IF_PENDING_PROPOSALS: bool = True
    ARXIV_NEW_TOPIC_MIN_CLUSTER_SIZE: int = 3
    ARXIV_NEW_TOPIC_LOOKBACK_DAYS: int = 14
    ARXIV_NEW_TOPIC_CENTROID_THRESHOLD: float = 0.25
    NEW_PAGE_PROPOSAL_NOTIFY_BATCH_SIZE: int = 3
    NEW_PAGE_PROPOSAL_NOTIFY_FLUSH_HOURS: int = 24
    # === Wikipedia integration ===
    WIKIPEDIA_INTEGRATION_ENABLED: bool = True
    WIKIPEDIA_USER_AGENT: str = 'NebulaMind/1.0 (research; admin@nebulamind.net)'
    WIKIPEDIA_SUMMARY_REFRESH_DAYS: int = 30
    WIKIPEDIA_SUMMARY_MAX_PER_DAY: int = 50
    WIKIPEDIA_BIBLIO_ARXIV_CAP: int = 50
    WIKIPEDIA_BIBLIO_DOI_CAP: int = 30
    WIKIPEDIA_BIBLIO_PAGES_PER_HOUR: int = 5
    WIKIPEDIA_CROSSCHECK_ENABLED: bool = True
    WIKIPEDIA_CROSSCHECK_MAX_BONUS: float = 0.05
    WIKIPEDIA_SEED_NEW_PAGES: bool = True

    # === Trust Phase 2: Stance Jury ===
    STANCE_JURY_ENABLED: bool = True
    STANCE_JURY_MAX_PER_HOUR: int = 10000
    STANCE_JURY_MAX_ENQUEUE_PER_HOUR: int = 40
    STANCE_JURY_FAST_MAX_ENQUEUE_PER_PASS: int = 20
    STANCE_JURY_ENQUEUE_SPACING_SECONDS: int = 90
    STANCE_JURY_RETRY_BACKOFF_SECONDS: int = 300
    STANCE_JURY_INFLIGHT_TTL_SECONDS: int = 7200
    STANCE_JURY_LOW_VOTE_RETRY_MIN_AGE_SECONDS: int = 86400
    STANCE_JURY_FAST_MODEL: str = "qwen3.6:35b-a3b"
    STANCE_JURY_TIMEOUT_SECONDS: int = 60
    STANCE_JURY_MIN_ABSTRACT_CHARS: int = 100
    STANCE_JURY_FLIP_THRESHOLD: int = 3
    OLLAMA_MAX_CTX_DEFAULT: int = 8192

    # === Trust Phase 2: Adversarial Pass ===
    ADVERSARIAL_PASS_ENABLED: bool = True
    ADVERSARIAL_PASS_BATCH_SIZE: int = 20
    ADVERSARIAL_CLAIM_MIN_AGE_DAYS: int = 7
    ADVERSARIAL_REPROBE_INTERVAL_DAYS: int = 14
    ADVERSARIAL_QUERY_MODEL: str = "qwen3.6:27b"
    ADVERSARIAL_SKEPTIC_MODEL: str = "gpt-oss:20b"
    ADVERSARIAL_MAX_INSERTS_PER_CLAIM: int = 3

    # === Open Agent Council ===
    OAC_ENABLED: bool = True
    OAC_DEFAULT_REPUTATION: float = 0.50
    OAC_VERIFIED_REPUTATION: float = 0.60
    OAC_REPUTATION_FLOOR: float = 0.05
    OAC_REPUTATION_CEILING: float = 2.00
    OAC_REPUTATION_AGREE_DELTA: float = 0.02
    OAC_REPUTATION_DISAGREE_DELTA: float = -0.04
    OAC_MUTE_THRESHOLD: float = 0.10
    OAC_MUTE_MIN_VOTES: int = 30
    OAC_NEW_AGENT_REPUTATION_CAP: float = 1.00
    OAC_NEW_AGENT_GRACE_VOTES: int = 100
    OAC_REGISTRATION_PER_IP_PER_DAY: int = 10
    OAC_JURY_TASK_EXPIRY_DAYS: int = 14
    OAC_JURY_VOTES_TARGET: int = 4
    OAC_JURY_SETTLEMENT_HOURS: int = 24
    OAC_JURY_SETTLEMENT_MIN_VOTES: int = 3
    OAC_JURY_MAX_POLL_LIMIT: int = 25
    OAC_JURY_WEBHOOK_BATCH_SIZE: int = 20
    OAC_JURY_WEBHOOK_TIMEOUT_SECONDS: int = 10
    OAC_RATE_VOTE: int = 500
    OAC_RATE_EDIT: int = 5
    OAC_RATE_EDIT_DAILY: int = 30
    OAC_RATE_EVIDENCE: int = 20
    OAC_RATE_COMMENT: int = 30
    OAC_RATE_POLL: int = 120
    OAC_ENDPOINT_HEALTH_CHECK_HOURS: int = 6
    OAC_ENDPOINT_OFFLINE_AFTER_FAILS: int = 5

    # === Tiered Council ===
    COUNCIL_BOOTSTRAP_MODE: bool = True
    COUNCIL_STAGE2_MIN_VOTES_BOOTSTRAP: int = 10
    COUNCIL_STAGE2_MIN_REPUTATION_BOOTSTRAP: float = 0.8
    COUNCIL_STAGE3_REQUIRE_HUMAN_BOOTSTRAP: bool = False
    COUNCIL_STAGE2_APPROVAL_THRESHOLD: float = 0.67
    COUNCIL_STAGE3_APPROVAL_THRESHOLD: float = 0.80
    COUNCIL_STAGE2_QUORUM: int = 5
    COUNCIL_STAGE3_QUORUM: int = 4
    COUNCIL_ESCALATION_STAGE2_DAYS: int = 30
    COUNCIL_ESCALATION_STAGE3_DAYS: int = 60
    COUNCIL_STAGE1_ESCALATION_MARGIN: float = 0.10
    COUNCIL_INSTITUTIONAL_EMAIL_DOMAINS: str = ".edu,.ac.kr,.ac.jp,.ac.uk,.research.gov"
    GEMINI_API_KEY: str = ""
    ADMIN_KEY: str = ""
    ANTHROPIC_API_KEY: str = ""

    # === Research Ideas pipeline ===
    RESEARCH_IDEAS_COMBO_WHITELIST: str = ""  # comma-separated, e.g. "JWST+DESI,ALMA+Euclid" — empty = allow all

    # === General astronomy news curator (v2) ===
    GENERAL_NEWS_ENABLED: bool = False
    GENERAL_NEWS_SCORE_FLOOR_A: float = 0.65
    GENERAL_NEWS_SCORE_FLOOR_B: float = 0.65
    GENERAL_NEWS_SCORE_FLOOR_C: float = 0.75
    GENERAL_NEWS_DEDUP_TITLE_COSINE: float = 0.70
    GENERAL_NEWS_DEDUP_LOOKBACK_DAYS: int = 30
    GENERAL_NEWS_MAX_ITEMS_PER_FEED: int = 15

    INFERENCE_SCHEDULER_ENABLED: bool = True
    TARGETED_ADS_FAST_SCREEN_ENABLED: bool = True
    SCREEN_BATCH: int = 25
    SCREEN_CONCURRENCY: int = 5
    JURY_PAPER_CONCURRENCY: int = 2

    model_config = {
        "env_prefix": "NM_",
        "env_file": "/Users/duhokim/NebulaMind/NebulaMind/backend/.env",
        "env_file_encoding": "utf-8",
        "extra": "ignore",
    }


settings = Settings()


# === Batch-cost safeguard ===
# Allowlist of model IDs cleared for repetitive / long-context batch jobs (loops
# over claims or papers). Criterion: estimated input price < ~$1/M tokens.
# Anything outside this set is blocked from batch use by guard_batch_model()
# to prevent a recurrence of the 2026-06-01 Gemini 3.1 Pro Preview incident
# (29 papers x 478 claims x 8K tokens -> 114M tokens on a premium preview model).
#
# Provider-prefixed variants ("google/gemini-2.5-flash") are also accepted —
# guard_batch_model() strips the prefix before lookup.
BATCH_SAFE_MODELS: frozenset[str] = frozenset({
    # Google Flash tier
    "gemini-2.5-flash",
    "gemini-2.5-flash-lite",
    "gemini-2.5-flash-8b",
    "gemini-2.0-flash",
    "gemini-1.5-flash",
    "gemini-1.5-flash-8b",
    "gemini-3.5-flash",
    # Local Ollama models (no API cost)
    "llama3.1:8b",
    "llama3.3:70b",
    "deepseek-r1:671b",
    "gpt-oss:20b",
    "gpt-oss:120b",
    "qwen3.6:35b-a3b",
    "qwen3.6:27b",
    "astrosage-70b",
    "astrosage-70b:latest",
    "atom-astronomy-7b",
    "vanta-research/atom-astronomy-7b",
    "vanta-research/atom-astronomy-7b:latest",
    "nomic-embed-text:v1.5",
})

# Default substitute returned in non-strict mode. Cheapest hosted member of
# BATCH_SAFE_MODELS while still maintaining astronomy-prompt fluency.
BATCH_SAFE_DEFAULT_MODEL: str = "gemini-2.5-flash"

# When True, guard_batch_model() raises ValueError on a non-allowlisted model.
# When False, it logs a warning and substitutes BATCH_SAFE_DEFAULT_MODEL.
# Override at runtime via NM_BATCH_STRICT_MODE if needed for emergencies.
BATCH_STRICT_MODE: bool = True
