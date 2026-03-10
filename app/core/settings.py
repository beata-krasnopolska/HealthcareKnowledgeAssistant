import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass
class Settings:
    openai_api_key: str
    model_name: str = "gpt-4o-mini"
    embedding_model: str = "text-embedding-3-small"
    vector_store_dir: str = "./data/vector_store"
    log_level: str = "INFO"
    app_name: str = "Healthcare Knowledge Assistant"
    top_k: int = 3


def get_settings() -> Settings:
    return Settings(
        openai_api_key=os.getenv("OPENAI_API_KEY", ""),
        model_name=os.getenv("MODEL_NAME", "gpt-4o-mini"),
        embedding_model=os.getenv("EMBEDDING_MODEL", "text-embedding-3-small"),
        vector_store_dir=os.getenv("VECTOR_STORE_DIR", "./data/vector_store"),
        log_level=os.getenv("LOG_LEVEL", "INFO"),
        app_name=os.getenv("APP_NAME", "Healthcare Knowledge Assistant"),
        top_k=int(os.getenv("TOP_K", "3"))
    )


settings = get_settings()