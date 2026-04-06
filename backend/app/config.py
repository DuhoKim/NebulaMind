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
    OPENCLAW_GATEWAY_URL: str = ""
    OPENCLAW_GATEWAY_TOKEN: str = ""
    DISCORD_WEBHOOK_URL: str = ""

    model_config = {
        "env_prefix": "NM_",
        "env_file": "/Users/duhokim/NebulaMind/NebulaMind/backend/.env",
        "env_file_encoding": "utf-8",
    }


settings = Settings()
