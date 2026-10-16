from pydantic import SecretStr
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

    anthropic_api_key: SecretStr
    database_url: SecretStr
    redis_url: str
    ollama_base_url: str
    embedding_model: str = "bge-m3"


settings = Settings()
