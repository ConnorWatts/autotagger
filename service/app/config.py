from dataclasses import dataclass
import os

class Config:
    """Base config class."""
    FLASK_APP = os.environ.get('FLASK_APP')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    """Development configurations."""
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

class TestingConfig(Config):
    """Testing configurations."""
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL")

class ProductionConfig(Config):
    """Production configurations."""
    DEBUG = False
    TESTING = False


@dataclass
class LLMConfig:
    """LLM config object."""

    llm_source: str = "openai"

@dataclass
class EmbeddingConfig:
    """Embedding config object."""

    default_source: str = "openai"

@dataclass
class OAIConfig:
    """Open AI config object."""

    api_key: str = os.getenv("OAI_API_KEY")
    model_name: str = "gpt-4"
    embed_model: str = "text-embedding-3-large"
    temperature: float = 0.5
    system_message: str = ... 

