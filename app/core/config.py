from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    GROQ_API_KEY: str
    GROQ_MODEL: str
    EMBEDDING_MODEL: str = "sentence-transformers/all-MiniLM-L6-v2"
    CHROMA_PERSIST_DIRECTORY: str = "./chroma_data"
    PIPER_MODEL_PATH: str = "app/models/piper/en_US-lessac-medium.onnx"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",
    )


settings = Settings()