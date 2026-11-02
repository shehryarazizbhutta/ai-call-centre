import pytest
from pydantic import ValidationError
from app.core.config import Settings


def test_settings_load_required_values():
    settings = Settings(
        GROQ_API_KEY="test-api-key",
        GROQ_MODEL="test-model",
    )

    assert settings.GROQ_API_KEY == "test-api-key"
    assert settings.GROQ_MODEL == "test-model"


def test_settings_require_groq_api_key():
    with pytest.raises(ValidationError):
        Settings(GROQ_MODEL="test-model", _env_file=None)


def test_settings_load_from_env_file():
    settings = Settings()

    assert settings.GROQ_API_KEY
    assert settings.GROQ_MODEL == "openai/gpt-oss-120b"